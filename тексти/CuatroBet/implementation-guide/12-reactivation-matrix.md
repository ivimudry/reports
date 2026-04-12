# 12 — Reactivation Matrix — Implementation Guide

**Chain:** Reactivation (2 Engagement Histories × 3 Time Buckets × 4 Comms + Value Tier Overlay + VNR Special Case)  
**Priority:** Phase 2 (Week 5–6)  
**Total Base Comms:** 24 + 4 (VNR) = 28 communications  
**Depends on:** Predictive Churn model, value tier segmentation, all channels active

---

## STEP 0: PRE-FLIGHT CHECKLIST

- [ ] Predictive Churn model active (early entry at day 3–4 for high-risk)
- [ ] Player value tiers segmented: Micro / Low / Mid / High / Pre-VIP+
- [ ] Behavioral engagement filter available: High / Low / Zero engagement
- [ ] All channels active: SMS, Email, In-app popup, Push, Feed
- [ ] Reactivation bonus templates configured (see Section F)
- [ ] Deep link to deposit page functional
- [ ] Gift/manual credit API available for escalation offers

---

## MATRIX STRUCTURE

```
              │  7-Day Dormant  │ 14-Day Dormant │ 21+ Day Dormant │
──────────────┼─────────────────┼────────────────┼─────────────────│
Active History│  4 comms        │  4 comms       │  4 comms        │
──────────────┼─────────────────┼────────────────┼─────────────────│
Passive Hist. │  4 comms        │  4 comms       │  4 comms        │
──────────────┴─────────────────┴────────────────┴─────────────────┘
                                + VNR Special Case (4 comms)
                                + Value Tier Overlay (multiplier)
                                + Behavioral Filter Overlay
```

---

## SEGMENT DEFINITIONS

### Engagement History

**Active History (AH):**
```
deposit_count ≥ 3
AND total_wagered_ars ≥ 15,000 ARS
AND sessions_30d_before_dormancy ≥ 5
```

**Passive History (PH):**
```
deposit_count < 3
OR total_wagered_ars < 15,000 ARS
OR sessions_30d_before_dormancy < 5
```

### Time Buckets (from last login)

| Bucket | Entry | Description |
|--------|-------|-------------|
| 7-Day | `last_login` 7–13 days ago | Early dormancy |
| 14-Day | `last_login` 14–20 days ago | Mid dormancy |
| 21+ Day | `last_login` ≥ 21 days ago | Deep dormancy |

### Value Tier Overlay (adjusts offer amounts)

| Value Tier | Deposit Range (lifetime) | Offer Multiplier |
|-----------|--------------------------|-----------------|
| Micro | < 5,000 ARS | 0.5× |
| Low | 5,000–25,000 ARS | 1× (base) |
| Mid | 25,001–75,000 ARS | 1.5× |
| High | 75,000–200,000 ARS | 2× |
| Pre-VIP+ | > 200,000 ARS | 3× (+ personal outreach) |

### Behavioral Filter Overlay

| Filter | Definition | Channel Adjustment |
|--------|-----------|-------------------|
| High engagement | Opened ≥3 comms in last 30 active days | Use email + push |
| Low engagement | Opened 1–2 comms in last 30 active days | Lead with SMS |
| Zero engagement | Opened 0 comms in last 30 active days | SMS only, then phone call for High+ value |

---

## A. ACTIVE HISTORY — 7-DAY DORMANT

**Journey Name:** `12-AH-7D-JOURNEY`  
**Entry:** `last_session_date > 7 days` AND Active History = true AND Predictive Churn flag optional (can enter at day 3–4)

### AH-7D-C1: Soft Check-In (Day 7 or Churn prediction trigger)

| Setting | Value |
|---------|-------|
| Campaign ID | `12-AH-7D-C1-EMAIL` |
| Channel | Email (High/Low engagement) or SMS (Zero engagement) |
| Subject (ES) | `🔔 {first_name}, algo nuevo te espera` |

**Email Content:**
- **Subject (ES):** `🔔 {first_name}, algo nuevo te espera`
- **Preheader (ES):** `Descubrí qué cambió desde tu última visita`
- **Banner Text (ES):** `Algo Nuevo Te Espera`
- **Banner Description:** Soft check-in — personalized game recommendation visual, cashback badge, "we noticed you've been away" friendly tone, warm welcoming colors
- **Body Description:** Soft engagement (no bonus yet). Show personalized game recommendation with new features. Remind active cashback. Friendly "your account is waiting" message.
- **CTA (ES):** `Ver novedades` → Homepage

