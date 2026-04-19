#!/usr/bin/env python3
"""Debug apostrophe/quote characters in rich_text lines."""
FILE = r"c:\Projects\REPORTS\тексти\Celsius\Failed Deposit Flow - Table data.txt"
with open(FILE, "r", encoding="utf-8") as f:
    lines = f.readlines()

# Check line 12 (Email 1 fr-FR rich_text)
line = lines[12]

# Find "didn" and show surrounding chars
idx = line.find("didn")
if idx >= 0:
    snippet = line[idx:idx+10]
    print(f"Found 'didn' at pos {idx}: {snippet!r}")
    for i, ch in enumerate(snippet):
        print(f"  char[{i}] = U+{ord(ch):04X} '{ch}'")

# Find "we" + "re" pattern  
idx = line.find("we\u2019re")
if idx >= 0:
    print(f"\nFound smart quote we're at pos {idx}")
idx = line.find("we're")
if idx >= 0:
    print(f"\nFound straight quote we're at pos {idx}")

# Find all apostrophe-like chars in line 12
import collections
apos = collections.Counter()
for ch in line:
    if ch in ("'", "\u2018", "\u2019", "\u02BC", "\u0060"):
        apos[f"U+{ord(ch):04X}"] += 1
print(f"\nApostrophe chars in line 12: {dict(apos)}")

# Also check "I'm" pattern
idx = line.find("I\u2019m")
if idx >= 0:
    print(f"Found smart I'm at pos {idx}")
idx = line.find("I'm")
if idx >= 0:
    print(f"Found straight I'm at pos {idx}")

# Check line 120 (Email 5)
line5 = lines[120]
idx = line5.find("Alex\u2019s")
if idx >= 0:
    print(f"\nLine 120: Found smart Alex's")
idx = line5.find("Alex's")
if idx >= 0:
    print(f"\nLine 120: Found straight Alex's")
idx = line5.find("That\u2019s")
if idx >= 0:
    print(f"Line 120: Found smart That's")
idx = line5.find("That's")  
if idx >= 0:
    print(f"Line 120: Found straight That's")

# Show exact text around "didn" on line 12
idx = line.find("didn")
if idx >= 0:
    context = line[idx-5:idx+30]
    print(f"\nContext around 'didn': {context!r}")
