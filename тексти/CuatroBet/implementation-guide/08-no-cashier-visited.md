# 08 — No Cashier Visited — Implementation Guide

**Chain:** No Cashier Visited (registered players who never opened the deposit page)  
**Three Paths:** Bounce (quick exit) / Long Session (browsed, no cashier) / Free Spins (played demo)  
**Estimated Communications:** 4 per path = 12 total  
**Prerequisites from Master Doc:** Events `session_start`, `session_end`, `cashier_opened`, `game_launched`; Attributes `last_session_duration_seconds`, `has_played_demo`, `deposit_count`; Segments `SEG-BOUNCE`, `SEG-LONG-NO-CASHIER`, `SEG-FS-NO-DEP`

---

## STEP 0: PRE-FLIGHT CHECKLIST

- [ ] Event `session_end` carries `session_duration_seconds`
- [ ] Event `cashier_opened` fires when player navigates to deposit page
- [ ] Attribute `has_played_demo` tracks demo/free-spin play
- [ ] Segment `SEG-BOUNCE`: session <60 seconds + no cashier interaction
- [ ] Segment `SEG-LONG-NO-CASHIER`: session >600 seconds + no cashier
- [ ] Segment `SEG-FS-NO-DEP`: played demo/FS + no deposit
- [ ] Demo game links: `{base_url}/game/{game_id}?demo=true`
- [ ] Session browsing history available for personalization (optional, for Path B Comm 2)

---

## STEP 1: CREATE THREE JOURNEYS

| Journey Name | Entry Trigger | Segment |
|-------------|---------------|---------|
| `08-NC-BOUNCE-JOURNEY` | `session_end` WHERE `session_duration < 60` AND `deposit_count = 0` AND no `cashier_opened` event | `SEG-BOUNCE` |
| `08-NC-LONG-JOURNEY` | `session_end` WHERE `session_duration >= 600` AND `deposit_count = 0` AND no `cashier_opened` event | `SEG-LONG-NO-CASHIER` |
| `08-NC-FS-JOURNEY` | `free_spins_used` OR `game_launched` WHERE `is_demo = true` AND `deposit_count = 0` | `SEG-FS-NO-DEP` |

**Global exit for all:** `deposit_success` → exit, enter Day 1 Retention Layer.

---

## STEP 2: PATH A — BOUNCE (Session <60 seconds)

**Assumption:** Player likely had a tech issue or wasn't hooked enough to explore.

### Comm 1 — T+15 min

| Setting | Value |
|---------|-------|
| **Campaign ID** | `08-NC-BOUNCE-C1-SMS` |
| **Channel** | SMS |
| **Timing** | 15 min after bounce |

**SMS Content (ES):**
- Text: `CuatroBet: Te fuiste rápido! Tu bono de 120% + 50 giros te espera. Volvé: {link}`
- Link: `{base_url}?utm_source=sms&utm_medium=crm&utm_campaign=08-NC-BOUNCE-C1`

---

### Comm 2 — T+4h

| Setting | Value |
|---------|-------|
| **Campaign ID** | `08-NC-BOUNCE-C2-EMAIL` |
| **Channel** | Email |

**Email Content:**
- **Subject (ES):** `🛠️ ¿Problema técnico? Tu cuenta está lista`
- **Preheader (ES):** `Tu bono de 120% + 50 giros te espera`
- **Banner Text (ES):** `Tu Cuenta Está Lista`
- **Banner Description:** Helpful tech-support theme — checkmark over device icon, step-by-step 1-2-3-4 icons, payment method logos (Mercado Pago, card, transfer), welcoming blue/green tones
- **Body Description:** Assume possible tech issue. Quick-start deposit guide (4 steps: log in, click deposit, choose payment, done). Show payment method options. Emphasize bonus activates instantly.
- **CTA (ES):** `Empezar ahora` → `{base_url}/cashier`

---

### Comm 3 — T+24h

| Setting | Value |
|---------|-------|
| **Campaign ID** | `08-NC-BOUNCE-C3-SMS` |
| **Channel** | SMS |

**SMS Content (ES):**
- Text: `CuatroBet: 120% + 50 giros gratis en Gates of Olympus. Depositá en 2 minutos: {link}`

---

