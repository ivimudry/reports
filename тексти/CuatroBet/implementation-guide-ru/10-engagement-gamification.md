# 10 — Вовлечение и Геймификация — Руководство по внедрению

**Цепочка:** Вовлечение (Лутбоксы, Стикеры, 8 Квестов, Еженедельные/Ежедневные/Праздничные бонусы)  
**Приоритет:** Фаза 3 (Неделя 7–8)  
**Это самая крупная цепочка — разбивается на подпроекты ниже**

---

## ШАГ 0: ПРЕДСТАРТОВЫЙ ЧЕК-ЛИСТ

- [ ] API начисления/списания CC (Cuatro Coins) работает
- [ ] Система Lucky Wheel активна с уровнями Silver/Gold/Platinum
- [ ] Каналы In-app popup и App Push активны
- [ ] UI лутбокса готов в личном кабинете игрока
- [ ] UI книги стикеров готов (сетка на 30 слотов)
- [ ] API отслеживания прогресса квестов доступен
- [ ] Сумма ставок отслеживается по типу игры в реальном времени
- [ ] Отслеживание логинов для функции ежедневной серии
- [ ] Календарь аргентинских праздников настроен на год

---

## A. ЛУТБОКСЫ

**Название Journey:** `10-LB-JOURNEY`  
**Тип:** По событию (постоянный)  
**Вход:** `total_wagered_ars` достигает следующего порога в 5 000 ARS (слоты) или 10 000 ARS (лайв)

### Правила начисления:
- 1 токен лутбокса за каждые 5 000 ARS ставок на слотах
- 1 токен лутбокса за каждые 10 000 ARS ставок в лайве
- Токены накапливаются в личном кабинете, открываются вручную

### Таблица наград:

| Награда | Вес | Значение |
|---------|-----|----------|
| Малый подарок CC | 50% | 25–50 CC |
| Free Spins (5–10) | 25% | На топ-слоте игрока |
| Бонусные деньги | 15% | 500–1 000 ARS |
| Вход в Lucky Wheel | 7% | 1 Silver вход |
| Премиум FS (25+) | 3% | На премиум-тайтлах |

### Создать 4 коммуникации:

**LB-C1: Токен получен (по событию)**
| Параметр | Значение |
|----------|----------|
| Campaign ID | `10-LB-C1-PUSH` |
| Канал | App Push |
| Текст (ES) | `¡Ganaste un loot box! Abrilo desde tu panel.` |
| CTA | Deep link на панель лутбоксов |

**LB-C2: Лутбокс открыт (по событию)**
| Параметр | Значение |
|----------|----------|
| Campaign ID | `10-LB-C2-POPUP` |
| Канал | In-app popup |
| **Текст баннера (ES)** | `¡Loot Box Abierto!` |
| **Описание баннера** | Celebration loot box opening — glowing box bursting open, reward icon revealed ({reward}), sparkle/confetti animation, golden light rays |
| **Тело (ES)** | `{reward} desbloqueado. ¡Seguí jugando para más!` |

**LB-C3: Еженедельное напоминание о неоткрытых (понедельник)**
| Параметр | Значение |
|----------|----------|
| Campaign ID | `10-LB-C3-EMAIL` |
| Канал | Email |
| **Тема (ES)** | `🎁 {count} loot boxes sin abrir te esperan` |
| **Прехедер (ES)** | `Descubrí qué hay adentro antes de que expiren` |
| **Текст баннера (ES)** | `{count} Loot Boxes Sin Abrir` |
| **Описание баннера** | Mystery loot boxes — stack of glowing unopened boxes, question marks floating, treasure hint, exciting blue/purple tones |
| **Описание тела** | Напоминание о неоткрытых лутбоксах с тизером загадки. Список возможных наград. Одна CTA на личный кабинет. |
| Условие | У игрока ≥1 неоткрытый лутбокс |
| **CTA (ES)** | `Abrir ahora` → личный кабинет |

**LB-C4: Ежемесячная сводка (1-е число месяца)**
| Параметр | Значение |
|----------|----------|
| Campaign ID | `10-LB-C4-EMAIL` |
| Канал | Email |
| **Тема (ES)** | `📊 Tu resumen mensual de loot boxes` |
| **Прехедер (ES)** | `Mirá todo lo que ganaste este mes` |
| **Текст баннера (ES)** | `Resumen Mensual de Loot Boxes` |
| **Описание баннера** | Monthly recap visual — opened loot boxes collage, reward summary icons, comparison chart (vs last month), celebratory purple/gold theme |
| **Описание тела** | Ежемесячная статистика лутбоксов: открыто коробок, общая сумма наград, сравнение с прошлым месяцем, тизер на следующий месяц. |

