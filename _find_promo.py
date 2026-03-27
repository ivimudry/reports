import os, re

base = os.path.join("тексти", "пантери нова праця")

files = [
    "DEP ret - Table data.txt",
    "nut 1 - Table data.txt",
    "nut 2 - Table data.txt",
    "welcome - Table data.txt",
    "Unsuccessful Deposit - Table data.txt",
]

for fname in files:
    fpath = os.path.join(base, fname)
    with open(fpath, "r", encoding="utf-8") as f:
        lines = f.readlines()

    current_email = 0
    found = False
    for i, line in enumerate(lines):
        m = re.match(r"name:\s*Email\s*#?(\d+)", line)
        if m:
            current_email = int(m.group(1))

        # Search for promo/coupon/code/bonus placeholders
        matches = re.findall(r'(\{\{[^}]*(?:promo|coupon|code|bonus|промо|купон)[^}]*\}\})', line, re.IGNORECASE)
        if not matches:
            # Also search for liquid-style placeholders
            matches = re.findall(r'(\{%[^%]*(?:promo|coupon|code|bonus)[^%]*%\})', line, re.IGNORECASE)
        if not matches:
            # Search for {{...}} near word promo/code
            if re.search(r'promo.?code|промокод|coupon|PROMO', line, re.IGNORECASE):
                field = line.split(":")[0].strip()
                snippet_matches = re.findall(r'\{\{[^}]+\}\}', line)
                if not found:
                    print(f"\n{'='*60}")
                    print(f"{fname}")
                    found = True
                print(f"  Email #{current_email}, line {i}, field '{field}':")
                if snippet_matches:
                    print(f"    Placeholders: {snippet_matches}")
                # Show context around promo
                for pm in re.finditer(r'(?:promo.?code|промокод|coupon|PROMO)', line, re.IGNORECASE):
                    start = max(0, pm.start() - 40)
                    end = min(len(line), pm.end() + 40)
                    print(f"    Context: ...{line[start:end]}...")
        else:
            field = line.split(":")[0].strip()
            if not found:
                print(f"\n{'='*60}")
                print(f"{fname}")
                found = True
            print(f"  Email #{current_email}, line {i}, field '{field}': {matches}")

    if not found:
        print(f"\n{fname}: no promo placeholders found")
