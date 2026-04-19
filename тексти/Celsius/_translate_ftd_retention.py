#!/usr/bin/env python3
"""Translate FTD Retention Flow fr-FR blocks from English to French."""
import re, os

FILE = os.path.join(os.path.dirname(__file__), "FTD Retention Flow - Table data.txt")

TR = {
    "Email 1C": {
        "subject": "🐍 Les sables bougent - débloquez 100% + 50 TG",
        "preheader": "Le bonus pour votre prochain dépôt sur Hand of Anubis est prêt",
        "greeting": " Bonjour, {{customer.first_name | default:\"ami\"}}👋 ",
        "body": "Vous êtes entré dans le jeu - il est temps d'aller plus loin. Utilisez le code <strong class=\"promocode\">ANUBIS10050</strong> sur votre prochain dépôt pour débloquer un <strong>bonus de 100% + 50 Tours Gratuits</strong> sur <strong>Hand of Anubis</strong> <strong>par Hacksaw Gaming</strong>. La puissance antique rencontre l'adrénaline moderne - prêt à tourner ?",
        "button": "RÉCLAMER MON BONUS"
    },
    "Email 1M": {
        "subject": "🎮 Votre prochaine étape ? Bonus Casino ou Pari Sans Risque Sport",
        "preheader": "Choisissez comment continuer - tours, paris ou les deux",
        "greeting": " Bonjour, {{customer.first_name | default:\"ami\"}}👋 ",
        "body": "Vous avez fait votre premier dépôt - gardons l'élan. Voici ce qui vous attend pour votre prochain coup : Un <strong>Bonus de 100%</strong> + <strong>50 Tours Gratuits</strong> sur <strong>Hand of Anubis par Hacksaw Gaming</strong> pour les amateurs de casino - utilisez le code <strong class=\"promocode\">ANUBIS10050</strong> Un <strong>20% Pari Sans Risque</strong> pour votre prochain pari sportif - utilisez le code <strong class=\"promocode\">WINBACKNRF20</strong> Doublez la mise au casino ou jouez malin au sportsbook - dans les deux cas, votre prochain coup commence ici.",
        "button": "CONTINUER À JOUER"
    },
    "Email 1S": {
        "subject": "🏆 20% Pari Sans Risque est actif pour vous",
        "preheader": "Récupérez 20% de votre mise si les choses ne tournent pas - uniquement après votre premier dépôt",
        "greeting": " Bonjour, {{customer.first_name | default:\"ami\"}}👋 ",
        "body": "Vous avez fait votre premier dépôt - il est temps de parier intelligemment. Utilisez le code <strong class=\"promocode\">WINBACKNRF20</strong> et profitez d'un <strong>20% Pari Sans Risque</strong> sur votre prochain pari. Si le résultat n'est pas en votre faveur, nous vous rendrons <strong>20%</strong> sur votre solde.&nbsp; Simple comme ça.",
        "button": "PLACER MON PARI GRATUIT"
    },
    "Email 2C": {
        "subject": "🎯 Votre prochain tour pourrait être le gros lot",
        "preheader": "Un dépôt de plus pourrait tourner les chances en votre faveur",
        "greeting": " Bonjour, {{customer.first_name | default:\"ami\"}}👋 ",
        "body": "Les rouleaux n'attendent pas - et les gains non plus. Des milliers de joueurs tournent chaque heure.&nbsp; Certains repartent avec l'adrénaline... d'autres avec un jackpot. Votre prochain dépôt, c'est tout ce qu'il faut pour revenir dans le jeu. Pas de pression - juste de l'adrénaline pure.",
        "button": "REJOUER"
    },
    "Email 2M": {
        "subject": "🎯 100% + 60 TG ou 20% Pari Sans Risque - Votre choix",
        "preheader": "Casino ou Sport ? Obtenez un bonus + Tours Gratuits ou jouez en sécurité avec le Pari Sans Risque",
        "greeting": " Bonjour, {{customer.first_name | default:\"ami\"}}👋 ",
        "body": "Maintenant que votre premier dépôt est derrière vous - allons plus loin. Choisissez comment booster votre prochain coup : Code <strong class=\"promocode\">DOG10060</strong> - <strong>Bonus de 100%</strong> + <strong>60 Tours Gratuits</strong> sur <strong>The Dog House Megaways par Pragmatic Play</strong> si vous tournez les rouleaux Code <strong class=\"promocode\">WINBACKNRF20</strong> - <strong>20% Pari Sans Risque</strong> si vous soutenez votre favori sur le terrain Quelle que soit votre voie, votre prochain gain commence ici.",
        "button": "RÉCLAMER MON BONUS"
    },
    "Email 2S": {
        "subject": "🎯 Pari raté ? Récupérez 20%",
        "preheader": "Votre 20% Pari Sans Risque est actif - continuez à jouer en confiance",
        "greeting": " Bonjour, {{customer.first_name | default:\"ami\"}}👋 ",
        "body": "Au sport, tous les paris ne passent pas - mais nous assurons vos arrières. Placez votre prochain pari avec le code <strong class=\"promocode\">WINBACKNRF20</strong> et obtenez un <strong>20% Pari Sans Risque</strong>. Si ça ne tourne pas en votre faveur, nous rendrons <strong>20%</strong> sur votre compte.&nbsp; Pas de stress, juste du jeu intelligent.",
        "button": "PLACER MON PARI GRATUIT"
    },
    "Email 3C": {
        "subject": "🍓 140% + 50 TG - Rejoignez la Fruit Party",
        "preheader": "Adoucissez votre prochain dépôt avec ce bonus juteux",
        "greeting": " Bonjour, {{customer.first_name | default:\"ami\"}}👋 ",
        "body": "Prêt pour quelque chose de sucré ? Utilisez le code <strong class=\"promocode\">PARTY140</strong> sur votre prochain dépôt et obtenez un <strong>bonus de 140% + 50 Tours Gratuits</strong> sur <strong>Fruit Party</strong> <strong>par Pragmatic Play</strong>. Ce jeu déborde de couleurs - et de potentiel de gains. Lancez les rouleaux !",
        "button": "OBTENIR MON BONUS"
    },
    "Email 3M": {
        "subject": "🎯 2%/3%/4% Cashback + 20%/25%/30% Pari Sans Risque",
        "preheader": "Boostez à la fois le casino et le sport",
        "greeting": " Bonjour, {{customer.first_name | default:\"ami\"}}👋 ",
        "body": "Votre prochain dépôt débloque une double récompense - peu importe ce que vous jouez. Utilisez le code <strong class=\"promocode\">SAFE2CB2</strong> / <strong class=\"promocode\">RETURN3CB3</strong> / <strong class=\"promocode\">BOOST4CB4</strong> et recevez : <strong>2%/3%/4% Cashback</strong> sur l'activité casino Ou utilisez le code <strong class=\"promocode\">WINBACKNRF20</strong> / <strong class=\"promocode\">SAFETYNRF25</strong> / <strong class=\"promocode\">COVERNRF30</strong> pour obtenir : <strong>20%/25%/30% Pari Sans Risque</strong> pour vos paris sportifs Vous choisissez comment jouer - et nous ferons en sorte que ça rapporte.",
        "button": "UTILISER MON CODE"
    },
    "Email 3S": {
        "subject": "🧲 20% Pari Sans Risque - Restez dans le jeu",
        "preheader": "Gagnant ou non, votre prochain pari s'accompagne de 20% en retour - utilisez le code WINBACKNRF20",
        "greeting": " Bonjour, {{customer.first_name | default:\"ami\"}}👋 ",
        "body": "Votre premier dépôt a débloqué un filet de sécurité - ne le laissez pas se perdre. Utilisez le code <strong class=\"promocode\">WINBACKNRF20</strong> pour activer le <strong>20% Pari Sans Risque</strong> et placez votre prochain pari en sachant que nous couvrirons une partie si ça ne passe pas.&nbsp; Simple, intelligent et sans tracas.",
        "button": "PLACER MON PARI"
    },
    "Email 4C": {
        "subject": "🧁 Devenez dork à fond - 110% + 50 TG à l'intérieur",
        "preheader": "Dork Unit vous attend avec un bonus tout sauf bête",
        "greeting": " Bonjour, {{customer.first_name | default:\"ami\"}}👋 ",
        "body": "Vous avez débloqué l'accès à l'un des hits les plus décalés du moment. Utilisez le code <strong class=\"promocode\">DORK50110</strong> sur votre prochain dépôt et obtenez un <strong>bonus de 110% + 50 Tours Gratuits</strong> sur <strong>Dork Unit</strong> <strong>par Hacksaw Gaming</strong>. Ne vous fiez pas au nom - cette machine à sous a un potentiel de gains sérieux.",
        "button": "ACTIVER MON BONUS"
    },
    "Email 4M": {
        "subject": "💸 Plus de 100 000 $ gagnés la semaine dernière - Ferez-vous partie de la liste ?",
        "preheader": "Découvrez les derniers gros gains de vrais joueurs et de vrais jeux",
        "greeting": " Bonjour, {{customer.first_name | default:\"ami\"}}👋 ",
        "body": "Les rouleaux étaient en feu la semaine dernière - et voici qui en a le plus profité : <strong>l•88 a gagné 47 230 $ sur Sweet Bonanza</strong> <strong>v•01 a décroché 35 910 $ sur Money Train 3</strong> <strong>B•in a remporté 18 450 $ sur Gates of Olympus</strong> Ce sont de vrais gains de vrais joueurs qui ont tourné comme vous. Alors... prêt à voir votre nom en haut la prochaine fois ?",
        "button": "TOURNEZ POUR GAGNER"
    },
    "Email 4S": {
        "subject": "💼 25% Pari Sans Risque - Vous êtes couvert",
        "preheader": "Placez votre prochain pari et récupérez 25% si ça ne passe pas",
        "greeting": " Bonjour, {{customer.first_name | default:\"ami\"}}👋 ",
        "body": "Vous avez déjà fait votre premier dépôt - il est temps de parier en confiance. Utilisez le code <strong class=\"promocode\">SAFETYNRF25</strong> pour activer un <strong>25% Pari Sans Risque</strong> - votre prochain pari s'accompagne d'un filet de sécurité. Si le résultat ne tourne pas en votre faveur, nous rendrons <strong>25%</strong> de votre mise sur votre solde.",
        "button": "PLACER MON PARI GRATUIT"
    },
    "Email 5C": {
        "subject": "🍭 Obtenez 100% + 80 TG sur Sweet Bonanza",
        "preheader": "Le bonus pour votre prochain dépôt vient de devenir beaucoup plus sucré",
        "greeting": " Bonjour, {{customer.first_name | default:\"ami\"}}👋 ",
        "body": "Préparez-vous pour une montée de sucre. Utilisez le code <strong class=\"promocode\">BONANZA10080</strong> sur votre prochain dépôt et obtenez un <strong>bonus de 100% + 80 Tours Gratuits</strong> sur <strong>Sweet Bonanza</strong> <strong>par Pragmatic Play</strong>. Des gains juteux, une haute volatilité et plein de surprises - qu'est-ce qui ne plaît pas ?",
        "button": "JOUER À SWEET BONANZA"
    },
    "Email 5M": {
        "subject": "🪙 100% + 70 TG ou 20% Pari Sans Risque - Faites votre choix",
        "preheader": "Casino ou sport - votre bonus de deuxième étape est prêt dans les deux cas",
        "greeting": " Bonjour, {{customer.first_name | default:\"ami\"}}👋 ",
        "body": "Vous avez passé votre premier dépôt - il est temps de booster votre prochain coup. Voici ce qui vous attend : 🎰 Avec le code <strong class=\"promocode\">CHAOS10070</strong> - <strong>Bonus de 100%</strong> + <strong>70 Tours Gratuits</strong> sur <strong>Chaos Crew II par Hacksaw Gaming</strong> pour les amateurs de casino ⚽ Avec le code <strong class=\"promocode\">WINBACKNRF20</strong> - <strong>20% Pari Sans Risque</strong> si vous êtes fan de cotes Quelle que soit votre façon de jouer, une récompense est taillée pour votre jeu.",
        "button": "CHOISIR MON BONUS"
    },
    "Email 5S": {
        "subject": "🏅 30% No Risk Only Win - C'est parti",
        "preheader": "Jouez en confiance - votre prochain pari s'accompagne d'un filet de sécurité de 30%",
        "greeting": " Bonjour, {{customer.first_name | default:\"ami\"}}👋 ",
        "body": "Vous avez déjà fait votre premier pas - lancez-vous en confiance. Profitez d'un <strong>bonus 30% No Risk Only Win</strong> sur votre prochain pari sportif avec le code <strong class=\"promocode\">ONLYWIN30</strong>. Si ça ne tourne pas en votre faveur, nous rendrons <strong>30%</strong> de votre mise.&nbsp; Pas de pression - juste du jeu pur.",
        "button": "PLACER MON PARI GRATUIT"
    },
    "Email 6C": {
        "subject": "📜 100% + 150 TG - Entrez dans le Tome of Madness",
        "preheader": "Boostez votre dépôt et tournez à travers les secrets",
        "greeting": " Bonjour, {{customer.first_name | default:\"ami\"}}👋 ",
        "body": "Prêt à découvrir des trésors sombres ? Utilisez le code <strong class=\"promocode\">RICH100150</strong> sur votre prochain dépôt et recevez un <strong>bonus de 100% + 150 Tours Gratuits</strong> sur <strong>Rich Wilde and the Tome of Madness</strong> <strong>par Play'n Go</strong>. Puissance arcane. Symboles mystérieux. Aventure sans fin.",
        "button": "RÉCLAMER MES TOURS GRATUITS"
    },
    "Email 6M": {
        "subject": "💰 2%/3%/4% Cashback + 20%/25%/30% Pari Sans Risque",
        "preheader": "Jouez malin avec le Cashback au casino et le Pari Sans Risque au sport",
        "greeting": " Bonjour, {{customer.first_name | default:\"ami\"}}👋 ",
        "body": "Prêt à tirer plus de chaque tour et pari ?&nbsp; Votre prochain dépôt avec le code <strong class=\"promocode\">SAFE2CB2</strong> / <strong class=\"promocode\">RETURN3CB3</strong> / <strong class=\"promocode\">BOOST4CB4</strong> vous donne : <strong>2%/3%/4% Cashback</strong> sur votre jeu casino Ou utilisez <strong class=\"promocode\">WINBACKNRF20</strong> / <strong class=\"promocode\">SAFETYNRF25</strong> / <strong class=\"promocode\">COVERNRF30</strong> et recevez : <strong>20%/25%/30% Pari Sans Risque</strong> pour vos paris sportifs Vous apportez le jeu - nous apportons la valeur. C'est votre style, maintenant amélioré.",
        "button": "UTILISER MON CODE"
    },
    "Email 6S": {
        "subject": "🔁 20% Pari Sans Risque - Laissez le prochain filer",
        "preheader": "Raté ? Nous rendrons 20% sur votre prochain pari - utilisez le code WINBACKNRF20",
        "greeting": " Bonjour, {{customer.first_name | default:\"ami\"}}👋 ",
        "body": "Vous avez placé votre premier pari - maintenant nous vous donnons plus de marge pour jouer audacieusement. Utilisez le code <strong class=\"promocode\">WINBACKNRF20</strong> pour activer un <strong>20% Pari Sans Risque</strong> - votre prochain pari s'accompagne d'une protection intégrée.&nbsp; Si le résultat ne tourne pas en votre faveur, nous rendrons <strong>20%</strong> de votre mise - tout simplement.",
        "button": "PLACER MON PARI GRATUIT"
    },
    "Email 7C": {
        "subject": "🔥 Les plus gros gains venaient de prochains dépôts",
        "preheader": "Serez-vous le prochain grand gagnant ?",
        "greeting": " Bonjour, {{customer.first_name | default:\"ami\"}}👋 ",
        "body": "Certaines de nos plus grandes histoires de jackpot ont commencé avec un prochain dépôt. Il n'y a pas de secret - juste une nouvelle chance de jouer à vos jeux préférés et de décrocher ce tour en or. Prêt à écrire votre propre histoire gagnante ?",
        "button": "JE REVIENS"
    },
    "Email 7M": {
        "subject": "🎉 Gros gains ce mois - Plus de 120 000 $ distribués",
        "preheader": "Ces joueurs ont touché le jackpot - découvrez ce qu'ils ont joué et combien ils ont gagné",
        "greeting": " Bonjour, {{customer.first_name | default:\"ami\"}}👋 ",
        "body": "Les chiffres sont tombés - et ce mois a apporté des gains sérieux : <strong>r•y45 a gagné 50 780 $ sur The Dog House Megaways</strong> <strong>Uncn a décroché 41 300 $ sur Book of Dead</strong> <strong>t•5s a remporté 31 920 $ sur Fruit Party</strong> Ils ont fait leur coup - et ça a payé.&nbsp; Le prochain grand moment pourrait-il être le vôtre ?",
        "button": "JOUEZ MAINTENANT"
    },
    "Email 7S": {
        "subject": "🏁 Votre 20% Pari Sans Risque est actif",
        "preheader": "Jouez votre prochain pari en confiance - 20% revient si ça ne passe pas",
        "greeting": " Bonjour, {{customer.first_name | default:\"ami\"}}👋 ",
        "body": "Bonne nouvelle - utilisez le code <strong class=\"promocode\">WINBACKNRF20</strong> pour réclamer votre <strong>20% Pari Sans Risque</strong>. Placez votre prochain pari sportif, et si ça ne passe pas, nous rendrons <strong>20%</strong> de votre mise sur votre solde. C'est simple, intelligent et conçu pour vous garder dans le jeu.",
        "button": "PLACER MON PARI GRATUIT"
    },
    "Email 8C": {
        "subject": "⚡ 150% + 30 TG - Libérez la puissance de Stormforged",
        "preheader": "Frappez fort avec votre bonus de prochain dépôt",
        "greeting": " Bonjour, {{customer.first_name | default:\"ami\"}}👋 ",
        "body": "Vous sentez le tonnerre ? C'est <strong>Stormforged</strong> qui appelle. Utilisez le code <strong class=\"promocode\">FORGED150</strong> sur votre prochain dépôt pour débloquer un <strong>bonus de 150% + 30 Tours Gratuits</strong> sur <strong>Stormforged par Hacksaw Gaming</strong>, cette machine à sous électrisante. Les dieux vous attendent - amenez la tempête.",
        "button": "RÉCLAMER MON BONUS"
    },
    "Email 8M": {
        "subject": "💵 2%/3%/4% Cashback + 20%/25%/30% Pari Sans Risque",
        "preheader": "Boostez à la fois le casino et le sport en un seul geste",
        "greeting": " Bonjour, {{customer.first_name | default:\"ami\"}}👋 ",
        "body": "Votre gameplay mérite plus - et ce combo livre. Sur votre prochain dépôt, utilisez le code <strong class=\"promocode\">SAFE2CB2</strong> / <strong class=\"promocode\">RETURN3CB3</strong> / <strong class=\"promocode\">BOOST4CB4</strong> pour débloquer : <strong>2%/3%/4% Cashback</strong> sur votre jeu casino Ou utilisez le code <strong class=\"promocode\">WINBACKNRF20</strong> / <strong class=\"promocode\">SAFETYNRF25</strong> / <strong class=\"promocode\">COVERNRF30</strong> pour obtenir : <strong>20%/25%/30% Pari Sans Risque</strong> pour vos prochains paris sportifs C'est intelligent, flexible et conçu pour récompenser votre style.",
        "button": "RÉCLAMER MON BONUS"
    },
    "Email 8S": {
        "subject": "🧲 30% Pari Sans Risque - Votre avantage sur le prochain pari",
        "preheader": "Pari raté ? Pas de souci - nous rendrons 30% de votre mise",
        "greeting": " Bonjour, {{customer.first_name | default:\"ami\"}}👋 ",
        "body": "Vous êtes entré dans le jeu - il est temps d'aller plus loin avec une protection supplémentaire. Placez votre prochain pari sportif avec un <strong>30% Pari Sans Risque</strong> avec le code <strong class=\"promocode\">ONLYWIN30</strong>. Si ça ne tourne pas en votre faveur, vous récupérerez <strong>30%</strong> de votre mise - sans questions.",
        "button": "PARIEZ SANS RISQUE"
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

            if stripped.startswith("text_1: "):
                new_line = re.sub(
                    r'(<strong>)(.+?)(</strong>)',
                    lambda m: m.group(1) + tr['greeting'] + m.group(3),
                    stripped
                )
                new_lines.append(new_line + "\n")
                changed += 1
                continue

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
    expected = len(TR) * 5
    n = apply_translations(FILE, TR)
    print(f"FTD Retention: {n} fields translated (expected {expected} = {len(TR)} emails x 5 fields)")
