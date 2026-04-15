#!/usr/bin/env python3
"""Apply hu-HU and pl-PL translations to DEP Retention - Table data.txt"""
import os, re, sys

base = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(base, 'DEP Retention - Table data.txt')

# ──────────────────────────────────────────────────────────────────
# TRANSLATION DATA: { email_name: { field: value } }
# Fields: subject_hu, subject_pl, preheader_hu, preheader_pl,
#         default_hu, default_pl,
#         greeting_en (to find), greeting_hu, greeting_pl,
#         text2_p_hu, text2_p_pl, text3_p_hu, text3_p_pl (None = skip),
#         button_hu, button_pl
# ──────────────────────────────────────────────────────────────────

T = {}

# ════════════════════════════════════════════════════════════════
# EMAIL 1C — 170% Bonus, SURGE170, Casino
# ════════════════════════════════════════════════════════════════
T["Email 1C"] = dict(
    subject_hu="💥 170% Bonus: Turbózd fel a játékod még ma",
    subject_pl="💥 170% Bonus: Doładuj swoją grę już dziś",
    preheader_hu="Nézd meg, mi vár rád, hogy nagyot nyerj az asztaloknál",
    preheader_pl="Sprawdź, co na Ciebie czeka, żebyś wygrywał przy stolikach",
    default_hu="Játékos", default_pl="Gracz",
    greeting_en=", the floor is yours!",
    greeting_hu=", a parkett a tiéd!",
    greeting_pl=", parkiet jest Twój!",
    text2_p_hu='Miért játszanál csak a befizetésedből, amikor <strong>170%</strong>-kal többel is mehetsz? Felturbózzuk a következő feltöltésedet, hogy tovább játszhass és nagyobb nyereményekre vadászhass.',
    text2_p_pl='Po co grać tylko za depozyt, skoro możesz grać z <strong>170%</strong> więcej? Doładowujemy Twój następny depozyt, żebyś grał dłużej i celował w większe wygrane.',
    text3_p_hu='Írd be a <strong class="promocode">SURGE170</strong> kódot a következő befizetésed előtt, és oldd fel a <strong>170% Bonusodat</strong>, hogy az egyenleged valódi előnnyé váljon.<br><br>Az akció élőben zajlik a <strong>Celsius Casino</strong>-ban - aktiváld a <strong>170% Bonusodat</strong>, válaszd ki a kedvenc asztalodat és lépj magabiztosan.',
    text3_p_pl='Wpisz kod <strong class="promocode">SURGE170</strong> przed następnym depozytem, żeby odblokować swój <strong>170% Bonus</strong> i zamienić saldo w realną przewagę.<br><br>Akcja trwa na żywo w <strong>Celsius Casino</strong> - aktywuj swój <strong>170% Bonus</strong>, wybierz ulubiony stolik i graj z pewnością.',
    button_hu="TURBÓZD FEL AZ EGYENLEGED",
    button_pl="DOŁADUJ SWOJE SALDO",
)

# ════════════════════════════════════════════════════════════════
# EMAIL 1S — 20% NoRisk Free Bet, WINSAFE20, Sport
# ════════════════════════════════════════════════════════════════
T["Email 1S"] = dict(
    subject_hu="🥊 20% NoRisk Free Bet: Üss keményen",
    subject_pl="🥊 20% NoRisk Free Bet: Uderz mocno",
    preheader_hu="A vonal nyitva - kockázatmentes előnyöd vár",
    preheader_pl="Linia otwarta - Twoja przewaga bez ryzyka czeka",
    default_hu="Bajnok", default_pl="Mistrzu",
    greeting_en=", victory is within reach!",
    greeting_hu=", a győzelem karnyújtásnyira van!",
    greeting_pl=", zwycięstwo na wyciągnięcie ręki!",
    text2_p_hu='Semmi sem jobb, mint egy nyerő fogadás öröme - ezért támogatjuk a következő lépésedet egy <strong>20% NoRisk Free Bet</strong>-tel, hogy magabiztosan játszhass.',
    text2_p_pl='Nic nie przebije emocji z wygranego zakładu - dlatego wspieramy Twój następny ruch <strong>20% NoRisk Free Bet</strong>, żebyś grał z pewnością.',
    text3_p_hu='Az aktiváláshoz írd be a <strong class="promocode">WINSAFE20</strong> promókódot a következő befizetésed előtt. A <strong>20% NoRisk Free Bet</strong> azonnal használatra kész.<br><br>Fedezd fel a legforróbb meccseket a <strong>Celsius Sport</strong>-on, válaszd ki a kedvenc piacodat és tedd meg a tipped, amíg az oddsok élőben vannak.',
    text3_p_pl='Żeby aktywować, wpisz kod promocyjny <strong class="promocode">WINSAFE20</strong> przed następnym depozytem. Twój <strong>20% NoRisk Free Bet</strong> będzie od razu gotowy do użycia.<br><br>Sprawdź najgorętsze mecze na <strong>Celsius Sport</strong>, wybierz ulubiony rynek i postaw, dopóki kursy są na żywo.',
    button_hu="AKTIVÁLD AZ ELŐNYÖD",
    button_pl="AKTYWUJ SWOJĄ PRZEWAGĘ",
)

