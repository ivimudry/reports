"""
Targeted fixes for the 7 remaining fr-FR fields with <br> issues.
Each fix is specified as exact search→replace pairs within text_2.
"""
import re, os

DIR = r'c:\Projects\REPORTS\тексти\Celsius'
BR_RE = re.compile(r'<br\s*/?>', re.I)

# Define targeted fixes: (file, email_name, [(old_str, new_str), ...])
FIXES = [
    # ── DEP 3C: 6→7 ──
    # Move <br><br> from after Celsius Casino to after last winner; add <br> at sentence break
    ('DEP Retention - Table data.txt', 'Email 3C', [
        # After last winner, insert <br><br> before "Les tables"
        ('\u20ac19 400 Les tables', '\u20ac19 400<br><br>Les tables'),
        # Sentence break: "prêtes." → add <br> before "Coupez"
        ('pr\u00eates. Coupez', 'pr\u00eates.<br>Coupez'),
        # Remove wrongly placed <br><br> after Celsius Casino</strong>
        ('Celsius Casino</strong><br><br>- votre', 'Celsius Casino</strong> - votre'),
    ]),

    # ── DEP 3S: 7→8 ──
    # Move <br><br> from after "coup." to after last winner; add <br> at sentence breaks
    ('DEP Retention - Table data.txt', 'Email 3S', [
        # After last winner, insert <br><br>
        ('\u20ac19 450 Ils', '\u20ac19 450<br><br>Ils'),
        # Existing wrong double → single at "coup."
        ('coup.<br><br>Les cotes', 'coup.<br>Les cotes'),
    ]),

    # ── DEP 6C: 6→7 ──
    # Same pattern as 3C
    ('DEP Retention - Table data.txt', 'Email 6C', [
        # After last winner
        ('\u20ac24 100 Les machines', '\u20ac24 100<br><br>Les machines'),
        # Sentence break
        ('v\u00f4tre. Entrez', 'v\u00f4tre.<br>Entrez'),
        # Remove wrong <br><br> after "vôtre."
        ('v\u00f4tre.<br><br>Entrez', 'v\u00f4tre.<br>Entrez'),
    ]),

    # ── SU 3C: 4→6 ──
    # Fix <br><br> placement around emoji and code
    ('SU Retention - Table data.txt', 'Email 3C', [
        # After emoji 🆙
        ('\U0001f199 Faites', '\U0001f199<br><br>Faites'),
        # Remove wrong <br><br> after </strong>
        ('140%</strong><br><br>- le boost', '140%</strong> - le boost'),
        # Before code line
        ('Celsius. Utilisez', 'Celsius.<br><br>Utilisez'),
    ]),

    # ── SU 4C: 2→6 ──
    ('SU Retention - Table data.txt', 'Email 4C', [
        # After emoji 🍬
        ('\U0001f36c Obtenez', '\U0001f36c<br><br>Obtenez'),
        # Before code line
        ('gourmand. Utilisez', 'gourmand.<br><br>Utilisez'),
    ]),

    # ── SU 5C: 3→7 ──
    ('SU Retention - Table data.txt', 'Email 5C', [
        # Paragraph break after "pour de vrai."
        ('de vrai. Faites', 'de vrai.<br><br>Faites'),
        # Fix existing wrong <br><br> → &nbsp;<br>
        ('d\u00e9marrer.<br><br>L\u2019offre', 'd\u00e9marrer.&nbsp;<br>L\u2019offre'),
        # Before code after 🎱
        ('\U0001f3b1 Utilisez', '\U0001f3b1<br><br>Utilisez'),
        # Fix single→double after code
        ('POWER140</strong><br>Lancez', 'POWER140</strong><br><br>Lancez'),
    ]),

    # ── Nutrition #2 4CL: 5→7 ──
    ('Nutrition #2 - Table data.txt', 'Email 4CL', [
        # Fix misplaced <br> inside first <strong>
        ('<strong><br>\U0001f48e Dt', '<strong>\U0001f48e Dt'),
        # Fix between first and second winner
        ('800</strong> <strong><br>\U0001f48e e', '800</strong><br><strong>\U0001f48e e'),
        # Fix between second and third winner  
        ('420</strong> <strong>\U0001f48e \u2022\u2022p', '420</strong><br><strong>\U0001f48e \u2022\u2022p'),
        # After last winner, add <br><br>
        ('760</strong> Votre nom', '760</strong><br><br>Votre nom'),
        # Fix double→&nbsp;single after "gagnants."
        ('gagnants.<br><br>Rejoignez', 'gagnants.&nbsp;<br>Rejoignez'),
        # Fix single→double before CTA
        ('coup !<br>Jouez', 'coup !<br><br>Jouez'),
    ]),
]


