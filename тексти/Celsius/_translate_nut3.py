# -*- coding: utf-8 -*-
"""Translate Nutrition #3 - 24 emails × 2 locales (hu-HU, pl-PL).
Fields: subject, preheader, text_1 (greeting), text_2 (body inner HTML), button_text_1.
"""
import re, os, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

filepath = r'c:\Projects\REPORTS\тексти\Celsius\Nutrition #3 - Table data.txt'

T = {}

# ============ Email 1CL ============
T['Email 1CL'] = {
  'hu-HU': {
    'subject': '🎲 Turbózd a Live játékodat 150% Bónusszal',
    'preheader': 'A következő feltöltésed 150% extra zsetont hoz az asztalokra',
    'button_text_1': 'BÓNUSZ IGÉNYLÉSE',
    'greeting': ' {{ customer.first_name | default:"Barátom" | capitalize }}, a harmadik befizetésed az esélyed, hogy megfordítsd a játékot. ',
    'body': 'Töltsd fel most a <strong class="promocode">VAULT150</strong> kóddal és kapj <strong>150% bónuszt</strong>, hogy tovább játszhass, nagyobb téteket tehess és magasabbra célozz a Live Casino asztaloknál.<br><br>A nyerő helyed vár – tegyük emlékezetessé! ♠️<br><br>Növeld a készletedet:',
  },
  'pl-PL': {
    'subject': '🎲 Doładuj grę Live 150% Bonusem',
    'preheader': 'Twoje następne doładowanie daje 150% dodatkowych żetonów na stoły',
    'button_text_1': 'ODBIERZ BONUS',
    'greeting': ' {{ customer.first_name | default:"Przyjacielu" | capitalize }}, trzecia wpłata to Twoja szansa, by odwrócić karty. ',
    'body': 'Doładuj teraz kodem <strong class="promocode">VAULT150</strong> i odbierz <strong>150% bonus</strong>, żeby grać dłużej, obstawiać więcej i celować wyżej przy stołach Live Casino.<br><br>Twoje zwycięskie miejsce czeka – niech ta wpłata się liczy! ♠️<br><br>Zwiększ swój stos:',
  },
}

# ============ Email 1CS ============
T['Email 1CS'] = {
  'hu-HU': {
    'subject': '🎯 200% Bónusz + 50 IP: Háromszor annyi szerencse!',
    'preheader': 'Turbózd fel a játékod a harmadik befizetéssel és merülj el kedvenc nyerőgépeidben',
    'button_text_1': 'BÓNUSZ IGÉNYLÉSE',
    'greeting': ' {{ customer.first_name | default:"Barátom" | capitalize }}, a harmadik befizetésed lehet a legizgalmasabb eddig! ',
    'body': "Kapj <strong>200% bónuszt és 50 Ingyenes Pörgetést a Rich Wilde and the Tome of Madness</strong> by Play'n Go játékra.<br><br>Használd a <strong class=\"promocode\">OCCULT200</strong> kódot a titkok feloldásához. Ez a te pillanatod, hogy nagyobbat pörgess és a következő nagy nyereményre célozz! 🐙<br><br>Igényeld a háromszoros erősítésedet:",
  },
  'pl-PL': {
    'subject': '🎯 200% Bonus + 50 DS: Trzeci raz sztuka!',
    'preheader': 'Wzmocnij grę trzecią wpłatą i zanurz się w ulubionych slotach',
    'button_text_1': 'ODBIERZ BONUS',
    'greeting': ' {{ customer.first_name | default:"Przyjacielu" | capitalize }}, Twoja trzecia wpłata może być najbardziej ekscytująca! ',
    'body': "Odbierz <strong>200% bonus i 50 Darmowych Spinów na Rich Wilde and the Tome of Madness</strong> by Play'n Go.<br><br>Wpisz kod <strong class=\"promocode\">OCCULT200</strong>, żeby odblokować sekrety. To Twój moment, żeby kręcić śmielej i celować w wielką wygraną! 🐙<br><br>Odbierz potrójne wzmocnienie:",
  },
}

# ============ Email 1S ============
T['Email 1S'] = {
  'hu-HU': {
    'subject': '🏆 Készen állsz a harmadik nyerőszériádra?',
    'preheader': 'Fogadj okosan – nyerj akár €500-ig kockázatmentesen a következő befizetéssel',
    'button_text_1': 'TEDD MEG A FOGADÁSOD',
    'greeting': ' {{ customer.first_name | default:"Barátom" | capitalize }}, már bizonyítottad, hogy benne vagy a játékban. Most a harmadik befizetéssel tedd meg a döntő lépést. ',
    'body': 'Kapj <strong>20% Kockázatmentes Fogadásokat akár €500-ig</strong> a <strong class="promocode">STEADY20</strong> kóddal és emeld a tippjeidet a következő szintre.<br><br>A pálya a tied – készen állsz a nagy játékra? 🏟️<br><br>Tedd meg kockázatmentes fogadásodat:',
  },
  'pl-PL': {
    'subject': '🏆 Gotowy na trzecią serię wygranych?',
    'preheader': 'Obstawiaj mądrze – wygraj do €500 bez ryzyka przy następnej wpłacie',
    'button_text_1': 'POSTAW ZAKŁAD',
    'greeting': ' {{ customer.first_name | default:"Przyjacielu" | capitalize }}, już udowodniłeś, że jesteś w grze. Teraz trzecią wpłatą zrób decydujący ruch. ',
    'body': 'Odbierz <strong>20% Zakłady Bez Ryzyka do €500</strong> z kodem <strong class="promocode">STEADY20</strong> i przenieś swoje typy na wyższy poziom.<br><br>Boisko jest Twoje – gotowy na wielką grę? 🏟️<br><br>Postaw zakład bez ryzyka:',
  },
}

