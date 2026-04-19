"""
Fallback fix for 15 fr-FR fields where tag counts don't match Default.
Uses emoji anchors, &nbsp; patterns, and sentence boundaries to restore <br>.
"""
import re, os

DIR = r'c:\Projects\REPORTS\тексти\Celsius'

FILES = [
    'DEP Retention - Table data.txt',
    'SU Retention - Table data.txt',
    'FTD Retention Flow - Table data.txt',
    'Nutrition #2 - Table data.txt',
]

BR_RE = re.compile(r'<br\s*/?>', re.I)
TAG_RE = re.compile(r'<[^>]+>')
WINNER_EMOJIS = '🏆💰🔥💎🥇🥈🥉'


def extract_non_br_tags(html):
    tags = []
    for m in TAG_RE.finditer(html):
        tag = m.group()
        if not BR_RE.fullmatch(tag):
            tags.append(tag)
    return tags


def fix_field(def_val, fr_val):
    """Fallback <br> restoration using anchored splitting."""
    def_br_total = len(BR_RE.findall(def_val))
    fr_br_total = len(BR_RE.findall(fr_val))
    if def_br_total == 0 or def_br_total == fr_br_total:
        return fr_val, False

    # Split Default by <br> groups to get segments + group sizes
    parts = re.split(r'((?:<br\s*/?>)+)', def_val)
    segments = [parts[i] for i in range(0, len(parts), 2)]
    br_groups = [len(BR_RE.findall(parts[i])) for i in range(1, len(parts), 2)]

    if not br_groups:
        return fr_val, False

    # For each br_group, determine the split point in fr_val
    split_specs = []  # (replace_start, replace_end, br_count)
    search_from = 0

    for idx, count in enumerate(br_groups):
        next_seg = segments[idx + 1] if idx + 1 < len(segments) else ''
        prev_seg = segments[idx]

        # Check if Default had &nbsp; right before this <br> group
        prev_has_nbsp = prev_seg.rstrip().endswith('&nbsp;')

        br_str = '<br>' * count
        found = False

        # --- Strategy 1: Emoji anchor ---
        # Check if next segment starts with (optional tags +) winner emoji
        next_stripped = re.sub(r'^(\s*<[^>]+>)*\s*', '', next_seg)
        emoji_char = next_stripped[0] if next_stripped and next_stripped[0] in WINNER_EMOJIS else None

        if emoji_char and not found:
            pos = fr_val.find(emoji_char, search_from)
            if pos > search_from:
                # Find the space(s) before emoji
                sp = pos - 1
                while sp >= search_from and fr_val[sp] in ' \t':
                    sp -= 1
                sp += 1  # first space char
                # Check for &nbsp; right before the space
                if sp >= 6 and fr_val[sp - 6:sp] == '&nbsp;':
                    if prev_has_nbsp:
                        # Keep &nbsp;, replace space with <br>
                        split_specs.append((sp, pos, br_str))
                    else:
                        # &nbsp; is artifact, replace it too
                        split_specs.append((sp - 6, pos, br_str))
                else:
                    split_specs.append((sp, pos, br_str))
                search_from = pos + 1
                found = True

        # --- Strategy 2: &nbsp; + space ---
        if not found:
            nbsp_pos = fr_val.find('&nbsp; ', search_from)
            if nbsp_pos >= search_from:
                if prev_has_nbsp:
                    # Default had &nbsp;<br>, keep &nbsp; in fr-FR
                    split_specs.append((nbsp_pos + 6, nbsp_pos + 7, br_str))
                else:
                    # &nbsp; is artifact
                    split_specs.append((nbsp_pos, nbsp_pos + 7, br_str))
                search_from = nbsp_pos + 7
                found = True

        # --- Strategy 3: </strong> SPACE before non-<strong> text ---
        if not found:
            m = re.search(r'</strong>\s+(?!<strong)', fr_val[search_from:])
            if m:
                abs_start = search_from + m.start() + len('</strong>')
                abs_end = search_from + m.end()
                split_specs.append((abs_start, abs_end, br_str))
                search_from = abs_end
                found = True

        # --- Strategy 4: Sentence boundary ---
        if not found:
            m = re.search(r'([.!?:…🆙🍬🎱🎰🌟])\s+', fr_val[search_from:])
            if m:
                abs_start = search_from + m.start() + len(m.group(1))
                abs_end = search_from + m.end()
                split_specs.append((abs_start, abs_end, br_str))
                search_from = abs_end
                found = True

        # --- Strategy 5: </strong> followed by space ---
        if not found:
            m = re.search(r'</strong>\s+', fr_val[search_from:])
            if m:
                abs_start = search_from + m.start() + len('</strong>')
                abs_end = search_from + m.end()
                split_specs.append((abs_start, abs_end, br_str))
                search_from = abs_end
                found = True

        if not found:
            print(f"      COULD NOT FIND split point for br_group #{idx} (count={count})")

    # Apply splits from right to left
    result = fr_val
    for start, end, br_str in reversed(split_specs):
        result = result[:start] + br_str + result[end:]

    new_br = len(BR_RE.findall(result))
    return result, result != fr_val


