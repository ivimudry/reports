# -*- coding: utf-8 -*-
"""Translate Welcome Flow - 27 emails × 2 locales (hu-HU, pl-PL).
Fields: subject, preheader, text_1 (greeting), text_2 (body inner HTML), button_text_1.
All greetings: Hello, {{customer.first_name | default:"friend"}}👋
"""
import re, os, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

filepath = r'c:\Projects\REPORTS\тексти\Celsius\Welcome Flow - Table data.txt'

GREETING_HU = ' Szia, {{customer.first_name | default:"Barátom"}}👋 '
GREETING_PL = ' Cześć, {{customer.first_name | default:"Przyjacielu"}}👋 '

T = {}

# ============ Email 1C ============
T['Email 1C'] = {
  'hu-HU': {
    'subject': '🚀 A Celsius kalandod itt kezdődik!',
    'preheader': 'Oldd fel a hatalmas bónuszokat az első 4 befizetésedre – akár €2000 + 250 Ingyenes Pörgetés!',
    'button_text_1': 'INDÍTS EL AZ UTAM',
    'body': 'A Celsius kaland most kezdődik – és erős jutalmakat állítottunk sorba az induláshoz.<br>Az első 4 befizetésed <strong>hatalmas bónuszokkal</strong> és <strong>rengeteg Ingyenes Pörgetéssel</strong> jár:<br><br><strong>1.: 100% akár €500 + 150 IP</strong><br><strong>2.: 100% akár €300 + 50 IP</strong><br><strong>3.: 200% akár €200 + 50 IP</strong><br><strong>4.: 150% akár €1000</strong><br><br>Ez akár <strong>€2000 + 250 Ingyenes Pörgetés</strong>, ami csak rád vár. Kezdj kicsiben vagy menj nagyban – a választás a tied.<br>Igényeld az üdvözlő bónuszaidat most',
  },
  'pl-PL': {
    'subject': '🚀 Twoja przygoda z Celsius zaczyna się tutaj!',
    'preheader': 'Odblokuj ogromne bonusy na pierwsze 4 wpłaty – do €2000 + 250 Darmowych Spinów!',
    'button_text_1': 'ZACZNIJ PODRÓŻ',
    'body': 'Przygoda z Celsius właśnie się zaczyna – i przygotowaliśmy potężne nagrody na start.<br>Twoje pierwsze 4 wpłaty przynoszą <strong>ogromne bonusy</strong> i <strong>mnóstwo Darmowych Spinów</strong>:<br><br><strong>1.: 100% do €500 + 150 DS</strong><br><strong>2.: 100% do €300 + 50 DS</strong><br><strong>3.: 200% do €200 + 50 DS</strong><br><strong>4.: 150% do €1000</strong><br><br>To aż <strong>€2000 + 250 Darmowych Spinów</strong> czekających właśnie na Ciebie. Zacznij na małą skalę lub idź na całość – wybór należy do Ciebie.<br>Odbierz bonusy powitalne teraz',
  },
}

# ============ Email 1M ============
T['Email 1M'] = {
  'hu-HU': {
    'subject': '🎯 Játssz a te módodra a Cashback Bónusszal',
    'preheader': 'Nyerőgépek, Élő Casino vagy Sport – kapj többet vissza minden játékból a Cashback Bónusszal.',
    'button_text_1': 'JÁTSSZ KORLÁTOK NÉLKÜL',
    'body': 'Kezdd a Celsius utadat a <strong>Cashback Bónusszal</strong> – egyszerű, kifizetődő, és a te játékod köré épül.<br><br>Akár nyerőgépeket, Élő Casinót vagy sportfogadást szeretsz, a játékod mostantól extra értékkel jár: kapj vissza egy részt cashback formájában és tartsd tovább az akciót.<br><br>Több játék. Több visszatérítés. Pont ahogy szereted.',
  },
  'pl-PL': {
    'subject': '🎯 Graj po swojemu z Bonusem Cashback',
    'preheader': 'Sloty, Kasyno Na Żywo lub Sport – odbieraj więcej z każdej gry dzięki Bonusowi Cashback.',
    'button_text_1': 'GRAJ BEZ LIMITÓW',
    'body': 'Rozpocznij podróż z Celsius od <strong>Bonusu Cashback</strong> – prostego, opłacalnego i dopasowanego do Twojej gry.<br><br>Czy wolisz sloty, Kasyno Na Żywo, czy zakłady sportowe, Twoja gra teraz przynosi dodatkową wartość: odbierz część z powrotem jako cashback i graj dłużej.<br><br>Więcej gry. Więcej zwrotów. Dokładnie tak, jak lubisz.',
  },
}

# ============ Email 1S ============
T['Email 1S'] = {
  'hu-HU': {
    'subject': '⚽ Indítsd el a sportutadat a Celsius-nál',
    'preheader': 'Akár €700-ig Kockázatmentes Fogadás vár rád az első két befizetésednél.',
    'button_text_1': 'KOCKÁZATMENTES FOGADÁS IGÉNYLÉSE',
    'body': 'Készen állsz, hogy új szintre vidd a sportfogadásaidat? Kezdd az utadat <strong>exkluzív Kockázatmentes Fogadás bónuszokkal</strong> csak új játékosoknak:<br><br><strong>1. befizetés: 50% Üdvözlő Kockázatmentes Fogadás Bónusz akár €200-ig</strong><br><strong>2. befizetés: 20% Kockázatmentes Fogadás Bónusz akár €500-ig</strong><br><br>Akár futballra, teniszre vagy e-sportra fogadsz – a Celsius a hátad mögött áll az első meccstől. Tedd meg a lépésedet és szerezd meg a Kockázatmentes Fogadásaidat most!',
  },
  'pl-PL': {
    'subject': '⚽ Rozpocznij sportową podróż z Celsius',
    'preheader': 'Zakłady Bez Ryzyka do €700 czekają na Ciebie przy pierwszych dwóch wpłatach.',
    'button_text_1': 'ODBIERZ ZAKŁADY BEZ RYZYKA',
    'body': 'Gotowy, by przenieść zakłady sportowe na wyższy poziom? Zacznij podróż z <strong>ekskluzywnymi bonusami Zakłady Bez Ryzyka</strong> tylko dla nowych graczy:<br><br><strong>1. wpłata: 50% Powitalny Bonus Zakład Bez Ryzyka do €200</strong><br><strong>2. wpłata: 20% Bonus Zakład Bez Ryzyka do €500</strong><br><br>Czy obstawiasz piłkę nożną, tenis czy e-sport – Celsius stoi za Tobą od pierwszego meczu. Zrób swój ruch i odbierz Zakłady Bez Ryzyka teraz!',
  },
}

