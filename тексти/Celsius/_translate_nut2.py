# -*- coding: utf-8 -*-
"""Translate Nutrition #2 - 24 emails × 2 locales (hu-HU, pl-PL).
Fields: subject, preheader, text_1 (greeting), text_2 (body inner HTML), button_text_1.
"""
import re, os, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

filepath = r'c:\Projects\REPORTS\тексти\Celsius\Nutrition #2 - Table data.txt'

# Nutrition #2 greetings use: {{ customer.first_name | default:"Player" | capitalize }} or "Friend"
# We need to replace the FULL greeting text inside the <strong> tag of text_1

T = {}

# ============ Email 1CL ============
T['Email 1CL'] = {
  'hu-HU': {
    'subject': '🎰 100% Bónusz + 50 Ingyenes Pörgetés a Hand of Anubis-on',
    'preheader': 'A következő befizetésed dupla akciót és 50 extra pörgetést hoz',
    'button_text_1': 'BÓNUSZ IGÉNYLÉSE',
    'greeting': ' {{ customer.first_name | default:"Játékos" | capitalize }}, a tárcsák hívnak! ',
    'body': 'Töltsd fel a számládat még ma a <strong class="promocode">UNDERDOG50</strong> kóddal és élvezd a <strong>100% bónuszt és 50 Ingyenes Pörgetést</strong> a <strong>Hand of Anubis by Hacksaw Gaming</strong> játékban.<br><br>Játssz a kedvenc nyerőgépeiden, nyerj sokat, és ne hagyd, hogy egyetlen pörgetés is kárba menjen. Az óra ketyeg – tedd emlékezetessé ezt a fordulót! 🐕<br><br>Igényeld a feltöltési bónuszodat:',
  },
  'pl-PL': {
    'subject': '🎰 100% Bonus + 50 Darmowych Spinów na Hand of Anubis',
    'preheader': 'Następna wpłata przynosi podwójną akcję i 50 dodatkowych spinów',
    'button_text_1': 'ODBIERZ BONUS',
    'greeting': ' {{ customer.first_name | default:"Gracz" | capitalize }}, bębny wzywają! ',
    'body': 'Doładuj konto już dziś kodem <strong class="promocode">UNDERDOG50</strong> i ciesz się <strong>100% bonusem i 50 Darmowymi Spinami</strong> na <strong>Hand of Anubis by Hacksaw Gaming</strong>.<br><br>Graj w ulubione sloty, trafiaj wygrane i niech każdy spin się liczy. Czas ucieka – niech ta runda będzie niezapomniana! 🐕<br><br>Odbierz swój bonus doładowania:',
  },
}

# ============ Email 1CS ============
T['Email 1CS'] = {
  'hu-HU': {
    'subject': '🎰 100% Bónusz + 50 Ingyenes Pörgetés: A második pörgetésed!',
    'preheader': 'Dupla izgalom a következő befizetésednél – igényeld a jutalmadat még ma',
    'button_text_1': 'BÓNUSZ IGÉNYLÉSE',
    'greeting': ' {{ customer.first_name | default:"Játékos" | capitalize }}, a tárcsák hívnak! ',
    'body': 'Töltsd fel a számládat még ma, írd be a <strong class="promocode">UNDERDOG50</strong> kódot és élvezd a <strong>100% bónuszt</strong> és <strong>50 Ingyenes Pörgetést a Hand of Anubis by Hacksaw Gaming</strong> játékban.<br><br>Játssz a kedvenc nyerőgépeiden, nyerj sokat, és ne hagyd, hogy egyetlen pörgetés is kárba menjen. Az óra ketyeg – tedd emlékezetessé ezt a fordulót! 🐕<br><br>Igényeld a feltöltési bónuszodat:',
  },
  'pl-PL': {
    'subject': '🎰 100% Bonus + 50 Darmowych Spinów: Twój drugi spin!',
    'preheader': 'Podwójna dawka emocji przy następnej wpłacie – odbierz nagrodę już dziś',
    'button_text_1': 'ODBIERZ BONUS',
    'greeting': ' {{ customer.first_name | default:"Gracz" | capitalize }}, bębny wzywają! ',
    'body': 'Doładuj konto już dziś, wpisz kod <strong class="promocode">UNDERDOG50</strong> i ciesz się <strong>100% bonusem</strong> i <strong>50 Darmowymi Spinami na Hand of Anubis by Hacksaw Gaming</strong>.<br><br>Graj w ulubione sloty, trafiaj wygrane i niech każdy spin się liczy. Czas ucieka – niech ta runda będzie niezapomniana! 🐕<br><br>Odbierz swój bonus doładowania:',
  },
}

