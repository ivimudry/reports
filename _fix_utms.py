"""Fix all UTM links across 5 campaign Table data files."""
import re, os

ROOT = r'C:\Projects\REPORTS\тексти\пантери нова праця'

# Campaign file → utm_campaign value
CAMPAIGNS = {
    'welcome - Table data.txt': 'welcome',
    'nut 1 - Table data.txt': 'nutrition1',
    'nut 2 - Table data.txt': 'nutrition2',
    'DEP ret - Table data.txt': 'dep',
    'Unsuccessful Deposit - Table data.txt': 'faileddep',
}

BASE_GAME = 'https://games.pantherbet.co.za/?fast-deposit=modal'
BASE_IG   = 'https://www.instagram.com/pantherbet_za?igsh=cmozYTJxNG5td3Zn'
BASE_FB   = 'https://www.facebook.com/share/1GfKVBAET9/?mibextid=wwXIfr'

def utm(campaign, email_num):
    return f'&utm_campaign={campaign}&utm_source=customerio&utm_medium=email&utm_language=en&utm_email={email_num}'

LINK_FIELDS = {'logo_href', 'banner_href', 'button_href_1'}
SOCIAL_FIELDS = {'instagram_href', 'facebook_href'}

total_fixes = 0

for fname, campaign in CAMPAIGNS.items():
    fpath = os.path.join(ROOT, fname)
    if not os.path.exists(fpath):
        print(f'  SKIP (not found): {fname}')
        continue

    with open(fpath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    email_num = 1  # fallback
    fixes = 0
    new_lines = []

    for line in lines:
        stripped = line.rstrip('\n').rstrip('\r')

        # Track current email number from name: lines
        m = re.match(r'^name:\s*Email\s*#?(\d+)', stripped)
        if m:
            email_num = int(m.group(1))

        # Fix logo_href, banner_href, button_href_1
        for field in LINK_FIELDS:
            if stripped.startswith(f'{field}:'):
                new_url = f'{BASE_GAME}{utm(campaign, email_num)}'
                new_line = f'{field}: {new_url}\n'
                if new_line != line:
                    fixes += 1
                line = new_line
                break

        # Fix instagram_href
        if stripped.startswith('instagram_href:'):
            new_url = f'{BASE_IG}{utm(campaign, email_num)}'
            new_line = f'instagram_href: {new_url}\n'
            if new_line != line:
                fixes += 1
            line = new_line

        # Fix facebook_href
        if stripped.startswith('facebook_href:'):
            new_url = f'{BASE_FB}{utm(campaign, email_num)}'
            new_line = f'facebook_href: {new_url}\n'
            if new_line != line:
                fixes += 1
            line = new_line

        new_lines.append(line)

    with open(fpath, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)

    print(f'  {fname}: {fixes} fixes')
    total_fixes += fixes

print(f'\nDone: {total_fixes} total fixes across {len(CAMPAIGNS)} files')
