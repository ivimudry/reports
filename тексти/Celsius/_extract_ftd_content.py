import os, re

filepath = r'c:\Projects\REPORTS\тексти\Celsius\FTD Retention Flow - Table data.txt'
outpath = r'c:\Projects\REPORTS\тексти\Celsius\_ftd_to_translate.txt'

with open(filepath, 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace('\r\n', '\n')
raw_blocks = text.split('\n\n')
blocks = []
for rb in raw_blocks:
    if not rb.strip():
        continue
    d = {}
    for line in rb.split('\n'):
        idx = line.find(':')
        if idx > 0:
            key = line[:idx].strip()
            val = line[idx+1:].strip()
            d[key] = val
    if d.get('name'):
        blocks.append(d)

def extract_text(html):
    t = re.sub(r'<[^>]+>', '', html)
    t = re.sub(r'&nbsp;', ' ', t)
    t = re.sub(r'\s+', ' ', t).strip()
    return t

out = open(outpath, 'w', encoding='utf-8')

# Group by name
emails = {}
for b in blocks:
    name = b.get('name', '?')
    locale = b.get('locale', '?')
    if name not in emails:
        emails[name] = {}
    emails[name][locale] = b

for ename in emails.keys():
    locales = emails[ename]
    default = locales.get('Default', {})
    hu = locales.get('hu-HU', {})
    
    if not default:
        continue
    
    out.write(f"\n=== {ename} ===\n")
    out.write(f"subject: {default.get('subject', '')}\n")
    out.write(f"preheader: {default.get('preheader', '')}\n")
    
    t1 = default.get('text_1', '')
    t1_text = extract_text(t1)
    out.write(f"text_1 visible: {t1_text}\n")
    
    t2 = default.get('text_2', '')
    t2_text = extract_text(t2)
    out.write(f"text_2 visible: {t2_text}\n")
    
    btn = default.get('button_text_1', '')
    out.write(f"button: {btn}\n")
    
    # Check if default name
    if 'default:' in t1:
        m = re.search(r'default:"([^"]+)"', t1)
        if m:
            out.write(f"default_name: {m.group(1)}\n")

out.close()
print(f"Extracted {len(emails)} emails to _ftd_to_translate.txt")
