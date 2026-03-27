import os, re

base = os.path.join("тексти", "пантери нова праця")

def show_promo_context(fname, label):
    fpath = os.path.join(base, fname)
    with open(fpath, "r", encoding="utf-8") as f:
        lines = f.readlines()
    
    current_email = 0
    print(f"\n{'='*60}")
    print(f"{label}")
    
    for i, line in enumerate(lines):
        m = re.match(r"name:\s*Email\s*#?(\d+)", line)
        if m:
            current_email = int(m.group(1))
        
        if "XXXX" in line:
            field = line.split(":")[0].strip()
            # Get subject for this email
            # Find subject line for this email block
            if field == "promocode_button_1":
                print(f"  Email #{current_email}, {field}: XXXX")
            else:
                # Show text around XXXX
                for pm in re.finditer(r"XXXX", line):
                    start = max(0, pm.start() - 80)
                    end = min(len(line), pm.end() + 80)
                    snippet = line[start:end].replace("\n", "")
                    print(f"  Email #{current_email}, {field}: ...{snippet}...")

    # Also show subjects for emails with XXXX
    current_email = 0
    xxxx_emails = set()
    for line in lines:
        m = re.match(r"name:\s*Email\s*#?(\d+)", line)
        if m:
            current_email = int(m.group(1))
        if "XXXX" in line:
            xxxx_emails.add(current_email)
    
    current_email = 0
    print(f"\n  Subjects of XXXX emails:")
    for line in lines:
        m = re.match(r"name:\s*Email\s*#?(\d+)", line)
        if m:
            current_email = int(m.group(1))
        if current_email in xxxx_emails and line.startswith("subject:"):
            print(f"    Email #{current_email}: {line.strip()}")

show_promo_context("nut 1 - Table data.txt", "NUT 1 (XXXX in #5,6,7,8)")
show_promo_context("nut 2 - Table data.txt", "NUT 2 (XXXX in #7,8)")
show_promo_context("welcome - Table data.txt", "WELCOME (XXXX in #9,10)")