# ============ Email 2C ============
T['Email 2C'] = {
  'hu-HU': {
    'subject': '🎰 Az első bónuszod már csak egy lépésre van',
    'preheader': 'Használd a kódot és kapj 100% + 150 Ingyenes Pörgetést az első befizetésedre.',
    'button_text_1': 'BÓNUSZ IGÉNYLÉSE',
    'body': 'Már csak egy lépésre vagy az első nagy jutalmad feloldásától a Celsius-nál.&nbsp;<br><br>Fizess be először a <strong class="promocode">BANDIT150</strong> kóddal és élvezd:&nbsp;<br><strong>100% Bónuszt</strong> és <strong>150 Ingyenes Pörgetést</strong> a <strong>Le bandit by Hacksaw Gaming</strong> játékra.&nbsp;<br><br>Ez a tökéletes módja a Celsius utad elindításának egy erősítéssel. Ne szalaszd el az esélyed – igényeld az üdvözlő bónuszodat ma.',
  },
  'pl-PL': {
    'subject': '🎰 Twój pierwszy bonus jest o krok dalej',
    'preheader': 'Wpisz kod i odbierz 100% + 150 Darmowych Spinów na pierwszą wpłatę.',
    'button_text_1': 'ODBIERZ BONUS',
    'body': 'Jesteś o krok od odblokowania pierwszej wielkiej nagrody w Celsius.&nbsp;<br><br>Dokonaj pierwszej wpłaty z kodem <strong class="promocode">BANDIT150</strong> i ciesz się:&nbsp;<br><strong>100% Bonusem</strong> i <strong>150 Darmowymi Spinami</strong> na <strong>Le bandit by Hacksaw Gaming</strong>.&nbsp;<br><br>To idealny sposób na rozpoczęcie przygody z Celsius z boostem. Nie przegap szansy – odbierz bonus powitalny dziś.',
  },
}

# ============ Email 2M ============
T['Email 2M'] = {
  'hu-HU': {
    'subject': '🎯 Nagy nyerőgépes nyeremények és 10% biztonsági háló a következő fogadásodra',
    'preheader': 'Játékosok nagyot nyertek a múlt héten – most te jössz, 10% Kockázatmentes Fogadással a kóddal.',
    'button_text_1': 'PRÓBÁLD KI A SZERENCSÉM',
    'body': 'A tárcsák nem álltak meg a múlt héten – és íme, kik távoztak mosolyogva:<br><br><strong>l•••••e nyert $29,343-t</strong><br><strong>k••••o betalált $18,920-t</strong><br><strong>a••••1h szerzett $11,480-t</strong><br><br>Benne vagy? Használd a <strong class="promocode">SAFE10</strong> kódot és kapj <strong>10% Kockázatmentes Fogadás Bónuszt</strong> a következő fogadásodra. Egy kattintás az egész, ami kell.',
  },
  'pl-PL': {
    'subject': '🎯 Wielkie wygrane na slotach i 10% siatka bezpieczeństwa na następny zakład',
    'preheader': 'Gracze trafili grubo w zeszłym tygodniu – teraz Twoja kolej, z 10% Zakładem Bez Ryzyka z kodem.',
    'button_text_1': 'SPRÓBUJ SZCZĘŚCIA',
    'body': 'Bębny nie przestawały kręcić się w zeszłym tygodniu – oto kto odszedł z uśmiechem:<br><br><strong>l•••••e wygrał $29,343</strong><br><strong>k••••o trafił $18,920</strong><br><strong>a••••1h zgarnął $11,480</strong><br><br>Wchodzisz? Wpisz kod <strong class="promocode">SAFE10</strong> i odbierz <strong>10% Bonus Zakład Bez Ryzyka</strong> na następny zakład. Jedno kliknięcie to wszystko, czego potrzeba.',
  },
}

# ============ Email 2S ============
T['Email 2S'] = {
  'hu-HU': {
    'subject': '⚽ A meccs elkezdődött — a fogadásod a pályára tartozik',
    'preheader': 'Az akció felforrósodik. Tedd meg a lépésedet és támogasd a tippedet ma.',
    'button_text_1': 'FOGADÁS MEGTÉTELE',
    'body': 'A pálya kész, a szorzók mozognak, és a feszültség nő – most itt az idő fogadni.&nbsp;<br><br>Válaszd ki a meccsedet, bízz az ösztöneidben, és hagyd, hogy a számok beszéljenek.<br><br>Hogy még jobb legyen, használd a <strong class="promocode">BOOST50</strong> kódot és élvezd az <strong>50%-os bónuszt a következő befizetésedre</strong> – több egyenleg, több magabiztosság, több nyeremény.',
  },
  'pl-PL': {
    'subject': '⚽ Mecz trwa — Twój zakład należy do boiska',
    'preheader': 'Akcja się rozkręca. Zrób ruch i obstaw swój typ dziś.',
    'button_text_1': 'POSTAW ZAKŁAD',
    'body': 'Boisko gotowe, kursy się zmieniają, a napięcie rośnie – teraz jest czas na zakład.&nbsp;<br><br>Wybierz mecz, zaufaj instynktowi i pozwól liczbom zagrać.<br><br>Żeby było jeszcze lepiej, wpisz kod <strong class="promocode">BOOST50</strong> i ciesz się <strong>50% bonusem na następną wpłatę</strong> – więcej salda, więcej pewności, więcej wygranych.',
  },
}

