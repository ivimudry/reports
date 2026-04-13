import os

DIR = r"c:\Projects\REPORTS\тексти\Celsius"
files = [f for f in os.listdir(DIR) if f.endswith(".txt")]

EN_RECEIVING = "You are receiving this email from celsiuscasino.com because during email verification you agreed to receive emails from us regarding new features, events, promotions and special offers."

translations = {
    "Default": {
        "receiving": EN_RECEIVING,
        "unsubscribe": ">Unsubscribe</a>",
        "all_rights": "All Rights Reserved ©",
    },
    "fr-FR": {
        "receiving": "Vous recevez cet e-mail de celsiuscasino.com",
        "unsubscribe": ">Se désabonner</a>",
        "all_rights": "Tous droits réservés ©",
    },
    "hu-HU": {
        "receiving": "Ezt az e-mailt a celsiuscasino.com küldi",
        "unsubscribe": ">Leiratkozás</a>",
        "all_rights": "Minden jog fenntartva ©",
    },
    "pl-PL": {
        "receiving": "Otrzymujesz tę wiadomość e-mail od celsiuscasino.com",
        "unsubscribe": ">Wypisz się</a>",
        "all_rights": "Wszelkie prawa zastrzeżone ©",
    },
}

errors = 0
checked = 0

for fname in sorted(files):
    path = os.path.join(DIR, fname)
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    
    current_locale = "Default"
    current_name = "???"
    
    for i, line in enumerate(lines, 1):
        stripped = line.strip()
        if stripped.startswith("name:"):
            current_name = stripped[5:].strip()
        elif stripped.startswith("locale:"):
            current_locale = stripped[7:].strip()
        
        tr = translations.get(current_locale)
        if not tr:
            continue
        
        # Check: English text should NOT appear in non-Default locales
        if current_locale != "Default":
            if EN_RECEIVING in line:
                print(f"ERROR: {fname} L{i} [{current_name}/{current_locale}] - Still has ENGLISH 'receiving' text!")
                errors += 1
            if ">Unsubscribe</a>" in line:
                print(f"ERROR: {fname} L{i} [{current_name}/{current_locale}] - Still has ENGLISH 'Unsubscribe'!")
                errors += 1
            if "All Rights Reserved ©" in line:
                print(f"ERROR: {fname} L{i} [{current_name}/{current_locale}] - Still has ENGLISH 'All Rights Reserved'!")
                errors += 1
        
        # Check: correct translation should be present for each locale
        if tr["receiving"] in line:
            checked += 1
        if tr["unsubscribe"] in line:
            checked += 1
        if tr["all_rights"] in line:
            checked += 1

if errors == 0:
    print(f"ALL OK - 0 errors, {checked} correct translations verified")
else:
    print(f"\n{errors} ERRORS found!")
