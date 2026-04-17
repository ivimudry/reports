CuatroBet Argentina: CRM Actions Playbook
Companion to the Miro architecture board
CRM Consulting Engagement
April 2026
Table of Contents

# Executive Summary

This playbook is the detailed companion to the CRM architecture on Miro. The Miro board shows the visual lifecycle map (preserved from the existing structure) plus four net-new lifecycle diagrams. This document contains the specific values, messages, timings, bonus mechanics, and the 12-week execution plan.
The engagement is anchored on seven headline baselines from the April 2026 discovery:
The single biggest insight from discovery: Day 1 retention is 27.8%. Roughly 72% of players who take a first action disappear within 24 hours. This is the highest-leverage problem in the funnel and drives every downstream metric including STD, ADPU, and bonus cost. The Day 1 Retention Layer in Part I is the single most important initiative in this playbook.
The second biggest insight: bonus cost is 10.5% against a 20% target because wagering is not completing, not because offers are too small. Wagering requirements are too high (40x on the welcome bonus) and the current ladder drops from 120% at D1 to 20% at D2, which punishes second-deposit intent. Fixing wagering mechanics and the D2 cliff is worth more than any new offer.

# Baselines and Targets


## Player base

Total registered: 19,000
FTD count: 4,165 (22.23% FTD conversion)
STD count: roughly 383 (9.20% STD conversion)
Active last 7 days: 1,028
Active last 30 days: 3,298 (17.4% of registered)
VIP tiers I to III combined: 15 players
Product mix: 99.9% casino

## Economics

Average deposit: roughly 36,500 ARS (6 USD)
Deposit frequency: 2.5 per user
Bonus cost: 10.5% of GGR in April, 9.5% in March
KYC soft threshold: 471,000 ARS (75 USD) before document verification required
Payment success rate: 55%
Payment methods: Mercado Pago, Naranja Betterbro, bank transfer

## Top 10 games (for free spin alignment)

Jackpot Joker (TaDa)
Joker’s Jewels (Pragmatic Play)
4 Supercharged Clovers (Playson)
Gates of Olympus (Pragmatic Play)
Joker’s Jewels Cash (Pragmatic Play)
Turkish Live Roulette (Ezugi)
Gold Party (Pragmatic Play)
3 Coin Volcanoes (3 Oaks)
Rush for Gold (3 Oaks)
Gates of Olympus 1000 (Pragmatic Play)
Note: Sweet Bonanza is featured in the Bonus Shop but does not appear in the top 10. All free spin offers should be rotated across the actual top titles, not Sweet Bonanza.

## Channel performance (from the April dashboards)

SMS: best performer. 19.68% click rate, 98.42% delivery, around 1,200 daily sends. Under-used.
Email: healthy. 99.13% delivery, roughly 22% open, 48% CTOR, volume declining (minus 18% trend). Around 1,150 daily sends.
NC Feed: fatigued. Volume scaled 10x in March to April (from 2,000 to 25,700 daily). Open rate fell from 32 to 40 percent down to 11%. Classic message fatigue.
NC Pop-Up: worse. Show rate 2.76%, open rate fell to 2.37%, click rate to 1.57%. Targeting and fatigue problem.
Web Push: dormant. Zero sends across the period observed. Recommended to be activated.
Web Push: negligible volume.

# How to use this document

This playbook is organized in four parts.
Part I: New lifecycles. Full playbooks for the net-new journeys shown as diagrams on the Miro board. Each playbook specifies every touch, the timing, the channel, the message copy, the offer mechanics, and the exit condition.
Part II: Calibration of the existing architecture. The existing lifecycle map on Miro has the structural bones in place but the Communication 1 through 4 boxes are empty and the bonus ladder values need calibration. This part fills them in.
Part III: Cross-cutting redesigns. Changes that span multiple lifecycles or touch product surfaces outside the lifecycle map: channel rebalancing, the bonuses landing page, the bonus shop catalogue, the referral program, smart segmentation setup, and Web Push activation.
Part IV: Execution. The 12-week roadmap, measurement framework, risks and dependencies.
Read in sequence on the first pass. After that, each section can be referenced independently by the CRM owner responsible for that lifecycle.

# PART I: FOUR NEW LIFECYCLES


# 1. Day 1 Retention Layer (highest priority)

The Day 1 Retention Layer is the single highest-priority initiative in this engagement. It directly attacks the 27.8% Day 1 retention baseline which is the root cause of the 9.20% STD conversion, the flat ADPU in month 0, and much of the channel fatigue problem (because the brand is compensating for poor retention with scale blasting).

## Purpose

Keep first-action players alive through the first 72 hours after FTD, using time-based and behaviour-based triggers with low-cost micro-bonuses, SMS, and in-session popups. The layer runs in parallel with the existing Welcome Bonus Ladder. The ladder triggers on deposit events. The Day 1 Layer triggers on time and behaviour events. They never conflict.

## Entry trigger

Real-time FTD success event from the GR8 Tech platform. The layer begins the moment the deposit is confirmed.

## Segmentation

The layer branches at T+1 hour into two paths based on first-session game category: Slots path (default, roughly 95% of players) or Aviator path (players whose first session was on Aviator or another crash game).

## Touch sequence (Slots path)


### T+0 (FTD success)

Channel: system
Action: grant 50 no-deposit free spins on Gates of Olympus (or player’s first-session game if different), expiring in 24 hours, wagering 20x on winnings
Exit: none, continues

### T+5 min: In-session celebration popup

Channel: native in-app popup
Content (ES): “Bienvenido! Tu bono 120% ya está activo. Extra: 50 giros gratis en Gates of Olympus para empezar”
CTA: “Jugar ahora” (deep-link to game)
Exit: player plays then continues

### T+30 min decision: still in session?

Yes: continue to T+1h in-session touches
No: jump to T+2h exit push

### T+1 h: In-session AI game recommendation

Channel: in-session widget
Content: personalized game recommendation based on the first-session game. Show 3 similar slots.
Rationale: GR8 Tech AI recommendations module is already in use. Leverage it for first-hour engagement.
Exit: player opens recommended game then continues

### T+2 h: Session exit push (if session ended)

Channel: SMS
Copy (ES, 160 chars): “CuatroBet: Tus 50 giros gratis en Gates of Olympus vencen en 22h. Seguir jugando: [link]”
Exit: player returns then continues

### T+6 h decision: returned to app?

Yes: send Comm A (engagement reward)
No: send Comm B (urgency SMS)

### T+6 h Comm A: Engagement reward

Channel: in-session popup
Content (ES): “Gracias por volver! Regalo extra: 100 CC gratis + progreso hacia tu primer nivel de lealtad”
Offer: 100 CC no-deposit gift, no wagering
Exit: continues to T+24h decision

### T+6 h Comm B: Urgency SMS

Channel: SMS
Copy (ES): “CuatroBet: Tus giros vencen pronto. Además, te regalamos 21,000 ARS extra si depositás en las próximas 6 horas: [link]”
Offer: 21,000 ARS no-deposit bonus on any deposit action within 6 hours, 15x wagering
Exit: continues to T+24h decision

### T+24 h decision: returned in first 24h?

Yes: exit to standard Post-FTD cadence (the player is likely to STD organically)
No: send T+24h email

### T+24 h: Email reload offer

Channel: Email
Subject (ES): “Tu bono de 75% + 20 giros te esperan”
Offer: 75% match up to 62,000 ARS plus 20 FS on Joker’s Jewels, wagering 25x, expires in 48 hours
Exit: deposit then Post-FTD cadence

### T+48 h decision: still inactive?

Yes: send T+48h SMS
No: exit to Post-FTD cadence

### T+48 h: Final touch SMS

Channel: SMS
Copy (ES): “CuatroBet: Un regalo de despedida. 10,500 ARS free bet en Aviator, sin depósito. Válido 24h: [link]”
Offer: 10,500 ARS no-deposit free bet on Aviator, wagering 1x
Rationale: cheap habit-seed. Aviator is quick-play and hooks players who are on the fence.
Exit: activity then Post-FTD, no activity then Reactivation Ladder Day 3 entry

### T+72 h decision: returned at all in window?

Yes: exit to Post-FTD to STD lifecycle
No: exit to Reactivation Ladder (Early Churn cohort, which enters at day 3 instead of the usual day 7)

## Touch sequence (Aviator path)

Same structure as the Slots path, with content substitutions:
T+0 grant: 5 Free Flights on Aviator (not 50 FS on Gates of Olympus)
T+5 min popup: “Bienvenido! Tus 5 Free Flights en Aviator están listos”
T+1 h recommendation: other crash and instant games
T+24 h email offer: 75% match plus 10 Free Flights on Aviator, 15x wagering (lower because Aviator crash contribution is higher)
T+48 h SMS: 10,500 ARS free bet on Aviator (same as Slots path)

## Cost model

Expected cost per player entering the Day 1 Layer:
Average deposit is 36,500 ARS, so the layer costs roughly 22% of the first deposit. This is fully funded from the existing bonus budget by reducing welcome bonus wagering (which lifts the bonus cost metric anyway) and stopping the NC Feed blast over-sending.

## KPI impact

Day 1 retention: 27.8% toward 38 to 42% (relative uplift of 35 to 50%)
STD conversion: 9.20% toward 12 to 14% (downstream of Day 1 retention)
Bonus cost % GGR: plus roughly 2% contribution toward the 20% target
Channel load: SMS usage doubles, NC Feed usage drops by more than half

## Implementation notes

Real-time event trigger required. Confirm with GR8 Tech that the FTD success event fires in real-time and can trigger a journey within 5 minutes. The in-session popup requires sub-second trigger latency.
Web Push must be activated before launch. The layer can run without Web Push but loses roughly 30% of its effective touches in the T+6h decision branch.
Aviator path depends on first-session game detection. Confirm the platform exposes the first-game played event to the CRM.
Test wagering contribution for Aviator. Crash games contribute differently than slots. The 15x wagering on the Aviator-path T+24h email assumes 100% Aviator contribution.

# 2. Pre-VIP Lifecycle


## Purpose

Identify players who have deposited 3,130,000 ARS cumulatively (roughly 500 USD) and coach them toward the VIP I threshold (roughly 6,260,000 ARS or 1,000 USD cumulative) within 30 days. The current VIP base is 15 players. A functioning Pre-VIP layer grows it to 30 to 45 in the first quarter by capturing players who are already on the path but are not being actively managed.

## Entry trigger

Cumulative lifetime deposits reach 3,130,000 ARS AND the player has been active in the last 14 days.

## Touch sequence


### Day 1: Pre-VIP activation

Action: assign CRM owner (named person, not brand), flag player in segmentation system, add to the Pre-VIP dashboard
Channel: personal email from the CRM owner (real name, signature, direct reply-to)
Subject (ES): “Acabás de desbloquear estatus Pre-VIP en CuatroBet”
Content: warm, personal, no hard sell. Congratulate the milestone, introduce the CRM owner by name, outline the benefits (15% weekly cashback, curated game recommendations, faster withdrawals, exclusive offers), hint at VIP I with the phrase “unos pocos pasos más”.
Gift: 500 CC plus 20 FS on player’s favorite slot from session history
In-app: Pre-VIP unlock banner on next login

### Day 3: Cashback activation

