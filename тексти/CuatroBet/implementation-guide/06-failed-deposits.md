# 06 — Failed Deposits: Communication Ladders — Implementation Guide

**Chain:** Failed Deposits (post-recovery follow-up)  
**Start Point:** T+5 min after deposit failure (chain 04 handles T+0 to T+5min)  
**Scope:** 5 failure reasons × 4 communications = 20 total communications  
**Prerequisites from Master Doc:** Events `deposit_failed`, `cashier_opened`, `cashier_closed`, `deposit_success`; Attributes `deposit_count`, `welcome_bonus_claimed`; Segments `SEG-CASHIER-ABANDONED`

---

## STEP 0: PRE-FLIGHT CHECKLIST

- [ ] Chain 04 (Payment Failure Recovery) is live and hands off at T+30min
- [ ] Event `cashier_closed` fires when player leaves deposit page without depositing
- [ ] Failure reason codes available: `INSUFF`, `METHOD`, `DECLINE`, `TIMEOUT`, `FRAUD`
- [ ] Player's `attempt_count_session` tracks retry count
- [ ] Support ticket API available (for Reason 3 and Reason 5)
- [ ] Fraud review queue exists (for Reason 5)
- [ ] All bonus templates from master doc are created (welcome bonus, apology credits)

---

## STEP 1: CREATE 5 SEPARATE JOURNEYS

Create one journey per failure reason. This keeps logic clean and allows independent optimization.

| Journey Name | Entry Trigger | Start Timing |
|-------------|---------------|--------------|
| `06-FAIL-R1-JOURNEY` | `cashier_closed` + no deposit attempt + 30 min inactive | T+30 min |
| `06-FAIL-R2-JOURNEY` | `deposit_failed` + `failure_reason = TIMEOUT/METHOD` + attempt_count = 1 + not recovered in chain 04 | T+5 min |
| `06-FAIL-R3-JOURNEY` | `deposit_failed` + `attempt_count_session >= 2` + technical reason + not recovered | T+5 min |
| `06-FAIL-R4-JOURNEY` | `deposit_failed` + `failure_reason = DECLINE/INSUFF` + not recovered | T+5 min |
| `06-FAIL-R5-JOURNEY` | `deposit_failed` + `failure_reason = FRAUD` | T+5 min |

**Global exit for all journeys:** `deposit_success` event → exit journey immediately.

---

## STEP 2: REASON 1 — No Attempt for Deposit

**Segment:** Player opened cashier, made no deposit attempt, left.

### Comm 1 — T+30 min

| Setting | Value |
|---------|-------|
| **Campaign ID** | `06-FAIL-R1-C1-POPUP-SMS` |
| **Channel** | In-app popup (if in session) OR SMS (if exited) |
| **Timing** | 30 min after cashier close |

**Popup Content (ES):**
- **Banner Text (ES):** `¡Te Faltó un Paso!`
- **Banner Description:** Friendly nudge — half-filled progress bar, one step remaining icon, welcome bonus preview (120% + 50 FS), inviting green CTA glow
- **Body (ES):** `Te faltó un paso. Tu bono de bienvenida te espera. Depositá ahora y empezá a jugar.`
- **CTA (ES):** `Depositar ahora` → `{base_url}/cashier`

**SMS Content (ES):**
- Text: `CuatroBet: Te faltó un paso. Tu bono de 120% + 50 giros te espera. Depositá ahora: {link}`

---

### Comm 2 — T+2h

| Setting | Value |
|---------|-------|
| **Campaign ID** | `06-FAIL-R1-C2-SMS` |
| **Channel** | SMS |

**SMS Content (ES):**
- Text: `CuatroBet: Tu bono de 120% + 50 giros aún te espera. Depositá en minutos: {link}`

---

### Comm 3 — T+24h

| Setting | Value |
|---------|-------|
| **Campaign ID** | `06-FAIL-R1-C3-EMAIL` |
| **Channel** | Email |

