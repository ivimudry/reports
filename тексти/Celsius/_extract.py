import os, re, json

DIR = r'c:\Projects\REPORTS\тексти\Celsius'
OUTPUT = r'c:\Projects\REPORTS\тексти\Celsius\_texts_to_translate.json'

def parse_file(path):
    lines = open(path, 'r', encoding='utf-8').readlines()
    blocks = []
    current = {}
    current_key = None
    for line in lines:
        raw = line.rstrip('\n')
        if not raw.strip():
            if current:
                blocks.append(current)
                current = {}
                current_key = None
            continue
        # Detect field: key starts at line beginning, contains ':'
        m = re.match(r'^([a-z_][a-z0-9_]*)\s*:\s*(.*)', raw)
        if m:
            current_key = m.group(1)
            current[current_key] = m.group(2)
        elif current_key:
            current[current_key] += '\n' + raw
    if current:
        blocks.append(current)
    return blocks

def strip_html(s):
    s = re.sub(r'<[^>]+>', '', s)
    s = re.sub(r'\{\{[^}]+\}\}', '{{...}}', s)
    s = s.replace('&nbsp;', ' ').replace('&amp;', '&')
    return s.strip()

files = sorted(f for f in os.listdir(DIR) if f.endswith('.txt') and not f.startswith('_'))

result = {}
for fn in files:
    blocks = parse_file(os.path.join(DIR, fn))
    
    # Group by email name
    emails = {}
    for b in blocks:
        name = b.get('name', '?')
        locale = b.get('locale', '?')
        if name not in emails:
            emails[name] = {}
        emails[name][locale] = b
    
    file_data = []
    for ename, locales in emails.items():
        default_b = locales.get('Default', {})
        hu_b = locales.get('hu-HU', {})
        pl_b = locales.get('pl-PL', {})
        
        if not default_b:
            continue
        
        # Determine which fields need translation
        translate_fields = []
        for field in ['subject', 'preheader', 'text_1', 'text_2', 'text_3', 'rich_text', 'button_text_1']:
            en_val = default_b.get(field, '')
            if not en_val:
                continue
            hu_val = hu_b.get(field, '')
            pl_val = pl_b.get(field, '')
            hu_needs = (hu_val == en_val) if hu_val else False
            pl_needs = (pl_val == en_val) if pl_val else False
            if hu_needs or pl_needs:
                translate_fields.append({
                    'field': field,
                    'en_text': strip_html(en_val),
                    'hu_needs': hu_needs,
                    'pl_needs': pl_needs
                })
        
        # Check team sig field (text_4 in DEP, text_3 in others)
        for field in ['text_3', 'text_4']:
            en_val = default_b.get(field, '')
            hu_val = hu_b.get(field, '')
            if not en_val:
                continue
            is_team_sig = 'Team.' in en_val or 'automated message' in en_val
            is_french_in_hu = "L'équipe" in hu_val or "Ceci est" in hu_val
            is_french_in_pl = "L'équipe" in (pl_b.get(field, '')) or "Ceci est" in (pl_b.get(field, ''))
            if is_team_sig and (is_french_in_hu or is_french_in_pl):
                translate_fields.append({
                    'field': field + ' (TEAM SIG - currently FR!)',
                    'en_text': strip_html(en_val),
                    'hu_needs': is_french_in_hu,
                    'pl_needs': is_french_in_pl
                })
        
        if translate_fields:
            file_data.append({
                'email': ename,
                'fields': translate_fields
            })
    
    result[fn] = file_data

# Save
with open(OUTPUT, 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=2)

# Print summary
total = 0
for fn, emails in result.items():
    count = sum(len(e['fields']) for e in emails)
    total += count
    print(f"{fn}: {len(emails)} emails, {count} field-groups needing translation")
print(f"\nTotal: {total} field-groups (×2 languages = {total*2} translations)")
