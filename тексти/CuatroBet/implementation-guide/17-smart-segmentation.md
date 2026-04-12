# 17 — Smart Segmentation Setup — Implementation Guide

**Chain:** 5-Axis Segmentation Model + Predictive Churn Activation  
**Priority:** Phase 0 (Week 1 — prerequisite for ALL other chains)  
**Type:** Infrastructure/data configuration, not a journey  
**This must be completed BEFORE launching any campaign chain.**

---

## STEP 0: PRE-FLIGHT CHECKLIST

- [ ] GR8 Tech Smart Segmentation module contract/license confirmed
- [ ] GR8 Tech Predictive Churn module contract/license confirmed
- [ ] Raw player-level data export access available
- [ ] Data warehouse or analytics layer accessible for validation
- [ ] GR8 Tech segmentation UI admin access
- [ ] Journey trigger system can read segment membership in real time
- [ ] At least 30 days of historical player data available for model training

---

## A. FIVE-AXIS MODEL OVERVIEW

Every player is classified on ALL 5 axes simultaneously. The combination of axes determines which journey they enter, what content they see, which channel is used, and how urgently.

```
┌─────────────────┐   ┌──────────────┐   ┌────────────────┐
│ Axis 1          │   │ Axis 2       │   │ Axis 3         │
│ LIFECYCLE STAGE │   │ VALUE TIER   │   │ GAME PREF      │
│ (which journey) │   │ (offer size) │   │ (content type) │
└────────┬────────┘   └──────┬───────┘   └───────┬────────┘
         │                   │                    │
         └──────────┬────────┘                    │
                    │                             │
              ┌─────┴──────┐              ┌───────┴────────┐
              │ Combined:   │              │ Axis 4         │
              │ Journey +   │              │ CHURN RISK     │
              │ Offer       │              │ (timing accel) │
              └─────┬──────┘              └───────┬────────┘
                    │                             │
                    └──────────┬──────────────────┘
                               │
                    ┌──────────┴──────────┐
                    │ Axis 5              │
                    │ KYC STATUS          │
                    │ (channel gate)      │
                    └─────────────────────┘
```

---

## B. AXIS 1: LIFECYCLE STAGE — BUILD RULES

**This axis drives WHICH journey the player enters.**

### Step 1: Create Segments in GR8 Tech

| Segment Name | Definition | Journey Mapping |
|-------------|-----------|-----------------|
| `LS_REGISTERED` | `has_account = true AND ftd_date IS NULL` | Pre-FTD comms only |
| `LS_ACTIVATED` | `has_account = true AND first_action_date IS NOT NULL AND ftd_date IS NULL` | Pre-FTD with nudges |
| `LS_FTD` | `ftd_date IS NOT NULL AND hours_since_ftd < 24` | Chain 01 (Day 1 Layer) |
| `LS_DAY_1_3` | `ftd_date IS NOT NULL AND hours_since_ftd BETWEEN 24 AND 72` | Chain 01 continued |
| `LS_PRE_STD` | `deposits_count = 1 AND hours_since_ftd > 72` | Chain 05 (Welcome Ladder) |
| `LS_REGULAR` | `deposits_count ≥ 2 AND last_login ≤ 14 days` | Chains 02, 07, 08, 09, 10, 11 |
| `LS_PRE_VIP` | `deposits_lifetime_ars BETWEEN 150000 AND 300000` | Chain 02 (Pre-VIP path) |
| `LS_VIP_I` | VIP tier I threshold (per GR8 Tech config) | VIP comms |
| `LS_VIP_II` | VIP tier II threshold | VIP comms |
| `LS_VIP_III` | VIP tier III threshold | VIP comms |
| `LS_VIP_IV` | VIP tier IV threshold | VIP comms |
| `LS_AT_RISK` | `churn_score ≥ 0.6 AND last_login ≤ 14 days` | Early reactivation trigger |
| `LS_DORMANT_7` | `last_login BETWEEN 7 AND 13 days ago` | Chain 12 (7-Day bucket) |
| `LS_DORMANT_14` | `last_login BETWEEN 14 AND 20 days ago` | Chain 12 (14-Day bucket) |
| `LS_DORMANT_21` | `last_login > 20 days ago` | Chain 12 (21+ Day bucket) |
| `LS_DORMANT_60` | `last_login > 60 days ago` | Suppressed (reactivation exhausted) |

### Step 2: Set Segment Priority

Players can technically match multiple lifecycle stages. Set priority order (highest wins):

1. `LS_VIP_*` (VIP always wins)
2. `LS_PRE_VIP`
3. `LS_FTD` / `LS_DAY_1_3` (time-critical)
4. `LS_AT_RISK`
5. `LS_DORMANT_*`
6. `LS_PRE_STD`
7. `LS_REGULAR`
8. `LS_ACTIVATED`
9. `LS_REGISTERED`

---

## C. AXIS 2: VALUE TIER — BUILD RULES

**This axis drives OFFER SIZE (multiplier on base offers).**

