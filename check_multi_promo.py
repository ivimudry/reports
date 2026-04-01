import os, re

folder = 'тексти/хейхо'
files = sorted([f for f in os.listdir(folder) if f.endswith('.txt') and 'Unsuccessful' not in f])

# Check for any promo-related fields beyond promocode_button_1
for fname in files:
    short = fname.replace(' - Table data.txt', '')
    fp = os.path.join(folder, fname)
    with open(fp, 'r', encoding='utf-8') as f:
        for line in f:
            if ':' in line:
                key = line.split(':', 1)[0].strip()
                if 'promo' in key.lower() and key != 'promocode_button_1':
                    val = line.split(':', 1)[1].strip()
                    print(f'{short}: {key} = {val}')
                    break

print('\nDone - any other promo fields shown above')
