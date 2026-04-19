#!/usr/bin/env python3
"""Set banner_src in DEP Retention, SU Retention, Welcome Flow table data files from 4 language banner files."""
import os

DIR = r"c:\Projects\REPORTS\тексти\Celsius"

LANG_TO_LOCALE = {"en": "Default", "fr": "fr-FR", "hu": "hu-HU", "pl": "pl-PL"}
CAMPAIGN_TO_FILE = {
    "DEP Retention": "DEP Retention - Table data.txt",
    "SU Retention": "SU Retention - Table data.txt",
    "Welcome Flow": "Welcome Flow - Table data.txt",
}

# 1. Parse all 4 banner files into a dict: (campaign, email_name, locale) -> url
banners = {}
for lang_code, locale in LANG_TO_LOCALE.items():
    fp = os.path.join(DIR, f"банери лінк {lang_code}.txt")
    with open(fp, "r", encoding="utf-8") as f:
        text = f.read()
    campaign = None
    email_label = None
    for line in text.split("\n"):
        line = line.strip()
        if not line:
            continue
        if line in CAMPAIGN_TO_FILE:
            campaign = line
        elif line.startswith("Email "):
            email_label = line
        elif line.startswith("https://"):
            key = (campaign, email_label, locale)
            banners[key] = line

print(f"Loaded {len(banners)} banner mappings from 4 language files.")

# 2. Apply to each table data file
total = 0
for campaign, table_file in CAMPAIGN_TO_FILE.items():
    fp = os.path.join(DIR, table_file)
    with open(fp, "r", encoding="utf-8") as f:
        lines = f.readlines()
    
    count = 0
    current_name = None
    current_locale = None
    
    for i, line in enumerate(lines):
        s = line.rstrip("\n")
        if s.startswith("name: "):
            current_name = s[6:]
        elif s.startswith("locale: "):
            current_locale = s[8:]
        elif s.startswith("banner_src:"):
            key = (campaign, current_name, current_locale)
            if key in banners:
                new_line = "banner_src: " + banners[key] + "\n"
                if lines[i] != new_line:
                    lines[i] = new_line
                    count += 1
    
    if count:
        with open(fp, "w", encoding="utf-8") as f:
            f.writelines(lines)
    print(f"  {table_file}: {count} banners set")
    total += count

print(f"\nDone: {total} banners set across {len(CAMPAIGN_TO_FILE)} files.")

# 3. Verify: count remaining empty banner_src in these files
empty = 0
for campaign, table_file in CAMPAIGN_TO_FILE.items():
    fp = os.path.join(DIR, table_file)
    with open(fp, "r", encoding="utf-8") as f:
        for line in f:
            if line.rstrip() == "banner_src:":
                empty += 1
print(f"Remaining empty banner_src: {empty}")