**Email Content:**
- **Subject (ES):** `🎰 120% + 50 Giros - vence pronto`
- **Preheader (ES):** `No pierdas tu bono de bienvenida, depositá ahora`
- **Banner Text (ES):** `120% + 50 Giros — Vence Pronto`
- **Banner Description:** Urgency welcome bonus visual — countdown clock overlay, "120% + 50 FS" in large gold text, Gates of Olympus artwork, amber glow for urgency
- **Body Description:** Urgency framing — bonus expiring soon. Step-by-step deposit guide (3 simple steps). List available payment methods. Offer: welcome bonus + 200 CC added incentive.
- **CTA (ES):** `Depositar ahora` → `{base_url}/cashier`

---

### Comm 4 — T+48h

| Setting | Value |
|---------|-------|
| **Campaign ID** | `06-FAIL-R1-C4-SMS` |
| **Channel** | SMS |

**SMS Content (ES):**
- Text: `CuatroBet: Última oportunidad. 120% + 50 giros. Válido 24h más: {link}`

**Exit:** Deposit → Day 1 Retention Layer. No response → Reactivation (pre-FTD cohort).

---

## STEP 3: REASON 2 — Failed Deposit (Tech, Single Attempt)

### Comm 1 — T+5 min

| Setting | Value |
|---------|-------|
| **Campaign ID** | `06-FAIL-R2-C1-POPUP` |
| **Channel** | In-session popup |

**Popup Content (ES):**
- **Banner Text (ES):** `Problema Técnico Resuelto`
- **Banner Description:** Recovery popup — wrench icon transforming to checkmark, supportive blue tones, "try again" arrow icon, payment method icons below
- **Body (ES):** `Tuvimos un problema técnico. Probá de nuevo o usá otro método de pago.`
- **CTA 1 (ES):** `Reintentar`
- **CTA 2 (ES):** `Otro método` → show alternative payment methods

---

### Comm 2 — T+1h

| Setting | Value |
|---------|-------|
| **Campaign ID** | `06-FAIL-R2-C2-SMS` |
| **Channel** | SMS |

**SMS Content (ES):**
- Text: `CuatroBet: El problema está resuelto. Depositá ahora y activá tu bono: {link}`
- Bonus: Welcome bonus reminder + 200 ARS extra no-deposit credit as apology

---

### Comm 3 — T+6h

| Setting | Value |
|---------|-------|
| **Campaign ID** | `06-FAIL-R2-C3-EMAIL` |
| **Channel** | Email |

**Email Content:**
- **Subject (ES):** `✅ Tu depósito está listo para completarse`
- **Preheader (ES):** `Probá con el método recomendado y activá tu bono`
- **Banner Text (ES):** `Tu Depósito Está Listo`
- **Banner Description:** Resolution visual — checkmark over payment icon, recommended payment method highlighted, 200 ARS apology gift visual, calm professional design
- **Body Description:** Apology for technical issue. Suggest best/recommended payment method with visual guide. Offer: welcome bonus + 200 ARS no-deposit apology credit.
- **CTA (ES):** `Depositar ahora`

---

### Comm 4 — T+24h

| Setting | Value |
|---------|-------|
| **Campaign ID** | `06-FAIL-R2-C4-SMS` |
| **Channel** | SMS |

**SMS Content (ES):**
- Text: `CuatroBet: Tu bono 120% + 50 giros + 200 ARS de regalo te esperan: {link}`

**Exit:** Deposit → Day 1 Retention + 200 ARS credit. No response → Reactivation (Payment-blocked sub-cohort).

---

## STEP 4: REASON 3 — Failed 2+ Attempts (Persistent Issue)

### Comm 1 — T+5 min

| Setting | Value |
|---------|-------|
| **Campaign ID** | `06-FAIL-R3-C1-POPUP` |
| **Channel** | In-session popup |

**Popup Content (ES):**
- **Banner Text (ES):** `Estamos Revisando`
- **Banner Description:** Investigation visual — magnifying glass over gear icon, support team avatar, progress indicator, reassuring blue tones
- **Body (ES):** `Detectamos un problema persistente. Nuestro equipo está revisando. Te avisamos cuando esté resuelto.`
- **CTA 1 (ES):** `Avisame por SMS`
- **CTA 2 (ES):** `Avisame por email`
- Action: Auto-create support ticket, record preferred contact method

---

### Comm 2 — T+2h or on resolution

