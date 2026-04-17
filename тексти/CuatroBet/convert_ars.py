"""
Bulk conversion script for CuatroBet -> Bluechip:
1. Replace "App Push" -> "Web Push" everywhere
2. Multiply all ARS values by 4.57 with smart rounding
Uses SINGLE-PASS approach to avoid double-conversion.
"""
import re
import os
import sys
import glob

sys.stdout.reconfigure(encoding='utf-8')

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
    cleaned = s.replace(',', '').replace('\u00a0', '')
    # Handle space-separated thousands (only strip spaces between digits)
    cleaned = re.sub(r'(?<=\d) (?=\d)', '', cleaned)
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
    # Detect separator from original
    if ',' in original_format:
        sep = ','
    elif re.search(r'\d \d', original_format):
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


# Number sub-pattern (non-capturing): matches 1,000  1 000  150000  500 etc.
# Uses literal space only (not \s) to avoid matching across lines
_NUM = r'(?:\d{1,3}(?:[, ]\d{3})+|\d+)'


def process_content(content):
    """Process content: App Push -> Web Push, ARS x 4.57 (single-pass)."""
    log = []

    # -- 1. App Push -> Web Push --
    for old, new in [('App Push', 'Web Push'), ('APP PUSH', 'WEB PUSH'),
                     ('app push', 'web push')]:
        count = content.count(old)
        if count:
            content = content.replace(old, new)
            log.append(f"  '{old}' -> '{new}' ({count}x)")

    # -- 2. SINGLE-PASS: All "number ARS" patterns --
    # Combined regex: range | slash | single  (tried left-to-right)
    master_pat = re.compile(
        r'(?<![.\d\w])(?:'
            # Alt 1: Range   number-number ARS
            r'(' + _NUM + r')'       # g1: num1
            r'([ ]*[-\u2013][ ]*)'   # g2: dash separator (- or en-dash)
            r'(' + _NUM + r')'       # g3: num2
            r'([ ]*ARS)\b'          # g4: ARS
        r'|'
            # Alt 2: Slash   num/num/.../ARS
            r'(\d[\d,]*(?:[ ]*/[ ]*\d[\d,]*)+)'  # g5: slash-joined
            r'([ ]*ARS)\b'                        # g6: ARS
        r'|'
            # Alt 3: Single  number ARS
            r'(' + _NUM + r')'       # g7: number
            r'([ ]*ARS)\b'          # g8: ARS
        r')',
        re.IGNORECASE
    )

    def repl_master(m):
        if m.group(1) is not None:
            # Range
            n1, sep, n2, suf = m.group(1), m.group(2), m.group(3), m.group(4)
            c1, c2 = convert_value(n1), convert_value(n2)
            log.append(f"  Range: {n1}{sep.strip()}{n2} ARS -> {c1}{sep.strip()}{c2} ARS")
            return f"{c1}{sep}{c2}{suf}"
        elif m.group(5) is not None:
            # Slash
            nums_str, suf = m.group(5), m.group(6)
            parts = re.split(r'[ ]*/[ ]*', nums_str)
            new_parts = [convert_value(p) for p in parts]
            log.append(f"  Slash: {nums_str} ARS -> {'/'.join(new_parts)} ARS")
            return '/'.join(new_parts) + suf
        else:
            # Single
            n, suf = m.group(7), m.group(8)
            c = convert_value(n)
            if c != n:
                log.append(f"  Single: {n} ARS -> {c} ARS")
            return f"{c}{suf}"

    content = master_pat.sub(repl_master, content)

    # -- 3. Code: _ars comparisons (NOT followed by ARS to skip already-done) --
    comp_pat = re.compile(
        r'(_ars\s*(?:>=|<=|\u2265|\u2264|>|<|=)\s*)'
        r'(\d[\d,]*)'
        r'(?!\s*ARS)',
        re.IGNORECASE
    )

    def repl_comp(m):
        pfx, n = m.group(1), m.group(2)
        c = convert_value(n, is_code=True)
        if c != n:
            log.append(f"  Code: {pfx.strip()}{n} -> {pfx.strip()}{c}")
        return f"{pfx}{c}"

    content = comp_pat.sub(repl_comp, content)

    # -- 4. Code: _ars BETWEEN X AND Y --
    between_pat = re.compile(
        r'(_ars\s+BETWEEN\s+)'
        r'(\d+)'
        r'(\s+AND\s+)'
        r'(\d+)',
        re.IGNORECASE
    )

    def repl_between(m):
        pfx, n1, mid, n2 = m.group(1), m.group(2), m.group(3), m.group(4)
        c1 = convert_value(n1, is_code=True)
        c2 = convert_value(n2, is_code=True)
        log.append(f"  BETWEEN: {n1} AND {n2} -> {c1} AND {c2}")
        return f"{pfx}{c1}{mid}{c2}"

    content = between_pat.sub(repl_between, content)

    # -- 5. Code: number before cumulative_deposits_ars --
    before_attr_pat = re.compile(
        r'(?<![.\d\w])(\d+)(\s*[-\u2013]\s*cumulative_deposits_ars)'
    )

    def repl_before(m):
        n, suf = m.group(1), m.group(2)
        c = convert_value(n, is_code=True)
        if c != n:
            log.append(f"  Before attr: {n} -> {c}")
        return f"{c}{suf}"

    content = before_attr_pat.sub(repl_before, content)

    return content, log


