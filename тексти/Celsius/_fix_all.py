# -*- coding: utf-8 -*-
"""
Comprehensive fix script for all Celsius campaign files:
1. Replace em-dashes and en-dashes with regular hyphens (all files, all locales)
2. Fix Hungarian terminology (Free Spins, Bonus, NoRisk Free Bet) with suffix grammar
3. Fix Polish terminology
4. Fix Failed Deposit Email 4 untranslated sentence in HU/PL
"""
import re, os, sys, io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

CELSIUS_DIR = r'c:\Projects\REPORTS\тексти\Celsius'
FILES = [
    'DEP Retention - Table data.txt',
    'FTD Retention Flow - Table data.txt',
    'Failed Deposit Flow - Table data.txt',
    'Nutrition 2 - Table data.txt',
    'Nutrition 3 - Table data.txt',
    'SU Retention - Table data.txt',
    'Welcome Flow - Table data.txt',
]

stats = {'dashes': 0, 'hu_fields': 0, 'pl_fields': 0, 'details': []}

def log(msg):
    stats['details'].append(msg)

# ── HU fixes ──────────────────────────────────────────────────

def fix_hu_subject_preheader(text):
    """Fix HU terminology in subject/preheader."""
    orig = text
    text = text.replace('NoRisk Free Bet', 'Kockázatmentes Fogadás')
    text = text.replace('NoRisk Bet', 'Kockázatmentes Fogadás')
    text = text.replace('FreeBet', 'Kockázatmentes Fogadás')
    text = text.replace('Free Spins', 'Ingyenes Pörgetés')
    text = text.replace('Free Spin', 'Ingyenes Pörgetés')
    text = re.sub(r'\bBonus\b', 'Bónusz', text)
    text = re.sub(r'\bbonus\b', 'bónusz', text)
    return text

def fix_hu_body(text):
    """Fix HU terminology in body HTML (text_2, text_3, rich_text) with suffix grammar."""
    # NoRisk Free Bet + suffixes (most specific first!)
    text = text.replace('NoRisk Free Bet</strong>tel', 'Kockázatmentes Fogadás</strong>sal')
    text = text.replace('NoRisk Free Bet</strong>edet', 'Kockázatmentes Fogadás</strong>odat')
    text = text.replace('NoRisk Free Bet</strong>ed', 'Kockázatmentes Fogadás</strong>od')
    text = text.replace('NoRisk Free Bet', 'Kockázatmentes Fogadás')
    text = text.replace('NoRisk Bet', 'Kockázatmentes Fogadás')
    text = text.replace('FreeBet', 'Kockázatmentes Fogadás')

    # Free Spins + suffixes
    text = text.replace('Free Spins</strong>szel', 'Ingyenes Pörgetés</strong>sel')
    text = text.replace('Free Spins</strong>od', 'Ingyenes Pörgetés</strong>ed')
    text = text.replace('Free Spins', 'Ingyenes Pörgetés')
    text = text.replace('Free Spin', 'Ingyenes Pörgetés')

    # Bonus (word boundary to avoid URL "bonuses")
    text = re.sub(r'\bBonus\b', 'Bónusz', text)
    text = re.sub(r'\bbonus\b', 'bónusz', text)
    return text

def fix_hu_button(text):
    """Fix HU button text (ALL CAPS)."""
    text = text.replace('NORISK BÉTED', 'KOCKÁZATMENTES FOGADÁSOD')
    text = text.replace('NORISK BET', 'KOCKÁZATMENTES FOGADÁS')
    text = text.replace('NORISK', 'KOCKÁZATMENTES')
    text = text.replace('FREE SPINS', 'INGYENES PÖRGETÉS')
    text = text.replace('FREE SPIN', 'INGYENES PÖRGETÉS')
    # Fix BONUSZ without accent → BÓNUSZ (handles BONUSZOMAT etc.)
    text = text.replace('BONUSZ', 'BÓNUSZ')
    # Fix standalone BONUS → BÓNUSZ
    text = re.sub(r'\bBONUS\b', 'BÓNUSZ', text)
    return text

# ── PL fixes ──────────────────────────────────────────────────

