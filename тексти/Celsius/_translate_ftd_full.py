# -*- coding: utf-8 -*-
import re, os, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

filepath = r'c:\Projects\REPORTS\тексти\Celsius\FTD Retention Flow - Table data.txt'

# Greeting replacements (inside <strong> tag of text_1)
GREETING_EN = ' Hello, {{customer.first_name | default:"friend"}}\U0001f44b '
GREETING_HU = ' Szia, {{customer.first_name | default:"Barátom"}}\U0001f44b '
GREETING_PL = ' Cześć, {{customer.first_name | default:"Przyjacielu"}}\U0001f44b '

# Translations: subject, preheader, body (inner <p> content), button_text_1
T = {}

# ============ Email 1C ============
T['Email 1C'] = {
  'hu-HU': {
    'subject': '🐍 A homok mozog - oldd fel a 100% + 50 Ingyenes Pörgetést',
    'preheader': 'Következő befizetési bónuszod a Hand of Anubis játékhoz kész',
    'body': 'Beléptél a játékba - most itt az idő mélyebbre menni.<br><br>Használd az <strong class="promocode">ANUBIS10050</strong> kódot a következő befizetésednél, hogy feloldd a <strong>100% Bónuszt + 50 Ingyenes Pörgetést</strong> a <strong>Hand of Anubis</strong> <strong>by Hacksaw Gaming</strong> játékban.<br><br>Ősi erő, modern izgalom - készen állsz a pörgetésre?',
    'button_text_1': 'BÓNUSZOM IGÉNYLÉSE',
  },
  'pl-PL': {
    'subject': '🐍 Piaski się przesuwają - odblokuj 100% + 50 Darmowych Spinów',
    'preheader': 'Bonus od następnej wpłaty na Hand of Anubis czeka',
    'body': 'Wszedłeś do gry - czas zagłębić się bardziej.<br><br>Użyj kodu <strong class="promocode">ANUBIS10050</strong> przy następnej wpłacie, żeby odblokować <strong>100% Bonus + 50 Darmowych Spinów</strong> w grze <strong>Hand of Anubis</strong> <strong>by Hacksaw Gaming</strong>.<br><br>Starożytna moc spotyka nowoczesny dreszcz - gotowy na obroty?',
    'button_text_1': 'ODBIERZ MÓJ BONUS',
  }
}

# ============ Email 1M ============
T['Email 1M'] = {
  'hu-HU': {
    'subject': '🎮 A második lépésed? Casino Bónusz vagy Kockázatmentes Sportfogadás',
    'preheader': 'Válaszd ki, hogyan folytatod - pörgetés, fogadás vagy mindkettő',
    'body': 'Megcsináltad az első befizetésedet - tartsuk fenn a lendületet.<br>Íme, mi vár a következő lépésednél:<br><br><strong>100% Bónusz</strong> + <strong>50 Ingyenes Pörgetés</strong> a <strong>Hand of Anubis by Hacksaw Gaming</strong> játékban casino rajongóknak - használd az <strong class="promocode">ANUBIS10050</strong> kódot<br><strong></strong><strong>20% Kockázatmentes Fogadás</strong> a következő sportfogadásodhoz - használd a <strong class="promocode">WINBACKNRF20</strong> kódot<br><br><strong></strong>Dupláz a casinóban vagy okosan játszol a sportfogadásban - bármelyiket is választod, fedezve vagy.',
    'button_text_1': 'JÁTÉK FOLYTATÁSA',
  },
  'pl-PL': {
    'subject': '🎮 Twój drugi krok? Bonus Casino lub Zakład Sportowy Bez Ryzyka',
    'preheader': 'Wybierz jak chcesz kontynuować - spiny, zakłady lub jedno i drugie',
    'body': 'Dokonałeś pierwszej wpłaty - utrzymajmy rozpęd.<br>Oto co czeka na Twój następny ruch:<br><br><strong>100% Bonus</strong> + <strong>50 Darmowych Spinów</strong> w grze <strong>Hand of Anubis by Hacksaw Gaming</strong> dla miłośników casino - użyj kodu <strong class="promocode">ANUBIS10050</strong><br><strong></strong><strong>20% Zakład Bez Ryzyka</strong> na Twój następny zakład sportowy - użyj kodu <strong class="promocode">WINBACKNRF20</strong><br><br><strong></strong>Podwajaj w casino lub graj mądrze w zakładach sportowych - tak czy inaczej, masz wsparcie.',
    'button_text_1': 'KONTYNUUJ GRĘ',
  }
}

# ============ Email 1S ============
T['Email 1S'] = {
  'hu-HU': {
    'subject': '🏆 20% Kockázatmentes Fogadás aktiválva számodra',
    'preheader': 'Kapd vissza a fogadásod 20%-át, ha nem jön be - csak az első befizetés után',
    'body': 'Megcsináltad az első befizetésedet - ideje okosan fogadni.<br>Használd a <strong class="promocode">WINBACKNRF20</strong> kódot és élvezd a <strong>20% Kockázatmentes Fogadást</strong> a következő téteden.<br><br>Ha nem a te javadra dől el, visszakapod a <strong>20%</strong>-ot az egyenlegedre.&nbsp;<br>Ilyen egyszerű.',
    'button_text_1': 'FOGADÁSOM ELHELYEZÉSE',
  },
  'pl-PL': {
    'subject': '🏆 20% Zakład Bez Ryzyka aktywny dla Ciebie',
    'preheader': 'Odzyskaj 20% zakładu, jeśli nie pójdzie po Twojej myśli - tylko po pierwszej wpłacie',
    'body': 'Dokonałeś pierwszej wpłaty - czas obstawiać mądrze.<br>Użyj kodu <strong class="promocode">WINBACKNRF20</strong> i ciesz się <strong>20% Zakładem Bez Ryzyka</strong> przy następnym zakładzie.<br><br>Jeśli wynik nie będzie po Twojej stronie, zwrócimy <strong>20%</strong> na Twoje saldo.&nbsp;<br>Tak po prostu.',
    'button_text_1': 'POSTAW MÓJ ZAKŁAD',
  }
}

