import os, re

DIR = r"c:\Projects\REPORTS\тексти\Celsius"
files = [f for f in os.listdir(DIR) if f.endswith(".txt")]

# Translations per locale
translations = {
    "Default": {
        "receiving": "You are receiving this email from celsiuscasino.com because during email verification you agreed to receive emails from us regarding new features, events, promotions and special offers.",
        "unsubscribe": "Unsubscribe",
        "all_rights": "All Rights Reserved",
    },
    "fr-FR": {
        "receiving": "Vous recevez cet e-mail de celsiuscasino.com car, lors de la vérification de votre adresse e-mail, vous avez accepté de recevoir des e-mails de notre part concernant les nouvelles fonctionnalités, événements, promotions et offres spéciales.",
        "unsubscribe": "Se désabonner",
        "all_rights": "Tous droits réservés",
    },
    "hu-HU": {
        "receiving": "Ezt az e-mailt a celsiuscasino.com küldi, mert az e-mail-cím hitelesítése során hozzájárult ahhoz, hogy e-maileket kapjon tőlünk az új funkciókról, eseményekről, promóciókról és különleges ajánlatokról.",
        "unsubscribe": "Leiratkozás",
        "all_rights": "Minden jog fenntartva",
    },
    "pl-PL": {
        "receiving": "Otrzymujesz tę wiadomość e-mail od celsiuscasino.com, ponieważ podczas weryfikacji adresu e-mail wyraziłeś zgodę na otrzymywanie od nas wiadomości dotyczących nowych funkcji, wydarzeń, promocji i ofert specjalnych.",
        "unsubscribe": "Wypisz się",
        "all_rights": "Wszelkie prawa zastrzeżone",
    },
}

EN_RECEIVING = "You are receiving this email from celsiuscasino.com because during email verification you agreed to receive emails from us regarding new features, events, promotions and special offers."
EN_UNSUBSCRIBE = "Unsubscribe"
EN_ALL_RIGHTS = "All Rights Reserved"

total_changes = 0

for fname in sorted(files):
    path = os.path.join(DIR, fname)
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    
    current_locale = "Default"
    changes = 0
    new_lines = []
    
    for line in lines:
        stripped = line.strip()
        
        # Track locale
        if stripped.startswith("locale:"):
            current_locale = stripped[7:].strip()
        
        tr = translations.get(current_locale)
        if not tr or current_locale == "Default":
            new_lines.append(line)
            continue
        
        modified = line
        
        # Replace "You are receiving this email..." text
        if EN_RECEIVING in modified:
            modified = modified.replace(EN_RECEIVING, tr["receiving"])
            changes += 1
        
        # Replace "Unsubscribe" link text (but NOT the {% unsubscribe_url %} tag)
        # Target: >Unsubscribe</a>
        if ">Unsubscribe</a>" in modified:
            modified = modified.replace(">Unsubscribe</a>", f">{tr['unsubscribe']}</a>")
            changes += 1
        
        # Replace "All Rights Reserved" text
        if EN_ALL_RIGHTS in modified and "Celsius Casino" in modified:
            modified = modified.replace(EN_ALL_RIGHTS, tr["all_rights"])
            changes += 1
        
        new_lines.append(modified)
    
    if changes > 0:
        with open(path, "w", encoding="utf-8") as f:
            f.writelines(new_lines)
        print(f"{fname}: {changes} replacements")
        total_changes += changes
    else:
        print(f"{fname}: no changes")

print(f"\nTOTAL: {total_changes} replacements across {len(files)} files")
