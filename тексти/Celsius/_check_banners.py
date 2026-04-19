#!/usr/bin/env python3
"""Check uniqueness of all banner URLs across all 4 language files."""
import re, os

DIR = r"c:\Projects\REPORTS\тексти\Celsius"
files = ["банери лінк en.txt", "банери лінк fr.txt", "банери лінк hu.txt", "банери лінк pl.txt"]

all_urls = []  # (url, lang, campaign, email_label)

for fn in files:
    lang = fn.replace("банери лінк ", "").replace(".txt", "")
    fp = os.path.join(DIR, fn)
    with open(fp, "r", encoding="utf-8") as f:
        text = f.read()
    
    campaign = None
    email_label = None
    for line in text.split("\n"):
        line = line.strip()
        if not line:
            continue
        if line in ("DEP Retention", "SU Retention", "Welcome Flow"):
            campaign = line
        elif line.startswith("Email "):
            email_label = line
        elif line.startswith("https://"):
            all_urls.append((line, lang, campaign, email_label))

# Check uniqueness
urls_only = [u[0] for u in all_urls]
unique = set(urls_only)
print(f"Total URLs: {len(urls_only)}")
print(f"Unique URLs: {len(unique)}")

if len(urls_only) != len(unique):
    from collections import Counter
    dupes = [u for u, c in Counter(urls_only).items() if c > 1]
    print(f"\nDUPLICATES FOUND: {len(dupes)}")
    for d in dupes:
        entries = [e for e in all_urls if e[0] == d]
        print(f"  URL: ...{d[-20:]}")
        for _, lang, camp, email in entries:
            print(f"    {lang} / {camp} / {email}")
else:
    print("ALL UNIQUE - OK!")

# Also show counts per lang/campaign
print("\nBreakdown:")
for fn in files:
    lang = fn.replace("банери лінк ", "").replace(".txt", "")
    for camp in ["DEP Retention", "SU Retention", "Welcome Flow"]:
        cnt = len([u for u in all_urls if u[1] == lang and u[2] == camp])
        if cnt:
            print(f"  {lang} / {camp}: {cnt} banners")
