import sys

filepath = r"c:\Projects\REPORTS\тексти\Celsius\DEP Retention - Table data.txt"

with open(filepath, 'r', encoding='utf-8') as f:
    lines = f.readlines()

current_name = ""
current_locale = ""
changes = 0

SQ = '\u2019'  # right single quotation mark
EM = '\u2014'  # em dash

for i in range(len(lines)):
    line = lines[i]
    s = line.strip()

    if s.startswith('name: '):
        current_name = s[6:]
    elif s.startswith('locale: '):
        current_locale = s[8:]

    if current_name != 'Email 1C':
        continue

    # ===== HU =====
    if current_locale == 'hu-HU':
        if s.startswith('subject:') and 'Power Up Your Play' in s:
            lines[i] = line.replace('170% Bonus: Power Up Your Play Today',
                                    '170% b\u00f3nusz: Fokozza j\u00e1t\u00e9k\u00e1t m\u00e9g ma')
            changes += 1

        elif s.startswith('preheader:') and 'help you win at the tables' in s:
            for q in [SQ, "'"]:
                trial = line.replace(f'Look what{q}s inside to help you win at the tables',
                                     'N\u00e9zze meg, mi seg\u00edthet \u00d6nnek a nyer\u00e9sben az asztalokn\u00e1l')
                if trial != line:
                    lines[i] = trial; break
            changes += 1

        elif s.startswith('text_1:') and 'the floor is yours' in s:
            lines[i] = line.replace('default:"Player"', 'default:"J\u00e1t\u00e9kos"')
            lines[i] = lines[i].replace(', the floor is yours!', ', a sz\u00f3 a ti\u00e9d!')
            changes += 1

        elif s.startswith('text_2:') and 'Why play on just your deposit' in s:
            for q in [SQ, "'"]:
                old = f'Why play on just your deposit when you can play with <strong>170%</strong> more? We{q}re supercharging your next top-up so you can stay in longer and chase bigger moments.'
                new = 'Mi\u00e9rt j\u00e1tszana csak a befizet\u00e9s\u00e9vel, amikor <strong>170%</strong>-kal t\u00f6bbel is j\u00e1tszhat? Felturb\u00f3zzuk a k\u00f6vetkez\u0151 felt\u00f6lt\u00e9s\u00e9t, hogy tov\u00e1bb maradjon \u00e9s nagyobb pillanatokat \u00e9lhessen meg.'
                trial = line.replace(old, new)
                if trial != line:
                    lines[i] = trial; break
            changes += 1

        elif s.startswith('text_3:') and 'SURGE170' in s and 'Enter <strong' in s:
            for d in [EM, '\u2014']:
                old = f'Enter <strong class="promocode">SURGE170</strong> before making your next deposit to unlock your <strong>170% Bonus</strong> and turn your balance into a real advantage.<br><br>The action is live at <strong>Celsius Casino</strong> {d} claim your <strong>170% Bonus</strong>, pick your favorite table, and make your move with confidence.'
                new = f'\u00cdrd be a <strong class="promocode">SURGE170</strong> k\u00f3dot a k\u00f6vetkez\u0151 befizet\u00e9sed el\u0151tt, hogy feloldd a <strong>170%-os b\u00f3nusz</strong>odat, \u00e9s val\u00f3di el\u0151nyre v\u00e1ltsd az egyenlegedet.<br><br>A <strong>Celsius Casino</strong>ban m\u00e1r zajlik a j\u00e1t\u00e9k {d} ig\u00e9nyeld meg a <strong>170%-os b\u00f3nusz</strong>odat, v\u00e1laszd ki a kedvenc asztalodat, \u00e9s magabiztosan l\u00e9pj!'
                trial = line.replace(old, new)
                if trial != line:
                    lines[i] = trial; break
            changes += 1

        elif s.startswith('text_4:') and 'Celsius Casino Team.' in s:
            lines[i] = line.replace('Celsius Casino Team.', 'Celsius Casino csapat.')
            lines[i] = lines[i].replace('This is an automated message, please do not reply.',
                                        'Ez egy automatikus \u00fczenet, k\u00e9rj\u00fck, ne v\u00e1laszoljon.')
            changes += 1

        elif s.startswith('button_text_1:') and 'BOOST YOUR BALANCE NOW' in s:
            lines[i] = line.replace('BOOST YOUR BALANCE NOW', 'N\u00d6VELD AZ EGYENLEGEDET MOST')
            changes += 1

    # ===== PL =====
    elif current_locale == 'pl-PL':
        if s.startswith('subject:') and 'Power Up Your Play' in s:
            lines[i] = line.replace('170% Bonus: Power Up Your Play Today',
                                    'Bonus 170%: Zwi\u0119ksz swoje szanse na wygran\u0105 ju\u017c dzi\u015b')
            changes += 1

        elif s.startswith('preheader:') and 'help you win at the tables' in s:
            for q in [SQ, "'"]:
                trial = line.replace(f'Look what{q}s inside to help you win at the tables',
                                     'Zobacz, co znajdziesz w \u015brodku, co pomo\u017ce Ci wygra\u0107 przy sto\u0142ach')
                if trial != line:
                    lines[i] = trial; break
            changes += 1

        elif s.startswith('text_1:') and 'the floor is yours' in s:
            lines[i] = line.replace('default:"Player"', 'default:"Gracz"')
            lines[i] = lines[i].replace(', the floor is yours!', ', parkiet nale\u017cy do Ciebie!')
            changes += 1

        elif s.startswith('text_2:') and 'Why play on just your deposit' in s:
            for q in [SQ, "'"]:
                old = f'Why play on just your deposit when you can play with <strong>170%</strong> more? We{q}re supercharging your next top-up so you can stay in longer and chase bigger moments.'
                new = 'Po co gra\u0107 tylko za swoje \u015brodki, skoro mo\u017cesz gra\u0107 z <strong>170%</strong> wi\u0119cej? Podkr\u0119camy Twoje nast\u0119pne do\u0142adowanie, aby\u015b m\u00f3g\u0142 gra\u0107 d\u0142u\u017cej i d\u0105\u017cy\u0107 do wi\u0119kszych wygranych.'
                trial = line.replace(old, new)
                if trial != line:
                    lines[i] = trial; break
            changes += 1

        elif s.startswith('text_3:') and 'SURGE170' in s and 'Enter <strong' in s:
            for d in [EM, '\u2014']:
                old = f'Enter <strong class="promocode">SURGE170</strong> before making your next deposit to unlock your <strong>170% Bonus</strong> and turn your balance into a real advantage.<br><br>The action is live at <strong>Celsius Casino</strong> {d} claim your <strong>170% Bonus</strong>, pick your favorite table, and make your move with confidence.'
                new = f'Wpisz kod <strong class="promocode">SURGE170</strong> przed dokonaniem kolejnej wp\u0142aty, aby odblokowa\u0107 <strong>bonus 170%</strong> i zamieni\u0107 swoje saldo w prawdziw\u0105 przewag\u0119.<br><br>Akcja trwa w <strong>Celsius Casino</strong> {d} odbierz sw\u00f3j <strong>bonus 170%</strong>, wybierz sw\u00f3j ulubiony st\u00f3\u0142 i graj z pewno\u015bci\u0105 siebie.'
                trial = line.replace(old, new)
                if trial != line:
                    lines[i] = trial; break
            changes += 1

        elif s.startswith('text_4:') and 'Celsius Casino Team.' in s:
            lines[i] = line.replace('Celsius Casino Team.', 'Zesp\u00f3\u0142 Celsius Casino.')
            lines[i] = lines[i].replace('This is an automated message, please do not reply.',
                                        'To jest wiadomo\u015b\u0107 automatyczna, prosimy nie odpowiada\u0107.')
            changes += 1

        elif s.startswith('button_text_1:') and 'BOOST YOUR BALANCE NOW' in s:
            lines[i] = line.replace('BOOST YOUR BALANCE NOW', 'ZWI\u0118KSZ SWOJE SALDO TERAZ')
            changes += 1

with open(filepath, 'w', encoding='utf-8') as f:
    f.writelines(lines)

print(f"Done! {changes} changes applied for Email 1C (hu-HU + pl-PL)")
if changes != 14:
    print(f"WARNING: Expected 14 changes (7 per locale), got {changes}")
    print("Some fields may not have matched — check encoding.")
