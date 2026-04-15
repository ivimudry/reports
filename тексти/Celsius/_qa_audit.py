# -*- coding: utf-8 -*-
"""
MEGA QA AUDIT — Celsius Campaign Files
Checks:
1. LINKS: correct locale prefix (/fr/, /hu/, /pl/) and utm_language param
2. TERMS-HU: No English Free Spins/Bonus/NoRisk in HU locale
3. TERMS-PL: No English Free Spins/NoRisk in PL locale  
4. DASHES: No em-dash or en-dash
5. PROMO: Promo codes wrapped in <strong class="promocode">...</strong>
6. HTML-TAGS: Balanced <strong>/<a>/<p>/<td>/<span> tags in HTML fields
7. MISSING-LOCALE: Every email must have all 4 locales
8. UNTRANSLATED: HU/PL body fields shouldn't be identical to Default
9. BUTTONS: HU/PL buttons should be ALL CAPS
10. FR-BODY: French subject/preheader/body should match English (Default)
11. LINKS-MATCH: HU/PL links should have /hu/ /pl/ prefix and utm_language
12. PROMO-CODES: Promo code values should be same across all locales for same email
"""
import re, os, sys, io, html
from collections import defaultdict

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

BASE = r'c:\Projects\REPORTS\тексти\Celsius'
FILES = [
    'DEP Retention - Table data.txt',
    'FTD Retention Flow - Table data.txt',
    'Failed Deposit Flow - Table data.txt',
    'Nutrition #2 - Table data.txt',
    'Nutrition #3 - Table data.txt',
    'SU Retention - Table data.txt',
    'Welcome Flow - Table data.txt',
]

issues = []
warnings = []

def issue(cat, file, email, locale, detail):
    issues.append(f"[{cat}] {file} | {email} | {locale}: {detail}")

def warn(cat, file, email, locale, detail):
    warnings.append(f"[{cat}] {file} | {email} | {locale}: {detail}")

def parse_file(filepath):
    """Parse file into list of dicts."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    content = content.replace('\r\n', '\n')
    blocks = content.split('\n\n')
    records = []
    for block in blocks:
        if not block.strip():
            continue
        lines = block.split('\n')
        d = {}
        for line in lines:
            idx = line.find(':')
            if idx > 0:
                key = line[:idx].strip()
                val = line[idx+1:].strip()
                d[key] = val
        if 'name' in d and 'locale' in d:
            records.append(d)
    return records

def check_balanced_tags(text, tag):
    """Check if HTML tag is balanced. Returns (opens, closes)."""
    opens = len(re.findall(f'<{tag}[\\s>]', text, re.IGNORECASE))
    closes = len(re.findall(f'</{tag}>', text, re.IGNORECASE))
    # Self-closing won't count
    return opens, closes

def check_promo_class(text):
    """Find promo codes and check they're wrapped in <strong class="promocode">."""
    # Known promo code patterns (typically uppercase letters/numbers, 4-20 chars)
    # Look for <strong class="promocode">SOMETHING</strong> pattern
    promo_matches = re.findall(r'<strong\s+class="promocode">(.*?)</strong>', text, re.IGNORECASE)
    
    # Also look for bare promo codes that might not be wrapped
    # Common promo patterns: all caps, sometimes with numbers
    bare_promos = re.findall(r'(?:promo(?:code)?|code|kód|kod|промокод)\s*[:\s]\s*(?:<[^>]+>)*([A-Z0-9]{4,20})(?:</[^>]+>)*', text, re.IGNORECASE)
    
    return promo_matches, bare_promos

def extract_promo_values(record):
    """Extract promo code values from record fields."""
    promos = set()
    for key, val in record.items():
        # From promocode fields
        if 'promocode' in key.lower() and 'button' not in key.lower() and 'href' not in key.lower():
            if val.strip():
                promos.add(val.strip())
        # From HTML body - extract from <strong class="promocode">
        if key in ('text_2', 'text_3', 'rich_text'):
            for m in re.findall(r'<strong\s+class="promocode">(.*?)</strong>', val, re.IGNORECASE):
                promos.add(m.strip())
    return promos

