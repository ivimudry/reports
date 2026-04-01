import os

folder = 'тексти/хейхо'
files = sorted([f for f in os.listdir(folder) if f.endswith('.txt') and 'Unsuccessful' not in f])

# Collect unique button_text_1 and button_text_2 per file
for fname in files:
    short = fname.replace(' - Table data.txt', '')
    fp = os.path.join(folder, fname)
    with open(fp, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    texts1 = set()
    texts2 = set()
    for line in lines:
        if ':' in line:
            key = line.split(':', 1)[0].strip()
            val = line.split(':', 1)[1].strip()
            if key == 'button_text_1' and val:
                texts1.add(val)
            elif key == 'button_text_2' and val:
                texts2.add(val)
    
    print(f'{short}:')
    print(f'  btn1: {texts1}')
    print(f'  btn2: {texts2}')
