import re
f = open(r'c:\Projects\REPORTS\тексти\Celsius\FTD Retention Flow - Table data.txt', 'r', encoding='utf-8')
t = f.read()
f.close()
blocks = t.replace('\r\n', '\n').split('\n\n')

for b in blocks:
    lines = b.split('\n')
    d = {}
    for l in lines:
        i = l.find(':')
        if i > 0:
            d[l[:i].strip()] = l[i+1:].strip()
    name = d.get('name', '')
    locale = d.get('locale', '')
    if locale == 'Default' and name:
        print(f"=== {name} ===")
        m2 = re.search(r'<p[^>]*>(.*?)</p>', d.get('text_2', ''), re.DOTALL)
        if m2:
            print(f"TEXT2: {m2.group(1)}")
        print()