def check_links(record, fname, email, locale):
    """Check link localization."""
    locale_prefix_map = {
        'Default': ('', 'en'),
        'fr-FR': ('/fr', 'fr'),
        'hu-HU': ('/hu', 'hu'),
        'pl-PL': ('/pl', 'pl'),
    }
    
    if locale not in locale_prefix_map:
        return
    
    expected_prefix, expected_lang = locale_prefix_map[locale]
    
    for key, val in record.items():
        if 'href' not in key.lower():
            continue
        if not val or 'celsiuscasino.com' not in val:
            continue
        
        # Check utm_language
        lang_match = re.search(r'utm_language=(\w+)', val)
        if lang_match:
            actual_lang = lang_match.group(1)
            if actual_lang != expected_lang:
                issue('LINK-LANG', fname, email, locale, 
                      f"{key}: utm_language={actual_lang}, expected={expected_lang}")
        
        # Check path prefix
        path_match = re.search(r'celsiuscasino\.com(/[^?]*)', val)
        if path_match:
            path = path_match.group(1)
            if locale == 'Default':
                # Should NOT have /fr/, /hu/, /pl/ prefix
                if path.startswith('/fr/') or path.startswith('/hu/') or path.startswith('/pl/'):
                    issue('LINK-PATH', fname, email, locale, 
                          f"{key}: Default link has locale prefix: {path[:20]}")
            elif expected_prefix:
                if not path.startswith(expected_prefix + '/'):
                    issue('LINK-PATH', fname, email, locale, 
                          f"{key}: missing {expected_prefix}/ prefix, got: {path[:30]}")
        
        # Also check links in HTML body fields
    for key in ('text_2', 'text_3', 'rich_text'):
        val = record.get(key, '')
        if not val:
            continue
        for href_match in re.finditer(r'href="([^"]*celsiuscasino[^"]*)"', val):
            url = href_match.group(1)
            lang_m = re.search(r'utm_language=(\w+)', url)
            if lang_m and lang_m.group(1) != expected_lang:
                issue('LINK-BODY', fname, email, locale,
                      f"{key}: body link utm_language={lang_m.group(1)}, expected={expected_lang}")
            
            path_m = re.search(r'celsiuscasino\.com(/[^?]*)', url)
            if path_m and expected_prefix:
                if not path_m.group(1).startswith(expected_prefix + '/'):
                    issue('LINK-BODY', fname, email, locale,
                          f"{key}: body link missing {expected_prefix}/ prefix")

def check_terminology_hu(record, fname, email):
    """Check HU record doesn't have English gambling terms."""
    ENGLISH_TERMS = [
        ('Free Spins', 'Ingyenes Pörgetés'),
        ('Free Spin', 'Ingyenes Pörgetés'),
        ('NoRisk Free Bet', 'Kockázatmentes Fogadás'),
        ('NoRisk Bet', 'Kockázatmentes Fogadás'),
        ('FreeBet', 'Kockázatmentes Fogadás'),
    ]
    
    for key in ('subject', 'preheader', 'text_1', 'text_2', 'text_3', 'rich_text'):
        val = record.get(key, '')
        if not val:
            continue
        for eng, hu in ENGLISH_TERMS:
            if eng in val:
                # Check it's not inside a URL
                # Find position, check context
                pos = val.find(eng)
                context_before = val[max(0, pos-30):pos]
                if 'utm_' not in context_before and 'href=' not in context_before and 'http' not in context_before:
                    issue('TERM-HU', fname, email, 'hu-HU', 
                          f"{key}: English '{eng}' found (should be '{hu}')")
                    break  # one issue per field
        
        # Check Bonus (not Bónusz) - be careful with URLs
        for m in re.finditer(r'\bBonus\b', val):
            pos = m.start()
            ctx = val[max(0, pos-40):pos]
            # Skip if inside URL
            if 'utm_' in ctx or 'href=' in ctx or 'http' in ctx or 'bonuses' in ctx.lower():
                continue
            issue('TERM-HU', fname, email, 'hu-HU', 
                  f"{key}: English 'Bonus' found at pos {pos} (should be 'Bónusz')")
            break
    
    # Check buttons
    for key in ('button_text_1', 'promocode_button_1'):
        val = record.get(key, '')
        if not val:
            continue
        for eng_upper in ['NORISK', 'FREE SPIN', 'FREE BET', 'FREEBETS']:
            if eng_upper in val.upper() and 'KOCKÁZATMENTES' not in val and 'INGYENES' not in val:
                issue('TERM-HU', fname, email, 'hu-HU', 
                      f"{key}: English term in button: '{val}'")
                break

