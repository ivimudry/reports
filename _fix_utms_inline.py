import os, re

FOLDER = os.path.join("тексти", "пантери нова праця")

CAMPAIGNS = {
    "DEP ret - Table data.txt": "dep",
    "nut 1 - Table data.txt": "nutrition1",
    "nut 2 - Table data.txt": "nutrition2",
    "welcome - Table data.txt": "welcome",
    "Unsuccessful Deposit - Table data.txt": "faileddep",
}

def make_utm_amp(campaign, num):
    return (f"utm_campaign={campaign}&amp;utm_source=customerio"
            f"&amp;utm_medium=email&amp;utm_language=en&amp;utm_email={num}")

total_all = 0

for fname, campaign in CAMPAIGNS.items():
    fpath = os.path.join(FOLDER, fname)
    with open(fpath, "r", encoding="utf-8") as f:
        lines = f.readlines()

    current_email = 0
    fixes = 0

    for i, line in enumerate(lines):
        m = re.match(r"^name: Email (\d+)", line)
        if m:
            current_email = int(m.group(1))

        if current_email == 0:
            continue

        original = line

        # FIX 1: Copyright link with NO UTM (DEP ret, nut1, nut2, welcome)
        if 'href="https://games.pantherbet.co.za/"' in line:
            line = line.replace(
                'href="https://games.pantherbet.co.za/"',
                'href="https://games.pantherbet.co.za/?' + make_utm_amp(campaign, current_email) + '"'
            )

        # FIX 2: Copyright link with WRONG domain (Unsuccessful Deposit)
        if 'href="https://pantherbet.co.za/?' in line:
            line = re.sub(
                r'href="https://pantherbet\.co\.za/\?utm_campaign=[^"]*"',
                'href="https://games.pantherbet.co.za/?' + make_utm_amp(campaign, current_email) + '"',
                line
            )

        # FIX 3: Live chat links - various wrong UTM patterns
        if "games.pantherbet.co.za/support?" in line:
            line = re.sub(
                r'https://games\.pantherbet\.co\.za/support\?utm_campaign=\w+&amp;[^"]*?utm_email=\d+',
                'https://games.pantherbet.co.za/support?' + make_utm_amp(campaign, current_email),
                line
            )

        if line != original:
            fixes += 1
            lines[i] = line

    if fixes > 0:
        with open(fpath, "w", encoding="utf-8") as f:
            f.writelines(lines)
        print(f"  {fixes} lines fixed in {fname}")
        total_all += fixes
    else:
        print(f"  0 changes in {fname}")

print(f"\nTotal: {total_all} lines fixed")

# === VERIFICATION ===
print("\n--- VERIFICATION ---")
for fname, campaign in CAMPAIGNS.items():
    fpath = os.path.join(FOLDER, fname)
    with open(fpath, "r", encoding="utf-8") as f:
        text = f.read()

    issues = []

    c1 = len(re.findall(r'href="https://games\.pantherbet\.co\.za/"', text))
    if c1:
        issues.append(f"{c1} bare copyright links")

    c2 = len(re.findall(r'href="https://pantherbet\.co\.za/\?', text))
    if c2:
        issues.append(f"{c2} wrong-domain copyright")

    support_links = re.findall(r'games\.pantherbet\.co\.za/support\?[^"]+', text)
    no_medium = [s for s in support_links if "utm_medium" not in s]
    if no_medium:
        issues.append(f"{len(no_medium)} support links missing utm_medium")

    wrong_camp = [s for s in support_links
                  if re.search(r'utm_campaign=(\w+)', s)
                  and re.search(r'utm_campaign=(\w+)', s).group(1) != campaign]
    if wrong_camp:
        issues.append(f"{len(wrong_camp)} support links with wrong campaign")

    if issues:
        print(f"  {fname}: {'; '.join(issues)}")
    else:
        print(f"  {fname}: OK")
