"""
Fix celsiuscasino.com base URLs per locale in all Celsius table data files.

Rules:
  Default → https://celsiuscasino.com/
  fr-FR   → https://celsiuscasino.com/fr/
  hu-HU   → https://celsiuscasino.com/hu/
  pl-PL   → https://celsiuscasino.com/pl/

Only celsiuscasino.com hrefs are affected (not image CDN, not social links).
"""

import os, re, glob

LOCALE_PREFIX = {
    "Default": "",
    "fr-FR":   "fr/",
    "hu-HU":   "hu/",
    "pl-PL":   "pl/",
}

BASE = "https://celsiuscasino.com/"

def fix_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()

    current_locale = "Default"
    changed = 0
    new_lines = []

    for line in lines:
        # Detect locale line
        m = re.match(r"^locale:\s*(.+)$", line.strip())
        if m:
            current_locale = m.group(1).strip()

        prefix = LOCALE_PREFIX.get(current_locale, "")
        correct_base = BASE + prefix  # e.g. https://celsiuscasino.com/fr/

        # Only process lines that contain celsiuscasino.com URLs
        if "celsiuscasino.com/" in line:
            # Replace all occurrences of celsiuscasino.com/ followed by path
            # but NOT the base with a locale already correctly set
            # Strategy: normalize all celsiuscasino.com URLs to remove any existing locale prefix, then add the correct one
            def replace_url(match):
                nonlocal changed
                url = match.group(0)
                # Remove existing locale prefix if any (fr/, hu/, pl/)
                after_base = url[len(BASE):]
                for loc_prefix in ["fr/", "hu/", "pl/"]:
                    if after_base.startswith(loc_prefix):
                        after_base = after_base[len(loc_prefix):]
                        break
                new_url = correct_base + after_base
                if new_url != url:
                    changed += 1
                return new_url

            line = re.sub(r"https://celsiuscasino\.com/[^\s\"'<>)*]+", replace_url, line)

        new_lines.append(line)

    if changed > 0:
        with open(filepath, "w", encoding="utf-8") as f:
            f.writelines(new_lines)
        print(f"  {os.path.basename(filepath)}: {changed} URLs fixed")
    else:
        print(f"  {os.path.basename(filepath)}: no changes needed")

    return changed

# Process all txt files in the Celsius folder
folder = os.path.dirname(os.path.abspath(__file__))
total = 0
files = sorted(glob.glob(os.path.join(folder, "*.txt")))
print(f"Processing {len(files)} files in {folder}\n")

for f in files:
    total += fix_file(f)

print(f"\nTotal URLs fixed: {total}")