---

## B. СТИКЕРЫ

**Название Journey:** `10-STK-JOURNEY`  
**Механика:** Книга стикеров на 30 слотов. Определённые действия открывают стикеры. Ряд из 5 = награда. Все 30 = главный приз.

### Действия для стикеров (примеры — настроить 30):
| Стикер | Требуемое действие |
|--------|-------------------|
| #1 | Сыграть в Jackpot Joker 10 раз |
| #2 | Внести депозит 3 дня подряд |
| #3 | Попробовать нового провайдера игр |
| #4 | Поставить 10 000 ARS за неделю |
| #5 | Выиграть 5× от ставки за один спин |
| ... | (Определить оставшиеся 25) |

### Уровни наград:
| Веха | Награда |
|------|---------|
| Одиночный стикер | 25 CC |
| Полный ряд из 5 | 200 ARS + 10 FS |
| Все 30 собраны | 10 000 ARS + Premium Lucky Wheel + превью VIP I |

### Создать 4 коммуникации:

**STK-C1: Стикер разблокирован**
| Campaign ID | `10-STK-C1-PUSH` |
|------------|-------------------|
| Канал | App Push |
| Текст (ES) | `Nueva figurita desbloqueada: {sticker_name}. ¡Seguí coleccionando!` |

**STK-C2: Один стикер до завершения ряда**
| Campaign ID | `10-STK-C2-EMAIL` |
|------------|---------------------|
| Канал | Email |
| **Тема (ES)** | `🧩 200 ARS + 10 giros: te falta 1 figurita` |
| **Прехедер (ES)** | `Completá la fila y ganate el premio` |
| **Текст баннера (ES)** | `¡Te Falta 1 Figurita!` |
| **Описание баннера** | Almost-complete sticker row — 4/5 sticker slots filled, last slot glowing/pulsing with question mark, 200 ARS + 10 FS reward preview, exciting urgency |
| **Описание тела** | Подсветить, какой стикер не хватает и какое действие его открывает. Показать превью награды: 200 ARS + 10 FS. Чёткая CTA на выполнение действия. |
| Условие | Собрано 4 из 5 стикеров в ряду |

**STK-C3: Ряд завершён**
| Campaign ID | `10-STK-C3-PUSH-POPUP` |
|------------|--------------------------|
| Канал | App Push + In-app popup |
| **Текст баннера (ES)** | `¡Fila Completa!` |
| **Описание баннера** | Celebration row complete — 5/5 stickers glowing, reward burst animation (200 ARS + 10 FS), confetti, golden completion badge |
| **Тело (ES)** | `¡Fila completa! Ganaste 200 ARS + 10 giros gratis.` |
| Действие | Начислить 200 ARS + 10 FS |

**STK-C4: Ежемесячная сводка**
| Campaign ID | `10-STK-C4-EMAIL` |
|------------|---------------------|
| Канал | Email |
| **Тема (ES)** | `📈 {count} figuritas este mes — faltan {remaining}` |
| **Прехедер (ES)** | `El gran premio de 10,000 ARS está cada vez más cerca` |
| **Текст баннера (ES)** | `{count} Figuritas Coleccionadas` |
| **Описание баннера** | Monthly sticker progress — sticker book grid showing filled/empty slots, progress bar to 30, grand prize preview (10,000 ARS + VIP), collector theme |
| **Описание тела** | Ежемесячный отчёт по стикерам: собрано, осталось до главного приза, подсказка по следующему достижимому стикеру, мотивация. |

---

## C. КВЕСТЫ (8 типов квестов)

### Квест 1: Квест на 4 депозита ("Misión Cuatro")

**Название Journey:** `10-Q1-MISSION-CUATRO`  
**Автоматическая регистрация:** При FTD  
**Окно:** 7 скользящих дней  
**Награды:** Возрастающие за каждый депозит (см. спецификацию)

