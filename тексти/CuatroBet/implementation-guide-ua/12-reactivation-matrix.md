# 12 — Матриця реактивації — Гайд з імплементації

**Ланцюг:** Reactivation (2 типи історії залучення × 3 часові бакети × 4 комунікації + Value Tier Overlay + VNR спеціальний кейс)  
**Пріоритет:** Фаза 2 (Тиждень 5–6)  
**Загальна кількість базових комунікацій:** 24 + 4 (VNR) = 28 комунікацій  
**Залежить від:** Predective Churn модель, сегментація за рівнем цінності, всі канали активні

---

## КРОК 0: ПЕРЕДСТАРТОВИЙ ЧЕК-ЛИСТ

- [ ] Predictive Churn модель активна (ранній вхід на день 3–4 для високоризикових)
- [ ] Рівні цінності гравців сегментовані: Micro / Low / Mid / High / Pre-VIP+
- [ ] Фільтр поведінкового залучення доступний: High / Low / Zero engagement
- [ ] Усі канали активні: SMS, Email, In-app popup, Push, Feed
- [ ] Шаблони бонусів реактивації налаштовані (див. Секцію F)
- [ ] Deep link на сторінку депозиту функціональний
- [ ] API подарунків/ручного кредитування доступний для ескалаційних пропозицій

---

## СТРУКТУРА МАТРИЦІ

```
              │  7-Day Dormant  │ 14-Day Dormant │ 21+ Day Dormant │
──────────────┼─────────────────┼────────────────┼─────────────────│
Active History│  4 comms        │  4 comms       │  4 comms        │
──────────────┼─────────────────┼────────────────┼─────────────────│
Passive Hist. │  4 comms        │  4 comms       │  4 comms        │
──────────────┴─────────────────┴────────────────┴─────────────────┘
                                + VNR Special Case (4 comms)
                                + Value Tier Overlay (multiplier)
                                + Behavioral Filter Overlay
```

---

## ВИЗНАЧЕННЯ СЕГМЕНТІВ

### Історія залучення

**Active History (AH) — Активна історія:**
```
deposit_count ≥ 3
AND total_wagered_ars ≥ 15,000 ARS
AND sessions_30d_before_dormancy ≥ 5
```

**Passive History (PH) — Пасивна історія:**
```
deposit_count < 3
OR total_wagered_ars < 15,000 ARS
OR sessions_30d_before_dormancy < 5
```

### Часові бакети (від останнього логіну)

| Бакет | Вхід | Опис |
|--------|-------|-------------|
| 7-Day | `last_login` 7–13 днів тому | Рання неактивність |
| 14-Day | `last_login` 14–20 днів тому | Середня неактивність |
| 21+ Day | `last_login` ≥ 21 днів тому | Глибока неактивність |

### Value Tier Overlay (коригує суми пропозицій)

| Рівень цінності | Діапазон депозитів (за весь час) | Множник пропозиції |
|-----------|--------------------------|-----------------|
| Micro | < 5,000 ARS | 0.5× |
| Low | 5,000–25,000 ARS | 1× (базовий) |
| Mid | 25,001–75,000 ARS | 1.5× |
| High | 75,000–200,000 ARS | 2× |
| Pre-VIP+ | > 200,000 ARS | 3× (+ персональний контакт) |

### Behavioral Filter Overlay (поведінковий фільтр)

| Фільтр | Визначення | Коригування каналу |
|--------|-----------|-------------------|
| High engagement | Відкрив ≥3 комунікації за останні 30 активних днів | Використовувати email + push |
| Low engagement | Відкрив 1–2 комунікації за останні 30 активних днів | Починати з SMS |
| Zero engagement | Відкрив 0 комунікацій за останні 30 активних днів | Лише SMS, потім телефонний дзвінок для High+ цінності |

---

## A. ACTIVE HISTORY — 7-DAY DORMANT

**Journey Name:** `12-AH-7D-JOURNEY`  
**Вхід:** `last_session_date > 7 days` AND Active History = true AND прапор Predictive Churn опціональний (може увійти на день 3–4)

### AH-7D-C1: М'яка перевірка (День 7 або тригер прогнозу відтоку)

