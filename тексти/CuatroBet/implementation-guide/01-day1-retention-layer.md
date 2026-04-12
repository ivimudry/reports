# 01 — Day 1 Retention Layer — Implementation Guide

**Chain:** Day 1 Retention Layer  
**Priority:** Highest  
**Estimated Communications:** 7 (Slots path) + 7 (Aviator path) = 14 total  
**Prerequisites from Master Doc:** Events `deposit_success`, `session_start`, `session_end`, `game_launched`; Attributes `game_preference`, `deposit_count`, `ftd_date`; Segments `SEG-FTD`, `SEG-D1LAYER`, `SEG-GAME-SLOTS`, `SEG-GAME-AVIATOR`

---

## STEP 0: PRE-FLIGHT CHECKLIST

Before building any campaigns, verify:

- [ ] Event `deposit_success` fires in real-time (≤5 seconds) with `is_ftd` flag
- [ ] Event `session_start` / `session_end` fire correctly
- [ ] Event `game_launched` fires with `game_type` field
- [ ] Attribute `game_preference` is populated (used for path branching)
- [ ] Bonus template `WBL-S-D1` exists (50 FS on Gates of Olympus, 20× wagering, 24h validity)
- [ ] Bonus template for Aviator: 5 Free Flights, 24h validity
- [ ] Deep links configured: `{base_url}/game/gates-of-olympus`, `{base_url}/game/aviator`, `{base_url}/cashier`
- [ ] In-app popup system active with sub-second trigger capability
- [ ] SMS gateway active, sender ID = "CuatroBet"
- [ ] App Push activated (optional but recommended — loses ~30% of T+6h branch without it)

---

## STEP 1: CREATE THE JOURNEY

**Campaign Name:** `01-D1RET-JOURNEY`  
**Type:** Triggered journey (event-based)  
**Entry Trigger:** Event = `deposit_success` WHERE `is_ftd = true`  
**Re-entry:** None (one-time per player)  
**Journey Window:** 72 hours from entry  
**Exit Conditions:**
- Player reaches `deposit_count >= 2` at any point → exit to Post-FTD cadence
- 72 hours pass → exit to Reactivation Ladder (if no return) or Post-FTD (if returned)

---

## STEP 2: ADD BRANCH — Slots vs Aviator

**Position:** Immediately after entry trigger  
**Branch Type:** Conditional split  
**Condition:**
- **Aviator Path:** `game_preference = "aviator"` OR first-session game type = `crash`
- **Slots Path:** Everything else (default)

Expected split: ~95% Slots / ~5% Aviator

---

## STEP 3: BUILD SLOTS PATH

### 3.1 Touch 1 — FTD Instant Grant (System Action)

| Setting | Value |
|---------|-------|
| **Campaign ID** | `01-D1RET-T1-SYSTEM` |
| **Type** | System action (no message sent) |
| **Timing** | T+0 (immediately on FTD) |
| **Action** | Call Bonus API → Grant bonus `WBL-S-D1` |

**Configuration steps:**
1. Add an "Action" node immediately after the Slots branch
2. Set action type: "Grant Bonus"
3. Bonus ID: `WBL-S-D1` (50 no-deposit free spins)
4. Game: Gates of Olympus (default) OR player's first-session game if different
5. Expiry: 24 hours from grant
6. Wagering: 20× on winnings
7. No message is sent — this is a silent system action

---

### 3.2 Touch 2 — In-Session Celebration Popup

| Setting | Value |
|---------|-------|
| **Campaign ID** | `01-D1RET-T2-POPUP` |
| **Channel** | In-app popup |
| **Delay** | 5 minutes after entry |
| **Condition** | Player is still in session (`session_end` has NOT fired) |

