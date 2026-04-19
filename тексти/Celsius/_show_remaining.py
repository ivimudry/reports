"""Show current state of the 7 remaining fields that need manual <br> fixes."""
import re, os

DIR = r'c:\Projects\REPORTS\тексти\Celsius'
BR_RE = re.compile(r'<br\s*/?>', re.I)

TARGETS = {
    'DEP Retention - Table data.txt': ['Email 3C', 'Email 3S', 'Email 6C'],
    'SU Retention - Table data.txt': ['Email 3C', 'Email 4C', 'Email 5C'],
    'Nutrition #2 - Table data.txt': ['Email 4CL'],
}

for fname, emails in TARGETS.items():
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

    for block in blocks:
        d = {k: v for _, k, v in block}
        name = d.get('name', '')
        locale = d.get('locale', '')
        if name not in emails:
            continue
        if locale not in ('Default', 'fr-FR'):
            continue
        text2 = d.get('text_2', '')
        n = len(BR_RE.findall(text2))
        print(f"\n{'='*80}")
        print(f"FILE: {fname} | EMAIL: {name} | LOCALE: {locale} | <br> count: {n}")
        print(f"{'='*80}")
        # Show text with <br> highlighted
        display = text2.replace('<br>', '\n  <<<BR>>>\n')
        print(display[:2000])
