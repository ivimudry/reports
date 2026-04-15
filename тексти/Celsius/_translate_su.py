# -*- coding: utf-8 -*-
"""Translate SU Retention - 30 emails × 2 locales (hu-HU, pl-PL).
Fields: subject, preheader, text_1 (greeting), text_2 (body inner HTML), button_text_1.
All greetings use: Hello, {{customer.first_name | default:"friend"}}👋
"""
import re, os, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

filepath = r'c:\Projects\REPORTS\тексти\Celsius\SU Retention - Table data.txt'

GREETING_HU = ' Szia, {{customer.first_name | default:"Barátom"}}👋 '
GREETING_PL = ' Cześć, {{customer.first_name | default:"Przyjacielu"}}👋 '

T = {}

# ============ Email 1C ============
T['Email 1C'] = {
  'hu-HU': {
    'subject': '🎁 100% Bónusz + 150 IP vár: Kapd el most!',
    'preheader': 'Az üdvözlő bónuszod sehova nem ment – fizess be még ma',
    'button_text_1': 'BÓNUSZ IGÉNYLÉSE',
    'body': 'Felfedezted a Celsius-t, most ideje megtenni az első igazi lépést.&nbsp;<br>Fizess be először és kapj <strong>100% Bónuszt és 150 Ingyenes Pörgetést a Razor Shark</strong> by Push Gaming játékra a <strong class="promocode">FINTASTIC150</strong> kóddal.<br><br>Az üdvözlő csomagod még aktív és vár rád. Ne hagyd ott pihenni! 🚀<br><br>Aktiváld a jutalmaidat azonnal:',
  },
  'pl-PL': {
    'subject': '🎁 100% Bonus + 150 DS czeka: Odbierz teraz!',
    'preheader': 'Twój bonus powitalny nadal czeka – dokonaj pierwszej wpłaty już dziś',
    'button_text_1': 'ODBIERZ BONUS',
    'body': 'Zapoznałeś się z Celsius, teraz czas na pierwszy prawdziwy krok.&nbsp;<br>Dokonaj pierwszej wpłaty i odbierz <strong>100% Bonus i 150 Darmowych Spinów na Razor Shark</strong> by Push Gaming z kodem <strong class="promocode">FINTASTIC150</strong>.<br><br>Twój pakiet powitalny jest nadal aktywny i czeka na Ciebie. Nie pozwól mu tam leżeć! 🚀<br><br>Aktywuj nagrody natychmiast:',
  },
}

# ============ Email 1M ============
T['Email 1M'] = {
  'hu-HU': {
    'subject': '🎁 Kapj 100% Bónuszt + 150 IP + 15% Kockázatmentes Fogadást!',
    'preheader': 'Fizess be először és kapj casino pörgetéseket és Kockázatmentes Fogadás bónuszt',
    'button_text_1': 'BÓNUSZ IGÉNYLÉSE',
    'body': 'Nem tudod, hol kezdd – casino vagy sport? Nem kell választanod.<br><br>Az első befizetésed <strong>100% Bónuszt + 150 Ingyenes Pörgetést a Razor Shark</strong> by Push Gaming játékra old fel a <strong class="promocode">FINTASTIC150</strong> kóddal, ÉS <strong>15% Kockázatmentes Fogadást</strong> sportfogadásra a <strong class="promocode">EARNNRF15X</strong> kóddal.<br><br>Merülj el a nyereményekben vagy fogadj a kedvenc csapatodra – az első lépéstől fedezve vagy. 🦈<br><br>Igényeld a teljes csomagot:',
  },
  'pl-PL': {
    'subject': '🎁 Odbierz 100% Bonus + 150 DS + 15% Zakład Bez Ryzyka!',
    'preheader': 'Dokonaj pierwszej wpłaty i odbierz spiny kasynowe i bonus Zakład Bez Ryzyka',
    'button_text_1': 'ODBIERZ BONUS',
    'body': 'Nie wiesz od czego zacząć – kasyno czy sport? Nie musisz wybierać.<br><br>Pierwsza wpłata odblokowuje <strong>100% Bonus + 150 Darmowych Spinów na Razor Shark</strong> by Push Gaming z kodem <strong class="promocode">FINTASTIC150</strong>, ORAZ <strong>15% Zakład Bez Ryzyka</strong> na zakłady sportowe z kodem <strong class="promocode">EARNNRF15X</strong>.<br><br>Zanurz się w wygranych lub obstaw ulubiony zespół – od pierwszego ruchu jesteś zabezpieczony. 🦈<br><br>Odbierz pełny pakiet:',
  },
}

# ============ Email 1S ============
T['Email 1S'] = {
  'hu-HU': {
    'subject': '🏆 15% Kockázatmentes Fogadás: A biztonsági hálód kész',
    'preheader': 'Csatlakoztál – most tedd meg a lépésedet 15% Kockázatmentes Fogadással az első befizetésednél',
    'button_text_1': 'BÓNUSZ IGÉNYLÉSE',
    'body': 'Regisztráltál és megnézted a platformot – most ideje leülni a padról és beállni a játékba.<br><br>Fizess be először a <strong class="promocode">EARNNRF15X</strong> kóddal és mi fedezünk téged <strong>15% Kockázatmentes Fogadás Bónusszal</strong>. Ha nem a te javadra alakul, mi a hátad mögött állunk. 🤝<br><br>Indítsd el az akciót itt:',
  },
  'pl-PL': {
    'subject': '🏆 15% Zakład Bez Ryzyka: Twoja siatka bezpieczeństwa gotowa',
    'preheader': 'Dołączyłeś – teraz zrób ruch z 15% Zakładem Bez Ryzyka przy pierwszej wpłacie',
    'button_text_1': 'ODBIERZ BONUS',
    'body': 'Zarejestrowałeś się i sprawdziłeś platformę – teraz czas wejść z ławki do gry.<br><br>Dokonaj pierwszej wpłaty z kodem <strong class="promocode">EARNNRF15X</strong>, a my weźmiemy Cię pod skrzydła z <strong>15% Bonusem Zakład Bez Ryzyka</strong>. Jeśli nie pójdzie po Twojej myśli, mamy Twoje plecy. 🤝<br><br>Zacznij akcję tutaj:',
  },
}

