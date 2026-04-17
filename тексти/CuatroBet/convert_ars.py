#!/usr/bin/env python3
"""
Bulk converter for CuatroBet implementation guides and playbooks.
Reads CLEAN content from specific git commits, applies:
  1) "App Push" -> "Web Push"
  2) All ARS numeric values * 4.57 (smart rounding)
  3) Injects a note into doc 02
Then writes the converted files to disk.
"""
import re, subprocess, sys, os

sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

MULT = 4.57
GUIDE_COMMIT = "dcd286b"
PLAYBOOK_COMMIT = "23424c6"
GUIDE_DIR = "implementation-guide-ru"

PLAYBOOK_FILES = [
    "cuatrobet_playbook_ru.md",
    "cuatrobet_playbook_en.md",
]

def smart_round(value):
    if value < 500:
        return int(round(value / 50) * 50)
    if value < 5000:
        return int(round(value / 100) * 100)
    if value < 50000:
        return int(round(value / 500) * 500)
    if value < 500000:
        return int(round(value / 1000) * 1000)
    return int(round(value / 5000) * 5000)

def convert_value(n, is_boundary=False):
    result = smart_round(n * MULT)
    if is_boundary and n > 1 and str(n).endswith('1'):
        result += 1
    return result

def parse_num(s):
    return int(s.replace(',', '').replace(' ', '').replace('\u00a0', ''))

def fmt_comma(n):
    return f"{n:,}"

def fmt_space(n):
    return f"{n:,}".replace(",", " ")

def git_show(commit, relpath):
    r = subprocess.run(
        ['git', 'show', f'{commit}:{relpath}'],
        capture_output=True, cwd=r'c:\Projects\REPORTS'
    )
    if r.returncode != 0:
        return None
    return r.stdout.decode('utf-8')

def list_guide_files():
    """List guide .md files from disk, return as git-relative paths."""
    base = os.path.join(r'c:\Projects\REPORTS', '\u0442\u0435\u043a\u0441\u0442\u0438', 'CuatroBet', GUIDE_DIR)
    files = sorted(f for f in os.listdir(base) if f.endswith('.md'))
    return [f'\u0442\u0435\u043a\u0441\u0442\u0438/CuatroBet/{GUIDE_DIR}/{f}' for f in files]

NOTE_ANCHOR = "**\u0422\u0440\u0438\u0433\u0433\u0435\u0440 \u0432\u0445\u043e\u0434\u0430:** `cumulative_deposits_ars >= 685000` AND `days_since_last_activity <= 14`"
NOTE_INSERT = (
    "\n\n> **\u041f\u0440\u0438\u043c\u0435\u0447\u0430\u043d\u0438\u0435:** \u041c\u0435\u0436\u0434\u0443 High (x2, \u0434\u043e 915,000 ARS) \u0438 Pre-VIP+ (x3) "
    "\u0441\u0443\u0449\u0435\u0441\u0442\u0432\u0443\u0435\u0442 \u0440\u0430\u0437\u0440\u044b\u0432 685,000\u2013915,000 ARS. \u0418\u0433\u0440\u043e\u043a\u0438 \u0432 \u044d\u0442\u043e\u043c \u0434\u0438\u0430\u043f\u0430\u0437\u043e\u043d\u0435 \u043f\u043e\u043b\u0443\u0447\u0430\u044e\u0442 "
    "\u0431\u043e\u043d\u0443\u0441\u044b \u0443\u0440\u043e\u0432\u043d\u044f High (x2). \u041f\u0440\u0438 \u0434\u043e\u0441\u0442\u0438\u0436\u0435\u043d\u0438\u0438 915,000 ARS \u0430\u043a\u0442\u0438\u0432\u0438\u0440\u0443\u0435\u0442\u0441\u044f Pre-VIP+ (x3)."
)

PAT_BETWEEN = re.compile(
    r'(_ars\s+BETWEEN\s+)(\d[\d,. \u00a0]*)(\s+AND\s+)(\d[\d,. \u00a0]*)',
    re.IGNORECASE
)

PAT_MAIN = re.compile(
    r'(\d[\d,\s\u00a0]*\d|\d)'
    r'(\s*[-/]\s*)'
    r'(\d[\d,\s\u00a0]*\d|\d)'
    r'(\s*ARS\b)'
    r'|'
    r'(\d[\d,\s\u00a0]*\d|\d)'
    r'(\s*ARS\b)'
)

PAT_CODE = re.compile(
    r'(_ars\s*(?:>=|<=|>|<|==|!=|=)\s*)(\d[\d,. \u00a0]*)'
)

def convert_text(text):
    def repl_between(m):
        pre, n1s, mid, n2s = m.group(1), m.group(2), m.group(3), m.group(4)
        return f"{pre}{convert_value(parse_num(n1s))}{mid}{convert_value(parse_num(n2s))}"

    text = PAT_BETWEEN.sub(repl_between, text)

    def repl_main(m):
        if m.group(1) is not None:
            n1s, sep, n2s, suffix = m.group(1), m.group(2), m.group(3), m.group(4)
            n1, n2 = parse_num(n1s), parse_num(n2s)
            c1, c2 = convert_value(n1), convert_value(n2)
            use_space = ' ' in n1s or '\u00a0' in n1s
            fmt = fmt_space if use_space else fmt_comma
            return f"{fmt(c1)}{sep}{fmt(c2)}{suffix}"
        else:
            ns, suffix = m.group(5), m.group(6)
            n = parse_num(ns)
            c = convert_value(n)
            use_space = ' ' in ns or '\u00a0' in ns
            fmt = fmt_space if use_space else fmt_comma
            return f"{fmt(c)}{suffix}"

    text = PAT_MAIN.sub(repl_main, text)

    def repl_code(m):
        pre, ns = m.group(1), m.group(2)
        return f"{pre}{convert_value(parse_num(ns), is_boundary=True)}"

    text = PAT_CODE.sub(repl_code, text)
    text = text.replace("App Push", "Web Push")
    return text

def main():
    base = r'c:\Projects\REPORTS\тексти\CuatroBet'

    guide_paths = list_guide_files()
    print(f"Found {len(guide_paths)} guide files")

    for gpath in guide_paths:
        fname = os.path.basename(gpath)
        content = git_show(GUIDE_COMMIT, gpath)
        if content is None:
            print(f"  SKIP (not in commit): {fname}")
            continue

        converted = convert_text(content)

        if fname.startswith("02-"):
            if NOTE_ANCHOR in converted:
                converted = converted.replace(NOTE_ANCHOR, NOTE_ANCHOR + NOTE_INSERT)
                print(f"  Injected note into {fname}")
            else:
                print(f"  WARNING: note anchor not found in {fname}")
        outpath = os.path.join(base, GUIDE_DIR, fname)
        with open(outpath, 'w', encoding='utf-8') as f:
            f.write(converted)
        print(f"  OK: {fname}")

    print(f"\nProcessing {len(PLAYBOOK_FILES)} playbook files")
    for pf in PLAYBOOK_FILES:
        relpath = f"\u0442\u0435\u043a\u0441\u0442\u0438/CuatroBet/{pf}"
        content = git_show(PLAYBOOK_COMMIT, relpath)
        if content is None:
            print(f"  SKIP (not in commit): {pf}")
            continue
        converted = convert_text(content)
        outpath = os.path.join(base, pf)
        with open(outpath, 'w', encoding='utf-8') as f:
            f.write(converted)
        print(f"  OK: {pf}")

    print("\nDone!")

if __name__ == '__main__':
    main()