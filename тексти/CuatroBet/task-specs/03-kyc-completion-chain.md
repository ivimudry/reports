# 03 — KYC Completion Chain

**Priority:** 🟡 High  
**Purpose:** Move KYC completion from 20% to 35–40% by turning verification into a rewarded journey  
**Three Phases:** Email → Phone → Document  
**Key side-effect:** Phone verification auto-opts-in players to SMS channel (best performing channel)

---

## PHASE 1: Email Verification

**Entry:** Registration complete

### Touch 1 — Email Verification Prompt
| Field | Value |
|-------|-------|
| **ID** | KYC-P1-01 |
| **Timing** | T+0 (registration) |
| **Channel** | In-session popup + Confirmation email with verification link |
| **Trigger** | Registration complete |
| **Segment** | All newly registered players |
| **Action** | Prompt to verify email |
| **Offer** | 500 ARS bonus on verification, no wagering, usable directly |
| **Copy (ES)** | "Verificá tu email y recibí 500 ARS de regalo al instante" |
| **CTA** | Verification link in email |
| **Exit** | Verified → credit 500 ARS → Phase 2; Not verified → Touch 2 |

---

### Decision Point — T+15 min
| **Condition** | Email verified? |
|-------|-------|
| **Yes →** | Credit 500 ARS → proceed to Phase 2 |
| **No →** | Touch 2 — SMS Reminder |

---

### Touch 2 — SMS Reminder (email not verified)
| Field | Value |
|-------|-------|
| **ID** | KYC-P1-02 |
| **Timing** | T+15 min |
| **Channel** | SMS |
| **Trigger** | Email not verified 15 min after registration |
| **Segment** | Unverified-email players |
| **Copy (ES)** | "CuatroBet: Verificá tu email y recibí 500 ARS al instante: [link]" |
| **CTA** | Verification link |
| **Exit** | Verified → credit 500 ARS → Phase 2; Still not verified → T+24h |

---

### Decision Point — T+24 h
| **Condition** | Email verified? |
|-------|-------|
| **Yes →** | Credit 500 ARS → proceed to Phase 2 |
| **No →** | Proceed to Phase 2 anyway (email can be verified later) |

---

## PHASE 2: Phone Verification

**Entry:** After email verification, OR at T+24h regardless of email status

### Touch 3 — Phone Verification Prompt
| Field | Value |
|-------|-------|
| **ID** | KYC-P2-01 |
| **Timing** | Immediately after Phase 1 completion |
| **Channel** | In-session popup + SMS with verification code |
| **Trigger** | Phase 1 completed (verified or timed out) |
| **Segment** | Players entering Phase 2 |
| **Action** | Prompt phone verification |
| **Offer** | 500 ARS bonus on phone verification, no wagering |
| **Copy (ES)** | "Verificá tu teléfono y recibí 500 ARS más. Total: 1,000 ARS al instante" |
| **CTA** | Enter verification code |
| **Exit** | Verified → credit 500 ARS + auto SMS opt-in; Not verified → Touch 4 |
| **Notes** | **Auto opt-in to SMS channel is the most valuable side-effect.** SMS is the best channel (19.68% click rate). |

---

### On Phone Verification:
- Credit 500 ARS
- **Auto opt-in the player to SMS channel**

---

### Touch 4 — Phone Reminder (if not verified in 48h)
| Field | Value |
|-------|-------|
| **ID** | KYC-P2-02 |
| **Timing** | T+48 h after Phase 2 start |
| **Channel** | SMS |
| **Trigger** | Phone not verified within 48h |
| **Segment** | Players who haven't verified phone |
| **Copy** | One SMS reminder |
| **Exit** | Proceed without blocking (player can still deposit) |

---

## PHASE 3: Document Verification

**Entry:** Cumulative deposits reach 15,000 ARS AND not yet document-verified  
**Rationale:** Start 30% earlier than the hard 22,500 ARS threshold so there's runway to complete before withdrawal block

