# 13 — Channel Strategy & Frequency Caps

**Purpose:** Rebalance channel mix — cool fatigued channels, activate dormant ones

---

## Current State vs Target

| Channel | Current State | Target (6 weeks) |
|---------|---------------|-------------------|
| **SMS** | Best performer (19.68% click, 98.42% delivery, ~1,200 daily). Under-used. | Primary channel. Scale to 2,500+ daily. |
| **Email** | Healthy (99.13% delivery, 22% open, 48% CTOR, -18% volume trend, ~1,150 daily) | Maintain. Stabilize volume decline. |
| **NC Feed** | Fatigued. 10× volume increase (2K→25.7K daily). Open rate crashed (32–40% → 11%). | Cut 60%. Max 10K daily. |
| **NC Pop-Up** | Worse. 2.76% show rate, 2.37% open, 1.57% click. | Investigate, strict cap, high-value only. |
| **App Push** | Dormant. Zero sends. | Activate. Target 40%+ opt-in. |
| **Web Push** | Negligible volume. | Low priority. |

---

## Frequency Caps (across all channels combined)

| Segment | Max messages/day | Notes |
|---------|------------------|-------|
| Pre-FTD | 2 | Don't overwhelm new registrations |
| Day 1 Layer (first 72h) | 3 | Higher cadence justified by urgency |
| Regular | 2 | Standard cap |
| Pre-VIP / VIP | 2 | Quality over quantity |
| Reactivation | 1 | Single strongest message |
| **Transactional / security** | Exempt | Not subject to caps |

---

## NC Feed Cooling Plan

| Action | Detail |
|--------|--------|
| **Immediate** | Cut daily volume by 60% (25,700 → 10,000) |
| **Cap** | Max 2 NC Feed items per player per day, min 4h between items |
| **Targeting** | Restrict to active players only (opened app in last 48h) |
| **Content** | Personalize by lifecycle stage |
| **Recovery monitor** | Weekly open rate check. Do NOT scale back up until open rate ≥ 20% |

## NC Pop-Up Cooling Plan

| Action | Detail |
|--------|--------|
| **Investigate** | 2.76% show rate — targeting or trigger issue? Escalate to GR8 Tech. |
| **Cap** | Max 1 popup per player per session |
| **Session exclusion** | No popup in first 60 seconds of session |
| **Use cases** | High-value triggers ONLY: deposit failure, VIP invitation, churn intervention |
| **Stop** | Using as broadcast channel |

## App Push Activation (new channel)

| Week | Action |
|------|--------|
| 1 | Technical setup. Opt-in prompt on app open (post-FTD only). |
| 2 | Enable for Day 1 Retention Layer touches |
| 3 | Enable for Post-FTD and Pre-VIP journeys |
| 4 | Evaluate opt-in rate (target 40%+), open rate (target 15%+). Enable for Reactivation if healthy. |
| 5+ | General use within frequency caps |

**Opt-in incentive:** 100 CC on opt-in.  
**Quiet hours:** No pushes 00:00–08:00 ART.

## Kill Switch

> If any channel's open rate drops >25% week-over-week → pause new campaigns on that channel and investigate before scaling back up.
