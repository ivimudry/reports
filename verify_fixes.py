"""Verify all fixes were applied correctly."""
fp = 'тексти/хейхо/Unsuccessful Deposit - Table data.txt'
with open(fp, 'r', encoding='utf-8') as f:
    c = f.read()

errors = 0

# 1. No bare <span> outside <p> before </td> in Email 2 Default
if 'HeyHo Support</span></td>' in c:
    print('FAIL: Email 2 Default still has bare span before </td>')
    errors += 1
elif 'HeyHo Support</span></p></td>' in c:
    print('OK: Email 2 Default - Thanks/HeyHo Support properly wrapped in <p>')
else:
    print('WARN: Email 2 Default - unusual pattern')

# 2. No truncated "Hey" in fr-FR
if "support Hey</span>" in c:
    print('FAIL: Still has truncated "Hey"')
    errors += 1
else:
    print('OK: No truncated "Hey" found')
if "support HeyHo</span>" in c:
    print('OK: "HeyHo" is present')

# 3. No /fr/ in nl-NL contact-us URLs
count_fr = c.count('heyhocasino.com/fr/page/contact-us')
count_nl = c.count('heyhocasino.com/nl/page/contact-us')
if count_fr > 0:
    # Check if any of these are in nl-NL locale blocks
    # Find all nl-NL blocks
    idx = 0
    nl_fr_count = 0
    while True:
        p = c.find('locale: nl-NL', idx)
        if p < 0: break
        # Find next locale or EOF
        next_locale = c.find('\nlocale:', p + 13)
        next_name = c.find('\nname:', p + 13)
        end = min(x for x in [next_locale, next_name, len(c)] if x > 0)
        block = c[p:end]
        if 'heyhocasino.com/fr/page/contact-us' in block:
            nl_fr_count += 1
        idx = p + 1
    if nl_fr_count > 0:
        print(f'FAIL: {nl_fr_count} nl-NL blocks still have /fr/ URLs')
        errors += 1
    else:
        print(f'OK: No /fr/ URLs in nl-NL blocks (total /fr/ URLs: {count_fr}, /nl/ URLs: {count_nl})')
else:
    print(f'OK: No /fr/ contact-us URLs found at all (/nl/ count: {count_nl})')

# 4. No <font><br></font> in Email 3 fr-FR
if '<font><br></font>' in c:
    print('FAIL: <font><br></font> still present')
    errors += 1
else:
    print('OK: No <font><br></font> found')

# 5. No raw newlines inside span tags (Email 3 fr-FR fix)
# Check for pattern: </a> \n</b>
if '</a> \n</b>' in c:
    print('FAIL: Raw newlines after link still present')
    errors += 1
else:
    print('OK: No raw newlines after links')

# 6. No "Try Again:" or "Support:" inline labels in Email 5
if 'Try Again: </span>' in c:
    print('FAIL: Email 5 Default still has inline "Try Again:"')
    errors += 1
else:
    print('OK: No inline "Try Again:" in Email 5')

if '>Erneut versuchen: </span>' in c:
    print('FAIL: Email 5 de-DE still has inline "Erneut versuchen:"')
    errors += 1
else:
    print('OK: No inline "Erneut versuchen:" in Email 5')

if 'Réessayer : </span>' in c:
    print('FAIL: Email 5 fr-FR still has inline "Réessayer :"')
    errors += 1
else:
    print('OK: No inline "Réessayer :" in Email 5')

if 'Opnieuw proberen: </span>' in c:
    print('FAIL: Email 5 nl-NL still has inline "Opnieuw proberen:"')
    errors += 1
else:
    print('OK: No inline "Opnieuw proberen:" in Email 5')

# 7. No bare <span> between </p> and <p> in Email 5 nl-NL
if '</p><span style=' in c:
    # Find these occurrences
    idx = 0
    bare_count = 0
    while True:
        p = c.find('</p><span style=', idx)
        if p < 0: break
        bare_count += 1
        snippet = c[p:p+100]
        print(f'  WARN: bare span at pos {p}: {repr(snippet[:80])}')
        idx = p + 1
    if bare_count:
        print(f'FAIL: {bare_count} bare <span> between </p> tags')
        errors += 1
else:
    print('OK: No bare <span> between </p> and <p>')

# 8. Check important structural elements still intact
promo = c.count('promocode_button_1:')
logo_src = c.count('logo_src:')
pirat_src = c.count('pirat_girl_src:')
name_count = c.count('\nname: ')
print(f'\nStructural check: promocode={promo}/4, logo_src={logo_src}/8, pirat_girl_src={pirat_src}/8, name entries={name_count}/20')

print(f'\n{"=" * 40}')
print(f'Errors: {errors}')
print('ALL GOOD!' if errors == 0 else 'SOME ISSUES REMAIN')