# ============ Email 2C ============
T['Email 2C'] = {
  'hu-HU': {
    'subject': '🎯 A következő pörgetésed lehet a nagy nyerő',
    'preheader': 'Még egy befizetés az esélyeidet is megfordíthatja',
    'body': 'A tárcsák nem várnak - és a nyeremények sem.<br>Játékosok ezrei pörgetnek minden órában.&nbsp;<br><br>Néhányan izgalommal távoznak\u2026 mások jackpottal.<br>A következő befizetésed elég ahhoz, hogy újra a játékban legyél.<br>Semmi nyomás - csak tiszta adrenalin.',
    'button_text_1': 'ÚJRA JÁTSZOM',
  },
  'pl-PL': {
    'subject': '🎯 Twój następny spin może być tym wielkim',
    'preheader': 'Jeszcze jedna wpłata może obrócić szanse na Twoją korzyść',
    'body': 'Bębny nie czekają - wygrane też nie.<br>Tysiące graczy kręci co godzinę.&nbsp;<br><br>Niektórzy odchodzą z dreszczykiem\u2026 inni z jackpotem.<br>Następna wpłata wystarczy, żebyś wrócił do gry.<br>Bez presji - czysty adrenalin.',
    'button_text_1': 'GRAM PONOWNIE',
  }
}

# ============ Email 2M ============
T['Email 2M'] = {
  'hu-HU': {
    'subject': '🎯 100% + 60 Ingyenes Pörgetés vagy 20% Kockázatmentes Fogadás - Te választasz',
    'preheader': 'Casino vagy Sport? Bónusz + Ingyenes Pörgetés vagy biztonságos Kockázatmentes Fogadás',
    'body': 'Most, hogy az első befizetésed megvan - vigyük tovább.<br>Válaszd ki, hogyan erősíted a játékodat:<br><br>Kód <strong class="promocode">DOG10060</strong> -<strong> 100% Bónusz</strong> + <strong>60 Ingyenes Pörgetés </strong>a <strong>The Dog House Megaways by Pragmatic Play</strong> játékban, ha a tárcsákat pörgeted<br>Kód <strong class="promocode">WINBACKNRF20</strong> -<strong> 20% Kockázatmentes Fogadás</strong>, ha a sportfogadásban bízol<br><br>Bármelyik utat is választod, a következő nyereményed itt kezdődik.',
    'button_text_1': 'BÓNUSZOM IGÉNYLÉSE',
  },
  'pl-PL': {
    'subject': '🎯 100% + 60 Darmowych Spinów lub 20% Zakład Bez Ryzyka - Twój wybór',
    'preheader': 'Casino czy Sport? Bonus + Darmowe Spiny lub graj bezpiecznie z Zakładem Bez Ryzyka',
    'body': 'Skoro pierwsza wpłata jest za Tobą - idźmy dalej.<br>Wybierz, jak chcesz wzmocnić swoją grę:<br><br>Kod <strong class="promocode">DOG10060</strong> -<strong> 100% Bonus</strong> + <strong>60 Darmowych Spinów </strong>w grze <strong>The Dog House Megaways by Pragmatic Play</strong>, jeśli kręcisz bębnami<br>Kod <strong class="promocode">WINBACKNRF20</strong> -<strong> 20% Zakład Bez Ryzyka</strong>, jeśli stawiasz na sport<br><br>Którąkolwiek drogę wybierzesz, Twoja następna wygrana zaczyna się tutaj.',
    'button_text_1': 'ODBIERZ MÓJ BONUS',
  }
}

# ============ Email 2S ============
T['Email 2S'] = {
  'hu-HU': {
    'subject': '🎯 Nem jött be a fogadás? Kapj vissza 20%-ot',
    'preheader': 'A 20% Kockázatmentes Fogadásod él - játssz tovább magabiztosan',
    'body': 'A sportban nem minden fogadás jön be - de mi a hátad mögött állunk.<br>Tedd meg a következő téted a <strong class="promocode">WINBACKNRF20</strong> kóddal és kapj <strong>20% Kockázatmentes Fogadást</strong>.<br><br>Ha nem a javadra dől el, visszakapod a <strong>20%</strong>-ot a számládra.&nbsp;<br>Semmi stressz, csak okos játék.',
    'button_text_1': 'FOGADÁSOM ELHELYEZÉSE',
  },
  'pl-PL': {
    'subject': '🎯 Zakład nie wypalił? Odzyskaj 20%',
    'preheader': 'Twój 20% Zakład Bez Ryzyka jest aktywny - graj pewnie dalej',
    'body': 'W sporcie nie każdy zakład trafia - ale my stoimy za Tobą.<br>Postaw następny zakład z kodem <strong class="promocode">WINBACKNRF20</strong> i odbierz <strong>20% Zakład Bez Ryzyka</strong>.<br><br>Jeśli nie pójdzie po Twojej myśli, zwrócimy <strong>20%</strong> na Twoje konto.&nbsp;<br>Zero stresu, tylko mądra gra.',
    'button_text_1': 'POSTAW MÓJ ZAKŁAD',
  }
}

