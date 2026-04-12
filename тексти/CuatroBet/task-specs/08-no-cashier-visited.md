# 08 — No Cashier Visited

**Purpose:** Engage registered players who haven't visited the cashier (deposit page)  
**Three sub-paths:** Bounce (quick exit), Long Session (browsed but no cashier), Free Spins (played demo/won no-deposit FS)

---

## Sub-Path A: Bounce

**Segment:** Session under 60 seconds, left site without cashier interaction.

### Comm 1
| Field | Value |
|-------|-------|
| **ID** | NC-BOUNCE-C1 |
| **Timing** | T+15 min after bounce |
| **Channel** | SMS |
| **Copy (ES)** | "CuatroBet: Te fuiste rápido! Tu bono de 120% + 50 giros te espera. Volvé: [link]" |
| **Offer** | Welcome bonus reminder |
| **CTA** | App/site deep link |

### Comm 2
| Field | Value |
|-------|-------|
| **ID** | NC-BOUNCE-C2 |
| **Timing** | T+4 h |
| **Channel** | Email |
| **Subject (ES)** | "¿Problema técnico? Tu cuenta está lista" |
| **Copy** | Assume possible tech issue. Quick-start guide, payment methods, 2-minute deposit walkthrough |
| **Offer** | Welcome bonus |
| **CTA** | "Empezar ahora" |

### Comm 3
| Field | Value |
|-------|-------|
| **ID** | NC-BOUNCE-C3 |
| **Timing** | T+24 h |
| **Channel** | SMS |
| **Copy (ES)** | "CuatroBet: 120% + 50 giros gratis en Gates of Olympus. Depositá en 2 minutos: [link]" |
| **CTA** | Cashier link |

### Comm 4
| Field | Value |
|-------|-------|
| **ID** | NC-BOUNCE-C4 |
| **Timing** | T+72 h |
| **Channel** | Email |
| **Subject (ES)** | "Tu bono de bienvenida expira pronto" |
| **Offer** | Welcome bonus + 200 CC sweetener |
| **CTA** | "Activar bono" |

**Exit:** Cashier visited + deposit → Day 1 Retention Layer. No response → Reactivation (pre-FTD).

---

## Sub-Path B: Long Session (browsed but no cashier)

**Segment:** Session longer than 10 minutes, browsed or played demo, never clicked deposit button.

### Comm 1
| Field | Value |
|-------|-------|
| **ID** | NC-LONG-C1 |
| **Timing** | T+30 min after session end |
| **Channel** | In-app popup (next session) or SMS |
| **Copy (ES)** | "¿Te gustó lo que viste? Con tu primer depósito desbloqueás 120% + 50 giros y mucho más." |
| **Offer** | Welcome bonus |
| **CTA** | "Depositar ahora" |
| **Notes** | Player showed interest (10+ min browsing). Higher quality lead. |

### Comm 2
| Field | Value |
|-------|-------|
| **ID** | NC-LONG-C2 |
| **Timing** | T+6 h |
| **Channel** | Email |
| **Subject (ES)** | "Tus juegos favoritos te esperan con un bono especial" |
| **Copy** | Reference games/pages they browsed (if available from session data). Personalize. |
| **Offer** | Welcome bonus + "Depositá desde solo 500 ARS" (low barrier messaging) |
| **CTA** | "Depositar y jugar" |

### Comm 3
| Field | Value |
|-------|-------|
| **ID** | NC-LONG-C3 |
| **Timing** | T+24 h |
| **Channel** | SMS |
| **Copy (ES)** | "CuatroBet: Gates of Olympus, Jackpot Joker y más. Tu bono de 120% te espera: [link]" |
| **CTA** | Cashier link |

### Comm 4
| Field | Value |
|-------|-------|
| **ID** | NC-LONG-C4 |
| **Timing** | T+48 h |
| **Channel** | Email |
| **Subject (ES)** | "Último recordatorio: tu bono + 50 giros gratis" |
| **Offer** | Welcome bonus + 300 CC sweetener (higher than Bounce path — this player showed interest) |
| **CTA** | "Activar bono" |

**Exit:** Deposit → Day 1 Retention Layer. No response → Reactivation (pre-FTD, high-engagement filter).

---

## Sub-Path C: Free Spins (played demo / won no-deposit FS)

**Segment:** Player triggered free spins demo or won no-deposit free spins, no real-money deposit yet.

### Comm 1
| Field | Value |
|-------|-------|
| **ID** | NC-FS-C1 |
| **Timing** | T+15 min after FS session |
| **Channel** | In-app popup |
| **Copy (ES)** | "¡Bien jugado! Con un depósito real desbloqueás 120% + 50 giros extra. Ganancias reales." |
| **Offer** | Welcome bonus + bridge from demo to real-money |
| **CTA** | "Depositar ahora" |

### Comm 2
| Field | Value |
|-------|-------|
| **ID** | NC-FS-C2 |
| **Timing** | T+3 h |
| **Channel** | SMS |
| **Copy (ES)** | "CuatroBet: Tus giros gratis ya terminaron. Con 500 ARS activás 120% + 50 giros más: [link]" |
| **Offer** | Low barrier messaging (500 ARS minimum) |
| **CTA** | Cashier link |

### Comm 3
| Field | Value |
|-------|-------|
| **ID** | NC-FS-C3 |
| **Timing** | T+12 h |
| **Channel** | Email |
| **Subject (ES)** | "De giros gratis a ganancias reales" |
| **Copy** | Transition messaging: "You played for free, now play for real". Show game they played. |
| **Offer** | Welcome bonus |
| **CTA** | "Depositar y jugar" |

### Comm 4
| Field | Value |
|-------|-------|
| **ID** | NC-FS-C4 |
| **Timing** | T+48 h |
| **Channel** | SMS |
| **Copy (ES)** | "CuatroBet: 10 giros gratis extra sin depósito. Probá suerte: [link]" |
| **Offer** | 10 additional no-deposit FS as a second hook |
| **CTA** | Game link |

**Exit:** Deposit → Day 1 Retention Layer. No response → Reactivation (pre-FTD, free-spins sub-cohort).
