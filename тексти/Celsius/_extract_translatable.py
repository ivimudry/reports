"""Extract all translatable English content from Celsius files for hu-HU and pl-PL locales."""
import os, re

DIR = r'c:\Projects\REPORTS\тексти\Celsius'
FILES = sorted(f for f in os.listdir(DIR) if f.endswith('.txt'))

def parse_file(path):
    blocks = []
    current = {}
    for line in open(path, 'r', encoding='utf-8'):
        line = line.rstrip('\n')
        if not line.strip():
            if current:
                blocks.append(current)
                current = {}
            continue
        idx = line.find(':')
        if idx > 0:
            key = line[:idx].strip()
            val = line[idx+1:].strip()
            current[key] = val
    if current:
        blocks.append(current)
    return blocks

def extract_text(html):
    """Extract visible text from HTML td cell."""
    text = re.sub(r'<[^>]+>', '', html)
    text = text.replace('&nbsp;', ' ').replace('&amp;', '&')
    text = re.sub(r'\s+', ' ', text).strip()
    return text

# Fields that need translation in hu-HU and pl-PL
TRANSLATABLE = ['subject', 'preheader', 'text_1', 'text_2', 'text_3', 'button_text_1', 'rich_text']

for fn in FILES:
    path = os.path.join(DIR, fn)
    blocks = parse_file(path)
    
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
    print(f"{'='*80}")
    print(f"Emails: {list(emails.keys())}")
    
    for email_name, locales in emails.items():
        default = locales.get('Default', {})
        hu = locales.get('hu-HU', {})
        pl = locales.get('pl-PL', {})
        
        if not hu and not pl:
            continue
        
        print(f"\n--- {email_name} ---")
        
        for field in TRANSLATABLE:
            en_val = default.get(field, '')
            hu_val = hu.get(field, '') if hu else ''
            pl_val = pl.get(field, '') if pl else ''
            
            if not en_val:
                continue
            
            # Check if hu/pl still equals English (needs translation)
            hu_needs = (hu_val == en_val) if hu_val else False
            pl_needs = (pl_val == en_val) if pl_val else False
            
            if hu_needs or pl_needs:
                en_text = extract_text(en_val) if field.startswith('text_') or field == 'rich_text' else en_val
                print(f"  {field}:")
                print(f"    EN: {en_text[:200]}")
                if hu_needs:
                    print(f"    HU: NEEDS TRANSLATION")
                if pl_needs:
                    print(f"    PL: NEEDS TRANSLATION")

print(f"\n\nDone.")