| Касание | Campaign ID | Время | Канал | Контент (ES) |
|---------|------------|-------|-------|-------------|
| C1 | `10-Q1-C1-POPUP-EMAIL` | При FTD | Popup + Email | **Popup Banner:** Активация квеста — логотип "Misión Cuatro", прогресс-бар на 4 шага, превью первой награды. **Email Banner:** То же. **Тело:** `¡Misión Cuatro activada! 4 depósitos en 7 días = premios increíbles.` |
| C2 | `10-Q1-C2-PUSH` | После 2-го депозита | App Push | `¡Vas por la mitad! 2 depósitos más para completar la Misión Cuatro.` |
| C3 | `10-Q1-C3-SMS` | После 3-го депозита | SMS | `CuatroBet: ¡Falta 1 depósito para ganar 30 giros + 200 CC + bono 50%! {link}` |
| C4 | `10-Q1-C4-POPUP-EMAIL` | После 4-го депозита | Popup + Email | **Popup Banner:** Миссия выполнена — 4/4 галочки, конфетти, каскад наград. **Email Banner:** То же + сводка наград. **Тело:** `¡Misión Cuatro completa! Tus premios están acreditados.` |

**Награды за каждый депозит:**
| Депозит | FS | CC | Дополнительно |
|---------|-----|-----|---------------|
| 1-й | 10 FS | 50 CC | — |
| 2-й | 15 FS | 75 CC | — |
| 3-й | 20 FS | 100 CC | — |
| 4-й | 30 FS | 200 CC | 50% матч до 3 000 ARS |

---

### Квест 2: Double Chance (Еженедельный Lucky Wheel)

**Название Journey:** `10-Q2-DOUBLE-CHANCE`  
**Триггер:** По расписанию (1 выходные в месяц)

| Касание | Campaign ID | Время | Канал | Контент (ES) |
|---------|------------|-------|-------|-------------|
| C1 | `10-Q2-C1-EMAIL` | Пятница утро | Email | **Тема:** `🎡 Doble Chance este fin de semana` **Прехедер:** `Cada depósito = 2 giros en Lucky Wheel` **Текст баннера:** `Doble Chance — Este Fin de Semana`. **Описание баннера:** Lucky Wheel ×2 visual, weekend party vibe, golden coins. **Описание тела:** Детали промо на выходные: каждый депозит = 2 вращения Lucky Wheel, доступно только Сб-Вс. |
| C2 | `10-Q2-C2-PUSH` | Суббота | Push | `Doble Chance está activo. Depositá y girá 2 veces.` |
| C3 | `10-Q2-C3-SMS` | Воскресенье | SMS | `CuatroBet: Último día de Doble Chance. Depositá y girá 2 veces: {link}` |
| C4 | `10-Q2-C4-EMAIL` | Понедельник | Email | **Тема:** `📊 Tu resumen de Doble Chance` **Прехедер:** `Mirá cuántos giros usaste y qué ganaste` **Текст баннера:** `Doble Chance — Resumen`. **Описание баннера:** Recap visual — Lucky Wheel results, total spins count. **Описание тела:** Итоги выходных: всего использовано вращений, выигранные награды, тизер на Double Chance следующего месяца. |

---

### Квест 3: Silver Spin (Уровневое колесо)

**Название Journey:** `10-Q3-SILVER-SPIN`  
**Постоянный:** Вращение зарабатывается на вехах по ставкам

| Касание | Campaign ID | Время | Канал | Контент (ES) |
|---------|------------|-------|-------|-------------|
| C1 | `10-Q3-C1-PUSH` | При получении | Push | `¡Ganaste un giro {tier}! Usalo ahora.` |
| C2 | `10-Q3-C2-SMS` | 48ч после получения | SMS | `CuatroBet: Tu giro {tier} está sin usar. No lo pierdas: {link}` |
| C3 | `10-Q3-C3-PUSH` | 24ч до истечения | Push | `Tu giro {tier} vence mañana. Usalo: {link}` |
| C4 | `10-Q3-C4-POPUP` | После вращения | Popup | **Текст баннера:** `¡Ganaste {reward}!` **Описание баннера:** Lucky Wheel result celebration — {tier} wheel stopping on reward, sparkle animation, reward icon. **Тело:** `¡Giraste y ganaste {reward}!` |

**Уровни:** Silver (2K ставок) / Gold (10K ставок) / Platinum (50K ставок)

---

### Квест 4: Steady Flow (Одинаковая сумма × 4)

**Название Journey:** `10-Q4-STEADY-FLOW`  
**Та же структура, что и выше.** Определяет 4 последовательных депозита одинаковой суммы.

### Квест 5: Triple Treat (3 последовательных дня)

**Название Journey:** `10-Q5-TRIPLE-TREAT`  
**3 депозита за 3 последовательных календарных дня.**

