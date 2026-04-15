import re
f = open(r'c:\Projects\REPORTS\тексти\Celsius\DEP Retention - Table data.txt', 'r', encoding='utf-8')
t = f.read()
f.close()
blocks = t.replace('\r\n', '\n').split('\n\n')

checks = [('Email 1C','hu-HU'), ('Email 8C','pl-PL'), ('Email 3C','hu-HU'), ('Email 8S','pl-PL'), ('Email 10S','hu-HU')]

for b in blocks:
    lines = b.split('\n')
    d = {}
    for l in lines:
        i = l.find(':')
        if i > 0:
            d[l[:i].strip()] = l[i+1:].strip()
    name = d.get('name', '')
    locale = d.get('locale', '')
    if (name, locale) in checks:
        print(f'=== {name} | {locale} ===')
        print(f'  subject: {d.get("subject", "?")}')
        print(f'  preheader: {d.get("preheader", "?")}')
        print(f'  button: {d.get("button_text_1", "?")}')
        m1 = re.search(r'<strong>(.*?)</strong>', d.get('text_1', ''))
        if m1:
            print(f'  text_1 greeting: {m1.group(1)}')
        m2 = re.search(r'<p[^>]*>(.*?)</p>', d.get('text_2', ''), re.DOTALL)
        if m2:
            print(f'  text_2 start: {m2.group(1)[:80]}...')
        m3 = re.search(r'<p[^>]*>(.*?)</p>', d.get('text_3', ''), re.DOTALL)
        if m3:
            print(f'  text_3 start: {m3.group(1)[:80]}...')
        print()
