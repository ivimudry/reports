import os

d = r'c:\Projects\REPORTS\тексти\Celsius'
files = sorted([f for f in os.listdir(d) if f.endswith('.txt') and 'Table data' in f])

for fname in files:
    path = os.path.join(d, fname)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    blocks = content.strip().split('\n\n')
    emails = {}
    
    for block in blocks:
        lines = block.strip().split('\n')
        data = {}
        for line in lines:
            idx = line.find(': ')
            if idx > 0:
                data[line[:idx].strip()] = line[idx+2:].strip()
        
        name = data.get('name', '')
        locale = data.get('locale', '')
        if name and locale:
            emails.setdefault(name, set()).add(locale)
    
    expected = {'Default', 'fr-FR', 'hu-HU', 'pl-PL'}
    missing = []
    for ename in sorted(emails.keys()):
        diff = expected - emails[ename]
        if diff:
            missing.append(f'  {ename}: missing {diff}')
    
    if missing:
        print(f'{fname}: ISSUES')
        for m in missing:
            print(m)
    else:
        print(f'{fname}: OK - {len(emails)} emails x 4 locales')
