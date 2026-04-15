import re

filepath = r'c:\Projects\REPORTS\тексти\Celsius\FTD Retention Flow - Table data.txt'
outpath = r'c:\Projects\REPORTS\тексти\Celsius\_ftd_html.txt'

with open(filepath, 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace('\r\n', '\n')
blocks = text.split('\n\n')

out = open(outpath, 'w', encoding='utf-8')

for b in blocks:
    if not b.strip():
        continue
    d = {}
    for line in b.split('\n'):
        idx = line.find(':')
        if idx > 0:
            d[line[:idx].strip()] = line[idx+1:].strip()
    
    if d.get('locale') == 'Default':
        name = d.get('name', '')
        t2 = d.get('text_2', '')
        m = re.match(r'(.*?<p[^>]*>)(.*)(</p></td>)', t2, re.DOTALL)
        if m:
            body = m.group(2)
            out.write(f"\n=== {name} ===\n")
            out.write(body + '\n')

out.close()
print("Done")