| Налаштування | Значення |
|---------|-------|
| Campaign ID | `12-AH-7D-C1-EMAIL` |
| Канал | Email (High/Low engagement) або SMS (Zero engagement) |
| Subject (ES) | `🔔 {first_name}, algo nuevo te espera` |

**Вміст емейлу:**
- **Subject (ES):** `🔔 {first_name}, algo nuevo te espera`
- **Preheader (ES):** `Descubrí qué cambió desde tu última visita`
- **Banner Text (ES):** `Algo Nuevo Te Espera`
- **Banner Description:** М'яка перевірка — персоналізований візуал рекомендації гри, значок cashback, дружній тон "ми помітили, що тебе не було", теплі привітні кольори
- **Body Description:** М'яке залучення (без бонусу поки що). Показати персоналізовану рекомендацію гри з новими функціями. Нагадати про активний cashback. Дружнє повідомлення "твій акаунт чекає".
- **CTA (ES):** `Ver novedades` → Головна сторінка

---

### AH-7D-C2: Легкий стимул (День 9)

| Налаштування | Значення |
|---------|-------|
| Campaign ID | `12-AH-7D-C2-PUSH-SMS` |
| Канал | Push (High engagement) / SMS (Low/Zero) |
| Умова | Немає логіну після C1 |

**SMS (ES):**
```
CuatroBet: {first_name}, tenés {free_spins_count} giros gratis esperándote. Válidos 48h: {link}
```

**Базова пропозиція:** 10 FS (× множник рівня цінності)

---

### AH-7D-C3: Ескальована пропозиція (День 11)

| Налаштування | Значення |
|---------|-------|
| Campaign ID | `12-AH-7D-C3-EMAIL-SMS` |
| Канал | Email + SMS |
| Умова | Немає логіну після C2 |
| Subject (ES) | `💰 {bonus_pct}% extra en tu próximo depósito` |

**Вміст емейлу:**
- **Subject (ES):** `💰 {bonus_pct}% extra en tu próximo depósito`
- **Preheader (ES):** `Oferta exclusiva por tiempo limitado, {first_name}`
- **Banner Text (ES):** `{bonus_pct}% Extra Para Vos`
- **Banner Description:** Ескальована пропозиція — великий текст "{bonus_pct}%", візуал reload match, монети депозиту, бурштиново-золотий тон терміновості
- **Body Description:** Ескальована пропозиція reload match: {bonus_pct}% up to 3,000 ARS (× множник рівня цінності). Показати як зробити депозит. Терміновість: обмежений час.

**Базова пропозиція:** 30% reload match up to 3,000 ARS (× множник рівня цінності)

---

### AH-7D-C4: Фінальний поштовх (День 13)

| Налаштування | Значення |
|---------|-------|
| Campaign ID | `12-AH-7D-C4-SMS` |
| Канал | SMS |
| Умова | Немає логіну після C3 |

**SMS (ES):**
```
CuatroBet: {first_name}, última oportunidad: {bonus_pct}% + {fs_count} giros. Vence mañana. {link}
```

**Базова пропозиція:** 50% reload + 20 FS (× множник рівня цінності)  
**Додатково для Pre-VIP+:** Персональний телефонний дзвінок від CRM-менеджера.

**Вихід:** Якщо немає логіну → Перехід у бакет 14-Day.

---

## B. ACTIVE HISTORY — 14-DAY DORMANT

**Journey Name:** `12-AH-14D-JOURNEY`  
**Вхід:** Пройшов з 7-Day бакету без логіну

### AH-14D-C1: "Ми сумуємо" (День 14)

| Налаштування | Значення |
|---------|-------|
| Campaign ID | `12-AH-14D-C1-EMAIL` |
| Канал | Email |
| Subject (ES) | `💳 {cc_balance} CC y cashback sin reclamar` |