# ── Main ──────────────────────────────────────────────────────────────────────

total_fixed = 0

for fname in FILES:
    fpath = os.path.join(DIR, fname)
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
            current.append((i, stripped[:idx], stripped[idx + 2:]))
    if current:
        blocks.append(current)

    index = {}
    for block in blocks:
        d = {k: v for _, k, v in block}
        index[(d.get('name', ''), d.get('locale', ''))] = block

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
            def_n = len(BR_RE.findall(def_val))
            fr_n = len(BR_RE.findall(fr_val))
            if def_n == 0 or def_n == fr_n:
                continue  # Already OK (fixed by first pass or never needed)
            new_val, changed = fix_field(def_val, fr_val)
            if changed:
                new_n = len(BR_RE.findall(new_val))
                lines[line_idx] = f'{key}: {new_val}\n'
                file_fixed += 1
                status = "OK" if new_n == def_n else f"PARTIAL ({new_n}/{def_n})"
                print(f"    {name}|{key}: {fr_n}->{new_n}/{def_n} — {status}")

    with open(fpath, 'w', encoding='utf-8') as f:
        f.writelines(lines)

    print(f"  {fname}: {file_fixed} fields fixed")
    total_fixed += file_fixed

print(f"\nDone: {total_fixed} total fields fixed.")

# ── Verification ──────────────────────────────────────────────────────────────
print("\n=== VERIFICATION ===")
all_ok = True
for fname in FILES:
    fpath = os.path.join(DIR, fname)
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
            current.append((i, stripped[:idx], stripped[idx + 2:]))
    if current:
        blocks.append(current)

    index = {}
    for block in blocks:
        d = {k: v for _, k, v in block}
        index[(d.get('name', ''), d.get('locale', ''))] = block

    fails = []
    for block in blocks:
        d = {k: v for _, k, v in block}
        if d.get('locale') != 'fr-FR':
            continue
        name = d.get('name', '')
        db = index.get((name, 'Default'))
        if not db:
            continue
        dd = {k: v for _, k, v in db}
        for _, key, fr_val in block:
            if not (key.startswith('text_') or key == 'rich_text'):
                continue
            def_val = dd.get(key, '')
            if not def_val:
                continue
            def_n = len(BR_RE.findall(def_val))
            fr_n = len(BR_RE.findall(fr_val))
            if def_n > 0 and def_n != fr_n:
                fails.append(f"    {name}|{key}: Default={def_n} fr-FR={fr_n}")
                all_ok = False

    if fails:
        print(f"  ISSUES {fname}:")
        for f in fails:
            print(f)
    else:
        print(f"  OK {fname}")

print(f"\n{'ALL OK' if all_ok else 'SOME ISSUES REMAIN'}")
