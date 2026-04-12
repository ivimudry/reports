# 10 — Engagement & Gamification — Implementation Guide

**Chain:** Engagement (Loot Boxes, Stickers, 8 Quests, Weekly/Daily/Holiday Bonuses)  
**Priority:** Phase 3 (Week 7–8)  
**This is the largest chain — break into sub-projects below**

---

## STEP 0: PRE-FLIGHT CHECKLIST

- [ ] CC (Cuatro Coins) credit/debit API functional
- [ ] Lucky Wheel system active with Silver/Gold/Platinum tiers
- [ ] In-app popup and App Push channels active
- [ ] Loot box UI ready in player dashboard
- [ ] Sticker book UI ready (30-slot grid)
- [ ] Quest progress tracking API available
- [ ] Wagering amount tracked per game type in real-time
- [ ] Login tracking for daily streak feature
- [ ] Argentine holiday calendar configured for the year

---

## A. LOOT BOXES

**Journey Name:** `10-LB-JOURNEY`  
**Type:** Event-triggered (ongoing)  
**Entry:** `total_wagered_ars` reaches next 5,000 ARS increment (slots) or 10,000 ARS (live)

### Earn Rules:
- 1 loot box token per 5,000 ARS wagered on slots
- 1 loot box token per 10,000 ARS wagered on live
- Tokens accumulate in dashboard, opened manually

### Reward Table:

| Reward | Weight | Value |
|--------|--------|-------|
| Small CC gift | 50% | 25–50 CC |
| Free Spins (5–10) | 25% | On player's top slot |
| Bonus Cash | 15% | 500–1,000 ARS |
| Lucky Wheel Entry | 7% | 1 Silver entry |
| Premium FS (25+) | 3% | On premium titles |

### Build 4 Communications:

**LB-C1: Token Earned (on event)**
| Setting | Value |
|---------|-------|
| Campaign ID | `10-LB-C1-PUSH` |
| Channel | App Push |
| Text (ES) | `¡Ganaste un loot box! Abrilo desde tu panel.` |
| CTA | Deep link to loot box dashboard |

**LB-C2: Box Opened (on event)**
| Setting | Value |
|---------|-------|
| Campaign ID | `10-LB-C2-POPUP` |
| Channel | In-app popup |
| **Banner Text (ES)** | `¡Loot Box Abierto!` |
| **Banner Description** | Celebration loot box opening — glowing box bursting open, reward icon revealed ({reward}), sparkle/confetti animation, golden light rays |
| **Body (ES)** | `{reward} desbloqueado. ¡Seguí jugando para más!` |

**LB-C3: Weekly Unclaimed Reminder (Monday)**
| Setting | Value |
|---------|-------|
| Campaign ID | `10-LB-C3-EMAIL` |
| Channel | Email |
| **Subject (ES)** | `🎁 {count} loot boxes sin abrir te esperan` |
| **Preheader (ES)** | `Descubrí qué hay adentro antes de que expiren` |
| **Banner Text (ES)** | `{count} Loot Boxes Sin Abrir` |
| **Banner Description** | Mystery loot boxes — stack of glowing unopened boxes, question marks floating, treasure hint, exciting blue/purple tones |
| **Body Description** | Reminder of unclaimed loot boxes with mystery teaser. List possible rewards. Single CTA to dashboard. |
| Condition | Player has ≥1 unopened loot box |
| **CTA (ES)** | `Abrir ahora` → dashboard |

**LB-C4: Monthly Summary (1st of month)**
| Setting | Value |
|---------|-------|
| Campaign ID | `10-LB-C4-EMAIL` |
| Channel | Email |
| **Subject (ES)** | `📊 Tu resumen mensual de loot boxes` |
| **Preheader (ES)** | `Mirá todo lo que ganaste este mes` |
| **Banner Text (ES)** | `Resumen Mensual de Loot Boxes` |
| **Banner Description** | Monthly recap visual — opened loot boxes collage, reward summary icons, comparison chart (vs last month), celebratory purple/gold theme |
| **Body Description** | Monthly loot box stats: boxes opened, total rewards won, comparison to last month, teaser for next month. |

