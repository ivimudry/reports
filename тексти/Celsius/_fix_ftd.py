path = r'c:\Projects\REPORTS\тексти\Celsius\FTD Retention Flow - Table data.txt'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

changes = 0

def safe_replace(content, old, new, label):
    global changes
    ct = content.count(old)
    if ct == 1:
        content = content.replace(old, new)
        changes += 1
        print(f'  OK: {label}')
    else:
        print(f'  SKIP ({ct} matches): {label}')
    return content

# ========== Email 1M fr-FR (line 177) ==========
content = safe_replace(content,
    "gardons l'\u00e9lan. Voici ce qui vous attend pour votre prochain coup : Un <strong>Bonus de 100%</strong><br>+ <strong>50 Tours Gratuits</strong><br><br>sur <strong>Hand of Anubis par Hacksaw Gaming</strong><br>pour les amateurs de casino - utilisez le code <strong class=\"promocode\">ANUBIS10050</strong><br><br>Un <strong>20% Pari Sans Risque</strong> pour votre prochain pari sportif - utilisez le code <strong class=\"promocode\">WINBACKNRF20</strong> Doublez la mise au casino ou jouez malin au sportsbook - dans les deux cas, votre prochain coup commence ici.",
    "gardons l'\u00e9lan.<br>Voici ce qui vous attend pour votre prochain coup :<br><br>Un <strong>Bonus de 100%</strong> + <strong>50 Tours Gratuits</strong> sur <strong>Hand of Anubis par Hacksaw Gaming</strong> pour les amateurs de casino - utilisez le code <strong class=\"promocode\">ANUBIS10050</strong><br><strong></strong>Un <strong>20% Pari Sans Risque</strong> pour votre prochain pari sportif - utilisez le code <strong class=\"promocode\">WINBACKNRF20</strong><br><br><strong></strong>Doublez la mise au casino ou jouez malin au sportsbook - dans les deux cas, votre prochain coup commence ici.",
    'Email 1M fr-FR full restructure')

# ========== Email 4M fr-FR (line 585) ==========
content = safe_replace(content,
    "allons plus loin.<br><br><br>Choisissez comment booster votre prochain coup : Code <strong class=\"promocode\">DOG10060</strong> - <strong>Bonus de 100%</strong> + <strong>60 Tours Gratuits</strong> sur <strong>The Dog House Megaways par Pragmatic Play</strong><br>si vous tournez les rouleaux Code <strong class=\"promocode\">WINBACKNRF20</strong> - <strong>20% Pari Sans Risque</strong><br><br>si vous soutenez votre favori sur le terrain Quelle que soit votre voie, votre prochain gain commence ici.",
    "allons plus loin.<br>Choisissez comment booster votre prochain coup :<br><br>Code <strong class=\"promocode\">DOG10060</strong> - <strong>Bonus de 100%</strong> + <strong>60 Tours Gratuits</strong> sur <strong>The Dog House Megaways par Pragmatic Play</strong> si vous tournez les rouleaux<br>Code <strong class=\"promocode\">WINBACKNRF20</strong> - <strong>20% Pari Sans Risque</strong> si vous soutenez votre favori sur le terrain<br><br>Quelle que soit votre voie, votre prochain gain commence ici.",
    'Email 4M fr-FR full restructure')

# ========== Email 5M fr-FR (line 1809) ==========
content = safe_replace(content,
    "booster votre prochain coup.<br><br><br>Voici ce qui vous attend : \U0001f3b0 Avec le code <strong class=\"promocode\">CHAOS10070</strong> - <strong>Bonus de 100%</strong> + <strong>70 Tours Gratuits</strong> sur <strong>Chaos Crew II par Hacksaw Gaming</strong><br>pour les amateurs de casino \u26bd Avec le code <strong class=\"promocode\">WINBACKNRF20</strong> - <strong>20% Pari Sans Risque</strong><br><br>si vous \u00eates fan de cotes Quelle que soit votre fa\u00e7on de jouer, une r\u00e9compense est taill\u00e9e pour votre jeu.",
    "booster votre prochain coup.<br>Voici ce qui vous attend :<br><br>\U0001f3b0 Avec le code <strong class=\"promocode\">CHAOS10070</strong> - <strong>Bonus de 100%</strong> + <strong>70 Tours Gratuits</strong> sur <strong>Chaos Crew II par Hacksaw Gaming</strong> pour les amateurs de casino<br>\u26bd Avec le code <strong class=\"promocode\">WINBACKNRF20</strong> - <strong>20% Pari Sans Risque</strong> si vous \u00eates fan de cotes<br><br>Quelle que soit votre fa\u00e7on de jouer, une r\u00e9compense est taill\u00e9e pour votre jeu.",
    'Email 5M fr-FR full restructure')

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f'\nTotal changes: {changes}')