# ════════════════════════════════════════════════════════════════
# EMAIL 2C — 150% + 70 FS Chaos Crew II, CREWBOOST150, Casino
# ════════════════════════════════════════════════════════════════
T["Email 2C"] = dict(
    subject_hu="⚡ 150% + 70 Free Spin: Ne hagyd ki, kapd el!",
    subject_pl="⚡ 150% + 70 Free Spinów: Nie zwlekaj, bierz!",
    preheader_hu="A következő nagy nyereményed kész - te kész vagy?",
    preheader_pl="Twoja następna duża wygrana czeka - a Ty?",
    default_hu="Játékos", default_pl="Gracz",
    greeting_en=", the games are waiting!",
    greeting_hu=", a játékok várnak!",
    greeting_pl=", gry czekają na Ciebie!",
    text2_p_hu='Miért ülnél a kispadon, amikor győzelmeket halmozhatsz? Fizess be most és lépj szintet egy <strong>150% bonus + 70 Free Spin</strong> juttatással a <strong>Chaos Crew II by Hacksaw Gaming</strong> játékban.',
    text2_p_pl='Po co siedzieć z boku, skoro możesz zbierać wygrane? Wpłać teraz i wejdź na wyższy poziom ze <strong>150% bonusem + 70 Free Spinami</strong> na <strong>Chaos Crew II by Hacksaw Gaming</strong>.',
    text3_p_hu='A feloldáshoz add hozzá a <strong class="promocode">CREWBOOST150</strong> promókódot, majd teljesítsd a befizetést - a <strong>150% bonuszod és 70 Free Spin</strong> az első pörgéstől kész.<br><br>Az akció nem áll meg a <strong>Celsius Casino</strong>-ban. Ugorj be a <strong>Chaos Crew II by Hacksaw Gaming</strong> játékba és vadássz a következő nagy nyereményre.',
    text3_p_pl='Żeby odblokować, wpisz kod promocyjny <strong class="promocode">CREWBOOST150</strong>, a następnie dokonaj wpłaty - Twój <strong>150% bonus i 70 Free Spinów</strong> czekają od pierwszego obrotu.<br><br>Akcja w <strong>Celsius Casino</strong> nie zwalnia. Wskakuj do <strong>Chaos Crew II by Hacksaw Gaming</strong> i poluj na następną wielką wygraną.',
    button_hu="KAPD EL A DUPLA JUTALMAT",
    button_pl="ODBIERZ PODWÓJNĄ NAGRODĘ",
)

# ════════════════════════════════════════════════════════════════
# EMAIL 2S — 20% NoRisk Free Bet Prime Time, WINSAFE20, Sport
# ════════════════════════════════════════════════════════════════
T["Email 2S"] = dict(
    subject_hu="⚽ 20% NoRisk Free Bet: Itt a főműsoridő",
    subject_pl="⚽ 20% NoRisk Free Bet: Czas na Prime Time",
    preheader_hu="A nap meccse hív - szállj be védelemmel",
    preheader_pl="Mecz dnia czeka - wejdź z ochroną",
    default_hu="Szurkoló", default_pl="Kibicu",
    greeting_en=", the lights are on!",
    greeting_hu=", a fények égnek!",
    greeting_pl=", światła się zapalają!",
    text2_p_hu='Közeleg a Prime Time - a nap legnagyobb meccse, hatalmas feszültség, és egyetlen pillanat mindent megváltoztathat. Szállj be a kezdőrúgás előtt.',
    text2_p_pl='Prime Time tuż-tuż - najważniejszy mecz dnia, ogromne napięcie, a jeden moment może zmienić wszystko. Wejdź do gry przed pierwszym gwizdkiem.',
    text3_p_hu='Hogy felpörgesd a mai akciót, aktiváld a <strong>20% NoRisk Free Bet</strong>-edet: add hozzá a <strong class="promocode">WINSAFE20</strong> promókódot, majd teljesítsd a befizetést a <strong>20% NoRisk Free Bet</strong> védelmed aktiválásához.<br><br>Töltsd fel a bankrollodat, nézd meg a felállásokat és tedd meg a tipped a <strong>Celsius Sport</strong>-on biztonsági hálóval a hátad mögött.',
    text3_p_pl='Żeby podkręcić dzisiejsze emocje, aktywuj swój <strong>20% NoRisk Free Bet</strong>: wpisz kod promocyjny <strong class="promocode">WINSAFE20</strong>, a następnie dokonaj wpłaty, żeby aktywować ochronę <strong>20% NoRisk Free Bet</strong>.<br><br>Doładuj bankroll, sprawdź składy i postaw na <strong>Celsius Sport</strong> z siatką bezpieczeństwa za plecami.',
    button_hu="AKTIVÁLD A NORISK TÉTET",
    button_pl="AKTYWUJ NORISK ZAKŁAD",
)

# ════════════════════════════════════════════════════════════════
# EMAIL 3C — WINNER Casino, no promo, text_3=team sig (skip)
# ════════════════════════════════════════════════════════════════
T["Email 3C"] = dict(
    subject_hu="🎡 Irány a nyeremények: A múlt hét csúcstalálataі",
    subject_pl="🎡 Droga do wygranych: Topowe trafienia ostatniego tygodnia",
    preheader_hu="Hagyd magad mögött a hétköznapokat és lépj be a győztesek körébe",
    preheader_pl="Zostaw codzienność za sobą i wkrocz w krąg zwycięzców",
    default_hu="Játékos", default_pl="Gracz",
    greeting_en=", ready to change the vibe?",
    greeting_hu=", készen állsz a hangulatváltásra?",
    greeting_pl=", gotowy na zmianę klimatu?",
    text2_p_hu='Néha nem több zajra van szükséged - hanem egy jobb adrenalinfröccsre. A <strong>Celsius Casino</strong>-ban a top játékosok a múlt héten nagyot kaszáltak:<br><br><strong>🏆 Lu••••7 – €52,300<br>🏆 S•••••n – €35,900<br>🏆 Bi•••••t – €19,400</strong><br><br>Az asztalok hívnak és a nyerőgépek készen állnak.<br>Kapcsold ki a stresszt és kapcsold be az izgalmat a <strong>Celsius Casino</strong>-ban - a helyed vár.',
    text2_p_pl='Czasem nie potrzebujesz więcej hałasu - potrzebujesz lepszego kopa adrenaliny. W <strong>Celsius Casino</strong> topowi gracze w zeszłym tygodniu zgarnęli poważne wygrane:<br><br><strong>🏆 Lu••••7 – €52,300<br>🏆 S•••••n – €35,900<br>🏆 Bi•••••t – €19,400</strong><br><br>Stoliki wzywają, a automaty są gotowe.<br>Wyłącz stres i włącz emocje w <strong>Celsius Casino</strong> - Twoje miejsce czeka.',
    text3_p_hu=None,  # team sig - skip
    text3_p_pl=None,
    button_hu="KEZDD EL MA A KALANDOT",
    button_pl="ZACZNIJ SWOJĄ PRZYGODĘ",
)

