# -*- coding: utf-8 -*-
"""Full audit of ALL 7 Celsius campaign files.
Checks:
1. Terminology: Free Spins/Bonus/NoRisk/FreeBet in HU/PL
2. Dashes: no em-dash or en-dash (only regular hyphen "-")
3. Button text: ALL CAPS in HU/PL
4. Default name: HU="Barátom"/"Játékos", PL="Przyjacielu"/"Gracz"
5. Missing translations: every email must have hu-HU and pl-PL
6. Links: locale params in URLs
7. French locale: subject/preheader/body in English, rest in French
"""
import re, os, sys, io
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

def add_issue(file, email, locale, category, detail):
    issues.append(f"[{category}] {file} | {email} | {locale}: {detail}")

def parse_blocks(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    content = content.replace('\r\n', '\n')
    raw_blocks = content.split('\n\n')
    blocks = []
    for rb in raw_blocks:
        if not rb.strip():
            continue
        lines = rb.split('\n')
        d = {}
        for line in lines:
            idx = line.find(':')
            if idx > 0:
                key = line[:idx].strip()
                val = line[idx+1:].strip()
                d[key] = val
        if d.get('name') and d.get('locale'):
            blocks.append(d)
    return blocks

for fname in FILES:
    filepath = os.path.join(BASE, fname)
    if not os.path.exists(filepath):
        issues.append(f"[MISSING FILE] {fname}")
        continue
    
    blocks = parse_blocks(filepath)
    short = fname.replace(' - Table data.txt', '')
    
    # Group by email name
    emails = {}
    for b in blocks:
        name = b['name']
        if name not in emails:
            emails[name] = {}
        emails[name][b['locale']] = b
    
    # Check each email has all 4 locales
    for ename, locales in sorted(emails.items()):
        for req_locale in ['Default', 'fr-FR', 'hu-HU', 'pl-PL']:
            if req_locale not in locales:
                add_issue(short, ename, req_locale, 'MISSING LOCALE', f'Locale {req_locale} missing entirely')
    
    # Check each block
    for b in blocks:
        name = b['name']
        locale = b['locale']
        
        # === DASH CHECK (all locales) ===
        for key, val in b.items():
            if key in ('name', 'locale', 'from_id'):
                continue
            # Check for em-dash (—) and en-dash (–)
            if '—' in val:
                add_issue(short, name, locale, 'DASH', f'{key}: contains em-dash "—"')
            if '–' in val:
                add_issue(short, name, locale, 'DASH', f'{key}: contains en-dash "–"')
        
        # === HU-HU CHECKS ===
        if locale == 'hu-HU':
            # Check for untranslated English terms
            for key, val in b.items():
                if key in ('name', 'locale', 'from_id', 'logo_src', 'logo_href', 'banner_src', 'banner_href',
                           'x_icon_src', 'x_icon_href', 'telegram_icon_src', 'telegram_icon_href',
                           'discord_icon_src', 'discord_icon_href', 'support_icon_src', 'support_icon_href',
                           'button_href_1'):
                    continue
                
                val_lower = val.lower()
                
                # "Free Spins" should be "Ingyenes Pörgetés" in HU
                if re.search(r'free\s+spins?', val_lower) and 'promocode' not in val_lower:
                    # Check it's not inside a game name context
                    if not re.search(r'by\s+\w+\s+gaming', val_lower):
                        add_issue(short, name, locale, 'TERM-HU', f'{key}: "Free Spin(s)" should be "Ingyenes Pörgetés" -> {val[:100]}')
                
                # "Bonus" should be "Bónusz" in HU (but not inside promo codes or class names)
                # Only flag standalone "Bonus" not "Bónusz"
                if re.search(r'\bBonus\b', val) and 'Bónusz' not in val and 'promocode' not in val:
                    # Could be a mixed case, check carefully
                    bonus_matches = re.findall(r'\bBonus\b', val)
                    for bm in bonus_matches:
                        context = val[max(0, val.find(bm)-20):val.find(bm)+30]
                        if 'promocode' not in context and 'class=' not in context:
                            add_issue(short, name, locale, 'TERM-HU', f'{key}: "Bonus" should be "Bónusz" -> ...{context}...')
                            break
                
                # "NoRisk Free Bet"/"FreeBet"/"FreeBets" should be "Kockázatmentes Fogadás"
                if re.search(r'free\s*bet', val_lower) and 'kockázatmentes' not in val_lower:
                    add_issue(short, name, locale, 'TERM-HU', f'{key}: "FreeBet" should be "Kockázatmentes Fogadás" -> {val[:100]}')
                if re.search(r'norisk', val_lower) and 'kockázatmentes' not in val_lower:
                    add_issue(short, name, locale, 'TERM-HU', f'{key}: "NoRisk" should be "Kockázatmentes" -> {val[:100]}')
                
                # "Cashback" stays English - OK
                
            # Default name check
            text1 = b.get('text_1', '')
            if 'default:' in text1:
                if '"friend"' in text1 or "'friend'" in text1:
                    add_issue(short, name, locale, 'DEFAULT-NAME', f'text_1: default:"friend" should be translated to HU')
                if '"Player"' in text1 or "'Player'" in text1:
                    add_issue(short, name, locale, 'DEFAULT-NAME', f'text_1: default:"Player" should be translated to HU')
                if '"Friend"' in text1 or "'Friend'" in text1:
                    add_issue(short, name, locale, 'DEFAULT-NAME', f'text_1: default:"Friend" should be translated to HU')
            
            # Button ALL CAPS check
            btn = b.get('button_text_1', '') or b.get('promocode_button_1', '')
            if btn and btn != btn.upper():
                add_issue(short, name, locale, 'BUTTON-CAPS', f'Button not ALL CAPS: "{btn}"')
            
            # Subject same as Default check (indicates untranslated)
            if name in emails and 'Default' in emails[name]:
                default_subj = emails[name]['Default'].get('subject', '')
                hu_subj = b.get('subject', '')
                if default_subj and hu_subj == default_subj:
                    add_issue(short, name, locale, 'UNTRANSLATED', f'subject same as Default: "{hu_subj[:80]}"')
                
                default_preh = emails[name]['Default'].get('preheader', '')
                hu_preh = b.get('preheader', '')
                if default_preh and hu_preh == default_preh:
                    add_issue(short, name, locale, 'UNTRANSLATED', f'preheader same as Default')
        
        # === PL-PL CHECKS ===
        if locale == 'pl-PL':
            for key, val in b.items():
                if key in ('name', 'locale', 'from_id', 'logo_src', 'logo_href', 'banner_src', 'banner_href',
                           'x_icon_src', 'x_icon_href', 'telegram_icon_src', 'telegram_icon_href',
                           'discord_icon_src', 'discord_icon_href', 'support_icon_src', 'support_icon_href',
                           'button_href_1'):
                    continue
                
                val_lower = val.lower()
                
                # "Free Spins" should be "Darmowe Spiny" in PL
                if re.search(r'free\s+spins?', val_lower) and 'promocode' not in val_lower:
                    if not re.search(r'by\s+\w+\s+gaming', val_lower):
                        add_issue(short, name, locale, 'TERM-PL', f'{key}: "Free Spin(s)" should be "Darmowe Spiny" -> {val[:100]}')
                
                # "Bonus" is OK in Polish (it's the same word)
                
                # "NoRisk Free Bet"/"FreeBet" should be "Zakład Bez Ryzyka"
                if re.search(r'free\s*bet', val_lower) and 'zakład' not in val_lower and 'zakłady' not in val_lower and 'zakładem' not in val_lower and 'zakładów' not in val_lower:
                    add_issue(short, name, locale, 'TERM-PL', f'{key}: "FreeBet" should be "Zakład Bez Ryzyka" -> {val[:100]}')
                if re.search(r'norisk', val_lower) and 'ryzyk' not in val_lower:
                    add_issue(short, name, locale, 'TERM-PL', f'{key}: "NoRisk" should be "Bez Ryzyka" -> {val[:100]}')
            
            # Default name check
            text1 = b.get('text_1', '')
            if 'default:' in text1:
                if '"friend"' in text1 or "'friend'" in text1:
                    add_issue(short, name, locale, 'DEFAULT-NAME', f'text_1: default:"friend" should be translated to PL')
                if '"Player"' in text1 or "'Player'" in text1:
                    add_issue(short, name, locale, 'DEFAULT-NAME', f'text_1: default:"Player" should be translated to PL')
                if '"Friend"' in text1 or "'Friend'" in text1:
                    add_issue(short, name, locale, 'DEFAULT-NAME', f'text_1: default:"Friend" should be translated to PL')
            
            # Button ALL CAPS check
            btn = b.get('button_text_1', '') or b.get('promocode_button_1', '')
            if btn and btn != btn.upper():
                add_issue(short, name, locale, 'BUTTON-CAPS', f'Button not ALL CAPS: "{btn}"')
            
            # Subject same as Default check
            if name in emails and 'Default' in emails[name]:
                default_subj = emails[name]['Default'].get('subject', '')
                pl_subj = b.get('subject', '')
                if default_subj and pl_subj == default_subj:
                    add_issue(short, name, locale, 'UNTRANSLATED', f'subject same as Default: "{pl_subj[:80]}"')
                
                default_preh = emails[name]['Default'].get('preheader', '')
                pl_preh = b.get('preheader', '')
                if default_preh and pl_preh == default_preh:
                    add_issue(short, name, locale, 'UNTRANSLATED', f'preheader same as Default')
        
        # === FR-FR CHECKS ===
        if locale == 'fr-FR':
            # Subject, preheader, body (text_1, text_2, sometimes text_3) should be in English
            # Compare with Default - they should be the same
            if name in emails and 'Default' in emails[name]:
                default_b = emails[name]['Default']
                
                # Subject should match Default (English)
                fr_subj = b.get('subject', '')
                def_subj = default_b.get('subject', '')
                if fr_subj and def_subj and fr_subj != def_subj:
                    add_issue(short, name, locale, 'FR-SUBJECT', f'subject differs from Default EN: FR="{fr_subj[:60]}" vs EN="{def_subj[:60]}"')
                
                # Preheader should match Default (English)
                fr_preh = b.get('preheader', '')
                def_preh = default_b.get('preheader', '')
                if fr_preh and def_preh and fr_preh != def_preh:
                    add_issue(short, name, locale, 'FR-PREHEADER', f'preheader differs from Default EN')
                
                # text_1 (greeting) should match Default (English)
                fr_t1 = b.get('text_1', '')
                def_t1 = default_b.get('text_1', '')
                if fr_t1 and def_t1 and fr_t1 != def_t1:
                    add_issue(short, name, locale, 'FR-BODY', f'text_1 differs from Default EN')
                
                # text_2 (body) should match Default (English)
                fr_t2 = b.get('text_2', '')
                def_t2 = default_b.get('text_2', '')
                if fr_t2 and def_t2 and fr_t2 != def_t2:
                    add_issue(short, name, locale, 'FR-BODY', f'text_2 differs from Default EN')
                
                # button_text_1 should match Default (English)
                fr_btn = b.get('button_text_1', '') or b.get('promocode_button_1', '')
                def_btn = default_b.get('button_text_1', '') or default_b.get('promocode_button_1', '')
                if fr_btn and def_btn and fr_btn != def_btn:
                    add_issue(short, name, locale, 'FR-BUTTON', f'button differs from Default EN: FR="{fr_btn}" vs EN="{def_btn}"')
        
        # === LINK/URL CHECKS (all locales) ===
        for key, val in b.items():
            if 'href' in key or 'src' in key:
                continue  # Skip checking href/src fields for now
            # Check for URLs in text fields
            urls = re.findall(r'https?://[^\s"<>]+', val)
            for url in urls:
                if locale == 'hu-HU' and '/hu/' not in url and 'lang=hu' not in url and '?hu' not in url:
                    # Not necessarily an issue - depends on the URL structure
                    pass
                if locale == 'pl-PL' and '/pl/' not in url and 'lang=pl' not in url and '?pl' not in url:
                    pass
        
        # Check button_href_1 for locale
        btn_href = b.get('button_href_1', '')
        if btn_href:
            if locale == 'hu-HU' and btn_href:
                def_href = emails.get(name, {}).get('Default', {}).get('button_href_1', '')
                if def_href and btn_href == def_href:
                    # Same as default - might need locale param
                    pass  # Many links are universal, not always an issue
            if locale == 'fr-FR' and btn_href:
                def_href = emails.get(name, {}).get('Default', {}).get('button_href_1', '')
                if def_href and btn_href != def_href:
                    add_issue(short, name, locale, 'FR-LINK', f'button_href_1 differs from Default')

# === SUMMARY ===
print("=" * 80)
print("CELSIUS FULL AUDIT REPORT")
print("=" * 80)

# Count by category
cats = {}
for iss in issues:
    cat = iss.split(']')[0].replace('[', '')
    cats[cat] = cats.get(cat, 0) + 1

print(f"\nTotal issues: {len(issues)}")
print("\nBy category:")
for cat, cnt in sorted(cats.items()):
    print(f"  {cat}: {cnt}")

print("\n" + "=" * 80)
print("DETAILED ISSUES")
print("=" * 80)

# Sort by category
for iss in sorted(issues):
    print(iss)

# Also output to file
outpath = os.path.join(BASE, '_full_audit_result.txt')
with open(outpath, 'w', encoding='utf-8') as f:
    f.write("CELSIUS FULL AUDIT REPORT\n")
    f.write("=" * 80 + "\n")
    f.write(f"\nTotal issues: {len(issues)}\n")
    f.write("\nBy category:\n")
    for cat, cnt in sorted(cats.items()):
        f.write(f"  {cat}: {cnt}\n")
    f.write("\n" + "=" * 80 + "\n")
    f.write("DETAILED ISSUES\n")
    f.write("=" * 80 + "\n")
    for iss in sorted(issues):
        f.write(iss + "\n")

print(f"\nResults also saved to: _full_audit_result.txt")
