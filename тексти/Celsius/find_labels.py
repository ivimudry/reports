import os, re

DIR = r"c:\Projects\REPORTS\тексти\Celsius"
files = [f for f in os.listdir(DIR) if f.endswith(".txt")]

targets = {
    "receiving_email": "You are receiving this email from celsiuscasino.com",
    "support_unsubscribe": "support@celsiuscasino.com",
    "all_rights": "All Rights Reserved",
}

for fname in sorted(files):
    path = os.path.join(DIR, fname)
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    
    current_name = "???"
    current_locale = "???"
    
    results = {k: [] for k in targets}
    
    for i, line in enumerate(lines, 1):
        stripped = line.strip()
        if stripped.startswith("name:"):
            current_name = stripped[5:].strip()
        elif stripped.startswith("locale:"):
            current_locale = stripped[7:].strip()
        else:
            # Find which text_N label this line has
            label_match = re.match(r'^(text_\d+):', stripped)
            label = label_match.group(1) if label_match else "???"
            
            for key, search in targets.items():
                if search in line:
                    results[key].append((current_name, current_locale, label, i))
    
    # Print results per file
    has_any = any(v for v in results.values())
    if has_any:
        print(f"\n{'='*80}")
        print(f"FILE: {fname}")
        print(f"{'='*80}")
        
        for key, label_name in [("receiving_email", '"You are receiving this email..."'),
                                 ("support_unsubscribe", '"support@celsiuscasino.com | Unsubscribe"'),
                                 ("all_rights", '"All Rights Reserved..."')]:
            entries = results[key]
            if entries:
                print(f"\n  {label_name}:")
                # Group by name
                seen = {}
                for name, locale, lbl, line_no in entries:
                    k = (name, lbl)
                    if k not in seen:
                        seen[k] = []
                    seen[k].append((locale, line_no))
                
                for (name, lbl), locales in seen.items():
                    locale_list = ", ".join(f"{loc}(L{ln})" for loc, ln in locales)
                    print(f"    [{lbl}] {name} → {locale_list}")
            else:
                print(f"\n  {label_name}: NOT FOUND")

# Also check for "support_icon_href" field separately
print(f"\n\n{'='*80}")
print("ALSO: 'support_icon_href: mailto:support@celsiuscasino.com' occurrences:")
print(f"{'='*80}")
for fname in sorted(files):
    path = os.path.join(DIR, fname)
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    current_name = "???"
    current_locale = "???"
    found = []
    for i, line in enumerate(lines, 1):
        stripped = line.strip()
        if stripped.startswith("name:"):
            current_name = stripped[5:].strip()
        elif stripped.startswith("locale:"):
            current_locale = stripped[7:].strip()
        elif "support_icon_href:" in stripped and "celsiuscasino" in stripped:
            found.append((current_name, current_locale, i))
    if found:
        print(f"\n  {fname}:")
        seen = {}
        for name, locale, ln in found:
            if name not in seen:
                seen[name] = []
            seen[name].append(f"{locale}(L{ln})")
        for name, locs in seen.items():
            print(f"    {name} → {', '.join(locs)}")
