# 15 — Bonus Shop SKU Catalogue Redesign — Implementation Guide

**Chain:** Bonus Shop Overhaul (4-Tier Catalogue + CC Economy Rebalancing)  
**Priority:** Phase 2 (Week 4–5)  
**Type:** Product/catalogue change with CRM comms support

---

## STEP 0: PRE-FLIGHT CHECKLIST

- [ ] Access to GR8 Tech Bonus Shop admin panel
- [ ] CC credit/debit and balance APIs functional
- [ ] Player lifecycle stage and loyalty tier available for shop filtering
- [ ] CC expiry mechanism available (or can be configured)
- [ ] Redemption analytics available (item, player, timestamp)
- [ ] Current SKU list exported for audit

---

## A. CURRENT SKU AUDIT & FIXES (Before Redesign)

### Fix 1: Aviator Duplication

| Problem | Two "5 Free Flights on Aviator" — one at 200 CC, one at 50 CC |
|---------|-----|
| Action | Delete the 50 CC version. Keep 100 CC (re-priced). Add "20 Free Flights" at 200 CC. |
| Result | `5 Free Flights = 100 CC` / `20 Free Flights = 200 CC` — consistent ratio |

### Fix 2: Free Bet Inconsistency

| Problem | 8,000 ARS free bet at 350 CC vs 3,000 ARS at 150 CC |
|---------|-----|
| Solution | Standardize CC:ARS ratio at ~20 ARS per CC |
| New pricing | 3,000 ARS = 150 CC ✓ / 8,000 ARS = 400 CC (was 350) |

### Fix 3: "Popular" Tag Abuse

| Problem | Multiple items tagged "Popular" regardless of actual redemptions |
|---------|-----|
| Action | Remove ALL "Popular" tags |
| New rule | Auto-apply "Popular" to top 3 items by weekly redemption count only |
| Refresh | Weekly on Monday |

### Fix 4: Sweet Bonanza FS

| Problem | FS featured on Sweet Bonanza (not in top 10 played) |
|---------|-----|
| Action | Replace with Jackpot Joker or Gates of Olympus FS |
| Rule | FS items must use top 10 played slots, rotated weekly |

---

## B. NEW 4-TIER CATALOGUE

### Tier 1: Entry (10–40 CC) — Habit Builders

**Accessible to:** All players (including pre-FTD with earned CC)

| # | Item | Price | Details | Wagering |
|---|------|-------|---------|----------|
| 1 | Small CC Gift | 10 CC | 25 CC back (net +15) | None |
| 2 | 5 FS on Weekly Top Slot | 20 CC | Rotates every Monday | 25× |
| 3 | 200 ARS Bonus Cash | 30 CC | Instant credit | None |
| 4 | Game Recommendation Unlock | 40 CC | AI-picked personalized slot | None |

**Purpose:** Build daily shop-visit habit. Low barrier, immediate gratification.

---

### Tier 2: Standard (50–150 CC) — Main Storefront

**Accessible to:** After FTD (lifecycle ≥ "FTD")

| # | Item | Price | Details | Wagering |
|---|------|-------|---------|----------|
| 5 | 10 FS on Jackpot Joker | 50 CC | — | 25× |
| 6 | 15 FS on Gates of Olympus | 75 CC | — | 20× |
| 7 | 1,000 ARS Match 50% | 100 CC | On next deposit | 15× |
| 8 | 5 Free Flights on Aviator | 100 CC | — | 20× |
| 9 | 3,000 ARS Free Bet | 150 CC | Odds min 1.80 | 12× |

---

### Tier 3: Premium (200–400 CC) — Loyalty Locked

**Accessible to:** Premium loyalty tier or above

| # | Item | Price | Details | Wagering |
|---|------|-------|---------|----------|
| 10 | 20 Free Flights on Aviator | 200 CC | — | 15× |
| 11 | 30 FS on Premium Title | 250 CC | New release rotation (monthly) | 15× |
| 12 | 5,000 ARS Match 75% | 300 CC | On next deposit | 12× |
| 13 | Silver Spin Entry | 350 CC | Lucky Wheel Silver tier | — |
| 14 | 8,000 ARS Free Bet | 400 CC | Odds min 1.80 | 10× |

---

### Tier 4: VIP (500–2,000 CC) — Pre-VIP/VIP Only

**Accessible to:** Pre-VIP and VIP tiers

| # | Item | Price | Details | Wagering |
|---|------|-------|---------|----------|
| 15 | 100 FS Premium Package | 500 CC | Player's top 3 slots, 33 FS each + 1 bonus | 12× |
| 16 | Gold Spin Entry | 750 CC | Lucky Wheel Gold tier | — |
| 17 | 15,000 ARS Match 100% | 1,000 CC | On next deposit | 10× |
| 18 | Platinum Spin Entry | 1,500 CC | Lucky Wheel Platinum tier | — |
| 19 | VIP Experience Package | 2,000 CC | Personal manager session + exclusive offer + surprise | — |

---

## C. SHOP UI CHANGES

### Tier Visibility Rules

| Lifecycle Stage | Visible Tiers | Locked Preview |
|-----------------|---------------|----------------|
| Pre-FTD | Entry only | Standard/Premium/VIP shown as locked silhouettes |
| Post-FTD (Regular) | Entry + Standard | Premium shown locked with "Unlock at Premium tier" |
| Premium loyalty | Entry + Standard + Premium | VIP shown locked with "Unlock at Pre-VIP" |
| Pre-VIP / VIP | All tiers | — |