**Вміст емейлу:**
- **Subject (ES):** `💳 {cc_balance} CC y cashback sin reclamar`
- **Preheader (ES):** `{first_name}, tus premios están esperando en tu cuenta`
- **Banner Text (ES):** `{cc_balance} CC + {cashback} ARS Sin Reclamar`
- **Banner Description** Попередження про невикористану цінність — купа монет CC + сума cashback на видному місці, візуал зникнення/терміновості, стрічка "забери поки не пізно"
- **Body Description:** Показати накопичений невикористаний баланс CC та cashback. Акцент на терміновості — цінність чекає на отримання. Розбивка того, що можна обміняти.

---

### AH-14D-C2: Значний бонус (День 16)

| Налаштування | Значення |
|---------|-------|
| Campaign ID | `12-AH-14D-C2-SMS` |
| Канал | SMS |

**SMS (ES):**
```
CuatroBet: {first_name}, bono especial de bienvenida: {bonus_ars} ARS gratis. Sin depósito. 48h: {link}
```

**Базова пропозиція:** 500 ARS no-deposit bonus (× множник рівня цінності)  
**Wagering:** 15× до виведення

---

### AH-14D-C3: Ексклюзивний доступ (День 18)

| Налаштування | Значення |
|---------|-------|
| Campaign ID | `12-AH-14D-C3-EMAIL-PUSH` |
| Канал | Email + Push |
| Subject (ES) | `🏆 Acceso exclusivo: torneo privado para vos` |

**Вміст емейлу:**
- **Subject (ES):** `🏆 Acceso exclusivo: torneo privado para vos`
- **Preheader (ES):** `Solo jugadores seleccionados fueron invitados`
- **Banner Text (ES):** `Torneo Privado Exclusivo`
- **Banner Description:** Запрошення на VIP турнір — ексклюзивний золотий квиток, трофей турніру, відображена сума призового фонду, преміальний темно-золотий дизайн
- **Body Description:** Ексклюзивний вхід на турнір. Для звичайних гравців: призовий фонд 1,000 ARS. Для Pre-VIP+: персональне запрошення від VIP-менеджера + турнір на 5,000 ARS.

**Пропозиція:** Вхід на ексклюзивний турнір + призовий фонд 1,000 ARS  
**Для Pre-VIP+:** Персональне запрошення від VIP-менеджера + турнір на 5,000 ARS

---

### AH-14D-C4: "Двері зачиняються" (День 20)

| Налаштування | Значення |
|---------|-------|
| Campaign ID | `12-AH-14D-C4-SMS` |
| Канал | SMS |

**SMS (ES):**
```
CuatroBet: {first_name}, tu oferta de {bonus_ars} ARS + {fs_count} giros vence hoy. No la pierdas: {link}
```

**Базова пропозиція:** 750 ARS no-deposit + 30 FS (× множник рівня цінності)  
**Вихід:** Якщо немає логіну → Перехід у бакет 21+ Day.

---

## C. ACTIVE HISTORY — 21+ DAY DORMANT (ГЛИБОКА)

**Journey Name:** `12-AH-21D-JOURNEY`  
**Вхід:** Пройшов з 14-Day бакету без логіну

### AH-21D-C1: Пакет повернення (День 21)

| Налаштування | Значення |
|---------|-------|
| Campaign ID | `12-AH-21D-C1-EMAIL` |
| Канал | Email |
| Subject (ES) | `🎁 Paquete de reactivación personalizado para vos` |

**Вміст емейлу:**
- **Subject (ES):** `🎁 Paquete de reactivación personalizado para vos`
- **Preheader (ES):** `Bonus + giros + CC armados según tu perfil`
- **Banner Text (ES):** `Tu Paquete de Reactivación`
- **Banner Description:** Візуал пакету повернення — преміальна подарункова коробка, що відкривається, 3 нагороди видимі (готівка + FS + match), персоналізований артворк топ-гри, вражаючий темно-золотий дизайн
- **Body Description:** Деталі персоналізованого пакету повернення: 1,000 ARS no-deposit + 50 FS на історично топовому слоті гравця + 100% match up to 5,000 ARS. Дійсний 72 год. Чітка CTA.

**Пакет (базовий):**
- 1,000 ARS no-deposit bonus
- 50 FS на історично топовому слоті гравця
- 100% match up to 5,000 ARS на наступний депозит
- Дійсний 72 год

---

