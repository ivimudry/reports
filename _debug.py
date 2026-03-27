import os

fpath = os.path.join("тексти", "пантери нова праця", "DEP ret - Table data.txt")
with open(fpath, "r", encoding="utf-8") as f:
    lines = f.readlines()

print(f"Total lines: {len(lines)}")
print(f"Line 0 repr[:80]: {repr(lines[0][:80])}")

# Check for name: Email
for i, line in enumerate(lines):
    if line.startswith("name:"):
        print(f"Line {i}: {line.strip()[:30]}")

# Check for copyright
for i, line in enumerate(lines):
    if "Copyright" in line:
        idx = line.index("pantherbet")
        snippet = line[idx-10:idx+60]
        print(f"Line {i} copyright snippet: {repr(snippet)}")
        break

# Check for support link
for i, line in enumerate(lines):
    if "pantherbet.co.za/support" in line:
        idx = line.index("pantherbet.co.za/support")
        snippet = line[idx-10:idx+80]
        print(f"Line {i} support snippet: {repr(snippet)}")
        break
