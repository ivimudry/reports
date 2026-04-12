# 10 — Залучення та гейміфікація — Гайд з імплементації

**Ланцюг:** Engagement (Loot Boxes, Stickers, 8 Quests, Weekly/Daily/Holiday Bonuses)  
**Пріоритет:** Фаза 3 (Тиждень 7–8)  
**Це найбільший ланцюг — розбити на підпроекти нижче**

---

## КРОК 0: ПЕРЕДСТАРТОВИЙ ЧЕК-ЛИСТ

- [ ] API кредитування/списання CC (Cuatro Coins) функціональний
- [ ] Lucky Wheel система активна з рівнями Silver/Gold/Platinum
- [ ] Канали In-app popup та App Push активні
- [ ] UI лут-боксів готовий у дашборді гравця
- [ ] UI книги наклейок готовий (сітка на 30 слотів)
- [ ] API відстеження прогресу квестів доступний
- [ ] Сума ставок відстежується за типом гри в реальному часі
- [ ] Відстеження логінів для функції денної серії
- [ ] Аргентинський календар свят налаштований на рік

---

## A. ЛУТБОКСИ

**Journey Name:** `10-LB-JOURNEY`  
**Тип:** Тригер на подію (постійний)  
**Вхід:** `total_wagered_ars` досягає наступного інкременту 5,000 ARS (слоти) або 10,000 ARS (live)

### Правила отримання:
- 1 токен лутбокса за кожні 5,000 ARS ставок на слотах
- 1 токен лутбокса за кожні 10,000 ARS ставок на live
- Токени накопичуються в дашборді, відкриваються вручну

### Таблиця нагород:

| Нагорода | Вага | Значення |
|--------|--------|-------|
| Малий подарунок CC | 50% | 25–50 CC |
| Free Spins (5–10) | 25% | На топовому слоті гравця |
| Бонусні гроші | 15% | 500–1,000 ARS |
| Вхід на Lucky Wheel | 7% | 1 Silver вхід |
| Преміальні FS (25+) | 3% | На преміальних іграх |

### 4 комунікації:

**LB-C1: Токен отримано (на подію)**
| Налаштування | Значення |
|---------|-------|
| Campaign ID | `10-LB-C1-PUSH` |
| Канал | App Push |
| Text (ES) | `¡Ganaste un loot box! Abrilo desde tu panel.` |
| CTA | Deep link на дашборд лутбоксів |

**LB-C2: Бокс відкрито (на подію)**
| Налаштування | Значення |
|---------|-------|
| Campaign ID | `10-LB-C2-POPUP` |
| Канал | In-app popup |
| **Banner Text (ES)** | `¡Loot Box Abierto!` |
| **Banner Description** | Святкування відкриття лутбокса — коробка, що світиться та відкривається, розкрита іконка нагороди ({reward}), анімація блиску/конфеті, золоті промені світла |
| **Body (ES)** | `{reward} desbloqueado. ¡Seguí jugando para más!` |

**LB-C3: Тижневе нагадування про незабрані бокси (Понеділок)**
| Налаштування | Значення |
|---------|-------|
| Campaign ID | `10-LB-C3-EMAIL` |
| Канал | Email |
| **Subject (ES)** | `🎁 {count} loot boxes sin abrir te esperan` |
| **Preheader (ES)** | `Descubrí qué hay adentro antes de que expiren` |
| **Banner Text (ES)** | `{count} Loot Boxes Sin Abrir` |
| **Banner Description** | Таємничі лутбокси — стопка коробок, що світяться, знаки питання, що літають, натяк на скарб, захопливі синьо-фіолетові тони |
| **Body Description** | Нагадування про незабрані лутбокси з таємничим тизером. Перелік можливих нагород. Єдина CTA до дашборду. |
| Умова | У гравця ≥1 невідкритий лутбокс |
| **CTA (ES)** | `Abrir ahora` → дашборд |

**LB-C4: Місячний підсумок (1-ше число місяця)**
| Налаштування | Значення |
|---------|-------|
| Campaign ID | `10-LB-C4-EMAIL` |
| Канал | Email |
| **Subject (ES)** | `📊 Tu resumen mensual de loot boxes` |
| **Preheader (ES)** | `Mirá todo lo que ganaste este mes` |
| **Banner Text (ES)** | `Resumen Mensual de Loot Boxes` |
| **Banner Description** | Візуал місячного підсумку — колаж відкритих лутбоксів, іконки підсумку нагород, діаграма порівняння (з минулим місяцем), святкова фіолетово-золота тема |
| **Body Description** | Місячна статистика лутбоксів: відкриті бокси, загальні виграні нагороди, порівняння з минулим місяцем, тизер на наступний місяць. |