### Comm 4 — T+72h

| Setting | Value |
|---------|-------|
| **Campaign ID** | `08-NC-BOUNCE-C4-EMAIL` |
| **Channel** | Email |

**Email Content:**
- **Subject (ES):** `⏰ Bono expira pronto - 120% + 50 giros`
- **Preheader (ES):** `Última oportunidad para activar tu bono de bienvenida`
- **Banner Text (ES):** `Bono Expira Pronto`
- **Banner Description:** Urgency countdown — fading bonus visual, timer/clock icon, "120% + 50 FS" in amber, 200 CC coins as extra sweetener, red urgency accents
- **Body Description:** Final urgency — welcome bonus expiry countdown visual. Offer: welcome bonus + 200 CC sweetener. Big prominent CTA.
- **CTA (ES):** `Activar bono` → `{base_url}/cashier`

**Exit:** Cashier visit + deposit → Day 1 Retention. No response → Reactivation (pre-FTD).

---

## STEP 3: PATH B — LONG SESSION (Browsed >10 min, No Cashier)

**Strategy:** These players showed genuine interest. Higher quality lead — personalize based on browsing.

### Comm 1 — T+30 min

| Setting | Value |
|---------|-------|
| **Campaign ID** | `08-NC-LONG-C1-POPUP-SMS` |
| **Channel** | In-app popup (next session) OR SMS |
| **Timing** | 30 min after session end |

**Popup Content (ES):**
- **Banner Text (ES):** `¿Te Gustó Lo Que Viste?`
- **Banner Description:** Positive engagement visual — game thumbnails from player's browse history, welcoming overlay, 120% bonus preview, sparkle effect
- **Body (ES):** `¿Te gustó lo que viste? Con tu primer depósito desbloquás 120% + 50 giros y mucho más.`
- **CTA (ES):** `Depositar ahora` → `{base_url}/cashier`

**SMS Content (ES):**
- Text: `CuatroBet: ¿Te gustó lo que viste? 120% + 50 giros con tu primer depósito: {link}`

---

### Comm 2 — T+6h

| Setting | Value |
|---------|-------|
| **Campaign ID** | `08-NC-LONG-C2-EMAIL` |
| **Channel** | Email |

**Email Content:**
- **Subject (ES):** `🎰 120% + 50 giros - tus juegos favoritos te esperan`
- **Preheader (ES):** `Desde solo 500 ARS activás todo`
- **Banner Text (ES):** `120% + 50 Giros — Desde 500 ARS`
- **Banner Description:** Personalized gaming — game thumbnails from player's browse session, "120%" large golden overlay, "desde 500 ARS" low-barrier badge, vibrant gaming atmosphere
- **Body Description:** Reference games/pages player browsed (session data personalization). Low barrier messaging: "desde solo 500 ARS." Show offer: 120% bonus + 50 FS on Gates of Olympus. Payment methods: Mercado Pago, card, transfer.
- **CTA (ES):** `Depositar y jugar` → `{base_url}/cashier`
- **Key message:** Low barrier — "desde solo 500 ARS"

---

### Comm 3 — T+24h

| Setting | Value |
|---------|-------|
| **Campaign ID** | `08-NC-LONG-C3-SMS` |
| **Channel** | SMS |

**SMS Content (ES):**
- Text: `CuatroBet: Gates of Olympus, Jackpot Joker y más. Tu bono de 120% te espera: {link}`

---

### Comm 4 — T+48h

| Setting | Value |
|---------|-------|
| **Campaign ID** | `08-NC-LONG-C4-EMAIL` |
| **Channel** | Email |

**Email Content:**
- **Subject (ES):** `💡 300 CC extra + 50 giros gratis`
- **Preheader (ES):** `Último recordatorio, tu bono te espera`
- **Banner Text (ES):** `Último Recordatorio — 300 CC Extra`
- **Banner Description:** Final reminder — welcome bonus fading visual, 300 Cuatro Coins pile as sweetener highlight, urgency amber/gold, "last chance" ribbon
- **Body Description:** Final reminder with urgency. Offer: welcome bonus + 300 CC sweetener (higher than Bounce — player showed real browsing interest). Clear CTA.
- **CTA (ES):** `Activar bono` → `{base_url}/cashier`