### AH-21D-C2: SMS нагадування (День 24)

| Налаштування | Значення |
|---------|-------|
| Campaign ID | `12-AH-21D-C2-SMS` |
| Канал | SMS |

**SMS (ES):**
```
CuatroBet: {first_name}, tu paquete de reactivación sigue activo. {bonus_ars} ARS + {fs} giros + {match}% match. 48h más: {link}
```

---

### AH-21D-C3: VIP-ескалація / Остання автоматизована (День 28)

| Налаштування | Значення |
|---------|-------|
| Campaign ID | `12-AH-21D-C3-SMS-EMAIL` |
| Канал | SMS + Email |

**Вміст емейлу:**
- **Subject (ES):** Для Micro/Low/Mid: `⚠️ {first_name}, última oferta antes de despedirnos` Для High/Pre-VIP+: Обробляється VIP-командою.
- **Preheader (ES):** `No queremos perderte — mirá lo que preparamos`
- **Banner Text (ES):** `Última Oferta`
- **Banner Description:** Фінальна автоматизована пропозиція — стрічка "останній шанс", преміальний візуал нагороди (1,500 ARS + 75 FS), візуал зачинених дверей, дизайн з червоно-бурштиновою терміновістю
- **Body Description:** Для Micro/Low/Mid: Фінальна автоматизована пропозиція — 1,500 ARS no-dep + 75 FS. Для High/Pre-VIP+: Передача VIP-команді для персональної кампанії повернення. Позначити для ручного контакту.

**Для Micro/Low/Mid:** Фінальна автоматизована пропозиція — 1,500 ARS no-deposit + 75 FS.  
**Для High/Pre-VIP+:** Передача VIP-команді для персональної кампанії повернення. Позначити гравця для ручного контакту.

---

### AH-21D-C4: Опитування на виході (День 35)

| Налаштування | Значення |
|---------|-------|
| Campaign ID | `12-AH-21D-C4-EMAIL` |
| Канал | Email |
| Subject (ES) | `📝 Nos gustaría saber por qué te fuiste` |

**Вміст емейлу:**
- **Subject (ES):** `📝 Nos gustaría saber por qué te fuiste`
- **Preheader (ES):** `Tu opinión nos ayuda a mejorar, {first_name}`
- **Banner Text (ES):** `Contános Tu Opinión`
- **Banner Description:** Опитування на виході — дружній запит зворотного зв'язку, іконки мовних бульбашок, візуал 3-х питань, нагорода 500 CC за завершення, м'який синьо-бірюзовий професійний тон
- **Body Description:** Опитування з 3 питань: чому пішли, що повернуло б, оцінка досвіду (1-5). 500 CC стимул за завершення. Позначити гравця відповідями.

**Стимул:** 500 CC за завершення опитування.  
**Дія:** Позначити гравця відповідями опитування для майбутніх кампаній.

---

## D. PASSIVE HISTORY — 7/14/21+ DAY (Та сама структура, нижчі пропозиції)

**Journey Names:** `12-PH-7D`, `12-PH-14D`, `12-PH-21D`

Застосовується та сама структура з 4 комунікацій як Active History, з такими коригуваннями:

| Різниця | Active History | Passive History |
|-----------|---------------|-----------------|
| Суми пропозицій | Базова × множник цінності | Базова × 0.7 × множник цінності |
| Пріоритет каналу | Email → Push → SMS | Спочатку SMS (вищий відгук для низького залучення) |
| Персоналізація | Рекомендації ігор, турнір | Простий cashback, лише FS |
| Ескалація до VIP-команди | High + Pre-VIP+ | Лише Pre-VIP+ |
| Опитування на виході | День 35 | День 28 (коротший цикл) |

### Підсумок комунікацій Passive History:

