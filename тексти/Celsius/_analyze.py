import os, re

DIR = r'c:\Projects\REPORTS\тексти\Celsius'
FIELDS_TO_TRANSLATE = ['subject', 'preheader', 'text_1', 'text_2', 'text_3', 'text_4', 'button_text_1']

files = sorted(f for f in os.listdir(DIR) if f.endswith('.txt'))

total_emails = 0
total_fields = 0

for fn in files:
    path = os.path.join(DIR, fn)
    lines = open(path, 'r', encoding='utf-8').readlines()
    
    # Parse into blocks
    blocks = []
    current = {}
    for line in lines:
        line = line.rstrip('\n')
        if not line.strip():
            if current:
                blocks.append(current)
                current = {}
            continue
        if ':' in line:
            key, val = line.split(':', 1)
            current[key.strip()] = val.strip()
    if current:
        blocks.append(current)
    
    # Group by email name
    emails = {}
    for b in blocks:
        name = b.get('name', '?')
        locale = b.get('locale', '?')
        if name not in emails:
            emails[name] = {}
        emails[name][locale] = b
    
    print(f"\n{'='*60}")
    print(f"FILE: {fn}")
    print(f"Emails: {len(emails)}")
    
    for ename, locales in emails.items():
        default_block = locales.get('Default', {})
        hu_block = locales.get('hu-HU', {})
        pl_block = locales.get('pl-PL', {})
        
        if not hu_block and not pl_block:
            continue
            
        total_emails += 1
        
        print(f"\n  [{ename}]")
        
        # Check which fields are in the file
        has_rich_text = 'rich_text' in default_block
        
        if has_rich_text:
            # Failed Deposit uses rich_text instead of text_1/2/3
            fields = ['subject', 'preheader', 'rich_text', 'text_1', 'text_2', 'text_3', 'text_4', 'button_text_1']
        else:
            fields = FIELDS_TO_TRANSLATE
        
        for field in fields:
            en_val = default_block.get(field, '')
            hu_val = hu_block.get(field, '') if hu_block else ''
            pl_val = pl_block.get(field, '') if pl_block else ''
            
            if not en_val:
                continue
            
            # Extract just the visible text for display
            text_only = re.sub(r'<[^>]+>', '', en_val)
            text_only = re.sub(r'\{\{[^}]+\}\}', '{{...}}', text_only)
            
            # Check if HU/PL still match English (untranslated)
            hu_needs = (hu_val == en_val) if hu_val else False
            pl_needs = (pl_val == en_val) if pl_val else False
            
            hu_status = "❌ EN" if hu_needs else ("✅ HU" if hu_val else "⚪ missing")
            pl_status = "❌ EN" if pl_needs else ("✅ PL" if pl_val else "⚪ missing")
            
            # Special check: is it French instead of target?
            hu_is_french = "L'équipe" in hu_val or "Ceci est" in hu_val if hu_val else False
            pl_is_french = "L'équipe" in pl_val or "Ceci est" in pl_val if pl_val else False
            
            if hu_is_french:
                hu_status = "❌ FR!"
            if pl_is_french:
                pl_status = "❌ FR!"
            
            if hu_needs or pl_needs or hu_is_french or pl_is_french:
                total_fields += 1
                short = text_only[:80] + ('...' if len(text_only) > 80 else '')
                print(f"    {field}: HU={hu_status} PL={pl_status}")
                print(f"      EN: {short}")

print(f"\n{'='*60}")
print(f"TOTAL: {total_emails} emails need work, {total_fields} field groups to translate")
