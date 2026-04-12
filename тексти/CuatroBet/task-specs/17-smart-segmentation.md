# 17 — Smart Segmentation Setup

**Purpose:** Activate GR8 Tech Smart Segmentation & Predictive Churn modules  
**Status:** Available but not activated — prerequisites for most lifecycles

---

## Five-Axis Segmentation Model

### Axis 1: Lifecycle Stage (drives which journey)
| Stage | Definition |
|-------|-----------|
| Registered | Account only |
| Activated | First action, no FTD |
| FTD | <24h old |
| Day 1–3 | In Day 1 Retention Layer window |
| Pre-STD | Wagered FTD, no second deposit yet |
| Regular | 2+ deposits, active in last 14 days |
| Pre-VIP | Lifetime deposits 150K–300K ARS |
| VIP I–IV | Per VIP program thresholds |
| At-risk | Active but predictive churn score above threshold |
| Dormant | 3–7 / 8–14 / 15–30 / 31–60 / 60+ days |

### Axis 2: Value Tier (drives offer selection)
| Tier | Lifetime Deposits |
|------|-------------------|
| Micro | <5,000 ARS |
| Low | 5,000–25,000 ARS |
| Mid | 25,000–75,000 ARS |
| High | 75,000–150,000 ARS |
| Pre-VIP+ | >150,000 ARS |

### Axis 3: Game Preference (drives content)
| Preference | Description |
|------------|-------------|
| Slots-only | Majority of players |
| Aviator / crash | Crash game players |
| Live Casino | Live table players |
| Mixed | Slots + one other |

### Axis 4: Churn Risk (accelerator)
| Risk | Score |
|------|-------|
| Healthy | <30% |
| Watch | 30–60% |
| At-risk | 60–85% |
| Critical | >85% |

### Axis 5: KYC Status (gate)
| Status | Description |
|--------|-------------|
| Unverified | No verification |
| Partially verified | Email + phone |
| Fully verified | Documents complete |

---

## How Axes Combine

| Axis | Role | Example |
|------|------|---------|
| **1 — Lifecycle** | Triggers journey | Post-FTD → STD lifecycle |
| **2 — Value** | Selects offer tier | Low → base offer |
| **3 — Game Pref** | Selects content/FS | Slots → Joker's Jewels FS |
| **4 — Churn Risk** | Accelerates timing | Watch → sent earlier than default |
| **5 — KYC** | Gates actions | Partially verified → SMS available |

**Example:** Low-value, Slots-preferring, Watch-tier player, 2 days post-FTD → enters Post-FTD lifecycle (Axis 1), receives Low-tier reload (Axis 2), with FS on Joker's Jewels (Axis 3), sent earlier (Axis 4), via SMS (Axis 5).

---

## Activation Checklist

- [ ] Contact GR8 Tech to enable Smart Segmentation module
- [ ] Contact GR8 Tech to enable Predictive Churn model
- [ ] Request raw player-level data export access
- [ ] Build 5-axis classification rules in GR8 Tech segmentation UI
- [ ] Validate against 1 week of historical data
- [ ] Connect segments to journey triggers
- [ ] Test churn score accuracy (does >60 predict actual churn?)
