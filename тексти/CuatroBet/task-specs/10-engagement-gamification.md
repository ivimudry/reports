# 10 — Engagement & Gamification

**Purpose:** Drive repeat deposits, wagering, and daily engagement through game mechanics  
**Components:** Loot Boxes, Stickers, 8 Quests, Weekly/Daily/Holiday Bonuses

---

## A. Loot Boxes

**Mechanic:** Players earn loot box tokens through gameplay.
- 1 token per 5,000 ARS wagered on slots
- 1 token per 10,000 ARS wagered on live
- Opened manually from dashboard

### Reward Table (weighted)
| Reward | Weight | Value |
|--------|--------|-------|
| Small CC gift | High | 25–50 CC |
| Free Spins (5–10) | Medium | On top-played slot |
| Bonus Cash | Low | 500–1,000 ARS |
| Lucky Wheel Entry | Low | 1 entry |
| Premium FS (25+) | Very low | On premium titles |

### Comms (4 touches)
| Comm | ID | Timing | Channel | Copy (ES) |
|------|----|--------|---------|-----------|
| Token earned | LB-C1 | On earn | App Push | "¡Ganaste un loot box! Abrilo desde tu panel." |
| Box opening celebration | LB-C2 | On open | In-app popup | "[Reward] desbloqueado. ¡Seguí jugando para más!" |
| Weekly unclaimed reminder | LB-C3 | Weekly (Monday) | Email | "Tenés [X] loot boxes sin abrir. ¿Qué hay adentro?" |
| Monthly summary | LB-C4 | Monthly | Email | "Este mes abriste [X] loot boxes y ganaste [total]." |

---

## B. Stickers

**Mechanic:** 30-slot sticker book. Collect via specific actions.
- Examples: play Jackpot Joker 10 times, deposit 3 days in a row, try a new provider
- Row of 5 complete = reward
- All 30 = grand prize

### Rewards
| Milestone | Reward |
|-----------|--------|
| Single sticker | 25 CC |
| Row of 5 | 200 ARS + 10 FS |
| All 30 | 10,000 ARS + premium Lucky Wheel + VIP I preview |

### Comms (4 touches)
| Comm | ID | Timing | Channel | Copy (ES) |
|------|----|--------|---------|-----------|
| New sticker available | STK-C1 | On sticker unlock | App Push | "Nueva figurita desbloqueada: [sticker name]. ¡Seguí coleccionando!" |
| 1 sticker away | STK-C2 | When 4 of 5 in a row | Email | "¡Te falta 1 figurita para completar la fila y ganar 200 ARS + 10 giros!" |
| Row complete | STK-C3 | On row completion | App Push + In-app popup | "¡Fila completa! Ganaste 200 ARS + 10 giros gratis." |
| Monthly summary | STK-C4 | Monthly | Email | "Este mes coleccionaste [X] figuritas. Te faltan [Y] para el gran premio." |

---

## C. Quests

### Quest 1: 4 Deposit Quest (Cuatro core mechanic)

**Mechanic:** 4 deposits in any rolling 7-day window. Core brand mechanic, directly addresses STD.  
**Auto-enrollment:** On first deposit. Wagering 20× on FS winnings.  
**Target:** STD +30–50% relative.

| Deposit | FS Reward | CC | Extra |
|---------|-----------|-----|-------|
| 1st | 10 FS on top slot | 50 CC | — |
| 2nd | 15 FS | 75 CC | — |
| 3rd | 20 FS | 100 CC | — |
| 4th (complete) | 30 FS | 200 CC | 50% match up to 3,000 ARS |

**Comms:**
| Comm | ID | Timing | Channel | Copy (ES) |
|------|----|--------|---------|-----------|
| Welcome to quest | Q1-C1 | On enrollment (FTD) | In-app popup + Email | "¡Misión Cuatro activada! 4 depósitos en 7 días = premios increíbles." |
| Halfway (2/4) | Q1-C2 | After 2nd deposit | App Push | "¡Vas por la mitad! 2 depósitos más para completar la Misión Cuatro." |
| 1 more to go (3/4) | Q1-C3 | After 3rd deposit | SMS | "CuatroBet: ¡Falta 1 depósito para ganar 30 giros + 200 CC + bono 50%! [link]" |
| Completion | Q1-C4 | After 4th deposit | In-app popup + Email | "¡Misión Cuatro completa! Tus premios están acreditados." |

---

### Quest 2: Double Chance

