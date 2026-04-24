import os, re

DIR = r'c:\Projects\REPORTS\тексти\хейхо'
domains = {}
for fn in sorted(os.listdir(DIR)):
    if not fn.endswith('.txt'):
        continue
    text = open(os.path.join(DIR, fn), 'r', encoding='utf-8').read()
    for m in re.finditer(r'https?://([^/\s"\'<>?#]+)', text):
        d = m.group(1).lower()
        domains[d] = domains.get(d, 0) + 1

print("=== All domains found ===")
for d, c in sorted(domains.items(), key=lambda x: -x[1]):
    print(f"{c:6d}  {d}")
