"""
Convert RU implementation-guide .md files to .docx.
Reuses process_md() from convert_to_docx.py
"""
import os, sys

# Temporarily override SRC/DST before importing
SRC = r"c:\Projects\REPORTS\тексти\CuatroBet\implementation-guide-ru"
DST = r"c:\Projects\REPORTS\тексти\CuatroBet\implementation-guide-ru-docx"
os.makedirs(DST, exist_ok=True)

# Import process_md from the existing converter
sys.path.insert(0, r"c:\Projects\REPORTS\тексти\CuatroBet")
from convert_to_docx import process_md

# Process all .md files
for fname in sorted(os.listdir(SRC)):
    if not fname.endswith('.md'):
        continue
    src_path = os.path.join(SRC, fname)
    dst_name = fname.replace('.md', '.docx')
    dst_path = os.path.join(DST, dst_name)
    print(f"Converting {fname} -> {dst_name} ... ", end='')
    try:
        doc = process_md(src_path)
        doc.save(dst_path)
        print("OK")
    except Exception as e:
        print(f"ERROR: {e}")

print(f"\nDone! All files in: {DST}")
