import os, re, html

def strip_html(s):
    s = re.sub(r'<br\s*/?>', ' | ', s)
    s = re.sub(r'<[^>]+>', '', s)
    s = html.unescape(s)
    return s.strip()

files = sorted([f for f in os.listdir('.') if f.endswith('.txt') and 'Table data' in f])

en_markers = [
    'Hello,', 'Start your', 'Whether you', 'journey at',
    'first deposit', 'Free Spins', 'waiting for', 'reels are',
    'Celsius Casino Team.', 'This is an automated', 'Unsubscribe',
    'You are receiving', 'because during', 'All Rights Reserved',
    'the action', 'keep the', 'built around', 'extra value',
    'More play', 'big wins', 'still waiting', 'Support',
    'Kick off', 'Unlock', 'unleash', 'triple', 'covers',
    'massive', 'explore', 'loaded with', 'just for you',
    'ready to', "don't miss", 'your way', 'play now',
    'grab your', 'claim your', 'every game', 'play your',
    'get more', 'head back', 'come back', 'deposit now',
    'one more', 'time to', 'spin the', 'bet on',
    'win big', 'three reasons', 'game on', 'cashback bonus',
    'sports betting', 'live casino', 'slots,', 'welcome bonus',
    'sign-up', 'no-risk', 'risk-free', 'your account',
    'complete your', 'finish your', 'we noticed', 'forgot something',
]

for fname in files:
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()
    
    blocks = content.strip().split('\n\n')
    
    print(f'\n{"="*60}')
    print(f'  {fname}')
    print(f'{"="*60}')
    
    found_issues = False
    for block in blocks:
        lines = block.strip().split('\n')
        data = {}
        for line in lines:
            idx = line.find(': ')
            if idx > 0:
                key = line[:idx].strip()
                val = line[idx+2:].strip()
                data[key] = val
        
        locale = data.get('locale', '')
        if locale not in ('hu-HU', 'pl-PL'):
            continue
        
        name = data.get('name', '')
        subj = data.get('subject', '')
        preh = data.get('preheader', '')
        t1 = strip_html(data.get('text_1', ''))
        t2 = strip_html(data.get('text_2', ''))
        t3 = strip_html(data.get('text_3', ''))
        btn = data.get('button_text_1', '')
        t12 = strip_html(data.get('text_12', ''))
        t13 = strip_html(data.get('text_13', ''))
        
        issues = []
        for fn, fv in [('subject', subj), ('preheader', preh), ('text_1', t1), 
                        ('text_2', t2), ('text_3', t3), ('button', btn),
                        ('text_12', t12), ('text_13', t13)]:
            for ew in en_markers:
                if ew.lower() in fv.lower():
                    issues.append((fn, ew))
                    break
        
        if issues:
            found_issues = True
            print(f'\n  [{locale}] {name}')
            for fn, ew in issues:
                print(f'    !! {fn} has EN marker: "{ew}"')
            # Print only flagged fields
            flagged_fields = set(fn for fn, _ in issues)
            for fn, label, val, maxlen in [
                ('subject', 'subject', subj, 100),
                ('preheader', 'prehead', preh, 100),
                ('text_1', 'text_1', t1, 100),
                ('text_2', 'text_2', t2, 200),
                ('text_3', 'text_3', t3, 100),
                ('button', 'button', btn, 50),
                ('text_12', 'text_12', t12, 120),
                ('text_13', 'text_13', t13, 120),
            ]:
                if fn in flagged_fields:
                    print(f'    {label}: {val[:maxlen]}')
    
    if not found_issues:
        print('  ALL OK - no English markers found')
    print(f'  --- done ---')
