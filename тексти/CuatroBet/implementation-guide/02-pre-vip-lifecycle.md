# 02 — Pre-VIP Lifecycle — Implementation Guide

**Chain:** Pre-VIP Lifecycle  
**Priority:** High  
**Estimated Communications:** 6 touches + decision points over 30 days  
**Prerequisites from Master Doc:** Attributes `cumulative_deposits_ars`, `days_since_last_activity`, `game_preference`, `most_played_game_name`; Segments `SEG-PREVIP`, `SEG-VIP`

---

## STEP 0: PRE-FLIGHT CHECKLIST

- [ ] Attribute `cumulative_deposits_ars` updates in real-time on every deposit
- [ ] Attribute `days_since_last_activity` calculated daily
- [ ] CRM owner assignment system ready (named person, real email, reply-to)
- [ ] 15% weekly cashback bonus template created (wager-free, Monday payout, cap 30,000 ARS)
- [ ] Bonus template for Touch 3: 60% match up to 10,000 ARS + 30 FS, 20× wagering, 72h validity
- [ ] Bonus template for Touch 5: 100% match up to 20,000 ARS + 50 FS, 15× wagering, 72h validity
- [ ] Predictive Churn module activated (for Day 21+ monitoring)
- [ ] Pre-VIP dashboard exists in CRM for team monitoring
- [ ] Player's favorite slot data (`most_played_game_name`) is available

---

## STEP 1: CREATE THE JOURNEY

**Campaign Name:** `02-PVIP-JOURNEY`  
**Type:** Triggered journey (attribute-based)  
**Entry Trigger:** `cumulative_deposits_ars >= 150000` AND `days_since_last_activity <= 14`  
**Re-entry:** None  
**Journey Window:** 30 days (extendable to 60)  
**Exit Conditions:**
- Player reaches `cumulative_deposits_ars >= 300000` (VIP I) → exit to VIP I onboarding
- 60 days pass without VIP I → drop to Regular lifecycle

---

## STEP 2: BUILD TOUCH SEQUENCE

### 2.1 Touch 1 — Pre-VIP Activation (Personal Email)

| Setting | Value |
|---------|-------|
| **Campaign ID** | `02-PVIP-T1-EMAIL` |
| **Channel** | Email |
| **Timing** | Day 1 (on journey entry) |
| **From** | Named CRM owner (e.g., "Matias de CuatroBet") — NOT generic |
| **Reply-to** | CRM owner's real email (or monitored inbox) |

**System Actions (before sending email):**
1. Assign named CRM owner to player record
2. Flag player as Pre-VIP in segmentation
3. Add player to Pre-VIP monitoring dashboard

**Email Content:**
- **Subject (ES):** `👑 Acabas de desbloquear estatus Pre-VIP en CuatroBet`
- **Preheader (ES):** `Soy {crm_owner_name}, tu manager personal`
- **Banner Text (ES):** `Desbloqueaste Pre-VIP`
- **Banner Description:** Premium gold-themed banner — Pre-VIP badge with crown icon, dark luxury background, golden particle effects, player name space
- **Body Description:** Personal greeting from named CRM owner. Congratulations on Pre-VIP status. List benefits: 15% weekly wager-free cashback, personalized game recommendations, faster withdrawals, exclusive offers. Mention proximity to VIP I. Welcome gift: 500 CC + 20 FS on player's favorite slot. Conversational tone, no hard CTA — signed by CRM owner with name, title, photo.
- **CTA:** None (conversational tone, no hard CTA)
- **Signature:** CRM owner name, title, photo if available

**Bonus Configuration:**
- 500 CC (Cuatro Coins) — credit immediately
- 20 FS on player's favorite slot (`most_played_game_name`)

**In-App Action:**
- Show Pre-VIP unlock banner on player's next login

**Configuration steps:**
1. Add email node at journey start
2. Use personalization tokens: `{first_name}`, `{crm_owner_name}`, `{player_favorite_slot}`
3. Set sender as CRM owner (not generic "CuatroBet")
4. Add parallel system action: Credit 500 CC + 20 FS
5. Add parallel action: Schedule in-app banner for next login

---

### 2.2 Touch 2 — Cashback Activation (Day 3)

| Setting | Value |
|---------|-------|
| **Campaign ID** | `02-PVIP-T2-EMAIL` |
| **Channel** | Email + In-app banner |
| **Timing** | Day 3 |

