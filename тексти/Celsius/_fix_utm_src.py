# -*- coding: utf-8 -*-
"""
Strip UTM parameters from all *_src fields (image source URLs).
UTM params should only be on href (link) fields, not on image sources.
"""
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

def strip_utm_from_url(url):
    """Remove UTM parameters from URL, keeping the base URL clean."""
    # Split at ? to get base and query
    if '?' not in url:
        return url
    base, query = url.split('?', 1)
    # Parse params, remove utm_*
    params = query.split('&')
    clean_params = [p for p in params if not p.startswith('utm_')]
    if clean_params:
        return base + '?' + '&'.join(clean_params)
    return base

total_fixed = 0

for fname in FILES:
    fpath = os.path.join(BASE, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    content = content.replace('\r\n', '\n')
    lines = content.split('\n')
    new_lines = []
    file_fixed = 0
    
    for line in lines:
        colon_idx = line.find(':')
        if colon_idx > 0:
            key = line[:colon_idx].strip()
            val = line[colon_idx+1:].strip()
            
            # Only fix *_src fields (image sources)
            if key.endswith('_src') and 'utm_' in val:
                clean_val = strip_utm_from_url(val)
                if clean_val != val:
                    # Preserve original spacing after colon
                    after_colon = line[colon_idx+1:]
                    spaces = len(after_colon) - len(after_colon.lstrip(' '))
                    new_line = f"{key}:{' ' * spaces}{clean_val}"
                    new_lines.append(new_line)
                    file_fixed += 1
                    continue
        
        new_lines.append(line)
    
    new_content = '\n'.join(new_lines)
    
    if new_content != content:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        total_fixed += file_fixed
        print(f"[{fname.split(' -')[0]}] Fixed {file_fixed} src fields")
    else:
        print(f"[{fname.split(' -')[0]}] No changes")

print(f"\nTotal src fields cleaned: {total_fixed}")