# ============ Email 2CL ============
T['Email 2CL'] = {
  'hu-HU': {
    'subject': '🏆 Live Casino legendák: A múlt hét top nyereményei',
    'preheader': 'Nézd, kik uralták az asztalokat – te leszel a következő?',
    'button_text_1': 'JÁTSZD ÉLŐ MOST',
    'greeting': ' {{ customer.first_name | default:"Barátom" | capitalize }}, a Live Casino asztalok lángoltak a múlt héten: ',
    'body': '<strong>🔥 Ln4s••• – €49,820</strong><br><strong>🔥 tin•••66 – €34,470</strong><br><strong>🔥 n•••tz – €25,960</strong><br><br>Három játékos, három hihetetlen menet – mind merész lépésekkel és okos játékkal. A neved ott lesz a jövő heti ranglistán?<br><br>Csatlakozz a győztesekhez:',
  },
  'pl-PL': {
    'subject': '🏆 Legendy Live Casino: Najlepsze wygrane zeszłego tygodnia',
    'preheader': 'Zobacz kto rządził przy stołach – może Ty będziesz następny?',
    'button_text_1': 'GRAJ NA ŻYWO',
    'greeting': ' {{ customer.first_name | default:"Przyjacielu" | capitalize }}, stoły Live Casino płonęły w zeszłym tygodniu: ',
    'body': '<strong>🔥 Ln4s••• – €49,820</strong><br><strong>🔥 tin•••66 – €34,470</strong><br><strong>🔥 n•••tz – €25,960</strong><br><br>Trzech graczy, trzy niesamowite serie – wszystko dzięki odważnym ruchom i mądrej grze. Twoje imię pojawi się na liście przyszłego tygodnia?<br><br>Dołącz do zwycięzców:',
  },
}

# ============ Email 2CS ============
T['Email 2CS'] = {
  'hu-HU': {
    'subject': '🏆 Nyerőgép bajnokok a múlt héten: Ki nyert nagyot?',
    'preheader': 'Ismerd meg a múlt hét legnagyobb nyerőgépes nyerteseit és a kifizetéseket',
    'button_text_1': 'PÖRGETÉS ÉS NYERÉS',
    'greeting': ' {{ customer.first_name | default:"Barátom" | capitalize }}, íme, hogyan jutalmazták a tárcsák a bajnokainkat: ',
    'body': '<strong>👑 mu••••n65 – €48,940</strong><br><strong>👑 Z3•••ky• – €36,280</strong><br><strong>👑 p••••sh – €29,760</strong><br><br>Minden pörgetésükkel számoltak – te is megteheted. A neved lesz a következő a listán?<br><br>Pörgess a dicsőségért:',
  },
  'pl-PL': {
    'subject': '🏆 Mistrzowie slotów w zeszłym tygodniu: Kto wygrał dużo?',
    'preheader': 'Poznaj największych zwycięzców slotów i zobacz wypłaty',
    'button_text_1': 'KRĘĆ I WYGRYWAJ',
    'greeting': ' {{ customer.first_name | default:"Przyjacielu" | capitalize }}, oto jak bębny nagrodziły naszych mistrzów: ',
    'body': '<strong>👑 mu••••n65 – €48,940</strong><br><strong>👑 Z3•••ky• – €36,280</strong><br><strong>👑 p••••sh – €29,760</strong><br><br>Każdy ich spin się liczył – Twój też może. Twoje imię będzie następne na liście?<br><br>Kręć po chwałę:',
  },
}

# ============ Email 2S ============
T['Email 2S'] = {
  'hu-HU': {
    'subject': '⚽ A következő nyereményed kockázatmentes lehet!',
    'preheader': 'Kapj 20% Kockázatmentes Fogadásokat akár €500-ig a harmadik befizetéssel',
    'button_text_1': 'FOGADJ MOST',
    'greeting': ' {{ customer.first_name | default:"Barátom" | capitalize }}, nagyszerűen játszottál eddig – most jön a harmadik forduló. ',
    'body': 'Tedd meg a harmadik befizetésedet, írd be a <strong class="promocode">STEADY20</strong> kódot és kapj <strong>20% Kockázatmentes Fogadásokat akár €500-ig</strong>. Egy elhibázott lövés sem lassít le.<br><br>Lépj a pályára és mutasd meg ki a főnök. 👟<br><br>Fogadj magabiztosan:',
  },
  'pl-PL': {
    'subject': '⚽ Twoja następna wygrana może być bez ryzyka!',
    'preheader': 'Odbierz 20% Zakłady Bez Ryzyka do €500 przy trzeciej wpłacie',
    'button_text_1': 'OBSTAWIAJ TERAZ',
    'greeting': ' {{ customer.first_name | default:"Przyjacielu" | capitalize }}, grałeś świetnie – teraz czas na trzecią rundę. ',
    'body': 'Dokonaj trzeciej wpłaty, wpisz kod <strong class="promocode">STEADY20</strong> i odbierz <strong>20% Zakłady Bez Ryzyka do €500</strong>. Nawet chybiony strzał Cię nie zatrzyma.<br><br>Wejdź na boisko i pokaż kto tu rządzi. 👟<br><br>Obstawiaj z pewnością:',
  },
}