**Locked Item Display:**
```
Card: Greyed out with lock icon overlay
Text: "Desbloqueá este artículo al alcanzar {tier_name}"
Effect: Creates aspiration, drives loyalty progression
```

### Tags

| Tag | Rule | Display |
|-----|------|---------|
| Popular | Top 3 by weekly redemption | 🔥 badge |
| New | Item added < 14 days ago | ✨ badge |
| Limited | Rotating items with countdown | ⏰ badge + timer |
| Recommended | AI-picked based on player history | ⭐ badge |

### Item Card Layout
```
Image: Game or reward icon (64×64)
Title: Item name (14px bold)
Price: CC amount with coin icon
Tag: Badge (if applicable)
CTA: "Canjear" button (primary if affordable, grey if insufficient CC)
Insufficient: "Te faltan {X} CC" text below button
```

---

## D. CC ECONOMY REBALANCING

### Current State Problems

| Problem | Detail |
|---------|--------|
| Earning is healthy | 6/8/12/18 CC per tier per mission |
| Burn is broken | Limited items, no cheap entry, hoarding |
| No expiry | Players accumulate indefinitely with no urgency |
| Earn-to-burn ratio | < 0.3 (most CC never spent) |

### Changes

| Parameter | Before | After |
|-----------|--------|-------|
| CC expiry | None | **90-day rolling inactivity expiry** |
| Entry items | None under 50 CC | 4 items at 10–40 CC |
| Burn frequency | Monthly (at best) | Daily (habit items) |
| Target earn-to-burn | <0.3 | 1.0–1.2 |

### CC Expiry Rules

| Rule | Detail |
|------|--------|
| Trigger | 90 consecutive days with zero CC earned AND zero CC spent |
| Warning 1 | Day 60: Email + Push — `Tus {balance} CC vencen en 30 días.` |
| Warning 2 | Day 83: SMS — `CuatroBet: Tus CC vencen en 7 días. Canjalos: {link}` |
| Expiry | Day 90: CC balance set to zero |
| Partial reset | Any earn or spend resets the 90-day clock |

**Warning Comms (link to Chain 11 PL-C3/C4 for loyalty passive members):**

| Comm | Campaign ID | Channel | Content (ES) |
|------|------------|---------|-------------|
| W1 | `15-CC-EXPIRY-W1` | Email + Push | **Subject:** `⚠️ Tus {balance} CC vencen en 30 días` **Preheader:** `Canjealos antes de que desaparezcan` **Email Banner Text:** `Tus CC Vencen en 30 Días` **Email Banner Desc:** Expiry warning — CC coins fading/dissolving, 30-day countdown timer, redemption options preview, amber urgency tones. **Body Desc:** CC balance + expiry date. Redemption options (FS, cash, Lucky Wheel). Urgency framing. **Push:** `Tus {balance} Cuatro Coins vencen en 30 días si no los usás. ¡Canjalos ahora!` |
| W2 | `15-CC-EXPIRY-W2` | SMS | `CuatroBet: Tus {balance} CC vencen en 7 días. Última oportunidad: {link}` |

---

## E. PROMOTIONAL ROTATION

### Weekly Featured Items

| Day | Action |
|-----|--------|
| Monday | Rotate "5 FS on Weekly Top Slot" to new slot |
| Monday | Recalculate "Popular" tags based on last week's redemptions |
| Monthly | Rotate "30 FS on Premium Title" to current month's new release |

### Limited-Time Items (Optional — Phase 2)

Add 1 limited-time item per week:
- 48-hour availability
- Countdown timer on card
- Slightly better value than permanent items (incentivize urgency)
- Example: `25 FS on {new_game} — 60 CC — Ends in 47h` (vs normal 75 CC for 15 FS)

---

## TESTING CHECKLIST

- [ ] Entry tier visible to all players (including pre-FTD)
- [ ] Standard tier locked for pre-FTD, visible after FTD
- [ ] Premium tier locked for non-Premium loyalty
- [ ] VIP tier locked for non-VIP players
- [ ] Locked items show as greyed silhouettes with unlock message
- [ ] "Canjear" button disabled when insufficient CC (shows deficit)
- [ ] Redemption correctly debits CC balance
- [ ] Wagering requirements applied on redemption
- [ ] "Popular" tag auto-updates weekly (top 3 only)
- [ ] "New" tag auto-removes after 14 days
- [ ] CC expiry warning fires at day 60 and day 83
- [ ] CC balance expires at day 90 of inactivity
- [ ] Any earn/spend resets the 90-day clock
- [ ] Weekly slot rotation updates Monday
- [ ] Aviator items correctly labeled (5 flights / 20 flights)
- [ ] Free bet pricing consistent (20 ARS per CC ratio)

---

## KPI TARGETS

| Metric | Current | Target (6 weeks) |
|--------|---------|-------------------|
| Shop redemption rate | Low | 2–3× increase |
| CC burn rate | <30% | >80% |
| Weekly shop visitors | Low | 3× increase |
| Entry tier daily redemptions | 0 (didn't exist) | Baseline + growth |
| CC hoarding (balance >1,000 CC) | High % | <20% of active players |
| Earn-to-burn ratio | <0.3 | 1.0–1.2 |