# ============ Email 3C ============
T['Email 3C'] = {
  'hu-HU': {
    'subject': '🍓 140% + 50 Ingyenes Pörgetés - Csatlakozz a Fruit Party-hoz',
    'preheader': 'Édesítsd meg a következő befizetésedet ezzel a zamatos bónusszal',
    'body': 'Készen állsz valami édesre?<br><br>Használd a <strong class="promocode">PARTY140</strong> kódot a következő befizetésednél és kapj <strong>140% Bónuszt + 50 Ingyenes Pörgetést</strong> a <strong>Fruit Party</strong> <strong>by Pragmatic Play</strong> játékban.<br><br>Ez a játék színekkel és nyerési lehetőségekkel teli.<br>Pörögjön a tárcsa!',
    'button_text_1': 'BÓNUSZOM MEGSZERZÉSE',
  },
  'pl-PL': {
    'subject': '🍓 140% + 50 Darmowych Spinów - Dołącz do Fruit Party',
    'preheader': 'Osłódź swoją następną wpłatę tym soczystym bonusem',
    'body': 'Gotowy na coś słodkiego?<br><br>Użyj kodu <strong class="promocode">PARTY140</strong> przy następnej wpłacie i odbierz <strong>140% Bonus + 50 Darmowych Spinów</strong> w grze <strong>Fruit Party</strong> <strong>by Pragmatic Play</strong>.<br><br>Ta gra pęka od kolorów i potencjału wygranych.<br>Kręćmy bębnami!',
    'button_text_1': 'ZGARNIJ MÓJ BONUS',
  }
}

# ============ Email 3M ============
T['Email 3M'] = {
  'hu-HU': {
    'subject': '🎯 2%/3%/4% Cashback + 20%/25%/30% Kockázatmentes Fogadás',
    'preheader': 'Erősítsd a játékod a casino és sport oldalon is',
    'body': 'A következő befizetésed kettős jutalmat old fel - bármit is játszol.<br><br>Használd a <strong class="promocode">SAFE2CB2</strong> / <strong class="promocode">RETURN3CB3</strong> / <strong class="promocode">BOOST4CB4 </strong>kódot és kapj:<br><strong>2%/3%/4% Cashback</strong>-et a casino tevékenységedre<br><br>Vagy használd a <strong class="promocode">WINBACKNRF20</strong> / <strong class="promocode">SAFETYNRF25</strong> / <strong class="promocode">COVERNRF30 </strong>kódot és kapj:<br><strong>20%/25%/30% Kockázatmentes Fogadást</strong> a sportfogadásaidra<br><br>Te döntöd el, hogyan játszol - mi gondoskodunk róla, hogy megtérüljön.',
    'button_text_1': 'KÓDOM HASZNÁLATA',
  },
  'pl-PL': {
    'subject': '🎯 2%/3%/4% Cashback + 20%/25%/30% Zakład Bez Ryzyka',
    'preheader': 'Wzmocnij grę w casino i w sporcie jednocześnie',
    'body': 'Twoja następna wpłata odblokowuje podwójną nagrodę - bez względu na to, w co grasz.<br><br>Użyj kodu <strong class="promocode">SAFE2CB2</strong> / <strong class="promocode">RETURN3CB3</strong> / <strong class="promocode">BOOST4CB4 </strong>i otrzymaj:<br><strong>2%/3%/4% Cashback</strong> na swoją aktywność w casino<br><br>Lub użyj kodu <strong class="promocode">WINBACKNRF20</strong> / <strong class="promocode">SAFETYNRF25</strong> / <strong class="promocode">COVERNRF30 </strong>i odbierz:<br><strong>20%/25%/30% Zakład Bez Ryzyka</strong> na swoje zakłady sportowe<br><br>Ty decydujesz, jak grać - my zadbamy, żeby się opłaciło.',
    'button_text_1': 'UŻYJ MOJEGO KODU',
  }
}

# ============ Email 3S ============
T['Email 3S'] = {
  'hu-HU': {
    'subject': '🧲 20% Kockázatmentes Fogadás - Maradj a játékban',
    'preheader': 'Nyersz vagy nem, a következő tétedre 20% visszajár - használd a WINBACKNRF20 kódot',
    'body': 'Az első befizetésed biztonsági hálót nyitott meg - ne hagyd, hogy kárba menjen.<br><br>Használd a <strong class="promocode">WINBACKNRF20</strong> kódot a <strong>20% Kockázatmentes Fogadás</strong> aktiválásához és tedd meg a következő téted tudván, hogy a veszteség egy részét fedjük, ha nem jön be.&nbsp;<br><br>Egyszerű, okos és gördülékeny fogadás.',
    'button_text_1': 'MEGTESZEM A TÉTEM',
  },
  'pl-PL': {
    'subject': '🧲 20% Zakład Bez Ryzyka - Zostań w grze',
    'preheader': 'Wygrasz czy nie, następny zakład z 20% zwrotem - użyj kodu WINBACKNRF20',
    'body': 'Twoja pierwsza wpłata odblokowała siatkę bezpieczeństwa - nie pozwól jej się zmarnować.<br><br>Użyj kodu <strong class="promocode">WINBACKNRF20</strong>, żeby aktywować <strong>20% Zakład Bez Ryzyka</strong> i postaw następny zakład ze świadomością, że pokryjemy część straty, jeśli nie trafi.&nbsp;<br><br>Proste, mądre i bezproblemowe obstawianie.',
    'button_text_1': 'STAWIAM MÓJ ZAKŁAD',
  }
}

