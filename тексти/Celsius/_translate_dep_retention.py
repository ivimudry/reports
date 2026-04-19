#!/usr/bin/env python3
"""Translate DEP Retention fr-FR blocks from English to French."""
import re, os

FILE = os.path.join(os.path.dirname(__file__), "DEP Retention - Table data.txt")

TR = {
    "Email 10C": {
        "subject": "⚡ 200 Tours Gratuits : Prêt à tourner ?",
        "preheader": "Accédez directement à votre récompense premium sur les machines",
        "greeting": "{{ customer.first_name | default:\"Ami\" | capitalize }}, votre boost est là.",
        "body": "Vous êtes là pour l'adrénaline - alors on a fait vite. Vos <strong>200 Tours Gratuits</strong> sur <strong>Gems Bonanza par Pragmatic Play</strong> sont prêts avec votre prochain dépôt. Entrez simplement le code promo <strong class=\"promocode\">GEMHUNT200</strong> avant de déposer pour les débloquer et foncez.",
        "body3": "Pas de recherche, pas de tracas - juste de l'action chez <strong>Celsius Casino</strong>. Rechargez, laissez les gemmes tomber et visez le gros lot.",
        "button": "LANCER MES TOURS"
    },
    "Email 10S": {
        "subject": "💥 30% Pari Sans Risque : Saisissez-le et dominez",
        "preheader": "Une façon plus intelligente de parier sur vos sports préférés",
        "greeting": "{{ customer.first_name | default:\"Champion\" | capitalize }}, prêt pour le coup d'envoi ?",
        "body": "Faites de votre prochain pari le bon - avec une protection intégrée. Votre <strong>30% Pari Sans Risque</strong> est actif maintenant, vous donnant plus de liberté pour suivre votre instinct.",
        "body3": "Pour le verrouiller, entrez le code promo <strong class=\"promocode\">ONLYSAFE30</strong> avant d'effectuer votre dépôt pour activer votre <strong>30% Pari Sans Risque</strong>. Rendez-vous sur <strong>Celsius Sport</strong>, consultez les meilleurs matchs, choisissez vos gagnants et pariez avec une mise protégée. Rapide, simple et prêt quand vous l'êtes.",
        "button": "ACTIVER ET JOUER"
    },
    "Email 1C": {
        "subject": "💥 Bonus de 170% : Boostez votre jeu aujourd'hui",
        "preheader": "Découvrez ce qui vous attend pour gagner aux tables",
        "greeting": "{{ customer.first_name | default:\"Joueur\" | capitalize }}, la piste est à vous !",
        "body": "Pourquoi jouer uniquement avec votre dépôt quand vous pouvez jouer avec <strong>170%</strong> en plus ? Nous rechargeons votre prochain top-up pour que vous puissiez rester plus longtemps et viser plus grand.",
        "body3": "Entrez <strong class=\"promocode\">SURGE170</strong> avant d'effectuer votre prochain dépôt pour débloquer votre <strong>Bonus de 170%</strong> et transformer votre solde en un véritable avantage. L'action est en direct chez <strong>Celsius Casino</strong> - réclamez votre <strong>Bonus de 170%</strong>, choisissez votre table préférée et faites votre coup en toute confiance.",
        "button": "BOOSTEZ VOTRE SOLDE"
    },
    "Email 1S": {
        "subject": "🥊 20% Pari Sans Risque : Frappez fort",
        "preheader": "Les cotes sont ouvertes - votre avantage sans risque vous attend",
        "greeting": "{{ customer.first_name | default:\"Champion\" | capitalize }}, la victoire est à portée de main !",
        "body": "Rien ne vaut l'adrénaline d'un pari gagnant - c'est pourquoi nous soutenons votre prochain coup avec un <strong>20% Pari Sans Risque</strong>, conçu pour jouer en toute confiance.",
        "body3": "Pour l'activer, entrez le code promo <strong class=\"promocode\">WINSAFE20</strong> avant d'effectuer votre prochain dépôt. Votre <strong>20% Pari Sans Risque</strong> sera prêt à utiliser immédiatement. Explorez les meilleurs matchs sur <strong>Celsius Sport</strong>, verrouillez votre marché favori et tentez votre chance tant que les cotes sont en direct.",
        "button": "SÉCURISER MON BOOST"
    },
    "Email 2C": {
        "subject": "⚡ 150% + 70 Tours Gratuits : Ne tardez pas !",
        "preheader": "Votre prochain gros gain est prêt - et vous ?",
        "greeting": "{{ customer.first_name | default:\"Joueur\" | capitalize }}, les jeux vous attendent !",
        "body": "Pourquoi rester en retrait quand vous pourriez enchaîner les gains ? Déposez maintenant et passez au niveau supérieur avec un <strong>bonus de 150% + 70 Tours Gratuits</strong> sur <strong>Chaos Crew II par Hacksaw Gaming</strong>.",
        "body3": "Pour le débloquer, ajoutez le code promo <strong class=\"promocode\">CREWBOOST150</strong> en premier, puis complétez votre dépôt - votre <strong>bonus de 150% et 70 Tours Gratuits</strong> sont prêts dès le premier tour. L'action chez <strong>Celsius Casino</strong> ne s'arrête jamais. Plongez dans <strong>Chaos Crew II par Hacksaw Gaming</strong> et visez votre prochain gros coup.",
        "button": "RÉCLAMEZ VOTRE DOUBLE RÉCOMPENSE"
    },
    "Email 2S": {
        "subject": "⚽ 20% Pari Sans Risque : C'est l'heure du match",
        "preheader": "Le match du jour vous appelle - entrez avec une protection",
        "greeting": "{{ customer.first_name | default:\"Supporter\" | capitalize }}, les projecteurs sont allumés !",
        "body": "Le Prime Time approche - le plus grand match de la journée, haute tension, et un instant peut tout changer. Entrez avant le coup d'envoi.",
        "body3": "Pour booster l'action du jour, réclamez votre <strong>20% Pari Sans Risque</strong> : ajoutez le code promo <strong class=\"promocode\">WINSAFE20</strong> en premier, puis complétez votre dépôt pour activer la protection de votre <strong>20% Pari Sans Risque</strong>. Rechargez votre bankroll, consultez les compositions et faites votre mise sur <strong>Celsius Sport</strong> avec un filet de sécurité.",
        "button": "OBTENIR MON PARI SANS RISQUE"
    },
    "Email 3C": {
        "subject": "🎡 Évadez-vous vers les gains : Les meilleurs résultats de la semaine",
        "preheader": "Laissez le monde derrière vous et entrez dans le cercle des gagnants",
        "greeting": "{{ customer.first_name | default:\"Joueur\" | capitalize }}, prêt à changer d'ambiance ?",
        "body": "Parfois, vous n'avez pas besoin de plus de bruit - vous avez besoin d'une meilleure montée d'adrénaline. Chez <strong>Celsius Casino</strong>, les meilleurs joueurs ont encaissé gros la semaine dernière : 🏆 Lu••••7 - €52 300 🏆 S•••••n - €35 900 🏆 Bi•••••t - €19 400 Les tables vous appellent et les machines sont prêtes. Coupez le stress et allumez l'adrénaline chez <strong>Celsius Casino</strong> - votre place vous attend.",
        "button": "COMMENCEZ VOTRE ÉVASION"
    },
    "Email 3S": {
        "subject": "🏆 Gagnants de la semaine : Ils ont fait le bon choix",
        "preheader": "Découvrez qui a dominé les cotes cette semaine sur Celsius Sport",
        "greeting": "{{ customer.first_name | default:\"Champion\" | capitalize }}, serez-vous le prochain ?",
        "body": "Les 7 derniers jours sur <strong>Celsius Sport</strong> ont été grands. Nos parieurs les plus affûtés ont fait le bon choix et sont repartis avec d'énormes gains : 💰 Str•••••X - €42 810 💰 Go•••••er - €31 200 💰 Pa•••••ng - €19 450 Ils n'ont pas juste regardé - ils ont joué le coup. Les cotes sont en direct pour les prochains matchs, alors choisissez votre place et pariez. Votre nom pourrait être le prochain sur cette liste.",
        "button": "VOIR LES COTES DU JOUR"
    },
    "Email 4C": {
        "subject": "💥 160% + 80 Tours Gratuits : Saisissez-les et ressentez l'adrénaline",
        "preheader": "Le timing parfait pour votre prochain gros gain",
        "greeting": "{{ customer.first_name | default:\"Joueur\" | capitalize }}, on monte la température !",
        "body": "Vous avez l'instinct - frappez pendant que le timing est parfait. Réclamez un <strong>bonus de 160% + 80 Tours Gratuits</strong> sur <strong>Wild West Gold par Pragmatic Play</strong> pour booster votre prochaine session.",
        "body3": "Entrez le code promo <strong class=\"promocode\">GUNSLINGER160</strong> avant de déposer pour débloquer votre <strong>bonus de 160% et 80 Tours Gratuits</strong>. Puis foncez dans <strong>Wild West Gold par Pragmatic Play</strong>. Les rouleaux sont chargés chez <strong>Celsius Casino</strong> - prêt à lancer une série gagnante ?",
        "button": "BOOSTEZ VOTRE TEMPO"
    },
    "Email 4S": {
        "subject": "⚽ Boost de 170% : Votre jeu, votre scénario",
        "preheader": "Prenez le contrôle du match et écrivez votre propre histoire",
        "greeting": "{{ customer.first_name | default:\"Coach\" | capitalize }}, c'est vous qui décidez !",
        "body": "Chaque match a son scénario - et aujourd'hui, c'est vous qui l'écrivez. Pour soutenir votre lecture du premier coup de sifflet au coup final, nous chargeons votre prochaine session avec un <strong>bonus de 170% sur votre dépôt</strong>.",
        "body3": "Entrez le code promo <strong class=\"promocode\">SURGE170</strong> avant votre dépôt pour débloquer votre <strong>bonus de 170%</strong>. Puis rendez-vous sur <strong>Celsius Sport</strong>, scannez les marchés et construisez votre ticket à votre façon. Le tableau est en direct - et votre avantage est prêt. Écrivez le résultat.",
        "button": "RÉCLAMER MON BOOST"
    },
    "Email 5C": {
        "subject": "🎰 Bonus de 170% : Boost instantané activé",
        "preheader": "Votre chemin vers un gros gain vient de s'accélérer",
        "greeting": "{{ customer.first_name | default:\"Joueur\" | capitalize }}, préparez-vous !",
        "body": "Quand les jeux chauffent, la vitesse fait la différence. Nous chargeons instantanément un <strong>bonus de 170%</strong> sur votre prochain dépôt - conçu pour pousser votre session plus loin, plus vite. N'oubliez pas d'entrer <strong class=\"promocode\">BOOSTER170</strong> avant votre dépôt pour le réclamer.",
        "body3": "Alimentez votre compte et regardez votre solde décoller chez <strong>Celsius Casino</strong>. Avec <strong>170%</strong> en plus, vous pouvez jouer plus longtemps, pousser plus fort et viser les gros multiplicateurs.",
        "button": "COMMENCER À GAGNER"
    },
    "Email 5S": {
        "subject": "🚀 20% Pari Sans Risque : Activez et gagnez",
        "preheader": "Accédez directement au cœur de l'action sans attendre",
        "greeting": "{{ customer.first_name | default:\"Joueur\" | capitalize }}, pas de temps à perdre !",
        "body": "Les plus grands moments sont en direct - et il y a un moyen plus rapide de vous lancer avec un avantage sur <strong>Celsius Sport</strong>. Pas de délai, juste de l'action avec une protection derrière votre mise.",
        "body3": "Votre raccourci : consultez les cotes, appliquez le code promo <strong class=\"promocode\">WINSAFE20</strong> avant votre dépôt, puis activez votre <strong>20% Pari Sans Risque</strong>. C'est une protection de <strong>20% Pari Sans Risque</strong> sur votre mise - conçue pour vous garder confiant du premier choix au coup de sifflet final. Trois étapes. Un avantage. Lancez votre série.",
        "button": "ACTIVER MON PARI SANS RISQUE"
    },
    "Email 6C": {
        "subject": "🌟 Rejoignez l'élite : Le palmarès de la semaine",
        "preheader": "Découvrez qui a dominé les rouleaux et réclamez votre place au sommet",
        "greeting": "{{ customer.first_name | default:\"Joueur\" | capitalize }}, c'est votre moment !",
        "body": "L'élan est incroyable - et les plus gros gains arrivent maintenant chez <strong>Celsius Casino</strong>. Voici les derniers champions : 🏆 Ja••••g - €61 200 🏆 Sp••••r - €42 800 🏆 Eli••••er - €24 100 Les machines sont chaudes et les cartes sont distribuées - le prochain titre pourrait être le vôtre. Entrez, vivez l'adrénaline et jouez chez <strong>Celsius Casino</strong>.",
        "button": "COMMENCEZ VOTRE PARCOURS"
    },
    "Email 6S": {
        "subject": "⚡ Boost de 170% : Libérez la puissance",
        "preheader": "Alimentez votre série gagnante avec une puissance de feu supplémentaire",
        "greeting": "{{ customer.first_name | default:\"Champion\" | capitalize }}, entrez sous les projecteurs !",
        "body": "Prêt à monter l'intensité ? Les plus grands matchs de la semaine s'accompagnent d'un <strong>bonus de 170% sur votre dépôt</strong> pour alimenter chacun de vos choix.",
        "body3": "Pour activer votre <strong>bonus de 170%</strong>, entrez le code promo <strong class=\"promocode\">BOOSTER170</strong> avant de recharger - votre boost est chargé instantanément. Que vous construisiez des combinés ou verrouilliez des paris simples affûtés, la puissance supplémentaire vous donne plus de marge pour jouer votre stratégie sur <strong>Celsius Sport</strong>. Prenez le contrôle et laissez votre avantage monter avec <strong>170%</strong>.",
        "button": "RÉCLAMER MON BOOST"
    },
    "Email 7C": {
        "subject": "🔥 Les plus gros gains venaient de prochains dépôts",
        "preheader": "Serez-vous le prochain grand gagnant ?",
        "greeting": "{{ customer.first_name | default:\"Joueur\" | capitalize }}, pourquoi attendre ?",
        "body": "Certaines de nos plus grandes histoires de jackpot ont commencé avec un prochain dépôt. Il n'y a pas de secret - juste une nouvelle chance de jouer à vos jeux préférés et de décrocher ce tour en or. Prêt à écrire votre propre histoire gagnante ?",
        "button": "JE REVIENS"
    },
    "Email 7S": {
        "subject": "⚡ 20% Pari Sans Risque : Votre avantage",
        "preheader": "Suivez la formule gagnante, du promo au match",
        "greeting": "{{ customer.first_name | default:\"Joueur\" | capitalize }}, prenez l'avantage !",
        "body": "Pourquoi laisser faire le hasard quand vous pouvez jouer avec un avantage ? Activez votre promo, placez votre pari et profitez du match avec une protection derrière votre mise.",
        "body3": "Commencez par entrer le code promo <strong class=\"promocode\">WINSAFE20</strong>, puis effectuez votre dépôt et débloquez votre <strong>20% Pari Sans Risque</strong>. Puis rendez-vous sur <strong>Celsius Sport</strong> et choisissez votre match - le derby, le duel tactique ou l'affiche incontournable. Avec la protection <strong>20% Pari Sans Risque</strong>, vous pouvez faire confiance à votre instinct et garder le contrôle du coup d'envoi au coup de sifflet final.",
        "button": "OBTENIR MON AVANTAGE"
    },
    "Email 8C": {
        "subject": "🚀 180% + 80 Tours Gratuits : Améliorez votre entrée",
        "preheader": "Découvrez comment booster votre prochain dépôt en quelques clics",
        "greeting": "{{ customer.first_name | default:\"Ami\" | capitalize }}, il est temps de passer au niveau supérieur !",
        "body": "Ne vous contentez pas de rejoindre le jeu - prenez le contrôle. Votre prochain dépôt bénéficie d'une sérieuse mise à niveau : un <strong>power-up de 180% + 80 Tours Gratuits</strong> sur <strong>Wanted Dead or a Wild par Hacksaw Gaming</strong>, conçu pour lancer votre session rapidement.",
        "body3": "Commencez par entrer le code promo <strong class=\"promocode\">OUTLAW180</strong>, puis effectuez votre dépôt et plongez dans <strong>Wanted Dead or a Wild par Hacksaw Gaming</strong> chez <strong>Celsius Casino</strong>. Votre <strong>boost de 180% et 80 Tours Gratuits</strong> sont prêts dès le premier tour.",
        "button": "OBTENIR MON POWER-UP"
    },
    "Email 8S": {
        "subject": "🏆 Ils ont gagné gros au sport - À votre tour",
        "preheader": "Découvrez les meilleurs gains de la semaine et choisissez votre match gagnant",
        "greeting": "{{ customer.first_name | default:\"Champion\" | capitalize }}, le classement vous attend !",
        "body": "La semaine dernière, ces joueurs ont fait confiance aux chiffres, ont trouvé le bon moment et ont encaissé gros : 💰 G••••er88 - €45 600 💰 O•••••ero - €32 150 💰 Be••••rd - €18 700 Le tableau est rafraîchi et les prochains matchs sont en direct sur <strong>Celsius Sport</strong>. Les cotes sont affichées, les marchés bougent et c'est votre fenêtre. Choisissez votre match, suivez votre instinct et faites votre coup - votre nom devrait être le prochain sur la liste des gagnants.",
        "button": "CHOISIR UN MATCH ET PARIER"
    },
    "Email 9C": {
        "subject": "💎 140% + 100 Tours Gratuits : Pourquoi attendre ?",
        "preheader": "Prenez l'avantage et sécurisez vos chances supplémentaires de gagner gros",
        "greeting": "{{ customer.first_name | default:\"Ami\" | capitalize }}, faites de cette journée une légende.",
        "body": "Le \"moment parfait\" n'arrive pas - c'est vous qui le créez. Aujourd'hui, visez plus grand dès le premier tour avec un <strong>bonus de 140% + 100 Tours Gratuits</strong> sur <strong>Big Bamboo par Push Gaming</strong>. Ajoutez simplement le code <strong class=\"promocode\">GIANTPANDA100</strong> en premier, puis complétez votre dépôt pour le débloquer.",
        "body3": "Entrez chez <strong>Celsius Casino</strong> avec un solde boosté et <strong>100 Tours Gratuits</strong> prêts à se déclencher. Jouez plus longtemps, poussez plus loin et visez le jackpot avec un vrai élan.",
        "button": "OBTENIR MON BOOST"
    },
    "Email 9S": {
        "subject": "🎾 30% Pari Sans Risque : Un spectacle intelligent",
        "preheader": "Combinez votre passion sportive avec un avantage sans risque",
        "greeting": "{{ customer.first_name | default:\"Joueur\" | capitalize }}, c'est l'heure de jouer.",
        "body": "La meilleure façon de regarder votre sport préféré ? Avec un enjeu dans la partie - et une protection sur votre mise. Aujourd'hui, bénéficiez d'une couverture <strong>30% Pari Sans Risque</strong> avec <strong class=\"promocode\">ONLYSAFE30</strong>.",
        "body3": "Activez le promo, choisissez votre marché et jouez en toute confiance : ajoutez le code <strong class=\"promocode\">ONLYSAFE30</strong> en premier, puis complétez votre dépôt et débloquez votre protection <strong>30% Pari Sans Risque</strong> pour l'action du jour. Sur <strong>Celsius Sport</strong>, nous apportons les cotes - vous apportez la stratégie. Placez votre pari et faites de ce match un moment unique.",
        "button": "RÉCLAMER MON PARI SANS RISQUE"
    },
}

