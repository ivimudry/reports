#!/usr/bin/env python3
"""
DEP Retention - Translate hu-HU and pl-PL locales.
20 unique emails x 2 locales = 40 blocks to translate.
Fields: subject, preheader, text_1 (greeting), text_2 (body), text_3 (CTA), button_text_1.
Winner emails (3C, 3S, 6C, 8S): text_3 is team sig (already translated) - skip.
"""
import re, os, sys

FILE = r'c:\Projects\REPORTS\тексти\Celsius\DEP Retention - Table data.txt'

with open(FILE, 'r', encoding='utf-8') as f:
    content = f.read()

le = '\r\n' if '\r\n' in content else '\n'
content = content.replace('\r\n', '\n')
blocks = content.split('\n\n')

# Translation data: (email_name, locale) -> dict
T = {}

# ==================== HUNGARIAN (hu-HU) ====================

T[('Email 1C', 'hu-HU')] = {
    'subject': '\U0001f4a5 170% Bonus: Turb\u00f3zd fel a j\u00e1t\u00e9kod m\u00e9g ma',
    'preheader': 'N\u00e9zd meg, mi v\u00e1r r\u00e1d az asztalokn\u00e1l',
    'text_1_strong': '{{ customer.first_name | default:"J\u00e1t\u00e9kos" | capitalize }}, a parkett a ti\u00e9d!',
    'text_2_p': 'Mi\u00e9rt j\u00e1tszan\u00e1l csak a befizet\u00e9seddel, ha <strong>170%</strong>-kal t\u00f6bbel is mehetsz? Felturb\u00f3zzuk a k\u00f6vetkez\u0151 felt\u00f6lt\u00e9sedet, hogy tov\u00e1bb maradhass a j\u00e1t\u00e9kban \u00e9s nagyobb pillanatokat hajszolhass.',
    'text_3_p': '\u00cdrd be a <strong class="promocode">SURGE170</strong> k\u00f3dot a k\u00f6vetkez\u0151 befizet\u00e9sed el\u0151tt, hogy feloldd a <strong>170% Bonus</strong>t \u00e9s val\u00f3di el\u0151nny\u00e9 v\u00e1ltoztasd az egyenleged.<br><br>Az akci\u00f3 \u00e9l a <strong>Celsius Casino</strong>ban - kapd el a <strong>170% Bonus</strong>t, v\u00e1laszd ki a kedvenc asztalodat \u00e9s l\u00e9pj magabiztosan.',
    'button_text_1': 'N\u00d6VELD AZ EGYENLEGED',
}

T[('Email 1S', 'hu-HU')] = {
    'subject': '\U0001f94a 20% NoRisk Free Bet: \u00dcss kem\u00e9nyen',
    'preheader': 'A vonal nyitva - a kock\u00e1zatmentes el\u0151ny\u00f6d v\u00e1r',
    'text_1_strong': '{{ customer.first_name | default:"Bajnok" | capitalize }}, a gy\u0151zelem karny\u00fajt\u00e1snyira van!',
    'text_2_p': 'Nincs jobb \u00e9rz\u00e9s, mint egy nyer\u0151 fogad\u00e1s - ez\u00e9rt a k\u00f6vetkez\u0151 l\u00e9p\u00e9sedet egy <strong>20% NoRisk Free Bet</strong>tel t\u00e1mogatjuk, hogy magabiztosan j\u00e1tszhass.',
    'text_3_p': 'Az aktiv\u00e1l\u00e1shoz \u00edrd be a <strong class="promocode">WINSAFE20</strong> prom\u00f3k\u00f3dot a k\u00f6vetkez\u0151 befizet\u00e9sed el\u0151tt. A <strong>20% NoRisk Free Bet</strong>ed azonnal haszn\u00e1latra k\u00e9sz.<br><br>Fedezd fel a legforr\u00f3bb meccseket a <strong>Celsius Sport</strong>on, v\u00e1laszd ki a kedvenc piacodat \u00e9s csapj le, am\u00edg az oddsok \u00e9l\u0151k.',
    'button_text_1': 'SZEREZD MEG AZ EL\u0150NY\u00d6D',
}

T[('Email 2C', 'hu-HU')] = {
    'subject': '\u26a1 150% + 70 Free Spins: Ne k\u00e9slekedj, kapd el',
    'preheader': 'A k\u00f6vetkez\u0151 nagy nyerem\u00e9nyed k\u00e9sz - te k\u00e9sz vagy?',
    'text_1_strong': '{{ customer.first_name | default:"J\u00e1t\u00e9kos" | capitalize }}, a j\u00e1t\u00e9kok v\u00e1rnak!',
    'text_2_p': 'Mi\u00e9rt \u00fcln\u00e9l a kispadon, ha gy\u0171jthetn\u00e9d a nyerem\u00e9nyeket? Fizess be most \u00e9s l\u00e9pj szintet <strong>150% bonus + 70 Free Spins</strong>szel a <strong>Chaos Crew II by Hacksaw Gaming</strong> j\u00e1t\u00e9kban.',
    'text_3_p': 'A felold\u00e1shoz add meg a <strong class="promocode">CREWBOOST150</strong> prom\u00f3k\u00f3dot, majd fejezd be a befizet\u00e9st - a <strong>150% bonus \u00e9s 70 Free Spins</strong> az els\u0151 p\u00f6rg\u00e9st\u0151l k\u00e9sz.<br><br>Az akci\u00f3 a <strong>Celsius Casino</strong>ban nem \u00e1ll meg. Ugorj be a <strong>Chaos Crew II by Hacksaw Gaming</strong> j\u00e1t\u00e9kba \u00e9s hajszold a k\u00f6vetkez\u0151 nagy tal\u00e1latot.',
    'button_text_1': 'KAPD EL A DUPLA JUTALMAT',
}

T[('Email 2S', 'hu-HU')] = {
    'subject': '\u26bd 20% NoRisk Free Bet: Itt a f\u0151 m\u0171sorid\u0151',
    'preheader': 'A nap meccse h\u00edv - sz\u00e1llj be v\u00e9delemmel',
    'text_1_strong': '{{ customer.first_name | default:"Szurkol\u00f3" | capitalize }}, felgyulladtak a f\u00e9nyek!',
    'text_2_p': 'A f\u0151 m\u0171sorid\u0151 k\u00f6zeledik - a nap legnagyobb meccse, magas fesz\u00fclts\u00e9g, \u00e9s egyetlen pillanat mindent megv\u00e1ltoztathat. Sz\u00e1llj be a kezd\u0151r\u00fag\u00e1s el\u0151tt.',
    'text_3_p': 'A mai akci\u00f3 fokoz\u00e1s\u00e1hoz ig\u00e9nyeld a <strong>20% NoRisk Free Bet</strong>edet: add meg a <strong class="promocode">WINSAFE20</strong> prom\u00f3k\u00f3dot, majd fejezd be a befizet\u00e9st a <strong>20% NoRisk Free Bet</strong> v\u00e9delem aktiv\u00e1l\u00e1s\u00e1hoz.<br><br>T\u00f6ltsd fel a bankrollodat, n\u00e9zd meg a fel\u00e1ll\u00e1sokat \u00e9s tedd meg a t\u00e9tjeidet a <strong>Celsius Sport</strong>on biztons\u00e1gi h\u00e1l\u00f3val a h\u00e1tad m\u00f6g\u00f6tt.',
    'button_text_1': 'KAPD MEG A NORISK B\u00c9TED',
}