---

## B. STICKERS

**Journey Name:** `10-STK-JOURNEY`  
**Mechanic:** 30-slot sticker book. Specific actions unlock stickers. Row of 5 = reward. All 30 = grand prize.

### Sticker Actions (examples — configure 30):
| Sticker | Action Required |
|---------|----------------|
| #1 | Play Jackpot Joker 10 times |
| #2 | Deposit 3 days in a row |
| #3 | Try a new game provider |
| #4 | Wager 10,000 ARS in a week |
| #5 | Win 5× your bet in one spin |
| ... | (Define remaining 25) |

### Reward Tiers:
| Milestone | Reward |
|-----------|--------|
| Single sticker | 25 CC |
| Row of 5 complete | 200 ARS + 10 FS |
| All 30 complete | 10,000 ARS + Premium Lucky Wheel + VIP I preview |

### Build 4 Communications:

**STK-C1: Sticker Unlocked**
| Campaign ID | `10-STK-C1-PUSH` |
|------------|-------------------|
| Channel | App Push |
| Text (ES) | `Nueva figurita desbloqueada: {sticker_name}. ¡Seguí coleccionando!` |

**STK-C2: One Sticker Away from Row**
| Campaign ID | `10-STK-C2-EMAIL` |
|------------|---------------------|
| Channel | Email |
| **Subject (ES)** | `🧩 200 ARS + 10 giros: te falta 1 figurita` |
| **Preheader (ES)** | `Completá la fila y ganate el premio` |
| **Banner Text (ES)** | `¡Te Falta 1 Figurita!` |
| **Banner Description** | Almost-complete sticker row — 4/5 sticker slots filled, last slot glowing/pulsing with question mark, 200 ARS + 10 FS reward preview, exciting urgency |
| **Body Description** | Highlight which sticker is missing and what action unlocks it. Show reward preview: 200 ARS + 10 FS. Clear CTA to complete the action. |
| Condition | 4 of 5 stickers in a row collected |

**STK-C3: Row Complete**
| Campaign ID | `10-STK-C3-PUSH-POPUP` |
|------------|--------------------------|
| Channel | App Push + In-app popup |
| **Banner Text (ES)** | `¡Fila Completa!` |
| **Banner Description** | Celebration row complete — 5/5 stickers glowing, reward burst animation (200 ARS + 10 FS), confetti, golden completion badge |
| **Body (ES)** | `¡Fila completa! Ganaste 200 ARS + 10 giros gratis.` |
| Action | Credit 200 ARS + 10 FS |

**STK-C4: Monthly Summary**
| Campaign ID | `10-STK-C4-EMAIL` |
|------------|---------------------|
| Channel | Email |
| **Subject (ES)** | `📈 {count} figuritas este mes — faltan {remaining}` |
| **Preheader (ES)** | `El gran premio de 10,000 ARS está cada vez más cerca` |
| **Banner Text (ES)** | `{count} Figuritas Coleccionadas` |
| **Banner Description** | Monthly sticker progress — sticker book grid showing filled/empty slots, progress bar to 30, grand prize preview (10,000 ARS + VIP), collector theme |
| **Body Description** | Monthly sticker recap: count collected, remaining to grand prize, next achievable sticker hint, motivation. |

---

## C. QUESTS (8 Quest Types)

### Quest 1: 4 Deposit Quest ("Misión Cuatro")

**Journey Name:** `10-Q1-MISSION-CUATRO`  
**Auto-enrollment:** On FTD  
**Window:** 7 rolling days  
**Rewards:** Escalating per deposit (see spec)

