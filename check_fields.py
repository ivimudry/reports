import os

folder = 'тексти/хейхо'
files = sorted([f for f in os.listdir(folder) if f.endswith('.txt') and 'Unsuccessful' not in f])
all_href = ['button_href_1', 'button_href_2', 'logo_href', 'banner_href', 'monkey_href', 'logo_botom_href', 'bottom_logo_href']

for fname in files:
    short = fname.replace(' - Table data.txt', '')
    fp = os.path.join(folder, fname)
    with open(fp, 'r', encoding='utf-8') as f:
        content = f.read()
    
    present = [h for h in all_href if f'\n{h}:' in content or content.startswith(f'{h}:')]
    count = {h: content.count(f'{h}:') for h in present}
    print(f'{short}: {count}')
