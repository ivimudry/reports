import os, re

DIR = r"c:\Projects\REPORTS\тексти\Celsius"

# Campaign mapping from filename
CAMPAIGN_MAP = {
    "Welcome Flow - Table data.txt": "welcome",
    "FTD Retention Flow - Table data.txt": "ftd",
    "DEP Retention - Table data.txt": "dep",
    "SU Retention - Table data.txt": "su",
    "Nutrition #2 - Table data.txt": "nutrition2",
    "Nutrition #3 - Table data.txt": "nutrition3",
    "Failed Deposit Flow - Table data.txt": "faildep",
}

# Locale → utm_language
LANG_MAP = {
    "Default": "en",
    "fr-FR": "fr",
    "hu-HU": "hu",
    "pl-PL": "pl",
}

def parse_email_name(name):
    """Parse 'Email 1CL' → (number=1, bonus_type='casino', bonus_subtype='live')"""
    m = re.match(r'Email\s+(\d+)([A-Z]*)', name)
    if not m:
        return None, None, None
    
    num = int(m.group(1))
    suffix = m.group(2)
    
    bonus_type = None
    bonus_subtype = None
    
    if len(suffix) == 0:
        pass  # no type
    elif len(suffix) == 1:
        if suffix == 'C':
            bonus_type = 'casino'
        elif suffix == 'S':
            bonus_type = 'sports'
        elif suffix == 'M':
            bonus_type = 'mixed'
    elif len(suffix) == 2:
        first = suffix[0]
        second = suffix[1]
        if first == 'C':
            bonus_type = 'casino'
        elif first == 'S':
            bonus_type = 'sports'
        elif first == 'M':
            bonus_type = 'mixed'
        
        if second == 'L':
            bonus_subtype = 'live'
        elif second == 'S':
            bonus_subtype = 'slots'
    
    return num, bonus_type, bonus_subtype

def build_utm(campaign, email_num, language, bonus_type, bonus_subtype):
    """Build UTM query string"""
    params = [
        f"utm_source=customerio",
        f"utm_medium=email",
        f"utm_campaign={campaign}",
        f"utm_email={email_num}",
        f"utm_language={language}",
    ]
    if bonus_type:
        params.append(f"utm_bonus_type={bonus_type}")
    if bonus_subtype:
        params.append(f"utm_bonus_subtype={bonus_subtype}")
    return "&".join(params)

def add_utm_to_url(url, utm_string):
    """Add UTM params to a URL"""
    if '?' in url:
        return url + '&' + utm_string
    else:
        return url + '?' + utm_string

total_urls = 0

for fn, campaign in sorted(CAMPAIGN_MAP.items()):
    path = os.path.join(DIR, fn)
    if not os.path.exists(path):
        print(f"SKIP {fn}: not found")
        continue
    
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    current_name = ''
    current_locale = ''
    file_urls = 0
    
    for i in range(len(lines)):
        s = lines[i].strip()
        if s.startswith('name: '):
            current_name = s[6:]
        elif s.startswith('locale: '):
            current_locale = s[8:]
            continue
        
        # Skip lines without https://
        if 'https://' not in lines[i]:
            continue
        
        # Parse email name
        email_num, bonus_type, bonus_subtype = parse_email_name(current_name)
        if email_num is None:
            continue
        
        language = LANG_MAP.get(current_locale, 'en')
        utm_string = build_utm(campaign, email_num, language, bonus_type, bonus_subtype)
        
        # Find all https:// URLs in this line and add UTM
        def replace_url(match):
            nonlocal file_urls
            url = match.group(0)
            file_urls += 1
            return add_utm_to_url(url, utm_string)
        
        # Match https:// URLs but NOT inside mailto: context
        # The URLs end at " or < or whitespace
        lines[i] = re.sub(r'https://[^\s"<>]+', replace_url, lines[i])
    
    with open(path, 'w', encoding='utf-8') as f:
        f.writelines(lines)
    
    print(f"{fn}: {file_urls} URLs updated (campaign={campaign})")
    total_urls += file_urls

print(f"\nTotal: {total_urls} URLs updated")
