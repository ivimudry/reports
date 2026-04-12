# 16 — Referral Program — Implementation Guide

**Chain:** Referral Mechanics (New feature — does not currently exist)  
**Priority:** Phase 4 (Week 9–10)  
**Type:** Product feature + CRM comms

---

## STEP 0: PRE-FLIGHT CHECKLIST

- [ ] Unique referral link/code generation API available in GR8 Tech
- [ ] Referral tracking: link click → registration → FTD → STD attribution
- [ ] Fraud detection: IP matching, device fingerprint, payment method dedup
- [ ] CC credit API for automated rewards
- [ ] Cash bonus credit API (manual or automated)
- [ ] Referral dashboard UI in player profile (or confirm build timeline)
- [ ] WhatsApp share, Instagram share, and copy-link buttons available
- [ ] KYC status check API (gate rewards above 1,000 ARS)

---

## A. REFERRAL MECHANICS

### How It Works

```
Referrer (existing player)          Referred (new player)
    │                                     │
    ├─ Gets unique link/code              │
    ├─ Shares via WhatsApp/IG/copy        │
    │                                     │
    │                    ┌────────────────┤
    │                    │ Registers with link
    │                    │ Gets enhanced welcome bonus
    │                    │ Makes FTD
    │                    │ Makes STD ←─── REWARD TRIGGER
    │                    └────────────────┘
    │
    ├─ Receives referral reward (cash + CC)
    └─ Progress toward tier milestone
```

**Why STD (Second Deposit) as trigger?**
- Protects against abuse (self-referral, bots)
- Aligns with actual value creation (player is engaged, not just testing)
- Reduces fraudulent sign-ups

---

## B. REWARD STRUCTURE

### Referrer Rewards (credited on referred player's STD)

| Reward Type | Amount | Conditions |
|-------------|--------|-----------|
| Cash bonus | **2,000 ARS** per successful referral | Auto-credited, 10× wagering |
| CC bonus | **500 CC** per referral | Instant credit |
| Tier milestone | **5 referrals** → 10,000 ARS + VIP Lucky Wheel entry | Cumulative, lifetime |
| Monthly leaderboard | **Top 10** → additional 10,000 ARS cash prize | Reset monthly |

### Referred Player Rewards (on registration)

| Reward Type | Amount | Conditions |
|-------------|--------|-----------|
| Enhanced welcome bonus | **150% match** (instead of standard 120%) + **60 FS** | On FTD, 15× wagering |
| Registration gift | **500 ARS** no-deposit bonus | Instant, 20× wagering |
| Profile badge | "Invited by {referrer_name}" | Visible in profile |

---

## C. ANTI-ABUSE RULES — CONFIGURE IN GR8 TECH

| Rule | Implementation | Action on violation |
|------|---------------|-------------------|
| Self-referral | Block if IP OR device fingerprint OR payment method matches | Reject referral, no rewards |
| Same payment method | Referrer + referred cannot share payment method | Reject at STD validation |
| Referrer eligibility | Must have ≥3 lifetime deposits to generate code | Hide referral section if ineligible |
| Monthly cap | Max 10 successful referrals per referrer per month | Disable link after 10, show "Limit reached" |
| KYC gate | KYC fully verified required for cash rewards >1,000 ARS | Hold reward, prompt KYC completion |
| Velocity check | >5 referrals in 48h | Flag for manual review, hold rewards |

### Fraud Review Queue

When velocity check triggers:
1. Hold all pending referral rewards
2. Send internal alert to fraud team
3. Manual review within 24h
4. If legitimate → release rewards
5. If fraudulent → void all referral rewards, flag referrer account

---

## D. REFERRAL DASHBOARD (Player-Facing)

### Location: Player profile → "Referidos" tab

| Element | Content |
|---------|---------|
| Referral link | `https://cuatrobet.com/r/{code}` with Copy button |
| Share buttons | WhatsApp, Instagram, Copy Link |
| Stats | Total referred: {count} / Successful (STD): {count} / Earnings: {total_ars} ARS + {total_cc} CC |
| Pending | "Esperando segundo depósito: {pending_count}" |
| Leaderboard position | "Tu posición este mes: #{rank}" |
| Milestone progress | Progress bar: {count}/5 para 10,000 ARS + VIP Lucky Wheel |

### Share Templates

**WhatsApp (ES):**
```
¡Jugá en CuatroBet con mi link y recibí un bono de bienvenida de 150% + 60 giros gratis + 500 ARS de regalo! 🎰
{referral_link}
```

**Instagram Story (deep link):**
```
CuatroBet 🎰 Usá mi código y arrancá con 150% + 60 giros gratis
{referral_link}
```

---

## E. LAUNCH CAMPAIGN (4 Communications)

### REF-C1: Announcement to Entire Active Base

| Setting | Value |
|---------|-------|
| Campaign ID | `16-REF-C1-EMAIL` |
| Channel | Email |
| Trigger | One-time blast, Week 1 of launch |
| Segment | All players with ≥3 deposits (eligible referrers) |
| Subject (ES) | `🤝 2,000 ARS por cada amigo que invites` |

**Email Content:**
- **Subject (ES):** `🤝 2,000 ARS por cada amigo que invites`
- **Preheader (ES):** `Compartí tu link y empezá a ganar ya`
- **Banner Text (ES):** `Invitá Amigos = 2,000 ARS`
- **Banner Description:** Referral program launch — two people high-fiving, money/coins flowing between them, "2,000 ARS" large text, CuatroBet community vibe, vibrant green/gold celebration
- **Body Description:** New referral program intro: for each friend who registers + makes 2 deposits, earn 2,000 ARS cash + 500 CC. Milestone: 5 referrals = 10,000 ARS + VIP Lucky Wheel. Personal referral link. Share via WhatsApp/Instagram/copy.
- **CTA (ES):** `Compartir mi link` → Referral dashboard

