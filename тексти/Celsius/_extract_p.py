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

def extract_p_content(html):
    """Extract content between <p ...> and </p>"""
    m = re.search(r'<p[^>]*>(.*)</p>', html)
    return m.group(1) if m else html

# Show p-content and default for all emails (Default locale only)
for b in blocks:
    if b.get('locale') != 'Default':
        continue
    name = b.get('name', '')
    print(f"\n{'='*60}")
    print(f"EMAIL: {name}")
    
    # text_1: extract default and greeting
    t1 = b.get('text_1', '')
    m_def = re.search(r'default:"([^"]*)"', t1)
    m_greet = re.search(r'\}\}\s*\|\s*capitalize\s*\}\}(.*?)</strong>', t1)
    if m_def:
        print(f"  default: \"{m_def.group(1)}\"")
    if m_greet:
        print(f"  greeting: {m_greet.group(1)}")
    
    # text_2: p-content
    t2 = b.get('text_2', '')
    t2_p = extract_p_content(t2)
    print(f"  text_2_p: {t2_p}")
    
    # text_3: p-content or team sig
    t3 = b.get('text_3', '')
    if t3:
        if 'Celsius Casino Team' in t3:
            print(f"  text_3: [TEAM SIG - skip]")
        else:
            t3_p = extract_p_content(t3)
            print(f"  text_3_p: {t3_p}")
