# 09 — Personalization Cluster — Implementation Guide

**Chain:** Personalization (Anniversary, Birthday, Custom, Zodiac)  
**Estimated Communications:** 4 per type × 4 types = 16 total  
**Prerequisites from Master Doc:** Attributes `registration_date`, `birthday`, `zodiac_sign`, `most_played_game_name`, `biggest_win_ars`, `total_rounds_played`

---

## STEP 0: PRE-FLIGHT CHECKLIST

- [ ] Attribute `registration_date` available (for anniversary calculation)
- [ ] Attribute `birthday` available (from KYC or profile)
- [ ] Attribute `zodiac_sign` calculated from birthday
- [ ] Player stats available: total rounds, favorite game, biggest win (for anniversary email)
- [ ] Bonus templates created: Anniversary Year 1 (100% up to 5,000 + 30 FS + 500 CC), Birthday (100% up to 3,000 + 25 FS + 300 CC)
- [ ] Zodiac bonus template: 50% match + 15 FS, 20× wagering, 7-day validity
- [ ] Lucky Wheel accessible for zodiac-matched games
- [ ] CRM owner can manually trigger "Personal Custom" campaigns

---

## TYPE A: ANNIVERSARY

**Journey Name:** `09-PERS-ANNIV-JOURNEY`  
**Entry Trigger:** Date match: `registration_date` anniversary (yearly)  
**Re-entry:** Yearly

### Comm 1 — Anniversary Celebration (Day 0, Morning)

| Setting | Value |
|---------|-------|
| **Campaign ID** | `09-PERS-ANNIV-C1-EMAIL-POPUP` |
| **Channel** | Email + In-app popup |

**Email Content:**
- **Subject (ES):** `🎉 100% + 30 giros + 500 CC - feliz {years} año`
- **Preheader (ES):** `Tu regalo de aniversario personalizado te espera`
- **Banner Text (ES):** `¡Feliz {years} Año!`
- **Banner Description:** Anniversary celebration — large gold anniversary badge with "{years}" number, confetti, CuatroBet logo, player's favorite game artwork ({most_played_game_name}) integrated, festive golden/purple tones
- **Body Description:** Personal anniversary greeting with player stats recap (total rounds played, favorite game, biggest win). Gift details: 100% match up to 5,000 ARS + 30 FS on their favorite game + 500 CC. Wagering 15×, valid 72h.
- **CTA (ES):** `Reclamar regalo` → `{base_url}/cashier`

**Offer (Year 1 base — scale up for Year 2+):**
- Year 1: 100% up to 5,000 ARS + 30 FS + 500 CC
- Year 2: 120% up to 7,000 ARS + 40 FS + 800 CC
- Year 3+: 150% up to 10,000 ARS + 60 FS + 1,200 CC

**In-App Popup (show on first login of anniversary day):**
- **Banner Text (ES):** `¡Feliz Aniversario!`
- **Banner Description:** Condensed anniversary celebration — gold badge, confetti burst, gift icon, warm golden tones
- **Body (ES):** `¡{first_name}, hoy es tu aniversario! Tenés 100% bono + 30 giros + 500 CC esperándote.`
- **CTA (ES):** `Reclamar regalo` → `{base_url}/cashier`

### Comm 2 — Follow-Up (Day +1)

| Campaign ID | `09-PERS-ANNIV-C2-SMS` |
|------------|------------------------|
| Channel | SMS |
| Text (ES) | `CuatroBet: Tu regalo de aniversario vence en 48h. No lo pierdas: {link}` |
| Condition | No deposit since Comm 1 |

### Comm 3 — Final Reminder (Day +2)

| Campaign ID | `09-PERS-ANNIV-C3-EMAIL` |
|------------|--------------------------|
| Channel | Email |
| **Subject (ES)** | `⏰ Último día: tu regalo de aniversario` |
| **Preheader (ES)** | `Tu bono expira hoy, no lo pierdas` |
| **Banner Text (ES)** | `Último Día — Tu Regalo` |
| **Banner Description** | Urgency anniversary — gift box with countdown timer, fading celebration confetti, "last day" ribbon, warm amber tones |
| **Body Description** | Final reminder: anniversary gift expires today. Recap offer details. Urgency framing. |
| Condition | No deposit since Comm 1 |

