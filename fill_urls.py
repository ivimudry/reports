import os, re

folder = 'тексти/хейхо'

LOCALE_MAP = {
    'Default': 'en',
    'de-DE': 'de',
    'fr-FR': 'fr',
    'nl-NL': 'nl',
}

# Campaign config: filename prefix -> (utm_campaign, bonus_type_mode)
# bonus_type_mode: 'live', 'slots', 'from_name' (L/S in email name), None (no bonus_type)
CAMPAIGN_CONFIG = {
    'DEP Retention':    ('dep',        'from_name'),
    'Nutrition #1 LIVE':('nutrition1', 'live'),
    'Nutrition #1 SLOTS':('nutrition1','slots'),
    'Nutrition #2 LIVE':('nutrition2', 'live'),
    'Nutrition #2 SLOTS':('nutrition2','slots'),
    'Nutrition #3 LIVE':('nutrition3', 'live'),
    'Nutrition #3 SLOTS':('nutrition3','slots'),
    'Nutrition #4 LIVE':('nutrition4', 'live'),
    'Nutrition #4 SLOTS':('nutrition4','slots'),
    'Nutrition #5 LIVE':('nutrition5', 'live'),
    'Nutrition #5 SLOTS':('nutrition5','slots'),
    'Nutrition #6 LIVE':('nutrition6', 'live'),
    'Nutrition #6 SLOTS':('nutrition6','slots'),
    'SU Retention':     ('su',         None),
    'Welcome Flow':     ('welcome',    None),
}

HREF_FIELDS = {'button_href_1', 'button_href_2', 'logo_href', 'banner_href',
               'monkey_href', 'bottom_logo_href', 'logo_botom_href'}

def get_email_id(name):
    """Extract email identifier for utm_email."""
    eid = name.replace('Email ', '')
    # "1 (1)" -> "1.1"
    eid = re.sub(r'\s*\((\d+)\)', r'.\1', eid)
    eid = eid.replace(' ', '')
    return eid

def get_bonus_type(name, mode):
    """Determine utm_bonus_type from email name and campaign mode."""
    if mode == 'live':
        return 'live'
    elif mode == 'slots':
        return 'slots'
    elif mode == 'from_name':
        # DEP Retention: Email 1L -> live, Email 1S -> slots
        if name.rstrip().endswith('L'):
            return 'live'
        elif name.rstrip().endswith('S'):
            return 'slots'
        else:
            return None  # fallback
    return None

def build_url(loc, promo_code, utm_campaign, bonus_type, utm_email):
    """Build the full URL with promo code and UTMs."""
    base = f'https://heyhocasino.com/{loc}?token={{{{customer.auth_token}}}}'
    
    if promo_code:
        base += f'&promo-code={promo_code}'
    
    # UTMs
    utms = f'&utm_campaign={utm_campaign}'
    if bonus_type:
        utms += f'&utm_bonus_type={bonus_type}'
    utms += f'&utm_source=customerio&utm_medium=email&utm_language={loc}&utm_email={utm_email}'
    
    return base + utms + '#modal=Wallet'

# Process each file
files = sorted([f for f in os.listdir(folder) if f.endswith('.txt') and 'Unsuccessful' not in f])
grand_total = 0

for fname in files:
    short = fname.replace(' - Table data.txt', '')
    if short not in CAMPAIGN_CONFIG:
        print(f'SKIP {short} - not in config')
        continue
    
    utm_campaign, bonus_mode = CAMPAIGN_CONFIG[short]
    fp = os.path.join(folder, fname)
    
    with open(fp, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # First pass: parse blocks to get name, locale, promo for each block
    # Track which line ranges belong to which block
    block_starts = []
    for i, line in enumerate(lines):
        if ':' in line:
            key = line.split(':', 1)[0].strip()
            if key == 'name':
                block_starts.append(i)
    
    # Build block info
    blocks = []
    for idx, start in enumerate(block_starts):
        end = block_starts[idx + 1] if idx + 1 < len(block_starts) else len(lines)
        block_info = {'start': start, 'end': end, 'name': '', 'locale': '', 'promo': ''}
        for i in range(start, end):
            if ':' in lines[i]:
                key = lines[i].split(':', 1)[0].strip()
                val = lines[i].split(':', 1)[1].strip()
                if key == 'name':
                    block_info['name'] = val
                elif key == 'locale':
                    block_info['locale'] = val
                elif key == 'promocode_button_1':
                    block_info['promo'] = val
        blocks.append(block_info)
    
    # Second pass: fill href fields
    file_count = 0
    new_lines = list(lines)
    
    for block in blocks:
        loc = LOCALE_MAP.get(block['locale'], 'en')
        email_id = get_email_id(block['name'])
        bonus_type = get_bonus_type(block['name'], bonus_mode)
        promo = block['promo']
        
        url = build_url(loc, promo, utm_campaign, bonus_type, email_id)
        
        for i in range(block['start'], block['end']):
            if ':' in new_lines[i]:
                key = new_lines[i].split(':', 1)[0].strip()
                val = new_lines[i].split(':', 1)[1].strip()
                if key in HREF_FIELDS and not val:
                    new_lines[i] = f'{key}: {url}\n'
                    file_count += 1
    
    with open(fp, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    
    grand_total += file_count
    print(f'{short}: {file_count} href fields filled')

print(f'\nTotal: {grand_total} fields filled across all files')