**Email Content:**
- **Subject (ES):** `💰 15% Cashback Pre-VIP está activo`
- **Preheader (ES):** `15% semanal, sin wagering, cada lunes`
- **Banner Text (ES):** `15% Cashback Semanal`
- **Banner Description:** Cashback visual — large "15%" in gold on dark background, coins flowing back to player icon, weekly calendar icon, "Sin Wagering" badge
- **Body Description:** Explain cashback mechanics: calculated on weekly net losses, credited every Monday automatically, zero wagering, 30,000 ARS weekly cap. Reassuring tone.
- **CTA Button (ES):** `Jugar ahora` → `{base_url}/cashier`

**System Action:**
- Enable 15% weekly cashback rule for this player (30-day validity, wager-free, Monday payout, 30,000 ARS cap)

**In-App Banner:**
- Text: "15% Cashback Activo — Sin wagering"
- Show for 7 days on login

**Configuration steps:**
1. Add 2-day delay (Day 1 → Day 3)
2. Add email node
3. Add system action: activate cashback rule
4. Add in-app banner (7-day display)

---

### 2.3 Touch 3 — Curated Game List + Reload Offer (Day 5)

| Setting | Value |
|---------|-------|
| **Campaign ID** | `02-PVIP-T3-EMAIL` |
| **Channel** | Email |
| **Timing** | Day 5 |

**Email Content:**
- **Subject (ES):** `🎮 60% Bono + tu selección personalizada`
- **Preheader (ES):** `Elegidos para vos + 60% en tu próximo depósito`
- **Banner Text (ES):** `Tu Selección + Bono 60%`
- **Banner Description:** Game tiles grid showing 5 personalized game thumbnails, "60%" golden overlay, sparkle effects on new releases marked with star badge
- **Body Description:** Show 5 personalized game recommendations (3 from player history + 2 new releases matching preference). Each with thumbnail and "Jugar" link. Exclusive offer: 60% match up to 10,000 ARS + 30 FS on premium Pragmatic Play title, 20× wagering, 72h validity.
- **CTA Button (ES):** `Depositar y jugar` → `{base_url}/cashier`

**Personalization required:**
- Top 3 games from player's history (`top_3_games[]`)
- 2 new releases matching `game_preference`
- Premium Pragmatic Play title for FS

**Bonus Configuration:**
- 60% match up to 10,000 ARS
- 30 FS on a premium Pragmatic Play title
- Wagering: 20×
- Validity: 72 hours

**Configuration steps:**
1. Add 2-day delay (Day 3 → Day 5)
2. Add email node with game recommendation data
3. Create bonus template: 60% match + 30 FS
4. Link bonus to next deposit within 72h

---

### 2.4 Touch 4 — Soft Coaching Push (Day 10)

| Setting | Value |
|---------|-------|
| **Campaign ID** | `02-PVIP-T4-PUSH-SMS` |
| **Channel** | App Push + SMS |
| **Timing** | Day 10 |

**App Push Content:**
- **Title (ES):** `¡Ya casi sos VIP!`
- **Body (ES):** `Estás a {remaining_amount} ARS de VIP I. Tu manager {crm_owner_name} te está esperando.`
- **CTA:** Tap → `{base_url}/cashier`

**SMS Content (fallback if no push):**
- **Text (ES):** `CuatroBet: Estás a {remaining_amount} ARS de VIP I. Tu manager personal te está esperando: {link}`
- **Link:** `{base_url}/cashier?utm_source=sms&utm_medium=crm&utm_campaign=02-PVIP-T4`

**Personalization:**
- `{remaining_amount}` = `300000 - cumulative_deposits_ars` (formatted with thousand separators)

**Configuration steps:**
1. Add 5-day delay (Day 5 → Day 10)
2. Add push notification node (primary)
3. Add SMS fallback for players without push opt-in
4. Compute `remaining_amount` dynamically

---

### 2.5 Decision Point — Day 14

| Condition | Path |
|-----------|------|
| `cumulative_deposits_ars >= 300000` | EXIT → VIP I onboarding flow |
| `cumulative_deposits_ars < 300000` | Continue to Touch 5 |

**Configuration steps:**
1. Add 4-day delay (Day 10 → Day 14)
2. Add conditional split on `cumulative_deposits_ars >= 300000`
3. "Yes" path → Exit node (tag: VIP I qualified)
4. "No" path → Continue

