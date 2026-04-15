import os, re

DIR = r'c:\Projects\REPORTS\тексти\Celsius'
FILE = os.path.join(DIR, 'DEP Retention - Table data.txt')

text = open(FILE, 'r', encoding='utf-8').read()
blocks = text.strip().split('\n\n')

for b in blocks:
    lines = b.strip().split('\n')
    d = {}
    for line in lines:
        if ':' in line:
            k, v = line.split(':', 1)
            d[k.strip()] = v.strip()
    
    locale = d.get('locale', '')
    name = d.get('name', '')
    
    if locale in ('hu-HU', 'pl-PL'):
        print(f"=== {name} | {locale} ===")
        print(f"  subject: {d.get('subject','')}")
        print(f"  preheader: {d.get('preheader','')}")
        print(f"  button_text_1: {d.get('button_text_1','')}")
        
        # Extract p-content from text_1
        t1 = d.get('text_1', '')
        m1 = re.search(r'<strong>(.*?)</strong>', t1)
        if m1:
            print(f"  text_1 inner: {m1.group(1)}")
        
        # Extract p-content from text_2
        t2 = d.get('text_2', '')
        m2 = re.search(r'<p[^>]*>(.*?)</p>', t2, re.DOTALL)
        if m2:
            print(f"  text_2 inner: {m2.group(1)}")
        
        # Extract p-content from text_3
        t3 = d.get('text_3', '')
        m3 = re.search(r'<p[^>]*>(.*?)</p>', t3, re.DOTALL)
        if m3:
            print(f"  text_3 inner: {m3.group(1)}")
        
        print()