# ════════════════════════════════════════════════════════════════
# EMAIL 3S — WINNER Sport, no promo, text_3=team sig (skip)
# ════════════════════════════════════════════════════════════════
T["Email 3S"] = dict(
    subject_hu="🏆 Heti győztesek: Ők jól döntöttek",
    subject_pl="🏆 Tygodniowi zwycięzcy: Dobrze postawili",
    preheader_hu="Nézd meg, kik uralták a vonalakat ezen a héten a Celsius Sport-on",
    preheader_pl="Zobacz, kto zdominował kursy w tym tygodniu na Celsius Sport",
    default_hu="Bajnok", default_pl="Mistrzu",
    greeting_en=", will you be next?",
    greeting_hu=", te leszel a következő?",
    greeting_pl=", będziesz następny?",
    text2_p_hu='Az elmúlt 7 nap a <strong>Celsius Sport</strong>-on hatalmas volt. A legélesebb fogadóink jól döntöttek és komoly nyereményeket vittek haza:<br><br><strong>💰 Str•••••X – €42,810<br>💰 Go•••••er – €31,200<br>💰 Pa•••••ng – €19,450</strong><br><br>Ők nem csak nézték - meglépték.<br>A vonalak élőben vannak a következő meccsekre, szóval válaszd ki a helyed és tedd meg a fogadásod.<br>A te neved lehet a következő ezen a listán.',
    text2_p_pl='Ostatnie 7 dni na <strong>Celsius Sport</strong> było wielkie. Nasi najlepsi typujący dobrze postawili i zgarnęli wielkie wypłaty:<br><br><strong>💰 Str•••••X – €42,810<br>💰 Go•••••er – €31,200<br>💰 Pa•••••ng – €19,450</strong><br><br>Nie tylko oglądali - postawili.<br>Kursy na kolejne mecze są na żywo, więc wybierz swoje miejsce i postaw zakład.<br>Twoje nazwisko może być następne na tej liście.',
    text3_p_hu=None,
    text3_p_pl=None,
    button_hu="NÉZD MEG A MAI ODDSOKAT",
    button_pl="SPRAWDŹ DZISIEJSZE KURSY",
)

# ════════════════════════════════════════════════════════════════
# EMAIL 4C — 160% + 80 Spins Wild West Gold, GUNSLINGER160, Casino
# ════════════════════════════════════════════════════════════════
T["Email 4C"] = dict(
    subject_hu="💥 160% + 80 Spin: Kapd el és érezd az adrenalint",
    subject_pl="💥 160% + 80 Spinów: Bierz i poczuj adrenalinę",
    preheader_hu="Kapd el a tökéletes pillanatot a következő nagy nyereményedhez",
    preheader_pl="Złap idealny moment na swoją następną wielką wygraną",
    default_hu="Játékos", default_pl="Gracz",
    greeting_en=", let's turn up the heat!",
    greeting_hu=", fokozzuk az adrenalint!",
    greeting_pl=", podkręcamy temperaturę!",
    text2_p_hu='Megvan az ösztönöd - most csapj le, amíg a pillanat tökéletes. Kapj meg egy <strong>160% bonus + 80 Free Spin</strong> juttatást a <strong>Wild West Gold by Pragmatic Play</strong> játékban és turbózd fel a következő meneted.',
    text2_p_pl='Masz instynkt - teraz uderz, gdy moment jest idealny. Zgarnij <strong>160% bonus + 80 Free Spinów</strong> na <strong>Wild West Gold by Pragmatic Play</strong> i doładuj następną sesję.',
    text3_p_hu='Írd be a <strong class="promocode">GUNSLINGER160</strong> promókódot a befizetésed előtt, és oldd fel a <strong>160% bonuszodat és 80 Free Spinnedet</strong>. Aztán ugorj egyenesen a <strong>Wild West Gold by Pragmatic Play</strong> játékba.<br><br>A tárcsák készen állnak a <strong>Celsius Casino</strong>-ban - indítasz egy nyerő sorozatot?',
    text3_p_pl='Wpisz kod promocyjny <strong class="promocode">GUNSLINGER160</strong> przed depozytem, żeby odblokować <strong>160% bonus i 80 Free Spinów</strong>. Potem wskakuj prosto do <strong>Wild West Gold by Pragmatic Play</strong>.<br><br>Bębny są gotowe w <strong>Celsius Casino</strong> - zaczynasz serię wygranych?',
    button_hu="FOKOZD A TEMPÓT",
    button_pl="PRZYSPIESZ TEMPO",
)

# ════════════════════════════════════════════════════════════════
# EMAIL 4S — 170% Boost, SURGE170, Sport
# ════════════════════════════════════════════════════════════════
T["Email 4S"] = dict(
    subject_hu="⚽ 170% Boost: A te meccsted, a te forgatókönyved",
    subject_pl="⚽ 170% Boost: Twój mecz, Twój scenariusz",
    preheader_hu="Vedd át az irányítást és írd a saját történeted",
    preheader_pl="Przejmij kontrolę i napisz swoją historię",
    default_hu="Edző", default_pl="Trenerze",
    greeting_en=", you call the shots!",
    greeting_hu=", te döntesz!",
    greeting_pl=", Ty decydujesz!",
    text2_p_hu='Minden meccsnek van egy forgatókönyve - és ma te írod. Hogy az első sípszótól az utolsó percig mögötted álljunk, a következő menetedet egy <strong>170% befizetési bonusszal</strong> töltjük fel.',
    text2_p_pl='Każdy mecz ma swój scenariusz - a dziś to Ty go piszesz. Żeby wspierać Cię od pierwszego gwizdka do ostatniej minuty, doładowujemy Twoją następną sesję <strong>170% bonusem od depozytu</strong>.',
    text3_p_hu='Írd be a <strong class="promocode">SURGE170</strong> promókódot a befizetésed előtt, és oldd fel a <strong>170% befizetési bonuszodat</strong>. Aztán menj a <strong>Celsius Sport</strong>-ra, nézd át a piacokat és építsd fel a szelvényed a saját stílusodban.<br><br>A tábla élőben van - és az előnyöd kész. Most írd meg az eredményt.',
    text3_p_pl='Wpisz kod promocyjny <strong class="promocode">SURGE170</strong> przed depozytem, żeby odblokować <strong>170% bonus od depozytu</strong>. Potem wejdź na <strong>Celsius Sport</strong>, przejrzyj rynki i skompletuj kupon po swojemu.<br><br>Tablica jest na żywo - a Twoja przewaga gotowa. Teraz napisz wynik.',
    button_hu="AKTIVÁLD A BONUSZOM",
    button_pl="AKTYWUJ MÓJ BONUS",
)