Action: enable 15% weekly cashback for 30 days (wager-free, applied every Monday on the previous week’s net losses, capped at 625,000 ARS)
Channel: Email plus in-app banner
Subject (ES): “Tu cashback Pre-VIP está activo”
Content: explain how the cashback works, when it pays out, the cap

### Day 5: Curated game list plus reload

Channel: Email
Subject (ES): “Tu selección personalizada y un bono especial”
Content: curated list of top slots plus 2 new releases matched to the player’s game preference
Offer: 60% match up to 208,000 ARS plus 30 FS on a premium PP title, wagering 20x, validity 72 hours

### Day 10: Soft coaching push

Channel: Web Push plus SMS
Copy (ES): “Estás a unos 1,040,000 ARS de VIP I. Tu manager personal te está esperando.”
Rationale: frame the VIP I threshold as achievable and desirable

### Day 14 decision: VIP I threshold reached?

Yes: exit to VIP I onboarding flow (personal manager assigned, welcome package)
No: continue to Day 15 second chance

### Day 15: Second chance reload

Channel: Email plus SMS from the CRM owner
Subject (ES): “Te extrañamos esta semana”
Offer: 100% match up to 416,000 ARS plus 50 FS plus extended cashback, wagering 15x, validity 72 hours

### Day 21 decision: any deposit since Day 14?

Yes: cashback top-up plus predictive churn monitoring enabled
No: add to Churn Intervention flow at Day 22

### Day 30 decision: VIP I reached?

Yes: exit to VIP I onboarding
No: stay in Pre-VIP for another 30 days with reduced cadence (one email per week, no SMS), drop back to Regular if no activity in the extended 30 days

## Offer calendar summary for Pre-VIP


## KPI impact

VIP base: 15 toward 30 to 45 in one quarter
Pre-VIP to VIP I conversion target: 30 to 40% within 30 days of entry
ADPU uplift among Pre-VIP cohort: historical cohort data shows ADPU doubles from month 3 to month 5, so active coaching through this window locks in the compounding

## Implementation notes

Assigning a named CRM owner is non-negotiable. The personal touch is the single biggest driver of conversion in this segment.
Cashback must be wager-free. High-value players punish perceived tricks, and wagering on cashback is perceived as a trick.
The 3,130,000 ARS entry threshold is calibrated against the brand’s own tier economics (Premium unlock at 315,000 ARS, Maestro at 730,000 ARS, VIP I starts around 6,260,000 ARS cumulative). Review quarterly.

# 3. KYC Completion Chain


## Purpose

Move KYC completion from 20% to 35 to 40% by converting verification from a compliance chore into a rewarded journey. The current state: half of verifiers complete immediately, half only when they try to withdraw, and most never complete at all. Verification is gated on the 471,000 ARS (75 USD) cumulative deposit threshold for documents, while email and phone verification are technically optional but should be driven earlier.

## Three phases

Phase 1: Email verification (day 0, triggered by registration)
Phase 2: Phone verification (day 0, immediately after email)
Phase 3: Document verification (triggered when cumulative deposits reach 315,000 ARS)

## Phase 1: Email verification


### Entry

Registration complete.

### T+0: Phase 1 prompt

Channel: in-session popup plus confirmation email with verification link
Content (ES): “Verificá tu email y recibí 10,500 ARS de regalo al instante”
Offer: 10,500 ARS bonus on email verification, no wagering on the bonus, can be used directly

### T+15 min decision: email verified?

Yes: credit 10,500 ARS, proceed to Phase 2
No: send T+15 min reminder SMS

### T+15 min: SMS reminder (if email not verified)

Channel: SMS
Copy (ES): “CuatroBet: Verificá tu email y recibí 10,500 ARS al instante: [link]”

### T+24 h decision: email verified?

Yes: credit 10,500 ARS, proceed to Phase 2
No: continue to Phase 2 anyway (email can be verified later)

## Phase 2: Phone verification


### Entry

After email verification, or T+24 h regardless of email status.

### T+0: Phase 2 prompt

Channel: in-session popup plus SMS with verification code
Content (ES): “Verificá tu teléfono y recibí 10,500 ARS más. Total: 21,000 ARS al instante”
Offer: 10,500 ARS bonus on phone verification, no wagering

### On verification

Credit 10,500 ARS
Auto opt-in the player to the SMS channel. This is the single most valuable side effect of phone verification. Given that SMS is the best performing channel, getting more players opted in is worth a significant retention lift downstream.

### If not verified within 48 hours

Send one SMS reminder
Proceed without blocking (player can still deposit)

## Phase 3: Document verification


### Entry

Cumulative deposits reach 315,000 ARS (roughly 50 USD) AND not yet document-verified.
Rationale: do not wait for the 471,000 ARS hard threshold. Start the document nudge 30% earlier so there is runway to complete before the withdrawal block kicks in.

### Day 1 at 315,000 ARS threshold

Channel: in-app banner plus Email
Content (ES): “Completá tu verificación ahora y desbloqueá retiros más rápidos plus un bono de 21,000 ARS”
Offer: 21,000 ARS bonus on document verification, no wagering
Documents required: government ID plus proof of address (standard KYC)

### Day 2: Email guide

Channel: Email
Subject (ES): “Tu cuenta está a un paso del acceso total”
Content: visual guide on how to upload documents, expected review time (24 hours), benefits of being fully verified
Offer: 21,000 ARS bonus still valid

### Day 3 decision: documents submitted?

Yes: if accepted, credit bonus, run celebration popup, exit to active lifecycle
No: continue to threshold approach message

### On cumulative deposits reaching 471,000 ARS (the hard threshold)

Channel: in-session popup plus Email plus SMS
Content (ES): “Verificación obligatoria para retiros. Completá ahora y recibí 41,000 ARS de bono final”
Offer: 41,000 ARS bonus (doubled from the Day 1 offer) as final reward for completing

### On verification acceptance

Credit the 41,000 ARS bonus
Run celebration popup: “Verificación completa. Retiros rápidos activados. Tenés acceso al canal VIP.”
Exit to active lifecycle at their current stage

### If rejected

Route to support queue for manual resolution
Email explaining next steps
Do not remove the bonus offer

## Cost model

Not all players will reach Phase 3. The blended cost across the whole registered base is lower, probably 400 to 10,500 ARS per registered player.

## KPI impact

KYC completion: 20% toward 35 to 40%
SMS opt-in rate: plus 25 to 40% (direct result of phone verification)
Withdrawal friction: reduced. Players arrive at their first withdrawal already verified, which improves VIP perception.
Fraud prevention: earlier document verification enables better risk management for Pre-VIP and VIP tiers.

# 4. Payment Failure Recovery


## Purpose

Recover 15 to 25% of failed deposit attempts in real-time, lifting the effective payment success rate from 55% toward 65 to 70%. This lifecycle is complementary to the existing Failed cluster in the Miro architecture. The Failed cluster handles follow-up communications from T+5 minutes onward. This lifecycle handles the first 30 seconds in-session, where the biggest recovery gains are available.

## Entry trigger

Real-time deposit failure event from the GR8 Tech platform. The lifecycle fires within 5 seconds of the failure.

## Classify failure reason

The platform should expose a failure reason code. Route the player based on reason:
Insufficient funds: the player tried to deposit more than they have in their payment method
Method unavailable: the payment method is temporarily down or unsupported
Acquirer declined: the bank or payment provider rejected the transaction
Timeout or technical: gateway timeout, network error, unknown

## Real-time recovery (in-session)


### Insufficient funds

Channel: in-session popup
Content (ES): “Probá con un monto menor”
Action: show preset amount buttons: 10,500/21,000/146,000 ARS
Rationale: the player likely wanted to deposit 5,000 but only has 1,500. A lower preset catches this.

### Method unavailable (Mercado Pago / Naranja / bank down)

Channel: in-session popup
Content (ES): “Probá con otro método”
Action: one-click buttons for the other 2 active methods, preselected
Rationale: friction-free alternative suggestion. The player does not have to find the other methods in a menu.

### Acquirer declined

Channel: in-session popup
Content (ES): “Tu banco rechazó el pago. Probá con otro método”
Action: same as method unavailable. The player’s bank is the issue; swap method.

### Timeout or technical

Channel: in-session popup
Action: auto-retry after 10 seconds with a spinner showing “Reintentando…” then show the result
Rationale: gateway timeouts often resolve on retry. Do not require the player to re-enter anything.

## Recovery decision


### Recovered within session?

Yes: show celebration popup with a 100 CC gift, then exit to Day 1 Retention Layer
No: hand off to the Failed cluster communication ladder at T+30 min (see Part II)

## Cost model

The Payment Failure Recovery lifecycle is the cheapest initiative in this playbook and has the highest leverage per peso spent.

## KPI impact

Payment success rate (effective, including recovered attempts): 55% toward 65 to 70%
FTD conversion (downstream): roughly plus 2 to 4 percentage points, because many FTD attempts fail today and are lost
Bonus cost: no direct impact. This is a payments issue, not a bonus issue.

## Integration with the Failed cluster on Miro

The Failed cluster handles 5 reasons each with a 4-communication ladder, starting at T+5 minutes. The Payment Failure Recovery flow handles T+0 to T+5 minutes. Both must be implemented together for end-to-end coverage.

## Implementation notes

Confirm real-time failure event exposure with GR8 Tech. The lifecycle requires a sub-5-second trigger latency.
Failure reason classification must be accurate. If the platform does not distinguish insufficient funds from acquirer declines, the routing collapses.
Work with the payments team to raise the raw 55% rate in parallel. CRM recovery is a ceiling. The real fix is upstream.

# PART II: CALIBRATION OF THE EXISTING ARCHITECTURE

The existing CRM architecture on Miro has the structural bones in place: Welcome flow, 10-deposit bonus ladders × 3 verticals, Failed cluster with 5 reasons, No Bonus, No Cashier, Personalization, Engagement/Gamification, Loyalization, Reactivation matrix. The problem is that the Communication 1 through 4 boxes are empty placeholders and the bonus ladder values need calibration. This part fills them in.

# 5. Welcome Bonus Ladder Calibration


## Design principles

D1 Welcome is the hook. Strongest headline bonus (120% standard, 150% for deposits above 315,000 ARS), 25x wagering, branded to the vertical.
D2 is the survival bridge. The existing draft jumped from 120% at D1 to 20% at D2, which is too punishing and is almost certainly a driver of the 9.20% STD conversion. The calibration holds at 75% match for D2 to prevent the cliff.
D3 to D5 are the habit phase. 50 to 60% match, steady cadence, lower wagering (15 to 18x) so wagering actually completes. This is where bonus cost % GGR gets reclaimed.
D6 to D8 are the loyalty phase. Slightly higher matches, richer free spins, introduction of Cuatro Coin (CC) gifts.
D9 and D10 are the Pre-VIP gate. High match with low wagering, Lucky Wheel entries, and at D10 automatic enrollment in the Pre-VIP Lifecycle if cumulative deposits reach 3,130,000 ARS.

## Slots ladder (the main audience, 99% of players)

Free spins are rotated across the actual top-played slots, not Sweet Bonanza.
Safeguards for Slots: wagering contribution slots 100% / live 10% / table 5%, max bet during wagering 32,000 ARS per spin, max bonus balance 625,000 ARS at any time, one claim per deposit.

## Live Casino ladder (small audience, higher ARPU)