def git_show(commit, rel_path, repo_dir):
    """Read file content directly from a git commit (bypass working tree)."""
    import subprocess
    git_path = rel_path.replace(os.sep, '/')
    result = subprocess.run(
        ['git', 'show', f'{commit}:{git_path}'],
        capture_output=True, text=True, encoding='utf-8',
        cwd=repo_dir
    )
    if result.returncode != 0:
        return None
    return result.stdout


# -- Main --
# Read CLEAN originals from specific git commits, process, write to disk.
REPO_DIR = r'c:\Projects\REPORTS'
GUIDE_COMMIT = 'dcd286b'   # April 13 — clean guide files
PLAYBOOK_COMMIT = '23424c6' # April 17 11:28 — clean playbook files

base_dir = os.path.dirname(os.path.abspath(__file__))
guide_dir = os.path.join(base_dir, 'implementation-guide-ru')

# Build file list with their git commits
files = []
for f in sorted(glob.glob(os.path.join(guide_dir, '*.md'))):
    files.append((f, GUIDE_COMMIT))
files.append((os.path.join(base_dir, 'cuatrobet_playbook_ru.md'), PLAYBOOK_COMMIT))
files.append((os.path.join(base_dir, 'cuatrobet_playbook_en.md'), PLAYBOOK_COMMIT))

# Special: doc 02 note must be injected into the clean content before conversion
NOTE_INSERT = (
    '**Триггер входа:** `cumulative_deposits_ars >= 150000` AND `days_since_last_activity <= 14`  \n'
    '**Повторный вход:** Нет\n'
    '\n'
    '> **Примечание:** Игроки с 150,000\u2013200,000 ARS получают офферы по множителю High (\u00d72) до достижения 200,000 ARS, затем переходят на Pre-VIP+ (\u00d73).\n'
    '\n'
    '**Окно Journey:** 30 дней (с возможностью расширения до 60)  '
)
NOTE_REPLACE = (
    '**Триггер входа:** `cumulative_deposits_ars >= 150000` AND `days_since_last_activity <= 14`  \n'
    '**Повторный вход:** Нет  \n'
    '**Окно Journey:** 30 дней (с возможностью расширения до 60)  '
)

total = 0
for fp, commit in files:
    # Read clean content from git
    rel = os.path.relpath(fp, REPO_DIR)
    original = git_show(commit, rel, REPO_DIR)
    if original is None:
        print(f"  SKIP (not in git): {os.path.basename(fp)}")
        continue

    # Inject doc 02 note before conversion
    if '02-pre-vip-lifecycle' in fp:
        original = original.replace(NOTE_REPLACE, NOTE_INSERT)

    processed, log = process_content(original)
    # Always write (since we're reading from git, not disk)
    with open(fp, 'w', encoding='utf-8') as f:
        f.write(processed)
    if log:
        print(f"\n{'='*60}")
        print(f"MODIFIED: {os.path.basename(fp)}")
        for entry in log:
            print(entry)
        total += 1
    else:
        print(f"  -- no changes: {os.path.basename(fp)}")

print(f"\n{'='*60}")
print(f"Total files modified: {total}/{len(files)}")
print("Done!")
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
