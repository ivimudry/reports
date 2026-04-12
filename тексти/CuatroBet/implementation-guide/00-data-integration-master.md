# 00 — Data Integration & Platform Setup Master Document

**Purpose:** This document lists EVERY data point, event, attribute, segment, and platform configuration required before any automation can be built. Complete this checklist first — individual chain guides reference items from here.

**Platform:** GR8 Tech CRM
**Last Updated:** April 2026

---

## TABLE OF CONTENTS

1. [Real-Time Events](#1-real-time-events)
2. [Player Attributes](#2-player-attributes)
3. [Calculated Metrics](#3-calculated-metrics)
4. [Segments to Build](#4-segments-to-build)
5. [Channel Configuration](#5-channel-configuration)
6. [Frequency Caps](#6-frequency-caps)
7. [Bonus Configuration](#7-bonus-configuration)
8. [Technical Dependencies](#8-technical-dependencies)
9. [Implementation Priority Order](#9-implementation-priority-order)

---

## 1. REAL-TIME EVENTS

These events must fire in real-time (sub-5-second latency) from GR8 Tech to the CRM engine. Each event must carry the listed payload attributes.

### 1.1 Registration & Authentication

| Event Name            | Fires When                                                   | Required Payload                                                                                 |
| --------------------- | ------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `player_registered` | Account creation complete                                    | `player_id`, `registration_timestamp`, `registration_source`, `country`, `device_type` |
| `session_start`     | Player opens app/site                                        | `player_id`, `session_id`, `timestamp`, `device_type`, `referrer`                      |
| `session_end`       | Player closes app/leaves site (or 30 min inactivity timeout) | `player_id`, `session_id`, `timestamp`, `session_duration_seconds`, `pages_visited[]`  |

### 1.2 KYC & Verification

| Event Name              | Fires When                      | Required Payload                                   |
| ----------------------- | ------------------------------- | -------------------------------------------------- |
| `email_verified`      | Player clicks verification link | `player_id`, `timestamp`, `email`            |
| `phone_verified`      | Player enters correct SMS code  | `player_id`, `timestamp`, `phone_number`     |
| `documents_submitted` | Player uploads KYC documents    | `player_id`, `timestamp`, `document_types[]` |
| `documents_approved`  | KYC review passes               | `player_id`, `timestamp`                       |
| `documents_rejected`  | KYC review fails                | `player_id`, `timestamp`, `rejection_reason` |

### 1.3 Deposits & Payments

| Event Name               | Fires When                                    | Required Payload                                                                                                                                                                            |
| ------------------------ | --------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `deposit_success`      | Deposit confirmed                             | `player_id`, `amount_ars`, `payment_method`, `deposit_number` (1st, 2nd, etc.), `timestamp`, `is_ftd` (boolean)                                                                 |
| `deposit_failed`       | Deposit attempt fails                         | `player_id`, `attempted_amount_ars`, `payment_method`, `failure_reason` (`INSUFF` / `METHOD` / `DECLINE` / `TIMEOUT` / `FRAUD`), `attempt_count_session`, `timestamp` |
| `cashier_opened`       | Player navigates to deposit page              | `player_id`, `timestamp`, `session_id`                                                                                                                                                |
| `cashier_closed`       | Player leaves deposit page without depositing | `player_id`, `timestamp`, `session_id`, `time_on_page_seconds`                                                                                                                      |
| `withdrawal_requested` | Player requests withdrawal                    | `player_id`, `amount_ars`, `timestamp`                                                                                                                                                |

### 1.4 Gameplay

| Event Name              | Fires When                      | Required Payload                                                                                                                                      |
| ----------------------- | ------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| `game_launched`       | Player opens a game             | `player_id`, `game_id`, `game_name`, `game_type` (`slots`/`live`/`sport`/`crash`), `provider`, `is_demo` (boolean), `timestamp` |
| `game_round_complete` | Round/spin finishes             | `player_id`, `game_id`, `bet_amount_ars`, `win_amount_ars`, `timestamp`                                                                     |
| `wagering_progress`   | Wagering requirement updates    | `player_id`, `bonus_id`, `wagered_amount`, `required_amount`, `percentage_complete`, `timestamp`                                          |
| `wagering_complete`   | Player completes bonus wagering | `player_id`, `bonus_id`, `timestamp`                                                                                                            |

### 1.5 Bonus & Promotions

| Event Name             | Fires When                 | Required Payload                                                                                |
| ---------------------- | -------------------------- | ----------------------------------------------------------------------------------------------- |
| `bonus_claimed`      | Player activates a bonus   | `player_id`, `bonus_id`, `bonus_type`, `bonus_value_ars`, `timestamp`                 |
| `bonus_expired`      | Bonus validity period ends | `player_id`, `bonus_id`, `timestamp`                                                      |
| `free_spins_awarded` | FS credited to player      | `player_id`, `spin_count`, `game_id`, `source` (welcome/quest/shop/etc.), `timestamp` |
| `free_spins_used`    | Player uses FS             | `player_id`, `spin_count`, `game_id`, `winnings_ars`, `timestamp`                     |
| `loot_box_earned`    | Player earns a loot box    | `player_id`, `timestamp`                                                                    |
| `loot_box_opened`    | Player opens a loot box    | `player_id`, `reward_type`, `reward_value`, `timestamp`                                 |
| `lucky_wheel_spin`   | Player spins Lucky Wheel   | `player_id`, `wheel_tier` (`silver`/`gold`/`platinum`), `reward`, `timestamp`     |

### 1.6 Loyalty & Quests

| Event Name              | Fires When                         | Required Payload                                                                             |
| ----------------------- | ---------------------------------- | -------------------------------------------------------------------------------------------- |
| `mission_completed`   | Player completes a loyalty mission | `player_id`, `mission_id`, `cc_earned`, `timestamp`                                  |
| `quest_progress`      | Quest checkpoint reached           | `player_id`, `quest_id`, `quest_name`, `step_current`, `step_total`, `timestamp` |
| `quest_completed`     | All quest steps done               | `player_id`, `quest_id`, `quest_name`, `rewards[]`, `timestamp`                    |
| `loyalty_tier_change` | Player moves up/down tiers         | `player_id`, `old_tier`, `new_tier`, `timestamp`                                     |
| `cc_earned`           | Cuatro Coins credited              | `player_id`, `amount_cc`, `source`, `timestamp`                                      |
| `cc_spent`            | Cuatro Coins redeemed              | `player_id`, `amount_cc`, `item_id`, `timestamp`                                     |

### 1.7 Referral

| Event Name                  | Fires When                    | Required Payload                                       |
| --------------------------- | ----------------------------- | ------------------------------------------------------ |
| `referral_link_generated` | Player creates referral link  | `player_id`, `referral_code`, `timestamp`        |
| `referral_registered`     | Referred player signs up      | `referrer_id`, `referred_player_id`, `timestamp` |
| `referral_qualified`      | Referred player completes STD | `referrer_id`, `referred_player_id`, `timestamp` |

### 1.8 Communication

| Event Name          | Fires When                    | Required Payload                                            |
| ------------------- | ----------------------------- | ----------------------------------------------------------- |
| `email_opened`    | Player opens email            | `player_id`, `campaign_id`, `timestamp`               |
| `email_clicked`   | Player clicks link in email   | `player_id`, `campaign_id`, `link_url`, `timestamp` |
| `sms_delivered`   | SMS delivered to carrier      | `player_id`, `campaign_id`, `timestamp`               |
| `push_opened`     | Player taps push notification | `player_id`, `campaign_id`, `timestamp`               |
| `popup_shown`     | In-app popup displayed        | `player_id`, `campaign_id`, `timestamp`               |
| `popup_clicked`   | Player clicks popup CTA       | `player_id`, `campaign_id`, `timestamp`               |
| `popup_dismissed` | Player closes popup           | `player_id`, `campaign_id`, `timestamp`               |

---

## 2. PLAYER ATTRIBUTES

These attributes must be stored and queryable in the CRM for segmentation, personalization, and journey logic.

### 2.1 Identity

| Attribute             | Type     | Source                   | Notes                        |
| --------------------- | -------- | ------------------------ | ---------------------------- |
| `player_id`         | String   | GR8 Tech                 | Primary key                  |
| `email`             | String   | Registration             |                              |
| `phone_number`      | String   | Registration/KYC         |                              |
| `first_name`        | String   | Registration             | For personalization tokens   |
| `country`           | String   | Registration             | Should be "AR" for Argentina |
| `language`          | String   | Registration             | Default "es-AR"              |
| `registration_date` | DateTime | Registration             |                              |
| `birthday`          | Date     | KYC/Profile              | For birthday bonus           |
| `zodiac_sign`       | String   | Calculated from birthday | For zodiac bonus             |

### 2.2 KYC Status

| Attribute               | Type    | Values                                               | Notes                                            |
| ----------------------- | ------- | ---------------------------------------------------- | ------------------------------------------------ |
| `email_verified`      | Boolean | true/false                                           |                                                  |
| `phone_verified`      | Boolean | true/false                                           | Unlocks SMS channel                              |
| `documents_submitted` | Boolean | true/false                                           |                                                  |
| `documents_status`    | Enum    | `none` / `pending` / `approved` / `rejected` |                                                  |
| `kyc_level`           | Enum    | `unverified` / `partial` / `full`              | partial = email+phone, full = documents approved |

### 2.3 Financial

| Attribute                      | Type     | Update Frequency  | Notes                                       |
| ------------------------------ | -------- | ----------------- | ------------------------------------------- |
| `deposit_count`              | Integer  | On each deposit   | Total deposits ever                         |
| `cumulative_deposits_ars`    | Float    | On each deposit   | Lifetime deposit sum                        |
| `last_deposit_date`          | DateTime | On each deposit   |                                             |
| `last_deposit_amount_ars`    | Float    | On each deposit   |                                             |
| `ftd_date`                   | DateTime | On first deposit  | Null if no FTD                              |
| `ftd_amount_ars`             | Float    | On first deposit  |                                             |
| `std_date`                   | DateTime | On second deposit | Null if no STD                              |
| `average_deposit_ars`        | Float    | Calculated        | `cumulative_deposits_ars / deposit_count` |
| `payment_methods_used[]`     | Array    | On each deposit   | List of methods used                        |
| `last_withdrawal_date`       | DateTime | On withdrawal     |                                             |
| `cumulative_withdrawals_ars` | Float    | On withdrawal     |                                             |
| `ggr_ars`                    | Float    | Calculated daily  | Gross Gaming Revenue                        |

### 2.4 Gameplay

| Attribute                         | Type     | Update Frequency  | Notes                                                      |
| --------------------------------- | -------- | ----------------- | ---------------------------------------------------------- |
| `game_preference`               | Enum     | Calculated weekly | `slots` / `live` / `aviator` / `mixed` / `sport` |
| `most_played_game_id`           | String   | Calculated weekly |                                                            |
| `most_played_game_name`         | String   | Calculated weekly | For FS personalization                                     |
| `top_3_games[]`                 | Array    | Calculated weekly | Game IDs                                                   |
| `total_rounds_played`           | Integer  | Realtime          |                                                            |
| `total_wagered_ars`             | Float    | Realtime          |                                                            |
| `biggest_win_ars`               | Float    | Realtime          | For anniversary personalization                            |
| `last_game_date`                | DateTime | Realtime          |                                                            |
| `last_session_date`             | DateTime | Realtime          |                                                            |
| `last_session_duration_seconds` | Integer  | Realtime          |                                                            |
| `has_played_demo`               | Boolean  | Realtime          | For No Cashier Visited path C                              |

### 2.5 Lifecycle & Value

| Attribute                    | Type           | Update Frequency | Notes                                                      |
| ---------------------------- | -------------- | ---------------- | ---------------------------------------------------------- |
| `lifecycle_stage`          | Enum           | Realtime         | See Axis 1 in section 17                                   |
| `value_tier`               | Enum           | Daily            | `micro` / `low` / `mid` / `high` / `previp_plus` |
| `days_since_last_activity` | Integer        | Daily            | For reactivation matrix                                    |
| `days_since_registration`  | Integer        | Daily            |                                                            |
| `engagement_history`       | Enum           | Weekly           | `active` / `passive` — for reactivation matrix        |
| `churn_score`              | Float (0–100) | Daily            | From Predictive Churn model                                |
| `churn_risk_level`         | Enum           | Daily            | `healthy` / `watch` / `at_risk` / `critical`       |

### 2.6 Loyalty

| Attribute                 | Type     | Notes                                                 |
| ------------------------- | -------- | ----------------------------------------------------- |
| `loyalty_enrolled`      | Boolean  |                                                       |
| `loyalty_tier`          | Enum     | `premium` / `prestige` / `maestro` / `legend` |
| `cc_balance`            | Integer  | Current Cuatro Coins balance                          |
| `cc_lifetime_earned`    | Integer  |                                                       |
| `cc_last_spent_date`    | DateTime | For CC expiry warnings                                |
| `missions_completed_7d` | Integer  | For active/passive classification                     |
| `last_mission_date`     | DateTime |                                                       |

### 2.7 Communication Preferences

| Attribute                    | Type    | Notes                                                  |
| ---------------------------- | ------- | ------------------------------------------------------ |
| `email_opt_in`             | Boolean |                                                        |
| `sms_opt_in`               | Boolean | Auto-set on phone verification                         |
| `push_opt_in`              | Boolean |                                                        |
| `preferred_contact_method` | Enum    | `sms` / `email` / `push`                         |
| `email_engagement_30d`     | Enum    | `high` / `low` / `zero` — based on opens/clicks |
| `messages_today_count`     | Integer | For frequency cap enforcement                          |

### 2.8 Bonus State

| Attribute                     | Type    | Notes                                                     |
| ----------------------------- | ------- | --------------------------------------------------------- |
| `welcome_bonus_claimed`     | Boolean |                                                           |
| `welcome_bonus_status`      | Enum    | `available` / `claimed` / `completed` / `expired` |
| `active_bonus_id`           | String  | Currently active bonus                                    |
| `active_bonus_wagering_pct` | Float   | 0–100% wagering completion                               |
| `welcome_ladder_step`       | Integer | 1–10 (which deposit in the ladder)                       |

### 2.9 Referral

| Attribute                      | Type    | Notes                        |
| ------------------------------ | ------- | ---------------------------- |
| `referral_code`              | String  | Player's unique code         |
| `referrals_successful_count` | Integer | STD-qualified referrals      |
| `referrals_successful_month` | Integer | This month's count (for cap) |
| `was_referred`               | Boolean | Player came via referral     |
| `referred_by_player_id`      | String  |                              |

---

## 3. CALCULATED METRICS

These must be computed by GR8 Tech and updated on the schedule indicated.

| Metric                   | Formula                                                                                                | Update            | Used By                 |
| ------------------------ | ------------------------------------------------------------------------------------------------------ | ----------------- | ----------------------- |
| `value_tier`           | Based on `cumulative_deposits_ars`: <5K=micro, 5–25K=low, 25–75K=mid, 75–150K=high, >150K=previp+ | Daily             | All offer scaling       |
| `lifecycle_stage`      | Rules-based on deposit count, last activity, cumulative deposits                                       | Realtime          | Journey entry/exit      |
| `game_preference`      | >70% of rounds in one type = that type; else "mixed"                                                   | Weekly            | Content personalization |
| `engagement_history`   | ≥1 mission in 7d = "active"; else "passive"                                                           | Daily             | Reactivation matrix     |
| `churn_score`          | Predictive Churn model output                                                                          | Daily             | Timing acceleration     |
| `email_engagement_30d` | Opens in 30d: ≥3 = high; 1–2 = low; 0 = zero                                                         | Daily             | Channel selection       |
| `zodiac_sign`          | Calculated from `birthday` field                                                                     | On profile update | Zodiac bonus            |
| `days_inactive`        | `today - max(last_deposit_date, last_session_date)`                                                  | Daily             | Reactivation triggers   |
| `bonus_cost_pct_ggr`   | `total_bonus_paid / ggr * 100`                                                                       | Weekly            | Cost monitoring         |

---

## 4. SEGMENTS TO BUILD

Build these segments in GR8 Tech's segmentation engine. They are referenced across all implementation guides.

### 4.1 Lifecycle Segments

| Segment ID      | Name               | Rules                                                                      |
| --------------- | ------------------ | -------------------------------------------------------------------------- |
| `SEG-REG`     | Registered, No FTD | `deposit_count = 0`                                                      |
| `SEG-FTD`     | FTD Done, <24h     | `deposit_count = 1 AND hours_since_ftd < 24`                             |
| `SEG-D1LAYER` | In Day 1 Layer     | `deposit_count >= 1 AND days_since_ftd <= 3`                             |
| `SEG-PRESTD`  | Pre-STD            | `deposit_count = 1 AND days_since_ftd > 1`                               |
| `SEG-REGULAR` | Regular            | `deposit_count >= 2 AND days_inactive < 14`                              |
| `SEG-PREVIP`  | Pre-VIP            | `cumulative_deposits_ars >= 150000 AND cumulative_deposits_ars < 300000` |
| `SEG-VIP`     | VIP                | `cumulative_deposits_ars >= 300000`                                      |

### 4.2 KYC Segments

| Segment ID                | Name               | Rules                                                              |
| ------------------------- | ------------------ | ------------------------------------------------------------------ |
| `SEG-KYC-NONE`          | Unverified         | `kyc_level = "unverified"`                                       |
| `SEG-KYC-EMAIL-PENDING` | Email Not Verified | `email_verified = false`                                         |
| `SEG-KYC-PHONE-PENDING` | Phone Not Verified | `phone_verified = false`                                         |
| `SEG-KYC-DOCS-PENDING`  | Docs Not Submitted | `documents_status = "none" AND cumulative_deposits_ars >= 15000` |
| `SEG-KYC-FULL`          | Fully Verified     | `kyc_level = "full"`                                             |

### 4.3 Behavioral Segments

| Segment ID                | Name                               | Rules                                                                                     |
| ------------------------- | ---------------------------------- | ----------------------------------------------------------------------------------------- |
| `SEG-BOUNCE`            | Bounced (session <60s, no cashier) | `last_session_duration < 60 AND cashier_opened = false`                                 |
| `SEG-LONG-NO-CASHIER`   | Long Session, No Cashier           | `last_session_duration > 600 AND cashier_opened = false`                                |
| `SEG-FS-NO-DEP`         | Played Free Spins, No Deposit      | `has_played_demo = true AND deposit_count = 0`                                          |
| `SEG-BONUS-MISSED`      | Missed Welcome Bonus               | `deposit_count = 0 AND welcome_bonus_claimed = false AND hours_since_registration >= 1` |
| `SEG-BONUS-DECLINED`    | Declined Welcome Bonus             | `welcome_bonus_status = "declined" OR (bonus_flow_bypassed = true)`                     |
| `SEG-CASHIER-ABANDONED` | Opened Cashier, No Deposit         | Event `cashier_closed` without subsequent `deposit_success` in 30 min                 |

### 4.4 Reactivation Segments

| Segment ID        | Name                     | Rules                                                                         |
| ----------------- | ------------------------ | ----------------------------------------------------------------------------- |
| `SEG-REACT-A7`  | Active × 7 Days         | `engagement_history = "active" AND days_inactive BETWEEN 7 AND 13`          |
| `SEG-REACT-A14` | Active × 14 Days        | `engagement_history = "active" AND days_inactive BETWEEN 14 AND 20`         |
| `SEG-REACT-A21` | Active × 21+ Days       | `engagement_history = "active" AND days_inactive >= 21`                     |
| `SEG-REACT-P7`  | Passive × 7 Days        | `engagement_history = "passive" AND days_inactive BETWEEN 7 AND 13`         |
| `SEG-REACT-P14` | Passive × 14 Days       | `engagement_history = "passive" AND days_inactive BETWEEN 14 AND 20`        |
| `SEG-REACT-P21` | Passive × 21+ Days      | `engagement_history = "passive" AND days_inactive >= 21`                    |
| `SEG-REACT-VNR` | Verified But No Activity | `kyc_level = "full" AND deposit_count = 0 AND days_since_verification >= 3` |

### 4.5 Value Tier Segments

| Segment ID         | Name     | Rules                                                |
| ------------------ | -------- | ---------------------------------------------------- |
| `SEG-VAL-MICRO`  | Micro    | `cumulative_deposits_ars < 5000`                   |
| `SEG-VAL-LOW`    | Low      | `cumulative_deposits_ars BETWEEN 5000 AND 24999`   |
| `SEG-VAL-MID`    | Mid      | `cumulative_deposits_ars BETWEEN 25000 AND 74999`  |
| `SEG-VAL-HIGH`   | High     | `cumulative_deposits_ars BETWEEN 75000 AND 149999` |
| `SEG-VAL-PREVIP` | Pre-VIP+ | `cumulative_deposits_ars >= 150000`                |

### 4.6 Game Preference Segments

| Segment ID           | Name          | Rules                           |
| -------------------- | ------------- | ------------------------------- |
| `SEG-GAME-SLOTS`   | Slots-Heavy   | `game_preference = "slots"`   |
| `SEG-GAME-LIVE`    | Live-Heavy    | `game_preference = "live"`    |
| `SEG-GAME-AVIATOR` | Aviator/Crash | `game_preference = "aviator"` |
| `SEG-GAME-MIXED`   | Mixed         | `game_preference = "mixed"`   |

### 4.7 Engagement Segments

| Segment ID          | Name                  | Rules                                                                                       |
| ------------------- | --------------------- | ------------------------------------------------------------------------------------------- |
| `SEG-ENG-HIGH`    | High Email Engagement | `email_engagement_30d = "high"`                                                           |
| `SEG-ENG-LOW`     | Low Email Engagement  | `email_engagement_30d = "low"`                                                            |
| `SEG-ENG-ZERO`    | Zero Engagement       | `email_engagement_30d = "zero"`                                                           |
| `SEG-LOY-ACTIVE`  | Active Loyalty        | `loyalty_enrolled = true AND missions_completed_7d >= 1`                                  |
| `SEG-LOY-PASSIVE` | Passive Loyalty       | `loyalty_enrolled = true AND missions_completed_7d = 0 AND days_since_last_mission <= 30` |

---

## 5. CHANNEL CONFIGURATION

### 5.1 SMS

| Setting            | Value                                                        |
| ------------------ | ------------------------------------------------------------ |
| Provider           | Existing GR8 Tech SMS gateway                                |
| Sender ID          | "CuatroBet"                                                  |
| Quiet hours        | 00:00–08:00 ART                                             |
| Max SMS/day/player | See frequency caps below                                     |
| Opt-in trigger     | Auto on `phone_verified` event                             |
| Link shortener     | Enable with tracking UTMs                                    |
| Default UTM        | `utm_source=sms&utm_medium=crm&utm_campaign={campaign_id}` |

### 5.2 Email

| Setting      | Value                                                          |
| ------------ | -------------------------------------------------------------- |
| From address | `hola@cuatrobet.com` (or equivalent)                         |
| From name    | "CuatroBet"                                                    |
| Reply-to     | `soporte@cuatrobet.com`                                      |
| Default UTM  | `utm_source=email&utm_medium=crm&utm_campaign={campaign_id}` |
| Unsubscribe  | Required by law — include in footer                           |
| Preheader    | Must be set per campaign                                       |

### 5.3 In-App Popup (NC Pop-Up)

| Setting                      | Value                                                       |
| ---------------------------- | ----------------------------------------------------------- |
| Max 1 popup per session      | Enforced                                                    |
| No popup in first 60 seconds | Enforced                                                    |
| Dismiss behavior             | Close and don't show again for this campaign                |
| Priority rules               | If multiple popups queued → show highest-value offer first |

### 5.4 In-App Feed (NC Feed)

| Setting                        | Value                                     |
| ------------------------------ | ----------------------------------------- |
| Max 2 items per player per day | Enforced                                  |
| Min 4 hours between items      | Enforced                                  |
| Target audience                | Active players only (session in last 48h) |
| Daily volume cap               | 10,000 total sends (down from 25,700)     |

### 5.5 App Push

| Setting          | Value                                                                                                |
| ---------------- | ---------------------------------------------------------------------------------------------------- |
| Status           | **ACTIVATE** — currently at zero sends                                                        |
| Opt-in prompt    | Show after first deposit (not at registration)                                                       |
| Opt-in incentive | 100 CC on opt-in                                                                                     |
| Quiet hours      | 00:00–08:00 ART                                                                                     |
| Rollout          | Week 1: setup → Week 2: Day 1 Layer → Week 3: Post-FTD/Pre-VIP → Week 4: evaluate → Week 5: full |

### 5.6 Deep Links

All CTA links in communications must use deep links that open the correct page in the app/site:

| Deep Link                               | Destination                          | Used By                  |
| --------------------------------------- | ------------------------------------ | ------------------------ |
| `{base_url}/cashier`                  | Deposit page                         | Most CTAs                |
| `{base_url}/cashier?method={method}`  | Deposit page with method preselected | Payment failure recovery |
| `{base_url}/cashier?amount={amount}`  | Deposit page with amount prefilled   | Lower amount recovery    |
| `{base_url}/game/{game_id}`           | Specific game                        | Game recommendations     |
| `{base_url}/game/{game_id}?demo=true` | Demo mode of specific game           | No-bonus cluster         |
| `{base_url}/bonuses`                  | Bonuses landing page                 | Bonus reminders          |
| `{base_url}/bonus-shop`               | Bonus shop                           | CC spend CTAs            |
| `{base_url}/missions`                 | Loyalty missions page                | Loyalty comms            |
| `{base_url}/profile/verify`           | KYC upload page                      | KYC chain                |
| `{base_url}/lucky-wheel`              | Lucky Wheel                          | Quest/gamification       |
| `{base_url}/referral`                 | Referral page                        | Referral comms           |

---

## 6. FREQUENCY CAPS

Configure these as global rules in GR8 Tech CRM.

| Segment                            | Max Messages/Day (all channels combined) |
| ---------------------------------- | ---------------------------------------- |
| `SEG-REG` (Pre-FTD)              | 2                                        |
| `SEG-D1LAYER` (Day 1, first 72h) | 3                                        |
| `SEG-REGULAR`                    | 2                                        |
| `SEG-PREVIP` / `SEG-VIP`       | 2                                        |
| Reactivation segments              | 1                                        |
| Transactional / Security           | **Exempt** (no cap)                |

**Collision rule:** If multiple campaigns fire on the same day for the same player and the cap is reached → send only the highest-priority / highest-value message. Suppress others.

**Kill switch:** If any channel's open rate drops >25% week-over-week → auto-pause new campaigns on that channel, alert CRM team.

---

## 7. BONUS CONFIGURATION

These bonus templates must exist in GR8 Tech before automations can reference them.

### 7.1 Welcome Ladder — Slots

| Bonus ID      | Deposit # | Match %             | FS Count | FS Game                | CC   | Wagering | Validity |
| ------------- | --------- | ------------------- | -------- | ---------------------- | ---- | -------- | -------- |
| `WBL-S-D1`  | 1st       | 120% (150% if >15K) | 50       | Gates of Olympus       | —   | 25×     | 7 days   |
| `WBL-S-D2`  | 2nd       | 75%                 | 30       | Joker's Jewels         | —   | 20×     | 5 days   |
| `WBL-S-D3`  | 3rd       | 60%                 | 25       | Jackpot Joker          | —   | 18×     | 5 days   |
| `WBL-S-D4`  | 4th       | 55%                 | 20       | 4 Supercharged Clovers | —   | 15×     | 5 days   |
| `WBL-S-D5`  | 5th       | 50%                 | 15       | Gold Party             | 200  | 15×     | 5 days   |
| `WBL-S-D6`  | 6th       | 60%                 | 30       | 3 Coin Volcanoes       | 300  | 15×     | 5 days   |
| `WBL-S-D7`  | 7th       | 65%                 | 35       | Rush for Gold          | 400  | 15×     | 5 days   |
| `WBL-S-D8`  | 8th       | 70%                 | 40       | Gates of Olympus 1000  | 500  | 15×     | 5 days   |
| `WBL-S-D9`  | 9th       | 80%                 | 50       | Player's top slot      | 600  | 12×     | 7 days   |
| `WBL-S-D10` | 10th      | 100%                | 60       | Player's top slot      | 1000 | 10×     | 7 days   |

### 7.2 Welcome Ladder — Live Casino

Same structure as Slots but with Bonus Cash instead of FS (see task spec 05).

### 7.3 Welcome Ladder — Sport

Same structure but with Free Bets at odds minimum 1.80 (see task spec 05).

### 7.4 KYC Verification Bonuses

| Bonus ID                  | Trigger                                | Amount    | Wagering | Notes   |
| ------------------------- | -------------------------------------- | --------- | -------- | ------- |
| `KYC-EMAIL-REWARD`      | Email verified                         | 500 ARS   | None     | Instant |
| `KYC-PHONE-REWARD`      | Phone verified                         | 500 ARS   | None     | Instant |
| `KYC-DOCS-REWARD-EARLY` | Docs approved before 22.5K threshold   | 1,000 ARS | None     |         |
| `KYC-DOCS-REWARD-HARD`  | Docs approved at/after 22.5K threshold | 2,000 ARS | None     |         |

### 7.5 Reactivation Offer Templates

Create offer templates that scale by value tier. See section 12 implementation guide for full matrix.

### 7.6 Wagering Rules

| Rule                    | Slots          | Live | Table | Sport |
| ----------------------- | -------------- | ---- | ----- | ----- |
| Contribution %          | 100%           | 10%  | 5%    | 100%  |
| Max bet during wagering | 1,500 ARS/spin | —   | —    | —    |
| Max bonus balance       | 30,000 ARS     | —   | —    | —    |

---

## 8. TECHNICAL DEPENDENCIES

### 8.1 Must Be Activated in GR8 Tech

| Module                       | Status                | Action Required                                                                 |
| ---------------------------- | --------------------- | ------------------------------------------------------------------------------- |
| Smart Segmentation           | Available, not active | Contact GR8 Tech to enable                                                      |
| Predictive Churn             | Available, not active | Contact GR8 Tech to enable                                                      |
| Real-time event streaming    | Unknown               | Verify sub-5-second latency for deposit events                                  |
| App Push infrastructure      | Not set up            | Set up push notification SDK in mobile app                                      |
| Deposit failure reason codes | Unknown               | Verify GR8 Tech exposes `INSUFF`/`METHOD`/`DECLINE`/`TIMEOUT`/`FRAUD` |

### 8.2 Data Exports / APIs Needed

| Integration              | Purpose                                  | Direction       |
| ------------------------ | ---------------------------------------- | --------------- |
| Player-level data export | Segmentation model validation            | GR8 Tech → CRM |
| Game catalog API         | Get game names, IDs, providers           | GR8 Tech → CRM |
| Bonus management API     | Credit bonuses, FS, CC programmatically  | CRM → GR8 Tech |
| Payment methods API      | Get available payment methods per player | GR8 Tech → CRM |
| Session tracking         | Real-time session status                 | GR8 Tech → CRM |

### 8.3 Creative Assets Needed (per chain)

| Asset Type                       | Needed For                        | Quantity                                    |
| -------------------------------- | --------------------------------- | ------------------------------------------- |
| Email templates                  | All email comms                   | ~50+ (reusable with dynamic content blocks) |
| In-app popup designs             | Day 1, KYC, Payment, Quests       | ~20                                         |
| In-app banner designs            | KYC Phase 3, NC Feed items        | ~10                                         |
| SMS copy (Spanish)               | All SMS comms                     | ~40+                                        |
| Push notification copy (Spanish) | App Push comms                    | ~30+                                        |
| Game banners/thumbnails          | Personalized game recommendations | Per game in top 10                          |

---

## 9. IMPLEMENTATION PRIORITY ORDER

Complete in this order. Each phase builds on the previous.

### Phase 0: Foundation (Week 1–2)

- [ ] Activate Smart Segmentation module
- [ ] Activate Predictive Churn module
- [ ] Verify all real-time events fire correctly (section 1)
- [ ] Build all player attributes (section 2)
- [ ] Build all segments (section 4)
- [ ] Configure all channels (section 5)
- [ ] Set frequency caps (section 6)
- [ ] Create all bonus templates (section 7)
- [ ] Set up deep links (section 5.6)

### Phase 1: Highest Impact (Week 3–4)

- [ ] 04 — Payment Failure Recovery (cheapest, highest ROI)
- [ ] 01 — Day 1 Retention Layer (biggest retention problem)
- [ ] 03 — KYC Completion Chain (SMS channel growth)
- [ ] 05 — Welcome Bonus Ladder (fix D1→D2 cliff)

### Phase 2: Pre-FTD Recovery (Week 5–6)

- [ ] 06 — Failed Deposits (20 comms)
- [ ] 07 — No Bonus Cluster
- [ ] 08 — No Cashier Visited

### Phase 3: Engagement (Week 7–8)

- [ ] 10 — Engagement & Gamification (Quests, Loot Boxes)
- [ ] 11 — Loyalization
- [ ] 09 — Personalization

### Phase 4: Lifecycle Completion (Week 9–10)

- [ ] 02 — Pre-VIP Lifecycle
- [ ] 12 — Reactivation Matrix
- [ ] 13 — Channel Strategy execution

### Phase 5: Platform & Growth (Week 11–12)

- [ ] 14 — Bonuses Landing Page Redesign
- [ ] 15 — Bonus Shop SKU Redesign
- [ ] 16 — Referral Program
- [ ] 17 — Smart Segmentation fine-tuning

---

## APPENDIX: Naming Convention for Campaigns

Use this pattern for all campaign names in GR8 Tech:

```
{chain_number}-{chain_abbrev}-{touch_id}-{channel}
```

Examples:

- `01-D1RET-T1-EMAIL` — Day 1 Retention, Touch 1, Email
- `03-KYC-P1-01-POPUP` — KYC Chain, Phase 1, Touch 1, Popup
- `04-PFR-01A-POPUP` — Payment Failure Recovery, Touch 1A, Popup
- `12-REACT-A7-C1-EMAIL` — Reactivation, Active×7, Comm 1, Email

This ensures all campaigns are traceable across the CRM.
