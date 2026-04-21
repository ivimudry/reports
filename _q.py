import json, sys
sys.stdout.reconfigure(encoding="utf-8")
p = r"c:\Projects\REPORTS\тексти\оші\схеми та інше\oshi-games-all.json"
data = json.load(open(p, encoding="utf-8"))
terms = ["Book of Dead","Razor Shark","Fire Joker","Big Bass","Sweet Bonanza","Wolf Gold","Mega Moolah","Sugar Rush","Gates of Olympus","Starburst","Gonzo","Reactoonz","Book of Ra","Buffalo","Dog House","Wanted Dead"]
geo_cats = {"slots:de","slots:en-CA","slots:en-AU","slots:fr-CA"}
for t in terms:
    tl = t.lower()
    matches = [g for g in data if tl in (g.get("title") or "").lower()]
    print(f"\n=== {t} ({len(matches)}) ===")
    for g in matches:
        cats = g.get("categories") or []
        if isinstance(cats, str):
            cats = [cats]
        present = sorted(set(cats) & geo_cats)
        print(f"{g.get('title')} | {g.get('provider')} | {g.get('identifier')} | geo={g.get('is_geo_available')} | {','.join(present) or '-'}")
