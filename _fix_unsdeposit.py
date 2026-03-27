import os, re

fpath = os.path.join("тексти", "пантери нова праця", "Unsuccessful Deposit - Table data.txt")
with open(fpath, "r", encoding="utf-8") as f:
    content = f.read()

# Remove duplicate &amp;utm_language=en before closing quote in support links
old = r'(pantherbet\.co\.za/support\?utm_campaign=faileddep&amp;utm_source=customerio&amp;utm_medium=email&amp;utm_language=en&amp;utm_email=\d+)&amp;utm_language=en"'
new = r'\1"'

count = len(re.findall(old, content))
content = re.sub(old, new, content)

with open(fpath, "w", encoding="utf-8") as f:
    f.write(content)

print(f"Fixed {count} duplicate utm_language in Unsuccessful Deposit")
