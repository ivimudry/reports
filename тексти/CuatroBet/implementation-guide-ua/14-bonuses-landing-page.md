# 14 — Редизайн лендінгу бонусів — Гайд з імплементації

**Ланцюжок:** Landing Page Personalization (Lifecycle-based card layout + виправлення)  
**Пріоритет:** Phase 1 (Тиждень 2–3)  
**Тип:** UI/UX зміна, не CRM journey  

---

## КРОК 0: ПЕРЕДСТАРТОВИЙ ЧЕК-ЛИСТ

- [ ] Доступ до CMS або конструктора лендінгів GR8 Tech
- [ ] Атрибут lifecycle stage гравця доступний для персоналізації сторінки
- [ ] Можливість рендерингу динамічного контенту (показ/приховування карток за сегментом)
- [ ] Розклад розіграшів Lucky Wheel налаштований (щоденно/щотижня)
- [ ] API рекомендацій ігор доступний (або ручний список топ-10)
- [ ] Аналітичне відстеження показів карток, кліків, конверсій

---

## A. ВИПРАВЛЕННЯ КРИТИЧНИХ ПРОБЛЕМ (до редизайну)

### Виправлення 1: Зворотний відлік Lucky Wheel

| Проблема | "357D LEFT" — майже рік. Жодної терміновості. Сторінка виглядає застарілою. |
|---------|-----|
| Рішення | Замінити на зворотний відлік до **наступного запланованого розіграшу** |
| Логіка | `IF draw_scheduled → show "Próximo sorteo en {hours}h {minutes}m"` <br> `IF no_draw_scheduled → show "Próximo Lucky Wheel: {date}" teaser` |
| **НІКОЛИ** | Показувати зворотний відлік > 7 днів. Якщо таймер > 7д — приховати картку. |

### Виправлення 2: Вітальний бонус на спорт

| Проблема | Помітно відображається. 99.9% — казино-гравці. Марна витрата простору. |
|---------|-----|
| Рішення | Додати фільтр-вкладки зверху: **Todo / Casino / Deportes** |
| За замовчуванням | Вкладка Casino обрана |
| Картка Sports | Видима тільки у вкладці Deportes |
| Виключення | Якщо `player.game_preference = "Sports"` → за замовчуванням вкладка Deportes |

### Виправлення 3: Дублікати вітальних карток

| Проблема | 2 майже ідентичні картки Slots/Live (150% + 60 FS vs 150%). Канібалізація. |
|---------|-----|
| Рішення | Об'єднати в **одну** hero-картку: `120% + 50 FS` (узгоджено з драбиною Chain 05) |
| Показувати | Одну картку з чітким CTA |
| Якщо гравець використав вітальний бонус | Приховати картку повністю, замінити на reload-пропозицію |

### Виправлення 4: Відсутня візуальна ієрархія

| Проблема | Lucky Wheel візуально рівний з вітальними бонусами |
|---------|-----|
| Рішення | Hero-картка (велика, зверху) + підтримуючі картки (менші, знизу) |
| Макет | 1 hero (на всю ширину) + 2–3 підтримуючі (сітка на половину ширини) |

---

## B. ПЕРСОНАЛІЗОВАНІ МАКЕТИ ЗА LIFECYCLE

### Макет 1: Гравець Pre-FTD

**Сегмент:** `lifecycle_stage = "Registered" OR "Activated"`

| Позиція | Картка | Контент (ES) | CTA |
|----------|------|-------------|-----|
| **Hero** (на всю ширину) | Welcome Bonus | `Bono de bienvenida: 120% + 50 giros gratis en Gates of Olympus` | `Depositar ahora` → Cashier |
| Підтримуюча 1 | Lucky Wheel | `Próximo sorteo en {countdown}. Depositá para participar.` | `Ver premios` → Wheel page |
| Підтримуюча 2 | Top Games Preview | 3 вибрані слоти з топ-10 (зображення + назви) | `Jugar gratis` → Demo mode |
| Підтримуюча 3 | How-To Guide | `Cómo depositar en 2 minutos` (покрокова візуалізація) | `Depositar` → Cashier |
| **Приховано** | Reload-пропозиції, VIP-контент, Bonus Shop, Quests | — | — |

---

### Макет 2: Day 1 Layer (Post-FTD, перші 72 год.)

**Сегмент:** `lifecycle_stage = "FTD" OR "Day_1_3"`

| Позиція | Картка | Контент (ES) | CTA |
|----------|------|-------------|-----|
| **Hero** | Second Deposit Offer | `Tu segundo depósito: 75% + 30 giros en {first_session_game}` | `Depositar` → Cashier |
| Підтримуюча 1 | Welcome FS Remaining | `Te quedan {remaining_fs} giros gratis. Usalos ahora.` | `Jugar` → Slot page |
| Підтримуюча 2 | Lucky Wheel | Реальний зворотний відлік | `Girar` → Wheel |
| Підтримуюча 3 | Game Recommendations | На основі поведінки першої сесії | `Probar` → Game |

