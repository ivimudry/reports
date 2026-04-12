# 00 — Інтеграція даних та налаштування платформи — Основний документ

**Мета:** Цей документ містить КОЖНУ точку даних, подію, атрибут, сегмент та конфігурацію платформи, необхідну перед побудовою будь-якої автоматизації. Завершіть цей чек-лист першим — окремі інструкції ланцюгів посилаються на елементи звідси.

**Платформа:** GR8 Tech CRM
**Останнє оновлення:** Квітень 2026

---

## ЗМІСТ

1. [Події в реальному часі](#1-події-в-реальному-часі)
2. [Атрибути гравця](#2-атрибути-гравця)
3. [Розрахункові метрики](#3-розрахункові-метрики)
4. [Сегменти для побудови](#4-сегменти-для-побудови)
5. [Конфігурація каналів](#5-конфігурація-каналів)
6. [Ліміти частоти](#6-ліміти-частоти)
7. [Конфігурація бонусів](#7-конфігурація-бонусів)
8. [Технічні залежності](#8-технічні-залежності)
9. [Пріоритетний порядок впровадження](#9-пріоритетний-порядок-впровадження)

---

## 1. ПОДІЇ В РЕАЛЬНОМУ ЧАСІ

Ці події мають спрацьовувати в реальному часі (затримка менше 5 секунд) від GR8 Tech до CRM-рушія. Кожна подія має нести зазначені атрибути payload.

### 1.1 Реєстрація та автентифікація

| Назва події | Спрацьовує коли | Обов'язковий payload |
| --------------------- | ------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `player_registered` | Створення акаунту завершено | `player_id`, `registration_timestamp`, `registration_source`, `country`, `device_type` |
| `session_start` | Гравець відкриває додаток/сайт | `player_id`, `session_id`, `timestamp`, `device_type`, `referrer` |
| `session_end` | Гравець закриває додаток/залишає сайт (або 30 хв таймаут неактивності) | `player_id`, `session_id`, `timestamp`, `session_duration_seconds`, `pages_visited[]` |

### 1.2 KYC та верифікація

| Назва події | Спрацьовує коли | Обов'язковий payload |
| ----------------------- | ------------------------------- | -------------------------------------------------- |
| `email_verified` | Гравець натискає посилання верифікації | `player_id`, `timestamp`, `email` |
| `phone_verified` | Гравець вводить правильний SMS-код | `player_id`, `timestamp`, `phone_number` |
| `documents_submitted` | Гравець завантажує KYC-документи | `player_id`, `timestamp`, `document_types[]` |
| `documents_approved` | KYC-перевірка пройдена | `player_id`, `timestamp` |
| `documents_rejected` | KYC-перевірка не пройдена | `player_id`, `timestamp`, `rejection_reason` |

### 1.3 Депозити та платежі

| Назва події | Спрацьовує коли | Обов'язковий payload |
| ------------------------ | --------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `deposit_success` | Депозит підтверджено | `player_id`, `amount_ars`, `payment_method`, `deposit_number` (1-й, 2-й тощо), `timestamp`, `is_ftd` (boolean) |
| `deposit_failed` | Спроба депозиту невдала | `player_id`, `attempted_amount_ars`, `payment_method`, `failure_reason` (`INSUFF` / `METHOD` / `DECLINE` / `TIMEOUT` / `FRAUD`), `attempt_count_session`, `timestamp` |
| `cashier_opened` | Гравець переходить на сторінку депозиту | `player_id`, `timestamp`, `session_id` |
| `cashier_closed` | Гравець залишає сторінку депозиту без поповнення | `player_id`, `timestamp`, `session_id`, `time_on_page_seconds` |
| `withdrawal_requested` | Гравець запитує виведення | `player_id`, `amount_ars`, `timestamp` |

### 1.4 Геймплей

| Назва події | Спрацьовує коли | Обов'язковий payload |
| ----------------------- | ------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| `game_launched` | Гравець відкриває гру | `player_id`, `game_id`, `game_name`, `game_type` (`slots`/`live`/`sport`/`crash`), `provider`, `is_demo` (boolean), `timestamp` |
| `game_round_complete` | Раунд/спін завершено | `player_id`, `game_id`, `bet_amount_ars`, `win_amount_ars`, `timestamp` |
| `wagering_progress` | Оновлення прогресу відіграшу | `player_id`, `bonus_id`, `wagered_amount`, `required_amount`, `percentage_complete`, `timestamp` |
| `wagering_complete` | Гравець завершив відіграш бонусу | `player_id`, `bonus_id`, `timestamp` |

### 1.5 Бонуси та промоакції

| Назва події | Спрацьовує коли | Обов'язковий payload |
| ---------------------- | -------------------------- | ----------------------------------------------------------------------------------------------- |
| `bonus_claimed` | Гравець активує бонус | `player_id`, `bonus_id`, `bonus_type`, `bonus_value_ars`, `timestamp` |
| `bonus_expired` | Закінчується термін дії бонусу | `player_id`, `bonus_id`, `timestamp` |
| `free_spins_awarded` | FS зараховано гравцеві | `player_id`, `spin_count`, `game_id`, `source` (welcome/quest/shop/тощо), `timestamp` |
| `free_spins_used` | Гравець використовує FS | `player_id`, `spin_count`, `game_id`, `winnings_ars`, `timestamp` |
| `loot_box_earned` | Гравець отримує лутбокс | `player_id`, `timestamp` |
| `loot_box_opened` | Гравець відкриває лутбокс | `player_id`, `reward_type`, `reward_value`, `timestamp` |
| `lucky_wheel_spin` | Гравець крутить Lucky Wheel | `player_id`, `wheel_tier` (`silver`/`gold`/`platinum`), `reward`, `timestamp` |

### 1.6 Лояльність та квести

| Назва події | Спрацьовує коли | Обов'язковий payload |
| ----------------------- | ------------------------------------ | -------------------------------------------------------------------------------------------- |
| `mission_completed` | Гравець завершує місію лояльності | `player_id`, `mission_id`, `cc_earned`, `timestamp` |
| `quest_progress` | Досягнуто контрольну точку квесту | `player_id`, `quest_id`, `quest_name`, `step_current`, `step_total`, `timestamp` |
| `quest_completed` | Усі кроки квесту виконані | `player_id`, `quest_id`, `quest_name`, `rewards[]`, `timestamp` |
| `loyalty_tier_change` | Гравець піднімається/опускається в тірах | `player_id`, `old_tier`, `new_tier`, `timestamp` |
| `cc_earned` | Cuatro Coins зараховано | `player_id`, `amount_cc`, `source`, `timestamp` |
| `cc_spent` | Cuatro Coins витрачено | `player_id`, `amount_cc`, `item_id`, `timestamp` |

### 1.7 Реферали

| Назва події | Спрацьовує коли | Обов'язковий payload |
| --------------------------- | ------------------------------ | ------------------------------------------------------ |
| `referral_link_generated` | Гравець створює реферальне посилання | `player_id`, `referral_code`, `timestamp` |
| `referral_registered` | Запрошений гравець реєструється | `referrer_id`, `referred_player_id`, `timestamp` |
| `referral_qualified` | Запрошений гравець завершує STD | `referrer_id`, `referred_player_id`, `timestamp` |

### 1.8 Комунікації

| Назва події | Спрацьовує коли | Обов'язковий payload |
| ------------------- | ------------------------------ | ----------------------------------------------------------- |
| `email_opened` | Гравець відкриває email | `player_id`, `campaign_id`, `timestamp` |
| `email_clicked` | Гравець натискає посилання в email | `player_id`, `campaign_id`, `link_url`, `timestamp` |
| `sms_delivered` | SMS доставлено оператору | `player_id`, `campaign_id`, `timestamp` |
| `push_opened` | Гравець натискає push-сповіщення | `player_id`, `campaign_id`, `timestamp` |
| `popup_shown` | In-app popup відображено | `player_id`, `campaign_id`, `timestamp` |
| `popup_clicked` | Гравець натискає CTA popup | `player_id`, `campaign_id`, `timestamp` |
| `popup_dismissed` | Гравець закриває popup | `player_id`, `campaign_id`, `timestamp` |

---

## 2. АТРИБУТИ ГРАВЦЯ

Ці атрибути мають зберігатися та бути доступними для запитів у CRM для сегментації, персоналізації та логіки подорожей.

### 2.1 Ідентифікація

| Атрибут | Тип | Джерело | Примітки |
| --------------------- | -------- | ------------------------ | ----------------------------- |
| `player_id` | String | GR8 Tech | Первинний ключ |
| `email` | String | Реєстрація | |
| `phone_number` | String | Реєстрація/KYC | |
| `first_name` | String | Реєстрація | Для токенів персоналізації |
| `country` | String | Реєстрація | Має бути "AR" для Аргентини |
| `language` | String | Реєстрація | За замовчуванням "es-AR" |
| `registration_date` | DateTime | Реєстрація | |
| `birthday` | Date | KYC/Профіль | Для бонусу на день народження |
| `zodiac_sign` | String | Розраховується з дати народження | Для зодіакального бонусу |

### 2.2 KYC-статус

| Атрибут | Тип | Значення | Примітки |
| ----------------------- | ------- | ---------------------------------------------------- | ------------------------------------------------ |
| `email_verified` | Boolean | true/false | |
| `phone_verified` | Boolean | true/false | Розблоковує SMS-канал |
| `documents_submitted` | Boolean | true/false | |
| `documents_status` | Enum | `none` / `pending` / `approved` / `rejected` | |
| `kyc_level` | Enum | `unverified` / `partial` / `full` | partial = email+телефон, full = документи підтверджено |

### 2.3 Фінансові

| Атрибут | Тип | Частота оновлення | Примітки |
| ------------------------------ | -------- | ----------------- | ------------------------------------------- |
| `deposit_count` | Integer | При кожному депозиті | Загальна кількість депозитів за весь час |
| `cumulative_deposits_ars` | Float | При кожному депозиті | Сума депозитів за весь час |
| `last_deposit_date` | DateTime | При кожному депозиті | |
| `last_deposit_amount_ars` | Float | При кожному депозиті | |
| `ftd_date` | DateTime | При першому депозиті | Null якщо немає FTD |
| `ftd_amount_ars` | Float | При першому депозиті | |
| `std_date` | DateTime | При другому депозиті | Null якщо немає STD |
| `average_deposit_ars` | Float | Розрахункова | `cumulative_deposits_ars / deposit_count` |
| `payment_methods_used[]` | Array | При кожному депозиті | Список використаних методів |
| `last_withdrawal_date` | DateTime | При виведенні | |
| `cumulative_withdrawals_ars` | Float | При виведенні | |
| `ggr_ars` | Float | Розраховується щоденно | Gross Gaming Revenue |

### 2.4 Геймплей

| Атрибут | Тип | Частота оновлення | Примітки |
| ---------------------------------- | -------- | ----------------- | ---------------------------------------------------------- |
| `game_preference` | Enum | Розраховується щотижня | `slots` / `live` / `aviator` / `mixed` / `sport` |
| `most_played_game_id` | String | Розраховується щотижня | |
| `most_played_game_name` | String | Розраховується щотижня | Для персоналізації FS |
| `top_3_games[]` | Array | Розраховується щотижня | ID ігор |
| `total_rounds_played` | Integer | Реальний час | |
| `total_wagered_ars` | Float | Реальний час | |
| `biggest_win_ars` | Float | Реальний час | Для персоналізації річниці |
| `last_game_date` | DateTime | Реальний час | |
| `last_session_date` | DateTime | Реальний час | |
| `last_session_duration_seconds` | Integer | Реальний час | |
| `has_played_demo` | Boolean | Реальний час | Для шляху C «Каса не відвідана» |

### 2.5 Життєвий цикл та цінність

| Атрибут | Тип | Частота оновлення | Примітки |
| ---------------------------- | -------------- | ---------------- | ---------------------------------------------------------- |
| `lifecycle_stage` | Enum | Реальний час | Дивіться Вісь 1 у секції 17 |
| `value_tier` | Enum | Щоденно | `micro` / `low` / `mid` / `high` / `previp_plus` |
| `days_since_last_activity` | Integer | Щоденно | Для матриці реактивації |
| `days_since_registration` | Integer | Щоденно | |
| `engagement_history` | Enum | Щотижня | `active` / `passive` — для матриці реактивації |
| `churn_score` | Float (0–100) | Щоденно | З моделі Predictive Churn |
| `churn_risk_level` | Enum | Щоденно | `healthy` / `watch` / `at_risk` / `critical` |

### 2.6 Лояльність

| Атрибут | Тип | Примітки |
| ------------------------- | -------- | ----------------------------------------------------- |
| `loyalty_enrolled` | Boolean | |
| `loyalty_tier` | Enum | `premium` / `prestige` / `maestro` / `legend` |
| `cc_balance` | Integer | Поточний баланс Cuatro Coins |
| `cc_lifetime_earned` | Integer | |
| `cc_last_spent_date` | DateTime | Для попереджень про закінчення CC |
| `missions_completed_7d` | Integer | Для класифікації активний/пасивний |
| `last_mission_date` | DateTime | |

### 2.7 Налаштування комунікацій

| Атрибут | Тип | Примітки |
| ---------------------------- | ------- | ------------------------------------------------------ |
| `email_opt_in` | Boolean | |
| `sms_opt_in` | Boolean | Автоматично при верифікації телефону |
| `push_opt_in` | Boolean | |
| `preferred_contact_method` | Enum | `sms` / `email` / `push` |
| `email_engagement_30d` | Enum | `high` / `low` / `zero` — на основі відкриттів/кліків |
| `messages_today_count` | Integer | Для контролю лімітів частоти |

### 2.8 Стан бонусів

| Атрибут | Тип | Примітки |
| ----------------------------- | ------- | --------------------------------------------------------- |
| `welcome_bonus_claimed` | Boolean | |
| `welcome_bonus_status` | Enum | `available` / `claimed` / `completed` / `expired` |
| `active_bonus_id` | String | Поточний активний бонус |
| `active_bonus_wagering_pct` | Float | 0–100% завершення відіграшу |
| `welcome_ladder_step` | Integer | 1–10 (який депозит у драбині) |

### 2.9 Реферали

| Атрибут | Тип | Примітки |
| ------------------------------ | ------- | ----------------------------- |
| `referral_code` | String | Унікальний код гравця |
| `referrals_successful_count` | Integer | Кваліфіковані реферали (STD) |
| `referrals_successful_month` | Integer | Кількість цього місяця (для ліміту) |
| `was_referred` | Boolean | Гравець прийшов за рефералом |
| `referred_by_player_id` | String | |

---

## 3. РОЗРАХУНКОВІ МЕТРИКИ

Ці метрики мають обчислюватися GR8 Tech та оновлюватися за вказаним графіком.

| Метрика | Формула | Оновлення | Використовується |
| ------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------ | ----------------------- |
| `value_tier` | На основі `cumulative_deposits_ars`: <5K=micro, 5–25K=low, 25–75K=mid, 75–150K=high, >150K=previp+ | Щоденно | Масштабування пропозицій |
| `lifecycle_stage` | На основі правил: кількість депозитів, остання активність, сума депозитів | Реальний час | Вхід/вихід з подорожі |
| `game_preference` | >70% раундів одного типу = цей тип; інакше "mixed" | Щотижня | Персоналізація контенту |
| `engagement_history` | ≥1 місія за 7д = "active"; інакше "passive" | Щоденно | Матриця реактивації |
| `churn_score` | Вихід моделі Predictive Churn | Щоденно | Прискорення часу |
| `email_engagement_30d` | Відкриття за 30д: ≥3 = high; 1–2 = low; 0 = zero | Щоденно | Вибір каналу |
| `zodiac_sign` | Розраховується з поля `birthday` | При оновленні профілю | Зодіакальний бонус |
| `days_inactive` | `today - max(last_deposit_date, last_session_date)` | Щоденно | Тригери реактивації |
| `bonus_cost_pct_ggr` | `total_bonus_paid / ggr * 100` | Щотижня | Моніторинг витрат |

---

## 4. СЕГМЕНТИ ДЛЯ ПОБУДОВИ

Побудуйте ці сегменти у рушії сегментації GR8 Tech. Вони використовуються у всіх інструкціях з впровадження.

### 4.1 Сегменти життєвого циклу

| ID сегмента | Назва | Правила |
| --------------- | ------------------ | -------------------------------------------------------------------------- |
| `SEG-REG` | Зареєстрований, без FTD | `deposit_count = 0` |
| `SEG-FTD` | FTD виконано, <24г | `deposit_count = 1 AND hours_since_ftd < 24` |
| `SEG-D1LAYER` | У Day 1 Layer | `deposit_count >= 1 AND days_since_ftd <= 3` |
| `SEG-PRESTD` | Pre-STD | `deposit_count = 1 AND days_since_ftd > 1` |
| `SEG-REGULAR` | Звичайний | `deposit_count >= 2 AND days_inactive < 14` |
| `SEG-PREVIP` | Pre-VIP | `cumulative_deposits_ars >= 150000 AND cumulative_deposits_ars < 300000` |
| `SEG-VIP` | VIP | `cumulative_deposits_ars >= 300000` |

### 4.2 KYC-сегменти

| ID сегмента | Назва | Правила |
| ------------------------- | -------------------- | ------------------------------------------------------------------ |
| `SEG-KYC-NONE` | Неверифікований | `kyc_level = "unverified"` |
| `SEG-KYC-EMAIL-PENDING` | Email не верифіковано | `email_verified = false` |
| `SEG-KYC-PHONE-PENDING` | Телефон не верифіковано | `phone_verified = false` |
| `SEG-KYC-DOCS-PENDING` | Документи не подано | `documents_status = "none" AND cumulative_deposits_ars >= 15000` |
| `SEG-KYC-FULL` | Повністю верифікований | `kyc_level = "full"` |

### 4.3 Поведінкові сегменти

| ID сегмента | Назва | Правила |
| ------------------------- | ----------------------------------- | ----------------------------------------------------------------------------------------- |
| `SEG-BOUNCE` | Відмова (сесія <60с, без каси) | `last_session_duration < 60 AND cashier_opened = false` |
| `SEG-LONG-NO-CASHIER` | Довга сесія, без каси | `last_session_duration > 600 AND cashier_opened = false` |
| `SEG-FS-NO-DEP` | Грав FS, без депозиту | `has_played_demo = true AND deposit_count = 0` |
| `SEG-BONUS-MISSED` | Пропущений Welcome-бонус | `deposit_count = 0 AND welcome_bonus_claimed = false AND hours_since_registration >= 1` |
| `SEG-BONUS-DECLINED` | Відхилений Welcome-бонус | `welcome_bonus_status = "declined" OR (bonus_flow_bypassed = true)` |
| `SEG-CASHIER-ABANDONED` | Відкрив касу, без депозиту | Подія `cashier_closed` без наступного `deposit_success` протягом 30 хв |

### 4.4 Сегменти реактивації

| ID сегмента | Назва | Правила |
| ------------------ | ------------------------ | ----------------------------------------------------------------------------- |
| `SEG-REACT-A7` | Активний × 7 днів | `engagement_history = "active" AND days_inactive BETWEEN 7 AND 13` |
| `SEG-REACT-A14` | Активний × 14 днів | `engagement_history = "active" AND days_inactive BETWEEN 14 AND 20` |
| `SEG-REACT-A21` | Активний × 21+ днів | `engagement_history = "active" AND days_inactive >= 21` |
| `SEG-REACT-P7` | Пасивний × 7 днів | `engagement_history = "passive" AND days_inactive BETWEEN 7 AND 13` |
| `SEG-REACT-P14` | Пасивний × 14 днів | `engagement_history = "passive" AND days_inactive BETWEEN 14 AND 20` |
| `SEG-REACT-P21` | Пасивний × 21+ днів | `engagement_history = "passive" AND days_inactive >= 21` |
| `SEG-REACT-VNR` | Верифікований, без активності | `kyc_level = "full" AND deposit_count = 0 AND days_since_verification >= 3` |

### 4.5 Сегменти за тіром цінності

| ID сегмента | Назва | Правила |
| ------------------- | -------- | ---------------------------------------------------- |
| `SEG-VAL-MICRO` | Micro | `cumulative_deposits_ars < 5000` |
| `SEG-VAL-LOW` | Low | `cumulative_deposits_ars BETWEEN 5000 AND 24999` |
| `SEG-VAL-MID` | Mid | `cumulative_deposits_ars BETWEEN 25000 AND 74999` |
| `SEG-VAL-HIGH` | High | `cumulative_deposits_ars BETWEEN 75000 AND 149999` |
| `SEG-VAL-PREVIP` | Pre-VIP+ | `cumulative_deposits_ars >= 150000` |

### 4.6 Сегменти за ігровими вподобаннями

| ID сегмента | Назва | Правила |
| -------------------- | ------------- | ------------------------------- |
| `SEG-GAME-SLOTS` | Слоти (основні) | `game_preference = "slots"` |
| `SEG-GAME-LIVE` | Live (основні) | `game_preference = "live"` |
| `SEG-GAME-AVIATOR` | Aviator/Crash | `game_preference = "aviator"` |
| `SEG-GAME-MIXED` | Змішані | `game_preference = "mixed"` |

### 4.7 Сегменти залученості

| ID сегмента | Назва | Правила |
| ------------------- | --------------------- | ------------------------------------------------------------------------------------------- |
| `SEG-ENG-HIGH` | Висока Email-залученість | `email_engagement_30d = "high"` |
| `SEG-ENG-LOW` | Низька Email-залученість | `email_engagement_30d = "low"` |
| `SEG-ENG-ZERO` | Нульова залученість | `email_engagement_30d = "zero"` |
| `SEG-LOY-ACTIVE` | Активна лояльність | `loyalty_enrolled = true AND missions_completed_7d >= 1` |
| `SEG-LOY-PASSIVE` | Пасивна лояльність | `loyalty_enrolled = true AND missions_completed_7d = 0 AND days_since_last_mission <= 30` |

---

## 5. КОНФІГУРАЦІЯ КАНАЛІВ

### 5.1 SMS

| Параметр | Значення |
| ------------------ | ------------------------------------------------------------ |
| Провайдер | Наявний SMS-шлюз GR8 Tech |
| Sender ID | "CuatroBet" |
| Тихі години | 00:00–08:00 ART |
| Макс SMS/день/гравець | Див. ліміти частоти нижче |
| Тригер opt-in | Автоматично при події `phone_verified` |
| Скорочувач посилань | Увімкнути з відстеженням UTM |
| UTM за замовчуванням | `utm_source=sms&utm_medium=crm&utm_campaign={campaign_id}` |

### 5.2 Email

| Параметр | Значення |
| ------------ | -------------------------------------------------------------- |
| Адреса відправника | `hola@cuatrobet.com` (або еквівалент) |
| Ім'я відправника | "CuatroBet" |
| Reply-to | `soporte@cuatrobet.com` |
| UTM за замовчуванням | `utm_source=email&utm_medium=crm&utm_campaign={campaign_id}` |
| Відписка | Обов'язкова за законом — включити у футер |
| Прехедер | Має бути встановлений для кожної кампанії |

### 5.3 In-App Popup (NC Pop-Up)

| Параметр | Значення |
| ---------------------------- | ----------------------------------------------------------- |
| Макс 1 popup за сесію | Забезпечено |
| Без popup у перші 60 секунд | Забезпечено |
| Поведінка при закритті | Закрити і не показувати знову для цієї кампанії |
| Правила пріоритету | Якщо кілька popup у черзі → показати пропозицію з найвищою цінністю першою |

### 5.4 In-App Feed (NC Feed)

| Параметр | Значення |
| ------------------------------ | ----------------------------------------- |
| Макс 2 елементи/гравець/день | Забезпечено |
| Мін 4 години між елементами | Забезпечено |
| Цільова аудиторія | Тільки активні гравці (сесія за останні 48г) |
| Денний ліміт обсягу | 10,000 загальних відправлень (знижено з 25,700) |

### 5.5 App Push

| Параметр | Значення |
| ---------------- | ---------------------------------------------------------------------------------------------------- |
| Статус | **АКТИВУВАТИ** — наразі нуль відправлень |
| Запит opt-in | Показувати після першого депозиту (не при реєстрації) |
| Стимул opt-in | 100 CC при opt-in |
| Тихі години | 00:00–08:00 ART |
| Розгортання | Тиждень 1: налаштування → Тиждень 2: Day 1 Layer → Тиждень 3: Post-FTD/Pre-VIP → Тиждень 4: оцінка → Тиждень 5: повне |

### 5.6 Deep Links

Усі CTA-посилання у комунікаціях мають використовувати deep links, які відкривають правильну сторінку в додатку/сайті:

| Deep Link | Призначення | Використовується |
| --------------------------------------- | ------------------------------------- | ------------------------ |
| `{base_url}/cashier` | Сторінка депозиту | Більшість CTA |
| `{base_url}/cashier?method={method}` | Сторінка депозиту з попередньо обраним методом | Відновлення після невдачі платежу |
| `{base_url}/cashier?amount={amount}` | Сторінка депозиту з попередньо заповненою сумою | Відновлення з меншою сумою |
| `{base_url}/game/{game_id}` | Конкретна гра | Рекомендації ігор |
| `{base_url}/game/{game_id}?demo=true` | Демо-режим конкретної гри | Кластер без бонусу |
| `{base_url}/bonuses` | Цільова сторінка бонусів | Нагадування про бонуси |
| `{base_url}/bonus-shop` | Бонус-шоп | CTA витрат CC |
| `{base_url}/missions` | Сторінка місій лояльності | Комунікації лояльності |
| `{base_url}/profile/verify` | Сторінка завантаження KYC | Ланцюг KYC |
| `{base_url}/lucky-wheel` | Lucky Wheel | Квести/гейміфікація |
| `{base_url}/referral` | Сторінка реферальної програми | Реферальні комунікації |

---

## 6. ЛІМІТИ ЧАСТОТИ

Налаштуйте ці правила як глобальні у GR8 Tech CRM.

| Сегмент | Макс повідомлень/день (усі канали разом) |
| ------------------------------------ | ---------------------------------------- |
| `SEG-REG` (Pre-FTD) | 2 |
| `SEG-D1LAYER` (Day 1, перші 72г) | 3 |
| `SEG-REGULAR` | 2 |
| `SEG-PREVIP` / `SEG-VIP` | 2 |
| Сегменти реактивації | 1 |
| Транзакційні / Безпека | **Без обмежень** (без ліміту) |

**Правило колізії:** Якщо кілька кампаній спрацьовують в один день для одного гравця і ліміт досягнуто → відправити тільки повідомлення з найвищим пріоритетом / найвищою цінністю. Решту придушити.

**Аварійна зупинка:** Якщо open rate будь-якого каналу падає >25% тиждень до тижня → автоматично призупинити нові кампанії на цьому каналі, оповістити CRM-команду.

---

## 7. КОНФІГУРАЦІЯ БОНУСІВ

Ці бонусні шаблони мають існувати у GR8 Tech перед тим, як автоматизації зможуть на них посилатися.

### 7.1 Welcome Ladder — Слоти

| ID бонусу | Депозит # | Матч % | Кількість FS | Гра для FS | CC | Відіграш | Термін дії |
| ------------- | --------- | ------------------- | -------- | ---------------------- | ---- | -------- | -------- |
| `WBL-S-D1` | 1-й | 120% (150% якщо >15K) | 50 | Gates of Olympus | — | 25× | 7 днів |
| `WBL-S-D2` | 2-й | 75% | 30 | Joker's Jewels | — | 20× | 5 днів |
| `WBL-S-D3` | 3-й | 60% | 25 | Jackpot Joker | — | 18× | 5 днів |
| `WBL-S-D4` | 4-й | 55% | 20 | 4 Supercharged Clovers | — | 15× | 5 днів |
| `WBL-S-D5` | 5-й | 50% | 15 | Gold Party | 200 | 15× | 5 днів |
| `WBL-S-D6` | 6-й | 60% | 30 | 3 Coin Volcanoes | 300 | 15× | 5 днів |
| `WBL-S-D7` | 7-й | 65% | 35 | Rush for Gold | 400 | 15× | 5 днів |
| `WBL-S-D8` | 8-й | 70% | 40 | Gates of Olympus 1000 | 500 | 15× | 5 днів |
| `WBL-S-D9` | 9-й | 80% | 50 | Улюблений слот гравця | 600 | 12× | 7 днів |
| `WBL-S-D10` | 10-й | 100% | 60 | Улюблений слот гравця | 1000 | 10× | 7 днів |

### 7.2 Welcome Ladder — Live Casino

Така ж структура як у Слотів, але з Bonus Cash замість FS (див. специфікацію завдання 05).

### 7.3 Welcome Ladder — Sport

Така ж структура, але з Free Bets при мінімальних коефіцієнтах 1.80 (див. специфікацію завдання 05).

### 7.4 Бонуси KYC-верифікації

| ID бонусу | Тригер | Сума | Відіграш | Примітки |
| ------------------------- | -------------------------------------- | --------- | -------- | ------- |
| `KYC-EMAIL-REWARD` | Email верифіковано | 500 ARS | Немає | Миттєво |
| `KYC-PHONE-REWARD` | Телефон верифіковано | 500 ARS | Немає | Миттєво |
| `KYC-DOCS-REWARD-EARLY` | Документи підтверджено до порогу 22.5K | 1,000 ARS | Немає | |
| `KYC-DOCS-REWARD-HARD` | Документи підтверджено на/після порогу 22.5K | 2,000 ARS | Немає | |

### 7.5 Шаблони пропозицій реактивації

Створіть шаблони пропозицій, які масштабуються за тіром цінності. Повну матрицю див. в інструкції з впровадження секції 12.

### 7.6 Правила відіграшу

| Правило | Слоти | Live | Table | Sport |
| ----------------------- | -------------- | ---- | ----- | ----- |
| Внесок % | 100% | 10% | 5% | 100% |
| Макс ставка під час відіграшу | 1,500 ARS/спін | — | — | — |
| Макс баланс бонусу | 30,000 ARS | — | — | — |

---

## 8. ТЕХНІЧНІ ЗАЛЕЖНОСТІ

### 8.1 Має бути активовано у GR8 Tech

| Модуль | Статус | Необхідні дії |
| ---------------------------- | --------------------- | ------------------------------------------------------------------------------- |
| Smart Segmentation | Доступно, не активно | Зв'язатися з GR8 Tech для активації |
| Predictive Churn | Доступно, не активно | Зв'язатися з GR8 Tech для активації |
| Потокова передача подій в реальному часі | Невідомо | Перевірити затримку менше 5 секунд для подій депозиту |
| Інфраструктура App Push | Не налаштовано | Налаштувати SDK push-сповіщень у мобільному додатку |
| Коди причин невдачі депозиту | Невідомо | Перевірити, що GR8 Tech надає `INSUFF`/`METHOD`/`DECLINE`/`TIMEOUT`/`FRAUD` |

### 8.2 Необхідні експорти даних / API

| Інтеграція | Призначення | Напрямок |
| ------------------------ | ---------------------------------------- | --------------- |
| Експорт даних на рівні гравця | Валідація моделі сегментації | GR8 Tech → CRM |
| API каталогу ігор | Отримання назв ігор, ID, провайдерів | GR8 Tech → CRM |
| API управління бонусами | Програмне нарахування бонусів, FS, CC | CRM → GR8 Tech |
| API методів оплати | Отримання доступних методів оплати для гравця | GR8 Tech → CRM |
| Відстеження сесій | Статус сесії в реальному часі | GR8 Tech → CRM |

### 8.3 Необхідні креативні матеріали (для кожного ланцюга)

| Тип матеріалу | Потрібен для | Кількість |
| -------------------------------- | --------------------------------- | ------------------------------------------- |
| Email-шаблони | Усі email-комунікації | ~50+ (багаторазові з динамічними блоками контенту) |
| Дизайни in-app popup | Day 1, KYC, Платежі, Квести | ~20 |
| Дизайни in-app банерів | KYC Фаза 3, NC Feed елементи | ~10 |
| SMS-копі (іспанською) | Усі SMS-комунікації | ~40+ |
| Push-копі (іспанською) | App Push комунікації | ~30+ |
| Банери/мініатюри ігор | Персоналізовані рекомендації ігор | Для кожної гри з топ-10 |

---

## 9. ПРІОРИТЕТНИЙ ПОРЯДОК ВПРОВАДЖЕННЯ

Виконуйте в цьому порядку. Кожна фаза будується на попередній.

### Фаза 0: Фундамент (Тиждень 1–2)

- [ ] Активувати модуль Smart Segmentation
- [ ] Активувати модуль Predictive Churn
- [ ] Перевірити коректність спрацювання всіх подій у реальному часі (секція 1)
- [ ] Побудувати всі атрибути гравця (секція 2)
- [ ] Побудувати всі сегменти (секція 4)
- [ ] Налаштувати всі канали (секція 5)
- [ ] Встановити ліміти частоти (секція 6)
- [ ] Створити всі бонусні шаблони (секція 7)
- [ ] Налаштувати deep links (секція 5.6)

### Фаза 1: Найвищий вплив (Тиждень 3–4)

- [ ] 04 — Payment Failure Recovery (найдешевший, найвищий ROI)
- [ ] 01 — Day 1 Retention Layer (найбільша проблема утримання)
- [ ] 03 — KYC Completion Chain (зростання SMS-каналу)
- [ ] 05 — Welcome Bonus Ladder (виправити обрив D1→D2)

### Фаза 2: Відновлення Pre-FTD (Тиждень 5–6)

- [ ] 06 — Failed Deposits (20 комунікацій)
- [ ] 07 — No Bonus Cluster
- [ ] 08 — No Cashier Visited

### Фаза 3: Залучення (Тиждень 7–8)

- [ ] 10 — Engagement & Gamification (Квести, Loot Boxes)
- [ ] 11 — Loyalization
- [ ] 09 — Personalization

### Фаза 4: Завершення життєвого циклу (Тиждень 9–10)

- [ ] 02 — Pre-VIP Lifecycle
- [ ] 12 — Reactivation Matrix
- [ ] 13 — Channel Strategy execution

### Фаза 5: Платформа та зростання (Тиждень 11–12)

- [ ] 14 — Bonuses Landing Page Redesign
- [ ] 15 — Bonus Shop SKU Redesign
- [ ] 16 — Referral Program
- [ ] 17 — Smart Segmentation fine-tuning

---

## ДОДАТОК: Конвенція іменування кампаній

Використовуйте цей шаблон для всіх назв кампаній у GR8 Tech:

```
{chain_number}-{chain_abbrev}-{touch_id}-{channel}
```

Приклади:

- `01-D1RET-T1-EMAIL` — Day 1 Retention, Touch 1, Email
- `03-KYC-P1-01-POPUP` — KYC Chain, Phase 1, Touch 1, Popup
- `04-PFR-01A-POPUP` — Payment Failure Recovery, Touch 1A, Popup
- `12-REACT-A7-C1-EMAIL` — Reactivation, Active×7, Comm 1, Email

Це забезпечує відстежуваність усіх кампаній у CRM.
