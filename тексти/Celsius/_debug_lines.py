#!/usr/bin/env python3
"""Debug: show what's on the expected fr-FR rich_text lines."""
FILE = r"c:\Projects\REPORTS\тексти\Celsius\Failed Deposit Flow - Table data.txt"
with open(FILE, "r", encoding="utf-8") as f:
    lines = f.readlines()

print(f"Total lines: {len(lines)}")
# Show first 50 chars of each line around expected positions
for i in [7,8,9,10,11,12,13,14,35,36,37,38,39,40,41,42]:
    content = lines[i].rstrip()[:80]
    print(f"  [{i}] {content}")

# Find all 'locale: fr-FR' occurrences
print("\nAll 'locale: fr-FR' lines:")
for i, line in enumerate(lines):
    if 'locale: fr-FR' in line:
        print(f"  [{i}] {line.rstrip()}")
        # Show next lines until we find rich_text
        for j in range(i+1, min(i+6, len(lines))):
            content = lines[j].rstrip()[:80]
            print(f"    [{j}] {content}")
            if lines[j].startswith("rich_text:"):
                # Check for English
                if "Your recent deposit" in lines[j]:
                    print(f"    ^^^ FOUND 'Your recent deposit' on line {j}")
                if "Use your spouse" in lines[j]:
                    print(f"    ^^^ FOUND 'Use your spouse' on line {j}")
                if "I'm assigning" in lines[j]:
                    print(f"    ^^^ FOUND 'I'm assigning' on line {j}")
                if "I\u2019m Alex" in lines[j] or "I'm Alex" in lines[j]:
                    print(f"    ^^^ FOUND 'I'm Alex' on line {j}")
                if "Looks like your deposit" in lines[j]:
                    print(f"    ^^^ FOUND 'Looks like your deposit' on line {j}")
                if "Alex\u2019s here" in lines[j] or "Alex's here" in lines[j]:
                    print(f"    ^^^ FOUND 'Alex's here' on line {j}")
                if "That\u2019s sad" in lines[j] or "That's sad" in lines[j]:
                    print(f"    ^^^ FOUND 'That's sad' on line {j}")
                if "If you need help" in lines[j]:
                    print(f"    ^^^ FOUND 'If you need help' on line {j}")
                break