### Create Segments:

| Segment Name | Definition | Offer Multiplier |
|-------------|-----------|-----------------|
| `VT_MICRO` | `deposits_lifetime_ars < 5000` | 0.5× |
| `VT_LOW` | `deposits_lifetime_ars BETWEEN 5000 AND 25000` | 1× (base) |
| `VT_MID` | `deposits_lifetime_ars BETWEEN 25001 AND 75000` | 1.5× |
| `VT_HIGH` | `deposits_lifetime_ars BETWEEN 75001 AND 200000` | 2× |
| `VT_PRE_VIP_PLUS` | `deposits_lifetime_ars > 200000` | 3× (+ personal outreach) |

### How to Apply:

Every journey that sends a bonus/offer reads the player's value tier and applies the multiplier:

```
final_offer_value = base_offer × value_tier_multiplier
```

Example: Chain 12 base offer = 500 ARS no-deposit
- Micro player: 250 ARS
- Low player: 500 ARS
- Mid player: 750 ARS
- High player: 1,000 ARS
- Pre-VIP+: 1,500 ARS + personal call

**Important:** Wagering requirements do NOT scale. Only offer value scales.

---

## D. AXIS 3: GAME PREFERENCE — BUILD RULES

**This axis drives CONTENT (which games, FS, banners to show).**

### Create Segments:

| Segment Name | Definition | Content Mapping |
|-------------|-----------|----------------|
| `GP_SLOTS` | `slots_wagered / total_wagered > 0.7` | FS on top slot, slot banners, slot tournaments |
| `GP_AVIATOR` | `aviator_wagered / total_wagered > 0.3` | Free flights, crash game content |
| `GP_LIVE` | `live_wagered / total_wagered > 0.3` | Table game offers, live dealer content |
| `GP_MIXED` | None of above >0.7 or >0.3 | Varied content, "try something new" |

### Content Library (build for each preference):

| Preference | FS Game | Banner Theme | Tournament Type | Recommendation |
|-----------|---------|-------------|----------------|----------------|
| Slots | Jackpot Joker, Gates of Olympus | Colorful, jackpot imagery | Slot tournaments | Top 10 by engagement |
| Aviator | Free Flights | Sky, airplane, multiplier | Crash game leaderboard | Similar crash games |
| Live | — (use bonus cash) | Elegant, dealer imagery | Live table tournaments | Premium tables |
| Mixed | Random from top 10 | Varied | Cross-game challenges | Under-played categories |

---

## E. AXIS 4: CHURN RISK — BUILD RULES

**This axis ACCELERATES timing — sends comms earlier for at-risk players.**

### Create Segments:

| Segment Name | Score Range | Action |
|-------------|-----------|--------|
| `CR_HEALTHY` | churn_score < 0.30 | Normal timing |
| `CR_WATCH` | churn_score 0.30–0.60 | Send 1 day earlier than default |
| `CR_AT_RISK` | churn_score 0.60–0.85 | Send 2 days earlier; escalate offer by 1 tier |
| `CR_CRITICAL` | churn_score > 0.85 | Immediate intervention; alert VIP team for High+ value |

### Integration with Journeys:

```
IF player.churn_risk = "CR_AT_RISK" AND player.lifecycle = "LS_REGULAR":
  → Enter Chain 12 (Reactivation) at 7-Day bucket EARLY (day 3-4)
  → Tag: "churn_predicted_early_entry"

IF player.churn_risk = "CR_CRITICAL" AND player.value_tier IN ("VT_HIGH", "VT_PRE_VIP_PLUS"):
  → Immediate internal alert to VIP team
  → Skip automated chain, personal outreach within 24h
  → Tag: "churn_critical_vip_intervention"
```

### Predictive Churn Model Setup:

| Step | Action |
|------|--------|
| 1 | Contact GR8 Tech to enable Predictive Churn module |
| 2 | Provide 30+ days historical data (logins, deposits, gameplay, comms engagement) |
| 3 | GR8 Tech trains model on CuatroBet-specific data |
| 4 | Model outputs daily `churn_score` (0.0–1.0) per player |
| 5 | Validate: check if score >0.6 correctly predicts churn in next 14 days |
| 6 | If accuracy <70%, retrain with adjusted features |
| 7 | Connect churn_score to segment rules above |

---

## F. AXIS 5: KYC STATUS — BUILD RULES

**This axis GATES channel availability and certain actions.**

### Create Segments:

| Segment Name | Definition | Channel Access |
|-------------|-----------|---------------|
| `KYC_UNVERIFIED` | No verification steps completed | Email only + NC Feed |
| `KYC_PARTIAL` | Email verified + phone verified | Email + SMS + NC Feed + Push |
| `KYC_FULL` | Documents verified (ID, proof of address) | All channels + withdrawals |

### Channel Gating Rules:

