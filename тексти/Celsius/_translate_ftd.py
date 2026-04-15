#!/usr/bin/env python3
"""FTD Retention Flow - Translate hu-HU and pl-PL. 24 emails x 2 locales = 48 blocks."""
import re

FILE = r'c:\Projects\REPORTS\тексти\Celsius\FTD Retention Flow - Table data.txt'
with open(FILE, 'r', encoding='utf-8') as f:
    content = f.read()
le = '\r\n' if '\r\n' in content else '\n'
content = content.replace('\r\n', '\n')
blocks = content.split('\n\n')

# text_1 is same for ALL emails: Hello, {{customer.first_name | default:"friend"}}
TEXT1_HU = ' Szia, {{customer.first_name | default:"bar\u00e1tom"}}\U0001f44b '
TEXT1_PL = ' Cze\u015b\u0107, {{customer.first_name | default:"przyjacielu"}}\U0001f44b '

T = {}

# ===== HUNGARIAN (hu-HU) =====

T[('Email 1C', 'hu-HU')] = {
    'subject': '\U0001f40d A homok mozog - oldd fel a 100% + 50 FS-t',
    'preheader': 'A k\u00f6vetkez\u0151 befizet\u00e9si b\u00f3nuszod a Hand of Anubis j\u00e1t\u00e9kra k\u00e9sz',
    'text_2_p': 'Bel\u00e9pt\u00e9l a j\u00e1t\u00e9kba - most itt az id\u0151 m\u00e9lyebbre mer\u00fclni.<br><br>Haszn\u00e1ld a <strong class="promocode">ANUBIS10050</strong> k\u00f3dot a k\u00f6vetkez\u0151 befizet\u00e9sedn\u00e9l, hogy feloldd a <strong>100% bonus + 50 Free Spins</strong>t a <strong>Hand of Anubis</strong> <strong>by Hacksaw Gaming</strong> j\u00e1t\u00e9kban.<br><br>\u0150si er\u0151 tal\u00e1lkozik modern izgalommal - k\u00e9szen \u00e1llsz a p\u00f6rget\u00e9sre?',
    'button_text_1': 'KAPD MEG A B\u00d3NUSZOM',
}
T[('Email 1M', 'hu-HU')] = {
    'subject': '\U0001f3ae A k\u00f6vetkez\u0151 l\u00e9p\u00e9sed? Casino b\u00f3nusz vagy NoRisk sportfogad\u00e1s',
    'preheader': 'V\u00e1laszd ki, hogyan szeretn\u00e9d folytatni - p\u00f6rget\u00e9s, fogad\u00e1s vagy mindkett\u0151',
    'text_2_p': 'Megtetted az els\u0151 befizet\u00e9sedet - most tartsuk fenn a lend\u00fcletet.<br>\u00cdme, mi v\u00e1r az asztalon a k\u00f6vetkez\u0151 l\u00e9p\u00e9sedre:<br><br>A <strong>100% Bonus</strong> + <strong>50 Free Spins</strong> a <strong>Hand of Anubis by Hacksaw Gaming</strong> j\u00e1t\u00e9kban a kaszin\u00f3 rajong\u00f3knak - haszn\u00e1ld a <strong class="promocode">ANUBIS10050</strong> k\u00f3dot<br><strong></strong>A <strong>20% NoRisk FreeBet</strong> a k\u00f6vetkez\u0151 sportfogad\u00e1sodra - haszn\u00e1ld a <strong class="promocode">WINBACKNRF20</strong> k\u00f3dot<br><br><strong></strong>Dupl\u00e1zz a kaszin\u00f3ban vagy j\u00e1tssz okosan a sportfogad\u00e1sban - b\u00e1rmelyiket is v\u00e1lasztod, a h\u00e1tad m\u00f6g\u00f6tt vagyunk.',
    'button_text_1': 'J\u00c1TSSZ TOV\u00c1BB',
}
T[('Email 1S', 'hu-HU')] = {
    'subject': '\U0001f3c6 A 20% NoRisk FreeBet akt\u00edv neked',
    'preheader': 'Kapj vissza 20%-ot ha nem j\u00f6n be a fogad\u00e1sod - az els\u0151 befizet\u00e9sed ut\u00e1n',
    'text_2_p': 'Megtetted az els\u0151 befizet\u00e9sedet - most itt az id\u0151 okosan fogadni.<br>Haszn\u00e1ld a <strong class="promocode">WINBACKNRF20</strong> k\u00f3dot \u00e9s \u00e9lvezd a <strong>20% NoRisk FreeBet</strong>et a k\u00f6vetkez\u0151 fogad\u00e1sodon.<br><br>Ha az eredm\u00e9ny nem kedvez, visszakapod a t\u00e9t <strong>20%</strong>-\u00e1t az egyenlegedre.\u00a0<br>Ilyen egyszer\u0171.',
    'button_text_1': 'TEDD MEG A FREEB\u00c9TED',
}
T[('Email 2C', 'hu-HU')] = {
    'subject': '\U0001f3af A k\u00f6vetkez\u0151 p\u00f6rget\u00e9sed lehet a nagy',
    'preheader': 'M\u00e9g egy befizet\u00e9s \u00e9s az es\u00e9lyek melletted sz\u00f3lhatnak',
    'text_2_p': 'A tekercsek nem v\u00e1rnak - \u00e9s a nyerem\u00e9nyek sem.<br>Ezrek p\u00f6rgetnek minden \u00f3r\u00e1ban.\u00a0<br><br>N\u00e9h\u00e1nyan izgalommal t\u00e1voznak\u2026 m\u00e1sok jackpottal.<br>Csak a k\u00f6vetkez\u0151 befizet\u00e9sed kell, hogy visszaker\u00fclj a j\u00e1t\u00e9kba.<br>Semmi nyom\u00e1s - csak tiszta adrenalin.',
    'button_text_1': 'J\u00c1TSSZ \u00daJRA',
}
T[('Email 2M', 'hu-HU')] = {
    'subject': '\U0001f3af 100% + 60 FS vagy 20% NoRisk FreeBet - Te v\u00e1lasztasz',
    'preheader': 'Casino vagy Sport? Kapj p\u00e1ros\u00edtott b\u00f3nuszt + Free Spinst vagy j\u00e1tssz biztons\u00e1gban NoRiskkel',
    'text_2_p': 'Most, hogy az els\u0151 befizet\u00e9sed m\u00f6g\u00f6tted van - menj\u00fcnk tov\u00e1bb.<br>V\u00e1laszd ki, hogyan er\u0151s\u00edten\u00e9d a k\u00f6vetkez\u0151 j\u00e1t\u00e9kodat:<br><br>K\u00f3d <strong class="promocode">DOG10060</strong> -<strong> 100% Bonus</strong> + <strong>60 Free Spins </strong>a <strong>The Dog House Megaways by Pragmatic Play</strong> j\u00e1t\u00e9kban ha a t\u00e1rcs\u00e1kat p\u00f6rgeted<br>K\u00f3d <strong class="promocode">WINBACKNRF20</strong> -<strong> 20% NoRisk FreeBet</strong> ha a p\u00e1ly\u00e1n fogadsz<br><br>B\u00e1rmelyiket is v\u00e1lasztod, a k\u00f6vetkez\u0151 nyerem\u00e9nyed itt kezd\u0151dik.',
    'button_text_1': 'KAPD MEG A B\u00d3NUSZOM',
}
T[('Email 2S', 'hu-HU')] = {
    'subject': '\U0001f3af Nem j\u00f6tt be a fogad\u00e1s? Kapj vissza 20%-ot',
    'preheader': 'A 20% NoRisk FreeBeted \u00e9l - j\u00e1tssz tov\u00e1bb magabiztosan',
    'text_2_p': 'A sportban nem minden fogad\u00e1s j\u00f6n be - de mi a h\u00e1tad m\u00f6g\u00f6tt vagyunk.<br>Tedd meg a k\u00f6vetkez\u0151 fogad\u00e1sodat a <strong class="promocode">WINBACKNRF20</strong> k\u00f3ddal \u00e9s kapj <strong>20% NoRisk FreeBet</strong>et.<br><br>Ha nem j\u00f6n be, <strong>20%</strong>-ot visszakapod a sz\u00e1ml\u00e1dra.\u00a0<br>Semmi stressz, csak okos j\u00e1t\u00e9k.',
    'button_text_1': 'TEDD MEG A FREEB\u00c9TED',
}
T[('Email 3C', 'hu-HU')] = {
    'subject': '\U0001f353 140% + 50 FS - Csatlakozz a Fruit Partyhoz',
    'preheader': '\u00c9des\u00edtsd meg a k\u00f6vetkez\u0151 befizet\u00e9sedet ezzel a szaftos b\u00f3nusszal',
    'text_2_p': 'K\u00e9szen \u00e1llsz valami \u00e9desre?<br><br>Haszn\u00e1ld a <strong class="promocode">PARTY140</strong> k\u00f3dot a k\u00f6vetkez\u0151 befizet\u00e9sedn\u00e9l \u00e9s kapj <strong>140% bonus + 50 Free Spins</strong>t a <strong>Fruit Party</strong> <strong>by Pragmatic Play</strong> j\u00e1t\u00e9kban.<br><br>Ez a j\u00e1t\u00e9k tele van sz\u00ednnel - \u00e9s kifizet\u00e9si potenci\u00e1llal.<br>Induljon a p\u00f6rget\u00e9s!',
    'button_text_1': 'KAPD MEG A B\u00d3NUSZOM',
}
T[('Email 3M', 'hu-HU')] = {
    'subject': '\U0001f3af 2%/3%/4% Cashback + 20%/25%/30% NoRisk FreeBet',
    'preheader': 'Kapj extra jutalmat a kaszin\u00f3ban \u00e9s a sportban is',
    'text_2_p': 'A k\u00f6vetkez\u0151 befizet\u00e9sed kett\u0151s jutalmat old fel - b\u00e1rmit is j\u00e1tszol.<br><br>Haszn\u00e1ld a <strong class="promocode">SAFE2CB2</strong> / <strong class="promocode">RETURN3CB3</strong> / <strong class="promocode">BOOST4CB4 </strong>k\u00f3dot \u00e9s kapj:<br><strong>2%/3%/4% Cashback</strong>et a kaszin\u00f3 j\u00e1t\u00e9kodra<br><br>Vagy haszn\u00e1ld a <strong class="promocode">WINBACKNRF20</strong> / <strong class="promocode">SAFETYNRF25</strong> / <strong class="promocode">COVERNRF30 </strong>k\u00f3dot:<br><strong>20%/25%/30% NoRisk FreeBet</strong>et a sportfogad\u00e1saidra<br><br>Te v\u00e1lasztod, hogyan j\u00e1tszol - mi pedig gondoskodunk, hogy meg\u00e9rje.',
    'button_text_1': 'HASZN\u00c1LD A K\u00d3DOM',
}
T[('Email 3S', 'hu-HU')] = {
    'subject': '\U0001f9f2 20% NoRisk FreeBet - Maradj a j\u00e1t\u00e9kban',
    'preheader': 'Nyersz vagy nem, a k\u00f6vetkez\u0151 fogad\u00e1sod 20%-os v\u00e9delemmel j\u00f6n',
    'text_2_p': 'Az els\u0151 befizet\u00e9sed feloldott egy biztons\u00e1gi h\u00e1l\u00f3t - ne hagyd kihaszn\u00e1latlanul.<br><br>Haszn\u00e1ld a <strong class="promocode">WINBACKNRF20</strong> k\u00f3dot a <strong>20% NoRisk FreeBet</strong> aktiv\u00e1l\u00e1s\u00e1hoz \u00e9s tedd meg a k\u00f6vetkez\u0151 fogad\u00e1sodat, tudv\u00e1n, hogy fedez\u00fcnk, ha nem j\u00f6n be.\u00a0<br><br>Egyszer\u0171, okos \u00e9s probl\u00e9mamentes fogad\u00e1s.',
    'button_text_1': 'TEDD MEG A T\u00c9TED',
}
T[('Email 4C', 'hu-HU')] = {
    'subject': '\U0001f9c1 Legy\u00e9l teljesen dork - 110% + 50 FS v\u00e1r',
    'preheader': 'A Dork Unit egy b\u00f3nusszal v\u00e1r, ami kor\u00e1ntsem ostoba',
    'text_2_p': 'Feloldottad a hozz\u00e1f\u00e9r\u00e9st az egyik legfurcs\u00e1bb tal\u00e1lathoz.<br><br>Haszn\u00e1ld a <strong class="promocode">DORK50110</strong> k\u00f3dot a k\u00f6vetkez\u0151 befizet\u00e9sedn\u00e9l \u00e9s kapj <strong>110% bonus + 50 Free Spins</strong>t a <strong>Dork Unit</strong> <strong>by Hacksaw Gaming</strong> j\u00e1t\u00e9kban.<br><br>Ne t\u00e9vesszen meg a neve - ez a slot komoly nyer\u00e9si potenci\u00e1lt rejt.',
    'button_text_1': 'AKTIV\u00c1LD A B\u00d3NUSZOMAT',
}
T[('Email 4M', 'hu-HU')] = {
    'subject': '\U0001f4b8 M\u00falt h\u00e9ten $100,000+ -ot nyertek - Te is csatlakozol?',
    'preheader': 'N\u00e9zd meg a legfrissebb nagy nyerem\u00e9nyeket val\u00f3di j\u00e1t\u00e9kosokt\u00f3l',
    'text_2_p': 'A tekercsek forr\u00f3ak voltak a m\u00falt h\u00e9ten - \u00e9s \u00edme, kik profit\u00e1ltak a legt\u00f6bbet:<br><br><strong>l\u202288 $47,230-ot nyert a Sweet Bonanza j\u00e1t\u00e9kon</strong><br><strong>v\u202201 $35,910-ot \u00fct\u00f6tt a Money Train 3 j\u00e1t\u00e9kon</strong><br><strong>B\u2022in $18,450-ot kapott a Gates of Olympus j\u00e1t\u00e9kon</strong><br><br>Ezek val\u00f3di nyerem\u00e9nyek val\u00f3di j\u00e1t\u00e9kosokt\u00f3l, akik ugyan\u00fagy p\u00f6rgettek, mint te.<br>Sz\u00f3val\u2026 k\u00e9szen \u00e1llsz, hogy a te neved legyen a k\u00f6vetkez\u0151?',
    'button_text_1': 'P\u00d6RGESS \u00c9S NYERJ',
}
T[('Email 4S', 'hu-HU')] = {
    'subject': '\U0001f4bc 25% NoRisk FreeBet - Fedezve vagy',
    'preheader': 'Tedd meg a k\u00f6vetkez\u0151 fogad\u00e1sod \u00e9s kapj vissza 25%-ot ha nem j\u00f6n be',
    'text_2_p': 'M\u00e1r megtetted az els\u0151 befizet\u00e9sedet - most itt az id\u0151 magabiztosan fogadni.<br><br>Haszn\u00e1ld a <strong class="promocode">SAFETYNRF25</strong> k\u00f3dot a <strong>25% NoRisk FreeBet</strong> aktiv\u00e1l\u00e1s\u00e1hoz - a k\u00f6vetkez\u0151 fogad\u00e1sod biztons\u00e1gi h\u00e1l\u00f3val j\u00f6n. Ha az eredm\u00e9ny nem kedvez, visszakapod a t\u00e9ted <strong>25%</strong>-\u00e1t az egyenlegedre.',
    'button_text_1': 'TEDD MEG A FREEB\u00c9TED',
}
T[('Email 5C', 'hu-HU')] = {
    'subject': '\U0001f36d Kapj 100% + 80 FS-t a Sweet Bonanza j\u00e1t\u00e9kon',
    'preheader': 'A k\u00f6vetkez\u0151 befizet\u00e9si b\u00f3nuszod most sokkal \u00e9desebb lett',
    'text_2_p': 'K\u00e9sz\u00fclj a cukorsokksra.<br><br>Haszn\u00e1ld a <strong class="promocode">BONANZA10080</strong> k\u00f3dot a k\u00f6vetkez\u0151 befizet\u00e9sedn\u00e9l \u00e9s kapj <strong>100% bonus + 80 Free Spins</strong>t a <strong>Sweet Bonanza</strong> <strong>by Pragmatic Play</strong> j\u00e1t\u00e9kon.<br><br>Szaftos kifizet\u00e9sek, magas volatilit\u00e1s \u00e9s rengeteg meglep\u00e9t\u00e9s - mi nem tetszik?',
    'button_text_1': 'J\u00c1TSSZ SWEET BONANZA',
}
T[('Email 5M', 'hu-HU')] = {
    'subject': '\U0001fa99 100% + 70 FS vagy 20% NoRisk FreeBet - V\u00e1lassz',
    'preheader': 'Casino vagy sport - a m\u00e1sodik b\u00f3nuszod b\u00e1rmelyik \u00faton k\u00e9sz',
    'text_2_p': 'T\u00fal vagy az els\u0151 befizet\u00e9sen - most itt az id\u0151 er\u0151s\u00edteni a k\u00f6vetkez\u0151 l\u00e9p\u00e9sedet.<br>\u00cdme, mi v\u00e1r r\u00e1d:<br><br>\U0001f3b0 A <strong class="promocode">CHAOS10070</strong> k\u00f3ddal - <strong>100% Bonus</strong> + <strong>70 Free Spins </strong>a<strong> Chaos Crew II by Hacksaw Gaming</strong> j\u00e1t\u00e9kban a kaszin\u00f3 rajong\u00f3knak<br>\u26bd A <strong class="promocode">WINBACKNRF20</strong> k\u00f3ddal - <strong>20% NoRisk FreeBet</strong> ha az oddsok a tieid<br><br>B\u00e1rmelyik \u00faton j\u00e1tszol, van egy jutalom, ami a j\u00e1t\u00e9kodra szabott.',
    'button_text_1': 'V\u00c1LASZD KI A B\u00d3NUSZOM',
}
T[('Email 5S', 'hu-HU')] = {
    'subject': '\U0001f3c5 30% No Risk Only Win - Aktiv\u00e1lva',
    'preheader': 'J\u00e1tssz magabiztosan - a k\u00f6vetkez\u0151 fogad\u00e1sod 30%-os biztons\u00e1gi h\u00e1l\u00f3val j\u00f6n',
    'text_2_p': 'M\u00e1r megtetted az els\u0151 l\u00e9p\u00e9sedet - most l\u0151j magabiztosan.<br><br>\u00c9lvezd a <strong>30% No Risk Only Win</strong> b\u00f3nuszt a k\u00f6vetkez\u0151 sportfogad\u00e1sodon a <strong class="promocode">ONLYWIN30</strong> k\u00f3ddal.<br><br>Ha nem j\u00f6n be, visszakapod a t\u00e9ted <strong>30%</strong>-\u00e1t.\u00a0<br>Semmi nyom\u00e1s - csak tiszta j\u00e1t\u00e9k.',
    'button_text_1': 'TEDD MEG A FREEB\u00c9TED',
}
T[('Email 6C', 'hu-HU')] = {
    'subject': '\U0001f4dc 100% + 150 FS - L\u00e9pj be a Tome of Madness vil\u00e1g\u00e1ba',
    'preheader': 'Turb\u00f3zd a befizet\u00e9sedet \u00e9s p\u00f6rgesd v\u00e9gig a titkokat',
    'text_2_p': 'K\u00e9szen \u00e1llsz s\u00f6t\u00e9t kincsekre?<br><br>Haszn\u00e1ld a <strong class="promocode">RICH100150</strong> k\u00f3dot a k\u00f6vetkez\u0151 befizet\u00e9sedn\u00e9l \u00e9s kapj <strong>100% bonus + 150 Free Spins</strong>t a <strong>Rich Wilde and the Tome of Madness</strong> <strong>by Play\'n Go</strong> j\u00e1t\u00e9kban.<br><br>Titokzatos er\u0151. Misztikus szimb\u00f3lumok. V\u00e9gtelen kaland.',
    'button_text_1': 'KAPD MEG A FREE SPINSEIMET',
}
T[('Email 6M', 'hu-HU')] = {
    'subject': '\U0001f4b0 2%/3%/4% Cashback + 20%/25%/30% NoRisk FreeBet',
    'preheader': 'J\u00e1tssz okosan Cashbackkel a kaszin\u00f3ban \u00e9s NoRisk FreeBettel a sportban',
    'text_2_p': 'K\u00e9szen \u00e1llsz, hogy t\u00f6bbet hozzon minden p\u00f6rget\u00e9s \u00e9s fogad\u00e1s?\u00a0<br><br>A k\u00f6vetkez\u0151 befizet\u00e9sed a <strong class="promocode">SAFE2CB2</strong> / <strong class="promocode">RETURN3CB3</strong> / <strong class="promocode">BOOST4CB4</strong> k\u00f3ddal adja:<br><strong>2%/3%/4% Cashback</strong>et a kaszin\u00f3 j\u00e1t\u00e9kodra<br><br>Vagy haszn\u00e1ld a <strong class="promocode">WINBACKNRF20</strong> / <strong class="promocode">SAFETYNRF25</strong> / <strong class="promocode">COVERNRF30 </strong>k\u00f3dot \u00e9s kapj:<br><strong>20%/25%/30% NoRisk FreeBet</strong>et a sportfogad\u00e1saidra<br><br>Te hozod a j\u00e1t\u00e9kot - mi hozzuk az \u00e9rt\u00e9ket. A te st\u00edlusod, most fejlesztve.',
    'button_text_1': 'HASZN\u00c1LD A K\u00d3DOM',
}
T[('Email 6S', 'hu-HU')] = {
    'subject': '\U0001f501 20% NoRisk FreeBet - Engedd futni a k\u00f6vetkez\u0151t',
    'preheader': 'Nem j\u00f6tt be? Visszakapod a 20%-ot a k\u00f6vetkez\u0151 fogad\u00e1sodon',
    'text_2_p': 'Megtetted az els\u0151 fogad\u00e1sodat - most t\u00f6bb teret adunk, hogy mer\u00e9szen j\u00e1tssz.<br><br>Haszn\u00e1ld a <strong class="promocode">WINBACKNRF20</strong> k\u00f3dot a <strong>20% NoRisk FreeBet</strong> aktiv\u00e1l\u00e1s\u00e1hoz - a k\u00f6vetkez\u0151 fogad\u00e1sod be\u00e9p\u00edtett v\u00e9delemmel j\u00f6n.\u00a0<br><br>Ha az eredm\u00e9ny nem kedvez, visszakapod a t\u00e9ted <strong>20%</strong>-\u00e1t - ennyire egyszer\u0171.',
    'button_text_1': 'TEDD MEG A FREEB\u00c9TED',
}
T[('Email 7C', 'hu-HU')] = {
    'subject': '\U0001f525 A legnagyobb nyerem\u00e9nyek a k\u00f6vetkez\u0151 befizet\u00e9sb\u0151l j\u00f6ttek',
    'preheader': 'Te leszel a k\u00f6vetkez\u0151 nagy nyertes?',
    'text_2_p': 'A legnagyobb jackpot t\u00f6rt\u00e9neteink n\u00e9melyike egy k\u00f6vetkez\u0151 befizet\u00e9ssel kezd\u0151d\u00f6tt.<br><br>Nincs tr\u00fckk - csak egy \u00fajabb es\u00e9ly, hogy a kedvenc j\u00e1t\u00e9kaidat j\u00e1tszd \u00e9s elkapd azt az arany p\u00f6rget\u00e9st.<br><br>K\u00e9szen \u00e1llsz meg\u00edrni a saj\u00e1t nyer\u0151 t\u00f6rt\u00e9neted?',
    'button_text_1': 'VISSZAT\u00c9RTEM',
}
T[('Email 7M', 'hu-HU')] = {
    'subject': '\U0001f389 Nagy nyerem\u00e9nyek ebben a h\u00f3napban - T\u00f6bb mint $120,000 kifizetve',
    'preheader': 'Ezek a j\u00e1t\u00e9kosok nagyot nyertek - n\u00e9zd meg mit j\u00e1tszottak \u00e9s mennyit nyertek',
    'text_2_p': 'A sz\u00e1mok bej\u00f6ttek - \u00e9s ez a h\u00f3nap komoly nyerem\u00e9nyeket hozott:<br><br><strong>r\u2022y45 $50,780-ot nyert a The Dog House Megaways j\u00e1t\u00e9kon</strong><br><strong>Uncn $41,300-ot \u00fct\u00f6tt a Book of Dead j\u00e1t\u00e9kon</strong><br><strong>t\u20225s $31,920-ot kapott a Fruit Party j\u00e1t\u00e9kon</strong><br><br>\u0150k megtett\u00e9k a l\u00e9p\u00e9s\u00fcket - \u00e9s kifizet\u0151d\u00f6tt.\u00a0<br>Lehetne a k\u00f6vetkez\u0151 nagy pillanat a ti\u00e9d?',
    'button_text_1': 'J\u00c1TSSZ MOST',
}
T[('Email 7S', 'hu-HU')] = {
    'subject': '\U0001f3c1 A 20% NoRisk FreeBeted \u00e9l',
    'preheader': 'Tedd meg a k\u00f6vetkez\u0151 fogad\u00e1sod magabiztosan - 20% visszaj\u00f6n ha nem j\u00f6n be',
    'text_2_p': 'J\u00f3 h\u00edr - haszn\u00e1ld a <strong class="promocode">WINBACKNRF20</strong> k\u00f3dot a <strong>20% NoRisk FreeBet</strong>ed ig\u00e9nyl\u00e9s\u00e9hez.<br><br>Tedd meg a k\u00f6vetkez\u0151 sportfogad\u00e1sodat, \u00e9s ha nem j\u00f6n be, visszakapod a t\u00e9ted <strong>20%</strong>-\u00e1t az egyenlegedre.<br><br>Egyszer\u0171, okos \u00e9s arra tervezve, hogy benne tart a j\u00e1t\u00e9kban.',
    'button_text_1': 'TEDD MEG A FREEB\u00c9TED',
}
T[('Email 8C', 'hu-HU')] = {
    'subject': '\u26a1 150% + 30 FS - Szabad\u00edtsd el a Stormforged erej\u00e9t',
    'preheader': 'Csapj le kem\u00e9nyen a k\u00f6vetkez\u0151 befizet\u00e9si b\u00f3nuszoddal',
    'text_2_p': '\u00c9rzed a mennyg\u00f6rg\u00e9st? A <strong>Stormforged</strong> h\u00edv.<br><br>Haszn\u00e1ld a <strong class="promocode">FORGED150</strong> k\u00f3dot a k\u00f6vetkez\u0151 befizet\u00e9sedn\u00e9l, hogy feloldd a <strong>150% bonus + 30 Free Spins</strong>t a <strong>Stormforged by Hacksaw Gaming</strong> elektriz\u00e1l\u00f3 slotj\u00e1n.<br><br>Az istenek v\u00e1rnak - hozd a vihart.',
    'button_text_1': 'KAPD MEG A B\u00d3NUSZOM',
}
T[('Email 8M', 'hu-HU')] = {
    'subject': '\U0001f4b5 2%/3%/4% Cashback + 20%/25%/30% NoRisk FreeBet',
    'preheader': 'Turb\u00f3zd a kaszin\u00f3t \u00e9s a sportot egy l\u00e9p\u00e9sben',
    'text_2_p': 'A j\u00e1t\u00e9kod t\u00f6bbet \u00e9rdemel - \u00e9s ez a komb\u00f3 teljes\u00edti.<br><br>A k\u00f6vetkez\u0151 befizet\u00e9sedn\u00e9l haszn\u00e1ld a <strong class="promocode">SAFE2CB2</strong> / <strong class="promocode">RETURN3CB3</strong> / <strong class="promocode">BOOST4CB4</strong> k\u00f3dot \u00e9s oldd fel:<br><strong>2%/3%/4% Cashback</strong>et a kaszin\u00f3 j\u00e1t\u00e9kodra<br><br>Vagy haszn\u00e1ld a <strong class="promocode">WINBACKNRF20</strong> / <strong class="promocode">SAFETYNRF25</strong> / <strong class="promocode">COVERNRF30 </strong>k\u00f3dot \u00e9s kapj:<br><strong>20%/25%/30% NoRisk FreeBet</strong>et a sportfogad\u00e1saidra<br><br>Okos, rugalmas, \u00e9s arra tervezve, hogy a st\u00edlusod jutalmat kapjon.',
    'button_text_1': 'KAPD MEG A B\u00d3NUSZOM',
}
T[('Email 8S', 'hu-HU')] = {
    'subject': '\U0001f9f2 30% NoRisk FreeBet - A te el\u0151ny\u00f6d a k\u00f6vetkez\u0151 fogad\u00e1son',
    'preheader': 'Nem j\u00f6n be a k\u00f6vetkez\u0151 fogad\u00e1s? Semmi gond - visszakapod a t\u00e9ted 30%-\u00e1t',
    'text_2_p': 'Bel\u00e9pt\u00e9l a j\u00e1t\u00e9kba - most itt az id\u0151, hogy tov\u00e1bb menj extra v\u00e9delemmel.<br><br>Tedd meg a k\u00f6vetkez\u0151 sportfogad\u00e1sodat <strong>30% NoRisk FreeBet</strong>tel a <strong class="promocode">ONLYWIN30</strong> k\u00f3ddal.<br><br><strong></strong>Ha nem j\u00f6n be, visszakapod a t\u00e9ted <strong>30%</strong>-\u00e1t - k\u00e9rd\u00e9s n\u00e9lk\u00fcl.',
    'button_text_1': 'FOGADJ KOCK\u00c1ZAT N\u00c9LK\u00dcL',
}