# ============ Email 3C ============
T['Email 3C'] = {
  'hu-HU': {
    'subject': '💥 100% + 150 IP — Az erősítés, amivel minden kezdődik',
    'preheader': 'Használd a kódot az első Celsius bónuszod feloldásához és lépj be a játékba',
    'button_text_1': 'KEZDÉS A BÓNUSSZAL',
    'body': 'Az első befizetésed előtti pillanat az, amikor minden elkezdődik.&nbsp;<br><br>Használd most a <strong class="promocode">CREW150</strong> kódot és kapj <strong>100% Bónuszt</strong> plusz <strong>150 Ingyenes Pörgetést</strong> a <strong>Chaos Crew II by Hacksaw Gaming</strong> játékra.&nbsp;<br><br>Ez a belépési pontod – nincs nyomás, csak a te játékod, feltételeid, és egy szilárd üdvözlő erősítés.',
  },
  'pl-PL': {
    'subject': '💥 100% + 150 DS — Boost, od którego wszystko się zaczyna',
    'preheader': 'Użyj kodu, by odblokować pierwszy bonus Celsius i wejdź do gry',
    'button_text_1': 'ZACZNIJ Z BONUSEM',
    'body': 'Moment przed pierwszą wpłatą to moment, gdy wszystko się zaczyna.&nbsp;<br><br>Wpisz teraz kod <strong class="promocode">CREW150</strong> i odbierz <strong>100% Bonus</strong> plus <strong>150 Darmowych Spinów</strong> na <strong>Chaos Crew II by Hacksaw Gaming</strong>.&nbsp;<br><br>To Twój punkt wejścia – bez presji, tylko Twoja gra, warunki i solidny powitalny boost.',
  },
}

# ============ Email 3M ============
T['Email 3M'] = {
  'hu-HU': {
    'subject': '🎰 Nagy jackpotok a múlt héten',
    'preheader': 'Nagy jackpotok a múlt héten – a te neved lesz a következő a listán?',
    'button_text_1': 'JÁTSSZ VAGY FOGADJ MOST',
    'body': 'Íme, mit hoztak a tárcsák a múlt héten – igazi nyeremények, igazi játékosok:<br><br><strong>a7g••••••n betalált $42,380-t &nbsp;</strong><br><strong>m2f•••••d szerzett $26,104-t &nbsp;</strong><br><strong>j3s•••••••7 nyert $33,987-t &nbsp;</strong><br><br>A nyerőgépek lángoltak – és ha ez nem a te világod, ne feledd: bármikor tehetsz fogadást élő sportra is. Egy pörgetés vagy egy lövés mindent megváltoztathat.',
  },
  'pl-PL': {
    'subject': '🎰 Wielkie jackpoty w zeszłym tygodniu',
    'preheader': 'Wielkie jackpoty w zeszłym tygodniu – czy Twoje nazwisko będzie następne na liście?',
    'button_text_1': 'GRAJ LUB OBSTAWIAJ TERAZ',
    'body': 'Oto co bębny dostarczyły w zeszłym tygodniu – prawdziwe wygrane, prawdziwi gracze:<br><br><strong>a7g••••••n trafił $42,380 &nbsp;</strong><br><strong>m2f•••••d zgarnął $26,104 &nbsp;</strong><br><strong>j3s•••••••7 wygrał $33,987 &nbsp;</strong><br><br>Sloty szalały – a jeśli to nie Twój klimat, pamiętaj: zawsze możesz postawić zakład na sport na żywo. Jeden spin lub jeden strzał może wszystko zmienić.',
  },
}

# ============ Email 3S ============
T['Email 3S'] = {
  'hu-HU': {
    'subject': '🏟️ Mérkőzésnapi energia a levegőben — Benne vagy?',
    'preheader': 'Ez a tökéletes pillanat a tipped rögzítésére és az adrenalin átérzésére.',
    'button_text_1': 'FOGADJ MOST',
    'body': 'Nagy meccsek. Merész szorzók. Minden a helyén van – kivéve a fogadásodat.&nbsp;<br><br>Akár a favoritra mész, akár az esélytelenre fogadsz, most itt az idő, hogy számítson.<br><br>És hogy extra előnyt adjunk neked, kapsz <strong>50%-os bónuszt a következő befizetésedre</strong> – több érték, több magabiztosság, több akció.',
  },
  'pl-PL': {
    'subject': '🏟️ Energia dnia meczowego w powietrzu — Wchodzisz?',
    'preheader': 'To idealny moment, by zatwierdzić swój typ i poczuć dreszczyk emocji.',
    'button_text_1': 'OBSTAWIAJ TERAZ',
    'body': 'Wielkie mecze. Odważne kursy. Wszystko na miejscu – oprócz Twojego zakładu.&nbsp;<br><br>Czy stawiasz na faworyta czy na outsidera, teraz jest czas, by się liczyło.<br><br>A żeby dać Ci dodatkową przewagę, dodajemy <strong>50% bonus na następną wpłatę</strong> – więcej wartości, więcej pewności, więcej akcji.',
  },
}