T[('Email 4C', 'hu-HU')] = {
    'subject': '\U0001f4a5 160% + 80 Spins: Kapd el \u00e9s \u00e9rezd a l\u00e1zat',
    'preheader': 'T\u00f6k\u00e9letes id\u0151z\u00edt\u00e9s a k\u00f6vetkez\u0151 nagy nyerem\u00e9nyedhez',
    'text_1_strong': '{{ customer.first_name | default:"J\u00e1t\u00e9kos" | capitalize }}, n\u00f6velj\u00fck a h\u0151fokot!',
    'text_2_p': 'Megvan az \u00f6szt\u00f6n\u00f6d - most csapj le, am\u00edg t\u00f6k\u00e9letes az id\u0151z\u00edt\u00e9s. Ig\u00e9nyelj <strong>160% bonus + 80 Free Spins</strong>t a <strong>Wild West Gold by Pragmatic Play</strong> j\u00e1t\u00e9kon \u00e9s turb\u00f3zd fel a k\u00f6vetkez\u0151 meneteidet.',
    'text_3_p': '\u00cdrd be a <strong class="promocode">GUNSLINGER160</strong> prom\u00f3k\u00f3dot a befizet\u00e9s el\u0151tt, hogy feloldd a <strong>160% bonus \u00e9s 80 Free Spins</strong>t. Azt\u00e1n ugorj egyenesen a <strong>Wild West Gold by Pragmatic Play</strong> j\u00e1t\u00e9kba.<br><br>A tekercsek k\u00e9szen \u00e1llnak a <strong>Celsius Casino</strong>ban - indulhat a nyer\u0151sorozat?',
    'button_text_1': 'TURB\u00d3ZD FEL A TEMP\u00d3D',
}

T[('Email 4S', 'hu-HU')] = {
    'subject': '\u26bd 170% Boost: A te j\u00e1t\u00e9kod, a te forgat\u00f3k\u00f6nyved',
    'preheader': 'Vedd \u00e1t az ir\u00e1ny\u00edt\u00e1st \u00e9s \u00edrd meg a saj\u00e1t t\u00f6rt\u00e9neted',
    'text_1_strong': '{{ customer.first_name | default:"Edz\u0151" | capitalize }}, te hat\u00e1rozol!',
    'text_2_p': 'Minden meccsnek van t\u00f6rt\u00e9nete - \u00e9s ma te \u00edrod. Hogy az els\u0151 s\u00edpsz\u00f3t\u00f3l az utols\u00f3 pillanatig t\u00e1mogasd a d\u00f6nt\u00e9seidet, a k\u00f6vetkez\u0151 meneted egy <strong>170% deposit bonus</strong>szal t\u00f6ltj\u00fck fel.',
    'text_3_p': 'Add meg a <strong class="promocode">SURGE170</strong> prom\u00f3k\u00f3dot a befizet\u00e9s el\u0151tt, hogy feloldd a <strong>170% deposit bonus</strong>t. Azt\u00e1n ir\u00e1ny a <strong>Celsius Sport</strong>, n\u00e9zd \u00e1t a piacokat \u00e9s \u00e1ll\u00edtsd \u00f6ssze a szelv\u00e9nyed a magad m\u00f3dj\u00e1n.<br><br>A t\u00e1bla \u00e9l - \u00e9s az el\u0151ny\u00f6d k\u00e9sz. Most \u00edrd meg az eredm\u00e9nyt.',
    'button_text_1': 'KAPD MEG A BONUSZOM',
}

T[('Email 5C', 'hu-HU')] = {
    'subject': '\U0001f3b0 170% Bonus: Azonnali felt\u00f6lt\u00e9s aktiv\u00e1lva',
    'preheader': 'Az utad a nagy nyerem\u00e9nyhez most sokkal gyorsabb lett',
    'text_1_strong': '{{ customer.first_name | default:"J\u00e1t\u00e9kos" | capitalize }}, k\u00e9sz\u00fclj a t\u00f6bbre!',
    'text_2_p': 'Amikor a j\u00e1t\u00e9kok beindulnak, a sebess\u00e9g sz\u00e1m\u00edt. Azonnal felt\u00f6lt\u00fcnk egy <strong>170% bonus</strong>t a k\u00f6vetkez\u0151 befizet\u00e9sedre - hogy a meneted gyorsabban \u00e9s messzebbre vigyen. Ne felejtsd el megadni a <strong class="promocode">BOOSTER170</strong> k\u00f3dot a befizet\u00e9s el\u0151tt.',
    'text_3_p': 'Tankold fel a sz\u00e1ml\u00e1dat \u00e9s n\u00e9zd, ahogy az egyenleged felsz\u00e1ll a <strong>Celsius Casino</strong>ban. <strong>170%</strong>-kal t\u00f6bbel tov\u00e1bb j\u00e1tszhatsz, kem\u00e9nyebben nyomhatod \u00e9s hajszolhatod a nagy szorz\u00f3kat.',
    'button_text_1': 'KEZDJ NYERNI MOST',
}

T[('Email 5S', 'hu-HU')] = {
    'subject': '\U0001f680 20% NoRisk Bet: Nyisd meg, aktiv\u00e1ld, nyerj',
    'preheader': 'K\u00e9sleked\u00e9s n\u00e9lk\u00fcl a legjobb akci\u00f3 kell\u0151s k\u00f6zep\u00e9be',
    'text_1_strong': '{{ customer.first_name | default:"J\u00e1t\u00e9kos" | capitalize }}, nincs vesztegetni val\u00f3 id\u0151!',
    'text_2_p': 'A legnagyobb pillanatok \u00e9l\u0151ben zajlanak - \u00e9s van egy gyorsabb \u00fat, hogy el\u0151nnyel sz\u00e1llj be a <strong>Celsius Sport</strong>on. Nincs v\u00e1rakoz\u00e1s, csak akci\u00f3 v\u00e9delemmel a j\u00e1t\u00e9kod m\u00f6g\u00f6tt.',
    'text_3_p': 'A gyors utad: n\u00e9zd meg az oddsokat, add meg a <strong class="promocode">WINSAFE20</strong> prom\u00f3k\u00f3dot a befizet\u00e9s el\u0151tt, majd aktiv\u00e1ld a <strong>20% NoRisk Free Bet</strong>edet. Ez <strong>20% NoRisk Free Bet</strong> v\u00e9delem a t\u00e9teden - ami v\u00e9gig magabiztos tart az els\u0151 v\u00e1laszt\u00e1st\u00f3l az utols\u00f3 s\u00edp sz\u00f3ig.<br><br>H\u00e1rom l\u00e9p\u00e9s. Egy el\u0151ny. Induljon a sorozatod.',
    'button_text_1': 'AKTIV\u00c1LD A NORISK B\u00c9TED',
}

T[('Email 6S', 'hu-HU')] = {
    'subject': '\u26a1 170% Boost: Szabad\u00edtsd fel az er\u0151t',
    'preheader': 'Turb\u00f3zd fel a nyer\u0151sorozatod extra t\u0171zer\u0151vel',
    'text_1_strong': '{{ customer.first_name | default:"Bajnok" | capitalize }}, l\u00e9pj a reflektorf\u00e9nybe!',
    'text_2_p': 'K\u00e9szen \u00e1llsz felp\u00f6rgetni az intenzit\u00e1st? A h\u00e9t legnagyobb meccseihez egy <strong>170% deposit bonus</strong> j\u00e1r, ami minden v\u00e1laszt\u00e1sodat megt\u00e1mogatja.',
    'text_3_p': 'A <strong>170% deposit bonus</strong> aktiv\u00e1l\u00e1s\u00e1hoz \u00edrd be a <strong class="promocode">BOOSTER170</strong> prom\u00f3k\u00f3dot a felt\u00f6lt\u00e9s el\u0151tt - a b\u00f3nuszod azonnal bet\u00f6lt\u0151dik.<br><br>Ak\u00e1r kombi fogad\u00e1sokat \u00e9p\u00edtesz, ak\u00e1r \u00e9les szingli t\u00e9teket teszel, az extra er\u0151 t\u00f6bb teret ad a strat\u00e9gi\u00e1dnak a <strong>Celsius Sport</strong>on. Vedd \u00e1t az ir\u00e1ny\u00edt\u00e1st \u00e9s engedd, hogy az el\u0151ny\u00f6d sz\u00e1rnyaljon a <strong>170%</strong>-kal.',
    'button_text_1': 'KAPD MEG A BONUSZOMAT',
}