# ============ Email 1S ============
T['Email 1S'] = {
  'hu-HU': {
    'subject': '🏆 20% Kockázatmentes Fogadás akár €500-ig vár',
    'preheader': 'A nyerő pillanatod már csak egy fogadásnyira van – kockázat nélkül',
    'button_text_1': 'FOGADJ MOST',
    'greeting': ' {{ customer.first_name | default:"Barátom" | capitalize }}, élvezd a játék izgalmát aggódás nélkül. ',
    'body': 'Kapj <strong>20% Kockázatmentes Fogadást</strong> akár €500-ig és változtasd minden tippedet nyerési eséllyé a <strong class="promocode">CLEARSHOT20</strong> kóddal.<br><br>Tedd meg a fogadásodat és érezd az adrenalint! 🏟️<br><br>Tedd meg a tipped:',
  },
  'pl-PL': {
    'subject': '🏆 20% Zakład Bez Ryzyka do €500 czeka',
    'preheader': 'Twój moment wygranej jest o jeden zakład – bez ryzyka',
    'button_text_1': 'OBSTAWIAJ TERAZ',
    'greeting': ' {{ customer.first_name | default:"Przyjacielu" | capitalize }}, ciesz się dreszczykiemgry bez obaw. ',
    'body': 'Odbierz <strong>20% Zakład Bez Ryzyka</strong> do €500 i zamień każdy typ w szansę na wygraną z kodem <strong class="promocode">CLEARSHOT20</strong>.<br><br>Postaw zakład i poczuj dreszczyk! 🏟️<br><br>Postaw swój typ:',
  },
}

# ============ Email 2CL ============
T['Email 2CL'] = {
  'hu-HU': {
    'subject': '🏆 €325,000 nyeremény a múlt héten: Nézd meg a nyerteseket',
    'preheader': 'Nézd meg a múlt hét legnagyobb nyereményeit – te lehetsz a következő',
    'button_text_1': 'PÖRGETÉS ÉS NYERÉS',
    'greeting': ' {{ customer.first_name | default:"Barátom" | capitalize }}, a múlt héten valóra vált a jackpot álom: ',
    'body': '<strong>🔥 Fi••••65y - €145,320</strong><br><strong>🔥 l<i>e••d4</i>• - €110,780</strong><br><strong>🔥 A••••in43 - €69,200</strong><br><br>Három játékos, három hatalmas nyeremény. Te leszel a következő a győztesek listáján?<br><br>Pörgess a nagy nyereményedért:',
  },
  'pl-PL': {
    'subject': '🏆 €325,000 wygranych w zeszłym tygodniu: Zobacz zwycięzców',
    'preheader': 'Zobacz największe wygrane zeszłego tygodnia – możesz być następny',
    'button_text_1': 'KRĘĆ I WYGRYWAJ',
    'greeting': ' {{ customer.first_name | default:"Przyjacielu" | capitalize }}, zeszły tydzień to spełniony sen o jackpocie: ',
    'body': '<strong>🔥 Fi••••65y - €145,320</strong><br><strong>🔥 l<i>e••d4</i>• - €110,780</strong><br><strong>🔥 A••••in43 - €69,200</strong><br><br>Trzech graczy, trzy ogromne wygrane. Czy będziesz następny na liście zwycięzców?<br><br>Kręć po swoją wielką wygraną:',
  },
}

# ============ Email 2CS ============
T['Email 2CS'] = {
  'hu-HU': {
    'subject': '🏆 €325,000 nyeremény a múlt héten: Te leszel a következő?',
    'preheader': 'Nézd meg a múlt hét legnagyobb nyerőgépes nyereményeit és inspirálódj',
    'button_text_1': 'PÖRGETÉS ÉS NYERÉS',
    'greeting': ' {{ customer.first_name | default:"Barátom" | capitalize }}, a múlt héten valóra vált a jackpot álom: ',
    'body': '<strong>🏆 Alex••••y - €145,320</strong><br><strong>🏆 l••677<i> - €110,780</i></strong><br><strong>🏆 i66••••7n - €69,200</strong><br><br>Három játékos, három hatalmas nyeremény – mind a kedvenc nyerőgépeiken pörgettek. Te leszel a következő a győztesek listáján? 🌟<br><br>Pörgess a nagy nyereményedért:',
  },
  'pl-PL': {
    'subject': '🏆 €325,000 wygranych w zeszłym tygodniu: Dołączysz?',
    'preheader': 'Zobacz największe wygrane na slotach w zeszłym tygodniu i daj się zainspirować',
    'button_text_1': 'KRĘĆ I WYGRYWAJ',
    'greeting': ' {{ customer.first_name | default:"Przyjacielu" | capitalize }}, zeszły tydzień to spełniony sen o jackpocie: ',
    'body': '<strong>🏆 Alex••••y - €145,320</strong><br><strong>🏆 l••677<i> - €110,780</i></strong><br><strong>🏆 i66••••7n - €69,200</strong><br><br>Trzech graczy, trzy ogromne wygrane – wszystkie z kręcenia ulubionych slotów. Czy będziesz następny na liście zwycięzców? 🌟<br><br>Kręć po swoją wielką wygraną:',
  },
}