| Setting | Value |
|---------|-------|
| **Campaign ID** | `06-FAIL-R3-C2-PREFERRED` |
| **Channel** | Player's preferred channel (SMS or Email, chosen in Comm 1) |

**Content (ES):**
- Text: `CuatroBet: El problema se resolvió. Depositá ahora y recibí un regalo extra: {link}`
- Bonus: Welcome bonus + 500 ARS apology credit (no wagering)

---

### Comm 3 — T+12h

| Setting | Value |
|---------|-------|
| **Campaign ID** | `06-FAIL-R3-C3-EMAIL` |
| **Channel** | Email |

**Email Content:**
- **Subject (ES):** `🎁 500 ARS de regalo + disculpas`
- **Preheader (ES):** `Problem resuelto, tenés un crédito especial esperando`
- **Banner Text (ES):** `Disculpas + 500 ARS de Regalo`
- **Banner Description:** Apology gift visual — gift box opening with 500 ARS coin, formal "sorry" ribbon, multiple payment method icons shown as options, professional warm design
- **Body Description:** Formal apology for persistent issue. Confirm issue is resolved. List all available payment methods with brief pros of each. Offer: welcome bonus + 500 ARS no-wagering apology credit.
- **CTA (ES):** `Depositar ahora`

---

### Comm 4 — T+48h

| Setting | Value |
|---------|-------|
| **Campaign ID** | `06-FAIL-R3-C4-SMS` |
| **Channel** | SMS |

**SMS Content (ES):**
- Text: `CuatroBet: Tu bono + 500 ARS de regalo siguen esperándote: {link}`

**Exit:** Deposit → exit. No response → Reactivation (Payment-blocked, high-priority flag).

---

## STEP 5: REASON 4 — Acquirer Declined

### Comm 1 — T+5 min

| Setting | Value |
|---------|-------|
| **Campaign ID** | `06-FAIL-R4-C1-POPUP` |
| **Channel** | In-session popup |

**Popup Content (ES):**
- **Banner Text (ES):** `Probá otro Método`
- **Banner Description:** Payment alternatives popup — declined card icon fading out, alternative method icons (Mercado Pago, bank transfer, Naranja) highlighted, helpful arrow pointing to alternatives
- **Body (ES):** `Tu banco no aprobó la transacción. Probá con otro método o un monto menor.`
- **CTA 1 (ES):** `Otro método` → alternative payment methods
- **CTA 2 (ES):** `Monto menor` → preset amounts (500/1000/1500 ARS)

---

### Comm 2 — T+1h

| Setting | Value |
|---------|-------|
| **Campaign ID** | `06-FAIL-R4-C2-SMS` |
| **Channel** | SMS |

**SMS Content (ES):**
- Text: `CuatroBet: Probá con Mercado Pago o transferencia bancaria. Tu bono te espera: {link}`
- Link: Cashier with alternative method preselected

---

### Comm 3 — T+12h

| Setting | Value |
|---------|-------|
| **Campaign ID** | `06-FAIL-R4-C3-EMAIL` |
| **Channel** | Email |

**Email Content:**
- **Subject (ES):** `💳 Métodos alternativos para tu depósito`
- **Preheader (ES):** `Mercado Pago, Naranja y más opciones para depositar`
- **Banner Text (ES):** `Métodos de Pago Alternativos`
- **Banner Description:** Payment methods showcase — grid of payment logos (Mercado Pago, Naranja, bank transfer), each with brief advantage label, inviting layout, green checkmarks
- **Body Description:** List all available payment methods with pros of each (Mercado Pago: instant, Naranja: easy, bank transfer: secure). Offer: welcome bonus + 100 CC for trying alternative method. Deep link per method.
- **CTA (ES):** Per-method deep links

---

### Comm 4 — T+48h

| Setting | Value |
|---------|-------|
| **Campaign ID** | `06-FAIL-R4-C4-SMS` |
| **Channel** | SMS |

**SMS Content (ES):**
- Text: `CuatroBet: Todavía podés activar tu bono de 120%. Probá otro método: {link}`

**Exit:** Deposit → exit. No response → Reactivation (Payment-blocked cohort).

---