# ============ Email 3CL ============
T['Email 3CL'] = {
  'hu-HU': {
    'subject': '🃏 Háromszorázd a zsetonjaidat + 50 Ingyenes Pörgetés!',
    'preheader': 'A Live Casino padló vár rád hatalmas bónusszal',
    'button_text_1': 'BÓNUSZ IGÉNYLÉSE',
    'greeting': ' {{ customer.first_name | default:"Barátom" | capitalize }}, lépj az akcióba és vidd tovább a játékodat. ',
    'body': "Fizess be most a <strong class=\"promocode\">OCCULT200</strong> kóddal és kapj <strong>200% bónuszt és 50 Ingyenes Pörgetést a Rich Wilde and the Tome of Madness</strong> by Play'n Go játékra, amit a kártyák után élvezhetsz.<br><br>A pillanatod itt van – játsszunk stílusosan. 🎩<br><br>Igényeld a kombinált csomagot:",
  },
  'pl-PL': {
    'subject': '🃏 Potrój żetony + 50 Darmowych Spinów!',
    'preheader': 'Podłoga Live Casino czeka na Ciebie z ogromnym bonusem',
    'button_text_1': 'ODBIERZ BONUS',
    'greeting': ' {{ customer.first_name | default:"Przyjacielu" | capitalize }}, wejdź do akcji i rozwiń swoją grę. ',
    'body': "Wpłać teraz z kodem <strong class=\"promocode\">OCCULT200</strong> i odbierz <strong>200% bonus i 50 Darmowych Spinów na Rich Wilde and the Tome of Madness</strong> by Play'n Go do zabawy po kartach.<br><br>Twój moment jest tu – grajmy z klasą. 🎩<br><br>Odbierz pakiet combo:",
  },
}

# ============ Email 3CS ============
T['Email 3CS'] = {
  'hu-HU': {
    'subject': '✨ Nagyot: 200% Bónusz + 50 IP',
    'preheader': 'Több egyenleg és több pörgetés a harmadik befizetéseddel',
    'button_text_1': 'BÓNUSZ IGÉNYLÉSE',
    'greeting': ' {{ customer.first_name | default:"Barátom" | capitalize }}, itt az ideje szintet lépni a játékodban. ',
    'body': "A harmadik befizetésed <strong>200% bónuszt és 50 Ingyenes Pörgetést a Rich Wilde and the Tome of Madness</strong> by Play'n Go játékra old fel.<br><br>Több egyenleg, több pörgetés és több esély az őrület felfedezésére. Írd be a <strong class=\"promocode\">OCCULT200</strong> kódot. 📖<br><br>Emeld az egyenlegedet:",
  },
  'pl-PL': {
    'subject': '✨ Na wielką skalę: 200% Bonus + 50 DS',
    'preheader': 'Więcej salda i więcej spinów z trzecią wpłatą',
    'button_text_1': 'ODBIERZ BONUS',
    'greeting': ' {{ customer.first_name | default:"Przyjacielu" | capitalize }}, czas podnieść poziom swojej gry. ',
    'body': "Trzecia wpłata odblokowuje <strong>200% bonus i 50 Darmowych Spinów na Rich Wilde and the Tome of Madness</strong> by Play'n Go.<br><br>Więcej salda, więcej spinów i więcej szans na odkrycie szaleństwa. Wpisz kod <strong class=\"promocode\">OCCULT200</strong>. 📖<br><br>Podnieś swoje saldo:",
  },
}

# ============ Email 3S ============
T['Email 3S'] = {
  'hu-HU': {
    'subject': '🏅 A harmadik befizetésed most még biztonságosabb',
    'preheader': 'Fogadj nagyot, kockáztass kevesebbet – akár €500-ig fedezünk',
    'button_text_1': 'TEDD MEG A FOGADÁSOD',
    'greeting': ' {{ customer.first_name | default:"Barátom" | capitalize }}, a nyerőszériád most kezdődik igazán. ',
    'body': 'A harmadik befizetéssel élvezd a <strong>20% Kockázatmentes Fogadásokat akár €500-ig</strong> – így merészen játszhatsz a tekintet nélkül. A kódod – <strong class="promocode">STEADY20</strong>.<br><br>Egy fogadás elég lehet. 🏆<br><br>Biztosítsd a fogadásodat:',
  },
  'pl-PL': {
    'subject': '🏅 Trzecia wpłata stała się bezpieczniejsza',
    'preheader': 'Obstawiaj dużo, ryzykuj mniej – zabezpieczamy do €500',
    'button_text_1': 'POSTAW ZAKŁAD',
    'greeting': ' {{ customer.first_name | default:"Przyjacielu" | capitalize }}, Twoja seria wygranych dopiero się rozkręca. ',
    'body': 'Przy trzeciej wpłacie ciesz się <strong>20% Zakładami Bez Ryzyka do €500</strong> – stawiaj odważnie bez oglądania się. Kod dla Ciebie – <strong class="promocode">STEADY20</strong>.<br><br>Jeden zakład może wystarczyć. 🏆<br><br>Zabezpiecz swój zakład:',
  },
}

