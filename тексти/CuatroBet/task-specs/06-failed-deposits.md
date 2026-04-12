# 06 — Failed Deposits: Communication Ladders

**Purpose:** Fill the empty Comm 1–4 boxes in the Failed cluster on Miro  
**Scope:** 5 failure reasons × 4 communications each = 20 comms  
**Timing:** Picks up from T+5 min (Payment Failure Recovery handles T+0 to T+5min)  
**Integration:** Works end-to-end with Payment Failure Recovery (section 04)

---

## Reason 1: No Attempt for Deposit (closed cashier page)

**Segment:** Player opened cashier page, did not attempt any deposit, closed/navigated away, 30+ min inactive.

### Comm 1
| Field | Value |
|-------|-------|
| **ID** | FAIL-R1-C1 |
| **Timing** | T+30 min after cashier close |
| **Channel** | In-app popup (if in session) or SMS (if exited) |
| **Copy (ES)** | "Te faltó un paso. Tu bono de bienvenida te espera. Depositá ahora y empezá a jugar: [link]" |
| **Offer** | Reminder of welcome bonus (120% + 50 FS) |
| **CTA** | Deep link to cashier |

### Comm 2
| Field | Value |
|-------|-------|
| **ID** | FAIL-R1-C2 |
| **Timing** | T+2 h |
| **Channel** | SMS |
| **Copy (ES)** | "CuatroBet: Tu bono de 120% + 50 giros aún te espera. Depositá en minutos: [link]" |
| **Offer** | Same welcome bonus |
| **CTA** | Cashier link |

### Comm 3
| Field | Value |
|-------|-------|
| **ID** | FAIL-R1-C3 |
| **Timing** | T+24 h |
| **Channel** | Email |
| **Subject (ES)** | "Tu bono de bienvenida vence pronto" |
| **Copy** | Urgency — bonus expiring, step-by-step deposit guide, payment method highlights |
| **Offer** | Welcome bonus + added 200 CC incentive |
| **CTA** | "Depositar ahora" |

### Comm 4
| Field | Value |
|-------|-------|
| **ID** | FAIL-R1-C4 |
| **Timing** | T+48 h |
| **Channel** | SMS |
| **Copy (ES)** | "CuatroBet: Última oportunidad. 120% + 50 giros. Válido 24h más: [link]" |
| **Offer** | Final urgency reminder |
| **CTA** | Cashier link |

**Exit:** Deposit attempted → Day 1 Retention Layer. No response after Comm 4 → Reactivation (pre-FTD cohort).

---

## Reason 2: Failed Deposit Attempt — Tech Reason (first attempt)

**Segment:** One deposit attempt failed due to technical reason (gateway timeout, network error, provider unavailable).

### Comm 1
| Field | Value |
|-------|-------|
| **ID** | FAIL-R2-C1 |
| **Timing** | T+5 min |
| **Channel** | In-session popup (if still in session) |
| **Copy (ES)** | "Tuvimos un problema técnico. Probá de nuevo o usá otro método de pago." |
| **Action** | Show alternative payment methods + retry button |
| **CTA** | "Reintentar" / "Otro método" |

### Comm 2
| Field | Value |
|-------|-------|
| **ID** | FAIL-R2-C2 |
| **Timing** | T+1 h |
| **Channel** | SMS |
| **Copy (ES)** | "CuatroBet: El problema está resuelto. Depositá ahora y activá tu bono: [link]" |
| **Offer** | Welcome bonus reminder + 200 ARS extra no-deposit credit as apology |
| **CTA** | Cashier link |

### Comm 3
| Field | Value |
|-------|-------|
| **ID** | FAIL-R2-C3 |
| **Timing** | T+6 h |
| **Channel** | Email |
| **Subject (ES)** | "Tu depósito está listo para completarse" |
| **Copy** | Apologize for tech issue, suggest best payment method based on time of day, visual guide |
| **Offer** | Welcome bonus + 200 ARS credit |
| **CTA** | "Depositar ahora" |

### Comm 4
| Field | Value |
|-------|-------|
| **ID** | FAIL-R2-C4 |
| **Timing** | T+24 h |
| **Channel** | SMS |
| **Copy (ES)** | "CuatroBet: Tu bono 120% + 50 giros + 200 ARS de regalo te esperan: [link]" |
| **CTA** | Cashier link |

**Exit:** Successful deposit → Day 1 Retention with credit applied. No response → Reactivation (Payment-blocked sub-cohort).

---

## Reason 3: Failed Two+ Deposit Attempts — Tech Reason

**Segment:** 2+ failed attempts in the same session = persistent issue.

### Comm 1
| Field | Value |
|-------|-------|
| **ID** | FAIL-R3-C1 |
| **Timing** | T+5 min |
| **Channel** | In-session popup |
| **Copy (ES)** | "Detectamos un problema persistente. Nuestro equipo está revisando. Te avisamos cuando esté resuelto." |
| **Action** | Collect player's preferred contact method, auto-create support ticket |
| **CTA** | "Avisame por SMS" / "Avisame por email" |

