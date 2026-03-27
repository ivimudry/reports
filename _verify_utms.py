import os, re

base = os.path.join("тексти", "пантери нова праця")

files = [
    ("DEP ret - Table data.txt", "dep"),
    ("nut 1 - Table data.txt", "nutrition1"),
    ("nut 2 - Table data.txt", "nutrition2"),
    ("welcome - Table data.txt", "welcome"),
    ("Unsuccessful Deposit - Table data.txt", "faileddep"),
]

for fname, campaign in files:
    fpath = os.path.join(base, fname)
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    # Check for bare copyright links (should be 0)
    bare = content.count('href="https://games.pantherbet.co.za/"')
    # Check all copyright links have correct campaign
    copy_correct = len(re.findall(rf'href="https://games\.pantherbet\.co\.za/\?utm_campaign={campaign}&amp;', content))
    # Check support links have correct campaign AND utm_medium=email
    sup_correct = len(re.findall(rf'href="https://games\.pantherbet\.co\.za/support\?utm_campaign={campaign}&amp;utm_source=customerio&amp;utm_medium=email&amp;utm_language=en&amp;utm_email=\d+"', content))
    # Check support links missing utm_medium
    sup_no_medium = len(re.findall(r'pantherbet\.co\.za/support\?utm_campaign=\w+&amp;utm_source=customerio&amp;utm_language=', content))

    print(f"\n{fname}:")
    print(f"  Bare copyright links: {bare} (should be 0)")
    print(f"  Copyright with correct UTMs: {copy_correct}")
    print(f"  Support with full correct UTMs: {sup_correct}")
    print(f"  Support missing utm_medium: {sup_no_medium} (should be 0)")

    # Sample first email's copyright and support
    lines = content.split("\n")
    current_email = 0
    for line in lines:
        m = re.match(r"name:\s*Email\s*#(\d+)", line)
        if m:
            current_email = int(m.group(1))
        if current_email == 1 and f"utm_campaign={campaign}" in line:
            if "pantherbet.co.za/?" in line or "pantherbet.co.za/support?" in line:
                idx = line.index("pantherbet")
                print(f"  Sample (E1): ...{line[idx-5:idx+100]}...")
                break
