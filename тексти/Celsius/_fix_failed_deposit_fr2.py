#!/usr/bin/env python3
"""Fix remaining English text in Failed Deposit Flow fr-FR blocks.
   Uses smart quotes (U+2019) to match actual file content."""
FILE = r"c:\Projects\REPORTS\тексти\Celsius\Failed Deposit Flow - Table data.txt"

with open(FILE, "r", encoding="utf-8") as f:
    lines = f.readlines()

# Smart quote
Q = "\u2019"

REPLACEMENTS = {
    # Email 1 fr-FR (line 12, 0-indexed)
    12: [
        (
            f"Your recent deposit attempt didn{Q}t complete due to a payment issue. Here{Q}s what we advice you:",
            "Votre derni\u00e8re tentative de d\u00e9p\u00f4t n\u2019a pas abouti en raison d\u2019un probl\u00e8me de paiement. Voici ce que nous vous conseillons :"
        ),
        (
            f"Use your spouse{Q}s card with their permission",
            "Utilisez la carte de votre conjoint(e) avec son autorisation"
        ),
        (
            f"If you need help, just reply to this email - we{Q}re here to assist right away. If you see a temporary hold on your bank side, it should auto-release per your bank{Q}s policy.",
            "Si vous avez besoin d\u2019aide, r\u00e9pondez simplement \u00e0 cet email \u2014 nous sommes l\u00e0 pour vous aider imm\u00e9diatement. Si vous constatez une retenue temporaire du c\u00f4t\u00e9 de votre banque, elle devrait \u00eatre lev\u00e9e automatiquement selon la politique de votre banque."
        ),
    ],
    # Email 2 fr-FR (line 40)
    40: [
        (
            f"Use your spouse{Q}s card with their permission",
            "Utilisez la carte de votre conjoint(e) avec son autorisation"
        ),
        (
            f"I{Q}m assigning you a personal manager who will contact you shortly to help you complete the payment. If you need support right now, just reply to this email. If you see a temporary hold on your bank side, it should auto-release per your bank{Q}s policy.",
            "Je vous attribue un responsable personnel qui vous contactera sous peu pour vous aider \u00e0 finaliser le paiement. Si vous avez besoin d\u2019aide maintenant, r\u00e9pondez simplement \u00e0 cet email. Si vous constatez une retenue temporaire du c\u00f4t\u00e9 de votre banque, elle devrait \u00eatre lev\u00e9e automatiquement selon la politique de votre banque."
        ),
    ],
    # Email 3 fr-FR (line 66)
    66: [
        (
            f"I{Q}m Alex, your personal manager at Celsius Casino Casino. Looks like you have a hard time making the deposit. Let me help you! Please answer this email and I{Q}ll help you to sort things out. ",
            "Je suis Alex, votre responsable personnel chez Celsius Casino. On dirait que vous avez des difficult\u00e9s avec votre d\u00e9p\u00f4t. Laissez-moi vous aider ! R\u00e9pondez \u00e0 cet email et je m\u2019occupe de tout. "
        ),
        (
            f"If you need help, just reply to this email - I{Q}m here to assist you.",
            "Si vous avez besoin d\u2019aide, r\u00e9pondez simplement \u00e0 cet email \u2014 je suis l\u00e0 pour vous aider."
        ),
    ],
    # Email 4 fr-FR (line 92)
    92: [
        (
            f"Looks like your deposit didn{Q}t complete. Finish it now and we{Q}ll add 20 Free Spins on Gates of Olympus as a thank you. ",
            "On dirait que votre d\u00e9p\u00f4t n\u2019a pas abouti. Finalisez-le maintenant et nous ajouterons 20 Tours Gratuits sur Gates of Olympus pour vous remercier. "
        ),
        (
            f"Use your spouse{Q}s card with their permission",
            "Utilisez la carte de votre conjoint(e) avec son autorisation"
        ),
        (
            f"If you need help, just reply to this email - we{Q}re here to assist right away. If you see a temporary hold on your bank side, it should auto-release per your bank{Q}s policy.",
            "Si vous avez besoin d\u2019aide, r\u00e9pondez simplement \u00e0 cet email \u2014 nous sommes l\u00e0 pour vous aider imm\u00e9diatement. Si vous constatez une retenue temporaire du c\u00f4t\u00e9 de votre banque, elle devrait \u00eatre lev\u00e9e automatiquement selon la politique de votre banque."
        ),
    ],
    # Email 5 fr-FR (line 120)
    120: [
        (
            f"Alex{Q}s here! I just saw you still haven{Q}t completed your deposit :( ",
            "C\u2019est Alex ! Je viens de voir que vous n\u2019avez toujours pas finalis\u00e9 votre d\u00e9p\u00f4t :( "
        ),
        (
            f"That{Q}s sad! Just let me know how I can help you, I{Q}m always here!",
            "C\u2019est dommage ! Dites-moi comment je peux vous aider, je suis toujours disponible !"
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
            print(f"  OK L{line_idx+1}: replaced '{eng[:50]}...'")
        else:
            print(f"  MISS L{line_idx+1}: '{eng[:50]}...' NOT FOUND")
    lines[line_idx] = line

with open(FILE, "w", encoding="utf-8") as f:
    f.writelines(lines)

print(f"\nDone: {total} replacements applied.")
