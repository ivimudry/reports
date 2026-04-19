path = r'c:\Projects\REPORTS\тексти\Celsius\FTD Retention Flow - Table data.txt'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

changes = 0

def safe_replace(content, old, new, label):
    global changes
    ct = content.count(old)
    if ct == 1:
        content = content.replace(old, new)
        changes += 1
        print(f'  OK: {label}')
    else:
        print(f'  SKIP ({ct} matches): {label}')
    return content

# Email 3M fr-FR: Cashback<br><br>sur l'activite casino Ou (ASCII apostrophe)
content = safe_replace(content,
    "Cashback</strong><br><br>sur l'activit\u00e9 casino Ou utilisez",
    "Cashback</strong> sur l'activit\u00e9 casino<br><br>Ou utilisez",
    'Email 3M fr-FR Cashback->casino')

# Email 6M fr-FR: la valeur.<br><br>C'est (ASCII apostrophe)
content = safe_replace(content,
    "la valeur.<br><br>C'est votre style, maintenant",
    "la valeur. C'est votre style, maintenant",
    "Email 6M fr-FR extra br before C'est")

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f'\nTotal changes: {changes}')
