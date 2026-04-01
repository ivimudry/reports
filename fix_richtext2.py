"""Fix remaining 4 issues in Unsuccessful Deposit rich_text emails."""

fp = 'тексти/хейхо/Unsuccessful Deposit - Table data.txt'
with open(fp, 'r', encoding='utf-8') as f:
    content = f.read()

fixes = 0

S_WC = 'font-size: 11pt; font-family: Arial, sans-serif; color: rgb(0, 0, 0); background-color: transparent; font-variant-numeric: normal; font-variant-east-asian: normal; font-variant-alternates: normal; font-variant-position: normal; font-variant-emoji: normal; vertical-align: baseline; white-space-collapse: preserve;'
S_PRE = 'font-size:11pt;font-family:Arial,sans-serif;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;'
S_INNER = 'font-size: 11pt; background-color: transparent; font-variant-numeric: normal; font-variant-east-asian: normal; font-variant-alternates: normal; font-variant-position: normal; font-variant-emoji: normal; vertical-align: baseline;'

def make_btn_p(href, label):
    return (f'<p style="line-height:1.38;margin-top:12pt;margin-bottom:12pt;">'
            f'<span style="{S_WC}"><a target="_blank" href="{href}">'
            f'<b>[{label}]</b></a><b> </b></span></p>')


# ===== FIX 1: Email 2 Default — bare <span> before </td> =====
# The issue: after bank's rules.</span></p> there are bare <span> tags without <p> wrapper
old1 = (
    "according to your bank\u2019s rules.</span></p>"
    f'<span style="{S_WC}">Thanks,</span>'
    f'<span style="{S_WC}"><br></span>'
    f'<span style="{S_WC}">HeyHo Support</span></td>'
)
if old1 not in content:
    # Try ASCII apostrophe
    old1 = (
        "according to your bank's rules.</span></p>"
        f'<span style="{S_WC}">Thanks,</span>'
        f'<span style="{S_WC}"><br></span>'
        f'<span style="{S_WC}">HeyHo Support</span></td>'
    )

new1 = old1.replace('rules.</span></p><span', 'rules.</span></p><p style="line-height:1.38;margin-top:12pt;margin-bottom:12pt;"><span').replace('Support</span></td>', 'Support</span></p></td>')

if old1 in content:
    content = content.replace(old1, new1, 1)
    fixes += 1
    print('Fix 1 OK: Email 2 Default — wrapped Thanks/HeyHo Support in <p>')
else:
    print('WARN: Fix 1 NOT FOUND')


# ===== FIX 2: Email 2 fr-FR — "Hey" -> "HeyHo" =====
old2 = "support Hey</span></p></td>"
new2 = "support HeyHo</span></p></td>"
if old2 in content:
    content = content.replace(old2, new2, 1)
    fixes += 1
    print('Fix 2 OK: fr-FR Hey -> HeyHo')
else:
    print('WARN: Fix 2 NOT FOUND')


# ===== FIX 4b: Email 3 fr-FR — raw newlines after CONTACTER LE SUPPORT =====
old4b = ('[CONTACTER LE SUPPORT]</a> \n</b></span>'
         '<span style="background-color: transparent; color: rgb(0, 0, 0); font-family: Arial, sans-serif; font-size: 11pt; white-space-collapse: preserve;">'
         '\nSi vous avez besoin d\u2019aide imm\u00e9diatement, vous pouvez \u00e9galement nous contacter via le chat en direct sur notre site.\n</span>'
         '<span style="background-color: transparent; color: rgb(0, 0, 0); font-family: Arial, sans-serif; font-size: 11pt; white-space-collapse: preserve;">')

# Get the rest
idx4 = content.find(old4b)
if idx4 >= 0:
    # Find the end of this block (up to </td>)
    end4 = content.find('</td>', idx4)
    block = content[idx4:end4+5]
    print(f'Fix 4b: found block len={len(block)}')
    print(repr(block[-200:]))
    
    new4b = ('[CONTACTER LE SUPPORT]</a> </b></span></p>'
             f'<p style="line-height:1.38;margin-top:12pt;margin-bottom:12pt;">'
             f'<span style="{S_WC}">Si vous avez besoin d\u2019aide imm\u00e9diatement, vous pouvez \u00e9galement nous contacter via le chat en direct sur notre site.</span></p>'
             f'<p style="line-height:1.38;margin-top:12pt;margin-bottom:12pt;">'
             f'<span style="{S_WC}">Merci,</span>'
             f'<span style="{S_WC}"><br></span>'
             f'<span style="{S_WC}">Alex, Support HeyHo</span></p></td>')
    
    content = content[:idx4] + new4b + content[end4+5:]
    fixes += 1
    print('Fix 4b OK: Email 3 fr-FR — fixed structure after CONTACTER LE SUPPORT')
else:
    # Try with smart quotes
    old4b_alt = old4b.replace("d\u2019aide", "d'aide")
    idx4 = content.find(old4b_alt)
    if idx4 >= 0:
        end4 = content.find('</td>', idx4)
        block = content[idx4:end4+5]
        
        new4b = ('[CONTACTER LE SUPPORT]</a> </b></span></p>'
                 f'<p style="line-height:1.38;margin-top:12pt;margin-bottom:12pt;">'
                 f'<span style="{S_WC}">Si vous avez besoin d\u2019aide imm\u00e9diatement, vous pouvez \u00e9galement nous contacter via le chat en direct sur notre site.</span></p>'
                 f'<p style="line-height:1.38;margin-top:12pt;margin-bottom:12pt;">'
                 f'<span style="{S_WC}">Merci,</span>'
                 f'<span style="{S_WC}"><br></span>'
                 f'<span style="{S_WC}">Alex, Support HeyHo</span></p></td>')
        
        content = content[:idx4] + new4b + content[end4+5:]
        fixes += 1
        print('Fix 4b OK (alt): Email 3 fr-FR — fixed structure')
    else:
        print('WARN: Fix 4b NOT FOUND')


