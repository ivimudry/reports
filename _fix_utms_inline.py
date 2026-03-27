import os, re, glob

FOLDER = os.path.join("тексти", "пантери нова праця")

# campaign name per file
CAMPAIGNS = {
    "DEP ret - Table data.txt": "dep",
    "nut 1 - Table data.txt": "nutrition1",
    "nut 2 - Table data.txt": "nutrition2",
    "welcome - Table data.txt": "welcome",
    "Unsuccessful Deposit - Table data.txt": "faileddep",
}

# Standard UTM suffix (HTML-encoded &amp;)
def utm_amp(campaign, email_num):
    return (f"utm_campaign={campaign}&amp;utm_source=customerio"
            f"&amp;utm_medium=email&amp;utm_language=en&amp;utm_email={email_num}")

# Standard UTM suffix (plain &)
def utm_plain(campaign, email_num):
    return (f"utm_campaign={campaign}&utm_source=customerio"
            f"&utm_medium=email&utm_language=en&utm_email={email_num}")

total_all = 0

for fname, campaign in CAMPAIGNS.items():
    fpath = os.path.join(FOLDER, fname)
    with open(fpath, "r", encoding="utf-8") as f:
        text = f.read()

    # Split into email blocks by "name: Email N"
    # Find all email block boundaries
    email_starts = list(re.finditer(r'^name: Email (\d+)', text, re.MULTILINE))
    
    file_fixes = 0
    
    for idx, match in enumerate(email_starts):
        email_num = int(match.group(1))
        block_start = match.start()
        block_end = email_starts[idx + 1].start() if idx + 1 < len(email_starts) else len(text)
        block = text[block_start:block_end]
        new_block = block
        
        # === FIX 1: Copyright link ===
        # Pattern A: href="https://games.pantherbet.co.za/" (no UTM)
        new_block = re.sub(
            r'href="https://games\.pantherbet\.co\.za/"',
            f'href="https://games.pantherbet.co.za/?{utm_amp(campaign, email_num)}"',
            new_block
        )
        # Pattern B: href="https://pantherbet.co.za/?utm_campaign=... (wrong domain, Unsuccessful Deposit)
        new_block = re.sub(
            r'href="https://pantherbet\.co\.za/\?utm_campaign=[^"]*"',
            f'href="https://games.pantherbet.co.za/?{utm_amp(campaign, email_num)}"',
            new_block
        )
        
        # === FIX 2: Live Chat inline links (HTML-encoded &amp;) ===
        # Match: games.pantherbet.co.za/support?utm_campaign=...&amp;...&amp;utm_email=N
        new_block = re.sub(
            r'https://games\.pantherbet\.co\.za/support\?utm_campaign=[^"]*?utm_email=\d+',
            f'https://games.pantherbet.co.za/support?{utm_amp(campaign, email_num)}',
            new_block
        )
        
        if new_block != block:
            fixes = 0
            # Count differences roughly
            for old_c, new_c in zip(block.split('\n'), new_block.split('\n')):
                if old_c != new_c:
                    fixes += 1
            file_fixes += fixes
            text = text[:block_start] + new_block + text[block_end:]
            # Recalculate positions since text length may have changed
            diff = len(new_block) - len(block)
            for j in range(idx + 1, len(email_starts)):
                email_starts[j] = re.search(
                    r'^name: Email ' + str(int(email_starts[j].group(1))),
                    text[email_starts[j].start() + diff:],
                    re.MULTILINE
                )
                # This won't work perfectly, let's just re-find all after edit

    # Re-process from scratch to avoid offset issues - do it iteratively
    # Actually, let's just re-read and do a simpler approach:
    # Re-read the original, process linearly
    
    # Simpler approach: re-read original and process per-line
    with open(fpath, "r", encoding="utf-8") as f:
        text = f.read()
    
    new_text = text
    current_email = 0
    lines = new_text.split('\n')
    new_lines = []
    
    for line in lines:
        # Track which email we're in
        m = re.match(r'^name: Email (\d+)', line)
        if m:
            current_email = int(m.group(1))
        
        if current_email > 0:
            original_line = line
            
            # FIX 1: Copyright - no UTM
            line = re.sub(
                r'href="https://games\.pantherbet\.co\.za/"',
                lambda _: f'href="https://games.pantherbet.co.za/?{utm_amp(campaign, current_email)}"',
                line
            )
            
            # FIX 2: Copyright - wrong domain (pantherbet.co.za without games.)
            line = re.sub(
                r'href="https://pantherbet\.co\.za/\?utm_campaign=[^"]*"',
                lambda _: f'href="https://games.pantherbet.co.za/?{utm_amp(campaign, current_email)}"',
                line
            )
            
            # FIX 3: Live chat inline (HTML &amp; encoded)
            line = re.sub(
                r'https://games\.pantherbet\.co\.za/support\?utm_campaign=[^"]*?(?=&amp;utm_email=\d+)&amp;utm_email=\d+',
                lambda _: f'https://games.pantherbet.co.za/support?{utm_amp(campaign, current_email)}',
                line
            )
            
            # FIX 3b: fallback if pattern is slightly different  
            line = re.sub(
                r'(https://games\.pantherbet\.co\.za/support\?)utm_campaign=\w+&amp;utm_source=customerio&amp;utm_language=en&amp;utm_email=\d+',
                lambda _: f'https://games.pantherbet.co.za/support?{utm_amp(campaign, current_email)}',
                line
            )
            
            # FIX 3c: with utm_medium already present
            line = re.sub(
                r'(https://games\.pantherbet\.co\.za/support\?)utm_campaign=\w+&amp;utm_medium=email&amp;utm_source=customerio&amp;utm_email=\d+&amp;utm_language=en',
                lambda _: f'https://games.pantherbet.co.za/support?{utm_amp(campaign, current_email)}',
                line
            )
            
            if line != original_line:
                file_fixes += 1
        
        new_lines.append(line)
    
    new_text = '\n'.join(new_lines)
    
    if new_text != text:
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(new_text)
        print(f"  {file_fixes} lines fixed in {fname}")
        total_all += file_fixes
    else:
        print(f"  0 changes in {fname}")