### Квест 6: Cuatro Cycle (Opt-In, фиксированная сумма × 4 за 7 дней) 🔴

**Название Journey:** `10-Q6-CUATRO-CYCLE`  
**Требуется Opt-in.** Игрок выбирает уровень: 1 500 / 3 000 / 5 000 / 10 000 ARS.

| Уровень | Награда за завершение |
|---------|----------------------|
| 1 500 × 4 | 50% матч на 5-й депозит + 20 FS + 200 CC |
| 3 000 × 4 | 75% матч + 30 FS + 400 CC |
| 5 000 × 4 | 100% матч + 50 FS + 800 CC |
| 10 000 × 4 | 120% матч + 75 FS + 1 500 CC + вход в Lucky Wheel |

### Квест 7: 4 дня подряд (Строгий Cuatro Cycle) 🔴

То же, что и Квест 6, но требует 4 последовательных календарных дня. Добавить 20% повышение кэшбэка.

### Квест 8: Достичь оборота в 4 случайных слотах (еженедельно) 🔴

**Название Journey:** `10-Q8-SLOT-CHALLENGE`  
**Автоматическое назначение:** Каждый понедельник, 4 случайных слота (2 из топ-10 + 2 новых/малоиграемых).

| Касание | Campaign ID | Время | Канал | Контент (ES) |
|---------|------------|-------|-------|-------------|
| C1 | `10-Q8-C1-EMAIL-BANNER` | Понедельник утро | Email + In-app | **Тема:** `🎰 Tu desafío semanal de slots empieza hoy` **Прехедер:** `4 slots asignados, premios por completar` **Текст баннера:** `Desafío Semanal de Slots`. **Описание баннера:** 4 slot game thumbnails in grid, weekly challenge badge, target indicator, exciting vibrant design. **Описание тела:** Вступление к еженедельному челленджу: 4 назначенных слота, цель по ставкам на каждый, награды за выполнение. |
| C2 | `10-Q8-C2-PUSH` | Среда | Push | `Desafío semanal: {X}/4 slots completados. ¡Seguí!` |
| C3 | `10-Q8-C3-SMS` | Пятница | SMS | `CuatroBet: Quedan 2 días para tu desafío semanal: {link}` |
| C4 | `10-Q8-C4-PUSH` | Воскресенье | Push | `¡Hoy es el último día del desafío! {X}/4 slots. Completalo ahora.` |

---

## D. СИТУАЦИОННЫЕ БОНУСЫ

### Еженедельный бонус (каждую пятницу)

**Название Journey:** `10-WB-WEEKLY`  
**Сегмент:** Игроки с ≥1 депозитом за последние 7 дней. Уровневый перезагруз.

| Касание | Campaign ID | Время | Канал | Контент (ES) |
|---------|------------|-------|-------|-------------|
| C1 | `10-WB-C1-EMAIL` | Пятница 10:00 | Email | **Тема:** `💰 {tier%} + {FS} giros: tu recarga semanal` **Прехедер:** `Válido hasta el domingo, no te lo pierdas` **Текст баннера:** `Recarga Semanal: {tier%} + {FS} Giros`. **Описание баннера:** Weekly reload visual — Friday party theme, bonus amount highlight, free spins icons, "válido hasta domingo" ribbon. **Описание тела:** Детали еженедельного перезагруза по уровню игрока: % матча, кол-во FS, срок действия (до воскресенья). Быстрая CTA на депозит. |
| C2 | `10-WB-C2-PUSH` | Пятница вечер | Push | `Tu bono semanal está listo. Activalo ahora.` |
| C3 | `10-WB-C3-SMS` | Суббота | SMS | `CuatroBet: Tu recarga semanal + giros gratis. Último día mañana: {link}` |
| C4 | `10-WB-C4-PUSH` | Воскресенье | Push | `Último día para tu recarga semanal.` |

### Ежедневный бонус (серия логинов)

**Название Journey:** `10-DB-DAILY`  
**Механика:** Последовательные ежедневные логины. Депозит не требуется.

