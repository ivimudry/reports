#!/usr/bin/env python3
"""Show email structure: name + locale pairs for DEP, SU, Welcome files."""
import os, glob

DIR = r"c:\Projects\REPORTS\тексти\Celsius"
files_to_check = [
    "DEP Retention - Table data.txt",
    "SU Retention - Table data.txt", 
    "Welcome Flow - Table data.txt",
]

for fn in files_to_check:
    fp = os.path.join(DIR, fn)
    with open(fp, "r", encoding="utf-8") as f:
        lines = f.readlines()
    
    print(f"\n=== {fn} ({len(lines)} lines) ===")
    name = None
    for line in lines:
        s = line.rstrip()
        if s.startswith("name: "):
            name = s[6:]
        elif s.startswith("locale: "):
            locale = s[8:]
            print(f"  {name} | {locale}")
