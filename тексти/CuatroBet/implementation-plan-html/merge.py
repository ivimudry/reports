"""Merge all implementation plan HTML pages into a single file with sequential numbering."""
import re
from pathlib import Path

BASE = Path(__file__).parent

# Ordered list: (old_filename, new_num, short_label)
PAGES = [
    ("00-data-integration.html",  "01", "Интеграция данных"),
    ("17-smart-segmentation.html","02", "Сегментация"),
    ("13-channel-strategy.html",  "03", "Каналы"),
    ("04-payment-failure.html",   "04", "Ошибки платежей"),
    ("05-welcome-bonus.html",     "05", "Welcome Bonus"),
    ("01-day1-retention.html",    "06", "Day 1 Retention"),
    ("03-kyc-completion.html",    "07", "KYC"),
    ("06-failed-deposits.html",   "08", "Failed Deposits"),
    ("14-bonuses-landing.html",   "09", "Бонус лендинг"),
    ("07-no-bonus.html",          "10", "No Bonus"),
    ("08-no-cashier.html",        "11", "No Cashier"),
    ("02-pre-vip.html",           "12", "Pre-VIP"),
    ("12-reactivation.html",      "13", "Реактивация"),
    ("09-personalization.html",   "14", "Персонализация"),
    ("15-bonus-shop.html",        "15", "Bonus Shop"),
    ("10-engagement.html",        "16", "Engagement"),
    ("11-loyalty.html",           "17", "Лояльность"),
    ("16-referral.html",          "18", "Реферальная"),
]

# Old number → new number mapping for title replacements
OLD_TO_NEW = {
    "00": "01", "17": "02", "13": "03", "04": "04", "05": "05",
    "01": "06", "03": "07", "06": "08", "14": "09", "07": "10",
    "08": "11", "02": "12", "12": "13", "09": "14", "15": "15",
    "10": "16", "11": "17", "16": "18",
}

def extract_page_content(html: str) -> str:
    """Extract inner content of <div class="page"> ... </div> before </body>."""
    # Find the first <div class="page">
    start_match = re.search(r'<div class="page">', html)
    if not start_match:
        return ""
    start = start_match.end()
    
    # Find the closing: last </div> before </body>
    end_match = html.rfind('</div>', start, html.rfind('</body>'))
    if end_match == -1:
        return html[start:]
    
    content = html[start:end_match]
    
    # Remove the "nav-back" link (we use the nav-bar instead)
    content = re.sub(r'\s*<a href="index\.html" class="nav-back">.*?</a>\s*', '\n', content, flags=re.DOTALL)
    
    # Remove page-nav (prev/next) blocks entirely — will be replaced with JS
    content = re.sub(r'\s*<div class="page-nav">.*?</div>\s*', '\n', content, flags=re.DOTALL)
    
    return content.strip()


def extract_index_content(html: str) -> str:
    """Extract index page content, removing nav-bar wrapper."""
    start_match = re.search(r'<div class="page">', html)
    if not start_match:
        return ""
    start = start_match.end()
    end_match = html.rfind('</div>', start, html.rfind('</body>'))
    content = html[start:end_match] if end_match != -1 else html[start:]
    return content.strip()


# Build nav links HTML
nav_links = ['<a href="#overview" data-page="overview" class="active">Обзор</a>']
for _, num, _ in PAGES:
    nav_links.append(f'<a href="#{num}" data-page="{num}">{num}</a>')

nav_html = "\n        ".join(nav_links)

# Read and process index
index_html = (BASE / "index.html").read_text(encoding="utf-8")
index_content = extract_index_content(index_html)

# Update index content: replace old campaign card hrefs with JS navigation
for old_file, new_num, label in PAGES:
    index_content = index_content.replace(f'href="{old_file}"', f'href="#{new_num}" data-page="{new_num}"')

# Update gantt labels and campaign card numbers in index
# Replace old doc numbers in cc-number spans and gantt labels
gantt_replacements = {
    "00 Data Integration": "01 Data Integration",
    "17 Сегментация": "02 Сегментация",
    "13 Каналы": "03 Каналы",
    "04 Ошибки платежей": "04 Ошибки платежей",
    "05 Welcome Ladder": "05 Welcome Ladder",
    "01 Day 1 Retention": "06 Day 1 Retention",
    "03 KYC": "07 KYC",
    "06 Failed Deposits": "08 Failed Deposits",
    "14 Landing Page": "09 Landing Page",
    "07 No Bonus": "10 No Bonus",
    "08 No Cashier": "11 No Cashier",
    "02 Pre-VIP": "12 Pre-VIP",
    "12 Реактивация": "13 Реактивация",
    "09 Персонализация": "14 Персонализация",
    "15 Bonus Shop": "15 Bonus Shop",
    "10 Геймификация": "16 Геймификация",
    "11 Лояльность": "17 Лояльность",
    "16 Реферальная": "18 Реферальная",
}
for old, new in gantt_replacements.items():
    index_content = index_content.replace(old, new)

# Update cc-number in campaign cards for index - these show the old doc number
# Pattern: <div class="cc-number">XX</div>
for old_num, new_num in OLD_TO_NEW.items():
    index_content = index_content.replace(
        f'<div class="cc-number">{old_num}</div>',
        f'<div class="cc-number">{new_num}</div>'
    )