| Бакет | C1 | C2 | C3 | C4 |
|--------|----|----|----|----|
| 7-Day | `12-PH-7D-C1` М'яка перевірка (SMS) | `12-PH-7D-C2` 7 FS (SMS) | `12-PH-7D-C3` 20% reload (Email+SMS) | `12-PH-7D-C4` 35% reload + 15 FS (SMS) |
| 14-Day | `12-PH-14D-C1` Сумуємо (Email) | `12-PH-14D-C2` 350 ARS no-dep (SMS) | `12-PH-14D-C3` Простий вхід на турнір (Email) | `12-PH-14D-C4` 500 ARS + 20 FS (SMS) |
| 21+ Day | `12-PH-21D-C1` Повернення лайт (Email) | `12-PH-21D-C2` Нагадування (SMS) | `12-PH-21D-C3` Фінальна пропозиція (SMS) | `12-PH-21D-C4` Опитування на виході (Email) |

---

## E. VNR — VERIFIED BUT NO REACTED (Верифіковані, але не зреагували — спеціальний кейс)

**Journey Name:** `12-VNR-JOURNEY`  
**Сегмент:** Завершив реєстрацію + KYC верифікацію, АЛЕ ніколи не робив депозит ТА `last_login` > 7 днів.

### VNR-C1: Нагадування про верифікований статус (День 7)

| Налаштування | Значення |
|---------|-------|
| Campaign ID | `12-VNR-C1-EMAIL` |
| Канал | Email |
| Subject (ES) | `✅ {first_name}, cuenta verificada — falta tu depósito` |

**Вміст емейлу:**
- **Subject (ES):** `✅ {first_name}, cuenta verificada — falta tu depósito`
- **Preheader (ES):** `Tu bono de bienvenida te está esperando`
- **Banner Text (ES):** `Cuenta Verificada — Listo Para Depositar`
- **Banner Description:** Верифікований акаунт — зелена галочка на іконці акаунту, тизер процесу депозиту, попередній перегляд вітального бонусу, чистий професійний дизайн
- **Body Description:** Акцент на завершеній верифікації. Депозит миттєвий. Вітальний бонус чекає. Покрокова інструкція з депозиту.
- **CTA (ES):** `Depositar ahora` → Каса

---

### VNR-C2: Бонусний поштовх (День 10)

| Налаштування | Значення |
|---------|-------|
| Campaign ID | `12-VNR-C2-SMS` |
| Канал | SMS |

**SMS (ES):**
```
CuatroBet: {first_name}, tu cuenta verificada tiene un bono de bienvenida de {bonus_pct}% esperando. Depositá ahora: {link}
```

---

### VNR-C3: Безкоштовна проба (День 14)

| Налаштування | Значення |
|---------|-------|
| Campaign ID | `12-VNR-C3-EMAIL-SMS` |
| Канал | Email + SMS |
| Subject (ES) | `🎰 {fs_count} giros gratis sin depósito para vos` |

**Вміст емейлу:**
- **Subject (ES):** `🎰 {fs_count} giros gratis sin depósito para vos`
- **Preheader (ES):** `Probá sin riesgo, solo para cuentas verificadas`
- **Banner Text (ES):** `{fs_count} Giros Gratis — Sin Depósito`
- **Banner Description:** Безкоштовна проба — візуал free spins зі значком "no deposit", ексклюзивна стрічка "лише для верифікованих", попередній перегляд артворку гри, захопливі синьо-золоті тони
- **Body Description:** Пропозиція безкоштовної проби: {fs_count} FS без депозиту, 10× wagering. Ексклюзивно для верифікованих гравців. Спробувати продукт без ризику.

**Пропозиція:** 20 FS no-deposit (низький wagering 10×), щоб дати їм спробувати продукт.

---

### VNR-C4: Фінальна спроба (День 21)

| Налаштування | Значення |
|---------|-------|
| Campaign ID | `12-VNR-C4-SMS` |
| Канал | SMS |

**SMS (ES):**
```
CuatroBet: {first_name}, última oportunidad. 500 ARS gratis + 30 giros. Solo hoy: {link}
```

**Пропозиція:** 500 ARS no-deposit + 30 FS. Wagering 15×.  
**Вихід:** Якщо немає депозиту після C4, позначити як `reactivation_exhausted`. Не контактувати повторно 60 днів.

---

## F. ШАБЛОНИ БОНУСІВ ДЛЯ РЕАКТИВАЦІЇ