---

## B. НАКЛЕЙКИ

**Journey Name:** `10-STK-JOURNEY`  
**Механіка:** Книга наклейок на 30 слотів. Конкретні дії розблоковують наклейки. Ряд з 5 = нагорода. Усі 30 = головний приз.

### Дії для наклейок (приклади — налаштувати 30):
| Наклейка | Потрібна дія |
|---------|----------------|
| #1 | Зіграти в Jackpot Joker 10 разів |
| #2 | Депозит 3 дні поспіль |
| #3 | Спробувати нового провайдера ігор |
| #4 | Поставити 10,000 ARS за тиждень |
| #5 | Виграти 5× ставку за один спін |
| ... | (Визначити решту 25) |

### Рівні нагород:
| Етап | Нагорода |
|-----------|--------|
| Одна наклейка | 25 CC |
| Ряд з 5 завершено | 200 ARS + 10 FS |
| Усі 30 завершено | 10,000 ARS + Premium Lucky Wheel + VIP I попередній перегляд |

### 4 комунікації:

**STK-C1: Наклейка розблокована**
| Campaign ID | `10-STK-C1-PUSH` |
|------------|-------------------|
| Канал | App Push |
| Text (ES) | `Nueva figurita desbloqueada: {sticker_name}. ¡Seguí coleccionando!` |

**STK-C2: Одна наклейка до завершення ряду**
| Campaign ID | `10-STK-C2-EMAIL` |
|------------|---------------------|
| Канал | Email |
| **Subject (ES)** | `🧩 200 ARS + 10 giros: te falta 1 figurita` |
| **Preheader (ES)** | `Completá la fila y ganate el premio` |
| **Banner Text (ES)** | `¡Te Falta 1 Figurita!` |
| **Banner Description** | Майже завершений ряд наклейок — 4/5 слотів заповнено, останній слот блимає/пульсує зі знаком питання, попередній перегляд нагороди 200 ARS + 10 FS, захоплива терміновість |
| **Body Description** | Підсвітити, якої наклейки не вистачає та яка дія її розблокує. Показати попередній перегляд нагороди: 200 ARS + 10 FS. Чітка CTA на виконання дії. |
| Умова | Зібрано 4 з 5 наклейок в ряду |

**STK-C3: Ряд завершено**
| Campaign ID | `10-STK-C3-PUSH-POPUP` |
|------------|--------------------------|
| Канал | App Push + In-app popup |
| **Banner Text (ES)** | `¡Fila Completa!` |
| **Banner Description** | Святкування завершення ряду — 5/5 наклейок сяють, анімація вибуху нагороди (200 ARS + 10 FS), конфеті, золотий значок завершення |
| **Body (ES)** | `¡Fila completa! Ganaste 200 ARS + 10 giros gratis.` |
| Дія | Зарахувати 200 ARS + 10 FS |

**STK-C4: Місячний підсумок**
| Campaign ID | `10-STK-C4-EMAIL` |
|------------|---------------------|
| Канал | Email |
| **Subject (ES)** | `📈 {count} figuritas este mes — faltan {remaining}` |
| **Preheader (ES)** | `El gran premio de 10,000 ARS está cada vez más cerca` |
| **Banner Text (ES)** | `{count} Figuritas Coleccionadas` |
| **Banner Description** | Місячний прогрес наклейок — сітка книги наклейок із заповненими/порожніми слотами, прогрес-бар до 30, попередній перегляд головного призу (10,000 ARS + VIP), колекційна тема |
| **Body Description** | Місячний підсумок наклейок: зібрано, залишилось до головного призу, підказка наступної досяжної наклейки, мотивація. |

---

## C. КВЕСТИ (8 типів квестів)

### Квест 1: 4 депозити ("Misión Cuatro")

**Journey Name:** `10-Q1-MISSION-CUATRO`  
**Автоматичне зарахування:** На FTD  
**Вікно:** 7 ковзних днів  
**Нагороди:** Зростаючі за кожен депозит (див. специфікацію)