# ============ Email 4C ============
T['Email 4C'] = {
  'hu-HU': {
    'subject': '🎯 120% + 170 Ingyenes Pörgetés vár rád',
    'preheader': 'Használd a kódot az első befizetésedre és indulj erősen a Celsius-szal',
    'button_text_1': 'BÓNUSZ IGÉNYLÉSE',
    'body': 'Regisztráltál, felfedezted a platformot – most ideje megtenni az első lépésedet.&nbsp;<br><br>Használd a <strong class="promocode">STORM170</strong> kódot az első befizetésednél és kapj <strong>120% Bónuszt</strong> és <strong>170 Ingyenes Pörgetést</strong> a <strong>Stormforged by Hacksaw Gaming</strong> játékra.&nbsp;<br><br>Indítsd el a Celsius utadat egy nyerő kezdésre tervezett ajánlattal.',
  },
  'pl-PL': {
    'subject': '🎯 120% + 170 Darmowych Spinów czeka na Ciebie',
    'preheader': 'Użyj kodu na pierwszą wpłatę i zacznij mocno z Celsius',
    'button_text_1': 'ODBIERZ BONUS',
    'body': 'Zarejestrowałeś się, zbadałeś platformę – teraz czas na pierwszy ruch.&nbsp;<br><br>Wpisz kod <strong class="promocode">STORM170</strong> przy pierwszej wpłacie i odbierz <strong>120% Bonus</strong> i <strong>170 Darmowych Spinów</strong> na <strong>Stormforged by Hacksaw Gaming</strong>.&nbsp;<br><br>Rozpocznij przygodę z Celsius ofertą stworzoną na zwycięski start.',
  },
}

# ============ Email 4M ============
T['Email 4M'] = {
  'hu-HU': {
    'subject': '🎮 100 IP + Kockázatmentes Fogadás bent',
    'preheader': 'Használd a kódot az első befizetésednél és lépj be a casinóba és sportba teljes háttérrel.',
    'button_text_1': 'BÓNUSZ AKTIVÁLÁSA',
    'body': 'Akár a pörgetések, akár az eredmények érdekelnek – az első befizetésed fedez.<br><br>Írd be a <strong class="promocode">LEGACY100</strong> kódot és kapj <strong>100 Ingyenes Pörgetést</strong> a <strong>Legacy of Dead by Play\'n Go</strong> játékra.<br>Írd be a <strong class="promocode">BETSAFE20</strong> kódot és kapj <strong>20% Kockázatmentes Fogadás Bónuszt</strong> sportra.<br><br>A te játékod, a te tempód – csak egy előnnyel az induláshoz.',
  },
  'pl-PL': {
    'subject': '🎮 100 DS + Zakłady Bez Ryzyka w środku',
    'preheader': 'Użyj kodu przy pierwszej wpłacie i wejdź do kasyna i sportu z pełnym wsparciem.',
    'button_text_1': 'AKTYWUJ BONUS',
    'body': 'Czy wolisz spiny czy wyniki – Twoja pierwsza wpłata Cię zabezpiecza.<br><br>Wpisz kod <strong class="promocode">LEGACY100</strong> i odbierz <strong>100 Darmowych Spinów</strong> w <strong>Legacy of Dead by Play\'n Go</strong>.<br>Wpisz kod <strong class="promocode">BETSAFE20</strong> i odbierz <strong>20% Bonus Zakład Bez Ryzyka</strong> na sport.<br><br>Twoja gra, Twoje tempo – z przewagą od startu.',
  },
}

# ============ Email 4S ============
T['Email 4S'] = {
  'hu-HU': {
    'subject': '🧤 50% Kockázatmentes Fogadás ráadásul',
    'preheader': 'Lépj be a játékba szilárd előnnyel – az üdvözlő Kockázatmentes Fogadásaid készek',
    'button_text_1': 'FOGADÁS INDÍTÁSA',
    'body': 'A fogadás még jobb, ha erősítéssel kezded.&nbsp;<br><br>Az első befizetésedre kapsz egy <strong>50% Kockázatmentes Fogadás Bónuszt</strong> akár <strong>€200-ig</strong> – tökéletes a nyerőszériád elindításához.&nbsp;<br><br>Egy lépés. Egy előny. A te döntésed.',
  },
  'pl-PL': {
    'subject': '🧤 50% Zakłady Bez Ryzyka na wierzchu',
    'preheader': 'Wejdź do gry z solidną przewagą – Twoje powitalne Zakłady Bez Ryzyka są gotowe',
    'button_text_1': 'ZACZNIJ OBSTAWIAĆ',
    'body': 'Obstawianie jest fajniejsze, gdy zaczynasz z boostem.&nbsp;<br><br>Na pierwszą wpłatę odbierz <strong>50% Bonus Zakład Bez Ryzyka</strong> do <strong>€200</strong> – idealny na start serii.&nbsp;<br><br>Jeden ruch. Jedna przewaga. Twoja decyzja.',
  },
}

# ============ Email 5C ============
T['Email 5C'] = {
  'hu-HU': {
    'subject': '🎁 Egy kód. Egy befizetés. Egy komoly kezdés.',
    'preheader': 'Használd a kódot és változtasd az első befizetést 100% + 150 Ingyenes Pörgetéssé.',
    'button_text_1': 'BÓNUSZ FELOLDÁSA',
    'body': 'Mi történik az első befizetésed után?&nbsp;<br><br>Kapj <strong>100% Bónuszt</strong> és <strong>150 Ingyenes Pörgetést</strong> a <strong>Rip City by Hacksaw Gaming</strong> játékra, amikor használod a <strong class="promocode">RIP100CITY</strong> kódot.&nbsp;<br><br>Ez nem csak üdvözlés – ez egy igazi indulás. Csináld, hogy számítson.',
  },
  'pl-PL': {
    'subject': '🎁 Jeden kod. Jedna wpłata. Jeden poważny start.',
    'preheader': 'Użyj kodu i zamień pierwszą wpłatę w 100% + 150 Darmowych Spinów.',
    'button_text_1': 'ODBLOKUJ BONUS',
    'body': 'Co się dzieje po pierwszej wpłacie?&nbsp;<br><br>Odbierz <strong>100% Bonus</strong> i <strong>150 Darmowych Spinów</strong> na <strong>Rip City by Hacksaw Gaming</strong>, gdy wpiszesz kod <strong class="promocode">RIP100CITY</strong>.&nbsp;<br><br>To nie tylko powitanie – to prawdziwy start. Spraw, by się liczył.',
  },
}

