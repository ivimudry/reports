import os

folder = 'тексти/хейхо'
files = sorted([f for f in os.listdir(folder) if f.endswith('.txt') and 'Unsuccessful' not in f])

for fname in files:
    short = fname.replace(' - Table data.txt', '')
    fp = os.path.join(folder, fname)
    with open(fp, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    blocks = []
    current = {}
    for line in lines:
        if ':' in line:
            key = line.split(':', 1)[0].strip()
            val = line.split(':', 1)[1].strip()
            if key == 'name':
                if current:
                    blocks.append(current)
                current = {'name': val, 'promos': {}}
            elif key == 'locale':
                current['locale'] = val
            elif 'promocode' in key.lower() or 'promo' in key.lower():
                if key in current['promos']:
                    current['promos'][key].append(val)
                else:
                    current['promos'][key] = [val]
    if current:
        blocks.append(current)
    
    print(f'\n=== {short} ===')
    for b in blocks:
        if b.get('locale', '') == 'Default':
            promos = b.get('promos', {})
            if promos:
                # Count non-empty promo values
                all_vals = []
                for k, vals in promos.items():
                    for v in vals:
                        if v:
                            all_vals.append(f'{k}={v}')
                if all_vals:
                    print(f"  {b['name']}: {', '.join(all_vals)}")
                else:
                    print(f"  {b['name']}: promo fields exist but EMPTY")
            else:
                print(f"  {b['name']}: NO PROMO FIELDS")
