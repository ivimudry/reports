# 05 — Welcome Bonus Ladder Calibration — Implementation Guide

**Chain:** Welcome Bonus Ladder (10 deposits × 3 verticals)  
**Priority:** High (fixes D1→D2 cliff that kills STD conversion)  
**Estimated Configurations:** 30 bonus templates (10 per vertical) + ladder trigger logic  
**Prerequisites from Master Doc:** Events `deposit_success` with `deposit_number`; Attributes `deposit_count`, `game_preference`, `cumulative_deposits_ars`, `most_played_game_name`; Bonus management API

---

## STEP 0: PRE-FLIGHT CHECKLIST

- [ ] Event `deposit_success` carries `deposit_number` (1 through 10+)
- [ ] Attribute `game_preference` correctly set: `slots` / `live` / `sport` / `mixed`
- [ ] Bonus management API can create deposit-match bonuses with FS/bonus cash/free bets
- [ ] Wagering contribution rules configured: Slots 100%, Live 10%, Table 5%, Sport 100%
- [ ] Max bet during wagering: 1,500 ARS per spin
- [ ] Max bonus balance: 30,000 ARS at any time
- [ ] Game IDs confirmed for all FS target games (see list below)
- [ ] Player's `most_played_game_name` available for D9 and D10 personalization
- [ ] Lucky Wheel system ready (for D9 and D10)
- [ ] CC (Cuatro Coins) credit API available
- [ ] Pre-VIP auto-enrollment trigger at D10 + cumulative ≥150K ARS

---

## STEP 1: CREATE BONUS TEMPLATES

### 1.1 Slots Ladder — 10 Templates

Create each bonus template in GR8 Tech's bonus management system:

| Template ID | Deposit # | Match % | Threshold Match* | FS Count | FS Game | CC | Wagering | Validity | Extra |
|------------|-----------|---------|-------------------|----------|---------|-----|----------|----------|-------|
| `WBL-S-D1` | 1st | 120% | 150% (>15K ARS) | 50 | Gates of Olympus** | — | 25× | 7 days | — |
| `WBL-S-D2` | 2nd | 75% | — | 30 | Joker's Jewels | — | 20× | 5 days | — |
| `WBL-S-D3` | 3rd | 60% | — | 25 | Jackpot Joker | — | 18× | 5 days | — |
| `WBL-S-D4` | 4th | 55% | — | 20 | 4 Supercharged Clovers | — | 15× | 5 days | — |
| `WBL-S-D5` | 5th | 50% | — | 15 | Gold Party | 200 | 15× | 5 days | CC intro |
| `WBL-S-D6` | 6th | 60% | — | 30 | 3 Coin Volcanoes | 300 | 15× | 5 days | — |
| `WBL-S-D7` | 7th | 65% | — | 35 | Rush for Gold | 400 | 15× | 5 days | — |
| `WBL-S-D8` | 8th | 70% | — | 40 | Gates of Olympus 1000 | 500 | 15× | 5 days | — |
| `WBL-S-D9` | 9th | 80% | — | 50 | Player's top slot | 600 | 12× | 7 days | +1 Lucky Wheel |
| `WBL-S-D10` | 10th | 100% | — | 60 | Player's top slot | 1000 | 10× | 7 days | +2 Lucky Wheel |

*Threshold Match: D1 gives 150% instead of 120% if deposit exceeds 15,000 ARS.  
**FS game defaults to Gates of Olympus but should use player's first-session game if different.

**For each template, configure in GR8 Tech:**
1. Navigate to Bonus Management → Create New Template
2. Set template name: `WBL-S-D{n}` (e.g., `WBL-S-D1`)
3. Type: Deposit Match
4. Match percentage: as per table
5. Add Free Spins component: count + target game ID
6. Add CC component (D5–D10): amount
7. Wagering requirement: as per table
8. Wagering contribution: Slots 100%, Live 10%, Table 5%
9. Max bet during wagering: 1,500 ARS/spin
10. Max bonus balance: 30,000 ARS
11. Validity period: as per table
12. Claims: One per deposit
13. For D1: Add conditional rule — if deposit amount > 15,000 ARS → match = 150%
14. For D9–D10: Add Lucky Wheel entry grant (1 or 2 entries)
15. For D10: Add flag — if `cumulative_deposits_ars >= 150000` → trigger Pre-VIP enrollment

---

### 1.2 Live Casino Ladder — 10 Templates