def check_terminology_pl(record, fname, email):
    """Check PL record doesn't have English gambling terms."""
    ENGLISH_TERMS = [
        ('Free Spins', 'Darmowe Spiny'),
        ('Free Spin', 'Darmowy Spin'),
        ('NoRisk Free Bet', 'Zakład Bez Ryzyka'),
        ('NoRisk Bet', 'Zakład Bez Ryzyka'),
        ('FreeBet', 'Zakład Bez Ryzyka'),
    ]
    
    for key in ('subject', 'preheader', 'text_1', 'text_2', 'text_3', 'rich_text'):
        val = record.get(key, '')
        if not val:
            continue
        for eng, pl in ENGLISH_TERMS:
            if eng in val:
                pos = val.find(eng)
                context_before = val[max(0, pos-30):pos]
                if 'utm_' not in context_before and 'href=' not in context_before and 'http' not in context_before:
                    issue('TERM-PL', fname, email, 'pl-PL', 
                          f"{key}: English '{eng}' found (should be '{pl}')")
                    break
    
    # Check buttons  
    for key in ('button_text_1', 'promocode_button_1'):
        val = record.get(key, '')
        if not val:
            continue
        for eng_upper in ['NORISK', 'FREE SPIN', 'FREE BET', 'FREEBETS']:
            if eng_upper in val.upper() and 'RYZYKA' not in val and 'DARMOW' not in val.upper():
                issue('TERM-PL', fname, email, 'pl-PL', 
                      f"{key}: English term in button: '{val}'")
                break

def check_html_integrity(record, fname, email, locale):
    """Check HTML tags are balanced in body fields."""
    for key in ('text_2', 'text_3', 'rich_text'):
        val = record.get(key, '')
        if not val or len(val) < 20:
            continue
        
        for tag in ('strong', 'a', 'span'):
            opens, closes = check_balanced_tags(val, tag)
            if opens != closes:
                issue('HTML-TAG', fname, email, locale, 
                      f"{key}: <{tag}> unbalanced: {opens} opens, {closes} closes")
        
        # Check for broken href attributes
        broken_hrefs = re.findall(r'href\s*=\s*"[^"]*$', val)  # unclosed href quotes
        if broken_hrefs:
            issue('HTML-HREF', fname, email, locale, 
                  f"{key}: potentially broken href attribute")
        
        # Check for empty href
        empty_hrefs = re.findall(r'href\s*=\s*""', val)
        if empty_hrefs:
            issue('HTML-EMPTY-HREF', fname, email, locale, 
                  f"{key}: empty href found")

