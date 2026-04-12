# 13 — Channel Strategy & Frequency Caps — Implementation Guide

**Chain:** Channel Rebalancing (NC Feed cooling, Pop-Up cooling, App Push activation, Frequency Caps)  
**Priority:** Phase 0 (Week 1 — do first, affects ALL chains)  
**This is infrastructure, not a journey. Implement before launching any campaign chain.**

---

## STEP 0: PRE-FLIGHT CHECKLIST

- [ ] Access to GR8 Tech channel management console
- [ ] Current daily volume metrics for each channel (baseline)
- [ ] App Push SDK integrated (or confirm integration timeline)
- [ ] Frequency cap engine available in GR8 Tech (global + per-journey overrides)
- [ ] Quiet hours configuration available
- [ ] Kill switch mechanism available (pause campaigns by channel)

---

## A. FREQUENCY CAP CONFIGURATION

### Step 1: Set Global Caps

In GR8 Tech channel settings, configure the following **global** caps. These apply across ALL campaigns unless overridden.

| Segment | Max messages/day (all channels combined) | Notes |
|---------|------------------------------------------|-------|
| Pre-FTD | 2 | Protect from overwhelm |
| Day 1 Layer (first 72h post-FTD) | 3 | Higher cadence justified |
| Regular | 2 | Standard |
| Pre-VIP / VIP | 2 | Quality over quantity |
| Reactivation (dormant) | 1 | Single strongest message |
| **Transactional / Security** | **Exempt** | Password reset, KYC, withdrawal confirm |

### Step 2: Set Per-Channel Caps

| Channel | Max per player per day | Min gap between sends |
|---------|------------------------|----------------------|
| SMS | 1 | 6h |
| Email | 2 | 4h |
| NC Feed | 2 | 4h |
| NC Pop-Up | 1 per session | Not in first 60s of session |
| App Push | 2 | 3h |
| Web Push | 1 | 8h |

### Step 3: Set Journey-Level Overrides

Some journeys need exceptions:

| Journey | Override | Reason |
|---------|----------|--------|
| Chain 10 (Quests/Gamification) | Exempt from daily cap | Engagement features, not marketing |
| Chain 04 (Payment Failure) | +1 to daily cap | Time-sensitive recovery |
| Chain 03 (KYC) | SMS exempt from gap rule | Verification OTP is transactional |
| Chain 12 (Reactivation) | Max 3/week total | Spread across week, not day |

---

## B. NC FEED COOLING PLAN

### Step 1: Cut Volume (Immediate)

| Action | Before | After |
|--------|--------|-------|
| Daily volume (all players) | ~25,700 | ≤10,000 |
| Reduction | — | **60%** |

**How to cut:**
1. Identify ALL active NC Feed campaigns in GR8 Tech
2. Disable broadcast/batch NC Feed campaigns (keep only triggered)
3. Add segment filter to remaining: `last_app_open ≤ 48h`
4. Set global NC Feed cap: 2 items per player per day, min 4h gap

### Step 2: Content Quality Filter

Only these use cases remain on NC Feed:
- Triggered by player action (deposit, game milestone, quest progress)
- Lifecycle-specific content (personalized, not broadcast)
- Lucky Wheel draw result
- Bonus expiry reminders

**Remove from NC Feed:**
- Generic promotions
- Broadcast announcements
- Cross-sell / upsell pushes
- Anything that was previously on email

### Step 3: Recovery Monitor

| Week | Check | Action |
|------|-------|--------|
| W1 | Baseline open rate (currently ~11%) | Record |
| W2 | Open rate after cooling | If ≥15%, hold. If <11%, investigate content. |
| W3 | Continue monitoring | — |
| W4 | Open rate target ≥20% | Only then consider selective scaling |
| W5+ | Gradual scale if healthy | Max +1,000/week, monitor weekly |

**DO NOT scale back up until open rate ≥ 20%.**

---

## C. NC POP-UP COOLING PLAN

### Step 1: Investigate Show Rate

Current show rate: 2.76% — this is abnormally low.

- [ ] Check: Are HTML pop-ups rendering on all device types?
- [ ] Check: Is the trigger firing correctly? (Log trigger vs show events)
- [ ] Check: Is ad-blocker or browser blocking popups?
- [ ] Escalate to GR8 Tech if trigger → show gap > 50%

### Step 2: Restrict to High-Value Triggers Only

| Allowed Pop-Up Use Cases | Example |
|--------------------------|---------|
| Deposit failure recovery | Chain 04: immediate 5-second popup |
| Churn intervention | Chain 12: high-value at-risk player |
| VIP tier upgrade celebration | Chain 11: tier milestone |
| First-time feature discovery | Day 1 Layer: first popup only |
| Quest completion celebration | Chain 10: quest reward popup |

**Remove from Pop-Up:**
- Generic promotions
- Loyalty reminders
- Broadcast content
- Anything that can go to NC Feed or Push instead

### Step 3: Session Rules

