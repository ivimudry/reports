import os, re

base = os.path.join("тексти", "пантери нова праця")

files = [
    ("DEP ret - Table data.txt", "DEP ret"),
    ("nut 1 - Table data.txt", "nut 1"),
    ("nut 2 - Table data.txt", "nut 2"),
    ("welcome - Table data.txt", "welcome"),
    ("Unsuccessful Deposit - Table data.txt", "Unsuccessful Deposit"),
]

all_codes = {}

for fname, label in files:
    fpath = os.path.join(base, fname)
    with open(fpath, "r", encoding="utf-8") as f:
        lines = f.readlines()

    current_email = 0
    for line in lines:
        m = re.match(r"name:\s*Email\s*#?(\d+)", line)
        if m:
            current_email = int(m.group(1))

        if line.startswith("promocode_button_1:"):
            code = line.split(":", 1)[1].strip()
            if code:
                key = code
                if key not in all_codes:
                    all_codes[key] = {"campaigns": [], "context": []}
                all_codes[key]["campaigns"].append(f"{label} #{current_email}")

        # Find bonus context near promo codes in text fields
        # Pattern: "X% Deposit Bonus" or "X Free Spins" or "X FS"
        for pm in re.finditer(r'(\d+%?\s*(?:Deposit\s+)?(?:Bonus|Free Spins|FS))', line):
            # Check if a promo code is nearby
            nearby = line[max(0, pm.start()-200):pm.end()+200]
            for code_match in re.finditer(r'(?:promo code|Use code|Enter code)\s*<strong[^>]*>(\w+)</strong>', nearby):
                code = code_match.group(1)
                bonus = pm.group(1)
                if code in all_codes and bonus not in all_codes[code]["context"]:
                    all_codes[code]["context"].append(bonus)

        # Also check subject for bonus info
        if line.startswith("subject:"):
            subj = line.split(":", 1)[1].strip()
            bonus_matches = re.findall(r'(\d+%?\s*(?:Deposit\s+)?(?:Bonus|Free Spins|FS))', subj)
            # Associate with this email's promo code - find it
            for line2 in lines:
                pass  # skip, handled below

# Second pass: get subject-based bonus for each email
for fname, label in files:
    fpath = os.path.join(base, fname)
    with open(fpath, "r", encoding="utf-8") as f:
        lines = f.readlines()

    current_email = 0
    current_subject = ""
    current_code = ""

    for line in lines:
        m = re.match(r"name:\s*Email\s*#?(\d+)", line)
        if m:
            current_email = int(m.group(1))
            current_subject = ""
            current_code = ""

        if line.startswith("subject:"):
            current_subject = line.split(":", 1)[1].strip()

        if line.startswith("promocode_button_1:"):
            current_code = line.split(":", 1)[1].strip()
            if current_code and current_code in all_codes:
                if current_subject and current_subject not in all_codes[current_code].get("subjects", []):
                    all_codes[current_code].setdefault("subjects", []).append(current_subject)

# Also extract bonus from text content
for fname, label in files:
    fpath = os.path.join(base, fname)
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    for code in all_codes:
        # Find text near code mentions
        for m in re.finditer(re.escape(code), content):
            nearby = content[max(0, m.start()-300):m.end()+300]
            bonuses = re.findall(r'(\d+)\s*(?:%\s*(?:Deposit\s+)?Bonus|Free Spins|FS\b)', nearby)
            percents = re.findall(r'(\d+%)\s*(?:Deposit\s+)?Bonus', nearby)
            fs = re.findall(r'(\d+)\s*(?:Free Spins|FS\b)', nearby)
            for p in percents:
                desc = f"{p} Bonus"
                if desc not in all_codes[code]["context"]:
                    all_codes[code]["context"].append(desc)
            for f_val in fs:
                desc = f"{f_val} FS"
                if desc not in all_codes[code]["context"]:
                    all_codes[code]["context"].append(desc)

# Print results
print("=" * 70)
print(f"{'CODE':<15} {'BONUS':<25} {'CAMPAIGNS'}")
print("=" * 70)

for code in sorted(all_codes.keys()):
    info = all_codes[code]
    bonus = ", ".join(info["context"]) if info["context"] else "—"
    camps = ", ".join(info["campaigns"])
    print(f"{code:<15} {bonus:<25} {camps}")