---

### AH-7D-C2: Light Incentive (Day 9)

| Setting | Value |
|---------|-------|
| Campaign ID | `12-AH-7D-C2-PUSH-SMS` |
| Channel | Push (High engagement) / SMS (Low/Zero) |
| Condition | No login since C1 |

**SMS (ES):**
```
CuatroBet: {first_name}, tenés {free_spins_count} giros gratis esperándote. Válidos 48h: {link}
```

**Base offer:** 10 FS (× value tier multiplier)

---

### AH-7D-C3: Escalated Offer (Day 11)

| Setting | Value |
|---------|-------|
| Campaign ID | `12-AH-7D-C3-EMAIL-SMS` |
| Channel | Email + SMS |
| Condition | No login since C2 |
| Subject (ES) | `💰 {bonus_pct}% extra en tu próximo depósito` |

**Email Content:**
- **Subject (ES):** `💰 {bonus_pct}% extra en tu próximo depósito`
- **Preheader (ES):** `Oferta exclusiva por tiempo limitado, {first_name}`
- **Banner Text (ES):** `{bonus_pct}% Extra Para Vos`
- **Banner Description:** Escalated offer — large "{bonus_pct}%" text overlay, reload match visual, deposit coins, urgency amber/gold tone
- **Body Description:** Escalated reload match offer: {bonus_pct}% up to 3,000 ARS (× value tier multiplier). Show how to deposit. Urgency: limited time.

**Base offer:** 30% reload match up to 3,000 ARS (× value tier multiplier)

---

### AH-7D-C4: Final Push (Day 13)

| Setting | Value |
|---------|-------|
| Campaign ID | `12-AH-7D-C4-SMS` |
| Channel | SMS |
| Condition | No login since C3 |

**SMS (ES):**
```
CuatroBet: {first_name}, última oportunidad: {bonus_pct}% + {fs_count} giros. Vence mañana. {link}
```

**Base offer:** 50% reload + 20 FS (× value tier multiplier)  
**Pre-VIP+ addition:** Personal phone call from CRM manager.

**Exit:** If no login → Move to 14-Day bucket.

---

## B. ACTIVE HISTORY — 14-DAY DORMANT

**Journey Name:** `12-AH-14D-JOURNEY`  
**Entry:** Falls through from 7-Day without login

### AH-14D-C1: "We Miss You" (Day 14)

| Setting | Value |
|---------|-------|
| Campaign ID | `12-AH-14D-C1-EMAIL` |
| Channel | Email |
| Subject (ES) | `💳 {cc_balance} CC y cashback sin reclamar` |

**Email Content:**
- **Subject (ES):** `💳 {cc_balance} CC y cashback sin reclamar`
- **Preheader (ES):** `{first_name}, tus premios están esperando en tu cuenta`
- **Banner Text (ES):** `{cc_balance} CC + {cashback} ARS Sin Reclamar`
- **Banner Description:** Unredeemed value alert — CC coins pile + cashback amount prominently displayed, fading/urgency visual, "claim before it's gone" ribbon
- **Body Description:** Show accumulated unredeemed CC balance and cashback. Urgency framing — value waiting to be claimed. Breakdown of what they can redeem.

---

### AH-14D-C2: Significant Bonus (Day 16)

| Setting | Value |
|---------|-------|
| Campaign ID | `12-AH-14D-C2-SMS` |
| Channel | SMS |

**SMS (ES):**
```
CuatroBet: {first_name}, bono especial de bienvenida: {bonus_ars} ARS gratis. Sin depósito. 48h: {link}
```

**Base offer:** 500 ARS no-deposit bonus (× value tier multiplier)  
**Wagering:** 15× before withdrawal

---

### AH-14D-C3: Exclusive Access (Day 18)

| Setting | Value |
|---------|-------|
| Campaign ID | `12-AH-14D-C3-EMAIL-PUSH` |
| Channel | Email + Push |
| Subject (ES) | `🏆 Acceso exclusivo: torneo privado para vos` |

