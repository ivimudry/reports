import re
import os

def parse_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Split into blocks by "name: " at start of line
    blocks = re.split(r'\n(?=name: )', '\n' + content)
    blocks = [b.strip() for b in blocks if b.strip()]
    
    emails = []
    for block in blocks:
        # Parse fields
        fields = {}
        for line in block.split('\n'):
            match = re.match(r'^(\w[\w_]*?):\s*(.*)', line)
            if match:
                fields[match.group(1)] = match.group(2).strip()
        
        if not fields.get('name'):
            continue
        
        # Skip fr-FR
        if fields.get('locale', '') == 'fr-FR':
            continue
        
        email = {
            'name': fields.get('name', ''),
            'locale': fields.get('locale', ''),
            'subject': fields.get('subject', ''),
            'preheader': fields.get('preheader', ''),
            'header_html_tag': fields.get('header_html_tag', ''),
            'text_1': fields.get('text_1', ''),
            'text_2': fields.get('text_2', ''),
            'button_text_1': fields.get('button_text_1', ''),
            'promocode_button_1': fields.get('promocode_button_1', ''),
        }
        
        # Extract data-promocode from header
        header_promo = re.findall(r'data-promocode="([^"]*)"', email['header_html_tag'])
        email['header_promos'] = header_promo[0] if header_promo else '-'
        
        # Extract promo codes from text (class="promocode">CODE<)
        text_promos = re.findall(r'class="promocode"[^>]*>([^<]+)<', email['text_2'])
        if not text_promos:
            text_promos = re.findall(r'class="promocode"[^>]*>([^<]+)<', email['text_1'])
        email['text_promos'] = ', '.join(text_promos) if text_promos else '-'
        
        # Strip HTML from text_2 for analysis
        clean_text = re.sub(r'<[^>]+>', ' ', email['text_2'])
        clean_text = re.sub(r'&nbsp;', ' ', clean_text)
        clean_text = re.sub(r'\s+', ' ', clean_text).strip()
        email['clean_text'] = clean_text
        
        # Extract bonuses - look for percentage offers, Free Spins, FreeBets, Cashback, etc.
        bonuses = []
        
        # Pattern: "X% ... up to €Y" or "X% Bonus"
        bonus_patterns = [
            r'(\d+%\s+(?:Welcome\s+)?(?:up to|Bonus|bonus|NoRisk|FreeBet|FreeBets|Cashback|Reload|Re-?load|Deposit)[^<.]*?)(?:\.|<|$)',
            r'(\d+%\s+(?:up to|bonus)[^<.]*)',
            r'(\d+st[^<]*?(?:up to|Bonus|FS|Free Spins)[^<]*)',
            r'(\d+nd[^<]*?(?:up to|Bonus|FS|Free Spins)[^<]*)',
            r'(\d+rd[^<]*?(?:up to|Bonus|FS|Free Spins)[^<]*)',
            r'(\d+th[^<]*?(?:up to|Bonus|FS|Free Spins)[^<]*)',
        ]
        
        # Better approach: extract structured bonus lines from HTML
        # Look for lines like "1st: 100% up to €500 + 150 FS"
        deposit_bonuses = re.findall(r'(\d+(?:st|nd|rd|th)[^<]*?(?:up to|Bonus|FS|Free Spins|FreeBet|FreeBets)[^<]*)', email['text_2'])
        for b in deposit_bonuses:
            clean_b = re.sub(r'&nbsp;', ' ', b).strip()
            if clean_b and clean_b not in bonuses:
                bonuses.append(clean_b)
        
        # Look for "X% Bonus/bonus" patterns
        pct_bonuses = re.findall(r'(\d+%[^<]*?(?:Bonus|bonus|up to|Free Spins|FS|FreeBet|FreeBets|Cashback)[^<]*)', email['text_2'])
        for b in pct_bonuses:
            clean_b = re.sub(r'&nbsp;', ' ', b).strip()
            # Don't add if it's already captured in deposit_bonuses
            already = False
            for existing in bonuses:
                if clean_b in existing or existing in clean_b:
                    already = True
                    break
            if clean_b and not already:
                bonuses.append(clean_b)
        
        # Free Spins standalone mentions
        fs_mentions = re.findall(r'(\d+\s+Free\s+Spins?(?:\s+on\s+[^<]*)?)', email['text_2'])
        for b in fs_mentions:
            clean_b = re.sub(r'&nbsp;', ' ', b).strip()
            already = False
            for existing in bonuses:
                if clean_b in existing or existing in clean_b:
                    already = True
                    break
            if clean_b and not already:
                bonuses.append(clean_b)
        
        # FreeBets standalone
        fb_mentions = re.findall(r'(\d+%?\s*(?:NoRisk\s+)?FreeBets?\s+(?:Bonus\s+)?(?:up to\s+[€$£]\d+[^<]*)?)', email['text_2'])
        for b in fb_mentions:
            clean_b = re.sub(r'&nbsp;', ' ', b).strip()
            already = False
            for existing in bonuses:
                if clean_b in existing or existing in clean_b:
                    already = True
                    break
            if clean_b and not already:
                bonuses.append(clean_b)
        
        # "up to €X + Y FS" patterns
        upto_patterns = re.findall(r'(up to\s+[€$£][\d,]+(?:\s*\+\s*\d+\s*(?:Free Spins|FS))?)', email['text_2'])
        
        # Cashback mentions
        cashback = re.findall(r'((?:\d+%?\s+)?[Cc]ashback[^<]*)', email['text_2'])
        for b in cashback:
            clean_b = re.sub(r'&nbsp;', ' ', b).strip()
            already = False
            for existing in bonuses:
                if clean_b.lower() in existing.lower() or existing.lower() in clean_b.lower():
                    already = True
                    break
            if clean_b and not already:
                bonuses.append(clean_b)
        
        # "€X bonus" or "$X bonus"
        money_bonus = re.findall(r'([€$£]\d+[\d,]*\s+(?:bonus|Bonus|cashback|Cashback|reward|free bet|FreeBet))', email['text_2'])
        for b in money_bonus:
            clean_b = re.sub(r'&nbsp;', ' ', b).strip()
            if clean_b and clean_b not in bonuses:
                bonuses.append(clean_b)
        
        email['bonuses'] = '; '.join(bonuses) if bonuses else '-'
        
        # Extract game names - slot names typically
        game_patterns = [
            r'on\s+(?:the\s+)?([A-Z][A-Za-z\s\']+(?:by\s+[A-Za-z\s]+)?)\s*[.<]',
            r'slot[s]?\s+(?:like\s+)?([A-Z][A-Za-z\s\'-]+)',
            r'game[s]?\s+(?:like\s+)?(?:include\s+)?([A-Z][A-Za-z\s\'-]+)',
            r'play\s+([A-Z][A-Za-z\s\']+(?:by\s+[A-Za-z\s]+)?)',
        ]
        
        games = []
        # More targeted: look for "on GameName by Provider" pattern
        game_by = re.findall(r'on\s+([A-Z][A-Za-z\s\'-]+?by\s+[A-Za-z\s]+?)(?:\.|<|,|\s{2,})', email['text_2'])
        for g in game_by:
            clean_g = re.sub(r'&nbsp;', ' ', g).strip().rstrip('.')
            if clean_g and len(clean_g) > 3:
                games.append(clean_g)
        
        # Look for known game name pattern in text - capitalized multi-word after "on "
        if not games:
            game_on = re.findall(r'on\s+(?:the\s+)?([A-Z][A-Za-z]+(?:\s+[A-Za-z]+){0,5}?)(?:\s+slot|\s+game|\.|!|<|,)', email['text_2'])
            for g in game_on:
                clean_g = g.strip()
                # Filter out common false positives
                skip_words = ['Your', 'The', 'Our', 'This', 'That', 'Just', 'All', 'More', 'Every', 'Sports', 'Slots',
                              'Live Casino', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday',
                              'Celsius', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
                              'September', 'October', 'November', 'December', 'NoRisk', 'Match']
                if clean_g and not any(clean_g.startswith(sw) for sw in skip_words) and len(clean_g) > 3:
                    games.append(clean_g)
        
        # Also check for specific game names in bold tags
        bold_games = re.findall(r'<strong>\s*([A-Z][A-Za-z\s\'-]+?(?:by\s+[A-Za-z\s]+)?)\s*</strong>', email['text_2'])
        for g in bold_games:
            clean_g = g.strip()
            # Check if it looks like a game name (not a bonus description)
            if (not re.search(r'\d', clean_g) and 
                not any(w in clean_g.lower() for w in ['bonus', 'deposit', 'free spin', 'freespin', 'freebet', 'cashback', 'reload', 'welcome', 'norisk', 'huge', 'tons']) and
                len(clean_g) > 3 and
                clean_g not in games):
                # Still filter known non-games
                if not any(clean_g.startswith(sw) for sw in ['Your', 'The ', 'Our ', 'This', 'That', 'Just', 'All ', 'More', 'Every']):
                    games.append(clean_g)
        
        email['games'] = ', '.join(games) if games else '-'
        
        # Content summary
        text_lower = clean_text.lower()
        if not bonuses and email['text_promos'] == '-':
            # No bonuses, no promos - what's the email about?
            if 'winner' in text_lower or 'won' in text_lower:
                summary = 'weekly winners showcase'
            elif 'top' in text_lower and ('game' in text_lower or 'slot' in text_lower):
                summary = 'top games/slots showcase'
            elif 'come back' in text_lower or 'miss' in text_lower or 'waiting' in text_lower:
                summary = 'motivational - come back and play'
            elif 'cashback' in text_lower:
                summary = 'cashback bonus offer'
            elif 'new game' in text_lower or 'new slot' in text_lower or 'just landed' in text_lower:
                summary = 'new game announcement'
            elif 'tournament' in text_lower:
                summary = 'tournament announcement'
            elif 'vip' in text_lower:
                summary = 'VIP program info'
            elif 'loyalty' in text_lower:
                summary = 'loyalty program info'
            elif 'mobile' in text_lower or 'app' in text_lower:
                summary = 'mobile app promotion'
            elif 'sport' in text_lower or 'bet' in text_lower or 'match' in text_lower:
                summary = 'sports betting motivation'
            elif 'responsible' in text_lower or 'limit' in text_lower:
                summary = 'responsible gaming reminder'
            else:
                summary = 'general engagement'
        elif bonuses and email['text_promos'] != '-':
            summary = 'bonus offer with promo code'
        elif bonuses:
            summary = 'bonus offer'
        elif email['text_promos'] != '-':
            summary = 'promo code offer'
        else:
            summary = 'general engagement'
        
        email['summary'] = summary
        
        emails.append(email)
    
    return emails

