import os, re

base = os.path.join("тексти", "пантери нова праця")

files = [
    ("nut 1 - Table data.txt", "nut 1"),
    ("nut 2 - Table data.txt", "nut 2"),
    ("welcome - Table data.txt", "welcome"),
]

all_ok = True
for fname, label in files:
    fpath = os.path.join(base, fname)
    with open(fpath, "r", encoding="utf-8") as f:
        lines = f.readlines()

    current_email = 0
    print(f"\n{'='*50}")
    print(f"{label}")

    # Check no XXXX remains
    xxxx_count = sum(1 for l in lines if "XXXX" in l)
    if xxxx_count > 0:
        print(f"  ❌ XXXX still found in {xxxx_count} lines!")
        all_ok = False
    else:
        print(f"  ✅ No XXXX remaining")

    # Check FSAVIATOR (only welcome)
    if "welcome" in label:
        fsa = sum(1 for l in lines if "FSAVIATOR" in l)
        if fsa > 0:
            print(f"  ❌ FSAVIATOR still found in {fsa} lines!")
            all_ok = False
        else:
            print(f"  ✅ No FSAVIATOR remaining")

    # Show all promo codes found
    for line in lines:
        m = re.match(r"name:\s*Email\s*#?(\d+)", line)
        if m:
            current_email = int(m.group(1))
        if line.startswith("promocode_button_1:"):
            code = line.split(":", 1)[1].strip()
            print(f"  Email #{current_email}: promocode_button_1 = {code}")
        # Also check inline promo codes in text
        for pm in re.finditer(r'promo code <strong[^>]*>(\w+)</strong>', line):
            field = line.split(":")[0].strip()
            print(f"  Email #{current_email}: {field} inline = {pm.group(1)}")
        for pm in re.finditer(r'Use code <strong[^>]*>(\w+)</strong>', line):
            field = line.split(":")[0].strip()
            print(f"  Email #{current_email}: {field} inline code = {pm.group(1)}")

print(f"\n{'='*50}")
print(f"OVERALL: {'ALL GOOD ✅' if all_ok else 'ISSUES ❌'}")
