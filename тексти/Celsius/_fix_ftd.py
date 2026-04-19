import os

BASE = r'c:\Projects\REPORTS\тексти\Celsius'
total = 0

def safe_replace(content, old, new, label):
    global total
    ct = content.count(old)
    if ct == 1:
        content = content.replace(old, new)
        total += 1
        print(f'  OK: {label}')
    elif ct == 0:
        print(f'  SKIP (0 matches): {label}')
    else:
        print(f'  SKIP ({ct} matches): {label}')
    return content

# ==========================================
# SU Retention
# ==========================================
print('=== SU Retention ===')
path = os.path.join(BASE, 'SU Retention - Table data.txt')
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# --- Winner block line 2081 ---
# Fix text gluing after last winner + sentence structure + CTA br
content = safe_replace(content,
    "</strong> Ces gains \u00e9taient r\u00e9els.<br><br>Les joueurs \u00e9taient r\u00e9els. Et votre chance ? Elle n'est qu'\u00e0 un tour. Rejoignez le cercle des gagnants :",
    "</strong><br><br>Ces gains \u00e9taient r\u00e9els. Les joueurs \u00e9taient r\u00e9els. Et votre chance ? Elle n'est qu'\u00e0 un tour.<br><br>Rejoignez le cercle des gagnants :",
    'SU 2081: winner block text gluing + structure')

# --- Line 585: dual offer structure ---
# Fix missing <br><br> after colon, item structure
content = safe_replace(content,
    "et obtenez : <strong>Bonus de 100% + 150 Tours Gratuits</strong> sur <strong>Razor Shark</strong> avec le code <strong class=\"promocode\">FINTASTIC150</strong><br><strong>4% Cashback</strong> sur vos paris sportifs avec le code <strong class=\"promocode\">CASHPLUS4</strong>.<br><br>Un seul",
    "et obtenez :<br><br><strong>Bonus de 100% + 150 Tours Gratuits</strong> sur <strong>Razor Shark</strong> avec le code <strong class=\"promocode\">FINTASTIC150</strong><br><strong>4% Cashback</strong> sur vos paris sportifs avec le code <strong class=\"promocode\">CASHPLUS4</strong>.<br><br>Un seul",
    'SU 585: missing br after colon')

# Fix emoji before CTA
content = safe_replace(content,
    "votre fa\u00e7on. \U0001f3b2 D\u00e9bloquez les deux bonus :",
    "votre fa\u00e7on. \U0001f3b2<br><br>D\u00e9bloquez les deux bonus :",
    'SU 585: emoji CTA br')

# --- Line 993: item list structure ---
content = safe_replace(content,
    "un <strong>Bonus de 140%</strong><br>au casino \u2022 Utilisez",
    "un <strong>Bonus de 140%</strong> au casino<br>\u2022 Utilisez",
    'SU 993: text on wrong line after Bonus')

content = safe_replace(content,
    "au sport C'est votre choix",
    "au sport<br><br>C'est votre choix",
    'SU 993: text gluing after sport')

content = safe_replace(content,
    "premier geste.<br><br>\U0001f680 S\u00e9lectionnez",
    "premier geste. \U0001f680<br><br>S\u00e9lectionnez",
    'SU 993: emoji CTA placement')

# --- Line 1401: item structure ---
content = safe_replace(content,
    "Bonanza</strong>.<br>\U0001f36c \u2022 <strong>Vous pr\u00e9f\u00e9rez parier ?</strong>",
    "Bonanza</strong>. \U0001f36c<br>\u2022 <strong>Vous pr\u00e9f\u00e9rez parier ?</strong>",
    'SU 1401: emoji on wrong line')

# --- Line 1809: similar ---
content = safe_replace(content,
    "Risque</strong>.<br><br>Votre bonus de bienvenue est pr\u00eat",
    "Risque</strong>.<br><br>Votre bonus de bienvenue est pr\u00eat",
    'SU 1809: check (should be OK)')

# --- Line 2217: item structure ---
content = safe_replace(content,
    "d\u00e9p\u00f4t.\u2022&nbsp;<br><strong>Fan de sport ?</strong>",
    "d\u00e9p\u00f4t.<br>\u2022 <strong>Fan de sport ?</strong>",
    'SU 2217: bullet on wrong line')

# --- Line 2625: item structure ---
content = safe_replace(content,
    "Chaos Crew II</strong>. \U0001f480\u2022&nbsp;<br><strong>Vous pr\u00e9f\u00e9rez parier ?</strong>",
    "Chaos Crew II</strong>. \U0001f480<br>\u2022 <strong>Vous pr\u00e9f\u00e9rez parier ?</strong>",
    'SU 2625: bullet on wrong line')

# --- Line 3033: same pattern as 2625 ---
content = safe_replace(content,
    "Chaos Crew II</strong>. \U0001f480\u2022&nbsp;<br><strong>Vous pr\u00e9f\u00e9rez parier ?</strong>",
    "Chaos Crew II</strong>. \U0001f480<br>\u2022 <strong>Vous pr\u00e9f\u00e9rez parier ?</strong>",
    'SU 3033: bullet on wrong line')

# --- Line 3441: item structure ---
content = safe_replace(content,
    "casino.<br>\U0001f419 \u2022 Utilisez le code",
    "casino. \U0001f419<br>\u2022 Utilisez le code",
    'SU 3441: emoji on wrong line')

# --- Line 3849: same as 3441 ---
content = safe_replace(content,
    "casino.<br>\U0001f419 \u2022 Utilisez le code",
    "casino. \U0001f419<br>\u2022 Utilisez le code",
    'SU 3849: emoji on wrong line')

# --- Generic: fix fr-FR missing <br><br> before CTA emoji lines ---
# Line 41: 🚀 Activez
content = safe_replace(content,
    "filer ! \U0001f680 Activez vos r\u00e9compenses :",
    "filer ! \U0001f680<br><br>Activez vos r\u00e9compenses :",
    'SU 41: emoji CTA br')

# Line 177: 🦈 Réclamez
content = safe_replace(content,
    "geste. \U0001f988 R\u00e9clamez le pack complet :",
    "geste. \U0001f988<br><br>R\u00e9clamez le pack complet :",
    'SU 177: emoji CTA br')

# Line 449: 🃏 Cliquez
content = safe_replace(content,
    "fort. \U0001f0cf Cliquez pour r\u00e9clamer votre pack :",
    "fort. \U0001f0cf<br><br>Cliquez pour r\u00e9clamer votre pack :",
    'SU 449: emoji CTA br')

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

# ==========================================
# Welcome Flow
# ==========================================
print('\n=== Welcome Flow ===')
path = os.path.join(BASE, 'Welcome Flow - Table data.txt')
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix missing space before <strong> 
content = safe_replace(content,
    "receive<strong>100",
    "receive <strong>100",
    'Welcome Default: space before strong')

content = safe_replace(content,
    "recevoir<strong> 100",
    "recevoir <strong>100",
    'Welcome fr-FR: space before strong')

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f'\nTotal changes: {total}')
