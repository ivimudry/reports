# 07 — No Bonus Cluster — Implementation Guide

**Chain:** No Bonus Cluster (players who didn't claim welcome bonus)  
**Two Branches:** Missed (didn't see) vs None Interested (actively declined)  
**Estimated Communications:** 4 per branch = 8 total  
**Prerequisites from Master Doc:** Attributes `welcome_bonus_claimed`, `welcome_bonus_status`; Segments `SEG-BONUS-MISSED`, `SEG-BONUS-DECLINED`

---

## STEP 0: PRE-FLIGHT CHECKLIST

- [ ] Attribute `welcome_bonus_claimed` tracks whether player claimed the welcome bonus
- [ ] Attribute `welcome_bonus_status` distinguishes: `available` / `claimed` / `declined` / `expired`
- [ ] Detection logic exists for "bonus bypassed" (player clicked through bonus flow without claiming)
- [ ] Demo/free play links work: `{base_url}/game/{game_id}?demo=true`
- [ ] Top 5 games list available for email personalization
- [ ] 200 CC / 300 CC bonus templates created (for sweeteners in Comms 4)

---

## STEP 1: CREATE TWO JOURNEYS

| Journey Name | Entry Trigger | Segment |
|-------------|---------------|---------|
| `07-NB-MISS-JOURNEY` | `deposit_count = 0` AND `welcome_bonus_claimed = false` AND `hours_since_registration >= 1` AND NO bonus interaction detected | `SEG-BONUS-MISSED` |
| `07-NB-NONE-JOURNEY` | `welcome_bonus_status = "declined"` OR bonus flow bypassed | `SEG-BONUS-DECLINED` |

**Global exit for both:** `deposit_success` → exit, enter Day 1 Retention Layer.

---

## STEP 2: BRANCH A — MISSED (Didn't See the Bonus)

**Strategy:** Direct — remind them the bonus exists, guide them to cashier.

### Comm 1 — T+1h

| Setting | Value |
|---------|-------|
| **Campaign ID** | `07-NB-MISS-C1-POPUP-SMS` |
| **Channel** | In-app popup (if in session) OR SMS |
| **Timing** | 1 hour after registration |

**Popup Content (ES):**
- **Banner Text (ES):** `¡No Te Pierdas Tu Bono!`
- **Banner Description:** Alert/reminder theme — gift box with "120% + 50 FS" floating above, spotlight effect, golden glow, exclamation icon
- **Body (ES):** `120% + 50 giros gratis te esperan con tu primer depósito.`
- **CTA (ES):** `Reclamar bono` → `{base_url}/cashier`

**SMS Content (ES):**
- Text: `CuatroBet: ¡No te pierdas tu bono de bienvenida! 120% + 50 giros gratis te esperan: {link}`

---

### Comm 2 — T+6h

| Setting | Value |
|---------|-------|
| **Campaign ID** | `07-NB-MISS-C2-EMAIL` |
| **Channel** | Email |

**Email Content:**
- **Subject (ES):** `🎰 120% + 50 giros - no te pierdas tu bono`
- **Preheader (ES):** `Depositá en 2 minutos y activalo`
- **Banner Text (ES):** `120% + 50 Giros Gratis`
- **Banner Description:** Bonus reminder hero — large "120%" text in gold, Gates of Olympus artwork background, step-by-step icons (1-2-3) shown below, warm inviting colors
- **Body Description:** Step-by-step deposit guide (3 easy steps) with visual icons. Show available payment methods. Emphasize speed — "2 minutes to activate."
- **CTA (ES):** `Depositar y activar` → `{base_url}/cashier`

---

### Comm 3 — T+24h

| Setting | Value |
|---------|-------|
| **Campaign ID** | `07-NB-MISS-C3-SMS` |
| **Channel** | SMS |

**SMS Content (ES):**
- Text: `CuatroBet: Tu bono de 120% + 50 giros vence pronto. Activalo ahora: {link}`

---

### Comm 4 — T+48h

| Setting | Value |
|---------|-------|
| **Campaign ID** | `07-NB-MISS-C4-EMAIL` |
| **Channel** | Email |

**Email Content:**
- **Subject (ES):** `⏰ Última oportunidad: tu bono expira en 24h`
- **Preheader (ES):** `Reclamá tu 120% + 200 CC extra antes de que sea tarde`
- **Banner Text (ES):** `Última Oportunidad — 24h`
- **Banner Description:** Urgency countdown — large timer showing 24:00:00, welcome bonus visual fading away, red/amber urgency tones, "last chance" ribbon
- **Body Description:** Final urgency framing with countdown visual. Big prominent CTA. Offer: welcome bonus + extra 200 CC sweetener as final incentive.
- **CTA (ES):** `Reclamar ahora` → `{base_url}/cashier`

**Exit:** Bonus claimed → Day 1 Retention. No response → Reactivation (pre-FTD cohort).

---

## STEP 3: BRANCH B — NONE INTERESTED (Actively Declined)

**Strategy:** Do NOT push bonuses. Focus on product discovery and habit-seeding. Low pressure.

### Comm 1 — T+2h

| Setting | Value |
|---------|-------|
| **Campaign ID** | `07-NB-NONE-C1-POPUP` |
| **Channel** | In-app popup |
| **Timing** | 2 hours after registration |

**Popup Content (ES):**
- **Banner Text (ES):** `Descubrí los Juegos Más Populares`
- **Banner Description:** Game discovery theme — Gates of Olympus artwork featured prominently, "FREE DEMO" badge, game thumbnails grid hint, exciting play-now vibe
- **Body (ES):** `Probá Gates of Olympus gratis — sin depósito necesario.`
- **CTA (ES):** `Jugar demo` → `{base_url}/game/gates-of-olympus?demo=true`
- **NO bonus mention** — pure game discovery

---

### Comm 2 — T+24h

| Setting | Value |
|---------|-------|
| **Campaign ID** | `07-NB-NONE-C2-EMAIL` |
| **Channel** | Email |

**Email Content:**
- **Subject (ES):** `🎮 Los 5 juegos más populares esta semana`
- **Preheader (ES):** `Gates of Olympus, Jackpot Joker y más te esperan`
- **Banner Text (ES):** `Top 5 Juegos de la Semana`
- **Banner Description:** Game showcase — collage of top 5 game thumbnails (Gates of Olympus, Joker's Jewels, Jackpot Joker, Roulette, Aviator), "TOP 5" badge, vibrant gaming atmosphere
- **Body Description:** Curated top 5 games list with thumbnails and mini-descriptions. Each game with individual "Jugar" deep link. Soft footer note: bonus still available if they change their mind.
- **CTA (ES):** `Explorar juegos` → `{base_url}/games`

---

### Comm 3 — T+72h

| Setting | Value |
|---------|-------|
| **Campaign ID** | `07-NB-NONE-C3-SMS` |
| **Channel** | SMS |

**SMS Content (ES):**
- Text: `CuatroBet: Jackpot Joker tiene 10 millones de premio. Probalo gratis: {link}`
- Link: `{base_url}/game/jackpot-joker?demo=true`

---

### Comm 4 — T+7 days

| Setting | Value |
|---------|-------|
| **Campaign ID** | `07-NB-NONE-C4-EMAIL` |
| **Channel** | Email |

**Email Content:**
- **Subject (ES):** `👋 Tu cuenta sigue lista`
- **Preheader (ES):** `Nuevos juegos, novedades y tu bono te esperan`
- **Banner Text (ES):** `Tu Cuenta Te Espera`
- **Banner Description:** Welcoming return visual — CuatroBet logo glow, warm inviting scene, new game release thumbnails, community vibe, soft golden tones
- **Body Description:** Soft re-engagement: new game releases this week, community highlights, what's happening. Soft bonus mention in footer: welcome bonus still available.
- **CTA (ES):** `Volver a CuatroBet` → `{base_url}`

**Exit:** Any deposit → Day 1 Retention Layer. No response → Reactivation (pre-FTD, low-engagement filter).

---

## STEP 4: TESTING CHECKLIST

- [ ] Branch A correctly identifies players who MISSED the bonus (no interaction, not declined)
- [ ] Branch B correctly identifies players who DECLINED the bonus (explicit action or bypass)
- [ ] Branch A: All 4 comms mention the welcome bonus directly
- [ ] Branch B: Comm 1 and Comm 3 have NO bonus mention (product discovery only)
- [ ] Branch B: Comm 2 and Comm 4 only have SOFT bonus mention in footer
- [ ] Demo links work correctly: `?demo=true` opens game in free play mode
- [ ] Global exit fires instantly on `deposit_success`
- [ ] 200 CC sweetener in Branch A Comm 4 credits correctly
- [ ] Frequency caps: max 2 messages/day (pre-FTD segment)
- [ ] UTM parameters on all links