# ============ Email 2C ============
T['Email 2C'] = {
  'hu-HU': {
    'subject': '🎰 Igényeld a 100% Bónuszodat + 150 IP-t ma',
    'preheader': 'Fizess be most és igényeld az üdvözlő csomagodat, amíg aktív',
    'button_text_1': 'BÓNUSZ IGÉNYLÉSE',
    'body': 'A Celsius üdvözlő bónuszod még fenntartva neked:&nbsp;<br><strong>100% Bónusz és 150 Ingyenes Pörgetés a Razor Shark</strong> by Push Gaming játékra az első befizetéssel a <strong class="promocode">FINTASTIC150</strong> kóddal.<br><br>Ha készen állsz igazi pénzért játszani – most a tökéletes idő az asztalokhoz ülni. 🃏<br><br>Kattints ide a csomagod igényléséhez:',
  },
  'pl-PL': {
    'subject': '🎰 Odbierz 100% Bonus + 150 DS już dziś',
    'preheader': 'Wpłać teraz i odbierz pakiet powitalny, póki jest aktywny',
    'button_text_1': 'ODBIERZ BONUS',
    'body': 'Twój powitalny bonus Celsius nadal na Ciebie czeka:&nbsp;<br><strong>100% Bonus i 150 Darmowych Spinów na Razor Shark</strong> by Push Gaming na pierwszą wpłatę z kodem <strong class="promocode">FINTASTIC150</strong>.<br><br>Jeśli jesteś gotowy grać na poważnie – teraz jest idealny moment na dołączenie do stołów. 🃏<br><br>Kliknij i odbierz pakiet:',
  },
}

# ============ Email 2M ============
T['Email 2M'] = {
  'hu-HU': {
    'subject': '🎮 100% Bónusz + 150 IP + 4% Cashback: Mind a tiéd',
    'preheader': 'Az első befizetés hoz pörgetéseket, bónuszt és Cashback-et – egyszerre',
    'button_text_1': 'BÓNUSZ IGÉNYLÉSE',
    'body': 'Még mindig gondolkozol hol kezdd – casino vagy sport? Miért ne mindkettő?<br><br>Fizess be először és kapd meg:<br><br><strong>100% Bónuszt + 150 Ingyenes Pörgetést</strong> a <strong>Razor Shark</strong> játékra a <strong class="promocode">FINTASTIC150</strong> kóddal<br><strong>4% Cashback-et</strong> a sportfogadásaidra a <strong class="promocode">CASHPLUS4</strong> kóddal.<br><br>Egy befizetés mindkét oldalt feloldja – és megadja a rugalmasságot, hogy úgy játssz, ahogy te szeretnéd. 🎲<br><br>Oldd fel mindkét bónuszt most:',
  },
  'pl-PL': {
    'subject': '🎮 100% Bonus + 150 DS + 4% Cashback: Wszystko Twoje',
    'preheader': 'Pierwsza wpłata daje spiny, bonus i Cashback – wszystko za jednym razem',
    'button_text_1': 'ODBIERZ BONUS',
    'body': 'Nadal myślisz od czego zacząć – kasyno czy sport? Dlaczego nie oba?<br><br>Dokonaj pierwszej wpłaty i odbierz:<br><br><strong>100% Bonus + 150 Darmowych Spinów</strong> na <strong>Razor Shark</strong> z kodem <strong class="promocode">FINTASTIC150</strong><br><strong>4% Cashback</strong> na zakłady sportowe z kodem <strong class="promocode">CASHPLUS4</strong>.<br><br>Jedna wpłata odblokowuje obie strony gry – i daje Ci elastyczność, by grać po swojemu. 🎲<br><br>Odblokuj oba bonusy teraz:',
  },
}

# ============ Email 2S ============
T['Email 2S'] = {
  'hu-HU': {
    'subject': '🔁 Igényeld a 4% Sport Cashback-edet ma',
    'preheader': 'Kapj 4%-ot vissza a sportfogadásaidra az első befizetéstől kezdve',
    'button_text_1': 'BÓNUSZ IGÉNYLÉSE',
    'body': 'Már megszerezted a sportbónuszodat – most ideje megtenni az első lépést.<br><br>Használd a <strong class="promocode">CASHPLUS4</strong> kódot a befizetésnél és aktiváld a <strong>4% Cashback-et az összes sportfogadásodra</strong>. Nyersz vagy veszítesz, az akció egy része visszajön hozzád. 💸<br><br>Biztosítsd a cashback-edet most:',
  },
  'pl-PL': {
    'subject': '🔁 Odbierz 4% Cashback sportowy już dziś',
    'preheader': 'Odbierz 4% zwrotu na zakłady sportowe od pierwszej wpłaty',
    'button_text_1': 'ODBIERZ BONUS',
    'body': 'Już odebrałeś swój bonus sportowy – teraz czas na pierwszy ruch.<br><br>Wpisz kod <strong class="promocode">CASHPLUS4</strong> przy wpłacie i aktywuj <strong>4% Cashback na wszystkie zakłady sportowe</strong>. Wygrywasz czy przegrywasz, część akcji wraca do Ciebie. 💸<br><br>Zabezpiecz swój cashback teraz:',
  },
}

# ============ Email 3C ============
T['Email 3C'] = {
  'hu-HU': {
    'subject': '💥 A 140%-os befizetési bónuszod kész',
    'preheader': 'Ne szalaszd el az esélyed az erős kezdésre – az erősítésed aktív',
    'button_text_1': 'BÓNUSZ IGÉNYLÉSE',
    'body': 'Csatlakoztál és felfedezted, most ideje szintet lépni. 🆙<br><br>Fizess be először és kapj <strong>140% Bónuszt</strong> – az üdvözlő erősítést, ami a Celsius kalandod helyes elindítására készült.<br><br>Használd a kódot: <strong class="promocode">POWER140</strong><br><br><strong></strong>Növeld az egyenlegedet most:',
  },
  'pl-PL': {
    'subject': '💥 Twój 140% Bonus na wpłatę jest gotowy',
    'preheader': 'Nie przegap szansy na mocny start – Twój boost jest aktywny',
    'button_text_1': 'ODBIERZ BONUS',
    'body': 'Dołączyłeś i zbadałeś platformę, teraz czas na wyższy poziom. 🆙<br><br>Dokonaj pierwszej wpłaty i odbierz <strong>140% Bonus</strong> – powitalny boost stworzony, by rozpocząć przygodę z Celsius właściwie.<br><br>Wpisz kod: <strong class="promocode">POWER140</strong><br><br><strong></strong>Zwiększ swoje saldo teraz:',
  },
}

