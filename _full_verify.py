import os, re

base = os.path.join("тексти", "пантери нова праця")

files = [
    ("DEP ret - Table data.txt", "dep", 11),
    ("nut 1 - Table data.txt", "nutrition1", 8),
    ("nut 2 - Table data.txt", "nutrition2", 8),
    ("welcome - Table data.txt", "welcome", 10),
    ("Unsuccessful Deposit - Table data.txt", "faileddep", 4),
]

all_ok = True

for fname, campaign, expected_emails in files:
    fpath = os.path.join(base, fname)
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    lines = content.split("\n")

    issues = []

    # 1. Count emails
    email_count = len(re.findall(r"^name:\s*Email\s*#\d+", content, re.MULTILINE))
    if email_count != expected_emails:
        issues.append(f"Email count: {email_count} (expected {expected_emails})")

    # 2. Bare copyright links (no UTMs)
    bare_copy = content.count('href="https://games.pantherbet.co.za/"')
    if bare_copy > 0:
        issues.append(f"Bare copyright links: {bare_copy}")

    # 3. Wrong domain copyright (pantherbet.co.za without games.)
    wrong_domain = len(re.findall(r'href="https://pantherbet\.co\.za/', content))
    if wrong_domain > 0:
        issues.append(f"Wrong domain (no games.): {wrong_domain}")

    # 4. Copyright with correct UTMs
    copy_ok = len(re.findall(
        rf'href="https://games\.pantherbet\.co\.za/\?utm_campaign={campaign}&amp;utm_source=customerio&amp;utm_medium=email&amp;utm_language=en&amp;utm_email=\d+"',
        content))
    if copy_ok != expected_emails:
        issues.append(f"Copyright with correct UTMs: {copy_ok}/{expected_emails}")

    # 5. Support with correct UTMs
    sup_ok = len(re.findall(
        rf'href="https://games\.pantherbet\.co\.za/support\?utm_campaign={campaign}&amp;utm_source=customerio&amp;utm_medium=email&amp;utm_language=en&amp;utm_email=\d+"',
        content))
    # Unsuccessful Deposit has 2 support links per email
    expected_sup = expected_emails * 2 if campaign == "faileddep" else expected_emails
    if sup_ok != expected_sup:
        issues.append(f"Support with correct UTMs: {sup_ok}/{expected_sup}")

    # 6. Support missing utm_medium
    sup_no_medium = len(re.findall(r'pantherbet\.co\.za/support\?utm_campaign=\w+&amp;utm_source=customerio&amp;utm_language=', content))
    if sup_no_medium > 0:
        issues.append(f"Support missing utm_medium: {sup_no_medium}")

    # 7. Wrong campaign name in any link
    wrong_campaign = re.findall(r'utm_campaign=(\w+)', content)
    wrong_ones = [c for c in wrong_campaign if c != campaign]
    if wrong_ones:
        from collections import Counter
        issues.append(f"Wrong campaign names: {dict(Counter(wrong_ones))}")

    # 8. Duplicate UTM params
    dup_lang = len(re.findall(r'utm_language=en&amp;utm_language=en', content))
    if dup_lang > 0:
        issues.append(f"Duplicate utm_language: {dup_lang}")

    # 9. Stripo CDN URLs remaining
    stripo = len(re.findall(r'stripo\.email', content))
    if stripo > 0:
        issues.append(f"Stripo CDN URLs remaining: {stripo}")

    # 10. Check utm_email numbers match email block
    current_email = 0
    for line in lines:
        m = re.match(r"name:\s*Email\s*#(\d+)", line)
        if m:
            current_email = int(m.group(1))
            continue
        if current_email > 0:
            for utm_m in re.finditer(r'utm_email=(\d+)', line):
                utm_num = int(utm_m.group(1))
                if utm_num != current_email:
                    issues.append(f"Email #{current_email}: utm_email={utm_num} (mismatch)")

    # 11. Old logo URLs (Flaticon)
    flaticon = len(re.findall(r'flaticon', content, re.IGNORECASE))
    if flaticon > 0:
        issues.append(f"Flaticon URLs remaining: {flaticon}")

    # Print results
    status = "OK" if not issues else "ISSUES"
    print(f"\n{'='*60}")
    print(f"{fname} [{status}]")
    print(f"  Emails: {email_count} | Campaign: {campaign}")
    if issues:
        all_ok = False
        for iss in issues:
            print(f"  ❌ {iss}")
    else:
        print(f"  ✅ All checks passed")

print(f"\n{'='*60}")
print(f"OVERALL: {'ALL GOOD' if all_ok else 'ISSUES FOUND'}")
