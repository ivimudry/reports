#!/usr/bin/env python3
"""Generate HTML files from Oshi newsletter texts and banners."""
import re, os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

INPUT_TEXTS   = 'oshi newsletters texts EN-DE.txt'
INPUT_BANNERS = 'oshi newsletters banners EN-DE.txt'
OUTPUT_TEXTS  = 'Oshi Newsletters.html'
OUTPUT_BANNERS = 'Oshi Newsletter Banners.html'

GAME_NAMES = [
    'Elvis Frog TRUEWAYS', 'Gates of Olympus', 'Sweet Bonanza',
    'Hold The Gold', 'Sugar Rush', 'Clover Gold', 'Gemhalla',
    'Pragmatic Play', 'Big Bass Bonanza', 'Hand of Midas 2',
    'Book of Dead', '3 Coins', 'Starburst',
]

CSS = ('body{font-family:Arial,sans-serif;font-size:14px;line-height:1.6;'
       'max-width:800px;margin:40px auto;color:#222;}'
       'h2{margin-top:40px;border-bottom:2px solid #333;padding-bottom:4px;color:#111;}'
       'h3{margin-top:28px;border-bottom:1px solid #ccc;padding-bottom:4px;color:#444;font-size:15px;}'
       '.tc{font-size:12px;color:#666;margin-top:2px;}')

# ── Bold formatting ──────────────────────────────────────────
def boldify(text):
    # Protect liquid tags
    lq = {}
    for i, m in enumerate(re.finditer(r'\{\{.*?\}\}', text)):
        ph = f'@@LQ{i}@@'
        lq[ph] = m.group(0)
    for ph, orig in lq.items():
        text = text.replace(orig, ph)

    # Protect game names
    gm = {}
    for i, name in enumerate(sorted(GAME_NAMES, key=len, reverse=True)):
        ph = f'@@GM{i}@@'
        text = text.replace(name, ph)
        gm[ph] = f'<b>{name}</b>'

    # Free Spins / Freispiele
    text = re.sub(r'\b(\d+\s+Free Spins?)\b', r'<b>\1</b>', text)
    text = re.sub(r'\b(\d+\s+Freispiele)\b', r'<b>\1</b>', text)

    # EUR amounts  (30 EUR, 350 EUR, 5,000 EUR, 10.000 EUR)
    text = re.sub(r'\b(\d{1,3}(?:[.,]\d{3})*\s+EUR)\b', r'<b>\1</b>', text)

    # Percentages
    text = re.sub(r'\b(\d+%)', r'<b>\1</b>', text)

    # Bonus codes after code / Code / Bonuscode (no (?i) — [A-Z] must stay uppercase)
    text = re.sub(r'([Cc]ode\s+)([A-Z][A-Z0-9]{2,})', r'\1<b>\2</b>', text)
    text = re.sub(r'([Bb]onus\s*[Cc]ode\s+)([A-Z][A-Z0-9]{2,})', r'\1<b>\2</b>', text)
    text = re.sub(r'(Bonuscode\s+)([A-Z][A-Z0-9]{2,})', r'\1<b>\2</b>', text)

    # Known standalone promo codes
    for code in ['SILVER', 'GOLD', 'STELLAR', 'UNIVERSE', 'SPECTRUM']:
        text = re.sub(rf'\b({code})\b', r'<b>\1</b>', text)

    # Restore game names & liquid tags
    for ph, repl in gm.items():
        text = text.replace(ph, repl)
    for ph, orig in lq.items():
        text = text.replace(ph, orig)

    # Fix any double-bold
    while '<b><b>' in text:
        text = text.replace('<b><b>', '<b>')
    while '</b></b>' in text:
        text = text.replace('</b></b>', '</b>')
    return text


# ── Parsing helpers ──────────────────────────────────────────
def split_sections(content):
    sec_re = re.compile(r'^={10,}\s*(.*?)\s*={10,}$', re.MULTILINE)
    headers = sec_re.findall(content)
    parts   = sec_re.split(content)
    return [(headers[i], parts[2*i+2]) for i in range(len(headers))]


def parse_text_subs(body):
    sub_re = re.compile(r'^---\s*(EMAIL|INAPP)\s*\((EN|DE)\)\s*---$', re.MULTILINE)
    keys   = sub_re.findall(body)
    parts  = sub_re.split(body)
    d = {}
    for i, (typ, lang) in enumerate(keys):
        d[f'{typ.lower()}_{lang.lower()}'] = parts[3*i+3].strip()
    return d


def extract_email(text):
    r = {}
    m = re.search(r'^Subject:\s*(.*)$', text, re.M)
    r['subject'] = m.group(1).strip() if m else ''
    m = re.search(r'^Preheader:\s*(.*)$', text, re.M)
    r['preheader'] = m.group(1).strip() if m else ''

    # Greeting + Body
    m = re.search(r'^Body:\s*\n(.*?)(?=^Button:)', text, re.M | re.S)
    raw_body = m.group(1).strip() if m else ''
    lines = raw_body.split('\n')
    if lines and (lines[0].strip().startswith('Hello') or lines[0].strip().startswith('Hallo')):
        r['greeting'] = lines[0].strip()
        r['body'] = '\n'.join(lines[1:]).strip()
    else:
        r['greeting'] = ''
        r['body'] = raw_body

    m = re.search(r'^Button:\s*(.*)$', text, re.M)
    r['button'] = m.group(1).strip() if m else ''
    m = re.search(r'^Terms&Conditions:\s*\n?(.*)', text, re.M | re.S)
    r['tc'] = m.group(1).strip() if m else ''
    return r


