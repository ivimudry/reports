"""Fix rich_text emails in Unsuccessful Deposit campaign.

Fixes:
1. Email 2 Default: bare <span>Thanks,/HeyHo Support</span> outside <p> tags
2. Email 2 fr-FR: truncated "Hey" -> "HeyHo"
3. All nl-NL: /fr/ -> /nl/ in contact-us URLs
4. Email 3 fr-FR: <font><br></font> mess + raw newlines in text
5. Email 5 Default: inline buttons -> separate <p> blocks
6. Email 5 de-DE: inline buttons -> separate <p> blocks
7. Email 5 fr-FR: inline buttons -> separate <p> blocks
8. Email 5 nl-NL: bare span + inline buttons -> separate <p> blocks
"""

fp = 'тексти/хейхо/Unsuccessful Deposit - Table data.txt'
with open(fp, 'r', encoding='utf-8') as f:
    content = f.read()

fixes = 0

# Standard span style constants
S_WC = 'font-size: 11pt; font-family: Arial, sans-serif; color: rgb(0, 0, 0); background-color: transparent; font-variant-numeric: normal; font-variant-east-asian: normal; font-variant-alternates: normal; font-variant-position: normal; font-variant-emoji: normal; vertical-align: baseline; white-space-collapse: preserve;'
S_PRE = 'font-size:11pt;font-family:Arial,sans-serif;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;'
S_INNER = 'font-size: 11pt; background-color: transparent; font-variant-numeric: normal; font-variant-east-asian: normal; font-variant-alternates: normal; font-variant-position: normal; font-variant-emoji: normal; vertical-align: baseline;'

def make_btn_p(href, label):
    return (f'<p style="line-height:1.38;margin-top:12pt;margin-bottom:12pt;">'
            f'<span style="{S_WC}"><a target="_blank" href="{href}">'
            f'<b>[{label}]</b></a><b> </b></span></p>')


# ===== FIX 1: Email 2 Default — wrap bare Thanks/HeyHo Support in <p> =====
old1 = (
    "disappears automatically according to your bank's rules.</span></p>"
    f'<span style="{S_WC}">Thanks,</span>'
    f'<span style="{S_WC}"><br></span>'
    f'<span style="{S_WC}">HeyHo Support</span></td>'
)
new1 = (
    "disappears automatically according to your bank's rules.</span></p>"
    f'<p style="line-height:1.38;margin-top:12pt;margin-bottom:12pt;">'
    f'<span style="{S_WC}">Thanks,</span>'
    f'<span style="{S_WC}"><br></span>'
    f'<span style="{S_WC}">HeyHo Support</span></p></td>'
)
if old1 in content:
    content = content.replace(old1, new1, 1)
    fixes += 1; print('Fix 1 OK: Email 2 Default — wrapped Thanks/HeyHo Support in <p>')
else:
    print('WARN: Fix 1 NOT FOUND')


# ===== FIX 2: Email 2 fr-FR — truncated "Hey" -> "HeyHo" =====
old2 = "L'\u00e9quipe support Hey</span>"
new2 = "L'\u00e9quipe support HeyHo</span>"
c = content.count(old2)
if c:
    content = content.replace(old2, new2); fixes += 1
    print(f"Fix 2 OK: Email 2 fr-FR — 'Hey' -> 'HeyHo' ({c}x)")
else:
    print('WARN: Fix 2 NOT FOUND')


# ===== FIX 3: nl-NL /fr/ -> /nl/ in contact-us URLs =====
old3 = 'heyhocasino.com/fr/page/contact-us?token=auth_token">[CONTACT MET SUPPORT]'
new3 = 'heyhocasino.com/nl/page/contact-us?token=auth_token">[CONTACT MET SUPPORT]'
c3 = content.count(old3)
if c3:
    content = content.replace(old3, new3); fixes += c3
    print(f'Fix 3 OK: nl-NL /fr/ -> /nl/ ({c3}x)')
else:
    print('WARN: Fix 3 NOT FOUND')


# ===== FIX 4: Email 3 fr-FR — two sub-fixes =====

# 4a: <font><br></font> before deposit button -> proper spacing with <br>
old4a = '<font><br></font><a target="_blank" href="https://heyhocasino.com/fr/wallet/deposit" style="background-color: transparent; font-family: Arial, sans-serif; font-size: 11pt; white-space-collapse: preserve;"><b>[COMPL\u00c9TER LE D\u00c9P\u00d4T]</b></a><b style="background-color: transparent; color: rgb(0, 0, 0); font-family: Arial, sans-serif; font-size: 11pt; white-space-collapse: preserve;"> </b></p>'
new4a = (f'<span style="{S_WC}"><a target="_blank" href="https://heyhocasino.com/fr/wallet/deposit">'
         f'<b>[COMPL\u00c9TER LE D\u00c9P\u00d4T]</b></a><b> </b></span></p>')
if old4a in content:
    content = content.replace(old4a, new4a, 1); fixes += 1
    print('Fix 4a OK: Email 3 fr-FR — replaced <font><br></font> + cleaned deposit button')
else:
    print('WARN: Fix 4a NOT FOUND')

