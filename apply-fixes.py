# -*- coding: utf-8 -*-
"""Apply all fixes from fixes.txt to campaign data files."""
import os, sys

ROOT = r"c:\Projects\REPORTS\тексти"
ok = 0
fail = 0

def fix(filepath, old, new, label):
    global ok, fail
    path = os.path.join(ROOT, filepath) if not os.path.isabs(filepath) else filepath
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    count = content.count(old)
    if count == 0:
        print(f"  [FAIL] {label} — old text NOT found")
        fail += 1
        return
    if count > 1:
        print(f"  [WARN] {label} — {count} matches, replacing all")
    content = content.replace(old, new)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  [OK] {label} ({count} match)")
    ok += 1

DEP = "DEP Retention - Table data.txt"
FTD = "FTD Retention Flow - Table data.txt"
SU  = "SU Retention - Table data.txt"
WF  = "Welcome Flow - Table data.txt"

# ═══════════════════════════════════════════════════
#  DEP RETENTION — Remove orphan promo tags from headers
# ═══════════════════════════════════════════════════
print("\n=== DEP RETENTION ===")

# C3.1 — remove orphan POWER140 (only 1 occurrence in file)
fix(DEP,
    ' data-promocode="POWER140"',
    '',
    "C3.1: remove POWER140 from header")

# S3.1 — remove orphan WIN20NRF (use preheader context)
fix(DEP,
    'preheader: See who dominated the lines this week at Celsius Sport\nheader_html_tag: dir="ltr" xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office" lang="en" data-promocode="WIN20NRF"',
    'preheader: See who dominated the lines this week at Celsius Sport\nheader_html_tag: dir="ltr" xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office" lang="en"',
    "S3.1: remove WIN20NRF from header")

# S8.1 — remove orphan WIN20NRF (use preheader context)
fix(DEP,
    'preheader: See the top payouts of the week and pick your winning match\nheader_html_tag: dir="ltr" xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office" lang="en" data-promocode="WIN20NRF"',
    'preheader: See the top payouts of the week and pick your winning match\nheader_html_tag: dir="ltr" xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office" lang="en"',
    "S8.1: remove WIN20NRF from header")

# ═══════════════════════════════════════════════════
#  FTD RETENTION — Add promo codes to headers + body
# ═══════════════════════════════════════════════════
print("\n=== FTD RETENTION — HEADERS ===")

# C1: ANUBIS10050
fix(FTD,
    'preheader: Second deposit bonus for Hand of Anubis is ready\nheader_html_tag: dir="ltr" xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office" lang="en"',
    'preheader: Second deposit bonus for Hand of Anubis is ready\nheader_html_tag: dir="ltr" xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office" lang="en" data-promocode="ANUBIS10050"',
    "FTD C1: add ANUBIS10050 to header")

# C3: PARTY140
fix(FTD,
    'preheader: Sweeten your second deposit with this juicy bonus\nheader_html_tag: dir="ltr" xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office" lang="en"',
    'preheader: Sweeten your second deposit with this juicy bonus\nheader_html_tag: dir="ltr" xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office" lang="en" data-promocode="PARTY140"',
    "FTD C3: add PARTY140 to header")

# C4: DORK50110
fix(FTD,
    "preheader: Dork Unit is waiting with a bonus that\u2019s anything but silly\nheader_html_tag: dir=\"ltr\" xmlns=\"http://www.w3.org/1999/xhtml\" xmlns:o=\"urn:schemas-microsoft-com:office:office\" lang=\"en\"",
    "preheader: Dork Unit is waiting with a bonus that\u2019s anything but silly\nheader_html_tag: dir=\"ltr\" xmlns=\"http://www.w3.org/1999/xhtml\" xmlns:o=\"urn:schemas-microsoft-com:office:office\" lang=\"en\" data-promocode=\"DORK50110\"",
    "FTD C4: add DORK50110 to header")