# ============ Email 4CL ============
T['Email 4CL'] = {
  'hu-HU': {
    'subject': '🎯 170% Erősítés: Urald az asztalokat ma',
    'preheader': 'A következő kezed megváltoztathat mindent, több zsetonnal',
    'button_text_1': 'JÁTSZD ÉLŐ MOST',
    'greeting': ' {{ customer.first_name | default:"Barátom" | capitalize }}, ideje nagyobbat és merészebbet játszani. ',
    'body': 'Fizess be a <strong class="promocode">RISEUP170</strong> kóddal és kapj <strong>170% bónuszt</strong> a következő Live Casino session-ödre.<br><br>Több zseton azt jelenti, több esélyed van a játék megfordítására. 🔴⚫<br><br>Növeld a tétet:',
  },
  'pl-PL': {
    'subject': '🎯 170% Boost: Rządź przy stołach dziś',
    'preheader': 'Twoja następna ręka może zmienić wszystko z większą liczbą żetonów',
    'button_text_1': 'GRAJ NA ŻYWO',
    'greeting': ' {{ customer.first_name | default:"Przyjacielu" | capitalize }}, czas grać większe i odważniej. ',
    'body': 'Wpłać z kodem <strong class="promocode">RISEUP170</strong> i odbierz <strong>170% bonus</strong> na następną sesję Live Casino.<br><br>Więcej żetonów to więcej szans na odwrócenie gry na swoją korzyść. 🔴⚫<br><br>Zwiększ swoją stawkę:',
  },
}

# ============ Email 4CS ============
T['Email 4CS'] = {
  'hu-HU': {
    'subject': '🎰 3 Pörgetés, 3 Vagyon: Nézd meg a nyerteseket',
    'preheader': 'Nézd a múlt hét nyerőgép jackpot sztárjait és inspirálódj',
    'button_text_1': 'JÁTSSZ MOST',
    'greeting': ' {{ customer.first_name | default:"Barátom" | capitalize }}, a szerencse ezekre a játékosokra mosolygott a múlt héten: ',
    'body': '<strong>💎 a•••76 – €42,510</strong><br><strong>💎 fad•••77 – €29,930</strong><br><strong>💎 Gg••••h6 – €24,930</strong><br><br>Három pörgetés, három jackpot. A következő szerencsés sorozat a tiéd lehet?<br><br>Próbáld ki a szerencsédet:',
  },
  'pl-PL': {
    'subject': '🎰 3 Spiny, 3 Fortuny: Sprawdź zwycięzców',
    'preheader': 'Zobacz gwiazdy jackpotów na slotach i daj się zainspirować',
    'button_text_1': 'GRAJ TERAZ',
    'greeting': ' {{ customer.first_name | default:"Przyjacielu" | capitalize }}, szczęście uśmiechnęło się do tych graczy w zeszłym tygodniu: ',
    'body': '<strong>💎 a•••76 – €42,510</strong><br><strong>💎 fad•••77 – €29,930</strong><br><strong>💎 Gg••••h6 – €24,930</strong><br><br>Trzy spiny, trzy jackpoty. Może następna szczęśliwa seria będzie Twoja?<br><br>Sprawdź swoje szczęście:',
  },
}

# ============ Email 4S ============
T['Email 4S'] = {
  'hu-HU': {
    'subject': '🏅 Fogadj félelem nélkül: A harmadik befizetésed fedezve van',
    'preheader': 'Igényeld a 20% Kockázatmentes Fogadásokat akár €500-ig még ma',
    'button_text_1': 'KEZDJ FOGADNI',
    'greeting': ' {{ customer.first_name | default:"Barátom" | capitalize }}, a harmadik befizetésed extra magabiztossággal jár. ',
    'body': 'Kapj <strong>20% Kockázatmentes Fogadásokat akár €500-ig</strong> a <strong class="promocode">STEADY20</strong> kóddal és tedd, hogy minden tét számítson.<br><br>Nincs habozás, csak tiszta akció. 🔥<br><br>Kezdj biztonságosan fogadni:',
  },
  'pl-PL': {
    'subject': '🏅 Obstawiaj bez strachu: Trzecia wpłata zabezpieczona',
    'preheader': 'Odbierz 20% Zakłady Bez Ryzyka do €500 już dziś',
    'button_text_1': 'ZACZNIJ OBSTAWIAĆ',
    'greeting': ' {{ customer.first_name | default:"Przyjacielu" | capitalize }}, trzecia wpłata daje dodatkową pewność siebie. ',
    'body': 'Odbierz <strong>20% Zakłady Bez Ryzyka do €500</strong> z kodem <strong class="promocode">STEADY20</strong> i niech każdy zakład się liczy.<br><br>Żadnego wahania, czysta akcja. 🔥<br><br>Zacznij obstawiać bezpiecznie:',
  },
}

