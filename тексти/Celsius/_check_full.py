import os, re

base = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(base, 'DEP Retention - Table data.txt')
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

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

# Show full text_2 for winner and sport winner emails
for b in blocks:
    if b.get('locale') == 'Default' and b.get('name') in ['Email 3C', 'Email 3S', 'Email 6C', 'Email 8S']:
        print(f"\n{'='*60}")
        print(f"{b['name']} - FULL text_2:")
        print(b.get('text_2', 'N/A'))
        print(f"\n{b['name']} - FULL text_3:")
        print(b.get('text_3', 'N/A'))
