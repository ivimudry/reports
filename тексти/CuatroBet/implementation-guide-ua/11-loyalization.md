# 11 — Лоялізація — Гайд з імплементації

**Ланцюг:** Loyalty Program Engagement (Active vs Passive Members)  
**Пріоритет:** Фаза 3 (Тиждень 7–8)  
**Залежить від:** Система рівнів лояльності активна, відстеження балансу CC

---

## КРОК 0: ПЕРЕДСТАРТОВИЙ ЧЕК-ЛИСТ

- [ ] Система рівнів лояльності налаштована (Standard / Silver / Gold / Platinum / VIP)
- [ ] API нарахування, витрат та балансу CC функціональні
- [ ] Тижневі метрики прогресу доступні (бали, зароблені цього тижня, % прогресу до рівня)
- [ ] Теги підсегментів гравця доступні: `top_game_type` = Slots / Live / Aviator / Mixed
- [ ] Система місій/челенджів готова (або система квестів із Ланцюга 10 може бути повторно використана)
- [ ] Механізм закінчення терміну CC активний (ковзні 90 днів)
- [ ] Подія досягнення рівня спрацьовує, коли гравець перетинає поріг рівня

---

## ВИЗНАЧЕННЯ СЕГМЕНТІВ

### Active Loyalty Member (Активний учасник лояльності)
```
loyalty_enrolled = true
AND last_session_date ≤ 7 days ago
AND (loyalty_points_earned_30d > 0 OR deposits_30d ≥ 1)
```

### Passive Loyalty Member (Пасивний учасник лояльності)
```
loyalty_enrolled = true
AND (last_session_date > 7 days ago OR loyalty_points_earned_30d = 0)
AND account_age > 14 days
```

---

## A. АКТИВНІ УЧАСНИКИ ЛОЯЛЬНОСТІ (4 комунікації)

### AL-C1: Тижневий звіт прогресу (кожного понеділка)

| Налаштування | Значення |
|---------|-------|
| Campaign ID | `11-AL-C1-EMAIL` |
| Канал | Email |
| Тригер | За розкладом, кожного понеділка 10:00 ART |
| Сегмент | Active Loyalty Members |
| Subject (ES) | `📊 {points_earned} puntos esta semana — faltan {points_to_next_tier} para {next_tier}` |

**Вміст емейлу:**

- **Subject (ES):** `📊 {points_earned} puntos esta semana — faltan {points_to_next_tier} para {next_tier}`
- **Preheader (ES):** `Tu resumen semanal de loyalty con progreso detallado`
- **Banner Text (ES):** `Progreso Semanal: {points_earned} Puntos`
- **Banner Description:** Дашборд тижневого прогресу — прогрес-бар до наступного рівня ({progress_pct}%), значок поточного рівня, візуал балансу CC, золота тема прогресу
- **Body Description:** Секція тижневої статистики (зароблені бали, баланс CC, поточний рівень). Візуальний прогрес-бар до наступного рівня. Рекомендація, підлаштована під підсегмент: гравці Slots отримують промо з подвійними балами, гравці Live — пропозицію VIP-столу, Aviator — місію з польотом, Mixed — бонус дослідження.
- **CTA (ES):** `Ver mi progreso` → Дашборд лояльності

---

### AL-C2: Середньотижневий буст (Середа)

| Налаштування | Значення |
|---------|-------|
| Campaign ID | `11-AL-C2-PUSH` |
| Канал | App Push |
| Тригер | За розкладом, середа 14:00 ART |
| Сегмент | Active Loyalty Members |

**Контент (ES):**
```
IF points_this_week < weekly_avg:
  "Vas un poco más lento esta semana. Activá tu boost de puntos: 2x hasta medianoche."
ELSE:
  "¡Gran semana! Ya superaste tu promedio. Seguí así para alcanzar {next_tier}."
```

**Дія:** Зарахувати множник балів 2× дійсний до опівночі, якщо нижче за середнє.

---

### AL-C3: Челендж вихідних (П'ятниця)

| Налаштування | Значення |
|---------|-------|
| Campaign ID | `11-AL-C3-EMAIL-PUSH` |
| Канал | Email + App Push |
| Тригер | За розкладом, п'ятниця 18:00 ART |
| Сегмент | Active Loyalty Members |
| Subject (ES) | `🏆 {challenge_reward}: desafío de fin de semana` |

