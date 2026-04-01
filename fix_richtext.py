"""Fix rich_text emails in Unsuccessful Deposit campaign."""
import re

fp = 'тексти/хейхо/Unsuccessful Deposit - Table data.txt'
with open(fp, 'r', encoding='utf-8') as f:
    content = f.read()

fixes = 0

# ===== FIX 1: Email 2 Default - Thanks/HeyHo Support outside <p> tags =====
# Bare <span>Thanks,</span><span><br></span><span>HeyHo Support</span> before </td>
# Need to wrap in <p> tags
old = 'disappears automatically according to your bank\'s rules.</span></p><span style="font-size: 11pt; font-family: Arial, sans-serif; color: rgb(0, 0, 0); background-color: transparent; font-variant-numeric: normal; font-variant-east-asian: normal; font-variant-alternates: normal; font-variant-position: normal; font-variant-emoji: normal; vertical-align: baseline; white-space-collapse: preserve;">Thanks,</span><span style="font-size: 11pt; font-family: Arial, sans-serif; color: rgb(0, 0, 0); background-color: transparent; font-variant-numeric: normal; font-variant-east-asian: normal; font-variant-alternates: normal; font-variant-position: normal; font-variant-emoji: normal; vertical-align: baseline; white-space-collapse: preserve;"><br></span><span style="font-size: 11pt; font-family: Arial, sans-serif; color: rgb(0, 0, 0); background-color: transparent; font-variant-numeric: normal; font-variant-east-asian: normal; font-variant-alternates: normal; font-variant-position: normal; font-variant-emoji: normal; vertical-align: baseline; white-space-collapse: preserve;">HeyHo Support</span></td>'

new = 'disappears automatically according to your bank\'s rules.</span></p><p style="line-height:1.38;margin-top:12pt;margin-bottom:12pt;"><span style="font-size: 11pt; font-family: Arial, sans-serif; color: rgb(0, 0, 0); background-color: transparent; font-variant-numeric: normal; font-variant-east-asian: normal; font-variant-alternates: normal; font-variant-position: normal; font-variant-emoji: normal; vertical-align: baseline; white-space-collapse: preserve;">Thanks,</span><span style="font-size: 11pt; font-family: Arial, sans-serif; color: rgb(0, 0, 0); background-color: transparent; font-variant-numeric: normal; font-variant-east-asian: normal; font-variant-alternates: normal; font-variant-position: normal; font-variant-emoji: normal; vertical-align: baseline; white-space-collapse: preserve;"><br></span><span style="font-size: 11pt; font-family: Arial, sans-serif; color: rgb(0, 0, 0); background-color: transparent; font-variant-numeric: normal; font-variant-east-asian: normal; font-variant-alternates: normal; font-variant-position: normal; font-variant-emoji: normal; vertical-align: baseline; white-space-collapse: preserve;">HeyHo Support</span></p></td>'

if old in content:
    content = content.replace(old, new, 1)
    fixes += 1
    print('Fix 1: Email 2 Default - wrapped Thanks/HeyHo Support in <p>')
else:
    print('WARN: Fix 1 not found')


# ===== FIX 2: Email 2 fr-FR - truncated 'Hey' -> 'HeyHo' =====
old2 = "L'équipe support Hey</span>"
new2 = "L'équipe support HeyHo</span>"
if old2 in content:
    content = content.replace(old2, new2, 1)
    fixes += 1
    print("Fix 2: Email 2 fr-FR - 'Hey' -> 'HeyHo'")
else:
    print('WARN: Fix 2 not found')


# ===== FIX 3: nl-NL /fr/ -> /nl/ in contact-us URLs =====
# All nl-NL locales have /fr/ in contact-us links
old3 = 'heyhocasino.com/fr/page/contact-us?token=auth_token">[CONTACT MET SUPPORT]'
new3 = 'heyhocasino.com/nl/page/contact-us?token=auth_token">[CONTACT MET SUPPORT]'
count3 = content.count(old3)
if count3 > 0:
    content = content.replace(old3, new3)
    fixes += count3
    print(f'Fix 3: nl-NL /fr/ -> /nl/ for CONTACT MET SUPPORT ({count3}x)')
else:
    print('WARN: Fix 3 not found')


# ===== FIX 4: Email 3 fr-FR - broken HTML structure =====
# Has <font><br></font> before deposit button, and raw line breaks after support button
# Find the Email 3 fr-FR rich_text and replace it entirely

