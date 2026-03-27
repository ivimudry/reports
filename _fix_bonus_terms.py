import os, re

base = os.path.join("тексти", "пантери нова праця")

files = {
    "DEP ret": ("DEP ret - Table data.txt", "dep"),
    "nut 1": ("nut 1 - Table data.txt", "nutrition1"),
    "nut 2": ("nut 2 - Table data.txt", "nutrition2"),
    "welcome": ("welcome - Table data.txt", "welcome"),
    "Unsuccessful Deposit": ("Unsuccessful Deposit - Table data.txt", "faileddep"),
}

for label, (fname, campaign) in files.items():
    fpath = os.path.join(base, fname)
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    lines = content.split("\n")

    current_email = 0
    changes = 0
    new_lines = []

    for line in lines:
        # Track email number (both "Email #N" and "Email N" formats)
        m = re.match(r"name:\s*Email\s*#?(\d+)", line)
        if m:
            current_email = int(m.group(1))

        modified = line

        # Fix bonus-terms-and-condition links with any UTM params
        bt_pattern = r'href="https://games\.pantherbet\.co\.za/bonus-terms-and-condition\?[^"]*"'
        bt_replacement = f'href="https://games.pantherbet.co.za/bonus-terms-and-condition?utm_campaign={campaign}&amp;utm_source=customerio&amp;utm_medium=email&amp;utm_language=en&amp;utm_email={current_email}"'
        if re.search(bt_pattern, modified):
            modified = re.sub(bt_pattern, bt_replacement, modified)
            changes += 1

        new_lines.append(modified)

    if changes > 0:
        with open(fpath, "w", encoding="utf-8") as f:
            f.write("\n".join(new_lines))
        print(f"{label}: {changes} bonus-terms fixes")
    else:
        print(f"{label}: 0 bonus-terms links found")