| Комунікація | Campaign ID | Час | Канал | Контент (ES) |
|------|------------|--------|---------|-------------|
| C1 | `10-Q1-C1-POPUP-EMAIL` | На FTD | Popup + Email | **Popup Banner:** Активація квесту — логотип "Misión Cuatro", прогрес-бар на 4 кроки, попередній перегляд першої нагороди. **Email Banner:** Те саме. **Body:** `¡Misión Cuatro activada! 4 depósitos en 7 días = premios increíbles.` |
| C2 | `10-Q1-C2-PUSH` | Після 2-го депозиту | App Push | `¡Vas por la mitad! 2 depósitos más para completar la Misión Cuatro.` |
| C3 | `10-Q1-C3-SMS` | Після 3-го депозиту | SMS | `CuatroBet: ¡Falta 1 depósito para ganar 30 giros + 200 CC + bono 50%! {link}` |
| C4 | `10-Q1-C4-POPUP-EMAIL` | Після 4-го депозиту | Popup + Email | **Popup Banner:** Місія завершена — 4/4 галочки, конфеті, каскад нагород. **Email Banner:** Те саме + підсумок нагород. **Body:** `¡Misión Cuatro completa! Tus premios están acreditados.` |

**Нагороди за кожен депозит:**
| Депозит | FS | CC | Додатково |
|---------|-----|-----|-------|
| 1-й | 10 FS | 50 CC | — |
| 2-й | 15 FS | 75 CC | — |
| 3-й | 20 FS | 100 CC | — |
| 4-й | 30 FS | 200 CC | 50% match up to 3,000 ARS |

---

### Квест 2: Double Chance (Lucky Wheel на вихідних)

**Journey Name:** `10-Q2-DOUBLE-CHANCE`  
**Тригер:** За розкладом (1 вихідний на місяць)

| Комунікація | Campaign ID | Час | Канал | Контент (ES) |
|------|------------|--------|---------|-------------|
| C1 | `10-Q2-C1-EMAIL` | П'ятниця ранок | Email | **Subject:** `🎡 Doble Chance este fin de semana` **Preheader:** `Cada depósito = 2 giros en Lucky Wheel` **Banner Text:** `Doble Chance — Este Fin de Semana`. **Banner Desc:** Візуал Lucky Wheel ×2, атмосфера вечірки вихідних, золоті монети. **Body Desc:** Деталі промо-акції вихідних: кожен депозит = 2 обертання Lucky Wheel, доступно лише Сб-Нд. |
| C2 | `10-Q2-C2-PUSH` | Субота | Push | `Doble Chance está activo. Depositá y girá 2 veces.` |
| C3 | `10-Q2-C3-SMS` | Неділя | SMS | `CuatroBet: Último día de Doble Chance. Depositá y girá 2 veces: {link}` |
| C4 | `10-Q2-C4-EMAIL` | Понеділок | Email | **Subject:** `📊 Tu resumen de Doble Chance` **Preheader:** `Mirá cuántos giros usaste y qué ganaste` **Banner Text:** `Doble Chance — Resumen`. **Banner Desc:** Візуал підсумку — результати Lucky Wheel, загальна кількість обертань. **Body Desc:** Підсумок вихідних: загальна кількість використаних обертань, виграні нагороди, тизер на Double Chance наступного місяця. |

---

### Квест 3: Silver Spin (Рівневе колесо)

**Journey Name:** `10-Q3-SILVER-SPIN`  
**Постійний:** Обертання заробляється на милях ставок

| Комунікація | Campaign ID | Час | Канал | Контент (ES) |
|------|------------|--------|---------|-------------|
| C1 | `10-Q3-C1-PUSH` | На отримання | Push | `¡Ganaste un giro {tier}! Usalo ahora.` |
| C2 | `10-Q3-C2-SMS` | 48 год після отримання | SMS | `CuatroBet: Tu giro {tier} está sin usar. No lo pierdas: {link}` |
| C3 | `10-Q3-C3-PUSH` | 24 год до закінчення | Push | `Tu giro {tier} vence mañana. Usalo: {link}` |
| C4 | `10-Q3-C4-POPUP` | Після обертання | Popup | **Banner Text:** `¡Ganaste {reward}!` **Banner Desc:** Святкування результату Lucky Wheel — колесо рівня {tier} зупиняється на нагороді, анімація блиску, іконка нагороди. **Body:** `¡Giraste y ganaste {reward}!` |

**Рівні:** Silver (2K ставок) / Gold (10K ставок) / Platinum (50K ставок)

---

### Квест 4: Steady Flow (Однакова сума × 4)

**Journey Name:** `10-Q4-STEADY-FLOW`  
**Та сама структура.** Виявлення 4 послідовних депозитів на однакову суму.

### Квест 5: Triple Treat (3 послідовні дні)

**Journey Name:** `10-Q5-TRIPLE-TREAT`  
**3 депозити за 3 послідовні календарні дні.**