| Template ID | Назва | Тип | Базова цінність | Wagering |
|------------|------|------|-----------|----------|
| `REACT-FS-10` | Light FS | Free Spins | 10 FS | 25× |
| `REACT-FS-20` | Medium FS | Free Spins | 20 FS | 20× |
| `REACT-FS-50` | Heavy FS | Free Spins | 50 FS | 15× |
| `REACT-RELOAD-30` | Lite Reload | Match | 30% up to 3K | 20× |
| `REACT-RELOAD-50` | Mid Reload | Match | 50% up to 5K | 18× |
| `REACT-RELOAD-100` | Full Reload | Match | 100% up to 5K | 15× |
| `REACT-NODEP-500` | No-Dep Small | Cash | 500 ARS | 15× |
| `REACT-NODEP-750` | No-Dep Medium | Cash | 750 ARS | 15× |
| `REACT-NODEP-1000` | No-Dep Large | Cash | 1,000 ARS | 12× |
| `REACT-NODEP-1500` | No-Dep XL | Cash | 1,500 ARS | 10× |
| `REACT-PKG` | Win-Back Package | Bundle | 1K + 50 FS + 100% match | 12× |

**Застосування множника цінності:**
```
final_value = base_value × value_tier_multiplier
final_wagering = base_wagering (незмінний — НЕ масштабувати wagering)
```

---

## G. ІНТЕГРАЦІЯ PREDICTIVE CHURN

**Логіка раннього входу:**
```
IF churn_score ≥ 0.7 AND last_session_date ≤ 4 days:
  Enter 7-Day journey immediately (skip waiting to day 7)
  Tag: "churn_predicted_early_entry"

IF churn_score ≥ 0.85 AND value_tier IN ("High", "Pre-VIP+"):
  Alert VIP team immediately via internal notification
  Tag: "churn_critical_high_value"
```

---

## ЧАСТОТНІ ОБМЕЖЕННЯ (перевизначення для реактивації)

| Правило | Налаштування |
|------|---------|
| Макс. комунікацій реактивації на тиждень | 3 |
| Мін. проміжок між комунікаціями | 48 годин |
| Перевизначення стандартних частотних обмежень | ТАК для journey реактивації |
| Не перетинатися з | Ланцюг 09 (Personalization birthday/anniversary) |
| Пауза після вичерпання | 60 днів без контакту |

---

## ЧЕК-ЛИСТ ТЕСТУВАННЯ

- [ ] Сегменти Active vs Passive History коректно заповнені
- [ ] Бакети 7/14/21 днів спрацьовують у правильні інтервали
- [ ] Множник рівня цінності застосовується до сум пропозицій (НЕ до wagering)
- [ ] Поведінковий фільтр направляє комунікації у правильні канали
- [ ] Ранній вхід Predictive Churn спрацьовує при ≥0.7 ймовірності
- [ ] Алерт VIP-команди спрацьовує для критичного відтоку високої цінності
- [ ] Сегмент VNR коректно ідентифікує гравців verified-no-deposit
- [ ] Потік VNR НЕ перетинається зі стандартною реактивацією
- [ ] Шаблони бонусів зараховують правильні суми
- [ ] No-deposit бонуси мають правильні вимоги wagering
- [ ] Опитування на виході записує відповіді та позначає гравця
- [ ] Тег `reactivation_exhausted` запобігає повторному входу на 60 днів
- [ ] Частотне обмеження 3/тиждень дотримується
- [ ] Мінімальний проміжок 48 годин між комунікаціями дотримується
- [ ] Сповіщення про телефонний дзвінок для Pre-VIP+ працює

---

## ЦІЛЬОВІ KPI

| Метрика | Ціль |
|--------|--------|
| Частка реактивації 7-Day (Active History) | ≥ 25% |
| Частка реактивації 7-Day (Passive History) | ≥ 12% |
| Частка реактивації 14-Day (Active History) | ≥ 15% |
| Частка реактивації 21+ Day (Active History) | ≥ 8% |
| Конверсія VNR у FTD | ≥ 10% |
| Частка завершення опитування на виході | ≥ 20% |
| Вартість реактивованого гравця | ≤ 2,500 ARS |
