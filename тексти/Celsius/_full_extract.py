import json, os, re

base = os.path.dirname(os.path.abspath(__file__))
data = json.load(open(os.path.join(base, '_texts_to_translate.json'), 'r', encoding='utf-8'))

# Read the actual file to get full-length fields
filename = 'DEP Retention - Table data.txt'
filepath = os.path.join(base, filename)
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Parse all blocks
blocks = []
current = {}
for line in content.split('\n'):
    line = line.rstrip('\r')
    if line.startswith('name: '):
        if current:
            blocks.append(current)
        current = {'name': line[6:]}
    elif ': ' in line and current:
        key, val = line.split(': ', 1)
        current[key] = val
if current:
    blocks.append(current)

# Extract only Default locale blocks with translatable fields
def strip_html(s):
    return re.sub(r'<[^>]+>', '', s).strip()

# Group by email name
emails = {}
for b in blocks:
    name = b.get('name', '')
    locale = b.get('locale', '')
    if locale == 'Default':
        emails[name] = b

# Output full English text for each email  
for name in sorted(emails.keys(), key=lambda x: (int(re.search(r'\d+', x).group()) if re.search(r'\d+', x) else 0, x)):
    b = emails[name]
    print(f'\n{"="*60}')
    print(f'EMAIL: {name}')
    print(f'{"="*60}')
    print(f'SUBJECT: {b.get("subject", "")}')
    print(f'PREHEADER: {b.get("preheader", "")}')
    
    t1 = b.get('text_1', '')
    t1_visible = strip_html(t1)
    print(f'TEXT_1 (visible): {t1_visible}')
    
    t2 = b.get('text_2', '')
    t2_visible = strip_html(t2)
    print(f'TEXT_2 (visible): {t2_visible}')
    
    t3 = b.get('text_3', '')
    if t3:
        t3_visible = strip_html(t3)
        print(f'TEXT_3 (visible): {t3_visible}')
    
    print(f'BUTTON: {b.get("button_text_1", "")}')
    print(f'PROMO: {b.get("promocode_button_1", "N/A")}')
