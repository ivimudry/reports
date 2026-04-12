# 05 — Welcome Bonus Ladder Calibration

**Purpose:** Recalibrate the 10-deposit welcome bonus ladder across 3 verticals (Slots, Live, Sport)  
**Key Problem:** D1→D2 cliff (120% → 20%) kills STD conversion; wagering too high (40×)  
**Solution:** Hold D2 at 75%, lower wagering to 15–18×, introduce CC gifts from D5

---

## Design Principles

1. **D1 = the hook** — strongest headline (120% standard, 150% for deposits >15,000 ARS), 25× wagering
2. **D2 = survival bridge** — hold at 75% (NOT 20%), prevent the cliff that kills STD
3. **D3–D5 = habit phase** — 50–60% match, lower wagering (15–18×) so wagering actually completes
4. **D6–D8 = loyalty phase** — slightly higher matches, richer FS, introduce CC gifts
5. **D9–D10 = Pre-VIP gate** — high match with low wagering, Lucky Wheel entries, D10 auto-enrolls in Pre-VIP if ≥150K ARS

---

## SLOTS LADDER (99% of players)

### Deposit 1 — Welcome Hook
| Field | Value |
|-------|-------|
| **ID** | WBL-SLOTS-D1 |
| **Trigger** | First deposit |
| **Match** | 120% (standard) / 150% (if deposit >15,000 ARS) |
| **Free Spins** | 50 FS on Gates of Olympus (or first-session game) |
| **Wagering** | 25× |
| **Validity** | 7 days |
| **Notes** | Branded to Slots vertical. FS rotated across actual top-played slots, NOT Sweet Bonanza. |

### Deposit 2 — Survival Bridge
| Field | Value |
|-------|-------|
| **ID** | WBL-SLOTS-D2 |
| **Trigger** | Second deposit |
| **Match** | 75% |
| **Free Spins** | 30 FS on Joker's Jewels |
| **Wagering** | 20× |
| **Validity** | 5 days |
| **Notes** | Critical fix: old value was 20% which punished STD intent. 75% prevents the cliff. |

### Deposit 3 — Habit Phase
| Field | Value |
|-------|-------|
| **ID** | WBL-SLOTS-D3 |
| **Trigger** | Third deposit |
| **Match** | 60% |
| **Free Spins** | 25 FS on Jackpot Joker |
| **Wagering** | 18× |
| **Validity** | 5 days |

### Deposit 4 — Habit Phase
| Field | Value |
|-------|-------|
| **ID** | WBL-SLOTS-D4 |
| **Trigger** | Fourth deposit |
| **Match** | 55% |
| **Free Spins** | 20 FS on 4 Supercharged Clovers |
| **Wagering** | 15× |
| **Validity** | 5 days |

### Deposit 5 — Habit Phase + CC Introduction
| Field | Value |
|-------|-------|
| **ID** | WBL-SLOTS-D5 |
| **Trigger** | Fifth deposit |
| **Match** | 50% |
| **Free Spins** | 15 FS on Gold Party |
| **CC Gift** | 200 CC |
| **Wagering** | 15× |
| **Validity** | 5 days |
| **Notes** | First CC gift in the ladder. Introduces players to CC economy. |

### Deposit 6 — Loyalty Phase
| Field | Value |
|-------|-------|
| **ID** | WBL-SLOTS-D6 |
| **Trigger** | Sixth deposit |
| **Match** | 60% |
| **Free Spins** | 30 FS on 3 Coin Volcanoes |
| **CC Gift** | 300 CC |
| **Wagering** | 15× |
| **Validity** | 5 days |

### Deposit 7 — Loyalty Phase
| Field | Value |
|-------|-------|
| **ID** | WBL-SLOTS-D7 |
| **Trigger** | Seventh deposit |
| **Match** | 65% |
| **Free Spins** | 35 FS on Rush for Gold |
| **CC Gift** | 400 CC |
| **Wagering** | 15× |
| **Validity** | 5 days |