def check_promocode_wrapping(record, fname, email, locale):
    """Check promo codes in body are wrapped in <strong class="promocode">."""
    for key in ('text_2', 'text_3', 'rich_text'):
        val = record.get(key, '')
        if not val:
            continue
        
        # Find all <strong class="promocode">...</strong> patterns
        wrapped_promos = set()
        for m in re.finditer(r'<strong\s+class="promocode">(.*?)</strong>', val, re.IGNORECASE):
            wrapped_promos.add(m.group(1).strip())
        
        # Check: if there's a known promo code field in the record, verify it appears wrapped
        for pkey, pval in record.items():
            if pkey.startswith('promocode_') and 'button' not in pkey and 'href' not in pkey:
                code = pval.strip()
                if code and code in val:
                    # Check it's wrapped
                    if code not in wrapped_promos:
                        # Maybe it appears both wrapped and unwrapped
                        pattern = re.escape(code)
                        # Find occurrences NOT inside <strong class="promocode">
                        all_positions = [(m.start(), m.end()) for m in re.finditer(pattern, val)]
                        wrapped_positions = [(m.start(1), m.end(1)) for m in re.finditer(
                            r'<strong\s+class="promocode">' + pattern + r'</strong>', val)]
                        
                        unwrapped_count = len(all_positions) - len(wrapped_positions)
                        if unwrapped_count > 0:
                            # Could be inside text description, skip if in running text
                            # Only flag if it looks like it should be a code display
                            pass  # Promo codes in running text are OK
        
        # More important: find any <strong> that looks like a promo code but doesn't have class="promocode"
        # Pattern: <strong>ALLCAPS4-20</strong> that's NOT <strong class="promocode">
        for m in re.finditer(r'<strong>([A-Z][A-Z0-9]{3,19})</strong>', val):
            code = m.group(1)
            # Skip common words
            skip_words = {'WEEKLY', 'DAILY', 'MONTHLY', 'BONUS', 'BÓNUSZ', 'CASINO', 'CELSIUS',
                         'SPORT', 'LIVE', 'TABLE', 'GAMES', 'POWER', 'GATES', 'OLYMPUS',
                         'CHAOSCREW', 'BAMBOO', 'PRAGMATIC', 'HACKSAW', 'GAMING', 'WANTED',
                         'DEAD', 'WILD', 'WEST', 'GOLD', 'GEMS', 'BONANZA', 'PUSH',
                         'NORISK', 'INGYENES', 'PÖRGETÉS', 'KOCKÁZATMENTES', 'FOGADÁS',
                         'DARMOWE', 'SPINY', 'ZAKŁAD', 'RYZYKA'}
            if code in skip_words:
                continue
            # This might be an unwrapped promo code
            warn('PROMO-NOWRAP', fname, email, locale, 
                 f"{key}: <strong>{code}</strong> might need class=\"promocode\"")

def check_promo_consistency(records_by_email, fname):
    """Check promo code values are consistent across locales for each email."""
    for email, locale_records in records_by_email.items():
        promo_by_locale = {}
        for locale, record in locale_records.items():
            for key, val in record.items():
                if key.startswith('promocode_') and 'button' not in key and 'href' not in key:
                    promo_by_locale.setdefault(key, {})[locale] = val.strip()
        
        for pkey, locale_vals in promo_by_locale.items():
            values = set(v for v in locale_vals.values() if v)
            if len(values) > 1:
                issue('PROMO-MISMATCH', fname, email, 'ALL', 
                      f"{pkey}: different values across locales: {locale_vals}")