# ============ Email 3M ============
T['Email 3M'] = {
  'hu-HU': {
    'subject': '🎯 140% Casino Bónusz vagy 15% Kockázatmentes Fogadás: Te döntesz',
    'preheader': 'Használd a kódodat casino vagy sport közül – az első befizetésed mindkét utat megnyitja',
    'button_text_1': 'BÓNUSZ IGÉNYLÉSE',
    'body': 'Akár a tárcsák, akár a valós idejű szorzók érdekelnek – az első befizetésed testre szabott kezdést ad:<br><br>• Használd a <strong class="promocode">POWER140</strong> kódot <strong>140% Bónuszhoz</strong> a casinóban<br>• Használd az <strong class="promocode">EARNNRF15X</strong> kódot <strong>15% Kockázatmentes Fogadáshoz</strong> sportfogadásban<br><br>Te döntöd el, hogyan kezdj – mindenképpen igazi lendületet kapsz az első lépéstől. 🚀<br><br>Válaszd ki a nyerő utadat:',
  },
  'pl-PL': {
    'subject': '🎯 140% Bonus Casino lub 15% Zakład Bez Ryzyka: Wybierz',
    'preheader': 'Użyj kodu na kasyno lub sport – pierwsza wpłata otwiera obie drogi',
    'button_text_1': 'ODBIERZ BONUS',
    'body': 'Czy wolisz bębny czy kursy na żywo – pierwsza wpłata daje Ci dopasowany start:<br><br>• Wpisz kod <strong class="promocode">POWER140</strong> na <strong>140% Bonus</strong> w kasynie<br>• Wpisz kod <strong class="promocode">EARNNRF15X</strong> na <strong>15% Zakład Bez Ryzyka</strong> w zakładach sportowych<br><br>Sam decydujesz jak zacząć – tak czy inaczej, dostajesz prawdziwy boost od pierwszego ruchu. 🚀<br><br>Wybierz swoją zwycięską ścieżkę:',
  },
}

# ============ Email 3S ============
T['Email 3S'] = {
  'hu-HU': {
    'subject': '🏆 A 15% Kockázatmentes Fogadásod vár',
    'preheader': 'Oldd fel a biztonsági hálódat az első befizetésnél és fogadj magabiztosan',
    'button_text_1': 'BÓNUSZ IGÉNYLÉSE',
    'body': 'Igényelted a sportbónuszodat – most tedd, hogy számítson.<br><br>Használd az <strong class="promocode">EARNNRF15X</strong> kódot az első befizetésnél és oldd fel a <strong>15% Kockázatmentes Fogadást</strong>. Tedd meg az első fogadásodat magabiztosan – mi a hátad mögött állunk, ha az eredmény nem a javadra alakul. 🛡️<br><br>Kapd meg az ingyenes fogadásodat:',
  },
  'pl-PL': {
    'subject': '🏆 Twój 15% Zakład Bez Ryzyka czeka',
    'preheader': 'Odblokuj siatkę bezpieczeństwa przy pierwszej wpłacie i obstawiaj z pewnością',
    'button_text_1': 'ODBIERZ BONUS',
    'body': 'Odebrałeś swój bonus sportowy – teraz spraw, by się liczył.<br><br>Wpisz kod <strong class="promocode">EARNNRF15X</strong> przy pierwszej wpłacie i odblokuj <strong>15% Zakład Bez Ryzyka</strong>. Postaw pierwszy zakład z pewnością – stoimy za Tobą, jeśli wynik nie pójdzie po Twojej myśli. 🛡️<br><br>Odbierz swój darmowy zakład:',
  },
}

# ============ Email 4C ============
T['Email 4C'] = {
  'hu-HU': {
    'subject': '🍭 130% Bónusz + 70 IP a Sweet Bonanza-n',
    'preheader': 'Az első befizetésed ízletes bónuszt old fel – kész, amikor te is',
    'button_text_1': 'BÓNUSZ IGÉNYLÉSE',
    'body': 'Majdnem ott vagy. A Celsius üdvözlő ajánlatod édesnek tűnik! 🍬<br><br>Kapj <strong>130% Bónuszt + 70 Ingyenes Pörgetést a Sweet Bonanza</strong> játékra. Még aktív és vár az első befizetésedre. Ne maradj le erről az édes kezdésről.<br><br>Használd a kódot: <strong class="promocode">CANDYDROP70</strong><br><br><strong></strong>Kapd meg az édes ajándékodat itt:',
  },
  'pl-PL': {
    'subject': '🍭 130% Bonus + 70 DS na Sweet Bonanza',
    'preheader': 'Twoja pierwsza wpłata odblokowuje słodki bonus – gotowy kiedy Ty',
    'button_text_1': 'ODBIERZ BONUS',
    'body': 'Prawie tam jesteś. Twoja powitalna oferta Celsius wygląda słodko! 🍬<br><br>Odbierz <strong>130% Bonus + 70 Darmowych Spinów na Sweet Bonanza</strong>. Nadal aktywna i czeka na pierwszą wpłatę. Nie przegap tego słodkiego startu.<br><br>Wpisz kod: <strong class="promocode">CANDYDROP70</strong><br><br><strong></strong>Odbierz słodką porcję tutaj:',
  },
}

# ============ Email 4M ============
T['Email 4M'] = {
  'hu-HU': {
    'subject': '🍭 130% + 70 IP a Sweet Bonanza-n – Vagy sport?',
    'preheader': 'Kezdd édes casino erősítéssel vagy válaszd a saját utadat a sportban',
    'button_text_1': 'BÓNUSZ IGÉNYLÉSE',
    'body': 'Még nem tetted meg az első befizetésedet – de amikor megteszed, van választási lehetőséged.<br><br>• <strong>Pörgetni akarsz?</strong> Használd a <strong class="promocode">CANDYDROP70</strong> kódot és kapj <strong>130% Bónuszt + 70 Ingyenes Pörgetést a Sweet Bonanza</strong> játékra. 🍬<br>• <strong>Inkább fogadni?</strong> Menj a sportkönyvbe és válaszd ki a promódat, amikor kész vagy.<br><br>Casino vagy sport – kezdd az utadat ott, ahol jól érzed magad.<br><br>Válaszd ki az üdvözlő ajánlatodat:',
  },
  'pl-PL': {
    'subject': '🍭 130% + 70 DS na Sweet Bonanza – Albo sport?',
    'preheader': 'Zacznij od słodkiego boosta kasynowego lub wybierz własną ścieżkę w sporcie',
    'button_text_1': 'ODBIERZ BONUS',
    'body': 'Nie dokonałeś jeszcze pierwszej wpłaty – ale gdy to zrobisz, masz opcje.<br><br>• <strong>Chcesz kręcić?</strong> Wpisz kod <strong class="promocode">CANDYDROP70</strong> i odbierz <strong>130% Bonus + 70 Darmowych Spinów na Sweet Bonanza</strong>. 🍬<br>• <strong>Wolisz obstawiać?</strong> Przejdź do zakładów sportowych i wybierz swoją promocję, gdy będziesz gotowy.<br><br>Kasyno czy sport – zacznij podróż tam, gdzie czujesz się dobrze.<br><br>Wybierz swoją ofertę powitalną:',
  },
}