# ============ Email 2S ============
T['Email 2S'] = {
  'hu-HU': {
    'subject': '⚽ Biztosítsd a fogadásodat: 20% Kockázatmentes Fogadás',
    'preheader': 'A legbiztosabb fogadásod ma kezdődik, akár €500-ig fedezve',
    'button_text_1': 'FOGADJ MOST',
    'greeting': ' {{ customer.first_name | default:"Barátom" | capitalize }}, lépj a pályára magabiztosan. ',
    'body': '<strong>20% Kockázatmentes Fogadással</strong> akár €500-ig, még egy elhibázott lövés sem állítja meg a nyerési sorozatodat. A kódod – <strong class="promocode">CLEARSHOT20</strong>.<br><br>A szorzók hívnak – tedd meg a fogadásodat most! 🥅<br><br>Szerezd meg a biztonsági hálódat:',
  },
  'pl-PL': {
    'subject': '⚽ Zabezpiecz swój zakład: 20% Zakład Bez Ryzyka',
    'preheader': 'Twój najbezpieczniejszy zakład zaczyna się dziś z pokryciem do €500',
    'button_text_1': 'OBSTAWIAJ TERAZ',
    'greeting': ' {{ customer.first_name | default:"Przyjacielu" | capitalize }}, wejdź na boisko z pewnością siebie. ',
    'body': 'Z <strong>20% Zakładem Bez Ryzyka</strong> do €500, nawet chybiony strzał nie zatrzyma Twojej serii. Kod dla Ciebie – <strong class="promocode">CLEARSHOT20</strong>.<br><br>Kursy wzywają – postaw teraz! 🥅<br><br>Odbierz swoją siatkę bezpieczeństwa:',
  },
}

# ============ Email 3CL ============
T['Email 3CL'] = {
  'hu-HU': {
    'subject': '🃏 100% Live Casino Bónusz: Duplázzál',
    'preheader': 'A következő befizetésed dupla izgalmat hoz az asztaloknál',
    'button_text_1': 'CSATLAKOZZ AZ ASZTALHOZ',
    'greeting': ' {{ customer.first_name | default:"Barátom" | capitalize }}, a kártyák készen állnak, a dealerek várnak. ',
    'body': 'Fizess be a <strong class="promocode">MATCH100</strong> kóddal és kapj <strong>100% bónuszt</strong> a következő feltöltésedre.<br>Lépj be az akcióba és számítson minden leosztás! ♠️<br><br>Csatlakozz az asztalhoz:',
  },
  'pl-PL': {
    'subject': '🃏 100% Bonus Live Casino: Podwój swoją grę',
    'preheader': 'Twoja następna wpłata przynosi podwójne emocje przy stołach',
    'button_text_1': 'DOŁĄCZ DO STOŁU',
    'greeting': ' {{ customer.first_name | default:"Przyjacielu" | capitalize }}, karty gotowe, krupierzy czekają. ',
    'body': 'Wpłać z kodem <strong class="promocode">MATCH100</strong> i odbierz <strong>100% bonus</strong> na następne doładowanie.<br>Wejdź do akcji i niech każda ręka się liczy! ♠️<br><br>Dołącz do stołu:',
  },
}

# ============ Email 3CS ============
T['Email 3CS'] = {
  'hu-HU': {
    'subject': '🔮 200% Bónusz + 50 Ingyenes Pörgetés a Tome of Madness-en',
    'preheader': 'Rich Wilde következő kalandja vár – háromszorázd az egyenlegedet most',
    'button_text_1': 'BÓNUSZ IGÉNYLÉSE',
    'greeting': ' {{ customer.first_name | default:"Barátom" | capitalize }}, lépj be Rich Wilde világába. ',
    'body': "Fizess be a <strong class=\"promocode\">OCCULT200</strong> kóddal és kapj <strong>200% bónuszt és 50 Ingyenes Pörgetést a Rich Wilde and the Tome of Madness</strong> by Play'n Go játékra, hogy felfedezd a rejtett kincseket.<br><br>Készen állsz, hogy megfordítsd a sors lapjait? A könyv nyitva áll. 📖<br><br>Nyisd meg a nyeremények könyvét:",
  },
  'pl-PL': {
    'subject': '🔮 200% Bonus + 50 Darmowych Spinów na Tome of Madness',
    'preheader': "Następna przygoda Rich Wilde'a czeka – potrój swoje saldo teraz",
    'button_text_1': 'ODBIERZ BONUS',
    'greeting': ' {{ customer.first_name | default:"Przyjacielu" | capitalize }}, wejdź do świata Rich Wilde. ',
    'body': "Wpłać z kodem <strong class=\"promocode\">OCCULT200</strong> i odbierz <strong>200% bonus i 50 Darmowych Spinów na Rich Wilde and the Tome of Madness</strong> by Play'n Go, żeby odkryć ukryte skarby.<br><br>Gotowy, by odwrócić karty losu? Księga jest otwarta. 📖<br><br>Otwórz księgę wygranych:",
  },
}

# ============ Email 3S ============
T['Email 3S'] = {
  'hu-HU': {
    'subject': '🥇 Fogadj akár €500-ig kockázatmentesen: 20% Bónusz',
    'preheader': 'A legmerészebb fogadásaidat is fedezzük a Kockázatmentes ajánlatunkkal',
    'button_text_1': 'TEDD MEG A FOGADÁSOD',
    'greeting': ' {{ customer.first_name | default:"Barátom" | capitalize }}, fogadj nagyot a veszteség félelme nélkül. ',
    'body': '<strong>20% Kockázatmentes Fogadással</strong> akár €500-ig, mindig a játékban maradsz.&nbsp;<br>Írd be a <strong class="promocode">CLEARSHOT20</strong> kódot.<br><br>Tedd meg a lépésedet – a győzelem már csak egy fogadásnyira lehet! 🏆<br><br>Tedd meg a védett fogadásodat:',
  },
  'pl-PL': {
    'subject': '🥇 Obstawiaj do €500 bez ryzyka: 20% Bonus',
    'preheader': 'Nawet najodważniejsze zakłady są zabezpieczone naszą ofertą Bez Ryzyka',
    'button_text_1': 'POSTAW ZAKŁAD',
    'greeting': ' {{ customer.first_name | default:"Przyjacielu" | capitalize }}, obstawiaj za duże stawki bez strachu. ',
    'body': 'Z <strong>20% Zakładem Bez Ryzyka</strong> do €500, zawsze jesteś w grze.&nbsp;<br>Wpisz kod <strong class="promocode">CLEARSHOT20</strong>.<br><br>Zrób swój ruch – wygrana może być o jeden zakład! 🏆<br><br>Postaw zabezpieczony zakład:',
  },
}