# ════════════════════════════════════════════════════════════════
# EMAIL 5C — 170% Bonus, BOOSTER170, Casino
# ════════════════════════════════════════════════════════════════
T["Email 5C"] = dict(
    subject_hu="🎰 170% Bonus: Azonnali erősítés aktiválva",
    subject_pl="🎰 170% Bonus: Natychmiastowe doładowanie aktywowane",
    preheader_hu="Gyorsabb utat kaptál a nagy nyereményhez",
    preheader_pl="Twoja droga do wielkiej wygranej właśnie przyspieszyła",
    default_hu="Játékos", default_pl="Gracz",
    greeting_en=", get ready for more!",
    greeting_hu=", készülj a többre!",
    greeting_pl=", szykuj się na więcej!",
    text2_p_hu='Amikor a játékok beindulnak, a sebesség nyer. Azonnal betöltünk egy <strong>170% bonuszt</strong> a következő befizetésedre - azért, hogy a meneted tovább tartson és gyorsabban haladj. Ne felejtsd el beírni a <strong class="promocode">BOOSTER170</strong> kódot a befizetésed előtt.',
    text2_p_pl='Gdy gry się rozkręcają, wygrywa szybkość. Natychmiast ładujemy <strong>170% bonus</strong> do Twojego następnego depozytu - żebyś grał dłużej i szybciej. Pamiętaj, żeby wpisać kod <strong class="promocode">BOOSTER170</strong> przed depozytem.',
    text3_p_hu='Töltsd fel a fiókodat és nézd, ahogy az egyenleged felszáll a <strong>Celsius Casino</strong>-ban. <strong>170%</strong>-kal többel tovább játszhatsz, keményebben nyomsz és vadászhatsz a nagy szorzókra.',
    text3_p_pl='Doładuj konto i patrz, jak Twoje saldo startuje w <strong>Celsius Casino</strong>. Z <strong>170%</strong> więcej możesz grać dłużej, grać agresywniej i polować na wielkie mnożniki.',
    button_hu="KEZDJ EL NYERNI",
    button_pl="ZACZNIJ WYGRYWAĆ",
)

# ════════════════════════════════════════════════════════════════
# EMAIL 5S — 20% NoRisk Bet, WINSAFE20, Sport
# ════════════════════════════════════════════════════════════════
T["Email 5S"] = dict(
    subject_hu="🚀 20% NoRisk Bet: Nyisd meg, aktiváld, nyerj",
    subject_pl="🚀 20% NoRisk Bet: Otwórz, aktywuj, wygraj",
    preheader_hu="Lépj be azonnal az akció közepébe - késlekedés nélkül",
    preheader_pl="Wejdź od razu w sam środek akcji - bez zwłoki",
    default_hu="Játékos", default_pl="Gracz",
    greeting_en=", no time to waste!",
    greeting_hu=", nincs vesztegetni való idő!",
    greeting_pl=", nie ma czasu do stracenia!",
    text2_p_hu='A legnagyobb pillanatok élőben vannak - és van egy gyorsabb módja, hogy előnnyel szállj be a <strong>Celsius Sport</strong>-on. Nincs várakozás, csak akció védelemmel a téted mögött.',
    text2_p_pl='Największe momenty trwają na żywo - a jest szybszy sposób, żeby wejść z przewagą na <strong>Celsius Sport</strong>. Bez opóźnień, tylko akcja z ochroną za Twoim zakładem.',
    text3_p_hu='A gyors utad: nézd meg az oddsokat, add hozzá a <strong class="promocode">WINSAFE20</strong> promókódot a befizetésed előtt, majd aktiváld a <strong>20% NoRisk Free Bet</strong>-edet. Ez <strong>20% NoRisk Free Bet</strong> védelem a tétedre - azért, hogy az első tippedtől az utolsó sípszóig magabiztos lehess.<br><br>Három lépés. Egy előny. Induljon a sorozatod.',
    text3_p_pl='Twoja szybka ścieżka: sprawdź kursy, wpisz kod promocyjny <strong class="promocode">WINSAFE20</strong> przed depozytem, a następnie aktywuj <strong>20% NoRisk Free Bet</strong>. To <strong>20% NoRisk Free Bet</strong> ochrona Twojej stawki - żebyś grał pewnie od pierwszego typu do ostatniego gwizdka.<br><br>Trzy kroki. Jedna przewaga. Ruszamy z serią.',
    button_hu="AKTIVÁLD A NORISK TÉTEM",
    button_pl="AKTYWUJ MÓJ NORISK ZAKŁAD",
)

# ════════════════════════════════════════════════════════════════
# EMAIL 6C — WINNER Casino, no promo, text_3=team sig (skip)
# ════════════════════════════════════════════════════════════════
T["Email 6C"] = dict(
    subject_hu="🌟 Csatlakozz az elithez: A heti dicsőségfal",
    subject_pl="🌟 Dołącz do elity: Hala sławy tego tygodnia",
    preheader_hu="Nézd meg, kik uralták a nyerőgépeket és foglald el a helyed a csúcson",
    preheader_pl="Zobacz, kto zdominował automaty i zajmij swoje miejsce na szczycie",
    default_hu="Játékos", default_pl="Gracz",
    greeting_en=", it's your time to shine!",
    greeting_hu=", itt az idő, hogy ragyogj!",
    greeting_pl=", czas zabłysnąć!",
    text2_p_hu='A lendület hihetetlen - és a legnagyobb nyeremények most születnek a <strong>Celsius Casino</strong>-ban. Íme a legfrissebb bajnokok:<br><br><strong>🏆 Ja••••g – €61,200<br>🏆 Sp••••r – €42,800<br>🏆 Eli••••er – €24,100</strong><br><br>A gépek forrók és a lapok osztva - a következő címlap a tiéd lehet.<br>Lépj be, élvezd az izgalmat és játssz a <strong>Celsius Casino</strong>-ban.',
    text2_p_pl='Rozpęd jest niesamowity - a największe wygrane dzieją się właśnie teraz w <strong>Celsius Casino</strong>. Oto najnowsi mistrzowie:<br><br><strong>🏆 Ja••••g – €61,200<br>🏆 Sp••••r – €42,800<br>🏆 Eli••••er – €24,100</strong><br><br>Automaty są gorące, a karty rozdane - następny nagłówek może być Twój.<br>Wejdź, poczuj emocje i graj w <strong>Celsius Casino</strong>.',
    text3_p_hu=None,
    text3_p_pl=None,
    button_hu="KEZDD EL A KALANDOD",
    button_pl="ZACZNIJ SWOJĄ DROGĘ",
)

