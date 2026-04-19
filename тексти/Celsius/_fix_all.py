"""
Fix all formatting issues found by audit in fr-FR locale.
Exact substring replacements based on manual file reading.
"""
import os, re

DIR = r'c:\Projects\REPORTS\тексти\Celsius'

total_fixes = 0

def fix_in_file(fname, replacements):
    """Apply a list of (old, new, description) replacements to a file."""
    global total_fixes
    fpath = os.path.join(DIR, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    for old, new, desc in replacements:
        if old not in content:
            print(f"  !! NOT FOUND: {desc}")
            # Show nearby context to debug
            for fragment in [old[:40], old[-40:]]:
                if fragment in content:
                    idx = content.index(fragment)
                    print(f"     Fragment found at pos {idx}")
            continue
        count = content.count(old)
        if count > 1:
            print(f"  !! AMBIGUOUS ({count} matches): {desc}")
            continue
        content = content.replace(old, new)
        total_fixes += 1
        print(f"  OK: {desc}")
    
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)


# ════════════════════════════════════════════════════════
# 1. DEP Retention — Winner <strong> wrapping (4 emails)
# ════════════════════════════════════════════════════════
print("=== DEP Retention ===")
fix_in_file('DEP Retention - Table data.txt', [
    # Email 3C fr-FR: wrap winners in <strong>
    (
        ':<br><br>🏆 Lu••••7 - €52 300<br>🏆 S•••••n - €35 900<br>🏆 Bi•••••t - €19 400<br><br>Les tables',
        ':<br><br><strong>🏆 Lu••••7 - €52 300<br>🏆 S•••••n - €35 900<br>🏆 Bi•••••t - €19 400</strong><br><br>Les tables',
        'DEP 3C: add <strong> around winners'
    ),
    # Email 3S fr-FR: wrap winners in <strong>
    (
        ':<br><br>💰 Str•••••X - €42 810<br>💰 Go•••••er - €31 200<br>💰 Pa•••••ng - €19 450<br><br>Ils',
        ':<br><br><strong>💰 Str•••••X - €42 810<br>💰 Go•••••er - €31 200<br>💰 Pa•••••ng - €19 450</strong><br><br>Ils',
        'DEP 3S: add <strong> around winners'
    ),
    # Email 6C fr-FR: wrap winners in <strong>
    (
        ':<br><br>🏆 Ja••••g - €61 200<br>🏆 Sp••••r - €42 800<br>🏆 Eli••••er - €24 100<br><br>Les machines',
        ':<br><br><strong>🏆 Ja••••g - €61 200<br>🏆 Sp••••r - €42 800<br>🏆 Eli••••er - €24 100</strong><br><br>Les machines',
        'DEP 6C: add <strong> around winners'
    ),
    # Email 8S fr-FR: wrap winners + add <br><br> + remove extra <br><br> after Celsius Sport
    (
        ':<br><br>💰 G••••er88 - €45 600<br>💰 O•••••ero - €32 150<br>💰 Be••••rd - €18 700 Le tableau',
        ':<br><br><strong>💰 G••••er88 - €45 600<br>💰 O•••••ero - €32 150<br>💰 Be••••rd - €18 700</strong><br><br>Le tableau',
        'DEP 8S: add <strong> + <br><br> after winners'
    ),
    # Email 8S fr-FR part 2: remove extra <br><br> after Celsius Sport to keep br count
    (
        '<strong>Celsius Sport</strong>.<br><br>Les cotes sont',
        '<strong>Celsius Sport</strong>. Les cotes sont',
        'DEP 8S: remove extra <br><br> after Celsius Sport'
    ),
])


