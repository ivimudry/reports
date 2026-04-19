#!/usr/bin/env python3
"""Final verification: check ALL fr-FR blocks in all 7 files for remaining English content."""
import os, re, glob

DIR = os.path.dirname(__file__)
files = sorted(glob.glob(os.path.join(DIR, "* - Table data.txt")))

# English phrases that should NOT appear in fr-FR blocks
EN_PHRASES = [
    # Greetings
    "Hi {first_name}",
    "Nice to meet you,",
    # Common phrases
    "Thanks,",
    "Celsius Casino Support",  # should be "Assistance Celsius Casino"
    "Alex from Celsius Casino",  # should be "Alex de Celsius Casino"
    "Complete deposit",  # should be "Finaliser le dépôt"
    # List items
    "Try a different card",
    "Use your spouse",
    "Deposit with cryptocurrency",
    # Buttons
    "CLAIM BONUS",
    "PLAY NOW",
    "SPIN & WIN",
    "BET NOW",
    "PLAY LIVE",
    "JOIN THE TABLE",
    "START BETTING",
    "PLACE YOUR BET",
    "CLAIM FREE SPINS",
    "CLAIM FREEBETS",
    # Subjects
    "Looks like something bad",
    "Still seeing trouble",
    "Unsuccessful deposit",
    "We love you",
    "Need help",
    "Get 20 FS",
    # Body content
    "Your recent deposit attempt",
    "I can see your deposit still",
    "I'm Alex, your personal manager",
    "Alex's here!",
    "That's sad!",
    "Quick ways to complete",
    "Quick options:",
    "If you need help, just reply",
    "I'm assigning you a personal manager",
    # Preheaders
    "We're here to help",
    "Need a hand?",
    "How it's going?",
    # Common body English
    "the reels are calling",
    "step into the game",
    "your next deposit",
    "Deposit with code",
    "your winning",
]

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
            locale = s[8:].strip()
            in_fr = (locale == "fr-FR")

        if in_fr:
            # Skip URL lines and from_id
            if s.startswith("url_") or s.startswith("from_id"):
                continue
            # Check for footer fields that should already be translated
            # Check subject, preheader, button_text_1, text_1, text_2, text_3, rich_text
            for phrase in EN_PHRASES:
                if phrase in s:
                    # Exclude if it's inside a URL
                    if "utm_" in phrase or "href=" in phrase:
                        continue
                    # Exclude if phrase is inside href attribute
                    href_match = re.search(r'href="[^"]*' + re.escape(phrase) + r'[^"]*"', s)
                    if href_match:
                        continue
                    field = s.split(":")[0] if ":" in s else "?"
                    file_issues.append(f"  Line {i} [{field}] {current_name}: found \"{phrase}\"")

    if file_issues:
        print(f"\n{'='*60}")
        print(f"ISSUES in {fname}: {len(file_issues)}")
        print(f"{'='*60}")
        for issue in file_issues:
            print(issue)
        total_issues += len(file_issues)
    else:
        print(f"OK  {fname}")

print(f"\n{'='*60}")
if total_issues:
    print(f"TOTAL ISSUES: {total_issues}")
else:
    print("ALL CLEAR - No remaining English found in any fr-FR block!")
print(f"{'='*60}")
