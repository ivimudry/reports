import os, re

f = open(r'c:\Projects\REPORTS\тексти\Celsius\_audit_result.txt', 'r', encoding='utf-8')
lines = f.readlines()
f.close()

current_file = ''
file_stats = {}
# Social labels that SHOULD be EN: X, Telegram, Discord
social_skip = {'text_4', 'text_5', 'text_6', 'text_7', 'text_8', 'text_9', 'text_10', 'text_11'}

for line in lines:
    line = line.rstrip()
    if line.startswith('FILE:'):
        current_file = line.replace('FILE:', '').strip()
        file_stats[current_file] = {'en_content': 0, 'tr_content': 0, 'en_social': 0}
    elif current_file and '[EN]' in line:
        # Check if it's a social label
        field = line.strip().split()[0] if line.strip() else ''
        is_social = False
        for sk in social_skip:
            if field == sk:
                is_social = True
                break
        if is_social:
            file_stats[current_file]['en_social'] += 1
        else:
            file_stats[current_file]['en_content'] += 1
    elif current_file and '[TR]' in line:
        file_stats[current_file]['tr_content'] += 1

print("=== TRANSLATION STATUS BY FILE ===\n")
for fn, stats in file_stats.items():
    total = stats['en_content'] + stats['tr_content']
    pct = (stats['tr_content'] / total * 100) if total > 0 else 0
    status = 'DONE' if stats['en_content'] == 0 else 'NEEDS WORK'
    print(f"{fn}")
    print(f"  Content:  {stats['tr_content']} translated, {stats['en_content']} still EN  ({pct:.0f}%)  [{status}]")
    print(f"  Social labels still EN (ok): {stats['en_social']}")
    print()