# ════════════════════════════════════════════════════════════════
# EMAIL 6S — 170% Boost, BOOSTER170, Sport
# ════════════════════════════════════════════════════════════════
T["Email 6S"] = dict(
    subject_hu="⚡ 170% Boost: Engedd szabadjára az erőt",
    subject_pl="⚡ 170% Boost: Uwolnij pełną moc",
    preheader_hu="Tüzeld fel a nyerő sorozatod extra tűzerővel",
    preheader_pl="Napędź swoją serię wygranych dodatkową mocą",
    default_hu="Bajnok", default_pl="Mistrzu",
    greeting_en=", step into the spotlight!",
    greeting_hu=", lépj a rivaldafénybe!",
    greeting_pl=", wejdź na scenę!",
    text2_p_hu='Készen állsz hogy fokozd az intenzitást? A hét legnagyobb meccseihez <strong>170% befizetési bonus</strong> jár, hogy extra erővel támogasd minden tipped.',
    text2_p_pl='Gotowy podkręcić intensywność? Największe mecze tego tygodnia idą w parze ze <strong>170% bonusem od depozytu</strong>, żeby napędzić każdy Twój typ.',
    text3_p_hu='A <strong>170% befizetési bonuszod</strong> aktiválásához írd be a <strong class="promocode">BOOSTER170</strong> promókódot a feltöltés előtt - a boosterod azonnal betöltődik.<br><br>Akár parlay-t építesz, akár éles szingókat zárolsz, az extra erő több teret ad a stratégiádnak a <strong>Celsius Sport</strong>-on. Vedd át az irányítást és engedd, hogy az előnyöd szárnyaljon <strong>170%</strong>-kal.',
    text3_p_pl='Żeby aktywować <strong>170% bonus od depozytu</strong>, wpisz kod promocyjny <strong class="promocode">BOOSTER170</strong> przed doładowaniem - Twój boost ładuje się natychmiast.<br><br>Czy budujesz akumulatory, czy stawiasz na ostrych singlach, dodatkowa moc daje Ci więcej miejsca na strategię na <strong>Celsius Sport</strong>. Przejmij kontrolę i pozwól swojej przewadze rosnąć z <strong>170%</strong>.',
    button_hu="AKTIVÁLD A BONUSZOM",
    button_pl="AKTYWUJ MÓJ BONUS",
)

# ════════════════════════════════════════════════════════════════
# EMAIL 7C — 160% + 80 FS Wild West Gold, GUNSLINGER160, Casino
# ════════════════════════════════════════════════════════════════
T["Email 7C"] = dict(
    subject_hu="⚡ 160% + 80 Free Spin: Aktiváld és pörgesd",
    subject_pl="⚡ 160% + 80 Free Spinów: Aktywuj i kręć",
    preheader_hu="Lépj egyenesen a nyerő részhez azonnali jutalmakkal",
    preheader_pl="Przejdź od razu do wygrywania z natychmiastowymi nagrodami",
    default_hu="Játékos", default_pl="Gracz",
    greeting_en=", why wait for the fun?",
    greeting_hu=", minek várni a szórakozásra?",
    greeting_pl=", po co czekać na zabawę?",
    text2_p_hu='Azonnalira csináltuk: aktiválsz, pörgetsz, nyereményekre vadászol. A következő befizetésed a <strong>Celsius Casino</strong>-ban feloldja a <strong>160% bonus + 80 Free Spin</strong> juttatást a <strong>Wild West Gold by Pragmatic Play</strong> játékban.',
    text2_p_pl='Zrobiliśmy to natychmiast: aktywujesz, kręcisz, gonisz wygrane. Twój następny depozyt w <strong>Celsius Casino</strong> odblokowuje <strong>160% bonus + 80 Free Spinów</strong> na <strong>Wild West Gold by Pragmatic Play</strong>.',
    text3_p_hu='Csak add hozzá a <strong class="promocode">GUNSLINGER160</strong> promókódot a feltöltés előtt - nincs várakozás, nincs extra lépés. Aztán lépj be a <strong>Wild West Gold by Pragmatic Play</strong> játékba és használd a <strong>80 Free Spinned</strong>, hogy elkapd a következő nagy szorzót.',
    text3_p_pl='Po prostu wpisz kod promocyjny <strong class="promocode">GUNSLINGER160</strong> przed doładowaniem - bez opóźnień, bez dodatkowych kroków. Potem wskakuj do <strong>Wild West Gold by Pragmatic Play</strong> i użyj swoich <strong>80 Free Spinów</strong>, żeby upolować następny wielki mnożnik.',
    button_hu="AKTIVÁLD A BONUSZOM",
    button_pl="AKTYWUJ MÓJ BONUS",
)

# ════════════════════════════════════════════════════════════════
# EMAIL 7S — 20% NoRisk Free Bet, WINSAFE20, Sport
# ════════════════════════════════════════════════════════════════
T["Email 7S"] = dict(
    subject_hu="⚡ 20% NoRisk Free Bet: A te előnyöd",
    subject_pl="⚡ 20% NoRisk Free Bet: Twoja przewaga",
    preheader_hu="Kövesd a nyerő formulát a promótól a meccsig",
    preheader_pl="Podążaj za zwycięską formułą od promocji do meczu",
    default_hu="Játékos", default_pl="Gracz",
    greeting_en=", get the edge you need!",
    greeting_hu=", szerezd meg a szükséges előnyt!",
    greeting_pl=", zdobądź przewagę, jakiej potrzebujesz!",
    text2_p_hu='Miért bíznád a véletlenre, amikor előnnyel is játszhatsz? Aktiváld a promódat, tedd meg a fogadásod és élvezd a meccset védelemmel a téted mögött.',
    text2_p_pl='Po co zostawiać to przypadkowi, skoro możesz grać z przewagą? Aktywuj promocję, postaw zakład i ciesz się meczem z ochroną za Twoim zakładem.',
    text3_p_hu='Kezdésként írd be a <strong class="promocode">WINSAFE20</strong> promókódot, majd teljesítsd a befizetést és oldd fel a <strong>20% NoRisk Free Bet</strong>-edet. Aztán menj a <strong>Celsius Sport</strong>-ra és válaszd ki a helyed - a derbi, a taktikai csata vagy a muszáj-meccset.<br><br>A <strong>20% NoRisk Free Bet</strong> védelemmel bízhatsz az ösztöneidben és kézben tarthatod a dolgokat a kezdőrúgástól a záró sípszóig.',
    text3_p_pl='Zacznij od wpisania kodu promocyjnego <strong class="promocode">WINSAFE20</strong>, następnie dokonaj wpłaty i odblokuj <strong>20% NoRisk Free Bet</strong>. Potem wejdź na <strong>Celsius Sport</strong> i wybierz swoje miejsce - derby, taktyczne starcie lub mecz, którego nie można przegapić.<br><br>Z ochroną <strong>20% NoRisk Free Bet</strong> możesz zaufać instynktowi i mieć kontrolę od pierwszego gwizdka do ostatniego.',
    button_hu="SZEREZD MEG AZ ELŐNYÖD",
    button_pl="ZDOBĄDŹ SWOJĄ PRZEWAGĘ",
)