**Mechanic:** 1 deposit = 2 Lucky Wheel spins during limited window (1 weekend/month).

**Comms:**
| Comm | ID | Timing | Channel | Copy (ES) |
|------|----|--------|---------|-----------|
| Friday announcement | Q2-C1 | Friday morning | Email | "Este fin de semana: cada depósito = 2 giros de la Rueda de la Suerte." |
| Saturday live | Q2-C2 | Saturday | App Push | "Doble Chance está activo. Depositá y girá 2 veces: [link]" |
| Sunday last day | Q2-C3 | Sunday | SMS | "CuatroBet: Último día de Doble Chance. Depositá y girá 2 veces: [link]" |
| Monday thank you | Q2-C4 | Monday | Email | "Doble Chance terminó. Giraste [X] veces. ¡Próximo fin de semana hay más!" |

---

### Quest 3: Silver Spin

**Mechanic:** Tiered wheel spins earned by wagering.
- Silver: 1 per 2,000 ARS wagered
- Gold: 1 per 10,000 ARS wagered
- Platinum: 1 per 50,000 ARS wagered

**Comms:**
| Comm | ID | Timing | Channel | Copy (ES) |
|------|----|--------|---------|-----------|
| Spin earned | Q3-C1 | On earn | App Push | "¡Ganaste un giro [Silver/Gold/Platinum]! Usalo ahora." |
| 48h unused | Q3-C2 | 48h after earn | SMS | "CuatroBet: Tu giro [tier] está sin usar. No lo pierdas: [link]" |
| 24h expiry warning | Q3-C3 | 24h before expiry | App Push | "Tu giro [tier] vence mañana. Usalo: [link]" |
| Post-spin celebration | Q3-C4 | After spin | In-app popup | "¡Giraste y ganaste [reward]!" |

---

### Quest 4: Steady Flow

**Mechanic:** 4 deposits of the same amount in a row (no time limit). Reward scales with deposit size.

**Comms:**
| Comm | ID | Timing | Channel | Copy (ES) |
|------|----|--------|---------|-----------|
| Started (after 1st) | Q4-C1 | After 1st matching deposit | In-app popup | "Flujo Constante activado. 3 depósitos más de [amount] ARS para el premio." |
| 2 more to go | Q4-C2 | After 2nd matching deposit | App Push | "¡Bien! 2 depósitos más de [amount] ARS." |
| 1 more to go | Q4-C3 | After 3rd matching deposit | SMS | "CuatroBet: ¡Último depósito de [amount] ARS para completar Flujo Constante! [link]" |
| Completion | Q4-C4 | After 4th matching deposit | In-app popup + Email | "¡Flujo Constante completo! Ganaste [reward]." |

---

### Quest 5: Triple Treat

**Mechanic:** 3 deposits in 3 consecutive calendar days.

**Comms:**
| Comm | ID | Timing | Channel | Copy (ES) |
|------|----|--------|---------|-----------|
| Day 1 start | Q5-C1 | After 1st deposit | In-app popup | "Triple Treat empieza hoy. Depositá mañana y pasado mañana para ganar." |
| Day 2 streak | Q5-C2 | Day 2 morning | App Push + SMS | "¡No rompas la racha! Depositá hoy para Triple Treat: [link]" |
| Day 3 final | Q5-C3 | Day 3 morning | SMS | "CuatroBet: ¡Último día para Triple Treat! Depositá y ganá: [link]" |
| Completion | Q5-C4 | After 3rd deposit | In-app popup | "¡Triple Treat completo! Tus premios están listos." |

---

### Quest 6: Cuatro Cycle (4 deposits, fixed amount) 🔴 HIGH PRIORITY

**Mechanic:** Player opts in and commits to a fixed amount (1,500 / 3,000 / 5,000 / 10,000 ARS), deposits that exact amount 4 times in 7 days. Resets if a deposit doesn't match.

**Reward Tiers:**
| Amount | Completion Reward |
|--------|-------------------|
| 1,500 ARS × 4 | 50% match on 5th deposit + 20 FS + 200 CC |
| 3,000 ARS × 4 | 75% match + 30 FS + 400 CC |
| 5,000 ARS × 4 | 100% match + 50 FS + 800 CC |
| 10,000 ARS × 4 | 120% match + 75 FS + 1,500 CC + Lucky Wheel entry |

