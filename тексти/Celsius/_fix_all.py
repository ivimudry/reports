"""
Fix all 25 formatting issues found by audit.
Each fix is an exact substring replacement within a specific file/email/locale/field.
"""
import os

DIR = r'c:\Projects\REPORTS\тексти\Celsius'

def fix_in_file(fname, replacements):
    """Apply a list of (old, new, description) replacements to a file."""
    fpath = os.path.join(DIR, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    for old, new, desc in replacements:
        if old not in content:
            print(f"  !! NOT FOUND: {desc}")
            print(f"     Searching for: {repr(old[:80])}...")
            continue
        count = content.count(old)
        if count > 1:
            print(f"  !! AMBIGUOUS ({count} matches): {desc}")
            continue
        content = content.replace(old, new)
        print(f"  OK: {desc}")
    
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)


# ════════════════════════════════════════════════
# DEP Retention
# ════════════════════════════════════════════════
print("=== DEP Retention ===")
fix_in_file('DEP Retention - Table data.txt', [
    # --- Email 3C fr-FR: wrap winners in <strong> ---
    (
        ':<br><br>\u200d🏆 Lu\u2022\u2022\u2022\u20227 - €52 300<br>🏆 S\u2022\u2022\u2022\u2022\u2022n - €35 900<br>🏆 Bi\u2022\u2022\u2022\u2022\u2022t - €19 400<br><br>',
        ':<br><br><strong>🏆 Lu\u2022\u2022\u2022\u20227 - €52 300<br>🏆 S\u2022\u2022\u2022\u2022\u2022n - €35 900<br>🏆 Bi\u2022\u2022\u2022\u2022\u2022t - €19 400</strong><br><br>',
        'DEP 3C: add <strong> around winners'
    ),
    # --- Email 3S fr-FR: wrap winners in <strong> ---
    (
        ':<br><br>\u200d💰 Str\u2022\u2022\u2022\u2022\u2022X - €42 810<br>💰 Go\u2022\u2022\u2022\u2022\u2022er - €31 200<br>💰 Pa\u2022\u2022\u2022\u2022\u2022ng - €19 450<br><br>',
        ':<br><br><strong>💰 Str\u2022\u2022\u2022\u2022\u2022X - €42 810<br>💰 Go\u2022\u2022\u2022\u2022\u2022er - €31 200<br>💰 Pa\u2022\u2022\u2022\u2022\u2022ng - €19 450</strong><br><br>',
        'DEP 3S: add <strong> around winners'
    ),
    # --- Email 6C fr-FR: wrap winners in <strong> ---
    (
        ':<br><br>\u200d🏆 Ja\u2022\u2022\u2022\u2022g - €61 200<br>🏆 Sp\u2022\u2022\u2022\u2022r - €42 800<br>🏆 Eli\u2022\u2022\u2022\u2022er - €24 100<br><br>',
        ':<br><br><strong>🏆 Ja\u2022\u2022\u2022\u2022g - €61 200<br>🏆 Sp\u2022\u2022\u2022\u2022r - €42 800<br>🏆 Eli\u2022\u2022\u2022\u2022er - €24 100</strong><br><br>',
        'DEP 6C: add <strong> around winners'
    ),
    # --- Email 8S fr-FR: wrap winners in <strong> + fix <br><br> after ---
    (
        ':<br><br>\u200d💰 G\u2022\u2022\u2022\u2022er88 - €45 600<br>💰 O\u2022\u2022\u2022\u2022\u2022ero - €32 150<br>💰 Be\u2022\u2022\u2022\u2022rd - €18 700 Le tableau',
        ':<br><br><strong>💰 G\u2022\u2022\u2022\u2022er88 - €45 600<br>💰 O\u2022\u2022\u2022\u2022\u2022ero - €32 150<br>💰 Be\u2022\u2022\u2022\u2022rd - €18 700</strong><br><br>Le tableau',
        'DEP 8S: add <strong> + fix <br><br> after winners'
    ),
])

print()
print("=== DONE ===")