Only Turkish Live Roulette appears in the top 10. Live wagering contribution is 10%, so match bonuses are combined with Bonus Cash to make wagering realistic.

## Sport ladder (0.1% of players, maintained but deprioritized)

Given the 99.9% casino mix, Sport is maintained for the rare sports-only user but receives the lowest CRM cadence priority. Values use free bets instead of free spins, odds minimum 1.80.

## Path to 20% bonus cost % GGR

The current 10.5% bonus cost is a wagering completion problem, not an offer size problem. The calibration above resolves this through three mechanisms:
Lower wagering requirements (from 40x to 15 to 18x for most deposits). More players complete wagering, so more of the already-budgeted bonus is recognized in the cost metric. Expected lift: 10.5% toward 14 to 15% in weeks 1 to 4.
D2 bridge (75% hold instead of the punishing 20% drop). Retains players who currently abandon between D1 and D2. Expected lift: plus 2 to 3% by week 6.
CC gifts from D5 onward. Straight-cost items that contribute directly to the bonus cost line without requiring wagering. Expected lift: plus 1 to 2% by week 8.
Target: 20% bonus cost by week 12.

# 6. Failed Deposits: Communication Specs

The Failed cluster handles 5 failure reasons with a 4-communication ladder each. These specs fill every Communication 1 through 4 box on the Miro board. The Payment Failure Recovery lifecycle (Part I, section 4) handles T+0 to T+5 minutes. These ladders pick up from T+5 minutes onward.

## 1. No attempt for deposit (closed cashier page)

Segment: player opened the cashier page, did not attempt any deposit, closed or navigated away, 30+ minutes inactive.
Exit: deposit attempted then Day 1 Retention Layer. No response after Comm 4 then Reactivation pre-FTD cohort.

## 2. Failed deposit attempt, tech reason (first attempt)

Segment: one deposit attempt failed due to technical reason (gateway timeout, network error, provider unavailable).
Exit: successful deposit then Day 1 Retention with credit applied. No response then Reactivation Payment-blocked sub-cohort.

## 3. Failed two deposit attempts tech reason

Segment: 2 or more failed attempts in the same session, indicating a persistent issue.
Exit: successful deposit then exit. No response then Reactivation Payment-blocked high-priority flag.

## 4. Deposit declined by acquirer

Segment: deposit attempt rejected by the acquiring bank or payment provider (insufficient funds, card blocked, provider risk rule).
Exit: successful deposit then exit. No response then Reactivation Payment-blocked cohort.

## 5. Fraud

Segment: deposit attempt flagged by the risk engine.
Exit: resolved fraud (false positive) then back to current lifecycle stage. Confirmed fraud then account closure.

# 7. No Bonus Cluster: Communication Specs


## Missed sub-branch

Segment: player registered, did not claim welcome bonus, 1+ hour after registration with no bonus-related interaction.

## None interested sub-branch

Segment: player explicitly declined welcome bonus OR behavior shows zero bonus interest (clicked through the bonus flow and bypassed it).
Rationale: high-pressure bonus messaging alienates this segment. Switch to low-friction habit-seeding and product discovery.

# 8. No Cashier Visited: Communication Specs


## Bounce sub-path

Segment: session under 60 seconds, left site without cashier interaction.

## Long session sub-path

Segment: session longer than 10 minutes, browsed or played demo, never clicked deposit button.

## Free spins sub-path

Segment: player triggered free spins demo or won no-deposit free spins, no real-money deposit yet.

# 9. Personalization: Communication Specs


## Anniversary

Segment: any active player reaching an account creation anniversary (1, 2, 3+ years).

## Birthday


## Personal custom

Segment: ad-hoc triggers set by the CRM manager (e.g., player mentioned a specific game in support, player 105,000 ARS from a tier threshold).
Template structure for each custom campaign: - Comm 1: trigger-specific initial message - Comm 2: follow-up 24 to 48 h later if no response - Comm 3: final reminder before offer expiry - Comm 4: thank-you or transition
Required fields per campaign: trigger condition, target audience size, channel per comm, copy per comm in Spanish, offer details, exit condition, success metric. Reviewed weekly in the CRM standup.

## Zodiac bonus

Segment: all active players, triggered on the first day of each zodiac month.

# 10. Engagement and Gamification: Full Specs


## Loot boxes

Mechanic: players earn loot box tokens through gameplay. 1 token per 105,000 ARS wagered on slots, 1 token per 208,000 ARS wagered on live. Opened manually from the dashboard.
Reward table (weighted):
Comms: token earn push, box open celebration, weekly unclaimed reminder, monthly summary.

## Stickers

Mechanic: 30-slot sticker book. Collect via specific actions (play Jackpot Joker 10 times, deposit 3 days in a row, try a new provider). Row of 5 complete = reward. All 30 = grand prize.
Rewards: single sticker 25 CC, row of 5 is 4,100 ARS + 10 FS, all 30 is 208,000 ARS + premium Lucky Wheel + VIP I preview.
Comms: new sticker available push, 1-sticker-away email, row complete push, monthly summary.

## Quests (8 named mechanics)


### Quest 1: 4 deposit quest (Cuatro core mechanic)

Mechanic: 4 deposits in any rolling 7-day window. Core brand mechanic, directly addresses STD.
Auto-enrolls on first deposit. Wagering 20x on FS winnings. Target: STD +30 to 50% relative.
Comms: welcome to quest, halfway, 1 more to go, completion celebration.

### Quest 2: Double chance

Mechanic: 1 deposit = 2 Lucky Wheel spins during a limited window (1 weekend per month).
Comms: Friday announcement, Saturday live, Sunday last day, Monday thank you.

### Quest 3: Silver spin

Mechanic: tiered wheel spins earned by wagering. Silver (1 per 41,000 ARS wagered), Gold (1 per 208,000 ARS), Platinum (1 per 1,040,000 ARS).
Comms: earned push, 48h unused reminder, 24h expiry warning, post-spin celebration.

### Quest 4: Steady flow

Mechanic: 4 deposits of the same amount in a row (no time limit). Reward scales with deposit size.
Comms: started after 1st, 2 more to go, 1 more to go, completion.

### Quest 5: Triple treat

Mechanic: 3 deposits in 3 consecutive calendar days.
Comms: day 1 start, day 2 don’t break the streak, day 3 final day, completion.

### Quest 6: Cuatro cycle (4 deposits, fixed amount)

High priority, flagged red in the original board.
Mechanic: player opts in and commits to a fixed amount (32,000/62,000/105,000/950,000 ARS), deposits that exact amount 4 times in 7 days. Resets if a deposit does not match.
Comms: opt-in confirmation, progress update after each deposit, day 5 final 2 days, completion.

### Quest 7: 4 days deposit fixed amount

High priority, flagged red.
Mechanic: identical concept to Cuatro Cycle but with a stricter time constraint of 4 consecutive calendar days instead of a 7-day window.
Recommendation: consolidate with Cuatro Cycle into a single mechanic with two variants labeled clearly, to avoid player confusion: “7-day flexible Cuatro Cycle” and “4-day consecutive Cuatro Cycle”. Rewards: same as Cuatro Cycle tiers with a 20% cashback uplift for the tighter 4-day variant.

### Quest 8: Reach turnover in 4 random slots

High priority, flagged red.
Mechanic: player must reach a wagering turnover target across 4 randomly assigned slots within a week. Random assignment each Monday. 2 slots drawn from the top 10 most played, 2 drawn from new releases or under-played titles (cross-promotion).
Comms: Monday quest launch with slot list, Wednesday progress, Friday final push, Sunday last day.

## Situational: Weekly bonuses

Every Friday, all players with at least 1 deposit in the previous 7 days get a tiered reload.
Comms: Friday 10 AM email, Friday evening push, Saturday SMS, Sunday last-day push.

## Situational: Daily bonuses

Daily login streak, no deposit required, reward scales with consecutive days.
Comms: daily morning push, 4+ streak evening SMS if not claimed, day 7 celebration, streak broken email.

## Situational: Holiday bonuses (Argentina calendar)

Comms per holiday: 1 week before teaser, 3 days before reminder, day of celebration push, day after residual offer.

# 11. Loyalization: Communication Specs


## Active loyalty members

Segment: players enrolled in the loyalty program who completed at least 1 mission in the last 7 days.
Sub-segments under Active (the 4 empty sub-boxes): Slots-heavy, Live-heavy, Aviator, Mixed. Same 4 comms above with content tailored to game preference.

## Passive loyalty members

Segment: players enrolled in the loyalty program, NOT completed a mission in 7+ days, still within 30 days of last activity.
Sub-segments under Passive: same 4 behavioral splits as Active.

# 12. Reactivation Matrix: Communication Specs

The Reactivation cluster is the most complex on the board: 2 engagement histories (Active vs Passive) × 3 time buckets (7, 14, 21+ days) × 4 comms each, plus a Verified-but-no-reacted special case and a Clicks/opens/pages behavioral filter. Total: 36+ comms specified below.

## Integration with Predictive Churn

Current ladder is reactive (acts at fixed day marks). When the GR8 Tech Predictive Churn model is activated, the entry point shifts earlier for at-risk players (churn score above 60 enters the 7-day ladder at day 3 or 4 instead of day 7). Ladders themselves remain the same.

## Offer calibration by value tier (applies to every cell below)

The matrix structure handles the temporal axis: how long the player has been inactive, and whether they were previously Active or Passive. The value tier overlay handles the economic axis: how much that player is actually worth. Both run simultaneously. Every cell in the matrix specifies a base offer, and the actual offer sent to a given player is that base scaled by the player’s lifetime value tier.

### Worked example

Active × 7 days Comm 1 specifies a base offer of “30% match up to 41,000 ARS + 20 FS on Jackpot Joker, 15x wagering, 48h validity”. Applied by tier at send time:
Micro player: 50 CC gift only, no match bonus. Reactivation cost near zero for a player unlikely to return.
Low player: 30% match up to 41,000 ARS + 20 FS, 15x, 48h. Base offer as written in the cell.
Mid player: 45% match up to 62,000 ARS + 30 FS, 15x, 48h.
High player: 60% match up to 85,000 ARS + 40 FS, 15x, 48h, sent from the CRM owner’s named email rather than the brand email.
Pre-VIP and above: 75% match up to 105,000 ARS + 50 FS + 100 CC, 12x, 72h, delivered by the CRM owner via WhatsApp with a personal message.
The same overlay applies to all cells in the matrix (Active × 14, Active × 21+, Passive × 7, 14, 21+, and Verified-but-no-reacted). The cells below show base offers only. Scale by tier at send time.

## Active × 7 days (highest return probability)

Rationale: low-friction, habit-preserving messaging. These players are most likely to return, do not burn budget.

## Active × 14 days


## Active × 21+ days

Higher urgency, higher offer value. For Pre-VIP and above, offers escalate further.
Exit: activity then Regular or Pre-VIP. No response then Deep Churn (quarterly win-back only).

## Passive × 7 days

Lower return probability, smaller offers to protect budget.

## Passive × 14 days


## Passive × 21+ days

Exit: activity then Regular. No response then Deep Churn.

## Verified but no reacted (special case)

Segment: player completed KYC (email, phone, documents) but never made a deposit or meaningful activity after verification.
Rationale: these players invested effort in verification, indicating interest, but something blocked them from depositing. Focus on removing perceived friction.

