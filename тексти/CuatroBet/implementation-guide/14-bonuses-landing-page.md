# 14 — Bonuses Landing Page Redesign — Implementation Guide

**Chain:** Landing Page Personalization (Lifecycle-based card layout + fixes)  
**Priority:** Phase 1 (Week 2–3)  
**Type:** UI/UX change, not a CRM journey  

---

## STEP 0: PRE-FLIGHT CHECKLIST

- [ ] Access to GR8 Tech CMS or landing page builder
- [ ] Player lifecycle stage attribute available for page personalization
- [ ] Dynamic content rendering capability (show/hide cards by segment)
- [ ] Lucky Wheel draw schedule configured (daily/weekly)
- [ ] Game recommendation API available (or manual top-10 list)
- [ ] Analytics tracking on card impressions, clicks, conversions

---

## A. FIX CRITICAL ISSUES (Before Redesign)

### Fix 1: Lucky Wheel Countdown

| Problem | "357D LEFT" — nearly a year. No urgency. Page feels stale. |
|---------|-----|
| Solution | Replace with countdown to **next scheduled draw** |
| Logic | `IF draw_scheduled → show "Próximo sorteo en {hours}h {minutes}m"` <br> `IF no_draw_scheduled → show "Próximo Lucky Wheel: {date}" teaser` |
| **NEVER** | Display a countdown > 7 days. If timer > 7d, hide the card. |

### Fix 2: Sports Welcome Bonus

| Problem | Prominently displayed. 99.9% are casino players. Wasted space. |
|---------|-----|
| Solution | Add filter tabs at top: **Todo / Casino / Deportes** |
| Default | Casino tab selected |
| Sports card | Only visible in Deportes tab |
| Exceptions | If `player.game_preference = "Sports"` → default to Deportes tab |

### Fix 3: Duplicate Welcome Cards

| Problem | 2 near-identical Slots/Live cards (150% + 60 FS vs 150%). Cannibalizes. |
|---------|-----|
| Solution | Merge into **one** hero card: `120% + 50 FS` (aligned with Chain 05 ladder) |
| Show | Single card with clear CTA |
| If player has used welcome bonus | Hide card entirely, replace with reload offer |

### Fix 4: No Visual Hierarchy

| Problem | Lucky Wheel visually equal to Welcome bonuses |
|---------|-----|
| Solution | Hero card (large, top) + supporting cards (smaller, below) |
| Layout | 1 hero (full-width) + 2–3 supporting (half-width grid) |

---

## B. LIFECYCLE-PERSONALIZED LAYOUTS

### Layout 1: Pre-FTD Player

**Segment:** `lifecycle_stage = "Registered" OR "Activated"`

| Position | Card | Content (ES) | CTA |
|----------|------|-------------|-----|
| **Hero** (full-width) | Welcome Bonus | `Bono de bienvenida: 120% + 50 giros gratis en Gates of Olympus` | `Depositar ahora` → Cashier |
| Supporting 1 | Lucky Wheel | `Próximo sorteo en {countdown}. Depositá para participar.` | `Ver premios` → Wheel page |
| Supporting 2 | Top Games Preview | 3 featured slots from top 10 (images + names) | `Jugar gratis` → Demo mode |
| Supporting 3 | How-To Guide | `Cómo depositar en 2 minutos` (step-by-step visual) | `Depositar` → Cashier |
| **Hidden** | Reload offers, VIP content, Bonus Shop, Quests | — | — |

---

### Layout 2: Day 1 Layer (Post-FTD, first 72h)

**Segment:** `lifecycle_stage = "FTD" OR "Day_1_3"`

| Position | Card | Content (ES) | CTA |
|----------|------|-------------|-----|
| **Hero** | Second Deposit Offer | `Tu segundo depósito: 75% + 30 giros en {first_session_game}` | `Depositar` → Cashier |
| Supporting 1 | Welcome FS Remaining | `Te quedan {remaining_fs} giros gratis. Usalos ahora.` | `Jugar` → Slot page |
| Supporting 2 | Lucky Wheel | Real countdown | `Girar` → Wheel |
| Supporting 3 | Game Recommendations | Based on first session behavior | `Probar` → Game |