# ============ Email 4CL ============
T['Email 4CL'] = {
  'hu-HU': {
    'subject': '🎯 Live Casino nyertesek: Hatalmas kifizetések a múlt héten',
    'preheader': 'Nézd, kik nyertek nagyot az asztaloknál',
    'button_text_1': 'JÁTSZD ÉLŐ MOST',
    'greeting': ' {{ customer.first_name | default:"Barátom" | capitalize }}, a Live Casino asztalok lángoltak a múlt héten: ',
    'body': '<strong>💎 Dt••••s<i> – </i>€49,800</strong><br><strong><i></i><i>💎 </i>e•••95<i> </i>– €33,420</strong><br><strong><i></i><i>💎 </i>••p•••sh•• – €21,760</strong><br><br>A neved lehet a következő a győztesek tábláján.&nbsp;<br>Csatlakozz az asztalokhoz és tedd meg a lépésedet!<br><br>Játssz élőben most:',
  },
  'pl-PL': {
    'subject': '🎯 Zwycięzcy Live Casino: Wielkie wypłaty w zeszłym tygodniu',
    'preheader': 'Zobacz kto odszedł z ogromnymi wygranymi od stołów',
    'button_text_1': 'GRAJ NA ŻYWO',
    'greeting': ' {{ customer.first_name | default:"Przyjacielu" | capitalize }}, stoły Live Casino były rozgrzane w zeszłym tygodniu: ',
    'body': '<strong>💎 Dt••••s<i> – </i>€49,800</strong><br><strong><i></i><i>💎 </i>e•••95<i> </i>– €33,420</strong><br><strong><i></i><i>💎 </i>••p•••sh•• – €21,760</strong><br><br>Twoje imię może być następne na tablicy zwycięzców.&nbsp;<br>Dołącz do stołów i zrób swój ruch!<br><br>Graj na żywo teraz:',
  },
}

# ============ Email 4CS ============
T['Email 4CS'] = {
  'hu-HU': {
    'subject': '🎯 100% Bónusz + 50 IP a Hand of Anubis-on',
    'preheader': 'A következő befizetésed több szórakozást és több nyerési esélyt hoz',
    'button_text_1': 'BÓNUSZ IGÉNYLÉSE',
    'greeting': ' {{ customer.first_name | default:"Barátom" | capitalize }}, tegyük a következő pörgetésedet kétszer olyan izgalmassá: ',
    'body': 'Kapj <strong>100% bónuszt és 50 Ingyenes Pörgetést a Hand of Anubis by Hacksaw Gaming</strong> játékra a <strong class="promocode">UNDERDOG50</strong> kóddal, amikor feltöltöd.<br><br>Több egyenleg, több pörgetés, több esély a nagy nyereményre – benne vagy? 🐾<br><br>Duplázd meg az egyenlegedet most:',
  },
  'pl-PL': {
    'subject': '🎯 100% Bonus + 50 DS na Hand of Anubis',
    'preheader': 'Twoja następna wpłata daje więcej zabawy i więcej szans na wygraną',
    'button_text_1': 'ODBIERZ BONUS',
    'greeting': ' {{ customer.first_name | default:"Przyjacielu" | capitalize }}, sprawmy, żeby następny spin był dwa razy bardziej ekscytujący: ',
    'body': 'Odbierz <strong>100% bonus i 50 Darmowych Spinów na Hand of Anubis by Hacksaw Gaming</strong> z kodem <strong class="promocode">UNDERDOG50</strong> przy doładowaniu.<br><br>Więcej salda, więcej spinów, więcej szans na trafienie czegoś wielkiego – wchodzisz? 🐾<br><br>Podwój swoje saldo teraz:',
  },
}

# ============ Email 4S ============
T['Email 4S'] = {
  'hu-HU': {
    'subject': '🏅 20% Kockázatmentes Fogadás: Fedezve vagy',
    'preheader': 'Lőj a nagy nyereményre akár €500-ig fedezve a fogadásodon',
    'button_text_1': 'KEZDJ FOGADNI',
    'greeting': ' {{ customer.first_name | default:"Barátom" | capitalize }}, lépj be az akcióba nyomás nélkül. ',
    'body': 'Élvezd a <strong>20% Kockázatmentes Fogadást</strong> akár €500-ig és változtass minden tétet nyerési eséllyé a <strong class="promocode">CLEARSHOT20</strong> kóddal.<br><br>Semmi félelem, csak tiszta adrenalin. 🔥<br><br>Kezdj fogadni kockázatmentesen:',
  },
  'pl-PL': {
    'subject': '🏅 20% Zakład Bez Ryzyka: Jesteś zabezpieczony',
    'preheader': 'Celuj w wielkie wygrane z pokryciem do €500 na zakładzie',
    'button_text_1': 'ZACZNIJ OBSTAWIAĆ',
    'greeting': ' {{ customer.first_name | default:"Przyjacielu" | capitalize }}, wejdź do akcji bez presji. ',
    'body': 'Ciesz się <strong>20% Zakładem Bez Ryzyka</strong> do €500 i zamień każdy zakład w szansę na wygraną z kodem <strong class="promocode">CLEARSHOT20</strong>.<br><br>Żadnego strachu, tylko czysty adrenalin. 🔥<br><br>Zacznij obstawiać bez ryzyka:',
  },
}

