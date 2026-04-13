import os, re

DIR = r"c:\Projects\REPORTS\тексти\Celsius"
files = [f for f in os.listdir(DIR) if f.endswith('Table data.txt')]

print("=== Sample URLs per file ===\n")
for fn in sorted(files):
    path = os.path.join(DIR, fn)
    lines = open(path, 'r', encoding='utf-8').readlines()
    locale = ''
    name = ''
    samples = {}
    for l in lines:
        s = l.strip()
        if s.startswith('name: '): name = s[6:]
        if s.startswith('locale: '): locale = s[8:]
        urls = re.findall(r'https://[^\s"<>]+', l)
        for u in urls:
            key = f"{name}|{locale}"
            if key not in samples:
                samples[key] = u
    print(f"{fn}:")
    shown = 0
    for key in list(samples.keys())[:8]:
        name_part, locale_part = key.split('|')
        print(f"  [{locale_part}] {name_part}: {samples[key][:120]}...")
        shown += 1
    print()

# Check no mailto: URLs got UTM
print("\n=== Checking mailto: URLs ===")
for fn in sorted(files):
    path = os.path.join(DIR, fn)
    c = open(path, 'r', encoding='utf-8').read()
    bad = re.findall(r'mailto:[^\s"<>]*utm_', c)
    if bad:
        print(f"  WARN {fn}: {len(bad)} mailto with UTM!")
    else:
        print(f"  {fn}: OK (no mailto UTM)")

# Check utm_source=customerio present
print("\n=== UTM counts ===")
for fn in sorted(files):
    path = os.path.join(DIR, fn)
    c = open(path, 'r', encoding='utf-8').read()
    cio = c.count('utm_source=customerio')
    print(f"  {fn}: {cio} urls with utm_source=customerio")

# Check no bare https:// without utm
print("\n=== URLs without UTM (should be 0 for https://) ===")
for fn in sorted(files):
    path = os.path.join(DIR, fn)
    c = open(path, 'r', encoding='utf-8').read()
    all_https = re.findall(r'https://[^\s"<>]+', c)
    no_utm = [u for u in all_https if 'utm_' not in u]
    if no_utm:
        print(f"  WARN {fn}: {len(no_utm)} URLs without UTM")
        for u in no_utm[:3]:
            print(f"    {u}")
    else:
        print(f"  {fn}: OK (all have UTM)")
