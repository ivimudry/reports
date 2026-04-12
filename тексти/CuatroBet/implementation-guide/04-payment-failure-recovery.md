# 04 — Payment Failure Recovery — Implementation Guide

**Chain:** Payment Failure Recovery  
**Priority:** High (cheapest initiative, highest ROI)  
**Estimated Communications:** 4 failure routes + 1 celebration = 5 touchpoints  
**Speed Requirement:** All recovery popups must fire within 5 SECONDS of failure event  
**Prerequisites from Master Doc:** Event `deposit_failed` with `failure_reason` field (`INSUFF`/`METHOD`/`DECLINE`/`TIMEOUT`); Payment methods API; Deep links `{base_url}/cashier?method={method}`, `{base_url}/cashier?amount={amount}`

---

## STEP 0: PRE-FLIGHT CHECKLIST

- [ ] Event `deposit_failed` fires within 5 seconds with accurate `failure_reason` codes
- [ ] Failure reason codes are distinguished: `INSUFF`, `METHOD`, `DECLINE`, `TIMEOUT`
- [ ] In-app popup system can trigger within 5 seconds of event (sub-second latency required)
- [ ] Payment methods API available (to show alternative methods)
- [ ] Deep links support preselected payment method: `{base_url}/cashier?method={method_id}`
- [ ] Deep links support prefilled amount: `{base_url}/cashier?amount={amount}`
- [ ] Auto-retry mechanism available for timeout failures
- [ ] 100 CC (Cuatro Coins) bonus template ready for recovery celebration
- [ ] Hand-off to Failed Deposits chain (06) configured at T+30min

**⚠️ CRITICAL:** If GR8 Tech cannot distinguish failure reasons (e.g., all failures return generic error), the routing logic collapses. Work with the platform team to ensure accurate reason codes BEFORE building this chain.

---

## STEP 1: CREATE THE JOURNEY

**Campaign Name:** `04-PFR-JOURNEY`  
**Type:** Triggered journey (event-based)  
**Entry Trigger:** Event = `deposit_failed`  
**Re-entry:** Yes (player can fail multiple times)  
**Re-entry cooldown:** 5 minutes (avoid spam on rapid retries)  
**Journey Window:** 30 minutes (after which → hand off to chain 06)

---

## STEP 2: ADD FAILURE REASON BRANCH

**Position:** Immediately after entry trigger  
**Branch Type:** Multi-way conditional split  
**Branch On:** `failure_reason` field from event payload

| Branch | Condition | Touch |
|--------|-----------|-------|
| A | `failure_reason = "INSUFF"` | Touch 1A — Lower Amount |
| B | `failure_reason = "METHOD"` | Touch 1B — Switch Method |
| C | `failure_reason = "DECLINE"` | Touch 1C — Switch Method |
| D | `failure_reason = "TIMEOUT"` | Touch 1D — Auto Retry |

---

## STEP 3: BUILD EACH FAILURE ROUTE

### 3.1 Touch 1A — Insufficient Funds Recovery

| Setting | Value |
|---------|-------|
| **Campaign ID** | `04-PFR-01A-POPUP` |
| **Channel** | In-session popup |
| **Timing** | Within 5 seconds of failure |

**Popup Content:**
- **Banner Text (ES):** `Probá con un Monto Menor`
- **Banner Description:** Compact recovery popup — wallet icon with down-arrow, friendly "try less" visual, three preset amount options highlighted, calm blue/green tones
- **Body:** Three preset amount buttons displayed prominently
- **Buttons:**
  | Button Label | Action |
  |-------------|--------|
  | `500 ARS` | One-click deposit → `{base_url}/cashier?amount=500` |
  | `1,000 ARS` | One-click deposit → `{base_url}/cashier?amount=1000` |
  | `1,500 ARS` | One-click deposit → `{base_url}/cashier?amount=1500` |
- **Dismiss:** "Cancelar" text link below buttons

**Logic:**
- Player attempted amount was likely higher than their balance
- Preset amounts are common low-value entry points for Argentine market
- One-click action reduces friction — player shouldn't need to re-enter payment details

**Configuration steps:**
1. On branch A, add popup node
2. Configure popup with 3 CTA buttons (each is a separate deposit deep link with prefilled amount)
3. Set popup trigger latency ≤5 seconds
4. Listen for `deposit_success` event after popup shown
5. If success → Touch 2 (celebration)
6. If failure again or no action within 30 min → hand off to chain 06