# ============ Email 4C ============
T['Email 4C'] = {
  'hu-HU': {
    'subject': '🧁 Legyél te a dork - 110% + 50 Ingyenes Pörgetés vár',
    'preheader': 'A Dork Unit vár egy bónusszal, ami korántsem vicces',
    'body': 'Hozzáférést kaptál az egyik legkülönlegesebb találathoz.<br><br>Használd a <strong class="promocode">DORK50110</strong> kódot a következő befizetésednél és kapj <strong>110% Bónuszt + 50 Ingyenes Pörgetést</strong> a <strong>Dork Unit</strong> <strong>by Hacksaw Gaming</strong> játékban.<br><br>Ne hagyd, hogy a név becsapjon - ez a nyerőgép komoly nyerési lehetőséget rejt.',
    'button_text_1': 'BÓNUSZOM AKTIVÁLÁSA',
  },
  'pl-PL': {
    'subject': '🧁 Bądź dorkiem - 110% + 50 Darmowych Spinów w środku',
    'preheader': 'Dork Unit czeka z bonusem, który wcale nie jest głupi',
    'body': 'Odblokowałeś dostęp do jednego z najbardziej ekscentrycznych hitów.<br><br>Użyj kodu <strong class="promocode">DORK50110</strong> przy następnej wpłacie i odbierz <strong>110% Bonus + 50 Darmowych Spinów</strong> w grze <strong>Dork Unit</strong> <strong>by Hacksaw Gaming</strong>.<br><br>Nie daj się zwieść nazwie - ten slot kryje poważny potencjał wygranych.',
    'button_text_1': 'AKTYWUJ MÓJ BONUS',
  }
}

# ============ Email 4M ============
T['Email 4M'] = {
  'hu-HU': {
    'subject': '💸 $100,000+ nyeremény a múlt héten - Te leszel a következő?',
    'preheader': 'Nézd meg a legújabb nagy nyereményeket valódi játékosoktól',
    'body': 'A tárcsák izzottak a múlt héten - és íme, kik húzták be a legnagyobbat:<br><br><strong>l\u202288 nyert $47,230-t a Sweet Bonanza játékban</strong><br><strong>v\u202201 betalált $35,910-et a Money Train 3-on</strong><br><strong>B\u2022in zsebelt $18,450-et a Gates of Olympus-on</strong><br><br>Ezek valódi nyeremények valódi játékosoktól, akik pont úgy pörgettek, mint te.<br>Szóval\u2026 készen állsz, hogy legközelebb a te neved legyen ott fent?',
    'button_text_1': 'PÖRGETÉS A NYEREMÉNYÉRT',
  },
  'pl-PL': {
    'subject': '💸 Ponad $100,000 wygranych w zeszłym tygodniu - Dołączysz do listy?',
    'preheader': 'Zobacz najnowsze wielkie wygrane prawdziwych graczy',
    'body': 'Bębny były rozgrzane w zeszłym tygodniu - a oto kto wyciągnął najwięcej:<br><br><strong>l\u202288 wygrał $47,230 na Sweet Bonanza</strong><br><strong>v\u202201 trafił $35,910 na Money Train 3</strong><br><strong>B\u2022in zgarnął $18,450 na Gates of Olympus</strong><br><br>To prawdziwe wygrane prawdziwych graczy, którzy kręcili tak samo jak Ty.<br>Więc\u2026 gotowy zobaczyć swoje imię na liście?',
    'button_text_1': 'KRĘĆ I WYGRYWAJ',
  }
}

# ============ Email 4S ============
T['Email 4S'] = {
  'hu-HU': {
    'subject': '💼 25% Kockázatmentes Fogadás - Fedezve vagy',
    'preheader': 'Tedd meg a következő téted és kapj vissza 25%-ot, ha nem jön be',
    'body': 'Már megcsináltad az első befizetésedet - ideje magabiztosan fogadni.<br><br>Használd a <strong class="promocode">SAFETYNRF25</strong> kódot a <strong>25% Kockázatmentes Fogadás</strong> aktiválásához - a következő téted biztonsági hálóval érkezik. Ha az eredmény nem a javadra dől el, visszakapod a téted <strong>25%</strong>-át az egyenlegedre.',
    'button_text_1': 'FOGADÁSOM ELHELYEZÉSE',
  },
  'pl-PL': {
    'subject': '💼 25% Zakład Bez Ryzyka - Jesteś zabezpieczony',
    'preheader': 'Postaw następny zakład i odzyskaj 25%, jeśli nie wyjdzie',
    'body': 'Już dokonałeś pierwszej wpłaty - czas obstawiać pewnie.<br><br>Użyj kodu <strong class="promocode">SAFETYNRF25</strong>, żeby aktywować <strong>25% Zakład Bez Ryzyka</strong> - Twój następny zakład ma siatkę bezpieczeństwa. Jeśli wynik nie będzie po Twojej stronie, zwrócimy <strong>25%</strong> Twojej stawki na saldo.',
    'button_text_1': 'POSTAW MÓJ ZAKŁAD',
  }
}