# ============ Email 5M ============
T['Email 5M'] = {
  'hu-HU': {
    'subject': '🎯 Három nagy nyeremény. Két módja a játéknak. Egy te.',
    'preheader': 'Nyerőgépek vagy sport – íme, mi történt a múlt héten és hogyan szállhatsz be',
    'button_text_1': 'PÖRGETS VAGY FOGADJ MOST',
    'body': 'A múlt héten a tárcsák komoly hőséget hoztak:<br><br><strong>r8d•••••1 nyert $38,210-t &nbsp;</strong><br><strong>t3s••••••k betalált $24,765-t &nbsp;</strong><br><strong>b6v••••n szerzett $31,402-t&nbsp;</strong><br><br>A nyerőgépek egyértelműen lángolnak – de ha inkább a taktika és az időzítés érdekel, a sportfogadás mindig csak egy kattintásnyira van. Akárhogy is, mindig van mit nyerni.',
  },
  'pl-PL': {
    'subject': '🎯 Trzy wielkie wygrane. Dwa sposoby gry. Jeden Ty.',
    'preheader': 'Sloty czy sport – oto co wydarzyło się w zeszłym tygodniu i jak możesz się włączyć',
    'button_text_1': 'KRĘĆ LUB OBSTAWIAJ TERAZ',
    'body': 'W zeszłym tygodniu bębny rozkręciły się na poważnie:<br><br><strong>r8d•••••1 wygrał $38,210 &nbsp;</strong><br><strong>t3s••••••k trafił $24,765 &nbsp;</strong><br><strong>b6v••••n zgarnął $31,402&nbsp;</strong><br><br>Sloty zdecydowanie szaleją – ale jeśli wolisz taktykę i wyczucie czasu, zakłady sportowe są zawsze o jedno kliknięcie dalej. Tak czy inaczej, zawsze jest co wygrywać.',
  },
}

# ============ Email 5S ============
T['Email 5S'] = {
  'hu-HU': {
    'subject': '🥶 50% Kockázatmentes Fogadás az első lépéseddel',
    'preheader': 'Fizess be először és mi megtoldjuk 50% Kockázatmentes Fogadással akár €200-ig.',
    'button_text_1': 'BELÉPÉS',
    'body': 'Nagy szorzók, gyors akció, és a fogadásod vár, hogy megtörténjen.&nbsp;<br><br>Fizess be először és szerezd meg az <strong>50% Üdvözlő Kockázatmentes Fogadás Bónuszt</strong> akár <strong>€200-ig</strong> – nem kell túlgondolni, csak egyenesen be a játékba.',
  },
  'pl-PL': {
    'subject': '🥶 50% Zakłady Bez Ryzyka z pierwszym ruchem',
    'preheader': 'Dokonaj pierwszej wpłaty, a my dorzucimy 50% Zakłady Bez Ryzyka do €200.',
    'button_text_1': 'WEJDŹ DO GRY',
    'body': 'Wielkie kursy, szybka akcja i Twój zakład czeka, by się wydarzyć.&nbsp;<br><br>Dokonaj pierwszej wpłaty i odbierz <strong>50% Powitalny Bonus Zakład Bez Ryzyka</strong> do <strong>€200</strong> – bez zastanawiania, prosto do gry.',
  },
}

# ============ Email 6C ============
T['Email 6C'] = {
  'hu-HU': {
    'subject': '🎯 Ideje feloldani a 100% + 150 IP-t!',
    'preheader': 'Az első befizetésed teljes erejű üdvözléssé válik – ha te is akarod.',
    'button_text_1': 'KEZDÉS',
    'body': 'Van egy bónusz az első lépésedre szabva – ha úgy döntesz, hogy elfogadod.&nbsp;<br><br>Használd a <strong class="promocode">BANDIT150</strong> kódot, hogy kapj <strong>100% Bónuszt</strong> és <strong>150 Ingyenes Pörgetést</strong> a <strong>Le bandit by Hacksaw Gaming</strong> játékra az első befizetésedre.&nbsp;<br><br>Tiszta, egyszerű, és kész, amikor te is.',
  },
  'pl-PL': {
    'subject': '🎯 Czas odblokować 100% + 150 DS!',
    'preheader': 'Twoja pierwsza wpłata zmienia się w pełnowymiarowe powitanie – jeśli chcesz.',
    'button_text_1': 'ZACZNIJ',
    'body': 'Jest bonus stworzony na Twój pierwszy ruch – jeśli zdecydujesz się go odebrać.&nbsp;<br><br>Wpisz kod <strong class="promocode">BANDIT150</strong>, by dostać <strong>100% Bonus</strong> i <strong>150 Darmowych Spinów</strong> na <strong>Le bandit by Hacksaw Gaming</strong> na pierwszą wpłatę.&nbsp;<br><br>Czysto, prosto i gotowe, kiedy tylko chcesz.',
  },
}

# ============ Email 6M ============
T['Email 6M'] = {
  'hu-HU': {
    'subject': '🎲 $47,890 nyeremény ezen a héten, te leszel a következő?',
    'preheader': 'A nyerőgépek vadul mentek a múlt héten – és a sport szorzók sem hűlnek le.',
    'button_text_1': 'PÖRGESS VAGY FOGADJ MOST',
    'body': 'Nagy hét. Nagy nyeremények. Íme, mi történt a Celsius-nál:<br><br><strong>a9n•••••z nyert $47,890-t &nbsp;</strong><br><strong>m4e••••q betalált $22,715-t &nbsp;</strong><br><strong>j2x•••••r szerzett $35,040-t</strong> &nbsp;<br><br>A pörgetések lángoltak – és ha inkább fogadni szeretnél, a sportkönyv készen áll élő akcióval és friss szorzókkal. Ahogy játszol, a következő nyeremény a te nevedet viselheti.',
  },
  'pl-PL': {
    'subject': '🎲 $47,890 wygranych w tym tygodniu, może Ty następny?',
    'preheader': 'Sloty szalały w zeszłym tygodniu – a kursy sportowe też nie odpuszczają.',
    'button_text_1': 'KRĘĆ LUB OBSTAWIAJ TERAZ',
    'body': 'Wielki tydzień. Wielkie wygrane. Oto co wydarzyło się w Celsius:<br><br><strong>a9n•••••z wygrał $47,890 &nbsp;</strong><br><strong>m4e••••q trafił $22,715 &nbsp;</strong><br><strong>j2x•••••r zgarnął $35,040</strong> &nbsp;<br><br>Spiny szalały – a jeśli wolisz obstawiać, zakłady sportowe czekają z akcją na żywo i świeżymi kursami. Jak byś nie grał, następna wygrana może mieć Twoje imię.',
  },
}

