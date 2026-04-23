import re, io
p=r'C:\Projects\REPORTS\тексти\оші\html\Oshi Welcome Flow Updated.html'
s=open(p,'r',encoding='utf-8').read()
lines=s.split('\n')

# Determine section per line
sect_email=[None]*(len(lines)+2)  # like "EMAIL #5", "INAPP #5", "SMS #7"
sect_geo=[None]*(len(lines)+2)
cur_email=None; cur_geo=None
hdr_re=re.compile(r'<!--\s*=+\s*(EMAIL|INAPP|SMS)\s*#([\d.]+)')
geo_re=re.compile(r'<h3>(EMAIL|INAPP|SMS)\s*\((DEFAULT|AU|CA|DE)\)')
for i,l in enumerate(lines):
    m=hdr_re.search(l)
    if m:
        cur_email=f"{m.group(1)} #{m.group(2)}"
        cur_geo=None
    m=geo_re.search(l)
    if m:
        cur_geo=m.group(2)
    sect_email[i]=cur_email
    sect_geo[i]=cur_geo

total_replacements=0

def replace_in_block(predicate, old, new):
    """Replace only in lines where predicate(email,geo) is True. Returns count."""
    global total_replacements
    cnt=0
    for i,l in enumerate(lines):
        if predicate(sect_email[i], sect_geo[i]):
            if old in l:
                cnt += l.count(old)
                lines[i] = l.replace(old, new)
    total_replacements += cnt
    return cnt

# === EMAIL #3 long sentences ===
e3_def_old="There's a whole world beyond the reels at Oshi. Spin global hits like Sweet Bonanza, Gates of Olympus and Sugar Rush, jump into weekly tournaments with real prize pools, and climb the loyalty ladder for cashback every Wednesday."
e3_def_new="There's a whole world beyond the reels at Oshi. Spin global hits like Elvis Frog TRUEWAYS, Gemhalla and Aztec Magic Bonanza from BGaming, jump into weekly tournaments with real prize pools, and climb the loyalty ladder for cashback every Wednesday."
print("E3 DEF:", replace_in_block(lambda e,g: e=='EMAIL #3' and g=='DEFAULT', e3_def_old, e3_def_new))

e3_au_old="There's a whole world beyond the reels at Oshi. Spin Aussie favourites like Big Bass Bonanza, Wolf Gold and Sweet Bonanza from Pragmatic Play, jump into weekly tournaments with real prize pools, and climb the loyalty ladder for cashback every Wednesday."
e3_au_new="There's a whole world beyond the reels at Oshi. Spin Aussie favourites like Lady Wolf Moon Megaways from BGaming, Big Catch Bonanza from netgame and Buffalo Trail from gamebeat, jump into weekly tournaments with real prize pools, and climb the loyalty ladder for cashback every Wednesday."
print("E3 AU:", replace_in_block(lambda e,g: e=='EMAIL #3' and g=='AU', e3_au_old, e3_au_new))

e3_ca_old="There's a whole world beyond the reels at Oshi. Spin Canadian favourites like Sugar Rush and Gates of Olympus from Pragmatic Play, plus Wanted Dead or a Wild from Hacksaw Gaming, jump into weekly tournaments with real prize pools, and climb the loyalty ladder for cashback every Wednesday."
e3_ca_new="There's a whole world beyond the reels at Oshi. Spin Canadian favourites like Olympus TRUEWAYS from BGaming and Gates of Olympus Super Scatter from Pragmatic, plus Lucky Gold Miner from 1spin4win, jump into weekly tournaments with real prize pools, and climb the loyalty ladder for cashback every Wednesday."
print("E3 CA:", replace_in_block(lambda e,g: e=='EMAIL #3' and g=='CA', e3_ca_old, e3_ca_new))

e3_de_old="Bei Oshi gibt es eine ganze Welt jenseits der Walzen. Spiele beliebte Slots wie Elvis Frog TRUEWAYS von BGaming, Book Of Ra Magic von Novomatic und Big Bass Splash von Pragmatic Play, nimm an wochentlichen Turnieren mit echten Preispools teil und klettere die Treue-Leiter hoch fur Cashback jeden Mittwoch."
e3_de_new="Bei Oshi gibt es eine ganze Welt jenseits der Walzen. Spiele beliebte Slots wie Elvis Frog TRUEWAYS von BGaming, Lucky Jane in Egypt von 1spin4win und Bonanza Trillion von BGaming, nimm an wochentlichen Turnieren mit echten Preispools teil und klettere die Treue-Leiter hoch fur Cashback jeden Mittwoch."
print("E3 DE body:", replace_in_block(lambda e,g: e=='EMAIL #3' and g=='DE', e3_de_old, e3_de_new))

e3_de_pre_old="Sofort, Paysafecard, Krypto - plus Elvis Frog TRUEWAYS, Book Of Ra Magic und Big Bass Splash"
e3_de_pre_new="Sofort, Paysafecard, Krypto - plus Elvis Frog TRUEWAYS, Lucky Jane in Egypt und Bonanza Trillion"
print("E3 DE pre:", replace_in_block(lambda e,g: e=='EMAIL #3' and g=='DE', e3_de_pre_old, e3_de_pre_new))

# === EMAIL #4 winners ===
def e4(geo, pairs):
    for old,new in pairs:
        c=replace_in_block(lambda e,g,geo=geo: e=='EMAIL #4' and g==geo, old, new)
        print(f"E4 {geo} '{old[:30]}...':", c)