# ============ Email 5C ============
T['Email 5C'] = {
  'hu-HU': {
    'subject': '🍭 Kapj 100% + 80 Ingyenes Pörgetést a Sweet Bonanza játékban',
    'preheader': 'A következő befizetési bónuszod most lett igazán édes',
    'body': 'Készülj a cukormámorra.<br><br>Használd a <strong class="promocode">BONANZA10080</strong> kódot a következő befizetésednél és kapj <strong>100% Bónuszt + 80 Ingyenes Pörgetést</strong> a <strong>Sweet Bonanza</strong> <strong>by Pragmatic Play</strong> játékon.<br><br>Zamatos nyeremények, magas volatilitás és rengeteg meglepetés - mi kell még?',
    'button_text_1': 'SWEET BONANZA JÁTÉK',
  },
  'pl-PL': {
    'subject': '🍭 Odbierz 100% + 80 Darmowych Spinów na Sweet Bonanza',
    'preheader': 'Bonus od następnej wpłaty właśnie stał się dużo słodszy',
    'body': 'Przygotuj się na cukrowy zastrzyk.<br><br>Użyj kodu <strong class="promocode">BONANZA10080</strong> przy następnej wpłacie i odbierz <strong>100% Bonus + 80 Darmowych Spinów</strong> w grze <strong>Sweet Bonanza</strong> <strong>by Pragmatic Play</strong>.<br><br>Soczyste wygrane, wysoka zmienność i mnóstwo niespodzianek - co tu nie kochać?',
    'button_text_1': 'GRAJ W SWEET BONANZA',
  }
}

# ============ Email 5M ============
T['Email 5M'] = {
  'hu-HU': {
    'subject': '🪙 100% + 70 Ingyenes Pörgetés vagy 20% Kockázatmentes Fogadás - Válassz',
    'preheader': 'Casino vagy sport - a második lépéses bónuszod mindkét esetben kész',
    'body': 'Az első befizetéseden túl vagy - most ideje erősíteni a következő lépésedet.<br>Íme, mi vár rád:<br><br>🎰 A <strong class="promocode">CHAOS10070</strong> kóddal - <strong>100% Bónusz</strong> + <strong>70 Ingyenes Pörgetés </strong>a<strong> Chaos Crew II by Hacksaw Gaming</strong> játékban casino rajongóknak<br>⚽ A <strong class="promocode">WINBACKNRF20</strong> kóddal - <strong>20% Kockázatmentes Fogadás</strong>, ha az odds a te műfajod<br><br>Bármelyik utat is választod, a jutalmad a te játékodra szabva vár.',
    'button_text_1': 'BÓNUSZOM KIVÁLASZTÁSA',
  },
  'pl-PL': {
    'subject': '🪙 100% + 70 Darmowych Spinów lub 20% Zakład Bez Ryzyka - Wybierz',
    'preheader': 'Casino czy sport - Twój bonus drugiego kroku jest gotowy w obu przypadkach',
    'body': 'Pierwsza wpłata za Tobą - czas wzmocnić następny ruch.<br>Oto co na Ciebie czeka:<br><br>🎰 Z kodem <strong class="promocode">CHAOS10070</strong> - <strong>100% Bonus</strong> + <strong>70 Darmowych Spinów </strong>w<strong> Chaos Crew II by Hacksaw Gaming</strong> dla miłośników casino<br>⚽ Z kodem <strong class="promocode">WINBACKNRF20</strong> - <strong>20% Zakład Bez Ryzyka</strong>, jeśli kursy to Twój żywioł<br><br>Niezależnie od tego, jak grasz, nagroda jest dopasowana do Twojej gry.',
    'button_text_1': 'WYBIERAM MÓJ BONUS',
  }
}

# ============ Email 5S ============
T['Email 5S'] = {
  'hu-HU': {
    'subject': '🏅 30% Kockázatmentes Fogadás - Rajt',
    'preheader': 'Játssz magabiztosan - a következő téted 30% biztonsági hálóval jön',
    'body': 'Már megtetted az első lépésedet - most lőj magabiztosan.<br><br>Élvezd a <strong>30% Kockázatmentes Fogadás</strong> bónuszt a következő sporttéteden a <strong class="promocode">ONLYWIN30</strong> kóddal.<br><br>Ha nem a javadra dől el, visszakapod a téted <strong>30%</strong>-át.&nbsp;<br>Semmi nyomás - csak tiszta játék.',
    'button_text_1': 'FOGADÁSOM ELHELYEZÉSE',
  },
  'pl-PL': {
    'subject': '🏅 30% Zakład Bez Ryzyka - Zaczynamy',
    'preheader': 'Graj pewnie - Twój następny zakład z 30% siatką bezpieczeństwa',
    'body': 'Zrobiłeś już pierwszy krok - teraz strzelaj pewnie.<br><br>Ciesz się <strong>30% Zakładem Bez Ryzyka</strong> na następny zakład sportowy z kodem <strong class="promocode">ONLYWIN30</strong>.<br><br>Jeśli nie pójdzie po Twojej myśli, zwrócimy <strong>30%</strong> Twojej stawki.&nbsp;<br>Bez presji - po prostu graj.',
    'button_text_1': 'POSTAW MÓJ ZAKŁAD',
  }
}

