import os, re, html, random

def strip_html(s):
    s = re.sub(r'<br\s*/?>', '\n', s)
    s = re.sub(r'<[^>]+>', '', s)
    s = html.unescape(s)
    return s.strip()

d = r'c:\Projects\REPORTS\тексти\Celsius'
files = sorted([f for f in os.listdir(d) if f.endswith('.txt') and 'Table data' in f])

# For each file, pick 2 random emails and show Default vs hu-HU vs pl-PL for text_2, subject, button
random.seed(42)

for fname in files:
    path = os.path.join(d, fname)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    blocks = content.strip().split('\n\n')
    emails = {}
    
    for block in blocks:
        lines = block.strip().split('\n')
        data = {}
        for line in lines:
            idx = line.find(': ')
            if idx > 0:
                data[line[:idx].strip()] = line[idx+2:].strip()
        name = data.get('name', '')
        locale = data.get('locale', '')
        if name and locale:
            emails.setdefault(name, {})[locale] = data
    
    print(f'\n{"="*70}')
    print(f'  {fname}')
    print(f'{"="*70}')
    
    names = sorted(emails.keys())
    # Pick first, middle, and last email
    picks = [names[0], names[len(names)//2], names[-1]]
    
    for ename in picks:
        locales = emails[ename]
        print(f'\n  --- {ename} ---')
        
        for loc in ['Default', 'hu-HU', 'pl-PL']:
            d2 = locales.get(loc, {})
            subj = d2.get('subject', 'N/A')
            preh = d2.get('preheader', 'N/A')
            t1 = strip_html(d2.get('text_1', 'N/A'))
            t2 = strip_html(d2.get('text_2', 'N/A'))
            t3 = strip_html(d2.get('text_3', 'N/A'))
            btn = d2.get('button_text_1', 'N/A')
            t12 = strip_html(d2.get('text_12', 'N/A'))
            
            print(f'    [{loc}]')
            print(f'      subject:  {subj[:90]}')
            print(f'      prehdr:   {preh[:90]}')
            print(f'      text_1:   {t1[:90]}')
            print(f'      text_2:   {t2[:150]}')
            print(f'      text_3:   {t3[:90]}')
            print(f'      button:   {btn}')
            print(f'      text_12:  {t12[:100]}')