T[('Email 7C', 'hu-HU')] = {
    'subject': '\u26a1 160% + 80 Free Spins: Aktiv\u00e1ld \u00e9s p\u00f6r\u00f6gj',
    'preheader': 'L\u00e9pj egyenesen a nyerem\u00e9nyek vil\u00e1g\u00e1ba',
    'text_1_strong': '{{ customer.first_name | default:"J\u00e1t\u00e9kos" | capitalize }}, mi\u00e9rt v\u00e1rn\u00e1l a sz\u00f3rakoz\u00e1ssal?',
    'text_2_p': 'Egyszer\u0171v\u00e9 tett\u00fck: aktiv\u00e1lod, p\u00f6rgetsz, hajszolod a nyerem\u00e9nyt. A k\u00f6vetkez\u0151 befizet\u00e9sed a <strong>Celsius Casino</strong>ban felold <strong>160% bonus + 80 Free Spins</strong>t a <strong>Wild West Gold by Pragmatic Play</strong> j\u00e1t\u00e9kon.',
    'text_3_p': 'Csak add meg a <strong class="promocode">GUNSLINGER160</strong> prom\u00f3k\u00f3dot a felt\u00f6lt\u00e9s el\u0151tt - semmi k\u00e9sleked\u00e9s, semmi extra l\u00e9p\u00e9s. Azt\u00e1n ir\u00e1ny a <strong>Wild West Gold by Pragmatic Play</strong> \u00e9s haszn\u00e1ld a <strong>80 Free Spins</strong>t a k\u00f6vetkez\u0151 nagy szorz\u00f3 vad\u00e1szat\u00e1hoz.',
    'button_text_1': 'AKTIV\u00c1LD A BONUSZOMAT',
}

T[('Email 7S', 'hu-HU')] = {
    'subject': '\u26a1 20% NoRisk Free Bet: A te el\u0151ny\u00f6d',
    'preheader': 'K\u00f6vesd a nyer\u0151 formul\u00e1t a prom\u00f3t\u00f3l a meccsig',
    'text_1_strong': '{{ customer.first_name | default:"J\u00e1t\u00e9kos" | capitalize }}, szerezd meg a sz\u00fcks\u00e9ges el\u0151nyt!',
    'text_2_p': 'Mi\u00e9rt b\u00edzn\u00e1d a v\u00e9letlenre, ha el\u0151nnyel is j\u00e1tszhatsz? Aktiv\u00e1ld a prom\u00f3dat, tedd meg a t\u00e9ted \u00e9s \u00e9lvezd a meccset v\u00e9delemmel a h\u00e1tad m\u00f6g\u00f6tt.',
    'text_3_p': 'Kezdd a <strong class="promocode">WINSAFE20</strong> prom\u00f3k\u00f3d megad\u00e1s\u00e1val, majd fizess be \u00e9s oldd fel a <strong>20% NoRisk Free Bet</strong>edet. Azt\u00e1n ir\u00e1ny a <strong>Celsius Sport</strong> \u00e9s v\u00e1laszd ki a helyed - a derbi, a taktikai csata vagy a k\u00f6telez\u0151 meccs.<br><br>A <strong>20% NoRisk Free Bet</strong> v\u00e9delemmel b\u00edzhatsz az \u00f6szt\u00f6neidben \u00e9s az ir\u00e1ny\u00edt\u00e1s a ti\u00e9d a kezd\u0151r\u00fag\u00e1st\u00f3l az utols\u00f3 percig.',
    'button_text_1': 'KAPD MEG AZ EL\u0150NY\u00d6M',
}

T[('Email 8C', 'hu-HU')] = {
    'subject': '\U0001f680 180% Bonus + 80 Free Spins: Fejleszd a l\u00e9p\u00e9sed',
    'preheader': 'N\u00e9zd meg, hogyan turb\u00f3zd fel a k\u00f6vetkez\u0151 befizet\u00e9sed',
    'text_1_strong': '{{ customer.first_name | default:"Bar\u00e1tom" | capitalize }}, itt az id\u0151 szintet l\u00e9pni!',
    'text_2_p': 'Ne csak csatlakozz a j\u00e1t\u00e9khoz - vedd \u00e1t az ir\u00e1ny\u00edt\u00e1st. A k\u00f6vetkez\u0151 befizet\u00e9sed komoly friss\u00edt\u00e9st kap: <strong>180% power-up + 80 Free Spins</strong> a <strong>Wanted Dead or a Wild by Hacksaw Gaming</strong> j\u00e1t\u00e9kban, ami azonnal beind\u00edtja a meneted.',
    'text_3_p': 'Kezdd a <strong class="promocode">OUTLAW180</strong> prom\u00f3k\u00f3d megad\u00e1s\u00e1val, majd fizess be \u00e9s ugorj be a <strong>Wanted Dead or a Wild by Hacksaw Gaming</strong> j\u00e1t\u00e9kba a <strong>Celsius Casino</strong>ban. A <strong>180% b\u00f3nuszod \u00e9s 80 Free Spins</strong>od az els\u0151 p\u00f6rg\u00e9st\u0151l k\u00e9sz.',
    'button_text_1': 'KAPD MEG A POWER-UP-OT',
}

T[('Email 9C', 'hu-HU')] = {
    'subject': '\U0001f48e 140% Bonus + 100 Free Spins: Mi\u00e9rt v\u00e1rn\u00e1l?',
    'preheader': 'Vedd \u00e1t a vezet\u00e9st \u00e9s biztos\u00edtsd be az extra es\u00e9lyeidet',
    'text_1_strong': '{{ customer.first_name | default:"Bar\u00e1tom" | capitalize }}, tedd legend\u00e1ss\u00e1 a napot.',
    'text_2_p': 'A "t\u00f6k\u00e9letes pillanat" nem j\u00f6n mag\u00e1t\u00f3l - te teremted meg. Ma az els\u0151 p\u00f6rg\u00e9st\u0151l nagyban mehetsz egy <strong>140% bonus + 100 Free Spins</strong>szel a <strong>Big Bamboo by Push Gaming</strong> j\u00e1t\u00e9kon. Csak add meg a <strong class="promocode">GIANTPANDA100</strong> k\u00f3dot, majd fejezd be a befizet\u00e9st.',
    'text_3_p': 'L\u00e9pj be a <strong>Celsius Casino</strong>ba felt\u00f6lt\u00f6tt egyenleggel \u00e9s <strong>100 Free Spins</strong>szel, ami azonnal t\u00fczel. J\u00e1tssz tov\u00e1bb, nyomj m\u00e9lyebbre \u00e9s hajszold a jackpotot val\u00f3di lend\u00fclettel.',
    'button_text_1': 'KAPD MEG A B\u00d3NUSZOM',
}

T[('Email 9S', 'hu-HU')] = {
    'subject': '\U0001f3be 30% NoRisk Bet: Okos n\u00e9z\u00e9s',
    'preheader': 'P\u00e1ros\u00edtsd a sportrajong\u00e1sod egy kock\u00e1zatmentes el\u0151nnyel',
    'text_1_strong': '{{ customer.first_name | default:"J\u00e1t\u00e9kos" | capitalize }}, itt az ideje j\u00e1tszani.',
    'text_2_p': 'Mi a legjobb m\u00f3dja a kedvenc sportod n\u00e9z\u00e9s\u00e9nek? Ha benne vagy a j\u00e1t\u00e9kban - \u00e9s v\u00e9delem van a t\u00e9teden. Ma <strong>30% NoRisk Free Bet</strong> v\u00e9delmet kapsz a <strong class="promocode">ONLYSAFE30</strong> k\u00f3ddal.',
    'text_3_p': 'Aktiv\u00e1ld a prom\u00f3t, v\u00e1laszd ki a piacodat \u00e9s j\u00e1tssz magabiztosan: add meg az <strong class="promocode">ONLYSAFE30</strong> k\u00f3dot, majd fejezd be a befizet\u00e9st \u00e9s oldd fel a <strong>30% NoRisk Free Bet</strong> v\u00e9delmet a mai akci\u00f3hoz.<br><br>A <strong>Celsius Sport</strong>on mi hozzuk a vonalakat - te hozod a strat\u00e9gi\u00e1t. Tedd meg a t\u00e9ted \u00e9s tedd k\u00fcl\u00f6nlegess\u00e9 ezt a meccset.',
    'button_text_1': 'KAPD MEG A NORISK B\u00c9TED',
}

