# 07 — No Bonus Cluster

**Purpose:** Engage players who registered but didn't claim the welcome bonus  
**Two sub-branches:** Missed (didn't see it) vs None Interested (actively declined)

---

## Sub-Branch A: Missed

**Segment:** Player registered, did not claim welcome bonus, 1+ hour after registration with no bonus-related interaction.

### Comm 1
| Field | Value |
|-------|-------|
| **ID** | NB-MISS-C1 |
| **Timing** | T+1 h after registration |
| **Channel** | In-app popup (if in session) or SMS |
| **Copy (ES)** | "¡No te pierdas tu bono de bienvenida! 120% + 50 giros gratis te esperan." |
| **Offer** | Welcome bonus reminder (120% + 50 FS) |
| **CTA** | "Reclamar bono" → cashier |

### Comm 2
| Field | Value |
|-------|-------|
| **ID** | NB-MISS-C2 |
| **Timing** | T+6 h |
| **Channel** | Email |
| **Subject (ES)** | "Olvidaste algo: tu bono de 120% + 50 giros" |
| **Copy** | Step-by-step how to claim bonus, visual deposit guide |
| **Offer** | Welcome bonus |
| **CTA** | "Depositar y activar" |

### Comm 3
| Field | Value |
|-------|-------|
| **ID** | NB-MISS-C3 |
| **Timing** | T+24 h |
| **Channel** | SMS |
| **Copy (ES)** | "CuatroBet: Tu bono de 120% + 50 giros vence pronto. Activalo ahora: [link]" |
| **CTA** | Cashier link |

### Comm 4
| Field | Value |
|-------|-------|
| **ID** | NB-MISS-C4 |
| **Timing** | T+48 h |
| **Channel** | Email |
| **Subject (ES)** | "Última oportunidad: tu bono expira en 24 horas" |
| **Offer** | Welcome bonus + extra 200 CC sweetener |
| **CTA** | "Reclamar ahora" |

**Exit:** Bonus claimed → Day 1 Retention Layer. No response after Comm 4 → Reactivation (pre-FTD cohort).

---

## Sub-Branch B: None Interested

**Segment:** Player explicitly declined welcome bonus OR behavior shows zero bonus interest (clicked through bonus flow, bypassed it).  
**Rationale:** High-pressure bonus messaging alienates this segment. Switch to low-friction habit-seeding and product discovery.

### Comm 1
| Field | Value |
|-------|-------|
| **ID** | NB-NONE-C1 |
| **Timing** | T+2 h after registration |
| **Channel** | In-app popup |
| **Copy (ES)** | "Descubrí los juegos más populares. Probá Gates of Olympus gratis." |
| **Offer** | NO bonus mention — pure game discovery |
| **CTA** | "Jugar demo" → top game |
| **Notes** | Do NOT push bonuses. Focus on product experience. |

### Comm 2
| Field | Value |
|-------|-------|
| **ID** | NB-NONE-C2 |
| **Timing** | T+24 h |
| **Channel** | Email |
| **Subject (ES)** | "Los 5 juegos más populares esta semana" |
| **Copy** | Curated top 5 from the top 10 list, screenshots, mini-reviews |
| **Offer** | No bonus — optional mention: "Siempre podés activar tu bono si cambiás de opinión" |
| **CTA** | "Explorar juegos" |

### Comm 3
| Field | Value |
|-------|-------|
| **ID** | NB-NONE-C3 |
| **Timing** | T+72 h |
| **Channel** | SMS |
| **Copy (ES)** | "CuatroBet: Jackpot Joker tiene 10 millones de premio. Probalo gratis: [link]" |
| **CTA** | Game link |

### Comm 4
| Field | Value |
|-------|-------|
| **ID** | NB-NONE-C4 |
| **Timing** | T+7 days |
| **Channel** | Email |
| **Subject (ES)** | "Tu cuenta sigue lista" |
| **Copy** | Soft re-engagement, new game releases, community highlights |
| **Offer** | Soft mention: "Tu bono de bienvenida sigue disponible" |
| **CTA** | "Volver a CuatroBet" |

**Exit:** Any deposit → Day 1 Retention Layer. No response → Reactivation (pre-FTD, low-engagement filter).
