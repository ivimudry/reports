import re, os

BASE = r'c:\Projects\REPORTS\тексти\Celsius'
files = [
    'SU Retention - Table data.txt',
    'Nutrition #2 - Table data.txt',
    'Nutrition #3 - Table data.txt',
    'Welcome Flow - Table data.txt',
]

total = 0

for fname in files:
    path = os.path.join(BASE, fname)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    orig = content
    changes = 0
    
    # Step 1: Replace 3+ consecutive <br> with exactly <br><br>
    new_content = re.sub(r'(<br>){3,}', '<br><br>', content)
    c1 = len(re.findall(r'(<br>){3,}', content))
    changes += c1
    content = new_content
    
    # Step 2: Remove space in <br> <strong> (winner blocks / item lists)
    c2 = content.count('<br> <strong>')
    content = content.replace('<br> <strong>', '<br><strong>')
    changes += c2
    
    if content != orig:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
    
    print(f'{fname}: {c1} triple-br fixes, {c2} space removals = {changes} total')
    total += changes

print(f'\nTotal changes across all files: {total}')
