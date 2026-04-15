import json, os

base = os.path.dirname(os.path.abspath(__file__))
data = json.load(open(os.path.join(base, '_texts_to_translate.json'), 'r', encoding='utf-8'))
total = 0
for fname, emails in data.items():
    n_fields = sum(len(em['fields']) for em in emails)
    total += n_fields
    print(f"{fname}: {len(emails)} emails, {n_fields} fields")
print(f"\nTotal fields to translate: {total}")
