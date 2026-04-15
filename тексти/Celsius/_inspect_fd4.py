# -*- coding: utf-8 -*-
"""Extract full rich_text for Failed Deposit Email 4 + check what other campaigns have."""
import os, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

filepath = r'c:\Projects\REPORTS\тексти\Celsius\Failed Deposit Flow - Table data.txt'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('\r\n', '\n')
raw_blocks = content.split('\n\n')

for rb in raw_blocks:
    if not rb.strip(): continue
    lines = rb.split('\n')
    d = {}
    for line in lines:
        idx = line.find(':')
        if idx > 0:
            d[line[:idx].strip()] = line[idx+1:].strip()
    name = d.get('name', '')
    locale = d.get('locale', '')
    if name == 'Email 4':
        rt = d.get('rich_text', '')
        print(f"\n=== {name} | {locale} ===")
        print(f"  rich_text length: {len(rt)}")
        print(f"  rich_text:\n{rt[:500]}")
        if len(rt) > 500:
            print(f"  ...({len(rt)} total chars)")
        
        # Also show Default for comparison
        subj = d.get('subject', '')
        preh = d.get('preheader', '')
        print(f"  subject: {subj}")
        print(f"  preheader: {preh}")