# C5: BONANZA10080
fix(FTD,
    'preheader: Second deposit bonus just got a whole lot sweeter\nheader_html_tag: dir="ltr" xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office" lang="en"',
    'preheader: Second deposit bonus just got a whole lot sweeter\nheader_html_tag: dir="ltr" xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office" lang="en" data-promocode="BONANZA10080"',
    "FTD C5: add BONANZA10080 to header")

# C6: RICH100150
fix(FTD,
    'preheader: Boost your deposit and spin through the secrets\nheader_html_tag: dir="ltr" xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office" lang="en"',
    'preheader: Boost your deposit and spin through the secrets\nheader_html_tag: dir="ltr" xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office" lang="en" data-promocode="RICH100150"',
    "FTD C6: add RICH100150 to header")

# C8: FORGED150
fix(FTD,
    'preheader: Strike hard with your second deposit bonus\nheader_html_tag: dir="ltr" xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office" lang="en"',
    'preheader: Strike hard with your second deposit bonus\nheader_html_tag: dir="ltr" xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office" lang="en" data-promocode="FORGED150"',
    "FTD C8: add FORGED150 to header")

# S1: WINBACKNRF20
fix(FTD,
    "preheader: Get 20% of your bet back if things don\u2019t go your way \u2014 only after your first deposit\nheader_html_tag: dir=\"ltr\" xmlns=\"http://www.w3.org/1999/xhtml\" xmlns:o=\"urn:schemas-microsoft-com:office:office\" lang=\"en\"",
    "preheader: Get 20% of your bet back if things don\u2019t go your way \u2014 only after your first deposit\nheader_html_tag: dir=\"ltr\" xmlns=\"http://www.w3.org/1999/xhtml\" xmlns:o=\"urn:schemas-microsoft-com:office:office\" lang=\"en\" data-promocode=\"WINBACKNRF20\"",
    "FTD S1: add WINBACKNRF20 to header")

# S2: WINBACKNRF20
fix(FTD,
    "preheader: Your 20% NoRisk FreeBet is live \u2014 keep playing with confidence\nheader_html_tag: dir=\"ltr\" xmlns=\"http://www.w3.org/1999/xhtml\" xmlns:o=\"urn:schemas-microsoft-com:office:office\" lang=\"en\"",
    "preheader: Your 20% NoRisk FreeBet is live \u2014 keep playing with confidence\nheader_html_tag: dir=\"ltr\" xmlns=\"http://www.w3.org/1999/xhtml\" xmlns:o=\"urn:schemas-microsoft-com:office:office\" lang=\"en\" data-promocode=\"WINBACKNRF20\"",
    "FTD S2: add WINBACKNRF20 to header")

# S3: WINBACKNRF20
fix(FTD,
    "preheader: Win or not, your next bet comes with 20% back \u2014 no promo code needed\nheader_html_tag: dir=\"ltr\" xmlns=\"http://www.w3.org/1999/xhtml\" xmlns:o=\"urn:schemas-microsoft-com:office:office\" lang=\"en\"",
    "preheader: Win or not, your next bet comes with 20% back \u2014 use code WINBACKNRF20\nheader_html_tag: dir=\"ltr\" xmlns=\"http://www.w3.org/1999/xhtml\" xmlns:o=\"urn:schemas-microsoft-com:office:office\" lang=\"en\" data-promocode=\"WINBACKNRF20\"",
    "FTD S3: add WINBACKNRF20 to header + fix preheader")

# S4: SAFETYNRF25
fix(FTD,
    "preheader: Place your next bet and get 25% back if it doesn\u2019t go your way\nheader_html_tag: dir=\"ltr\" xmlns=\"http://www.w3.org/1999/xhtml\" xmlns:o=\"urn:schemas-microsoft-com:office:office\" lang=\"en\"",
    "preheader: Place your next bet and get 25% back if it doesn\u2019t go your way\nheader_html_tag: dir=\"ltr\" xmlns=\"http://www.w3.org/1999/xhtml\" xmlns:o=\"urn:schemas-microsoft-com:office:office\" lang=\"en\" data-promocode=\"SAFETYNRF25\"",
    "FTD S4: add SAFETYNRF25 to header")

