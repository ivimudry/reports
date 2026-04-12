# 04 — Payment Failure Recovery

**Priority:** 🟡 High  
**Purpose:** Recover 15–25% of failed deposit attempts in real-time (first 30 seconds in-session)  
**Entry Trigger:** Real-time deposit failure event from GR8 Tech (fires within 5 seconds)  
**Complements:** Failed cluster (Part II, section 6) which handles T+5min onward

---

## Failure Reason Classification

The platform must expose a failure reason code. Four routes:

| Code | Reason | Description |
|------|--------|-------------|
| `INSUFF` | Insufficient funds | Player tried to deposit more than available balance |
| `METHOD` | Method unavailable | Payment method temporarily down or unsupported |
| `DECLINE` | Acquirer declined | Bank or payment provider rejected transaction |
| `TIMEOUT` | Timeout / technical | Gateway timeout, network error, unknown |

---

### Touch 1A — Insufficient Funds Recovery
| Field | Value |
|-------|-------|
| **ID** | PFR-01A |
| **Timing** | T+0 (within 5 seconds of failure) |
| **Channel** | In-session popup |
| **Trigger** | Deposit failed, reason = Insufficient funds |
| **Segment** | Players with failed deposit (insufficient funds) |
| **Copy (ES)** | "Probá con un monto menor" |
| **Action** | Show preset amount buttons: **500 / 1,000 / 1,500 ARS** |
| **CTA** | One-click deposit at lower amount |
| **Exit** | Deposit succeeds → Touch 2 (celebration); Fails again → hand off to Failed cluster at T+30min |
| **Notes** | Player likely wanted to deposit 5,000 but only has 1,500. Lower preset catches this. |

---

### Touch 1B — Method Unavailable Recovery
| Field | Value |
|-------|-------|
| **ID** | PFR-01B |
| **Timing** | T+0 (within 5 seconds) |
| **Channel** | In-session popup |
| **Trigger** | Deposit failed, reason = Method unavailable (Mercado Pago / Naranja / bank down) |
| **Copy (ES)** | "Probá con otro método" |
| **Action** | One-click buttons for the other 2 active payment methods, preselected |
| **CTA** | Select alternative method → retry |
| **Exit** | Deposit succeeds → Touch 2; Fails → Failed cluster |
| **Notes** | Friction-free swap. Player doesn't need to find methods in a menu. |

---

### Touch 1C — Acquirer Declined Recovery
| Field | Value |
|-------|-------|
| **ID** | PFR-01C |
| **Timing** | T+0 (within 5 seconds) |
| **Channel** | In-session popup |
| **Trigger** | Deposit failed, reason = Acquirer declined |
| **Copy (ES)** | "Tu banco rechazó el pago. Probá con otro método" |
| **Action** | Same as Method Unavailable — one-click buttons for other methods |
| **CTA** | Select alternative method → retry |
| **Exit** | Deposit succeeds → Touch 2; Fails → Failed cluster |
| **Notes** | Bank is the issue. Only method swap can help. |

---

### Touch 1D — Timeout / Technical Recovery
| Field | Value |
|-------|-------|
| **ID** | PFR-01D |
| **Timing** | T+0 (within 5 seconds) |
| **Channel** | In-session popup |
| **Trigger** | Deposit failed, reason = Timeout / technical |
| **Action** | Auto-retry after 10 seconds with spinner showing "Reintentando…" |
| **Copy (ES)** | "Reintentando…" (spinner) |
| **CTA** | — (automatic) |
| **Exit** | Auto-retry succeeds → Touch 2; Fails → show manual retry button + alternative methods |
| **Notes** | Gateway timeouts often resolve on retry. No player re-entry required. |

---

### Touch 2 — Recovery Celebration (all reasons)
| Field | Value |
|-------|-------|
| **ID** | PFR-02 |
| **Timing** | Immediately on successful recovery |
| **Channel** | In-session popup |
| **Trigger** | Deposit succeeded after recovery flow |
| **Segment** | Players who recovered from a failed deposit |
| **Action** | Celebration + gift |
| **Offer** | 100 CC (Cuatro Coins) gift |
| **Copy (ES)** | Celebration popup |
| **Exit** | EXIT → Day 1 Retention Layer (if FTD) or current lifecycle |

---

### Hand-off — Not Recovered
| Field | Value |
|-------|-------|
| **Timing** | T+30 min (no recovery in session) |
| **Action** | Hand off to Failed cluster communication ladder (section 06) |
| **Notes** | The Failed cluster picks up from T+5min with 5 reasons × 4 comms each |

---

## Cost Model
| Item | Value |
|------|-------|
| Cost | Cheapest initiative in the playbook |
| Leverage | Highest leverage per peso spent |
| 100 CC gift per recovery | Negligible |

## KPI Targets
| Metric | Baseline | Target |
|--------|----------|--------|
| Payment success (effective, incl. recovered) | 55% | 65–70% |
| FTD conversion (downstream) | — | +2–4 pp |
| Bonus cost | — | No direct impact (payments issue) |

## Implementation Dependencies
1. Real-time failure event exposure from GR8 Tech (sub-5-second latency)
2. Failure reason classification must be accurate (if platform can't distinguish insufficient funds from acquirer declines, routing collapses)
3. Work with payments team to raise raw 55% rate in parallel — CRM recovery is a ceiling, real fix is upstream