**Exit:** Deposit → Day 1 Retention. No response → Reactivation (pre-FTD, high-engagement filter).

---

## STEP 4: PATH C — FREE SPINS (Played Demo)

**Strategy:** Bridge from free play to real money. Emphasize the upgrade from demo to real winnings.

### Comm 1 — T+15 min

| Setting | Value |
|---------|-------|
| **Campaign ID** | `08-NC-FS-C1-POPUP` |
| **Channel** | In-app popup |
| **Timing** | 15 min after FS/demo session |

**Popup Content (ES):**
- **Banner Text (ES):** `¡Bien Jugado!`
- **Banner Description:** Demo-to-real bridge — game artwork of the demo they played, "REAL WINNINGS" badge overlay, coins/cash visual, upgrade arrow from demo to real
- **Body (ES):** `Con un depósito real desbloquás 120% + 50 giros extra. Ganancias reales.`
- **CTA (ES):** `Depositar ahora` → `{base_url}/cashier`

---

### Comm 2 — T+3h

| Setting | Value |
|---------|-------|
| **Campaign ID** | `08-NC-FS-C2-SMS` |
| **Channel** | SMS |

**SMS Content (ES):**
- Text: `CuatroBet: Tus giros gratis ya terminaron. Con 500 ARS activás 120% + 50 giros más: {link}`
- **Key message:** Low barrier — "Con 500 ARS"

---

### Comm 3 — T+12h

| Setting | Value |
|---------|-------|
| **Campaign ID** | `08-NC-FS-C3-EMAIL` |
| **Channel** | Email |

**Email Content:**
- **Subject (ES):** `💰 De giros gratis a ganancias reales`
- **Preheader (ES):** `Con 500 ARS desbloquás 120% + 50 giros extra`
- **Banner Text (ES):** `Ganancias Reales Te Esperan`
- **Banner Description:** Demo-to-real upgrade — split visual: left side demo/free play (faded), right side real money (vibrant coins, cash), arrow bridge, player's demo game artwork, "desde 500 ARS" badge
- **Body Description:** Congratulate demo play. Bridge to real money: show offer (120% match + 50 FS on their played game). Emphasize real withdrawable winnings. Low barrier: desde 500 ARS.
- **CTA (ES):** `Depositar y jugar` → `{base_url}/cashier`

---

### Comm 4 — T+48h

| Setting | Value |
|---------|-------|
| **Campaign ID** | `08-NC-FS-C4-SMS` |
| **Channel** | SMS |

**SMS Content (ES):**
- Text: `CuatroBet: 10 giros gratis extra sin depósito. Probá suerte: {link}`
- Offer: 10 additional no-deposit FS as a second hook
- Link: `{base_url}/game/{last_demo_game}?utm_source=sms&utm_medium=crm&utm_campaign=08-NC-FS-C4`

**Exit:** Deposit → Day 1 Retention. No response → Reactivation (pre-FTD, free-spins sub-cohort).

---

## STEP 5: TESTING CHECKLIST

- [ ] Path A: Bounce detection correct (session <60s + no cashier)
- [ ] Path B: Long session detection correct (session >600s + no cashier)
- [ ] Path C: Demo/FS play detection correct
- [ ] All 3 paths exit immediately on `deposit_success`
- [ ] Path A Comm 2: Quick-start guide renders with payment method icons
- [ ] Path B: Browsing personalization works (if available from session data)
- [ ] Path C: Game personalization (`{game_they_played}`) resolves correctly
- [ ] Path C Comm 4: 10 no-deposit FS credit on link click
- [ ] Sweetener amounts: Bounce = 200 CC, Long Session = 300 CC, FS = 10 extra FS
- [ ] Frequency caps: max 2/day (pre-FTD segment)
- [ ] No overlap between paths (player enters only ONE path based on behavior)
- [ ] UTM parameters on all links

---

## SUMMARY

| Path | Lead Quality | Sweetener | Strategy |
|------|-------------|-----------|----------|
| A: Bounce | Low | 200 CC | Assume tech issue, guide |
| B: Long Session | High | 300 CC | Personalize, low-barrier messaging |
| C: Free Spins | Medium | 10 extra FS | Bridge demo → real money |