total_applied = 0

for fname, email_name, replacements in FIXES:
    fpath = os.path.join(DIR, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Find the fr-FR block for this email
    blocks = []
    current = []
    for i, raw in enumerate(lines):
        stripped = raw.rstrip('\n').rstrip('\r')
        if not stripped.strip():
            if current:
                blocks.append(current)
                current = []
            continue
        idx = stripped.find(': ')
        if idx > 0:
            current.append((i, stripped[:idx], stripped[idx + 2:]))
    if current:
        blocks.append(current)

    # Find target block
    target_line = None
    target_key = None
    target_val = None
    for block in blocks:
        d = {k: v for _, k, v in block}
        if d.get('name') == email_name and d.get('locale') == 'fr-FR':
            for li, k, v in block:
                if k == 'text_2':
                    target_line = li
                    target_key = k
                    target_val = v
                    break
            break

    if target_line is None:
        print(f"  NOT FOUND: {fname} / {email_name}")
        continue

    before_br = len(BR_RE.findall(target_val))
    new_val = target_val
    applied = 0

    for old_s, new_s in replacements:
        if old_s in new_val:
            new_val = new_val.replace(old_s, new_s, 1)
            applied += 1
        else:
            print(f"    SKIP {fname}/{email_name}: '{old_s[:60]}...' not found")

    after_br = len(BR_RE.findall(new_val))

    if new_val != target_val:
        lines[target_line] = f'{target_key}: {new_val}\n'
        with open(fpath, 'w', encoding='utf-8') as f:
            f.writelines(lines)
        total_applied += applied

    # Get Default br count for comparison
    for block in blocks:
        d = {k: v for _, k, v in block}
        if d.get('name') == email_name and d.get('locale') == 'Default':
            def_val = {k: v for _, k, v in block}.get('text_2', '')
            def_br = len(BR_RE.findall(def_val))
            break
    else:
        def_br = '?'

    status = 'OK' if after_br == def_br else f'MISMATCH ({after_br}/{def_br})'
    print(f"  {fname}/{email_name}: {before_br}→{after_br}/{def_br} ({applied} replacements) — {status}")

print(f"\nDone: {total_applied} total replacements applied.")

# ── Final verification across all 4 files ──
print("\n=== FINAL VERIFICATION ===")
all_files = [
    'DEP Retention - Table data.txt',
    'SU Retention - Table data.txt',
    'FTD Retention Flow - Table data.txt',
    'Nutrition #2 - Table data.txt',
    'Nutrition #3 - Table data.txt',
    'Welcome Flow - Table data.txt',
]
all_ok = True
for fname in all_files:
    fpath = os.path.join(DIR, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    blocks = []
    current = []
    for i, raw in enumerate(lines):
        stripped = raw.rstrip('\n').rstrip('\r')
        if not stripped.strip():
            if current:
                blocks.append(current)
                current = []
            continue
        idx = stripped.find(': ')
        if idx > 0:
            current.append((i, stripped[:idx], stripped[idx + 2:]))
    if current:
        blocks.append(current)

    index = {}
    for b in blocks:
        d = {k: v for _, k, v in b}
        index[(d.get('name', ''), d.get('locale', ''))] = b

    fails = []
    for b in blocks:
        d = {k: v for _, k, v in b}
        if d.get('locale') != 'fr-FR':
            continue
        name = d.get('name', '')
        db = index.get((name, 'Default'))
        if not db:
            continue
        dd = {k: v for _, k, v in db}
        for _, key, fr_val in b:
            if not (key.startswith('text_') or key == 'rich_text'):
                continue
            def_val = dd.get(key, '')
            if not def_val:
                continue
            def_n = len(BR_RE.findall(def_val))
            fr_n = len(BR_RE.findall(fr_val))
            if def_n > 0 and def_n != fr_n:
                fails.append(f"    {name}|{key}: Default={def_n} fr-FR={fr_n}")
                all_ok = False

    if fails:
        print(f"  ISSUES {fname}:")
        for f in fails:
            print(f)
    else:
        print(f"  OK {fname}")

print(f"\n{'ALL OK!' if all_ok else 'SOME ISSUES REMAIN'}")