# ════════════════════════════════════════════════════════════════
# EMAIL 8C — 180% + 80 FS Wanted Dead or Wild, OUTLAW180, Casino
# ════════════════════════════════════════════════════════════════
T["Email 8C"] = dict(
    subject_hu="🚀 180% Bonus + 80 Free Spin: Emeld a szintet",
    subject_pl="🚀 180% Bonus + 80 Free Spinów: Podnieś stawkę",
    preheader_hu="Nézd meg, hogyan turbózhatod fel a következő befizetésed pár kattintással",
    preheader_pl="Zobacz, jak doładować następny depozyt w kilka kliknięć",
    default_hu="Barátom", default_pl="Przyjacielu",
    greeting_en=", it's time to level up!",
    greeting_hu=", itt az idő szintet lépni!",
    greeting_pl=", czas wejść na wyższy poziom!",
    text2_p_hu='Ne csak csatlakozz a játékhoz - vedd át az irányítást. A következő befizetésed komoly frissítést kap: <strong>180% erősítés + 80 Free Spin</strong> a <strong>Wanted Dead or a Wild by Hacksaw Gaming</strong> játékban, ami villámgyorsan indítja a meneted.',
    text2_p_pl='Nie dołączaj po prostu do gry - przejmij kontrolę. Twój następny depozyt dostaje poważne ulepszenie: <strong>180% doładowanie + 80 Free Spinów</strong> na <strong>Wanted Dead or a Wild by Hacksaw Gaming</strong>, żeby wystartować błyskawicznie.',
    text3_p_hu='Kezdésként írd be a <strong class="promocode">OUTLAW180</strong> promókódot, majd teljesítsd a befizetést és ugorj be a <strong>Wanted Dead or a Wild by Hacksaw Gaming</strong> játékba a <strong>Celsius Casino</strong>-ban. A <strong>180% boostered és 80 Free Spinned</strong> az első pörgéstől kész.',
    text3_p_pl='Zacznij od wpisania kodu promocyjnego <strong class="promocode">OUTLAW180</strong>, następnie dokonaj wpłaty i wskakuj do <strong>Wanted Dead or a Wild by Hacksaw Gaming</strong> w <strong>Celsius Casino</strong>. Twoje <strong>180% doładowanie i 80 Free Spinów</strong> są gotowe od pierwszego obrotu.',
    button_hu="KAPD MEG AZ ERŐSÍTÉST",
    button_pl="ODBIERZ DOŁADOWANIE",
)

# ════════════════════════════════════════════════════════════════
# EMAIL 8S — WINNER Sport, no promo, text_3=team sig (skip)
# ════════════════════════════════════════════════════════════════
T["Email 8S"] = dict(
    subject_hu="🏆 Nagyot nyertek a sporton - most rajtad a sor",
    subject_pl="🏆 Wygrali wielkie pieniądze na sporcie - teraz Twoja kolej",
    preheader_hu="Nézd meg a hét top kifizetéseit és válaszd ki a nyerő meccsedet",
    preheader_pl="Sprawdź topowe wypłaty tygodnia i wybierz swój zwycięski mecz",
    default_hu="Bajnok", default_pl="Mistrzu",
    greeting_en=", the leaderboard is waiting!",
    greeting_hu=", a ranglista vár!",
    greeting_pl=", tabela czeka!",
    text2_p_hu='A múlt héten ezek a játékosok bíztak a számokban, elkapták a megfelelő pillanatot és nagyot kaszáltak:<br><br><strong>💰 G••••er88 – €45,600<br>💰 O•••••ero – €32,150<br>💰 Be••••rd – €18,700</strong><br><br>A tábla frissült és a következő meccsek élőben vannak a <strong>Celsius Sport</strong>-on. Az oddsok fent vannak, a piacok mozognak, és ez a te ablakod.<br><br>Válaszd ki a meccsedet, bízz az ösztöneidben és lépj - a te neved legyen a következő a győztesek listáján.',
    text2_p_pl='W zeszłym tygodniu ci gracze zaufali liczbom, trafili w odpowiedni moment i zgarnęli wielkie wygrane:<br><br><strong>💰 G••••er88 – €45,600<br>💰 O•••••ero – €32,150<br>💰 Be••••rd – €18,700</strong><br><br>Tablica jest odświeżona, a kolejne mecze są na żywo na <strong>Celsius Sport</strong>. Kursy są aktualne, rynki się poruszają, a to jest Twoje okno.<br><br>Wybierz mecz, zaufaj instynktowi i postaw - Twoje nazwisko powinno być następne na liście zwycięzców.',
    text3_p_hu=None,
    text3_p_pl=None,
    button_hu="VÁLASSZ MECCSET ÉS FOGADJ",
    button_pl="WYBIERZ MECZ I POSTAW",
)

