#!/usr/bin/env python3
"""Minimal verification - writes to C:/Projects/REPORTS/vr.txt"""
import os, re, glob

DIR = r"c:\Projects\REPORTS\тексти\Celsius"
files = sorted(glob.glob(os.path.join(DIR, "* - Table data.txt")))

EN = ["Hi {first_name}", "Nice to meet you,", "Thanks,",
      "Celsius Casino Support", "Alex from Celsius Casino",
      "Complete deposit", "Try a different card",
      "Deposit with cryptocurrency", "CLAIM BONUS", "PLAY NOW",
      "BET NOW", "PLAY LIVE", "JOIN THE TABLE", "PLACE YOUR BET",
      "CLAIM FREE SPINS", "CLAIM FREEBETS", "SPIN & WIN",
      "START BETTING", "We love you", "Need help", "Get 20 FS",
      "Your recent deposit attempt", "Quick ways to complete",
      "Quick options:", "Deposit with code", "the reels are calling"]

out = []
total = 0
for fp in files:
    fn = os.path.basename(fp)
    with open(fp, "r", encoding="utf-8") as f:
        lines = f.readlines()
    name = None
    infr = False
    issues = []
    for i, line in enumerate(lines, 1):
        s = line.rstrip()
        if s.startswith("name: "):
            name = s[6:].strip()
            infr = False
        if s.startswith("locale: "):
            infr = s[8:].strip() == "fr-FR"
        if infr and not s.startswith("url_") and not s.startswith("from_id"):
            for p in EN:
                if p in s:
                    if re.search(r'href="[^"]*' + re.escape(p), s):
                        continue
                    field = s.split(":")[0]
                    issues.append(f"  L{i} [{field}] {name}: \"{p}\"")
    if issues:
        out.append(f"ISSUES {fn}: {len(issues)}")
        out.extend(issues)
        total += len(issues)
    else:
        out.append(f"OK {fn}")

out.append(f"\nTOTAL: {total}")
with open(r"c:\Projects\REPORTS\vr.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(out))
