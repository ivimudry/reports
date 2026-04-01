import os, re

fp = os.path.join('тексти/хейхо', 'Unsuccessful Deposit - Table data.txt')
with open(fp, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Fix trailing <br> at the end of rich_text values (before </td>)
fixed = 0
new_lines = []
for line in lines:
    if line.startswith('rich_text:'):
        # Remove trailing <br> tags right before the end
        original = line
        # Pattern: <br> at the very end after </td>
        line = re.sub(r'</td>(<br>)+\s*$', '</td>\n', line)
        # Pattern: <br> right before </td>
        line = re.sub(r'(<br>)+</td>', '</td>', line)
        if line != original:
            fixed += 1
    new_lines.append(line)

with open(fp, 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print(f'Removed trailing <br> from {fixed} rich_text lines')

# Count lines per block to verify structure
with open(fp, 'r', encoding='utf-8') as f:
    content = f.read()

blocks = content.split('name: ')
print(f'Total blocks: {len(blocks) - 1}')  # -1 for content before first name

# Verify each Email 2 block has full content
for block in blocks[1:]:
    bname = block.split('\n')[0].strip()
    if bname == 'Email 2':
        locale_line = [l for l in block.split('\n') if l.startswith('locale:')]
        locale = locale_line[0].split(':')[1].strip() if locale_line else '?'
        
        rt_lines = [l for l in block.split('\n') if l.startswith('rich_text:')]
        if rt_lines:
            rt = rt_lines[0]
            # Check for key content
            has_greeting = 'Hi ' in rt or 'Hallo ' in rt or 'Bonjour ' in rt or 'Hoi ' in rt
            has_deposit = 'COMPLETE DEPOSIT' in rt or 'EINZAHLUNG' in rt or 'DÉPÔT' in rt or 'STORTING' in rt
            has_support = 'CONTACT SUPPORT' in rt or 'KONTAKTIERE' in rt or 'CONTACTER' in rt or 'CONTACT MET' in rt
            has_thanks = 'Thanks' in rt or 'Danke' in rt or 'Merci' in rt or 'Bedankt' in rt
            has_bank = 'bank' in rt.lower()
            
            status = 'OK' if all([has_greeting, has_deposit, has_support, has_thanks, has_bank]) else 'ISSUE'
            missing = []
            if not has_greeting: missing.append('greeting')
            if not has_deposit: missing.append('deposit_btn')
            if not has_support: missing.append('support_btn')
            if not has_thanks: missing.append('thanks')
            if not has_bank: missing.append('bank_mention')
            
            print(f'Email 2 [{locale}]: {status} (len={len(rt)}) {f"MISSING: {missing}" if missing else ""}')