# ============ Email 5CL ============
T['Email 5CL'] = {
  'hu-HU': {
    'subject': '💎 200% Live Casino Bónusz: Háromszorázd az egyenlegedet',
    'preheader': 'A következő Live Casino session-öd jelentősen erősebbé vált',
    'button_text_1': 'JÁTSZD ÉLŐ MOST',
    'greeting': ' {{ customer.first_name | default:"Barátom" | capitalize }}, foglald el a helyed a Live Casino asztaloknál és játssz háromszoros erővel. ',
    'body': 'Fizess be a <strong class="promocode">ROCKET200</strong> kóddal és kapj <strong>200% bónuszt</strong> a következő feltöltésedre.<br>Az akció él – készen állsz csatlakozni? 🚀<br><br>Turbózd fel az egyenlegedet:',
  },
  'pl-PL': {
    'subject': '💎 200% Bonus Live Casino: Potrój swoje saldo',
    'preheader': 'Twoja następna sesja Live Casino stała się większa i lepsza',
    'button_text_1': 'GRAJ NA ŻYWO',
    'greeting': ' {{ customer.first_name | default:"Przyjacielu" | capitalize }}, zajmij miejsce przy stołach Live Casino i graj z potrójną mocą. ',
    'body': 'Wpłać z kodem <strong class="promocode">ROCKET200</strong> i odbierz <strong>200% bonus</strong> na następne doładowanie.<br>Akcja trwa na żywo – gotowy dołączyć? 🚀<br><br>Doładuj swoje saldo:',
  },
}

# ============ Email 5CS ============
T['Email 5CS'] = {
  'hu-HU': {
    'subject': '📚 200% Bónusz + 50 IP: Háromszorázd az egyenlegedet!',
    'preheader': 'Lépj be Rich Wilde kalandjába és igényeld a jutalmaidat a befizetéseddel',
    'button_text_1': 'BÓNUSZ IGÉNYLÉSE',
    'greeting': ' {{ customer.first_name | default:"Barátom" | capitalize }}, a következő befizetésed megnyithatja a szerencse kapuit: ',
    'body': "Kapj <strong>200% bónuszt és 50 Ingyenes Pörgetést a Rich Wilde and the Tome of Madness</strong> by Play'n GO játékra a <strong class=\"promocode\">OCCULT200</strong> kóddal.<br><br>A tárcsák készen állnak – elég bátor vagy szembenézni az őrülettel? 👁️<br><br>Fedezd fel a titkos kincseket:",
  },
  'pl-PL': {
    'subject': '📚 200% Bonus + 50 DS: Potrój swoje saldo!',
    'preheader': "Wejdź w przygodę Rich Wilde'a i odbierz nagrody przy wpłacie",
    'button_text_1': 'ODBIERZ BONUS',
    'greeting': ' {{ customer.first_name | default:"Przyjacielu" | capitalize }}, Twoja następna wpłata może otworzyć bramy fortuny: ',
    'body': "Odbierz <strong>200% bonus i 50 Darmowych Spinów w Rich Wilde and the Tome of Madness</strong> by Play'n GO z kodem <strong class=\"promocode\">OCCULT200</strong>.<br><br>Bębny są gotowe – czy jesteś na tyle odważny, by zmierzyć się z szaleństwem? 👁️<br><br>Odkryj sekretne skarby:",
  },
}

# ============ Email 5S ============
T['Email 5S'] = {
  'hu-HU': {
    'subject': '🏟 Nagy sportfogadási nyeremények a múlt héten: Nézd meg az eredményeket',
    'preheader': 'Nézd, kik nyertek nagyot – te leszel a következő?',
    'button_text_1': 'TEDD MEG A FOGADÁSOD',
    'greeting': ' {{ customer.first_name | default:"Barátom" | capitalize }}, nézd meg a top 3 fogadót, aki beváltotta a múlt héten: ',
    'body': '<strong>🏆 se•••54 – €48,200</strong><br><strong>🏆 Ra••34•• – €32,900</strong><br><strong>🏆 H••••a – €26,400</strong><br><br>A nyerő szelvényed már csak egy fogadásnyira lehet. 🎫<br><br>Tedd meg a nyerő fogadásodat:',
  },
  'pl-PL': {
    'subject': '🏟 Wielkie wygrane sportowe w zeszłym tygodniu: Zobacz wyniki',
    'preheader': 'Zobacz kto trafił grubo – może Ty będziesz następny?',
    'button_text_1': 'POSTAW ZAKŁAD',
    'greeting': ' {{ customer.first_name | default:"Przyjacielu" | capitalize }}, sprawdź top 3 typujących, którzy zgarnęli w zeszłym tygodniu: ',
    'body': '<strong>🏆 se•••54 – €48,200</strong><br><strong>🏆 Ra••34•• – €32,900</strong><br><strong>🏆 H••••a – €26,400</strong><br><br>Twój wygrany kupon może być o jeden zakład. 🎫<br><br>Postaw swój wygrany zakład:',
  },
}

