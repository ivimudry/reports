#!/usr/bin/env python3
"""Translate Nutrition #3 fr-FR blocks from English to French."""
import re, os

FILE = os.path.join(os.path.dirname(__file__), "Nutrition #3 - Table data.txt")

TR = {
    "Email 1CL": {
        "subject": "🎲 Boostez votre jeu Live avec un Bonus de 150%",
        "preheader": "Votre prochain rechargement est accompagné de 150% de jetons supplémentaires",
        "greeting": "{{ customer.first_name | default:\"Ami\" | capitalize }}, votre troisième dépôt est l'occasion de renverser la table.",
        "body": "Rechargez maintenant avec le code <strong class=\"promocode\">VAULT150</strong> et obtenez un <strong>bonus de 150%</strong> pour jouer plus longtemps, miser plus gros et viser plus haut aux tables du Casino Live. Votre siège gagnant vous attend - rendons celui-ci mémorable. ♠️ Boostez votre solde :",
        "button": "RÉCLAMER LE BONUS"
    },
    "Email 1CS": {
        "subject": "🎯 200% Bonus + 50 TG : La troisième est la bonne !",
        "preheader": "Boostez votre jeu sur votre troisième dépôt et plongez dans vos machines préférées",
        "greeting": "{{ customer.first_name | default:\"Ami\" | capitalize }}, votre troisième dépôt pourrait être le plus palpitant !",
        "body": "Obtenez un <strong>bonus de 200% plus 50 Tours Gratuits sur Rich Wilde and the Tome of Madness</strong> par Play'n Go. Utilisez le code <strong class=\"promocode\">OCCULT200</strong> pour débloquer les secrets. C'est votre moment pour viser plus gros, tourner plus audacieusement et décrocher le prochain gros gain ! 🐙 Réclamez votre triple boost :",
        "button": "RÉCLAMER LE BONUS"
    },
    "Email 1S": {
        "subject": "🏆 Prêt pour votre troisième série gagnante ?",
        "preheader": "Pariez malin - gagnez jusqu'à €500 sans risque sur votre prochain dépôt",
        "greeting": "{{ customer.first_name | default:\"Ami\" | capitalize }}, vous avez déjà prouvé que vous êtes dans le jeu. Il est temps de faire compter votre troisième dépôt.",
        "body": "Obtenez <strong>20% Paris Sans Risque jusqu'à €500</strong> avec le code <strong class=\"promocode\">STEADY20</strong> et passez vos pronostics au niveau supérieur. Le terrain est à vous - êtes-vous prêt à jouer gros ? 🏟️ Placez votre pari sans risque :",
        "button": "PLACEZ VOTRE PARI"
    },
    "Email 2CL": {
        "subject": "🏆 Légendes du Casino Live : Les gros gains de la semaine",
        "preheader": "Découvrez qui a dominé les tables - serez-vous le prochain ?",
        "greeting": "{{ customer.first_name | default:\"Ami\" | capitalize }}, les tables du Casino Live étaient en feu la semaine dernière :",
        "body": "<strong>🔥 Ln4s••• - €49 820</strong> <strong>🔥 tin•••66 - €34 470</strong> <strong>🔥 n•••tz - €25 960</strong> Trois joueurs, trois parcours incroyables - tous grâce à des coups audacieux et des stratégies malines. Votre nom sera-t-il au classement la semaine prochaine ? Rejoignez les gagnants :",
        "button": "JOUEZ EN DIRECT"
    },
    "Email 2CS": {
        "subject": "🏆 Champions des machines la semaine dernière : Qui a gagné gros ?",
        "preheader": "Découvrez les plus gros gagnants aux machines et leurs gains",
        "greeting": "{{ customer.first_name | default:\"Ami\" | capitalize }}, voici comment les rouleaux ont traité nos champions :",
        "body": "<strong>👑 mu••••n65 - €48 940</strong> <strong>👑 Z3•••ky• - €36 280</strong> <strong>👑 p••••sh - €29 760</strong> Ils ont fait compter chaque tour - et vous pouvez en faire autant. Votre nom sera-t-il en tête de la liste la semaine prochaine ? Tournez pour la gloire :",
        "button": "TOURNEZ ET GAGNEZ"
    },
    "Email 2S": {
        "subject": "⚽ Votre prochain gain pourrait être sans risque !",
        "preheader": "Obtenez 20% Paris Sans Risque jusqu'à €500 sur votre troisième dépôt",
        "greeting": "{{ customer.first_name | default:\"Ami\" | capitalize }}, vous jouez bien - il est temps pour le troisième round.",
        "body": "Faites votre troisième dépôt, utilisez le code <strong class=\"promocode\">STEADY20</strong> et obtenez <strong>20% Paris Sans Risque jusqu'à €500</strong>. Même un tir manqué ne vous ralentira pas. Entrez sur le terrain et montrez-leur qui est le patron. 👟 Pariez en confiance :",
        "button": "PARIEZ MAINTENANT"
    },
    "Email 3CL": {
        "subject": "🃏 Triplez vos jetons + 50 Tours Gratuits !",
        "preheader": "Le Casino Live vous attend avec un bonus massif",
        "greeting": "{{ customer.first_name | default:\"Ami\" | capitalize }}, entrez dans l'action et poussez votre jeu plus loin.",
        "body": "Déposez maintenant avec le code <strong class=\"promocode\">OCCULT200</strong> et obtenez un <strong>bonus de 200% plus 50 Tours Gratuits sur Rich Wilde and the Tome of Madness</strong> par Play'n Go à savourer après les cartes. Votre moment est arrivé - jouons avec style. 🎩 Réclamez le combo :",
        "button": "RÉCLAMER LE BONUS"
    },
    "Email 3CS": {
        "subject": "✨ Voyez grand : 200% Bonus + 50 Tours Gratuits",
        "preheader": "Votre troisième dépôt débloque plus de solde et plus de tours",
        "greeting": "{{ customer.first_name | default:\"Ami\" | capitalize }}, il est temps de passer au niveau supérieur.",
        "body": "Votre troisième dépôt débloque un <strong>bonus de 200% et 50 Tours Gratuits sur Rich Wilde and the Tome of Madness</strong> par Play'n Go. Plus de solde, plus de tours et plus de chances de percer les mystères. Entrez le code <strong class=\"promocode\">OCCULT200</strong>. 📖 Boostez votre solde :",
        "button": "RÉCLAMER LE BONUS"
    },
    "Email 3S": {
        "subject": "🏅 Votre troisième dépôt vient de devenir plus sûr",
        "preheader": "Misez gros, risquez moins - jusqu'à €500 couverts par nous",
        "greeting": "{{ customer.first_name | default:\"Ami\" | capitalize }}, votre série gagnante ne fait que commencer.",
        "body": "Avec votre troisième dépôt, profitez de <strong>20% Paris Sans Risque jusqu'à €500</strong> - pour jouer audacieusement sans regarder en arrière. Votre code - <strong class=\"promocode\">STEADY20</strong>. Un seul pari pourrait suffire. 🏆 Sécurisez votre pari :",
        "button": "PLACEZ VOTRE PARI"
    },
    "Email 4CL": {
        "subject": "🎯 Boost de 170% : Dominez les tables aujourd'hui",
        "preheader": "Votre prochaine main pourrait tout changer avec plus de jetons",
        "greeting": "{{ customer.first_name | default:\"Ami\" | capitalize }}, il est temps de jouer plus gros et plus audacieusement.",
        "body": "Déposez avec le code <strong class=\"promocode\">RISEUP170</strong> et décrochez un <strong>bonus de 170%</strong> pour votre prochaine session au Casino Live. Plus de jetons signifie plus de chances de renverser le jeu en votre faveur. 🔴⚫ Augmentez votre mise :",
        "button": "JOUEZ EN DIRECT"
    },
    "Email 4CS": {
        "subject": "🎰 3 tours, 3 fortunes : Découvrez les gagnants",
        "preheader": "Découvrez les stars des jackpots de la semaine et inspirez-vous",
        "greeting": "{{ customer.first_name | default:\"Ami\" | capitalize }}, la fortune a souri à ces joueurs la semaine dernière :",
        "body": "<strong>💎 a•••76 - €42 510</strong> <strong>💎 fad•••77 - €29 930</strong> <strong>💎 Gg••••h6 - €24 930</strong> Trois tours, trois jackpots. La prochaine série chanceuse sera-t-elle la vôtre ? Tentez votre chance :",
        "button": "JOUEZ MAINTENANT"
    },
    "Email 4S": {
        "subject": "🏅 Jouez sans peur : Votre troisième dépôt est couvert",
        "preheader": "Réclamez 20% Paris Sans Risque jusqu'à €500 aujourd'hui",
        "greeting": "{{ customer.first_name | default:\"Ami\" | capitalize }}, votre troisième dépôt est accompagné d'une confiance supplémentaire.",
        "body": "Obtenez <strong>20% Paris Sans Risque jusqu'à €500</strong> avec le code <strong class=\"promocode\">STEADY20</strong> et faites compter chaque mise. Pas d'hésitation, juste de l'action pure. 🔥 Commencez à parier en sécurité :",
        "button": "COMMENCEZ À PARIER"
    },
    "Email 5CL": {
        "subject": "🏆 Les champions du Casino Live de la semaine",
        "preheader": "3 joueurs. 3 gains massifs. Votre tour ensuite ?",
        "greeting": "{{ customer.first_name | default:\"Ami\" | capitalize }}, voici qui a conquis les tables du Casino Live la semaine dernière :",
        "body": "<strong>🥇 j89••• - €47 250</strong> <strong>🥈 oz•••66z• - €36 180</strong> <strong>🥉 R••••er - €24 940</strong> Vos compétences pourraient faire de vous le prochain grand gagnant - êtes-vous prêt à prendre place ? Défiez le croupier :",
        "button": "JOUEZ EN DIRECT"
    },
    "Email 5CS": {
        "subject": "💎 Votre nom mérite d'être sur la liste des gagnants",
        "preheader": "Découvrez comment nos derniers champions ont gagné gros la semaine dernière",
        "greeting": "{{ customer.first_name | default:\"Ami\" | capitalize }}, le tableau des jackpots s'est illuminé la semaine dernière :",
        "body": "<strong>🔥 ozz - €49 210</strong> <strong>🔥 Dts•• - €30 470</strong> <strong>🔥 e•nz - €25 660</strong> Il suffit d'un tour chanceux - votre moment pourrait être le prochain. 🎰 Tournez pour le jackpot :",
        "button": "TOURNEZ ET GAGNEZ"
    },
    "Email 5S": {
        "subject": "🏟 Les champions sportifs de la semaine dernière",
        "preheader": "Faites votre troisième dépôt et rejoignez la liste des gagnants",
        "greeting": "{{ customer.first_name | default:\"Ami\" | capitalize }}, votre troisième dépôt est accompagné d'une confiance supplémentaire.",
        "body": "<strong>💰 se••••9s - €48 200</strong> <strong>💰 M87•••• - €32 900</strong> <strong>💰 l••••na88 - €26 400</strong> Votre troisième dépôt pourrait être celui qui affiche votre nom ici la semaine prochaine. 🎫 Faites votre coup :",
        "button": "PLACEZ VOTRE PARI"
    },
    "Email 6CL": {
        "subject": "🎩 Boost de 170% pour votre prochaine session",
        "preheader": "Jouez au Casino Live avec plus de puissance sur votre troisième dépôt",
        "greeting": "{{ customer.first_name | default:\"Ami\" | capitalize }}, rendons votre troisième dépôt inoubliable.",
        "body": "Déposez avec le code <strong class=\"promocode\">RISEUP170</strong> et obtenez un <strong>bonus de 170%</strong> pour profiter de sessions plus longues et de mises plus élevées aux tables Live. Votre moment commence maintenant. 🎲 Boostez votre jeu :",
        "button": "RÉCLAMER LE BONUS"
    },
    "Email 6CS": {
        "subject": "🪄 Offre magique : 200% Bonus + 50 TG",
        "preheader": "Plus de solde et plus de tours pour votre troisième dépôt",
        "greeting": "{{ customer.first_name | default:\"Ami\" | capitalize }}, votre troisième dépôt est votre ticket vers plus de sensations.",
        "body": "Obtenez <strong>200% de solde supplémentaire plus 50 Tours Gratuits sur Rich Wilde and the Tome of Madness</strong> par Play'n Go pour continuer à faire tourner les rouleaux. Votre code - <strong class=\"promocode\">OCCULT200</strong>. Chaque tour est une nouvelle chance de décrocher quelque chose de spectaculaire. ✨ Débloquez la magie :",
        "button": "RÉCLAMER LE BONUS"
    },
    "Email 6S": {
        "subject": "🎯 Troisième dépôt ? On vous couvre !",
        "preheader": "Pariez avec 20% Paris Sans Risque jusqu'à €500 maintenant",
        "greeting": "{{ customer.first_name | default:\"Ami\" | capitalize }}, gardez l'élan avec votre troisième dépôt.",
        "body": "Profitez de <strong>20% Paris Sans Risque jusqu'à €500</strong> avec le code <strong class=\"promocode\">STEADY20</strong> et pariez sans arrière-pensée. Un pas de plus vers votre prochain gros gain. 🥅 Réclamez votre couverture :",
        "button": "PARIEZ MAINTENANT"
    },
    "Email 7CL": {
        "subject": "💰 Bonus 170% + 30 Tours Gratuits inclus",
        "preheader": "Passez au niveau supérieur au Casino Live et obtenez des tours bonus",
        "greeting": "{{ customer.first_name | default:\"Ami\" | capitalize }}, voici votre chance de booster votre solde et de profiter de tours bonus ensuite.",
        "body": "Déposez avec le code <strong class=\"promocode\">COWBOY170</strong> et obtenez <strong>170% de jetons supplémentaires + 30 Tours Gratuits sur Wild West Gold</strong> par Pragmatic Play pour un mélange parfait d'excitation Live et de fun aux machines. Les tables vous attendent - serez-vous de la partie ? 🌵 Réclamez vos jetons et tours :",
        "button": "RÉCLAMER LE BONUS"
    },
    "Email 7CS": {
        "subject": "🎲 Bonus amélioré : 170% + 30 Tours Gratuits",
        "preheader": "Votre troisième dépôt est maintenant accompagné d'un boost Wild West",
        "greeting": "{{ customer.first_name | default:\"Ami\" | capitalize }}, votre troisième dépôt est maintenant accompagné d'un badge de shérif :",
        "body": "Obtenez <strong>170% supplémentaires + 30 Tours Gratuits sur Wild West Gold</strong> par Pragmatic Play avec le code <strong class=\"promocode\">COWBOY170</strong>. Les portes du saloon sont ouvertes et les rouleaux vous attendent - êtes-vous prêt à les affronter ? 🤠 En selle pour les gains :",
        "button": "RÉCLAMER LE BONUS"
    },
    "Email 7S": {
        "subject": "🏇 Votre troisième dépôt : Foncez jusqu'au bout",
        "preheader": "20% Paris Sans Risque - sans peur, que de l'adrénaline",
        "greeting": "{{ customer.first_name | default:\"Ami\" | capitalize }}, la course n'est pas encore terminée.",
        "body": "Faites votre troisième dépôt et obtenez <strong>20% Paris Sans Risque jusqu'à €500</strong> avec le code <strong class=\"promocode\">STEADY20</strong>. Que ce soit le football, le tennis ou les courses - votre série gagnante commence maintenant. 🏎️ Démarrez votre moteur :",
        "button": "PLACEZ VOTRE PARI"
    },
    "Email 8CL": {
        "subject": "🎲 Boost de 170% pour dominer le Casino Live",
        "preheader": "Plus de jetons. Plus de chances. Plus de gains sur votre troisième dépôt",
        "greeting": "{{ customer.first_name | default:\"Ami\" | capitalize }}, le troisième dépôt est votre moment de frapper fort.",
        "body": "Déposez avec le code <strong class=\"promocode\">RISEUP170</strong> et obtenez <strong>170% de jetons supplémentaires</strong> pour jouer plus gros, tenir plus longtemps et viser le sommet. Votre place est prête - l'action commence maintenant. 🚀 Rejoignez les grands joueurs :",
        "button": "REJOINDRE LA TABLE"
    },
    "Email 8CS": {
        "subject": "🏺 200% Bonus + 50 TG sur Tome of Madness",
        "preheader": "Entrez dans le tombeau et réclamez vos trésors sur votre troisième dépôt",
        "greeting": "{{ customer.first_name | default:\"Ami\" | capitalize }}, votre prochain tour pourrait révéler des richesses anciennes.",
        "body": "Faites votre troisième dépôt avec le code <strong class=\"promocode\">OCCULT200</strong> et obtenez <strong>200% de bonus + 50 Tours Gratuits sur Rich Wilde and the Tome of Madness</strong> par Play'n Go. Il est temps d'explorer les tombeaux et de réclamer ce qui vous revient. 👁️ Commencez l'aventure :",
        "button": "RÉCLAMER LE BONUS"
    },
    "Email 8S": {
        "subject": "🏆 Jouez malin sur votre troisième dépôt",
        "preheader": "Gagnez sans risque - jusqu'à €500 couverts pour vous",
        "greeting": "{{ customer.first_name | default:\"Ami\" | capitalize }}, faites votre troisième dépôt et entrez dans le jeu en confiance.",
        "body": "Avec <strong>20% Paris Sans Risque jusqu'à €500</strong>, un raté ne vous coûtera rien - mais un gain pourrait être énorme. Votre code - <strong class=\"promocode\">STEADY20</strong>. La façon la plus sûre de vivre l'adrénaline est ici. 🛡️ Réclamez vos paris gratuits :",
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
    print(f"Nutrition #3: {n} fields translated (expected {expected} = {len(TR)} emails x 5 fields)")
