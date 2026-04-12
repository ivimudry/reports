# 11 — Loyalization — Implementation Guide

**Chain:** Loyalty Program Engagement (Active vs Passive Members)  
**Priority:** Phase 3 (Week 7–8)  
**Depends on:** Loyalty tier system active, CC balance tracking

---

## STEP 0: PRE-FLIGHT CHECKLIST

- [ ] Loyalty tier system configured (Standard / Silver / Gold / Platinum / VIP)
- [ ] CC earn, spend, and balance APIs functional
- [ ] Weekly progress metrics available (points earned this week, tier % progress)
- [ ] Player sub-segment tags available: `top_game_type` = Slots / Live / Aviator / Mixed
- [ ] Mission/challenge system ready (or Quest system from Chain 10 can be reused)
- [ ] CC expiry mechanism active (90-day rolling)
- [ ] Tier milestone event fires when player crosses tier threshold

---

## SEGMENT DEFINITIONS

### Active Loyalty Member
```
loyalty_enrolled = true
AND last_session_date ≤ 7 days ago
AND (loyalty_points_earned_30d > 0 OR deposits_30d ≥ 1)
```

### Passive Loyalty Member
```
loyalty_enrolled = true
AND (last_session_date > 7 days ago OR loyalty_points_earned_30d = 0)
AND account_age > 14 days
```

---

## A. ACTIVE LOYALTY MEMBERS (4 Communications)

### AL-C1: Weekly Progress Report (Every Monday)

| Setting | Value |
|---------|-------|
| Campaign ID | `11-AL-C1-EMAIL` |
| Channel | Email |
| Trigger | Scheduled, every Monday 10:00 ART |
| Segment | Active Loyalty Members |
| Subject (ES) | `📊 {points_earned} puntos esta semana — faltan {points_to_next_tier} para {next_tier}` |

**Email Content:**

- **Subject (ES):** `📊 {points_earned} puntos esta semana — faltan {points_to_next_tier} para {next_tier}`
- **Preheader (ES):** `Tu resumen semanal de loyalty con progreso detallado`
- **Banner Text (ES):** `Progreso Semanal: {points_earned} Puntos`
- **Banner Description:** Weekly progress dashboard — progress bar to next tier ({progress_pct}%), current tier badge, CC balance visual, golden momentum theme
- **Body Description:** Weekly stats section (points earned, CC balance, current tier). Visual progress bar to next tier. Sub-segment tailored recommendation: Slots players get double-points promo, Live players get VIP table offer, Aviator gets flight mission, Mixed get exploration bonus.
- **CTA (ES):** `Ver mi progreso` → Loyalty dashboard

---

### AL-C2: Mid-Week Boost (Wednesday)

| Setting | Value |
|---------|-------|
| Campaign ID | `11-AL-C2-PUSH` |
| Channel | App Push |
| Trigger | Scheduled, Wednesday 14:00 ART |
| Segment | Active Loyalty Members |

**Content (ES):**
```
IF points_this_week < weekly_avg:
  "Vas un poco más lento esta semana. Activá tu boost de puntos: 2x hasta medianoche."
ELSE:
  "¡Gran semana! Ya superaste tu promedio. Seguí así para alcanzar {next_tier}."
```

**Action:** Credit 2× point multiplier valid until midnight if below average.

---

### AL-C3: Weekend Challenge (Friday)

| Setting | Value |
|---------|-------|
| Campaign ID | `11-AL-C3-EMAIL-PUSH` |
| Channel | Email + App Push |
| Trigger | Scheduled, Friday 18:00 ART |
| Segment | Active Loyalty Members |
| Subject (ES) | `🏆 {challenge_reward}: desafío de fin de semana` |

**Email Content:**
- **Subject (ES):** `🏆 {challenge_reward}: desafío de fin de semana`
- **Preheader (ES):** `Completá el reto y ganá premios exclusivos`
- **Banner Text (ES):** `Desafío de Fin de Semana`
- **Banner Description:** Weekend challenge launch — trophy icon, challenge type visual (rotating weekly), reward preview, vibrant weekend party colors, action-oriented design
- **Body Description:** This weekend's rotating challenge details (wagering/game variety/multiplier/deposit streak). Reward breakdown. Sub-segment tailoring: slots vs live vs aviator-focused goals.
| Week | Challenge | Reward |
|------|-----------|--------|
| 1 | Wagered 15,000 ARS this weekend | 500 CC + 10 FS |
| 2 | Play 3 different game types | 300 CC + 15 FS |
| 3 | Win 5× your bet once | 400 CC + Lucky Wheel spin |
| 4 | Deposit every day Fri-Sun | 600 CC + 20 FS |

