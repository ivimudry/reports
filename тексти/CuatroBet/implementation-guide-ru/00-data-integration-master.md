# 00 — Интеграция данных и настройка платформы: Мастер-документ

**Цель:** Этот документ содержит КАЖДУЮ точку данных, событие, атрибут, сегмент и конфигурацию платформы, которые необходимо подготовить до создания любой автоматизации. Сначала завершите этот чек-лист — отдельные руководства по цепочкам ссылаются на элементы отсюда.

**Платформа:** GR8 Tech CRM
**Последнее обновление:** Апрель 2026

---

## СОДЕРЖАНИЕ

1. [События в реальном времени](#1-события-в-реальном-времени)
2. [Атрибуты игрока](#2-атрибуты-игрока)
3. [Расчётные метрики](#3-расчётные-метрики)
4. [Сегменты для построения](#4-сегменты-для-построения)
5. [Конфигурация каналов](#5-конфигурация-каналов)
6. [Лимиты частоты](#6-лимиты-частоты)
7. [Конфигурация бонусов](#7-конфигурация-бонусов)
8. [Технические зависимости](#8-технические-зависимости)
9. [Приоритетный порядок внедрения](#9-приоритетный-порядок-внедрения)

---

## 1. СОБЫТИЯ В РЕАЛЬНОМ ВРЕМЕНИ

Эти события должны срабатывать в реальном времени (задержка менее 5 секунд) от GR8 Tech к CRM-движку. Каждое событие должно нести указанные атрибуты payload.

### 1.1 Регистрация и аутентификация

| Название события        | Срабатывает когда                                               | Обязательный payload                                                                             |
| ----------------------- | --------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| `player_registered` | Завершено создание аккаунта                                     | `player_id`, `registration_timestamp`, `registration_source`, `country`, `device_type` |
| `session_start`     | Игрок открывает приложение/сайт                                 | `player_id`, `session_id`, `timestamp`, `device_type`, `referrer`                      |
| `session_end`       | Игрок закрывает приложение/покидает сайт (или таймаут 30 мин неактивности) | `player_id`, `session_id`, `timestamp`, `session_duration_seconds`, `pages_visited[]`  |

### 1.2 KYC и верификация

| Название события          | Срабатывает когда                              | Обязательный payload                                   |
| ------------------------- | ---------------------------------------------- | ------------------------------------------------------ |
| `email_verified`      | Игрок нажимает ссылку верификации              | `player_id`, `timestamp`, `email`            |
| `phone_verified`      | Игрок вводит правильный SMS-код                | `player_id`, `timestamp`, `phone_number`     |
| `documents_submitted` | Игрок загружает KYC-документы                  | `player_id`, `timestamp`, `document_types[]` |
| `documents_approved`  | KYC-проверка пройдена                          | `player_id`, `timestamp`                       |
| `documents_rejected`  | KYC-проверка не пройдена                       | `player_id`, `timestamp`, `rejection_reason` |

### 1.3 Депозиты и платежи

| Название события           | Срабатывает когда                                      | Обязательный payload                                                                                                                                                                            |
| -------------------------- | ------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `deposit_success`      | Депозит подтверждён                                    | `player_id`, `amount_ars`, `payment_method`, `deposit_number` (1-й, 2-й и т.д.), `timestamp`, `is_ftd` (boolean)                                                                 |
| `deposit_failed`       | Попытка депозита неудачна                              | `player_id`, `attempted_amount_ars`, `payment_method`, `failure_reason` (`INSUFF` / `METHOD` / `DECLINE` / `TIMEOUT` / `FRAUD`), `attempt_count_session`, `timestamp` |
| `cashier_opened`       | Игрок переходит на страницу депозита                   | `player_id`, `timestamp`, `session_id`                                                                                                                                                |
| `cashier_closed`       | Игрок покидает страницу депозита без внесения депозита | `player_id`, `timestamp`, `session_id`, `time_on_page_seconds`                                                                                                                      |
| `withdrawal_requested` | Игрок запрашивает вывод средств                        | `player_id`, `amount_ars`, `timestamp`                                                                                                                                                |

### 1.4 Геймплей

| Название события          | Срабатывает когда                         | Обязательный payload                                                                                                                                      |
| ------------------------- | ----------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `game_launched`       | Игрок открывает игру                      | `player_id`, `game_id`, `game_name`, `game_type` (`slots`/`live`/`sport`/`crash`), `provider`, `is_demo` (boolean), `timestamp` |
| `game_round_complete` | Раунд/спин завершён                       | `player_id`, `game_id`, `bet_amount_ars`, `win_amount_ars`, `timestamp`                                                                     |
| `wagering_progress`   | Обновление прогресса вейджера             | `player_id`, `bonus_id`, `wagered_amount`, `required_amount`, `percentage_complete`, `timestamp`                                          |
| `wagering_complete`   | Игрок завершает отыгрыш бонуса            | `player_id`, `bonus_id`, `timestamp`                                                                                                            |

### 1.5 Бонусы и промоакции

| Название события         | Срабатывает когда                       | Обязательный payload                                                                                |
| ------------------------ | --------------------------------------- | --------------------------------------------------------------------------------------------------- |
| `bonus_claimed`      | Игрок активирует бонус                  | `player_id`, `bonus_id`, `bonus_type`, `bonus_value_ars`, `timestamp`                 |
| `bonus_expired`      | Истекает срок действия бонуса           | `player_id`, `bonus_id`, `timestamp`                                                      |
| `free_spins_awarded` | FS зачислены игроку                     | `player_id`, `spin_count`, `game_id`, `source` (welcome/quest/shop/etc.), `timestamp` |
| `free_spins_used`    | Игрок использует FS                     | `player_id`, `spin_count`, `game_id`, `winnings_ars`, `timestamp`                     |
| `loot_box_earned`    | Игрок получает лутбокс                  | `player_id`, `timestamp`                                                                    |
| `loot_box_opened`    | Игрок открывает лутбокс                 | `player_id`, `reward_type`, `reward_value`, `timestamp`                                 |
| `lucky_wheel_spin`   | Игрок крутит Lucky Wheel                | `player_id`, `wheel_tier` (`silver`/`gold`/`platinum`), `reward`, `timestamp`     |

### 1.6 Лояльность и квесты

| Название события          | Срабатывает когда                             | Обязательный payload                                                                             |
| ------------------------- | --------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| `mission_completed`   | Игрок выполняет миссию лояльности             | `player_id`, `mission_id`, `cc_earned`, `timestamp`                                  |
| `quest_progress`      | Достигнута контрольная точка квеста           | `player_id`, `quest_id`, `quest_name`, `step_current`, `step_total`, `timestamp` |
| `quest_completed`     | Все шаги квеста выполнены                     | `player_id`, `quest_id`, `quest_name`, `rewards[]`, `timestamp`                    |
| `loyalty_tier_change` | Игрок перемещается вверх/вниз по уровням      | `player_id`, `old_tier`, `new_tier`, `timestamp`                                     |
| `cc_earned`           | Cuatro Coins зачислены                        | `player_id`, `amount_cc`, `source`, `timestamp`                                      |
| `cc_spent`            | Cuatro Coins использованы                     | `player_id`, `amount_cc`, `item_id`, `timestamp`                                     |

### 1.7 Рефералы

| Название события              | Срабатывает когда                             | Обязательный payload                                       |
| ----------------------------- | --------------------------------------------- | ---------------------------------------------------------- |
| `referral_link_generated` | Игрок создаёт реферальную ссылку              | `player_id`, `referral_code`, `timestamp`        |
| `referral_registered`     | Приглашённый игрок регистрируется             | `referrer_id`, `referred_player_id`, `timestamp` |
| `referral_qualified`      | Приглашённый игрок выполняет STD              | `referrer_id`, `referred_player_id`, `timestamp` |

### 1.8 Коммуникации

| Название события      | Срабатывает когда                              | Обязательный payload                                            |
| --------------------- | ---------------------------------------------- | --------------------------------------------------------------- |
| `email_opened`    | Игрок открывает email                          | `player_id`, `campaign_id`, `timestamp`               |
| `email_clicked`   | Игрок нажимает ссылку в email                  | `player_id`, `campaign_id`, `link_url`, `timestamp` |
| `sms_delivered`   | SMS доставлено оператору                       | `player_id`, `campaign_id`, `timestamp`               |
| `push_opened`     | Игрок нажимает push-уведомление                | `player_id`, `campaign_id`, `timestamp`               |
| `popup_shown`     | In-app popup отображён                         | `player_id`, `campaign_id`, `timestamp`               |
| `popup_clicked`   | Игрок нажимает CTA в popup                     | `player_id`, `campaign_id`, `timestamp`               |
| `popup_dismissed` | Игрок закрывает popup                          | `player_id`, `campaign_id`, `timestamp`               |

---

## 2. АТРИБУТЫ ИГРОКА

Эти атрибуты должны храниться и быть доступны для запросов в CRM для сегментации, персонализации и логики путешествий.

### 2.1 Идентификация

| Атрибут               | Тип      | Источник                    | Примечания                          |
| --------------------- | -------- | --------------------------- | ----------------------------------- |
| `player_id`         | String   | GR8 Tech                    | Первичный ключ                      |
| `email`             | String   | Регистрация                 |                                     |
| `phone_number`      | String   | Регистрация/KYC             |                                     |
| `first_name`        | String   | Регистрация                 | Для токенов персонализации          |
| `country`           | String   | Регистрация                 | Должно быть "AR" для Аргентины     |
| `language`          | String   | Регистрация                 | По умолчанию "es-AR"               |
| `registration_date` | DateTime | Регистрация                 |                                     |
| `birthday`          | Date     | KYC/Профиль                 | Для бонуса на день рождения        |
| `zodiac_sign`       | String   | Рассчитывается из birthday  | Для зодиакального бонуса           |

### 2.2 KYC-статус

| Атрибут                 | Тип     | Значения                                             | Примечания                                             |
| ----------------------- | ------- | ---------------------------------------------------- | ------------------------------------------------------ |
| `email_verified`      | Boolean | true/false                                           |                                                        |
| `phone_verified`      | Boolean | true/false                                           | Включает SMS-канал                                     |
| `documents_submitted` | Boolean | true/false                                           |                                                        |
| `documents_status`    | Enum    | `none` / `pending` / `approved` / `rejected` |                                                        |
| `kyc_level`           | Enum    | `unverified` / `partial` / `full`              | partial = email+phone, full = документы подтверждены   |

### 2.3 Финансовые

| Атрибут                          | Тип      | Частота обновления  | Примечания                                  |
| -------------------------------- | -------- | ------------------- | ------------------------------------------- |
| `deposit_count`              | Integer  | При каждом депозите | Общее количество депозитов за всё время     |
| `cumulative_deposits_ars`    | Float    | При каждом депозите | Сумма депозитов за всё время                |
| `last_deposit_date`          | DateTime | При каждом депозите |                                             |
| `last_deposit_amount_ars`    | Float    | При каждом депозите |                                             |
| `ftd_date`                   | DateTime | При первом депозите | Null, если FTD нет                          |
| `ftd_amount_ars`             | Float    | При первом депозите |                                             |
| `std_date`                   | DateTime | При втором депозите | Null, если STD нет                          |
| `average_deposit_ars`        | Float    | Расчётный           | `cumulative_deposits_ars / deposit_count` |
| `payment_methods_used[]`     | Array    | При каждом депозите | Список использованных методов               |
| `last_withdrawal_date`       | DateTime | При выводе          |                                             |
| `cumulative_withdrawals_ars` | Float    | При выводе          |                                             |
| `ggr_ars`                    | Float    | Расчёт ежедневно    | Gross Gaming Revenue                        |

### 2.4 Геймплей

| Атрибут                             | Тип      | Частота обновления  | Примечания                                                 |
| ----------------------------------- | -------- | ------------------- | ---------------------------------------------------------- |
| `game_preference`               | Enum     | Расчёт еженедельно | `slots` / `live` / `aviator` / `mixed` / `sport` |
| `most_played_game_id`           | String   | Расчёт еженедельно |                                                            |
| `most_played_game_name`         | String   | Расчёт еженедельно | Для персонализации FS                                      |
| `top_3_games[]`                 | Array    | Расчёт еженедельно | Game ID                                                    |
| `total_rounds_played`           | Integer  | Реальное время      |                                                            |
| `total_wagered_ars`             | Float    | Реальное время      |                                                            |
| `biggest_win_ars`               | Float    | Реальное время      | Для персонализации годовщины                               |
| `last_game_date`                | DateTime | Реальное время      |                                                            |
| `last_session_date`             | DateTime | Реальное время      |                                                            |
| `last_session_duration_seconds` | Integer  | Реальное время      |                                                            |
| `has_played_demo`               | Boolean  | Реальное время      | Для пути C «No Cashier Visited»                            |

### 2.5 Жизненный цикл и ценность

| Атрибут                        | Тип            | Частота обновления | Примечания                                                 |
| ------------------------------ | -------------- | ------------------ | ---------------------------------------------------------- |
| `lifecycle_stage`          | Enum           | Реальное время     | См. Ось 1 в разделе 17                                    |
| `value_tier`               | Enum           | Ежедневно          | `micro` / `low` / `mid` / `high` / `previp_plus` |
| `days_since_last_activity` | Integer        | Ежедневно          | Для матрицы реактивации                                    |
| `days_since_registration`  | Integer        | Ежедневно          |                                                            |
| `engagement_history`       | Enum           | Еженедельно        | `active` / `passive` — для матрицы реактивации        |
| `churn_score`              | Float (0–100) | Ежедневно          | Из модели Predictive Churn                                 |
| `churn_risk_level`         | Enum           | Ежедневно          | `healthy` / `watch` / `at_risk` / `critical`       |

### 2.6 Лояльность

| Атрибут                     | Тип      | Примечания                                            |
| --------------------------- | -------- | ----------------------------------------------------- |
| `loyalty_enrolled`      | Boolean  |                                                       |
| `loyalty_tier`          | Enum     | `premium` / `prestige` / `maestro` / `legend` |
| `cc_balance`            | Integer  | Текущий баланс Cuatro Coins                           |
| `cc_lifetime_earned`    | Integer  |                                                       |
| `cc_last_spent_date`    | DateTime | Для предупреждений об истечении CC                     |
| `missions_completed_7d` | Integer  | Для классификации active/passive                      |
| `last_mission_date`     | DateTime |                                                       |

### 2.7 Предпочтения коммуникации

| Атрибут                        | Тип     | Примечания                                              |
| ------------------------------ | ------- | ------------------------------------------------------- |
| `email_opt_in`             | Boolean |                                                         |
| `sms_opt_in`               | Boolean | Автоматически при верификации телефона                   |
| `push_opt_in`              | Boolean |                                                         |
| `preferred_contact_method` | Enum    | `sms` / `email` / `push`                         |
| `email_engagement_30d`     | Enum    | `high` / `low` / `zero` — на основе открытий/кликов |
| `messages_today_count`     | Integer | Для контроля лимитов частоты                            |

### 2.8 Состояние бонуса

| Атрибут                         | Тип     | Примечания                                                |
| ------------------------------- | ------- | --------------------------------------------------------- |
| `welcome_bonus_claimed`     | Boolean |                                                           |
| `welcome_bonus_status`      | Enum    | `available` / `claimed` / `completed` / `expired` |
| `active_bonus_id`           | String  | Текущий активный бонус                                    |
| `active_bonus_wagering_pct` | Float   | 0–100% выполнения вейджера                               |
| `welcome_ladder_step`       | Integer | 1–10 (какой депозит в лестнице)                          |

### 2.9 Рефералы

| Атрибут                          | Тип     | Примечания                         |
| -------------------------------- | ------- | ---------------------------------- |
| `referral_code`              | String  | Уникальный код игрока              |
| `referrals_successful_count` | Integer | Квалифицированные рефералы по STD  |
| `referrals_successful_month` | Integer | Количество за этот месяц (для лимита) |
| `was_referred`               | Boolean | Игрок пришёл по реферальной ссылке |
| `referred_by_player_id`      | String  |                                    |

---

## 3. РАСЧЁТНЫЕ МЕТРИКИ

Эти метрики должны рассчитываться GR8 Tech и обновляться по указанному расписанию.

| Метрика                  | Формула                                                                                                          | Обновление        | Используется в          |
| ------------------------ | ---------------------------------------------------------------------------------------------------------------- | ----------------- | ----------------------- |
| `value_tier`           | На основе `cumulative_deposits_ars`: <5K=micro, 5–25K=low, 25–75K=mid, 75–150K=high, >150K=previp+             | Ежедневно         | Масштабирование офферов |
| `lifecycle_stage`      | На основе правил: количество депозитов, последняя активность, сумма депозитов                                    | Реальное время    | Вход/выход из путешествий |
| `game_preference`      | >70% раундов в одном типе = этот тип; иначе "mixed"                                                             | Еженедельно       | Персонализация контента |
| `engagement_history`   | ≥1 миссия за 7д = "active"; иначе "passive"                                                                     | Ежедневно         | Матрица реактивации     |
| `churn_score`          | Результат модели Predictive Churn                                                                                | Ежедневно         | Ускорение тайминга      |
| `email_engagement_30d` | Открытия за 30д: ≥3 = high; 1–2 = low; 0 = zero                                                                | Ежедневно         | Выбор канала            |
| `zodiac_sign`          | Рассчитывается из поля `birthday`                                                                              | При обновлении профиля | Зодиакальный бонус  |
| `days_inactive`        | `today - max(last_deposit_date, last_session_date)`                                                              | Ежедневно         | Триггеры реактивации    |
| `bonus_cost_pct_ggr`   | `total_bonus_paid / ggr * 100`                                                                                   | Еженедельно       | Мониторинг расходов     |

---

## 4. СЕГМЕНТЫ ДЛЯ ПОСТРОЕНИЯ

Создайте эти сегменты в движке сегментации GR8 Tech. На них ссылаются все руководства по внедрению.

### 4.1 Сегменты жизненного цикла

| ID сегмента     | Название           | Правила                                                                    |
| --------------- | ------------------ | -------------------------------------------------------------------------- |
| `SEG-REG`     | Registered, No FTD | `deposit_count = 0`                                                      |
| `SEG-FTD`     | FTD Done, <24h     | `deposit_count = 1 AND hours_since_ftd < 24`                             |
| `SEG-D1LAYER` | In Day 1 Layer     | `deposit_count >= 1 AND days_since_ftd <= 3`                             |
| `SEG-PRESTD`  | Pre-STD            | `deposit_count = 1 AND days_since_ftd > 1`                               |
| `SEG-REGULAR` | Regular            | `deposit_count >= 2 AND days_inactive < 14`                              |
| `SEG-PREVIP`  | Pre-VIP            | `cumulative_deposits_ars >= 685000AND cumulative_deposits_ars < 1370000` |
| `SEG-VIP`     | VIP                | `cumulative_deposits_ars >= 1370000`                                      |

### 4.2 KYC-сегменты

| ID сегмента                 | Название           | Правила                                                            |
| --------------------------- | ------------------ | ------------------------------------------------------------------ |
| `SEG-KYC-NONE`          | Unverified         | `kyc_level = "unverified"`                                       |
| `SEG-KYC-EMAIL-PENDING` | Email Not Verified | `email_verified = false`                                         |
| `SEG-KYC-PHONE-PENDING` | Phone Not Verified | `phone_verified = false`                                         |
| `SEG-KYC-DOCS-PENDING`  | Docs Not Submitted | `documents_status = "none" AND cumulative_deposits_ars >= 69000` |
| `SEG-KYC-FULL`          | Fully Verified     | `kyc_level = "full"`                                             |

### 4.3 Поведенческие сегменты

| ID сегмента                 | Название                           | Правила                                                                                       |
| --------------------------- | ---------------------------------- | --------------------------------------------------------------------------------------------- |
| `SEG-BOUNCE`            | Bounced (session <60s, no cashier) | `last_session_duration < 60 AND cashier_opened = false`                                     |
| `SEG-LONG-NO-CASHIER`   | Long Session, No Cashier           | `last_session_duration > 600 AND cashier_opened = false`                                    |
| `SEG-FS-NO-DEP`         | Played Free Spins, No Deposit      | `has_played_demo = true AND deposit_count = 0`                                              |
| `SEG-BONUS-MISSED`      | Missed Welcome Bonus               | `deposit_count = 0 AND welcome_bonus_claimed = false AND hours_since_registration >= 1`     |
| `SEG-BONUS-DECLINED`    | Declined Welcome Bonus             | `welcome_bonus_status = "declined" OR (bonus_flow_bypassed = true)`                         |
| `SEG-CASHIER-ABANDONED` | Opened Cashier, No Deposit         | Событие `cashier_closed` без последующего `deposit_success` в течение 30 мин               |

### 4.4 Сегменты реактивации

| ID сегмента         | Название                 | Правила                                                                       |
| ------------------- | ------------------------ | ----------------------------------------------------------------------------- |
| `SEG-REACT-A7`  | Active × 7 Days         | `engagement_history = "active" AND days_inactive BETWEEN 7 AND 13`          |
| `SEG-REACT-A14` | Active × 14 Days        | `engagement_history = "active" AND days_inactive BETWEEN 14 AND 20`         |
| `SEG-REACT-A21` | Active × 21+ Days       | `engagement_history = "active" AND days_inactive >= 21`                     |
| `SEG-REACT-P7`  | Passive × 7 Days        | `engagement_history = "passive" AND days_inactive BETWEEN 7 AND 13`         |
| `SEG-REACT-P14` | Passive × 14 Days       | `engagement_history = "passive" AND days_inactive BETWEEN 14 AND 20`        |
| `SEG-REACT-P21` | Passive × 21+ Days      | `engagement_history = "passive" AND days_inactive >= 21`                    |
| `SEG-REACT-VNR` | Verified But No Activity | `kyc_level = "full" AND deposit_count = 0 AND days_since_verification >= 3` |

### 4.5 Сегменты по уровню ценности

| ID сегмента         | Название | Правила                                              |
| ------------------- | -------- | ---------------------------------------------------- |
| `SEG-VAL-MICRO`  | Micro    | `cumulative_deposits_ars < 23000`                   |
| `SEG-VAL-LOW`    | Low      | `cumulative_deposits_ars BETWEEN 23000 AND 114000`   |
| `SEG-VAL-MID`    | Mid      | `cumulative_deposits_ars BETWEEN 114000 AND 343000`  |
| `SEG-VAL-HIGH`   | High     | `cumulative_deposits_ars BETWEEN 343000 AND 685000` |
| `SEG-VAL-PREVIP` | Pre-VIP+ | `cumulative_deposits_ars >= 685000`                |

### 4.6 Сегменты по игровым предпочтениям

| ID сегмента           | Название      | Правила                         |
| --------------------- | ------------- | ------------------------------- |
| `SEG-GAME-SLOTS`   | Slots-Heavy   | `game_preference = "slots"`   |
| `SEG-GAME-LIVE`    | Live-Heavy    | `game_preference = "live"`    |
| `SEG-GAME-AVIATOR` | Aviator/Crash | `game_preference = "aviator"` |
| `SEG-GAME-MIXED`   | Mixed         | `game_preference = "mixed"`   |

### 4.7 Сегменты вовлечённости

| ID сегмента          | Название              | Правила                                                                                     |
| -------------------- | --------------------- | ------------------------------------------------------------------------------------------- |
| `SEG-ENG-HIGH`    | High Email Engagement | `email_engagement_30d = "high"`                                                           |
| `SEG-ENG-LOW`     | Low Email Engagement  | `email_engagement_30d = "low"`                                                            |
| `SEG-ENG-ZERO`    | Zero Engagement       | `email_engagement_30d = "zero"`                                                           |
| `SEG-LOY-ACTIVE`  | Active Loyalty        | `loyalty_enrolled = true AND missions_completed_7d >= 1`                                  |
| `SEG-LOY-PASSIVE` | Passive Loyalty       | `loyalty_enrolled = true AND missions_completed_7d = 0 AND days_since_last_mission <= 30` |

---

## 5. КОНФИГУРАЦИЯ КАНАЛОВ

### 5.1 SMS

| Настройка          | Значение                                                     |
| ------------------ | ------------------------------------------------------------ |
| Провайдер          | Существующий SMS-шлюз GR8 Tech                               |
| Sender ID          | "CuatroBet"                                                  |
| Тихие часы         | 00:00–08:00 ART                                             |
| Макс. SMS/день/игрок | См. лимиты частоты ниже                                   |
| Триггер opt-in     | Автоматически при событии `phone_verified`                 |
| Сокращатель ссылок | Включить с трекинговыми UTM                                  |
| UTM по умолчанию   | `utm_source=sms&utm_medium=crm&utm_campaign={campaign_id}` |

### 5.2 Email

| Настройка     | Значение                                                       |
| ------------- | -------------------------------------------------------------- |
| From address  | `hola@cuatrobet.com` (или аналог)                            |
| From name     | "CuatroBet"                                                    |
| Reply-to      | `soporte@cuatrobet.com`                                      |
| UTM по умолчанию | `utm_source=email&utm_medium=crm&utm_campaign={campaign_id}` |
| Отписка       | Обязательна по закону — включить в footer                      |
| Preheader     | Должен быть настроен для каждой кампании                       |

### 5.3 In-App Popup (NC Pop-Up)

| Настройка                            | Значение                                                    |
| ------------------------------------ | ----------------------------------------------------------- |
| Макс. 1 popup за сессию             | Принудительно                                               |
| Без popup в первые 60 секунд        | Принудительно                                               |
| Поведение при закрытии              | Закрыть и не показывать снова для этой кампании             |
| Правила приоритета                  | Если несколько popup в очереди → показать оффер с наибольшей ценностью |

### 5.4 In-App Feed (NC Feed)

| Настройка                                | Значение                                      |
| ---------------------------------------- | --------------------------------------------- |
| Макс. 2 элемента на игрока в день       | Принудительно                                 |
| Мин. 4 часа между элементами            | Принудительно                                 |
| Целевая аудитория                       | Только активные игроки (сессия за последние 48ч) |
| Дневной лимит объёма                    | 10 000 всего отправок (снижено с 25 700)      |

### 5.5 Web Push

| Настройка         | Значение                                                                                                         |
| ----------------- | ---------------------------------------------------------------------------------------------------------------- |
| Статус            | **АКТИВИРОВАТЬ** — в настоящее время ноль отправок                                                        |
| Запрос opt-in     | Показывать после первого депозита (не при регистрации)                                                            |
| Стимул opt-in     | 100 CC за opt-in                                                                                                 |
| Тихие часы        | 00:00–08:00 ART                                                                                                 |
| Раскатка          | Неделя 1: настройка → Неделя 2: Day 1 Layer → Неделя 3: Post-FTD/Pre-VIP → Неделя 4: оценка → Неделя 5: полная |

### 5.6 Deep Links

Все CTA-ссылки в коммуникациях должны использовать deep links, открывающие правильную страницу в приложении/сайте:

| Deep Link                               | Назначение                                   | Используется в           |
| --------------------------------------- | -------------------------------------------- | ------------------------ |
| `{base_url}/cashier`                  | Страница депозита                            | Большинство CTA          |
| `{base_url}/cashier?method={method}`  | Страница депозита с предвыбранным методом    | Восстановление при сбое оплаты |
| `{base_url}/cashier?amount={amount}`  | Страница депозита с предзаполненной суммой   | Восстановление меньшей суммы |
| `{base_url}/game/{game_id}`           | Конкретная игра                              | Рекомендации игр         |
| `{base_url}/game/{game_id}?demo=true` | Демо-режим конкретной игры                   | Кластер без бонуса       |
| `{base_url}/bonuses`                  | Страница бонусов                             | Напоминания о бонусах    |
| `{base_url}/bonus-shop`               | Бонусный магазин                             | CTA для трат CC          |
| `{base_url}/missions`                 | Страница миссий лояльности                   | Коммуникации лояльности  |
| `{base_url}/profile/verify`           | Страница загрузки KYC                        | KYC-цепочка              |
| `{base_url}/lucky-wheel`              | Lucky Wheel                                  | Квесты/геймификация      |
| `{base_url}/referral`                 | Реферальная страница                         | Реферальные коммуникации |

---

## 6. ЛИМИТЫ ЧАСТОТЫ

Настройте эти правила как глобальные в GR8 Tech CRM.

| Сегмент                              | Макс. сообщений/день (все каналы суммарно) |
| ------------------------------------ | ------------------------------------------ |
| `SEG-REG` (Pre-FTD)              | 2                                          |
| `SEG-D1LAYER` (Day 1, первые 72ч) | 3                                          |
| `SEG-REGULAR`                    | 2                                          |
| `SEG-PREVIP` / `SEG-VIP`       | 2                                          |
| Сегменты реактивации                 | 1                                          |
| Транзакционные / Безопасность        | **Без ограничений** (нет лимита)    |

**Правило коллизий:** Если несколько кампаний срабатывают в один день для одного игрока и лимит достигнут → отправить только сообщение с наивысшим приоритетом / наибольшей ценностью. Остальные подавить.

**Kill switch:** Если open rate любого канала падает более чем на 25% неделя к неделе → автоматически приостановить новые кампании на этом канале, уведомить CRM-команду.

---

## 7. КОНФИГУРАЦИЯ БОНУСОВ

Эти шаблоны бонусов должны существовать в GR8 Tech до того, как автоматизации смогут на них ссылаться.

### 7.1 Welcome Ladder — Slots

| Bonus ID      | Депозит # | Match %             | FS Count | FS Game                | CC   | Wagering | Срок     |
| ------------- | --------- | ------------------- | -------- | ---------------------- | ---- | -------- | -------- |
| `WBL-S-D1`  | 1-й       | 120% (150% если >15K) | 50     | Gates of Olympus       | —   | 25×     | 7 дней   |
| `WBL-S-D2`  | 2-й       | 75%                 | 30       | Joker's Jewels         | —   | 20×     | 5 дней   |
| `WBL-S-D3`  | 3-й       | 60%                 | 25       | Jackpot Joker          | —   | 18×     | 5 дней   |
| `WBL-S-D4`  | 4-й       | 55%                 | 20       | 4 Supercharged Clovers | —   | 15×     | 5 дней   |
| `WBL-S-D5`  | 5-й       | 50%                 | 15       | Gold Party             | 200  | 15×     | 5 дней   |
| `WBL-S-D6`  | 6-й       | 60%                 | 30       | 3 Coin Volcanoes       | 300  | 15×     | 5 дней   |
| `WBL-S-D7`  | 7-й       | 65%                 | 35       | Rush for Gold          | 400  | 15×     | 5 дней   |
| `WBL-S-D8`  | 8-й       | 70%                 | 40       | Gates of Olympus 1000  | 500  | 15×     | 5 дней   |
| `WBL-S-D9`  | 9-й       | 80%                 | 50       | Топовый слот игрока    | 600  | 12×     | 7 дней   |
| `WBL-S-D10` | 10-й      | 100%                | 60       | Топовый слот игрока    | 1000 | 10×     | 7 дней   |

### 7.2 Welcome Ladder — Live Casino

Та же структура, что и для Slots, но с Bonus Cash вместо FS (см. спецификацию задачи 05).

### 7.3 Welcome Ladder — Sport

Та же структура, но с Free Bets при минимальном коэффициенте 1.80 (см. спецификацию задачи 05).

### 7.4 Бонусы за KYC-верификацию

| Bonus ID                  | Триггер                                           | Сумма     | Wagering | Примечания |
| ------------------------- | ------------------------------------------------- | --------- | -------- | ---------- |
| `KYC-EMAIL-REWARD`      | Email подтверждён                                 | 2,300 ARS   | None     | Мгновенно  |
| `KYC-PHONE-REWARD`      | Телефон подтверждён                               | 2,300 ARS   | None     | Мгновенно  |
| `KYC-DOCS-REWARD-EARLY` | Документы подтверждены до порога 22.5K            | 4,600 ARS | None     |            |
| `KYC-DOCS-REWARD-HARD`  | Документы подтверждены на пороге/после 22.5K      | 9,000 ARS | None     |            |

### 7.5 Шаблоны офферов реактивации

Создайте шаблоны офферов, масштабируемые по уровню ценности. Полную матрицу см. в руководстве по внедрению раздела 12.

### 7.6 Правила вейджера

| Правило                        | Slots          | Live | Table | Sport |
| ------------------------------ | -------------- | ---- | ----- | ----- |
| Вклад %                       | 100%           | 10%  | 5%    | 100%  |
| Макс. ставка при отыгрыше     | 7,000 ARS/спин | —   | —    | —    |
| Макс. бонусный баланс         | 137,000 ARS     | —   | —    | —    |

---

## 8. ТЕХНИЧЕСКИЕ ЗАВИСИМОСТИ

### 8.1 Необходимо активировать в GR8 Tech

| Модуль                              | Статус                     | Необходимое действие                                                                    |
| ----------------------------------- | -------------------------- | --------------------------------------------------------------------------------------- |
| Smart Segmentation                  | Доступен, не активен       | Связаться с GR8 Tech для активации                                                      |
| Predictive Churn                    | Доступен, не активен       | Связаться с GR8 Tech для активации                                                      |
| Потоковая передача событий в реальном времени | Неизвестно         | Проверить задержку менее 5 секунд для событий депозитов                                  |
| Инфраструктура Web Push             | Не настроена               | Настроить SDK push-уведомлений в мобильном приложении                                   |
| Коды причин сбоя депозита           | Неизвестно                 | Проверить, что GR8 Tech предоставляет `INSUFF`/`METHOD`/`DECLINE`/`TIMEOUT`/`FRAUD` |

### 8.2 Необходимые экспорты данных / API

| Интеграция                  | Назначение                                          | Направление     |
| --------------------------- | --------------------------------------------------- | --------------- |
| Экспорт данных на уровне игрока | Валидация модели сегментации                    | GR8 Tech → CRM |
| API каталога игр            | Получение названий игр, ID, провайдеров             | GR8 Tech → CRM |
| API управления бонусами     | Программное начисление бонусов, FS, CC              | CRM → GR8 Tech |
| API методов оплаты          | Получение доступных методов оплаты для каждого игрока | GR8 Tech → CRM |
| Отслеживание сессий         | Статус сессий в реальном времени                    | GR8 Tech → CRM |

### 8.3 Необходимые креативные материалы (по цепочкам)

| Тип материала                        | Необходим для                     | Количество                                      |
| ------------------------------------ | --------------------------------- | ----------------------------------------------- |
| Email-шаблоны                        | Все email-коммуникации            | ~50+ (переиспользуемые с динамическими блоками) |
| Дизайны in-app popup                 | Day 1, KYC, Payment, Quests       | ~20                                             |
| Дизайны in-app баннеров              | KYC Phase 3, NC Feed items        | ~10                                             |
| SMS-копи (испанский)                 | Все SMS-коммуникации              | ~40+                                            |
| Push-уведомления копи (испанский)    | Web Push коммуникации             | ~30+                                            |
| Баннеры/миниатюры игр                | Персонализированные рекомендации игр | По каждой игре из топ-10                     |

---

## 9. ПРИОРИТЕТНЫЙ ПОРЯДОК ВНЕДРЕНИЯ

Выполняйте в указанном порядке. Каждая фаза основывается на предыдущей.

### Фаза 0: Фундамент (Неделя 1–2)

- [ ] Активировать модуль Smart Segmentation
- [ ] Активировать модуль Predictive Churn
- [ ] Проверить корректность срабатывания всех событий реального времени (раздел 1)
- [ ] Создать все атрибуты игроков (раздел 2)
- [ ] Создать все сегменты (раздел 4)
- [ ] Настроить все каналы (раздел 5)
- [ ] Установить лимиты частоты (раздел 6)
- [ ] Создать все шаблоны бонусов (раздел 7)
- [ ] Настроить deep links (раздел 5.6)

### Фаза 1: Наибольшее влияние (Неделя 3–4)

- [ ] 04 — Payment Failure Recovery (самое дешёвое, максимальный ROI)
- [ ] 01 — Day 1 Retention Layer (главная проблема удержания)
- [ ] 03 — KYC Completion Chain (рост SMS-канала)
- [ ] 05 — Welcome Bonus Ladder (исправление обрыва D1→D2)

### Фаза 2: Восстановление Pre-FTD (Неделя 5–6)

- [ ] 06 — Failed Deposits (20 коммуникаций)
- [ ] 07 — No Bonus Cluster
- [ ] 08 — No Cashier Visited

### Фаза 3: Вовлечение (Неделя 7–8)

- [ ] 10 — Engagement & Gamification (Quests, Loot Boxes)
- [ ] 11 — Loyalization
- [ ] 09 — Personalization

### Фаза 4: Завершение жизненного цикла (Неделя 9–10)

- [ ] 02 — Pre-VIP Lifecycle
- [ ] 12 — Reactivation Matrix
- [ ] 13 — Channel Strategy execution

### Фаза 5: Платформа и рост (Неделя 11–12)

- [ ] 14 — Bonuses Landing Page Redesign
- [ ] 15 — Bonus Shop SKU Redesign
- [ ] 16 — Referral Program
- [ ] 17 — Smart Segmentation fine-tuning

---

## ПРИЛОЖЕНИЕ: Конвенция именования кампаний

Используйте этот паттерн для всех названий кампаний в GR8 Tech:

```
{chain_number}-{chain_abbrev}-{touch_id}-{channel}
```

Примеры:

- `01-D1RET-T1-EMAIL` — Day 1 Retention, Touch 1, Email
- `03-KYC-P1-01-POPUP` — KYC Chain, Phase 1, Touch 1, Popup
- `04-PFR-01A-POPUP` — Payment Failure Recovery, Touch 1A, Popup
- `12-REACT-A7-C1-EMAIL` — Reactivation, Active×7, Comm 1, Email

Это обеспечивает отслеживаемость всех кампаний в CRM.