**Email Content:**
- **Subject (ES):** `🏆 Acceso exclusivo: torneo privado para vos`
- **Preheader (ES):** `Solo jugadores seleccionados fueron invitados`
- **Banner Text (ES):** `Torneo Privado Exclusivo`
- **Banner Description:** VIP tournament invitation — exclusive golden ticket visual, tournament trophy, prize pool amount displayed, premium dark/gold design
- **Body Description:** Exclusive tournament entry. For standard players: 1,000 ARS prize pool. For Pre-VIP+: personal VIP manager invitation + 5,000 ARS tournament.

**Offer:** Entry to exclusive tournament + 1,000 ARS prize pool  
**For Pre-VIP+:** Personal invitation from VIP manager + 5,000 ARS tournament

---

### AH-14D-C4: "Door Closing" (Day 20)

| Setting | Value |
|---------|-------|
| Campaign ID | `12-AH-14D-C4-SMS` |
| Channel | SMS |

**SMS (ES):**
```
CuatroBet: {first_name}, tu oferta de {bonus_ars} ARS + {fs_count} giros vence hoy. No la pierdas: {link}
```

**Base offer:** 750 ARS no-deposit + 30 FS (× value tier multiplier)  
**Exit:** If no login → Move to 21+ Day bucket.

---

## C. ACTIVE HISTORY — 21+ DAY DORMANT (DEEP)

**Journey Name:** `12-AH-21D-JOURNEY`  
**Entry:** Falls through from 14-Day without login

### AH-21D-C1: Win-Back Package (Day 21)

| Setting | Value |
|---------|-------|
| Campaign ID | `12-AH-21D-C1-EMAIL` |
| Channel | Email |
| Subject (ES) | `🎁 Paquete de reactivación personalizado para vos` |

**Email Content:**
- **Subject (ES):** `🎁 Paquete de reactivación personalizado para vos`
- **Preheader (ES):** `Bonus + giros + CC armados según tu perfil`
- **Banner Text (ES):** `Tu Paquete de Reactivación`
- **Banner Description:** Win-back package visual — premium gift box opening, 3 rewards visible (cash + FS + match), personalized top-game artwork, impactful dark/gold design
- **Body Description:** Personalized win-back package details: 1,000 ARS no-deposit + 50 FS on their historical top slot + 100% match up to 5,000 ARS. Valid 72h. Clear CTA.

**Package (base):**
- 1,000 ARS no-deposit bonus
- 50 FS on player's historical top slot
- 100% match up to 5,000 ARS on next deposit
- 72h validity

---

### AH-21D-C2: SMS Reminder (Day 24)

| Setting | Value |
|---------|-------|
| Campaign ID | `12-AH-21D-C2-SMS` |
| Channel | SMS |

**SMS (ES):**
```
CuatroBet: {first_name}, tu paquete de reactivación sigue activo. {bonus_ars} ARS + {fs} giros + {match}% match. 48h más: {link}
```

---

### AH-21D-C3: VIP Escalation / Last Automated (Day 28)

| Setting | Value |
|---------|-------|
| Campaign ID | `12-AH-21D-C3-SMS-EMAIL` |
| Channel | SMS + Email |

**Email Content:**
- **Subject (ES):** For Micro/Low/Mid: `⚠️ {first_name}, última oferta antes de despedirnos` For High/Pre-VIP+: Handled by VIP team.
- **Preheader (ES):** `No queremos perderte — mirá lo que preparamos`
- **Banner Text (ES):** `Última Oferta`
- **Banner Description:** Final automated offer — "last chance" ribbon, premium reward visual (1,500 ARS + 75 FS), door-closing visual, urgency red/amber design
- **Body Description:** For Micro/Low/Mid: Final automated offer — 1,500 ARS no-dep + 75 FS. For High/Pre-VIP+: Handover to VIP team for personal win-back campaign. Tag for manual outreach.

**For Micro/Low/Mid:** Final automated offer — 1,500 ARS no-deposit + 75 FS.  
**For High/Pre-VIP+:** Handover to VIP team for personal win-back campaign. Tag player for manual outreach.

---

### AH-21D-C4: Exit Survey (Day 35)

| Setting | Value |
|---------|-------|
| Campaign ID | `12-AH-21D-C4-EMAIL` |
| Channel | Email |
| Subject (ES) | `📝 Nos gustaría saber por qué te fuiste` |