# ============ Email 6S ============
T['Email 6S'] = {
  'hu-HU': {
    'subject': '🏁 A fogadásod nem él, amíg te nem',
    'preheader': '50% Kockázatmentes Fogadás akár €200-ig – kezdj a saját feltételeiden',
    'button_text_1': 'BÓNUSZ AKTIVÁLÁSA',
    'body': 'Láttad a szorzókat. Most indítsd el az egészet.&nbsp;<br><br>Az első befizetésed hoz egy <strong>50% Üdvözlő Kockázatmentes Fogadás Bónuszt</strong> akár <strong>€200-ig</strong> – semmi zavaró tényező, csak tiszta lendület az induláshoz.',
  },
  'pl-PL': {
    'subject': '🏁 Twój zakład nie żyje, póki Ty nie wejdziesz',
    'preheader': '50% Zakłady Bez Ryzyka do €200 – zacznij na swoich warunkach',
    'button_text_1': 'AKTYWUJ BONUS',
    'body': 'Widziałeś kursy. Teraz wpraw je w ruch.&nbsp;<br><br>Twoja pierwsza wpłata przynosi <strong>50% Powitalny Bonus Zakład Bez Ryzyka</strong> do <strong>€200</strong> – bez rozpraszaczy, czysty impet na start.',
  },
}

# ============ Email 7C ============
T['Email 7C'] = {
  'hu-HU': {
    'subject': '💸 Nagy nyerőgépes nyeremények a múlt héten — Te leszel a következő?',
    'preheader': 'Nézd, mit nyertek mások a Celsius-nál és vedd célba a következő nagy nyereményt.',
    'button_text_1': 'PRÓBÁLD KI A SZERENCSÉD',
    'body': 'A múlt héten a Celsius-nál a tárcsák lángoltak – íme, mit vittek haza a szerencsések:<br><br><strong>a•••••••n nyert $29,343-t</strong><br><strong>j•••••e betalált $17,920-t</strong><br><strong>m••••x11 szerzett $11,608-t</strong><br><br>Nincs trükk, nincs bónuszkód – csak tiszta játék és igazi nyeremények.&nbsp;<br>Készen állsz a te lövésedre?',
  },
  'pl-PL': {
    'subject': '💸 Wielkie wygrane na slotach w zeszłym tygodniu — Może Ty następny?',
    'preheader': 'Sprawdź co inni wygrali na Celsius i spróbuj trafić następną wielką wygraną.',
    'button_text_1': 'SPRÓBUJ SZCZĘŚCIA',
    'body': 'W zeszłym tygodniu w Celsius bębny szalały – oto co szczęściarze zabrali do domu:<br><br><strong>a•••••••n wygrał $29,343</strong><br><strong>j•••••e trafił $17,920</strong><br><strong>m••••x11 zgarnął $11,608</strong><br><br>Bez trików, bez kodów bonusowych – czysta gra i prawdziwe wygrane.&nbsp;<br>Gotowy na swój strzał?',
  },
}

# ============ Email 7M ============
T['Email 7M'] = {
  'hu-HU': {
    'subject': '🎯 Ne maradj le: 100 Ingyenes Pörgetés + 20% Kockázatmentes Fogadás',
    'preheader': '100 Ingyenes Pörgetés + 20% Kockázatmentes Fogadás – írd be a kódot az első befizetésnél.',
    'button_text_1': 'KOMBÓ INDÍTÁSA',
    'body': 'Miért válassz casino és sport között, amikor mindkettőt megkaphatod az indulástól?<br><br>Használd a <strong class="promocode">LEGACY100</strong> kódot az első befizetésnél, hogy kapj <strong>100 Ingyenes Pörgetést</strong> a <strong>Legacy of Dead by Play\'n Go</strong> játékra, és használd a <strong class="promocode">BETSAFE20</strong> kódot <strong>20% Kockázatmentes Fogadás Bónuszhoz</strong>.<br><br>Két út. Egy lépés. A játékod most kezdődik.',
  },
  'pl-PL': {
    'subject': '🎯 Nie przegap: 100 Darmowych Spinów + 20% Zakład Bez Ryzyka',
    'preheader': '100 Darmowych Spinów + 20% Zakład Bez Ryzyka – wpisz kod przy pierwszej wpłacie.',
    'button_text_1': 'ZACZNIJ COMBO',
    'body': 'Po co wybierać między kasynem a sportem, skoro możesz mieć oba od startu?<br><br>Wpisz kod <strong class="promocode">LEGACY100</strong> przy pierwszej wpłacie, by dostać <strong>100 Darmowych Spinów</strong> na <strong>Legacy of Dead by Play\'n Go</strong>, i wpisz kod <strong class="promocode">BETSAFE20</strong> na <strong>20% Bonus Zakład Bez Ryzyka</strong>.<br><br>Dwie ścieżki. Jeden ruch. Twoja gra zaczyna się teraz.',
  },
}