### Comm 4 — Thank You / Transition (Day +3)

| Campaign ID | `09-PERS-ANNIV-C4-EMAIL` |
|------------|--------------------------|
| Channel | Email || **Subject (ES)** | `🙏 Gracias por {years} año con nosotros` |
| **Preheader (ES)** | `Tu historia con CuatroBet apenas comienza` || **Banner Text (ES)** | `Gracias por Ser Parte` |
| **Banner Description** | Thank-you visual — warm golden scene, CuatroBet community, heart/handshake icon, player's journey timeline hint |
| **Body Description** | If claimed: thank-you + experience recap. If not claimed: soft "we'll be here" message with return invitation. |
| Exit | Return to regular lifecycle |

---

## TYPE B: BIRTHDAY

**Journey Name:** `09-PERS-BDAY-JOURNEY`  
**Entry Trigger:** Date match: `birthday` field  
**Re-entry:** Yearly

### Comm 1 — Birthday Celebration (Birthday, Morning)

| Setting | Value |
|---------|-------|
| **Campaign ID** | `09-PERS-BDAY-C1-EMAIL-POPUP-SMS` |
| **Channel** | Email + In-app popup + SMS |

**Email Content:**
- **Subject (ES):** `🎂 100% + 25 giros + 300 CC - feliz cumpleaños`
- **Preheader (ES):** `Tu regalo de cumpleaños de CuatroBet te espera`
- **Banner Text (ES):** `¡Feliz Cumpleaños, {first_name}!`
- **Banner Description:** Birthday party theme — birthday cake with candles, colorful balloons, confetti burst, gift box opening, "🎂" visual, warm festive purple/gold tones
- **Body Description:** Birthday greeting with player's name. Gift details: 100% match up to 3,000 ARS + 25 FS on their favorite game + 300 CC. Wagering 15×, valid 48h.
- **CTA (ES):** `Abrir regalo` → `{base_url}/cashier`

**In-App Popup:**
- **Banner Text (ES):** `¡Feliz Cumpleaños!`
- **Banner Description:** Condensed birthday celebration — cake icon, balloons, confetti, gift badge
- **Body (ES):** `¡Feliz cumpleaños, {first_name}! Tu regalo: 100% bono + 25 giros + 300 CC.`
- **CTA (ES):** `Abrir regalo` → `{base_url}/cashier`

**SMS Content (ES):**
- Text: `CuatroBet: ¡Feliz cumpleaños {first_name}! Tu regalo: 100% bono + 25 giros + 300 CC. Reclamalo: {link}`

### Comm 2 — Evening Push (Birthday +12h)

| Campaign ID | `09-PERS-BDAY-C2-PUSH` |
|------------|-------------------------|
| Channel | App Push |
| Text (ES) | `Tu regalo de cumpleaños te está esperando. Abrilo ahora 🎂` |
| CTA | Deep link to bonus |

### Comm 3 — Reminder (Birthday +24h)

| Campaign ID | `09-PERS-BDAY-C3-SMS` |
|------------|------------------------|
| Channel | SMS |
| Text (ES) | `CuatroBet: Tu regalo de cumpleaños vence en 24h: {link}` |

### Comm 4 — Expiry (Birthday +48h)

| Campaign ID | `09-PERS-BDAY-C4-EMAIL` |
|------------|--------------------------|
| Channel | Email || **Subject (ES)** | `🎂 Gracias por celebrar con CuatroBet` |
| **Preheader (ES)** | `Esperamos que hayas disfrutado tu día especial` || **Banner Text (ES)** | `Gracias` |
| **Banner Description** | Post-birthday thank-you — warm afterglow, balloons deflating gently, "thanks" ribbon, soft golden tones |
| **Body Description** | If claimed: thank-you with birthday recap. If not claimed: offer expiry notification with soft return message. |
| Exit | Return to regular lifecycle |

---

## TYPE C: PERSONAL CUSTOM

**Journey Name:** Manual trigger (no automated journey)  
**CRM Manager Action:** Create one-off campaign using template structure

### Template for Each Custom Campaign:

| Comm | Timing | Channel | Content |
|------|--------|---------|---------|
| C1 | Trigger-specific | Best channel for player | Initial personalized message |
| C2 | +24–48h | Follow-up channel | Reminder if no response |
| C3 | +72h | Final channel | Last reminder before offer expiry |
| C4 | +96h | Email | Thank-you or transition |