T[('Email 10C', 'hu-HU')] = {
    'subject': '\u26a1 200 Free Spins: K\u00e9szen \u00e1llsz p\u00f6rgetni?',
    'preheader': 'Azonnali hozz\u00e1f\u00e9r\u00e9s a pr\u00e9mium slot jutalmadhoz',
    'text_1_strong': '{{ customer.first_name | default:"Bar\u00e1tom" | capitalize }}, itt a b\u00f3nuszod.',
    'text_2_p': 'A sz\u00f3rakoz\u00e1s\u00e9rt j\u00f6tt\u00e9l - mi pedig gyorsan int\u00e9zt\u00fck. A <strong>200 Free Spins</strong>ed a <strong>Gems Bonanza by Pragmatic Play</strong> j\u00e1t\u00e9kon a k\u00f6vetkez\u0151 befizet\u00e9seddel k\u00e9sz. Csak \u00edrd be a <strong class="promocode">GEMHUNT200</strong> prom\u00f3k\u00f3dot a befizet\u00e9s el\u0151tt \u00e9s ugorj egyenesen be.',
    'text_3_p': 'Nincs keresg\u00e9l\u00e9s, nincs macera - csak akci\u00f3 a <strong>Celsius Casino</strong>ban. T\u00f6ltsd fel, engedd, hogy hulljanak a dr\u00e1gak\u00f6vek \u00e9s hajszold azt a nagy pillanatot.',
    'button_text_1': 'KEZDJ P\u00d6RGETNI MOST',
}

T[('Email 10S', 'hu-HU')] = {
    'subject': '\U0001f4a5 30% NoRisk Free Bet: Kapd el \u00e9s urald a vonalat',
    'preheader': 'Egy okosabb fogad\u00e1si m\u00f3d a kedvenc sportjaidra',
    'text_1_strong': '{{ customer.first_name | default:"Bajnok" | capitalize }}, k\u00e9szen \u00e1llsz a kezd\u0151r\u00fag\u00e1sra?',
    'text_2_p': 'Tedd okoss\u00e1 a k\u00f6vetkez\u0151 fogad\u00e1sod - be\u00e9p\u00edtett v\u00e9delemmel. A <strong>30% NoRisk Free Bet</strong>ed most \u00e9l, \u00e9s t\u00f6bb szabads\u00e1got ad, hogy k\u00f6vesd a meg\u00e9rz\u00e9sedet.',
    'text_3_p': 'A lez\u00e1r\u00e1shoz \u00edrd be az <strong class="promocode">ONLYSAFE30</strong> prom\u00f3k\u00f3dot a befizet\u00e9s el\u0151tt a <strong>30% NoRisk Free Bet</strong> aktiv\u00e1l\u00e1s\u00e1hoz.<br><br>Ir\u00e1ny a <strong>Celsius Sport</strong>, n\u00e9zd \u00e1t a topm\u00e9rk\u0151z\u00e9seket, v\u00e1laszd ki a befut\u00f3kat \u00e9s j\u00e1tssz v\u00e9dett t\u00e9ttel. Gyors, egyszer\u0171 \u00e9s azonnal k\u00e9sz.',
    'button_text_1': 'AKTIV\u00c1LD \u00c9S J\u00c1TSSZ MOST',
}

# Winner emails HU (no text_3 - already translated team sig)
T[('Email 3C', 'hu-HU')] = {
    'subject': '\U0001f3a1 Menek\u00fclj a nyerem\u00e9nyekhez: A m\u00falt h\u00e9t sl\u00e1gerei',
    'preheader': 'Hagyd magad m\u00f6g\u00f6tt a vil\u00e1got \u00e9s l\u00e9pj a nyertesek k\u00f6z\u00e9',
    'text_1_strong': '{{ customer.first_name | default:"J\u00e1t\u00e9kos" | capitalize }}, k\u00e9szen \u00e1llsz a hangulat v\u00e1lt\u00e1sra?',
    'text_2_p': 'N\u00e9ha nem t\u00f6bb zajra van sz\u00fcks\u00e9ged - hanem egy jobb adrenalinfroccsr\u00e9. A <strong>Celsius Casino</strong>ban a topj\u00e1t\u00e9kosok nagyot kasz\u00e1ltak a m\u00falt h\u00e9ten:<br><br><strong>\U0001f3c6 Lu\u2022\u2022\u2022\u20227 - \u20ac52,300<br>\U0001f3c6 S\u2022\u2022\u2022\u2022\u2022n - \u20ac35,900<br>\U0001f3c6 Bi\u2022\u2022\u2022\u2022\u2022t - \u20ac19,400</strong><br><br>Az asztalok h\u00edvnak \u00e9s a nyer\u0151g\u00e9pek k\u00e9szen \u00e1llnak.<br>Kapcsold ki a stresszt \u00e9s kapcsold be az izgalmat a <strong>Celsius Casino</strong>ban - a helyed v\u00e1r.',
    'button_text_1': 'KEZDD EL A MENEK\u00dcL\u00c9SED MA',
}

T[('Email 3S', 'hu-HU')] = {
    'subject': '\U0001f3c6 Heti nyertesek: J\u00f3l d\u00f6nt\u00f6ttek',
    'preheader': 'N\u00e9zd, ki uralta a vonalakat ezen a h\u00e9ten a Celsius Sporton',
    'text_1_strong': '{{ customer.first_name | default:"Bajnok" | capitalize }}, te leszel a k\u00f6vetkez\u0151?',
    'text_2_p': 'Az elm\u00falt 7 nap a <strong>Celsius Sport</strong>on nagyot sz\u00f3lt. A leg\u00e9lesebb fogad\u00f3ink j\u00f3l olvastak \u00e9s hatalmas nyerem\u00e9nyeket vittek haza:<br><br><strong>\U0001f4b0 Str\u2022\u2022\u2022\u2022\u2022X - \u20ac42,810<br>\U0001f4b0 Go\u2022\u2022\u2022\u2022\u2022er - \u20ac31,200<br>\U0001f4b0 Pa\u2022\u2022\u2022\u2022\u2022ng - \u20ac19,450</strong><br><br>\u0150k nem csak n\u00e9zt\u00e9k - megtett\u00e9k a l\u00e9p\u00e9st.<br>A vonalak \u00e9l\u0151ben vannak a k\u00f6vetkez\u0151 meccsekre, sz\u00f3val v\u00e1laszd ki a helyed \u00e9s tedd meg a t\u00e9ted.<br>A te neved lehet a k\u00f6vetkez\u0151 ezen a list\u00e1n.',
    'button_text_1': '\u00c9L\u0150 ODDSOK MEGTEK INT\u00c9SE',
}

T[('Email 6C', 'hu-HU')] = {
    'subject': '\U0001f31f Csatlakozz az elithez: A h\u00e9t dics\u0151s\u00e9gfalja',
    'preheader': 'N\u00e9zd, ki uralta a t\u00e1rcs\u00e1kat \u00e9s foglald el a helyed a cs\u00facson',
    'text_1_strong': '{{ customer.first_name | default:"J\u00e1t\u00e9kos" | capitalize }}, el\u00e9rkezett a te id\u0151d!',
    'text_2_p': 'A lend\u00fclet elk\u00e9peszt\u0151 - \u00e9s a legnagyobb nyerem\u00e9nyek \u00e9ppen most t\u00f6rt\u00e9nnek a <strong>Celsius Casino</strong>ban. \u00cdme a legfrissebb bajnokok:<br><br><strong>\U0001f3c6 Ja\u2022\u2022\u2022\u2022g - \u20ac61,200<br>\U0001f3c6 Sp\u2022\u2022\u2022\u2022r - \u20ac42,800<br>\U0001f3c6 Eli\u2022\u2022\u2022\u2022er - \u20ac24,100</strong><br><br>A g\u00e9pek izzanak \u00e9s a k\u00e1rty\u00e1k kiosztva - a k\u00f6vetkez\u0151 f\u0151c\u00edm a ti\u00e9d lehet.<br>L\u00e9pj be, \u00e9lvezd az izgalmat \u00e9s j\u00e1tssz a <strong>Celsius Casino</strong>ban.',
    'button_text_1': 'KEZDD EL AZ UTADAT MOST',
}

