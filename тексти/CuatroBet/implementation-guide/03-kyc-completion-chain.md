# 03 — KYC Completion Chain — Implementation Guide

**Chain:** KYC Completion (Email → Phone → Document)  
**Priority:** High  
**Estimated Communications:** 9+ touches across 3 phases  
**Key Outcome:** Phone verification auto-opts players into SMS channel (best channel: 19.68% click rate)  
**Prerequisites from Master Doc:** Events `email_verified`, `phone_verified`, `documents_submitted`, `documents_approved`, `documents_rejected`, `deposit_success`; Attributes `kyc_level`, `email_verified`, `phone_verified`, `documents_status`, `cumulative_deposits_ars`; Segments `SEG-KYC-NONE`, `SEG-KYC-EMAIL-PENDING`, `SEG-KYC-PHONE-PENDING`, `SEG-KYC-DOCS-PENDING`

---

## STEP 0: PRE-FLIGHT CHECKLIST

- [ ] Event `email_verified` fires when player clicks verification link
- [ ] Event `phone_verified` fires when player enters correct SMS code
- [ ] Event `documents_submitted` fires when player uploads KYC documents
- [ ] Event `documents_approved` / `documents_rejected` fire on review completion
- [ ] Attribute `cumulative_deposits_ars` updates in real-time
- [ ] Bonus template `KYC-EMAIL-REWARD`: 500 ARS, no wagering
- [ ] Bonus template `KYC-PHONE-REWARD`: 500 ARS, no wagering
- [ ] Bonus template `KYC-DOCS-REWARD-EARLY`: 1,000 ARS, no wagering
- [ ] Bonus template `KYC-DOCS-REWARD-HARD`: 2,000 ARS, no wagering
- [ ] Phone verification auto-enables SMS opt-in (configure in channel settings)
- [ ] Document upload page deep link: `{base_url}/profile/verify`
- [ ] KYC document review SLA defined (target: 24h)

---

## STEP 1: CREATE THE JOURNEY

**Campaign Name:** `03-KYC-JOURNEY`  
**Type:** Triggered journey (event-based)  
**Entry Trigger:** Event = `player_registered`  
**Re-entry:** None  
**Journey Window:** Indefinite (Phase 3 triggers on deposit threshold, may be weeks later)

---

## STEP 2: PHASE 1 — EMAIL VERIFICATION

### 2.1 Touch 1 — Email Verification Prompt (T+0)

| Setting | Value |
|---------|-------|
| **Campaign ID** | `03-KYC-P1-01-POPUP-EMAIL` |
| **Channel** | In-session popup + Confirmation email |
| **Timing** | T+0 (immediately on registration) |

**In-Session Popup Content:**
- **Banner Text (ES):** `Verificá tu Email`
- **Banner Description:** Clean verification theme — envelope icon with checkmark, 500 ARS coin reward visual, green accent color, simple and trustworthy design
- **Body (ES):** `Verificá tu email y recibí 500 ARS de regalo al instante`
- **CTA Button (ES):** `Verificar` → triggers email resend if needed
- **Dismiss:** Can dismiss, but show again on next session

**Verification Email Content:**
- **Subject (ES):** `🎁 500 ARS de regalo - verificá tu email`
- **Preheader (ES):** `Un click y recibís 500 ARS al instante`
- **Banner Text (ES):** `500 ARS de Regalo`
- **Banner Description:** Email verification visual — envelope opening with golden coins spilling out, checkmark badge, CuatroBet branding
- **Body Description:** Welcome greeting. Explain that verifying email unlocks 500 ARS instant gift. Single-action CTA to verify.
- **CTA Button (ES):** `Verificar mi email` → verification link
- **Footer:** Standard legal + explain this is a one-time verification

**Configuration steps:**
1. On registration event, fire two parallel actions:
   - Show in-session popup
   - Send verification email with unique link
2. On `email_verified` event → credit 500 ARS → proceed to Phase 2
3. If not verified → wait 15 minutes → Touch 2

---

### 2.2 Decision Point — T+15 min

| Condition | Path |
|-----------|------|
| `email_verified = true` | Credit 500 ARS → jump to Phase 2 |
| `email_verified = false` | Touch 2 (SMS reminder) |

---

### 2.3 Touch 2 — SMS Reminder (T+15 min)