### Deposit 8 — Loyalty Phase
| Field | Value |
|-------|-------|
| **ID** | WBL-SLOTS-D8 |
| **Trigger** | Eighth deposit |
| **Match** | 70% |
| **Free Spins** | 40 FS on Gates of Olympus 1000 |
| **CC Gift** | 500 CC |
| **Wagering** | 15× |
| **Validity** | 5 days |

### Deposit 9 — Pre-VIP Gate
| Field | Value |
|-------|-------|
| **ID** | WBL-SLOTS-D9 |
| **Trigger** | Ninth deposit |
| **Match** | 80% |
| **Free Spins** | 50 FS on player's most-played slot |
| **CC Gift** | 600 CC |
| **Extra** | 1 Lucky Wheel entry |
| **Wagering** | 12× |
| **Validity** | 7 days |

### Deposit 10 — Pre-VIP Auto-Enrollment
| Field | Value |
|-------|-------|
| **ID** | WBL-SLOTS-D10 |
| **Trigger** | Tenth deposit |
| **Match** | 100% |
| **Free Spins** | 60 FS on player's most-played slot |
| **CC Gift** | 1,000 CC |
| **Extra** | 2 Lucky Wheel entries |
| **Wagering** | 10× |
| **Validity** | 7 days |
| **Auto-action** | If cumulative deposits ≥ 150,000 ARS → auto-enroll in Pre-VIP Lifecycle |

---

## Slots Safeguards
| Rule | Value |
|------|-------|
| Wagering contribution: Slots | 100% |
| Wagering contribution: Live | 10% |
| Wagering contribution: Table | 5% |
| Max bet during wagering | 1,500 ARS per spin |
| Max bonus balance | 30,000 ARS at any time |
| Claims | One claim per deposit |

---

## LIVE CASINO LADDER (small audience, higher ARPU)

**Note:** Only Turkish Live Roulette appears in the top 10. Live wagering contribution is 10%, so match bonuses combine with Bonus Cash to make wagering realistic.

| Deposit | Match | Bonus Cash | Wagering | Validity | Notes |
|---------|-------|------------|----------|----------|-------|
| D1 | 120% / 150% | — | 25× | 7 days | Live-branded welcome |
| D2 | 75% | 1,000 ARS bonus cash | 20× | 5 days | Bridge (same principle as Slots) |
| D3 | 60% | 800 ARS bonus cash | 18× | 5 days | |
| D4 | 55% | 600 ARS bonus cash | 15× | 5 days | |
| D5 | 50% | 500 ARS bonus cash + 200 CC | 15× | 5 days | |
| D6–D8 | 60–70% | Bonus cash scaling | 15× | 5 days | + CC gifts |
| D9–D10 | 80–100% | Bonus cash + Lucky Wheel | 10–12× | 7 days | + Pre-VIP auto-enrollment |

---

## SPORT LADDER (0.1% of players, deprioritized)

**Note:** 99.9% casino mix. Sport maintained for rare sports-only users but lowest CRM cadence priority. Uses free bets instead of free spins, odds minimum 1.80.

| Deposit | Match | Free Bet | Wagering | Validity | Notes |
|---------|-------|----------|----------|----------|-------|
| D1 | 120% / 150% | 500 ARS free bet | 25× | 7 days | Sport-branded welcome |
| D2 | 75% | 300 ARS free bet | 20× | 5 days | |
| D3–D5 | 50–60% | 200 ARS free bet | 15–18× | 5 days | |
| D6–D10 | Scaling | Scaling free bets + CC | 10–15× | 5–7 days | |

---

## Path to 20% Bonus Cost % GGR

The current 10.5% is a **wagering completion problem**, not an offer size problem. Three mechanisms:

| Mechanism | Impact | Timeline |
|-----------|--------|----------|
| Lower wagering (40× → 15–18×) — more players complete, budget recognized | 10.5% → 14–15% | Weeks 1–4 |
| D2 bridge (75% hold instead of 20% drop) — retains players | +2–3% | By week 6 |
| CC gifts from D5 — direct cost items, no wagering needed | +1–2% | By week 8 |
| **Target** | **20%** | **Week 12** |