**Required fields for each campaign:**
- Trigger condition (what event or manual selection)
- Target audience size
- Channel per comm
- Copy per comm in Spanish
- Offer details (match %, FS, CC, wagering, validity)
- Exit condition
- Success metric
- **Review: Weekly CRM standup**

---

## TYPE D: ZODIAC BONUS

**Journey Name:** `09-PERS-ZODIAC-JOURNEY`  
**Entry Trigger:** First day of each zodiac period, filtered by `zodiac_sign`  
**Re-entry:** Monthly (each zodiac period)

### Zodiac Calendar:

| Period | Sign | Dates |
|--------|------|-------|
| 1 | Aries | Mar 21 – Apr 19 |
| 2 | Taurus | Apr 20 – May 20 |
| 3 | Gemini | May 21 – Jun 20 |
| 4 | Cancer | Jun 21 – Jul 22 |
| 5 | Leo | Jul 23 – Aug 22 |
| 6 | Virgo | Aug 23 – Sep 22 |
| 7 | Libra | Sep 23 – Oct 22 |
| 8 | Scorpio | Oct 23 – Nov 21 |
| 9 | Sagittarius | Nov 22 – Dec 21 |
| 10 | Capricorn | Dec 22 – Jan 19 |
| 11 | Aquarius | Jan 20 – Feb 18 |
| 12 | Pisces | Feb 19 – Mar 20 |

### Comm 1 — Zodiac Launch (Day 1)

| Setting | Value |
|---------|-------|
| **Campaign ID** | `09-PERS-ZODIAC-C1-EMAIL-BANNER` |
| **Channel** | Email + In-app banner |

**Email Content:**
- **Subject (ES):** `✨ 50% + 15 giros - tu bono zodiacal de {sign_name}`
- **Preheader (ES):** `Tu signo tiene un regalo especial esperando`
- **Banner Text (ES):** `Bono Zodiacal: {sign_name}`
- **Banner Description:** Zodiac-themed visual — current zodiac sign constellation artwork, mystical star-field background, zodiac symbol prominently displayed, matching color palette per sign
- **Body Description:** Zodiac greeting for current sign. Offer: 50% match + 15 FS on zodiac-matched game, 20× wagering, 7-day validity. Lucky Wheel teaser.
- **CTA (ES):** `Reclamar bono zodiacal` → `{base_url}/cashier`

### Comm 2 — Day 3

| Campaign ID | `09-PERS-ZODIAC-C2-PUSH` |
|------------|---------------------------|
| Channel | App Push |
| Text (ES) | `Tu bono zodiacal de {sign_name} está activo. Usalo antes de que termine: {link}` |

### Comm 3 — Day 5

| Campaign ID | `09-PERS-ZODIAC-C3-SMS` |
|------------|--------------------------|
| Channel | SMS |
| Text (ES) | `CuatroBet: Último chance para tu bono zodiacal. Vence en 2 días: {link}` |

### Comm 4 — Last Day

| Campaign ID | `09-PERS-ZODIAC-C4-EMAIL` |
|------------|----------------------------|
| Channel | Email || **Subject (ES)** | `⌛ Último día para tu bono de {sign_name}` |
| **Preheader (ES)** | `Mañana cambia el signo y tu oferta desaparece` || **Banner Text (ES)** | `Último Día Zodiacal` |
| **Banner Description** | Zodiac period ending — current sign fading, next sign teaser appearing, countdown visual, mystical transition |
| **Body Description** | Final reminder for zodiac bonus + teaser for the next zodiac sign's offer. |
| Exit | Return to regular lifecycle |

---

## TESTING CHECKLIST

- [ ] Anniversary triggers on correct date (registration_date anniversary)
- [ ] Anniversary Year 2+ scales offer correctly
- [ ] Player stats in anniversary email are accurate
- [ ] Birthday triggers only for players with verified birthday field
- [ ] Birthday multi-channel (email + popup + SMS) fires simultaneously
- [ ] Zodiac sign calculated correctly from birthday
- [ ] Zodiac campaign targets only matching sign players
- [ ] Custom campaigns can be launched manually by CRM owner
- [ ] All offers have correct wagering, validity, and amounts
- [ ] Bonuses credit correctly on deposit