# ============ Email 6CL ============
T['Email 6CL'] = {
  'hu-HU': {
    'subject': '🏆 Top 3 nyertesek a múlt héten: Nézd meg a listát',
    'preheader': 'Nézd, mennyit nyertek a top 3 játékosaink nemrég',
    'button_text_1': 'JÁTSSZ MOST',
    'greeting': ' {{ customer.first_name | default:"Barátom" | capitalize }}, a múlt hét elképesztő volt: ',
    'body': '<strong>💰 se•••s – €48,200</strong><br><strong>💰 M8•••7 – €32,750</strong><br><strong>💰 g•••ns – €27,460</strong><br><br>Három szerencsés pörgetés, három életreszóló nyeremény. Meglátjuk a nevedet ezen a heti listán?<br><br>Próbáld ki a szerencsédet ma:',
  },
  'pl-PL': {
    'subject': '🏆 Top 3 zwycięzców w zeszłym tygodniu: Sprawdź listę',
    'preheader': 'Zobacz ile zgarnęli nasi top 3 gracze ostatnio',
    'button_text_1': 'GRAJ TERAZ',
    'greeting': ' {{ customer.first_name | default:"Przyjacielu" | capitalize }}, zeszły tydzień był niesamowity: ',
    'body': '<strong>💰 se•••s – €48,200</strong><br><strong>💰 M8•••7 – €32,750</strong><br><strong>💰 g•••ns – €27,460</strong><br><br>Trzy szczęśliwe obroty, trzy nagrody zmieniające życie. Zobaczymy Twoje imię na liście tego tygodnia?<br><br>Sprawdź swoje szczęście dziś:',
  },
}

# ============ Email 6CS ============
T['Email 6CS'] = {
  'hu-HU': {
    'subject': '🏆 Hatalmas jackpot nyeremények a múlt héten: Nézd meg',
    'preheader': 'Nézd, mennyit nyertek a top 3 játékosaink nemrég',
    'button_text_1': 'JÁTSSZ MOST',
    'greeting': ' {{ customer.first_name | default:"Barátom" | capitalize }}, a múlt hét elképesztő volt: ',
    'body': '<strong>💰 ses – €48,200</strong><br><strong>💰 M87 – €32,750</strong><br><strong>💰 g•ns – €27,460</strong><br><br>Három szerencsés pörgetés, három életreszóló nyeremény. Meglátjuk a nevedet ezen a heti listán?<br><br>Próbáld ki a szerencsédet ma:',
  },
  'pl-PL': {
    'subject': '🏆 Ogromne wygrane na jackpocie w zeszłym tygodniu: Sprawdź',
    'preheader': 'Zobacz ile zgarnęli nasi top 3 gracze ostatnio',
    'button_text_1': 'GRAJ TERAZ',
    'greeting': ' {{ customer.first_name | default:"Przyjacielu" | capitalize }}, zeszły tydzień był niesamowity: ',
    'body': '<strong>💰 ses – €48,200</strong><br><strong>💰 M87 – €32,750</strong><br><strong>💰 g•ns – €27,460</strong><br><br>Trzy szczęśliwe obroty, trzy nagrody zmieniające życie. Zobaczymy Twoje imię na liście tego tygodnia?<br><br>Sprawdź swoje szczęście dziś:',
  },
}

# ============ Email 6S ============
T['Email 6S'] = {
  'hu-HU': {
    'subject': '🎯 20% Kockázatmentes Fogadás: A második esélyed',
    'preheader': 'Lőj – akár €500-ig fedezünk',
    'button_text_1': 'KEZDJ FOGADNI',
    'greeting': ' {{ customer.first_name | default:"Barátom" | capitalize }}, rajtad a lépés. ',
    'body': 'Élvezd a <strong>20% Kockázatmentes Fogadást</strong> akár €500-ig és játssz habozás nélkül a <strong class="promocode">CLEARSHOT20</strong> kóddal.<br><br>Minden tipped közelebb visz a nyereményhez. ⚽<br><br>Igényeld a fedezetedet:',
  },
  'pl-PL': {
    'subject': '🎯 20% Zakład Bez Ryzyka: Twoja druga szansa',
    'preheader': 'Celuj – zabezpieczymy Cię do €500',
    'button_text_1': 'ZACZNIJ OBSTAWIAĆ',
    'greeting': ' {{ customer.first_name | default:"Przyjacielu" | capitalize }}, Twój ruch. ',
    'body': 'Ciesz się <strong>20% Zakładem Bez Ryzyka</strong> do €500 i graj bez wahania z kodem <strong class="promocode">CLEARSHOT20</strong>.<br><br>Każdy typ przybliża Cię do wygranej. ⚽<br><br>Odbierz swoją ochronę:',
  },
}