# ===== POLISH (pl-PL) =====

T[('Email 1C', 'pl-PL')] = {
    'subject': '\U0001f40d Piaski si\u0119 przesuwaj\u0105 - odblokuj 100% + 50 FS',
    'preheader': 'Bonus za nast\u0119pn\u0105 wp\u0142at\u0119 na Hand of Anubis jest gotowy',
    'text_2_p': 'Wszed\u0142e\u015b do gry - teraz czas p\u00f3j\u015b\u0107 g\u0142\u0119biej.<br><br>U\u017cyj kodu <strong class="promocode">ANUBIS10050</strong> przy nast\u0119pnej wp\u0142acie, \u017ceby odblokowa\u0107 <strong>100% bonus + 50 Free Spins</strong> w grze <strong>Hand of Anubis</strong> <strong>by Hacksaw Gaming</strong>.<br><br>Staro\u017cytna moc spotyka nowoczesne emocje - gotowy do kr\u0119cenia?',
    'button_text_1': 'ODBIERZ M\u00d3J BONUS',
}
T[('Email 1M', 'pl-PL')] = {
    'subject': '\U0001f3ae Tw\u00f3j drugi krok? Bonus kasynowy lub NoRisk zak\u0142ad sportowy',
    'preheader': 'Wybierz, jak chcesz kontynuowa\u0107 - obroty, zak\u0142ady lub jedno i drugie',
    'text_2_p': 'Dokona\u0142e\u015b pierwszej wp\u0142aty - teraz utrzymajmy rozp\u0119d.<br>Oto, co czeka na Tw\u00f3j nast\u0119pny ruch:<br><br>A <strong>100% Bonus</strong> + <strong>50 Free Spins</strong> w <strong>Hand of Anubis by Hacksaw Gaming</strong> dla mi\u0142o\u015bnik\u00f3w kasyna - u\u017cyj kodu <strong class="promocode">ANUBIS10050</strong><br><strong></strong>A <strong>20% NoRisk FreeBet</strong> na Tw\u00f3j nast\u0119pny zak\u0142ad sportowy - u\u017cyj kodu <strong class="promocode">WINBACKNRF20</strong><br><br><strong></strong>Podw\u00f3j w kasynie lub graj m\u0105drze w zak\u0142adach sportowych - tak czy inaczej, masz nasze wsparcie.',
    'button_text_1': 'GRAJ DALEJ',
}
T[('Email 1S', 'pl-PL')] = {
    'subject': '\U0001f3c6 20% NoRisk FreeBet jest aktywny dla Ciebie',
    'preheader': 'Odzyskaj 20% je\u015bli zak\u0142ad nie wyjdzie - tylko po pierwszej wp\u0142acie',
    'text_2_p': 'Dokona\u0142e\u015b pierwszej wp\u0142aty - teraz czas obstawia\u0107 m\u0105drze.<br>U\u017cyj kodu <strong class="promocode">WINBACKNRF20</strong> i ciesz si\u0119 <strong>20% NoRisk FreeBet</strong> na nast\u0119pny zak\u0142ad.<br><br>Je\u015bli wynik nie b\u0119dzie po Twojej stronie, zwr\u00f3cimy <strong>20%</strong> na Twoje saldo.\u00a0<br>Tak prosto.',
    'button_text_1': 'POSTAW M\u00d3J FREEBET',
}
T[('Email 2C', 'pl-PL')] = {
    'subject': '\U0001f3af Tw\u00f3j nast\u0119pny obr\u00f3t mo\u017ce by\u0107 tym wielkim',
    'preheader': 'Jeszcze jedna wp\u0142ata i szanse mog\u0105 si\u0119 odwr\u00f3ci\u0107 na Twoj\u0105 korzy\u015b\u0107',
    'text_2_p': 'B\u0119bny nie czekaj\u0105 - i wygrane te\u017c nie.<br>Tysi\u0105ce graczy kr\u0119ci co godzin\u0119.\u00a0<br><br>Jedni odchodz\u0105 z dreszczem emocji\u2026 inni z jackpotem.<br>Twoja nast\u0119pna wp\u0142ata to wszystko, czego potrzebujesz, \u017ceby wr\u00f3ci\u0107 do gry.<br>Bez presji - czysta adrenalina.',
    'button_text_1': 'GRAJ PONOWNIE',
}
T[('Email 2M', 'pl-PL')] = {
    'subject': '\U0001f3af 100% + 60 FS lub 20% NoRisk FreeBet - Tw\u00f3j wyb\u00f3r',
    'preheader': 'Kasyno lub Sport? Odbierz dopasowany bonus + Free Spins lub graj bezpiecznie z NoRisk',
    'text_2_p': 'Teraz, kiedy pierwsza wp\u0142ata jest za Tob\u0105 - id\u017amy dalej.<br>Wybierz, jak chcesz wzmocni\u0107 swoj\u0105 nast\u0119pn\u0105 gr\u0119:<br><br>Kod <strong class="promocode">DOG10060</strong> -<strong> 100% Bonus</strong> + <strong>60 Free Spins </strong>w <strong>The Dog House Megaways by Pragmatic Play</strong> je\u015bli kr\u0119cisz b\u0119bnami<br>Kod <strong class="promocode">WINBACKNRF20</strong> -<strong> 20% NoRisk FreeBet</strong> je\u015bli obstawiasz na boisku<br><br>Bez wzgl\u0119du na wyb\u00f3r, Twoja nast\u0119pna wygrana zaczyna si\u0119 tutaj.',
    'button_text_1': 'ODBIERZ M\u00d3J BONUS',
}
T[('Email 2S', 'pl-PL')] = {
    'subject': '\U0001f3af Zak\u0142ad nie wyszed\u0142? Odzyskaj 20%',
    'preheader': 'Tw\u00f3j 20% NoRisk FreeBet jest aktywny - graj dalej z pewno\u015bci\u0105',
    'text_2_p': 'W sporcie nie ka\u017cdy zak\u0142ad trafia - ale my trzymamy Twoje plecy.<br>Postaw nast\u0119pny zak\u0142ad z kodem <strong class="promocode">WINBACKNRF20</strong> i odbierz <strong>20% NoRisk FreeBet</strong>.<br><br>Je\u015bli nie wyjdzie, zwr\u00f3cimy <strong>20%</strong> na Twoje konto.\u00a0<br>Bez stresu, sama m\u0105dra gra.',
    'button_text_1': 'POSTAW M\u00d3J FREEBET',
}
T[('Email 3C', 'pl-PL')] = {
    'subject': '\U0001f353 140% + 50 FS - Do\u0142\u0105cz do Fruit Party',
    'preheader': 'Os\u0142od\u017a swoj\u0105 nast\u0119pn\u0105 wp\u0142at\u0119 tym soczystym bonusem',
    'text_2_p': 'Gotowy na co\u015b s\u0142odkiego?<br><br>U\u017cyj kodu <strong class="promocode">PARTY140</strong> przy nast\u0119pnej wp\u0142acie i odbierz <strong>140% bonus + 50 Free Spins</strong> w grze <strong>Fruit Party</strong> <strong>by Pragmatic Play</strong>.<br><br>Ta gra p\u0119ka od kolor\u00f3w - i potencja\u0142u wyp\u0142at.<br>Niech b\u0119bny si\u0119 kr\u0119c\u0105!',
    'button_text_1': 'ZGARNIJ M\u00d3J BONUS',
}
T[('Email 3M', 'pl-PL')] = {
    'subject': '\U0001f3af 2%/3%/4% Cashback + 20%/25%/30% NoRisk FreeBet',
    'preheader': 'Odbierz wzmocnienie w kasynie i sporcie',
    'text_2_p': 'Twoja nast\u0119pna wp\u0142ata odblokowuje podw\u00f3jn\u0105 nagrod\u0119 - bez wzgl\u0119du na to, co grasz.<br><br>U\u017cyj kodu <strong class="promocode">SAFE2CB2</strong> / <strong class="promocode">RETURN3CB3</strong> / <strong class="promocode">BOOST4CB4 </strong>i odbierz:<br><strong>2%/3%/4% Cashback</strong> na gr\u0119 w kasynie<br><br>Lub u\u017cyj kodu <strong class="promocode">WINBACKNRF20</strong> / <strong class="promocode">SAFETYNRF25</strong> / <strong class="promocode">COVERNRF30 </strong>\u017ceby dosta\u0107:<br><strong>20%/25%/30% NoRisk FreeBet</strong> na zak\u0142ady sportowe<br><br>Ty wybierasz, jak grasz - a my zadbamy, \u017ceby to si\u0119 op\u0142aci\u0142o.',
    'button_text_1': 'U\u017bYJ MOJEGO KODU',
}
T[('Email 3S', 'pl-PL')] = {
    'subject': '\U0001f9f2 20% NoRisk FreeBet - Zosta\u0144 w grze',
    'preheader': 'Wygrasz czy nie, nast\u0119pny zak\u0142ad ma 20% ochrony',
    'text_2_p': 'Twoja pierwsza wp\u0142ata odblokowa\u0142a siatk\u0119 bezpiecze\u0144stwa - nie zmarnuj jej.<br><br>U\u017cyj kodu <strong class="promocode">WINBACKNRF20</strong>, \u017ceby aktywowa\u0107 <strong>20% NoRisk FreeBet</strong> i postaw nast\u0119pny zak\u0142ad wiedz\u0105c, \u017ce pokryjemy cz\u0119\u015b\u0107, je\u015bli nie wyjdzie.\u00a0<br><br>Proste, m\u0105dre i bezproblemowe obstawianie.',
    'button_text_1': 'POSTAW M\u00d3J ZAK\u0141AD',
}
T[('Email 4C', 'pl-PL')] = {
    'subject': '\U0001f9c1 B\u0105d\u017a totalnym dorkiem - 110% + 50 FS w \u015brodku',
    'preheader': 'Dork Unit czeka z bonusem, kt\u00f3ry wcale nie jest g\u0142upi',
    'text_2_p': 'Odblokowa\u0142e\u015b dost\u0119p do jednego z najbardziej niekonwencjonalnych hit\u00f3w.<br><br>U\u017cyj kodu <strong class="promocode">DORK50110</strong> przy nast\u0119pnej wp\u0142acie i odbierz <strong>110% bonus + 50 Free Spins</strong> w grze <strong>Dork Unit</strong> <strong>by Hacksaw Gaming</strong>.<br><br>Nie daj si\u0119 zmyli\u0107 nazw\u0105 - ten slot ma powa\u017cny potencja\u0142 wygranych.',
    'button_text_1': 'AKTYWUJ M\u00d3J BONUS',
}
T[('Email 4M', 'pl-PL')] = {
    'subject': '\U0001f4b8 Ponad $100,000 wygranych w zesz\u0142ym tygodniu - Do\u0142\u0105czysz do listy?',
    'preheader': 'Sprawd\u017a najnowsze du\u017ce wygrane od prawdziwych graczy',
    'text_2_p': 'B\u0119bny by\u0142y gor\u0105ce w zesz\u0142ym tygodniu - i oto kto skorzysta\u0142 najbardziej:<br><br><strong>l\u202288 wygra\u0142 $47,230 na Sweet Bonanza</strong><br><strong>v\u202201 trafi\u0142 $35,910 na Money Train 3</strong><br><strong>B\u2022in zgarno\u0105\u0142 $18,450 na Gates of Olympus</strong><br><br>To prawdziwe wygrane prawdziwych graczy, kt\u00f3rzy kr\u0119cili tak jak Ty.<br>Wi\u0119c\u2026 gotowy zobaczy\u0107 swoje imi\u0119 nast\u0119pne?',
    'button_text_1': 'KR\u0118\u0106 I WYGRYWAJ',
}
T[('Email 4S', 'pl-PL')] = {
    'subject': '\U0001f4bc 25% NoRisk FreeBet - Jeste\u015b zabezpieczony',
    'preheader': 'Postaw nast\u0119pny zak\u0142ad i odzyskaj 25% je\u015bli nie wyjdzie',
    'text_2_p': 'Ju\u017c dokona\u0142e\u015b pierwszej wp\u0142aty - teraz czas obstawia\u0107 z pewno\u015bci\u0105.<br><br>U\u017cyj kodu <strong class="promocode">SAFETYNRF25</strong>, \u017ceby aktywowa\u0107 <strong>25% NoRisk FreeBet</strong> - Tw\u00f3j nast\u0119pny zak\u0142ad ma siatk\u0119 bezpiecze\u0144stwa. Je\u015bli wynik nie b\u0119dzie po Twojej stronie, zwr\u00f3cimy <strong>25%</strong> Twojej stawki na saldo.',
    'button_text_1': 'POSTAW M\u00d3J FREEBET',
}
T[('Email 5C', 'pl-PL')] = {
    'subject': '\U0001f36d Odbierz 100% + 80 FS na Sweet Bonanza',
    'preheader': 'Bonus za nast\u0119pn\u0105 wp\u0142at\u0119 w\u0142a\u015bnie sta\u0142 si\u0119 du\u017co s\u0142odszy',
    'text_2_p': 'Przygotuj si\u0119 na cukrowy zastrzyk.<br><br>U\u017cyj kodu <strong class="promocode">BONANZA10080</strong> przy nast\u0119pnej wp\u0142acie i odbierz <strong>100% bonus + 80 Free Spins</strong> na <strong>Sweet Bonanza</strong> <strong>by Pragmatic Play</strong>.<br><br>Soczyste wyp\u0142aty, wysoka zmienno\u015b\u0107 i mn\u00f3stwo niespodzianek - co tu nie kocha\u0107?',
    'button_text_1': 'GRAJ W SWEET BONANZA',
}
T[('Email 5M', 'pl-PL')] = {
    'subject': '\U0001fa99 100% + 70 FS lub 20% NoRisk FreeBet - Wybierz',
    'preheader': 'Kasyno lub sport - Tw\u00f3j drugi bonus jest gotowy na ka\u017cd\u0105 gr\u0119',
    'text_2_p': 'Masz za sob\u0105 pierwsz\u0105 wp\u0142at\u0119 - teraz czas wzmocni\u0107 nast\u0119pny ruch.<br>Oto, co na Ciebie czeka:<br><br>\U0001f3b0 Z kodem <strong class="promocode">CHAOS10070</strong> - <strong>100% Bonus</strong> + <strong>70 Free Spins </strong>w<strong> Chaos Crew II by Hacksaw Gaming</strong> dla mi\u0142o\u015bnik\u00f3w kasyna<br>\u26bd Z kodem <strong class="promocode">WINBACKNRF20</strong> - <strong>20% NoRisk FreeBet</strong> je\u015bli wolisz kursy<br><br>Bez wzgl\u0119du na to, jak grasz, jest nagroda dopasowana do Twojej gry.',
    'button_text_1': 'WYBIERZ M\u00d3J BONUS',
}
T[('Email 5S', 'pl-PL')] = {
    'subject': '\U0001f3c5 30% No Risk Only Win - W\u0142\u0105czone',
    'preheader': 'Graj z pewno\u015bci\u0105 - Tw\u00f3j nast\u0119pny zak\u0142ad ma 30% siatk\u0119 bezpiecze\u0144stwa',
    'text_2_p': 'Ju\u017c zrobi\u0142e\u015b sw\u00f3j pierwszy ruch - teraz strzelaj z pewno\u015bci\u0105.<br><br>Ciesz si\u0119 bonusem <strong>30% No Risk Only Win</strong> na nast\u0119pny zak\u0142ad sportowy z kodem <strong class="promocode">ONLYWIN30</strong>.<br><br>Je\u015bli nie wyjdzie, zwr\u00f3cimy <strong>30%</strong> Twojej stawki.\u00a0<br>Bez presji - czysta gra.',
    'button_text_1': 'POSTAW M\u00d3J FREEBET',
}
T[('Email 6C', 'pl-PL')] = {
    'subject': '\U0001f4dc 100% + 150 FS - Wejd\u017a do Tome of Madness',
    'preheader': 'Do\u0142aduj swoj\u0105 wp\u0142at\u0119 i kr\u0119\u0107 przez sekrety',
    'text_2_p': 'Gotowy odkrywa\u0107 mroczne skarby?<br><br>U\u017cyj kodu <strong class="promocode">RICH100150</strong> przy nast\u0119pnej wp\u0142acie i odbierz <strong>100% bonus + 150 Free Spins</strong> w grze <strong>Rich Wilde and the Tome of Madness</strong> <strong>by Play\'n Go</strong>.<br><br>Tajemnicza moc. Mistyczne symbole. Nieko\u0144cz\u0105ca si\u0119 przygoda.',
    'button_text_1': 'ODBIERZ MOJE FREE SPINS',
}
T[('Email 6M', 'pl-PL')] = {
    'subject': '\U0001f4b0 2%/3%/4% Cashback + 20%/25%/30% NoRisk FreeBet',
    'preheader': 'Graj m\u0105drze z Cashback w kasynie i NoRisk FreeBet w sporcie',
    'text_2_p': 'Gotowy na wi\u0119cej z ka\u017cdego obrotu i zak\u0142adu?\u00a0<br><br>Twoja nast\u0119pna wp\u0142ata z kodem <strong class="promocode">SAFE2CB2</strong> / <strong class="promocode">RETURN3CB3</strong> / <strong class="promocode">BOOST4CB4</strong> daje:<br><strong>2%/3%/4% Cashback</strong> na gr\u0119 w kasynie<br><br>Lub u\u017cyj <strong class="promocode">WINBACKNRF20</strong> / <strong class="promocode">SAFETYNRF25</strong> / <strong class="promocode">COVERNRF30 </strong>i odbierz:<br><strong>20%/25%/30% NoRisk FreeBet</strong> na zak\u0142ady sportowe<br><br>Ty dajesz gr\u0119 - my dajemy warto\u015b\u0107. Tw\u00f3j styl, teraz ulepszony.',
    'button_text_1': 'U\u017bYJ MOJEGO KODU',
}
T[('Email 6S', 'pl-PL')] = {
    'subject': '\U0001f501 20% NoRisk FreeBet - Niech nast\u0119pny leci',
    'preheader': 'Nie trafi\u0142e\u015b? Zwr\u00f3cimy 20% na nast\u0119pny zak\u0142ad',
    'text_2_p': 'Postawi\u0142e\u015b sw\u00f3j pierwszy zak\u0142ad - teraz dajemy Ci wi\u0119cej miejsca na odwa\u017cn\u0105 gr\u0119.<br><br>U\u017cyj kodu <strong class="promocode">WINBACKNRF20</strong>, \u017ceby aktywowa\u0107 <strong>20% NoRisk FreeBet</strong> - Tw\u00f3j nast\u0119pny zak\u0142ad ma wbudowan\u0105 ochron\u0119.\u00a0<br><br>Je\u015bli wynik nie b\u0119dzie po Twojej stronie, zwr\u00f3cimy <strong>20%</strong> Twojej stawki - tak prosto.',
    'button_text_1': 'POSTAW M\u00d3J FREEBET',
}
T[('Email 7C', 'pl-PL')] = {
    'subject': '\U0001f525 Najwi\u0119ksze wygrane przysz\u0142y z nast\u0119pnych wp\u0142at',
    'preheader': 'Czy b\u0119dziesz nast\u0119pnym wielkim zwyci\u0119zc\u0105?',
    'text_2_p': 'Niekt\u00f3re z naszych najwi\u0119kszych historii jackpot\u00f3w zacz\u0119\u0142y si\u0119 od nast\u0119pnej wp\u0142aty.<br><br>Nie ma sztuczki - po prostu kolejna szansa na granie w ulubione gry i trafienie tego z\u0142otego obrotu.<br><br>Gotowy napisa\u0107 swoj\u0105 w\u0142asn\u0105 histori\u0119 wygranej?',
    'button_text_1': 'WRACAM DO GRY',
}
T[('Email 7M', 'pl-PL')] = {
    'subject': '\U0001f389 Wielkie wygrane w tym miesi\u0105cu - Ponad $120,000 wyp\u0142acone',
    'preheader': 'Ci gracze wygrali wielkie - zobacz, w co grali i ile wygrali',
    'text_2_p': 'Liczby s\u0105 jasne - i ten miesi\u0105c przyni\u00f3s\u0142 powa\u017cne wygrane:<br><br><strong>r\u2022y45 wygra\u0142 $50,780 na The Dog House Megaways</strong><br><strong>Uncn trafi\u0142 $41,300 na Book of Dead</strong><br><strong>t\u20225s zgarno\u0105\u0142 $31,920 na Fruit Party</strong><br><br>Oni postawili na swoim - i si\u0119 op\u0142aci\u0142o.\u00a0<br>Mo\u017ce nast\u0119pny wielki moment nale\u017cy do Ciebie?',
    'button_text_1': 'GRAJ TERAZ',
}
T[('Email 7S', 'pl-PL')] = {
    'subject': '\U0001f3c1 Tw\u00f3j 20% NoRisk FreeBet jest aktywny',
    'preheader': 'Postaw nast\u0119pny zak\u0142ad z pewno\u015bci\u0105 - 20% wraca je\u015bli nie trafi',
    'text_2_p': 'Dobra wiadomo\u015b\u0107 - u\u017cyj kodu <strong class="promocode">WINBACKNRF20</strong>, \u017ceby odebra\u0107 sw\u00f3j <strong>20% NoRisk FreeBet</strong>.<br><br>Postaw nast\u0119pny zak\u0142ad sportowy, a je\u015bli nie trafi, zwr\u00f3cimy <strong>20%</strong> Twojej stawki na saldo.<br><br>Proste, m\u0105dre i zaprojektowane, \u017ceby trzyma\u0107 Ci\u0119 w grze.',
    'button_text_1': 'POSTAW M\u00d3J FREEBET',
}
T[('Email 8C', 'pl-PL')] = {
    'subject': '\u26a1 150% + 30 FS - Uwolnij moc Stormforged',
    'preheader': 'Uderz mocno z bonusem za nast\u0119pn\u0105 wp\u0142at\u0119',
    'text_2_p': 'Czujesz grzmot? To <strong>Stormforged</strong> wzywa.<br><br>U\u017cyj kodu <strong class="promocode">FORGED150</strong> przy nast\u0119pnej wp\u0142acie, \u017ceby odblokowa\u0107 <strong>150% bonus + 30 Free Spins</strong> na elektryzuj\u0105cym slocie <strong>Stormforged by Hacksaw Gaming</strong>.<br><br>Bogowie czekaj\u0105 - sprowad\u017a burz\u0119.',
    'button_text_1': 'ODBIERZ M\u00d3J BONUS',
}
T[('Email 8M', 'pl-PL')] = {
    'subject': '\U0001f4b5 2%/3%/4% Cashback + 20%/25%/30% NoRisk FreeBet',
    'preheader': 'Wzmocnij kasyno i sport jednym ruchem',
    'text_2_p': 'Twoja gra zas\u0142uguje na wi\u0119cej - i to combo to dostarcza.<br><br>Przy nast\u0119pnej wp\u0142acie u\u017cyj kodu <strong class="promocode">SAFE2CB2</strong> / <strong class="promocode">RETURN3CB3</strong> / <strong class="promocode">BOOST4CB4</strong>, \u017ceby odblokowa\u0107:<br><strong>2%/3%/4% Cashback</strong> na gr\u0119 w kasynie<br><br>Lub u\u017cyj kodu <strong class="promocode">WINBACKNRF20</strong> / <strong class="promocode">SAFETYNRF25</strong> / <strong class="promocode">COVERNRF30 </strong>\u017ceby dosta\u0107:<br><strong>20%/25%/30% NoRisk FreeBet</strong> na Twoje nast\u0119pne zak\u0142ady sportowe<br><br>M\u0105dre, elastyczne i zaprojektowane, \u017ceby nagradza\u0107 Tw\u00f3j styl.',
    'button_text_1': 'ODBIERZ M\u00d3J BONUS',
}
T[('Email 8S', 'pl-PL')] = {
    'subject': '\U0001f9f2 30% NoRisk FreeBet - Twoja przewaga na nast\u0119pny zak\u0142ad',
    'preheader': 'Nast\u0119pny zak\u0142ad nie wyjdzie? Bez obaw - zwr\u00f3cimy 30% Twojej stawki',
    'text_2_p': 'Wszed\u0142e\u015b do gry - teraz czas i\u015b\u0107 dalej z dodatkowym zabezpieczeniem.<br><br>Postaw nast\u0119pny zak\u0142ad sportowy z <strong>30% NoRisk FreeBet</strong> z kodem <strong class="promocode">ONLYWIN30.</strong><br><br><strong></strong>Je\u015bli nie wyjdzie, dostaniesz <strong>30%</strong> stawki z powrotem - bez pyta\u0144.',
    'button_text_1': 'OBSTAWIAJ BEZ RYZYKA',
}

