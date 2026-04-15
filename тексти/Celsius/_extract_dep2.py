import os, re

DIR = r'c:\Projects\REPORTS\тексти\Celsius'
FILE = os.path.join(DIR, 'DEP Retention - Table data.txt')
OUT = os.path.join(DIR, '_dep_extract.txt')

text = open(FILE, 'r', encoding='utf-8').read()
blocks = text.strip().split('\n\n')

lines_out = []
for b in blocks:
    blines = b.strip().split('\n')
    d = {}
    for line in blines:
        if ':' in line:
            k, v = line.split(':', 1)
            d[k.strip()] = v.strip()
    
    locale = d.get('locale', '')
    name = d.get('name', '')
    
    if locale in ('hu-HU', 'pl-PL'):
        lines_out.append(f"=== {name} | {locale} ===")
        lines_out.append(f"  subject: {d.get('subject','')}")
        lines_out.append(f"  preheader: {d.get('preheader','')}")
        lines_out.append(f"  button_text_1: {d.get('button_text_1','')}")
        
        t1 = d.get('text_1', '')
        m1 = re.search(r'<strong>(.*?)</strong>', t1)
        if m1:
            lines_out.append(f"  text_1 inner: {m1.group(1)}")
        
        t2 = d.get('text_2', '')
        m2 = re.search(r'<p[^>]*>(.*?)</p>', t2, re.DOTALL)
        if m2:
            lines_out.append(f"  text_2 p-content: {m2.group(1)}")
        
        t3 = d.get('text_3', '')
        m3 = re.search(r'<p[^>]*>(.*?)</p>', t3, re.DOTALL)
        if m3:
            lines_out.append(f"  text_3 p-content: {m3.group(1)}")
        
        lines_out.append("")

with open(OUT, 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines_out))

print(f"Written {len(lines_out)} lines to _dep_extract.txt")