---

### 2.6 Touch 5 — Second Chance Reload (Day 15)

| Setting | Value |
|---------|-------|
| **Campaign ID** | `02-PVIP-T5-EMAIL-SMS` |
| **Channel** | Email + SMS (from CRM owner) |
| **Timing** | Day 15 |

**Email Content:**
- **From:** CRM owner (same as Touch 1)
- **Subject (ES):** `💡 100% Mega Bono - te extrañamos esta semana`
- **Preheader (ES):** `Tu bono más grande hasta ahora te espera`
- **Banner Text (ES):** `Tu Mega Bono Pre-VIP`
- **Banner Description:** Premium urgency design — large "100%" in gold, VIP crown icon, countdown visual suggesting limited time, dark luxury background
- **Body Description:** Personal tone from CRM owner. Noted player was less active this week. Present mega offer: 100% match up to 20,000 ARS, 50 FS, extended cashback, 15× wagering, 72h validity. Motivate with VIP I proximity. Signed by CRM owner.
- **CTA Button (ES):** `Depositar ahora` → `{base_url}/cashier`

**SMS Content:**
- **Text (ES):** `CuatroBet ({crm_owner_name}): Tu bono del 100% hasta 20,000 ARS vence en 72h. Estás cerca de VIP I: {link}`

**Bonus Configuration:**
- 100% match up to 20,000 ARS
- 50 FS
- Extended cashback (add 2 more weeks)
- Wagering: 15×
- Validity: 72 hours

**Configuration steps:**
1. Add 1-day delay (Day 14 → Day 15)
2. Send email (from CRM owner) + SMS simultaneously
3. Create bonus template: 100% match + 50 FS + cashback extension
4. Link bonus to next deposit within 72h

---

### 2.7 Decision Point — Day 21

| Condition | Path |
|-----------|------|
| Any deposit since Day 14 | Touch 6 (Cashback Top-Up) + continue monitoring |
| No deposit since Day 14 | Add to Churn Intervention flow at Day 22 |

---

### 2.8 Touch 6 — Cashback Top-Up (Day 21, Deposited)

| Setting | Value |
|---------|-------|
| **Campaign ID** | `02-PVIP-T6-SYSTEM-EMAIL` |
| **Channel** | System + Email |
| **Timing** | Day 21 (only if deposited since Day 14) |

**System Actions:**
- Top-up cashback percentage (15% → 18% for remaining days)
- Enable Predictive Churn monitoring (alert CRM owner if churn_score rises)

**Email Content:**
- Brief thank-you note from CRM owner
- Reminder of VIP I benefits waiting
- No new bonus (monitoring/nurture phase)

---

### 2.9 Decision Point — Day 30 (Final)

| Condition | Path |
|-----------|------|
| `cumulative_deposits_ars >= 300000` | EXIT → VIP I onboarding |
| Active but below 300,000 | Stay in Pre-VIP for 30 more days, reduced cadence (1 email/week, no SMS) |
| No activity in extended period | Drop to Regular lifecycle |

---

## STEP 3: TESTING CHECKLIST

- [ ] Journey triggers when cumulative deposits cross 150,000 ARS
- [ ] Journey does NOT trigger for players inactive >14 days
- [ ] CRM owner is assigned correctly on entry
- [ ] Touch 1 email comes from CRM owner (not generic sender)
- [ ] 500 CC + 20 FS credited on Touch 1
- [ ] Cashback activates on Day 3 (verify Monday payout works)
- [ ] Game recommendations in Touch 3 match player history
- [ ] Touch 4 push shows correct remaining amount
- [ ] Day 14 decision correctly detects VIP I qualification
- [ ] Touch 5 bonus (100% match) only available to non-VIP players
- [ ] Day 21 churn monitoring activates for deposited players
- [ ] Exit to VIP I onboarding works at any point during journey
- [ ] Extended 30-day window has reduced cadence
- [ ] All emails from CRM owner have correct reply-to

---

## KPI TARGETS

| Metric | Baseline | Target |
|--------|----------|--------|
| VIP base | 15 players | 30–45 in Q1 |
| Pre-VIP → VIP I conversion | Unknown | 30–40% within 30 days |
| ADPU uplift (Pre-VIP cohort) | — | 2× from month 3 to month 5 |
