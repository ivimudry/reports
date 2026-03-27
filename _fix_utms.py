import os, re

base = os.path.join("тексти", "пантери нова праця")

files = {
    "DEP ret": ("DEP ret - Table data.txt", "dep"),
    "nut 1": ("nut 1 - Table data.txt", "nutrition1"),
    "nut 2": ("nut 2 - Table data.txt", "nutrition2"),
    "welcome": ("welcome - Table data.txt", "welcome"),
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
        # Track email number
        m = re.match(r"name:\s*Email\s*#(\d+)", line)
        if m:
            current_email = int(m.group(1))

        modified = line

        # Fix copyright: bare href="https://games.pantherbet.co.za/"
        old_copy = 'href="https://games.pantherbet.co.za/"'
        if old_copy in modified:
            new_copy = f'href="https://games.pantherbet.co.za/?utm_campaign={campaign}&amp;utm_source=customerio&amp;utm_medium=email&amp;utm_language=en&amp;utm_email={current_email}"'
            modified = modified.replace(old_copy, new_copy)
            changes += 1

        # Fix support links: replace any pantherbet.co.za/support?... with correct UTMs
        support_pattern = r'href="https://games\.pantherbet\.co\.za/support\?[^"]*"'
        support_replacement = f'href="https://games.pantherbet.co.za/support?utm_campaign={campaign}&amp;utm_source=customerio&amp;utm_medium=email&amp;utm_language=en&amp;utm_email={current_email}"'
        if re.search(support_pattern, modified):
            modified = re.sub(support_pattern, support_replacement, modified)
            changes += 1

        new_lines.append(modified)

    if changes > 0:
        with open(fpath, "w", encoding="utf-8") as f:
            f.write("\n".join(new_lines))
        print(f"{label}: {changes} fixes applied")
    else:
        print(f"{label}: 0 changes (nothing matched)")