T[('Email 8S', 'hu-HU')] = {
    'subject': '\U0001f3c6 Nagyot nyertek sportfogad\u00e1son - most rajtad a sor',
    'preheader': 'N\u00e9zd a h\u00e9t legjobb kifizet\u00e9seit \u00e9s v\u00e1laszd ki a nyer\u0151 meccsedet',
    'text_1_strong': '{{ customer.first_name | default:"Bajnok" | capitalize }}, a rangsor v\u00e1r!',
    'text_2_p': 'A m\u00falt h\u00e9ten ezek a j\u00e1t\u00e9kosok b\u00edztak a sz\u00e1mokban, elkaptk a megfelel\u0151 pillanatot \u00e9s nagyot kasz\u00e1ltak:<br><br><strong>\U0001f4b0 G\u2022\u2022\u2022\u2022er88 - \u20ac45,600<br>\U0001f4b0 O\u2022\u2022\u2022\u2022\u2022ero - \u20ac32,150<br>\U0001f4b0 Be\u2022\u2022\u2022\u2022rd - \u20ac18,700</strong><br><br>A t\u00e1bla friss\u00fclt \u00e9s a k\u00f6vetkez\u0151 meccsek \u00e9l\u0151ben vannak a <strong>Celsius Sport</strong>on. Az oddsok fent vannak, a piacok mozognak, \u00e9s ez a te ablakod.<br><br>V\u00e1laszd ki a meccsedet, b\u00edzz az \u00f6szt\u00f6neidben \u00e9s tedd meg a l\u00e9p\u00e9sedet - a te neved legyen a k\u00f6vetkez\u0151 a nyertesek list\u00e1j\u00e1n.',
    'button_text_1': 'V\u00c1LASSZ MECCSET \u00c9S FOGADJ',
}

# ==================== POLISH (pl-PL) ====================

T[('Email 1C', 'pl-PL')] = {
    'subject': '\U0001f4a5 170% Bonus: Wzmocnij swoj\u0105 gr\u0119 ju\u017c dzi\u015b',
    'preheader': 'Zobacz, co czeka na Ciebie przy sto\u0142ach',
    'text_1_strong': '{{ customer.first_name | default:"Gracz" | capitalize }}, parkiet jest Tw\u00f3j!',
    'text_2_p': 'Po co gra\u0107 tylko za wp\u0142at\u0119, skoro mo\u017cesz gra\u0107 z <strong>170%</strong> wi\u0119cej? Do\u0142adowujemy Twoje kolejne zasilenie, \u017ceby\u015b m\u00f3g\u0142 gra\u0107 d\u0142u\u017cej i goni\u0107 wi\u0119ksze wygrane.',
    'text_3_p': 'Wpisz kod <strong class="promocode">SURGE170</strong> przed nast\u0119pn\u0105 wp\u0142at\u0105, \u017ceby odblokowa\u0107 <strong>170% Bonus</strong> i zamieni\u0107 swoje saldo w prawdziw\u0105 przewag\u0119.<br><br>Akcja trwa w <strong>Celsius Casino</strong> - odbierz sw\u00f3j <strong>170% Bonus</strong>, wybierz ulubiony st\u00f3\u0142 i graj z pewno\u015bci\u0105 siebie.',
    'button_text_1': 'ZWI\u0118KSZ SWOJE SALDO',
}

T[('Email 1S', 'pl-PL')] = {
    'subject': '\U0001f94a 20% NoRisk Free Bet: Uderz mocno',
    'preheader': 'Linia otwarta - Twoja bezpieczna przewaga czeka',
    'text_1_strong': '{{ customer.first_name | default:"Mistrzu" | capitalize }}, zwyci\u0119stwo jest na wyci\u0105gni\u0119cie r\u0119ki!',
    'text_2_p': 'Nic nie bije dreszczu wygranego zak\u0142adu - dlatego wspieramy Tw\u00f3j nast\u0119pny ruch <strong>20% NoRisk Free Bet</strong>, \u017ceby\u015b m\u00f3g\u0142 gra\u0107 pewnie.',
    'text_3_p': 'Aby aktywowa\u0107, wpisz kod promocyjny <strong class="promocode">WINSAFE20</strong> przed nast\u0119pn\u0105 wp\u0142at\u0105. Tw\u00f3j <strong>20% NoRisk Free Bet</strong> b\u0119dzie gotowy do u\u017cycia od razu.<br><br>Sprawd\u017a najgor\u0119tsze mecze na <strong>Celsius Sport</strong>, postaw na ulubiony rynek i wykorzystaj szans\u0119, p\u00f3ki kursy s\u0105 na \u017cywo.',
    'button_text_1': 'ZABEZPIECZ M\u00d3J BONUS',
}

T[('Email 2C', 'pl-PL')] = {
    'subject': '\u26a1 150% + 70 Free Spins: Nie czekaj, zgarnij je',
    'preheader': 'Twoja kolejna wielka wygrana jest gotowa - a Ty?',
    'text_1_strong': '{{ customer.first_name | default:"Gracz" | capitalize }}, gry czekaj\u0105!',
    'text_2_p': 'Po co siedzie\u0107 z boku, skoro mo\u017cesz zbiera\u0107 wygrane? Wp\u0142a\u0107 teraz i wejd\u017a na wy\u017cszy poziom z <strong>150% bonus + 70 Free Spins</strong> w grze <strong>Chaos Crew II by Hacksaw Gaming</strong>.',
    'text_3_p': '\u017beby odblokowa\u0107, wpisz kod <strong class="promocode">CREWBOOST150</strong>, a potem doko\u0144cz wp\u0142at\u0119 - Tw\u00f3j <strong>150% bonus i 70 Free Spins</strong> czekaj\u0105 od pierwszego obrotu.<br><br>Akcja w <strong>Celsius Casino</strong> nie zwalnia. Wskocz do <strong>Chaos Crew II by Hacksaw Gaming</strong> i go\u0144 nast\u0119pne wielkie trafienie.',
    'button_text_1': 'ODBIERZ PODW\u00d3JN\u0104 NAGROD\u0118',
}

T[('Email 2S', 'pl-PL')] = {
    'subject': '\u26bd 20% NoRisk Free Bet: Czas na Prime Time',
    'preheader': 'Mecz dnia wzywa - wejd\u017a z ochron\u0105',
    'text_1_strong': '{{ customer.first_name | default:"Kibicu" | capitalize }}, \u015bwiat\u0142a si\u0119 zapali\u0142y!',
    'text_2_p': 'Prime Time nadchodzi - najwi\u0119kszy mecz dnia, wielkie napi\u0119cie i jeden moment mo\u017ce zmieni\u0107 wszystko. Wejd\u017a przed pierwszym gwizdkiem.',
    'text_3_p': '\u017beby wzmocni\u0107 dzisiejsz\u0105 akcj\u0119, odbierz sw\u00f3j <strong>20% NoRisk Free Bet</strong>: wpisz kod <strong class="promocode">WINSAFE20</strong>, a potem doko\u0144cz wp\u0142at\u0119, \u017ceby aktywowa\u0107 ochron\u0119 <strong>20% NoRisk Free Bet</strong>.<br><br>Do\u0142aduj bankroll, sprawd\u017a sk\u0142ady i postaw na <strong>Celsius Sport</strong> z siatk\u0105 bezpiecze\u0144stwa za plecami.',
    'button_text_1': 'ODBIERZ M\u00d3J NORISK BET',
}

T[('Email 4C', 'pl-PL')] = {
    'subject': '\U0001f4a5 160% + 80 Spins: Zgarnij i poczuj dreszcz',
    'preheader': 'Z\u0142ap idealny moment na kolejn\u0105 wielk\u0105 wygrn\u0105',
    'text_1_strong': '{{ customer.first_name | default:"Gracz" | capitalize }}, podkr\u0119\u0107my temperatur\u0119!',
    'text_2_p': 'Masz instynkt - teraz dzia\u0142aj, kiedy czas jest idealny. Odbierz <strong>160% bonus + 80 Free Spins</strong> w grze <strong>Wild West Gold by Pragmatic Play</strong> i wzmocnij swoj\u0105 nast\u0119pn\u0105 sesj\u0119.',
    'text_3_p': 'Wpisz kod <strong class="promocode">GUNSLINGER160</strong> przed wp\u0142at\u0105, \u017ceby odblokowa\u0107 <strong>160% bonus i 80 Free Spins</strong>. Potem wskakuj prosto w <strong>Wild West Gold by Pragmatic Play</strong>.<br><br>B\u0119bny s\u0105 gotowe w <strong>Celsius Casino</strong> - czas na seri\u0119 wygranych?',
    'button_text_1': 'WZMOCNIJ SWOJE TEMPO',
}