---

### Макет 3: Звичайний гравець

**Сегмент:** `lifecycle_stage = "Regular"`

| Позиція | Картка | Контент (ES) | CTA |
|----------|------|-------------|-----|
| **Hero** | Weekly Reload (ротація) | `Recarga semanal: {offer_pct}% + {fs_count} giros. Válido hasta domingo.` | `Activar` → Deposit |
| Підтримуюча 1 | Active Quests | `Misión activa: {quest_name}. Progreso: {progress}%` | `Ver misión` → Quest page |
| Підтримуюча 2 | Lucky Wheel | Реальний зворотний відлік | `Girar` |
| Підтримуюча 3 | Bonus Shop Featured | Топ-2 позиції за кількістю обмінів | `Ver tienda` → Shop |

---

### Макет 4: Pre-VIP / VIP

**Сегмент:** `lifecycle_stage IN ("Pre-VIP", "VIP_I", "VIP_II", "VIP_III", "VIP_IV")`

| Позиція | Картка | Контент (ES) | CTA |
|----------|------|-------------|-----|
| **Hero** | Personal Message | `{crm_owner_name}: {personalized_message}. Tu cashback esta semana: {cashback_amount} ARS.` | `Ver mi cuenta VIP` |
| Підтримуюча 1 | Exclusive Offer | Ексклюзивна VIP-пропозиція (ротація щотижня) | `Activar` |
| Підтримуюча 2 | VIP Events | Майбутні турніри, ексклюзивні розіграші | `Ver eventos` |
| Підтримуюча 3 | Curated Games | AI-підбір на основі історії гри | `Jugar` |
| **Приховано** | Стандартні welcome/reload-пропозиції | — | — |

---

## C. СПЕЦИФІКАЦІЇ КОМПОНЕНТУ КАРТКИ

### Hero-картка
```
Width: 100%
Height: 280px
Background: Градієнт або банерне зображення гри
Title: Bold, 24px, white
Subtitle: 16px, white 80% opacity
CTA Button: Primary brand color, 14px bold uppercase
Countdown (якщо застосовується): Live-таймер, 18px monospace
```

### Підтримуюча картка
```
Width: 48% (2-колонкова сітка з відступом 4%)
Height: 160px
Background: Темна картка, акцентна рамка бренду
Title: 16px bold
Description: 13px, макс. 2 рядки
CTA: Вторинна кнопка або текстове посилання
```

---

## D. АНАЛІТИЧНЕ ВІДСТЕЖЕННЯ

| Подія | Коли | Дані |
|-------|------|------|
| `card_impression` | Картка видима у viewport | `card_id`, `lifecycle_stage`, `position` |
| `card_click` | Гравець клікає CTA | `card_id`, `lifecycle_stage`, `cta_text` |
| `card_conversion` | Гравець завершує дію (депозит, гра тощо) | `card_id`, `lifecycle_stage`, `conversion_value` |

**Щотижневий звіт:**
- CTR карток за lifecycle stage
- Conversion rate hero-картки
- Використання фільтр-вкладок (Casino vs Sports)
- Engagement rate Lucky Wheel (до/після виправлення)

---

## ЧЕК-ЛИСТ ТЕСТУВАННЯ

- [ ] Гравець Pre-FTD бачить welcome hero, а НЕ reload-пропозиції
- [ ] Гравець Day 1 бачить hero другого депозиту з правильною грою
- [ ] Звичайний гравець бачить hero щотижневого reload
- [ ] VIP-гравець бачить hero з персональним повідомленням
- [ ] Lucky Wheel показує реальний зворотний відлік (не 357 днів)
- [ ] Картка Lucky Wheel прихована, якщо розіграшу немає протягом 7 днів
- [ ] Картка Sports видима тільки у вкладці Deportes
- [ ] Вкладка Casino є за замовчуванням для всіх не-спортивних гравців
- [ ] Дублікати вітальних карток об'єднані в одну картку
- [ ] Візуальна ієрархія Hero/підтримуючі чітка
- [ ] Картки відстежують покази та кліки
- [ ] Мобільна адаптивність (картки стакаються вертикально)
- [ ] Без зсуву макету при перемиканні вкладок

---

## ЦІЛЬОВІ KPI

| Метрика | Поточне | Ціль (4 тижні) |
|--------|---------|-------------------|
| CTR hero-картки | N/A (немає hero) | ≥ 8% |
| Конверсія вітального бонусу (Pre-FTD) | Невідомо | ≥ 15% |
| Engagement Lucky Wheel | Низький (застарілий відлік) | 2× від поточного |
| Використання вкладки Sports | N/A | Зафіксувати baseline |
| Bounce rate сторінки | Високий (передбачуваний) | -30% |