### Touch 5 — Document Verification Prompt
| Field | Value |
|-------|-------|
| **ID** | KYC-P3-01 |
| **Timing** | Day 1 (deposits hit 15,000 ARS) |
| **Channel** | In-app banner + Email |
| **Trigger** | Cumulative deposits ≥ 15,000 ARS, documents not submitted |
| **Segment** | Players at 15K threshold, unverified |
| **Action** | Nudge document upload |
| **Offer** | 1,000 ARS bonus on document verification, no wagering |
| **Copy (ES)** | "Completá tu verificación ahora y desbloqueá retiros más rápidos plus un bono de 1,000 ARS" |
| **CTA** | "Verificar ahora" → document upload page |
| **Exit** | Submitted → review → Touch 7; Not submitted → Touch 6 |
| **Documents required** | Government ID + proof of address (standard KYC) |

---

### Touch 6 — Email Guide (Day 2)
| Field | Value |
|-------|-------|
| **ID** | KYC-P3-02 |
| **Timing** | Day 2 (of Phase 3) |
| **Channel** | Email |
| **Trigger** | Documents not submitted by Day 2 |
| **Segment** | Unverified players at 15K threshold |
| **Subject (ES)** | "Tu cuenta está a un paso del acceso total" |
| **Body** | Visual guide: how to upload documents, expected review time (24h), benefits of full verification |
| **Offer** | 1,000 ARS bonus still valid |
| **CTA** | "Subir documentos" |
| **Exit** | Submitted → review; Not submitted → continue |

---

### Decision Point — Day 3
| **Condition** | Documents submitted? |
|-------|-------|
| **Yes (accepted)** → | Credit 1,000 ARS bonus, celebration popup, EXIT to active lifecycle |
| **No →** | Continue — wait for 22,500 ARS hard threshold |

---

### Touch 7 — Hard Threshold Reached (22,500 ARS)
| Field | Value |
|-------|-------|
| **ID** | KYC-P3-03 |
| **Timing** | When cumulative deposits reach 22,500 ARS |
| **Channel** | In-session popup + Email + SMS |
| **Trigger** | Deposits cross 22,500 ARS (hard KYC threshold), still unverified |
| **Segment** | Players at mandatory threshold |
| **Action** | Urgent verification prompt — withdrawals now blocked until verified |
| **Offer** | 2,000 ARS bonus (doubled from Day 1 offer) as final reward |
| **Copy (ES)** | "Verificación obligatoria para retiros. Completá ahora y recibí 2,000 ARS de bono final" |
| **CTA** | "Verificar ahora" → document upload page |
| **Exit** | Submitted → review |

---

### Touch 8 — Verification Accepted
| Field | Value |
|-------|-------|
| **ID** | KYC-P3-04 |
| **Timing** | On document acceptance |
| **Channel** | In-session popup + System |
| **Action** | Credit bonus + celebrate |
| **Offer** | Credit 2,000 ARS bonus (or 1,000 ARS if verified before hard threshold) |
| **Copy (ES)** | "Verificación completa. Retiros rápidos activados. Tenés acceso al canal VIP." |
| **Exit** | EXIT to active lifecycle at current stage |

---

### Touch 9 — Verification Rejected
| Field | Value |
|-------|-------|
| **ID** | KYC-P3-05 |
| **Timing** | On document rejection |
| **Channel** | Email + Support queue |
| **Action** | Route to support queue for manual resolution |
| **Body** | Explain rejection reason, next steps |
| **Offer** | Bonus offer NOT removed — still available upon successful verification |
| **Exit** | Awaiting resolution |

---

## Cost Model
| Item | Value |
|------|-------|
| Phase 1 (email) | 500 ARS per verifier |
| Phase 2 (phone) | 500 ARS per verifier |
| Phase 3 (documents) | 1,000–2,000 ARS per verifier |
| Blended cost per registered player | 400–500 ARS |

## KPI Targets
| Metric | Baseline | Target |
|--------|----------|--------|
| KYC completion | 20% | 35–40% |
| SMS opt-in rate | — | +25–40% (from phone verification) |
| Withdrawal friction | High | Reduced (pre-verified at first withdrawal) |
| Fraud prevention | — | Earlier document verification for Pre-VIP/VIP |