| Rule | Setting |
|------|---------|
| Max popups per session | 1 |
| Min time before first popup | 60 seconds after session start |
| Min time between popups (across sessions) | 4 hours |
| Do not show if player is mid-game | Wait for game exit |

---

## D. APP PUSH ACTIVATION (New Channel)

### Week 1: Technical Setup

| Task | Detail |
|------|--------|
| Confirm SDK integration | Firebase (Android) / APNs (iOS) |
| Set up opt-in prompt | Show after FTD only (not on registration) |
| Opt-in incentive | 100 CC credited immediately on opt-in |
| Opt-in message (ES) | `Activá notificaciones y recibí 100 Cuatro Coins gratis. Te avisamos de ofertas exclusivas.` |
| Quiet hours | 00:00–08:00 ART — no pushes |

### Week 2: Pilot — Day 1 Retention Layer

| Action | Detail |
|--------|--------|
| Enable push for | Chain 01 touches only |
| Monitor | Opt-in rate, delivery rate, open rate |
| Target | 40% opt-in, 15% open |

### Week 3: Expand — Post-FTD & Pre-VIP

| Action | Detail |
|--------|--------|
| Enable push for | Chain 02, Chain 05 |
| Monitor | Same metrics |

### Week 4: Evaluate & Decide

| Metric | Target | Action if below |
|--------|--------|----------------|
| Opt-in rate | ≥ 40% | Test different prompt timing/copy |
| Open rate | ≥ 15% | Reduce frequency, improve content |
| Unsubscribe rate | < 3% | Reduce frequency immediately |

### Week 5+: General Availability

If Week 4 targets met → enable App Push for all journey chains within frequency caps.

---

## E. SMS OPTIMIZATION

SMS is the best-performing channel (19.68% click rate). Scale carefully.

| Action | Detail |
|--------|--------|
| Current volume | ~1,200 daily |
| Target volume | 2,500+ daily (within 6 weeks) |
| Scale plan | +200/week, monitor click rate weekly |
| Content rules | Max 160 chars, always include {link}, always include brand name |
| Opt-in compliance | SMS only to players who opted in (KYC phone verification = opt-in for Chain 03) |
| Cost monitoring | Track cost per click weekly |

### SMS Content Templates

| Type | Template (ES) |
|------|---------------|
| Offer | `CuatroBet: {first_name}, {offer_description}. Válido {validity}. {link}` |
| Reminder | `CuatroBet: {first_name}, {reminder_text}. {link}` |
| Urgency | `CuatroBet: Última oportunidad: {offer}. Vence hoy. {link}` |
| Celebration | `CuatroBet: ¡Felicitaciones! {achievement}. {reward} acreditado.` |

---

## F. KILL SWITCH PROTOCOL

If any channel's **open rate drops ≥25% week-over-week:**

1. **Immediately** pause all non-triggered campaigns on that channel
2. **Investigate:** Volume spike? Content issue? Technical problem?
3. **Do not resume** until root cause identified and fixed
4. **Resume** at 50% of previous volume, monitor for 1 week
5. **Gradually** return to full volume only if metrics recover

| Channel | Current Open Rate | Kill Switch Trigger (25% drop) |
|---------|-------------------|-------------------------------|
| SMS | ~55% implied (19.68% click ÷ ~35% CTR) | < 41% open |
| Email | 22% | < 16.5% open |
| NC Feed | 11% | < 8.25% open |
| App Push | TBD | TBD after Week 2 baseline |

---

## IMPLEMENTATION ORDER

| Step | Action | Timeline |
|------|--------|----------|
| 1 | Configure global frequency caps | Day 1 |
| 2 | Configure per-channel caps | Day 1 |
| 3 | Cut NC Feed volume 60% | Day 1–2 |
| 4 | Restrict NC Pop-Up to high-value triggers | Day 1–2 |
| 5 | Investigate Pop-Up show rate issue | Day 2–3 |
| 6 | Begin App Push technical setup | Day 3 |
| 7 | Set SMS scaling plan | Day 3 |
| 8 | App Push opt-in prompt live | Week 2 |
| 9 | Monitor all channels weekly | Ongoing |
| 10 | Kill switch protocol documented & shared | Day 1 |

---

## TESTING CHECKLIST

- [ ] Global frequency cap enforced across all campaigns
- [ ] Per-channel caps respected (test with high-activity test player)
- [ ] NC Feed volume ≤ 10,000/day confirmed
- [ ] NC Feed only shows to players active in last 48h
- [ ] NC Pop-Up limited to 1 per session, not in first 60s
- [ ] App Push opt-in prompt appears only after FTD
- [ ] 100 CC credited on opt-in
- [ ] Quiet hours (00:00–08:00 ART) enforced for Push
- [ ] SMS contains link and brand name in every message
- [ ] Kill switch protocol tested (simulate 25% drop scenario)
- [ ] Journey-level overrides work (Chain 10 exempt, Chain 04 +1)