**Email Content:**
- **Subject (ES):** `📝 Nos gustaría saber por qué te fuiste`
- **Preheader (ES):** `Tu opinión nos ayuda a mejorar, {first_name}`
- **Banner Text (ES):** `Contános Tu Opinión`
- **Banner Description:** Exit survey — friendly feedback request, speech bubble icons, 3-question visual, 500 CC reward for completing, soft blue/teal professional tone
- **Body Description:** 3-question survey: why left, what would bring you back, rate experience (1-5). 500 CC incentive for completion. Tag player with responses.

**Incentive:** 500 CC for completing survey.  
**Action:** Tag player with survey responses for future campaigns.

---

## D. PASSIVE HISTORY — 7/14/21+ DAY (Same Structure, Lower Offers)

**Journey Names:** `12-PH-7D`, `12-PH-14D`, `12-PH-21D`

Apply the same 4-comm structure as Active History, with these adjustments:

| Difference | Active History | Passive History |
|-----------|---------------|-----------------|
| Offer amounts | Base × value multiplier | Base × 0.7 × value multiplier |
| Channel priority | Email → Push → SMS | SMS first (higher response for low-engagement) |
| Personalization | Game recommendations, tournament | Simple cashback, FS only |
| Escalation to VIP team | High + Pre-VIP+ | Pre-VIP+ only |
| Exit survey | At Day 35 | At Day 28 (shorter cycle) |

### Passive History Communications Summary:

| Bucket | C1 | C2 | C3 | C4 |
|--------|----|----|----|----|
| 7-Day | `12-PH-7D-C1` Soft check-in (SMS) | `12-PH-7D-C2` 7 FS (SMS) | `12-PH-7D-C3` 20% reload (Email+SMS) | `12-PH-7D-C4` 35% reload + 15 FS (SMS) |
| 14-Day | `12-PH-14D-C1` Miss you (Email) | `12-PH-14D-C2` 350 ARS no-dep (SMS) | `12-PH-14D-C3` Simple tournament entry (Email) | `12-PH-14D-C4` 500 ARS + 20 FS (SMS) |
| 21+ Day | `12-PH-21D-C1` Win-back lite (Email) | `12-PH-21D-C2` Reminder (SMS) | `12-PH-21D-C3` Final offer (SMS) | `12-PH-21D-C4` Exit survey (Email) |

---

## E. VNR — VERIFIED BUT NO REACTED (Special Case)

**Journey Name:** `12-VNR-JOURNEY`  
**Segment:** Completed registration + KYC verification BUT never deposited AND last_login > 7 days.

### VNR-C1: Reminder of Verified Status (Day 7)

| Setting | Value |
|---------|-------|
| Campaign ID | `12-VNR-C1-EMAIL` |
| Channel | Email |
| Subject (ES) | `✅ {first_name}, cuenta verificada — falta tu depósito` |

**Email Content:**
- **Subject (ES):** `✅ {first_name}, cuenta verificada — falta tu depósito`
- **Preheader (ES):** `Tu bono de bienvenida te está esperando`
- **Banner Text (ES):** `Cuenta Verificada — Listo Para Depositar`
- **Banner Description:** Verified account — green checkmark on account icon, deposit flow teaser, welcome bonus preview, clean professional design
- **Body Description:** Emphasize verification is done. Deposit is instant. Welcome bonus waiting. Step-by-step deposit guide.
- **CTA (ES):** `Depositar ahora` → Cashier

---

### VNR-C2: Bonus Push (Day 10)

| Setting | Value |
|---------|-------|
| Campaign ID | `12-VNR-C2-SMS` |
| Channel | SMS |

**SMS (ES):**
```
CuatroBet: {first_name}, tu cuenta verificada tiene un bono de bienvenida de {bonus_pct}% esperando. Depositá ahora: {link}
```

---

### VNR-C3: Free Trial (Day 14)

| Setting | Value |
|---------|-------|
| Campaign ID | `12-VNR-C3-EMAIL-SMS` |
| Channel | Email + SMS |
| Subject (ES) | `🎰 {fs_count} giros gratis sin depósito para vos` |

**Email Content:**
- **Subject (ES):** `🎰 {fs_count} giros gratis sin depósito para vos`
- **Preheader (ES):** `Probá sin riesgo, solo para cuentas verificadas`
- **Banner Text (ES):** `{fs_count} Giros Gratis — Sin Depósito`
- **Banner Description:** Free trial — free spins visual with "no deposit" badge, verified-only exclusive ribbon, game artwork preview, exciting blue/gold tones
- **Body Description:** Free trial offer: {fs_count} FS no-deposit, 10× wagering. Exclusive for verified players. Experience the product risk-free.