def apply_translations(filepath, translations):
    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()

    current_name = None
    in_fr = False
    changed = 0
    new_lines = []

    for line in lines:
        stripped = line.rstrip("\n")

        if stripped.startswith("name: "):
            current_name = stripped[6:].strip()
            in_fr = False

        if stripped.startswith("locale: "):
            locale = stripped[8:].strip()
            in_fr = (locale == "fr-FR")

        if in_fr and current_name in translations:
            tr = translations[current_name]

            if stripped.startswith("subject: "):
                new_lines.append(f"subject: {tr['subject']}\n")
                changed += 1
                continue

            if stripped.startswith("preheader: "):
                new_lines.append(f"preheader: {tr['preheader']}\n")
                changed += 1
                continue

            if stripped.startswith("button_text_1: "):
                new_lines.append(f"button_text_1: {tr['button']}\n")
                changed += 1
                continue

            # Greeting (text_1) - replace inner <strong> content
            if stripped.startswith("text_1: "):
                new_line = re.sub(
                    r'(<strong>)(.+?)(</strong>)',
                    lambda m: m.group(1) + tr['greeting'] + m.group(3),
                    stripped
                )
                new_lines.append(new_line + "\n")
                changed += 1
                continue

            # Body (text_2) - replace inner <p> content
            if stripped.startswith("text_2: "):
                new_line = re.sub(
                    r'(<p\s[^>]*>)(.+)(</p></td>)',
                    lambda m: m.group(1) + tr['body'] + m.group(3),
                    stripped
                )
                new_lines.append(new_line + "\n")
                changed += 1
                continue

            # Body3 (text_3) - only translate if body3 exists in translations
            if stripped.startswith("text_3: ") and "body3" in tr:
                new_line = re.sub(
                    r'(<p\s[^>]*>)(.+)(</p></td>)',
                    lambda m: m.group(1) + tr['body3'] + m.group(3),
                    stripped
                )
                new_lines.append(new_line + "\n")
                changed += 1
                continue

        new_lines.append(line)

    with open(filepath, "w", encoding="utf-8") as f:
        f.writelines(new_lines)

    return changed


if __name__ == "__main__":
    body3_count = sum(1 for v in TR.values() if "body3" in v)
    expected = len(TR) * 5 + body3_count  # 5 base fields + body3 where present
    n = apply_translations(FILE, TR)
    print(f"DEP Retention: {n} fields translated (expected {expected} = {len(TR)} emails x 5 + {body3_count} body3)")