# ============ Email 6C ============
T['Email 6C'] = {
  'hu-HU': {
    'subject': '📜 100% + 150 Ingyenes Pörgetés - Lépj be a Tome of Madness-be',
    'preheader': 'Turbózd fel a befizetésedet és pörögj a titkokon keresztül',
    'body': 'Készen állsz a sötét kincsek felfedezésére?<br><br>Használd a <strong class="promocode">RICH100150</strong> kódot a következő befizetésednél és kapj <strong>100% Bónuszt + 150 Ingyenes Pörgetést</strong> a <strong>Rich Wilde and the Tome of Madness</strong> <strong>by Play\'n Go</strong> játékban.<br><br>Misztikus erő. Titokzatos szimbólumok. Végtelen kaland.',
    'button_text_1': 'INGYENES PÖRGETÉSEIM IGÉNYLÉSE',
  },
  'pl-PL': {
    'subject': '📜 100% + 150 Darmowych Spinów - Wejdź do Tome of Madness',
    'preheader': 'Doładuj wpłatę i kręć przez sekrety',
    'body': 'Gotowy na odkrycie mrocznych skarbów?<br><br>Użyj kodu <strong class="promocode">RICH100150</strong> przy następnej wpłacie i odbierz <strong>100% Bonus + 150 Darmowych Spinów</strong> w grze <strong>Rich Wilde and the Tome of Madness</strong> <strong>by Play\'n Go</strong>.<br><br>Tajemnicza moc. Mistyczne symbole. Niekończąca się przygoda.',
    'button_text_1': 'ODBIERZ MOJE DARMOWE SPINY',
  }
}

# ============ Email 6M ============
T['Email 6M'] = {
  'hu-HU': {
    'subject': '💰 2%/3%/4% Cashback + 20%/25%/30% Kockázatmentes Fogadás',
    'preheader': 'Játssz okosan Cashback-kel a casinóban és Kockázatmentes Fogadással a sportban',
    'body': 'Többet akarsz minden pörgetésből és fogadásból?&nbsp;<br><br>A következő befizetésed a <strong class="promocode">SAFE2CB2</strong> / <strong class="promocode">RETURN3CB3</strong> / <strong class="promocode">BOOST4CB4</strong> kóddal:<br><strong>2%/3%/4% Cashback</strong>-et ad a casino játékodra<br><br>Vagy használd a <strong class="promocode">WINBACKNRF20</strong> / <strong class="promocode">SAFETYNRF25</strong> / <strong class="promocode">COVERNRF30 </strong>kódot és kapj:<br><strong>20%/25%/30% Kockázatmentes Fogadást</strong> a sportfogadásaidra<br><br>Te hozod a játékot - mi hozzuk az értéket. A te stílusod, most felturbózva.',
    'button_text_1': 'KÓDOM HASZNÁLATA',
  },
  'pl-PL': {
    'subject': '💰 2%/3%/4% Cashback + 20%/25%/30% Zakład Bez Ryzyka',
    'preheader': 'Graj mądrze z Cashbackiem w casino i Zakładem Bez Ryzyka w sporcie',
    'body': 'Chcesz więcej z każdego spinu i zakładu?&nbsp;<br><br>Twoja następna wpłata z kodem <strong class="promocode">SAFE2CB2</strong> / <strong class="promocode">RETURN3CB3</strong> / <strong class="promocode">BOOST4CB4</strong> daje Ci:<br><strong>2%/3%/4% Cashback</strong> na Twoją grę w casino<br><br>Lub użyj <strong class="promocode">WINBACKNRF20</strong> / <strong class="promocode">SAFETYNRF25</strong> / <strong class="promocode">COVERNRF30 </strong>i otrzymaj:<br><strong>20%/25%/30% Zakład Bez Ryzyka</strong> na swoje zakłady sportowe<br><br>Ty dostarczasz grę - my dostarczamy wartość. Twój styl, teraz ulepszony.',
    'button_text_1': 'UŻYJ MOJEGO KODU',
  }
}

# ============ Email 6S ============
T['Email 6S'] = {
  'hu-HU': {
    'subject': '🔁 20% Kockázatmentes Fogadás - Legyen a következő a nyerő',
    'preheader': 'Nem jött be? Visszakapod a 20%-ot a következő tétedre - használd a WINBACKNRF20 kódot',
    'body': 'Megtetted az első fogadásodat - most több teret adunk a merész játékhoz.<br><br>Használd a <strong class="promocode">WINBACKNRF20</strong> kódot a <strong>20% Kockázatmentes Fogadás</strong> aktiválásához - a következő téted beépített védelemmel érkezik.&nbsp;<br><br>Ha nem a javadra dől el, visszakapod a téted <strong>20%</strong>-át - ilyen egyszerű.',
    'button_text_1': 'FOGADÁSOM ELHELYEZÉSE',
  },
  'pl-PL': {
    'subject': '🔁 20% Zakład Bez Ryzyka - Niech następny trafi',
    'preheader': 'Nie trafiłeś? Zwrócimy 20% na następny zakład - użyj kodu WINBACKNRF20',
    'body': 'Postawiłeś pierwszy zakład - teraz dajemy Ci więcej przestrzeni na odważną grę.<br><br>Użyj kodu <strong class="promocode">WINBACKNRF20</strong>, żeby aktywować <strong>20% Zakład Bez Ryzyka</strong> - Twój następny zakład ma wbudowaną ochronę.&nbsp;<br><br>Jeśli wynik nie będzie po Twojej stronie, zwrócimy <strong>20%</strong> Twojej stawki - tak po prostu.',
    'button_text_1': 'POSTAW MÓJ ZAKŁAD',
  }
}