# ============ Email 4S ============
T['Email 4S'] = {
  'hu-HU': {
    'subject': '🔄 4% Cashback minden fogadásra: Aktív most',
    'preheader': 'Az első befizetésed 4%-ot ad vissza az összes sportakcióra',
    'button_text_1': 'BÓNUSZ IGÉNYLÉSE',
    'body': 'Már megszerezted a bónuszodat – most ideje bevetni.<br><br>Használd a <strong class="promocode">CASHPLUS4</strong> kódot az első befizetésnél és aktiváld a <strong>4% Cashback-et az összes sportfogadásodra</strong>. Több akció, kevesebb kockázat – minden fogadás visszafizet. ⚽<br><br>Térj vissza a játékba:',
  },
  'pl-PL': {
    'subject': '🔄 4% Cashback na każdy zakład: Aktywny teraz',
    'preheader': 'Pierwsza wpłata odblokowuje 4% zwrotu na wszystkie akcje sportowe',
    'button_text_1': 'ODBIERZ BONUS',
    'body': 'Już odebrałeś bonus – teraz czas go wykorzystać.<br><br>Wpisz kod <strong class="promocode">CASHPLUS4</strong> przy pierwszej wpłacie i aktywuj <strong>4% Cashback na wszystkie zakłady sportowe</strong>. Więcej akcji, mniej ryzyka – każdy zakład się zwraca. ⚽<br><br>Wróć do gry:',
  },
}

# ============ Email 5C ============
T['Email 5C'] = {
  'hu-HU': {
    'subject': '🎯 140% első befizetési bónusz: Az ajánlat hamarosan lejár?',
    'preheader': 'Az üdvözlő erősítésed még aktív – 140% bónusz az első befizetésre',
    'button_text_1': 'BÓNUSZ IGÉNYLÉSE',
    'body': 'Teljesítetted az első lépéseket – most ideje igazából játszani.<br><br>Fizess be először és kapj <strong>140% Bónuszt</strong>, hogy erősen indulj.&nbsp;<br>Az ajánlat kész – te is? 🎱<br><br>Használd a kódot: <strong class="promocode">POWER140</strong><br><br><strong></strong>Indítsd el a nyerőszériádat:',
  },
  'pl-PL': {
    'subject': '🎯 140% bonus na pierwszą wpłatę: Oferta wkrótce się kończy?',
    'preheader': 'Twój powitalny boost nadal aktywny – 140% bonus na pierwszą wpłatę',
    'button_text_1': 'ODBIERZ BONUS',
    'body': 'Wykonałeś pierwsze kroki – teraz czas grać na poważnie.<br><br>Dokonaj pierwszej wpłaty i odbierz <strong>140% Bonus</strong>, żeby zacząć z mocą.&nbsp;<br>Oferta gotowa – a Ty? 🎱<br><br>Wpisz kod: <strong class="promocode">POWER140</strong><br><br><strong></strong>Rozpocznij swoją serię wygranych:',
  },
}

# ============ Email 5M ============
T['Email 5M'] = {
  'hu-HU': {
    'subject': '🎯 140% Casino Bónusz vagy 15% Kockázatmentes Fogadás?',
    'preheader': 'Válaszd ki a neked való kezdést: casino erősítés vagy sport biztonsági háló',
    'button_text_1': 'BÓNUSZ IGÉNYLÉSE',
    'body': 'Már csak egy lépésre vagy az indulástól – és te választod, hogyan kezdj:<br><br>• <strong>Inkább a tárcsák?</strong> Használd a <strong class="promocode">POWER140</strong> kódot <strong>140% Casino Bónuszhoz</strong> az első befizetésre.<br>• <strong>Sportba?</strong> Használd az <strong class="promocode">EARNNRF15X</strong> kódot <strong>15% Kockázatmentes Fogadás</strong> aktiválásához.<br><br>Az üdvözlő bónuszod kész – már csak az első lépés hiányzik. ⚖️<br><br>Igényeld a preferált bónuszodat:',
  },
  'pl-PL': {
    'subject': '🎯 140% Bonus Casino lub 15% Zakład Bez Ryzyka?',
    'preheader': 'Wybierz start pasujący do Twojej gry: boost kasynowy lub siatka sportowa',
    'button_text_1': 'ODBIERZ BONUS',
    'body': 'Jesteś o krok od rozpoczęcia – i sam wybierasz jak zacząć:<br><br>• <strong>Wolisz bębny?</strong> Wpisz kod <strong class="promocode">POWER140</strong> na <strong>140% Bonus Casino</strong> na pierwszą wpłatę.<br>• <strong>Stawiasz na sport?</strong> Wpisz kod <strong class="promocode">EARNNRF15X</strong>, by aktywować <strong>15% Zakład Bez Ryzyka</strong>.<br><br>Twój bonus powitalny jest gotowy – brakuje tylko pierwszego ruchu. ⚖️<br><br>Odbierz preferowany bonus:',
  },
}

# ============ Email 5S ============
T['Email 5S'] = {
  'hu-HU': {
    'subject': '🛡️ Védd a fogadásaidat: 15% Kockázatmentes Fogadás',
    'preheader': 'Kezdj fogadni nyugalommal az első befizetésnél',
    'button_text_1': 'BÓNUSZ IGÉNYLÉSE',
    'body': 'Biztosítottad a sportbónuszodat – most tedd meg a következő lépést.<br><br>Használd az <strong class="promocode">EARNNRF15X</strong> kódot az első befizetésnél és oldd fel a <strong>15% Kockázatmentes Fogadást</strong>. Akár nyer, akár nem az első fogadásod, mindkét esetben védve vagy. 🥅<br><br>Játssz biztonsági hálóval:',
  },
  'pl-PL': {
    'subject': '🛡️ Chroń swoje zakłady: 15% Zakład Bez Ryzyka',
    'preheader': 'Zacznij obstawiać ze spokojem ducha przy pierwszej wpłacie',
    'button_text_1': 'ODBIERZ BONUS',
    'body': 'Zabezpieczyłeś swój bonus sportowy – teraz zrób następny krok.<br><br>Wpisz kod <strong class="promocode">EARNNRF15X</strong> przy pierwszej wpłacie i odblokuj <strong>15% Zakład Bez Ryzyka</strong>. Czy pierwszy zakład wygra czy nie, jesteś zabezpieczony tak czy inaczej. 🥅<br><br>Graj z siatką bezpieczeństwa:',
  },
}