# S6: WINBACKNRF20
fix(FTD,
    "preheader: Miss the mark? We\u2019ll return 20% on your next bet \u2014 no code needed\nheader_html_tag: dir=\"ltr\" xmlns=\"http://www.w3.org/1999/xhtml\" xmlns:o=\"urn:schemas-microsoft-com:office:office\" lang=\"en\"",
    "preheader: Miss the mark? We\u2019ll return 20% on your next bet \u2014 use code WINBACKNRF20\nheader_html_tag: dir=\"ltr\" xmlns=\"http://www.w3.org/1999/xhtml\" xmlns:o=\"urn:schemas-microsoft-com:office:office\" lang=\"en\" data-promocode=\"WINBACKNRF20\"",
    "FTD S6: add WINBACKNRF20 to header + fix preheader")

# S7: WINBACKNRF20
fix(FTD,
    "preheader: Play your next bet with confidence \u2014 20% comes back if it misses\nheader_html_tag: dir=\"ltr\" xmlns=\"http://www.w3.org/1999/xhtml\" xmlns:o=\"urn:schemas-microsoft-com:office:office\" lang=\"en\"",
    "preheader: Play your next bet with confidence \u2014 20% comes back if it misses\nheader_html_tag: dir=\"ltr\" xmlns=\"http://www.w3.org/1999/xhtml\" xmlns:o=\"urn:schemas-microsoft-com:office:office\" lang=\"en\" data-promocode=\"WINBACKNRF20\"",
    "FTD S7: add WINBACKNRF20 to header")

# ─── FTD BODY FIXES ───
print("\n=== FTD RETENTION — BODY ===")

# C1 body: add ANUBIS10050
fix(FTD,
    'Make your second deposit and unlock a <strong>100% bonus + 50 Free Spins</strong> in <strong>Hand of Anubis</strong> <strong>by Hacksaw Gaming</strong>.',
    'Use code <strong class="promocode">ANUBIS10050</strong> on your second deposit to unlock a <strong>100% bonus + 50 Free Spins</strong> in <strong>Hand of Anubis</strong> <strong>by Hacksaw Gaming</strong>.',
    "FTD C1 body: add ANUBIS10050")

# C3 body: add PARTY140
fix(FTD,
    'Your second deposit gets a <strong>140% bonus + 50 Free Spins</strong> in <strong>Fruit Party</strong> <strong>by Pragmatic Play</strong>.',
    'Use code <strong class="promocode">PARTY140</strong> on your second deposit and get a <strong>140% bonus + 50 Free Spins</strong> in <strong>Fruit Party</strong> <strong>by Pragmatic Play</strong>.',
    "FTD C3 body: add PARTY140")

# C4 body: add DORK50110
fix(FTD,
    'Make your second deposit and get a <strong>110% bonus + 50 Free Spins</strong> in <strong>Dork Unit</strong> <strong>by Hacksaw Gaming</strong>.',
    'Use code <strong class="promocode">DORK50110</strong> on your second deposit and get a <strong>110% bonus + 50 Free Spins</strong> in <strong>Dork Unit</strong> <strong>by Hacksaw Gaming</strong>.',
    "FTD C4 body: add DORK50110")

# C5 body: add BONANZA10080
fix(FTD,
    'Your second deposit brings a <strong>100% bonus + 80 Free Spins</strong> on <strong>Sweet Bonanza</strong> <strong>by Pragmatic Play</strong>.',
    'Use code <strong class="promocode">BONANZA10080</strong> on your second deposit and get a <strong>100% bonus + 80 Free Spins</strong> on <strong>Sweet Bonanza</strong> <strong>by Pragmatic Play</strong>.',
    "FTD C5 body: add BONANZA10080")

