# 15 — Bonus Shop SKU Catalogue Redesign

**Purpose:** Fix pricing inconsistencies, add tiers, personalize by lifecycle

---

## Current Issues

| Problem | Detail |
|---------|--------|
| Flat pricing | Every deposit match = 300 CC regardless of vertical |
| Inconsistent Free Bet pricing | 8,000 ARS at 350 CC vs 3,000 ARS at 150 CC — different CC:ARS ratios |
| Aviator duplication | Two "5 Free Flights on Aviator" at 200 CC and 50 CC. Breaks trust. |
| No entry-level item (<50 CC) | No habit-building cheap items |
| No aspirational item (>350 CC) | Nothing to save for |
| FS misaligned | Featured on Sweet Bonanza (not in top 10) |
| No personalization | Same catalogue for all players |
| No tier locks | All items visible to all players |

---

## Redesigned Catalogue: 4 Tiers

### Entry Tier (10–40 CC) — Habit Builders
**Available to:** All players

| Item | Price | Details |
|------|-------|---------|
| Small CC gift | 10 CC | 25 CC back (net +15, builds habit) |
| 5 FS on random top-10 slot | 20 CC | Rotates weekly |
| 200 ARS bonus cash | 30 CC | No wagering |
| Game recommendation unlock | 40 CC | Personalized AI pick |

### Standard Tier (50–150 CC) — Main Storefront
**Available to:** After FTD

| Item | Price | Details |
|------|-------|---------|
| 10 FS on Jackpot Joker | 50 CC | |
| 15 FS on Gates of Olympus | 75 CC | |
| 1,000 ARS deposit match 50% | 100 CC | 15× wagering |
| 5 Free Flights on Aviator | 100 CC | (corrected from duplication) |
| 3,000 ARS free bet | 150 CC | Odds min 1.80 |

### Premium Tier (200–400 CC) — Loyalty Locked
**Available to:** Premium loyalty tier or above

| Item | Price | Details |
|------|-------|---------|
| 20 Free Flights on Aviator | 200 CC | (corrected label) |
| 30 FS on premium PP title | 250 CC | New release rotation |
| 5,000 ARS deposit match 75% | 300 CC | 12× wagering |
| Silver Spin entry | 350 CC | |
| 8,000 ARS free bet | 400 CC | Odds min 1.80 |

### VIP Tier (500–2,000 CC) — Pre-VIP / VIP Only
**Available to:** Pre-VIP and above

| Item | Price | Details |
|------|-------|---------|
| 100 FS premium package | 500 CC | Player's top 3 slots |
| Gold Spin entry | 750 CC | |
| 15,000 ARS match 100% | 1,000 CC | 10× wagering |
| Platinum Spin entry | 1,500 CC | |
| VIP experience package | 2,000 CC | Personal manager session + exclusive offer |

---

## Lifecycle Personalization

| Lifecycle Stage | Catalogue View |
|-----------------|----------------|
| Pre-FTD | Entry tier only, others teased as locked |
| Post-FTD | Entry + Standard |
| Regular | Entry + Standard + Premium locked preview |
| Pre-VIP+ | All tiers |

## Fixes Before Launch
- [ ] Correct Aviator labeling: "5 Free Flights" (100 CC) and "20 Free Flights" (200 CC)
- [ ] Harmonize free bet CC pricing: consistent ARS-per-CC ratio
- [ ] Remove "Popular" tag from all. Re-apply to top 3 by weekly redemption only
- [ ] Add "New" tag to items <14 days old
- [ ] Add real countdown to rotating FS offers (7-day rotations)

## CC Economy Rebalancing

| Parameter | Current | Target |
|-----------|---------|--------|
| Earning rates | Premium 6 CC, Prestige 8, Maestro 12, Legend 18 per mission | Keep |
| Burn opportunities | Limited | Entry tier at every visit |
| Expiry | None | 90-day inactivity soft expiry |
| Earn-to-burn ratio | <0.3 (hoarding) | 1.0–1.2 |

**Expected Impact:**
- Bonus Shop redemption rate: 2–3× within 6 weeks
- CC burn rate: <30% → >80%
- Weekly shop visit: new habit loop