| Касание | Campaign ID | Время | Канал | Контент (ES) |
|---------|------------|-------|-------|-------------|
| C1 | `10-DB-C1-PUSH` | Ежедневно утро | Push | `Día {X} de tu racha. Reclamá tu premio diario.` |
| C2 | `10-DB-C2-SMS` | Вечер (если не забрано, серия 4+) | SMS | `CuatroBet: Racha de {X} días. No pierdas tu premio: {link}` |
| C3 | `10-DB-C3-EMAIL-POPUP` | День 7 | Email + Popup | **Тема:** `🔥 7 días seguidos — tu premio especial` **Прехедер:** `Tu racha de login desbloquea algo grande` **Popup Banner:** Бейдж 7-дневной серии, конфетти, золотая иконка вехи. **Текст баннера Email:** `¡7 Días Seguidos!` **Описание баннера Email:** 7-day streak milestone — calendar with 7 checkmarks, special reward unlocking, gold theme. **Описание тела:** Поздравление с 7-дневной серией. Детали специальной награды. Мотивация продолжать. |
| C4 | `10-DB-C4-EMAIL` | День после обрыва | Email | **Тема:** `😔 Tu racha de {X} días se rompió` **Прехедер:** `Empezá de nuevo hoy y recuperá tu progreso` **Текст баннера:** `Tu Racha Se Rompió`. **Описание баннера:** Broken streak visual — calendar chain broken, motivational "start again" arrow, new streak preview. **Описание тела:** Серия оборвалась на {X} днях. Мотивация начать заново: сегодняшний логин = День 1. Превью награды за следующую веху. |

### Праздничные бонусы (аргентинский календарь)

**Название Journey:** `10-HOL-{HOLIDAY_CODE}`  
**Ключевые даты:** 25 мая, 9 июля, 12 октября, 25 декабря, Карнавал, Пасха и т.д.

| Касание | Campaign ID | Время | Канал | Контент (ES) |
|---------|------------|-------|-------|-------------|
| C1 | `10-HOL-C1-EMAIL` | −7 дней | Email | **Тема:** `🎉 {holiday} se acerca con ofertas especiales` **Прехедер:** `Mirá lo que te preparamos para este feriado` **Текст баннера:** `Se Acerca {holiday}`. **Описание баннера:** Holiday teaser — themed visual for specific holiday (national colors for patriotic, festive for Christmas, etc.), "coming soon" countdown. **Описание тела:** Приближается праздник: превью специальных предложений, даты, чего ожидать. Создание ожидания. |
| C2 | `10-HOL-C2-PUSH` | −3 дня | Push | `En 3 días: ofertas de {holiday}. ¡No te lo pierdas!` |
| C3 | `10-HOL-C3-ALL` | День праздника | Email + SMS + In-app | **Тема:** `🥳 Feliz {holiday} — tu regalo te espera` **Прехедер:** `Abrí tu bono especial de {holiday}` **Текст баннера Email:** `¡Feliz {holiday}!` **Описание баннера Email:** Full holiday celebration — themed artwork, festive decorations, offer highlight, national/festive colors. **Popup Banner:** Condensed holiday visual with offer. **Описание тела:** Праздничное поздравление + детали бонуса ({offer}). Мультиканал: email — полный макет, SMS — ссылка, in-app popup — сокращённая версия. |
| C4 | `10-HOL-C4-EMAIL` | +1 день | Email | **Тема:** `⏰ {holiday} — últimas 24h para tu bono` **Прехедер:** `Extendimos la oferta un día más, aprovechá` **Текст баннера:** `{holiday} — Últimas 24h`. **Описание баннера:** Extended holiday offer — same holiday theme but with countdown/urgency, "24h more" badge. **Описание тела:** Напоминание на следующий день: праздничное предложение продлено ещё на 24ч. Акцент на срочности. |

---

## ЧЕК-ЛИСТ ТЕСТИРОВАНИЯ

- [ ] Токены лутбоксов начисляются при правильных порогах ставок (5K слоты / 10K лайв)
- [ ] Веса наград лутбоксов соответствуют спецификации
- [ ] Действия для стикеров корректно отслеживают выполнение
- [ ] Завершение ряда стикеров начисляет 200 ARS + 10 FS
- [ ] Квест 1 сбрасывается через 7 дней, если не завершён
- [ ] UI opt-in Квеста 6 работает, выбор уровня сохраняется
- [ ] Назначение случайных слотов в Квесте 8 меняется еженедельно
- [ ] Еженедельный бонус нацелен на правильный сегмент (депозит за последние 7 дней)
- [ ] Счётчик ежедневной серии корректно увеличивается и сбрасывается
- [ ] Праздничные кампании запускаются в правильные даты
- [ ] Все начисления CC, FS, бонусы матча применяются корректно
- [ ] Лимиты частоты: квесты/геймификация ИСКЛЮЧЕНЫ из стандартных ограничений (это функции вовлечения)
