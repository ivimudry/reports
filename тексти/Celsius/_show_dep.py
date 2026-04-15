import json, os

base = os.path.dirname(os.path.abspath(__file__))
data = json.load(open(os.path.join(base, '_texts_to_translate.json'), 'r', encoding='utf-8'))
dep = data['DEP Retention - Table data.txt']
for em in dep:
    print(f'=== {em["email"]} ===')
    for f in em['fields']:
        t = f['en_text']
        if len(t) > 150:
            t = t[:150] + '...'
        print(f'  {f["field"]}: {t}')
    print()