| Setting | Value |
|---------|-------|
| **Campaign ID** | `03-KYC-P1-02-SMS` |
| **Channel** | SMS |
| **Timing** | T+15 minutes |
| **Condition** | Email NOT verified |

**SMS Content:**
- **Text (ES):** `CuatroBet: Verificá tu email y recibí 500 ARS al instante: {verification_link}`
- **Character count:** ≤160

**Configuration steps:**
1. Add 15-minute delay after registration
2. Add condition: `email_verified = false`
3. If true → send SMS with verification link
4. On `email_verified` event at any point → credit 500 ARS → Phase 2

---

### 2.4 Decision Point — T+24h

| Condition | Path |
|-----------|------|
| `email_verified = true` | Credit 500 ARS → Phase 2 |
| `email_verified = false` | Proceed to Phase 2 anyway (email can be verified later; listening continues) |

---

## STEP 3: PHASE 2 — PHONE VERIFICATION

**Entry:** Immediately after Phase 1 completes (either verified or timed out at 24h)

### 3.1 Touch 3 — Phone Verification Prompt

| Setting | Value |
|---------|-------|
| **Campaign ID** | `03-KYC-P2-01-POPUP-SMS` |
| **Channel** | In-session popup + SMS with verification code |
| **Timing** | Immediately on Phase 2 entry |

**In-Session Popup Content:**
- **Banner Text (ES):** `Verificá tu Teléfono`
- **Banner Description:** Phone verification visual — smartphone icon with shield/lock, SMS code bubbles, 500 ARS coin reward, green trust accents
- **Body (ES):** `Verificá tu teléfono y recibí 500 ARS más. Total: 1,000 ARS al instante`
- **CTA Button (ES):** `Ingresar código`
- **Input field:** 6-digit code entry

**SMS with Verification Code:**
- **Text (ES):** `CuatroBet: Tu código de verificación es {code}. Ingresalo en la app para recibir 500 ARS.`

**On Phone Verification (`phone_verified` event):**
1. Credit 500 ARS bonus (no wagering)
2. **AUTO OPT-IN TO SMS CHANNEL** ← Most valuable side-effect
3. Update `sms_opt_in = true`
4. Proceed to Phase 2 complete

**Configuration steps:**
1. Add popup node showing verification prompt
2. Trigger SMS OTP send
3. Listen for `phone_verified` event
4. On verification: credit bonus + enable SMS opt-in
5. If not verified within 48h → Touch 4

---

### 3.2 Touch 4 — Phone Reminder (T+48h after Phase 2 start)

| Setting | Value |
|---------|-------|
| **Campaign ID** | `03-KYC-P2-02-SMS` |
| **Channel** | SMS |
| **Timing** | 48 hours after Phase 2 start |
| **Condition** | Phone NOT verified |

**SMS Content:**
- **Text (ES):** `CuatroBet: 500 ARS te esperan. Verificá tu teléfono para recibirlos: {link}`

**Configuration steps:**
1. Add 48-hour delay
2. Condition: `phone_verified = false`
3. Send SMS reminder
4. Do NOT block player from depositing — proceed regardless after reminder

---

## STEP 4: PHASE 3 — DOCUMENT VERIFICATION

**Entry:** `cumulative_deposits_ars >= 15000` AND `documents_status = "none"`  
**Rationale:** Start 30% before the hard 22,500 ARS threshold

### 4.1 Touch 5 — Document Verification Prompt (Day 1 of Phase 3)

| Setting | Value |
|---------|-------|
| **Campaign ID** | `03-KYC-P3-01-BANNER-EMAIL` |
| **Channel** | In-app banner + Email |
| **Timing** | When deposits reach 15,000 ARS |

**In-App Banner:**
- **Position:** Top of main screen, persistent until dismissed or verified
- **Text (ES):** `Completá tu verificación y desbloqueá retiros rápidos + 1,000 ARS`
- **CTA (ES):** `Verificar ahora` → `{base_url}/profile/verify`

