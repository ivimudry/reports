import re, os, json

BASE = r"c:\Projects\REPORTS\тексти\Celsius"
FILES = [
    "Welcome Flow - Table data.txt",
    "DEP Retention - Table data.txt",
    "SU Retention - Table data.txt",
    "FTD Retention Flow - Table data.txt",
    "Nutrition #2 - Table data.txt",
    "Nutrition #3 - Table data.txt",
    "Failed Deposit Flow - Table data.txt",
]

def parse_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    blocks = []
    current_block = {}
    current_key = None
    
    for line in content.split('\n'):
        if line.strip() == '' and current_block:
            if 'name' in current_block and 'locale' in current_block:
                blocks.append(current_block)
            current_block = {}
            current_key = None
            continue
        
        m = re.match(r'^([\w_]+):\s*(.*)', line)
        if m:
            current_key = m.group(1)
            current_block[current_key] = m.group(2)
        elif current_key and line.strip():
            current_block[current_key] = current_block.get(current_key, '') + '\n' + line
    
    if current_block and 'name' in current_block and 'locale' in current_block:
        blocks.append(current_block)
    
    return blocks

def extract_p_inner(html):
    m = re.search(r'<p\s[^>]*>(.*)</p>', html, re.DOTALL)
    return m.group(1).strip() if m else ''

def extract_strong_inner(html):
    m = re.search(r'<strong>(.*?)</strong>', html, re.DOTALL)
    return m.group(1).strip() if m else ''

def extract_h2_strong_inner(html):
    m = re.search(r'<strong>(.*?)</strong>', html, re.DOTALL)
    return m.group(1).strip() if m else ''

import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

for fname in FILES:
    fpath = os.path.join(BASE, fname)
    if not os.path.exists(fpath):
        continue
    
    blocks = parse_file(fpath)
    defaults = {b['name']: b for b in blocks if b.get('locale') == 'Default'}
    
    print(f"\n\n{'#'*80}")
    print(f"# {fname}")
    print(f"# Default blocks: {len(defaults)}")
    print(f"{'#'*80}")
    
    for name in sorted(defaults.keys(), key=lambda x: (x.split()[1] if len(x.split())>1 else '', x)):
        d = defaults[name]
        subj = d.get('subject', '')
        preh = d.get('preheader', '')
        btn = d.get('button_text_1', '')
        
        t1 = d.get('text_1', '')
        t2 = d.get('text_2', '')
        t3 = d.get('text_3', '')
        rt = d.get('rich_text', '')
        
        greeting = extract_h2_strong_inner(t1)
        body = extract_p_inner(t2)
        
        # Check if text_3 is body or footer
        t3_is_body = t3 and 'Celsius Casino Team' not in t3 and "L'équipe" not in t3
        body3 = extract_p_inner(t3) if t3_is_body else ''
        
        print(f"\n--- {name} ---")
        print(f"S: {subj}")
        print(f"P: {preh}")
        print(f"B: {btn}")
        print(f"G: {greeting}")
        if body:
            # Show body with HTML tags visible but readable
            clean = body.replace('<br>', '\n').replace('<br><br>', '\n\n')
            clean = re.sub(r'<strong class="promocode">(.*?)</strong>', r'[PROMO:\1]', clean)
            clean = re.sub(r'<strong>(.*?)</strong>', r'**\1**', clean)
            clean = re.sub(r'<[^>]+>', '', clean)
            clean = re.sub(r'\s+', ' ', clean).strip()
            print(f"BODY: {clean[:300]}")
        if body3:
            clean3 = body3.replace('<br>', '\n')
            clean3 = re.sub(r'<strong class="promocode">(.*?)</strong>', r'[PROMO:\1]', clean3)
            clean3 = re.sub(r'<strong>(.*?)</strong>', r'**\1**', clean3)
            clean3 = re.sub(r'<[^>]+>', '', clean3)
            clean3 = re.sub(r'\s+', ' ', clean3).strip()
            print(f"BODY3: {clean3[:300]}")
        if rt:
            clean_rt = re.sub(r'<[^>]+>', '', rt)
            clean_rt = re.sub(r'\s+', ' ', clean_rt).strip()
            print(f"RICH: {clean_rt[:300]}")