# Parse line by line to find and replace specific rich_text blocks
lines = content.split('\n')
i = 0
email3_fr_fixed = False
email5_default_fixed = False
email5_de_fixed = False
email5_fr_fixed = False
email5_nl_fixed = False

# Standard span style used across the file
S_WC = 'font-size: 11pt; font-family: Arial, sans-serif; color: rgb(0, 0, 0); background-color: transparent; font-variant-numeric: normal; font-variant-east-asian: normal; font-variant-alternates: normal; font-variant-position: normal; font-variant-emoji: normal; vertical-align: baseline; white-space-collapse: preserve;'
S_PRE = 'font-size:11pt;font-family:Arial,sans-serif;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;'
S_INNER = 'font-size: 11pt; background-color: transparent; font-variant-numeric: normal; font-variant-east-asian: normal; font-variant-alternates: normal; font-variant-position: normal; font-variant-emoji: normal; vertical-align: baseline;'

def make_btn_paragraph(href, label):
    """Create a standardized button paragraph matching Email 2/3 Default style."""
    return f'<p style="line-height:1.38;margin-top:12pt;margin-bottom:12pt;"><span style="{S_WC}"><a target="_blank" href="{href}"><b>[{label}]</b></a><b> </b></span></p>'

def make_text_paragraph(text):
    """Create standard text paragraph."""
    return f'<p style="line-height:1.38;margin-top:12pt;margin-bottom:12pt;"><span style="{S_WC}">{text}</span></p>'

def make_sign_paragraph(line1, line2):
    """Create signature paragraph: line1<br>line2."""
    return f'<p style="line-height:1.38;margin-top:12pt;margin-bottom:12pt;"><span style="{S_WC}">{line1}</span><span style="{S_WC}"><br></span><span style="{S_WC}">{line2}</span></p>'


while i < len(lines):
    line = lines[i]
    
    # Identify Email 3 fr-FR by looking for name + locale pattern
    if line.startswith('name: Email 3') and i+1 < len(lines) and lines[i+1].strip() == 'locale: fr-FR':
        # Find the rich_text line
        for j in range(i+2, min(i+10, len(lines))):
            if lines[j].startswith('rich_text:'):
                # Replace the entire rich_text value for Email 3 fr-FR
                # Build correct rich_text
                rt = '<td>'
                rt += f'<p style="line-height:1.38;margin-top:12pt;margin-bottom:12pt;"><span style="{S_WC}">Ravi de te rencontrer, '
                rt += '{{ customer.first_name | default:&quot;ami&quot; | capitalize }} !</span><span style="' + S_WC + '"><br></span><span style="' + S_WC + '">'
                # Actually, let me keep the original text content but fix the HTML structure
                # I'll just re-read the broken line and extract the text content
                break
        # Too complex to rebuild from scratch without losing text. Let me do targeted fixes instead.
        pass
    i += 1

# ----- FIX 4: Email 3 fr-FR - fix <font><br></font> and raw line breaks -----
# Replace <font><br></font> with proper spacing
old4 = '<font><br></font><a target="_blank" href="https://heyhocasino.com/fr/wallet/deposit"'
new4 = '<span style="' + S_WC + '"><br></span><span style="' + S_WC + '"><br></span><span style="' + S_WC + '"><a target="_blank" href="https://heyhocasino.com/fr/wallet/deposit"'
if old4 in content:
    content = content.replace(old4, new4, 1)
    fixes += 1
    print('Fix 4a: Email 3 fr-FR - replaced <font><br></font> with proper spans')
else:
    print('WARN: Fix 4a not found')

# Fix the messy part after [CONTACTER LE SUPPORT] button - raw line breaks and text outside proper tags
old4b = '''[CONTACTER LE SUPPORT]</a> \n</b></span><span style="background-color: transparent; color: rgb(0, 0, 0); font-family: Arial, sans-serif; font-size: 11pt; white-space-collapse: preserve;"> \nSi vous avez besoin d\u2019aide imm\u00e9diatement, vous pouvez \u00e9galement nous contacter via le chat en direct sur notre site.\n</span><span style="background-color: transparent; color: rgb(0, 0, 0); font-family: Arial, sans-serif; font-size: 11pt; white-space-collapse: preserve;">     \nMerci,\n</span><span style="background-color: transparent; color: rgb(0, 0, 0); font-family: Arial, sans-serif; font-size: 11pt; white-space-collapse: preserve;">Alex, Support HeyHo</span></p></td>'''

