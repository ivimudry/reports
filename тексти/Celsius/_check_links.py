# -*- coding: utf-8 -*-
"""Check FR-LINK differences - show actual FR vs Default URLs."""
import os, sys, io
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

def parse_blocks(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    content = content.replace('\r\n', '\n')
    raw_blocks = content.split('\n\n')
    blocks = []
    for rb in raw_blocks:
        if not rb.strip(): continue
        lines = rb.split('\n')
        d = {}
        for line in lines:
            idx = line.find(':')
            if idx > 0:
                key = line[:idx].strip()
                val = line[idx+1:].strip()
                d[key] = val
        if d.get('name') and d.get('locale'):
            blocks.append(d)
    return blocks

# Just show first few FR-LINK differences per file
for fname in FILES:
    filepath = os.path.join(BASE, fname)
    blocks = parse_blocks(filepath)
    short = fname.replace(' - Table data.txt', '')
    emails = {}
    for b in blocks:
        name = b['name']
        if name not in emails: emails[name] = {}
        emails[name][b['locale']] = b

    shown = 0
    for ename in sorted(emails.keys()):
        if shown >= 3: break
        if 'fr-FR' in emails[ename] and 'Default' in emails[ename]:
            fr_href = emails[ename]['fr-FR'].get('button_href_1', '')
            def_href = emails[ename]['Default'].get('button_href_1', '')
            if fr_href != def_href:
                print(f"\n--- {short} | {ename} ---")
                print(f"  Default: {def_href[:150]}")
                print(f"  fr-FR:   {fr_href[:150]}")
                shown += 1

# Also check HU/PL links vs Default
print("\n\n=== HU/PL LINK CHECK (first 3 per file) ===")
for fname in FILES:
    filepath = os.path.join(BASE, fname)
    blocks = parse_blocks(filepath)
    short = fname.replace(' - Table data.txt', '')
    emails = {}
    for b in blocks:
        name = b['name']
        if name not in emails: emails[name] = {}
        emails[name][b['locale']] = b
    
    shown = 0
    for ename in sorted(emails.keys()):
        if shown >= 3: break
        if 'hu-HU' in emails[ename] and 'Default' in emails[ename]:
            hu_href = emails[ename]['hu-HU'].get('button_href_1', '')
            def_href = emails[ename]['Default'].get('button_href_1', '')
            if hu_href != def_href:
                print(f"\n--- {short} | {ename} (HU vs Default) ---")
                print(f"  Default: {def_href[:150]}")
                print(f"  hu-HU:   {hu_href[:150]}")
                shown += 1
            elif hu_href == def_href and hu_href:
                print(f"\n--- {short} | {ename} (HU = Default) ---")
                print(f"  Same: {hu_href[:120]}")
                shown += 1