def fix_pl_subject_preheader(text):
    """Fix PL terminology in subject/preheader."""
    text = text.replace('NoRisk Free Bet', 'Zakład Bez Ryzyka')
    text = text.replace('NoRisk Bet', 'Zakład Bez Ryzyka')
    text = text.replace('FreeBet', 'Zakład Bez Ryzyka')
    text = text.replace('Free Spins', 'Darmowe Spiny')
    text = text.replace('Free Spin', 'Darmowy Spin')
    return text

def fix_pl_body(text):
    """Fix PL terminology in body HTML."""
    text = text.replace('NoRisk Free Bet', 'Zakład Bez Ryzyka')
    text = text.replace('NoRisk Bet', 'Zakład Bez Ryzyka')
    text = text.replace('FreeBet', 'Zakład Bez Ryzyka')
    text = text.replace('Free Spins', 'Darmowe Spiny')
    text = text.replace('Free Spin', 'Darmowy Spin')
    return text

def fix_pl_button(text):
    """Fix PL button text (ALL CAPS)."""
    text = text.replace('NORISK BET', 'ZAKŁAD BEZ RYZYKA')
    text = text.replace('NORISK', 'BEZ RYZYKA')
    text = text.replace('FREE SPINS', 'DARMOWE SPINY')
    text = text.replace('FREE SPIN', 'DARMOWY SPIN')
    return text

# ── Failed Deposit Email 4 ──────────────────────────────────

EN_SENTENCE_VARIANTS = [
    "Looks like your deposit didn\u2019t complete. Finish it now and we\u2019ll add 20 Free Spins on Gates of Olympus as a thank you.",
    "Looks like your deposit didn't complete. Finish it now and we'll add 20 Free Spins on Gates of Olympus as a thank you.",
]
HU_SENTENCE = "Úgy tűnik, a befizetésed nem fejeződött be. Fejezd be most, és hozzáadunk 20 Ingyenes Pörgetést a Gates of Olympus játékban köszönetképpen."
PL_SENTENCE = "Wygląda na to, że Twoja wpłata nie została ukończona. Dokończ ją teraz, a dodamy 20 Darmowych Spinów w Gates of Olympus w podziękowaniu."

# ── Main processing ──────────────────────────────────────────

