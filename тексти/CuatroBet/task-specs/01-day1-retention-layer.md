# 01 — Day 1 Retention Layer

**Priority:** 🔴 Highest  
**Purpose:** Keep first-action players alive through the first 72 hours after FTD  
**Entry Trigger:** Real-time FTD success event from GR8 Tech platform  
**Branching:** At T+1h → Slots path (95%) or Aviator path (5%)  
**Runs in parallel with:** Welcome Bonus Ladder (ladder triggers on deposit; Day 1 Layer on time/behaviour)

---

## SLOTS PATH (default, ~95% of players)

### Touch 1 — FTD Instant Grant
| Field | Value |
|-------|-------|
| **ID** | D1-SLOTS-01 |
| **Timing** | T+0 (FTD success) |
| **Channel** | System (automatic grant) |
| **Trigger** | FTD deposit confirmed |
| **Segment** | All FTD players (Slots path) |
| **Action** | Grant 50 no-deposit free spins on Gates of Olympus (or player's first-session game if different) |
| **Offer** | 50 FS, expires in 24h, wagering 20× on winnings |
| **Copy** | — (system action, no message) |
| **CTA** | — |
| **Exit** | None — continues to next touch |
| **Notes** | If first-session game ≠ Gates of Olympus, FS go to that game instead |

---

### Touch 2 — In-Session Celebration Popup
| Field | Value |
|-------|-------|
| **ID** | D1-SLOTS-02 |
| **Timing** | T+5 min |
| **Channel** | Native in-app popup |
| **Trigger** | 5 min after FTD confirmed, player still in session |
| **Segment** | All FTD players (Slots path), in-session |
| **Action** | Display celebration popup |
| **Offer** | Awareness of 120% welcome bonus + 50 FS already granted |
| **Copy (ES)** | "¡Bienvenido! Tu bono 120% ya está activo. Extra: 50 giros gratis en Gates of Olympus para empezar" |
| **CTA** | "Jugar ahora" → deep-link to Gates of Olympus (or first-session game) |
| **Exit** | Player plays → continues |
| **Notes** | Must render within 5 min. Sub-second trigger latency required. |

---

### Decision Point — T+30 min
| Field | Value |
|-------|-------|
| **Timing** | T+30 min |
| **Condition** | Is the player still in session? |
| **Yes →** | Continue to Touch 3 (T+1h AI recommendation) |
| **No →** | Skip to Touch 4 (T+2h SMS exit push) |

---

### Touch 3 — AI Game Recommendation
| Field | Value |
|-------|-------|
| **ID** | D1-SLOTS-03 |
| **Timing** | T+1 h |
| **Channel** | In-session widget |
| **Trigger** | 1h after FTD, player still in session |
| **Segment** | Slots path players who are still in session at T+30min |
| **Action** | Show personalized game recommendation widget |
| **Offer** | No bonus — pure engagement |
| **Content** | 3 similar slots based on first-session game (via GR8 Tech AI recommendations module) |
| **CTA** | Click to open recommended game |
| **Exit** | Player opens recommended game → continues |
| **Notes** | GR8 Tech AI recommendations module already in use. Leverage existing infrastructure. |

---

### Touch 4 — Session Exit SMS
| Field | Value |
|-------|-------|
| **ID** | D1-SLOTS-04 |
| **Timing** | T+2 h (if session ended) |
| **Channel** | SMS |
| **Trigger** | Player left session AND 2h elapsed since FTD |
| **Segment** | Slots path players whose session ended before T+2h |
| **Action** | Send urgency SMS about expiring free spins |
| **Offer** | Reminder of the 50 FS (from Touch 1), expiring in ~22h |
| **Copy (ES)** | "CuatroBet: Tus 50 giros gratis en Gates of Olympus vencen en 22h. Seguir jugando: [link]" |
| **CTA** | Link to game lobby / Gates of Olympus |
| **Exit** | Player returns → continues |
| **Notes** | 160 chars max. Personalize game name if first-session game differs. |

---

### Decision Point — T+6 h
| Field | Value |
|-------|-------|
| **Timing** | T+6 h |
| **Condition** | Has the player returned to the app since last session? |
| **Yes →** | Touch 5A — Engagement Reward (popup) |
| **No →** | Touch 5B — Urgency SMS |

---

### Touch 5A — Engagement Reward (player returned)
| Field | Value |
|-------|-------|
| **ID** | D1-SLOTS-05A |
| **Timing** | T+6 h |
| **Channel** | In-session popup |
| **Trigger** | Player returned to app AND 6h elapsed since FTD |
| **Segment** | Slots path players who returned before T+6h |
| **Action** | Reward with CC for returning |
| **Offer** | 100 CC (Cuatro Coins), no-deposit gift, no wagering |
| **Copy (ES)** | "¡Gracias por volver! Regalo extra: 100 CC gratis + progreso hacia tu primer nivel de lealtad" |
| **CTA** | Dismiss / "Ver mi progreso" |
| **Exit** | Continues to T+24h decision |
| **Notes** | 100 CC = loyalty currency. Introduces player to CC economy early. |

---

### Touch 5B — Urgency SMS (player did NOT return)
| Field | Value |
|-------|-------|
| **ID** | D1-SLOTS-05B |
| **Timing** | T+6 h |
| **Channel** | SMS |
| **Trigger** | Player has NOT returned to app AND 6h elapsed since FTD |
| **Segment** | Slots path players who have not returned by T+6h |
| **Action** | Urgency deposit incentive |
| **Offer** | 1,000 ARS no-deposit bonus on any deposit within 6 hours, wagering 15× |
| **Copy (ES)** | "CuatroBet: Tus giros vencen pronto. Además, te regalamos 1,000 ARS extra si depositás en las próximas 6 horas: [link]" |
| **CTA** | Deep link to cashier |
| **Exit** | Continues to T+24h decision |
| **Notes** | Time-limited (6h validity on the 1,000 ARS bonus). Creates urgency. |

---

### Decision Point — T+24 h
| Field | Value |
|-------|-------|
| **Timing** | T+24 h |
| **Condition** | Has the player returned at any point in the first 24h? |
| **Yes →** | EXIT → standard Post-FTD cadence (player likely to STD organically) |
| **No →** | Touch 6 — Email Reload Offer |

---

### Touch 6 — Email Reload Offer (24h inactive)
| Field | Value |
|-------|-------|
| **ID** | D1-SLOTS-06 |
| **Timing** | T+24 h |
| **Channel** | Email |
| **Trigger** | Player has NOT returned in first 24h after FTD |
| **Segment** | Slots path players inactive for 24h |
| **Action** | Send email with strong reload offer |
| **Offer** | 75% match up to 3,000 ARS + 20 FS on Joker's Jewels, wagering 25×, expires in 48h |
| **Subject (ES)** | "Tu bono de 75% + 20 giros te esperan" |
| **Body** | — (design template needed) |
| **CTA** | "Depositar ahora" → cashier deep link |
| **Exit** | Deposit → Post-FTD cadence |
| **Notes** | Joker's Jewels is #2 in top 10. 48h validity creates urgency. |

---

### Decision Point — T+48 h
| Field | Value |
|-------|-------|
| **Timing** | T+48 h |
| **Condition** | Is the player still inactive (no return since FTD)? |
| **Yes →** | Touch 7 — Final SMS |
| **No →** | EXIT → Post-FTD cadence |

---

### Touch 7 — Final Touch SMS (48h inactive)
| Field | Value |
|-------|-------|
| **ID** | D1-SLOTS-07 |
| **Timing** | T+48 h |
| **Channel** | SMS |
| **Trigger** | Player still inactive 48h after FTD |
| **Segment** | Slots path players inactive for 48h |
| **Action** | Last-chance engagement with cross-game free bet |
| **Offer** | 500 ARS no-deposit free bet on Aviator, wagering 1×, valid 24h |
| **Copy (ES)** | "CuatroBet: Un regalo de despedida. 500 ARS free bet en Aviator, sin depósito. Válido 24h: [link]" |
| **CTA** | Deep link to Aviator |
| **Exit** | Activity → Post-FTD cadence; No activity → T+72h decision |
| **Notes** | Aviator is quick-play, hooks players on the fence. Wagering 1× = almost no barrier. Cheap habit-seed. |

---

### Decision Point — T+72 h (final)
| Field | Value |
|-------|-------|
| **Timing** | T+72 h |
| **Condition** | Has the player returned at any point in the 72h window? |
| **Yes →** | EXIT → Post-FTD to STD lifecycle |
| **No →** | EXIT → Reactivation Ladder (Early Churn cohort, enters at Day 3 instead of usual Day 7) |

---

## AVIATOR PATH (~5% of players)

**Entry:** Player whose first session game was Aviator or another crash game.

### Touch 1 — FTD Instant Grant (Aviator)
| Field | Value |
|-------|-------|
| **ID** | D1-AVI-01 |
| **Timing** | T+0 (FTD success) |
| **Channel** | System (automatic grant) |
| **Action** | Grant 5 Free Flights on Aviator |
| **Offer** | 5 Free Flights, expires in 24h |
| **Notes** | "Free Flights" = Aviator equivalent of free spins |

---

### Touch 2 — In-Session Celebration Popup (Aviator)
| Field | Value |
|-------|-------|
| **ID** | D1-AVI-02 |
| **Timing** | T+5 min |
| **Channel** | Native in-app popup |
| **Copy (ES)** | "¡Bienvenido! Tus 5 Free Flights en Aviator están listos" |
| **CTA** | "Jugar ahora" → deep-link to Aviator |

---

### Touch 3 — AI Game Recommendation (Aviator)
| Field | Value |
|-------|-------|
| **ID** | D1-AVI-03 |
| **Timing** | T+1 h |
| **Channel** | In-session widget |
| **Content** | Other crash and instant games (not slots) |

---

### Touch 4–5 — Same structure as Slots path
SMS at T+2h, decision at T+6h, Comm A / Comm B — **same structure, Aviator-themed copy**.

---

### Touch 6 — Email Reload Offer (Aviator, 24h inactive)
| Field | Value |
|-------|-------|
| **ID** | D1-AVI-06 |
| **Timing** | T+24 h |
| **Channel** | Email |
| **Offer** | 75% match + 10 Free Flights on Aviator, wagering 15× (lower because Aviator crash contribution is higher) |
| **Validity** | 48h |

---

### Touch 7 — Final SMS (Aviator, 48h inactive)
| Field | Value |
|-------|-------|
| **ID** | D1-AVI-07 |
| **Timing** | T+48 h |
| **Channel** | SMS |
| **Offer** | 500 ARS free bet on Aviator (same as Slots path) |

---

### Decision Points — same as Slots path (T+30min, T+6h, T+24h, T+48h, T+72h)

---

## Cost Model
| Item | Value |
|------|-------|
| Average FTD | 1,800 ARS |
| Layer cost per player | ~22% of first deposit |
| Funded from | Existing bonus budget (savings from lower wagering + NC Feed reduction) |

## KPI Targets
| Metric | Baseline | Target |
|--------|----------|--------|
| Day 1 Retention | 27.8% | 38–42% (+35–50% relative) |
| STD Conversion | 9.20% | 12–14% |
| Bonus Cost % GGR | +~2% contribution | Toward 20% target |
| Channel load | — | SMS doubles, NC Feed drops >50% |

## Implementation Dependencies
1. Real-time FTD event trigger from GR8 Tech (must fire within 5 min)
2. In-session popup requires sub-second trigger latency
3. App Push must be activated before launch (loses ~30% of T+6h branch without it)
4. Aviator path depends on first-session game detection (platform must expose first-game-played event)
5. Test wagering contribution for Aviator crash games (15× assumes 100% Aviator contribution)
