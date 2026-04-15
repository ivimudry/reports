# -*- coding: utf-8 -*-
"""Find exact Free Spins occurrences in Failed Deposit Email 4 rich_text."""
import os, sys, io, re
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
    if name == 'Email 4' and locale in ('hu-HU', 'pl-PL', 'Default'):
        rt = d.get('rich_text', '')
        # Find ALL occurrences of Free Spin (case insensitive)
        print(f"\n=== {name} | {locale} === (len={len(rt)})")
        for m in re.finditer(r'free spin', rt, re.IGNORECASE):
            start = max(0, m.start() - 80)
            end = min(len(rt), m.end() + 80)
            print(f"  pos {m.start()}: ...{rt[start:end]}...")
        
        # Also check for any other English terms left
        for term in ['Bonus', 'NoRisk', 'Free Bet', 'deposit', 'Gates of Olympus']:
            for m in re.finditer(re.escape(term), rt, re.IGNORECASE):
                if term.lower() == 'deposit' or term == 'Gates of Olympus':
                    start = max(0, m.start() - 60)
                    end = min(len(rt), m.end() + 60)
                    print(f"  '{term}' pos {m.start()}: ...{rt[start:end]}...")