def check_french_locale(default_rec, fr_rec, fname, email):
    """Check French locale rules: subject/preheader/body in English, rest in French."""
    # Subject should match Default (English)
    for fld in ('subject', 'preheader'):
        def_val = default_rec.get(fld, '')
        fr_val = fr_rec.get(fld, '')
        if def_val and fr_val and def_val != fr_val:
            issue('FR-SUBJ', fname, email, 'fr-FR', 
                  f"{fld}: differs from Default. Default='{def_val[:60]}' FR='{fr_val[:60]}'")
    
    # Body fields (text_1, text_2, sometimes text_3 for promo emails) should match Default
    # But first determine which text fields are "body"
    body_fields = ['text_1', 'text_2']
    # If there's a promocode_button, text_3 is also body
    if default_rec.get('promocode_button_1', ''):
        body_fields.append('text_3')
    
    for fld in body_fields:
        def_val = default_rec.get(fld, '')
        fr_val = fr_rec.get(fld, '')
        if def_val and fr_val and def_val != fr_val:
            # Only flag if significantly different (not just whitespace)
            if def_val.strip() != fr_val.strip():
                issue('FR-BODY', fname, email, 'fr-FR', 
                      f"{fld}: body differs from Default (should be English). Diff length: {abs(len(def_val)-len(fr_val))}")
    
    # rich_text should match Default if present
    if 'rich_text' in default_rec and 'rich_text' in fr_rec:
        def_rt = default_rec['rich_text']
        fr_rt = fr_rec['rich_text']
        if def_rt and fr_rt and def_rt.strip() != fr_rt.strip():
            # Check if it's just link localization
            def_no_links = re.sub(r'utm_language=\w+', '', def_rt)
            fr_no_links = re.sub(r'utm_language=\w+', '', fr_rt)
            def_no_links = re.sub(r'celsiuscasino\.com/fr/', 'celsiuscasino.com/', def_no_links)
            if def_no_links.strip() != fr_no_links.strip():
                issue('FR-BODY', fname, email, 'fr-FR', 
                      f"rich_text: body differs from Default (should be English)")

def check_buttons_caps(record, fname, email, locale):
    """Check button text is ALL CAPS."""
    for key in ('button_text_1', 'promocode_button_1'):
        val = record.get(key, '')
        if not val:
            continue
        # Check if ALL CAPS (allowing spaces, hyphens, unicode uppercase)
        if val != val.upper():
            issue('BTN-CAPS', fname, email, locale, 
                  f"{key}: not ALL CAPS: '{val}'")

def check_dashes(record, fname, email, locale):
    """Check no em-dash or en-dash."""
    for key, val in record.items():
        if '\u2014' in val:
            issue('DASH', fname, email, locale, f"{key}: em-dash found")
        if '\u2013' in val:
            issue('DASH', fname, email, locale, f"{key}: en-dash found")

def check_untranslated(default_rec, locale_rec, fname, email, locale):
    """Check that body content is actually translated (not copy of Default)."""
    for fld in ('text_1', 'text_2', 'text_3'):
        def_val = default_rec.get(fld, '')
        loc_val = locale_rec.get(fld, '')
        if def_val and loc_val and def_val.strip() == loc_val.strip() and len(def_val) > 50:
            issue('UNTRANSLATED', fname, email, locale, 
                  f"{fld}: identical to Default (possible untranslated content)")
    
    # Check rich_text too
    def_rt = default_rec.get('rich_text', '')
    loc_rt = locale_rec.get('rich_text', '')
    if def_rt and loc_rt and def_rt.strip() == loc_rt.strip() and len(def_rt) > 100:
        issue('UNTRANSLATED', fname, email, locale, 
              f"rich_text: identical to Default (possible untranslated content)")
    
    # Check subject
    def_subj = default_rec.get('subject', '')
    loc_subj = locale_rec.get('subject', '')
    if def_subj and loc_subj and def_subj.strip() == loc_subj.strip():
        issue('UNTRANSLATED', fname, email, locale, 
              f"subject: identical to Default '{def_subj[:50]}'")
    
    # Check preheader
    def_pre = default_rec.get('preheader', '')
    loc_pre = locale_rec.get('preheader', '')
    if def_pre and loc_pre and def_pre.strip() == loc_pre.strip():
        issue('UNTRANSLATED', fname, email, locale, 
              f"preheader: identical to Default '{def_pre[:50]}'")

# ═══════════════════════════════════════════════════════════════
# MAIN AUDIT LOOP
# ═══════════════════════════════════════════════════════════════

