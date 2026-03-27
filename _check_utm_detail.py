import os, re

base = os.path.join("тексти", "пантери нова праця")

# DEP ret line 14 — find utm_campaign
with open(os.path.join(base, "DEP ret - Table data.txt"), "r", encoding="utf-8") as f:
    lines = f.readlines()

line = lines[14]
for m in re.finditer(r'href="[^"]*utm_campaign[^"]*"', line):
    print(f"DEP E1 line14: {m.group()}")

line = lines[246]
for m in re.finditer(r'href="[^"]*utm_campaign[^"]*"', line):
    print(f"DEP E9 line246: {m.group()}")

line = lines[274]
for m in re.finditer(r'href="[^"]*utm_campaign[^"]*"', line):
    print(f"DEP E10 line274: {m.group()}")

line = lines[301]
for m in re.finditer(r'href="[^"]*utm_campaign[^"]*"', line):
    print(f"DEP E11 line301: {m.group()}")

# NUT1 line 14
with open(os.path.join(base, "nut 1 - Table data.txt"), "r", encoding="utf-8") as f:
    lines = f.readlines()
line = lines[14]
for m in re.finditer(r'href="[^"]*utm_campaign[^"]*"', line):
    print(f"NUT1 E1 line14: {m.group()}")

# NUT2 line 14 and 129
with open(os.path.join(base, "nut 2 - Table data.txt"), "r", encoding="utf-8") as f:
    lines = f.readlines()
line = lines[14]
for m in re.finditer(r'href="[^"]*utm_campaign[^"]*"', line):
    print(f"NUT2 E3 line14: {m.group()}")
line = lines[129]
for m in re.finditer(r'href="[^"]*utm_campaign[^"]*"', line):
    print(f"NUT2 E1 line129: {m.group()}")
