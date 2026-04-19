"""
Comprehensive manual-review dump: extracts ALL text fields from all blocks,
grouping by email name so Default / fr-FR / hu-HU / pl-PL are side by side.
Checks: promocode class, <strong> wrapping, <br> counts, <i> tags, &nbsp; usage.
"""
import re, os, json

DIR = r'c:\Projects\REPORTS\тексти\Celsius'
FILES = [
    'DEP Retention - Table data.txt',
    'SU Retention - Table data.txt',
    'Welcome Flow - Table data.txt',
    'FTD Retention Flow - Table data.txt',
    'Nutrition #2 - Table data.txt',
    'Nutrition #3 - Table data.txt',
    'Failed Deposit Flow - Table data.txt',
]

BR_RE = re.compile(r'<br\s*/?>', re.I)
STRONG_RE = re.compile(r'<strong[^>]*>.*?</strong>', re.DOTALL)
PROMO_RE = re.compile(r'<strong\s+class="promocode">[^<]+</strong>')
BARE_PROMO_RE = re.compile(r'<strong>([A-Z0-9]{4,})</strong>')  # promocode without class
WINNER_EMOJIS = '🏆💰🔥💎🥇🥈🥉'

issues = []

def parse_file(fpath):
    with open(fpath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    blocks = []
    current = []
    for i, raw in enumerate(lines):
        stripped = raw.rstrip('\n').rstrip('\r')
        if not stripped.strip():
            if current:
                blocks.append(current)
                current = []
            continue
        idx = stripped.find(': ')
        if idx > 0:
            current.append((i+1, stripped[:idx], stripped[idx+2:]))
    if current:
        blocks.append(current)
    return blocks

def check_issues(fname, email_name, locale, key, line_num, value, default_value):
    """Compare locale field against default field and report issues."""
    pfx = f"{fname} | {email_name} | {locale} | {key} (L{line_num})"
    
    # 1. Promocode class check
    bare_promos = BARE_PROMO_RE.findall(value)
    for code in bare_promos:
        # Check if this code exists as promocode in default
        if f'class="promocode">{code}</strong>' in default_value or f'class="promocode">{code}</strong>' in value:
            continue
        # Check if default has it as promocode
        if f'class="promocode">{code}' in default_value:
            issues.append(f"PROMOCODE_CLASS | {pfx} | Code '{code}' missing class='promocode'")
    
    # Also check if default has promocodes that locale doesn't
    def_promos = set(re.findall(r'class="promocode">([^<]+)</strong>', default_value))
    loc_promos = set(re.findall(r'class="promocode">([^<]+)</strong>', value))
    loc_bare = set(re.findall(r'<strong>([A-Z][A-Z0-9]{3,})</strong>', value))
    
    for code in def_promos:
        if code not in loc_promos:
            if code in loc_bare:
                issues.append(f"PROMOCODE_CLASS | {pfx} | Code '{code}' has <strong> but missing class='promocode'")
            elif code in value:
                issues.append(f"PROMOCODE_WRAP | {pfx} | Code '{code}' present but not wrapped in <strong class='promocode'>")

    # 2. <br> count check
    def_br = len(BR_RE.findall(default_value))
    loc_br = len(BR_RE.findall(value))
    if def_br != loc_br:
        issues.append(f"BR_COUNT | {pfx} | Default={def_br} Locale={loc_br}")

    # 3. Winner emoji block <strong> wrapping check
    # Check if default has winner lines wrapped in <strong> that locale doesn't
    for emoji in WINNER_EMOJIS:
        if emoji in default_value and emoji in value:
            # Check if emoji is inside <strong> in default
            def_in_strong = bool(re.search(r'<strong[^>]*>[^<]*' + re.escape(emoji), default_value))
            loc_in_strong = bool(re.search(r'<strong[^>]*>[^<]*' + re.escape(emoji), value))
            if def_in_strong and not loc_in_strong:
                issues.append(f"WINNER_STRONG | {pfx} | Winner emoji {emoji} not wrapped in <strong> (Default has it)")
                break  # One report per field is enough

    # 4. <strong> tag count check (excluding empty <strong></strong>)
    def_strong_open = len(re.findall(r'<strong[^>]*>', default_value))
    def_strong_close = len(re.findall(r'</strong>', default_value))
    loc_strong_open = len(re.findall(r'<strong[^>]*>', value))
    loc_strong_close = len(re.findall(r'</strong>', value))
    
    # Don't flag if just empty <strong></strong> difference
    def_empty = default_value.count('<strong></strong>')
    loc_empty = value.count('<strong></strong>')
    
    real_def = def_strong_open - def_empty
    real_loc = loc_strong_open - loc_empty
    if real_def != real_loc:
        issues.append(f"STRONG_COUNT | {pfx} | Default={real_def}({def_empty} empty) Locale={real_loc}({loc_empty} empty)")

    # 5. <i> tag check
    def_i = len(re.findall(r'</?i>', default_value))
    loc_i = len(re.findall(r'</?i>', value))
    if def_i != loc_i:
        issues.append(f"I_TAG_COUNT | {pfx} | Default={def_i} Locale={loc_i}")

    # 6. &nbsp; check
    def_nbsp = default_value.count('&nbsp;')
    loc_nbsp = value.count('&nbsp;')
    if def_nbsp != loc_nbsp:
        issues.append(f"NBSP_COUNT | {pfx} | Default={def_nbsp} Locale={loc_nbsp}")


# ── Main ──
for fname in FILES:
    fpath = os.path.join(DIR, fname)
    blocks = parse_file(fpath)
    
    # Index by (name, locale)
    index = {}
    for block in blocks:
        d = {k: v for _, k, v in block}
        name = d.get('name', '')
        locale = d.get('locale', '')
        index[(name, locale)] = block
    
    # Get all email names in order
    seen = set()
    email_names = []
    for block in blocks:
        d = {k: v for _, k, v in block}
        name = d.get('name', '')
        if name not in seen:
            seen.add(name)
            email_names.append(name)
    
    for email_name in email_names:
        default_block = index.get((email_name, 'Default'))
        if not default_block:
            continue
        default_d = {k: v for _, k, v in default_block}
        
        for locale in ['fr-FR', 'hu-HU', 'pl-PL']:
            loc_block = index.get((email_name, locale))
            if not loc_block:
                issues.append(f"MISSING_BLOCK | {fname} | {email_name} | {locale} | Block missing!")
                continue
            
            for line_num, key, loc_val in loc_block:
                if not (key.startswith('text_') or key == 'rich_text' or key.startswith('button_text')):
                    continue
                def_val = default_d.get(key, '')
                if not def_val:
                    continue
                check_issues(fname, email_name, locale, key, line_num, loc_val, def_val)


# ── Report ──
print(f"Total issues found: {len(issues)}\n")

# Group by issue type
by_type = {}
for issue in issues:
    itype = issue.split(' | ')[0]
    by_type.setdefault(itype, []).append(issue)

for itype, items in sorted(by_type.items()):
    print(f"\n{'='*80}")
    print(f"  {itype}: {len(items)} issues")
    print(f"{'='*80}")
    for item in items:
        print(f"  {item}")