# ============ Email 5CL ============
T['Email 5CL'] = {
  'hu-HU': {
    'subject': '🏆 Ismerd meg a múlt hét Live Casino bajnokait',
    'preheader': '3 játékos. 3 hatalmas nyeremény. Te leszel a következő?',
    'button_text_1': 'JÁTSZD ÉLŐ MOST',
    'greeting': ' {{ customer.first_name | default:"Barátom" | capitalize }}, íme, kik hódították meg a Live Casino asztalokat a múlt héten: ',
    'body': '<strong>🥇 j89••• – €47,250</strong><br><strong>🥈 oz•••66z• – €36,180</strong><br><strong>🥉 R••••er – €24,940</strong><br><br>A tudásod téged tehet a következő nagy nyertessé – készen állsz elfoglalni a helyed?<br><br>Kihívás a dealernek:',
  },
  'pl-PL': {
    'subject': '🏆 Poznaj mistrzów Live Casino z zeszłego tygodnia',
    'preheader': '3 graczy. 3 ogromne wygrane. Twoja kolej?',
    'button_text_1': 'GRAJ NA ŻYWO',
    'greeting': ' {{ customer.first_name | default:"Przyjacielu" | capitalize }}, oto kto podbił stoły Live Casino w zeszłym tygodniu: ',
    'body': '<strong>🥇 j89••• – €47,250</strong><br><strong>🥈 oz•••66z• – €36,180</strong><br><strong>🥉 R••••er – €24,940</strong><br><br>Twoje umiejętności mogą Cię uczynić następnym wielkim zwycięzcą – gotowy zająć miejsce?<br><br>Wyzwij krupiera:',
  },
}

# ============ Email 5CS ============
T['Email 5CS'] = {
  'hu-HU': {
    'subject': '💎 A neved ott kell legyen a nyertesek listáján',
    'preheader': 'Nézd, hogyan nyertek nagyot a legújabb bajnokaink a múlt héten',
    'button_text_1': 'PÖRGETÉS ÉS NYERÉS',
    'greeting': ' {{ customer.first_name | default:"Barátom" | capitalize }}, a jackpot tábla kigyúlt a múlt héten: ',
    'body': '<strong>🔥 ozz – €49,210</strong><br><strong>🔥 Dts•• – €30,470</strong><br><strong>🔥 e•nz – €25,660</strong><br><br>Egyetlen szerencsés pörgetés kell – a te pillanatod lehet a következő. 🎰<br><br>Pörgess a jackpotért:',
  },
  'pl-PL': {
    'subject': '💎 Twoje imię powinno być na liście zwycięzców',
    'preheader': 'Zobacz jak nasi najnowsi mistrzowie wygrywali w zeszłym tygodniu',
    'button_text_1': 'KRĘĆ I WYGRYWAJ',
    'greeting': ' {{ customer.first_name | default:"Przyjacielu" | capitalize }}, tablica jackpotów zapłonęła w zeszłym tygodniu: ',
    'body': '<strong>🔥 ozz – €49,210</strong><br><strong>🔥 Dts•• – €30,470</strong><br><strong>🔥 e•nz – €25,660</strong><br><br>Wystarczy jeden szczęśliwy spin – Twój moment może być następny. 🎰<br><br>Kręć po jackpot:',
  },
}

# ============ Email 5S ============
T['Email 5S'] = {
  'hu-HU': {
    'subject': '🏟 Nézd meg a múlt hét sportfogadási bajnokait',
    'preheader': 'Fizess be harmadszor és csatlakozz a nyertesek listájához',
    'button_text_1': 'TEDD MEG A FOGADÁSOD',
    'greeting': ' {{ customer.first_name | default:"Barátom" | capitalize }}, a harmadik befizetésed extra magabiztossággal jár. ',
    'body': '<strong>💰 se••••9s – €48,200</strong><br><strong>💰 M87•••• – €32,900</strong><br><strong>💰 l••••na88 – €26,400</strong><br><br>A harmadik befizetésed lehet az, ami a nevedet ide juttatja a jövő héten. 🎫<br><br>Tedd meg a lépésedet:',
  },
  'pl-PL': {
    'subject': '🏟 Sprawdź mistrzów sportowych z zeszłego tygodnia',
    'preheader': 'Wpłać po raz trzeci i dołącz do listy zwycięzców',
    'button_text_1': 'POSTAW ZAKŁAD',
    'greeting': ' {{ customer.first_name | default:"Przyjacielu" | capitalize }}, trzecia wpłata daje dodatkową pewność. ',
    'body': '<strong>💰 se••••9s – €48,200</strong><br><strong>💰 M87•••• – €32,900</strong><br><strong>💰 l••••na88 – €26,400</strong><br><br>Trzecia wpłata może być tą, która umieści Twoje imię tutaj w przyszłym tygodniu. 🎫<br><br>Zrób swój ruch:',
  },
}

# ============ Email 6CL ============
T['Email 6CL'] = {
  'hu-HU': {
    'subject': '🎩 170% Erősítés a következő session-ödre',
    'preheader': 'Játssz Live Casino-ban extra erővel a harmadik befizetéssel',
    'button_text_1': 'BÓNUSZ IGÉNYLÉSE',
    'greeting': ' {{ customer.first_name | default:"Barátom" | capitalize }}, tegyük a harmadik befizetésedet felejthetetlenné. ',
    'body': 'Fizess be a <strong class="promocode">RISEUP170</strong> kóddal és kapj <strong>170% bónuszt</strong>, hogy tovább játszhass és nagyobb téteket tehess a Live asztaloknál.<br><br>A pillanatod most kezdődik. 🎲<br><br>Turbózd fel a játékodat:',
  },
  'pl-PL': {
    'subject': '🎩 170% Boost na następną sesję',
    'preheader': 'Graj w Live Casino z ekstra mocą na trzecią wpłatę',
    'button_text_1': 'ODBIERZ BONUS',
    'greeting': ' {{ customer.first_name | default:"Przyjacielu" | capitalize }}, Twoja trzecia wpłata niech będzie niezapomniana. ',
    'body': 'Wpłać z kodem <strong class="promocode">RISEUP170</strong> i odbierz <strong>170% bonus</strong>, żeby grać dłużej i obstawiać więcej przy stołach Live.<br><br>Twój moment zaczyna się teraz. 🎲<br><br>Doładuj swoją grę:',
  },
}