# C6 body: add RICH100150 + fix game name (Play'n GO → Play'n Go)
fix(FTD,
    "Make your second deposit and receive a <strong>100% bonus + 150 Free Spins</strong> in <strong>Rich Wilde and the Tome of Madness</strong> <strong>by Play\u2019n GO</strong>.",
    "Use code <strong class=\"promocode\">RICH100150</strong> on your second deposit and receive a <strong>100% bonus + 150 Free Spins</strong> in <strong>Rich Wilde and the Tome of Madness</strong> <strong>by Play\u2019n Go</strong>.",
    "FTD C6 body: add RICH100150 + fix game name")

# C8 body: add FORGED150
fix(FTD,
    'Your second deposit unlocks a <strong>150% bonus + 30 Free Spins</strong> on <strong>Stormforged by Hacksaw Gaming</strong> electrifying slot.',
    'Use code <strong class="promocode">FORGED150</strong> on your second deposit to unlock a <strong>150% bonus + 30 Free Spins</strong> on <strong>Stormforged by Hacksaw Gaming</strong> electrifying slot.',
    "FTD C8 body: add FORGED150")

# S1 body: add WINBACKNRF20
fix(FTD,
    'Enjoy a <strong>20% NoRisk FreeBet</strong> on your next wager.',
    'Use code <strong class="promocode">WINBACKNRF20</strong> and enjoy a <strong>20% NoRisk FreeBet</strong> on your next wager.',
    "FTD S1 body: add WINBACKNRF20")

# S2 body: add WINBACKNRF20
fix(FTD,
    'Place your next wager and get a <strong>20% NoRisk FreeBet</strong>.',
    'Place your next wager with code <strong class="promocode">WINBACKNRF20</strong> and get a <strong>20% NoRisk FreeBet</strong>.',
    "FTD S2 body: add WINBACKNRF20")

# S3 body: add WINBACKNRF20 + remove "No code" text
fix(FTD,
    'With the <strong>20% NoRisk FreeBet</strong>, you can place your next wager knowing we',
    'Use code <strong class="promocode">WINBACKNRF20</strong> to activate the <strong>20% NoRisk FreeBet</strong> and place your next wager knowing we',
    "FTD S3 body: add WINBACKNRF20")

fix(FTD,
    'No code. No hassle. Just smarter betting.',
    'Simple, smart, and hassle-free betting.',
    "FTD S3 body: remove 'No code' text")

# S4 body: add SAFETYNRF25
fix(FTD,
    'With a <strong>25% NoRisk FreeBet</strong>, your next wager comes with a safety net.',
    'Use code <strong class="promocode">SAFETYNRF25</strong> to activate a <strong>25% NoRisk FreeBet</strong> — your next wager comes with a safety net.',
    "FTD S4 body: add SAFETYNRF25")

# S6 body: add WINBACKNRF20
fix(FTD,
    'With a <strong>20% NoRisk FreeBet</strong>, your next wager comes with built-in protection.',
    'Use code <strong class="promocode">WINBACKNRF20</strong> to activate a <strong>20% NoRisk FreeBet</strong> — your next wager comes with built-in protection.',
    "FTD S6 body: add WINBACKNRF20")

# S7 body: add WINBACKNRF20
fix(FTD,
    'Good news \u2014 your <strong>20% NoRisk FreeBet</strong> is active and ready.',
    'Good news \u2014 use code <strong class="promocode">WINBACKNRF20</strong> to claim your <strong>20% NoRisk FreeBet</strong>.',
    "FTD S7 body: add WINBACKNRF20")

# ═══════════════════════════════════════════════════
#  SU RETENTION — Add promo codes
# ═══════════════════════════════════════════════════
print("\n=== SU RETENTION ===")