T[('Email 4S', 'pl-PL')] = {
    'subject': '\u26bd 170% Boost: Twoja gra, Tw\u00f3j scenariusz',
    'preheader': 'Przejmij kontrol\u0119 nad gr\u0105 i napisz swoj\u0105 histori\u0119',
    'text_1_strong': '{{ customer.first_name | default:"Trenerze" | capitalize }}, to Ty podejmujesz decyzje!',
    'text_2_p': 'Ka\u017cdy mecz ma swoj\u0105 histori\u0119 - a dzi\u015b to Ty j\u0105 piszesz. \u017beby wesprze\u0107 Twoje decyzje od pierwszego gwizdka do ko\u0144cowej akcji, do\u0142adowujemy nast\u0119pn\u0105 sesj\u0119 <strong>170% deposit bonus</strong>em.',
    'text_3_p': 'Wpisz kod <strong class="promocode">SURGE170</strong> przed wp\u0142at\u0105, \u017ceby odblokowa\u0107 <strong>170% deposit bonus</strong>. Potem kieruj si\u0119 na <strong>Celsius Sport</strong>, przejrzyj rynki i zbuduj sw\u00f3j kupon po swojemu.<br><br>Tablica jest na \u017cywo - a Twoja przewaga gotowa. Teraz napisz wynik.',
    'button_text_1': 'ODBIERZ M\u00d3J BONUS',
}

T[('Email 5C', 'pl-PL')] = {
    'subject': '\U0001f3b0 170% Bonus: Natychmiastowe do\u0142adowanie aktywowane',
    'preheader': 'Twoja droga do wielkiej wygranej w\u0142a\u015bnie przyspieszy\u0142a',
    'text_1_strong': '{{ customer.first_name | default:"Gracz" | capitalize }}, szykuj si\u0119 na wi\u0119cej!',
    'text_2_p': 'Kiedy gry s\u0105 rozgrzane, liczy si\u0119 szybko\u015b\u0107. Natychmiast \u0142adujemy <strong>170% bonus</strong> na Twoj\u0105 nast\u0119pn\u0105 wp\u0142at\u0119 - \u017ceby Twoja sesja posz\u0142a dalej i szybciej. Pami\u0119taj, \u017ceby wpisa\u0107 kod <strong class="promocode">BOOSTER170</strong> przed wp\u0142at\u0105.',
    'text_3_p': 'Do\u0142aduj konto i patrz, jak Twoje saldo startuje w <strong>Celsius Casino</strong>. Z <strong>170%</strong> wi\u0119cej mo\u017cesz gra\u0107 d\u0142u\u017cej, cisn\u0105\u0107 mocniej i goni\u0107 wielkie mno\u017cniki.',
    'button_text_1': 'ZACZNIJ WYGRYWA\u0106',
}

T[('Email 5S', 'pl-PL')] = {
    'subject': '\U0001f680 20% NoRisk Bet: Otw\u00f3rz, aktywuj, wygraj',
    'preheader': 'Przejd\u017a prosto do sedna akcji bez op\u00f3\u017anie\u0144',
    'text_1_strong': '{{ customer.first_name | default:"Gracz" | capitalize }}, nie ma czasu do stracenia!',
    'text_2_p': 'Najwi\u0119ksze momenty s\u0105 na \u017cywo - a jest szybszy spos\u00f3b, \u017ceby wej\u015b\u0107 z przewag\u0105 na <strong>Celsius Sport</strong>. Bez op\u00f3\u017anie\u0144, sama akcja z ochron\u0105 za Twoj\u0105 gr\u0105.',
    'text_3_p': 'Twoja szybka \u015bcie\u017cka: sprawd\u017a kursy, wpisz kod <strong class="promocode">WINSAFE20</strong> przed wp\u0142at\u0105 i aktywuj <strong>20% NoRisk Free Bet</strong>. To <strong>20% NoRisk Free Bet</strong> ochrona na Tw\u00f3j zak\u0142ad - \u017ceby\u015b czu\u0142 si\u0119 pewnie od pierwszego typowania do ostatniego gwizdka.<br><br>Trzy kroki. Jedna przewaga. Zaczynamy Twoj\u0105 seri\u0119.',
    'button_text_1': 'AKTYWUJ M\u00d3J NORISK BET',
}

T[('Email 6S', 'pl-PL')] = {
    'subject': '\u26a1 170% Boost: Uwolnij moc',
    'preheader': 'Do\u0142aduj swoj\u0105 seri\u0119 wygranych dodatkow\u0105 si\u0142\u0105 ognia',
    'text_1_strong': '{{ customer.first_name | default:"Mistrzu" | capitalize }}, wejd\u017a w \u015bwiat\u0142a reflektor\u00f3w!',
    'text_2_p': 'Gotowy podkr\u0119ci\u0107 intensywno\u015b\u0107? Najwi\u0119ksze mecze tego tygodnia id\u0105 w parze z <strong>170% deposit bonus</strong>em, kt\u00f3ry zasili ka\u017cdy Tw\u00f3j typ.',
    'text_3_p': '\u017beby aktywowa\u0107 <strong>170% deposit bonus</strong>, wpisz kod <strong class="promocode">BOOSTER170</strong> przed do\u0142adowaniem - Tw\u00f3j bonus \u0142aduje si\u0119 natychmiast.<br><br>Niezale\u017cnie czy budujesz multiki czy stawiasz na ostre singielki, dodatkowa moc daje Ci wi\u0119cej przestrzeni na strategi\u0119 na <strong>Celsius Sport</strong>. Przejmij kontrol\u0119 i pozw\u00f3l swojej przewadze wzrosn\u0105\u0107 z <strong>170%</strong>.',
    'button_text_1': 'ODBIERZ M\u00d3J BONUS',
}

T[('Email 7C', 'pl-PL')] = {
    'subject': '\u26a1 160% + 80 Free Spins: Aktywuj i kr\u0119\u0107',
    'preheader': 'Przejd\u017a prosto do wygrywania z natychmiastowymi nagrodami',
    'text_1_strong': '{{ customer.first_name | default:"Gracz" | capitalize }}, po co czeka\u0107 na zabaw\u0119?',
    'text_2_p': 'Zrobili\u015bmy to natychmiastowym: aktywujesz, kr\u0119cisz, gonisz wygrane. Twoja nast\u0119pna wp\u0142ata w <strong>Celsius Casino</strong> odblokowuje <strong>160% bonus + 80 Free Spins</strong> w grze <strong>Wild West Gold by Pragmatic Play</strong>.',
    'text_3_p': 'Wystarczy wpisa\u0107 kod <strong class="promocode">GUNSLINGER160</strong> przed do\u0142adowaniem - bez op\u00f3\u017anie\u0144, bez dodatkowych krok\u00f3w. Potem wskakuj w <strong>Wild West Gold by Pragmatic Play</strong> i u\u017cyj swoich <strong>80 Free Spins</strong>, \u017ceby polowa\u0107 na kolejny wielki mno\u017cnik.',
    'button_text_1': 'AKTYWUJ M\u00d3J BONUS',
}

T[('Email 7S', 'pl-PL')] = {
    'subject': '\u26a1 20% NoRisk Free Bet: Twoja przewaga',
    'preheader': 'Pod\u0105\u017caj za wygrywaj\u0105c\u0105 formu\u0142\u0105 od promo do meczu',
    'text_1_strong': '{{ customer.first_name | default:"Gracz" | capitalize }}, zdob\u0105d\u017a przewag\u0119, kt\u00f3rej potrzebujesz!',
    'text_2_p': 'Po co zostawia\u0107 to przypadkowi, skoro mo\u017cesz gra\u0107 z przewag\u0105? Aktywuj promo, postaw zak\u0142ad i ciesz si\u0119 meczem z ochron\u0105 za Twoj\u0105 gr\u0105.',
    'text_3_p': 'Zacznij od wpisania kodu <strong class="promocode">WINSAFE20</strong>, potem wp\u0142a\u0107 i odblokuj <strong>20% NoRisk Free Bet</strong>. Nast\u0119pnie kieruj si\u0119 na <strong>Celsius Sport</strong> i wybierz swoje miejsce - derby, taktyczne starcie lub mecz, kt\u00f3rego nie mo\u017cna przegapi\u0107.<br><br>Z ochron\u0105 <strong>20% NoRisk Free Bet</strong> mo\u017cesz zaufa\u0107 swoim instynktom i mie\u0107 kontrol\u0119 od pierwszego gwizdka do ostatniej minuty.',
    'button_text_1': 'ZDOB\u0104D\u0179 MOJ\u0104 PRZEWAG\u0118',
}

