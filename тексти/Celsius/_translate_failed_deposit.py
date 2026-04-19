#!/usr/bin/env python3
"""Translate Failed Deposit Flow fr-FR blocks from English to French."""
import re, os

FILE = os.path.join(os.path.dirname(__file__), "Failed Deposit Flow - Table data.txt")

# For each email, define: subject, preheader (if exists), and rich_text replacements (old→new pairs)
TR = {
    "Email 1": {
        "subject": "😟 On dirait qu'il y a eu un problème",
        "preheader": "Nous sommes là pour vous aider",
        "rich_text_replacements": [
            ("Hi {first_name},", "Bonjour {first_name},"),
            ("Your recent deposit attempt didn't complete due to a payment issue. Here's what we advice you:", "Votre tentative de dépôt récente n'a pas abouti en raison d'un problème de paiement. Voici ce que nous vous conseillons :"),
            ("Try a different card or payment network", "Essayez une autre carte ou un autre réseau de paiement"),
            ("Use your spouse's card with their permission", "Utilisez la carte de votre conjoint(e) avec son autorisation"),
            ("Deposit with cryptocurrency in the Cashier", "Déposez avec des cryptomonnaies dans la Caisse"),
            (">Complete deposit</a>", ">Finaliser le dépôt</a>"),
            ("If you need help, just reply to this email - we're here to assist right away. If you see a temporary hold on your bank side, it should auto-release per your bank's policy.", "Si vous avez besoin d'aide, répondez simplement à cet email - nous sommes là pour vous assister immédiatement. Si vous voyez une retenue temporaire côté banque, elle devrait être levée automatiquement selon la politique de votre banque."),
            (">Thanks,<", ">Merci,<"),
            (">Celsius Casino Support<", ">Assistance Celsius Casino<"),
        ]
    },
    "Email 2": {
        "subject": "🔴 Toujours des difficultés avec votre dépôt ?",
        "preheader": "Besoin d'aide ? Votre responsable personnel est en route",
        "rich_text_replacements": [
            ("Hi {first_name},", "Bonjour {first_name},"),
            ("I can see your deposit still did not go through. Do you need help finishing it? Quick options:", "Je constate que votre dépôt n'est toujours pas passé. Vous avez besoin d'aide pour le finaliser ? Options rapides :"),
            ("Try a different card or payment network", "Essayez une autre carte ou un autre réseau de paiement"),
            ("Use your spouse's card with their permission", "Utilisez la carte de votre conjoint(e) avec son autorisation"),
            ("Deposit with cryptocurrency in the Cashier", "Déposez avec des cryptomonnaies dans la Caisse"),
            (">Complete deposit</a>", ">Finaliser le dépôt</a>"),
            ("I'm assigning you a personal manager who will contact you shortly to help you complete the payment. If you need support right now, just reply to this email. If you see a temporary hold on your bank side, it should auto-release per your bank's policy.", "Je vous attribue un responsable personnel qui vous contactera sous peu pour vous aider à finaliser le paiement. Si vous avez besoin d'assistance maintenant, répondez simplement à cet email. Si vous voyez une retenue temporaire côté banque, elle devrait être levée automatiquement selon la politique de votre banque."),
            (">Thanks,<", ">Merci,<"),
            (">Celsius Casino Support<", ">Assistance Celsius Casino<"),
        ]
    },
    "Email 3": {
        "subject": "RE: Dépôt non abouti",
        "rich_text_replacements": [
            ("Nice to meet you, {first_name},", "Enchanté, {first_name},"),
            ("I'm Alex, your personal manager at Celsius Casino Casino. Looks like you have a hard time making the deposit. Let me help you! Please answer this email and I'll help you to sort things out. ", "Je suis Alex, votre responsable personnel chez Celsius Casino. Il semble que vous ayez des difficultés à effectuer votre dépôt. Laissez-moi vous aider ! Répondez à cet email et je vous aiderai à résoudre le problème. "),
            (">Complete deposit</a>", ">Finaliser le dépôt</a>"),
            ("If you need help, just reply to this email - I'm here to assist you.", "Si vous avez besoin d'aide, répondez simplement à cet email - je suis là pour vous assister."),
            (">Thanks,<", ">Merci,<"),
            (">Alex from Celsius Casino<", ">Alex de Celsius Casino<"),
        ]
    },
    "Email 4": {
        "subject": "🤗 On vous adore !",
        "preheader": "Recevez 20 TG sur votre dépôt !",
        "rich_text_replacements": [
            ("Hi {first_name},", "Bonjour {first_name},"),
            ("Looks like your deposit didn't complete. Finish it now and we'll add 20 Free Spins on Gates of Olympus as a thank you. ", "Il semble que votre dépôt n'a pas abouti. Finalisez-le maintenant et nous ajouterons 20 Tours Gratuits sur Gates of Olympus pour vous remercier. "),
            ("Quick ways to complete:", "Moyens rapides pour finaliser :"),
            ("Try a different card or payment network", "Essayez une autre carte ou un autre réseau de paiement"),
            ("Use your spouse's card with their permission", "Utilisez la carte de votre conjoint(e) avec son autorisation"),
            ("Deposit with cryptocurrency in the Cashier", "Déposez avec des cryptomonnaies dans la Caisse"),
            (">Complete deposit</a>", ">Finaliser le dépôt</a>"),
            ("If you need help, just reply to this email - we're here to assist right away. If you see a temporary hold on your bank side, it should auto-release per your bank's policy.", "Si vous avez besoin d'aide, répondez simplement à cet email - nous sommes là pour vous assister immédiatement. Si vous voyez une retenue temporaire côté banque, elle devrait être levée automatiquement selon la politique de votre banque."),
            (">Thanks,<", ">Merci,<"),
            (">Celsius Casino Support<", ">Assistance Celsius Casino<"),
        ]
    },
    "Email 5": {
        "subject": "RE: Besoin d'aide",
        "preheader": "Comment ça se passe ?",
        "rich_text_replacements": [
            ("Hi {first_name},", "Bonjour {first_name},"),
            ("Alex's here! I just saw you still haven't completed your deposit :( ", "C'est Alex ! Je viens de voir que vous n'avez toujours pas finalisé votre dépôt :( "),
            ("That's sad! Just let me know how I can help you, I'm always here!", "C'est dommage ! Dites-moi comment je peux vous aider, je suis toujours disponible !"),
            ("Try again: [", "Réessayez : ["),
            (">Complete deposit</a>", ">Finaliser le dépôt</a>"),
            ("If you need help, just reply to this email!", "Si vous avez besoin d'aide, répondez simplement à cet email !"),
            (">Thanks,<", ">Merci,<"),
            (">Alex from Celsius Casino<", ">Alex de Celsius Casino<"),
        ]
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

            if stripped.startswith("subject: ") and "subject" in tr:
                new_lines.append(f"subject: {tr['subject']}\n")
                changed += 1
                continue

            if stripped.startswith("preheader: ") and "preheader" in tr:
                new_lines.append(f"preheader: {tr['preheader']}\n")
                changed += 1
                continue

            if stripped.startswith("rich_text: "):
                new_val = stripped
                rt_changes = 0
                for old_text, new_text in tr["rich_text_replacements"]:
                    if old_text in new_val:
                        new_val = new_val.replace(old_text, new_text, 1)
                        rt_changes += 1
                new_lines.append(new_val + "\n")
                changed += 1
                print(f"  {current_name}: {rt_changes}/{len(tr['rich_text_replacements'])} rich_text replacements applied")
                continue

        new_lines.append(line)

    with open(filepath, "w", encoding="utf-8") as f:
        f.writelines(new_lines)

    return changed


if __name__ == "__main__":
    n = apply_translations(FILE, TR)
    print(f"\nFailed Deposit Flow: {n} fields translated across {len(TR)} emails")