# ════════════════════════════════════════════════════════════════
# EMAIL 9C — 140% + 100 FS Big Bamboo, GIANTPANDA100, Casino
# ════════════════════════════════════════════════════════════════
T["Email 9C"] = dict(
    subject_hu="💎 140% Bonus + 100 Free Spin: Minek vársz?",
    subject_pl="💎 140% Bonus + 100 Free Spinów: Po co czekać?",
    preheader_hu="Vedd át a vezetést és biztosítsd az extra esélyeidet a nagy nyereményhez",
    preheader_pl="Przejmij prowadzenie i zapewnij sobie dodatkowe szanse na wielką wygraną",
    default_hu="Barátom", default_pl="Przyjacielu",
    greeting_en=", make today legendary.",
    greeting_hu=", tedd legendássá a mai napot.",
    greeting_pl=", spraw, żeby ten dzień był legendą.",
    text2_p_hu='A "tökéletes pillanat" nem érkezik meg - te teremted meg. Ma lépj nagyobbat az első pörgéstől egy <strong>140% bonus + 100 Free Spin</strong> juttatással a <strong>Big Bamboo by Push Gaming</strong> játékban. Csak add hozzá a <strong class="promocode">GIANTPANDA100</strong> kódot, majd teljesítsd a befizetést a feloldáshoz.',
    text2_p_pl='\"Idealny moment\" nie przychodzi sam - to Ty go tworzysz. Dziś zacznij mocniej od pierwszego obrotu ze <strong>140% bonusem + 100 Free Spinami</strong> na <strong>Big Bamboo by Push Gaming</strong>. Po prostu wpisz kod <strong class="promocode">GIANTPANDA100</strong>, a następnie dokonaj wpłaty, żeby odblokować.',
    text3_p_hu='Lépj be a <strong>Celsius Casino</strong>-ba megnövelt egyenleggel és <strong>100 Free Spin</strong> készen áll az indulásra. Játssz tovább, nyomj mélyebbre és vadássz a jackpotra valódi lendülettel.',
    text3_p_pl='Wejdź do <strong>Celsius Casino</strong> z podbitym saldem i <strong>100 Free Spinami</strong> gotowymi do akcji. Graj dłużej, idź głębiej i poluj na jackpota z prawdziwym rozpędem.',
    button_hu="KAPD MEG A BOOSTERT",
    button_pl="ODBIERZ DOŁADOWANIE",
)

# ════════════════════════════════════════════════════════════════
# EMAIL 9S — 30% NoRisk Bet, ONLYSAFE30, Sport
# ════════════════════════════════════════════════════════════════
T["Email 9S"] = dict(
    subject_hu="🎾 30% NoRisk Bet: Okos nézés",
    subject_pl="🎾 30% NoRisk Bet: Mądre oglądanie",
    preheader_hu="Kombináld a sport iránti szenvedélyed kockázatmentes előnnyel",
    preheader_pl="Połącz pasję do sportu z przewagą bez ryzyka",
    default_hu="Játékos", default_pl="Gracz",
    greeting_en=", it's time to play.",
    greeting_hu=", itt az idő játszani.",
    greeting_pl=", czas na grę.",
    text2_p_hu='A legjobb módja a kedvenc sportod nézésének? Bőrrel a játékban - és védelemmel a téteden. Ma <strong>30% NoRisk Free Bet</strong> védelmet kapsz a <strong class="promocode">ONLYSAFE30</strong> kóddal.',
    text2_p_pl='Najlepszy sposób na oglądanie ulubionego sportu? Ze stawką w grze - i ochroną na Twoim zakładzie. Dziś dostajesz ochronę <strong>30% NoRisk Free Bet</strong> z kodem <strong class="promocode">ONLYSAFE30</strong>.',
    text3_p_hu='Aktiváld a promót, válaszd ki a piacodat és játssz magabiztosan: add hozzá a <strong class="promocode">ONLYSAFE30</strong> kódot először, majd teljesítsd a befizetést és oldd fel a <strong>30% NoRisk Free Bet</strong> védelmedet a mai akcióhoz.<br><br>A <strong>Celsius Sport</strong>-on mi adjuk a vonalakat - te hozod a stratégiát. Tedd meg a fogadásod és tedd különlegessé ezt a meccset.',
    text3_p_pl='Aktywuj promocję, wybierz rynek i graj z pewnością: wpisz kod <strong class="promocode">ONLYSAFE30</strong>, a następnie dokonaj wpłaty i odblokuj ochronę <strong>30% NoRisk Free Bet</strong> na dzisiejszą akcję.<br><br>Na <strong>Celsius Sport</strong> my dajemy kursy - Ty wnosisz strategię. Postaw zakład i spraw, żeby ten mecz miał znaczenie.',
    button_hu="AKTIVÁLD A NORISK TÉTEM",
    button_pl="AKTYWUJ MÓJ NORISK ZAKŁAD",
)

# ════════════════════════════════════════════════════════════════
# EMAIL 10C — 200 FS Gems Bonanza, GEMHUNT200, Casino
# ════════════════════════════════════════════════════════════════
T["Email 10C"] = dict(
    subject_hu="⚡ 200 Free Spin: Készen állsz pörgetni?",
    subject_pl="⚡ 200 Free Spinów: Gotowy kręcić?",
    preheader_hu="Kapd meg az azonnali hozzáférést a prémium nyerőgépes jutalmadhoz",
    preheader_pl="Uzyskaj natychmiastowy dostęp do premiumowej nagrody na automacie",
    default_hu="Barátom", default_pl="Przyjacielu",
    greeting_en=", your boost is here.",
    greeting_hu=", megérkezett az erősítésed.",
    greeting_pl=", Twoje doładowanie jest tutaj.",
    text2_p_hu='Azért vagy itt, mert vonzza az adrenalin - szóval gyorsra csináltuk. A <strong>200 Free Spinned</strong> a <strong>Gems Bonanza by Pragmatic Play</strong> játékban kész a következő befizetéseddel. Csak írd be a <strong class="promocode">GEMHUNT200</strong> promókódot a befizetés előtt és máris benne vagy.',
    text2_p_pl='Jesteś tu dla emocji - więc zrobiliśmy to szybko. Twoje <strong>200 Free Spinów</strong> na <strong>Gems Bonanza by Pragmatic Play</strong> czekają z następnym depozytem. Po prostu wpisz kod promocyjny <strong class="promocode">GEMHUNT200</strong> przed wpłatą i od razu wskakujesz do gry.',
    text3_p_hu='Nincs keresés, nincs macera - csak akció a <strong>Celsius Casino</strong>-ban. Töltsd fel, engedd, hogy hulljanak a drágakövek, és vadássz a nagy pillanatra.',
    text3_p_pl='Bez szukania, bez kłopotów - tylko akcja w <strong>Celsius Casino</strong>. Doładuj, pozwól klejnotom spadać i poluj na ten wielki moment.',
    button_hu="KEZDJ EL PÖRGETNI",
    button_pl="ZACZNIJ KRĘCIĆ",
)

