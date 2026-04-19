#!/usr/bin/env python3
"""Translate Nutrition #2 fr-FR blocks from English to French."""
import re, os

FILE = os.path.join(os.path.dirname(__file__), "Nutrition #2 - Table data.txt")

TR = {
    "Email 1CL": {
        "subject": "🎰 100% Bonus + 50 Tours Gratuits sur Hand of Anubis",
        "preheader": "Votre prochain dépôt double l'action et ajoute 50 tours supplémentaires",
        "greeting": "{{ customer.first_name | default:\"Joueur\" | capitalize }}, les rouleaux vous appellent !",
        "body": "Rechargez votre prochain dépôt aujourd'hui avec le code <strong class=\"promocode\">UNDERDOG50</strong> et profitez d'un <strong>bonus de 100% plus 50 Tours Gratuits</strong> sur <strong>Hand of Anubis par Hacksaw Gaming</strong>. Jouez à vos machines préférées, décrochez des gains et faites que chaque tour compte. Le temps presse - rendons cette manche inoubliable ! 🐕 Réclamez votre boost :",
        "button": "RÉCLAMER LE BONUS"
    },
    "Email 1CS": {
        "subject": "🎰 100% Bonus + 50 Tours Gratuits : Votre deuxième chance !",
        "preheader": "Doublez l'adrénaline sur votre prochain dépôt - réclamez votre récompense aujourd'hui",
        "greeting": "{{ customer.first_name | default:\"Joueur\" | capitalize }}, les rouleaux vous appellent !",
        "body": "Rechargez votre prochain dépôt aujourd'hui, entrez le code <strong class=\"promocode\">UNDERDOG50</strong> et profitez d'un <strong>bonus de 100%</strong> plus <strong>50 Tours Gratuits sur Hand of Anubis par Hacksaw Gaming</strong>. Jouez à vos machines préférées, décrochez des gains et faites que chaque tour compte. Le temps presse - rendons cette manche inoubliable ! 🐕 Réclamez votre boost :",
        "button": "RÉCLAMER LE BONUS"
    },
    "Email 1S": {
        "subject": "🏆 20% Paris Sans Risque jusqu'à €500 vous attendent",
        "preheader": "Votre moment gagnant n'est qu'à un pari - sans risque",
        "greeting": "{{ customer.first_name | default:\"Ami\" | capitalize }}, profitez de l'adrénaline du jeu sans inquiétude.",
        "body": "Obtenez <strong>20% Paris Sans Risque</strong> jusqu'à €500 et transformez chaque pronostic en chance de gagner avec le code <strong class=\"promocode\">CLEARSHOT20</strong>. Placez vos paris et ressentez l'adrénaline ! 🏟️ Faites votre pronostic :",
        "button": "PARIEZ MAINTENANT"
    },
    "Email 2CL": {
        "subject": "🏆 325 000 € gagnés la semaine dernière : Découvrez les gagnants",
        "preheader": "Découvrez les plus gros gains de la semaine - vous pourriez être le prochain",
        "greeting": "{{ customer.first_name | default:\"Ami\" | capitalize }}, la semaine dernière était un rêve de jackpot :",
        "body": "<strong>🔥 Fi••••65y - €145 320</strong> <strong>🔥 le••d4• - €110 780</strong> <strong>🔥 A••••in43 - €69 200</strong> Trois joueurs, trois gains massifs. Serez-vous le prochain sur la liste des gagnants ? Tournez pour votre propre gros gain :",
        "button": "TOURNEZ ET GAGNEZ"
    },
    "Email 2CS": {
        "subject": "🏆 325 000 € gagnés la semaine dernière : Serez-vous le prochain ?",
        "preheader": "Découvrez les plus gros gains aux machines et inspirez-vous",
        "greeting": "{{ customer.first_name | default:\"Ami\" | capitalize }}, la semaine dernière était un rêve de jackpot :",
        "body": "<strong>🏆 Alex••••y - €145 320</strong> <strong>🏆 l••677 - €110 780</strong> <strong>🏆 i66••••7n - €69 200</strong> Trois joueurs, trois gains massifs - tous en tournant leurs machines préférées. Serez-vous le prochain sur la liste des gagnants ? 🌟 Tournez pour votre propre gros gain :",
        "button": "TOURNEZ ET GAGNEZ"
    },
    "Email 2S": {
        "subject": "⚽ Sécurisez votre pari : 20% Paris Sans Risque",
        "preheader": "Votre pari le plus sûr commence aujourd'hui avec jusqu'à €500 couverts",
        "greeting": "{{ customer.first_name | default:\"Ami\" | capitalize }}, entrez sur le terrain en confiance.",
        "body": "Avec <strong>20% Paris Sans Risque</strong> jusqu'à €500, même un tir manqué n'arrêtera pas votre série gagnante. Code pour vous - <strong class=\"promocode\">CLEARSHOT20</strong>. Les cotes vous appellent - placez votre pari maintenant ! 🥅 Obtenez votre filet de sécurité :",
        "button": "PARIEZ MAINTENANT"
    },
    "Email 3CL": {
        "subject": "🃏 100% Bonus Casino Live : Doublez votre jeu",
        "preheader": "Votre prochain dépôt double l'excitation aux tables",
        "greeting": "{{ customer.first_name | default:\"Ami\" | capitalize }}, les cartes sont prêtes, les croupiers vous attendent.",
        "body": "Déposez avec le code <strong class=\"promocode\">MATCH100</strong> et obtenez un <strong>bonus de 100%</strong> sur votre prochain rechargement. Entrez dans l'action et faites que chaque main compte ! ♠️ Rejoignez la table :",
        "button": "REJOINDRE LA TABLE"
    },
    "Email 3CS": {
        "subject": "🔮 200% Bonus + 50 Tours Gratuits sur Tome of Madness",
        "preheader": "La prochaine aventure de Rich Wilde vous attend - triplez votre solde maintenant",
        "greeting": "{{ customer.first_name | default:\"Ami\" | capitalize }}, entrez dans le monde de Rich Wilde.",
        "body": "Déposez avec le code <strong class=\"promocode\">OCCULT200</strong> et obtenez un <strong>bonus de 200% plus 50 Tours Gratuits sur Rich Wilde and the Tome of Madness</strong> par Play'n Go pour découvrir des trésors cachés. Êtes-vous prêt à tourner les pages de la fortune ? Le livre est ouvert. 📖 Ouvrez le livre des gains :",
        "button": "RÉCLAMER LE BONUS"
    },
    "Email 3S": {
        "subject": "🥇 Pariez jusqu'à €500 sans risque : Bonus de 20%",
        "preheader": "Même les paris les plus audacieux sont couverts avec notre offre Sans Risque",
        "greeting": "{{ customer.first_name | default:\"Ami\" | capitalize }}, pariez gros sans peur de perdre.",
        "body": "Avec <strong>20% Paris Sans Risque</strong> jusqu'à €500, vous êtes toujours dans le jeu.&nbsp; Entrez le code <strong class=\"promocode\">CLEARSHOT20</strong>. Faites votre coup - la victoire pourrait n'être qu'à un pari ! 🏆 Placez votre pari protégé :",
        "button": "PLACEZ VOTRE PARI"
    },
    "Email 4CL": {
        "subject": "🎯 Gagnants au Casino Live : Gros gains la semaine dernière",
        "preheader": "Découvrez qui est reparti avec d'énormes gains aux tables",
        "greeting": "{{ customer.first_name | default:\"Ami\" | capitalize }}, les tables du Casino Live étaient en feu la semaine dernière :",
        "body": "<strong>💎 Dt••••s - €49 800</strong> <strong>💎 e•••95 - €33 420</strong> <strong>💎 ••p•••sh•• - €21 760</strong> Votre nom pourrait être le prochain au tableau des gagnants.&nbsp; Rejoignez les tables et faites votre coup ! Jouez en direct :",
        "button": "JOUEZ EN DIRECT"
    },
    "Email 4CS": {
        "subject": "🎯 100% Bonus + 50 TG sur Hand of Anubis",
        "preheader": "Votre prochain dépôt vous offre plus de fun et plus de chances de gagner",
        "greeting": "{{ customer.first_name | default:\"Ami\" | capitalize }}, rendons votre prochain tour deux fois plus excitant :",
        "body": "Obtenez un <strong>bonus de 100% plus 50 Tours Gratuits sur Hand of Anubis par Hacksaw Gaming</strong> avec le code <strong class=\"promocode\">UNDERDOG50</strong> lors de votre rechargement. Plus de solde, plus de tours, plus de chances de décrocher le gros lot - vous en êtes ? 🐾 Doublez votre solde :",
        "button": "RÉCLAMER LE BONUS"
    },
    "Email 4S": {
        "subject": "🏅 20% Paris Sans Risque : On assure vos arrières",
        "preheader": "Tentez le coup avec jusqu'à €500 de couverture sur votre pari",
        "greeting": "{{ customer.first_name | default:\"Ami\" | capitalize }}, lancez-vous dans l'action sans pression.",
        "body": "Profitez de <strong>20% Paris Sans Risque</strong> jusqu'à €500 et transformez chaque mise en chance de gagner avec le code <strong class=\"promocode\">CLEARSHOT20</strong>. Pas de peur, juste de l'adrénaline pure. 🔥 Commencez à parier sans risque :",
        "button": "COMMENCEZ À PARIER"
    },
    "Email 5CL": {
        "subject": "💎 200% Bonus Casino Live : Triplez votre solde",
        "preheader": "Votre prochaine session au Casino Live devient plus grande et meilleure",
        "greeting": "{{ customer.first_name | default:\"Ami\" | capitalize }}, prenez place aux tables du Casino Live et jouez avec une puissance triplée.",
        "body": "Déposez avec le code <strong class=\"promocode\">ROCKET200</strong> et obtenez un <strong>bonus de 200%</strong> sur votre prochain rechargement. L'action est en direct - êtes-vous prêt ? 🚀 Boostez votre solde :",
        "button": "JOUEZ EN DIRECT"
    },
    "Email 5CS": {
        "subject": "📚 200% Bonus + 50 TG : Triplez votre solde !",
        "preheader": "Plongez dans l'aventure de Rich Wilde et réclamez vos récompenses sur votre dépôt",
        "greeting": "{{ customer.first_name | default:\"Ami\" | capitalize }}, votre prochain dépôt pourrait ouvrir les portes de la fortune :",
        "body": "Obtenez un <strong>bonus de 200% plus 50 Tours Gratuits pour Rich Wilde and the Tome of Madness</strong> par Play'n GO avec le code <strong class=\"promocode\">OCCULT200</strong>. Les rouleaux sont prêts - êtes-vous assez courageux pour affronter la folie ? 👁️ Découvrez les trésors secrets :",
        "button": "RÉCLAMER LE BONUS"
    },
    "Email 5S": {
        "subject": "🏟 Gros gains sportifs la semaine dernière : Découvrez les scores",
        "preheader": "Découvrez qui a marqué gros - serez-vous le prochain ?",
        "greeting": "{{ customer.first_name | default:\"Ami\" | capitalize }}, découvrez le top 3 des parieurs qui ont encaissé la semaine dernière :",
        "body": "<strong>🏆 se•••54 - €48 200</strong> <strong>🏆 Ra••34•• - €32 900</strong> <strong>🏆 H••••a - €26 400</strong> Votre ticket gagnant pourrait n'être qu'à un pari. 🎫 Placez votre pari gagnant :",
        "button": "PLACEZ VOTRE PARI"
    },
    "Email 6CL": {
        "subject": "🏆 Top 3 des gagnants de la semaine : Découvrez la liste",
        "preheader": "Découvrez combien nos 3 meilleurs joueurs ont remporté récemment",
        "greeting": "{{ customer.first_name | default:\"Ami\" | capitalize }}, la semaine dernière était incroyable :",
        "body": "<strong>💰 se•••s - €48 200</strong> <strong>💰 M8•••7 - €32 750</strong> <strong>💰 g•••ns - €27 460</strong> Trois tours chanceux, trois prix qui changent la vie. Verrons-nous votre nom sur la liste de cette semaine ? Tentez votre chance :",
        "button": "JOUEZ MAINTENANT"
    },
    "Email 6CS": {
        "subject": "🏆 Énormes jackpots la semaine dernière : Regardez ça",
        "preheader": "Découvrez combien nos 3 meilleurs joueurs ont remporté récemment",
        "greeting": "{{ customer.first_name | default:\"Ami\" | capitalize }}, la semaine dernière était incroyable :",
        "body": "<strong>💰 ses - €48 200</strong> <strong>💰 M87 - €32 750</strong> <strong>💰 g•ns - €27 460</strong> Trois tours chanceux, trois prix qui changent la vie. Verrons-nous votre nom sur la liste de cette semaine ? Tentez votre chance :",
        "button": "JOUEZ MAINTENANT"
    },
    "Email 6S": {
        "subject": "🎯 20% Paris Sans Risque : Votre seconde chance",
        "preheader": "Tentez le coup - nous vous couvrons jusqu'à €500",
        "greeting": "{{ customer.first_name | default:\"Ami\" | capitalize }}, c'est votre tour.",
        "body": "Profitez de <strong>20% Paris Sans Risque</strong> jusqu'à €500 et jouez sans arrière-pensée avec le code <strong class=\"promocode\">CLEARSHOT20</strong>. Chaque pronostic vous rapproche de la victoire. ⚽ Réclamez votre couverture :",
        "button": "COMMENCEZ À PARIER"
    },
    "Email 7CL": {
        "subject": "🎩 210% Boost Casino Live : Offre exclusive",
        "preheader": "Triplez l'excitation au Casino Live sur votre prochain dépôt",
        "greeting": "{{ customer.first_name | default:\"Ami\" | capitalize }}, entrez au Casino Live et jouez avec une puissance inégalée.",
        "body": "Déposez avec le code <strong class=\"promocode\">BLAST210</strong> et obtenez un <strong>bonus de 210%</strong> sur votre prochain rechargement. Les croupiers sont prêts - votre série gagnante commence maintenant. 🎲 Réclamez votre boost exclusif :",
        "button": "JOUEZ EN DIRECT"
    },
    "Email 7CS": {
        "subject": "💰 3 gagnants massifs la semaine dernière - Pourquoi pas vous ?",
        "preheader": "3 joueurs. 3 gains. Votre nom pourrait être le prochain sur la liste",
        "greeting": "{{ customer.first_name | default:\"Ami\" | capitalize }}, voici qui a décroché l'or la semaine dernière :",
        "body": "<strong>🥇 Li•••n8• - €45 320</strong> <strong>🥈 a••7tz - €38 940</strong> <strong>🥉 h••••in - €26 580</strong> Votre nom pourrait être sur la prochaine liste des champions.&nbsp; Il suffit d'un tour chanceux ! 🎰 Rejoignez le cercle des gagnants :",
        "button": "JOUEZ MAINTENANT"
    },
    "Email 7S": {
        "subject": "🏇 Pariez audacieusement : 20% Paris Sans Risque actifs",
        "preheader": "Pariez jusqu'à €500 sans peur de perdre",
        "greeting": "{{ customer.first_name | default:\"Ami\" | capitalize }}, lancez-vous dans l'action !",
        "body": "Obtenez <strong>20% Paris Sans Risque</strong> jusqu'à €500 avec le code <strong class=\"promocode\">CLEARSHOT20</strong>. Football, tennis ou courses - votre pari est couvert. Pas de risque, que de l'adrénaline. 🏁 Lancez votre série gagnante :",
        "button": "PLACEZ VOTRE PARI"
    },
    "Email 8CL": {
        "subject": "💥 220% Bonus : Boostez votre session Live",
        "preheader": "Plus de jetons, plus de chances, plus de gains sur votre prochain dépôt",
        "greeting": "{{ customer.first_name | default:\"Ami\" | capitalize }}, le Casino Live vous attend.",
        "body": "Déposez avec le code <strong class=\"promocode\">BOOSTED220</strong> et obtenez un <strong>bonus de 220%</strong> sur votre prochain rechargement. Votre place est réservée - faisons que chaque main compte ! 🔴⚫ Obtenez votre <strong>bonus de 220%</strong> :",
        "button": "REJOINDRE LA TABLE"
    },
    "Email 8CS": {
        "subject": "🎰 Réclamez 100 Tours Gratuits sur Legacy of Dead",
        "preheader": "Entrez dans les tombes et réclamez vos gains sur votre prochain dépôt",
        "greeting": "{{ customer.first_name | default:\"Ami\" | capitalize }}, les rouleaux de Legacy of Dead vous appellent.",
        "body": "Déposez avec le code <strong class=\"promocode\">PHARAOH100</strong> et débloquez <strong>100 Tours Gratuits sur Legacy of Dead</strong> par Play'n Go pour explorer des trésors cachés. Votre aventure commence avec un seul tour - prêt ? 🏺 Entrez dans le tombeau des gains :",
        "button": "RÉCLAMER LES TOURS GRATUITS"
    },
    "Email 8S": {
        "subject": "🏆 20% Paris Sans Risque : Gagnez ou soyez remboursé",
        "preheader": "Votre filet de sécurité vous attend - pariez jusqu'à €500 sans risque",
        "greeting": "{{ customer.first_name | default:\"Ami\" | capitalize }}, lancez-vous dans le jeu !",
        "body": "Jouez avec <strong>20% Paris Sans Risque</strong> jusqu'à €500. Votre code : <strong class=\"promocode\">CLEARSHOT20</strong>. Raté ? Nous vous couvrons. Gagné ? Les gains sont à vous. La façon la plus sûre de vivre l'adrénaline est ici. 🛡️ Réclamez vos paris gratuits :",
        "button": "RÉCLAMER LES PARIS GRATUITS"
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
    print(f"Nutrition #2: {n} fields translated (expected {expected} = {len(TR)} emails x 5 fields)")
