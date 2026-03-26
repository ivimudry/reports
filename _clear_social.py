import re, os

folder = r'C:\Projects\REPORTS\тексти\пантери нова праця'
files = ['welcome - Table data.txt', 'nut 1 - Table data.txt', 'nut 2 - Table data.txt']
FIELDS = ['instagram_href', 'facebook_href']

for fname in files:
    path = os.path.join(folder, fname)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    count = 0
    for field in FIELDS:
        # Replace field value with empty
        content, n = re.subn(rf'^({field}): .+$', r'\1: ', content, flags=re.MULTILINE)
        count += n
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f'{fname}: cleared {count} fields')

print('Done')