# ============ Email 7CL ============
T['Email 7CL'] = {
  'hu-HU': {
    'subject': '🎩 210% Live Casino erősítés: Exkluzív ajánlat',
    'preheader': 'Háromszoros izgalom a Live Casino-ban a következő befizetéseddel',
    'button_text_1': 'JÁTSZD ÉLŐ MOST',
    'greeting': ' {{ customer.first_name | default:"Barátom" | capitalize }}, lépj a Live Casino-ba és játssz felülmúlhatatlan erővel. ',
    'body': 'Fizess be a <strong class="promocode">BLAST210</strong> kóddal és kapj <strong>210% bónuszt</strong> a következő feltöltésedre.<br>A dealerek készen állnak – a nyerőszériád most kezdődik. 🎲<br><br>Igényeld az exkluzív bónuszodat:',
  },
  'pl-PL': {
    'subject': '🎩 210% Boost Live Casino: Ekskluzywna oferta',
    'preheader': 'Potrójna dawka emocji w Live Casino przy następnej wpłacie',
    'button_text_1': 'GRAJ NA ŻYWO',
    'greeting': ' {{ customer.first_name | default:"Przyjacielu" | capitalize }}, wejdź do Live Casino i graj z niezrównaną mocą. ',
    'body': 'Wpłać z kodem <strong class="promocode">BLAST210</strong> i odbierz <strong>210% bonus</strong> na następne doładowanie.<br>Krupierzy są gotowi – Twoja seria wygranych zaczyna się teraz. 🎲<br><br>Odbierz swój ekskluzywny boost:',
  },
}

# ============ Email 7CS ============
T['Email 7CS'] = {
  'hu-HU': {
    'subject': '💰 3 hatalmas nyertes a múlt héten – Miért ne te?',
    'preheader': '3 játékos. 3 nyeremény. A neved lehet a következő a listán',
    'button_text_1': 'JÁTSSZ MOST',
    'greeting': ' {{ customer.first_name | default:"Barátom" | capitalize }}, íme, kik ütötték meg az aranyat a múlt héten: ',
    'body': '<strong>🥇 L<i>i•••n8</i>• – €45,320</strong><br><strong>🥈 a••7tz – €38,940</strong><br><strong>🥉 h••••in – €26,580</strong><br><br>A neved a következő bajnokok listáján lehet.&nbsp;<br>Csak egy szerencsés pörgetés kell! 🎰<br><br>Csatlakozz a győztesek köréhez:',
  },
  'pl-PL': {
    'subject': '💰 3 ogromne wygrane w zeszłym tygodniu – Dlaczego nie Ty?',
    'preheader': '3 graczy. 3 wygrane. Twoje imię może być następne na liście',
    'button_text_1': 'GRAJ TERAZ',
    'greeting': ' {{ customer.first_name | default:"Przyjacielu" | capitalize }}, oto kto trafił złoto w zeszłym tygodniu: ',
    'body': '<strong>🥇 L<i>i•••n8</i>• – €45,320</strong><br><strong>🥈 a••7tz – €38,940</strong><br><strong>🥉 h••••in – €26,580</strong><br><br>Twoje imię może pojawić się na następnej liście mistrzów.&nbsp;<br>Wystarczy jeden szczęśliwy spin! 🎰<br><br>Dołącz do kręgu zwycięzców:',
  },
}

# ============ Email 7S ============
T['Email 7S'] = {
  'hu-HU': {
    'subject': '🏇 Fogadj merészen: 20% Kockázatmentes Fogadás aktív',
    'preheader': 'Fogadj akár €500-ig a veszteség félelme nélkül',
    'button_text_1': 'TEDD MEG A FOGADÁSOD',
    'greeting': ' {{ customer.first_name | default:"Barátom" | capitalize }}, szállj be az akcióba! ',
    'body': 'Kapj <strong>20% Kockázatmentes Fogadást</strong> akár €500-ig a <strong class="promocode">CLEARSHOT20</strong> kóddal.<br><br>Legyen foci, tenisz vagy autóverseny – a fogadásod fedezve van. Semmi kockázat, csupa izgalom. 🏁<br><br>Indulhat a nyerő szériád:',
  },
  'pl-PL': {
    'subject': '🏇 Obstawiaj odważnie: 20% Zakład Bez Ryzyka aktywny',
    'preheader': 'Obstawiaj do €500 bez strachu przed przegraniem',
    'button_text_1': 'POSTAW ZAKŁAD',
    'greeting': ' {{ customer.first_name | default:"Przyjacielu" | capitalize }}, wejdź do akcji! ',
    'body': 'Odbierz <strong>20% Zakład Bez Ryzyka</strong> do €500 z kodem <strong class="promocode">CLEARSHOT20</strong>.<br><br>Czy to piłka nożna, tenis czy wyścigi – Twój zakład jest zabezpieczony. Zero ryzyka, sam dreszczyk. 🏁<br><br>Ruszaj po wygraną:',
  },
}

