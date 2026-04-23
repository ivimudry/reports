import re
p=r'C:\Projects\REPORTS\тексти\оші\html\Oshi Welcome Flow Updated.html'
s=open(p,'r',encoding='utf-8').read()
lines=s.split('\n')

sect_email=[None]*(len(lines)+2)
sect_geo=[None]*(len(lines)+2)
cur_email=None; cur_geo=None
hdr_re=re.compile(r'<!--\s*=+\s*(EMAIL|INAPP|SMS)\s*#([\d.]+)')
geo_re=re.compile(r'<h3>(EMAIL|INAPP|SMS)\s*\((DEFAULT|AU|CA|DE)\)')
for i,l in enumerate(lines):
    m=hdr_re.search(l)
    if m:
        cur_email=f"{m.group(1)} #{m.group(2)}"; cur_geo=None
    m=geo_re.search(l)
    if m: cur_geo=m.group(2)
    sect_email[i]=cur_email; sect_geo[i]=cur_geo

total=0
def rep_block(pred, old, new):
    global total
    c=0
    for i,l in enumerate(lines):
        if pred(sect_email[i], sect_geo[i]) and old in l:
            c+=l.count(old); lines[i]=l.replace(old,new)
    total+=c
    return c

def rep_block_re(pred, pattern, repl):
    global total
    c=0
    rgx=re.compile(pattern)
    for i,l in enumerate(lines):
        if pred(sect_email[i], sect_geo[i]):
            new,n=rgx.subn(repl,l)
            if n: c+=n; lines[i]=new
    total+=c
    return c

# === EMAIL #3 — replace bolded game name triplets per GEO ===
# DEFAULT: Sweet Bonanza, Gates of Olympus and Sugar Rush -> Elvis Frog TRUEWAYS, Gemhalla and Aztec Magic Bonanza from BGaming
print("E3 DEF:", rep_block_re(lambda e,g: e=='EMAIL #3' and g=='DEFAULT',
    r'<b>Sweet Bonanza</b>, <b>Gates of Olympus</b> and <b>Sugar Rush</b>',
    '<b>Elvis Frog TRUEWAYS</b>, <b>Gemhalla</b> and <b>Aztec Magic Bonanza</b> from BGaming'))

# AU
print("E3 AU:", rep_block_re(lambda e,g: e=='EMAIL #3' and g=='AU',
    r'<b>Big Bass Bonanza</b>, <b>Wolf Gold</b> and <b>Sweet Bonanza</b> from Pragmatic Play',
    '<b>Lady Wolf Moon Megaways</b> from BGaming, <b>Big Catch Bonanza</b> from netgame and <b>Buffalo Trail</b> from gamebeat'))

# CA
print("E3 CA:", rep_block_re(lambda e,g: e=='EMAIL #3' and g=='CA',
    r'<b>Sugar Rush</b> and <b>Gates of Olympus</b> from Pragmatic Play, plus <b>Wanted Dead or a Wild</b> from Hacksaw Gaming',
    '<b>Olympus TRUEWAYS</b> from BGaming and <b>Gates of Olympus Super Scatter</b> from Pragmatic, plus <b>Lucky Gold Miner</b> from 1spin4win'))

# DE body
print("E3 DE body:", rep_block_re(lambda e,g: e=='EMAIL #3' and g=='DE',
    r'<b>Elvis Frog TRUEWAYS</b> von BGaming, <b>Book Of Ra Magic</b> von Novomatic und <b>Big Bass Splash</b> von Pragmatic Play',
    '<b>Elvis Frog TRUEWAYS</b> von BGaming, <b>Lucky Jane in Egypt</b> von 1spin4win und <b>Bonanza Trillion</b> von BGaming'))

# DE preheader (may have <b> too — try both)
print("E3 DE pre v1:", rep_block(lambda e,g: e=='EMAIL #3' and g=='DE',
    "Sofort, Paysafecard, Krypto - plus Elvis Frog TRUEWAYS, Book Of Ra Magic und Big Bass Splash",
    "Sofort, Paysafecard, Krypto - plus Elvis Frog TRUEWAYS, Lucky Jane in Egypt und Bonanza Trillion"))
# Alt with HTML entities or different dash
print("E3 DE pre v2:", rep_block(lambda e,g: e=='EMAIL #3' and g=='DE',
    "Book Of Ra Magic und Big Bass Splash",
    "Lucky Jane in Egypt und Bonanza Trillion"))

# === EMAIL #4 winners — game names may be bold ===
def e4(geo, pairs):
    for old,new in pairs:
        # try plain
        c=rep_block(lambda e,g,geo=geo: e=='EMAIL #4' and g==geo, old, new)
        # try with <b>
        old_b=old.replace("on ","on <b>")+"</b>" if old.startswith("on ") else old
        new_b=new.replace("on ","on <b>")+"</b>" if new.startswith("on ") else new
        old_bb=old.replace("bei ","bei <b>")+"</b>" if old.startswith("bei ") else old
        new_bb=new.replace("bei ","bei <b>")+"</b>" if new.startswith("bei ") else new
        c2=rep_block(lambda e,g,geo=geo: e=='EMAIL #4' and g==geo, old_b, new_b) if old_b!=old else 0
        c3=rep_block(lambda e,g,geo=geo: e=='EMAIL #4' and g==geo, old_bb, new_bb) if old_bb!=old else 0
        print(f"E4 {geo} {old!r}: plain={c} b={c2} bb={c3}")

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
 # Gates of Olympus already replaced earlier with Super Scatter - skip
 ("on Wanted Dead or a Wild","on Lucky Gold Miner"),
])
e4('DE',[
 ("bei Book Of Ra Magic","bei Elvis Frog TRUEWAYS"),
 ("bei Gates of Olympus","bei Lucky Jane in Egypt"),
 ("bei Big Bass Splash","bei Bonanza Trillion"),
])