| Comm | Campaign ID | Timing | Channel | Content (ES) |
|------|------------|--------|---------|-------------|
| C1 | `10-Q1-C1-POPUP-EMAIL` | On FTD | Popup + Email | **Popup Banner:** Quest activation — "Misión Cuatro" logo, 4-step progress bar, first reward preview. **Email Banner:** Same. **Body:** `¡Misión Cuatro activada! 4 depósitos en 7 días = premios increíbles.` |
| C2 | `10-Q1-C2-PUSH` | After 2nd deposit | App Push | `¡Vas por la mitad! 2 depósitos más para completar la Misión Cuatro.` |
| C3 | `10-Q1-C3-SMS` | After 3rd deposit | SMS | `CuatroBet: ¡Falta 1 depósito para ganar 30 giros + 200 CC + bono 50%! {link}` |
| C4 | `10-Q1-C4-POPUP-EMAIL` | After 4th deposit | Popup + Email | **Popup Banner:** Mission complete — 4/4 checkmarks, confetti, reward cascade. **Email Banner:** Same + reward summary. **Body:** `¡Misión Cuatro completa! Tus premios están acreditados.` |

**Rewards per deposit:**
| Deposit | FS | CC | Extra |
|---------|-----|-----|-------|
| 1st | 10 FS | 50 CC | — |
| 2nd | 15 FS | 75 CC | — |
| 3rd | 20 FS | 100 CC | — |
| 4th | 30 FS | 200 CC | 50% match up to 3,000 ARS |

---

### Quest 2: Double Chance (Weekend Lucky Wheel)

**Journey Name:** `10-Q2-DOUBLE-CHANCE`  
**Trigger:** Scheduled (1 weekend per month)

| Comm | Campaign ID | Timing | Channel | Content (ES) |
|------|------------|--------|---------|-------------|
| C1 | `10-Q2-C1-EMAIL` | Friday AM | Email | **Subject:** `🎡 Doble Chance este fin de semana` **Preheader:** `Cada depósito = 2 giros en Lucky Wheel` **Banner Text:** `Doble Chance — Este Fin de Semana`. **Banner Desc:** Lucky Wheel ×2 visual, weekend party vibe, golden coins. **Body Desc:** Weekend promo details: each deposit = 2 Lucky Wheel spins, available Sat-Sun only. |
| C2 | `10-Q2-C2-PUSH` | Saturday | Push | `Doble Chance está activo. Depositá y girá 2 veces.` |
| C3 | `10-Q2-C3-SMS` | Sunday | SMS | `CuatroBet: Último día de Doble Chance. Depositá y girá 2 veces: {link}` |
| C4 | `10-Q2-C4-EMAIL` | Monday | Email | **Subject:** `📊 Tu resumen de Doble Chance` **Preheader:** `Mirá cuántos giros usaste y qué ganaste` **Banner Text:** `Doble Chance — Resumen`. **Banner Desc:** Recap visual — Lucky Wheel results, total spins count. **Body Desc:** Weekend recap: total spins used, rewards won, teaser for next month's Double Chance. |

---

### Quest 3: Silver Spin (Tiered Wheel)

**Journey Name:** `10-Q3-SILVER-SPIN`  
**Ongoing:** Spin earned on wagering milestones

| Comm | Campaign ID | Timing | Channel | Content (ES) |
|------|------------|--------|---------|-------------|
| C1 | `10-Q3-C1-PUSH` | On earn | Push | `¡Ganaste un giro {tier}! Usalo ahora.` |
| C2 | `10-Q3-C2-SMS` | 48h after earn | SMS | `CuatroBet: Tu giro {tier} está sin usar. No lo pierdas: {link}` |
| C3 | `10-Q3-C3-PUSH` | 24h before expiry | Push | `Tu giro {tier} vence mañana. Usalo: {link}` |
| C4 | `10-Q3-C4-POPUP` | After spin | Popup | **Banner Text:** `¡Ganaste {reward}!` **Banner Desc:** Lucky Wheel result celebration — {tier} wheel stopping on reward, sparkle animation, reward icon. **Body:** `¡Giraste y ganaste {reward}!` |

**Tiers:** Silver (2K wager) / Gold (10K wager) / Platinum (50K wager)

---

### Quest 4: Steady Flow (Same Amount × 4)

**Journey Name:** `10-Q4-STEADY-FLOW`  
**Same structure as above.** Detect 4 consecutive same-amount deposits.

### Quest 5: Triple Treat (3 Consecutive Days)

**Journey Name:** `10-Q5-TRIPLE-TREAT`  
**3 deposits in 3 consecutive calendar days.**