**Sub-segment tailoring:**
- Slots players: challenge skewed toward slot milestones
- Live players: live table wager goals
- Aviator: flight count / multiplier targets

---

### AL-C4: Tier Milestone (Event-based)

| Setting | Value |
|---------|-------|
| Campaign ID | `11-AL-C4-ALL` |
| Channel | In-app popup + Email + Push |
| Trigger | Event: `loyalty_tier_change` |
| Segment | Active Loyalty Members |

**Popup (ES):**
- **Banner Text (ES):** `¡Subiste a {new_tier}!`
- **Banner Description:** Tier upgrade celebration — new tier badge prominently displayed, sparkle/confetti, old tier fading upward into new tier, benefit icons previewed, luxurious gold/purple theme
- **Body (ES):** `¡Felicitaciones! Subiste a {new_tier}. Tus nuevos beneficios: Cashback {cashback_pct}%, {monthly_fs} giros mensuales, Soporte {support_level}.`
- **CTA (ES):** `Ver mis beneficios` → Loyalty dashboard

**Email:**
- **Subject (ES):** `👑 Bienvenido a {new_tier} — nuevos beneficios`
- **Preheader (ES):** `Descubrí todo lo que incluye tu nuevo nivel`
- **Banner Text (ES):** `Bienvenido a {new_tier}`
- **Banner Description:** Full tier welcome — new tier badge hero, benefit comparison table teaser, luxurious upgrade visual, golden/purple celebratory theme
- **Body Description:** Full welcome to new tier with benefit comparison table (cashback%, monthly FS, CC bonus%, support level). Compare old tier vs new tier. CTA to loyalty dashboard.

**Tier Benefits:**
| Tier | Cashback | Monthly FS | CC Bonus | Support |
|------|----------|-----------|----------|---------|
| Silver | 5% | 10 | +10% | Standard |
| Gold | 8% | 25 | +15% | Priority |
| Platinum | 12% | 50 | +25% | Dedicated |
| VIP | 15% | 100 | +40% | Personal manager |

---

## B. PASSIVE LOYALTY MEMBERS (4 Communications)

### PL-C1: Re-Engagement Nudge (Triggered: 8 days inactive)

| Setting | Value |
|---------|-------|
| Campaign ID | `11-PL-C1-SMS-EMAIL` |
| Channel | SMS + Email |
| Trigger | `last_session_date > 8 days` AND `loyalty_enrolled = true` |
| Segment | Passive Loyalty Members |

**SMS (ES):**
```
CuatroBet: Hace {days} días que no te vemos. Tus {cc_balance} CC te esperan. Entrá hoy y ganá puntos dobles: {link}
```

**Email:**
- **Subject (ES):** `👋 {cc_balance} Cuatro Coins te esperan`
- **Preheader (ES):** `Hoy ganás puntos dobles si volvés a jugar`
- **Banner Text (ES):** `{cc_balance} CC Te Esperan`
- **Banner Description:** Re-engagement — Cuatro Coins pile glowing with "{cc_balance}" number prominent, tier progress bar hint, 2× points badge, warm welcoming tones
- **Body Description:** Show CC balance prominently. Show proximity to next tier. Announce 2× points active for 48h. Soft re-engagement tone.
- **CTA (ES):** `Volver a jugar` → Homepage

---

### PL-C2: Easy Mission Offer (T+3 days after C1)

| Setting | Value |
|---------|-------|
| Campaign ID | `11-PL-C2-EMAIL` |
| Channel | Email |
| Condition | Did NOT log in after C1 |
| Subject (ES) | `🎯 200 CC + 10 giros: misión fácil de 1 depósito` |