# ============ Email 7S ============
T['Email 7S'] = {
  'hu-HU': {
    'subject': '🥊 60% Kockázatmentes Fogadás az első ütésedre',
    'preheader': 'Használd a kódot és erősítsd az első befizetésedet 60% Kockázatmentes Fogadás Bónusszal.',
    'button_text_1': 'KÓD HASZNÁLATA',
    'body': 'Az első befizetéseknek hatásosnak kell lenniük.&nbsp;<br><br>Írd be a <strong class="promocode">FIREUP60</strong> kódot és szerezd meg a <strong>60% Üdvözlő Kockázatmentes Fogadás Bónuszt</strong> rögtön az induláskor.&nbsp;<br><br>Tedd meg a fogadásodat, érezd a ritmust, és játssz a magad módján.',
  },
  'pl-PL': {
    'subject': '🥊 60% Zakłady Bez Ryzyka na Twój pierwszy cios',
    'preheader': 'Użyj kodu i wzmocnij pierwszą wpłatę 60% Bonusem Zakłady Bez Ryzyka.',
    'button_text_1': 'UŻYJ KODU',
    'body': 'Pierwsze wpłaty powinny robić wrażenie.&nbsp;<br><br>Wpisz kod <strong class="promocode">FIREUP60</strong> i odbierz <strong>60% Powitalny Bonus Zakład Bez Ryzyka</strong> od samego startu.&nbsp;<br><br>Postaw zakład, poczuj rytm i graj po swojemu.',
  },
}

# ============ Email 8C ============
T['Email 8C'] = {
  'hu-HU': {
    'subject': '🧨 Kezdj erősen: 100% + 150 Ingyenes Pörgetés az első befizetésre',
    'preheader': 'Szerezd meg az üdvözlő bónuszodat és tedd emlékezetessé az első pillanataidat a Celsius-on.',
    'button_text_1': 'PRÓBÁLD KI A SZERENCSÉD',
    'body': 'Megvan a kódod – most ideje használni.&nbsp;<br><br>Az első befizetésnél írd be a <strong class="promocode">CREW150</strong> kódot és kapj <strong>100% Bónuszt</strong> és <strong>150 Ingyenes Pörgetést</strong> a <strong>Chaos Crew II by Hacksaw Gaming</strong> játékra.&nbsp;<br><br>Ez nem a nyomásról szól. Ez az erőről szól – és az erőd itt kezdődik.',
  },
  'pl-PL': {
    'subject': '🧨 Zacznij mocno: 100% + 150 Darmowych Spinów na pierwszą wpłatę',
    'preheader': 'Odbierz bonus powitalny i spraw, by pierwsze chwile w Celsius się liczyły.',
    'button_text_1': 'SPRÓBUJ SZCZĘŚCIA',
    'body': 'Masz kod – teraz czas go użyć.&nbsp;<br><br>Przy pierwszej wpłacie wpisz <strong class="promocode">CREW150</strong> i odbierz <strong>100% Bonus</strong> i <strong>150 Darmowych Spinów</strong> na <strong>Chaos Crew II by Hacksaw Gaming</strong>.&nbsp;<br><br>Tu nie chodzi o presję. Chodzi o moc – a Twoja moc zaczyna się tutaj.',
  },
}

# ============ Email 8M ============
T['Email 8M'] = {
  'hu-HU': {
    'subject': '🎯 Jackpotok felforrósodtak $41,226-ig',
    'preheader': 'Nézd meg a múlt heti top nyereményeket – a nyerőgépek hozták, és a sport hív.',
    'button_text_1': 'UGORJ BE',
    'body': 'A múlt héten nagy nyeremények csaptak be erősen – íme, mit vittek haza a játékosaink:<br><br><strong>sn••••an nyert $41,226-t</strong><br><strong>d••••ir betalált $36,078-t</strong><br><strong>t••••1964 szerzett $28,914-t</strong><br><br>Amíg a nyerőgépek jackpotokat osztottak, a sportkönyv is pörgött. Pörgethetsz vagy fogadhatsz – bármi is a stílusod, a következő nyeremény csak egy kattintásnyira van.',
  },
  'pl-PL': {
    'subject': '🎯 Jackpoty rozgrzane do $41,226',
    'preheader': 'Sprawdź najlepsze wygrane z zeszłego tygodnia – sloty dostarczyły, a sport czeka.',
    'button_text_1': 'WSKAKUJ',
    'body': 'W zeszłym tygodniu wielkie wygrane uderzyły mocno – oto co zabrali nasi gracze:<br><br><strong>sn••••an wygrał $41,226</strong><br><strong>d••••ir trafił $36,078</strong><br><strong>t••••1964 zgarnął $28,914</strong><br><br>Kiedy sloty sypały jackpotami, zakłady sportowe też nie stały w miejscu. Kręć lub obstawiaj – jakikolwiek Twój styl, następna wygrana jest o jedno kliknięcie dalej.',
  },
}

# ============ Email 8S ============
T['Email 8S'] = {
  'hu-HU': {
    'subject': '🏆 Egy lövés. 60% extra a támogatásához.',
    'preheader': 'Az első befizetés 60% Kockázatmentes Fogadással jár – írd be a kódot és hajrá',
    'button_text_1': 'KOCKÁZATMENTES FOGADÁS IGÉNYLÉSE',
    'body': 'Amikor az első fogadásod, csináld, hogy számítson.&nbsp;<br><br>Használd a <strong class="promocode">FIREUP60</strong> kódot az első befizetésnél és kapj <strong>60% Üdvözlő Kockázatmentes Fogadás Bónuszt</strong>, hogy extra súlyt adj a tippednek.&nbsp;<br><br>Nincs hezitálás – csak okos játék az indulástól.',
  },
  'pl-PL': {
    'subject': '🏆 Jeden strzał. 60% ekstra na wsparcie.',
    'preheader': 'Pierwsza wpłata daje 60% Zakłady Bez Ryzyka – wpisz kod i ruszaj',
    'button_text_1': 'ODBIERZ ZAKŁADY BEZ RYZYKA',
    'body': 'Kiedy to Twój pierwszy zakład, spraw by się liczył.&nbsp;<br><br>Wpisz kod <strong class="promocode">FIREUP60</strong> przy pierwszej wpłacie i odbierz <strong>60% Powitalny Bonus Zakład Bez Ryzyka</strong>, by dać dodatkową wagę Twojemu typowi.&nbsp;<br><br>Bez wahania – mądra gra od startu.',
  },
}