### Квест 6: Cuatro Cycle (Opt-In, фіксована сума × 4 за 7 днів) 🔴

**Journey Name:** `10-Q6-CUATRO-CYCLE`  
**Потрібен opt-in.** Гравець обирає рівень: 1,500 / 3,000 / 5,000 / 10,000 ARS.

| Рівень | Нагорода за завершення |
|------|------------------|
| 1,500 × 4 | 50% match on 5th deposit + 20 FS + 200 CC |
| 3,000 × 4 | 75% match + 30 FS + 400 CC |
| 5,000 × 4 | 100% match + 50 FS + 800 CC |
| 10,000 × 4 | 120% match + 75 FS + 1,500 CC + Lucky Wheel entry |

### Квест 7: 4 дні поспіль (Суворіший Cuatro Cycle) 🔴

Як Квест 6, але вимагає 4 послідовні календарні дні. Додати 20% cashback uplift.

### Квест 8: Досягнення обороту в 4 випадкових слотах (Щотижнево) 🔴

**Journey Name:** `10-Q8-SLOT-CHALLENGE`  
**Автоматичне призначення:** Кожного понеділка 4 випадкові слоти (2 з топ-10 + 2 нові/мало-грані).

| Комунікація | Campaign ID | Час | Канал | Контент (ES) |
|------|------------|--------|---------|-------------|
| C1 | `10-Q8-C1-EMAIL-BANNER` | Понеділок ранок | Email + In-app | **Subject:** `🎰 Tu desafío semanal de slots empieza hoy` **Preheader:** `4 slots asignados, premios por completar` **Banner Text:** `Desafío Semanal de Slots`. **Banner Desc:** 4 мініатюри слотів у сітці, значок тижневого виклику, індикатор цілі, захоплий яскравий дизайн. **Body Desc:** Вступ до тижневого виклику: 4 призначених слоти, ціль ставок на кожен слот, нагороди за завершення. |
| C2 | `10-Q8-C2-PUSH` | Середа | Push | `Desafío semanal: {X}/4 slots completados. ¡Seguí!` |
| C3 | `10-Q8-C3-SMS` | П'ятниця | SMS | `CuatroBet: Quedan 2 días para tu desafío semanal: {link}` |
| C4 | `10-Q8-C4-PUSH` | Неділя | Push | `¡Hoy es el último día del desafío! {X}/4 slots. Completalo ahora.` |

---

## D. СИТУАТИВНІ БОНУСИ

### Тижневий бонус (кожної п'ятниці)

**Journey Name:** `10-WB-WEEKLY`  
**Сегмент:** Гравці з ≥1 депозитом за попередні 7 днів. Рівневий перезавантажувальний бонус.

| Комунікація | Campaign ID | Час | Канал | Контент (ES) |
|------|------------|--------|---------|-------------|
| C1 | `10-WB-C1-EMAIL` | П'ятниця 10:00 | Email | **Subject:** `💰 {tier%} + {FS} giros: tu recarga semanal` **Preheader:** `Válido hasta el domingo, no te lo pierdas` **Banner Text:** `Recarga Semanal: {tier%} + {FS} Giros`. **Banner Desc:** Візуал тижневого перезавантаження — тема вечірки п'ятниці, підсвітка суми бонусу, іконки free spins, стрічка "válido hasta domingo". **Body Desc:** Деталі тижневої пропозиції перезавантаження за рівнем гравця: match %, кількість FS, дійсність (до неділі). CTA швидкого депозиту. |
| C2 | `10-WB-C2-PUSH` | П'ятниця вечір | Push | `Tu bono semanal está listo. Activalo ahora.` |
| C3 | `10-WB-C3-SMS` | Субота | SMS | `CuatroBet: Tu recarga semanal + giros gratis. Último día mañana: {link}` |
| C4 | `10-WB-C4-PUSH` | Неділя | Push | `Último día para tu recarga semanal.` |

### Щоденний бонус (серія логінів)

**Journey Name:** `10-DB-DAILY`  
**Механіка:** Послідовні щоденні логіни. Депозит не потрібен.

