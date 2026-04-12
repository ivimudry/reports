# 12 — Reactivation Matrix

**Purpose:** Win back inactive players with escalating offers based on engagement history and time inactive  
**Structure:** 2 engagement histories × 3 time buckets × 4 comms + special cases  
**Total:** 36+ communications  
**Value tier overlay:** Every base offer scales by player's lifetime value tier at send time

---

## Value Tier Overlay (applies to ALL cells)

Every cell below specifies a **base offer**. Actual offer is scaled by lifetime value:

| Tier | Lifetime Deposits | Scaling | Channel |
|------|-------------------|---------|---------|
| **Micro** | <5,000 ARS | CC gift only, no match bonus | Standard |
| **Low** | 5,000–25,000 ARS | Base offer as written | Standard |
| **Mid** | 25,000–75,000 ARS | 1.5× match amount, +10 FS | Standard |
| **High** | 75,000–150,000 ARS | 2× match amount, +20 FS | Named CRM owner email |
| **Pre-VIP+** | >150,000 ARS | 2.5× match, +30 FS, +100 CC, lower wagering | CRM owner via WhatsApp |

---

## Frequency Cap
**Maximum 1 message per day per player.** If multiple ladders fire on the same day → collapse to highest-value message only.

---

## Integration with Predictive Churn
When GR8 Tech Predictive Churn model is activated:
- Players with churn score >60 enter the 7-day ladder at **day 3 or 4** instead of day 7
- Ladder structure remains the same

---

## ACTIVE × 7 DAYS (highest return probability)

**Segment:** Was actively engaged (deposits, sessions, missions), now 7 days inactive.  
**Rationale:** Low-friction, habit-preserving. Most likely to return — don't burn budget.

### Comm 1
| Field | Value |
|-------|-------|
| **ID** | REACT-A7-C1 |
| **Timing** | Day 7 of inactivity |
| **Channel** | Email |
| **Subject (ES)** | "Te extrañamos, [Name]. Tu slot favorito tiene novedades." |
| **Base Offer** | 30% match up to 2,000 ARS + 20 FS on Jackpot Joker, 15× wagering, 48h validity |
| **CTA** | "Volver a jugar" |

### Comm 2
| Field | Value |
|-------|-------|
| **ID** | REACT-A7-C2 |
| **Timing** | Day 9 |
| **Channel** | App Push |
| **Copy (ES)** | "Tu bono de regreso vence en 24h: [link]" |
| **CTA** | Cashier link |

### Comm 3
| Field | Value |
|-------|-------|
| **ID** | REACT-A7-C3 |
| **Timing** | Day 11 |
| **Channel** | SMS |
| **Copy (ES)** | "CuatroBet: 30% + 20 giros gratis te esperan. Última oportunidad: [link]" |
| **CTA** | Cashier link |

### Comm 4
| Field | Value |
|-------|-------|
| **ID** | REACT-A7-C4 |
| **Timing** | Day 13 |
| **Channel** | Email |
| **Subject (ES)** | "Tu oferta exclusiva se va" |
| **Base Offer** | Sweetened: 40% match up to 2,500 ARS + 25 FS, 15× wagering, 24h validity |
| **CTA** | "Última oportunidad" |

**Exit:** Activity → Regular or Pre-VIP. No response → escalate to Active × 14 days.

---

## ACTIVE × 14 DAYS

**Segment:** Was active, now 14 days inactive. Medium urgency.

### Comm 1
| Field | Value |
|-------|-------|
| **ID** | REACT-A14-C1 |
| **Timing** | Day 14 |
| **Channel** | Email |
| **Subject (ES)** | "Han pasado 2 semanas. Esto te puede interesar." |
| **Base Offer** | 50% match up to 3,000 ARS + 30 FS on Gates of Olympus, 15× wagering, 48h |
| **CTA** | "Depositar y jugar" |

### Comm 2
| Field | Value |
|-------|-------|
| **ID** | REACT-A14-C2 |
| **Timing** | Day 16 |
| **Channel** | SMS |
| **Copy (ES)** | "CuatroBet: 50% de bono + 30 giros gratis. Oferta exclusiva: [link]" |