# ============ Email 7C ============
T['Email 7C'] = {
  'hu-HU': {
    'subject': '🔥 A legnagyobb nyeremények a következő befizetésekből jöttek',
    'preheader': 'Te leszel a következő nagy nyertes?',
    'body': 'Néhány legnagyobb jackpot történetünk egy újabb befizetéssel kezdődött.<br><br>Nincs trükk - csak egy újabb esély a kedvenc játékaidra és az arany pörgetésre.<br><br>Készen állsz, hogy megírd a saját nyerő történetedet?',
    'button_text_1': 'VISSZAJÖTTEM',
  },
  'pl-PL': {
    'subject': '🔥 Największe wygrane przyszły z kolejnych wpłat',
    'preheader': 'Będziesz następnym wielkim zwycięzcą?',
    'body': 'Niektóre z naszych największych historii jackpotów zaczęły się od kolejnej wpłaty.<br><br>Żadna sztuczka - po prostu kolejna szansa na ulubione gry i złoty obrót.<br><br>Gotowy napisać swoją własną historię wygranej?',
    'button_text_1': 'WRACAM DO GRY',
  }
}

# ============ Email 7M ============
T['Email 7M'] = {
  'hu-HU': {
    'subject': '🎉 Nagy nyeremények ebben a hónapban - Több mint $120,000 kifizetve',
    'preheader': 'Ezek a játékosok nagyot kaszáltak - nézd, miben nyertek',
    'body': 'A számok megérkeztek - és ez a hónap komoly nyereményeket hozott:<br><br><strong>r\u2022y45 nyert $50,780-t a The Dog House Megaways játékban</strong><br><strong>Uncn betalált $41,300-at a Book of Dead-en</strong><br><strong>t\u20225s zsebelt $31,920-t a Fruit Party-n</strong><br><br>Ők megtették a lépésüket - és megtérült.&nbsp;<br>A következő nagy pillanat a tiéd lehet?',
    'button_text_1': 'JÁTSZOM MOST',
  },
  'pl-PL': {
    'subject': '🎉 Wielkie wygrane w tym miesiącu - Ponad $120,000 wypłacone',
    'preheader': 'Ci gracze trafili grubo - zobacz w co grali i ile wygrali',
    'body': 'Liczby są już znane - a ten miesiąc przyniósł poważne wygrane:<br><br><strong>r\u2022y45 wygrał $50,780 na The Dog House Megaways</strong><br><strong>Uncn trafił $41,300 na Book of Dead</strong><br><strong>t\u20225s zgarnął $31,920 na Fruit Party</strong><br><br>Zrobili swój ruch - i się opłaciło.&nbsp;<br>Czy następny wielki moment będzie Twój?',
    'button_text_1': 'GRAJ TERAZ',
  }
}

# ============ Email 7S ============
T['Email 7S'] = {
  'hu-HU': {
    'subject': '🏁 A 20% Kockázatmentes Fogadásod él',
    'preheader': 'Fogadj magabiztosan - ha nem jön be, 20% visszajár',
    'body': 'Jó hír - használd a <strong class="promocode">WINBACKNRF20</strong> kódot a <strong>20% Kockázatmentes Fogadásod</strong> igényléséhez.<br><br>Tedd meg a következő sporttétedet, és ha nem jön be, visszakapod a téted <strong>20%</strong>-át az egyenlegedre.<br><br>Egyszerű, okos, és arra készült, hogy a játékban tartson.',
    'button_text_1': 'FOGADÁSOM ELHELYEZÉSE',
  },
  'pl-PL': {
    'subject': '🏁 Twój 20% Zakład Bez Ryzyka jest aktywny',
    'preheader': 'Obstawiaj pewnie - 20% wraca, jeśli nie trafi',
    'body': 'Dobra wiadomość - użyj kodu <strong class="promocode">WINBACKNRF20</strong>, żeby odebrać swój <strong>20% Zakład Bez Ryzyka</strong>.<br><br>Postaw następny zakład sportowy, a jeśli nie trafi, zwrócimy <strong>20%</strong> Twojej stawki na saldo.<br><br>Proste, mądre i stworzone, żebyś został w grze.',
    'button_text_1': 'POSTAW MÓJ ZAKŁAD',
  }
}

# ============ Email 8C ============
T['Email 8C'] = {
  'hu-HU': {
    'subject': '⚡ 150% + 30 Ingyenes Pörgetés - Szabadítsd el a Stormforged erejét',
    'preheader': 'Üss keményen a következő befizetési bónuszoddal',
    'body': 'Érzed a mennydörgést? A <strong>Stormforged</strong> hív.<br><br>Használd a <strong class="promocode">FORGED150</strong> kódot a következő befizetésednél, hogy feloldd a <strong>150% Bónuszt + 30 Ingyenes Pörgetést</strong> a <strong>Stormforged by Hacksaw Gaming</strong> elektrizáló nyerőgépén.<br><br>Az istenek várnak - hozd a vihart.',
    'button_text_1': 'BÓNUSZOM IGÉNYLÉSE',
  },
  'pl-PL': {
    'subject': '⚡ 150% + 30 Darmowych Spinów - Uwolnij moc Stormforged',
    'preheader': 'Uderz mocno z bonusem od następnej wpłaty',
    'body': 'Czujesz grzmot? To <strong>Stormforged</strong> wzywa.<br><br>Użyj kodu <strong class="promocode">FORGED150</strong> przy następnej wpłacie, żeby odblokować <strong>150% Bonus + 30 Darmowych Spinów</strong> na elektryzującym slocie <strong>Stormforged by Hacksaw Gaming</strong>.<br><br>Bogowie czekają - sprowadź burzę.',
    'button_text_1': 'ODBIERZ MÓJ BONUS',
  }
}