| Комунікація | Campaign ID | Час | Канал | Контент (ES) |
|------|------------|--------|---------|-------------|
| C1 | `10-DB-C1-PUSH` | Щоранку | Push | `Día {X} de tu racha. Reclamá tu premio diario.` |
| C2 | `10-DB-C2-SMS` | Вечір (якщо не забрано, серія 4+) | SMS | `CuatroBet: Racha de {X} días. No pierdas tu premio: {link}` |
| C3 | `10-DB-C3-EMAIL-POPUP` | День 7 | Email + Popup | **Subject:** `🔥 7 días seguidos — tu premio especial` **Preheader:** `Tu racha de login desbloquea algo grande` **Popup Banner:** Значок серії 7 днів, конфеті, золота іконка досягнення. **Email Banner Text:** `¡7 Días Seguidos!` **Email Banner Desc:** Досягнення серії 7 днів — календар із 7 галочками, спеціальна нагорода розблоковується, золота тема. **Body Desc:** Привітання з серією 7 днів. Деталі спеціальної нагороди. Заохочення продовжувати. |
| C4 | `10-DB-C4-EMAIL` | День після розриву | Email | **Subject:** `😔 Tu racha de {X} días se rompió` **Preheader:** `Empezá de nuevo hoy y recuperá tu progreso` **Banner Text:** `Tu Racha Se Rompió`. **Banner Desc:** Візуал зламаної серії — розірваний ланцюг на календарі, мотиваційна стрілка "почни знову", попередній перегляд нової серії. **Body Desc:** Серію перервано на {X} днях. Заохочення перезапустити з сьогоднішнім логіном як День 1. Попередній перегляд нагороди наступного досягнення. |

### Святкові бонуси (аргентинський календар)

**Journey Name:** `10-HOL-{HOLIDAY_CODE}`  
**Ключові дати:** 25 травня, 9 липня, 12 жовтня, 25 грудня, Карнавал, Великдень тощо.

| Комунікація | Campaign ID | Час | Канал | Контент (ES) |
|------|------------|--------|---------|-------------|
| C1 | `10-HOL-C1-EMAIL` | -7 днів | Email | **Subject:** `🎉 {holiday} se acerca con ofertas especiales` **Preheader:** `Mirá lo que te preparamos para este feriado` **Banner Text:** `Se Acerca {holiday}`. **Banner Desc:** Тизер свята — тематичний візуал для конкретного свята (національні кольори для патріотичних, святкові для Різдва тощо), зворотний відлік "coming soon". **Body Desc:** Свято наближається: попередній перегляд спеціальних пропозицій, дати, чого очікувати. Створення очікування. |
| C2 | `10-HOL-C2-PUSH` | -3 дні | Push | `En 3 días: ofertas de {holiday}. ¡No te lo pierdas!` |
| C3 | `10-HOL-C3-ALL` | День свята | Email + SMS + In-app | **Subject:** `🥳 Feliz {holiday} — tu regalo te espera` **Preheader:** `Abrí tu bono especial de {holiday}` **Email Banner Text:** `¡Feliz {holiday}!` **Email Banner Desc:** Повне святкування — тематичний артворк, святковий декор, підсвітка пропозиції, національні/святкові кольори. **Popup Banner:** Компактний святковий візуал із пропозицією. **Body Desc:** Святкове привітання + деталі бонусу ({offer}). Багатоканальність: email має повний макет, SMS має посилання, in-app popup має компактну версію. |
| C4 | `10-HOL-C4-EMAIL` | +1 день | Email | **Subject:** `⏰ {holiday} — últimas 24h para tu bono` **Preheader:** `Extendimos la oferta un día más, aprovechá` **Banner Text:** `{holiday} — Últimas 24h`. **Banner Desc:** Продовжена святкова пропозиція — та сама святкова тема, але зі зворотним відліком/терміновістю, значок "24h more". **Body Desc:** Нагадування наступного дня: святкову пропозицію продовжено ще на 24 год. Акцент на терміновості. |

---

## ЧЕК-ЛИСТ ТЕСТУВАННЯ

- [ ] Токени лутбоксів нараховуються на правильних порогах ставок (5K слоти / 10K live)
- [ ] Ваги нагород лутбоксів відповідають специфікації
- [ ] Дії наклейок коректно відстежують завершення
- [ ] Завершення ряду наклейок зараховує 200 ARS + 10 FS
- [ ] Квест 1 скидається через 7 днів, якщо не завершений
- [ ] UI opt-in Квесту 6 працює, вибір рівня зберігається
- [ ] Призначення випадкових слотів у Квесті 8 змінюється щотижня
- [ ] Тижневий бонус націлюється на правильний сегмент (депозит за останні 7 днів)
- [ ] Лічильник денної серії коректно збільшується та скидається
- [ ] Святкові кампанії спрацьовують у правильні дати
- [ ] Усі кредити CC, FS, match-бонуси застосовуються правильно
- [ ] Частотні обмеження: квести/гейміфікація ЗВІЛЬНЕНІ від стандартних лімітів (це функції залучення)