# ════════════════════════════════════════════════════════
# 2. SU Retention — Winner <strong> structure + <i> + &nbsp; (2 emails)
# ════════════════════════════════════════════════════════
print("\n=== SU Retention ===")
fix_in_file('SU Retention - Table data.txt', [
    # Email 8C fr-FR: fix <strong> structure + <i> + &nbsp; + 🎰
    # Current: `: <strong><br><br>💰 H••H55 a gagné 44 190 $ sur The Dog House Megaways</strong> <strong><br>💰 y•••54 a décroché 28 670 $ sur Sweet Bonanza</strong> <strong><br>💰 Da••••K33d a remporté 13 520 $ sur Book of Dead</strong> Ce sont de vrais gains de vrais joueurs.<br><br>Il ne manque plus que votre premier tour.<br>🎰<br><br>`
    # Target: `:<br><br><strong>💰 H••H55 a gagné 44 190 $ sur The Dog House Megaways</strong><br><strong>💰 <i>y</i>•••54 a décroché 28 670 $ sur Sweet Bonanza</strong><br><strong>💰 Da••••K33d a remporté 13 520 $ sur Book of Dead</strong><br><br>Ce sont de vrais gains de vrais joueurs.&nbsp;<br>Il ne manque plus que votre premier tour. 🎰<br><br>`
    (
        'dernière : <strong><br><br>💰 H••H55 a gagné 44 190 $ sur The Dog House Megaways</strong> <strong><br>💰 y•••54 a décroché 28 670 $ sur Sweet Bonanza</strong> <strong><br>💰 Da••••K33d a remporté 13 520 $ sur Book of Dead</strong> Ce sont de vrais gains de vrais joueurs.<br><br>Il ne manque plus que votre premier tour.<br>🎰<br><br>',
        'dernière :<br><br><strong>💰 H••H55 a gagné 44 190 $ sur The Dog House Megaways</strong><br><strong>💰 <i>y</i>•••54 a décroché 28 670 $ sur Sweet Bonanza</strong><br><strong>💰 Da••••K33d a remporté 13 520 $ sur Book of Dead</strong><br><br>Ce sont de vrais gains de vrais joueurs.&nbsp;<br>Il ne manque plus que votre premier tour. 🎰<br><br>',
        'SU 8C: fix <strong> structure + <i>y</i> + &nbsp; + 🎰'
    ),
    # Email 10C fr-FR: fix <strong> structure + <i>
    # Current: `: <strong><br><br>🔥 Rich••••s a gagné 49 870 $ sur Gates of Olympus</strong> <strong><br>🔥 Bll• a décroché 27 430 $ sur Fruit Party 2</strong> <strong><br>🔥 Blu••••86s a remporté 15 980 $ sur Legacy of Dead</strong><br><br>Pas d'astuces`
    # Target: `:<br><br><strong>🔥 Rich••••s a gagné 49 870 $ sur Gates of Olympus</strong><br><strong>🔥 Bl<i>l</i>• a décroché 27 430 $ sur Fruit Party 2</strong><br><strong>🔥 Blu••••86s a remporté 15 980 $ sur Legacy of Dead</strong><br><br>Pas d'astuces`
    (
        'gros : <strong><br><br>🔥 Rich••••s a gagné 49 870 $ sur Gates of Olympus</strong> <strong><br>🔥 Bll• a décroché 27 430 $ sur Fruit Party 2</strong> <strong><br>🔥 Blu••••86s a remporté 15 980 $ sur Legacy of Dead</strong><br><br>Pas',
        'gros :<br><br><strong>🔥 Rich••••s a gagné 49 870 $ sur Gates of Olympus</strong><br><strong>🔥 Bl<i>l</i>• a décroché 27 430 $ sur Fruit Party 2</strong><br><strong>🔥 Blu••••86s a remporté 15 980 $ sur Legacy of Dead</strong><br><br>Pas',
        'SU 10C: fix <strong> structure + <i>l</i>'
    ),
])