---

### 3.2 Touch 1B — Method Unavailable Recovery

| Setting | Value |
|---------|-------|
| **Campaign ID** | `04-PFR-01B-POPUP` |
| **Channel** | In-session popup |
| **Timing** | Within 5 seconds of failure |

**Popup Content:**
- **Banner Text (ES):** `Probá con Otro Método`
- **Banner Description:** Method switch popup — payment card icon with refresh/swap arrows, alternative payment logos (Mercado Pago, bank transfer), supportive green accents
- **Body (ES):** `Tu método de pago no está disponible en este momento. Elegí otro:`
- **Buttons:** Dynamic — show the 2–3 other active payment methods available to the player
  | Button | Action |
  |--------|--------|
  | `{alt_method_1_name}` | `{base_url}/cashier?method={alt_method_1_id}` |
  | `{alt_method_2_name}` | `{base_url}/cashier?method={alt_method_2_id}` |
  | `{alt_method_3_name}` (if exists) | `{base_url}/cashier?method={alt_method_3_id}` |
- **Dismiss:** "Cancelar" text link

**Data Required:**
- Payment methods API call to get available alternatives (exclude the failed method)
- Map method IDs to display names (e.g., "Mercado Pago", "Tarjeta de crédito", "Transferencia")

**Configuration steps:**
1. On branch B, call Payment Methods API to get alternatives
2. Show popup with dynamic buttons for each available method
3. Each button opens cashier with that method preselected
4. Same amount as original attempt is preserved
5. Listen for `deposit_success` → Touch 2
6. Failure or timeout → chain 06

---

### 3.3 Touch 1C — Acquirer Declined Recovery

| Setting | Value |
|---------|-------|
| **Campaign ID** | `04-PFR-01C-POPUP` |
| **Channel** | In-session popup |
| **Timing** | Within 5 seconds of failure |

**Popup Content:**
- **Banner Text (ES):** `Tu Banco Rechazó el Pago`
- **Banner Description:** Bank decline popup — bank building icon with X mark, shield symbol, alternative methods shown below, calm reassuring amber tones
- **Body (ES):** `No te preocupes, probá con otro método de pago:`
- **Buttons:** Same as Touch 1B — dynamic alternative methods
- **Dismiss:** "Cancelar" text link

**Notes:**
- Bank is the issue, not the platform
- Only a method swap can help
- Same implementation as 1B, different copy

**Configuration steps:**
1. On branch C, same as 1B but with different headline/body text
2. Show alternative payment methods
3. Listen for `deposit_success` → Touch 2
4. Failure or timeout → chain 06

---

### 3.4 Touch 1D — Timeout / Technical Recovery

| Setting | Value |
|---------|-------|
| **Campaign ID** | `04-PFR-01D-POPUP` |
| **Channel** | In-session popup (auto-retry) |
| **Timing** | Within 5 seconds of failure |

**Popup Content — Phase 1 (Auto-Retry):**
- **Banner Text (ES):** `Reintentando...`
- **Banner Description:** Loading/retry visual — circular spinner animation, gear icon, calm blue processing theme, progress indicator
- **Text (ES):** `Reintentando…`
- **Behavior:** Auto-retry the same deposit with same amount and method after 10-second delay
- **No player action required**

**Popup Content — Phase 2 (If auto-retry fails):**
- **Banner Text (ES):** `Problema Técnico`
- **Banner Description:** Technical issue popup — wrench/gear icon with warning triangle, two clear action buttons below, supportive amber/blue tones
- **Body (ES):** `Podés reintentar o probar con otro método:`
- **Button 1 (ES):** `Reintentar` → retry same deposit
- **Button 2 (ES):** `Otro método` → show alternatives (same as 1B)
- **Dismiss:** "Cancelar" text link

**Configuration steps:**
1. On branch D, trigger auto-retry after 10 seconds
2. Show spinner popup with "Reintentando…" text
3. If auto-retry succeeds → Touch 2 (celebration)
4. If auto-retry fails → replace spinner with manual retry + alternatives popup
5. Listen for `deposit_success` → Touch 2
6. No success within 30 min → chain 06

---

## STEP 4: RECOVERY CELEBRATION (All Routes)