# CFS2 header: add FINTASTIC150
fix(SU,
    'preheader: Make your first deposit and start spinning with a bonus built for casino players\nheader_html_tag: dir="ltr" xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office" lang="en"',
    'preheader: Make your first deposit and start spinning with a bonus built for casino players\nheader_html_tag: dir="ltr" xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office" lang="en" data-promocode="FINTASTIC150"',
    "SU CFS2: add FINTASTIC150 to header")

# CFS2 body: add FINTASTIC150 + remove "no code needed"
fix(SU,
    'Get a <strong>100% Bonus and 150 Free Spins on Razor Shark</strong> \u2014 no code needed.',
    'Use code <strong class="promocode">FINTASTIC150</strong> and get a <strong>100% Bonus and 150 Free Spins on Razor Shark</strong>.',
    "SU CFS2 body: add FINTASTIC150")

# S1 header: add EARNNRF15X (use name as unique context — S10 has same preheader!)
fix(SU,
    "name: Email 1S\nlocale: Default\nsubject: \U0001F3C6 15% NoRisk FreeBets: Your Safety Net is Ready\npreheader: You\u2019ve joined \u2014 now make your move with 15% FreeBets on your first deposit\nheader_html_tag: dir=\"ltr\" xmlns=\"http://www.w3.org/1999/xhtml\" xmlns:o=\"urn:schemas-microsoft-com:office:office\" lang=\"en\"",
    "name: Email 1S\nlocale: Default\nsubject: \U0001F3C6 15% NoRisk FreeBets: Your Safety Net is Ready\npreheader: You\u2019ve joined \u2014 now make your move with 15% FreeBets on your first deposit\nheader_html_tag: dir=\"ltr\" xmlns=\"http://www.w3.org/1999/xhtml\" xmlns:o=\"urn:schemas-microsoft-com:office:office\" lang=\"en\" data-promocode=\"EARNNRF15X\"",
    "SU S1: add EARNNRF15X to header")

# S1 body: add EARNNRF15X (unique — ends with 🤝, S10 ends with 🥊)
fix(SU,
    "Make your first deposit and we\u2019ll back you with a <strong>15% NoRisk FreeBets Bonus</strong>. If it doesn\u2019t go your way, we\u2019ve got your back. \U0001F91D",
    "Make your first deposit with code <strong class=\"promocode\">EARNNRF15X</strong> and we\u2019ll back you with a <strong>15% NoRisk FreeBets Bonus</strong>. If it doesn\u2019t go your way, we\u2019ve got your back. \U0001F91D",
    "SU S1 body: add EARNNRF15X")

# S10 header: add EARNNRF15X (use name as unique context)
fix(SU,
    "name: Email 10S\nlocale: Default\nsubject: \U0001F3C6 Still Waiting: 15% NoRisk FreeBets\npreheader: You\u2019ve joined \u2014 now make your move with 15% FreeBets on your first deposit\nheader_html_tag: dir=\"ltr\" xmlns=\"http://www.w3.org/1999/xhtml\" xmlns:o=\"urn:schemas-microsoft-com:office:office\" lang=\"en\"",
    "name: Email 10S\nlocale: Default\nsubject: \U0001F3C6 Still Waiting: 15% NoRisk FreeBets\npreheader: You\u2019ve joined \u2014 now make your move with 15% FreeBets on your first deposit\nheader_html_tag: dir=\"ltr\" xmlns=\"http://www.w3.org/1999/xhtml\" xmlns:o=\"urn:schemas-microsoft-com:office:office\" lang=\"en\" data-promocode=\"EARNNRF15X\"",
    "SU S10: add EARNNRF15X to header")