# ════════════════════════════════════════════════════════
# 3. Nutrition #2 — <strong> structure + <i> tags (4 emails)
# ════════════════════════════════════════════════════════
print("\n=== Nutrition #2 ===")
fix_in_file('Nutrition #2 - Table data.txt', [
    # Email 2CL fr-FR: fix <strong> structure + <i>
    # Current: `<strong><br>🔥 Fi••••65y - €145 320</strong> <strong><br>🔥 le••d4• - €110 780</strong> <strong>🔥 A••••in43 - €69 200</strong><br><br>`
    # Target: `<strong>🔥 Fi••••65y - €145 320</strong><br><strong>🔥 l<i>e••d4</i>• - €110 780</strong><br><strong>🔥 A••••in43 - €69 200</strong><br><br>`
    (
        '<strong><br>🔥 Fi••••65y - €145 320</strong> <strong><br>🔥 le••d4• - €110 780</strong> <strong>🔥 A••••in43 - €69 200</strong><br><br>Trois joueurs, trois gains massifs.<br><br>Serez-vous',
        '<strong>🔥 Fi••••65y - €145 320</strong><br><strong>🔥 l<i>e••d4</i>• - €110 780</strong><br><strong>🔥 A••••in43 - €69 200</strong><br><br>Trois joueurs, trois gains massifs. Serez-vous',
        'N2 2CL: fix <strong> structure + <i>e••d4</i>'
    ),
    # Email 2CS fr-FR: fix <strong> structure + <i>
    # Current: `<strong><br>🏆 Alex••••y - €145 320</strong> <strong><br>🏆 l••677 - €110 780</strong> <strong>🏆 i66••••7n - €69 200</strong><br><br>Trois joueurs, trois gains massifs - tous en tournant leurs machines préférées.<br><br>Serez-vous`
    # Target: `<strong>🏆 Alex••••y - €145 320</strong><br><strong>🏆 l••677<i> - €110 780</i></strong><br><strong>🏆 i66••••7n - €69 200</strong><br><br>Trois joueurs, trois gains massifs - tous en tournant leurs machines préférées. Serez-vous`
    (
        '<strong><br>🏆 Alex••••y - €145 320</strong> <strong><br>🏆 l••677 - €110 780</strong> <strong>🏆 i66••••7n - €69 200</strong><br><br>Trois joueurs, trois gains massifs - tous en tournant leurs machines préférées.<br><br>Serez-vous',
        '<strong>🏆 Alex••••y - €145 320</strong><br><strong>🏆 l••677<i> - €110 780</i></strong><br><strong>🏆 i66••••7n - €69 200</strong><br><br>Trois joueurs, trois gains massifs - tous en tournant leurs machines préférées. Serez-vous',
        'N2 2CS: fix <strong> structure + <i> - €110 780</i>'
    ),
    # Email 4CL fr-FR: restore <i> tags (strong wrapping is already correct)
    # Current: `<strong>💎 Dt••••s - €49 800</strong><br><strong>💎 e•••95 - €33 420</strong><br><strong>💎 ••p•••sh•• - €21 760</strong>`
    # Target: `<strong>💎 Dt••••s<i> - </i>€49 800</strong><br><strong><i></i><i>💎 </i>e•••95<i> </i>- €33 420</strong><br><strong><i></i><i>💎 </i>••p•••sh•• - €21 760</strong>`
    (
        '<strong>💎 Dt••••s - €49 800</strong><br><strong>💎 e•••95 - €33 420</strong><br><strong>💎 ••p•••sh•• - €21 760</strong>',
        '<strong>💎 Dt••••s<i> - </i>€49 800</strong><br><strong><i></i><i>💎 </i>e•••95<i> </i>- €33 420</strong><br><strong><i></i><i>💎 </i>••p•••sh•• - €21 760</strong>',
        'N2 4CL: restore <i> tags in winners'
    ),
    # Email 7CS fr-FR: fix <strong> structure + <i> + &nbsp; + 🎰
    # Current: `<strong>🥇 Li•••n8• - €45 320</strong> <strong><br>🥈 a••7tz - €38 940</strong> <strong><br>🥉 h••••in - €26 580</strong> Votre nom pourrait être sur la prochaine liste des champions.<br><br>Il suffit d'un tour chanceux !<br>🎰<br><br>`
    # Target: `<strong>🥇 L<i>i•••n8</i>• - €45 320</strong><br><strong>🥈 a••7tz - €38 940</strong><br><strong>🥉 h••••in - €26 580</strong><br><br>Votre nom pourrait être sur la prochaine liste des champions.&nbsp;<br>Il suffit d'un tour chanceux ! 🎰<br><br>`
    (
        '<strong>🥇 Li•••n8• - €45 320</strong> <strong><br>🥈 a••7tz - €38 940</strong> <strong><br>🥉 h••••in - €26 580</strong> Votre nom pourrait être sur la prochaine liste des champions.<br><br>Il suffit d\'un tour chanceux !<br>🎰<br><br>',
        '<strong>🥇 L<i>i•••n8</i>• - €45 320</strong><br><strong>🥈 a••7tz - €38 940</strong><br><strong>🥉 h••••in - €26 580</strong><br><br>Votre nom pourrait être sur la prochaine liste des champions.&nbsp;<br>Il suffit d\'un tour chanceux ! 🎰<br><br>',
        'N2 7CS: fix <strong> + <i>i•••n8</i> + &nbsp; + 🎰'
    ),
])


