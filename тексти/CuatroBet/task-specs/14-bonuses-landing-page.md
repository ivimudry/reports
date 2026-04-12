# 14 — Bonuses Landing Page Redesign

**Purpose:** Fix structural issues, add lifecycle personalization

---

## Current Issues

| Problem | Detail |
|---------|--------|
| Lucky Wheel countdown | Shows "357D LEFT" — nearly a year, not urgency, decoration. Makes page feel stale. |
| Sports Welcome Bonus | Prominently displayed despite 99.9% casino players. Wasted real estate. |
| Duplicate welcome cards | 2 near-identical Slots/Live cards (150% + 60 FS, 150%). Cannibalizes attention. |
| No personalization | Every player sees same 4 cards regardless of lifecycle stage. |
| No hierarchy | Lucky Wheel visually equal to Welcome bonuses. |

---

## Redesigned Layout by Lifecycle

### Pre-FTD Player
| Position | Card | Details |
|----------|------|---------|
| **Hero (large, top)** | Welcome Bonus 120% + 50 FS | Gates of Olympus. Clear CTA: "Depositar ahora" |
| Supporting 1 | Lucky Wheel | Genuine countdown to next draw, not 357 days |
| Supporting 2 | Top games preview | 3 featured slots from top 10 |
| Supporting 3 | "How to deposit in 2 min" | Walkthrough |
| **Hidden** | All reload offers, VIP content | Not shown to pre-FTD |

### Post-FTD Player (within Day 1 Layer)
| Position | Card |
|----------|------|
| **Hero** | Second deposit 75% + 30 FS (matching first-session game) |
| Supporting | FS remaining on welcome, Lucky Wheel, game recommendations |

### Regular Player
| Position | Card |
|----------|------|
| **Hero** | Current weekly reload offer (rotates by day) |
| Supporting | Active quests, Lucky Wheel, bonus shop featured items |

### Pre-VIP / VIP
| Position | Card |
|----------|------|
| **Hero** | Personal message from CRM owner, cashback status, exclusive offer |
| Supporting | VIP events, curated games, direct contact |

---

## Sports Card Handling

- Deprioritize sports in casino-default view
- Add filter tab at top: **All / Casino / Sports**
- Default to Casino
- Sports users find offers in Sports tab

## Lucky Wheel Fix

- Show time until **next scheduled draw** (daily for daily, weekly for weekly)
- If no current draw → hide card or show "Next Lucky Wheel: [date]" teaser
- NEVER show 357-day countdowns
