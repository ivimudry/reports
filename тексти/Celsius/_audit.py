import os, re, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

DIR = r'c:\Projects\REPORTS\тексти\Celsius'

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
    """Extract visible text from HTML for display"""
    t = re.sub(r'<[^>]+>', '', html)
    t = re.sub(r'\s+', ' ', t).strip()
    return t[:120]

files = sorted(f for f in os.listdir(DIR) if f.endswith('.txt') and not f.startswith('_'))

for fn in files:
    path = os.path.join(DIR, fn)
    blocks = parse_blocks(path)
    
    # Group by email name
    emails = {}
    for b in blocks:
        name = b.get('name', '?')
        locale = b.get('locale', '?')
        if name not in emails:
            emails[name] = {}
        emails[name][locale] = b
    
    print(f"\n{'='*80}")
    print(f"FILE: {fn}")
    print(f"Emails: {len(emails)} | Blocks: {len(blocks)}")
    print(f"Email names: {list(emails.keys())}")
    
    # Check what fields exist
    all_keys = set()
    for b in blocks:
        all_keys.update(b.keys())
    print(f"All fields: {sorted(all_keys)}")
    
    # For each email, check HU and PL translation status
    for ename in sorted(emails.keys()):
        locales = emails[ename]
        default = locales.get('Default', {})
        hu = locales.get('hu-HU', {})
        pl = locales.get('pl-PL', {})
        
        if not hu and not pl:
            continue
            
        print(f"\n  --- {ename} ---")
        
        # Check subject
        def_subj = default.get('subject', '')
        hu_subj = hu.get('subject', '')
        pl_subj = pl.get('subject', '')
        hu_subj_translated = hu_subj != def_subj if hu_subj else False
        pl_subj_translated = pl_subj != def_subj if pl_subj else False
        print(f"  subject EN: {def_subj}")
        print(f"  subject HU: {'[TRANSLATED]' if hu_subj_translated else '[ENGLISH]'} {hu_subj[:80]}")
        print(f"  subject PL: {'[TRANSLATED]' if pl_subj_translated else '[ENGLISH]'} {pl_subj[:80]}")
        
        # Check preheader
        def_pre = default.get('preheader', '')
        hu_pre = hu.get('preheader', '')
        pl_pre = pl.get('preheader', '')
        if def_pre:
            hu_pre_tr = hu_pre != def_pre if hu_pre else False
            pl_pre_tr = pl_pre != def_pre if pl_pre else False
            print(f"  preheader EN: {def_pre}")
            print(f"  preheader HU: {'[TRANSLATED]' if hu_pre_tr else '[ENGLISH]'} {hu_pre[:80]}")
            print(f"  preheader PL: {'[TRANSLATED]' if pl_pre_tr else '[ENGLISH]'} {pl_pre[:80]}")
        
        # Check text fields
        for key in sorted(default.keys()):
            if not key.startswith('text_') and key != 'rich_text':
                continue
            def_val = default.get(key, '')
            hu_val = hu.get(key, '')
            pl_val = pl.get(key, '')
            
            def_text = extract_visible_text(def_val)
            hu_text = extract_visible_text(hu_val)
            pl_text = extract_visible_text(pl_val)
            
            hu_tr = hu_text != def_text if hu_text else False
            pl_tr = pl_text != def_text if pl_text else False
            
            print(f"  {key} EN: {def_text}")
            print(f"  {key} HU: {'[TR]' if hu_tr else '[EN]'} {hu_text}")
            print(f"  {key} PL: {'[TR]' if pl_tr else '[EN]'} {pl_text}")
        
        # Check button
        def_btn = default.get('button_text_1', '')
        hu_btn = hu.get('button_text_1', '')
        pl_btn = pl.get('button_text_1', '')
        if def_btn:
            print(f"  button EN: {def_btn}")
            print(f"  button HU: {'[TR]' if hu_btn != def_btn else '[EN]'} {hu_btn}")
            print(f"  button PL: {'[TR]' if pl_btn != def_btn else '[EN]'} {pl_btn}")
        
        # Check default name
        if 'default:"Player"' in str(hu):
            print(f"  !!! HU still has default:\"Player\"")
        if 'default:"Player"' in str(pl):
            print(f"  !!! PL still has default:\"Player\"")

print("\n\nDONE")