# ============ Email 6C ============
T['Email 6C'] = {
  'hu-HU': {
    'subject': '💸 Több mint $100,000 nyeremény a múlt héten – Benne vagy?',
    'preheader': 'Igazi játékosok, igazi nyeremények – nézd meg a múlt hét top nyerőgépes találatait',
    'button_text_1': 'CSATLAKOZZ MOST',
    'body': 'Hatalmas dolgok történtek a múlt héten a tárcsákon – és itt a bizonyíték:<br><br><strong>🏆 rik••••64 nyert $46,870-t a Gates of Olympus-on</strong><br><strong>🏆 m••••n betalált $36,240-t a Sugar Rush-on</strong><br><strong>🏆 t•••y szerzett $32,905-t a Wanted Dead or a Wild-on</strong><br><br>Ezek a nyeremények valósak voltak. A játékosok valósak voltak. A te esélyed pedig? Csak egy pörgetésnyire van.<br><br>Csatlakozz a győztesek köréhez:',
  },
  'pl-PL': {
    'subject': '💸 Ponad $100,000 wygranych w zeszłym tygodniu – Wchodzisz?',
    'preheader': 'Prawdziwi gracze, prawdziwe wygrane – sprawdź najlepsze trafienia na slotach',
    'button_text_1': 'DOŁĄCZ TERAZ',
    'body': 'W zeszłym tygodniu na bębnach działy się wielkie rzeczy – oto dowód:<br><br><strong>🏆 rik••••64 wygrał $46,870 na Gates of Olympus</strong><br><strong>🏆 m••••n trafił $36,240 na Sugar Rush</strong><br><strong>🏆 t•••y zgarnął $32,905 na Wanted Dead or a Wild</strong><br><br>Te wygrane były prawdziwe. Gracze byli prawdziwi. A Twoja szansa? Tylko jeden spin dalej.<br><br>Dołącz do kręgu zwycięzców:',
  },
}

# ============ Email 6M ============
T['Email 6M'] = {
  'hu-HU': {
    'subject': '🎯 140% Casino Bónusz vagy 15% Kockázatmentes Fogadás?',
    'preheader': 'Válaszd ki a neked való kezdést: casino erősítés vagy sport biztonsági háló',
    'button_text_1': 'BÓNUSZ IGÉNYLÉSE',
    'body': 'Már csak egy lépésre vagy az indulástól – és te választod, hogyan kezdj:<br><br>• <strong>Inkább a tárcsák?</strong> Használd a <strong class="promocode">POWER140</strong> kódot <strong>140% Casino Bónuszhoz</strong> az első befizetésre.•&nbsp;<br><strong>Sportba?</strong> Használd az <strong class="promocode">EARNNRF15X</strong> kódot <strong>15% Kockázatmentes Fogadás</strong> aktiválásához.<br><br>Az üdvözlő bónuszod kész – már csak az első lépés hiányzik. ⚖️<br><br>Igényeld a preferált bónuszodat:',
  },
  'pl-PL': {
    'subject': '🎯 140% Bonus Casino lub 15% Zakład Bez Ryzyka?',
    'preheader': 'Wybierz start pasujący do Twojej gry: boost kasynowy lub siatka sportowa',
    'button_text_1': 'ODBIERZ BONUS',
    'body': 'Jesteś o krok od rozpoczęcia – i sam wybierasz jak zacząć:<br><br>• <strong>Wolisz bębny?</strong> Wpisz kod <strong class="promocode">POWER140</strong> na <strong>140% Bonus Casino</strong> na pierwszą wpłatę.•&nbsp;<br><strong>Stawiasz na sport?</strong> Wpisz kod <strong class="promocode">EARNNRF15X</strong>, by aktywować <strong>15% Zakład Bez Ryzyka</strong>.<br><br>Twój bonus powitalny jest gotowy – brakuje tylko pierwszego ruchu. ⚖️<br><br>Odbierz preferowany bonus:',
  },
}

# ============ Email 6S ============
T['Email 6S'] = {
  'hu-HU': {
    'subject': '🛡️ Védd a fogadásaidat: 15% Kockázatmentes Fogadás',
    'preheader': 'Kezdj fogadni nyugalommal az első befizetésnél',
    'button_text_1': 'BÓNUSZ IGÉNYLÉSE',
    'body': 'Biztosítottad a sportbónuszodat – most tedd meg a következő lépést.<br><br>Használd az <strong class="promocode">EARNNRF15X</strong> kódot az első befizetésnél és oldd fel a <strong>15% Kockázatmentes Fogadást</strong>. Akár nyer, akár nem az első fogadásod, mindkét esetben védve vagy. 🥅<br><br>Játssz biztonsági hálóval:',
  },
  'pl-PL': {
    'subject': '🛡️ Chroń swoje zakłady: 15% Zakład Bez Ryzyka',
    'preheader': 'Zacznij obstawiać ze spokojem ducha przy pierwszej wpłacie',
    'button_text_1': 'ODBIERZ BONUS',
    'body': 'Zabezpieczyłeś swój bonus sportowy – teraz zrób następny krok.<br><br>Wpisz kod <strong class="promocode">EARNNRF15X</strong> przy pierwszej wpłacie i odblokuj <strong>15% Zakład Bez Ryzyka</strong>. Czy pierwszy zakład wygra czy nie, jesteś zabezpieczony tak czy inaczej. 🥅<br><br>Graj z siatką bezpieczeństwa:',
  },
}

# ============ Email 7C ============
T['Email 7C'] = {
  'hu-HU': {
    'subject': '🎁 140% Bónusz + 80 IP a Chaos Crew II-n',
    'preheader': 'Oldd fel az üdvözlő csomagodat és szabadítsd el a káoszt az első befizetéssel',
    'button_text_1': 'BÓNUSZ IGÉNYLÉSE',
    'body': 'Már csatlakoztál – most ideje elkezdeni nyerni.<br><br>Fizess be először és használd a <strong class="promocode">CHAOSCTRL80</strong> kódot, hogy kapj <strong>140% Bónuszt és 80 Ingyenes Pörgetést a Chaos Crew II</strong> játékra. Ez a tökéletes pillanat beszállni és igazi előnnyel játszani. 🤘<br><br>Szabadítsd el a káoszt:',
  },
  'pl-PL': {
    'subject': '🎁 140% Bonus + 80 DS na Chaos Crew II',
    'preheader': 'Odblokuj pakiet powitalny i uwolnij chaos przy pierwszej wpłacie',
    'button_text_1': 'ODBIERZ BONUS',
    'body': 'Już dołączyłeś – teraz czas zacząć wygrywać.<br><br>Dokonaj pierwszej wpłaty i wpisz kod <strong class="promocode">CHAOSCTRL80</strong>, żeby dostać <strong>140% Bonus i 80 Darmowych Spinów na Chaos Crew II</strong>. To idealny moment, by wskoczyć i grać z prawdziwą przewagą. 🤘<br><br>Uwolnij chaos:',
  },
}

