#!/usr/bin/env python3
"""Final verification: write results to file."""
import os, re, glob, sys

DIR = r"c:\Projects\REPORTS\тексти\Celsius"
OUT = r"c:\Projects\REPORTS\verify_result.txt"
files = sorted(glob.glob(os.path.join(DIR, "* - Table data.txt")))

EN_PHRASES = [
    "Hi {first_name}", "Nice to meet you,", "Thanks,",
    "Celsius Casino Support", "Alex from Celsius Casino", "Complete deposit",
    "Try a different card", "Use your spouse", "Deposit with cryptocurrency",
    "CLAIM BONUS", "PLAY NOW", "SPIN & WIN", "BET NOW", "PLAY LIVE",
    "JOIN THE TABLE", "START BETTING", "PLACE YOUR BET", "CLAIM FREE SPINS",
    "CLAIM FREEBETS", "Looks like something bad", "Still seeing trouble",
    "Unsuccessful deposit", "We love you", "Need help", "Get 20 FS",
    "Your recent deposit attempt", "I can see your deposit still",
    "I'm Alex, your personal manager", "That's sad!",
    "Quick ways to complete", "Quick options:",
    "If you need help, just reply", "I'm assigning you a personal manager",
    "We're here to help", "Need a hand?", "How it's going?",
    "Deposit with code", "the reels are calling",
]

results = []
total_issues = 0

for filepath in files:
    fname = os.path.basename(filepath)
    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()

    current_name = None
    in_fr = False
    file_issues = []

    for i, line in enumerate(lines, 1):
        s = line.rstrip("\n")
        if s.startswith("name: "):
            current_name = s[6:].strip()
            in_fr = False
        if s.startswith("locale: "):
            in_fr = (s[8:].strip() == "fr-FR")
        if in_fr:
            if s.startswith("url_") or s.startswith("from_id"):
                continue
            for phrase in EN_PHRASES:
                if phrase in s:
                    href_match = re.search(r'href="[^"]*' + re.escape(phrase) + r'[^"]*"', s)
                    if href_match:
                        continue
                    field = s.split(":")[0] if ":" in s else "?"
                    file_issues.append(f"  L{i} [{field}] {current_name}: \"{phrase}\"")

    if file_issues:
        results.append(f"\nISSUES in {fname}: {len(file_issues)}")
        results.extend(file_issues)
        total_issues += len(file_issues)
    else:
        results.append(f"OK  {fname}")

results.append(f"\n{'='*50}")
if total_issues:
    results.append(f"TOTAL ISSUES: {total_issues}")
else:
    results.append("ALL CLEAR - No English in fr-FR blocks!")
results.append(f"{'='*50}")

with open(OUT, "w", encoding="utf-8") as f:
    f.write("\n".join(results))

# Also print count for quick check
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
print(f"Done. Issues: {total_issues}. Results in {OUT}")