### Quest 6: Cuatro Cycle (Opt-In, Fixed Amount × 4 in 7 Days) 🔴

**Journey Name:** `10-Q6-CUATRO-CYCLE`  
**Opt-in required.** Player selects tier: 1,500 / 3,000 / 5,000 / 10,000 ARS.

| Tier | Completion Reward |
|------|------------------|
| 1,500 × 4 | 50% match on 5th deposit + 20 FS + 200 CC |
| 3,000 × 4 | 75% match + 30 FS + 400 CC |
| 5,000 × 4 | 100% match + 50 FS + 800 CC |
| 10,000 × 4 | 120% match + 75 FS + 1,500 CC + Lucky Wheel entry |

### Quest 7: 4 Days Consecutive (Stricter Cuatro Cycle) 🔴

Same as Quest 6 but requires 4 consecutive calendar days. Add 20% cashback uplift.

### Quest 8: Reach Turnover in 4 Random Slots (Weekly) 🔴

**Journey Name:** `10-Q8-SLOT-CHALLENGE`  
**Auto-assignments:** Each Monday, 4 random slots (2 from top 10 + 2 new/under-played).

| Comm | Campaign ID | Timing | Channel | Content (ES) |
|------|------------|--------|---------|-------------|
| C1 | `10-Q8-C1-EMAIL-BANNER` | Monday AM | Email + In-app | **Subject:** `🎰 Tu desafío semanal de slots empieza hoy` **Preheader:** `4 slots asignados, premios por completar` **Banner Text:** `Desafío Semanal de Slots`. **Banner Desc:** 4 slot game thumbnails in grid, weekly challenge badge, target indicator, exciting vibrant design. **Body Desc:** Weekly challenge intro: 4 assigned slots, wagering target per slot, rewards for completion. |
| C2 | `10-Q8-C2-PUSH` | Wednesday | Push | `Desafío semanal: {X}/4 slots completados. ¡Seguí!` |
| C3 | `10-Q8-C3-SMS` | Friday | SMS | `CuatroBet: Quedan 2 días para tu desafío semanal: {link}` |
| C4 | `10-Q8-C4-PUSH` | Sunday | Push | `¡Hoy es el último día del desafío! {X}/4 slots. Completalo ahora.` |

---

## D. SITUATIONAL BONUSES

### Weekly Bonus (Every Friday)

**Journey Name:** `10-WB-WEEKLY`  
**Segment:** Players with ≥1 deposit in previous 7 days. Tiered reload.

| Comm | Campaign ID | Timing | Channel | Content (ES) |
|------|------------|--------|---------|-------------|
| C1 | `10-WB-C1-EMAIL` | Friday 10 AM | Email | **Subject:** `💰 {tier%} + {FS} giros: tu recarga semanal` **Preheader:** `Válido hasta el domingo, no te lo pierdas` **Banner Text:** `Recarga Semanal: {tier%} + {FS} Giros`. **Banner Desc:** Weekly reload visual — Friday party theme, bonus amount highlight, free spins icons, "válido hasta domingo" ribbon. **Body Desc:** Weekly reload offer details by player tier: match %, FS count, validity (until Sunday). Quick deposit CTA. |
| C2 | `10-WB-C2-PUSH` | Friday PM | Push | `Tu bono semanal está listo. Activalo ahora.` |
| C3 | `10-WB-C3-SMS` | Saturday | SMS | `CuatroBet: Tu recarga semanal + giros gratis. Último día mañana: {link}` |
| C4 | `10-WB-C4-PUSH` | Sunday | Push | `Último día para tu recarga semanal.` |

### Daily Bonus (Login Streak)

**Journey Name:** `10-DB-DAILY`  
**Mechanic:** Consecutive daily logins. No deposit required.

