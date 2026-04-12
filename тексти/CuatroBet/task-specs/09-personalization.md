# 09 — Personalization Cluster

**Purpose:** Personal celebration and recognition touchpoints  
**Types:** Anniversary, Birthday, Personal Custom, Zodiac Bonus

---

## Type A: Anniversary

**Segment:** Any active player reaching account creation anniversary (1, 2, 3+ years)

### Comm 1 — Anniversary Celebration
| Field | Value |
|-------|-------|
| **ID** | PERS-ANNIV-C1 |
| **Timing** | Anniversary date, morning |
| **Channel** | Email + In-app popup |
| **Subject (ES)** | "¡Feliz [X] año con CuatroBet!" |
| **Copy** | Celebration, player stats summary (total games played, favorite game, biggest win) |
| **Offer** | Year 1: 100% match up to 5,000 ARS + 30 FS + 500 CC. Year 2+: scale up. Wagering 15×, 72h validity. |
| **CTA** | "Reclamar regalo" |

### Comm 2 — Follow-Up
| Field | Value |
|-------|-------|
| **ID** | PERS-ANNIV-C2 |
| **Timing** | Anniversary +24 h (if no response) |
| **Channel** | SMS |
| **Copy (ES)** | "CuatroBet: Tu regalo de aniversario vence en 48h. No lo pierdas: [link]" |
| **CTA** | Cashier link |

### Comm 3 — Final Reminder
| Field | Value |
|-------|-------|
| **ID** | PERS-ANNIV-C3 |
| **Timing** | Anniversary +48 h (if still no response) |
| **Channel** | Email |
| **Subject (ES)** | "Último día: tu regalo de aniversario" |
| **CTA** | "Reclamar ahora" |

### Comm 4 — Thank You / Transition
| Field | Value |
|-------|-------|
| **ID** | PERS-ANNIV-C4 |
| **Timing** | Anniversary +72 h |
| **Channel** | Email |
| **Copy** | Thank-you message if claimed. Soft "we'll be here" if not claimed. |
| **Exit** | Return to regular lifecycle |

---

## Type B: Birthday

**Segment:** Any player with verified birthday

### Comm 1 — Birthday Celebration
| Field | Value |
|-------|-------|
| **ID** | PERS-BDAY-C1 |
| **Timing** | Birthday date, morning |
| **Channel** | Email + In-app popup + SMS |
| **Subject (ES)** | "¡Feliz cumpleaños! CuatroBet tiene un regalo para vos" |
| **Offer** | 100% match up to 3,000 ARS + 25 FS on player's favorite slot + 300 CC. Wagering 15×, 48h validity. |
| **CTA** | "Abrir regalo" |

### Comm 2
| Field | Value |
|-------|-------|
| **ID** | PERS-BDAY-C2 |
| **Timing** | Birthday +12 h |
| **Channel** | App Push |
| **Copy (ES)** | "Tu regalo de cumpleaños te está esperando. Abrilo ahora 🎂" |
| **CTA** | Deep link to bonus |

### Comm 3
| Field | Value |
|-------|-------|
| **ID** | PERS-BDAY-C3 |
| **Timing** | Birthday +24 h |
| **Channel** | SMS |
| **Copy (ES)** | "CuatroBet: Tu regalo de cumpleaños vence en 24h: [link]" |
| **CTA** | Cashier link |

### Comm 4
| Field | Value |
|-------|-------|
| **ID** | PERS-BDAY-C4 |
| **Timing** | Birthday +48 h |
| **Channel** | Email |
| **Copy** | Thank-you / offer expiry notification |
| **Exit** | Return to regular lifecycle |

---

## Type C: Personal Custom

**Segment:** Ad-hoc triggers set by CRM manager (e.g., player mentioned a specific game in support, player 5,000 ARS from a tier threshold).

### Template Structure
| Comm | Purpose |
|------|---------|
| **Comm 1** | Trigger-specific initial message |
| **Comm 2** | Follow-up 24–48h later if no response |
| **Comm 3** | Final reminder before offer expiry |
| **Comm 4** | Thank-you or transition |

### Required Fields Per Campaign
- Trigger condition
- Target audience size
- Channel per comm
- Copy per comm in Spanish
- Offer details
- Exit condition
- Success metric
- **Reviewed weekly** in CRM standup

---

## Type D: Zodiac Bonus

**Segment:** All active players, triggered on first day of each zodiac month.

### Comm 1 — Zodiac Launch
| Field | Value |
|-------|-------|
| **ID** | PERS-ZODIAC-C1 |
| **Timing** | First day of zodiac month |
| **Channel** | Email + In-app banner |
| **Subject (ES)** | "Tu bono zodiacal de [Signo] llegó" |
| **Offer** | Zodiac-themed bonus: 50% match + 15 FS on a zodiac-matched game, wagering 20×, 7-day validity |
| **CTA** | "Reclamar bono zodiacal" |

### Comm 2
| Field | Value |
|-------|-------|
| **ID** | PERS-ZODIAC-C2 |
| **Timing** | Day 3 of zodiac month |
| **Channel** | App Push |
| **Copy (ES)** | "Tu bono zodiacal de [Signo] está activo. Usalo antes de que termine: [link]" |

### Comm 3
| Field | Value |
|-------|-------|
| **ID** | PERS-ZODIAC-C3 |
| **Timing** | Day 5 of zodiac month |
| **Channel** | SMS |
| **Copy (ES)** | "CuatroBet: Último chance para tu bono zodiacal. Vence en 2 días: [link]" |

### Comm 4
| Field | Value |
|-------|-------|
| **ID** | PERS-ZODIAC-C4 |
| **Timing** | Last day of zodiac period |
| **Channel** | Email |
| **Copy** | Final reminder + teaser for next zodiac sign |
| **Exit** | Return to regular lifecycle |
