# 09 — Персоналізація — Гайд з імплементації

**Ланцюг:** Personalization (Anniversary, Birthday, Custom, Zodiac)  
**Приблизна кількість комунікацій:** 4 на тип × 4 типи = 16 загалом  
**Передумови з Master Doc:** Атрибути `registration_date`, `birthday`, `zodiac_sign`, `most_played_game_name`, `biggest_win_ars`, `total_rounds_played`

---

## КРОК 0: ПЕРЕДСТАРТОВИЙ ЧЕК-ЛИСТ

- [ ] Атрибут `registration_date` доступний (для розрахунку річниці)
- [ ] Атрибут `birthday` доступний (з KYC або профілю)
- [ ] Атрибут `zodiac_sign` розраховується з дня народження
- [ ] Статистика гравця доступна: загальна кількість раундів, улюблена гра, найбільший виграш (для річнічного емейлу)
- [ ] Бонусні шаблони створені: Anniversary Year 1 (100% up to 5,000 + 30 FS + 500 CC), Birthday (100% up to 3,000 + 25 FS + 300 CC)
- [ ] Шаблон зодіакального бонусу: 50% match + 15 FS, 20× wagering, 7-day validity
- [ ] Lucky Wheel доступний для ігор, прив'язаних до знака зодіаку
- [ ] CRM-менеджер може вручну ініціювати кампанії "Personal Custom"

---

## ТИП A: РІЧНИЦЯ

**Journey Name:** `09-PERS-ANNIV-JOURNEY`  
**Тригер входу:** Збіг дати: річниця `registration_date` (щорічно)  
**Повторний вхід:** Щорічно

### Комунікація 1 — Святкування річниці (День 0, ранок)

| Налаштування | Значення |
|---------|-------|
| **Campaign ID** | `09-PERS-ANNIV-C1-EMAIL-POPUP` |
| **Канал** | Email + In-app popup |

**Вміст емейлу:**
- **Subject (ES):** `🎉 100% + 30 giros + 500 CC - feliz {years} año`
- **Preheader (ES):** `Tu regalo de aniversario personalizado te espera`
- **Banner Text (ES):** `¡Feliz {years} Año!`
- **Banner Description:** Святкування річниці — великий золотий значок річниці з числом "{years}", конфеті, логотип CuatroBet, інтеграція артворку улюбленої гри гравця ({most_played_game_name}), святкові золоті/фіолетові тони
- **Body Description:** Персональне привітання з річницею з підсумком статистики гравця (загальна кількість зіграних раундів, улюблена гра, найбільший виграш). Деталі подарунка: 100% match up to 5,000 ARS + 30 FS на улюблену гру + 500 CC. Wagering 15×, дійсний 72 год.
- **CTA (ES):** `Reclamar regalo` → `{base_url}/cashier`

**Пропозиція (Year 1 базова — масштабується для Year 2+):**
- Year 1: 100% up to 5,000 ARS + 30 FS + 500 CC
- Year 2: 120% up to 7,000 ARS + 40 FS + 800 CC
- Year 3+: 150% up to 10,000 ARS + 60 FS + 1,200 CC

**In-App Popup (показати при першому логіні в день річниці):**
- **Banner Text (ES):** `¡Feliz Aniversario!`
- **Banner Description:** Компактне святкування річниці — золотий значок, спалах конфеті, іконка подарунка, теплі золоті тони
- **Body (ES):** `¡{first_name}, hoy es tu aniversario! Tenés 100% bono + 30 giros + 500 CC esperándote.`
- **CTA (ES):** `Reclamar regalo` → `{base_url}/cashier`

### Комунікація 2 — Нагадування (День +1)

| Campaign ID | `09-PERS-ANNIV-C2-SMS` |
|------------|------------------------|
| Канал | SMS |
| Text (ES) | `CuatroBet: Tu regalo de aniversario vence en 48h. No lo pierdas: {link}` |
| Умова | Немає депозиту після Комунікації 1 |

### Комунікація 3 — Фінальне нагадування (День +2)

| Campaign ID | `09-PERS-ANNIV-C3-EMAIL` |
|------------|--------------------------|
| Канал | Email |
| **Subject (ES)** | `⏰ Último día: tu regalo de aniversario` |
| **Preheader (ES)** | `Tu bono expira hoy, no lo pierdas` |
| **Banner Text (ES)** | `Último Día — Tu Regalo` |
| **Banner Description** | Терміновість річниці — коробка з подарунком із таймером зворотного відліку, конфеті, що зникає, стрічка "last day", теплі бурштинові тони |
| **Body Description** | Фінальне нагадування: подарунок на річницю закінчується сьогодні. Нагадування деталей пропозиції. Акцент на терміновості. |
| Умова | Немає депозиту після Комунікації 1 |

### Комунікація 4 — Подяка / Перехід (День +3)