e4('DEFAULT',[
 ("on Sweet Bonanza","on Elvis Frog TRUEWAYS"),
 ("on Gates of Olympus","on Gemhalla"),
 ("on Sugar Rush","on Aztec Magic Bonanza"),
])
e4('AU',[
 ("on Big Bass Bonanza","on Lady Wolf Moon Megaways"),
 ("on Wolf Gold","on Big Catch Bonanza"),
 ("on Sweet Bonanza","on Buffalo Trail"),
])
e4('CA',[
 ("on Sugar Rush","on Olympus TRUEWAYS"),
 ("on Gates of Olympus","on Gates of Olympus Super Scatter"),
 ("on Wanted Dead or a Wild","on Lucky Gold Miner"),
])
e4('DE',[
 ("bei Book Of Ra Magic","bei Elvis Frog TRUEWAYS"),
 ("bei Gates of Olympus","bei Lucky Jane in Egypt"),
 ("bei Big Bass Splash","bei Bonanza Trillion"),
])

# === EMAIL #5 / INAPP #5 / SMS #5 / EMAIL #6: AU + CA mapping ===
def in_set(emails, geo):
    return lambda e,g,emails=emails,geo=geo: e in emails and g==geo
emails56=['EMAIL #5','INAPP #5','SMS #5','EMAIL #6']
print("E5/6 AU 'Big Bass Bonanza':", replace_in_block(in_set(emails56,'AU'), "Big Bass Bonanza","Lady Wolf Moon Megaways"))
print("E5/6 AU 'BASS125':", replace_in_block(in_set(emails56,'AU'), "BASS125","WOLF125"))
print("E5/6 CA 'Sugar Rush':", replace_in_block(in_set(emails56,'CA'), "Sugar Rush","Olympus TRUEWAYS"))
print("E5/6 CA 'SUGAR125':", replace_in_block(in_set(emails56,'CA'), "SUGAR125","OLYMP125"))

# === EMAIL #7 / SMS #7 ===
e7s=['EMAIL #7','SMS #7']
# DEFAULT
print("E7 DEF 'Book Of Ra Magic':", replace_in_block(in_set(e7s,'DEFAULT'), "Book Of Ra Magic","Gemhalla"))
print("E7 DEF 'BOOKRA150':", replace_in_block(in_set(e7s,'DEFAULT'), "BOOKRA150","GEM150"))
# DE
print("E7 DE 'Book Of Ra Magic':", replace_in_block(in_set(e7s,'DE'), "Book Of Ra Magic","Lucky Jane in Egypt"))
print("E7 DE 'BOOKRA150':", replace_in_block(in_set(e7s,'DE'), "BOOKRA150","JANE150"))
# AU
print("E7 AU 'Sweet Bonanza':", replace_in_block(in_set(e7s,'AU'), "Sweet Bonanza","Big Catch Bonanza"))
print("E7 AU 'SWEET150':", replace_in_block(in_set(e7s,'AU'), "SWEET150","CATCH150"))
# CA: Gates of Olympus -> Gates of Olympus Super Scatter, only when not already followed by " Super Scatter"
ca_cnt=0
for i,l in enumerate(lines):
    if sect_email[i] in e7s and sect_geo[i]=='CA':
        new=re.sub(r'Gates of Olympus(?! Super Scatter)','Gates of Olympus Super Scatter',l)
        if new!=l:
            ca_cnt += new.count('Gates of Olympus Super Scatter') - l.count('Gates of Olympus Super Scatter')
            lines[i]=new
print("E7 CA 'Gates of Olympus':", ca_cnt)

# === EMAIL #8 ===
print("E8 DEF 'Big Bass Splash':", replace_in_block(in_set(['EMAIL #8'],'DEFAULT'), "Big Bass Splash","Aztec Magic Bonanza"))
print("E8 DEF 'BASS160':", replace_in_block(in_set(['EMAIL #8'],'DEFAULT'), "BASS160","AZTEC160"))
print("E8 DE 'Big Bass Splash':", replace_in_block(in_set(['EMAIL #8'],'DE'), "Big Bass Splash","Bonanza Trillion"))
print("E8 DE 'BASS160':", replace_in_block(in_set(['EMAIL #8'],'DE'), "BASS160","TRILL160"))
print("E8 AU 'Wolf Gold':", replace_in_block(in_set(['EMAIL #8'],'AU'), "Wolf Gold","Buffalo Trail"))
print("E8 AU 'WOLF160':", replace_in_block(in_set(['EMAIL #8'],'AU'), "WOLF160","BUFF160"))
print("E8 CA 'Wanted Dead or a Wild':", replace_in_block(in_set(['EMAIL #8'],'CA'), "Wanted Dead or a Wild","Lucky Gold Miner"))
print("E8 CA 'WANTED160':", replace_in_block(in_set(['EMAIL #8'],'CA'), "WANTED160","GOLD160"))

out='\n'.join(lines)
open(p,'w',encoding='utf-8',newline='').write(out)
print("TOTAL replacements:", total_replacements)

# Re-scan
print("\n=== REMAINING SCAN ===")
patterns=["BASS125","SUGAR125","BOOKRA150","SWEET150","BASS160","WOLF160","WANTED160",
 "Big Bass Bonanza","Sugar Rush","Book Of Ra","Sweet Bonanza","Big Bass Splash","Wolf Gold","Wanted Dead",
 "bonus=BASS125","bonus=SUGAR125","bonus=BOOKRA150","bonus=SWEET150","bonus=BASS160","bonus=WOLF160","bonus=WANTED160"]
new_lines=out.split('\n')
for pat in patterns:
    hits=[(i+1,new_lines[i]) for i in range(len(new_lines)) if pat in new_lines[i]]
    if hits:
        print(f"\n-- {pat} ({len(hits)} hits) --")
        for ln,txt in hits:
            print(f" L{ln} [{sect_email[ln-1]}/{sect_geo[ln-1]}]: {txt[:200]}")