# 4b: messy CONTACTER LE SUPPORT block with raw newlines
old4b = (f'<span style="{S_PRE}"><b><a target="_blank" href="https://heyhocasino.com/fr/page/contact-us?token=auth_token">'
         '[CONTACTER LE SUPPORT]</a> \n</b></span>'
         '<span style="background-color: transparent; color: rgb(0, 0, 0); font-family: Arial, sans-serif; font-size: 11pt; white-space-collapse: preserve;">'
         ' \nSi vous avez besoin d\u2019aide imm\u00e9diatement, vous pouvez \u00e9galement nous contacter via le chat en direct sur notre site.\n</span>'
         '<span style="background-color: transparent; color: rgb(0, 0, 0); font-family: Arial, sans-serif; font-size: 11pt; white-space-collapse: preserve;">'
         '     \nMerci,\n</span>'
         '<span style="background-color: transparent; color: rgb(0, 0, 0); font-family: Arial, sans-serif; font-size: 11pt; white-space-collapse: preserve;">'
         'Alex, Support HeyHo</span></p></td>')

new4b = (f'<span style="{S_WC}"><b><a target="_blank" href="https://heyhocasino.com/fr/page/contact-us?token=auth_token">'
         '[CONTACTER LE SUPPORT]</a> </b></span></p>'
         f'<p style="line-height:1.38;margin-top:12pt;margin-bottom:12pt;">'
         f'<span style="{S_WC}">Si vous avez besoin d\u2019aide imm\u00e9diatement, vous pouvez \u00e9galement nous contacter via le chat en direct sur notre site.</span></p>'
         f'<p style="line-height:1.38;margin-top:12pt;margin-bottom:12pt;">'
         f'<span style="{S_WC}">Merci,</span>'
         f'<span style="{S_WC}"><br></span>'
         f'<span style="{S_WC}">Alex, Support HeyHo</span></p></td>')

if old4b in content:
    content = content.replace(old4b, new4b, 1); fixes += 1
    print('Fix 4b OK: Email 3 fr-FR — fixed CONTACTER LE SUPPORT block + signature')
else:
    print('WARN: Fix 4b NOT FOUND')


# ===== FIX 5a: Email 5 Default — inline buttons -> separate <p> blocks =====
old5en = (
    f"If you'd like, I can help you finish it quickly. Tap below to try again.</span>"
    f'<span style="{S_WC}"><br></span>'
    f'<span style="{S_WC}">Try Again: </span>'
    f'<a target="_blank" href="https://heyhocasino.com/en/wallet/deposit" style="background-color: transparent; font-family: Arial, sans-serif; font-size: 11pt; white-space-collapse: preserve;"><b>[COMPLETE DEPOSIT]</b></a>'
    f'<b style="background-color: transparent; color: rgb(0, 0, 0); font-family: Arial, sans-serif; font-size: 11pt; white-space-collapse: preserve;"> \n\n</b>'
    f'<span style="{S_WC}">Or contact us.</span>'
    f'<span style="{S_WC}"><br></span>'
    f'<span style="{S_WC}">Support: </span>'
    f'<a target="_blank" href="https://heyhocasino.com/en/page/contact-us?token=auth_token" style="background-color: transparent; font-family: Arial, sans-serif; font-size: 11pt; white-space-collapse: preserve;"><b>[CONTACT SUPPORT]</b></a>'
    f'<b style="background-color: transparent; color: rgb(0, 0, 0); font-family: Arial, sans-serif; font-size: 11pt; white-space-collapse: preserve;"> </b></p>'
)
new5en = (
    f"If you'd like, I can help you finish it quickly. Tap below to try again.</span></p>"
    + make_btn_p('https://heyhocasino.com/en/wallet/deposit', 'COMPLETE DEPOSIT')
    + make_btn_p('https://heyhocasino.com/en/page/contact-us?token=auth_token', 'CONTACT SUPPORT')
    + '<p style="line-height:1.38;margin-top:12pt;margin-bottom:12pt;">'
)
if old5en in content:
    content = content.replace(old5en, new5en, 1); fixes += 1
    print('Fix 5a OK: Email 5 Default — standardized buttons')
else:
    print('WARN: Fix 5a NOT FOUND')