---

### Layout 3: Regular Player

**Segment:** `lifecycle_stage = "Regular"`

| Position | Card | Content (ES) | CTA |
|----------|------|-------------|-----|
| **Hero** | Weekly Reload (rotates) | `Recarga semanal: {offer_pct}% + {fs_count} giros. Válido hasta domingo.` | `Activar` → Deposit |
| Supporting 1 | Active Quests | `Misión activa: {quest_name}. Progreso: {progress}%` | `Ver misión` → Quest page |
| Supporting 2 | Lucky Wheel | Real countdown | `Girar` |
| Supporting 3 | Bonus Shop Featured | Top 2 items by redemption | `Ver tienda` → Shop |

---

### Layout 4: Pre-VIP / VIP

**Segment:** `lifecycle_stage IN ("Pre-VIP", "VIP_I", "VIP_II", "VIP_III", "VIP_IV")`

| Position | Card | Content (ES) | CTA |
|----------|------|-------------|-----|
| **Hero** | Personal Message | `{crm_owner_name}: {personalized_message}. Tu cashback esta semana: {cashback_amount} ARS.` | `Ver mi cuenta VIP` |
| Supporting 1 | Exclusive Offer | VIP-only offer (rotates weekly) | `Activar` |
| Supporting 2 | VIP Events | Upcoming tournaments, exclusive draws | `Ver eventos` |
| Supporting 3 | Curated Games | AI-picked based on play history | `Jugar` |
| **Hidden** | Standard welcome/reload offers | — | — |

---

## C. CARD COMPONENT SPECIFICATIONS

### Hero Card
```
Width: 100%
Height: 280px
Background: Gradient or game-specific banner image
Title: Bold, 24px, white
Subtitle: 16px, white 80% opacity
CTA Button: Primary brand color, 14px bold uppercase
Countdown (if applicable): Live timer, 18px monospace
```

### Supporting Card
```
Width: 48% (2-column grid with 4% gap)
Height: 160px
Background: Dark card, brand accent border
Title: 16px bold
Description: 13px, 2 lines max
CTA: Secondary button or text link
```

---

## D. ANALYTICS TRACKING

| Event | When | Data |
|-------|------|------|
| `card_impression` | Card visible in viewport | `card_id`, `lifecycle_stage`, `position` |
| `card_click` | Player clicks CTA | `card_id`, `lifecycle_stage`, `cta_text` |
| `card_conversion` | Player completes action (deposit, play, etc.) | `card_id`, `lifecycle_stage`, `conversion_value` |

**Weekly Report:**
- Card CTR by lifecycle stage
- Hero card conversion rate
- Tab filter usage (Casino vs Sports)
- Lucky Wheel engagement rate (before/after fix)

---

## TESTING CHECKLIST

- [ ] Pre-FTD player sees welcome hero, NOT reload offers
- [ ] Day 1 player sees second-deposit hero with correct game
- [ ] Regular player sees weekly reload hero
- [ ] VIP player sees personalized message hero
- [ ] Lucky Wheel shows real countdown (not 357 days)
- [ ] Lucky Wheel card hides if no draw within 7 days
- [ ] Sports card only visible in Deportes tab
- [ ] Casino tab is default for all non-sports players
- [ ] Duplicate welcome cards merged into single card
- [ ] Hero/supporting visual hierarchy clear
- [ ] Cards track impressions and clicks
- [ ] Mobile responsive (cards stack vertically)
- [ ] No layout shift on tab switch

---

## KPI TARGETS

| Metric | Current | Target (4 weeks) |
|--------|---------|-------------------|
| Hero card CTR | N/A (no hero) | ≥ 8% |
| Welcome bonus conversion (Pre-FTD) | Unknown | ≥ 15% |
| Lucky Wheel engagement | Low (stale countdown) | 2× current |
| Sports tab usage | N/A | Track baseline |
| Page bounce rate | High (implied) | -30% |