# ============ Email 6CS ============
T['Email 6CS'] = {
  'hu-HU': {
    'subject': '🪄 Varázslatos ajánlat: 200% Bónusz + 50 IP',
    'preheader': 'Több egyenleg és több pörgetés a harmadik befizetéssel',
    'button_text_1': 'BÓNUSZ IGÉNYLÉSE',
    'greeting': ' {{ customer.first_name | default:"Barátom" | capitalize }}, a harmadik befizetésed a jegyed a nagyobb izgalmakhoz. ',
    'body': "Kapj <strong>200% extra egyenleget és 50 Ingyenes Pörgetést a Rich Wilde and the Tome of Madness</strong> by Play'n Go játékra, hogy tovább pörögjön.<br><br>A kódod – <strong class=\"promocode\">OCCULT200</strong>. Minden pörgetés újabb esély valami látványosra. ✨<br><br>Oldd fel a varázslatot:",
  },
  'pl-PL': {
    'subject': '🪄 Magiczna oferta: 200% Bonus + 50 DS',
    'preheader': 'Więcej salda i więcej spinów na trzecią wpłatę',
    'button_text_1': 'ODBIERZ BONUS',
    'greeting': ' {{ customer.first_name | default:"Przyjacielu" | capitalize }}, trzecia wpłata to Twój bilet na większe emocje. ',
    'body': "Odbierz <strong>200% dodatkowego salda i 50 Darmowych Spinów na Rich Wilde and the Tome of Madness</strong> by Play'n Go, żeby bębny dalej się kręciły.<br><br>Twój kod – <strong class=\"promocode\">OCCULT200</strong>. Każdy spin to kolejna szansa na coś spektakularnego. ✨<br><br>Odblokuj magię:",
  },
}

# ============ Email 6S ============
T['Email 6S'] = {
  'hu-HU': {
    'subject': '🎯 Harmadik befizetés? Fedezünk!',
    'preheader': 'Fogadj 20% Kockázatmentes Fogadásokkal akár €500-ig most',
    'button_text_1': 'FOGADJ MOST',
    'greeting': ' {{ customer.first_name | default:"Barátom" | capitalize }}, tartsd a lendületet a harmadik befizetéssel. ',
    'body': 'Élvezd a <strong>20% Kockázatmentes Fogadásokat akár €500-ig</strong> a <strong class="promocode">STEADY20</strong> kóddal és fogadj gondolkodás nélkül.<br><br>Egy lépéssel közelebb a következő nagy nyereményhez. 🥅<br><br>Igényeld a fedezetedet:',
  },
  'pl-PL': {
    'subject': '🎯 Trzecia wpłata? Zabezpieczamy Cię!',
    'preheader': 'Obstawiaj z 20% Zakładami Bez Ryzyka do €500 teraz',
    'button_text_1': 'OBSTAWIAJ TERAZ',
    'greeting': ' {{ customer.first_name | default:"Przyjacielu" | capitalize }}, utrzymaj tempo trzecią wpłatą. ',
    'body': 'Ciesz się <strong>20% Zakładami Bez Ryzyka do €500</strong> z kodem <strong class="promocode">STEADY20</strong> i obstawiaj bez zastanowienia.<br><br>O krok bliżej następnej wielkiej wygranej. 🥅<br><br>Odbierz swoją ochronę:',
  },
}

# ============ Email 7CL ============
T['Email 7CL'] = {
  'hu-HU': {
    'subject': '💰 170% Bónusz + 30 Ingyenes Pörgetés benne van',
    'preheader': 'Vidd a Live játékodat a következő szintre és kapj extra pörgetéseket',
    'button_text_1': 'BÓNUSZ IGÉNYLÉSE',
    'greeting': ' {{ customer.first_name | default:"Barátom" | capitalize }}, itt az esélyed, hogy feltöltsd az egyenlegedet és élvezz néhány pörgetést utána. ',
    'body': 'Fizess be a <strong class="promocode">COWBOY170</strong> kóddal és kapj <strong>170% extra zsetont + 30 Ingyenes Pörgetést a Wild West Gold</strong> by Pragmatic Play játékra – a tökéletes keveréke a Live izgalomnak és a nyerőgépes szórakozásnak.<br><br>Az asztalok várnak – csatlakozol? 🌵<br><br>Igényeld a zsetonjaidat és pörgetéseidet:',
  },
  'pl-PL': {
    'subject': '💰 170% Bonus + 30 Darmowych Spinów w środku',
    'preheader': 'Przenieś grę Live na wyższy poziom i odbierz dodatkowe spiny',
    'button_text_1': 'ODBIERZ BONUS',
    'greeting': ' {{ customer.first_name | default:"Przyjacielu" | capitalize }}, oto Twoja szansa, by doładować saldo i cieszyć się spinami. ',
    'body': 'Wpłać z kodem <strong class="promocode">COWBOY170</strong> i odbierz <strong>170% dodatkowych żetonów + 30 Darmowych Spinów na Wild West Gold</strong> by Pragmatic Play – idealne połączenie emocji Live i zabawy na slotach.<br><br>Stoły czekają – dołączysz? 🌵<br><br>Odbierz żetony i spiny:',
  },
}

