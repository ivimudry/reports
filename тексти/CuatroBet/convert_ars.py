"""
Bulk conversion script for CuatroBet → Bluechip:
1. Replace "App Push" → "Web Push" everywhere
2. Multiply all ARS values by 4.57 with smart rounding
"""
import re
import os
import glob

MULTIPLIER = 4.57

def smart_round(value):
    """Round to a clean number appropriate for CRM documents."""
    if value < 500:
        return int(round(value / 50) * 50)
    elif value < 5000:
        return int(round(value / 100) * 100)
    elif value < 50000:
        return int(round(value / 500) * 500)
    elif value < 500000:
        return int(round(value / 1000) * 1000)
    else:
        return int(round(value / 5000) * 5000)

def parse_number(s):
    """Parse a number string like '1,000' or '1 000' or '150000' to int."""
    cleaned = s.replace(',', '').replace(' ', '').replace('\u00a0', '')
    try:
        return int(cleaned)
    except ValueError:
        try:
            return int(float(cleaned))
        except ValueError:
            return None

def format_number(value, original_format, is_code=False):
    """Format a number preserving the original separator style."""
    value = int(value)
    if is_code:
        return str(value)
    if value < 1000:
        return str(value)
    # Detect separator
    if ',' in original_format:
        sep = ','
    elif re.search(r'\d\s\d', original_format):
        sep = ' '
    else:
        sep = ','
    s = str(value)
    parts = []
    while len(s) > 3:
        parts.append(s[-3:])
        s = s[:-3]
    parts.append(s)
    return sep.join(reversed(parts))

def convert_value(original_str, is_code=False):
    """Convert an ARS value: multiply by MULTIPLIER, round, format."""
    num = parse_number(original_str)
    if num is None or num == 0:
        return original_str
    is_boundary = (num % 10 == 1) and num > 10
    new_value = num * MULTIPLIER
    rounded = smart_round(new_value)
    if is_boundary:
        rounded += 1
    return format_number(rounded, original_str, is_code)

def process_content(content):
    """Process content: App Push → Web Push, ARS × 4.57."""
    log = []

    # 1. App Push → Web Push
    for old, new in [('App Push', 'Web Push'), ('APP PUSH', 'WEB PUSH'), ('app push', 'web push')]:
        count = content.count(old)
        if count:
            content = content.replace(old, new)
            log.append(f"  Replace '{old}' → '{new}' ({count}×)")

    # 2. ARS range patterns: number–number ARS
    range_pat = re.compile(
        r'(?<![.\d\w])'
        r'(\d{1,3}(?:[,\s]\d{3})+|\d+)'
        r'(\s*[–\-]\s*)'
        r'(\d{1,3}(?:[,\s]\d{3})+|\d+)'
        r'(\s*ARS\b)',
        re.IGNORECASE
    )
    def repl_range(m):
        n1, sep, n2, suf = m.group(1), m.group(2), m.group(3), m.group(4)
        new1, new2 = convert_value(n1), convert_value(n2)
        log.append(f"  Range: {n1}{sep.strip()}{n2} ARS → {new1}{sep.strip()}{new2} ARS")
        return f"{new1}{sep}{new2}{suf}"
    content = range_pat.sub(repl_range, content)

    # 2.5. Slash-separated: 500/1000/1500 ARS
    slash_pat = re.compile(
        r'(?<![.\d\w])'
        r'(\d[\d,]*(?:\s*/\s*\d[\d,]*)+)'
        r'(\s*ARS\b)',
        re.IGNORECASE
    )
    def repl_slash(m):
        nums_str, suf = m.group(1), m.group(2)
        parts = re.split(r'\s*/\s*', nums_str)
        new_parts = [convert_value(p) for p in parts]
        log.append(f"  Slash: {nums_str} ARS → {'/'.join(new_parts)} ARS")
        return '/'.join(new_parts) + suf
    content = slash_pat.sub(repl_slash, content)

    # 3. Single number ARS
    single_pat = re.compile(
        r'(?<![.\d\w])'
        r'(\d{1,3}(?:[,\s]\d{3})+|\d+)'
        r'(\s*ARS\b)',
        re.IGNORECASE
    )
    def repl_single(m):
        n, suf = m.group(1), m.group(2)
        new = convert_value(n)
        if new != n:
            log.append(f"  Single: {n} ARS → {new} ARS")
        return f"{new}{suf}"
    content = single_pat.sub(repl_single, content)

    # 4. _ars comparison (not followed by ARS to skip already-converted)
    comp_pat = re.compile(
        r'(_ars\s*(?:>=|<=|≥|≤|>|<|=)\s*)'
        r'(\d[\d,]*)'
        r'(?!\s*ARS)',
        re.IGNORECASE
    )
    def repl_comp(m):
        pfx, n = m.group(1), m.group(2)
        new = convert_value(n, is_code=True)
        if new != n:
            log.append(f"  Code: {pfx.strip()}{n} → {pfx.strip()}{new}")
        return f"{pfx}{new}"
    content = comp_pat.sub(repl_comp, content)

    # 5. _ars BETWEEN X AND Y
    between_pat = re.compile(
        r'(_ars\s+BETWEEN\s+)'
        r'(\d+)'
        r'(\s+AND\s+)'
        r'(\d+)',
        re.IGNORECASE
    )
    def repl_between(m):
        pfx, n1, mid, n2 = m.group(1), m.group(2), m.group(3), m.group(4)
        new1, new2 = convert_value(n1, is_code=True), convert_value(n2, is_code=True)
        log.append(f"  BETWEEN: {n1} AND {n2} → {new1} AND {new2}")
        return f"{pfx}{new1}{mid}{new2}"
    content = between_pat.sub(repl_between, content)

    # 6. Number before cumulative_deposits_ars: 300000 - cumulative_deposits_ars
    before_attr_pat = re.compile(
        r'(?<![.\d\w])(\d+)(\s*[-–]\s*cumulative_deposits_ars)'
    )
    def repl_before(m):
        n, suf = m.group(1), m.group(2)
        new = convert_value(n, is_code=True)
        if new != n:
            log.append(f"  Before attr: {n} → {new}")
        return f"{new}{suf}"
    content = before_attr_pat.sub(repl_before, content)

    return content, log

# ── Main ──
base_dir = os.path.dirname(os.path.abspath(__file__))
guide_dir = os.path.join(base_dir, 'implementation-guide-ru')

files = sorted(glob.glob(os.path.join(guide_dir, '*.md')))
files.append(os.path.join(base_dir, 'cuatrobet_playbook_ru.md'))
files.append(os.path.join(base_dir, 'cuatrobet_playbook_en.md'))

total = 0
for fp in files:
    with open(fp, 'r', encoding='utf-8') as f:
        original = f.read()
    processed, log = process_content(original)
    if original != processed:
        with open(fp, 'w', encoding='utf-8') as f:
            f.write(processed)
        print(f"\n{'='*60}")
        print(f"MODIFIED: {os.path.basename(fp)}")
        for entry in log:
            print(entry)
        total += 1
    else:
        print(f"  — no changes: {os.path.basename(fp)}")

print(f"\n{'='*60}")
print(f"Total files modified: {total}/{len(files)}")
print("Done!")