# ============ Email 7M ============
T['Email 7M'] = {
  'hu-HU': {
    'subject': '🎁 140% + 80 IP vagy 20% Kockázatmentes Fogadás: Te választasz',
    'preheader': 'Két módja a kezdésnek az első befizetésnél – szabadítsd el a káoszt vagy fogadj biztonságosan',
    'button_text_1': 'BÓNUSZ IGÉNYLÉSE',
    'body': 'Az üdvözlő utad még nyitva áll – és te viheted abba az irányba, ami a legjobban illik hozzád:<br><br>• <strong>Nyerőgépekkel akarod kezdeni?</strong> Használd a <strong class="promocode">CHAOSCTRL80</strong> kódot és kapj <strong>140% Bónuszt + 80 Ingyenes Pörgetést a Chaos Crew II</strong> játékra. 💀•&nbsp;<br><strong>Inkább fogadni?</strong> Használd a <strong class="promocode">WIN20NRF</strong> kódot <strong>20% Kockázatmentes Fogadás</strong> igényléséhez az első befizetésre.<br><br>Csak egy lépés kell bármelyik ajánlat feloldásához – a választás a tied.<br><br>Kezdd el az utadat itt:',
  },
  'pl-PL': {
    'subject': '🎁 140% + 80 DS lub 20% Zakład Bez Ryzyka: Twój wybór',
    'preheader': 'Dwa sposoby na start przy pierwszej wpłacie – uwolnij chaos lub obstawiaj bezpiecznie',
    'button_text_1': 'ODBIERZ BONUS',
    'body': 'Twoja powitalna ścieżka jest nadal otwarta – i możesz pójść w kierunku, który Ci najbardziej odpowiada:<br><br>• <strong>Chcesz zacząć od slotów?</strong> Wpisz kod <strong class="promocode">CHAOSCTRL80</strong> i odbierz <strong>140% Bonus + 80 Darmowych Spinów na Chaos Crew II</strong>. 💀•&nbsp;<br><strong>Wolisz obstawiać?</strong> Wpisz kod <strong class="promocode">WIN20NRF</strong>, by odebrać <strong>20% Zakład Bez Ryzyka</strong> na pierwszą wpłatę.<br><br>Wystarczy jeden ruch, by odblokować każdą ofertę – wybór należy do Ciebie.<br><br>Rozpocznij podróż tutaj:',
  },
}

# ============ Email 7S ============
T['Email 7S'] = {
  'hu-HU': {
    'subject': '🏁 Indulj erősen: 20% Kockázatmentes Fogadás kész',
    'preheader': 'Aktiváld a biztonsági hálódat az első befizetésnél ma',
    'button_text_1': 'BÓNUSZ IGÉNYLÉSE',
    'body': 'Megvan a bónuszod – most lőj. 🏀<br><br>Fizess be először a <strong class="promocode">WIN20NRF</strong> kóddal és aktiváld a <strong>20% Kockázatmentes Fogadást</strong>. Ez a legegyszerűbb módja annak, hogy teljes magabiztossággal lépj be a játékba.<br><br>Oldd fel a 20%-os védelmedet:',
  },
  'pl-PL': {
    'subject': '🏁 Zacznij mocno: 20% Zakład Bez Ryzyka gotowy',
    'preheader': 'Aktywuj siatkę bezpieczeństwa przy pierwszej wpłacie dziś',
    'button_text_1': 'ODBIERZ BONUS',
    'body': 'Masz bonus – teraz strzelaj. 🏀<br><br>Dokonaj pierwszej wpłaty z kodem <strong class="promocode">WIN20NRF</strong> i aktywuj <strong>20% Zakład Bez Ryzyka</strong>. To najłatwiejszy sposób, by wejść do gry z pełną pewnością.<br><br>Odblokuj swoją 20% ochronę:',
  },
}

# ============ Email 8C ============
T['Email 8C'] = {
  'hu-HU': {
    'subject': '💥 A jackpot nyeremények folytatódnak – Te leszel a következő?',
    'preheader': 'Nézd, mit nyertek a játékosok a múlt héten – igazi pörgetések, igazi nyeremények',
    'button_text_1': 'JÁTSSZ MOST',
    'body': 'Láttad, miről szól a Celsius – most nézd, mi történt múlt héten:<br><br><strong>💰 H••H55 nyert $44,190-t a The Dog House Megaways-en</strong><br><strong>💰 <i>y</i>•••54 betalált $28,670-t a Sweet Bonanza-n</strong><br><strong>💰 Da••••K33d szerzett $13,520-t a Book of Dead-en</strong><br><br>Ezek igazi nyeremények igazi játékosoktól.&nbsp;<br>Már csak az első pörgetésed hiányzik. 🎰<br><br>Lőj a jackpotra:',
  },
  'pl-PL': {
    'subject': '💥 Jackpoty nie przestają padać – Może Ty będziesz następny?',
    'preheader': 'Zobacz co wygrali gracze w zeszłym tygodniu – prawdziwe spiny, prawdziwe wygrane',
    'button_text_1': 'GRAJ TERAZ',
    'body': 'Widziałeś, o co chodzi w Celsius – teraz zobacz, co wydarzyło się w zeszłym tygodniu:<br><br><strong>💰 H••H55 wygrał $44,190 na The Dog House Megaways</strong><br><strong>💰 <i>y</i>•••54 trafił $28,670 na Sweet Bonanza</strong><br><strong>💰 Da••••K33d zgarnął $13,520 na Book of Dead</strong><br><br>To prawdziwe wygrane prawdziwych graczy.&nbsp;<br>Brakuje tylko Twojego pierwszego spinu. 🎰<br><br>Celuj w jackpot:',
  },
}

# ============ Email 8M ============
T['Email 8M'] = {
  'hu-HU': {
    'subject': '🎁 140% + 80 IP vagy 20% Kockázatmentes Fogadás: Te választasz',
    'preheader': 'Két módja a kezdésnek az első befizetésnél – szabadítsd el a káoszt vagy fogadj biztonságosan',
    'button_text_1': 'BÓNUSZ IGÉNYLÉSE',
    'body': 'Az üdvözlő utad még nyitva áll – és te viheted abba az irányba, ami a legjobban illik hozzád:<br><br>• <strong>Nyerőgépekkel akarod kezdeni?</strong> Használd a <strong class="promocode">CHAOSCTRL80</strong> kódot és kapj <strong>140% Bónuszt + 80 Ingyenes Pörgetést a Chaos Crew II</strong> játékra. 💀•&nbsp;<br><strong>Inkább fogadni?</strong> Használd a <strong class="promocode">WIN20NRF</strong> kódot <strong>20% Kockázatmentes Fogadás</strong> igényléséhez az első befizetésre.<br><br>Csak egy lépés kell bármelyik ajánlat feloldásához – a választás a tied.<br>Kezdd el az utadat itt:',
  },
  'pl-PL': {
    'subject': '🎁 140% + 80 DS lub 20% Zakład Bez Ryzyka: Twój wybór',
    'preheader': 'Dwa sposoby na start przy pierwszej wpłacie – uwolnij chaos lub obstawiaj bezpiecznie',
    'button_text_1': 'ODBIERZ BONUS',
    'body': 'Twoja powitalna ścieżka jest nadal otwarta – i możesz pójść w kierunku, który Ci najbardziej odpowiada:<br><br>• <strong>Chcesz zacząć od slotów?</strong> Wpisz kod <strong class="promocode">CHAOSCTRL80</strong> i odbierz <strong>140% Bonus + 80 Darmowych Spinów na Chaos Crew II</strong>. 💀•&nbsp;<br><strong>Wolisz obstawiać?</strong> Wpisz kod <strong class="promocode">WIN20NRF</strong>, by odebrać <strong>20% Zakład Bez Ryzyka</strong> na pierwszą wpłatę.<br><br>Wystarczy jeden ruch, by odblokować każdą ofertę – wybór należy do Ciebie.<br>Rozpocznij podróż tutaj:',
  },
}