### Comm 3
| Field | Value |
|-------|-------|
| **ID** | REACT-A14-C3 |
| **Timing** | Day 18 |
| **Channel** | App Push |
| **Copy (ES)** | "Tu bono especial de regreso expira en 48h." |

### Comm 4
| Field | Value |
|-------|-------|
| **ID** | REACT-A14-C4 |
| **Timing** | Day 20 |
| **Channel** | Email |
| **Subject (ES)** | "Última oportunidad antes de que tu oferta expire" |
| **Base Offer** | 60% match up to 4,000 ARS + 40 FS, 12× wagering, 24h |
| **CTA** | "Activar ahora" |

**Exit:** Activity → Regular/Pre-VIP. No response → escalate to Active × 21+ days.

---

## ACTIVE × 21+ DAYS

**Segment:** Was active, now 21+ days inactive. High urgency, higher offers.

### Comm 1
| Field | Value |
|-------|-------|
| **ID** | REACT-A21-C1 |
| **Timing** | Day 21 |
| **Channel** | Email + SMS |
| **Subject (ES)** | "Hace 3 semanas que no te vemos. Esto es lo mejor que tenemos." |
| **Base Offer** | 75% match up to 5,000 ARS + 50 FS + 200 CC, 12× wagering, 72h |
| **CTA** | "Volver ahora" |

### Comm 2
| Field | Value |
|-------|-------|
| **ID** | REACT-A21-C2 |
| **Timing** | Day 24 |
| **Channel** | SMS |
| **Copy (ES)** | "CuatroBet: Tu bono de recuperación de 75% vence en 48h: [link]" |

### Comm 3
| Field | Value |
|-------|-------|
| **ID** | REACT-A21-C3 |
| **Timing** | Day 27 |
| **Channel** | Email |
| **Subject (ES)** | "Último intento: tu mejor oferta de este mes" |
| **Base Offer** | 100% match up to 6,000 ARS + 60 FS + 500 CC + Lucky Wheel entry, 10× wagering, 48h |

### Comm 4
| Field | Value |
|-------|-------|
| **ID** | REACT-A21-C4 |
| **Timing** | Day 30 |
| **Channel** | SMS |
| **Copy (ES)** | "CuatroBet: Oferta final. 100% + 60 giros + Lucky Wheel. Válido 24h: [link]" |

**Exit:** Activity → Regular or Pre-VIP. No response → **Deep Churn** (quarterly win-back only).

---

## PASSIVE × 7 DAYS

**Segment:** Was passive (low engagement before going inactive), 7 days inactive.  
**Lower return probability, smaller offers to protect budget.**

### Comm 1
| Field | Value |
|-------|-------|
| **ID** | REACT-P7-C1 |
| **Timing** | Day 7 |
| **Channel** | Email |
| **Subject (ES)** | "Algo nuevo te espera en CuatroBet" |
| **Base Offer** | 20% match up to 1,500 ARS + 10 FS, 20× wagering, 48h |
| **CTA** | "Descubrir" |

### Comm 2
| Field | Value |
|-------|-------|
| **ID** | REACT-P7-C2 |
| **Timing** | Day 10 |
| **Channel** | SMS |
| **Copy (ES)** | "CuatroBet: 20% bono + 10 giros gratis: [link]" |

### Comm 3
| Field | Value |
|-------|-------|
| **ID** | REACT-P7-C3 |
| **Timing** | Day 12 |
| **Channel** | App Push |
| **Copy (ES)** | "Nuevos juegos disponibles. ¡Vení a probarlos!" |

### Comm 4
| Field | Value |
|-------|-------|
| **ID** | REACT-P7-C4 |
| **Timing** | Day 13 |
| **Channel** | Email |
| **Base Offer** | 25% match up to 2,000 ARS + 15 FS, 18× wagering, 24h |

**Exit:** Activity → Regular. No response → Passive × 14.

---

## PASSIVE × 14 DAYS

