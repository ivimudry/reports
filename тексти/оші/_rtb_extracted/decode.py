import json, zlib, struct

base = r'c:\Projects\REPORTS\тексти\оші\_rtb_extracted'

for fname in ['canvas.json', 'tables.json']:
    data = open(f'{base}\\{fname}', 'rb').read()
    print(f'=== {fname} === size={len(data)}')
    print('First 32 bytes:', list(data[:32]))
    
    # Try skipping various header sizes then zlib
    for skip in [0, 1, 2, 4, 8, 16]:
        for wbits in [-15, 15, 31, -9, 9]:
            try:
                d = zlib.decompress(data[skip:], wbits)
                print(f'  zlib OK (skip={skip}, wbits={wbits}), len={len(d)}')
                text = d.decode('utf-8', errors='replace')
                print(f'  Content: {text[:300]}')
                break
            except Exception:
                pass
    print()