# Process all files
base_dir = r"C:\Projects\REPORTS\тексти"
files = [
    ("Welcome Flow", "Welcome Flow - Table data.txt"),
    ("SU Retention", "SU Retention - Table data.txt"),
    ("FTD Retention Flow", "FTD Retention Flow - Table data.txt"),
    ("Nutrition #2", "Nutrition #2 - Table data.txt"),
    ("Nutrition #3", "Nutrition #3 - Table data.txt"),
    ("DEP Retention", "DEP Retention - Table data.txt"),
]

for campaign_name, filename in files:
    filepath = os.path.join(base_dir, filename)
    emails = parse_file(filepath)
    
    print(f"\n{'='*80}")
    print(f"CAMPAIGN: {campaign_name} ({len(emails)} emails)")
    print(f"{'='*80}")
    
    for e in emails:
        parts = [e['name']]
        parts.append(f"Bonus: {e['bonuses']}")
        parts.append(f"TextPromo: {e['text_promos']}")
        parts.append(f"HeaderPromo: {e['header_promos']}")
        parts.append(f"Game: {e['games']}")
        parts.append(f"Content: {e['summary']}")
        if e['promocode_button_1']:
            parts.append(f"PromoBtn: {e['promocode_button_1']}")
        
        print(' | '.join(parts))
    
    print(f"\nTotal: {len(emails)} emails")
