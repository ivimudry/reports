"""Fix the single remaining SU 5C: <br><br> → &nbsp;<br> at 'démarrer.'"""
import re, os

fpath = os.path.join(r'c:\Projects\REPORTS\тексти\Celsius', 'SU Retention - Table data.txt')
with open(fpath, 'r', encoding='utf-8') as f:
    content = f.read()

# The text has curly apostrophe U+2019 in L'offre/L\u2019offre
# Need to change <br><br> to &nbsp;<br> between "démarrer." and "L*offre"
# Use regex to handle both quote types
old = re.compile(r'd\u00e9marrer\.<br><br>L[\u2019\']offre')
m = old.search(content)
if m:
    matched = m.group()
    replacement = matched.replace('<br><br>', '&nbsp;<br>')
    content = content[:m.start()] + replacement + content[m.end():]
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Fixed: '{matched[:50]}' → '{replacement[:50]}'")
else:
    print("Pattern not found, let me search...")
    # Search nearby
    idx = content.find('d\u00e9marrer.')
    if idx == -1:
        idx = content.find('démarrer.')
    if idx >= 0:
        snippet = content[idx:idx+80]
        print(f"Found at {idx}: {repr(snippet)}")

# Verify
BR_RE = re.compile(r'<br\s*/?>', re.I)
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
for b in blocks:
    d = {k: v for _, k, v in b}
    index[(d.get('name', ''), d.get('locale', ''))] = b

# Check Email 5C
for loc in ('Default', 'fr-FR'):
    b = index.get(('Email 5C', loc))
    if b:
        d = {k: v for _, k, v in b}
        n = len(BR_RE.findall(d.get('text_2', '')))
        print(f"  Email 5C|{loc}: {n} <br>")
