# -*- coding: utf-8 -*-
"""Extract exact DEP Retention problematic fields for analysis."""
import re, os, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

filepath = r'c:\Projects\REPORTS\тексти\Celsius\DEP Retention - Table data.txt'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('\r\n', '\n')
raw_blocks = content.split('\n\n')

targets_hu = ['Email 1C', 'Email 1S', 'Email 2C', 'Email 2S', 'Email 4C', 'Email 5C', 'Email 5S',
              'Email 7C', 'Email 7S', 'Email 8C', 'Email 9C', 'Email 9S', 'Email 10C', 'Email 10S']
targets_pl = targets_hu

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
    
    name = d.get('name', '')
    locale = d.get('locale', '')
    
    if locale == 'hu-HU' and name in targets_hu:
        subj = d.get('subject', '')
        btn = d.get('button_text_1', '') or d.get('promocode_button_1', '')
        
        # Check subject for English terms
        has_issue = False
        for term in ['Free Spin', 'NoRisk', 'Free Bet', 'FreeBet']:
            if term.lower() in subj.lower():
                has_issue = True
        if 'Bonus' in subj and 'Bónusz' not in subj:
            has_issue = True
        
        if has_issue:
            print(f"\n=== {name} | {locale} ===")
            print(f"  subject: {subj}")
            if btn:
                print(f"  button: {btn}")
            
            # Check text_2 for terms
            t2 = d.get('text_2', '')
            for term in ['Free Spin', 'NoRisk', 'Free Bet', 'FreeBet']:
                if term.lower() in t2.lower():
                    # Extract 80 chars around the match
                    idx = t2.lower().find(term.lower())
                    start = max(0, idx - 40)
                    end = min(len(t2), idx + 60)
                    print(f"  text_2 has '{term}': ...{t2[start:end]}...")
                    break
            
            # Check text_3 for terms
            t3 = d.get('text_3', '')
            for term in ['Free Spin', 'NoRisk', 'Free Bet', 'FreeBet']:
                if term.lower() in t3.lower():
                    idx = t3.lower().find(term.lower())
                    start = max(0, idx - 40)
                    end = min(len(t3), idx + 60)
                    print(f"  text_3 has '{term}': ...{t3[start:end]}...")
                    break
    
    if locale == 'pl-PL' and name in targets_pl:
        subj = d.get('subject', '')
        btn = d.get('button_text_1', '') or d.get('promocode_button_1', '')
        
        has_issue = False
        for term in ['Free Spin', 'NoRisk', 'Free Bet', 'FreeBet']:
            if term.lower() in subj.lower():
                has_issue = True
        
        if has_issue:
            print(f"\n=== {name} | {locale} ===")
            print(f"  subject: {subj}")
            if btn:
                print(f"  button: {btn}")
            
            t2 = d.get('text_2', '')
            for term in ['Free Spin', 'NoRisk', 'Free Bet', 'FreeBet']:
                if term.lower() in t2.lower():
                    idx = t2.lower().find(term.lower())
                    start = max(0, idx - 40)
                    end = min(len(t2), idx + 60)
                    print(f"  text_2 has '{term}': ...{t2[start:end]}...")
                    break
            
            t3 = d.get('text_3', '')
            for term in ['Free Spin', 'NoRisk', 'Free Bet', 'FreeBet']:
                if term.lower() in t3.lower():
                    idx = t3.lower().find(term.lower())
                    start = max(0, idx - 40)
                    end = min(len(t3), idx + 60)
                    print(f"  text_3 has '{term}': ...{t3[start:end]}...")
                    break

# Also check Failed Deposit
print("\n\n=== FAILED DEPOSIT FLOW ===")
filepath2 = r'c:\Projects\REPORTS\тексти\Celsius\Failed Deposit Flow - Table data.txt'
with open(filepath2, 'r', encoding='utf-8') as f:
    content2 = f.read()
content2 = content2.replace('\r\n', '\n')
for rb in content2.split('\n\n'):
    if not rb.strip(): continue
    lines = rb.split('\n')
    d = {}
    for line in lines:
        idx = line.find(':')
        if idx > 0:
            d[line[:idx].strip()] = line[idx+1:].strip()
    name = d.get('name', '')
    locale = d.get('locale', '')
    if name == 'Email 4' and locale in ('hu-HU', 'pl-PL'):
        rt = d.get('rich_text', '')
        print(f"\n--- {name} | {locale} ---")
        # Find Free Spin context
        idx = rt.lower().find('free spin')
        if idx >= 0:
            start = max(0, idx - 60)
            end = min(len(rt), idx + 80)
            print(f"  rich_text has 'Free Spin': ...{rt[start:end]}...")
