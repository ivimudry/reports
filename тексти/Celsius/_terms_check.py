import os, re

d = r'c:\Projects\REPORTS\тексти\Celsius'
files = sorted([f for f in os.listdir(d) if f.endswith('.txt') and 'Table data' in f])

# Collect hu-HU and pl-PL subjects to see how terms are translated
for locale in ['hu-HU', 'pl-PL']:
    print(f'\n{"="*60}')
    print(f'  {locale} - subject samples with key terms')
    print(f'{"="*60}')
    
    seen = set()
    for fname in files:
        path = os.path.join(d, fname)
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        blocks = content.strip().split('\n\n')
        for block in blocks:
            lines = block.strip().split('\n')
            data = {}
            for line in lines:
                idx = line.find(': ')
                if idx > 0:
                    data[line[:idx].strip()] = line[idx+2:].strip()
            
            if data.get('locale') != locale:
                continue
            
            subj = data.get('subject', '')
            btn = data.get('button_text_1', '')
            name = data.get('name', '')
            
            # Show samples with key terms
            for term in ['Free Sp', 'Ingyenes', 'Darmow', 'NoRisk', 'Kockázat', 'Bez Ryzyka', 
                         'FreeBet', 'Fogadás', 'Zakład', 'Cashback', 'Bonus', 'Bónusz',
                         'Deposit', 'Befizet', 'Wpłat']:
                if term.lower() in subj.lower() or term.lower() in btn.lower():
                    key = f'{locale}|{subj[:50]}'
                    if key not in seen:
                        seen.add(key)
                        print(f'  {name} ({fname[:20]})')
                        print(f'    subject: {subj[:100]}')
                        print(f'    button:  {btn}')
                    break
            
            if len(seen) >= 15:
                break
        if len(seen) >= 15:
            break
