"""Patch text_3 (T&C from original), text_4 (bonus T&C link locale),
text_7 (support link locale) in Welcome Flow - Table data.txt."""
import re
from pathlib import Path

SRC = Path(r"c:\Projects\REPORTS\тексти\оші\тексти\oshi welcome flow texts EN-DE.txt")
DST = Path(r"c:\Projects\REPORTS\тексти\оші\тексти\Welcome Flow - Table data.txt")

# ---------- 1. Parse originals ----------
# Collect T&C: {(email_num:str, geo:str|None): [line1, line2, line3]}
tnc = {}
src_lines = SRC.read_text(encoding="utf-8").splitlines()

email_hdr = re.compile(r"^==========\s*EMAIL\s*#(\d+)\s*\|")
section_hdr = re.compile(r"^---\s*EMAIL\s*\(([A-Z]+)\)\s*---")

cur_email = None
cur_geo = None
in_tnc = False
buf = []

def flush():
    if cur_email and cur_geo and buf:
        tnc[(cur_email, cur_geo)] = buf[:3]

for line in src_lines:
    m = email_hdr.match(line)
    if m:
        flush()
        cur_email = m.group(1)
        cur_geo = None
        in_tnc = False
        buf = []
        continue
    m = section_hdr.match(line)
    if m:
        flush()
        cur_geo = m.group(1)
        in_tnc = False
        buf = []
        continue
    if line.strip() == "Terms&Conditions:":
        in_tnc = True
        buf = []
        continue
    if in_tnc:
        if line.startswith("Link:") or line.strip() == "":
            in_tnc = False
            continue
        buf.append(line.strip())

flush()

print(f"Parsed T&C blocks: {len(tnc)}")
for k in sorted(tnc): print(" ", k, "->", tnc[k])

# ---------- 2. Rewrite Table data ----------
dst_lines = DST.read_text(encoding="utf-8").splitlines(keepends=True)

GEO_PREFIX = {"DEFAULT": "", "AU": "en-AU/", "CA": "en-CA/", "DE": "de/"}
name_re = re.compile(r"^name:\s*Email\s+(\d+)(?:\s+(AU|CA|DE))?\s*$")

# Style snippets reused
P_STYLE = (
    'class="es-text-mobile-size-10" '
    'style="Margin:0;mso-line-height-rule:exactly;'
    'font-family:Montserrat, helvetica, arial, sans-serif;'
    'line-height:18px;letter-spacing:0;color:#cacbcd;font-size:12px"'
)
TEXT_3_PREFIX = (
    'text_3: <td align="center" class="es-m-text" '
    'style="padding:0 20px;Margin:0">'
    '<p style="Margin:0;mso-line-height-rule:exactly;'
    'font-family:Montserrat, helvetica, arial, sans-serif;'
    'line-height:18px;letter-spacing:0;color:#cacbcd;font-size:12px">'
    '<strong style="font-weight:700 !important">&nbsp;</strong></p>'
)
# Note: original uses a literal space, but &nbsp; is safer; the user file had
# a regular space, so keep regular space for round-trip fidelity:
TEXT_3_PREFIX = TEXT_3_PREFIX.replace('&nbsp;', ' ')

def build_text_3(lines):
    parts = "".join(f'<p {P_STYLE}>{ln}</p>' for ln in lines)
    return f"{TEXT_3_PREFIX}{parts}</td>"

cur_email = None
cur_geo = "DEFAULT"
changes = {"text_3": 0, "text_4": 0, "text_7": 0}

for i, line in enumerate(dst_lines):
    m = name_re.match(line)
    if m:
        cur_email = m.group(1)
        cur_geo = m.group(2) if m.group(2) else "DEFAULT"
        continue

    # ----- text_3 -----
    if line.startswith("text_3:") and cur_email:
        key = (cur_email, cur_geo)
        if key in tnc:
            new_line = build_text_3(tnc[key]) + "\n"
            if new_line != line:
                dst_lines[i] = new_line
                changes["text_3"] += 1
        continue

    # ----- text_4: bonus T&C link locale -----
    if line.startswith("text_4:") and cur_email:
        prefix = GEO_PREFIX[cur_geo]
        # Only DEFAULT stays without prefix
        if prefix:
            new = re.sub(
                r'https://www\.oshi\.io/bonus-terms-and-conditions',
                f'https://www.oshi.io/{prefix}bonus-terms-and-conditions',
                line,
            )
            # But DE original already has /de/ — avoid double
            new = new.replace(
                f'https://www.oshi.io/{prefix}{prefix}',
                f'https://www.oshi.io/{prefix}',
            )
            if new != line:
                dst_lines[i] = new
                changes["text_4"] += 1
        continue

    # ----- text_7: support link locale -----
    if line.startswith("text_7:") and cur_email:
        prefix = GEO_PREFIX[cur_geo]
        # Current baked-in value is /de/support for EN locales — wrong.
        # Replace ANY /xx/support OR /support path component with correct one.
        target = f'https://www.oshi.io/{prefix}support'
        new = re.sub(
            r'https://www\.oshi\.io/(?:[a-z\-]+/)?support',
            target,
            line,
        )
        if new != line:
            dst_lines[i] = new
            changes["text_7"] += 1
        continue

DST.write_text("".join(dst_lines), encoding="utf-8", newline="")
print("Changes:", changes)