| Template ID | Deposit # | Match % | Bonus Cash | CC | Wagering | Validity |
|------------|-----------|---------|------------|-----|----------|----------|
| `WBL-L-D1` | 1st | 120%/150% | — | — | 25× | 7 days |
| `WBL-L-D2` | 2nd | 75% | 1,000 ARS | — | 20× | 5 days |
| `WBL-L-D3` | 3rd | 60% | 800 ARS | — | 18× | 5 days |
| `WBL-L-D4` | 4th | 55% | 600 ARS | — | 15× | 5 days |
| `WBL-L-D5` | 5th | 50% | 500 ARS | 200 | 15× | 5 days |
| `WBL-L-D6` | 6th | 60% | 700 ARS | 300 | 15× | 5 days |
| `WBL-L-D7` | 7th | 65% | 900 ARS | 400 | 15× | 5 days |
| `WBL-L-D8` | 8th | 70% | 1,100 ARS | 500 | 15× | 5 days |
| `WBL-L-D9` | 9th | 80% | 1,500 ARS | 600 | 12× | 7 days |
| `WBL-L-D10` | 10th | 100% | 2,000 ARS | 1000 | 10× | 7 days |

**Key difference from Slots:** Uses Bonus Cash instead of Free Spins because Live wagering contribution is only 10%.

---

### 1.3 Sport Ladder — 10 Templates

| Template ID | Deposit # | Match % | Free Bet | CC | Wagering | Validity | Min Odds |
|------------|-----------|---------|----------|-----|----------|----------|----------|
| `WBL-SP-D1` | 1st | 120%/150% | 500 ARS | — | 25× | 7 days | 1.80 |
| `WBL-SP-D2` | 2nd | 75% | 300 ARS | — | 20× | 5 days | 1.80 |
| `WBL-SP-D3` | 3rd | 60% | 200 ARS | — | 18× | 5 days | 1.80 |
| `WBL-SP-D4` | 4th | 55% | 200 ARS | — | 15× | 5 days | 1.80 |
| `WBL-SP-D5` | 5th | 50% | 200 ARS | 200 | 15× | 5 days | 1.80 |
| `WBL-SP-D6–D8` | 6–8th | 60–70% | Scaling | 300–500 | 15× | 5 days | 1.80 |
| `WBL-SP-D9` | 9th | 80% | 500 ARS | 600 | 12× | 7 days | 1.80 |
| `WBL-SP-D10` | 10th | 100% | 700 ARS | 1000 | 10× | 7 days | 1.80 |

**Key difference:** Uses Free Bets instead of FS/Bonus Cash. All bets must meet minimum odds of 1.80.

---

## STEP 2: CREATE THE AUTOMATED LADDER JOURNEY

**Campaign Name:** `05-WBL-JOURNEY`  
**Type:** Triggered journey (event-based)  
**Entry Trigger:** Event = `deposit_success` WHERE `deposit_number <= 10`  
**Re-entry:** Yes (fires on each of the first 10 deposits)

### Journey Logic (Pseudocode):

```
ON deposit_success WHERE deposit_number <= 10:
  
  1. DETERMINE VERTICAL:
     IF game_preference = "live"  → use WBL-L-D{deposit_number}
     IF game_preference = "sport" → use WBL-SP-D{deposit_number}
     ELSE                         → use WBL-S-D{deposit_number}  (default)
  
  2. APPLY BONUS:
     Call Bonus API → grant template for this deposit number
     
  3. IF deposit_number = 1 AND amount > 15000:
     Override match to 150%
  
  4. IF deposit_number >= 5:
     Credit CC (amount per template)
  
  5. IF deposit_number >= 9:
     Grant Lucky Wheel entries
  
  6. IF deposit_number = 10 AND cumulative_deposits >= 150000:
     Trigger Pre-VIP enrollment (chain 02)
  
  7. SEND NOTIFICATION:
     Show in-app popup confirming bonus grant
     Copy: "¡Bono de depósito #{deposit_number} activado! {match}% + {fs/cash/bet} + {cc} CC"
```

**Configuration steps:**
1. Create triggered campaign on `deposit_success` event
2. Add conditional branch on `game_preference` for vertical selection
3. Within each vertical branch, add conditional branch on `deposit_number` (1–10)
4. For each deposit number, assign the correct bonus template
5. Add D1 override condition for >15K ARS deposits
6. Add CC credit actions for D5–D10
7. Add Lucky Wheel grant for D9–D10
8. Add Pre-VIP enrollment trigger for D10 + cumulative ≥150K
9. Add confirmation popup after each bonus grant

