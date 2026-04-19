"""
Restore <br> tags in fr-FR locale blocks.
Compares Default block HTML structure with fr-FR and re-inserts missing <br>.
"""
import re, os

DIR = r'c:\Projects\REPORTS\тексти\Celsius'

FILES = [
    'Welcome Flow - Table data.txt',
    'DEP Retention - Table data.txt',
    'SU Retention - Table data.txt',
    'FTD Retention Flow - Table data.txt',
    'Nutrition #2 - Table data.txt',
    'Nutrition #3 - Table data.txt',
]

BR_RE = re.compile(r'<br\s*/?>', re.I)
TAG_RE = re.compile(r'<[^>]+>')


def extract_non_br_tags(html):
    """Extract non-<br> HTML tags with positions."""
    tags = []
    for m in TAG_RE.finditer(html):
        tag = m.group()
        if not BR_RE.fullmatch(tag):
            tags.append((m.start(), m.end(), tag))
    return tags


def count_br(html, start, end):
    return len(BR_RE.findall(html[start:end]))


def fix_gap(fr_gap, def_gap, br_count):
    """Insert <br> tags into fr_gap based on default gap structure."""
    if br_count == 0:
        return fr_gap

    existing = len(BR_RE.findall(fr_gap))
    if existing >= br_count:
        return fr_gap

    br_str = '<br>' * br_count

    # Check if Default gap had &nbsp; (outside of <br>)
    def_clean = BR_RE.sub('', def_gap)
    def_has_nbsp = '&nbsp;' in def_clean

    if '&nbsp; ' in fr_gap:
        if def_has_nbsp:
            # Default had &nbsp; before <br> — keep &nbsp;, add <br> after it
            return fr_gap.replace('&nbsp; ', '&nbsp;' + br_str, 1)
        else:
            # &nbsp; is an artifact of removed <br> — replace it entirely
            return fr_gap.replace('&nbsp; ', br_str, 1)
    else:
        # No &nbsp; artifact — find sentence boundary
        m = re.search(r'([.!?:…]) +', fr_gap)
        if m:
            pos = m.start() + len(m.group(1))
            return fr_gap[:pos] + br_str + fr_gap[m.end():]
        elif ' ' in fr_gap.strip():
            pos = fr_gap.find(' ')
            return fr_gap[:pos] + br_str + fr_gap[pos + 1:]
        else:
            return br_str + fr_gap


def fix_field(def_val, fr_val):
    """Restore <br> in fr_val using def_val as reference. Returns (new_val, changed)."""
    def_br = len(BR_RE.findall(def_val))
    fr_br = len(BR_RE.findall(fr_val))

    if def_br == 0 or def_br == fr_br:
        return fr_val, False

    def_tags = extract_non_br_tags(def_val)
    fr_tags = extract_non_br_tags(fr_val)

    if len(def_tags) != len(fr_tags):
        print(f"      WARN tag-count mismatch: Default={len(def_tags)} fr-FR={len(fr_tags)}")
        return fr_val, False

    for i, (dt, ft) in enumerate(zip(def_tags, fr_tags)):
        if dt[2] != ft[2]:
            print(f"      WARN tag mismatch at #{i}: '{dt[2]}' vs '{ft[2]}'")
            return fr_val, False

    # Compute per-gap br counts and default gap text
    gaps_br = []
    gaps_def = []
    prev_d = 0
    for ds, de, _ in def_tags:
        gaps_br.append(count_br(def_val, prev_d, ds))
        gaps_def.append(def_val[prev_d:ds])
        prev_d = de
    gaps_br.append(count_br(def_val, prev_d, len(def_val)))
    gaps_def.append(def_val[prev_d:])

    # Rebuild fr text with <br> restored
    parts = []
    prev_f = 0
    for i, (fs, fe, ft) in enumerate(fr_tags):
        fr_gap = fr_val[prev_f:fs]
        parts.append(fix_gap(fr_gap, gaps_def[i], gaps_br[i]))
        parts.append(ft)
        prev_f = fe
    fr_gap = fr_val[prev_f:]
    parts.append(fix_gap(fr_gap, gaps_def[-1], gaps_br[-1]))

    result = ''.join(parts)
    return result, result != fr_val