| Campaign ID | `09-PERS-ANNIV-C4-EMAIL` |
|------------|--------------------------|
| Канал | Email || **Subject (ES)** | `🙏 Gracias por {years} año con nosotros` |
| **Preheader (ES)** | `Tu historia con CuatroBet apenas comienza` || **Banner Text (ES)** | `Gracias por Ser Parte` |
| **Banner Description** | Візуал подяки — тепла золота сцена, спільнота CuatroBet, іконка серця/рукостискання, натяк на хронологію шляху гравця |
| **Body Description** | Якщо активовано: подяка + огляд досвіду. Якщо не активовано: м'яке повідомлення "ми тут для тебе" із запрошенням повернутися. |
| Вихід | Повернення до звичайного життєвого циклу |

---

## ТИП B: ДЕНЬ НАРОДЖЕННЯ

**Journey Name:** `09-PERS-BDAY-JOURNEY`  
**Тригер входу:** Збіг дати: поле `birthday`  
**Повторний вхід:** Щорічно

### Комунікація 1 — Святкування дня народження (День народження, ранок)

| Налаштування | Значення |
|---------|-------|
| **Campaign ID** | `09-PERS-BDAY-C1-EMAIL-POPUP-SMS` |
| **Канал** | Email + In-app popup + SMS |

**Вміст емейлу:**
- **Subject (ES):** `🎂 100% + 25 giros + 300 CC - feliz cumpleaños`
- **Preheader (ES):** `Tu regalo de cumpleaños de CuatroBet te espera`
- **Banner Text (ES):** `¡Feliz Cumpleaños, {first_name}!`
- **Banner Description:** Тема вечірки на день народження — торт зі свічками, кольорові кульки, спалах конфеті, коробка з подарунком, що відкривається, візуал "🎂", теплі святкові фіолетові/золоті тони
- **Body Description:** Привітання з днем народження з іменем гравця. Деталі подарунка: 100% match up to 3,000 ARS + 25 FS на улюблену гру + 300 CC. Wagering 15×, дійсний 48 год.
- **CTA (ES):** `Abrir regalo` → `{base_url}/cashier`

**In-App Popup:**
- **Banner Text (ES):** `¡Feliz Cumpleaños!`
- **Banner Description:** Компактне святкування дня народження — іконка торта, кульки, конфеті, значок подарунка
- **Body (ES):** `¡Feliz cumpleaños, {first_name}! Tu regalo: 100% bono + 25 giros + 300 CC.`
- **CTA (ES):** `Abrir regalo` → `{base_url}/cashier`

**Вміст SMS (ES):**
- Text: `CuatroBet: ¡Feliz cumpleaños {first_name}! Tu regalo: 100% bono + 25 giros + 300 CC. Reclamalo: {link}`

### Комунікація 2 — Вечірній Push (День народження +12 год)

| Campaign ID | `09-PERS-BDAY-C2-PUSH` |
|------------|-------------------------|
| Канал | App Push |
| Text (ES) | `Tu regalo de cumpleaños te está esperando. Abrilo ahora 🎂` |
| CTA | Deep link на бонус |

### Комунікація 3 — Нагадування (День народження +24 год)

| Campaign ID | `09-PERS-BDAY-C3-SMS` |
|------------|------------------------|
| Канал | SMS |
| Text (ES) | `CuatroBet: Tu regalo de cumpleaños vence en 24h: {link}` |

### Комунікація 4 — Закінчення терміну (День народження +48 год)

| Campaign ID | `09-PERS-BDAY-C4-EMAIL` |
|------------|--------------------------|
| Канал | Email || **Subject (ES)** | `🎂 Gracias por celebrar con CuatroBet` |
| **Preheader (ES)** | `Esperamos que hayas disfrutado tu día especial` || **Banner Text (ES)** | `Gracias` |
| **Banner Description** | Подяка після дня народження — тепле післясвітіння, кульки, що повільно здуваються, стрічка "дякуємо", м'які золоті тони |
| **Body Description** | Якщо активовано: подяка з підсумком дня народження. Якщо не активовано: нотифікація про закінчення пропозиції з м'яким повідомленням про повернення. |
| Вихід | Повернення до звичайного життєвого циклу |

---

## ТИП C: ПЕРСОНАЛЬНІ КАСТОМНІ

**Journey Name:** Ручний запуск (без автоматизованого journey)  
**Дія CRM-менеджера:** Створення разової кампанії за шаблонною структурою

### Шаблон для кожної кастомної кампанії:

| Комунікація | Час | Канал | Контент |
|------|--------|---------|---------|
| C1 | Специфічний для тригера | Найкращий канал для гравця | Початкове персоналізоване повідомлення |
| C2 | +24–48 год | Канал для нагадування | Нагадування, якщо немає відповіді |
| C3 | +72 год | Фінальний канал | Останнє нагадування перед закінченням пропозиції |
| C4 | +96 год | Email | Подяка або перехід |