## STEP 6: REASON 5 — Fraud

### Comm 1 — T+5 min

| Setting | Value |
|---------|-------|
| **Campaign ID** | `06-FAIL-R5-C1-POPUP` |
| **Channel** | In-session popup |

**Popup Content (ES):**
- **Banner Text (ES):** `Verificación de Seguridad`
- **Banner Description:** Security verification visual — shield icon with magnifying glass, professional dark blue security theme, progress spinner, trust-building design
- **Body (ES):** `Tu transacción está siendo verificada por seguridad. Te contactaremos pronto.`
- **Action:** Flag account, route to fraud review queue
- **CTA:** None (informational only)

---

### Comm 2 — On fraud review completion

| Setting | Value |
|---------|-------|
| **Campaign ID** | `06-FAIL-R5-C2-EMAIL` |
| **Channel** | Email |

**If false positive (ES):**
- **Subject:** `✅ Tu cuenta está verificada`
- **Preheader:** `Todo listo, ya podés depositar normalmente`
- **Banner Text (ES):** `Cuenta Verificada`
- **Banner Description:** Verification success — green shield with checkmark, "verified" badge, welcoming design, deposit CTA prominent
- **Body Description:** Confirm security verification passed. Inform player can deposit normally. Welcoming tone.
- **CTA (ES):** `Depositar ahora` → cashier

**If confirmed fraud:**
- Account closure notification (separate template managed by legal/compliance)

---

### Comm 3 — T+24h (false positive only)

| Setting | Value |
|---------|-------|
| **Campaign ID** | `06-FAIL-R5-C3-SMS` |
| **Channel** | SMS |

**SMS Content (ES):**
- Text: `CuatroBet: Tu cuenta está verificada. Depositá y activá tu bono: {link}`

---

### Comm 4 — T+48h (false positive only)

| Setting | Value |
|---------|-------|
| **Campaign ID** | `06-FAIL-R5-C4-EMAIL` |
| **Channel** | Email |

**Email Content:**
- **Subject (ES):** `🎰 Tu bono de bienvenida sigue disponible`
- **Preheader (ES):** `120% + 50 giros te esperan, depositá ahora`
- **Banner Text (ES):** `Tu Bono Te Espera`
- **Banner Description:** Welcome bonus reminder — 120% + 50 FS visual, friendly inviting design, "still available" badge, warm golden tones
- **Body Description:** Final reminder with welcome bonus details (120% match + 50 FS). Reassure player after security check cleared. Soft urgency.
- **CTA (ES):** `Depositar ahora`

**Exit:** Resolved (false positive) → normal lifecycle. Confirmed fraud → account closed.

---

## STEP 7: TESTING CHECKLIST

- [ ] Each reason correctly routes to its own journey
- [ ] Global exit fires on `deposit_success` (stops all comms immediately)
- [ ] Reason 1: Cashier close + 30 min inactivity triggers journey
- [ ] Reason 2: Single tech failure + no recovery → journey starts at T+5min
- [ ] Reason 3: 2+ failures detected → support ticket auto-created
- [ ] Reason 3: Player's preferred contact method is recorded and used
- [ ] Reason 4: Alternative payment methods shown dynamically
- [ ] Reason 5: Account flagged → fraud review queue
- [ ] Reason 5: Comms 3–4 only fire for false positives
- [ ] Apology credits (200 ARS / 500 ARS) credited correctly
- [ ] SMS character count ≤160 for all messages
- [ ] UTM parameters on all links
- [ ] Frequency caps respected (max 2/day for pre-FTD)
- [ ] No overlap with chain 04 (PFR handles T+0 to T+5min only)

---

## SUMMARY TABLE

| Reason | Comms | Bonus/Credit | Priority |
|--------|-------|-------------|----------|
| R1: No attempt | 4 | Welcome bonus + 200 CC | High |
| R2: Tech (single) | 4 | Welcome bonus + 200 ARS | High |
| R3: Tech (persistent) | 4 | Welcome bonus + 500 ARS | Critical |
| R4: Acquirer declined | 4 | Welcome bonus + 100 CC | Medium |
| R5: Fraud | 4 | Welcome bonus (if cleared) | Low |