new4b = '[CONTACTER LE SUPPORT]</a><b> </b></span></p>'
new4b += '<p style="line-height:1.38;margin-top:12pt;margin-bottom:12pt;">'
new4b += f'<span style="{S_WC}">Si vous avez besoin d\u2019aide imm\u00e9diatement, vous pouvez \u00e9galement nous contacter via le chat en direct sur notre site.</span></p>'
new4b += '<p style="line-height:1.38;margin-top:12pt;margin-bottom:12pt;">'
new4b += f'<span style="{S_WC}">Merci,</span>'
new4b += f'<span style="{S_WC}"><br></span>'
new4b += f'<span style="{S_WC}">Alex, Support HeyHo</span></p></td>'

if old4b in content:
    content = content.replace(old4b, new4b, 1)
    fixes += 1
    print('Fix 4b: Email 3 fr-FR - fixed broken structure after CONTACTER LE SUPPORT')
else:
    print('WARN: Fix 4b not found')


# ===== FIX 5: Email 5 - standardize inline buttons to separate paragraphs =====

# Email 5 Default - inline "Try Again: [COMPLETE DEPOSIT]" and "Support: [CONTACT SUPPORT]"
# Need to make them separate <p> blocks like Email 2/3
old5_en = '''If you'd like, I can help you finish it quickly. Tap below to try again.</span><span style="''' + S_WC + '''"><br></span><span style="''' + S_WC + '''">Try Again: </span><a target="_blank" href="https://heyhocasino.com/en/wallet/deposit" style="background-color: transparent; font-family: Arial, sans-serif; font-size: 11pt; white-space-collapse: preserve;"><b>[COMPLETE DEPOSIT]</b></a><b style="background-color: transparent; color: rgb(0, 0, 0); font-family: Arial, sans-serif; font-size: 11pt; white-space-collapse: preserve;"> \n\n</b><span style="''' + S_WC + '''">Or contact us.</span><span style="''' + S_WC + '''"><br></span><span style="''' + S_WC + '''">Support: </span><a target="_blank" href="https://heyhocasino.com/en/page/contact-us?token=auth_token" style="background-color: transparent; font-family: Arial, sans-serif; font-size: 11pt; white-space-collapse: preserve;"><b>[CONTACT SUPPORT]</b></a><b style="background-color: transparent; color: rgb(0, 0, 0); font-family: Arial, sans-serif; font-size: 11pt; white-space-collapse: preserve;"> </b></p>'''

new5_en = f'If you\'d like, I can help you finish it quickly. Tap below to try again.</span></p>'
new5_en += make_btn_paragraph('https://heyhocasino.com/en/wallet/deposit', 'COMPLETE DEPOSIT')
new5_en += make_btn_paragraph('https://heyhocasino.com/en/page/contact-us?token=auth_token', 'CONTACT SUPPORT')
new5_en += f'<p style="line-height:1.38;margin-top:12pt;margin-bottom:12pt;">'

if old5_en in content:
    content = content.replace(old5_en, new5_en, 1)
    fixes += 1
    print('Fix 5a: Email 5 Default - standardized button structure')
else:
    print('WARN: Fix 5a not found')

# Email 5 de-DE - inline buttons
old5_de_btn = 'Wenn du möchtest, helfe ich dir, sie schnell abzuschließen. Klicke unten, um es erneut zu versuchen.</span><span style="' + S_INNER + '"><br></span><span style="' + S_INNER + '">Erneut versuchen: </span></span><span style="' + S_WC + '"><b><a target="_blank" href="https://heyhocasino.com/de/wallet/deposit">[EINZAHLUNG ABSCHLIESSEN]</a> </b></span><span style="' + S_WC + '"><br></span><span style="' + S_WC + '"><br></span><span style="' + S_WC + '"><span style="' + S_INNER + '">Oder kontaktieren Sie uns.</span><span style="' + S_INNER + '"><br></span><span style="' + S_INNER + '">Support: </span><b><a target="_blank" href="https://heyhocasino.com/de/page/contact-us?token=auth_token">[KONTAKTIERE DEN SUPPORT]</a> </b></span>'

new5_de_btn = 'Wenn du möchtest, helfe ich dir, sie schnell abzuschließen. Klicke unten, um es erneut zu versuchen.</span></span></p>'
new5_de_btn += make_btn_paragraph('https://heyhocasino.com/de/wallet/deposit', 'EINZAHLUNG ABSCHLIESSEN')
new5_de_btn += make_btn_paragraph('https://heyhocasino.com/de/page/contact-us?token=auth_token', 'KONTAKTIERE DEN SUPPORT')
new5_de_btn += f'<p style="line-height:1.38;margin-top:12pt;margin-bottom:12pt;"><span style="{S_WC}">'