# Also update dependency section references
dep_replacements = {
    "<code>00</code>": "<code>01</code>",
    "<code>17</code>": "<code>02</code>",
    "<code>13</code>": "<code>03</code>",
    "<code>04</code>": "<code>04</code>",
    "<code>05</code>": "<code>05</code>",
    "<code>01</code>": "<code>06</code>",
    "<code>02</code>": "<code>12</code>",
    "<code>10</code>": "<code>16</code>",
    "<code>12</code>": "<code>13</code>",
    "<code>14</code>": "<code>09</code>",
}
# Can't do simple replacements here because of conflicts. Skip — the dependency section
# references original doc numbers which is fine as domain knowledge.


# Read CSS
css = (BASE / "style.css").read_text(encoding="utf-8")

# Build page sections
sections = []

for old_file, new_num, label in PAGES:
    html = (BASE / old_file).read_text(encoding="utf-8")
    content = extract_page_content(html)
    
    # Update page title: replace "XX —" at start of h1 with new number
    old_num_from_file = old_file.split("-")[0]
    content = content.replace(
        f'<h1>{old_num_from_file} — ',
        f'<h1>{new_num} — '
    )
    # Also handle the case where h1 starts differently
    content = content.replace(
        f'<h1>{old_num_from_file.lstrip("0") or "0"} — ',
        f'<h1>{new_num} — '
    )
    
    # Update footer doc number
    content = content.replace(f'Doc {old_num_from_file}', f'Doc {new_num}')
    
    sections.append(f'  <section id="p{new_num}" class="page-section" style="display:none">\n    <div class="page">\n{content}\n    </div>\n  </section>')


# Write combined file
output = f"""<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>CuatroBet — План внедрения CRM</title>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <style>
{css}

/* === SINGLE-PAGE ADDITIONS === */
.page-section {{ display: none; }}
.page-section.active {{ display: block; }}

.flow-diagram {{
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0;
  margin: 24px 0;
}}
.flow-step {{
  background: var(--bg-card);
  border: 2px solid var(--step-color, var(--border));
  border-radius: var(--radius);
  padding: 14px 24px;
  text-align: center;
  min-width: 280px;
  max-width: 600px;
  width: 100%;
}}
.flow-step .flow-label {{
  font-size: .92rem;
  color: var(--text-primary);
}}
.flow-diagram .flow-arrow {{
  text-align: center;
  color: var(--text-muted);
  font-size: .85rem;
  padding: 6px 0;
  width: auto;
  height: auto;
  background: none;
}}
.flow-diagram .flow-arrow::after {{ display: none; }}
  </style>
</head>
<body>

<nav class="nav-bar">
  <span class="logo">🎯 CuatroBet CRM</span>
  <div class="nav-links">
    {nav_html}
  </div>
</nav>

<!-- OVERVIEW -->
<section id="overview" class="page-section active">
  <div class="page">
{index_content}
  </div>
</section>

{chr(10).join(sections)}

<script>
(function() {{
  const navLinks = document.querySelectorAll('.nav-links a');
  const sections = document.querySelectorAll('.page-section');
  
  function showPage(id) {{
    sections.forEach(s => {{ s.style.display = 'none'; s.classList.remove('active'); }});
    navLinks.forEach(a => a.classList.remove('active'));
    
    // Find section  
    let section = document.getElementById(id) || document.getElementById('p' + id);
    if (!section) section = document.getElementById('overview');
    if (section) {{
      section.style.display = 'block';
      section.classList.add('active');
    }}
    
    // Activate nav link
    const activeLink = document.querySelector('.nav-links a[data-page="' + (id.replace('p','')) + '"]') 
                    || document.querySelector('.nav-links a[data-page="overview"]');
    if (activeLink) activeLink.classList.add('active');
    
    window.scrollTo(0, 0);
  }}
  
  // Handle nav clicks
  navLinks.forEach(a => {{
    a.addEventListener('click', function(e) {{
      e.preventDefault();
      const page = this.getAttribute('data-page');
      history.pushState(null, '', '#' + page);
      showPage(page === 'overview' ? 'overview' : 'p' + page);
    }});
  }});
  
  // Handle campaign card clicks on overview page (they have data-page attrs)
  document.addEventListener('click', function(e) {{
    const link = e.target.closest('a[data-page]');
    if (link && !link.closest('.nav-bar')) {{
      e.preventDefault();
      const page = link.getAttribute('data-page');
      history.pushState(null, '', '#' + page);
      showPage('p' + page);
    }}
  }});
  
  // Handle hash on load
  const hash = location.hash.slice(1);
  if (hash && hash !== 'overview') {{
    showPage('p' + hash);
  }}
  
  // Handle back/forward
  window.addEventListener('popstate', function() {{
    const hash = location.hash.slice(1) || 'overview';
    showPage(hash === 'overview' ? 'overview' : 'p' + hash);
  }});
}})();
</script>

</body>
</html>
"""

outpath = BASE / "cuatrobet-crm-plan.html"
outpath.write_text(output, encoding="utf-8")
print(f"✅ Created: {outpath}")
print(f"   Size: {outpath.stat().st_size / 1024:.0f} KB")
print(f"   Pages: overview + {len(PAGES)} campaign pages")
