# -*- coding: utf-8 -*-
"""Detailed verification of all fixes per email."""
import re

ROOT = r"c:\Projects\REPORTS\тексти"

def check_file(path):
    d = open(f"{ROOT}\\{path}", encoding='utf-8', newline='').read()
    # Parse emails
    emails = []
    blocks = re.split(r'(?=^name: Email )', d, flags=re.MULTILINE)
    for b in blocks:
        if not b.strip():
            continue
        name_m = re.search(r'^name: Email (.+)$', b, re.MULTILINE)
        if not name_m:
            continue
        eid = name_m.group(1).strip()
        header_m = re.search(r'^header_html_tag: (.+)$', b, re.MULTILINE)
        header = header_m.group(1) if header_m else ""
        preheader_m = re.search(r'^preheader: (.+)$', b, re.MULTILINE)
        preheader = preheader_m.group(1) if preheader_m else ""
        
        h_codes = re.findall(r'data-promocode="([^"]+)"', header)
        b_codes = re.findall(r'class="promocode">([^<]+)<', b)
        
        emails.append({
            'id': eid, 
            'h_codes': h_codes[0].split(', ') if h_codes else [],
            'b_codes': b_codes,
            'preheader': preheader,
            'has_no_code_text': 'no code needed' in b.lower() or 'no code.' in b.lower() or 'no promo code' in b.lower()
        })
    return emails

# ═══ DEP ═══
print("=== DEP RETENTION ===")
emails = check_file("DEP Retention - Table data.txt")
checks = {'C3.1': ('no_orphan',), 'S3.1': ('no_orphan',), 'S8.1': ('no_orphan',)}
for e in emails:
    eid = e['id']
    h = set(e['h_codes'])
    b = set(e['b_codes'])
    # C3, S3, S8 should have NO orphan codes (header codes without body code)
    orphans = h - b
    if orphans:
        print(f"  [!] {eid}: orphan header codes {orphans}")
    if eid in checks:
        if not orphans:
            print(f"  [OK] {eid}: no orphan codes")

# ═══ FTD ═══
print("\n=== FTD RETENTION ===")
emails = check_file("FTD Retention Flow - Table data.txt")
ftd_required = {
    '1C': ['ANUBIS10050'], '3C': ['PARTY140'], '4C': ['DORK50110'],
    '5C': ['BONANZA10080'], '6C': ['RICH100150'], '8C': ['FORGED150'],
    '1S': ['WINBACKNRF20'], '2S': ['WINBACKNRF20'], '3S': ['WINBACKNRF20'],
    '4S': ['SAFETYNRF25'], '6S': ['WINBACKNRF20'], '7S': ['WINBACKNRF20']
}
for e in emails:
    eid = e['id']
    if eid in ftd_required:
        required = ftd_required[eid]
        for code in required:
            in_h = code in e['h_codes']
            in_b = code in e['b_codes']
            status = "OK" if in_h and in_b else "MISSING"
            details = f"header={'Y' if in_h else 'N'} body={'Y' if in_b else 'N'}"
            print(f"  [{status}] {eid} -> {code}: {details}")
        if e['has_no_code_text']:
            print(f"  [!] {eid}: still has 'no code' text in body/preheader!")

# ═══ SU ═══
print("\n=== SU RETENTION ===")
emails = check_file("SU Retention - Table data.txt")
su_required = {
    '2CFS': ['FINTASTIC150'],
    '1S': ['EARNNRF15X'],
    '10S': ['EARNNRF15X'],
    '1M': ['FINTASTIC150', 'EARNNRF15X'],
    '7M': ['CHAOSCTRL80', 'WIN20NRF']
}
for e in emails:
    eid = e['id']
    if eid in su_required:
        required = su_required[eid]
        for code in required:
            in_h = code in e['h_codes']
            in_b = code in e['b_codes']
            status = "OK" if in_h and in_b else ("HDR-ONLY" if in_h else "MISSING")
            details = f"header={'Y' if in_h else 'N'} body={'Y' if in_b else 'N'}"
            print(f"  [{status}] {eid} -> {code}: {details}")
        if e['has_no_code_text']:
            print(f"  [!] {eid}: still has 'no code' text!")

# ═══ WF ═══
print("\n=== WELCOME FLOW ===")
emails = check_file("Welcome Flow - Table data.txt")
wf_required = {'2S': ['BOOST50']}
for e in emails:
    eid = e['id']
    if eid in wf_required:
        required = wf_required[eid]
        for code in required:
            in_h = code in e['h_codes']
            in_b = code in e['b_codes']
            status = "OK" if in_h and in_b else "MISSING"
            details = f"header={'Y' if in_h else 'N'} body={'Y' if in_b else 'N'}"
            print(f"  [{status}] {eid} -> {code}: {details}")

# ═══ FTD C6 game name check ═══
print("\n=== SPECIAL CHECKS ===")
ftd = open(f"{ROOT}\\FTD Retention Flow - Table data.txt", encoding='utf-8', newline='').read()
if "Play\u2019n GO" in ftd:
    print("  [!] FTD C6: 'Play\u2019n GO' found (should be 'Play\u2019n Go')")
elif "Play\u2019n Go" in ftd or "Play'n Go" in ftd:
    print("  [OK] FTD C6: game name is correct (Play'n Go)")

# Check FTD S3 preheader
for e in check_file("FTD Retention Flow - Table data.txt"):
    if e['id'] == '3S':
        if 'no promo code' in e['preheader'].lower():
            print(f"  [!] FTD S3 preheader still says: {e['preheader']}")
        else:
            print(f"  [OK] FTD S3 preheader: {e['preheader']}")
    if e['id'] == '6S':
        if 'no code' in e['preheader'].lower():
            print(f"  [!] FTD S6 preheader still says: {e['preheader']}")
        else:
            print(f"  [OK] FTD S6 preheader: {e['preheader']}")

# FTD S3 "No code" text check
for e in check_file("FTD Retention Flow - Table data.txt"):
    if e['id'] == '3S' and e['has_no_code_text']:
        print(f"  [!] FTD S3: still has 'no code' text in body")
