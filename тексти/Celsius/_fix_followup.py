# -*- coding: utf-8 -*-
"""
Follow-up fixes:
1. Nutrition #2 and #3 dash replacement (missed due to wrong filename)
2. Failed Deposit Email 4: fix partially-translated sentence in HU/PL rich_text
"""
import os, sys, io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

CELSIUS_DIR = r'c:\Projects\REPORTS\тексти\Celsius'

# ── Fix 1: Nutrition files dashes ──

for fname in ['Nutrition #2 - Table data.txt', 'Nutrition #3 - Table data.txt']:
    fpath = os.path.join(CELSIUS_DIR, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    em = content.count('\u2014')
    en = content.count('\u2013')
    total = em + en
    
    if total > 0:
        content = content.replace('\u2014', '-').replace('\u2013', '-')
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"[{fname}] Replaced {total} dashes (em={em}, en={en})")
    else:
        print(f"[{fname}] No dashes found")

# ── Fix 2: Failed Deposit Email 4 sentence ──

fpath = os.path.join(CELSIUS_DIR, 'Failed Deposit Flow - Table data.txt')
with open(fpath, 'r', encoding='utf-8') as f:
    content = f.read()

# The first fix script already replaced "Free Spins" inside the sentence,
# so now the HU rich_text has "20 Ingyenes Pörgetés on Gates" and PL has "20 Darmowe Spiny on Gates"
# We need to find and replace these partially-translated sentences

hu_partial_variants = [
    "Looks like your deposit didn\u2019t complete. Finish it now and we\u2019ll add 20 Ingyenes Pörgetés on Gates of Olympus as a thank you.",
    "Looks like your deposit didn't complete. Finish it now and we'll add 20 Ingyenes Pörgetés on Gates of Olympus as a thank you.",
    # Original English (in case dashes weren't in apostrophes)
    "Looks like your deposit didn\u2019t complete. Finish it now and we\u2019ll add 20 Free Spins on Gates of Olympus as a thank you.",
    "Looks like your deposit didn't complete. Finish it now and we'll add 20 Free Spins on Gates of Olympus as a thank you.",
]

pl_partial_variants = [
    "Looks like your deposit didn\u2019t complete. Finish it now and we\u2019ll add 20 Darmowe Spiny on Gates of Olympus as a thank you.",
    "Looks like your deposit didn't complete. Finish it now and we'll add 20 Darmowe Spiny on Gates of Olympus as a thank you.",
    "Looks like your deposit didn\u2019t complete. Finish it now and we\u2019ll add 20 Free Spins on Gates of Olympus as a thank you.",
    "Looks like your deposit didn't complete. Finish it now and we'll add 20 Free Spins on Gates of Olympus as a thank you.",
]

HU_SENTENCE = "Úgy tűnik, a befizetésed nem fejeződött be. Fejezd be most, és hozzáadunk 20 Ingyenes Pörgetést a Gates of Olympus játékban köszönetképpen."
PL_SENTENCE = "Wygląda na to, że Twoja wpłata nie została ukończona. Dokończ ją teraz, a dodamy 20 Darmowych Spinów w Gates of Olympus w podziękowaniu."

changed = False

# Process block by block to target only HU and PL locales
blocks = content.split('\n\n')
new_blocks = []

for block in blocks:
    if not block.strip():
        new_blocks.append(block)
        continue
    
    # Quick check if this is Email 4
    if 'name: Email 4' not in block:
        new_blocks.append(block)
        continue
    
    if 'locale: hu-HU' in block:
        orig = block
        for variant in hu_partial_variants:
            if variant in block:
                block = block.replace(variant, HU_SENTENCE)
                print(f"[Failed Deposit] Email 4/hu-HU: Replaced partial EN→HU sentence")
                changed = True
                break
        if block == orig:
            # Check if the sentence was already translated
            if HU_SENTENCE in block:
                print(f"[Failed Deposit] Email 4/hu-HU: Already has correct HU sentence")
            else:
                # Try to find any remaining English
                if 'Looks like your deposit' in block:
                    print(f"[Failed Deposit] Email 4/hu-HU: WARNING - still has English, trying broader match")
                    # Find and show the context
                    idx = block.find('Looks like your deposit')
                    end_idx = block.find('thank you.', idx)
                    if end_idx > 0:
                        old_sentence = block[idx:end_idx + len('thank you.')]
                        print(f"  Found: {old_sentence[:120]}...")
                        block = block.replace(old_sentence, HU_SENTENCE)
                        changed = True
                        print(f"  -> Replaced with HU translation")
                else:
                    print(f"[Failed Deposit] Email 4/hu-HU: No English sentence found (might already be OK)")
    
    elif 'locale: pl-PL' in block:
        orig = block
        for variant in pl_partial_variants:
            if variant in block:
                block = block.replace(variant, PL_SENTENCE)
                print(f"[Failed Deposit] Email 4/pl-PL: Replaced partial EN→PL sentence")
                changed = True
                break
        if block == orig:
            if PL_SENTENCE in block:
                print(f"[Failed Deposit] Email 4/pl-PL: Already has correct PL sentence")
            else:
                if 'Looks like your deposit' in block:
                    print(f"[Failed Deposit] Email 4/pl-PL: WARNING - still has English, trying broader match")
                    idx = block.find('Looks like your deposit')
                    end_idx = block.find('thank you.', idx)
                    if end_idx > 0:
                        old_sentence = block[idx:end_idx + len('thank you.')]
                        print(f"  Found: {old_sentence[:120]}...")
                        block = block.replace(old_sentence, PL_SENTENCE)
                        changed = True
                        print(f"  -> Replaced with PL translation")
                else:
                    print(f"[Failed Deposit] Email 4/pl-PL: No English sentence found (might already be OK)")
    
    new_blocks.append(block)

content = '\n\n'.join(new_blocks)

if changed:
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"\n[Failed Deposit] File saved with updates")
else:
    print(f"\n[Failed Deposit] No changes needed")