# ════════════════════════════════════════════════════════
# 4. Welcome Flow — Extra <br> + &nbsp; issues (5 emails)
# ════════════════════════════════════════════════════════
print("\n=== Welcome Flow ===")
fix_in_file('Welcome Flow - Table data.txt', [
    # Email 1M fr-FR: fix extra <br><br> (4→2) + &nbsp; → <br><br>
    # Current: `jeu.<br><br><br><br>Que vous aimiez...cashback et prolongez l'action.&nbsp; Plus de jeu.`
    # Target: `jeu.<br><br>Que vous aimiez...cashback et prolongez l'action.<br><br>Plus de jeu.`
    (
        'jeu.<br><br><br><br>Que',
        'jeu.<br><br>Que',
        'WF 1M: fix extra <br> (4→2)'
    ),
    (
        "l'action.&nbsp; Plus de jeu.",
        "l'action.<br><br>Plus de jeu.",
        'WF 1M: fix &nbsp; → <br><br>'
    ),
    # Email 2S fr-FR: fix extra <br><br> + &nbsp;
    # Current: `pari.&nbsp;<br><br><br><br>Choisissez...parler.&nbsp; Pour rendre`
    # Target: `pari.&nbsp;<br><br>Choisissez...parler.<br><br>Pour rendre`
    (
        'pari.&nbsp;<br><br><br><br>Choisissez',
        'pari.&nbsp;<br><br>Choisissez',
        'WF 2S: fix extra <br> (4→2)'
    ),
    (
        'parler.&nbsp; Pour rendre',
        'parler.<br><br>Pour rendre',
        'WF 2S: fix &nbsp; → <br><br>'
    ),
    # Email 3S fr-FR: fix extra <br><br> + &nbsp;
    # Current: `pari.&nbsp;<br><br><br><br>Que vous misiez...coup.&nbsp; Et pour`
    # Target: `pari.&nbsp;<br><br>Que vous misiez...coup.<br><br>Et pour`
    (
        'pari.&nbsp;<br><br><br><br>Que',
        'pari.&nbsp;<br><br>Que',
        'WF 3S: fix extra <br> (4→2)'
    ),
    (
        'coup.&nbsp; Et pour',
        'coup.<br><br>Et pour',
        'WF 3S: fix &nbsp; → <br><br>'
    ),
    # Email 7C fr-FR: fix extra <br> after winners + &nbsp;
    # Current: `$</strong>&nbsp;<br><br><br>Pas d'astuces...réels.&nbsp; Prêt à tenter`
    # Target: `$</strong><br><br>Pas d'astuces...réels.&nbsp;<br>Prêt à tenter`
    (
        '$</strong>&nbsp;<br><br><br>Pas',
        '$</strong><br><br>Pas',
        'WF 7C: fix &nbsp;+extra <br> after winners'
    ),
    (
        'réels.&nbsp; Prêt à tenter',
        'réels.&nbsp;<br>Prêt à tenter',
        'WF 7C: fix &nbsp;space → &nbsp;<br>'
    ),
])


# ════════════════════════════════════════════════════════
# Summary
# ════════════════════════════════════════════════════════
print(f"\n{'='*60}")
print(f"Total fixes applied: {total_fixes}")
print(f"{'='*60}")
