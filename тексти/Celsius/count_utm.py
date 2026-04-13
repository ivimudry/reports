import os, re

DIR = r"c:\Projects\REPORTS\тексти\Celsius"
files = [f for f in os.listdir(DIR) if f.endswith('Table data.txt')]

for fn in sorted(files):
    path = os.path.join(DIR, fn)
    c = open(path, 'r', encoding='utf-8').read()
    utms = re.findall(r'[?&]utm_\w+=[^&\s"<>]+', c)
    print(f"{fn}: {len(utms)} utm params")