## Clicks/opens/pages filter

The Clicks/opens/pages shape in the existing cluster is a behavioral filter, not a comm sequence. Use it as a segmentation overlay on all ladders above:
High-engagement filter (opens emails, clicks links, no deposit): offer-heavy sequences, higher match %. These players are curious but waiting for the right offer.
Low-engagement filter (low open rate): SMS-heavy sequences, drop email frequency, simplify content.
Zero-engagement filter (no opens, no clicks, no visits): single strong SMS at day 21, then Deep Churn.

## Frequency cap across all Reactivation ladders

Maximum 1 message per day per player. If multiple ladders would fire on the same day, collapse to the highest-value message only.

# PART III: CROSS-CUTTING REDESIGNS


# 13. Channel Strategy and Frequency Caps

The current channel mix is out of balance. NC Feed and NC Pop-Up are fatigued from over-sending, SMS is the best performer and under-used, Email is healthy but declining, Web Push is dormant.

## Target channel mix (next 6 weeks)


## Frequency caps (across all channels combined)

Transactional and security messages are not subject to these caps.

## Channel-to-stage mapping


## NC Feed and NC Pop-Up cooling plan

Both channels show classic fatigue signatures: volume scaled aggressively while engagement collapsed. The fix is to cool, re-segment, and cap:

### NC Feed cooling

Cut daily volume by 60% immediately (from 25,700 to 10,000)
Apply strict cap: maximum 2 NC Feed items per player per day, minimum 4 hours between items
Restrict to active players only (opened app in last 48 h)
Personalize by lifecycle stage
Monitor open rate weekly, do not scale back up until open rate recovers to 20%+

### NC Pop-Up cooling

Investigate the 2.76% show rate with the GR8 Tech team (targeting or trigger issue)
Apply strict cap: maximum 1 popup per player per session
Session exclusion: no popup in the first 60 seconds of a session
Use only for high-value triggers (deposit failure, VIP invitation, churn intervention)
Stop using as a broadcast channel

## Web Push activation (new channel)

Prerequisite: platform configuration plus opt-in flow in the app.
Launch sequence:
Week 1: technical setup, opt-in prompt on app open (post-FTD only to start, avoids scaring new users)
Week 2: enable for Day 1 Retention Layer touches
Week 3: enable for Post-FTD and Pre-VIP journeys
Week 4: evaluate opt-in rate (target 40%+), open rate (target 15%+), enable for Reactivation if healthy
Week 5+: general use within frequency caps
Opt-in incentive: 100 CC on opt-in.
Quiet hours: no pushes between 00:00 and 08:00 ART.

## Kill switch

If any channel’s open rate drops more than 25% week-over-week, pause new campaigns on that channel and investigate before scaling back up.

# 14. Bonuses Landing Page Redesign

The current Bonuses landing page has structural issues visible from the screenshot review.

## Current issues

“Lucky Wheel” card shows 357D LEFT countdown. A countdown of nearly an entire year is not urgency, it is decoration. It also makes the page feel stale.
Sports Welcome Bonus prominently displayed despite 99.9% of players being casino. This is wasted real estate.
Two near-identical Slots / Live Welcome cards (150% + 60 FS for Slots, 150% for Live). Cannibalizes attention.
No lifecycle personalization. Every player sees the same 4 cards regardless of whether they are pre-FTD, post-FTD, Regular, or VIP.
No hierarchy. The Lucky Wheel is visually equal to the Welcome bonuses even though they serve completely different purposes.

## Redesigned layout


### Pre-FTD player

Hero card (large, top): Welcome Bonus 120% + 50 FS on Gates of Olympus. Clear CTA: “Depositar ahora”.
Supporting card 1: Lucky Wheel (with genuine countdown to next draw, not 357 days).
Supporting card 2: Top games preview with 3 featured slots from the top 10.
Supporting card 3: “How to deposit in 2 minutes” walkthrough.
Hidden for pre-FTD: all reload offers, VIP content.

### Post-FTD player (within Day 1 Layer)

Hero card: Second deposit bonus 75% + 30 FS matching the player’s first-session game.
Supporting: free spins remaining on welcome, Lucky Wheel, game recommendations.

### Regular player

Hero card: current weekly reload offer (rotates based on day of week).
Supporting: active quests, Lucky Wheel, bonus shop featured items.

### Pre-VIP and VIP

Hero card: personal message from CRM owner, cashback status, exclusive offer.
Supporting: VIP events, curated games, direct contact.

## Sports card handling

Deprioritize sports in the casino-default view. Add a filter tab at the top: All / Casino / Sports. Default to Casino. Sports users find their offers in the Sports tab.

## Lucky Wheel countdown fix

The 357-day countdown suggests the card was never updated after launch. The Lucky Wheel should: - Show time until the next scheduled draw (daily for daily Lucky Wheel, weekly for weekly, never 357 days) - If there is no current draw, hide the card or show a “Next Lucky Wheel: [date]” teaser

# 15. Bonus Shop SKU Catalogue Redesign


## Current issues

Flat pricing: every deposit match bonus is 300 CC regardless of vertical.
Inconsistent Free Bet pricing: 167,000 ARS free bet at 350 CC, 62,000 ARS free bet at 150 CC. Different CC-to-ARS ratios for similar products.
Aviator labeling duplication: two items labeled “5 Free Flights on Aviator” at 200 CC and 50 CC. Breaks catalogue trust.
No entry-level item under 50 CC to build the spending habit.
No aspirational item above 350 CC to give players something to save for.
Free spins misaligned with top games: featured on Sweet Bonanza which is not in the top 10.
No personalization: every player sees the same catalogue.
No tier locks: all items visible to all players, diluting aspiration.

## Redesigned catalogue: 4 tiers


### Entry tier (10 to 40 CC): habit builders

Available to all players. Builds the habit of visiting and spending CC.

### Standard tier (50 to 150 CC): main storefront

Available after FTD.

### Premium tier (200 to 400 CC): locked behind loyalty level

Requires Premium loyalty tier or above.

### VIP tier (500 to 2,000 CC): locked behind Pre-VIP / VIP


## Lifecycle personalization


## Catalogue fixes before launch

Correct the Aviator labeling: one SKU clearly “5 Free Flights” and another clearly “20 Free Flights” with prices reflecting actual value.
Harmonize free bet CC pricing: consistent ARS-per-CC ratio across all free bet SKUs.
Remove the “Popular” tag from all items. Re-apply only to items crossing a real redemption volume threshold (top 3 by weekly redemption).
Add a “New” tag to items introduced in the last 14 days.
Add a real countdown timer to rotating free spin offers (genuine 7-day rotations).

## CC economy rebalancing

Earning side: keep the current XP and CC earning rates by loyalty tier (Premium 6 CC/mission, Prestige 8 CC, Maestro 12 CC, Legend 18 CC).
Burning side: Entry tier exists to create burn opportunities at every visit.
Expiry: introduce soft expiry: CC expire after 90 days of player inactivity (not 90 days of holding). Creates urgency without penalizing active players.
Target earn-to-burn ratio: 1.0 to 1.2 (currently below 0.3, players are hoarding).

## Expected impact

Bonus Shop redemption rate: 2x to 3x current baseline within 6 weeks
CC burn rate: from below 30% of earned to above 80%
Weekly shop visit frequency: new habit loop established

# 16. Referral Program Design

Referral program does not currently exist. Launching it is a low-effort, medium-impact addition that taps the existing active base as an acquisition channel.

## Mechanic

Referrer (existing player): gets a unique referral link or code shareable via WhatsApp, Instagram, or copy-paste.
Referred player (new): registers using the link, gets an enhanced welcome bonus.
Referrer reward: triggered when the referred player completes their second deposit (STD), not just FTD. Protects against abuse and aligns rewards with actual value creation.

## Offer structure


## Anti-abuse rules

Self-referral blocked (IP, device fingerprint, payment method match)
Same payment method cannot be used by both referrer and referred
Referrer must have at least 3 deposits themselves to be eligible
Maximum 10 successful referrals per referrer per month
KYC required for referrer to receive rewards above 21,000 ARS cash
Velocity check: if a single referrer generates more than 5 referrals in 48 hours, flag for manual review

## Launch campaign

Week 1 of launch: email to entire active base announcing the program, personalized referral link embedded
Launch bonus: first 100 successful referrals (STD) get an extra 21,000 ARS cash on top of standard reward
Leaderboard: top 10 referrers per month get an additional 208,000 ARS cash prize
Comms cadence: weekly email reminder to active players, “Your referral earnings this month: X ARS”

## Expected impact

5 to 10% of new registrations coming via referral within 12 weeks
Higher quality cohort: referred players typically show 20 to 30% higher retention than paid acquisition channels
Activation of latent VIP identification: referrers who bring in multiple players tend to be enthusiastic brand advocates, candidates for VIP upgrade

# 17. Smart Segmentation Setup

Discovery confirmed GR8 Tech’s Smart Segmentation and Predictive Churn modules are available but not activated. These are prerequisites for most of the lifecycles in this playbook.

## Five-axis segmentation model


### Axis 1: Lifecycle Stage

Drives which journey a player is in.
Registered (account only)
Activated (first action, no FTD)
FTD (less than 24 hours old)
Day 1 to 3 (in Day 1 Retention Layer window)
Pre-STD (wagered FTD, no second deposit yet)
Regular (2+ deposits, active in last 14 days)
Pre-VIP (lifetime deposits 150,000 to 6,260,000 ARS)
VIP I to IV (per VIP program thresholds)
At-risk (active but predictive churn score above threshold)
Dormant 3-7 / 8-14 / 15-30 / 31-60 / 60+ days

### Axis 2: Value Tier (lifetime deposits)


### Axis 3: Game Preference

Slots-only (majority)
Aviator / crash games
Live Casino
Mixed (slots + one other)

### Axis 4: Churn Risk (from Predictive Churn module)

Healthy (below 30%)
Watch (30 to 60%)
At-risk (60 to 85%)
Critical (above 85%)

### Axis 5: KYC Status

Unverified
Partially verified (email and phone)
Fully verified (documents)

## How the axes combine

Journeys trigger on Axis 1 (Lifecycle Stage)
Offers within a journey are selected by Axis 2 (Value Tier)
Content and game-specific rewards are selected by Axis 3 (Game Preference)
Axis 4 (Churn Risk) is an accelerator that pulls a player into an earlier touch
Axis 5 (KYC) is a gate that determines permitted actions
Example: a Low-value, Slots-preferring, Watch-tier player who is 2 days post-FTD enters the Post-FTD to STD lifecycle (Axis 1), receives the Low-tier reload offer (Axis 2), with free spins on Joker’s Jewels (Axis 3), sent earlier than default because they are on the Watch list (Axis 4), via SMS because their KYC is partially verified (Axis 5).

## Activation checklist

Contact GR8 Tech account team to enable Smart Segmentation module
Contact GR8 Tech to enable Predictive Churn model
Request access to raw player-level data export (mentioned as available in discovery)
Build the 5-axis classification rules in the GR8 Tech segmentation UI
Validate against 1 week of historical data before going live
Connect segments to journey triggers

# PART IV: EXECUTION


# 18. 12-Week Implementation Roadmap