**Comms:**
| Comm | ID | Timing | Channel | Copy (ES) |
|------|----|--------|---------|-----------|
| Opt-in confirmation | Q6-C1 | On opt-in | Email + In-app | "Te inscribiste en Ciclo Cuatro ([amount] ARS × 4). ¡Empecemos!" |
| Progress after each | Q6-C2 | After each deposit | App Push | "Ciclo Cuatro: [X]/4 completos. Seguí así!" |
| Day 5 warning | Q6-C3 | Day 5 of 7 | SMS | "CuatroBet: Te quedan 2 días para completar Ciclo Cuatro. [X]/4 hechos: [link]" |
| Completion | Q6-C4 | After 4th deposit | In-app popup + Email | "¡Ciclo Cuatro completo! [Rewards] acreditados." |

---

### Quest 7: 4 Days Deposit Fixed Amount 🔴 HIGH PRIORITY

**Mechanic:** Identical to Cuatro Cycle but 4 consecutive calendar days (stricter).  
**Recommendation:** Consolidate with Quest 6 as two variants: "7-day flexible Cuatro Cycle" and "4-day consecutive Cuatro Cycle".  
**Rewards:** Same tiers as Quest 6 with 20% cashback uplift for the tighter variant.

**Comms:** Same structure as Quest 6 (Q7-C1 through Q7-C4).

---

### Quest 8: Reach Turnover in 4 Random Slots 🔴 HIGH PRIORITY

**Mechanic:** Player must reach wagering turnover target across 4 randomly assigned slots within a week.
- Random assignment each Monday
- 2 slots from top 10 most played
- 2 slots from new releases or under-played titles (cross-promotion)

**Comms:**
| Comm | ID | Timing | Channel | Copy (ES) |
|------|----|--------|---------|-----------|
| Monday launch | Q8-C1 | Monday AM | Email + In-app | "Tu desafío semanal: jugá [4 slots] y alcanzá [target]. Premios esperan." |
| Wednesday progress | Q8-C2 | Wednesday | App Push | "Desafío semanal: [X]/4 slots completados. ¡Seguí!" |
| Friday push | Q8-C3 | Friday | SMS | "CuatroBet: Quedan 2 días para tu desafío semanal: [link]" |
| Sunday last day | Q8-C4 | Sunday | App Push | "¡Hoy es el último día del desafío! [X]/4 slots. Completalo ahora." |

---

## D. Situational Bonuses

### Weekly Bonuses (every Friday)

**Segment:** All players with ≥1 deposit in previous 7 days. Tiered reload.

| Comm | ID | Timing | Channel | Copy (ES) |
|------|----|--------|---------|-----------|
| Friday offer | WB-C1 | Friday 10 AM | Email | "Tu recarga semanal: [tier%] + [FS] giros. Válido hasta domingo." |
| Friday evening | WB-C2 | Friday PM | App Push | "Tu bono semanal está listo. Activalo ahora." |
| Saturday | WB-C3 | Saturday | SMS | "CuatroBet: Tu recarga semanal + giros gratis. Último día mañana: [link]" |
| Sunday last day | WB-C4 | Sunday | App Push | "Último día para tu recarga semanal: [link]" |

### Daily Bonuses (login streak)

**Mechanic:** Daily login streak, no deposit required. Reward scales with consecutive days.

| Comm | ID | Timing | Channel | Copy (ES) |
|------|----|--------|---------|-----------|
| Daily morning | DB-C1 | Daily AM | App Push | "Día [X] de tu racha. Reclamá tu premio diario." |
| 4+ streak (unclaimed) | DB-C2 | Evening | SMS | "CuatroBet: Racha de [X] días. No pierdas tu premio: [link]" |
| Day 7 celebration | DB-C3 | Day 7 | Email + In-app popup | "¡7 días seguidos! Premio especial desbloqueado." |
| Streak broken | DB-C4 | Day after break | Email | "Tu racha se rompió en [X] días. Empezá de nuevo hoy: [link]" |

### Holiday Bonuses (Argentina calendar)

| Comm | ID | Timing | Channel | Copy (ES) |
|------|----|--------|---------|-----------|
| 1 week before | HOL-C1 | -7 days | Email | "Se acerca [holiday]. Preparate para ofertas especiales." |
| 3 days before | HOL-C2 | -3 days | App Push | "En 3 días: ofertas de [holiday]. ¡No te lo pierdas!" |
| Day of | HOL-C3 | Holiday | Email + SMS + In-app | "¡Feliz [holiday]! Tu bono festivo: [offer]." |
| Day after | HOL-C4 | +1 day | Email | "Todavía podés aprovechar la oferta de [holiday]. Válida 24h más." |
