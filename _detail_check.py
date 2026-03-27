import os, re

base = os.path.join("тексти", "пантери нова праця")

# 1. DEP ret — where are nut1/welcome campaign names?
print("="*60)
print("DEP RET — lines with wrong campaign")
fpath = os.path.join(base, "DEP ret - Table data.txt")
with open(fpath, "r", encoding="utf-8") as f:
    lines = f.readlines()
current_email = 0
for i, line in enumerate(lines):
    m = re.match(r"name:\s*Email\s*#(\d+)", line)
    if m:
        current_email = int(m.group(1))
    if "utm_campaign=" in line and "utm_campaign=dep" not in line:
        # Find the field name
        field = line.split(":")[0].strip() if ":" in line else "?"
        campaigns = re.findall(r"utm_campaign=(\w+)", line)
        print(f"  Email #{current_email}, line {i}, field '{field}': campaigns={campaigns}")

# 2. NUT 1 — where are nut1 campaign names?
print("\n" + "="*60)
print("NUT 1 — lines with wrong campaign")
fpath = os.path.join(base, "nut 1 - Table data.txt")
with open(fpath, "r", encoding="utf-8") as f:
    lines = f.readlines()
current_email = 0
for i, line in enumerate(lines):
    m = re.match(r"name:\s*Email\s*#(\d+)", line)
    if m:
        current_email = int(m.group(1))
    if "utm_campaign=" in line and "utm_campaign=nutrition1" not in line:
        field = line.split(":")[0].strip() if ":" in line else "?"
        campaigns = re.findall(r"utm_campaign=(\w+)", line)
        print(f"  Email #{current_email}, line {i}, field '{field}': campaigns={campaigns}")

# 3. NUT 2 — where are nut2 campaign names?
print("\n" + "="*60)
print("NUT 2 — lines with wrong campaign")
fpath = os.path.join(base, "nut 2 - Table data.txt")
with open(fpath, "r", encoding="utf-8") as f:
    lines = f.readlines()
current_email = 0
for i, line in enumerate(lines):
    m = re.match(r"name:\s*Email\s*#(\d+)", line)
    if m:
        current_email = int(m.group(1))
    if "utm_campaign=" in line and "utm_campaign=nutrition2" not in line:
        field = line.split(":")[0].strip() if ":" in line else "?"
        campaigns = re.findall(r"utm_campaign=(\w+)", line)
        print(f"  Email #{current_email}, line {i}, field '{field}': campaigns={campaigns}")

# 4. DEP ret — check utm_email mismatches
print("\n" + "="*60)
print("DEP RET — utm_email mismatches")
fpath = os.path.join(base, "DEP ret - Table data.txt")
with open(fpath, "r", encoding="utf-8") as f:
    lines = f.readlines()
current_email = 0
for i, line in enumerate(lines):
    m = re.match(r"name:\s*Email\s*#(\d+)", line)
    if m:
        current_email = int(m.group(1))
    if current_email in (9, 10, 11) and "utm_email=" in line:
        field = line.split(":")[0].strip()
        nums = re.findall(r"utm_email=(\d+)", line)
        wrong = [n for n in nums if int(n) != current_email]
        if wrong:
            print(f"  Email #{current_email}, line {i}, field '{field}': utm_email={nums}")

# 5. Unsuccessful Deposit — name format
print("\n" + "="*60)
print("UNSUCCESSFUL DEPOSIT — name format")
fpath = os.path.join(base, "Unsuccessful Deposit - Table data.txt")
with open(fpath, "r", encoding="utf-8") as f:
    lines = f.readlines()
for i, line in enumerate(lines):
    if line.startswith("name:"):
        print(f"  Line {i}: {line.strip()}")