# S10 body: add EARNNRF15X (unique — ends with 🥊)
fix(SU,
    "Make your first deposit and we\u2019ll back you with a <strong>15% NoRisk FreeBets Bonus</strong>. If it doesn\u2019t go your way, we\u2019ve still got you covered. \U0001F94A",
    "Make your first deposit with code <strong class=\"promocode\">EARNNRF15X</strong> and we\u2019ll back you with a <strong>15% NoRisk FreeBets Bonus</strong>. If it doesn\u2019t go your way, we\u2019ve still got you covered. \U0001F94A",
    "SU S10 body: add EARNNRF15X")

# M1 header: add FINTASTIC150, EARNNRF15X (use unique preheader)
fix(SU,
    'preheader: Make your first deposit and get both casino spins and NoRisk FreeBet bonus\nheader_html_tag: dir="ltr" xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office" lang="en"',
    'preheader: Make your first deposit and get both casino spins and NoRisk FreeBet bonus\nheader_html_tag: dir="ltr" xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office" lang="en" data-promocode="FINTASTIC150, EARNNRF15X"',
    "SU M1: add FINTASTIC150+EARNNRF15X to header")

# M1 body: add both promo codes
fix(SU,
    'Your first deposit unlocks a <strong>100% Bonus + 150 Free Spins on Razor Shark</strong> by Push Gaming for casino, AND a <strong>15% NoRisk FreeBet</strong> for sports betting.',
    'Your first deposit unlocks a <strong>100% Bonus + 150 Free Spins on Razor Shark</strong> by Push Gaming for casino with code <strong class="promocode">FINTASTIC150</strong>, AND a <strong>15% NoRisk FreeBet</strong> for sports betting with code <strong class="promocode">EARNNRF15X</strong>.',
    "SU M1 body: add FINTASTIC150 + EARNNRF15X")

# M7 header: add WIN20NRF alongside existing CHAOSCTRL80
# Need to use name as context since subject/preheader may be duplicated
fix(SU,
    'name: Email 7M\nlocale: Default\nsubject: \U0001F381 140% + 80 FS or 20% FreeBet: Your Choice\npreheader: Two ways to start on your first deposit \u2014 unleash chaos or bet safely\nheader_html_tag: dir="ltr" xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office" lang="en" data-promocode="CHAOSCTRL80"',
    'name: Email 7M\nlocale: Default\nsubject: \U0001F381 140% + 80 FS or 20% FreeBet: Your Choice\npreheader: Two ways to start on your first deposit \u2014 unleash chaos or bet safely\nheader_html_tag: dir="ltr" xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office" lang="en" data-promocode="CHAOSCTRL80, WIN20NRF"',
    "SU M7: add WIN20NRF to header")

# ═══════════════════════════════════════════════════
#  WELCOME FLOW — Add promo code to 2S
# ═══════════════════════════════════════════════════
print("\n=== WELCOME FLOW ===")

# 2S header: add BOOST50
fix(WF,
    "preheader: The action\u2019s heating up. Make your move and back your pick today.\nheader_html_tag: dir=\"ltr\" xmlns=\"http://www.w3.org/1999/xhtml\" xmlns:o=\"urn:schemas-microsoft-com:office:office\" lang=\"en\"",
    "preheader: The action\u2019s heating up. Make your move and back your pick today.\nheader_html_tag: dir=\"ltr\" xmlns=\"http://www.w3.org/1999/xhtml\" xmlns:o=\"urn:schemas-microsoft-com:office:office\" lang=\"en\" data-promocode=\"BOOST50\"",
    "WF 2S: add BOOST50 to header")

# 2S body: add BOOST50
fix(WF,
    'enjoy a <strong>50% bonus on your next deposit</strong>',
    'use code <strong class="promocode">BOOST50</strong> and enjoy a <strong>50% bonus on your next deposit</strong>',
    "WF 2S body: add BOOST50")

# ═══════════════════════════════════════════════════
#  SUMMARY
# ═══════════════════════════════════════════════════
print(f"\n{'='*50}")
print(f"Done! OK: {ok}, FAIL: {fail}")
if fail > 0:
    print("!!! Some fixes failed — check output above !!!")
    sys.exit(1)