**Email Content:**
- **Subject (ES):** `🔓 1,000 ARS - tu cuenta a un paso del acceso total`
- **Preheader (ES):** `Verificá tus documentos y recibí 1,000 ARS`
- **Banner Text (ES):** `1,000 ARS por Verificación`
- **Banner Description:** Document verification visual — ID card icon with checkmark, golden 1,000 ARS coin stack, padlock-to-unlock transition, professional trust design
- **Body Description:** Inform player account is almost complete. List required documents (DNI front/back, proof of address). List benefits: faster withdrawals, higher limits, 1,000 ARS no-wagering bonus. Mention 24h review SLA.
- **CTA Button (ES):** `Subir documentos` → `{base_url}/profile/verify`

**Configuration steps:**
1. Create new triggered journey or sub-journey: `03-KYC-P3-JOURNEY`
2. Entry trigger: `cumulative_deposits_ars >= 15000` AND `documents_status = "none"`
3. Show persistent in-app banner
4. Send email with document upload instructions
5. Listen for `documents_submitted` event

---

### 4.2 Touch 6 — Email Guide (Day 2 of Phase 3)

| Setting | Value |
|---------|-------|
| **Campaign ID** | `03-KYC-P3-02-EMAIL` |
| **Channel** | Email |
| **Timing** | Day 2 of Phase 3 |
| **Condition** | Documents NOT submitted |

**Email Content:**
- **Subject (ES):** `❓ ¿Necesitás ayuda con la verificación?`
- **Preheader (ES):** `Nuestro equipo está listo para asistirte`
- **Banner Text (ES):** `Verificación en 5 Pasos`
- **Banner Description:** Step-by-step visual guide — 5 numbered steps as icons (account → verify → photo → upload → done), progress bar, friendly helper character
- **Body Description:** Step-by-step how-to guide with screenshots: 1) Go to "Mi Cuenta", 2) Click "Verificar identidad", 3) Photo front/back DNI, 4) Upload proof of address, 5) Submit and wait <24h. Visual guide/screenshots included. Remind about 1,000 ARS bonus waiting.
- **CTA Button (ES):** `Subir documentos` → `{base_url}/profile/verify`

**Configuration steps:**
1. Add 1-day delay from Touch 5
2. Condition: `documents_status = "none"`
3. Send how-to email with visual guide

---

### 4.3 Decision Point — Day 3

| Condition | Path |
|-----------|------|
| `documents_submitted = true` AND `documents_status = "approved"` | Credit 1,000 ARS → celebration → EXIT |
| `documents_submitted = false` | Wait for hard threshold (22,500 ARS) |

---

### 4.4 Touch 7 — Hard Threshold Reached (22,500 ARS)

| Setting | Value |
|---------|-------|
| **Campaign ID** | `03-KYC-P3-03-POPUP-EMAIL-SMS` |
| **Channel** | In-session popup + Email + SMS |
| **Timing** | When deposits reach 22,500 ARS |
| **Condition** | Documents NOT submitted |

**In-Session Popup Content:**
- **Banner Text (ES):** `Verificación Obligatoria`
- **Banner Description:** Urgent warning theme — amber/orange background, shield with exclamation mark, 2,000 ARS golden coin stack as reward incentive, serious but motivating design
- **Body (ES):** `Verificación obligatoria para retiros. Completá ahora y recibí 2,000 ARS de bono final`
- **CTA Button (ES):** `Verificar ahora` → `{base_url}/profile/verify`
- **Style:** Urgent (amber/warning theme)

**Email Content:**
- **Subject (ES):** `📢 Acción requerida: verificá tu cuenta para retiros`
- **Preheader (ES):** `Completá la verificación para habilitar retiros`
- **Banner Text (ES):** `Acción Requerida — 2,000 ARS`
- **Banner Description:** Urgent theme — amber warning stripe, lock icon transitioning to unlock, "2,000 ARS" prominently displayed, action-required badge
- **Body Description:** Inform withdrawals are paused until identity verification complete. Describe simple 5-minute process (upload DNI + proof of address). Highlight doubled bonus: 2,000 ARS on completion.
- **CTA Button (ES):** `Verificar ahora` → `{base_url}/profile/verify`

**SMS Content:**
- **Text (ES):** `CuatroBet: Verificación obligatoria para retiros. Completá ahora y recibí 2,000 ARS: {link}`

**Configuration steps:**
1. Create trigger: `cumulative_deposits_ars >= 22500` AND `documents_status = "none"`
2. Fire all 3 channels simultaneously (popup, email, SMS)
3. This is URGENT — withdrawals are blocked