# ===== FIX 5a: Email 5 Default — inline buttons =====
old5en = (
    f'<span style="{S_WC}">Try Again: </span>'
    '<a target="_blank" href="https://heyhocasino.com/en/wallet/deposit" '
    'style="background-color: transparent; font-family: Arial, sans-serif; font-size: 11pt; white-space-collapse: preserve;">'
    '<b>[COMPLETE DEPOSIT]</b></a>'
    '<b style="background-color: transparent; color: rgb(0, 0, 0); font-family: Arial, sans-serif; font-size: 11pt; white-space-collapse: preserve;"> \n\n</b>'
    f'<span style="{S_WC}">Or contact us.</span>'
    f'<span style="{S_WC}"><br></span>'
    f'<span style="{S_WC}">Support: </span>'
    '<a target="_blank" href="https://heyhocasino.com/en/page/contact-us?token=auth_token" '
    'style="background-color: transparent; font-family: Arial, sans-serif; font-size: 11pt; white-space-collapse: preserve;">'
    '<b>[CONTACT SUPPORT]</b></a>'
    '<b style="background-color: transparent; color: rgb(0, 0, 0); font-family: Arial, sans-serif; font-size: 11pt; white-space-collapse: preserve;"> </b></p>'
)

# Also need to capture what's before "Try Again" - find the text that leads to it
idx5a = content.find('Try Again: </span><a target="_blank"')
if idx5a >= 0:
    # Go back to find the <br> before "Try Again"
    before5a = content[idx5a-200:idx5a]
    print(f'=== before Try Again ===')
    print(repr(before5a[-150:]))

new5en = (
    f'</span></p>'
    + make_btn_p('https://heyhocasino.com/en/wallet/deposit', 'COMPLETE DEPOSIT')
    + make_btn_p('https://heyhocasino.com/en/page/contact-us?token=auth_token', 'CONTACT SUPPORT')
    + '<p style="line-height:1.38;margin-top:12pt;margin-bottom:12pt;">'
)

if old5en in content:
    # Need to also remove the preceding <br> and "tap below" text break
    # Find larger context
    pre = f'Tap below to try again.</span><span style="{S_WC}"><br></span>'
    full_old = pre + old5en
    full_new = 'Tap below to try again.</span></p>' + make_btn_p('https://heyhocasino.com/en/wallet/deposit', 'COMPLETE DEPOSIT') + make_btn_p('https://heyhocasino.com/en/page/contact-us?token=auth_token', 'CONTACT SUPPORT') + '<p style="line-height:1.38;margin-top:12pt;margin-bottom:12pt;">'
    
    if full_old in content:
        content = content.replace(full_old, full_new, 1)
        fixes += 1
        print('Fix 5a OK: Email 5 Default — standardized buttons')
    else:
        print('WARN: Fix 5a full context NOT FOUND')
else:
    print('WARN: Fix 5a NOT FOUND')


# ===== FIX 5c: Email 5 fr-FR — inline buttons =====
# The fr-FR uses "Réessayer :" (non-breaking space before colon) 
old5fr = (
    f'R\u00e9essayer\u00a0: </span></span>'
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

if old5fr in content:
    # Need to also capture preceding text
    pre5fr = f'Cliquez ci-dessous pour r\u00e9essayer.</span><span style="{S_INNER}"><br></span><span style="{S_INNER}">'
    full5fr = pre5fr + old5fr
    if full5fr in content:
        new5fr = (f'Cliquez ci-dessous pour r\u00e9essayer.</span></span></p>'
                  + make_btn_p('https://heyhocasino.com/fr/wallet/deposit', 'COMPL\u00c9TER LE D\u00c9P\u00d4T')
                  + make_btn_p('https://heyhocasino.com/fr/page/contact-us?token=auth_token', 'CONTACTER LE SUPPORT')
                  + '<p style="line-height:1.38;margin-top:12pt;margin-bottom:12pt;">')
        content = content.replace(full5fr, new5fr, 1)
        fixes += 1
        print('Fix 5c OK: Email 5 fr-FR — standardized buttons')
    else:
        print('WARN: Fix 5c with context NOT FOUND')
        # Try standalone
        content = content.replace(old5fr, '</span></p>' + make_btn_p('https://heyhocasino.com/fr/wallet/deposit', 'COMPL\u00c9TER LE D\u00c9P\u00d4T') + make_btn_p('https://heyhocasino.com/fr/page/contact-us?token=auth_token', 'CONTACTER LE SUPPORT') + '<p style="line-height:1.38;margin-top:12pt;margin-bottom:12pt;">', 1)
        fixes += 1
        print('Fix 5c OK (standalone): Email 5 fr-FR')
else:
    print('WARN: Fix 5c base NOT FOUND')
    # Check what's actually there
    idx = content.find('Réessayer')
    if idx >= 0:
        print(repr(content[idx:idx+400]))


print(f'\nTotal fixes applied: {fixes}')
with open(fp, 'w', encoding='utf-8') as f:
    f.write(content)
print('File saved.')