### Comm 1
| Field | Value |
|-------|-------|
| **ID** | REACT-P14-C1 |
| **Timing** | Day 14 |
| **Channel** | Email |
| **Base Offer** | 35% match up to 2,000 ARS + 20 FS, 18× wagering, 48h |

### Comm 2
| Field | Value |
|-------|-------|
| **ID** | REACT-P14-C2 |
| **Timing** | Day 17 |
| **Channel** | SMS |

### Comm 3
| Field | Value |
|-------|-------|
| **ID** | REACT-P14-C3 |
| **Timing** | Day 19 |
| **Channel** | App Push |

### Comm 4
| Field | Value |
|-------|-------|
| **ID** | REACT-P14-C4 |
| **Timing** | Day 20 |
| **Channel** | Email |
| **Base Offer** | 45% match up to 2,500 ARS + 25 FS, 15× wagering, 24h |

**Exit:** Activity → Regular. No response → Passive × 21+.

---

## PASSIVE × 21+ DAYS

### Comm 1
| Field | Value |
|-------|-------|
| **ID** | REACT-P21-C1 |
| **Timing** | Day 21 |
| **Channel** | Email + SMS |
| **Base Offer** | 50% match up to 3,000 ARS + 30 FS + 100 CC, 15× wagering, 72h |

### Comm 2
| Field | Value |
|-------|-------|
| **ID** | REACT-P21-C2 |
| **Timing** | Day 24 |
| **Channel** | SMS |

### Comm 3
| Field | Value |
|-------|-------|
| **ID** | REACT-P21-C3 |
| **Timing** | Day 27 |
| **Channel** | Email |
| **Base Offer** | 65% match up to 4,000 ARS + 40 FS + 200 CC, 12× wagering, 48h |

### Comm 4
| Field | Value |
|-------|-------|
| **ID** | REACT-P21-C4 |
| **Timing** | Day 30 |
| **Channel** | SMS |

**Exit:** Activity → Regular. No response → **Deep Churn**.

---

## SPECIAL CASE: Verified But No Reacted

**Segment:** Player completed KYC (email, phone, documents) but never deposited or had meaningful activity after verification.  
**Rationale:** Invested effort in verification = interest exists. Something blocked them.

### Comm 1
| Field | Value |
|-------|-------|
| **ID** | REACT-VNR-C1 |
| **Timing** | Day 3 after full verification |
| **Channel** | Email |
| **Subject (ES)** | "Tu cuenta está 100% lista. Solo falta tu primer depósito." |
| **Offer** | Enhanced welcome: 150% match + 60 FS, 20× wagering, 72h |
| **CTA** | "Depositar ahora" |

### Comm 2
| Field | Value |
|-------|-------|
| **ID** | REACT-VNR-C2 |
| **Timing** | Day 5 |
| **Channel** | SMS |
| **Copy (ES)** | "CuatroBet: Verificación completa. 150% bono de bienvenida te espera: [link]" |

### Comm 3
| Field | Value |
|-------|-------|
| **ID** | REACT-VNR-C3 |
| **Timing** | Day 10 |
| **Channel** | Email |
| **Subject (ES)** | "¿Tuviste un problema con el depósito?" |
| **Copy** | Support-focused: "If payment failed, try these methods". List all 3 methods with guides. |
| **Offer** | Same enhanced welcome |

### Comm 4
| Field | Value |
|-------|-------|
| **ID** | REACT-VNR-C4 |
| **Timing** | Day 14 |
| **Channel** | SMS |
| **Copy (ES)** | "CuatroBet: Tu bono exclusivo de 150% + 60 giros. Última semana: [link]" |

**Exit:** Deposit → Day 1 Retention Layer. No response → Deep Churn.

---

## Behavioral Filter (Clicks/Opens/Pages)

Applied as segmentation overlay on ALL ladders above:

| Filter | Behavior | Strategy |
|--------|----------|----------|
| **High-engagement** | Opens emails, clicks links, no deposit | Offer-heavy sequences, higher match % |
| **Low-engagement** | Low open rate | SMS-heavy, drop email frequency, simplify content |
| **Zero-engagement** | No opens, no clicks, no visits | Single strong SMS at day 21 → Deep Churn |
