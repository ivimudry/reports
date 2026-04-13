import os

DIR = r"c:\Projects\REPORTS\тексти\Celsius"
FILES = [
    "DEP Retention - Table data.txt",
    "FTD Retention Flow - Table data.txt",
    "Nutrition #2 - Table data.txt",
    "Nutrition #3 - Table data.txt",
    "SU Retention - Table data.txt",
    "Welcome Flow - Table data.txt",
    "Failed Deposit Flow - Table data.txt",
]

# EN originals to search for
EN_TEXTS = {
    'team_sig': 'Celsius Casino Team.',
    'auto_msg': 'This is an automated message, please do not reply.',
    'footer_email': 'You are receiving this email from celsiuscasino.com',
    'unsubscribe': '>Unsubscribe<',
    'rights': 'All Rights Reserved',
    'support_label': '>Support<',
}

for fn in FILES:
    path = os.path.join(DIR, fn)
    lines = open(path, 'r', encoding='utf-8').readlines()
    locale = ''
    fr_lines = []
    
    for l in lines:
        s = l.strip()
        if s.startswith('locale: '):
            locale = s[8:]
        if locale == 'fr-FR':
            fr_lines.append(l)
    
    if not fr_lines:
        print(f"\n{fn}: NO fr-FR locale found!")
        continue
    
    fr_text = ''.join(fr_lines)
    print(f"\n{fn} (fr-FR):")
    for key, en in EN_TEXTS.items():
        count = fr_text.count(en)
        if count > 0:
            print(f"  {key}: {count} still EN")
        else:
            print(f"  {key}: 0 (translated or absent)")

# Also check what labels contain "Support" text
print("\n\n=== Labels containing 'Support' word ===")
for fn in FILES:
    path = os.path.join(DIR, fn)
    lines = open(path, 'r', encoding='utf-8').readlines()
    locale = ''
    name = ''
    found = set()
    for l in lines:
        s = l.strip()
        if s.startswith('name: '): name = s[6:]
        if s.startswith('locale: '): locale = s[8:]
        if locale == 'Default' and '>Support<' in s:
            lbl = s.split(':')[0]
            found.add(lbl)
    if found:
        print(f"  {fn}: {sorted(found)}")

# Check text_5 through text_12 content in DEP Retention Default
print("\n\n=== DEP Retention Default: text_5..text_12 content ===")
lines = open(os.path.join(DIR, "DEP Retention - Table data.txt"), 'r', encoding='utf-8').readlines()
locale = ''
name = ''
for l in lines:
    s = l.strip()
    if s.startswith('name: '): name = s[6:]
    if s.startswith('locale: '): locale = s[8:]
    if locale == 'Default' and name == 'Email 1C':
        for t in ['text_5','text_6','text_7','text_8','text_9','text_10','text_11','text_12']:
            if s.startswith(t + ':'):
                # Extract visible text between > and <
                import re
                vis = re.findall(r'>([^<]+)<', s)
                vis_text = [v for v in vis if v.strip()]
                print(f"  {t}: {vis_text}")
