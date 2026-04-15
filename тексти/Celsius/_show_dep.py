import os, re, json

DIR = r'c:\Projects\REPORTS\тексти\Celsius'

def parse_file(path):
    lines = open(path, 'r', encoding='utf-8').readlines()
    blocks = []
    current = {}
    for line in lines:
        raw = line.rstrip('\n')
        if not raw.strip():
            if current:
                blocks.append(current)
                current = {}
            continue
        idx = raw.find(':')
        if idx > 0:
            key = raw[:idx].strip()
            val = raw[idx+1:].strip()
            current[key] = val
    if current:
        blocks.append(current)
    return blocks

def strip_html(s):
    s = re.sub(r'<[^>]+>', '', s)
    s = re.sub(r'\{\{[^}]+\}\}', '{{name}}', s)
    s = s.replace('&nbsp;', ' ').replace('&amp;', '&').replace('&lt;', '<').replace('&gt;', '>')
    return s.strip()

fn = "DEP Retention - Table data.txt"
blocks = parse_file(os.path.join(DIR, fn))

# Group by email
emails = {}
order = []
for b in blocks:
    name = b.get('name', '?')
    locale = b.get('locale', '?')
    if name not in emails:
        emails[name] = {}
        order.append(name)
    emails[name][locale] = b

for ename in order:
    default_b = emails[ename].get('Default', {})
    if not default_b:
        continue
    
    print(f"\n{'='*70}")
    print(f"EMAIL: {ename}")
    print(f"{'='*70}")
    
    for field in ['subject', 'preheader', 'text_1', 'text_2', 'text_3', 'button_text_1']:
        val = default_b.get(field, '')
        if not val:
            continue
        text = strip_html(val)
        print(f"\n  [{field}]")
        # Wrap long text
        if len(text) > 100:
            words = text.split()
            line = "    "
            for w in words:
                if len(line) + len(w) + 1 > 100:
                    print(line)
                    line = "    " + w
                else:
                    line += " " + w if line.strip() else "    " + w
            if line.strip():
                print(line)
        else:
            print(f"    {text}")
