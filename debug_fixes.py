"""Debug: find exact context for unfixed patterns."""

fp = 'тексти/хейхо/Unsuccessful Deposit - Table data.txt'
with open(fp, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix 1: Thanks outside <p> in Email 2 Default
idx = content.find("according to your bank")
if idx >= 0:
    snippet = content[idx:idx+400]
    print('=== Fix 1 context (Email 2 Default - Thanks) ===')
    print(repr(snippet))
    print()

# Fix 2: Hey -> HeyHo
idx2 = content.find("support Hey</span>")
if idx2 >= 0:
    print('=== Fix 2 context ===')
    print(repr(content[idx2:idx2+80]))
else:
    print('Fix 2: "support Hey</span>" not found')
    idx2b = content.find("support HeyHo</span>")
    if idx2b >= 0:
        print('  -> already HeyHo (good)')
print()

# Fix 4b: CONTACTER LE SUPPORT in Email 3 fr-FR
start = 0
positions = []
while True:
    p = content.find('[CONTACTER LE SUPPORT]</a>', start)
    if p < 0:
        break
    positions.append(p)
    start = p + 1

for p in positions:
    snippet = content[p:p+400]
    print(f'=== CONTACTER at pos {p} ===')
    print(repr(snippet[:400]))
    print()

# Fix 5a: Email 5 Default buttons
idx5 = content.find('Try Again: </span>')
if idx5 >= 0:
    print('=== Fix 5a context (Email 5 Default) ===')
    print(repr(content[idx5-200:idx5+300]))
else:
    print('Fix 5a: Try Again not found')
print()

# Fix 5c: Email 5 fr-FR buttons
idx5c = content.find('Réessayer')
if idx5c >= 0:
    print('=== Fix 5c context (Email 5 fr-FR) ===')
    print(repr(content[idx5c-20:idx5c+300]))
else:
    print('Fix 5c: Réessayer not found')