# ==================== PROCESSING ====================

def replace_strong_content(html, new_content):
    def repl(m): return m.group(1) + new_content + m.group(3)
    return re.sub(r'(<strong>)(.*?)(</strong>)', repl, html, count=1, flags=re.DOTALL)

def replace_p_content(html, new_content):
    def repl(m): return m.group(1) + new_content + m.group(3)
    return re.sub(r'(<p[^>]*>)(.*?)(</p>)', repl, html, count=1, flags=re.DOTALL)

changed = 0
new_blocks = []

for block in blocks:
    lines = block.split('\n')
    d = {}
    for line in lines:
        idx = line.find(':')
        if idx > 0:
            d[line[:idx].strip()] = line[idx+1:].strip()
    
    name = d.get('name', '')
    locale = d.get('locale', '')
    key = (name, locale)
    
    if key not in T:
        new_blocks.append(block)
        continue
    
    trans = T[key]
    t1_content = TEXT1_HU if locale == 'hu-HU' else TEXT1_PL
    new_lines = []
    fields_changed = 0
    
    for line in lines:
        idx = line.find(':')
        if idx <= 0:
            new_lines.append(line)
            continue
        k = line[:idx].strip()
        v = line[idx+1:].strip()
        
        if k == 'subject':
            new_lines.append(f'subject: {trans["subject"]}')
            fields_changed += 1
        elif k == 'preheader':
            new_lines.append(f'preheader: {trans["preheader"]}')
            fields_changed += 1
        elif k == 'button_text_1':
            new_lines.append(f'button_text_1: {trans["button_text_1"]}')
            fields_changed += 1
        elif k == 'text_1':
            new_v = replace_strong_content(v, t1_content)
            new_lines.append(f'text_1: {new_v}')
            fields_changed += 1
        elif k == 'text_2' and 'text_2_p' in trans:
            new_v = replace_p_content(v, trans['text_2_p'])
            new_lines.append(f'text_2: {new_v}')
            fields_changed += 1
        else:
            new_lines.append(line)
    
    new_blocks.append('\n'.join(new_lines))
    changed += 1
    print(f"  OK: {name} | {locale} ({fields_changed} fields)")

output = '\n\n'.join(new_blocks)
if le == '\r\n':
    output = output.replace('\n', '\r\n')
with open(FILE, 'w', encoding='utf-8') as f:
    f.write(output)

print(f"\nDone! Changed {changed} blocks. Dict has {len(T)} entries.")