T[('Email 8C', 'pl-PL')] = {
    'subject': '\U0001f680 180% Bonus + 80 Free Spins: Ulepsz swoje wej\u015bcie',
    'preheader': 'Zobacz, jak wzmocni\u0107 nast\u0119pn\u0105 wp\u0142at\u0119 w kilku krokach',
    'text_1_strong': '{{ customer.first_name | default:"Przyjacielu" | capitalize }}, czas wej\u015b\u0107 na wy\u017cszy poziom!',
    'text_2_p': 'Nie tylko do\u0142\u0105cz do gry - przejmij kontrol\u0119. Twoja nast\u0119pna wp\u0142ata dostaje powa\u017cne ulepszenie: <strong>180% power-up + 80 Free Spins</strong> w grze <strong>Wanted Dead or a Wild by Hacksaw Gaming</strong>, \u017ceby szybko wystartowa\u0107 sesj\u0119.',
    'text_3_p': 'Zacznij od wpisania kodu <strong class="promocode">OUTLAW180</strong>, potem wp\u0142a\u0107 i wskocz do <strong>Wanted Dead or a Wild by Hacksaw Gaming</strong> w <strong>Celsius Casino</strong>. Tw\u00f3j <strong>180% boost i 80 Free Spins</strong> czekaj\u0105 od pierwszego obrotu.',
    'button_text_1': 'ODBIERZ M\u00d3J POWER-UP',
}

T[('Email 9C', 'pl-PL')] = {
    'subject': '\U0001f48e 140% Bonus + 100 Free Spins: Po co czeka\u0107?',
    'preheader': 'Przejmij prowadzenie i zabezpiecz dodatkowe szanse na wygrn\u0105',
    'text_1_strong': '{{ customer.first_name | default:"Przyjacielu" | capitalize }}, zr\u00f3b z tego dnia legend\u0119.',
    'text_2_p': '"Idealny moment" nie przychodzi sam - to Ty go tworzysz. Dzi\u015b graj wi\u0119ksz\u0105 stawk\u0105 od pierwszego obrotu z <strong>140% bonus + 100 Free Spins</strong> w grze <strong>Big Bamboo by Push Gaming</strong>. Wpisz kod <strong class="promocode">GIANTPANDA100</strong>, a potem doko\u0144cz wp\u0142at\u0119.',
    'text_3_p': 'Wejd\u017a do <strong>Celsius Casino</strong> z do\u0142adowanym saldem i <strong>100 Free Spins</strong> gotowymi do akcji. Graj d\u0142u\u017cej, si\u0119gaj g\u0142\u0119biej i go\u0144 jackpot z prawdziwym rozp\u0119dem.',
    'button_text_1': 'ZGARNIJ M\u00d3J BONUS',
}

T[('Email 9S', 'pl-PL')] = {
    'subject': '\U0001f3be 30% NoRisk Bet: M\u0105dre ogl\u0105danie',
    'preheader': 'Po\u0142\u0105cz pasj\u0119 do sportu z bezpieczn\u0105 przewag\u0105',
    'text_1_strong': '{{ customer.first_name | default:"Gracz" | capitalize }}, czas gra\u0107.',
    'text_2_p': 'Najlepszy spos\u00f3b na ogl\u0105danie ulubionego sportu? Z udzia\u0142em w grze - i ochron\u0105 na zak\u0142adzie. Dzi\u015b dostajesz <strong>30% NoRisk Free Bet</strong> z kodem <strong class="promocode">ONLYSAFE30</strong>.',
    'text_3_p': 'Aktywuj promo, wybierz rynek i graj pewnie: wpisz kod <strong class="promocode">ONLYSAFE30</strong>, doko\u0144cz wp\u0142at\u0119 i odblokuj ochron\u0119 <strong>30% NoRisk Free Bet</strong> na dzisiejsz\u0105 akcj\u0119.<br><br>Na <strong>Celsius Sport</strong> my dajemy linie - Ty dajesz strategi\u0119. Postaw zak\u0142ad i niech ten mecz b\u0119dzie wyj\u0105tkowy.',
    'button_text_1': 'ODBIERZ M\u00d3J NORISK BET',
}

T[('Email 10C', 'pl-PL')] = {
    'subject': '\u26a1 200 Free Spins: Gotowy do kr\u0119cenia?',
    'preheader': 'Natychmiastowy dost\u0119p do Twojej premiumowej nagrody slotowej',
    'text_1_strong': '{{ customer.first_name | default:"Przyjacielu" | capitalize }}, Tw\u00f3j bonus jest tutaj.',
    'text_2_p': 'Przyszed\u0142e\u015b po dreszcz emocji - my to przyspieszylimy. Twoje <strong>200 Free Spins</strong> w grze <strong>Gems Bonanza by Pragmatic Play</strong> czekaj\u0105 z nast\u0119pn\u0105 wp\u0142at\u0105. Wpisz kod <strong class="promocode">GEMHUNT200</strong> przed wp\u0142at\u0105 i wskakuj od razu.',
    'text_3_p': 'Bez szukania, bez komplikacji - sama akcja w <strong>Celsius Casino</strong>. Do\u0142aduj, pozw\u00f3l klejnotom spa\u015b\u0107 i go\u0144 ten wielki moment.',
    'button_text_1': 'ZACZNIJ KR\u0118CI\u0106',
}

T[('Email 10S', 'pl-PL')] = {
    'subject': '\U0001f4a5 30% NoRisk Free Bet: Zgarnij i rz\u0105d\u017a na linii',
    'preheader': 'M\u0105drzejszy spos\u00f3b na obstawianie ulubionych sport\u00f3w jest tutaj',
    'text_1_strong': '{{ customer.first_name | default:"Mistrzu" | capitalize }}, gotowy na pierwszy gwizdek?',
    'text_2_p': 'Zr\u00f3b z nast\u0119pnego zak\u0142adu m\u0105dry ruch - z wbudowan\u0105 ochron\u0105. Tw\u00f3j <strong>30% NoRisk Free Bet</strong> jest aktywny, daj\u0105c wi\u0119cej swobody, \u017ceby pod\u0105\u017ca\u0107 za instynktem.',
    'text_3_p': '\u017beby go zablokowa\u0107, wpisz kod <strong class="promocode">ONLYSAFE30</strong> przed wp\u0142at\u0105, \u017ceby aktywowa\u0107 <strong>30% NoRisk Free Bet</strong>.<br><br>Kieruj si\u0119 na <strong>Celsius Sport</strong>, przejrzyj topmecze, wybierz zwyci\u0119zc\u00f3w i graj z chronionym zak\u0142adem. Szybko, prosto i od razu gotowe.',
    'button_text_1': 'AKTYWUJ I GRAJ TERAZ',
}

# Winner emails PL (no text_3 - already translated team sig)
T[('Email 3C', 'pl-PL')] = {
    'subject': '\U0001f3a1 Uciekaj do wygranych: Hity zesz\u0142ego tygodnia',
    'preheader': 'Zostaw \u015bwiat za sob\u0105 i wkrocz do kr\u0119gu zwyci\u0119zc\u00f3w',
    'text_1_strong': '{{ customer.first_name | default:"Gracz" | capitalize }}, gotowy na zmian\u0119 klimatu?',
    'text_2_p': 'Czasem nie potrzebujesz wi\u0119cej ha\u0142asu - potrzebujesz lepszego dreszczu. W <strong>Celsius Casino</strong> topowi gracze zgarn\u0119li du\u017ce wygrane w zesz\u0142ym tygodniu:<br><br><strong>\U0001f3c6 Lu\u2022\u2022\u2022\u20227 - \u20ac52,300<br>\U0001f3c6 S\u2022\u2022\u2022\u2022\u2022n - \u20ac35,900<br>\U0001f3c6 Bi\u2022\u2022\u2022\u2022\u2022t - \u20ac19,400</strong><br><br>Sto\u0142y wzywaj\u0105, a sloty s\u0105 gotowe.<br>Wy\u0142\u0105cz stres i w\u0142\u0105cz emocje w <strong>Celsius Casino</strong> - Twoje miejsce czeka.',
    'button_text_1': 'ZACZNIJ SWOJ\u0104 UCIECZK\u0118',
}

