#!/usr/bin/env python3
"""Fix remaining English text in Failed Deposit Flow fr-FR blocks."""
import re

FILE = r"c:\Projects\REPORTS\тексти\Celsius\Failed Deposit Flow - Table data.txt"

with open(FILE, "r", encoding="utf-8") as f:
    lines = f.readlines()

# We know fr-FR rich_text lines: 13, 41, 67, 93, 121 (1-indexed)
FR_LINES = [12, 40, 66, 92, 120]  # 0-indexed

# Replacements per email (applied only to fr-FR rich_text lines)
# Each tuple: (english_text, french_text)
REPLACEMENTS = {
    # Email 1 (line index 12)
    12: [
        (
            "Your recent deposit attempt didn't complete due to a payment issue. Here's what we advice you:",
            "Votre dernière tentative de dépôt n'a pas abouti en raison d'un problème de paiement. Voici ce que nous vous conseillons :"
        ),
        (
            "Use your spouse's card with their permission",
            "Utilisez la carte de votre conjoint(e) avec son autorisation"
        ),
        (
            "If you need help, just reply to this email - we're here to assist right away. If you see a temporary hold on your bank side, it should auto-release per your bank's policy.",
            "Si vous avez besoin d'aide, répondez simplement à cet email — nous sommes là pour vous aider immédiatement. Si vous constatez une retenue temporaire du côté de votre banque, elle devrait être levée automatiquement selon la politique de votre banque."
        ),
    ],
    # Email 2 (line index 40)
    40: [
        (
            "Use your spouse's card with their permission",
            "Utilisez la carte de votre conjoint(e) avec son autorisation"
        ),
        (
            "I'm assigning you a personal manager who will contact you shortly to help you complete the payment. If you need support right now, just reply to this email. If you see a temporary hold on your bank side, it should auto-release per your bank's policy.",
            "Je vous attribue un responsable personnel qui vous contactera sous peu pour vous aider à finaliser le paiement. Si vous avez besoin d'aide maintenant, répondez simplement à cet email. Si vous constatez une retenue temporaire du côté de votre banque, elle devrait être levée automatiquement selon la politique de votre banque."
        ),
    ],
    # Email 3 (line index 66)
    66: [
        (
            "I'm Alex, your personal manager at Celsius Casino Casino. Looks like you have a hard time making the deposit. Let me help you! Please answer this email and I'll help you to sort things out. ",
            "Je suis Alex, votre responsable personnel chez Celsius Casino. On dirait que vous avez des difficultés avec votre dépôt. Laissez-moi vous aider ! Répondez à cet email et je m'occupe de tout. "
        ),
        (
            "If you need help, just reply to this email - I'm here to assist you.",
            "Si vous avez besoin d'aide, répondez simplement à cet email — je suis là pour vous aider."
        ),
    ],
    # Email 4 (line index 92)
    92: [
        (
            "Looks like your deposit didn't complete. Finish it now and we'll add 20 Free Spins on Gates of Olympus as a thank you. ",
            "On dirait que votre dépôt n'a pas abouti. Finalisez-le maintenant et nous ajouterons 20 Tours Gratuits sur Gates of Olympus pour vous remercier. "
        ),
        (
            "Use your spouse's card with their permission",
            "Utilisez la carte de votre conjoint(e) avec son autorisation"
        ),
        (
            "If you need help, just reply to this email - we're here to assist right away. If you see a temporary hold on your bank side, it should auto-release per your bank's policy.",
            "Si vous avez besoin d'aide, répondez simplement à cet email — nous sommes là pour vous aider immédiatement. Si vous constatez une retenue temporaire du côté de votre banque, elle devrait être levée automatiquement selon la politique de votre banque."
        ),
    ],
    # Email 5 (line index 120)
    120: [
        (
            "Alex's here! I just saw you still haven't completed your deposit :( ",
            "C'est Alex ! Je viens de voir que vous n'avez toujours pas finalisé votre dépôt :( "
        ),
        (
            "That's sad! Just let me know how I can help you, I'm always here!",
            "C'est dommage ! Dites-moi comment je peux vous aider, je suis toujours disponible !"
        ),
    ],
}

total = 0
for line_idx, replacements in REPLACEMENTS.items():
    line = lines[line_idx]
    for eng, fra in replacements:
        if eng in line:
            line = line.replace(eng, fra, 1)
            total += 1
            print(f"  OK: replaced '{eng[:50]}...' on line {line_idx+1}")
        else:
            print(f"  MISS: '{eng[:50]}...' NOT FOUND on line {line_idx+1}")
    lines[line_idx] = line

with open(FILE, "w", encoding="utf-8") as f:
    f.writelines(lines)

print(f"\nDone: {total} replacements applied.")