def extract_inapp(text):
    r = {}
    m = re.search(r'^Body:\s*(.*?)(?=^Button:)', text, re.M | re.S)
    r['body'] = m.group(1).strip() if m else ''
    m = re.search(r'^Button:\s*(.*)$', text, re.M)
    r['button'] = m.group(1).strip() if m else ''
    return r


def body_html(text):
    if not text:
        return ''
    paras = re.split(r'\n\n+', text.strip())
    parts = []
    for p in paras:
        parts.append('<br>\n'.join(p.strip().split('\n')))
    return boldify('<br><br>\n'.join(parts))


def tc_inline(text):
    if not text.strip():
        return ''
    return ' | '.join(l.strip() for l in text.strip().split('\n') if l.strip())


def parse_banner_subs(body):
    d = {}
    for key, label in [('email_en','EMAIL BANNER (EN)'), ('email_de','EMAIL BANNER (DE)'),
                        ('inapp_en','INAPP BANNER (EN)'), ('inapp_de','INAPP BANNER (DE)')]:
        pat = re.escape(f'--- {label} ---')
        m = re.search(pat + r'\s*\n(.*?)(?=\n---|$)', body, re.S)
        d[key] = m.group(1).strip() if m else ''
    return d


# ── Read sources ─────────────────────────────────────────────
with open(INPUT_TEXTS, encoding='utf-8') as f:
    txt_raw = f.read()
with open(INPUT_BANNERS, encoding='utf-8') as f:
    ban_raw = f.read()

txt_secs = split_sections(txt_raw)
ban_secs = split_sections(ban_raw)

txt_entries = [{'header': h, **parse_text_subs(b)} for h, b in txt_secs]
ban_entries = [{'header': h, **parse_banner_subs(b)} for h, b in ban_secs]


# ── Generate Newsletters HTML ────────────────────────────────
def email_block(raw, label):
    if not raw:
        return ''
    f = extract_email(raw)
    out = f'\n<h3>{label}</h3>\n'
    if f['subject']:
        out += f'<p><b>Subject:</b> {f["subject"]}</p>\n'
    if f['preheader']:
        out += f'<p><b>Preheader:</b> {f["preheader"]}</p>\n'
    if f['greeting']:
        out += f'<p><b>Greeting:</b> {f["greeting"]}</p>\n'
    if f['body']:
        out += f'<p><b>Body:</b><br>\n{body_html(f["body"])}</p>\n'
    if f['button']:
        out += f'<p><b>CTA:</b> {f["button"]}</p>\n'
    if f['tc']:
        out += f'<p class="tc"><b>T&amp;C:</b> {tc_inline(f["tc"])}</p>\n'
    return out


def inapp_block(raw, label):
    if not raw:
        return ''
    f = extract_inapp(raw)
    out = f'\n<h3>{label}</h3>\n'
    if f['body']:
        out += f'<p><b>Body:</b><br>\n{body_html(f["body"])}</p>\n'
    if f['button']:
        out += f'<p><b>CTA:</b> {f["button"]}</p>\n'
    return out


html = f'''<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"><title>Oshi Newsletters</title>
<style>{CSS}</style></head>
<body>

<h1>OSHI NEWSLETTERS &#128240;</h1>
'''

for e in txt_entries:
    html += f'\n<h2>{e["header"]}</h2>\n'
    html += email_block(e.get('email_en',''), 'EMAIL (EN)')
    html += email_block(e.get('email_de',''), 'EMAIL (DE)')
    html += inapp_block(e.get('inapp_en',''), 'INAPP (EN)')
    html += inapp_block(e.get('inapp_de',''), 'INAPP (DE)')

html += '\n</body>\n</html>'

with open(OUTPUT_TEXTS, 'w', encoding='utf-8') as f:
    f.write(html)
print(f'✅ {OUTPUT_TEXTS}: {len(txt_entries)} entries')


# ── Generate Banners HTML ────────────────────────────────────
html2 = f'''<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"><title>Oshi Newsletter Banners</title>
<style>{CSS}</style></head>
<body>

<h1>OSHI NEWSLETTER BANNERS &#127912;</h1>
'''

for e in ban_entries:
    html2 += f'\n<h2>{e["header"]}</h2>\n'
    if e.get('email_en'):
        html2 += f'\n<h3>EMAIL BANNER (EN)</h3>\n<p>{e["email_en"]}</p>\n'
    if e.get('email_de'):
        html2 += f'\n<h3>EMAIL BANNER (DE)</h3>\n<p>{e["email_de"]}</p>\n'
    if e.get('inapp_en'):
        html2 += f'\n<h3>INAPP BANNER (EN)</h3>\n<p>{e["inapp_en"]}</p>\n'
    if e.get('inapp_de'):
        html2 += f'\n<h3>INAPP BANNER (DE)</h3>\n<p>{e["inapp_de"]}</p>\n'

html2 += '\n</body>\n</html>'

with open(OUTPUT_BANNERS, 'w', encoding='utf-8') as f:
    f.write(html2)
print(f'✅ {OUTPUT_BANNERS}: {len(ban_entries)} entries')
