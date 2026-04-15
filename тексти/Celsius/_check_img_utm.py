# -*- coding: utf-8 -*-
"""Find UTM parameters on image src URLs (should only be on href links)."""
import re, os, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

BASE = r'c:\Projects\REPORTS\тексти\Celsius'
FILES = [
    'DEP Retention - Table data.txt',
    'FTD Retention Flow - Table data.txt',
    'Failed Deposit Flow - Table data.txt',
    'Nutrition #2 - Table data.txt',
    'Nutrition #3 - Table data.txt',
    'SU Retention - Table data.txt',
    'Welcome Flow - Table data.txt',
]

total = 0

for fname in FILES:
    fpath = os.path.join(BASE, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = content.replace('\r\n', '\n')
    blocks = content.split('\n\n')
    
    for block in blocks:
        if not block.strip():
            continue
        lines = block.split('\n')
        d = {}
        for line in lines:
            idx = line.find(':')
            if idx > 0:
                d[line[:idx].strip()] = line[idx+1:].strip()
        
        name = d.get('name', '')
        locale = d.get('locale', '')
        
        for key, val in d.items():
            # Find src="..." with utm params
            for m in re.finditer(r'src="([^"]*utm_[^"]*)"', val):
                url = m.group(1)
                total += 1
                if total <= 30:
                    print(f"[{fname.split(' -')[0]}] {name} | {locale} | {key}")
                    print(f"  src: {url[:120]}...")
                    print()
            
            # Also check image_href / image_src type fields
            if ('image' in key.lower() or 'src' in key.lower() or 'img' in key.lower()) and 'utm_' in val:
                if 'href' not in key.lower():
                    total += 1
                    if total <= 50:
                        print(f"[{fname.split(' -')[0]}] {name} | {locale} | FIELD: {key}")
                        print(f"  val: {val[:150]}")
                        print()

print(f"\nTotal image URLs with UTM params: {total}")