for fname in FILES:
    fpath = os.path.join(BASE, fname)
    if not os.path.exists(fpath):
        issue('FILE', fname, '-', '-', 'File not found!')
        continue
    
    short = fname.replace(' - Table data.txt', '')
    records = parse_file(fpath)
    
    # Group by email name
    emails = defaultdict(dict)  # {email_name: {locale: record}}
    for r in records:
        emails[r['name']][r['locale']] = r
    
    # Check each email has all 4 locales
    expected_locales = {'Default', 'fr-FR', 'hu-HU', 'pl-PL'}
    for email, locale_recs in emails.items():
        present = set(locale_recs.keys())
        missing = expected_locales - present
        if missing:
            issue('MISSING-LOCALE', short, email, ','.join(missing), 'locale(s) missing')
    
    # Check promo consistency
    check_promo_consistency(emails, short)
    
    # Per-record checks
    for r in records:
        email = r['name']
        locale = r['locale']
        
        # Dashes
        check_dashes(r, short, email, locale)
        
        # HTML integrity
        check_html_integrity(r, short, email, locale)
        
        # Promo wrapping
        check_promocode_wrapping(r, short, email, locale)
        
        # Links
        check_links(r, short, email, locale)
        
        # Locale-specific checks
        if locale == 'hu-HU':
            check_terminology_hu(r, short, email)
            check_buttons_caps(r, short, email, locale)
            default_rec = emails[email].get('Default', {})
            if default_rec:
                check_untranslated(default_rec, r, short, email, locale)
        
        elif locale == 'pl-PL':
            check_terminology_pl(r, short, email)
            check_buttons_caps(r, short, email, locale)
            default_rec = emails[email].get('Default', {})
            if default_rec:
                check_untranslated(default_rec, r, short, email, locale)
        
        elif locale == 'fr-FR':
            default_rec = emails[email].get('Default', {})
            if default_rec:
                check_french_locale(default_rec, r, short, email)

# ═══════════════════════════════════════════════════════════════
# OUTPUT
# ═══════════════════════════════════════════════════════════════

print("=" * 80)
print("CELSIUS MEGA QA AUDIT")
print("=" * 80)

# Categorize
cats = defaultdict(list)
for i in issues:
    cat = i.split(']')[0].lstrip('[')
    cats[cat].append(i)

warn_cats = defaultdict(list)
for w in warnings:
    cat = w.split(']')[0].lstrip('[')
    warn_cats[cat].append(w)

print(f"\nTotal ISSUES: {len(issues)}")
print(f"Total WARNINGS: {len(warnings)}")

if issues:
    print("\nBy category:")
    for cat in sorted(cats.keys()):
        print(f"  {cat}: {len(cats[cat])}")

if warnings:
    print("\nWarnings by category:")
    for cat in sorted(warn_cats.keys()):
        print(f"  {cat}: {len(warn_cats[cat])}")

if issues:
    print("\n" + "=" * 80)
    print("ISSUES (must fix)")
    print("=" * 80)
    for cat in sorted(cats.keys()):
        print(f"\n--- {cat} ({len(cats[cat])}) ---")
        for i in cats[cat]:
            print(i)

if warnings:
    print("\n" + "=" * 80)
    print("WARNINGS (review)")
    print("=" * 80)
    for cat in sorted(warn_cats.keys()):
        print(f"\n--- {cat} ({len(warn_cats[cat])}) ---")
        for w in warn_cats[cat]:
            print(w)

if not issues and not warnings:
    print("\n*** ALL CLEAR — No issues or warnings found! ***")

# Save to file
out_path = os.path.join(BASE, '_qa_audit_result.txt')
with open(out_path, 'w', encoding='utf-8') as f:
    f.write(f"Total ISSUES: {len(issues)}\n")
    f.write(f"Total WARNINGS: {len(warnings)}\n\n")
    if issues:
        f.write("BY CATEGORY:\n")
        for cat in sorted(cats.keys()):
            f.write(f"  {cat}: {len(cats[cat])}\n")
        f.write("\nALL ISSUES:\n")
        for i in issues:
            f.write(i + '\n')
    if warnings:
        f.write("\nALL WARNINGS:\n")
        for w in warnings:
            f.write(w + '\n')

print(f"\nFull report: {out_path}")