**Вміст емейлу:**
- **Subject (ES):** `🏆 {challenge_reward}: desafío de fin de semana`
- **Preheader (ES):** `Completá el reto y ganá premios exclusivos`
- **Banner Text (ES):** `Desafío de Fin de Semana`
- **Banner Description:** Запуск челенджу вихідних — іконка трофею, візуал типу челенджу (ротація щотижня), попередній перегляд нагороди, яскраві кольори вечірки вихідних, орієнтований на дію дизайн
- **Body Description:** Деталі ротаційного челенджу цих вихідних (ставки/різноманітність ігор/множник/серія депозитів). Розбивка нагород. Підлаштування під підсегмент: цілі по слотах vs live vs aviator.
| Тиждень | Челендж | Нагорода |
|------|-----------|--------|
| 1 | Поставити 15,000 ARS цих вихідних | 500 CC + 10 FS |
| 2 | Зіграти в 3 різні типи ігор | 300 CC + 15 FS |
| 3 | Виграти 5× ставку хоча б раз | 400 CC + Lucky Wheel spin |
| 4 | Депозит кожного дня Пт-Нд | 600 CC + 20 FS |

**Підлаштування під підсегмент:**
- Гравці Slots: челендж спрямований на досягнення у слотах
- Гравці Live: цілі ставок за live-столами
- Aviator: кількість польотів / цілі множника

---

### AL-C4: Досягнення рівня (на подію)

| Налаштування | Значення |
|---------|-------|
| Campaign ID | `11-AL-C4-ALL` |
| Канал | In-app popup + Email + Push |
| Тригер | Подія: `loyalty_tier_change` |
| Сегмент | Active Loyalty Members |

**Popup (ES):**
- **Banner Text (ES):** `¡Subiste a {new_tier}!`
- **Banner Description:** Святкування підвищення рівня — новий значок рівня на видному місці, блиск/конфеті, старий рівень зникає вгору в новий рівень, іконки переваг у попередньому перегляді, розкішна золото-фіолетова тема
- **Body (ES):** `¡Felicitaciones! Subiste a {new_tier}. Tus nuevos beneficios: Cashback {cashback_pct}%, {monthly_fs} giros mensuales, Soporte {support_level}.`
- **CTA (ES):** `Ver mis beneficios` → Дашборд лояльності

**Email:**
- **Subject (ES):** `👑 Bienvenido a {new_tier} — nuevos beneficios`
- **Preheader (ES):** `Descubrí todo lo que incluye tu nuevo nivel`
- **Banner Text (ES):** `Bienvenido a {new_tier}`
- **Banner Description:** Повне вітання з рівнем — значок нового рівня як головний елемент, тизер таблиці порівняння переваг, розкішний візуал підвищення, святкова золото-фіолетова тема
- **Body Description:** Повне вітання з переходом на новий рівень із таблицею порівняння переваг (cashback%, місячні FS, бонус CC%, рівень підтримки). Порівняння старого та нового рівня. CTA до дашборду лояльності.

**Переваги рівнів:**
| Рівень | Cashback | Місячні FS | CC Бонус | Підтримка |
|------|----------|-----------|----------|---------|
| Silver | 5% | 10 | +10% | Standard |
| Gold | 8% | 25 | +15% | Priority |
| Platinum | 12% | 50 | +25% | Dedicated |
| VIP | 15% | 100 | +40% | Personal manager |

---

## B. ПАСИВНІ УЧАСНИКИ ЛОЯЛЬНОСТІ (4 комунікації)

### PL-C1: Поштовх до повернення (Тригер: 8 днів неактивності)

| Налаштування | Значення |
|---------|-------|
| Campaign ID | `11-PL-C1-SMS-EMAIL` |
| Канал | SMS + Email |
| Тригер | `last_session_date > 8 days` AND `loyalty_enrolled = true` |
| Сегмент | Passive Loyalty Members |

**SMS (ES):**
```
CuatroBet: Hace {days} días que no te vemos. Tus {cc_balance} CC te esperan. Entrá hoy y ganá puntos dobles: {link}
```

**Email:**
- **Subject (ES):** `👋 {cc_balance} Cuatro Coins te esperan`
- **Preheader (ES):** `Hoy ganás puntos dobles si volvés a jugar`
- **Banner Text (ES):** `{cc_balance} CC Te Esperan`
- **Banner Description:** Поверненння до гри — купа Cuatro Coins, що світиться, з числом "{cc_balance}" на видному місці, натяк на прогрес-бар рівня, значок балів 2×, теплі привітні тони
- **Body Description:** Показати баланс CC на видному місці. Показати близькість до наступного рівня. Оголосити 2× бали активні на 48 год. М'який тон повернення.
- **CTA (ES):** `Volver a jugar` → Головна сторінка

---

### PL-C2: Пропозиція легкої місії (T+3 дні після C1)

| Налаштування | Значення |
|---------|-------|
| Campaign ID | `11-PL-C2-EMAIL` |
| Канал | Email |
| Умова | НЕ залогінився після C1 |
| Subject (ES) | `🎯 200 CC + 10 giros: misión fácil de 1 depósito` |