if old5_de_btn in content:
    content = content.replace(old5_de_btn, new5_de_btn, 1)
    fixes += 1
    print('Fix 5b: Email 5 de-DE - standardized button structure')
else:
    print('WARN: Fix 5b not found - trying to find it...')
    # Check if the substring exists partially
    if 'Erneut versuchen: </span></span>' in content:
        print('  Found "Erneut versuchen" pattern')
    if 'Oder kontaktieren Sie uns.' in content:
        print('  Found "Oder kontaktieren" pattern')

# Email 5 fr-FR - inline buttons  
old5_fr_btn = 'Si vous le souhaitez, je peux vous aider à le terminer rapidement. Cliquez ci-dessous pour réessayer.</span><span style="' + S_INNER + '"><br></span><span style="' + S_INNER + '">Réessayer : </span></span><span style="' + S_PRE + '"><a target="_blank" href="https://heyhocasino.com/fr/wallet/deposit"><b>[COMPLÉTER LE DÉPÔT]</b></a><b> </b></span><span style="' + S_PRE + '"><br></span><span style="' + S_PRE + '"><br></span><span style="' + S_PRE + '"><span style="' + S_INNER + '">Ou contactez-nous.</span><span style="' + S_INNER + '"><br></span><span style="' + S_INNER + '">Support : </span><b><a target="_blank" href="https://heyhocasino.com/fr/page/contact-us?token=auth_token">[CONTACTER LE SUPPORT]</a> </b></span><span style="' + S_PRE + '"><br></span><span style="' + S_PRE + '"><br></span></p>'

new5_fr_btn = 'Si vous le souhaitez, je peux vous aider à le terminer rapidement. Cliquez ci-dessous pour réessayer.</span></span></p>'
new5_fr_btn += make_btn_paragraph('https://heyhocasino.com/fr/wallet/deposit', 'COMPLÉTER LE DÉPÔT')
new5_fr_btn += make_btn_paragraph('https://heyhocasino.com/fr/page/contact-us?token=auth_token', 'CONTACTER LE SUPPORT')
new5_fr_btn += '<p style="line-height:1.38;margin-top:12pt;margin-bottom:12pt;">'

if old5_fr_btn in content:
    content = content.replace(old5_fr_btn, new5_fr_btn, 1)
    fixes += 1
    print('Fix 5c: Email 5 fr-FR - standardized button structure')
else:
    print('WARN: Fix 5c not found')

# Email 5 nl-NL - inline buttons + bare span outside <p>
old5_nl_btn = '''Als je wilt, help ik je om het snel af te ronden. Klik hieronder om het opnieuw te proberen.</span><span style="''' + S_INNER + '''"><br></span><span style="''' + S_INNER + '''">Opnieuw proberen: </span></span><span style="''' + S_PRE + '''"><b><a target="_blank" href="https://heyhocasino.com/nl/wallet/deposit">[STORTING VOLTOOIEN]</a> </b></span></p><span style="''' + S_WC + '''">Of neem contact met ons op.</span><span style="''' + S_WC + '''"><br></span><p style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;"><span style="''' + S_WC + '''"><span style="background-color: transparent; font-size: 11pt;">Support: </span><b><a target="_blank" href="https://heyhocasino.com/nl/page/contact-us?token=auth_token">[CONTACT MET SUPPORT]</a> </b></span>'''

new5_nl_btn = 'Als je wilt, help ik je om het snel af te ronden. Klik hieronder om het opnieuw te proberen.</span></span></p>'
new5_nl_btn += make_btn_paragraph('https://heyhocasino.com/nl/wallet/deposit', 'STORTING VOLTOOIEN')
new5_nl_btn += make_btn_paragraph('https://heyhocasino.com/nl/page/contact-us?token=auth_token', 'CONTACT MET SUPPORT')
new5_nl_btn += f'<p style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;"><span style="{S_WC}">'

if old5_nl_btn in content:
    content = content.replace(old5_nl_btn, new5_nl_btn, 1)
    fixes += 1
    print('Fix 5d: Email 5 nl-NL - standardized button structure')
else:
    print('WARN: Fix 5d not found')

print(f'\nTotal fixes: {fixes}')

with open(fp, 'w', encoding='utf-8') as f:
    f.write(content)

print('File saved.')