---

### REF-C2: Early Bird Bonus (Launch Week)

| Setting | Value |
|---------|-------|
| Campaign ID | `16-REF-C2-EMAIL-SMS` |
| Channel | Email + SMS |
| Trigger | Day 2 of launch |
| Segment | Same as C1 |
| Subject (ES) | `🏁 1,000 ARS extra: los primeros 100 referidos` |

**Email Content:**
- **Subject (ES):** `🏁 1,000 ARS extra: los primeros 100 referidos`
- **Preheader (ES):** `Aprovechá la promo antes de que se acaben los cupos`
- **Banner Text (ES):** `¡Primeros 100 = 1,000 ARS Extra!`
- **Banner Description:** Early bird FOMO — countdown counter showing remaining spots out of 100, golden "exclusive" badge, money pile growing, urgency red/gold tones
- **Body Description:** Early bird launch bonus: first 100 successful referrals (across platform) get +1,000 ARS extra. Show remaining counter. Urgency: limited availability.

**SMS (ES):**
```
CuatroBet: Primeros 100 referidos con 2 depósitos = 1,000 ARS extra para el referidor. Compartí tu link: {link}
```

**Mechanic:** First 100 successful referrals (across all referrers) get +1,000 ARS bonus.  
**Counter:** Show "Quedan {remaining}/100 bonos extra" on referral page.

---

### REF-C3: Weekly Reminder (Ongoing)

| Setting | Value |
|---------|-------|
| Campaign ID | `16-REF-C3-EMAIL` |
| Channel | Email |
| Trigger | Scheduled, every Wednesday |
| Segment | Eligible referrers with ≥1 successful referral |
| Subject (ES) | `💸 {total_ars} ARS ganados por referidos este mes` |

**Email Content:**
- **Subject (ES):** `💸 {total_ars} ARS ganados por referidos este mes`
- **Preheader (ES):** `Tu resumen mensual y cómo ganar más`
- **Banner Text (ES):** `{total_ars} ARS Ganados Este Mes`
- **Banner Description:** Monthly earnings recap — money counter visual, referral count icons, "invite more" arrow, progress toward milestone, green success tones
- **Body Description:** Monthly referral earnings summary: total ARS + CC earned, pending referrals waiting for STD, referral count, CTA to share link again.

---

### REF-C4: Monthly Leaderboard (End of Month)

| Setting | Value |
|---------|-------|
| Campaign ID | `16-REF-C4-EMAIL` |
| Channel | Email |
| Trigger | Last day of month |
| Segment | All eligible referrers |
| Subject (ES) | `🏅 Ranking de referidos: ¿estás en el Top 10?` |

**Email Content:**
- **Subject (ES):** `🏅 Ranking de referidos: ¿estás en el Top 10?`
- **Preheader (ES):** `Mirá tu posición y los premios del mes`
- **Banner Text (ES):** `Ranking de Referidos — {month}`
- **Banner Description:** Leaderboard visual — podium with top 3, trophy icon, player's rank highlighted, 10,000 ARS prize for top 10, competitive dark/gold/red theme
- **Body Description:** Top 10 leaderboard table (rank, name, count). Player's own position highlighted. Prize: 10,000 ARS for top 10. Motivation to climb.

**Action for Top 10:** Auto-credit 10,000 ARS with `Leaderboard Prize` tag.

---

## F. REFERRAL LIFECYCLE FOR REFERRED PLAYER

After referred player registers, they enter standard lifecycle BUT with enhanced offers:

| Stage | Standard | Referral Enhanced |
|-------|----------|------------------|
| Welcome bonus | 120% + 50 FS | **150% + 60 FS** |
| Registration gift | None | **500 ARS no-deposit** |
| Day 1 Layer | Standard Chain 01 | Same Chain 01 + badge |
| Chain 05 ladder | Standard tiers | Same tiers |

**Important:** After FTD, referred players follow ALL standard chains. Enhancement is registration + FTD only.

---

## TESTING CHECKLIST

- [ ] Referral link generated with unique code per player
- [ ] Link only available to players with ≥3 deposits
- [ ] Registration via link correctly attributes to referrer
- [ ] Reward triggers on STD (not FTD)
- [ ] 2,000 ARS + 500 CC credited to referrer on trigger
- [ ] Referred player gets 150% + 60 FS + 500 ARS
- [ ] Self-referral blocked (IP, fingerprint, payment method)
- [ ] Monthly cap of 10 enforced (link disabled after 10)
- [ ] Velocity check triggers at >5 in 48h
- [ ] KYC gate holds rewards >1,000 ARS for unverified referrers
- [ ] WhatsApp share opens with pre-filled message
- [ ] Copy link works on all browsers
- [ ] Dashboard shows correct stats (total, successful, pending, earnings)
- [ ] Milestone progress bar updates correctly
- [ ] Leaderboard calculates correctly at month end
- [ ] Top 10 auto-credited with 10,000 ARS

---

## KPI TARGETS

| Metric | Target |
|--------|--------|
| Referral share of new registrations | 5–10% within 12 weeks |
| Referred player FTD rate | ≥ 60% (vs ~40% organic) |
| Referred player retention (30-day) | +20–30% vs paid acquisition |
| Average referrals per active referrer | 2–3 per month |
| Cost per acquired player (referral) | ≤ 3,000 ARS (cheaper than paid ads) |
| Prolific referrers identified as VIP candidates | Track top 20 |
