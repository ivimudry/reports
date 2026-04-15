import os, re

base = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(base, 'DEP Retention - Table data.txt')
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

# Show specific emails' text_2 and text_3 html for Default locale
for b in blocks:
    if b.get('locale') == 'Default' and b.get('name') in ['Email 3C', 'Email 6C']:
        print(f"\n=== {b['name']} (Default) ===")
        print(f"text_2: {b.get('text_2', 'N/A')[:500]}")
        print(f"---")
        print(f"text_3: {b.get('text_3', 'N/A')[:500]}")
        print(f"---")
        # Check if text_2 has <br>
        t2 = b.get('text_2', '')
        brs = t2.count('<br')
        strongs = t2.count('<strong')
        print(f"text_2 <br> count: {brs}, <strong> count: {strongs}, length: {len(t2)}")
