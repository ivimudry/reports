import os, re

BASE = r"c:\Projects\REPORTS\тексти\Celsius"
FILES = [
    "Welcome Flow - Table data.txt",
    "DEP Retention - Table data.txt",
    "SU Retention - Table data.txt",
    "FTD Retention Flow - Table data.txt",
    "Nutrition #2 - Table data.txt",
    "Nutrition #3 - Table data.txt",
    "Failed Deposit Flow - Table data.txt",
]

def parse_blocks(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    blocks = re.split(r'\n{2,}', content)
    results = []
    for block in blocks:
        lines = block.strip().split('\n')
        if not lines:
            continue
        data = {}
        current_key = None
        for line in lines:
            m = re.match(r'^(\w[\w_]*?):\s*(.*)', line)
            if m:
                current_key = m.group(1)
                data[current_key] = m.group(2)
            elif current_key:
                data[current_key] = data[current_key] + '\n' + line
        if 'name' in data and 'locale' in data:
            results.append(data)
    return results

def extract_visible_text(html):
    text = re.sub(r'<[^>]+>', '', html)
    text = re.sub(r'\s+', ' ', text).strip()
    return text[:200]

for fname in FILES:
    fpath = os.path.join(BASE, fname)
    if not os.path.exists(fpath):
        print(f"SKIP: {fname}")
        continue
    blocks = parse_blocks(fpath)
    fr_blocks = [b for b in blocks if b.get('locale') == 'fr-FR']
    print(f"\n{'='*80}")
    print(f"FILE: {fname}")
    print(f"Total fr-FR blocks: {len(fr_blocks)}")
    print(f"{'='*80}")
    
    for b in fr_blocks:
        name = b.get('name', '?')
        subj = b.get('subject', '')
        preh = b.get('preheader', '')
        btn = b.get('button_text_1', '')
        
        t1_raw = b.get('text_1', '')
        t2_raw = b.get('text_2', '')
        t3_raw = b.get('text_3', '')
        rt_raw = b.get('rich_text', '')
        
        t1_vis = extract_visible_text(t1_raw)
        t2_vis = extract_visible_text(t2_raw)
        t3_vis = extract_visible_text(t3_raw)
        
        # Check if text looks French
        fr_markers = ['équipe', 'automatique', 'répondre', 'veuillez', 'Celsius Casino csapat', 'Zespół']
        t3_is_footer = any(m in t3_raw for m in fr_markers) or 'Celsius Casino Team' in t3_raw
        
        # Check if subject is still English
        en_markers = ['Your', 'Get', 'Bonus', 'Free Spins', 'Claim', 'Don\'t', 'Unlock', 'Top', 'Last', 'Big', 'Real', 'Play', 'Bet', 'Spin', 'Win', 'The', 'We', 'It\'s', 'No Risk']
        subj_is_en = any(m in subj for m in en_markers)
        
        needs_translation = []
        if subj_is_en:
            needs_translation.append('subject')
        if any(m in preh for m in en_markers):
            needs_translation.append('preheader')
        # Check text_1 for English
        if any(m.lower() in t1_vis.lower() for m in ['hello', 'player', 'friend', 'the floor', 'the reels', 'ready']):
            needs_translation.append('text_1')
        if any(m.lower() in t2_vis.lower() for m in ['your', 'you', 'deposit', 'bonus', 'code', 'claim', 'why play', 'top up']):
            needs_translation.append('text_2')
        if not t3_is_footer and t3_vis:
            needs_translation.append('text_3')
        if btn and all(c.isascii() for c in btn) and not any(m in btn for m in ['É', 'è', 'ê', 'à']):
            needs_translation.append('button')
        if rt_raw:
            needs_translation.append('rich_text')
            
        if needs_translation:
            print(f"\n  {name}: NEEDS [{', '.join(needs_translation)}]")
            print(f"    subject: {subj[:80]}")
            print(f"    preheader: {preh[:80]}")
            print(f"    button: {btn}")
            if 'text_1' in needs_translation:
                print(f"    text_1: {t1_vis[:100]}")
            if 'text_2' in needs_translation:
                print(f"    text_2: {t2_vis[:150]}")
            if 'text_3' in needs_translation:
                print(f"    text_3: {t3_vis[:150]}")
        else:
            print(f"\n  {name}: OK (already translated)")
