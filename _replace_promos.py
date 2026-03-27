import os, re

base = os.path.join("тексти", "пантери нова праця")
total = 0

def replace_in_file(fname, replacements, label):
    """replacements: list of (email_nums, old, new, ordered_multi)"""
    global total
    fpath = os.path.join(base, fname)
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    lines = content.split("\n")

    current_email = 0
    changes = 0
    new_lines = []

    for line in lines:
        m = re.match(r"name:\s*Email\s*#?(\d+)", line)
        if m:
            current_email = int(m.group(1))

        modified = line
        for email_nums, old, new, ordered_multi in replacements:
            if current_email in email_nums:
                if ordered_multi:
                    # ordered_multi is a list of replacements for sequential XXXX
                    # e.g. [("STAG140", "GATE100")] - first XXXX→STAG140, second→GATE100
                    codes = ordered_multi
                    count = modified.count(old)
                    if count >= len(codes):
                        for code in codes:
                            modified = modified.replace(old, code, 1)
                            changes += 1
                elif old in modified:
                    modified = modified.replace(old, new)
                    changes += modified.count(new) if modified.count(new) > line.count(new) else 1
                    # Simpler: just count
                    changes = changes  # already counted

        new_lines.append(modified)

    new_content = "\n".join(new_lines)
    if new_content != content:
        actual_changes = sum(1 for a, b in zip(content.split("\n"), new_content.split("\n")) if a != b)
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"{label}: {actual_changes} lines changed")
        total += actual_changes
    else:
        print(f"{label}: 0 changes")

# nut 1: #5,6 → SUGAR150; #7,8 → AVIA117
replace_in_file("nut 1 - Table data.txt", [
    ({5, 6}, "XXXX", "SUGAR150", None),
    ({7, 8}, "XXXX", "AVIA117", None),
], "nut 1")

# nut 2: #7,8 → STARS120; #5,6 → ordered (STAG140, GATE100)
# For #5,6 the text_2 has two XXXX: first for 140% bonus, second for Gates of Olympus
fpath = os.path.join(base, "nut 2 - Table data.txt")
with open(fpath, "r", encoding="utf-8") as f:
    content = f.read()
lines = content.split("\n")

current_email = 0
nut2_changes = 0
new_lines = []
for line in lines:
    m = re.match(r"name:\s*Email\s*#?(\d+)", line)
    if m:
        current_email = int(m.group(1))

    modified = line
    if current_email in (7, 8) and "XXXX" in modified:
        modified = modified.replace("XXXX", "STARS120")
        nut2_changes += 1
    elif current_email in (5, 6) and "XXXX" in modified:
        # Two XXXX in text_2: first = STAG140, second = GATE100
        modified = modified.replace("XXXX", "STAG140", 1)
        modified = modified.replace("XXXX", "GATE100", 1)
        nut2_changes += 1

    new_lines.append(modified)

with open(fpath, "w", encoding="utf-8") as f:
    f.write("\n".join(new_lines))
print(f"nut 2: {nut2_changes} lines changed")
total += nut2_changes

# welcome: #9,10 → GATES150; #7,8 → FSAVIATOR→AVIA100
replace_in_file("welcome - Table data.txt", [
    ({9, 10}, "XXXX", "GATES150", None),
    ({7, 8}, "FSAVIATOR", "AVIA100", None),
], "welcome")

print(f"\nTotal changes: {total}")
