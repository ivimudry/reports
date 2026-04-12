# 11 — Loyalization

**Purpose:** Keep loyalty program members engaged (Active) or re-engage them (Passive)  
**Segments:**
- Active: completed ≥1 mission in last 7 days
- Passive: enrolled but 0 missions in 7+ days, still within 30 days of last activity
- **Sub-segments (both):** Slots-heavy, Live-heavy, Aviator, Mixed

---

## Active Loyalty Members

**Segment:** Players enrolled in loyalty program, completed ≥1 mission in last 7 days.

### Comm 1 — Weekly Progress & Mission Push
| Field | Value |
|-------|-------|
| **ID** | LOY-ACT-C1 |
| **Timing** | Weekly (Monday) |
| **Channel** | Email |
| **Subject (ES)** | "Tu progreso de lealtad esta semana" |
| **Copy** | Weekly summary: CC earned, missions completed, distance to next tier, new missions available |
| **Offer** | New weekly missions (tailored by sub-segment: Slots/Live/Aviator/Mixed) |
| **CTA** | "Ver misiones" |

### Comm 2 — Mid-Week Engagement
| Field | Value |
|-------|-------|
| **ID** | LOY-ACT-C2 |
| **Timing** | Wednesday |
| **Channel** | App Push |
| **Copy (ES)** | "Completaste [X] misiones. ¡[Y] más y subís de nivel!" |
| **CTA** | Deep link to missions |
| **Notes** | Content tailored to sub-segment game preference |

### Comm 3 — Weekend Challenge
| Field | Value |
|-------|-------|
| **ID** | LOY-ACT-C3 |
| **Timing** | Friday |
| **Channel** | SMS |
| **Copy (ES)** | "CuatroBet: Desafío de fin de semana. Completá 2 misiones más y ganá [bonus]: [link]" |
| **Offer** | Weekend mission bonus (e.g., 2× CC on weekend missions) |
| **CTA** | Missions link |

### Comm 4 — Tier Progress Celebration
| Field | Value |
|-------|-------|
| **ID** | LOY-ACT-C4 |
| **Timing** | On tier milestone (10/25/50/75/90% of next tier) |
| **Channel** | In-app popup |
| **Copy (ES)** | "¡[X]% del camino hacia [Next Tier]! Seguí así." |
| **Offer** | Small CC bonus at certain milestones (50%, 75%) |
| **CTA** | "Seguir jugando" |

---

### Active Sub-Segment Tailoring

| Sub-Segment | Game Highlight | FS Alignment | Missions Example |
|-------------|---------------|--------------|------------------|
| **Slots-heavy** | Top 10 slots | Gates of Olympus, Jackpot Joker | "Play 50 rounds on any slot" |
| **Live-heavy** | Turkish Live Roulette | — (bonus cash instead) | "Place 20 live bets" |
| **Aviator** | Aviator / crash games | Free Flights | "Reach 5× multiplier 3 times" |
| **Mixed** | Rotating | Mixed FS + bonus cash | "Play 3 different game types" |

---

## Passive Loyalty Members

**Segment:** Enrolled in loyalty, 0 missions completed in 7+ days, still within 30 days of last activity.

### Comm 1 — Re-Engagement Nudge
| Field | Value |
|-------|-------|
| **ID** | LOY-PAS-C1 |
| **Timing** | Day 7 of inactivity |
| **Channel** | Email |
| **Subject (ES)** | "Tus misiones de lealtad te extrañan" |
| **Copy** | Show uncompleted missions, CC balance, distance to next tier. "If you don't act, progress stalls." |
| **Offer** | Complete 1 mission this week and get 2× CC reward |
| **CTA** | "Volver a misiones" |

### Comm 2 — Easy Mission Push
| Field | Value |
|-------|-------|
| **ID** | LOY-PAS-C2 |
| **Timing** | Day 10 |
| **Channel** | App Push + SMS |
| **Copy (ES)** | "Misión fácil: jugá 10 rondas en [favorite game] y ganá [CC]. Solo hoy: [link]" |
| **Offer** | Easy mission with low barrier + bonus CC |
| **CTA** | Game deep link |
| **Notes** | Personalize game to sub-segment preference |

### Comm 3 — CC Expiry Warning
| Field | Value |
|-------|-------|
| **ID** | LOY-PAS-C3 |
| **Timing** | Day 14 |
| **Channel** | Email |
| **Subject (ES)** | "Tus CC están a punto de expirar" |
| **Copy** | CC balance, 90-day inactivity expiry warning, suggest Bonus Shop items to spend CC on |
| **Offer** | "Gastá tus CC en la Tienda de Bonos antes de que expiren" |
| **CTA** | "Ir a la Tienda" |

### Comm 4 — Last Chance
| Field | Value |
|-------|-------|
| **ID** | LOY-PAS-C4 |
| **Timing** | Day 21 |
| **Channel** | SMS |
| **Copy (ES)** | "CuatroBet: Completá 1 misión y conservá tu progreso de lealtad: [link]" |
| **Offer** | Complete any 1 mission to reset inactivity timer |
| **CTA** | Missions link |

**Exit:** Mission completed → back to Active. No response by Day 30 → Reactivation Matrix.

---

### Passive Sub-Segment Tailoring

Same 4 sub-segments as Active (Slots-heavy, Live-heavy, Aviator, Mixed) with content tailored accordingly.