def process_file(filepath):
    fname = os.path.basename(filepath)
    is_faildep = 'Failed Deposit' in fname
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Step 1: Fix dashes globally
    dash_before = content.count('\u2014') + content.count('\u2013')
    content = content.replace('\u2014', '-').replace('\u2013', '-')
    if dash_before > 0:
        stats['dashes'] += dash_before
        log(f"  [{fname}] Replaced {dash_before} dashes")
    
    # Step 2: Parse into blocks and fix terminology
    blocks = content.split('\n\n')
    new_blocks = []
    
    for block in blocks:
        if not block.strip():
            new_blocks.append(block)
            continue
        
        lines = block.split('\n')
        # Parse fields
        field_order = []  # list of (key, value) or ('__RAW__', raw_line)
        fields = {}
        
        for line in lines:
            colon_idx = line.find(':')
            if colon_idx > 0 and not line[:colon_idx].strip().startswith('<'):
                key = line[:colon_idx].strip()
                val = line[colon_idx+1:].lstrip(' ')  # preserve value as-is after ": "
                fields[key] = val
                field_order.append(('FIELD', key))
            else:
                field_order.append(('RAW', line))
        
        locale = fields.get('locale', '')
        name = fields.get('name', '')
        
        if locale == 'hu-HU':
            hu_changed = False
            
            for fld in ['subject', 'preheader']:
                if fld in fields:
                    orig = fields[fld]
                    fixed = fix_hu_subject_preheader(orig)
                    if fixed != orig:
                        fields[fld] = fixed
                        hu_changed = True
                        log(f"  [{fname}] {name}/{locale} {fld}: fixed HU terms")
            
            for fld in ['text_1', 'text_2', 'text_3', 'rich_text']:
                if fld in fields:
                    orig = fields[fld]
                    fixed = fix_hu_body(orig)
                    # Also handle Failed Deposit Email 4
                    if is_faildep and name == 'Email 4' and fld == 'rich_text':
                        for en_v in EN_SENTENCE_VARIANTS:
                            if en_v in fixed:
                                fixed = fixed.replace(en_v, HU_SENTENCE)
                                log(f"  [{fname}] {name}/{locale} rich_text: translated English sentence")
                                break
                    if fixed != orig:
                        fields[fld] = fixed
                        hu_changed = True
                        log(f"  [{fname}] {name}/{locale} {fld}: fixed HU terms")
            
            for fld in ['button_text_1', 'promocode_button_1']:
                if fld in fields:
                    orig = fields[fld]
                    fixed = fix_hu_button(orig)
                    if fixed != orig:
                        fields[fld] = fixed
                        hu_changed = True
                        log(f"  [{fname}] {name}/{locale} {fld}: fixed HU button")
            
            if hu_changed:
                stats['hu_fields'] += 1
        
        elif locale == 'pl-PL':
            pl_changed = False
            
            for fld in ['subject', 'preheader']:
                if fld in fields:
                    orig = fields[fld]
                    fixed = fix_pl_subject_preheader(orig)
                    if fixed != orig:
                        fields[fld] = fixed
                        pl_changed = True
                        log(f"  [{fname}] {name}/{locale} {fld}: fixed PL terms")
            
            for fld in ['text_1', 'text_2', 'text_3', 'rich_text']:
                if fld in fields:
                    orig = fields[fld]
                    fixed = fix_pl_body(orig)
                    if is_faildep and name == 'Email 4' and fld == 'rich_text':
                        for en_v in EN_SENTENCE_VARIANTS:
                            if en_v in fixed:
                                fixed = fixed.replace(en_v, PL_SENTENCE)
                                log(f"  [{fname}] {name}/{locale} rich_text: translated English sentence")
                                break
                    if fixed != orig:
                        fields[fld] = fixed
                        pl_changed = True
                        log(f"  [{fname}] {name}/{locale} {fld}: fixed PL terms")
            
            for fld in ['button_text_1', 'promocode_button_1']:
                if fld in fields:
                    orig = fields[fld]
                    fixed = fix_pl_button(orig)
                    if fixed != orig:
                        fields[fld] = fixed
                        pl_changed = True
                        log(f"  [{fname}] {name}/{locale} {fld}: fixed PL button")
            
            if pl_changed:
                stats['pl_fields'] += 1
        
        # Reconstruct block
        result_lines = []
        for item_type, item_val in field_order:
            if item_type == 'RAW':
                result_lines.append(item_val)
            else:
                result_lines.append(f"{item_val}: {fields[item_val]}")
        
        new_blocks.append('\n'.join(result_lines))
    
    content = '\n\n'.join(new_blocks)
    
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

# ── Run ──────────────────────────────────────────────────────

print("=" * 60)
print("CELSIUS COMPREHENSIVE FIX")
print("=" * 60)

files_changed = 0
for fname in FILES:
    fpath = os.path.join(CELSIUS_DIR, fname)
    if not os.path.exists(fpath):
        print(f"SKIP (not found): {fname}")
        continue
    
    print(f"\nProcessing: {fname}")
    changed = process_file(fpath)
    if changed:
        files_changed += 1
        print(f"  -> MODIFIED")
    else:
        print(f"  -> no changes")

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)
print(f"Files modified: {files_changed}/{len(FILES)}")
print(f"Dashes replaced: {stats['dashes']}")
print(f"HU blocks fixed: {stats['hu_fields']}")
print(f"PL blocks fixed: {stats['pl_fields']}")

if stats['details']:
    print(f"\nDetailed changes ({len(stats['details'])} entries):")
    for d in stats['details']:
        print(d)

# Save detailed log
log_path = os.path.join(CELSIUS_DIR, '_fix_log.txt')
with open(log_path, 'w', encoding='utf-8') as f:
    f.write(f"Files modified: {files_changed}/{len(FILES)}\n")
    f.write(f"Dashes replaced: {stats['dashes']}\n")
    f.write(f"HU blocks fixed: {stats['hu_fields']}\n")
    f.write(f"PL blocks fixed: {stats['pl_fields']}\n\n")
    for d in stats['details']:
        f.write(d + '\n')
print(f"\nLog saved: {log_path}")