# ════════════════════════════════════════════════════════════════
# EMAIL 10S — 30% NoRisk Free Bet, ONLYSAFE30, Sport
# ════════════════════════════════════════════════════════════════
T["Email 10S"] = dict(
    subject_hu="💥 30% NoRisk Free Bet: Kapd el és urald a vonalat",
    subject_pl="💥 30% NoRisk Free Bet: Bierz i dominuj na kursach",
    preheader_hu="Okosabb módja a kedvenc sportjaidra fogadni - itt van",
    preheader_pl="Mądrzejszy sposób na obstawianie ulubionego sportu - właśnie tutaj",
    default_hu="Bajnok", default_pl="Mistrzu",
    greeting_en=", ready for the kick-off?",
    greeting_hu=", készen állsz a kezdőrúgásra?",
    greeting_pl=", gotowy na pierwszy gwizdek?",
    text2_p_hu='Legyen a következő fogadásod az okos - beépített védelemmel. A <strong>30% NoRisk Free Bet</strong>-ed most aktív, több szabadságot adva, hogy kövesd a megérzésedet.',
    text2_p_pl='Niech Twój następny zakład będzie tym mądrym - z wbudowaną ochroną. Twój <strong>30% NoRisk Free Bet</strong> jest teraz aktywny, dając Ci więcej swobody w podążaniu za instynktem.',
    text3_p_hu='A zároláshoz írd be a <strong class="promocode">ONLYSAFE30</strong> promókódot a befizetésed előtt, és aktiváld a <strong>30% NoRisk Free Bet</strong>-edet.<br><br>Menj a <strong>Celsius Sport</strong>-ra, nézd át a top meccseket, válaszd ki a győzteseidet és játssz védett téttel. Gyors, egyszerű és kész, amikor te is az vagy.',
    text3_p_pl='Żeby to zablokować, wpisz kod promocyjny <strong class="promocode">ONLYSAFE30</strong> przed depozytem i aktywuj <strong>30% NoRisk Free Bet</strong>.<br><br>Wejdź na <strong>Celsius Sport</strong>, przejrzyj topowe mecze, wybierz zwycięzców i graj z chronioną stawką. Szybko, prosto i gotowe, gdy tylko Ty jesteś.',
    button_hu="AKTIVÁLD ÉS JÁTSSZ",
    button_pl="AKTYWUJ I GRAJ",
)


# ──────────────────────────────────────────────────────────────
# ENGINE: Parse file, apply translations, write back
# ──────────────────────────────────────────────────────────────

def parse_blocks(text):
    """Parse the file into a list of (block_dict, raw_lines) tuples."""
    blocks = []
    current_lines = []
    current_dict = {}
    
    for line in text.split('\n'):
        raw = line.rstrip('\r')
        if raw.startswith('name: '):
            if current_dict:
                blocks.append((dict(current_dict), list(current_lines)))
            current_lines = [raw]
            current_dict = {'name': raw[6:]}
        elif ': ' in raw and current_dict:
            key, val = raw.split(': ', 1)
            current_dict[key] = val
            current_lines.append(raw)
        elif raw == '' and current_dict:
            current_lines.append(raw)
        else:
            current_lines.append(raw)
    
    if current_dict:
        blocks.append((dict(current_dict), list(current_lines)))
    
    return blocks

def apply_translations(blocks):
    """Apply translations to hu-HU and pl-PL blocks."""
    changes = 0
    
    for block_dict, block_lines in blocks:
        name = block_dict.get('name', '')
        locale = block_dict.get('locale', '')
        
        if name not in T:
            continue
        if locale not in ('hu-HU', 'pl-PL'):
            continue
        
        tr = T[name]
        lang = 'hu' if locale == 'hu-HU' else 'pl'
        
        for i, line in enumerate(block_lines):
            if not ': ' in line:
                continue
            key, val = line.split(': ', 1)
            new_val = None
            
            # --- subject ---
            if key == 'subject':
                new_val = tr[f'subject_{lang}']
            
            # --- preheader ---
            elif key == 'preheader':
                new_val = tr[f'preheader_{lang}']
            
            # --- button_text_1 ---
            elif key == 'button_text_1':
                new_val = tr[f'button_{lang}']
            
            # --- text_1: replace default and greeting ---
            elif key == 'text_1':
                # Replace default name
                m = re.search(r'default:"([^"]*)"', val)
                if m:
                    val = val.replace(f'default:"{m.group(1)}"', f'default:"{tr[f"default_{lang}"]}"')
                # Replace greeting text (after capitalize }}, ... before </strong>)
                greeting_en = tr.get('greeting_en', '')
                greeting_new = tr.get(f'greeting_{lang}', '')
                if greeting_en and greeting_new and greeting_en in val:
                    val = val.replace(greeting_en, greeting_new)
                new_val = val
            
            # --- text_2: replace p-content ---
            elif key == 'text_2':
                p_content_new = tr.get(f'text2_p_{lang}')
                if p_content_new:
                    # Extract current p-content and replace
                    m = re.search(r'(<p[^>]*>)(.*)(</p></td>)', val, re.DOTALL)
                    if m:
                        new_val = m.group(1) + p_content_new + m.group(3)
                    else:
                        print(f"WARNING: Could not find p-content in text_2 for {name} {locale}")
            
            # --- text_3: replace p-content (only for promo emails) ---
            elif key == 'text_3':
                p_content_new = tr.get(f'text3_p_{lang}')
                if p_content_new is not None:
                    m = re.search(r'(<p[^>]*>)(.*)(</p></td>)', val, re.DOTALL)
                    if m:
                        new_val = m.group(1) + p_content_new + m.group(3)
                    else:
                        print(f"WARNING: Could not find p-content in text_3 for {name} {locale}")
            
            if new_val is not None and new_val != line.split(': ', 1)[1]:
                block_lines[i] = f'{key}: {new_val}'
                changes += 1
    
    return changes

def reconstruct(blocks):
    """Reconstruct the file from blocks."""
    lines = []
    for i, (_, block_lines) in enumerate(blocks):
        lines.extend(block_lines)
        if i < len(blocks) - 1:
            lines.append('')  # separator between blocks
    return '\n'.join(lines)

# ──────────────────────────────────────────────────────────────
# MAIN
# ──────────────────────────────────────────────────────────────

print(f"Reading: {filepath}")
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

blocks = parse_blocks(content)
print(f"Parsed {len(blocks)} blocks")

# Count how many blocks match
matching = sum(1 for b, _ in blocks if b.get('name') in T and b.get('locale') in ('hu-HU', 'pl-PL'))
print(f"Blocks to translate: {matching}")

changes = apply_translations(blocks)
print(f"Fields changed: {changes}")

if changes > 0:
    result = reconstruct(blocks)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(result)
    print(f"File written successfully!")
else:
    print("No changes made.")
