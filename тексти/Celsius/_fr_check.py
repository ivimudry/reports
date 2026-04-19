import os, re, html

d = r'c:\Projects\REPORTS\тексти\Celsius'
files = sorted([f for f in os.listdir(d) if f.endswith('.txt') and 'Table data' in f])

# Collect fr-FR subjects and buttons to see terminology
for fname in files[:3]:  # check 3 files
    path = os.path.join(d, fname)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    blocks = content.strip().split('\n\n')
    print(f'\n=== {fname} (fr-FR samples) ===')
    count = 0
    for block in blocks:
        lines = block.strip().split('\n')
        data = {}
        for line in lines:
            idx = line.find(': ')
            if idx > 0:
                data[line[:idx].strip()] = line[idx+2:].strip()
        
        if data.get('locale') == 'fr-FR':
            name = data.get('name', '')
            subj = data.get('subject', '')
            btn = data.get('button_text_1', '')
            preh = data.get('preheader', '')
            print(f'  {name}')
            print(f'    subject: {subj}')
            print(f'    button:  {btn}')
            print(f'    prehead: {preh[:100]}')
            count += 1
            if count >= 5:
                break