# ===== FIX 5b: Email 5 de-DE — inline buttons -> separate <p> blocks =====
old5de = (
    f'Wenn du m\u00f6chtest, helfe ich dir, sie schnell abzuschlie\u00dfen. Klicke unten, um es erneut zu versuchen.</span>'
    f'<span style="{S_INNER}"><br></span>'
    f'<span style="{S_INNER}">Erneut versuchen: </span></span>'
    f'<span style="{S_WC}"><b><a target="_blank" href="https://heyhocasino.com/de/wallet/deposit">[EINZAHLUNG ABSCHLIESSEN]</a> </b></span>'
    f'<span style="{S_WC}"><br></span>'
    f'<span style="{S_WC}"><br></span>'
    f'<span style="{S_WC}"><span style="{S_INNER}">Oder kontaktieren Sie uns.</span>'
    f'<span style="{S_INNER}"><br></span>'
    f'<span style="{S_INNER}">Support: </span>'
    f'<b><a target="_blank" href="https://heyhocasino.com/de/page/contact-us?token=auth_token">[KONTAKTIERE DEN SUPPORT]</a> </b></span>'
)
new5de = (
    f'Wenn du m\u00f6chtest, helfe ich dir, sie schnell abzuschlie\u00dfen. Klicke unten, um es erneut zu versuchen.</span></span></p>'
    + make_btn_p('https://heyhocasino.com/de/wallet/deposit', 'EINZAHLUNG ABSCHLIESSEN')
    + make_btn_p('https://heyhocasino.com/de/page/contact-us?token=auth_token', 'KONTAKTIERE DEN SUPPORT')
    + f'<p style="line-height:1.38;margin-top:12pt;margin-bottom:12pt;"><span style="{S_WC}">'
)
if old5de in content:
    content = content.replace(old5de, new5de, 1); fixes += 1
    print('Fix 5b OK: Email 5 de-DE — standardized buttons')
else:
    print('WARN: Fix 5b NOT FOUND')


# ===== FIX 5c: Email 5 fr-FR — inline buttons -> separate <p> blocks =====
old5fr = (
    f'Si vous le souhaitez, je peux vous aider \u00e0 le terminer rapidement. Cliquez ci-dessous pour r\u00e9essayer.</span>'
    f'<span style="{S_INNER}"><br></span>'
    f'<span style="{S_INNER}">R\u00e9essayer\u00a0: </span></span>'
    f'<span style="{S_PRE}"><a target="_blank" href="https://heyhocasino.com/fr/wallet/deposit"><b>[COMPL\u00c9TER LE D\u00c9P\u00d4T]</b></a><b> </b></span>'
    f'<span style="{S_PRE}"><br></span>'
    f'<span style="{S_PRE}"><br></span>'
    f'<span style="{S_PRE}"><span style="{S_INNER}">Ou contactez-nous.</span>'
    f'<span style="{S_INNER}"><br></span>'
    f'<span style="{S_INNER}">Support\u00a0: </span>'
    f'<b><a target="_blank" href="https://heyhocasino.com/fr/page/contact-us?token=auth_token">[CONTACTER LE SUPPORT]</a> </b></span>'
    f'<span style="{S_PRE}"><br></span>'
    f'<span style="{S_PRE}"><br></span></p>'
)
new5fr = (
    f'Si vous le souhaitez, je peux vous aider \u00e0 le terminer rapidement. Cliquez ci-dessous pour r\u00e9essayer.</span></span></p>'
    + make_btn_p('https://heyhocasino.com/fr/wallet/deposit', 'COMPL\u00c9TER LE D\u00c9P\u00d4T')
    + make_btn_p('https://heyhocasino.com/fr/page/contact-us?token=auth_token', 'CONTACTER LE SUPPORT')
    + '<p style="line-height:1.38;margin-top:12pt;margin-bottom:12pt;">'
)
if old5fr in content:
    content = content.replace(old5fr, new5fr, 1); fixes += 1
    print('Fix 5c OK: Email 5 fr-FR — standardized buttons')
else:
    print('WARN: Fix 5c NOT FOUND')


# ===== FIX 5d: Email 5 nl-NL — bare span + inline buttons -> separate <p> blocks =====
old5nl = (
    f'Als je wilt, help ik je om het snel af te ronden. Klik hieronder om het opnieuw te proberen.</span>'
    f'<span style="{S_INNER}"><br></span>'
    f'<span style="{S_INNER}">Opnieuw proberen: </span></span>'
    f'<span style="{S_PRE}"><b><a target="_blank" href="https://heyhocasino.com/nl/wallet/deposit">[STORTING VOLTOOIEN]</a> </b></span></p>'
    f'<span style="{S_WC}">Of neem contact met ons op.</span>'
    f'<span style="{S_WC}"><br></span>'
    f'<p style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;">'
    f'<span style="{S_WC}"><span style="background-color: transparent; font-size: 11pt;">Support: </span>'
    f'<b><a target="_blank" href="https://heyhocasino.com/nl/page/contact-us?token=auth_token">[CONTACT MET SUPPORT]</a> </b></span>'
)
new5nl = (
    f'Als je wilt, help ik je om het snel af te ronden. Klik hieronder om het opnieuw te proberen.</span></span></p>'
    + make_btn_p('https://heyhocasino.com/nl/wallet/deposit', 'STORTING VOLTOOIEN')
    + make_btn_p('https://heyhocasino.com/nl/page/contact-us?token=auth_token', 'CONTACT MET SUPPORT')
    + f'<p style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;"><span style="{S_WC}">'
)
if old5nl in content:
    content = content.replace(old5nl, new5nl, 1); fixes += 1
    print('Fix 5d OK: Email 5 nl-NL — standardized buttons')
else:
    print('WARN: Fix 5d NOT FOUND')


# ===== SAVE =====
print(f'\nTotal fixes applied: {fixes}')
with open(fp, 'w', encoding='utf-8') as f:
    f.write(content)
print('File saved.')
