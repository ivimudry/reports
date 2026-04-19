#!/usr/bin/env python3
"""Translate SU Retention fr-FR blocks from English to French."""
import re, os

FILE = os.path.join(os.path.dirname(__file__), "SU Retention - Table data.txt")

TR = {
    "Email 10C": {
        "subject": "🎰 Plus de 90 000 $ de gains la semaine dernière - Pourquoi pas vous ?",
        "preheader": "Découvrez les derniers gains de vrais joueurs - vous pourriez être le prochain",
        "greeting": " Bonjour, {{customer.first_name | default:\"ami\"}}👋 ",
        "body": "Pendant que vous exploriez, d'autres tournaient - et gagnaient gros : <strong>🔥 Rich••••s a gagné 49 870 $ sur Gates of Olympus</strong> <strong>🔥 Bll• a décroché 27 430 $ sur Fruit Party 2</strong> <strong>🔥 Blu••••86s a remporté 15 980 $ sur Legacy of Dead</strong> Pas d'astuces, pas de codes - juste le bon tour au bon moment. Peut-être que c'est le vôtre ? Tournez pour votre propre gros gain :",
        "button": "TOURNEZ MAINTENANT"
    },
    "Email 10M": {
        "subject": "🎁 160% + 90 TG ou 25% Paris Gratuits : Décidez maintenant",
        "preheader": "Les deux offres sont toujours ouvertes - lancez votre aventure ou placez votre pari",
        "greeting": " Bonjour, {{customer.first_name | default:\"ami\"}}👋 ",
        "body": "Vous hésitez encore ? Que vous soyez fan de rouleaux ou de cotes en direct, nous avons quelque chose pour vous : • Utilisez le code <strong class=\"promocode\">MADNESS16090</strong> pour un <strong>Bonus de 160% + 90 Tours Gratuits sur Rich Wilde and the Tome of Madness</strong> au casino. 🐙 • Utilisez le code <strong class=\"promocode\">SECURE25</strong> pour un <strong>25% Pari Sans Risque</strong> sur votre premier pari sportif. Deux offres, une décision - choisissez votre camp et faites que ce premier pas compte. Activez votre bonus :",
        "button": "RÉCLAMER MON BONUS"
    },
    "Email 10S": {
        "subject": "🏆 En attente : 15% Paris Sans Risque",
        "preheader": "Vous nous avez rejoints - faites votre premier pas avec 15% de Paris Gratuits sur votre premier dépôt",
        "greeting": " Bonjour, {{customer.first_name | default:\"ami\"}}👋 ",
        "body": "Vous vous êtes inscrit, vous avez découvert la plateforme - il est temps de passer à l'action. Faites votre premier dépôt avec le code <strong class=\"promocode\">EARNNRF15X</strong> et nous vous soutiendrons avec un <strong>15% Bonus Paris Sans Risque</strong>. Si ça ne tourne pas en votre faveur, nous vous couvrons quand même. 🥊 Placez votre pari gagnant :",
        "button": "RÉCLAMER MON BONUS"
    },
    "Email 1C": {
        "subject": "🎁 100% Bonus + 150 TG en attente : Saisissez-les !",
        "preheader": "Votre bonus de bienvenue est toujours là - faites votre premier dépôt aujourd'hui",
        "greeting": " Bonjour, {{customer.first_name | default:\"ami\"}}👋 ",
        "body": "Vous avez exploré Celsius, maintenant il est temps de passer aux choses sérieuses.&nbsp; Faites votre premier dépôt et obtenez un <strong>Bonus de 100% plus 150 Tours Gratuits sur Razor Shark</strong> par Push Gaming avec le code <strong class=\"promocode\">FINTASTIC150</strong>. Votre pack de bienvenue est toujours actif et n'attend que vous. Ne le laissez pas filer ! 🚀 Activez vos récompenses :",
        "button": "RÉCLAMER MON BONUS"
    },
    "Email 1M": {
        "subject": "🎁 Obtenez 100% Bonus + 150 TG + 15% Paris Gratuits !",
        "preheader": "Faites votre premier dépôt et profitez de tours au casino et de Paris Sans Risque",
        "greeting": " Bonjour, {{customer.first_name | default:\"ami\"}}👋 ",
        "body": "Pas sûr de par où commencer - casino ou sport ? Pas besoin de choisir. Votre premier dépôt débloque un <strong>Bonus de 100% + 150 Tours Gratuits sur Razor Shark</strong> par Push Gaming pour le casino avec le code <strong class=\"promocode\">FINTASTIC150</strong>, ET un <strong>15% Pari Sans Risque</strong> pour les paris sportifs avec le code <strong class=\"promocode\">EARNNRF15X</strong>. Plongez dans les gains ou pariez sur votre équipe favorite - vous êtes couvert dès le premier geste. 🦈 Réclamez le pack complet :",
        "button": "RÉCLAMER MON BONUS"
    },
    "Email 1S": {
        "subject": "🏆 15% Paris Sans Risque : Votre filet de sécurité est prêt",
        "preheader": "Vous nous avez rejoints - faites votre premier pas avec 15% de Paris Gratuits sur votre premier dépôt",
        "greeting": " Bonjour, {{customer.first_name | default:\"ami\"}}👋 ",
        "body": "Vous vous êtes inscrit et avez découvert la plateforme - il est temps de quitter le banc de touche et d'entrer dans le jeu. Faites votre premier dépôt avec le code <strong class=\"promocode\">EARNNRF15X</strong> et nous vous soutiendrons avec un <strong>15% Bonus Paris Sans Risque</strong>. Si ça ne tourne pas en votre faveur, nous assurons vos arrières. 🤝 Lancez l'action :",
        "button": "RÉCLAMER MON BONUS"
    },
    "Email 2C": {
        "subject": "🎰 Réclamez votre 100% Bonus + 150 TG aujourd'hui",
        "preheader": "Faites votre premier dépôt maintenant et réclamez votre pack de bienvenue tant qu'il est actif",
        "greeting": " Bonjour, {{customer.first_name | default:\"ami\"}}👋 ",
        "body": "Votre bonus de bienvenue Celsius est toujours réservé pour vous :&nbsp; <strong>Bonus de 100% et 150 Tours Gratuits sur Razor Shark</strong> par Push Gaming sur votre premier dépôt avec le code <strong class=\"promocode\">FINTASTIC150</strong>. Si vous êtes prêt à jouer pour de vrai - c'est le moment idéal de frapper fort. 🃏 Cliquez pour réclamer votre pack :",
        "button": "RÉCLAMER MON BONUS"
    },
    "Email 2M": {
        "subject": "🎮 100% Bonus + 150 TG + 4% Cashback : Tout est à vous",
        "preheader": "Le premier dépôt vous offre des tours, un bonus et du Cashback - tout en un",
        "greeting": " Bonjour, {{customer.first_name | default:\"ami\"}}👋 ",
        "body": "Vous hésitez entre casino et sport ? Pourquoi pas les deux ? Faites votre premier dépôt et obtenez : <strong>Bonus de 100% + 150 Tours Gratuits</strong> sur <strong>Razor Shark</strong> avec le code <strong class=\"promocode\">FINTASTIC150</strong> <strong>4% Cashback</strong> sur vos paris sportifs avec le code <strong class=\"promocode\">CASHPLUS4</strong>. Un seul dépôt débloque les deux côtés du jeu - et vous donne la flexibilité de jouer à votre façon. 🎲 Débloquez les deux bonus :",
        "button": "RÉCLAMER MON BONUS"
    },
    "Email 2S": {
        "subject": "🔁 Réclamez votre 4% Cashback Sport aujourd'hui",
        "preheader": "Récupérez 4% sur vos paris sportifs dès votre premier dépôt",
        "greeting": " Bonjour, {{customer.first_name | default:\"ami\"}}👋 ",
        "body": "Vous avez déjà récupéré votre bonus sport - il est temps de passer à l'action. Utilisez le code <strong class=\"promocode\">CASHPLUS4</strong> sur votre dépôt et activez votre <strong>4% Cashback sur tous vos paris sportifs</strong>. Gagnant ou perdant, une partie de l'action vous revient. 💸 Sécurisez votre cashback :",
        "button": "RÉCLAMER MON BONUS"
    },
    "Email 3C": {
        "subject": "💥 Votre Bonus de 140% est prêt",
        "preheader": "Ne manquez pas votre chance de démarrer fort - votre boost est actif",
        "greeting": " Bonjour, {{customer.first_name | default:\"ami\"}}👋 ",
        "body": "Vous avez rejoint et exploré, maintenant il est temps de monter d'un cran. 🆙 Faites votre premier dépôt et obtenez un <strong>Bonus de 140%</strong> - le boost de bienvenue conçu pour bien lancer votre aventure Celsius. Utilisez le code : <strong class=\"promocode\">POWER140</strong> Boostez votre solde :",
        "button": "RÉCLAMER MON BONUS"
    },
    "Email 3M": {
        "subject": "🎯 140% Bonus Casino ou 15% Paris Gratuits : À vous de choisir",
        "preheader": "Utilisez votre code pour choisir entre casino ou sport - votre premier dépôt ouvre les deux voies",
        "greeting": " Bonjour, {{customer.first_name | default:\"ami\"}}👋 ",
        "body": "Que vous soyez fan de rouleaux ou de cotes en temps réel - votre premier dépôt vous offre un départ sur mesure : • Utilisez le code <strong class=\"promocode\">POWER140</strong> pour un <strong>Bonus de 140%</strong> au casino • Utilisez le code <strong class=\"promocode\">EARNNRF15X</strong> pour un <strong>15% Pari Sans Risque</strong> au sport C'est votre choix de départ - dans tous les cas, vous bénéficiez d'un vrai boost dès le premier geste. 🚀 Sélectionnez votre voie gagnante :",
        "button": "RÉCLAMER MON BONUS"
    },
    "Email 3S": {
        "subject": "🏆 Votre 15% Pari Sans Risque vous attend",
        "preheader": "Débloquez votre filet de sécurité sur votre premier dépôt et pariez en confiance",
        "greeting": " Bonjour, {{customer.first_name | default:\"ami\"}}👋 ",
        "body": "Vous avez réclamé votre bonus sport - il est temps de le mettre en jeu. Utilisez le code <strong class=\"promocode\">EARNNRF15X</strong> sur votre premier dépôt et débloquez un <strong>15% Pari Sans Risque</strong>. Placez votre premier pari en confiance - nous assurons vos arrières si le score ne tourne pas en votre faveur. 🛡️ Récupérez votre pari gratuit :",
        "button": "RÉCLAMER MON BONUS"
    },
    "Email 4C": {
        "subject": "🍭 130% Bonus + 70 TG sur Sweet Bonanza",
        "preheader": "Votre premier dépôt débloque un bonus savoureux - prêt quand vous l'êtes",
        "greeting": " Bonjour, {{customer.first_name | default:\"ami\"}}👋 ",
        "body": "Vous y êtes presque. Votre offre de bienvenue Celsius est savoureuse ! 🍬 Obtenez un <strong>Bonus de 130% + 70 Tours Gratuits sur Sweet Bonanza</strong>. Elle est toujours active et attend votre premier dépôt. Ne manquez pas ce départ gourmand. Utilisez le code : <strong class=\"promocode\">CANDYDROP70</strong> Régalez-vous :",
        "button": "RÉCLAMER MON BONUS"
    },
    "Email 4M": {
        "subject": "🍭 130% + 70 TG sur Sweet Bonanza - Ou Sport ?",
        "preheader": "Commencez avec un boost casino savoureux ou choisissez votre voie au sport",
        "greeting": " Bonjour, {{customer.first_name | default:\"ami\"}}👋 ",
        "body": "Vous n'avez pas encore fait votre premier dépôt - mais quand vous le ferez, vous aurez le choix. • <strong>Envie de tourner ?</strong> Utilisez le code <strong class=\"promocode\">CANDYDROP70</strong> et obtenez un <strong>Bonus de 130% + 70 Tours Gratuits sur Sweet Bonanza</strong>. 🍬 • <strong>Vous préférez parier ?</strong> Rendez-vous au sportsbook et choisissez votre promo quand vous serez prêt. Casino ou sport - commencez votre aventure là où ça vous convient. Choisissez votre offre :",
        "button": "RÉCLAMER MON BONUS"
    },
    "Email 4S": {
        "subject": "🔄 4% Cashback sur chaque pari : Actif maintenant",
        "preheader": "Votre premier dépôt débloque 4% de retour sur toute l'action sportive",
        "greeting": " Bonjour, {{customer.first_name | default:\"ami\"}}👋 ",
        "body": "Vous avez déjà récupéré votre bonus - il est temps de le mettre en jeu. Utilisez le code <strong class=\"promocode\">CASHPLUS4</strong> sur votre premier dépôt et activez le <strong>4% Cashback sur tous vos paris sportifs</strong>. Plus d'action, moins de risque - chaque pari rapporte. ⚽ Revenez dans le jeu :",
        "button": "RÉCLAMER MON BONUS"
    },
    "Email 5C": {
        "subject": "🎯 Bonus de 140% sur le 1er dépôt : L'offre s'achève bientôt ?",
        "preheader": "Votre boost de bienvenue est toujours actif - bonus de 140% sur votre premier dépôt",
        "greeting": " Bonjour, {{customer.first_name | default:\"ami\"}}👋 ",
        "body": "Vous avez franchi les premières étapes - il est temps de jouer pour de vrai. Faites votre premier dépôt et récupérez un <strong>Bonus de 140%</strong> pour bien démarrer.&nbsp; L'offre est prête - et vous ? 🎱 Utilisez le code : <strong class=\"promocode\">POWER140</strong> Lancez votre série gagnante :",
        "button": "RÉCLAMER MON BONUS"
    },
    "Email 5M": {
        "subject": "🎯 140% Bonus Casino ou 15% Paris Gratuits ?",
        "preheader": "Choisissez le départ qui correspond à votre jeu : boost casino ou filet de sécurité sport",
        "greeting": " Bonjour, {{customer.first_name | default:\"ami\"}}👋 ",
        "body": "Vous n'êtes qu'à un pas de tout lancer - et c'est vous qui choisissez comment commencer : • <strong>Vous préférez les rouleaux ?</strong> Utilisez le code <strong class=\"promocode\">POWER140</strong> pour un <strong>Bonus Casino de 140%</strong> sur votre premier dépôt. • <strong>Fan de sport ?</strong> Utilisez le code <strong class=\"promocode\">EARNNRF15X</strong> pour activer un <strong>15% Pari Sans Risque</strong>. Votre bonus de bienvenue est prêt - il ne reste plus qu'à faire votre premier geste. ⚖️ Réclamez votre bonus préféré :",
        "button": "RÉCLAMER MON BONUS"
    },
    "Email 5S": {
        "subject": "🛡️ Protégez vos paris : 15% Pari Sans Risque",
        "preheader": "Commencez à parier l'esprit tranquille sur votre premier dépôt",
        "greeting": " Bonjour, {{customer.first_name | default:\"ami\"}}👋 ",
        "body": "Vous avez sécurisé votre bonus sport - passez à l'étape suivante. Utilisez le code <strong class=\"promocode\">EARNNRF15X</strong> sur votre premier dépôt et débloquez un <strong>15% Pari Sans Risque</strong>. Que votre premier pari gagne ou non, vous êtes protégé dans les deux cas. 🥅 Jouez avec un filet de sécurité :",
        "button": "RÉCLAMER MON BONUS"
    },
    "Email 6C": {
        "subject": "💸 Plus de 100 000 $ gagnés la semaine dernière - Vous en êtes ?",
        "preheader": "De vrais joueurs, de vrais gains - découvrez les meilleurs résultats de la semaine",
        "greeting": " Bonjour, {{customer.first_name | default:\"ami\"}}👋 ",
        "body": "De grandes choses se sont passées la semaine dernière sur les rouleaux - et en voici la preuve : <strong>🏆 rik••••64 a gagné 46 870 $ sur Gates of Olympus</strong> <strong>🏆 m••••n a décroché 36 240 $ sur Sugar Rush</strong> <strong>🏆 t•••y a remporté 32 905 $ sur Wanted Dead or a Wild</strong> Ces gains étaient réels. Les joueurs étaient réels. Et votre chance ? Elle n'est qu'à un tour. Rejoignez le cercle des gagnants :",
        "button": "REJOIGNEZ-NOUS"
    },
    "Email 6M": {
        "subject": "🎯 140% Bonus Casino ou 15% Paris Gratuits ?",
        "preheader": "Choisissez le départ qui correspond à votre jeu : boost casino ou filet de sécurité sport",
        "greeting": " Bonjour, {{customer.first_name | default:\"ami\"}}👋 ",
        "body": "Vous n'êtes qu'à un pas de tout lancer - et c'est vous qui choisissez comment commencer : • <strong>Vous préférez les rouleaux ?</strong> Utilisez le code <strong class=\"promocode\">POWER140</strong> pour un <strong>Bonus Casino de 140%</strong> sur votre premier dépôt.•&nbsp; <strong>Fan de sport ?</strong> Utilisez le code <strong class=\"promocode\">EARNNRF15X</strong> pour activer un <strong>15% Pari Sans Risque</strong>. Votre bonus de bienvenue est prêt - il ne reste plus qu'à faire votre premier geste. ⚖️ Réclamez votre bonus préféré :",
        "button": "RÉCLAMER MON BONUS"
    },
    "Email 6S": {
        "subject": "🛡️ Protégez vos paris : 15% Pari Sans Risque",
        "preheader": "Commencez à parier l'esprit tranquille sur votre premier dépôt",
        "greeting": " Bonjour, {{customer.first_name | default:\"ami\"}}👋 ",
        "body": "Vous avez sécurisé votre bonus sport - passez à l'étape suivante. Utilisez le code <strong class=\"promocode\">EARNNRF15X</strong> sur votre premier dépôt et débloquez un <strong>15% Pari Sans Risque</strong>. Que votre premier pari gagne ou non, vous êtes protégé dans les deux cas. 🥅 Jouez avec un filet de sécurité :",
        "button": "RÉCLAMER MON BONUS"
    },
    "Email 7C": {
        "subject": "🎁 140% Bonus + 80 TG sur Chaos Crew II",
        "preheader": "Débloquez votre pack de bienvenue et déchaînez le chaos sur votre premier dépôt",
        "greeting": " Bonjour, {{customer.first_name | default:\"ami\"}}👋 ",
        "body": "Vous nous avez déjà rejoints - il est temps de commencer à gagner. Faites votre premier dépôt et utilisez le code <strong class=\"promocode\">CHAOSCTRL80</strong> pour obtenir un <strong>Bonus de 140% plus 80 Tours Gratuits sur Chaos Crew II</strong>. C'est le moment parfait pour plonger et jouer avec un vrai avantage. 🤘 Déchaînez le chaos :",
        "button": "RÉCLAMER MON BONUS"
    },
    "Email 7M": {
        "subject": "🎁 140% + 80 TG ou 20% Paris Gratuits : Votre choix",
        "preheader": "Deux façons de démarrer sur votre premier dépôt - déchaînez le chaos ou pariez en sécurité",
        "greeting": " Bonjour, {{customer.first_name | default:\"ami\"}}👋 ",
        "body": "Votre voie de bienvenue est toujours ouverte - et vous pouvez la prendre dans la direction qui vous convient : • <strong>Envie de commencer par les machines ?</strong> Utilisez le code <strong class=\"promocode\">CHAOSCTRL80</strong> et obtenez un <strong>Bonus de 140% + 80 Tours Gratuits sur Chaos Crew II</strong>. 💀•&nbsp; <strong>Vous préférez parier ?</strong> Utilisez le code <strong class=\"promocode\">WIN20NRF</strong> pour réclamer un <strong>20% Pari Sans Risque</strong> sur votre premier dépôt. Un seul geste suffit pour débloquer l'une ou l'autre offre - le choix est le vôtre. Démarrez votre aventure :",
        "button": "RÉCLAMER MON BONUS"
    },
    "Email 7S": {
        "subject": "🏁 Démarrez fort : 20% Pari Sans Risque prêt",
        "preheader": "Activez votre filet de sécurité sur votre premier dépôt aujourd'hui",
        "greeting": " Bonjour, {{customer.first_name | default:\"ami\"}}👋 ",
        "body": "Vous avez le bonus - c'est le moment de tirer. 🏀 Faites votre premier dépôt avec le code <strong class=\"promocode\">WIN20NRF</strong> et activez un <strong>20% Pari Sans Risque</strong>. C'est la façon la plus simple d'entrer dans le jeu en toute confiance. Débloquez votre protection de 20% :",
        "button": "RÉCLAMER MON BONUS"
    },
    "Email 8C": {
        "subject": "💥 Les jackpots continuent de tomber - Serez-vous le prochain ?",
        "preheader": "Découvrez ce que les joueurs ont gagné la semaine dernière - de vrais tours, de vrais gains",
        "greeting": " Bonjour, {{customer.first_name | default:\"ami\"}}👋 ",
        "body": "Vous avez vu ce que Celsius propose - voici ce qui s'est passé la semaine dernière : <strong>💰 H••H55 a gagné 44 190 $ sur The Dog House Megaways</strong> <strong>💰 y•••54 a décroché 28 670 $ sur Sweet Bonanza</strong> <strong>💰 Da••••K33d a remporté 13 520 $ sur Book of Dead</strong> Ce sont de vrais gains de vrais joueurs.&nbsp; Il ne manque plus que votre premier tour. 🎰 Tentez votre chance au jackpot :",
        "button": "JOUEZ MAINTENANT"
    },
    "Email 8M": {
        "subject": "🎁 140% + 80 TG ou 20% Paris Gratuits : Votre choix",
        "preheader": "Deux façons de démarrer sur votre premier dépôt - déchaînez le chaos ou pariez en sécurité",
        "greeting": " Bonjour, {{customer.first_name | default:\"ami\"}}👋 ",
        "body": "Votre voie de bienvenue est toujours ouverte - et vous pouvez la prendre dans la direction qui vous convient : • <strong>Envie de commencer par les machines ?</strong> Utilisez le code <strong class=\"promocode\">CHAOSCTRL80</strong> et obtenez un <strong>Bonus de 140% + 80 Tours Gratuits sur Chaos Crew II</strong>. 💀•&nbsp; <strong>Vous préférez parier ?</strong> Utilisez le code <strong class=\"promocode\">WIN20NRF</strong> pour réclamer un <strong>20% Pari Sans Risque</strong> sur votre premier dépôt. Un seul geste suffit pour débloquer l'une ou l'autre offre - le choix est le vôtre. Démarrez votre aventure :",
        "button": "RÉCLAMER MON BONUS"
    },
    "Email 8S": {
        "subject": "🏁 Démarrez fort : 20% Pari Sans Risque prêt",
        "preheader": "Activez votre filet de sécurité sur votre premier dépôt aujourd'hui",
        "greeting": " Bonjour, {{customer.first_name | default:\"ami\"}}👋 ",
        "body": "Vous avez le bonus - c'est le moment de tirer. 🏀 Faites votre premier dépôt avec le code <strong class=\"promocode\">WIN20NRF</strong> et activez un <strong>20% Pari Sans Risque</strong>. C'est la façon la plus simple d'entrer dans le jeu en toute confiance. Débloquez votre protection de 20% :",
        "button": "RÉCLAMER MON BONUS"
    },
    "Email 9C": {
        "subject": "🎁 160% Bonus + 90 TG sur Tome of Madness",
        "preheader": "Utilisez votre code sur votre premier dépôt et démarrez avec un vrai boost",
        "greeting": " Bonjour, {{customer.first_name | default:\"ami\"}}👋 ",
        "body": "Vous n'êtes qu'à un pas de débloquer l'intégralité de votre bonus de bienvenue. Utilisez le code <strong class=\"promocode\">MADNESS16090</strong> sur votre premier dépôt pour découvrir un <strong>Bonus de 160% plus 90 Tours Gratuits sur Rich Wilde and the Tome of Madness</strong>. Les rouleaux vous attendent - et votre moment commence maintenant. 👁️ Ouvrez le livre des gains :",
        "button": "RÉCLAMER MON BONUS"
    },
    "Email 9M": {
        "subject": "🎁 160% + 90 TG ou 25% Paris Gratuits : Décidez maintenant",
        "preheader": "Les deux offres sont toujours ouvertes - lancez votre aventure ou placez votre pari",
        "greeting": " Bonjour, {{customer.first_name | default:\"ami\"}}👋 ",
        "body": "Vous hésitez encore ? Que vous soyez fan de rouleaux ou de cotes en direct, nous avons quelque chose pour vous : • Utilisez le code <strong class=\"promocode\">MADNESS16090</strong> pour un <strong>Bonus de 160% + 90 Tours Gratuits sur Rich Wilde and the Tome of Madness</strong> au casino. 🐙 • Utilisez le code <strong class=\"promocode\">SECURE25</strong> pour un <strong>25% Pari Sans Risque</strong> sur votre premier pari sportif. Deux offres, une décision - choisissez votre camp et faites que ce premier pas compte. Activez votre bonus :",
        "button": "RÉCLAMER MON BONUS"
    },
    "Email 9S": {
        "subject": "🏆 25% Pari Sans Risque : Ne ratez pas ça !",
        "preheader": "Commencez à parier en confiance sur votre premier dépôt",
        "greeting": " Bonjour, {{customer.first_name | default:\"ami\"}}👋 ",
        "body": "Vous avez déjà réclamé votre bonus sport - il est temps de l'utiliser. Faites votre premier dépôt avec le code <strong class=\"promocode\">SECURE25</strong> et activez un <strong>25% Pari Sans Risque</strong>. Si votre premier pari ne passe pas, nous vous en rendrons une partie. Pas de pression - jouez simplement. 🏟️ Réclamez votre départ sans risque :",
        "button": "RÉCLAMER MON BONUS"
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
    print(f"SU Retention: {n} fields translated (expected {expected} = {len(TR)} emails x 5 fields)")
