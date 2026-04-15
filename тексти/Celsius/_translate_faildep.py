# -*- coding: utf-8 -*-
import re, os, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

filepath = r'c:\Projects\REPORTS\тексти\Celsius\Failed Deposit Flow - Table data.txt'

# Translations for each email: subject, preheader, and text replacements within rich_text
T = {
  'Email 1': {
    'hu-HU': {
      'subject': '😟 Úgy tűnik, valami hiba történt',
      'preheader': 'Segítünk',
      'text_replacements': [
        ('Hi {first_name},', 'Szia {first_name},'),
        ("Your recent deposit attempt didn't complete due to a payment issue. Here's what we advice you:", 'A legutóbbi befizetési kísérlet fizetési hiba miatt nem teljesült. Íme, mit javasolunk:'),
        ('Try a different card or payment network', 'Próbálj meg másik kártyát vagy fizetési hálózatot'),
        ("Use your spouse's card with their permission", 'Használd házastársad kártyáját az ő engedélyével'),
        ('Deposit with cryptocurrency in the Cashier', 'Fizess be kriptovalutával a Pénztárban'),
        ('Complete deposit', 'Befizetés befejezése'),
        ("If you need help, just reply to this email - we're here to assist right away. If you see a temporary hold on your bank side, it should auto-release per your bank's policy.", "Ha segítségre van szükséged, válaszolj erre az e-mailre - azonnal segítünk. Ha ideiglenes zárolást látsz a bankod oldalán, az automatikusan feloldódik a bankod szabályzata szerint."),
        ('Thanks,', 'Köszönjük,'),
        ('utm_language=en', 'utm_language=hu'),
      ],
    },
    'pl-PL': {
      'subject': '😟 Wygląda na to, że coś poszło nie tak',
      'preheader': 'Jesteśmy tu, żeby pomóc',
      'text_replacements': [
        ('Hi {first_name},', 'Cześć {first_name},'),
        ("Your recent deposit attempt didn't complete due to a payment issue. Here's what we advice you:", 'Twoja ostatnia próba wpłaty nie powiodła się z powodu problemu z płatnością. Oto co zalecamy:'),
        ('Try a different card or payment network', 'Wypróbuj inną kartę lub sieć płatniczą'),
        ("Use your spouse's card with their permission", 'Użyj karty współmałżonka za ich zgodą'),
        ('Deposit with cryptocurrency in the Cashier', 'Wpłać kryptowalutą w Kasie'),
        ('Complete deposit', 'Dokończ wpłatę'),
        ("If you need help, just reply to this email - we're here to assist right away. If you see a temporary hold on your bank side, it should auto-release per your bank's policy.", "Jeśli potrzebujesz pomocy, po prostu odpowiedz na ten email - pomożemy od razu. Jeśli widzisz tymczasową blokadę po stronie Twojego banku, powinna zostać automatycznie zwolniona zgodnie z polityką Twojego banku."),
        ('Thanks,', 'Dzięki,'),
        ('utm_language=en', 'utm_language=pl'),
      ],
    },
  },
  'Email 2': {
    'hu-HU': {
      'subject': '🔴 Még mindig gondok vannak a befizetéssel?',
      'preheader': 'Segítünk? Személyes menedzsered már úton van',
      'text_replacements': [
        ('Hi {first_name},', 'Szia {first_name},'),
        ('I can see your deposit still did not go through. Do you need help finishing it? Quick options:', 'Látom, hogy a befizetésed még mindig nem ment át. Segítsünk befejezni? Gyors lehetőségek:'),
        ('Try a different card or payment network', 'Próbálj meg másik kártyát vagy fizetési hálózatot'),
        ("Use your spouse's card with their permission", 'Használd házastársad kártyáját az ő engedélyével'),
        ('Deposit with cryptocurrency in the Cashier', 'Fizess be kriptovalutával a Pénztárban'),
        ('Complete deposit', 'Befizetés befejezése'),
        ("I'm assigning you a personal manager who will contact you shortly to help you complete the payment. If you need support right now, just reply to this email. If you see a temporary hold on your bank side, it should auto-release per your bank's policy.", "Személyes menedzsert rendelek hozzád, aki hamarosan felveszi veled a kapcsolatot a befizetés befejezéséhez. Ha most azonnal segítségre van szükséged, válaszolj erre az e-mailre. Ha ideiglenes zárolást látsz a bankod oldalán, az automatikusan feloldódik a bankod szabályzata szerint."),
        ('Thanks,', 'Köszönjük,'),
        ('utm_language=en', 'utm_language=hu'),
      ],
    },
    'pl-PL': {
      'subject': '🔴 Nadal masz problem z wpłatą?',
      'preheader': 'Potrzebujesz pomocy? Twój osobisty menedżer jest w drodze',
      'text_replacements': [
        ('Hi {first_name},', 'Cześć {first_name},'),
        ('I can see your deposit still did not go through. Do you need help finishing it? Quick options:', 'Widzę, że Twoja wpłata nadal nie przeszła. Potrzebujesz pomocy w jej dokończeniu? Szybkie opcje:'),
        ('Try a different card or payment network', 'Wypróbuj inną kartę lub sieć płatniczą'),
        ("Use your spouse's card with their permission", 'Użyj karty współmałżonka za ich zgodą'),
        ('Deposit with cryptocurrency in the Cashier', 'Wpłać kryptowalutą w Kasie'),
        ('Complete deposit', 'Dokończ wpłatę'),
        ("I'm assigning you a personal manager who will contact you shortly to help you complete the payment. If you need support right now, just reply to this email. If you see a temporary hold on your bank side, it should auto-release per your bank's policy.", "Przydzielam Ci osobistego menedżera, który wkrótce się z Tobą skontaktuje, aby pomóc dokończyć płatność. Jeśli potrzebujesz wsparcia teraz, po prostu odpowiedz na ten email. Jeśli widzisz tymczasową blokadę po stronie Twojego banku, powinna zostać automatycznie zwolniona zgodnie z polityką Twojego banku."),
        ('Thanks,', 'Dzięki,'),
        ('utm_language=en', 'utm_language=pl'),
      ],
    },
  },
  'Email 3': {
    'hu-HU': {
      'subject': 'RE: Sikertelen befizetés',
      'text_replacements': [
        ('Nice to meet you, {first_name},', 'Örülök, hogy megismerhetlek, {first_name},'),
        ("I'm Alex, your personal manager at Celsius Casino Casino. Looks like you have a hard time making the deposit. Let me help you! Please answer this email and I'll help you to sort things out.", "Alex vagyok, a személyes menedzsered a Celsius Casino-nál. Úgy látom, nehézségeid vannak a befizetéssel. Hadd segítsek! Válaszolj erre az e-mailre, és segítek rendezni a dolgokat."),
        ('Complete deposit', 'Befizetés befejezése'),
        ("If you need help, just reply to this email - I'm here to assist you.", "Ha segítségre van szükséged, válaszolj erre az e-mailre - itt vagyok, hogy segítsek."),
        ('Thanks,', 'Köszönjük,'),
        ('Alex from Celsius Casino', 'Alex a Celsius Casino-tól'),
        ('utm_language=en', 'utm_language=hu'),
      ],
    },
    'pl-PL': {
      'subject': 'RE: Nieudana wpłata',
      'text_replacements': [
        ('Nice to meet you, {first_name},', 'Miło Cię poznać, {first_name},'),
        ("I'm Alex, your personal manager at Celsius Casino Casino. Looks like you have a hard time making the deposit. Let me help you! Please answer this email and I'll help you to sort things out.", "Jestem Alex, Twój osobisty menedżer w Celsius Casino. Wygląda na to, że masz problem z dokonaniem wpłaty. Pozwól, że pomogę! Odpowiedz na ten email, a pomogę Ci wszystko załatwić."),
        ('Complete deposit', 'Dokończ wpłatę'),
        ("If you need help, just reply to this email - I'm here to assist you.", "Jeśli potrzebujesz pomocy, po prostu odpowiedz na ten email - jestem tu, żeby Ci pomóc."),
        ('Thanks,', 'Dzięki,'),
        ('Alex from Celsius Casino', 'Alex z Celsius Casino'),
        ('utm_language=en', 'utm_language=pl'),
      ],
    },
  },
  'Email 4': {
    'hu-HU': {
      'subject': '🤗 Értékesek vagytok számunkra!',
      'preheader': 'Kapj 20 Ingyenes Pörgetést a befizetésedhez!',
      'text_replacements': [
        ('Hi {first_name},', 'Szia {first_name},'),
        ("Looks like your deposit didn't complete. Finish it now and we'll add 20 Free Spins on Gates of Olympus as a thank you.", "Úgy tűnik, a befizetésed nem teljesült. Fejezd be most, és köszönetként 20 Ingyenes Pörgetést adunk a Gates of Olympus játékra."),
        ('Quick ways to complete:', 'Gyors módok a befejezéshez:'),
        ('Try a different card or payment network', 'Próbálj meg másik kártyát vagy fizetési hálózatot'),
        ("Use your spouse's card with their permission", 'Használd házastársad kártyáját az ő engedélyével'),
        ('Deposit with cryptocurrency in the Cashier', 'Fizess be kriptovalutával a Pénztárban'),
        ('Complete deposit', 'Befizetés befejezése'),
        ("If you need help, just reply to this email - we're here to assist right away. If you see a temporary hold on your bank side, it should auto-release per your bank's policy.", "Ha segítségre van szükséged, válaszolj erre az e-mailre - azonnal segítünk. Ha ideiglenes zárolást látsz a bankod oldalán, az automatikusan feloldódik a bankod szabályzata szerint."),
        ('Thanks,', 'Köszönjük,'),
        ('utm_language=en', 'utm_language=hu'),
      ],
    },
    'pl-PL': {
      'subject': '🤗 Jesteś dla nas ważny!',
      'preheader': 'Odbierz 20 Darmowych Spinów do wpłaty!',
      'text_replacements': [
        ('Hi {first_name},', 'Cześć {first_name},'),
        ("Looks like your deposit didn't complete. Finish it now and we'll add 20 Free Spins on Gates of Olympus as a thank you.", "Wygląda na to, że Twoja wpłata się nie powiodła. Dokończ ją teraz, a w podziękowaniu dodamy 20 Darmowych Spinów na Gates of Olympus."),
        ('Quick ways to complete:', 'Szybkie sposoby dokończenia:'),
        ('Try a different card or payment network', 'Wypróbuj inną kartę lub sieć płatniczą'),
        ("Use your spouse's card with their permission", 'Użyj karty współmałżonka za ich zgodą'),
        ('Deposit with cryptocurrency in the Cashier', 'Wpłać kryptowalutą w Kasie'),
        ('Complete deposit', 'Dokończ wpłatę'),
        ("If you need help, just reply to this email - we're here to assist right away. If you see a temporary hold on your bank side, it should auto-release per your bank's policy.", "Jeśli potrzebujesz pomocy, po prostu odpowiedz na ten email - pomożemy od razu. Jeśli widzisz tymczasową blokadę po stronie Twojego banku, powinna zostać automatycznie zwolniona zgodnie z polityką Twojego banku."),
        ('Thanks,', 'Dzięki,'),
        ('utm_language=en', 'utm_language=pl'),
      ],
    },
  },
  'Email 5': {
    'hu-HU': {
      'subject': 'RE: Segítség kell',
      'preheader': 'Hogy megy?',
      'text_replacements': [
        ('Hi {first_name},', 'Szia {first_name},'),
        ("Alex's here! I just saw you still haven't completed your deposit :( That's sad! Just let me know how I can help you, I'm always here!", "Alex vagyok! Épp láttam, hogy még mindig nem fejezted be a befizetésedet :( Ez szomorú! Csak szólj, hogyan segíthetek, mindig itt vagyok!"),
        ('Try again:', 'Próbáld újra:'),
        ('Complete deposit', 'Befizetés befejezése'),
        ('If you need help, just reply to this email!', 'Ha segítségre van szükséged, válaszolj erre az e-mailre!'),
        ('Thanks,', 'Köszönjük,'),
        ('Alex from Celsius Casino', 'Alex a Celsius Casino-tól'),
        ('utm_language=en', 'utm_language=hu'),
      ],
    },
    'pl-PL': {
      'subject': 'RE: Potrzebujesz pomocy',
      'preheader': 'Jak idzie?',
      'text_replacements': [
        ('Hi {first_name},', 'Cześć {first_name},'),
        ("Alex's here! I just saw you still haven't completed your deposit :( That's sad! Just let me know how I can help you, I'm always here!", "Tu Alex! Właśnie zauważyłem, że nadal nie dokończyłeś wpłaty :( Szkoda! Po prostu daj znać, jak mogę Ci pomóc, zawsze tu jestem!"),
        ('Try again:', 'Spróbuj ponownie:'),
        ('Complete deposit', 'Dokończ wpłatę'),
        ('If you need help, just reply to this email!', 'Jeśli potrzebujesz pomocy, po prostu odpowiedz na ten email!'),
        ('Thanks,', 'Dzięki,'),
        ('Alex from Celsius Casino', 'Alex z Celsius Casino'),
        ('utm_language=en', 'utm_language=pl'),
      ],
    },
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
            # Replace subject
            if 'subject' in tr:
                d['subject'] = tr['subject']
                changes += 1
            
            # Replace preheader
            if 'preheader' in tr and 'preheader' in d:
                d['preheader'] = tr['preheader']
                changes += 1
            
            # Replace rich_text text content
            if 'text_replacements' in tr and 'rich_text' in d:
                rt = d['rich_text']
                for old_text, new_text in tr['text_replacements']:
                    if old_text in rt:
                        rt = rt.replace(old_text, new_text)
                        changes += 1
                d['rich_text'] = rt
    
    # Reconstruct block  
    new_lines = []
    for key in field_order:
        new_lines.append(f'{key}: {d[key]}')
    new_blocks.append('\n'.join(new_lines))

result = '\n\n'.join(new_blocks)
with open(filepath, 'w', encoding='utf-8') as f:
    f.write(result)

print(f"Failed Deposit Flow: {changes} fields translated")