**Обов'язкові поля для кожної кампанії:**
- Умова тригера (яка подія або ручний відбір)
- Розмір цільової аудиторії
- Канал на кожну комунікацію
- Текст на кожну комунікацію іспанською
- Деталі пропозиції (match %, FS, CC, wagering, validity)
- Умова виходу
- Метрика успіху
- **Огляд: Щотижневий CRM-стендап**

---

## ТИП D: ЗОДІАКАЛЬНИЙ БОНУС

**Journey Name:** `09-PERS-ZODIAC-JOURNEY`  
**Тригер входу:** Перший день кожного зодіакального періоду, фільтр за `zodiac_sign`  
**Повторний вхід:** Щомісячно (кожен зодіакальний період)

### Зодіакальний календар:

| Період | Знак | Дати |
|--------|------|-------|
| 1 | Aries | Mar 21 – Apr 19 |
| 2 | Taurus | Apr 20 – May 20 |
| 3 | Gemini | May 21 – Jun 20 |
| 4 | Cancer | Jun 21 – Jul 22 |
| 5 | Leo | Jul 23 – Aug 22 |
| 6 | Virgo | Aug 23 – Sep 22 |
| 7 | Libra | Sep 23 – Oct 22 |
| 8 | Scorpio | Oct 23 – Nov 21 |
| 9 | Sagittarius | Nov 22 – Dec 21 |
| 10 | Capricorn | Dec 22 – Jan 19 |
| 11 | Aquarius | Jan 20 – Feb 18 |
| 12 | Pisces | Feb 19 – Mar 20 |

### Комунікація 1 — Запуск зодіаку (День 1)

| Налаштування | Значення |
|---------|-------|
| **Campaign ID** | `09-PERS-ZODIAC-C1-EMAIL-BANNER` |
| **Канал** | Email + In-app banner |

**Вміст емейлу:**
- **Subject (ES):** `✨ 50% + 15 giros - tu bono zodiacal de {sign_name}`
- **Preheader (ES):** `Tu signo tiene un regalo especial esperando`
- **Banner Text (ES):** `Bono Zodiacal: {sign_name}`
- **Banner Description:** Візуал на зодіакальну тематику — артворк сузір'я поточного знака зодіаку, містичний фон зоряного неба, символ зодіаку на видному місці, відповідна кольорова палітра для кожного знака
- **Body Description:** Зодіакальне привітання для поточного знака. Пропозиція: 50% match + 15 FS на гру, підібрану за зодіаком, 20× wagering, дійсний 7 днів. Тизер Lucky Wheel.
- **CTA (ES):** `Reclamar bono zodiacal` → `{base_url}/cashier`

### Комунікація 2 — День 3

| Campaign ID | `09-PERS-ZODIAC-C2-PUSH` |
|------------|---------------------------|
| Канал | App Push |
| Text (ES) | `Tu bono zodiacal de {sign_name} está activo. Usalo antes de que termine: {link}` |

### Комунікація 3 — День 5

| Campaign ID | `09-PERS-ZODIAC-C3-SMS` |
|------------|--------------------------|
| Канал | SMS |
| Text (ES) | `CuatroBet: Último chance para tu bono zodiacal. Vence en 2 días: {link}` |

### Комунікація 4 — Останній день

| Campaign ID | `09-PERS-ZODIAC-C4-EMAIL` |
|------------|----------------------------|
| Канал | Email || **Subject (ES)** | `⌛ Último día para tu bono de {sign_name}` |
| **Preheader (ES)** | `Mañana cambia el signo y tu oferta desaparece` || **Banner Text (ES)** | `Último Día Zodiacal` |
| **Banner Description** | Закінчення зодіакального періоду — поточний знак зникає, тизер наступного знака з'являється, візуал зворотного відліку, містичний перехід |
| **Body Description** | Фінальне нагадування про зодіакальний бонус + тизер пропозиції наступного знака зодіаку. |
| Вихід | Повернення до звичайного життєвого циклу |

---

## ЧЕК-ЛИСТ ТЕСТУВАННЯ

- [ ] Річниця спрацьовує у правильну дату (річниця `registration_date`)
- [ ] Річниця Year 2+ коректно масштабує пропозицію
- [ ] Статистика гравця в річнічному емейлі точна
- [ ] День народження спрацьовує лише для гравців із підтвердженим полем birthday
- [ ] Багатоканальність дня народження (email + popup + SMS) спрацьовує одночасно
- [ ] Знак зодіаку правильно розраховується з дня народження
- [ ] Зодіакальна кампанія націлюється лише на гравців відповідного знака
- [ ] Кастомні кампанії можуть бути запущені вручну CRM-менеджером
- [ ] Усі пропозиції мають правильні wagering, validity та суми
- [ ] Бонуси правильно зараховуються на депозит
