import re

filepath = r'c:\Projects\REPORTS\тексти\Celsius\FTD Retention Flow - Table data.txt'

# === TRANSLATIONS ===
# greeting replacements (inside <strong> tag of text_1)
GREETING_EN = ' Hello, {{customer.first_name | default:"friend"}}\U0001f44b '
GREETING_HU = ' Szia, {{customer.first_name | default:"Bar\u00e1tom"}}\U0001f44b '
GREETING_PL = ' Cze\u015b\u0107, {{customer.first_name | default:"Przyjacielu"}}\U0001f44b '

T = {}  # translations dict

T['Email 1C'] = {
    'hu-HU': {
        'subject': '\U0001f40d A homok mozog - oldd fel a 100% + 50 Ingyenes P\u00f6rget\u00e9st',
        'preheader': 'K\u00f6vetkez\u0151 befizet\u00e9si b\u00f3nuszod a Hand of Anubis j\u00e1t\u00e9khoz k\u00e9sz',
        'body': r'''Bel\u00e9pt\u00e9l a j\u00e1t\u00e9kba - most itt az id\u0151 m\u00e9lyebbre menni.<br><br>Haszn\u00e1ld az <strong class="promocode">ANUBIS10050</strong> k\u00f3dot a k\u00f6vetkez\u0151 befizet\u00e9sedn\u00e9l, hogy feloldd a <strong>100% B\u00f3nuszt + 50 Ingyenes P\u00f6rget\u00e9st</strong> a <strong>Hand of Anubis</strong> <strong>by Hacksaw Gaming</strong> j\u00e1t\u00e9kban.<br><br>\u0150si er\u0151, modern izgalom - k\u00e9szen \u00e1llsz a p\u00f6rget\u00e9sre?''',
        'button_text_1': 'B\u00d3NUSZOM IG\u00c9NYL\u00c9SE',
    },
    'pl-PL': {
        'subject': '\U0001f40d Piaski si\u0119 przesuwaj\u0105 - odblokuj 100% + 50 Darmowych Spin\u00f3w',
        'preheader': 'Bonus od nast\u0119pnej wp\u0142aty na Hand of Anubis czeka',
        'body': r'''Wszed\u0142e\u015b do gry - czas zag\u0142\u0119bi\u0107 si\u0119 bardziej.<br><br>U\u017cyj kodu <strong class="promocode">ANUBIS10050</strong> przy nast\u0119pnej wp\u0142acie, \u017ceby odblokowa\u0107 <strong>100% Bonus + 50 Darmowych Spin\u00f3w</strong> w grze <strong>Hand of Anubis</strong> <strong>by Hacksaw Gaming</strong>.<br><br>Staro\u017cytna moc spotyka nowoczesny dreszcz - gotowy na obroty?''',
        'button_text_1': 'ODBIERZ M\u00d3J BONUS',
    }
}
