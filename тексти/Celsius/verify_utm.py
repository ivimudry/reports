import os, re

DIR = r"c:\Projects\REPORTS\тексти\Celsius"
files = [f for f in os.listdir(DIR) if f.endswith('Table data.txt')]

for fn in sorted(files):
    path = os.path.join(DIR, fn)
    content = open(path, 'r', encoding='utf-8').read()
    
    # Check no utm_ remains
    utms = re.findall(r'utm_', content)
    if utms:
        print(f"WARN {fn}: {len(utms)} utm_ remnants!")
    
    # Check no dangling ? at end of URLs
    dangling = re.findall(r'https?://[^\s"<>]+\?(?=["\s<>])', content)
    if dangling:
        print(f"WARN {fn}: {len(dangling)} dangling '?' in URLs")
        for d in dangling[:3]:
            print(f"  {d}")
    
    # Show first 3 URLs as sample
    urls = re.findall(r'https://celsiuscasino\.com[^\s"<>]*', content)
    unique = list(dict.fromkeys(urls))[:5]
    print(f"{fn}: {len(urls)} celsiuscasino URLs, samples:")
    for u in unique:
        print(f"  {u}")
    print()