T[('Email 3S', 'pl-PL')] = {
    'subject': '\U0001f3c6 Tygodniowi zwyci\u0119zcy: Trafili w dziesi\u0105tk\u0119',
    'preheader': 'Zobacz, kto dominowa\u0142 na liniach w tym tygodniu na Celsius Sport',
    'text_1_strong': '{{ customer.first_name | default:"Mistrzu" | capitalize }}, czy b\u0119dziesz nast\u0119pny?',
    'text_2_p': 'Ostatnie 7 dni na <strong>Celsius Sport</strong> by\u0142o wielkie. Nasi najlepsi typerzy trafili idealnie i zabrali do domu ogromne wyp\u0142aty:<br><br><strong>\U0001f4b0 Str\u2022\u2022\u2022\u2022\u2022X - \u20ac42,810<br>\U0001f4b0 Go\u2022\u2022\u2022\u2022\u2022er - \u20ac31,200<br>\U0001f4b0 Pa\u2022\u2022\u2022\u2022\u2022ng - \u20ac19,450</strong><br><br>Oni nie tylko ogl\u0105dali - postawili zak\u0142ad.<br>Linie s\u0105 na \u017cywo na kolejne mecze, wi\u0119c wybierz miejsce i postaw.<br>Twoje nazwisko mo\u017ce by\u0107 nast\u0119pne na tej li\u015bcie.',
    'button_text_1': 'SPRAWD\u0179 DZISIEJSZE KURSY',
}

T[('Email 6C', 'pl-PL')] = {
    'subject': '\U0001f31f Do\u0142\u0105cz do elity: Galeria s\u0142awy tego tygodnia',
    'preheader': 'Zobacz, kto zdominowa\u0142 b\u0119bny i zajmij swoje miejsce na szczycie',
    'text_1_strong': '{{ customer.first_name | default:"Gracz" | capitalize }}, to Tw\u00f3j czas, \u017ceby b\u0142yszzcze\u0107!',
    'text_2_p': 'Rozp\u0119d jest niesamowity - a najwi\u0119ksze wygrane dziej\u0105 si\u0119 w\u0142a\u015bnie teraz w <strong>Celsius Casino</strong>. Oto najnowsi mistrzowie:<br><br><strong>\U0001f3c6 Ja\u2022\u2022\u2022\u2022g - \u20ac61,200<br>\U0001f3c6 Sp\u2022\u2022\u2022\u2022r - \u20ac42,800<br>\U0001f3c6 Eli\u2022\u2022\u2022\u2022er - \u20ac24,100</strong><br><br>Automaty s\u0105 gor\u0105ce, a karty rozdane - nast\u0119pny nag\u0142\u00f3wek mo\u017ce by\u0107 Tw\u00f3j.<br>Wejd\u017a, poczuj emocje i graj w <strong>Celsius Casino</strong>.',
    'button_text_1': 'ROZPOCZNIJ SWOJ\u0104 PODR\u00d3\u017b',
}

T[('Email 8S', 'pl-PL')] = {
    'subject': '\U0001f3c6 Wygrali wielkie na sporcie - teraz Twoja kolej',
    'preheader': 'Zobacz topowe wyp\u0142aty tygodnia i wybierz sw\u00f3j zwyci\u0119ski mecz',
    'text_1_strong': '{{ customer.first_name | default:"Mistrzu" | capitalize }}, ranking czeka!',
    'text_2_p': 'W zesz\u0142ym tygodniu ci gracze zaufali liczbom, trafili idealny moment i zgarn\u0119li wielkie wygrane:<br><br><strong>\U0001f4b0 G\u2022\u2022\u2022\u2022er88 - \u20ac45,600<br>\U0001f4b0 O\u2022\u2022\u2022\u2022\u2022ero - \u20ac32,150<br>\U0001f4b0 Be\u2022\u2022\u2022\u2022rd - \u20ac18,700</strong><br><br>Tablica si\u0119 od\u015bwie\u017cy\u0142a i kolejne mecze s\u0105 na \u017cywo na <strong>Celsius Sport</strong>. Kursy s\u0105 aktualne, rynki si\u0119 ruszaj\u0105 i to jest Twoje okno.<br><br>Wybierz mecz, zaufaj instynktom i zr\u00f3b sw\u00f3j ruch - Twoje nazwisko powinno by\u0107 nast\u0119pne na li\u015bcie zwyci\u0119zc\u00f3w.',
    'button_text_1': 'WYBIERZ MECZ I OBSTAWIAJ',
}

# ==================== PROCESSING ====================

WINNER_EMAILS = {'Email 3C', 'Email 3S', 'Email 6C', 'Email 8S'}

def replace_strong_content(html, new_content):
    """Replace content inside the first <strong>...</strong> in text_1."""
    def repl(m):
        return m.group(1) + new_content + m.group(3)
    return re.sub(r'(<strong>)(.*?)(</strong>)', repl, html, count=1, flags=re.DOTALL)

def replace_p_content(html, new_content):
    """Replace content inside the first <p ...>...</p> in text_2/text_3."""
    def repl(m):
        return m.group(1) + new_content + m.group(3)
    return re.sub(r'(<p[^>]*>)(.*?)(</p>)', repl, html, count=1, flags=re.DOTALL)

changed = 0
skipped = 0
new_blocks = []

for block in blocks:
    lines = block.split('\n')
    d = {}
    for line in lines:
        idx = line.find(':')
        if idx > 0:
            k = line[:idx].strip()
            v = line[idx+1:].strip()
            d[k] = v
    
    name = d.get('name', '')
    locale = d.get('locale', '')
    key = (name, locale)
    
    if key not in T:
        new_blocks.append(block)
        if locale in ('hu-HU', 'pl-PL') and name:
            skipped += 1
            print(f"  SKIPPED (no translation): {name} | {locale}")
        continue
    
    trans = T[key]
    new_lines = []
    fields_changed = 0
    
    for line in lines:
        idx = line.find(':')
        if idx <= 0:
            new_lines.append(line)
            continue
        
        k = line[:idx].strip()
        v = line[idx+1:].strip()  # value after ": "
        prefix = line[:idx+2]     # "key: "
        
        if k == 'subject' and 'subject' in trans:
            new_lines.append(f'subject: {trans["subject"]}')
            fields_changed += 1
        elif k == 'preheader' and 'preheader' in trans:
            new_lines.append(f'preheader: {trans["preheader"]}')
            fields_changed += 1
        elif k == 'button_text_1' and 'button_text_1' in trans:
            new_lines.append(f'button_text_1: {trans["button_text_1"]}')
            fields_changed += 1
        elif k == 'text_1' and 'text_1_strong' in trans:
            new_v = replace_strong_content(v, trans['text_1_strong'])
            new_lines.append(f'text_1: {new_v}')
            fields_changed += 1
        elif k == 'text_2' and 'text_2_p' in trans:
            new_v = replace_p_content(v, trans['text_2_p'])
            new_lines.append(f'text_2: {new_v}')
            fields_changed += 1
        elif k == 'text_3' and 'text_3_p' in trans:
            new_v = replace_p_content(v, trans['text_3_p'])
            new_lines.append(f'text_3: {new_v}')
            fields_changed += 1
        else:
            new_lines.append(line)
    
    new_blocks.append('\n'.join(new_lines))
    changed += 1
    print(f"  OK: {name} | {locale} ({fields_changed} fields)")

# Reconstruct file
output = '\n\n'.join(new_blocks)
if le == '\r\n':
    output = output.replace('\n', '\r\n')

with open(FILE, 'w', encoding='utf-8') as f:
    f.write(output)

print(f"\nDone! Changed {changed} blocks, skipped {skipped}.")
print(f"Total translations in dict: {len(T)}")
