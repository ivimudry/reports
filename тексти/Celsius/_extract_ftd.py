import re
f = open(r'c:\Projects\REPORTS\тексти\Celsius\FTD Retention Flow - Table data.txt', 'r', encoding='utf-8')
t = f.read()
f.close()
blocks = t.replace('\r\n', '\n').split('\n\n')

# First pass: list all unique emails
emails_seen = set()
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
        emails_seen.add(name)

print(f"Unique emails: {len(emails_seen)}")
for e in sorted(emails_seen):
    print(f"  {e}")

print("\n--- HU/PL translatable content ---\n")

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
        print(f"=== {name} | Default ===")
        print(f"  subject: {d.get('subject', '?')}")
        print(f"  preheader: {d.get('preheader', '?')}")
        m1 = re.search(r'<strong>(.*?)</strong>', d.get('text_1', ''), re.DOTALL)
        if m1:
            print(f"  text_1 greeting: {m1.group(1).strip()}")
        m2 = re.search(r'<p[^>]*>(.*?)</p>', d.get('text_2', ''), re.DOTALL)
        if m2:
            print(f"  text_2 body: {m2.group(1)[:200]}...")
        print(f"  button: {d.get('button_text_1', '?')}")
        print()
