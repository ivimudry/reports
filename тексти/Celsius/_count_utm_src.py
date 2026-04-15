# -*- coding: utf-8 -*-
"""
Count and show stats on UTM params in *_src fields, then show one full example URL.
Also check inside HTML body src= attributes.
"""
import re, os, sys, io
from collections import defaultdict
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

field_count = defaultdict(int)
inline_src_count = 0
total_src_fields = 0

# Show one full example per field type
examples = {}

for fname in FILES:
    fpath = os.path.join(BASE, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    content = content.replace('\r\n', '\n')
    
    for block in content.split('\n\n'):
        if not block.strip():
            continue
        lines = block.split('\n')
        d = {}
        for line in lines:
            idx = line.find(':')
            if idx > 0:
                d[line[:idx].strip()] = line[idx+1:].strip()
        
        for key, val in d.items():
            # Check _src fields with utm params
            if key.endswith('_src') and 'utm_' in val:
                field_count[key] += 1
                total_src_fields += 1
                if key not in examples:
                    examples[key] = val
            
            # Check src="..." inside HTML body fields
            if key in ('text_2', 'text_3', 'rich_text'):
                for m in re.finditer(r'src="([^"]*utm_[^"]*)"', val):
                    inline_src_count += 1

print("=== UTM on _src fields ===")
for k in sorted(field_count.keys()):
    print(f"  {k}: {field_count[k]} occurrences")
print(f"\nTotal _src fields with UTM: {total_src_fields}")
print(f"Inline src= in HTML body with UTM: {inline_src_count}")

print("\n=== Full example URLs ===")
for k, v in sorted(examples.items()):
    print(f"\n{k}:")
    print(f"  {v}")
    # Show what it would look like after stripping UTM
    utm_pos = v.find('?utm_')
    if utm_pos < 0:
        utm_pos = v.find('&utm_')
    if utm_pos >= 0:
        print(f"  -> CLEAN: {v[:utm_pos]}")