# ============ Email 8S ============
T['Email 8S'] = {
  'hu-HU': {
    'subject': '🏁 Indulj erősen: 20% Kockázatmentes Fogadás kész',
    'preheader': 'Aktiváld a biztonsági hálódat az első befizetésnél ma',
    'button_text_1': 'BÓNUSZ IGÉNYLÉSE',
    'body': 'Megvan a bónuszod – most lőj. 🏀<br><br>Fizess be először a <strong class="promocode">WIN20NRF</strong> kóddal és aktiváld a <strong>20% Kockázatmentes Fogadást</strong>. Ez a legegyszerűbb módja annak, hogy teljes magabiztossággal lépj be a játékba.<br><br>Oldd fel a 20%-os védelmedet:',
  },
  'pl-PL': {
    'subject': '🏁 Zacznij mocno: 20% Zakład Bez Ryzyka gotowy',
    'preheader': 'Aktywuj siatkę bezpieczeństwa przy pierwszej wpłacie dziś',
    'button_text_1': 'ODBIERZ BONUS',
    'body': 'Masz bonus – teraz strzelaj. 🏀<br><br>Dokonaj pierwszej wpłaty z kodem <strong class="promocode">WIN20NRF</strong> i aktywuj <strong>20% Zakład Bez Ryzyka</strong>. To najłatwiejszy sposób, by wejść do gry z pełną pewnością.<br><br>Odblokuj swoją 20% ochronę:',
  },
}

# ============ Email 9C ============
T['Email 9C'] = {
  'hu-HU': {
    'subject': '🎁 160% Bónusz + 90 IP a Tome of Madness-en',
    'preheader': 'Használd a kódodat az első befizetésnél és kezdj igazi erősítéssel',
    'button_text_1': 'BÓNUSZ IGÉNYLÉSE',
    'body': "Már csak egy lépésre vagy a teljes üdvözlő bónusz feloldásától.<br><br>Használd a <strong class=\"promocode\">MADNESS16090</strong> kódot az első befizetésnél és fedezd fel a <strong>160% Bónuszt és 90 Ingyenes Pörgetést a Rich Wilde and the Tome of Madness</strong> játékra.<br><br>A tárcsák várnak – és a pillanatod most indul. 👁️<br><br>Nyisd meg a nyeremények könyvét:",
  },
  'pl-PL': {
    'subject': '🎁 160% Bonus + 90 DS na Tome of Madness',
    'preheader': 'Użyj kodu przy pierwszej wpłacie i zacznij z prawdziwym boostem',
    'button_text_1': 'ODBIERZ BONUS',
    'body': "Jesteś o krok od odblokowania pełnego bonusu powitalnego.<br><br>Wpisz kod <strong class=\"promocode\">MADNESS16090</strong> przy pierwszej wpłacie i odkryj <strong>160% Bonus i 90 Darmowych Spinów na Rich Wilde and the Tome of Madness</strong>.<br><br>Bębny czekają – i Twój moment zaczyna się teraz. 👁️<br><br>Otwórz księgę wygranych:",
  },
}

# ============ Email 9M ============
T['Email 9M'] = {
  'hu-HU': {
    'subject': '🎁 160% + 90 IP vagy 25% Kockázatmentes Fogadás: Döntsd el most',
    'preheader': 'Mindkét ajánlat még nyitva – indítsd a kalandot vagy tedd meg a fogadásod',
    'button_text_1': 'BÓNUSZ IGÉNYLÉSE',
    'body': "Még mindig gondolkozol hogyan kezdj? Akár a tárcsák, akár a valós idejű szorzók érdekelnek, van valami pont neked:<br><br>• Használd a <strong class=\"promocode\">MADNESS16090</strong> kódot <strong>160% Bónuszhoz + 90 Ingyenes Pörgetés a Rich Wilde and the Tome of Madness</strong> játékra a casinóban. 🐙<br>• Használd a <strong class=\"promocode\">SECURE25</strong> kódot <strong>25% Kockázatmentes Fogadáshoz</strong> az első sportfogadásra.<br><br>Két ajánlat, egy döntés – válaszd ki az oldaladat és tedd, hogy az első lépés számítson.<br><br>Aktiváld a bónuszodat:",
  },
  'pl-PL': {
    'subject': '🎁 160% + 90 DS lub 25% Zakład Bez Ryzyka: Zdecyduj teraz',
    'preheader': 'Obie oferty nadal otwarte – rozpocznij przygodę lub postaw zakład',
    'button_text_1': 'ODBIERZ BONUS',
    'body': "Nadal myślisz jak zacząć? Czy wolisz bębny czy kursy na żywo, mamy coś specjalnie dla Ciebie:<br><br>• Wpisz kod <strong class=\"promocode\">MADNESS16090</strong> na <strong>160% Bonus + 90 Darmowych Spinów na Rich Wilde and the Tome of Madness</strong> w kasynie. 🐙<br>• Wpisz kod <strong class=\"promocode\">SECURE25</strong> na <strong>25% Zakład Bez Ryzyka</strong> na pierwszy zakład sportowy.<br><br>Dwie oferty, jedna decyzja – wybierz stronę i spraw, by pierwszy ruch się liczył.<br><br>Aktywuj swój bonus:",
  },
}