The roadmap is sequenced to deliver quick wins first (channel cooling, bonus ladder calibration) while longer-lead items (Web Push, Predictive Churn) are built in parallel.

## Weeks 1 to 2: Foundations and quick wins

Immediate: cut NC Feed volume by 60%, apply frequency caps
Immediate: cut NC Pop-Up to 5,000 per day, investigate targeting with GR8 Tech
Week 1: activate Smart Segmentation module, build the 5-axis model
Week 1: activate Predictive Churn model
Week 1: request Web Push technical setup
Week 2: recalibrate the Welcome Bonus Ladder (Slots, Live, Sport) with new wagering requirements
Week 2: launch the Day 1 Retention Layer (phase 1 without Web Push)
Week 2: fix the Bonuses landing page Lucky Wheel countdown
Week 2: fix the Bonus Shop Aviator labeling and free bet pricing inconsistencies
Expected KPI impact by end of week 2: - Bonus cost % GGR: 10.5% toward 12 to 13% - Day 1 retention: 27.8% toward 32%

## Weeks 3 to 4: Payment recovery and KYC chain

Week 3: launch Payment Failure Recovery lifecycle (real-time in-session flow)
Week 3: launch KYC Completion Chain (all 3 phases)
Week 4: activate Web Push channel (opt-in flow, Day 1 Layer integration)
Week 4: launch Failed cluster communication ladders (all 5 reasons)
Week 4: first weekly measurement review with baseline vs target comparison
Expected KPI impact by end of week 4: - Day 1 retention: roughly 34 to 36% - Payment success (effective): 55% toward 58 to 60% - KYC completion: 20% toward 25%

## Weeks 5 to 6: Lifecycles and personalization

Week 5: launch Pre-VIP Lifecycle, identify initial cohort from historical data
Week 5: launch the No Bonus cluster communication ladders
Week 6: launch the No Cashier Visited communication ladders
Week 6: launch Personalization cluster (Anniversary, Birthday, Zodiac)
Week 6: begin weekly CRM standup with the 5-axis segmentation health check
Expected KPI impact by end of week 6: - STD conversion: 9.2% toward 11 to 12% - Bonus cost % GGR: 14 to 15% - Pre-VIP cohort identified: first 20 players in the program

## Weeks 7 to 8: Engagement and loyalization

Week 7: launch Loyalization communication ladders (Active + Passive)
Week 7: launch the 4 Deposit Quest (Cuatro core mechanic)
Week 8: launch Daily bonuses (login streak)
Week 8: launch Weekly bonuses (tiered Friday reload)
Week 8: consolidate Cuatro Cycle and 4 Days Deposit into a single mechanic with two variants
Expected KPI impact by end of week 8: - Day 1 retention: roughly 38 to 40% - Bonus cost % GGR: 16 to 17% - STD conversion: 12 to 13%

## Weeks 9 to 10: Reactivation and quests

Week 9: launch redesigned Reactivation ladders (Active + Passive, 7 / 14 / 21+ days)
Week 9: launch Verified-but-no-reacted special case
Week 10: launch remaining quests (Double chance, Silver spin, Steady flow, Triple treat, Reach turnover in 4 random slots)
Week 10: launch Loot boxes and Stickers
Expected KPI impact by end of week 10: - 30-day active ratio: 17.4% toward 21 to 23% - Bonus cost % GGR: 17 to 19%

## Weeks 11 to 12: Cross-cutting and measurement

Week 11: launch the Bonus Shop redesign (tiered catalogue, lifecycle personalization)
Week 11: launch the Referral Program
Week 12: launch Holiday bonus calendar (ready for next holiday)
Week 12: full measurement review against all baseline KPIs
Expected KPI impact by end of week 12: - Day 1 retention: 38 to 42% (target reached) - STD conversion: 13 to 14% - Bonus cost % GGR: 20% (target reached) - 30-day active ratio: 22 to 25% (target reached) - KYC completion: 35 to 40% (target reached) - VIP base: 30 to 45 players (target reached) - Payment success (effective): 65 to 70% (target reached)

# 19. Measurement Framework


## Weekly CRM review (every Monday morning)

Standing agenda:
Headline KPI movement week-over-week
Channel performance (open, click, unsubscribe, frequency cap breaches)
Bonus cost trend and wagering completion rate
All active journeys performance (Day 1 Layer, Post-FTD, Reactivation, Pre-VIP, KYC, Payment)
Assign next week’s experiments

## Bi-weekly stakeholder readout

Headline KPI vs target
Strategic action status
Risks and dependencies
Next 2 weeks’ priorities

## Monthly deep dive

Segmentation health check (are segments still meaningful, is churn score predictive)
Bonus cost by channel and by journey
Cohort retention curves (pre vs post intervention)
VIP pipeline review with the account team

## Tracked KPIs


## Supporting KPIs

SMS open / click rate: maintain 20%+ open, 15%+ click
Email CTOR: maintain 40%+
NC Feed open rate recovery: target 20%+ (currently 11%)
NC Pop-Up show rate: target 15%+ (currently 2.76%)
Web Push opt-in rate: target 40%+
CC earn-to-burn ratio: target 1.0 to 1.2 (currently below 0.3)
Bonus Shop redemption rate: 2x to 3x current within 6 weeks
Frequency cap compliance: 100% (no player exceeds the cap on any given day)

## A/B testing program

Every new journey launches with at least one A/B test. Standard templates:
Minimum 2-week test duration. Minimum 500 players per cell. Significance threshold: 95%.

# 20. Risks and Dependencies


## Platform dependencies


## Operational risks


## Organizational risks


# Appendix A: Data Prerequisites

Before the engagement can measure outcomes, the following data access must be in place:
Player-level transactional data export from GR8 Tech (requested during discovery)
Campaign performance data per channel per campaign (currently available in Tableau, scheduled reports)
Bonus cost breakdown by bonus type and by journey
Segmentation snapshots captured weekly for trend analysis
Predictive churn scores per player, updated daily
Cohort retention curves (requires historical data by registration week)
Real-time event stream access for Day 1 Layer and Payment Failure Recovery triggers

# Appendix B: Tool Configuration Checklist

☐ Smart Segmentation module activated in GR8 Tech
☐ Predictive Churn model activated in GR8 Tech
☐ Web Push channel configured and opt-in flow live
☐ Real-time FTD event trigger validated
☐ Real-time payment failure event trigger validated
☐ Bonus ladder wagering requirements updated (Slots, Live, Sport)
☐ Welcome bonus landing page updated (Lucky Wheel fix, lifecycle personalization)
☐ Bonus Shop SKU catalogue updated (4 tiers, tier locks)
☐ Frequency cap rules configured per segment
☐ Journey calendar central source-of-truth established
☐ Weekly CRM review meeting scheduled
☐ Bi-weekly stakeholder readout scheduled
☐ KPI dashboard built with baseline vs target tracking

# Appendix C: Key Numbers at a Glance

Player base - Total registered: 19,000 - FTD: 4,165 (22.23%) - STD: ~383 (9.20%) - Active 7 days: 1,028 - Active 30 days: 3,298 (17.4%) - VIP I to III combined: 15
Economics - Average deposit: 36,500 ARS (~6 USD) - Deposit frequency: 2.5 per user - Bonus cost: 10.5% of GGR - ADPU matures ~10x from month 0 ($15) to month 5 ($150)
Argentina context - Working rate: ~6,500 ARS per USD - KYC threshold: 471,000 ARS (75 USD) - Payment methods: Mercado Pago, Naranja Betterbro, bank transfer - Product mix: 99.9% casino
Top 10 games (for all FS alignment) 1. Jackpot Joker (TaDa) 2. Joker’s Jewels (PP) 3. 4 Supercharged Clovers (Playson) 4. Gates of Olympus (PP) 5. Joker’s Jewels Cash (PP) 6. Turkish Live Roulette (Ezugi) 7. Gold Party (PP) 8. 3 Coin Volcanoes (3 Oaks) 9. Rush for Gold (3 Oaks) 10. Gates of Olympus 1000 (PP)
End of playbook. Companion to the CuatroBet Argentina CRM architecture board on Miro.

<!-- TABLE 0 -->
| KPI | Baseline | Target | Primary owner |
| --- | --- | --- | --- |
| Day 1 retention | 27.8% | 38 to 42% | Day 1 Retention Layer |
| STD conversion | 9.20% | 13 to 15% | Post-FTD lifecycle + bonus ladder recalibration |
| 30-day active ratio | 17.4% | 22 to 25% | Reactivation + Predictive Churn |
| Bonus cost % GGR | 10.5% | 20% | Bonus Economy restructure |
| Payment success (effective) | 55% | 65 to 70% | Payment Failure Recovery |
| KYC completion | 20% | 35 to 40% | KYC Completion Chain |
| VIP base | 15 players | 30 to 45 | Pre-VIP Lifecycle |


<!-- TABLE 1 -->
| Item | Amount | Cost per player (ARS) |
| --- | --- | --- |
| Grant: 50 FS on Gates of Olympus | 100% claim rate | roughly 80 |
| 100 CC engagement reward (T+6h Comm A) | 40% reach rate | roughly 40 |
| 21,000 ARS urgency bonus (T+6h Comm B) | 30% reach rate | roughly 100 |
| 75% reload email (T+24h) | 20% claim | roughly 150 |
| 10,500 ARS Aviator free bet (T+48h) | 10% claim | roughly 25 |
| Average cost per FTD player |  | roughly 8,000 ARS |


<!-- TABLE 2 -->
| Day | Channel | Offer | Purpose |
| --- | --- | --- | --- |
| 1 | Personal email + in-app | 500 CC + 20 FS + Pre-VIP flag | Activation |
| 3 | Email + banner | 15% weekly cashback enabled | Core Pre-VIP benefit |
| 5 | Email | 60% match up to 208,000 ARS + 30 FS (20x) | First coaching reload |
| 10 | Push + SMS | Soft coaching message, no offer | Awareness |
| 15 | Email + SMS | 100% match up to 416,000 ARS + 50 FS (15x) | Strong second chance |
| 22 | System | Add to Churn Intervention if no Day 21 deposit | Safety net |


<!-- TABLE 3 -->
| Phase | Reward | Reach rate | Cost per enrolled player (ARS) |
| --- | --- | --- | --- |
| Phase 1 email | 10,500 ARS | roughly 60% | 300 |
| Phase 2 phone | 10,500 ARS | roughly 50% | 250 |
| Phase 3 docs (at 15k) | 21,000 ARS | roughly 20% | 200 |
| Phase 3 docs (at 22.5k) | 41,000 ARS | roughly 15% | 300 |
| Total average |  |  | roughly 22,000 ARS per player |


<!-- TABLE 4 -->
| Touch | Cost per attempt | Reach rate |
| --- | --- | --- |
| In-session popup | 0 ARS | 100% |
| 100 CC recovery reward | roughly 900 ARS | 20% of failures |
| Average cost per failure | roughly 250 ARS |  |