**Email Content:**
- **Subject (ES):** `🎯 200 CC + 10 giros: misión fácil de 1 depósito`
- **Preheader (ES):** `Solo un depósito y los premios son tuyos`
- **Banner Text (ES):** `Misión Fácil: 200 CC + 10 Giros`
- **Banner Description:** Easy mission — single deposit icon, low barrier visual, 200 CC + 10 FS reward preview, "only 1 deposit" badge, encouraging green/gold tones
- **Body Description:** Simple offer: 1 deposit of {min_deposit} ARS = 200 CC + 10 FS. Valid 48h. By-tier minimum deposit amounts shown.

**Min deposit by tier:**
| Tier | Min Deposit |
|------|------------|
| Standard | 1,000 ARS |
| Silver | 1,500 ARS |
| Gold | 2,000 ARS |
| Platinum | 3,000 ARS |

---

### PL-C3: CC Expiry Warning (30 days before expiry)

| Setting | Value |
|---------|-------|
| Campaign ID | `11-PL-C3-EMAIL-PUSH` |
| Channel | Email + Push |
| Trigger | `cc_expiry_date - 30 days` |
| Segment | Passive Loyalty Members with CC balance > 0 |

**Push (ES):**
```
Tus {cc_balance} Cuatro Coins vencen en 30 días. Usalos o perdelos.
```

**Email:**
- **Subject (ES):** `⚠️ {cc_balance} CC vencen el {expiry_date}`
- **Preheader (ES):** `Canjeálos antes de que desaparezcan para siempre`
- **Banner Text (ES):** `{cc_balance} CC Vencen Pronto`
- **Banner Description:** Expiry warning — CC balance fading/dissolving visual, countdown timer to {expiry_date}, redemption options icons (FS, cash, Lucky Wheel), amber urgency tones
- **Body Description:** CC balance with countdown to expiry date. Redemption options: FS, bonus cash, Lucky Wheel entries. Urgency framing.
- **CTA (ES):** `Canjear mis CC` → CC shop

---

### PL-C4: Last Chance (7 days before CC expiry)

| Setting | Value |
|---------|-------|
| Campaign ID | `11-PL-C4-SMS-PUSH` |
| Channel | SMS + Push |
| Trigger | `cc_expiry_date - 7 days` |
| Condition | CC balance still > 0 AND no login since C3 |

**SMS (ES):**
```
CuatroBet: ÚLTIMA OPORTUNIDAD. Tus {cc_balance} CC vencen en 7 días. Canjalos ahora: {link}
```

**Push (ES):**
```
⏰ 7 días para canjear tus {cc_balance} CC. No los pierdas.
```

**Sweetener:** Add +100 CC bonus if they log in and redeem within 48h.

---

## EXIT CONDITIONS

| Condition | Action |
|-----------|--------|
| Active → login within 7 days of comm | Stay in Active flow, reset timers |
| Active → tier upgraded | Fire AL-C4, reset weekly cycle |
| Passive → logs in after C1 or C2 | Move to Active flow |
| Passive → redeems CC after C3/C4 | Move to Active flow |
| Passive → CC expires with no action | Remove from loyalty comms, move to Chain 12 (Reactivation) |

---

## TESTING CHECKLIST

- [ ] Active segment correctly includes only 7-day active loyalty members
- [ ] Passive segment correctly excludes non-loyalty members
- [ ] Weekly progress email shows correct CC balance, tier progress
- [ ] Sub-segment tailoring (Slots/Live/Aviator/Mixed) renders correct content
- [ ] Mid-week boost applies 2× multiplier correctly
- [ ] Weekend challenges rotate weekly (4-week cycle)
- [ ] Tier milestone fires immediately on upgrade event
- [ ] Tier benefits table matches configuration
- [ ] CC expiry warning fires at exactly 30 days
- [ ] Last chance fires at exactly 7 days
- [ ] +100 CC sweetener credits only if login within 48h
- [ ] Passive → Active transition works (player moved between flows)
- [ ] No duplicate comms if player transitions mid-week

---

## KPI TARGETS

| Metric | Target |
|--------|--------|
| Active loyalty weekly email open rate | ≥ 35% |
| Passive re-engagement login within 48h (C1) | ≥ 15% |
| CC expiry redemption rate (C3+C4) | ≥ 40% |
| Tier upgrade rate (monthly) | ≥ 8% of Active |
| Weekend challenge completion | ≥ 25% |