# ============ Email 9S ============
T['Email 9S'] = {
  'hu-HU': {
    'subject': '🏆 25% Kockázatmentes Fogadás: Ne szalaszd el!',
    'preheader': 'Kezdj fogadni magabiztosan az első befizetésnél',
    'button_text_1': 'BÓNUSZ IGÉNYLÉSE',
    'body': 'Már igényelted a sportbónuszodat – most ideje használni.<br><br>Fizess be először a <strong class="promocode">SECURE25</strong> kóddal és aktiváld a <strong>25% Kockázatmentes Fogadást</strong>. Ha az első fogadásod nem talál, visszaadjuk egy részét. Nincs nyomás – csak játssz. 🏟️<br><br>Igényeld a kockázatmentes kezdésedet:',
  },
  'pl-PL': {
    'subject': '🏆 25% Zakład Bez Ryzyka: Nie przegap!',
    'preheader': 'Zacznij obstawiać z pewnością przy pierwszej wpłacie',
    'button_text_1': 'ODBIERZ BONUS',
    'body': 'Już odebrałeś swój bonus sportowy – teraz czas go użyć.<br><br>Dokonaj pierwszej wpłaty z kodem <strong class="promocode">SECURE25</strong> i aktywuj <strong>25% Zakład Bez Ryzyka</strong>. Jeśli pierwszy zakład nie wyjdzie, zwrócimy część. Bez presji – po prostu graj. 🏟️<br><br>Odbierz start bez ryzyka:',
  },
}

# ============ Email 10C ============
T['Email 10C'] = {
  'hu-HU': {
    'subject': '🎰 Több mint $90,000 kifizetés a múlt héten – Miért ne te?',
    'preheader': 'Nézd meg a legújabb nyereményeket igazi játékosoktól – te lehetsz a következő',
    'button_text_1': 'PÖRGETÉS MOST',
    'body': 'Miközben te felfedezted a platformot, mások pörgettek – és nagyot nyertek:<br><br><strong>🔥 Rich••••s nyert $49,870-t a Gates of Olympus-on</strong><br><strong>🔥 Bl<i>l</i>• betalált $27,430-t a Fruit Party 2-n</strong><br><strong>🔥 Blu••••86s szerzett $15,980-t a Legacy of Dead-en</strong><br><br>Nincs trükk, nincs kód – csak a megfelelő pörgetés a megfelelő időben. Lehet, hogy a tied?<br><br>Pörgesd ki a saját nagy nyereményedet:',
  },
  'pl-PL': {
    'subject': '🎰 Ponad $90,000 wypłat w zeszłym tygodniu – Dlaczego nie Ty?',
    'preheader': 'Sprawdź ostatnie wygrane prawdziwych graczy – możesz być następny',
    'button_text_1': 'KRĘĆ TERAZ',
    'body': 'Kiedy Ty odkrywałeś platformę, inni kręcili – i wygrywali grubo:<br><br><strong>🔥 Rich••••s wygrał $49,870 na Gates of Olympus</strong><br><strong>🔥 Bl<i>l</i>• trafił $27,430 na Fruit Party 2</strong><br><strong>🔥 Blu••••86s zgarnął $15,980 na Legacy of Dead</strong><br><br>Bez trików, bez kodów – tylko właściwy spin we właściwym czasie. Może to Twój?<br><br>Kręć po własną wielką wygraną:',
  },
}

# ============ Email 10M ============
T['Email 10M'] = {
  'hu-HU': {
    'subject': '🎁 160% + 90 IP vagy 25% Kockázatmentes Fogadás: Döntsd el most',
    'preheader': 'Mindkét ajánlat még nyitva – indítsd a kalandot vagy tedd meg a fogadásod',
    'button_text_1': 'BÓNUSZ IGÉNYLÉSE',
    'body': "Még mindig gondolkozol hogyan kezdj? Akár a tárcsák, akár a valós idejű szorzók érdekelnek, van valami pont neked:<br><br>• Használd a <strong class=\"promocode\">MADNESS16090</strong> kódot <strong>160% Bónuszhoz + 90 Ingyenes Pörgetés a Rich Wilde and the Tome of Madness</strong> játékra a casinóban. 🐙<br>• Használd a <strong class=\"promocode\">SECURE25</strong> kódot <strong>25% Kockázatmentes Fogadáshoz</strong> az első sportfogadásra.<br><br>Két ajánlat, egy döntés – válaszd ki az oldaladat és tedd, hogy az első lépés számítson.<br><br>Aktiváld a bónuszodat:",
  },
  'pl-PL': {
    'subject': '🎁 160% + 90 DS lub 25% Zakład Bez Ryzyka: Zdecyduj teraz',
    'preheader': 'Obie oferty nadal otwarte – rozpocznij przygodę lub postaw zakład',
    'button_text_1': 'ODBIERZ BONUS',
    'body': "Nadal myślisz jak zacząć? Czy wolisz bębny czy kursy na żywo, mamy coś specjalnie dla Ciebie:<br><br>• Wpisz kod <strong class=\"promocode\">MADNESS16090</strong> na <strong>160% Bonus + 90 Darmowych Spinów na Rich Wilde and the Tome of Madness</strong> w kasynie. 🐙<br>• Wpisz kod <strong class=\"promocode\">SECURE25</strong> na <strong>25% Zakład Bez Ryzyka</strong> na pierwszy zakład sportowy.<br><br>Dwie oferty, jedna decyzja – wybierz stronę i spraw, by pierwszy ruch się liczył.<br><br>Aktywuj swój bonus:",
  },
}

# ============ Email 10S ============
T['Email 10S'] = {
  'hu-HU': {
    'subject': '🏆 Még mindig vár: 15% Kockázatmentes Fogadás',
    'preheader': 'Csatlakoztál – most tedd meg a lépésedet 15% Kockázatmentes Fogadással az első befizetésnél',
    'button_text_1': 'BÓNUSZ IGÉNYLÉSE',
    'body': 'Regisztráltál, megnézted a platformot – most ideje beállni a játékba.<br><br>Fizess be először a <strong class="promocode">EARNNRF15X</strong> kóddal és mi fedezünk <strong>15% Kockázatmentes Fogadás Bónusszal</strong>. Ha nem a javadra alakul, még mindig a hátad mögött állunk. 🥊<br><br>Tedd meg a nyerő fogadásodat:',
  },
  'pl-PL': {
    'subject': '🏆 Nadal czeka: 15% Zakłady Bez Ryzyka',
    'preheader': 'Dołączyłeś – teraz zrób ruch z 15% Zakładami Bez Ryzyka przy pierwszej wpłacie',
    'button_text_1': 'ODBIERZ BONUS',
    'body': 'Zarejestrowałeś się, sprawdziłeś platformę – teraz czas wejść do gry.<br><br>Dokonaj pierwszej wpłaty z kodem <strong class="promocode">EARNNRF15X</strong>, a weźmiemy Cię pod skrzydła z <strong>15% Bonusem Zakłady Bez Ryzyka</strong>. Jeśli nie pójdzie po Twojej myśli, nadal mamy Twoje plecy. 🥊<br><br>Postaw swój wygrany zakład:',
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

print(f"SU Retention: {changes} fields translated")
print(f"Expected: 300 (30 emails x 2 locales x 5 fields)")
