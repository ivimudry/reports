import os, re

DIR = r"c:\Projects\REPORTS\тексти\Celsius"
files = [f for f in os.listdir(DIR) if f.endswith('Table data.txt')]

for fn in sorted(files):
    path = os.path.join(DIR, fn)
    lines = open(path, 'r', encoding='utf-8').readlines()
    names = []
    for l in lines:
        s = l.strip()
        if s.startswith('name: '):
            n = s[6:]
            if n not in names:
                names.append(n)
    print(f"\n{fn}:")
    for n in names:
        m = re.match(r'Email\s+(\d+)([A-Z]*)', n)
        if m:
            num = m.group(1)
            suffix = m.group(2)
            print(f"  {n} → num={num}, suffix='{suffix}'")
        else:
            print(f"  {n} → PARSE ERROR")
