import os

folder = 'тексти/хейхо'
files = sorted([f for f in os.listdir(folder) if f.endswith('.txt') and 'Unsuccessful' not in f])
href_fields = ['button_href_1', 'button_href_2', 'logo_href', 'banner_href', 'monkey_href', 'bottom_logo_href']

for fname in files:
    short = fname.replace(' - Table data.txt', '')
    fp = os.path.join(folder, fname)
    with open(fp, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    filled = {}
    for line in lines:
        if ':' in line:
            key = line.split(':', 1)[0].strip()
            val = line.split(':', 1)[1].strip()
            if key in href_fields and val:
                filled[key] = filled.get(key, 0) + 1
    
    if filled:
        print(f'{short}: {filled}')
    else:
        print(f'{short}: all empty')
