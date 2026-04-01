import os, re, json

folder = 'тексти/хейхо'
files = sorted([f for f in os.listdir(folder) if f.endswith('.txt') and 'Unsuccessful' not in f])

HREF_FIELDS = {'button_href_1', 'button_href_2', 'logo_href', 'banner_href',
               'monkey_href', 'bottom_logo_href', 'logo_botom_href'}

errors = []
stats = {}

for fname in files:
    short = fname.replace(' - Table data.txt', '')
    fp = os.path.join(folder, fname)
    with open(fp, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    current_name = ''
    current_locale = ''
    current_promo = ''
    file_urls = []
    empty_hrefs = 0
    
    for line in lines:
        if ':' in line:
            key = line.split(':', 1)[0].strip()
            val = line.split(':', 1)[1].strip()
            
            if key == 'name':
                current_name = val
            elif key == 'locale':
                current_locale = val
            elif key == 'promocode_button_1':
                current_promo = val
            elif key in HREF_FIELDS:
                if not val:
                    empty_hrefs += 1
                    errors.append(f'{short}/{current_name}/{current_locale}: {key} is EMPTY')
                else:
                    file_urls.append({
                        'file': short,
                        'email': current_name,
                        'locale': current_locale,
                        'field': key,
                        'url': val,
                        'promo': current_promo,
                    })
    
    stats[short] = {'filled': len(file_urls), 'empty': empty_hrefs}
    
    # Validate URLs in this file
    for u in file_urls:
        url = u['url']
        # Check base structure
        if not url.startswith('https://heyhocasino.com/'):
            errors.append(f"{u['file']}/{u['email']}/{u['locale']}/{u['field']}: bad base URL")
        
        # Check token
        if '?token={{customer.auth_token}}' not in url:
            errors.append(f"{u['file']}/{u['email']}/{u['locale']}/{u['field']}: missing auth_token")
        
        # Check #modal=Wallet at end
        if not url.endswith('#modal=Wallet'):
            errors.append(f"{u['file']}/{u['email']}/{u['locale']}/{u['field']}: missing #modal=Wallet at end")
        
        # Check UTMs present
        for utm in ['utm_campaign=', 'utm_source=customerio', 'utm_medium=email', 'utm_language=', 'utm_email=']:
            if utm not in url:
                errors.append(f"{u['file']}/{u['email']}/{u['locale']}/{u['field']}: missing {utm}")
        
        # Check locale in URL path matches utm_language
        loc_map = {'Default': 'en', 'de-DE': 'de', 'fr-FR': 'fr', 'nl-NL': 'nl'}
        expected_loc = loc_map.get(u['locale'], 'en')
        if f'heyhocasino.com/{expected_loc}?' not in url:
            errors.append(f"{u['file']}/{u['email']}/{u['locale']}/{u['field']}: wrong locale in path (expected {expected_loc})")
        if f'utm_language={expected_loc}' not in url:
            errors.append(f"{u['file']}/{u['email']}/{u['locale']}/{u['field']}: wrong utm_language (expected {expected_loc})")
        
        # Check promo code consistency
        if u['promo']:
            if f"promo-code={u['promo']}" not in url:
                errors.append(f"{u['file']}/{u['email']}/{u['locale']}/{u['field']}: promo code {u['promo']} not in URL")
        else:
            if 'promo-code=' in url:
                errors.append(f"{u['file']}/{u['email']}/{u['locale']}/{u['field']}: has promo-code but email has no promo")

# Check DEP Retention bonus types
for fname in files:
    short = fname.replace(' - Table data.txt', '')
    if short == 'DEP Retention':
        fp = os.path.join(folder, fname)
        with open(fp, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        current_name = ''
        for line in lines:
            if ':' in line:
                key = line.split(':', 1)[0].strip()
                val = line.split(':', 1)[1].strip()
                if key == 'name':
                    current_name = val
                elif key in HREF_FIELDS and val:
                    if current_name.endswith('L') and 'utm_bonus_type=live' not in val:
                        errors.append(f'DEP/{current_name}: L email missing utm_bonus_type=live')
                    if current_name.endswith('S') and 'utm_bonus_type=slots' not in val:
                        errors.append(f'DEP/{current_name}: S email missing utm_bonus_type=slots')
                    break  # just check first href per block

# Print stats
print('=== STATS ===')
total_filled = 0
total_empty = 0
for f, s in sorted(stats.items()):
    print(f"  {f}: {s['filled']} filled, {s['empty']} empty")
    total_filled += s['filled']
    total_empty += s['empty']
print(f'  TOTAL: {total_filled} filled, {total_empty} empty')

# Print errors
print(f'\n=== ERRORS ({len(errors)}) ===')
for e in errors[:30]:
    print(f'  {e}')
if len(errors) > 30:
    print(f'  ... and {len(errors) - 30} more')

# Show sample URLs for each campaign
print('\n=== SAMPLE URLs (first Default locale per campaign) ===')
shown = set()
for fname in files:
    short = fname.replace(' - Table data.txt', '')
    fp = os.path.join(folder, fname)
    with open(fp, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    current_name = ''
    current_locale = ''
    for line in lines:
        if ':' in line:
            key = line.split(':', 1)[0].strip()
            val = line.split(':', 1)[1].strip()
            if key == 'name':
                current_name = val
            elif key == 'locale':
                current_locale = val
            elif key == 'button_href_1' and val and current_locale == 'Default' and short not in shown:
                shown.add(short)
                print(f'\n  {short} / {current_name}:')
                print(f'    {val}')
