import os

DIR = r"c:\Projects\REPORTS\тексти\Celsius"
FILES = [
    "DEP Retention - Table data.txt",
    "FTD Retention Flow - Table data.txt",
    "Nutrition #2 - Table data.txt",
    "Nutrition #3 - Table data.txt",
    "SU Retention - Table data.txt",
    "Welcome Flow - Table data.txt",
]

total = 0

for fn in FILES:
    path = os.path.join(DIR, fn)
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    locale = ''
    file_changes = 0

    for i in range(len(lines)):
        s = lines[i].strip()
        if s.startswith('locale: '):
            locale = s[8:]

        # === 1. Team signature + auto message (fr-FR only, hu/pl already done) ===
        if locale == 'fr-FR' and 'Celsius Casino Team.' in lines[i] and 'This is an automated message, please do not reply.' in lines[i]:
            lines[i] = lines[i].replace(
                'Celsius Casino Team.',
                "L'\u00e9quipe Celsius Casino."
            ).replace(
                'This is an automated message, please do not reply.',
                'Ceci est un message automatique, veuillez ne pas r\u00e9pondre.'
            )
            file_changes += 1

        # === 2. "Support" label → translate for fr-FR, hu-HU, pl-PL ===
        if '>Support<' in lines[i]:
            if locale == 'fr-FR':
                lines[i] = lines[i].replace('>Support<', '>Assistance<')
                file_changes += 1
            elif locale == 'hu-HU':
                lines[i] = lines[i].replace('>Support<', '>T\u00e1mogat\u00e1s<')
                file_changes += 1
            elif locale == 'pl-PL':
                lines[i] = lines[i].replace('>Support<', '>Wsparcie<')
                file_changes += 1

    with open(path, 'w', encoding='utf-8') as f:
        f.writelines(lines)

    print(f"{fn}: {file_changes} changes")
    total += file_changes

print(f"\nTotal: {total} changes")