**Вміст емейлу:**
- **Subject (ES):** `🎯 200 CC + 10 giros: misión fácil de 1 depósito`
- **Preheader (ES):** `Solo un depósito y los premios son tuyos`
- **Banner Text (ES):** `Misión Fácil: 200 CC + 10 Giros`
- **Banner Description:** Легка місія — іконка одного депозиту, візуал низького бар'єру, попередній перегляд нагороди 200 CC + 10 FS, значок "тільки 1 депозит", заохочувальні зелено-золоті тони
- **Body Description:** Проста пропозиція: 1 депозит від {min_deposit} ARS = 200 CC + 10 FS. Дійсний 48 год. Мінімальні суми депозитів за рівнем.

**Мінімальний депозит за рівнем:**
| Рівень | Мін. депозит |
|------|------------|
| Standard | 1,000 ARS |
| Silver | 1,500 ARS |
| Gold | 2,000 ARS |
| Platinum | 3,000 ARS |

---

### PL-C3: Попередження про закінчення терміну CC (за 30 днів до закінчення)

| Налаштування | Значення |
|---------|-------|
| Campaign ID | `11-PL-C3-EMAIL-PUSH` |
| Канал | Email + Push |
| Тригер | `cc_expiry_date - 30 days` |
| Сегмент | Passive Loyalty Members з балансом CC > 0 |

**Push (ES):**
```
Tus {cc_balance} Cuatro Coins vencen en 30 días. Usalos o perdelos.
```

**Email:**
- **Subject (ES):** `⚠️ {cc_balance} CC vencen el {expiry_date}`
- **Preheader (ES):** `Canjeálos antes de que desaparezcan para siempre`
- **Banner Text (ES):** `{cc_balance} CC Vencen Pronto`
- **Banner Description:** Попередження про закінчення терміну — баланс CC, що зникає/розчиняється, таймер зворотного відліку до {expiry_date}, іконки опцій обміну (FS, готівка, Lucky Wheel), бурштинові тони терміновості
- **Body Description:** Баланс CC зі зворотним відліком до дати закінчення. Опції обміну: FS, бонусна готівка, входи на Lucky Wheel. Акцент на терміновості.
- **CTA (ES):** `Canjear mis CC` → Магазин CC

---

### PL-C4: Останній шанс (за 7 днів до закінчення CC)

| Налаштування | Значення |
|---------|-------|
| Campaign ID | `11-PL-C4-SMS-PUSH` |
| Канал | SMS + Push |
| Тригер | `cc_expiry_date - 7 days` |
| Умова | Баланс CC досі > 0 ТА немає логіну після C3 |

**SMS (ES):**
```
CuatroBet: ÚLTIMA OPORTUNIDAD. Tus {cc_balance} CC vencen en 7 días. Canjalos ahora: {link}
```

**Push (ES):**
```
⏰ 7 días para canjear tus {cc_balance} CC. No los pierdas.
```

**Підсилювач:** Додати +100 CC бонус, якщо залогіниться та обміняє протягом 48 год.

---

## УМОВИ ВИХОДУ

| Умова | Дія |
|-----------|--------|
| Active → логін протягом 7 днів після комунікації | Залишається в Active flow, скидання таймерів |
| Active → підвищення рівня | Спрацьовує AL-C4, скидання тижневого циклу |
| Passive → логін після C1 або C2 | Перехід до Active flow |
| Passive → обмін CC після C3/C4 | Перехід до Active flow |
| Passive → CC закінчуються без дії | Прибрати з комунікацій лояльності, перехід до Ланцюга 12 (Reactivation) |

---

## ЧЕК-ЛИСТ ТЕСТУВАННЯ

- [ ] Сегмент Active коректно включає лише учасників лояльності, активних 7 днів
- [ ] Сегмент Passive коректно виключає не-учасників лояльності
- [ ] Тижневий емейл прогресу показує правильний баланс CC, прогрес рівня
- [ ] Підлаштування під підсегмент (Slots/Live/Aviator/Mixed) відображає правильний контент
- [ ] Середньотижневий буст коректно застосовує множник 2×
- [ ] Челенджі вихідних ротуються щотижня (цикл 4 тижні)
- [ ] Досягнення рівня спрацьовує негайно при події підвищення
- [ ] Таблиця переваг рівнів відповідає конфігурації
- [ ] Попередження про закінчення CC спрацьовує рівно за 30 днів
- [ ] Останній шанс спрацьовує рівно за 7 днів
- [ ] Підсилювач +100 CC зараховується лише при логіні протягом 48 год
- [ ] Перехід Passive → Active працює (гравець переходить між потоками)
- [ ] Немає дублювання комунікацій при переході в середині тижня

---

## ЦІЛЬОВІ KPI

| Метрика | Ціль |
|--------|--------|
| Open rate тижневого емейлу Active loyalty | ≥ 35% |
| Логін Passive протягом 48 год після повернення (C1) | ≥ 15% |
| Частка обміну CC до закінчення (C3+C4) | ≥ 40% |
| Частка підвищення рівня (щомісячно) | ≥ 8% від Active |
| Завершення челенджу вихідних | ≥ 25% |