# ============ Email 9C ============
T['Email 9C'] = {
  'hu-HU': {
    'subject': '🎠 180 Ingyenes Pörgetés vár!',
    'preheader': 'Az első befizetésed megnyitja a kapukat – a kód hoz 180 Ingyenes Pörgetést',
    'button_text_1': 'PÖRGETÉSEK FELOLDÁSA',
    'body': 'Az első lépések számítanak – és a tied <strong>180 Ingyenes Pörgetéssel</strong> jár a <strong>Sweet Bonanza by Pragmatic Play</strong> játékra, amikor befizetsz és beírod a <strong class="promocode">SWEET180</strong> kódot.&nbsp;<br><br>Nincs bónuszfeltétel, csak tiszta játék és esély, hogy megtaláld a ritmusodat az első pörgetéstől.',
  },
  'pl-PL': {
    'subject': '🎠 180 Darmowych Spinów czeka!',
    'preheader': 'Twoja pierwsza wpłata otwiera bramy – kod przynosi 180 Darmowych Spinów',
    'button_text_1': 'ODBLOKUJ SPINY',
    'body': 'Pierwsze kroki się liczą – a Twój przynosi <strong>180 Darmowych Spinów</strong> na <strong>Sweet Bonanza by Pragmatic Play</strong> przy wpłacie i wpisaniu kodu <strong class="promocode">SWEET180</strong>.&nbsp;<br><br>Bez warunków bonusowych, czysta rozgrywka i szansa na złapanie rytmu od pierwszego spinu.',
  },
}

# ============ Email 9M ============
T['Email 9M'] = {
  'hu-HU': {
    'subject': '🎮 A játék mindkét oldalát fedi',
    'preheader': '100 Ingyenes Pörgetés és 20% Kockázatmentes Fogadás – a kód elindít.',
    'button_text_1': 'BÓNUSZAIM IGÉNYLÉSE',
    'body': 'Casino vagy sportkönyv? Nem kell oldalt választanod.&nbsp;<br><br>Használd a <strong class="promocode">LEGACY100</strong> kódot az első befizetésnél és oldd fel a <strong>100 Ingyenes Pörgetést</strong> a <strong>Legacy of Dead by Play\'n Go</strong> játékra, és használd a <strong class="promocode">BETSAFE20</strong> kódot <strong>20% Kockázatmentes Fogadás Bónuszhoz</strong> az első fogadásaidra.&nbsp;<br><br>Két módja a nyerésnek – egy egyszerű kezdés.',
  },
  'pl-PL': {
    'subject': '🎮 Obejmuje obie strony gry',
    'preheader': '100 Darmowych Spinów i 20% Zakład Bez Ryzyka – kod Cię uruchomi.',
    'button_text_1': 'ODBIERZ BONUSY',
    'body': 'Kasyno czy zakłady sportowe? Nie musisz wybierać strony.&nbsp;<br><br>Wpisz kod <strong class="promocode">LEGACY100</strong> przy pierwszej wpłacie i odblokuj <strong>100 Darmowych Spinów</strong> na <strong>Legacy of Dead by Play\'n Go</strong>, i wpisz kod <strong class="promocode">BETSAFE20</strong> na <strong>20% Bonus Zakład Bez Ryzyka</strong> na pierwsze zakłady.&nbsp;<br><br>Dwa sposoby na wygraną – jeden prosty start.',
  },
}

# ============ Email 9S ============
T['Email 9S'] = {
  'hu-HU': {
    'subject': '🧨 Első fogadás? 60% extra vár',
    'preheader': 'Fizess be először, használd a kódot, és kapj 60% Kockázatmentes Fogadás Bónuszt',
    'button_text_1': 'FOGADÁSOM ERŐSÍTÉSE',
    'body': 'Az első fogadásod több súlyt érdemel – és megvan hozzá az erősítés.&nbsp;<br><br>Használd a <strong class="promocode">FIREUP60</strong> kódot az első befizetésnél és oldd fel a <strong>60% Üdvözlő Kockázatmentes Fogadás Bónuszt</strong>.&nbsp;<br><br>Légy merész. Csináld, hogy számítson.',
  },
  'pl-PL': {
    'subject': '🧨 Pierwszy zakład? 60% ekstra czeka',
    'preheader': 'Dokonaj pierwszej wpłaty, użyj kodu i odbierz 60% Bonus Zakłady Bez Ryzyka',
    'button_text_1': 'WZMOCNIJ ZAKŁAD',
    'body': 'Pierwsze zakłady zasługują na większą wagę – i mamy na to boost.&nbsp;<br><br>Wpisz kod <strong class="promocode">FIREUP60</strong> przy pierwszej wpłacie i odblokuj <strong>60% Powitalny Bonus Zakład Bez Ryzyka</strong>.&nbsp;<br><br>Bądź odważny. Spraw, by się liczyło.',
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
            
            # Replace greeting in text_1
            old_text1 = d.get('text_1', '')
            m = re.search(r'(<strong[^>]*>)(.*?)(</strong>)', old_text1, re.DOTALL)
            if m:
                greeting = GREETING_HU if locale == 'hu-HU' else GREETING_PL
                d['text_1'] = old_text1[:m.start(2)] + greeting + old_text1[m.end(2):]
                changes += 1
            
            # Replace body in text_2
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

print(f"Welcome Flow: {changes} fields translated")
print(f"Expected: 270 (27 emails x 2 locales x 5 fields)")
