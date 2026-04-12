# 02 — Pre-VIP Lifecycle

**Priority:** 🟡 High  
**Purpose:** Coach players who deposited 150,000 ARS cumulatively toward VIP I threshold (300,000 ARS) within 30 days  
**Current VIP base:** 15 players → Target: 30–45 in first quarter  
**Entry Trigger:** Cumulative lifetime deposits ≥ 150,000 ARS AND active in last 14 days

---

### Touch 1 — Pre-VIP Activation (Personal Email)
| Field | Value |
|-------|-------|
| **ID** | PVIP-01 |
| **Timing** | Day 1 (on entry trigger) |
| **Channel** | Personal email from CRM owner (real name, signature, direct reply-to) |
| **Trigger** | Lifetime deposits cross 150,000 ARS + active in last 14 days |
| **Segment** | Newly qualified Pre-VIP players |
| **Action** | Assign named CRM owner, flag in segmentation, add to Pre-VIP dashboard |
| **Subject (ES)** | "Acabás de desbloquear estatus Pre-VIP en CuatroBet" |
| **Body** | Warm, personal, no hard sell. Congratulate milestone, introduce CRM owner by name, outline benefits (15% weekly cashback, curated game recs, faster withdrawals, exclusive offers), hint at VIP I ("unos pocos pasos más") |
| **Offer** | 500 CC + 20 FS on player's favorite slot (from session history) |
| **CTA** | — (conversational, no hard CTA) |
| **In-App** | Pre-VIP unlock banner on next login |
| **Exit** | Continues to Day 3 |
| **Notes** | Named CRM owner is NON-NEGOTIABLE. Personal touch is the #1 conversion driver in this segment. |

---

### Touch 2 — Cashback Activation
| Field | Value |
|-------|-------|
| **ID** | PVIP-02 |
| **Timing** | Day 3 |
| **Channel** | Email + In-app banner |
| **Trigger** | Day 3 of Pre-VIP lifecycle |
| **Segment** | Pre-VIP players |
| **Action** | Enable 15% weekly cashback for 30 days |
| **Offer** | 15% weekly cashback — wager-free, applied every Monday on previous week's net losses, capped at 30,000 ARS |
| **Subject (ES)** | "Tu cashback Pre-VIP está activo" |
| **Body** | Explain how cashback works, when it pays out (Mondays), the cap (30,000 ARS) |
| **CTA** | — |
| **Exit** | Continues to Day 5 |
| **Notes** | Cashback MUST be wager-free. High-value players punish perceived tricks. |

---

### Touch 3 — Curated Game List + Reload Offer
| Field | Value |
|-------|-------|
| **ID** | PVIP-03 |
| **Timing** | Day 5 |
| **Channel** | Email |
| **Trigger** | Day 5 of Pre-VIP lifecycle |
| **Segment** | Pre-VIP players |
| **Action** | Send curated game list + reload bonus |
| **Subject (ES)** | "Tu selección personalizada y un bono especial" |
| **Body** | Curated list of top slots + 2 new releases matched to player's game preference |
| **Offer** | 60% match up to 10,000 ARS + 30 FS on a premium Pragmatic Play title, wagering 20×, validity 72h |
| **CTA** | "Depositar y jugar" |
| **Exit** | Continues to Day 10 |

---

### Touch 4 — Soft Coaching Push
| Field | Value |
|-------|-------|
| **ID** | PVIP-04 |
| **Timing** | Day 10 |
| **Channel** | App Push + SMS |
| **Trigger** | Day 10 of Pre-VIP lifecycle |
| **Segment** | Pre-VIP players |
| **Action** | Progress nudge toward VIP I |
| **Offer** | No bonus — motivational message |
| **Copy (ES)** | "Estás a unos 50,000 ARS de VIP I. Tu manager personal te está esperando." |
| **CTA** | Link to deposit / loyalty dashboard |
| **Exit** | Continues to Day 14 decision |
| **Notes** | Frame VIP I as achievable and desirable. Personalize the remaining amount. |

---

### Decision Point — Day 14
| Field | Value |
|-------|-------|
| **Timing** | Day 14 |
| **Condition** | Has the player reached VIP I threshold (300,000 ARS lifetime deposits)? |
| **Yes →** | EXIT → VIP I onboarding flow (personal manager, welcome package) |
| **No →** | Touch 5 — Second Chance Reload |

---

### Touch 5 — Second Chance Reload
| Field | Value |
|-------|-------|
| **ID** | PVIP-05 |
| **Timing** | Day 15 |
| **Channel** | Email + SMS (from CRM owner personally) |
| **Trigger** | Day 15, player has NOT reached VIP I by Day 14 |
| **Segment** | Pre-VIP players below VIP I threshold |
| **Subject (ES)** | "Te extrañamos esta semana" |
| **Offer** | 100% match up to 20,000 ARS + 50 FS + extended cashback, wagering 15×, validity 72h |
| **CTA** | "Depositar ahora" |
| **Exit** | Continues to Day 21 decision |

---

### Decision Point — Day 21
| Field | Value |
|-------|-------|
| **Timing** | Day 21 |
| **Condition** | Any deposit since Day 14? |
| **Yes →** | Cashback top-up + predictive churn monitoring enabled. Continue to Day 30. |
| **No →** | Add to Churn Intervention flow at Day 22 |

---

### Touch 6 — Cashback Top-Up (Day 21, deposited)
| Field | Value |
|-------|-------|
| **ID** | PVIP-06 |
| **Timing** | Day 21 (if deposited since Day 14) |
| **Channel** | System + Email |
| **Action** | Top-up cashback, enable predictive churn monitoring |
| **Notes** | Passive touch — monitoring intensifies, no aggressive messaging |

---

### Decision Point — Day 30
| Field | Value |
|-------|-------|
| **Timing** | Day 30 |
| **Condition** | Has the player reached VIP I (300,000 ARS)? |
| **Yes →** | EXIT → VIP I onboarding |
| **No →** | Stay in Pre-VIP for 30 more days with reduced cadence (1 email/week, no SMS). Drop to Regular if no activity in extended 30 days. |

---

## KPI Targets
| Metric | Baseline | Target |
|--------|----------|--------|
| VIP base | 15 | 30–45 in Q1 |
| Pre-VIP → VIP I conversion | — | 30–40% within 30 days |
| ADPU uplift (Pre-VIP cohort) | — | 2× from month 3 to month 5 |

## Implementation Notes
1. Named CRM owner assignment is non-negotiable
2. Cashback must be wager-free
3. 150,000 ARS entry threshold calibrated against tier economics (Premium 15K, Maestro 35K, VIP I ~300K). Review quarterly.
4. Personalize the "distance to VIP I" in all messages