| Channel | Requires |
|---------|----------|
| Email | `KYC_UNVERIFIED` or above (always available) |
| NC Feed | `KYC_UNVERIFIED` or above |
| NC Pop-Up | `KYC_UNVERIFIED` or above (in-app only) |
| SMS | `KYC_PARTIAL` or above (phone number required) |
| App Push | `KYC_UNVERIFIED` or above (device token, not KYC-dependent) |
| WhatsApp | `KYC_PARTIAL` or above |

### KYC → Chain 03 Integration:

If `KYC_UNVERIFIED` or `KYC_PARTIAL`:
- Player enters Chain 03 (KYC Completion Chain) automatically
- Chain 03 triggers escalate based on deposit thresholds (15K soft, 22.5K hard)

---

## G. COMBINED EXAMPLE

**Player Profile:**
```
Name: Juan
Lifecycle: LS_REGULAR (active, 5 deposits)
Value Tier: VT_MID (42,000 ARS lifetime)
Game Pref: GP_SLOTS (85% slots wagered)
Churn Risk: CR_WATCH (score 0.45)
KYC Status: KYC_FULL
```

**What happens:**
1. **Axis 1 (Lifecycle):** Juan is in Regular lifecycle → eligible for Chains 02, 07, 08, 09, 10, 11
2. **Axis 2 (Value):** Mid tier → all offers × 1.5 multiplier
3. **Axis 3 (Game Pref):** Slots → FS on Jackpot Joker, slot banners, slot tournament content
4. **Axis 4 (Churn Risk):** Watch → comms sent 1 day earlier than default schedule
5. **Axis 5 (KYC):** Full → all channels available (SMS, email, push, popup, etc.)

**Result:** Juan receives Chain 10 quest notifications with slot-specific challenges, offered 1.5× base FS amounts, sent 1 day earlier, via his preferred channel (determined by engagement history from Chain 13).

---

## H. VALIDATION PROTOCOL

### Step 1: Historical Backtest (Before Launch)

| Action | Detail |
|--------|--------|
| Export 1 week of player data | All 5 axis attributes for each player |
| Run classification | Apply segment rules to all players |
| Check distribution | No segment should have <1% or >60% of players |
| Check overlaps | Players should be in exactly 1 segment per axis |
| Spot check | Manually verify 50 random players against known profiles |

### Expected Distribution:

| Axis | Segment | Expected % |
|------|---------|-----------|
| Lifecycle | Registered | 15–25% |
| Lifecycle | Regular | 30–40% |
| Lifecycle | Dormant (all buckets) | 20–30% |
| Value | Micro + Low | 60–70% |
| Value | Mid | 15–20% |
| Value | High + Pre-VIP+ | 5–10% |
| Game Pref | Slots | 70–80% |
| Game Pref | Aviator | 5–10% |
| Churn | Healthy | 50–60% |
| Churn | At-Risk + Critical | 10–20% |
| KYC | Full | 30–40% (goal: increase) |

### Step 2: Live Validation (Week 1)

| Day | Action |
|-----|--------|
| Day 1 | Segments live. Spot check 20 players. |
| Day 2 | Check segment transition: did new FTD move from Registered → FTD? |
| Day 3 | Check churn score: does it update daily? |
| Day 5 | Full audit: all 5 axes for 100 random players |
| Day 7 | Sign-off: segments validated, ready for journey connections |

---

## TESTING CHECKLIST

- [ ] All 16 lifecycle segments created and populated
- [ ] 5 value tier segments created with correct ARS thresholds
- [ ] 4 game preference segments created with correct wager ratios
- [ ] 4 churn risk segments created with correct score thresholds
- [ ] 3 KYC status segments created
- [ ] Each player is in exactly 1 segment per axis
- [ ] Segment priority order enforced for lifecycle axis
- [ ] Value tier multiplier applied correctly in test journey
- [ ] Game preference drives correct content templates
- [ ] Churn risk accelerates timing (Watch = -1 day, At-Risk = -2 days)
- [ ] KYC gates channel access (SMS blocked for unverified)
- [ ] Predictive churn model outputs daily scores
- [ ] Churn score >0.6 in backtest predicted actual churn ≥70% accuracy
- [ ] VIP team alert fires for Critical + High Value
- [ ] Segments update in real time (not batch-only)
- [ ] Historical backtest distribution matches expected ranges

---

## ACTIVATION ORDER (Dependencies)

| Order | Action | Blocked By |
|-------|--------|-----------|
| **1** | Enable Smart Segmentation module | GR8 Tech contract |
| **2** | Enable Predictive Churn module | GR8 Tech contract |
| **3** | Build Axis 5 (KYC) segments | Data available now |
| **4** | Build Axis 1 (Lifecycle) segments | Data available now |
| **5** | Build Axis 2 (Value) segments | Data available now |
| **6** | Build Axis 3 (Game Pref) segments | Requires gameplay data |
| **7** | Train churn model (Axis 4) | Requires 30 days data + module |
| **8** | Validate all axes against 1 week data | Steps 3–7 complete |
| **9** | Connect segments to journey triggers | Step 8 validated |
| **10** | Launch first journey (Chain 01) | Step 9 complete |