### 4.1 Touch 2 — Recovery Celebration

| Setting | Value |
|---------|-------|
| **Campaign ID** | `04-PFR-02-POPUP` |
| **Channel** | In-session popup |
| **Timing** | Immediately on successful deposit after recovery |

**Popup Content:**
- **Banner Text (ES):** `Depósito Exitoso`
- **Banner Description:** Celebration theme — confetti explosion, golden coins falling, large green checkmark, Cuatro Coins icon (100 CC), sparkle effects
- **Body (ES):** `Depósito exitoso. Te regalamos 100 CC por tu perseverancia.`
- **CTA Button (ES):** `Seguir jugando` → dismiss
- **Auto-dismiss:** 8 seconds

**System Action:**
- Credit 100 CC (Cuatro Coins) to player's balance

**Configuration steps:**
1. Add celebration popup node after any successful `deposit_success` within the recovery flow
2. Credit 100 CC
3. EXIT journey
4. Player continues to Day 1 Retention Layer (if this was FTD) or current lifecycle

---

## STEP 5: HAND-OFF TO CHAIN 06 (Failed Deposits)

| Setting | Value |
|---------|-------|
| **Timing** | T+30 minutes after initial failure |
| **Condition** | No successful deposit within recovery window |

**Configuration steps:**
1. After 30 minutes with no `deposit_success` event → end this journey
2. Tag player with `payment_failed_unrecovered = true` and `last_failure_reason = {reason}`
3. Chain 06 (Failed Deposits) picks up from T+5min with its own communication ladder

---

## STEP 6: TESTING CHECKLIST

- [ ] Popup fires within 5 seconds of `deposit_failed` event (measure latency)
- [ ] Branch correctly routes based on failure reason codes
- [ ] Touch 1A: Preset amount buttons (500, 1000, 1500) work as one-click deposits
- [ ] Touch 1B: Alternative payment methods are dynamically loaded and correct
- [ ] Touch 1C: Same method alternatives as 1B, different copy displayed
- [ ] Touch 1D: Auto-retry fires after 10 seconds
- [ ] Touch 1D: If auto-retry fails, manual retry + alternatives shown
- [ ] Touch 2: Celebration popup appears on successful recovery
- [ ] Touch 2: 100 CC credited to player balance
- [ ] Re-entry cooldown (5 min) prevents popup spam on rapid failures
- [ ] Hand-off to chain 06 at T+30min for unrecovered failures
- [ ] Popups don't appear if player is NOT in session (edge case: player closes app during retry)
- [ ] Frequency cap: recovery popups are EXEMPT from daily message limits (transactional)

**Load test:**
- [ ] Simulate 100 concurrent failures — all popups fire within 5 seconds
- [ ] No duplicate popups on same failure event

---

## FLOW DIAGRAM

```
deposit_failed
     │
     ├── INSUFF ──→ [Lower amount buttons: 500/1000/1500] ──→ deposit_success? ──→ 🎉 Celebration + 100 CC
     │                                                      └──→ 30 min timeout ──→ Chain 06
     │
     ├── METHOD ──→ [Alt payment method buttons] ──→ deposit_success? ──→ 🎉 Celebration + 100 CC
     │                                             └──→ 30 min timeout ──→ Chain 06
     │
     ├── DECLINE ──→ [Alt payment method buttons] ──→ deposit_success? ──→ 🎉 Celebration + 100 CC
     │                                              └──→ 30 min timeout ──→ Chain 06
     │
     └── TIMEOUT ──→ [Auto-retry 10s] ──→ success? ──→ 🎉 Celebration + 100 CC
                                        └──→ [Manual retry + alt methods] ──→ deposit_success?
                                                                             └──→ 30 min timeout ──→ Chain 06
```

---

## COST MODEL

| Item | Cost |
|------|------|
| Recovery celebration | 100 CC per recovery (~50 ARS) |
| Total cost | Cheapest initiative in entire playbook |
| ROI leverage | Highest per peso spent |

---

## KPI TARGETS

| Metric | Baseline | Target |
|--------|----------|--------|
| Payment success rate (incl. recovered) | 55% | 65–70% |
| FTD conversion uplift (downstream) | — | +2–4 percentage points |
| Recovery rate within 30 seconds | — | 15–25% of failed attempts |