# ============ Email 8M ============
T['Email 8M'] = {
  'hu-HU': {
    'subject': '💵 2%/3%/4% Cashback + 20%/25%/30% Kockázatmentes Fogadás',
    'preheader': 'Erősítsd a casinót és a sportot egyetlen lépéssel',
    'body': 'A játékod többet érdemel - és ez a kombó megadja.<br><br>A következő befizetésednél használd a <strong class="promocode">SAFE2CB2</strong> / <strong class="promocode">RETURN3CB3</strong> / <strong class="promocode">BOOST4CB4</strong> kódot és oldd fel:<br><strong>2%/3%/4% Cashback</strong>-et a casino játékodra<br><br>Vagy használd a <strong class="promocode">WINBACKNRF20</strong> / <strong class="promocode">SAFETYNRF25</strong> / <strong class="promocode">COVERNRF30 </strong>kódot és kapj:<br><strong>20%/25%/30% Kockázatmentes Fogadást</strong> a következő sportfogadásaidraOkos, rugalmas, és a te stílusod jutalmazására tervezve.',
    'button_text_1': 'BÓNUSZOM IGÉNYLÉSE',
  },
  'pl-PL': {
    'subject': '💵 2%/3%/4% Cashback + 20%/25%/30% Zakład Bez Ryzyka',
    'preheader': 'Wzmocnij casino i sport jednym ruchem',
    'body': 'Twoja gra zasługuje na więcej - a to combo dostarcza.<br><br>Przy następnej wpłacie użyj kodu <strong class="promocode">SAFE2CB2</strong> / <strong class="promocode">RETURN3CB3</strong> / <strong class="promocode">BOOST4CB4</strong>, żeby odblokować:<br><strong>2%/3%/4% Cashback</strong> na Twoją grę w casino<br><br>Lub użyj kodu <strong class="promocode">WINBACKNRF20</strong> / <strong class="promocode">SAFETYNRF25</strong> / <strong class="promocode">COVERNRF30 </strong>i odbierz:<br><strong>20%/25%/30% Zakład Bez Ryzyka</strong> na następne zakłady sportoweMądrze, elastycznie i zaprojektowane, żeby nagradzać Twój styl.',
    'button_text_1': 'ODBIERZ MÓJ BONUS',
  }
}

# ============ Email 8S ============
T['Email 8S'] = {
  'hu-HU': {
    'subject': '🧲 30% Kockázatmentes Fogadás - Az előnyöd a következő tétben',
    'preheader': 'Nem jön be a következő téted? Semmi gond - visszakapod a téted 30%-át',
    'body': 'Beléptél a játékba - most ideje továbblépni extra biztonsággal.<br><br>Tedd meg a következő sporttétedet <strong>30% Kockázatmentes Fogadással</strong> a <strong class="promocode">ONLYWIN30.</strong> kóddal.<br><br><strong></strong>Ha nem a javadra dől el, visszakapod a téted <strong>30%</strong>-át - kérdés nélkül.',
    'button_text_1': 'FOGADÁS KOCKÁZAT NÉLKÜL',
  },
  'pl-PL': {
    'subject': '🧲 30% Zakład Bez Ryzyka - Twoja przewaga w następnym zakładzie',
    'preheader': 'Następny zakład nie trafi? Bez obaw - zwrócimy 30% stawki',
    'body': 'Wszedłeś do gry - czas pójść dalej z dodatkowym zabezpieczeniem.<br><br>Postaw następny zakład sportowy z <strong>30% Zakładem Bez Ryzyka</strong> z kodem <strong class="promocode">ONLYWIN30.</strong><br><br><strong></strong>Jeśli nie pójdzie po Twojej myśli, dostaniesz <strong>30%</strong> stawki z powrotem - bez pytań.',
    'button_text_1': 'OBSTAWIAJ BEZ RYZYKA',
  }
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
            # Replace subject
            if 'subject' in tr:
                d['subject'] = tr['subject']
                changes += 1
            
            # Replace preheader
            if 'preheader' in tr:
                d['preheader'] = tr['preheader']
                changes += 1
            
            # Replace button_text_1
            if 'button_text_1' in tr:
                d['button_text_1'] = tr['button_text_1']
                changes += 1
            
            # Replace text_1 greeting
            old_text1 = d.get('text_1', '')
            if locale == 'hu-HU':
                new_greeting = GREETING_HU
            else:
                new_greeting = GREETING_PL
            if GREETING_EN in old_text1:
                d['text_1'] = old_text1.replace(GREETING_EN, new_greeting)
                changes += 1
            
            # Replace text_2 body
            if 'body' in tr:
                old_text2 = d.get('text_2', '')
                m = re.match(r'(.*?<p[^>]*>)(.*)(</p></td>)', old_text2, re.DOTALL)
                if m:
                    d['text_2'] = m.group(1) + tr['body'] + m.group(3)
                    changes += 1
    
    # Reconstruct block
    new_lines = []
    for key in field_order:
        new_lines.append(f'{key}: {d[key]}')
    new_blocks.append('\n'.join(new_lines))

# Write back
result = '\n\n'.join(new_blocks)
with open(filepath, 'w', encoding='utf-8') as f:
    f.write(result)

print(f"FTD Retention Flow: {changes} fields translated")
print(f"Expected: 240 (24 emails x 2 locales x 5 fields)")
