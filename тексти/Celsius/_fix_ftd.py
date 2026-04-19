import os

BASE = r'c:\Projects\REPORTS\тексти\Celsius'

path = os.path.join(BASE, 'SU Retention - Table data.txt')
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = [
    ('\u2696\ufe0f R\u00e9clamez votre bonus pr\u00e9f\u00e9r\u00e9 :', '\u2696\ufe0f<br><br>R\u00e9clamez votre bonus pr\u00e9f\u00e9r\u00e9 :'),
    ('le v\u00f4tre. D\u00e9marrez votre aventure :', 'le v\u00f4tre.<br><br>D\u00e9marrez votre aventure :'),
    ('pour vous : \u2022 Utilisez le code', 'pour vous :<br><br>\u2022 Utilisez le code'),
    ('au casino.<br>\U0001f419 \u2022 Utilisez le code', 'au casino. \U0001f419<br>\u2022 Utilisez le code'),
    ('compte. Activez votre bonus :', 'compte.<br><br>Activez votre bonus :'),
]

total = 0
for old, new in replacements:
    ct = content.count(old)
    content = content.replace(old, new)
    total += ct

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

# Write result to a file since terminal output is broken
with open(os.path.join(BASE, '_result.txt'), 'w') as f:
    f.write(f'Total replacements: {total}\n')
