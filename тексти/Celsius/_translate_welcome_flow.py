#!/usr/bin/env python3
"""Translate Welcome Flow fr-FR blocks from English to French."""
import re, os

FILE = os.path.join(os.path.dirname(__file__), "Welcome Flow - Table data.txt")

# {email_name: {subject, preheader, greeting, body, button}}
TR = {
    "Email 1C": {
        "subject": "🚀 Votre aventure Celsius commence ici !",
        "preheader": "Débloquez des bonus massifs sur vos 4 premiers dépôts - jusqu'à €2000 + 250 Tours Gratuits !",
        "greeting": " Bonjour, {{customer.first_name | default:\"ami\"}}👋 ",
        "body": "L'aventure Celsius ne fait que commencer - et nous avons préparé des récompenses pour bien démarrer.&nbsp; Vos 4 premiers dépôts s'accompagnent de <strong>bonus généreux</strong> et de <strong>nombreux Tours Gratuits</strong> :&nbsp; <strong>1er : 100% jusqu'à €500 + 150 TG</strong>&nbsp; <strong>2e : 100% jusqu'à €300 + 50 TG</strong>&nbsp; <strong>3e : 200% jusqu'à €200 + 50 TG</strong>&nbsp; <strong>4e : 150% jusqu'à €1000</strong>&nbsp; C'est jusqu'à <strong>€2000 + 250 Tours Gratuits</strong> qui n'attendent que vous. Commencez petit ou visez grand - à vous de choisir.<br>Réclamez vos bonus de bienvenue maintenant",
        "button": "COMMENCER MON AVENTURE"
    },
    "Email 1M": {
        "subject": "🎯 Jouez à votre façon avec le Bonus Cashback",
        "preheader": "Machines à sous, Casino Live ou Sport - récupérez davantage sur chaque mise avec notre Bonus Cashback.",
        "greeting": " Bonjour, {{customer.first_name | default:\"ami\"}}👋 ",
        "body": "Démarrez votre aventure chez Celsius avec le <strong>Bonus Cashback</strong> - simple, gratifiant et adapté à votre style de jeu.&nbsp; Que vous aimiez les machines à sous, le Casino Live ou les paris sportifs, vos mises vous rapportent désormais plus : recevez une partie en cashback et prolongez l'action.&nbsp; Plus de jeu. Plus de retour. Exactement comme vous aimez.",
        "button": "JOUEZ SANS LIMITES"
    },
    "Email 1S": {
        "subject": "⚽ Lancez votre parcours sportif chez Celsius",
        "preheader": "Des Paris Gratuits jusqu'à €700 vous attendent sur vos deux premiers dépôts.",
        "greeting": " Bonjour, {{customer.first_name | default:\"ami\"}}👋 ",
        "body": "Prêt à passer vos paris sportifs au niveau supérieur ?&nbsp; Démarrez votre aventure avec des <strong>bonus de Paris Gratuits exclusifs</strong> réservés aux nouveaux joueurs :&nbsp; <strong>1er Dépôt : 50% de Bonus Paris Gratuits de bienvenue jusqu'à €200</strong>&nbsp; <strong>2e Dépôt : 20% de Bonus Pari Sans Risque jusqu'à €500</strong>&nbsp; Que vous pariez sur le football, le tennis ou l'esport - Celsius vous couvre dès le premier match.&nbsp; Faites votre choix et récupérez vos Paris Gratuits maintenant !",
        "button": "RÉCLAMEZ MES PARIS GRATUITS"
    },
    "Email 2C": {
        "subject": "🎰 Votre premier bonus n'est qu'à un pas",
        "preheader": "Utilisez le code et obtenez 100% + 150 Tours Gratuits sur votre premier dépôt.",
        "greeting": " Bonjour, {{customer.first_name | default:\"ami\"}}👋 ",
        "body": "Vous n'êtes qu'à un pas de débloquer votre première grande récompense chez Celsius.&nbsp; Effectuez votre premier dépôt avec le code <strong class=\"promocode\">BANDIT150</strong> et profitez de :&nbsp; un <strong>Bonus de 100%</strong> et <strong>150 Tours Gratuits </strong>sur<strong> Le Bandit par Hacksaw Gaming</strong>.&nbsp; C'est la meilleure façon de lancer votre aventure Celsius avec un coup de pouce. Ne manquez pas cette chance - réclamez votre bonus de bienvenue aujourd'hui.",
        "button": "RÉCLAMER MON BONUS"
    },
    "Email 2M": {
        "subject": "🎯 Gros gains aux machines et 10% Pari Sans Risque sur votre prochain pari",
        "preheader": "Des joueurs ont décroché le jackpot la semaine dernière - à votre tour, avec un code 10% Pari Sans Risque.",
        "greeting": " Bonjour, {{customer.first_name | default:\"ami\"}}👋 ",
        "body": "Les rouleaux n'ont pas arrêté de tourner la semaine dernière - voici ceux qui sont repartis gagnants :&nbsp; <strong>l•••••e a gagné 29 343 $</strong>&nbsp; <strong>k••••o a décroché 18 920 $</strong>&nbsp; <strong>a••••1h a remporté 11 480 $</strong>&nbsp; Envie de participer ? Utilisez le code <strong class=\"promocode\">SAFE10</strong> et obtenez un <strong>Bonus de 10% Pari Sans Risque</strong> sur votre prochain pari. Un clic pourrait tout changer.",
        "button": "TENTER MA CHANCE"
    },
    "Email 2S": {
        "subject": "⚽ C'est l'heure du match - Votre pari appartient au terrain",
        "preheader": "L'action monte en puissance. Faites votre choix et soutenez votre favori aujourd'hui.",
        "greeting": " Bonjour, {{customer.first_name | default:\"ami\"}}👋 ",
        "body": "Le terrain est prêt, les cotes bougent et la tension monte - c'est le moment de placer votre pari.&nbsp; Choisissez votre match, faites confiance à votre instinct et laissez les chiffres parler.&nbsp; Pour rendre l'expérience encore meilleure, utilisez le code <strong class=\"promocode\">BOOST50</strong> et profitez d'un <strong>bonus de 50% sur votre prochain dépôt</strong> - plus de solde, plus de confiance, plus de victoires.",
        "button": "PLACER MON PARI"
    },
    "Email 3C": {
        "subject": "💥 100% + 150 TG - Le coup d'envoi de votre aventure",
        "preheader": "Utilisez le code pour débloquer votre premier bonus Celsius et entrez dans le jeu.",
        "greeting": " Bonjour, {{customer.first_name | default:\"ami\"}}👋 ",
        "body": "L'instant juste avant votre premier dépôt, c'est là que tout commence.&nbsp; Utilisez le code <strong class=\"promocode\">CREW150</strong> maintenant et obtenez un <strong>Bonus de 100%</strong> plus <strong>150 Tours Gratuits </strong>sur<strong> Chaos Crew II par Hacksaw Gaming</strong>.&nbsp; Voici votre point d'entrée - sans pression, juste votre jeu, vos conditions et un solide bonus de bienvenue.",
        "button": "DÉMARRER AVEC MON BONUS"
    },
    "Email 3M": {
        "subject": "🎰 De gros jackpots la semaine dernière",
        "preheader": "De gros jackpots la semaine dernière - votre nom sera-t-il le prochain sur la liste ?",
        "greeting": " Bonjour, {{customer.first_name | default:\"ami\"}}👋 ",
        "body": "Voici ce que les rouleaux ont livré la semaine dernière - de vrais gains, de vrais joueurs :&nbsp; <strong>a7g••••••n a décroché 42 380 $ &nbsp;</strong>&nbsp; <strong>m2f•••••d a marqué 26 104 $ &nbsp;</strong>&nbsp; <strong>j3s•••••••7 a remporté 33 987 $ &nbsp;</strong>&nbsp; Les machines étaient en feu - et si ce n'est pas votre truc, n'oubliez pas : vous pouvez aussi parier sur le sport en direct. Un tour ou un pari pourrait tout changer.",
        "button": "JOUEZ OU PARIEZ MAINTENANT"
    },
    "Email 3S": {
        "subject": "🏟️ L'énergie du jour de match est dans l'air - Vous êtes partant ?",
        "preheader": "C'est le moment idéal de verrouiller votre choix et de ressentir l'adrénaline.",
        "greeting": " Bonjour, {{customer.first_name | default:\"ami\"}}👋 ",
        "body": "Grands matchs. Cotes audacieuses. Tout est en place - sauf votre pari.&nbsp; Que vous misiez sur le favori ou sur l'outsider, c'est le moment de marquer le coup.&nbsp; Et pour vous donner cet avantage supplémentaire, nous ajoutons un <strong>bonus de 50% sur votre prochain dépôt</strong> - plus de valeur, plus de confiance, plus d'action.",
        "button": "PARIEZ MAINTENANT"
    },
    "Email 4C": {
        "subject": "🎯 120% + 170 Tours Gratuits vous attendent",
        "preheader": "Utilisez le code sur votre premier dépôt et démarrez fort avec Celsius.",
        "greeting": " Bonjour, {{customer.first_name | default:\"ami\"}}👋 ",
        "body": "Vous vous êtes inscrit, vous avez exploré la plateforme - il est temps de faire votre premier pas.&nbsp; Utilisez le code <strong class=\"promocode\">STORM170</strong> sur votre premier dépôt et recevez un <strong>Bonus de 120%</strong> et <strong>170 Tours Gratuits </strong>sur <strong>Stormforged par Hacksaw Gaming</strong>.&nbsp; Commencez votre aventure Celsius avec une offre taillée pour un départ gagnant.",
        "button": "RÉCLAMER MON BONUS"
    },
    "Email 4M": {
        "subject": "🎮 100 TG + Paris Sans Risque à l'intérieur",
        "preheader": "Utilisez le code sur votre premier dépôt et lancez-vous au casino et dans le sport.",
        "greeting": " Bonjour, {{customer.first_name | default:\"ami\"}}👋 ",
        "body": "Que vous soyez là pour les tours ou les scores - votre premier dépôt vous couvre.&nbsp; Entrez le code <strong class=\"promocode\">LEGACY100</strong> et obtenez <strong>100 Tours Gratuits</strong> sur <strong>Legacy of Dead par Play'n Go</strong>.&nbsp; Entrez le code <strong class=\"promocode\">BETSAFE20</strong> et obtenez un <strong>Bonus de 20% Pari Sans Risque</strong> pour le sport.&nbsp; Votre jeu, votre rythme - avec une longueur d'avance.",
        "button": "ACTIVER MON BONUS"
    },
    "Email 4S": {
        "subject": "🧤 50% de Paris Gratuits en plus",
        "preheader": "Entrez dans le jeu avec un vrai avantage - vos Paris Gratuits de bienvenue sont prêts.",
        "greeting": " Bonjour, {{customer.first_name | default:\"ami\"}}👋 ",
        "body": "Parier, c'est encore mieux quand on commence avec un coup de pouce.&nbsp; Sur votre premier dépôt, vous recevrez un <strong>Bonus de 50% de Paris Gratuits</strong> jusqu'à <strong>€200</strong> - parfait pour lancer votre série.&nbsp; Un geste. Un avantage. À vous de jouer.",
        "button": "COMMENCER À PARIER"
    },
    "Email 5C": {
        "subject": "🎁 Un code. Un dépôt. Un vrai démarrage.",
        "preheader": "Utilisez le code et transformez votre premier dépôt en 100% + 150 Tours Gratuits.",
        "greeting": " Bonjour, {{customer.first_name | default:\"ami\"}}👋 ",
        "body": "Que se passe-t-il après votre premier dépôt ?&nbsp; Obtenez un <strong>Bonus de 100%</strong> et <strong>150 Tours Gratuits </strong>sur <strong>Rip City par Hacksaw Gaming</strong>, en utilisant le code <strong class=\"promocode\">RIP100CITY</strong>.&nbsp; Ce n'est pas juste un accueil - c'est un vrai lancement. Faites que ça compte.",
        "button": "DÉBLOQUER MON BONUS"
    },
    "Email 5M": {
        "subject": "🎯 Trois gros gains. Deux façons de jouer. Un seul vous.",
        "preheader": "Machines à sous ou Sport - voici ce qui s'est passé la semaine dernière et comment participer.",
        "greeting": " Bonjour, {{customer.first_name | default:\"ami\"}}👋 ",
        "body": "La semaine dernière, les rouleaux ont livré des gains sérieux :&nbsp; <strong>r8d•••••1 a gagné 38 210 $ &nbsp;</strong>&nbsp; <strong>t3s••••••k a décroché 24 765 $ &nbsp;</strong>&nbsp; <strong>b6v••••n a remporté 31 402 $&nbsp;</strong>&nbsp; Les machines sont clairement en feu - mais si vous préférez la tactique et le timing, les paris sportifs sont toujours à un clic. Dans les deux cas, il y a toujours quelque chose à gagner.",
        "button": "TOURNEZ OU PARIEZ MAINTENANT"
    },
    "Email 5S": {
        "subject": "🥶 50% de Paris Gratuits dès votre premier geste",
        "preheader": "Faites votre premier dépôt et nous ajoutons 50% de Paris Gratuits jusqu'à €200.",
        "greeting": " Bonjour, {{customer.first_name | default:\"ami\"}}👋 ",
        "body": "Grosses cotes, action rapide et votre pari qui n'attend que vous.&nbsp; Faites votre premier dépôt et récupérez un <strong>Bonus de 50% de Paris Gratuits de bienvenue</strong> jusqu'à <strong>€200</strong> - pas de réflexion excessive, juste un tir direct dans le jeu.",
        "button": "C'EST PARTI"
    },
    "Email 6C": {
        "subject": "🎯 Il est temps de débloquer 100% + 150 TG !",
        "preheader": "Votre premier dépôt se transforme en un accueil complet - si vous le souhaitez.",
        "greeting": " Bonjour, {{customer.first_name | default:\"ami\"}}👋 ",
        "body": "Il y a un bonus prévu pour votre premier pas - si vous décidez de le saisir.&nbsp; Utilisez le code <strong class=\"promocode\">BANDIT150</strong> pour obtenir un <strong>Bonus de 100%</strong> et <strong>150 Tours Gratuits</strong> sur <strong>Le Bandit par Hacksaw Gaming </strong>sur votre premier dépôt.&nbsp; Simple, direct et prêt quand vous l'êtes.",
        "button": "C'EST PARTI"
    },
    "Email 6M": {
        "subject": "🎲 47 890 $ de gains cette semaine, serez-vous le prochain ?",
        "preheader": "Les machines étaient en feu la semaine dernière - et les cotes sportives ne refroidissent pas non plus.",
        "greeting": " Bonjour, {{customer.first_name | default:\"ami\"}}👋 ",
        "body": "Grosse semaine. Gros gains. Voici ce qui s'est passé chez Celsius :&nbsp; <strong>a9n•••••z a gagné 47 890 $ &nbsp;</strong>&nbsp; <strong>m4e••••q a décroché 22 715 $ &nbsp;</strong>&nbsp; <strong>j2x•••••r a marqué 35 040 $</strong> &nbsp; Les rouleaux étaient en feu - et si vous préférez parier, le sportsbook est prêt avec de l'action en direct et des cotes fraîches. Peu importe comment vous jouez, le prochain gain pourrait porter votre nom.",
        "button": "TOURNEZ OU PARIEZ MAINTENANT"
    },
    "Email 6S": {
        "subject": "🏁 Votre pari ne sera actif que quand vous le serez",
        "preheader": "50% de Paris Gratuits jusqu'à €200 - commencez à votre rythme.",
        "greeting": " Bonjour, {{customer.first_name | default:\"ami\"}}👋 ",
        "body": "Vous avez vu les cotes. Maintenant, mettez-les en mouvement.&nbsp; Votre premier dépôt vous offre un <strong>Bonus de 50% de Paris Gratuits de bienvenue</strong> jusqu'à <strong>€200</strong> - pas de distractions, juste l'élan nécessaire pour bien démarrer.",
        "button": "ACTIVER MON BONUS"
    },
    "Email 7C": {
        "subject": "💸 Gros gains aux machines la semaine dernière - Serez-vous le prochain ?",
        "preheader": "Voyez ce que d'autres ont gagné chez Celsius et tentez votre chance pour le prochain gros lot.",
        "greeting": " Bonjour, {{customer.first_name | default:\"ami\"}}👋 ",
        "body": "La semaine dernière chez Celsius, les rouleaux étaient en feu - voici ce que certains joueurs chanceux ont remporté :&nbsp; <strong>a•••••••n a gagné 29 343 $</strong>&nbsp; <strong>j•••••e a décroché 17 920 $</strong>&nbsp; <strong>m••••x11 a marqué 11 608 $</strong>&nbsp; Pas d'astuces, pas de codes bonus - juste du jeu pur et des gains réels.&nbsp; Prêt à tenter votre chance ?",
        "button": "TENTEZ VOTRE CHANCE"
    },
    "Email 7M": {
        "subject": "🎯 À ne pas manquer : 100 Tours Gratuits + 20% Pari Sans Risque",
        "preheader": "100 Tours Gratuits + 20% Pari Sans Risque - entrez simplement le code sur votre premier dépôt.",
        "greeting": " Bonjour, {{customer.first_name | default:\"ami\"}}👋 ",
        "body": "Pourquoi choisir entre casino et sport quand vous pouvez avoir les deux dès le départ ?&nbsp; Utilisez le code <strong class=\"promocode\">LEGACY100</strong> sur votre premier dépôt pour recevoir<strong> 100 Tours Gratuits </strong>sur <strong>Legacy of Dead par Play'n Go</strong>, et utilisez le code <strong class=\"promocode\">BETSAFE20</strong> pour obtenir un <strong>Bonus de 20% Pari Sans Risque</strong>.&nbsp; Deux voies. Un seul geste. Votre jeu commence maintenant.",
        "button": "LANCER MON COMBO"
    },
    "Email 7S": {
        "subject": "🥊 60% de Paris Gratuits sur votre premier dépôt",
        "preheader": "Utilisez le code et boostez votre premier dépôt avec un Bonus de 60% de Paris Gratuits.",
        "greeting": " Bonjour, {{customer.first_name | default:\"ami\"}}👋 ",
        "body": "Un premier dépôt, ça doit faire de l'effet.&nbsp; Entrez le code <strong class=\"promocode\">FIREUP60</strong> et récupérez un <strong>Bonus de 60% de Paris Gratuits de bienvenue</strong> dès le départ.&nbsp; Placez votre pari, trouvez le rythme et jouez à votre façon.",
        "button": "UTILISER MON CODE"
    },
    "Email 8C": {
        "subject": "🧨 Démarrez fort : 100% + 150 Tours Gratuits sur votre premier dépôt",
        "preheader": "Obtenez votre bonus de bienvenue et profitez de vos premiers instants chez Celsius.",
        "greeting": " Bonjour, {{customer.first_name | default:\"ami\"}}👋 ",
        "body": "Vous avez le code - il est temps de l'utiliser.&nbsp; Sur votre premier dépôt, entrez <strong class=\"promocode\">CREW150</strong> et recevez un <strong>Bonus de 100%</strong> et <strong>150 Tours Gratuits </strong>sur <strong>Chaos Crew II par Hacksaw Gaming</strong>.&nbsp; Ce n'est pas une question de pression. C'est une question de puissance - et votre puissance commence ici.",
        "button": "TENTEZ VOTRE CHANCE"
    },
    "Email 8M": {
        "subject": "🎯 Des jackpots en hausse jusqu'à 41 226 $",
        "preheader": "Découvrez les meilleurs gains de la semaine - les machines ont livré, et le sport vous attend.",
        "greeting": " Bonjour, {{customer.first_name | default:\"ami\"}}👋 ",
        "body": "La semaine dernière, de gros gains ont frappé fort - voici ce que certains joueurs ont remporté :&nbsp; <strong>sn••••an a gagné 41 226 $</strong>&nbsp; <strong>d••••ir a décroché 36 078 $</strong>&nbsp; <strong>t••••1964 a remporté 28 914 $</strong>&nbsp; Pendant que les machines distribuaient des jackpots, le sportsbook restait actif aussi. Vous pouvez tourner ou parier - quel que soit votre style, le prochain gain est à un clic.",
        "button": "LANCEZ-VOUS"
    },
    "Email 8S": {
        "subject": "🏆 Un pari. 60% en plus pour le soutenir.",
        "preheader": "Le premier dépôt s'accompagne de 60% de Paris Gratuits - entrez le code et c'est parti.",
        "greeting": " Bonjour, {{customer.first_name | default:\"ami\"}}👋 ",
        "body": "Quand c'est votre premier pari, faites que ça compte.&nbsp; Utilisez le code <strong class=\"promocode\">FIREUP60</strong> sur votre premier dépôt et obtenez un <strong>Bonus de 60% de Paris Gratuits de bienvenue</strong> pour donner plus de poids à votre choix.&nbsp; Pas d'hésitation - juste du jeu intelligent dès le départ.",
        "button": "RÉCLAMER MES PARIS GRATUITS"
    },
    "Email 9C": {
        "subject": "🎠 180 Tours Gratuits vous attendent !",
        "preheader": "Votre premier dépôt ouvre les portes - le code apporte 180 Tours Gratuits.",
        "greeting": " Bonjour, {{customer.first_name | default:\"ami\"}}👋 ",
        "body": "Les premiers pas comptent - et le vôtre s'accompagne de <strong>180 Tours Gratuits</strong> sur <strong>Sweet Bonanza par Pragmatic Play </strong>lorsque vous effectuez un dépôt et entrez le code <strong class=\"promocode\">SWEET180</strong>.&nbsp; Pas de conditions bonus, juste du gameplay pur et l'occasion de trouver votre rythme dès le premier tour.",
        "button": "DÉBLOQUER MES TOURS"
    },
    "Email 9M": {
        "subject": "🎮 Couvre les deux côtés du jeu",
        "preheader": "100 Tours Gratuits et 20% Pari Sans Risque - le code vous lance.",
        "greeting": " Bonjour, {{customer.first_name | default:\"ami\"}}👋 ",
        "body": "Casino ou sportsbook ? Pas besoin de choisir un camp.&nbsp; Utilisez le code <strong class=\"promocode\">LEGACY100</strong> sur votre premier dépôt et débloquez <strong>100 Tours Gratuits</strong> pour <strong>Legacy of Dead par Play'n Go</strong>, et utilisez le code <strong class=\"promocode\">BETSAFE20</strong> pour un <strong>Bonus de 20% Pari Sans Risque</strong> pour vos premiers paris.&nbsp; Deux façons de gagner - un seul départ simple.",
        "button": "OBTENIR MES BONUS"
    },
    "Email 9S": {
        "subject": "🧨 Premier pari ? 60% en plus vous attend",
        "preheader": "Effectuez votre premier dépôt, utilisez le code et obtenez un Bonus de 60% de Paris Gratuits.",
        "greeting": " Bonjour, {{customer.first_name | default:\"ami\"}}👋 ",
        "body": "Les premiers paris méritent plus de poids - et nous avons le boost qu'il vous faut.&nbsp; Utilisez le code <strong class=\"promocode\">FIREUP60</strong> sur votre premier dépôt et débloquez un <strong>Bonus de 60% de Paris Gratuits de bienvenue</strong>.&nbsp; Soyez audacieux. Faites que ça compte.",
        "button": "BOOSTER MON PARI"
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

        # Track block name
        if stripped.startswith("name: "):
            current_name = stripped[6:].strip()
            in_fr = False

        # Track locale
        if stripped.startswith("locale: "):
            locale = stripped[8:].strip()
            in_fr = (locale == "fr-FR")

        # Apply translations for fr-FR blocks
        if in_fr and current_name in translations:
            tr = translations[current_name]

            # Subject
            if stripped.startswith("subject: "):
                new_lines.append(f"subject: {tr['subject']}\n")
                changed += 1
                continue

            # Preheader
            if stripped.startswith("preheader: "):
                new_lines.append(f"preheader: {tr['preheader']}\n")
                changed += 1
                continue

            # Button
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

        new_lines.append(line)

    with open(filepath, "w", encoding="utf-8") as f:
        f.writelines(new_lines)

    return changed


if __name__ == "__main__":
    n = apply_translations(FILE, TR)
    print(f"Welcome Flow: {n} fields translated (expected {len(TR) * 5} = {len(TR)} emails x 5 fields)")