print(f"\nTotal: {total_all} lines fixed across all files")

# Verify - check for remaining issues
print("\n--- VERIFICATION ---")
for fname, campaign in CAMPAIGNS.items():
    fpath = os.path.join(FOLDER, fname)
    with open(fpath, "r", encoding="utf-8") as f:
        text = f.read()
    
    # Check for bare copyright links
    bare = len(re.findall(r'href="https://games\.pantherbet\.co\.za/"', text))
    if bare:
        print(f"  WARNING: {bare} bare copyright links remain in {fname}")
    
    # Check for wrong domain copyright
    wrong_domain = len(re.findall(r'href="https://pantherbet\.co\.za/\?', text))
    if wrong_domain:
        print(f"  WARNING: {wrong_domain} wrong-domain copyright links in {fname}")
    
    # Check for missing utm_medium in support links
    support_no_medium = len(re.findall(r'pantherbet\.co\.za/support\?(?:(?!utm_medium).)*"', text))
    # Actually let's just count support links total vs those with utm_medium
    all_support = re.findall(r'games\.pantherbet\.co\.za/support\?[^"]+', text)
    for s in all_support:
        if 'utm_medium' not in s:
            print(f"  WARNING: support link missing utm_medium in {fname}: ...{s[-60:]}")
    
    # Check for wrong campaign in support links
    for s in all_support:
        m = re.search(r'utm_campaign=(\w+)', s)
        if m and m.group(1) != campaign:
            print(f"  WARNING: wrong campaign '{m.group(1)}' (should be '{campaign}') in {fname}")

print("\nDone.")
