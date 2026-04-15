import os, re

DIR = r'c:\Projects\REPORTS\тексти\Celsius'
OUT = os.path.join(DIR, '_audit_result.txt')

def parse_blocks(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()
    text = text.replace('\r\n', '\n')
    raw_blocks = text.split('\n\n')
    blocks = []
    for rb in raw_blocks:
        if not rb.strip():
            continue
        d = {}
        for line in rb.split('\n'):
            idx = line.find(':')
            if idx > 0:
                key = line[:idx].strip()
                val = line[idx+1:].strip()
                d[key] = val
        if d.get('name'):
            blocks.append(d)
    return blocks

def extract_visible_text(html):
    t = re.sub(r'<[^>]+>', '', html)
    t = re.sub(r'\s+', ' ', t).strip()
    return t[:150]

out = open(OUT, 'w', encoding='utf-8')
def p(s=''):
    out.write(s + '\n')

files = sorted(f for f in os.listdir(DIR) if f.endswith('.txt') and not f.startswith('_'))

for fn in files:
    path = os.path.join(DIR, fn)
    blocks = parse_blocks(path)
    
    emails = {}
    for b in blocks:
        name = b.get('name', '?')
        locale = b.get('locale', '?')
        if name not in emails:
            emails[name] = {}
        emails[name][locale] = b
    
    p(f"\n{'='*80}")
    p(f"FILE: {fn}")
    p(f"Emails: {len(emails)} | Blocks: {len(blocks)}")
    p(f"Email names: {list(emails.keys())}")
    
    all_keys = set()
    for b in blocks:
        all_keys.update(b.keys())
    p(f"All fields: {sorted(all_keys)}")
    
    for ename in emails.keys():
        locales_data = emails[ename]
        default = locales_data.get('Default', {})
        hu = locales_data.get('hu-HU', {})
        pl = locales_data.get('pl-PL', {})
        
        if not hu and not pl:
            continue
            
        p(f"\n  --- {ename} ---")
        
        # Subject
        def_subj = default.get('subject', '')
        hu_subj = hu.get('subject', '')
        pl_subj = pl.get('subject', '')
        p(f"  subject EN: {def_subj}")
        p(f"  subject HU: {'[TR]' if hu_subj != def_subj else '[EN]'} {hu_subj}")
        p(f"  subject PL: {'[TR]' if pl_subj != def_subj else '[EN]'} {pl_subj}")
        
        # Preheader
        def_pre = default.get('preheader', '')
        hu_pre = hu.get('preheader', '')
        pl_pre = pl.get('preheader', '')
        if def_pre:
            p(f"  preheader EN: {def_pre}")
            p(f"  preheader HU: {'[TR]' if hu_pre != def_pre else '[EN]'} {hu_pre}")
            p(f"  preheader PL: {'[TR]' if pl_pre != def_pre else '[EN]'} {pl_pre}")
        
        # Text fields
        text_keys = sorted([k for k in default.keys() if k.startswith('text_') or k == 'rich_text'], 
                          key=lambda x: int(re.search(r'\d+', x).group()) if re.search(r'\d+', x) else 0)
        for key in text_keys:
            def_val = default.get(key, '')
            hu_val = hu.get(key, '')
            pl_val = pl.get(key, '')
            
            def_text = extract_visible_text(def_val)
            hu_text = extract_visible_text(hu_val)
            pl_text = extract_visible_text(pl_val)
            
            hu_tr = hu_text != def_text if hu_text else False
            pl_tr = pl_text != def_text if pl_text else False
            
            p(f"  {key} EN: {def_text}")
            p(f"  {key} HU: {'[TR]' if hu_tr else '[EN]'} {hu_text}")
            p(f"  {key} PL: {'[TR]' if pl_tr else '[EN]'} {pl_text}")
        
        # Button
        def_btn = default.get('button_text_1', '')
        hu_btn = hu.get('button_text_1', '')
        pl_btn = pl.get('button_text_1', '')
        if def_btn:
            p(f"  button EN: {def_btn}")
            p(f"  button HU: {'[TR]' if hu_btn != def_btn else '[EN]'} {hu_btn}")
            p(f"  button PL: {'[TR]' if pl_btn != def_btn else '[EN]'} {pl_btn}")
        
        # Default name check
        hu_str = str(hu)
        pl_str = str(pl)
        if 'default:"Player"' in hu_str or "default:'Player'" in hu_str:
            p(f"  !!! HU has default:\"Player\" (needs Jatekos)")
        if 'default:"Player"' in pl_str or "default:'Player'" in pl_str:
            p(f"  !!! PL has default:\"Player\" (needs Gracz)")
        if 'default:"friend"' in hu_str:
            p(f"  !!! HU has default:\"friend\"")
        if 'default:"friend"' in pl_str:
            p(f"  !!! PL has default:\"friend\"")

out.write("\n\nDONE\n")
out.close()
print("Audit complete. Written to _audit_result.txt")