### Comm 2
| Field | Value |
|-------|-------|
| **ID** | FAIL-R3-C2 |
| **Timing** | T+2 h (or when issue resolved, whichever first) |
| **Channel** | Player's preferred contact method |
| **Copy (ES)** | "CuatroBet: El problema se resolvió. Depositá ahora y recibí un regalo extra: [link]" |
| **Offer** | Welcome bonus + 500 ARS apology credit, no wagering |
| **CTA** | Cashier link |

### Comm 3
| Field | Value |
|-------|-------|
| **ID** | FAIL-R3-C3 |
| **Timing** | T+12 h |
| **Channel** | Email |
| **Subject (ES)** | "Disculpas y un regalo especial" |
| **Copy** | Formal apology, confirm issue resolved, multiple payment options listed |
| **Offer** | Welcome bonus + 500 ARS credit |
| **CTA** | "Depositar ahora" |

### Comm 4
| Field | Value |
|-------|-------|
| **ID** | FAIL-R3-C4 |
| **Timing** | T+48 h |
| **Channel** | SMS |
| **Copy (ES)** | "CuatroBet: Tu bono + 500 ARS de regalo siguen esperándote: [link]" |
| **CTA** | Cashier link |

**Exit:** Successful deposit → exit. No response → Reactivation (Payment-blocked high-priority flag).

---

## Reason 4: Deposit Declined by Acquirer

**Segment:** Deposit rejected by acquiring bank or payment provider (insufficient funds, card blocked, provider risk rule).

### Comm 1
| Field | Value |
|-------|-------|
| **ID** | FAIL-R4-C1 |
| **Timing** | T+5 min |
| **Channel** | In-session popup |
| **Copy (ES)** | "Tu banco no aprobó la transacción. Probá con otro método o un monto menor." |
| **Action** | Show alternative payment methods + lower amount presets |
| **CTA** | "Otro método" / "Monto menor" |

### Comm 2
| Field | Value |
|-------|-------|
| **ID** | FAIL-R4-C2 |
| **Timing** | T+1 h |
| **Channel** | SMS |
| **Copy (ES)** | "CuatroBet: Probá con Mercado Pago o transferencia bancaria. Tu bono te espera: [link]" |
| **CTA** | Cashier link with alternative method preselected |

### Comm 3
| Field | Value |
|-------|-------|
| **ID** | FAIL-R4-C3 |
| **Timing** | T+12 h |
| **Channel** | Email |
| **Subject (ES)** | "Métodos alternativos para completar tu depósito" |
| **Copy** | List all available methods (Mercado Pago, Naranja Betterbro, bank transfer), pros of each |
| **Offer** | Welcome bonus + 100 CC for trying alternative method |
| **CTA** | Deep link per method |

### Comm 4
| Field | Value |
|-------|-------|
| **ID** | FAIL-R4-C4 |
| **Timing** | T+48 h |
| **Channel** | SMS |
| **Copy (ES)** | "CuatroBet: Todavía podés activar tu bono de 120%. Probá otro método: [link]" |
| **CTA** | Cashier link |

**Exit:** Successful deposit → exit. No response → Reactivation (Payment-blocked cohort).

---

## Reason 5: Fraud

**Segment:** Deposit attempt flagged by risk engine.

### Comm 1
| Field | Value |
|-------|-------|
| **ID** | FAIL-R5-C1 |
| **Timing** | T+5 min |
| **Channel** | In-session popup |
| **Copy (ES)** | "Tu transacción está siendo verificada por seguridad. Te contactaremos pronto." |
| **Action** | Flag account, route to fraud review queue |
| **CTA** | — (informational) |

### Comm 2
| Field | Value |
|-------|-------|
| **ID** | FAIL-R5-C2 |
| **Timing** | On fraud review completion |
| **Channel** | Email |
| **If false positive:** | "La verificación fue exitosa. Ya podés depositar normalmente: [link]" |
| **If confirmed fraud:** | Account closure notification |

### Comm 3
| Field | Value |
|-------|-------|
| **ID** | FAIL-R5-C3 |
| **Timing** | T+24 h (false positive only) |
| **Channel** | SMS |
| **Copy (ES)** | "CuatroBet: Tu cuenta está verificada. Depositá y activá tu bono: [link]" |
| **CTA** | Cashier link |

### Comm 4
| Field | Value |
|-------|-------|
| **ID** | FAIL-R5-C4 |
| **Timing** | T+48 h (false positive only) |
| **Channel** | Email |
| **Copy** | Final reminder with welcome bonus details |
| **CTA** | "Depositar ahora" |

**Exit:** Resolved fraud (false positive) → back to current lifecycle stage. Confirmed fraud → account closure.