<!-- TABLE 5 -->
| Deposit | Match | Max cap | Free spins | Wagering | Validity | Extra |
| --- | --- | --- | --- | --- | --- | --- |
| D1 Welcome | 120% | 208,000 ARS | 50 FS on Gates of Olympus | 25x | 7 days | Max bet 32,000 ARS |
| D2 | 75% | 105,000 ARS | 30 FS on Joker’s Jewels | 20x | 48 h |  |
| D3 | 60% | 105,000 ARS | 30 FS on Jackpot Joker | 20x | 48 h |  |
| D4 | 50% | 126,000 ARS | 40 FS on 4 Supercharged Clovers | 18x | 48 h |  |
| D5 | 50% | 158,000 ARS | 50 FS rotating PP top | 18x | 48 h | 50 CC gift |
| D6 | 50% | 167,000 ARS | 60 FS | 15x | 48 h | Weekly Lucky Wheel entry |
| D7 | 60% | 208,000 ARS | 70 FS | 15x | 48 h | 100 CC gift |
| D8 | 60% | 208,000 ARS | 80 FS | 15x | 72 h | 200 CC gift |
| D9 | 70% | 315,000 ARS | 90 FS | 15x | 72 h | Lucky Wheel premium |
| D10 | 100% | 416,000 ARS | 100 FS | 12x | 72 h | 500 CC + Pre-VIP gate |


<!-- TABLE 6 -->
| Deposit | Match | Max cap | Bonus Cash | Wagering | Validity | Extra |
| --- | --- | --- | --- | --- | --- | --- |
| D1 Welcome | 120% | 208,000 ARS | 105,000 ARS | 30x | 7 days | Bet cap 5,000/hand |
| D2 | 75% | 146,000 ARS | 62,000 ARS | 25x | 48 h |  |
| D3 | 60% | 126,000 ARS | 62,000 ARS | 25x | 48 h |  |
| D4 | 50% | 158,000 ARS | 85,000 ARS | 20x | 48 h |  |
| D5 | 50% | 167,000 ARS | 105,000 ARS | 20x | 48 h | 100 CC |
| D6 | 50% | 208,000 ARS | 105,000 ARS | 20x | 48 h |  |
| D7 | 60% | 251,000 ARS | 126,000 ARS | 18x | 48 h | 200 CC |
| D8 | 60% | 315,000 ARS | 167,000 ARS | 18x | 72 h |  |
| D9 | 75% | 416,000 ARS | 208,000 ARS | 15x | 72 h | Lucky Wheel |
| D10 | 100% | 520,000 ARS | 315,000 ARS | 12x | 72 h | 500 CC + Pre-VIP gate |


<!-- TABLE 7 -->
| Deposit | Match | Max cap | Free Bet | Wagering | Validity | Extra |
| --- | --- | --- | --- | --- | --- | --- |
| D1 Welcome | 120% | 167,000 ARS | 62,000 ARS | 5x | 7 days | Min odds 1.80 |
| D2 | 75% | 105,000 ARS | 41,000 ARS | 5x | 48 h |  |
| D3 | 60% | 85,000 ARS | 41,000 ARS | 5x | 48 h |  |
| D4 | 50% | 105,000 ARS | 53,000 ARS | 5x | 48 h |  |
| D5 | 50% | 126,000 ARS | 62,000 ARS | 5x | 48 h | 50 CC |
| D6 | 50% | 146,000 ARS | 73,000 ARS | 5x | 48 h |  |
| D7 | 60% | 167,000 ARS | 85,000 ARS | 5x | 48 h | 100 CC |
| D8 | 60% | 208,000 ARS | 105,000 ARS | 5x | 72 h |  |
| D9 | 70% | 251,000 ARS | 126,000 ARS | 5x | 72 h | Lucky Wheel |
| D10 | 100% | 315,000 ARS | 167,000 ARS | 5x | 72 h | 500 CC + Pre-VIP gate |


<!-- TABLE 8 -->
| Comm | Timing | Channel | Content and offer |
| --- | --- | --- | --- |
| Comm 1 | T+30 min | In-app popup + Web Push | ES: “Listo para empezar? Reclamá tu 120% + 50 FS ahora”. CTA: deep-link to cashier with welcome bonus preselected. |
| Comm 2 | T+3 h | Email | Subject ES: “Tu bono de bienvenida te está esperando”. Step-by-step deposit guide (Mercado Pago, Naranja, bank transfer), welcome bonus reminder. |
| Comm 3 | T+24 h | SMS | ES 160 chars: “CuatroBet: Todavía no activaste tu bono. 120% + 50 FS te esperan. Tap: [link]” |
| Comm 4 | T+72 h | Email + Web Push | Subject ES: “Última oportunidad: 150% en tu primer depósito”. Enhanced 150% offer, 48 h validity, 25x wagering. |


<!-- TABLE 9 -->
| Comm | Timing | Channel | Content and offer |
| --- | --- | --- | --- |
| Comm 1 | T+5 min | In-session popup (if on site) or Web Push | ES: “Hubo un problema procesando tu depósito. Probá con otro método ahora”. CTA: 3 buttons for Mercado Pago, Naranja Betterbro, bank transfer. |
| Comm 2 | T+30 min | SMS | ES 160 chars: “CuatroBet: Probá de nuevo: [link]. Sumamos 4,100 ARS de regalo por la molestia”. 4,100 ARS no-deposit goodwill credit, no wagering. |
| Comm 3 | T+4 h | Email | Subject ES: “Solucionamos el problema con tu depósito”. Payment methods troubleshooting guide, welcome bonus reminder. |
| Comm 4 | T+24 h | Web Push + NC Feed | ES: “Tu bono 120% + 50 FS te sigue esperando. Probá con Transferencia bancaria” |


<!-- TABLE 10 -->
| Comm | Timing | Channel | Content and offer |
| --- | --- | --- | --- |
| Comm 1 | T+15 min | SMS + auto-ticket | ES: “CuatroBet: Un agente va a contactarte en 1 hora para ayudarte a depositar”. Auto-create priority ticket for payments team. |
| Comm 2 | T+1 h | Email (personal, “María, equipo CuatroBet”) | Subject ES: “Podemos ayudarte a depositar”. Offer callback or WhatsApp support, 3 alternate methods, 10,500 ARS goodwill credit. |
| Comm 3 | T+6 h | SMS | ES: “Responde RETRY y te llamamos, o probá acá: [link]”. 10,500 ARS credit still valid. |
| Comm 4 | T+24 h | Email | Subject ES: “Último intento, con una solución específica”. Diagnosis if available, escalation to CRM manual outreach for Pre-VIP and High tiers. |


<!-- TABLE 11 -->
| Comm | Timing | Channel | Content and offer |
| --- | --- | --- | --- |
| Comm 1 | T+5 min real-time | In-session popup | ES: “Tu banco rechazó el depósito. Probá con otro método: Mercado Pago, Naranja, Transferencia”. 3 buttons preselecting alternate methods. |
| Comm 2 | T+1 h | SMS | ES: “Tu banco rechazó el depósito. Probá con [next most-used method]: [link]”. Method swap based on user history. |
| Comm 3 | T+6 h | Email | Subject ES: “Guía rápida: métodos de pago en CuatroBet”. Troubleshooting per method. |
| Comm 4 | T+24 h | Web Push + SMS | ES SMS: “CuatroBet: Tu bono sigue vigente. Probá con Transferencia bancaria” |


<!-- TABLE 12 -->
| Comm | Timing | Channel | Content |
| --- | --- | --- | --- |
| Comm 1 | T+0 automatic | System + Email | Standard security hold notice, account temporarily limited, instructions to contact support. Compliance mandatory. |
| Comm 2 | T+1 h | Email (personal, “María, Seguridad CuatroBet”) | Subject ES: “Tu cuenta requiere verificación”. KYC escalation, personal contact, document list. Route into KYC Phase 3 if not completed. |
| Comm 3 | T+24 h if unresolved | SMS | ES: “CuatroBet: Para continuar, enviá tus documentos acá: [link]. Soporte: [phone]” |
| Comm 4 | T+72 h if unresolved | Email | Subject ES: “Resolución de tu caso de seguridad”. Final decision notice (unblocked or closed), next steps. |


<!-- TABLE 13 -->
| Comm | Timing | Channel | Content and offer |
| --- | --- | --- | --- |
| Comm 1 | T+1 h | In-session popup + Web Push | ES: “Tu bono de bienvenida 120% + 50 FS está listo. Reclamalo ahora”. CTA auto-applies bonus. |
| Comm 2 | T+12 h | Email | Subject ES: “Reclamá tu bono de bienvenida antes de que venza”. Quick-start deposit guide, bonus terms. |
| Comm 3 | T+48 h | SMS | ES 160 chars: “CuatroBet: Tu bono 120% + 50 FS vence en 24h. Reclamalo: [link]” |
| Comm 4 | T+72 h | Email enhanced | Subject ES: “Última oportunidad: 140% en tu primer depósito”. Enhanced 140% offer, 48 h validity. |


<!-- TABLE 14 -->
| Comm | Timing | Channel | Content and offer |
| --- | --- | --- | --- |
| Comm 1 | T+24 h | Email | Subject ES: “Bienvenido a CuatroBet. Explorá nuestra biblioteca de juegos”. Top games showcase, 10,500 ARS no-deposit Aviator free bet at the end (1x wagering). |
| Comm 2 | T+7 days | Email | Subject ES: “Novedades en CuatroBet esta semana”. New games, tournaments, soft reminder of the 10,500 ARS free bet. |
| Comm 3a | T+14 days, track A | Web Push + NC Feed | ES: “Girá la Lucky Wheel. Entrada gratis esta semana”. Free Lucky Wheel spin, prizes 50 to 41,000 ARS. |
| Comm 3b | T+14 days, track B (opens but doesn’t click) | Email | Subject ES: “Tu juego favorito te está esperando” (AI-personalized). No offer, pure discovery. |
| Comm 4 | T+30 days | Email + SMS | Subject ES: “Recarga única: 50% sin letra chica”. 50% match up to 41,000 ARS, 15x wagering, 72 h expiry. |


<!-- TABLE 15 -->
| Comm | Timing | Channel | Content |
| --- | --- | --- | --- |
| Comm 1 | T+30 min | Web Push or Web Push | ES: “Gracias por visitarnos. Tu bono 120% + 50 FS te está esperando”. Deep-link to homepage with welcome modal. |
| Comm 2 | T+2 h | Email | Subject ES: “Encontraste lo que buscabas?”. Top 5 games, simple onboarding. |
| Comm 3 | T+24 h | Email | Subject ES: “Nuevos juegos en CuatroBet esta semana”. Curated top slots, hero banner Jackpot Joker. |
| Comm 4 | T+72 h | SMS | ES: “CuatroBet: Empezá con 120% + 50 FS. Depositar: [link]” |


<!-- TABLE 16 -->
| Comm | Timing | Channel | Content |
| --- | --- | --- | --- |
| Comm 1 | At session end | In-app popup | ES: “Te gustaron los juegos? Tu bono de bienvenida te da 120% + 50 FS para jugar en serio” |
| Comm 2 | T+2 h | Web Push | ES: “Tu bono sigue disponible. Mercado Pago acepta desde 10,500 ARS” |
| Comm 3 | T+24 h | Email | Subject ES: “Cómo depositar en 2 minutos”. Step-by-step walkthrough with screenshots. |
| Comm 4 | T+72 h | SMS | ES: “CuatroBet: Reclamá tu 120% + 50 FS antes de que venza: [link]” |


