# -*- coding: utf-8 -*-
import re, os, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

files = [
    'Failed Deposit Flow - Table data.txt',
    'Nutrition #2 - Table data.txt',
    'Nutrition #3 - Table data.txt',
    'SU Retention - Table data.txt',
    'Welcome Flow - Table data.txt',
]

base = r'c:\Projects\REPORTS\тексти\Celsius'
out = os.path.join(base, '_all_extract.txt')

with open(out, 'w', encoding='utf-8') as f:
    for fname in files:
        fpath = os.path.join(base, fname)
        with open(fpath, 'r', encoding='utf-8') as src:
            content = src.read().replace('\r\n', '\n')
        
        blocks = content.split('\n\n')
        f.write(f"{'='*80}\n")
        f.write(f"FILE: {fname}\n")
        f.write(f"Total blocks: {len([b for b in blocks if b.strip()])}\n")
        
        # Collect unique email names and their fields
        emails = {}
        for block in blocks:
            if not block.strip():
                continue
            lines = block.split('\n')
            d = {}
            for line in lines:
                idx = line.find(':')
                if idx > 0:
                    key = line[:idx].strip()
                    val = line[idx+1:].strip()
                    d[key] = val
            name = d.get('name', '?')
            locale = d.get('locale', '?')
            if name not in emails:
                emails[name] = {}
            emails[name][locale] = d
        
        f.write(f"Unique emails: {len(emails)}\n")
        f.write(f"Email names: {list(emails.keys())}\n\n")
        
        for ename, locales in emails.items():
            f.write(f"\n--- {ename} ---\n")
            f.write(f"  Locales: {list(locales.keys())}\n")
            
            # Show Default fields
            default = locales.get('Default', {})
            f.write(f"  Fields: {list(default.keys())}\n")
            
            # Show subject, preheader, button_text_1 for Default
            f.write(f"  subject: {default.get('subject', 'N/A')}\n")
            f.write(f"  preheader: {default.get('preheader', 'N/A')}\n")
            f.write(f"  button_text_1: {default.get('button_text_1', 'N/A')}\n")
            
            # Extract text of text_1 or greeting
            text1 = default.get('text_1', '')
            if text1:
                # Extract text from within strong tags
                m = re.search(r'<strong[^>]*>(.*?)</strong>', text1)
                if m:
                    f.write(f"  text_1 greeting: {m.group(1)}\n")
            
            # Extract text_2 body inner content
            text2 = default.get('text_2', '')
            if text2:
                m = re.search(r'<p[^>]*>(.*)</p>', text2, re.DOTALL)
                if m:
                    inner = m.group(1).strip()
                    f.write(f"  text_2 body: {inner}\n")
            
            # For Failed Deposit, show rich_text visible text
            rich = default.get('rich_text', '')
            if rich:
                # Strip HTML and show plain text
                plain = re.sub(r'<[^>]+>', ' ', rich)
                plain = re.sub(r'\s+', ' ', plain).strip()
                f.write(f"  rich_text (plain): {plain}\n")
            
            # Check hu-HU status
            hu = locales.get('hu-HU', {})
            if hu:
                hu_subj = hu.get('subject', '')
                def_subj = default.get('subject', '')
                if hu_subj == def_subj:
                    f.write(f"  hu-HU: NOT TRANSLATED (subject same as Default)\n")
                else:
                    f.write(f"  hu-HU: subject={hu_subj}\n")
            
            pl = locales.get('pl-PL', {})
            if pl:
                pl_subj = pl.get('subject', '')
                def_subj = default.get('subject', '')
                if pl_subj == def_subj:
                    f.write(f"  pl-PL: NOT TRANSLATED (subject same as Default)\n")
                else:
                    f.write(f"  pl-PL: subject={pl_subj}\n")
        
        f.write(f"\n\n")

print(f"Written to {out}")