# === EMAIL #5/INAPP #5/SMS #5/EMAIL #6: AU + CA ===
def in_set(emails, geo):
    return lambda e,g,emails=emails,geo=geo: e in emails and g==geo
em56=['EMAIL #5','INAPP #5','SMS #5','EMAIL #6']
print("56 AU BBB:", rep_block(in_set(em56,'AU'), "Big Bass Bonanza","Lady Wolf Moon Megaways"))
print("56 AU BASS125:", rep_block(in_set(em56,'AU'), "BASS125","WOLF125"))
print("56 CA SR:", rep_block(in_set(em56,'CA'), "Sugar Rush","Olympus TRUEWAYS"))
print("56 CA SUGAR125:", rep_block(in_set(em56,'CA'), "SUGAR125","OLYMP125"))

# === EMAIL #7 / SMS #7 ===
e7s=['EMAIL #7','SMS #7']
print("E7 DEF BoR:", rep_block(in_set(e7s,'DEFAULT'), "Book Of Ra Magic","Gemhalla"))
print("E7 DEF BOOKRA150:", rep_block(in_set(e7s,'DEFAULT'), "BOOKRA150","GEM150"))
print("E7 DE BoR:", rep_block(in_set(e7s,'DE'), "Book Of Ra Magic","Lucky Jane in Egypt"))
print("E7 DE BOOKRA150:", rep_block(in_set(e7s,'DE'), "BOOKRA150","JANE150"))
print("E7 AU SB:", rep_block(in_set(e7s,'AU'), "Sweet Bonanza","Big Catch Bonanza"))
print("E7 AU SWEET150:", rep_block(in_set(e7s,'AU'), "SWEET150","CATCH150"))
# CA Gates of Olympus -> Super Scatter (skip if already followed)
ca=0
for i,l in enumerate(lines):
    if sect_email[i] in e7s and sect_geo[i]=='CA':
        new=re.sub(r'Gates of Olympus(?! Super Scatter)','Gates of Olympus Super Scatter',l)
        if new!=l:
            ca += len(re.findall(r'Gates of Olympus(?! Super Scatter)',l))
            lines[i]=new
print("E7 CA GoO->SS:", ca); total+=ca

# === EMAIL #8 ===
print("E8 DEF BBS:", rep_block(in_set(['EMAIL #8'],'DEFAULT'), "Big Bass Splash","Aztec Magic Bonanza"))
print("E8 DEF BASS160:", rep_block(in_set(['EMAIL #8'],'DEFAULT'), "BASS160","AZTEC160"))
print("E8 DE BBS:", rep_block(in_set(['EMAIL #8'],'DE'), "Big Bass Splash","Bonanza Trillion"))
print("E8 DE BASS160:", rep_block(in_set(['EMAIL #8'],'DE'), "BASS160","TRILL160"))
print("E8 AU WG:", rep_block(in_set(['EMAIL #8'],'AU'), "Wolf Gold","Buffalo Trail"))
print("E8 AU WOLF160:", rep_block(in_set(['EMAIL #8'],'AU'), "WOLF160","BUFF160"))
print("E8 CA WDoaW:", rep_block(in_set(['EMAIL #8'],'CA'), "Wanted Dead or a Wild","Lucky Gold Miner"))
print("E8 CA WANTED160:", rep_block(in_set(['EMAIL #8'],'CA'), "WANTED160","GOLD160"))

out='\n'.join(lines)
open(p,'w',encoding='utf-8',newline='').write(out)
print("\nTOTAL:", total)

# === Re-scan ===
print("\n=== REMAINING ===")
new_lines=out.split('\n')
patterns=["BASS125","SUGAR125","BOOKRA150","SWEET150","BASS160","WOLF160","WANTED160",
 "Big Bass Bonanza","Sugar Rush","Book Of Ra","Sweet Bonanza","Big Bass Splash","Wolf Gold","Wanted Dead",
 "bonus=BASS125","bonus=SUGAR125","bonus=BOOKRA150","bonus=SWEET150","bonus=BASS160","bonus=WOLF160","bonus=WANTED160"]
for pat in patterns:
    hits=[(i+1,new_lines[i]) for i in range(len(new_lines)) if pat in new_lines[i]]
    if hits:
        print(f"\n-- {pat} ({len(hits)}) --")
        for ln,txt in hits:
            print(f" L{ln} [{sect_email[ln-1]}/{sect_geo[ln-1]}]: {txt[:200]}")