**Offer:** 20 FS no-deposit (low wagering 10×) to let them experience the product.

---

### VNR-C4: Final Attempt (Day 21)

| Setting | Value |
|---------|-------|
| Campaign ID | `12-VNR-C4-SMS` |
| Channel | SMS |

**SMS (ES):**
```
CuatroBet: {first_name}, última oportunidad. 500 ARS gratis + 30 giros. Solo hoy: {link}
```

**Offer:** 500 ARS no-deposit + 30 FS. Wagering 15×.  
**Exit:** If no deposit after C4, mark as `reactivation_exhausted`. Do not contact again for 60 days.

---

## F. BONUS TEMPLATES FOR REACTIVATION

| Template ID | Name | Type | Base Value | Wagering |
|------------|------|------|-----------|----------|
| `REACT-FS-10` | Light FS | Free Spins | 10 FS | 25× |
| `REACT-FS-20` | Medium FS | Free Spins | 20 FS | 20× |
| `REACT-FS-50` | Heavy FS | Free Spins | 50 FS | 15× |
| `REACT-RELOAD-30` | Lite Reload | Match | 30% up to 3K | 20× |
| `REACT-RELOAD-50` | Mid Reload | Match | 50% up to 5K | 18× |
| `REACT-RELOAD-100` | Full Reload | Match | 100% up to 5K | 15× |
| `REACT-NODEP-500` | No-Dep Small | Cash | 500 ARS | 15× |
| `REACT-NODEP-750` | No-Dep Medium | Cash | 750 ARS | 15× |
| `REACT-NODEP-1000` | No-Dep Large | Cash | 1,000 ARS | 12× |
| `REACT-NODEP-1500` | No-Dep XL | Cash | 1,500 ARS | 10× |
| `REACT-PKG` | Win-Back Package | Bundle | 1K + 50 FS + 100% match | 12× |

**Value Multiplier Application:**
```
final_value = base_value × value_tier_multiplier
final_wagering = base_wagering (unchanged — do NOT scale wagering)
```

---

## G. PREDICTIVE CHURN INTEGRATION

**Early Entry Logic:**
```
IF churn_score ≥ 0.7 AND last_session_date ≤ 4 days:
  Enter 7-Day journey immediately (skip waiting to day 7)
  Tag: "churn_predicted_early_entry"

IF churn_score ≥ 0.85 AND value_tier IN ("High", "Pre-VIP+"):
  Alert VIP team immediately via internal notification
  Tag: "churn_critical_high_value"
```

---

## FREQUENCY CAPS (Reactivation Override)

| Rule | Setting |
|------|---------|
| Max reactivation comms per week | 3 |
| Min gap between comms | 48 hours |
| Override standard frequency caps | YES for reactivation journey |
| Do not overlap with | Chain 09 (Personalization birthday/anniversary) |
| Cool-off after exhaustion | 60 days no contact |

---

## TESTING CHECKLIST

- [ ] Active vs Passive History segments correctly populated
- [ ] 7/14/21-day buckets trigger at correct intervals
- [ ] Value tier multiplier applies to offer amounts (NOT wagering)
- [ ] Behavioral filter routes comms to correct channels
- [ ] Predictive churn early entry triggers at ≥0.7 probability
- [ ] VIP team alert fires for critical high-value churn
- [ ] VNR segment correctly identifies verified-no-deposit players
- [ ] VNR flow does NOT overlap with standard reactivation
- [ ] Bonus templates credit correct amounts
- [ ] No-deposit bonuses have correct wagering requirements
- [ ] Exit survey records responses and tags player
- [ ] `reactivation_exhausted` tag prevents re-entry for 60 days
- [ ] Frequency cap of 3/week enforced
- [ ] 48-hour minimum gap between comms respected
- [ ] Pre-VIP+ phone call handover notification works

---

## KPI TARGETS

| Metric | Target |
|--------|--------|
| 7-Day reactivation rate (Active History) | ≥ 25% |
| 7-Day reactivation rate (Passive History) | ≥ 12% |
| 14-Day reactivation rate (Active History) | ≥ 15% |
| 21+ Day reactivation rate (Active History) | ≥ 8% |
| VNR conversion to FTD | ≥ 10% |
| Exit survey completion rate | ≥ 20% |
| Cost per reactivated player | ≤ 2,500 ARS |