<!-- TABLE 17 -->
| Comm | Timing | Channel | Content |
| --- | --- | --- | --- |
| Comm 1 | At free spins end | In-app popup | ES: “Listo para jugar en serio? Tu bono 120% + 50 FS te da mucho más” |
| Comm 2 | T+2 h | Email | Subject ES: “Ganaste. Ahora desbloqueá tu bono de bienvenida”. Celebrate, top games list. |
| Comm 3 | T+24 h | Web Push | ES: “Tu bono 120% + 50 FS te espera. Depositá desde 10,500 ARS” |
| Comm 4 | T+72 h | SMS | ES: “CuatroBet: 120% + 50 FS antes de que venza: [link]” |


<!-- TABLE 18 -->
| Comm | Timing | Channel | Content and offer |
| --- | --- | --- | --- |
| Comm 1 | 3 days before | Email | Subject ES: “Tu aniversario con CuatroBet se acerca”. Teaser, stats from the past year. |
| Comm 2 | Day of | Email + Web Push | Subject ES: “Feliz aniversario! Tu regalo te espera”. 100% reload up to 208,000 ARS + 100 FS on favorite game, 15x wagering, 7 days. |
| Comm 3 | Day after (if not claimed) | SMS | ES: “Tu regalo de aniversario CuatroBet te espera hasta el [fecha]: [link]” |
| Comm 4 | 3 days after | Email | Subject ES: “Último llamado: tu regalo de aniversario”. Final reminder. |


<!-- TABLE 19 -->
| Comm | Timing | Channel | Content and offer |
| --- | --- | --- | --- |
| Comm 1 | 3 days before | Email | Subject ES: “Tu cumpleaños se acerca”. 50 no-deposit free spins on favorite slot. |
| Comm 2 | Day of | Email + Web Push + SMS | Subject ES: “Feliz cumpleaños!”. 105,000 ARS wager-free cash + 50 FS on Gates of Olympus. |
| Comm 3 | Day after | Email | Subject ES: “Gracias por pasar tu cumpleaños con nosotros”. Warm message, 7-day validity reminder. |
| Comm 4 | 7 days after | Web Push | ES: “Tu regalo de cumpleaños vence hoy. Reclamalo: [link]” |


<!-- TABLE 20 -->
| Comm | Timing | Channel | Content and offer |
| --- | --- | --- | --- |
| Comm 1 | Day 1 | Email + NC Feed | Subject ES: “Empezó la temporada de [signo]”. Themed landing page, themed slot recommendations. |
| Comm 2 | Day 3 | Web Push | 50% match up to 105,000 ARS + 30 FS on themed slots, 20x wagering. |
| Comm 3 | Day 10 | Email | Mid-period reminder, optional themed leaderboard. |
| Comm 4 | Day 20 | SMS | ES: “La temporada de [signo] vence pronto. Reclamá tu bono: [link]” |


<!-- TABLE 21 -->
| Tier | Probability | Reward options |
| --- | --- | --- |
| Common | 60% | 2,100 ARS cash or 20 CC or 5 FS |
| Uncommon | 25% | 10,500 ARS cash or 50 CC or 15 FS |
| Rare | 10% | 32,000 ARS cash or 150 CC or 30 FS premium |
| Epic | 4% | 105,000 ARS cash or 500 CC or Lucky Wheel spin |
| Legendary | 1% | 315,000 ARS cash or VIP I preview |


<!-- TABLE 22 -->
| Deposit in window | Reward |
| --- | --- |
| D1 | 25 CC + 10 FS on Jackpot Joker |
| D2 | 50 CC + 20 FS on Joker’s Jewels |
| D3 | 75 CC + 30 FS on Gates of Olympus |
| D4 | 150 CC + 60 FS + 1 free Lucky Wheel spin |


<!-- TABLE 23 -->
| Tier | Reward range |
| --- | --- |
| Silver | 50 to 10,500 ARS cash, or 5 to 20 FS, or 10 to 50 CC |
| Gold | 200 to 41,000 ARS cash, or 20 to 80 FS, or 50 to 200 CC |
| Platinum | 1,000 to 315,000 ARS cash, or Lucky Wheel entry, or VIP I preview |


<!-- TABLE 24 -->
| Deposit size × 4 | Reward |
| --- | --- |
| 4 × 21,000 ARS | 10,500 ARS cashback + 20 FS |
| 4 × 53,000 ARS | 32,000 ARS cashback + 40 FS + 100 CC |
| 4 × 105,000 ARS | 85,000 ARS cashback + 80 FS + 250 CC |
| 4 × 208,000 ARS | 208,000 ARS cashback + 150 FS + 500 CC + Lucky Wheel |


<!-- TABLE 25 -->
| Day | Reward |
| --- | --- |
| Day 1 | 10 CC + 5 FS |
| Day 2 consecutive | 30 CC + 15 FS |
| Day 3 consecutive | 100 CC + 50 FS + 41,000 ARS bonus cash |


<!-- TABLE 26 -->
| Committed amount × 4 | Reward |
| --- | --- |
| 4 × 32,000 ARS | 32,000 ARS cashback + 30 FS |
| 4 × 62,000 ARS | 85,000 ARS cashback + 60 FS + 150 CC |
| 4 × 105,000 ARS | 167,000 ARS cashback + 100 FS + 300 CC + Lucky Wheel |
| 4 × 208,000 ARS | 416,000 ARS cashback + 200 FS + 750 CC + Pre-VIP preview |


<!-- TABLE 27 -->
| Tier | Total turnover across 4 slots | Reward |
| --- | --- | --- |
| Light | 416,000 ARS | 10,500 ARS cashback + 20 FS |
| Medium | 1,040,000 ARS | 41,000 ARS cashback + 50 FS + 100 CC |
| Heavy | 3,130,000 ARS | 167,000 ARS cashback + 100 FS + 300 CC + Lucky Wheel |


<!-- TABLE 28 -->
| Tier | Criteria | Offer |
| --- | --- | --- |
| Low | 1 deposit in last 7 days | 40% up to 62,000 ARS + 20 FS, 15x |
| Mid | 2 to 3 deposits | 50% up to 105,000 ARS + 30 FS + 50 CC, 15x |
| High | 4+ deposits | 60% up to 167,000 ARS + 50 FS + 100 CC, 12x |
| Pre-VIP/VIP | Status | 75% up to 315,000 ARS + 75 FS + 200 CC + cashback boost, 10x |


<!-- TABLE 29 -->
| Day | Reward |
| --- | --- |
| 1 | 10 CC |
| 2 | 20 CC + 5 FS |
| 3 | 30 CC + 10 FS |
| 4 | 50 CC + 20 FS + 2,100 ARS |
| 5 | 75 CC + 25 FS + 5,000 ARS |
| 6 | 100 CC + 40 FS + 10,500 ARS |
| 7 (weekly reset) | 200 CC + 60 FS + 32,000 ARS + Lucky Wheel |


<!-- TABLE 30 -->
| Holiday | Date | Headline offer |
| --- | --- | --- |
| New Year | Jan 1 | 150% up to 315,000 ARS + 150 FS |
| Carnaval | Feb/Mar (varies) | 100% + themed slot bonuses |
| Día del Trabajador | May 1 | 75% day-off reload |
| Revolución de Mayo | May 25 | 50% patriotic reload |
| Día de la Independencia | Jul 9 | 100% independence match |
| Día del Niño | August, 3rd Sunday | Family-friendly themed slots |
| Día de la Madre | October, 3rd Sunday | Cashback emphasis |
| Día de la Tradición | Nov 10 | Gaucho-themed slot selection |
| Navidad | Dec 24 to 25 | 12-day advent calendar daily rewards |
| Fin de Año | Dec 31 | New Year’s Eve mega offer |


<!-- TABLE 31 -->
| Comm | Timing | Channel | Content |
| --- | --- | --- | --- |
| Comm 1 | Weekly Monday | Email + dashboard card | “Your week in CuatroBet Rewards”. XP earned, CC balance, missions completed, progress bar toward next tier, top 3 bonus shop items. |
| Comm 2 | Bi-weekly Thursday | Web Push | “Tu bonus shop tiene items nuevos” with personalized top 3 SKUs. Drives shop redemption. |
| Comm 3 | Monthly (tier milestone) | Email | “Alcanzaste [tier]” or “Estás cerca de [next tier]”. Tier benefits reminder, exclusive perks preview. |
| Comm 4 | Monthly exclusive | Email + Web Push | “Evento exclusivo para [tier]”. Invitation to a loyalty-only tournament or giveaway. |


<!-- TABLE 32 -->
| Comm | Timing | Channel | Content and offer |
| --- | --- | --- | --- |
| Comm 1 | Day 8 since last mission | Email | Subject: “Estás a X misiones de [next tier]”. Concrete tier progression, list of easy missions available today. |
| Comm 2 | Day 10 | Web Push + NC Feed | ES: “No pierdas tu progreso. Completá una misión hoy y ganá 50 CC extra”. 50 CC bonus on next mission. |
| Comm 3 | Day 14 | Email + SMS | 40% reload up to 62,000 ARS + 100 CC + 20 FS, 15x wagering, 72 h. |
| Comm 4 | Day 21 | Email | Subject: “Advertencia de bajada de tier”. Loss aversion frame, strongest offer: 75% match + 50 FS + 200 CC + tier protection. |


<!-- TABLE 33 -->
| Value tier | Lifetime deposits | Offer multiplier | Additional treatment |
| --- | --- | --- | --- |
| Micro | 0 to 105,000 ARS | 0.5x (or swap for CC-only gift) | Low return probability, protect budget |
| Low | 5,000 to 625,000 ARS | 1.0x (base) | Standard reactivation offer |
| Mid | 30,000 to 3,130,000 ARS | 1.5x | Stronger pull, same channel mix |
| High | 150,000 to 12,520,000 ARS | 2.0x | Personal email from CRM owner name (not brand) |
| Pre-VIP and above | above 12,520,000 ARS or Pre-VIP flag | 2.5x | WhatsApp outreach plus manager escalation |


<!-- TABLE 34 -->
| Comm | Day | Channel | Content and offer |
| --- | --- | --- | --- |
| 1 | Day 7 | SMS | ES: “Te extrañamos. 30% en tu próximo depósito + 20 FS en Jackpot Joker: [link]”. 30% match up to 41,000 ARS + 20 FS, 15x, 48 h. |
| 2 | Day 8 | Email | Subject: “Novedades en CuatroBet esta semana”. Top games, tournaments, bonus reminder at bottom. |
| 3 | Day 9 | Web Push | ES: “100 CC de regalo si volvés a jugar hoy”. 100 CC no-deposit, no wagering. |
| 4 | Day 10 | NC Feed + Web Push | Lucky Wheel free spin invitation, no deposit. |


<!-- TABLE 35 -->
| Comm | Day | Channel | Content and offer |
| --- | --- | --- | --- |
| 1 | 14 | Email (personal tone) | Subject: “Nota personal de CuatroBet”. 50% up to 105,000 ARS + 30 FS on favorite game, 15x, 72 h. |
| 2 | 15 | SMS | ES: “Tu bono 50% + 30 FS te espera. Vence mañana: [link]” |
| 3 | 16 | Web Push | Gamification entry (Lucky Wheel or 4 Deposit Quest pitch). |
| 4 | 18 | Email | Subject: “Tu bono 50% terminó pero tenemos algo nuevo”. Fresh 60% up to 126,000 ARS + 40 FS + 100 CC, 72 h. |


