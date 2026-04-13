import os, re

DIR = r"c:\Projects\REPORTS\тексти\Celsius"
files = [f for f in os.listdir(DIR) if f.endswith('Table data.txt')]

# Pattern: remove ?utm_...  or &utm_... query strings from URLs
# Case 1: URL?utm_x=a&utm_y=b  → URL (remove ? and all utm params after it)
# Case 2: URL?non_utm=a&utm_x=b → URL?non_utm=a (remove &utm_... parts)
# In our case, all query params are utm_ based, so we just strip ?utm...$ from URLs

total_changes = 0

for fn in sorted(files):
    path = os.path.join(DIR, fn)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    before_count = len(re.findall(r'[?&]utm_', content))
    
    # Remove the entire query string if it starts with utm_
    # Pattern: ?utm_param=val(&utm_param=val)*
    new_content = re.sub(r'\?utm_\w+=[^&\s"<>]*(?:&utm_\w+=[^&\s"<>]*)*', '', content)
    
    # Also handle case where utm_ params come after other params (unlikely but safe)
    new_content = re.sub(r'&utm_\w+=[^&\s"<>]*', '', new_content)
    
    after_count = len(re.findall(r'[?&]utm_', new_content))
    
    changes = before_count - after_count
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"{fn}: removed {changes} utm params (remaining: {after_count})")
    total_changes += changes

print(f"\nTotal: {total_changes} utm params removed")
