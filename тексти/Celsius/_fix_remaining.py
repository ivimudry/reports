"""Fix remaining 3 formatting issues (DEP 7C is separate - wrong content)."""
import os

DIR = r'c:\Projects\REPORTS\тексти\Celsius'
fixes = 0

def fix(fname, old, new, desc):
    global fixes
    fpath = os.path.join(DIR, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()
    if old not in c:
        print(f"  !! NOT FOUND: {desc}")
        return
    if c.count(old) > 1:
        print(f"  !! AMBIGUOUS: {desc}")
        return
    c = c.replace(old, new)
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(c)
    fixes += 1
    print(f"  OK: {desc}")

# N2 2CL: restore <br><br> between sentences
fix('Nutrition #2 - Table data.txt',
    'massifs. Serez-vous',
    'massifs.<br><br>Serez-vous',
    'N2 2CL: restore <br><br> between sentences')

# N2 2CS: restore <br><br> between sentences
fix('Nutrition #2 - Table data.txt',
    'préférées. Serez-vous',
    'préférées.<br><br>Serez-vous',
    'N2 2CS: restore <br><br> between sentences')

# Welcome 1S: remove 2 extra &nbsp;
fix('Welcome Flow - Table data.txt',
    'supérieur ?&nbsp; Démarrez',
    'supérieur ? Démarrez',
    'WF 1S: remove &nbsp; after ?')

fix('Welcome Flow - Table data.txt',
    'match.&nbsp; Faites',
    'match. Faites',
    'WF 1S: remove &nbsp; after .')

print(f"\nTotal fixes: {fixes}")