---

### 4.5 Touch 8 — Verification Accepted

| Setting | Value |
|---------|-------|
| **Campaign ID** | `03-KYC-P3-04-POPUP-SYSTEM` |
| **Channel** | In-session popup + System action |
| **Timing** | On `documents_approved` event |

**Popup Content:**
- **Banner Text (ES):** `Verificación Completa`
- **Banner Description:** Celebration theme — green background, large animated checkmark, confetti, golden coins falling, "Verified" badge
- **Body (ES):** `Retiros rápidos activados. Tenés acceso al canal VIP.`
- **Dismiss:** Auto-dismiss after 10 seconds or on CTA click

**System Actions:**
1. Credit bonus:
   - If verified BEFORE 22,500 threshold → 1,000 ARS
   - If verified AT/AFTER 22,500 threshold → 2,000 ARS
2. Update `kyc_level = "full"`
3. Unlock withdrawals
4. EXIT to active lifecycle at current stage

**Configuration steps:**
1. Listen for `documents_approved` event
2. Check which bonus amount applies (conditional on timing)
3. Credit bonus
4. Show celebration popup
5. End KYC journey

---

### 4.6 Touch 9 — Verification Rejected

| Setting | Value |
|---------|-------|
| **Campaign ID** | `03-KYC-P3-05-EMAIL-SUPPORT` |
| **Channel** | Email + Support queue |
| **Timing** | On `documents_rejected` event |

**Email Content:**
- **Subject (ES):** `📝 Tu verificación necesita una corrección`
- **Preheader (ES):** `Un pequeño ajuste y estarás listo`
- **Banner Text (ES):** `Corrección Necesaria`
- **Banner Description:** Soft warning — orange/amber info banner, document icon with pencil/edit symbol, supportive and non-alarming design, arrow suggesting retry
- **Body Description:** Inform player documents were reviewed and correction needed. Show rejection reason (dynamic). Provide 3 tips: clear/legible photo, non-expired document, re-upload from app. Reassure bonus still available after successful verification.
- **CTA Button (ES):** `Subir documentos de nuevo` → `{base_url}/profile/verify`

**System Actions:**
1. Create support ticket with rejection details
2. Re-enter waiting state for new document submission
3. Bonus offer remains valid

**Configuration steps:**
1. Listen for `documents_rejected` event
2. Send rejection email with reason (personalize `{rejection_reason}`)
3. Create support ticket
4. Loop back to waiting for `documents_submitted` event

---

## STEP 5: TESTING CHECKLIST

- [ ] Phase 1: Registration triggers popup + verification email
- [ ] Phase 1: Email verification credits 500 ARS instantly
- [ ] Phase 1: T+15min SMS fires only if email not verified
- [ ] Phase 2: Phone verification popup appears after Phase 1
- [ ] Phase 2: Correct OTP code verifies the phone
- [ ] Phase 2: Phone verification credits 500 ARS + enables SMS opt-in
- [ ] Phase 2: T+48h reminder fires only if phone not verified
- [ ] Phase 3: Triggers at 15,000 ARS deposits (not 22,500)
- [ ] Phase 3: In-app banner persists until verified or dismissed
- [ ] Phase 3: Day 2 email only sent if documents not submitted
- [ ] Phase 3: Hard threshold (22,500) triggers urgent multi-channel push
- [ ] Phase 3: Accepted → correct bonus (1,000 or 2,000 ARS based on timing)
- [ ] Phase 3: Rejected → email with reason + support ticket + re-entry loop
- [ ] Player is NOT blocked from depositing during any phase
- [ ] SMS opt-in correctly enabled after phone verification

---

## COST MODEL

| Phase | Cost per Verifier |
|-------|-------------------|
| Phase 1 (Email) | 500 ARS |
| Phase 2 (Phone) | 500 ARS |
| Phase 3 (Documents, early) | 1,000 ARS |
| Phase 3 (Documents, hard threshold) | 2,000 ARS |
| **Blended per registered player** | **400–500 ARS** |

---

## KPI TARGETS

| Metric | Baseline | Target |
|--------|----------|--------|
| KYC completion rate | 20% | 35–40% |
| SMS opt-in rate (from phone verification) | — | +25–40% |