**Popup Content:**
- **Banner Text (ES):** `¡Bienvenido a CuatroBet!`
- **Banner Description:** Celebration theme — confetti and sparkle animation, gold coins falling, Gates of Olympus game artwork in background, prominent welcome badge overlay
- **Body (ES):** `Tu bono 120% ya está activo. Extra: 50 giros gratis en Gates of Olympus para empezar`
- **CTA Button (ES):** `Jugar ahora`
- **CTA Link:** `{base_url}/game/gates-of-olympus` (or player's first-session game)
- **Dismiss:** X button, don't show again

**Configuration steps:**
1. Add 5-minute delay node after Touch 1
2. Add condition check: "Player in session" = true
3. If in session → show popup with above content
4. If NOT in session → skip (will be caught by Touch 4)

---

### 3.3 Decision Point — T+30 min

| Setting | Value |
|---------|-------|
| **Delay** | 30 minutes after FTD |
| **Condition** | Player still in session? |
| **Yes →** | Touch 3 (AI recommendation) |
| **No →** | Skip to Touch 4 (SMS) |

**Configuration steps:**
1. Add 30-minute delay node
2. Add conditional split: Check `session_end` event — if NO `session_end` fired since FTD → "In session" branch; if `session_end` fired → "Left session" branch

---

### 3.4 Touch 3 — AI Game Recommendation

| Setting | Value |
|---------|-------|
| **Campaign ID** | `01-D1RET-T3-WIDGET` |
| **Channel** | In-session widget |
| **Timing** | T+1 hour |
| **Condition** | Player still in session at T+30min |

**Widget Content:**
- **Type:** Game recommendation carousel
- **Source:** GR8 Tech AI recommendations module
- **Count:** 3 similar slots based on first-session game
- **No bonus attached** — pure engagement
- **CTA:** Click to open recommended game

**Configuration steps:**
1. Add 30-minute delay after the T+30min check (total = T+1h)
2. Trigger in-session widget via GR8 Tech AI recommendations API
3. Display 3 game tiles with thumbnails, names, and "Play" buttons
4. No bonus or offer needed

---

### 3.5 Touch 4 — Session Exit SMS

| Setting | Value |
|---------|-------|
| **Campaign ID** | `01-D1RET-T4-SMS` |
| **Channel** | SMS |
| **Timing** | T+2 hours |
| **Condition** | Player's session has ended (left before T+2h) |

**SMS Content:**
- **Text (ES):** `CuatroBet: Tus 50 giros gratis en Gates of Olympus vencen en 22h. Seguir jugando: {link}`
- **Character count:** ≤160 characters
- **Link:** `{base_url}/game/gates-of-olympus?utm_source=sms&utm_medium=crm&utm_campaign=01-D1RET-T4`
- **Personalization:** If player's first game ≠ Gates of Olympus → replace game name and link

**Configuration steps:**
1. On the "Left session" branch from T+30min decision, add delay to reach T+2h total
2. Also: for players who WERE in session at T+30min but left before T+2h, merge them into this SMS send
3. Add SMS node with above content
4. Enable link shortening with UTM tracking

---

### 3.6 Decision Point — T+6 hours

| Setting | Value |
|---------|-------|
| **Delay** | T+6 hours from FTD |
| **Condition** | Has the player returned to the app since their last session ended? |
| **Yes →** | Touch 5A (Engagement Reward popup) |
| **No →** | Touch 5B (Urgency SMS) |

**Configuration steps:**
1. Wait until T+6h from FTD
2. Check: has event `session_start` fired after the most recent `session_end`?
3. Split accordingly

---

### 3.7 Touch 5A — Engagement Reward (Player Returned)

| Setting | Value |
|---------|-------|
| **Campaign ID** | `01-D1RET-T5A-POPUP` |
| **Channel** | In-session popup |
| **Timing** | T+6 hours (if returned) |

**Popup Content:**
- **Banner Text (ES):** `¡Gracias por volver!`
- **Banner Description:** Warm welcome-back scene — glowing Cuatro Coins icon, player avatar silhouette returning through golden doorway, loyalty progress bar teaser
- **Body (ES):** `Regalo extra: 100 CC gratis + progreso hacia tu primer nivel de lealtad`
- **CTA Button 1 (ES):** `Ver mi progreso` → `{base_url}/missions`
- **CTA Button 2:** Dismiss (X)
- **Reward:** 100 CC (Cuatro Coins), no wagering

**Configuration steps:**
1. On "Returned" branch, add popup node
2. Add system action: Credit 100 CC to player's balance
3. Continue to T+24h decision

---

### 3.8 Touch 5B — Urgency SMS (Player NOT Returned)

| Setting | Value |
|---------|-------|
| **Campaign ID** | `01-D1RET-T5B-SMS` |
| **Channel** | SMS |
| **Timing** | T+6 hours (if NOT returned) |

**SMS Content:**
- **Text (ES):** `CuatroBet: Tus giros vencen pronto. Además, te regalamos 1,000 ARS extra si depositás en las próximas 6 horas: {link}`
- **Link:** `{base_url}/cashier?utm_source=sms&utm_medium=crm&utm_campaign=01-D1RET-T5B`
- **Bonus:** 1,000 ARS no-deposit bonus on any deposit within 6 hours, wagering 15×

**Configuration steps:**
1. On "Not returned" branch, add SMS node
2. Add system action: Create time-limited bonus (1,000 ARS, 6h validity, 15× wagering)
3. Bonus auto-credits on next deposit within 6h window
4. Continue to T+24h decision

---

### 3.9 Decision Point — T+24 hours

| Setting | Value |
|---------|-------|
| **Condition** | Has the player returned at any point in the first 24h? |
| **Yes →** | EXIT → Post-FTD to STD lifecycle |
| **No →** | Touch 6 — Email Reload Offer |

**Configuration steps:**
1. Wait until T+24h
2. Check: any `session_start` event in last 24h?
3. If yes → end journey, move to standard Post-FTD cadence
4. If no → continue to Touch 6

---

### 3.10 Touch 6 — Email Reload Offer (24h Inactive)

| Setting | Value |
|---------|-------|
| **Campaign ID** | `01-D1RET-T6-EMAIL` |
| **Channel** | Email |
| **Timing** | T+24 hours |

**Email Content:**
- **Subject (ES):** `🎰 75% + 20 giros gratis te esperan`
- **Preheader (ES):** `Depositá hoy y recibí hasta 3,000 ARS extra`
- **Banner Text (ES):** `75% + 20 Giros Gratis`
- **Banner Description:** Hero image — Joker's Jewels slot artwork as background, large "75%" golden text overlay, free spins icons scattered, dark gradient at bottom for readability
- **Body Description:** Remind player about waiting bonus. List exclusive offer: 75% match up to 3,000 ARS, 20 FS on Joker's Jewels, 25× wagering, 48h validity. Urgency framing.
- **CTA Button (ES):** `Depositar ahora`
- **CTA Link:** `{base_url}/cashier?utm_source=email&utm_medium=crm&utm_campaign=01-D1RET-T6`
- **Footer:** Standard unsubscribe + legal text

**Bonus Configuration:**
- 75% match up to 3,000 ARS
- 20 FS on Joker's Jewels
- Wagering: 25×
- Validity: 48 hours

**Configuration steps:**
1. Add email node on "Not returned in 24h" branch
2. Create email template with above content
3. Create bonus template: 75% match + 20 FS
4. Link bonus to deposit event within 48h window

---

### 3.11 Decision Point — T+48 hours

| Setting | Value |
|---------|-------|
| **Condition** | Player still inactive? |
| **Yes →** | Touch 7 — Final SMS |
| **No →** | EXIT → Post-FTD cadence |

---

### 3.12 Touch 7 — Final Touch SMS (48h Inactive)

| Setting | Value |
|---------|-------|
| **Campaign ID** | `01-D1RET-T7-SMS` |
| **Channel** | SMS |
| **Timing** | T+48 hours |

**SMS Content:**
- **Text (ES):** `CuatroBet: Un regalo de despedida. 500 ARS free bet en Aviator, sin depósito. Válido 24h: {link}`
- **Link:** `{base_url}/game/aviator?utm_source=sms&utm_medium=crm&utm_campaign=01-D1RET-T7`

**Bonus Configuration:**
- 500 ARS no-deposit free bet on Aviator
- Wagering: 1× (almost no barrier)
- Validity: 24 hours

**Configuration steps:**
1. Add SMS node
2. Create bonus: 500 ARS free bet, Aviator only, 1× wagering, 24h validity
3. Auto-credit to player immediately

---

### 3.13 Decision Point — T+72 hours (Final)

| Outcome | Action |
|---------|--------|
| Player returned at any point in 72h | EXIT → Post-FTD to STD lifecycle |
| Player never returned | EXIT → Reactivation Ladder (Early Churn cohort, enters at Day 3 instead of usual Day 7) |

---

## STEP 4: BUILD AVIATOR PATH

The Aviator path mirrors the Slots path with these differences:

### 4.1 Touch 1 — FTD Instant Grant (Aviator)

| Difference | Value |
|-----------|-------|
| **Campaign ID** | `01-D1RET-AVI-T1-SYSTEM` |
| **Bonus** | 5 Free Flights on Aviator (instead of 50 FS) |
| **Expiry** | 24 hours |

---

### 4.2 Touch 2 — Celebration Popup (Aviator)

| Difference | Value |
|-----------|-------|
| **Campaign ID** | `01-D1RET-AVI-T2-POPUP` |
| **Banner Text (ES)** | `¡Bienvenido a CuatroBet!` |
| **Banner Description** | Celebration theme — Aviator aircraft flying upward with multiplier trail, confetti, welcome badge |
| **Body (ES)** | `¡Bienvenido! Tus 5 Free Flights en Aviator están listos` |
| **CTA Link** | `{base_url}/game/aviator` |

---

### 4.3 Touch 3 — AI Recommendation (Aviator)

| Difference | Value |
|-----------|-------|
| **Campaign ID** | `01-D1RET-AVI-T3-WIDGET` |
| **Content** | Other crash and instant games (NOT slots) |

---

### 4.4 Touch 4 — Session Exit SMS (Aviator)

| Difference | Value |
|-----------|-------|
| **Campaign ID** | `01-D1RET-AVI-T4-SMS` |
| **Text (ES)** | `CuatroBet: Tus Free Flights en Aviator vencen en 22h. Seguir jugando: {link}` |
| **Link** | `{base_url}/game/aviator` |

---

### 4.5 Touches 5A, 5B — Same as Slots Path

Same logic, same copy, same amounts.

---

### 4.6 Touch 6 — Email Reload (Aviator)

| Difference | Value |
|-----------|-------|
| **Campaign ID** | `01-D1RET-AVI-T6-EMAIL` |
| **Offer** | 75% match + 10 Free Flights on Aviator |
| **Wagering** | 15× (lower than Slots because Aviator contribution is higher) |
| **Subject (ES)** | `✈️ 75% + Free Flights en Aviator te esperan` |
| **Preheader (ES)** | `Depositá y desbloqueá tu bono exclusivo de Aviator` |
| **Banner Text (ES)** | `75% + Free Flights` |
| **Banner Description** | Aviator aircraft soaring with multiplier trail, "75%" large golden text, sky/clouds cinematic background |

---

### 4.7 Touch 7 — Final SMS (Aviator)

Same as Slots path — 500 ARS free bet on Aviator.

---

## STEP 5: TESTING CHECKLIST

- [ ] FTD fires and journey triggers within 5 seconds
- [ ] Branch correctly identifies Aviator vs Slots players
- [ ] Touch 1 bonus is credited immediately (check player's bonus balance)
- [ ] Touch 2 popup appears exactly at T+5min for in-session players
- [ ] Touch 2 popup does NOT appear for players who left before T+5min
- [ ] T+30min decision correctly detects in-session vs left
- [ ] Touch 4 SMS arrives at T+2h for session-exit players
- [ ] T+6h decision correctly detects return vs no-return
- [ ] Touch 5A popup + 100 CC credit for returned players
- [ ] Touch 5B SMS + 1,000 ARS time-limited bonus for non-returned
- [ ] Touch 6 email sent only to 24h inactive players
- [ ] Touch 6 bonus (75% match + 20 FS) auto-credits on deposit
- [ ] Touch 7 SMS sent only to 48h inactive players
- [ ] Touch 7 bonus (500 ARS free bet) auto-credits
- [ ] Journey exits correctly at 72h
- [ ] Frequency caps respected (max 3 messages/day during D1 Layer)
- [ ] UTM parameters present on all links

---

## COST SUMMARY

| Touch | Channel | Bonus Cost (per player) |
|-------|---------|------------------------|
| T1 | System | 50 FS (~400 ARS value) |
| T2 | Popup | None (awareness) |
| T3 | Widget | None |
| T4 | SMS | None (reminder) |
| T5A | Popup | 100 CC (~50 ARS) |
| T5B | SMS | 1,000 ARS |
| T6 | Email | 75% match + 20 FS (~2,600 ARS max) |
| T7 | SMS | 500 ARS |
| **Average per player** | | **~22% of average FTD (1,800 ARS)** |