# ============ Email 7CS ============
T['Email 7CS'] = {
  'hu-HU': {
    'subject': '🎲 Fejlesztett bónusz: 170% + 30 Ingyenes Pörgetés',
    'preheader': 'A harmadik befizetésed most Wild West erősítéssel jön',
    'button_text_1': 'BÓNUSZ IGÉNYLÉSE',
    'greeting': ' {{ customer.first_name | default:"Barátom" | capitalize }}, a harmadik befizetésed most seriff jelvénnyel jár: ',
    'body': 'Kapj <strong>170% extrát + 30 Ingyenes Pörgetést a Wild West Gold</strong> by Pragmatic Play játékra a <strong class="promocode">COWBOY170</strong> kóddal.<br><br>A szaloon ajtók nyitva állnak és a tárcsák várnak – készen állsz felvenni velük a harcot? 🤠<br><br>Nyeregbe a nyereményekért:',
  },
  'pl-PL': {
    'subject': '🎲 Ulepszony bonus: 170% + 30 Darmowych Spinów',
    'preheader': 'Trzecia wpłata teraz z power-upem z Dzikiego Zachodu',
    'button_text_1': 'ODBIERZ BONUS',
    'greeting': ' {{ customer.first_name | default:"Przyjacielu" | capitalize }}, trzecia wpłata teraz z odznaką szeryfa: ',
    'body': 'Odbierz <strong>170% ekstra + 30 Darmowych Spinów na Wild West Gold</strong> by Pragmatic Play z kodem <strong class="promocode">COWBOY170</strong>.<br><br>Drzwi salonu są otwarte, a bębny czekają – gotowy się z nimi zmierzyć? 🤠<br><br>Ruszaj po wygrane:',
  },
}

# ============ Email 7S ============
T['Email 7S'] = {
  'hu-HU': {
    'subject': '🏇 A harmadik befizetésed: Menj végig',
    'preheader': '20% Kockázatmentes Fogadások – félelem nélkül, minden izgalommal fogadj',
    'button_text_1': 'TEDD MEG A FOGADÁSOD',
    'greeting': ' {{ customer.first_name | default:"Barátom" | capitalize }}, a verseny még nem ért véget. ',
    'body': 'Tedd meg a harmadik befizetésedet és kapj <strong>20% Kockázatmentes Fogadásokat akár €500-ig</strong> a <strong class="promocode">STEADY20</strong> kóddal.<br><br>Legyen foci, tenisz vagy verseny – a nyerőszériád most indul. 🏎️<br><br>Indítsd be a motort:',
  },
  'pl-PL': {
    'subject': '🏇 Trzecia wpłata: Na całego',
    'preheader': '20% Zakłady Bez Ryzyka – bez strachu, sam dreszczyk na zakładach',
    'button_text_1': 'POSTAW ZAKŁAD',
    'greeting': ' {{ customer.first_name | default:"Przyjacielu" | capitalize }}, wyścig jeszcze się nie skończył. ',
    'body': 'Dokonaj trzeciej wpłaty i odbierz <strong>20% Zakłady Bez Ryzyka do €500</strong> z kodem <strong class="promocode">STEADY20</strong>.<br><br>Czy to piłka nożna, tenis czy wyścigi – Twoja wygrana jazda zaczyna się teraz. 🏎️<br><br>Odpal silnik:',
  },
}

# ============ Email 8CL ============
T['Email 8CL'] = {
  'hu-HU': {
    'subject': '🎲 170% Erősítés a Live Casino uralmához',
    'preheader': 'Több zseton. Több esély. Több nyeremény a harmadik befizetéssel',
    'button_text_1': 'CSATLAKOZZ AZ ASZTALHOZ',
    'greeting': ' {{ customer.first_name | default:"Barátom" | capitalize }}, a harmadik befizetés a pillanatod a nagy dobásra. ',
    'body': 'Fizess be a <strong class="promocode">RISEUP170</strong> kóddal és kapj <strong>170% extra zsetont</strong>, hogy nagyobbat játszhass, tovább kitarts és a csúcsra célozz.<br><br>A helyed kész – az akció most kezdődik. 🚀<br><br>Csatlakozz a nagymenőkhöz:',
  },
  'pl-PL': {
    'subject': '🎲 170% Boost by rządzić w Live Casino',
    'preheader': 'Więcej żetonów. Więcej szans. Więcej wygranych na trzecią wpłatę',
    'button_text_1': 'DOŁĄCZ DO STOŁU',
    'greeting': ' {{ customer.first_name | default:"Przyjacielu" | capitalize }}, trzecia wpłata to Twój moment na wielki cios. ',
    'body': 'Wpłać z kodem <strong class="promocode">RISEUP170</strong> i odbierz <strong>170% dodatkowych żetonów</strong>, żeby grać większe, wytrzymać dłużej i celować na szczyt.<br><br>Twoje miejsce gotowe – akcja rusza teraz. 🚀<br><br>Dołącz do highrollerów:',
  },
}