---

## STEP 3: COMMUNICATION TEMPLATES

For each deposit in the ladder, send a notification confirming the bonus:

### Deposit Confirmation Popup (all deposits)

**Channel:** In-app popup (immediate on deposit)

**Banner Text (ES):** `¡Depósito #{deposit_number} Completado!`  
**Banner Description:** Celebration popup — deposit number displayed large in gold circle, bonus icon stack (FS/cash/CC coins based on vertical), confetti burst, progress bar showing position in 10-step ladder

**Body (ES):**
```
Tu bono está activo:
• {match}% match aplicado
• {fs_count} giros gratis en {game_name} [Slots]
• {bonus_cash} ARS bonus cash [Live]
• {free_bet} ARS free bet [Sport]
• {cc} CC acreditados [D5+]
Wagering: {wagering}× | Válido: {validity} días
```
**CTA (ES):** `Jugar ahora` → game link

### Email Summary (sent after D3, D5, D7, D10 — milestone deposits)

| Deposit | Subject (ES) | Banner Text (ES) | Banner Description | Body Description |
|---------|-------------|-------------------|--------------------|-----------------|
| D3 | `📈 3 depósitos - tu progreso en CuatroBet` | `3/10 Depósitos` | Progress achievement — progress bar at 30%, three golden checkmarks, ladder visualization, next rewards preview | Summary of bonuses claimed so far, games played, progress bar showing 3/10 toward full ladder completion |
| D5 | `⭐ Mitad del camino + tus primeros CC` | `Mitad del Camino` | Halfway celebration — progress bar at 50%, Cuatro Coins icon stack (first CC introduction), golden star badge for milestone | Introduce CC economy for the first time, show CC balance earned, explain what CC can buy in Bonus Shop, preview D6-D10 rewards |
| D7 | `🔥 7 depósitos - los mejores bonos vienen ahora` | `7/10 - Casi al Final` | Almost-there visual — progress bar at 70%, preview of D8-D10 premium rewards as locked/glowing icons, anticipation design | Preview D8-D10 reward escalation (higher match %, more FS/cash, Lucky Wheel), build anticipation for final three deposits |
| D10 | `🏆 Welcome Ladder completo` | `Ladder Completo` | Grand celebration — full progress bar at 100%, trophy/crown icon, confetti explosion, transition teaser to loyalty program | Celebration of full ladder completion, summary of ALL 10 bonuses claimed, total value received, transition message to loyalty program and ongoing benefits |

---

## STEP 4: SAFEGUARDS CONFIGURATION

Set these rules globally in GR8 Tech:

| Rule | Configuration |
|------|--------------|
| Wagering contribution: Slots | 100% |
| Wagering contribution: Live | 10% |
| Wagering contribution: Table | 5% |
| Wagering contribution: Sport | 100% |
| Max bet during wagering | 1,500 ARS per spin |
| Max bonus balance | 30,000 ARS at any time |
| Claims per deposit | 1 (cannot claim ladder bonus twice for same deposit) |
| Vertical lock | Player stays on one vertical for entire ladder |

---

## STEP 5: TESTING CHECKLIST

- [ ] D1 bonus grants correctly at 120% (standard) and 150% (>15K) 
- [ ] D2 grants at 75% (NOT old 20% — this is the critical fix)
- [ ] FS credit to correct game for each deposit
- [ ] D5 CC credit works (first CC in ladder)
- [ ] D9 Lucky Wheel entry is granted
- [ ] D10 Lucky Wheel × 2 entries granted
- [ ] D10 Pre-VIP auto-enrollment fires for qualifying players (≥150K)
- [ ] Live ladder uses Bonus Cash correctly (not FS)
- [ ] Sport ladder uses Free Bets with 1.80 minimum odds
- [ ] Wagering caps enforced (max bet 1,500 ARS, max balance 30,000 ARS)
- [ ] Vertical detection correct (`game_preference` → correct ladder)
- [ ] Milestone emails (D3, D5, D7, D10) send correctly
- [ ] No duplicate bonus on same deposit number

---

## PATH TO 20% BONUS COST / GGR

| Mechanism | Impact | Timeline |
|-----------|--------|----------|
| Lower wagering (40× → 15–18×) | 10.5% → 14–15% | Weeks 1–4 |
| D2 bridge (75% holds STD conversion) | +2–3% | By week 6 |
| CC gifts from D5 (direct cost) | +1–2% | By week 8 |
| **Combined target** | **20%** | **Week 12** |