# ── Main ──────────────────────────────────────────────────────────────────────

total_fixed = 0
total_verified_ok = 0
total_verified_fail = 0

for fname in FILES:
    fpath = os.path.join(DIR, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Parse blocks with line indices
    blocks = []          # list of [ (line_idx, key, value), ... ]
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
            key = stripped[:idx]
            value = stripped[idx + 2:]
            current.append((i, key, value))
    if current:
        blocks.append(current)

    # Index by (email_name, locale)
    index = {}
    for block in blocks:
        d = {k: v for _, k, v in block}
        name = d.get('name', '')
        locale = d.get('locale', '')
        index[(name, locale)] = block

    file_fixed = 0
    for block in blocks:
        d = {k: v for _, k, v in block}
        if d.get('locale') != 'fr-FR':
            continue
        name = d.get('name', '')
        default_block = index.get((name, 'Default'))
        if not default_block:
            continue
        default_d = {k: v for _, k, v in default_block}

        for line_idx, key, fr_val in block:
            if not (key.startswith('text_') or key == 'rich_text'):
                continue
            def_val = default_d.get(key, '')
            if not def_val:
                continue
            new_val, changed = fix_field(def_val, fr_val)
            if changed:
                lines[line_idx] = f'{key}: {new_val}\n'
                file_fixed += 1

    with open(fpath, 'w', encoding='utf-8') as f:
        f.writelines(lines)

    # ── Verify ────────────────────────────────────────────────────────────
    # Re-read and check <br> counts match Default for all fr-FR text fields
    with open(fpath, 'r', encoding='utf-8') as f:
        lines2 = f.readlines()

    blocks2 = []
    current2 = []
    for i, raw in enumerate(lines2):
        stripped = raw.rstrip('\n').rstrip('\r')
        if not stripped.strip():
            if current2:
                blocks2.append(current2)
                current2 = []
            continue
        idx = stripped.find(': ')
        if idx > 0:
            current2.append((i, stripped[:idx], stripped[idx + 2:]))
    if current2:
        blocks2.append(current2)

    idx2 = {}
    for b in blocks2:
        dd = {k: v for _, k, v in b}
        idx2[(dd.get('name', ''), dd.get('locale', ''))] = b

    v_ok = 0
    v_fail = 0
    for b in blocks2:
        dd = {k: v for _, k, v in b}
        if dd.get('locale') != 'fr-FR':
            continue
        name = dd.get('name', '')
        db = idx2.get((name, 'Default'))
        if not db:
            continue
        dbd = {k: v for _, k, v in db}
        for _, key, fr_val in b:
            if not (key.startswith('text_') or key == 'rich_text'):
                continue
            def_val = dbd.get(key, '')
            if not def_val:
                continue
            def_n = len(BR_RE.findall(def_val))
            fr_n = len(BR_RE.findall(fr_val))
            if def_n == fr_n:
                v_ok += 1
            elif def_n > 0:
                v_fail += 1
                print(f"    VERIFY FAIL {name}|{key}: Default={def_n} fr-FR={fr_n}")

    status = "OK" if v_fail == 0 else f"ISSUES ({v_fail})"
    print(f"  {fname}: {file_fixed} fixed | verify: {v_ok} ok, {v_fail} fail — {status}")
    total_fixed += file_fixed
    total_verified_ok += v_ok
    total_verified_fail += v_fail

print(f"\n{'=' * 60}")
print(f"TOTAL: {total_fixed} fields fixed")
print(f"VERIFY: {total_verified_ok} ok, {total_verified_fail} fail")