# ============ Email 8CS ============
T['Email 8CS'] = {
  'hu-HU': {
    'subject': '🏺 200% Bónusz + 50 IP a Tome of Madness-en',
    'preheader': 'Lépj be a sírokba és igényeld a kincseidet a harmadik befizetéssel',
    'button_text_1': 'BÓNUSZ IGÉNYLÉSE',
    'greeting': ' {{ customer.first_name | default:"Barátom" | capitalize }}, a következő pörgetésed felfedezhet ősi kincseket. ',
    'body': "Tedd meg a harmadik befizetésedet a <strong class=\"promocode\">OCCULT200</strong> kóddal és kapj <strong>200% bónuszt + 50 Ingyenes Pörgetést a Rich Wilde and the Tome of Madness</strong> by Play'n Go játékra.<br><br>Itt az ideje, hogy felfedezd a sírokat és igényeld, ami a tied. 👁️<br><br>Indítsd el a kalandot:",
  },
  'pl-PL': {
    'subject': '🏺 200% Bonus + 50 DS na Tome of Madness',
    'preheader': 'Wejdź do grobowca i zgarnij skarby na trzecią wpłatę',
    'button_text_1': 'ODBIERZ BONUS',
    'greeting': ' {{ customer.first_name | default:"Przyjacielu" | capitalize }}, Twój następny spin może odkryć starożytne bogactwa. ',
    'body': "Dokonaj trzeciej wpłaty z kodem <strong class=\"promocode\">OCCULT200</strong> i odbierz <strong>200% bonus + 50 Darmowych Spinów na Rich Wilde and the Tome of Madness</strong> by Play'n Go.<br><br>Czas eksplorować grobowce i odebrać to, co Twoje. 👁️<br><br>Rozpocznij przygodę:",
  },
}

# ============ Email 8S ============
T['Email 8S'] = {
  'hu-HU': {
    'subject': '🏆 Fogadj okosan a harmadik befizetéssel',
    'preheader': 'Nyerj kockázat nélkül – akár €500-ig fedezünk',
    'button_text_1': 'FOGADÁSOK IGÉNYLÉSE',
    'greeting': ' {{ customer.first_name | default:"Barátom" | capitalize }}, tedd meg a harmadik befizetésedet és lépj a játékba magabiztosan. ',
    'body': '<strong>20% Kockázatmentes Fogadásokkal akár €500-ig</strong>, egy mellélövés sem kerül semmibe – de egy találat hatalmas lehet. A kódod – <strong class="promocode">STEADY20</strong>.<br><br>A legbiztonságosabb módja az izgalom hajszolásának itt van. 🛡️<br><br>Igényeld a fogadásaidat:',
  },
  'pl-PL': {
    'subject': '🏆 Obstawiaj mądrze na trzecią wpłatę',
    'preheader': 'Wygrywaj bez ryzyka – zabezpieczamy do €500',
    'button_text_1': 'ODBIERZ ZAKŁADY',
    'greeting': ' {{ customer.first_name | default:"Przyjacielu" | capitalize }}, dokonaj trzeciej wpłaty i wejdź do gry z pewnością. ',
    'body': 'Z <strong>20% Zakładami Bez Ryzyka do €500</strong>, chybienie nic nie kosztuje – ale trafienie może być ogromne. Kod dla Ciebie – <strong class="promocode">STEADY20</strong>.<br><br>Najbezpieczniejszy sposób na ściganie emocji jest tutaj. 🛡️<br><br>Odbierz swoje zakłady:',
  },
}


# ============================================================
# APPLY TRANSLATIONS
# ============================================================

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('\r\n', '\n')
raw_blocks = content.split('\n\n')

new_blocks = []
changes = 0

for rb in raw_blocks:
    if not rb.strip():
        new_blocks.append(rb)
        continue
    
    lines = rb.split('\n')
    d = {}
    field_order = []
    for line in lines:
        idx = line.find(':')
        if idx > 0:
            key = line[:idx].strip()
            val = line[idx+1:].strip()
            d[key] = val
            field_order.append(key)
    
    name = d.get('name', '')
    locale = d.get('locale', '')
    
    if locale in ('hu-HU', 'pl-PL') and name in T:
        tr = T[name].get(locale, {})
        if tr:
            if 'subject' in tr:
                d['subject'] = tr['subject']
                changes += 1
            if 'preheader' in tr:
                d['preheader'] = tr['preheader']
                changes += 1
            if 'button_text_1' in tr:
                d['button_text_1'] = tr['button_text_1']
                changes += 1
            
            if 'greeting' in tr:
                old_text1 = d.get('text_1', '')
                m = re.search(r'(<strong[^>]*>)(.*?)(</strong>)', old_text1, re.DOTALL)
                if m:
                    d['text_1'] = old_text1[:m.start(2)] + tr['greeting'] + old_text1[m.end(2):]
                    changes += 1
            
            if 'body' in tr:
                old_text2 = d.get('text_2', '')
                m = re.search(r'(<p[^>]*>)(.*)(</p></td>)', old_text2, re.DOTALL)
                if m:
                    d['text_2'] = old_text2[:m.start(2)] + tr['body'] + old_text2[m.end(2):]
                    changes += 1
    
    new_lines = []
    for key in field_order:
        new_lines.append(f'{key}: {d[key]}')
    new_blocks.append('\n'.join(new_lines))

result = '\n\n'.join(new_blocks)
with open(filepath, 'w', encoding='utf-8') as f:
    f.write(result)

print(f"Nutrition #3: {changes} fields translated")
print(f"Expected: 240 (24 emails x 2 locales x 5 fields)")