# ============ Email 8CL ============
T['Email 8CL'] = {
  'hu-HU': {
    'subject': '💥 220% Bónusz: Turbózd fel a Live Session-ödet',
    'preheader': 'Több zseton, több esély, több nyeremény a következő befizetéseddel',
    'button_text_1': 'CSATLAKOZZ AZ ASZTALHOZ',
    'greeting': ' {{ customer.first_name | default:"Barátom" | capitalize }}, a Live Casino padló hív. ',
    'body': 'Fizess be a <strong class="promocode">BOOSTED220</strong> kóddal és kapj <strong>220% bónuszt</strong> a következő feltöltésedre.<br>A helyed vár – tegyük, hogy minden leosztás számítson! 🔴⚫<br><br>Kapd meg a <strong>220% bónuszodat</strong>:',
  },
  'pl-PL': {
    'subject': '💥 220% Bonus: Doładuj swoją sesję Live',
    'preheader': 'Więcej żetonów, więcej szans, więcej wygranych przy następnej wpłacie',
    'button_text_1': 'DOŁĄCZ DO STOŁU',
    'greeting': ' {{ customer.first_name | default:"Przyjacielu" | capitalize }}, podłoga Live Casino wzywa. ',
    'body': 'Wpłać z kodem <strong class="promocode">BOOSTED220</strong> i odbierz <strong>220% bonus</strong> na następne doładowanie.<br>Twoje miejsce czeka – niech każda ręka się liczy! 🔴⚫<br><br>Odbierz swój <strong>220% bonus</strong>:',
  },
}

# ============ Email 8CS ============
T['Email 8CS'] = {
  'hu-HU': {
    'subject': '🎰 Igényelj 100 Ingyenes Pörgetést a Legacy of Dead-en',
    'preheader': 'Lépj be a sírokba és igényeld a nyereményeidet a következő befizetéseddel',
    'button_text_1': 'INGYENES PÖRGETÉS IGÉNYLÉSE',
    'greeting': ' {{ customer.first_name | default:"Barátom" | capitalize }}, a Legacy of Dead tárcsái hívnak. ',
    'body': "Fizess be a <strong class=\"promocode\">PHARAOH100</strong> kóddal és oldd fel a <strong>100 Ingyenes Pörgetést a Legacy of Dead</strong> by Play'n Go játékra, hogy felfedezd a rejtett kincseket.<br>A kalandod egyetlen pörgetéssel kezdődik – készen állsz? 🏺<br><br>Lépj be a nyeremények sírkamrájába:",
  },
  'pl-PL': {
    'subject': '🎰 Odbierz 100 Darmowych Spinów na Legacy of Dead',
    'preheader': 'Wejdź do grobowca i zgarnij wygrane przy następnej wpłacie',
    'button_text_1': 'ODBIERZ DARMOWE SPINY',
    'greeting': ' {{ customer.first_name | default:"Przyjacielu" | capitalize }}, bębny Legacy of Dead wzywają. ',
    'body': "Wpłać z kodem <strong class=\"promocode\">PHARAOH100</strong> i odblokuj <strong>100 Darmowych Spinów na Legacy of Dead</strong> by Play'n Go, żeby odkryć ukryte skarby.<br>Twoja przygoda zaczyna się od jednego spinu – gotowy? 🏺<br><br>Wejdź do grobowca wygranych:",
  },
}

# ============ Email 8S ============
T['Email 8S'] = {
  'hu-HU': {
    'subject': '🏆 20% Kockázatmentes Fogadás: Nyerj vagy kapd vissza',
    'preheader': 'A biztonsági hálód vár – fogadj akár €500-ig kockázatmentesen',
    'button_text_1': 'FOGADÁSOK IGÉNYLÉSE',
    'greeting': ' {{ customer.first_name | default:"Barátom" | capitalize }}, szállj be a játékba! ',
    'body': 'Játssz a <strong>20% Kockázatmentes Fogadással</strong> akár €500-ig. A kódod: <strong class="promocode">CLEARSHOT20</strong>.<br><br>Mellélőttél? Fedezünk.<br>Betaláltál? A nyeremény mind a tied.<br>A legbiztonságosabb módja az izgalom hajszolásának itt van. 🛡️<br><br>Igényeld a fogadásaidat:',
  },
  'pl-PL': {
    'subject': '🏆 20% Zakład Bez Ryzyka: Wygrywaj lub odzyskaj',
    'preheader': 'Twoja siatka bezpieczeństwa czeka – obstawiaj do €500 bez ryzyka',
    'button_text_1': 'ODBIERZ ZAKŁADY',
    'greeting': ' {{ customer.first_name | default:"Przyjacielu" | capitalize }}, wejdź do gry! ',
    'body': 'Graj z <strong>20% Zakładem Bez Ryzyka</strong> do €500. Twój kod: <strong class="promocode">CLEARSHOT20</strong>.<br><br>Nie trafiłeś? Zabezpieczamy Cię.<br>Trafiłeś? Wygrana jest cała Twoja.<br>Najbezpieczniejszy sposób na ściganie emocji jest tutaj. 🛡️<br><br>Odbierz swoje zakłady:',
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
            if 'greeting' in tr:
                old_text1 = d.get('text_1', '')
                # Find existing greeting inside <strong> tag
                m = re.search(r'(<strong[^>]*>)(.*?)(</strong>)', old_text1, re.DOTALL)
                if m:
                    d['text_1'] = old_text1[:m.start(2)] + tr['greeting'] + old_text1[m.end(2):]
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

print(f"Nutrition #2: {changes} fields translated")
print(f"Expected: 240 (24 emails x 2 locales x 5 fields)")