| Comm | Campaign ID | Timing | Channel | Content (ES) |
|------|------------|--------|---------|-------------|
| C1 | `10-DB-C1-PUSH` | Daily AM | Push | `Día {X} de tu racha. Reclamá tu premio diario.` |
| C2 | `10-DB-C2-SMS` | Evening (if unclaimed, 4+ streak) | SMS | `CuatroBet: Racha de {X} días. No pierdas tu premio: {link}` |
| C3 | `10-DB-C3-EMAIL-POPUP` | Day 7 | Email + Popup | **Subject:** `🔥 7 días seguidos — tu premio especial` **Preheader:** `Tu racha de login desbloquea algo grande` **Popup Banner:** 7-day streak badge, confetti, golden milestone icon. **Email Banner Text:** `¡7 Días Seguidos!` **Email Banner Desc:** 7-day streak milestone — calendar with 7 checkmarks, special reward unlocking, gold theme. **Body Desc:** Congratulate 7-day streak. Special reward details. Encourage continuation. |
| C4 | `10-DB-C4-EMAIL` | Day after break | Email | **Subject:** `😔 Tu racha de {X} días se rompió` **Preheader:** `Empezá de nuevo hoy y recuperá tu progreso` **Banner Text:** `Tu Racha Se Rompió`. **Banner Desc:** Broken streak visual — calendar chain broken, motivational "start again" arrow, new streak preview. **Body Desc:** Streak broken at {X} days. Encourage restart with today's login as Day 1. Show next milestone reward preview. |

### Holiday Bonuses (Argentine Calendar)

**Journey Name:** `10-HOL-{HOLIDAY_CODE}`  
**Key dates:** May 25, Jul 9, Oct 12, Dec 25, Carnaval, Easter, etc.

| Comm | Campaign ID | Timing | Channel | Content (ES) |
|------|------------|--------|---------|-------------|
| C1 | `10-HOL-C1-EMAIL` | -7 days | Email | **Subject:** `🎉 {holiday} se acerca con ofertas especiales` **Preheader:** `Mirá lo que te preparamos para este feriado` **Banner Text:** `Se Acerca {holiday}`. **Banner Desc:** Holiday teaser — themed visual for specific holiday (national colors for patriotic, festive for Christmas, etc.), "coming soon" countdown. **Body Desc:** Holiday approaching: preview of special offers, dates, what to expect. Build anticipation. |
| C2 | `10-HOL-C2-PUSH` | -3 days | Push | `En 3 días: ofertas de {holiday}. ¡No te lo pierdas!` |
| C3 | `10-HOL-C3-ALL` | Holiday day | Email + SMS + In-app | **Subject:** `🥳 Feliz {holiday} — tu regalo te espera` **Preheader:** `Abrí tu bono especial de {holiday}` **Email Banner Text:** `¡Feliz {holiday}!` **Email Banner Desc:** Full holiday celebration — themed artwork, festive decorations, offer highlight, national/festive colors. **Popup Banner:** Condensed holiday visual with offer. **Body Desc:** Holiday greeting + bonus details ({offer}). Multi-channel: email has full layout, SMS has link, in-app popup has condensed version. |
| C4 | `10-HOL-C4-EMAIL` | +1 day | Email | **Subject:** `⏰ {holiday} — últimas 24h para tu bono` **Preheader:** `Extendimos la oferta un día más, aprovechá` **Banner Text:** `{holiday} — Últimas 24h`. **Banner Desc:** Extended holiday offer — same holiday theme but with countdown/urgency, "24h more" badge. **Body Desc:** Day-after reminder: holiday offer extended 24h more. Urgency framing. |

---

## TESTING CHECKLIST

- [ ] Loot box tokens earn at correct wagering thresholds (5K slots / 10K live)
- [ ] Loot box reward weights match spec
- [ ] Sticker actions correctly track completion
- [ ] Sticker row completion credits 200 ARS + 10 FS
- [ ] Quest 1 resets after 7 days if incomplete
- [ ] Quest 6 opt-in UI works, tier selection persists
- [ ] Quest 8 random slot assignment varies weekly
- [ ] Weekly bonus targets correct segment (deposited in last 7 days)
- [ ] Daily streak counter increments and resets correctly
- [ ] Holiday campaigns fire on correct dates
- [ ] All CC credits, FS, match bonuses apply correctly
- [ ] Frequency caps: quests/gamification are EXEMPT from standard limits (they're engagement features)