<!-- TABLE 36 -->
| Comm | Day | Channel | Content and offer |
| --- | --- | --- | --- |
| 1 | 21 | Email (from CRM owner name) | Subject: “Construimos algo que te va a encantar”. Personal tone, curated game recommendation. 75% up to 208,000 ARS + 50 FS + 250 CC, 12x, 72 h. For Pre-VIP+: 100% match + cashback boost. |
| 2 | 25 | SMS + Email | ES: “CuatroBet: Tu 75% + 50 FS sigue disponible hasta [fecha]: [link]” |
| 3 | 28 | WhatsApp (Pre-VIP+) or Web Push (others) | Personal outreach for high-value, automated push for others. |
| 4 | 30 | Email | Subject: “Último llamado”. Escalated 100% up to 315,000 ARS + 75 FS + 500 CC, 15x, 48 h. |


<!-- TABLE 37 -->
| Comm | Day | Channel | Content and offer |
| --- | --- | --- | --- |
| 1 | 7 | Email | Subject: “Tus juegos favoritos te esperan”. 25% up to 32,000 ARS + 15 FS, 15x, 72 h. |
| 2 | 8 | Web Push | 50 CC gift, no deposit. |
| 3 | 9 | NC Feed | Lucky Wheel preview. |
| 4 | 10 | SMS | ES: “CuatroBet: 25% + 15 FS hasta hoy: [link]” |


<!-- TABLE 38 -->
| Comm | Day | Channel | Content and offer |
| --- | --- | --- | --- |
| 1 | 14 | Email | 35% up to 53,000 ARS + 20 FS, 15x, 72 h. |
| 2 | 15 | Web Push | Bonus reminder. |
| 3 | 16 | Email | Game showcase, no offer. |
| 4 | 18 | SMS | Final 72 h push. |


<!-- TABLE 39 -->
| Comm | Day | Channel | Content and offer |
| --- | --- | --- | --- |
| 1 | 21 | Email | 50% up to 85,000 ARS + 25 FS + 100 CC, 15x, 72 h. |
| 2 | 25 | SMS | Reminder. |
| 3 | 28 | Web Push | Reminder. |
| 4 | 30 | Email | Final 60% up to 105,000 ARS + 30 FS, 48 h. |


<!-- TABLE 40 -->
| Comm | Timing | Channel | Content and offer |
| --- | --- | --- | --- |
| 1 | T+0 after verification | Email | Subject: “Bienvenido! Tu cuenta está totalmente verificada”. Celebrate verification, deposit guide, enhanced welcome 150% up to 251,000 ARS + 75 FS, 20x. |
| 2 | T+24 h | SMS | ES: “CuatroBet: Tu cuenta está verificada. 150% + 75 FS te esperan: [link]” |
| 3 | T+72 h | Email + Web Push | Address friction (payment methods walkthrough, deposit amount flexibility, trust signals). |
| 4 | T+7 days | Email | Subject: “Todo bien con tu cuenta?”. Empathy-led, offer WhatsApp/phone support, final bonus reminder. |


<!-- TABLE 41 -->
| Channel | Current daily | Target daily | Primary use |
| --- | --- | --- | --- |
| SMS | 1,200 | 4,000 to 5,000 | Time-sensitive retention, Day 1 Layer, Reactivation, personal VIP |
| Email | 1,150 | 3,000 to 4,000 | Detailed offers, Pre-VIP coaching, loyalty updates |
| NC Feed | 25,700 | 8,000 to 10,000 | COOL aggressively, only active players |
| NC Pop-Up | 21,400 | 5,000 | COOL aggressively, only high-value triggers |
| Web Push | 0 | 3,000 to 5,000 | ACTIVATE, Day 1 Layer, Post-FTD, Pre-VIP |
| Web Push | negligible | keep low | Fallback for email opt-outs |


<!-- TABLE 42 -->
| Segment | Max commercial messages per day |
| --- | --- |
| All players (default) | 4 |
| Day 1 Layer active (first 72h) | 6 |
| Pre-VIP and VIP | No cap (manager approval required) |
| At-risk (churn score above 60) | 3 |
| Dormant 15+ days | 2 per week |


<!-- TABLE 43 -->
| Lifecycle stage | Primary channels |
| --- | --- |
| Registration + KYC | In-app popup, Email, SMS (post-phone verification) |
| Day 1 Retention (0 to 72h) | In-session popup, SMS, Web Push |
| Post-FTD to STD | Email, SMS, Web Push, sparing NC Feed |
| Regular player | Email, Web Push, NC Feed (properly segmented) |
| Pre-VIP | Personal Email (CRM owner), SMS, WhatsApp |
| VIP I to IV | Personal Email, WhatsApp, SMS, phone call |
| Reactivation | SMS first, then Email, escalating by tier |
| Payment Failure | In-session popup, SMS, Email |


<!-- TABLE 44 -->
| CC | Reward |
| --- | --- |
| 10 | 2,100 ARS site credit, no wagering |
| 20 | 5 Free Spins on Jackpot Joker |
| 20 | 5 Free Spins on Joker’s Jewels |
| 25 | 1 Free Flight on Aviator |
| 30 | 6,500 ARS free bet (sport) |
| 40 | 10 Free Spins on Gates of Olympus |


<!-- TABLE 45 -->
| CC | Reward |
| --- | --- |
| 50 | 15 FS on weekly rotating PP top slot |
| 60 | 5 Free Flights on Aviator |
| 80 | 21,000 ARS site credit (10x wagering) |
| 100 | 25 FS on 4 Supercharged Clovers |
| 120 | 41,000 ARS site credit (10x wagering) |
| 150 | 30% match up to 62,000 ARS on any deposit |


<!-- TABLE 46 -->
| CC | Reward |
| --- | --- |
| 200 | 50% match up to 105,000 ARS + 20 FS on top game |
| 250 | 10 Free Flights on Aviator + 100 CC bonus |
| 300 | 62,000 ARS free bet + 10,500 ARS cashback |
| 350 | 75% match up to 167,000 ARS + 30 FS |
| 400 | 100% match up to 208,000 ARS (15x wagering) |


<!-- TABLE 47 -->
| CC | Reward |
| --- | --- |
| 500 | Wager-free 53,000 ARS bonus |
| 800 | VIP 100% reload up to 520,000 ARS (10x wagering) |
| 1,200 | 105,000 ARS pure cash, wager-free, instant withdrawal |
| 2,000 | Physical reward (Apple / gadget from VIP closed draws) |


<!-- TABLE 48 -->
| Player stage | Visible tiers |
| --- | --- |
| Registered (pre-FTD) | Entry only, with aspirational teaser |
| FTD to STD | Entry + Standard, “Unlock more after your second deposit” banner |
| Regular | Entry + Standard + Premium (locked) with loyalty tier requirement |
| Premium loyalty+ | Entry + Standard + Premium unlocked |
| Pre-VIP | VIP tier visible but locked, “Reach VIP I to unlock” |
| VIP I to IV | Full catalogue unlocked |


<!-- TABLE 49 -->
| Event | Referrer reward | Referred reward |
| --- | --- | --- |
| Referred player registers | 50 CC (immediate tracking nudge) | Standard 120% welcome bonus |
| Referred player FTD | 200 CC | Enhanced welcome at 140% (vs standard 120%) |
| Referred player STD | 41,000 ARS cash (wager-free) + 100 CC | Nothing extra (already boosted) |
| Referred player reaches 5 deposits | 105,000 ARS cash (wager-free) + Lucky Wheel spin | Nothing extra |


<!-- TABLE 50 -->
| Tier | Range (ARS) | Range (USD approx) |
| --- | --- | --- |
| Micro | 0 to 5,000 | 0 to 17 |
| Low | 5,000 to 30,000 | 17 to 100 |
| Mid | 30,000 to 150,000 | 100 to 500 |
| High | 150,000 to 600,000 | 500 to 2,000 |
| VIP | above 600,000 | above 2,000 |


<!-- TABLE 51 -->
| KPI | Baseline | 6-week target | 12-week target | Owner |
| --- | --- | --- | --- | --- |
| Day 1 retention | 27.8% | 34% | 38 to 42% | Day 1 Layer |
| STD conversion | 9.20% | 11.5% | 13 to 15% | Post-FTD + Ladder |
| 30-day active ratio | 17.4% | 20% | 22 to 25% | Reactivation + Churn |
| Bonus cost % GGR | 10.5% | 15% | 20% | Bonus Economy |
| Payment success effective | 55% | 60% | 65 to 70% | Payment Recovery |
| KYC completion | 20% | 28% | 35 to 40% | KYC Chain |
| VIP base (players) | 15 | 25 | 30 to 45 | Pre-VIP |
| ADPU Casino | roughly $8 | support ramp | $13 to $16 | Retention core |


<!-- TABLE 52 -->
| Test type | Example | Measurement |
| --- | --- | --- |
| Offer amount | 50% match vs 60% match | STD rate, bonus cost |
| Wagering requirement | 15x vs 20x | Wagering completion rate |
| Channel | SMS vs Web Push | Open / click / deposit rate |
| Timing | T+30 min vs T+2 h | Conversion rate |
| Copy tone | Urgency vs warmth | Click-through rate |
| Gamification | 4 Deposit Quest on vs off | STD conversion, ADPU |


<!-- TABLE 53 -->
| Dependency | Risk | Mitigation |
| --- | --- | --- |
| GR8 Tech real-time event triggers | Day 1 Layer requires sub-5-second latency on FTD success event | Confirm with GR8 Tech account team in week 1, escalate if not available |
| Smart Segmentation module activation | Blocks all lifecycle routing | Request in week 1, have fallback manual segmentation ready |
| Predictive Churn model | Blocks early Reactivation entry | Request in week 1, launch reactive ladder first, add predictive overlay later |
| Raw player-level data export | Needed for A/B test analysis and cohort curves | Requested during discovery, follow up week 1 |
| Web Push channel setup | Requires platform configuration and app update | Begin week 1, allow 3 to 4 weeks for rollout |


<!-- TABLE 54 -->
| Risk | Likelihood | Impact | Mitigation |
| --- | --- | --- | --- |
| Payment success rate remains low | Medium | High (caps all downstream KPIs) | Work with payments team in parallel, Payment Failure Recovery is a ceiling not a fix |
| Channel fatigue persists on NC Feed | Low | Medium | Aggressive cooling plan, monitor weekly, kill switch rule |
| Welcome bonus wagering change triggers bonus abuse | Low | Medium | Bet caps, wagering contribution rules, max bonus balance cap, bonus abuse monitoring |
| Pre-VIP cohort smaller than expected | Medium | Low | Lower the 3,130,000 ARS threshold after 4 weeks if needed |
| KYC rejection rate high | Medium | Medium | Monitor rejection reasons weekly, operational team owns document review SLA |


<!-- TABLE 55 -->
| Risk | Mitigation |
| --- | --- |
| CRM standup discipline slips | Dedicated weekly agenda, bi-weekly stakeholder readout forcing function |
| Conflicting campaigns across journeys | Frequency cap compliance enforced at platform level, single journey calendar |
| CRM owner turnover during engagement | Document every journey fully in this playbook, cross-train CRM team |
| Stakeholder fatigue on weekly reports | Bi-weekly (not weekly) readouts to stakeholders, weekly review stays internal |
