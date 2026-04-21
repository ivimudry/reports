# Fetches the full Oshi.io games catalog via /api/games_filter
# Aggregates all pages and produces inventory artifacts.
import json
import time
import sys
from pathlib import Path
from collections import Counter, defaultdict
import urllib.request
import urllib.error

OUT_DIR = Path(__file__).parent
RAW_FILE = OUT_DIR / "oshi-games-all.json"
INVENTORY_FILE = OUT_DIR / "oshi-inventory.md"
PROVIDERS_FILE = OUT_DIR / "oshi-providers.json"

URL = "https://www.oshi.io/api/games_filter"
HEADERS = {
    "accept": "application/vnd.s.v2+json",
    "accept-language": "en",
    "content-type": "application/json",
    "origin": "https://www.oshi.io",
    "referer": "https://www.oshi.io/games",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36",
    "x-content-policy": "1",
    "x-display-mode": "browser",
}


def fetch_page(page: int) -> dict:
    body = json.dumps({
        "device": "desktop",
        "page": page,
        "filter": {"categories": {"identifiers": ["all"], "strategy": "OR"}, "providers": []},
        "sort": {"direction": "ASC", "type": "global"},
        "page_size": 48,
        "without_territorial_restrictions": False,
    }).encode("utf-8")
    req = urllib.request.Request(URL, data=body, headers=HEADERS, method="POST")
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read().decode("utf-8"))


def main():
    all_games = []
    page = 1
    total_pages = None
    while True:
        try:
            payload = fetch_page(page)
        except urllib.error.HTTPError as e:
            print(f"HTTPError page {page}: {e}", file=sys.stderr)
            time.sleep(2)
            continue
        except Exception as e:
            print(f"Error page {page}: {e}", file=sys.stderr)
            time.sleep(2)
            continue
        data = payload.get("data", [])
        all_games.extend(data)
        pg = payload.get("pagination", {})
        total_pages = pg.get("total_pages") or total_pages
        total_count = pg.get("total_count")
        print(f"page {page}/{total_pages} fetched ({len(data)} games, total so far {len(all_games)}/{total_count})")
        if not pg.get("next_page"):
            break
        page = pg["next_page"]
        time.sleep(0.15)

    # Save raw aggregate (slim version - drop currencies to keep file small)
    slim = []
    for g in all_games:
        slim.append({
            "identifier": g.get("identifier"),
            "title": g.get("title"),
            "provider": g.get("provider"),
            "seo_title": g.get("seo_title"),
            "categories": g.get("categories", []),
            "is_geo_available": g.get("is_geo_available"),
            "volatility_rating": g.get("volatility_rating"),
            "payout": g.get("payout"),
            "lines": g.get("lines"),
            "ways": g.get("ways"),
        })
    RAW_FILE.write_text(json.dumps(slim, ensure_ascii=False, indent=2), encoding="utf-8")

    # Provider stats
    provider_counts = Counter(g["provider"] for g in slim if g.get("provider"))
    # Category stats (top-level only — exclude locale-suffixed)
    cat_counts = Counter()
    for g in slim:
        for c in g.get("categories", []):
            if ":" in c:
                continue
            cat_counts[c] += 1

    # Provider -> by category map
    provider_by_cat = defaultdict(lambda: Counter())
    for g in slim:
        prov = g.get("provider") or "?"
        for c in g.get("categories", []):
            if ":" in c or c.startswith("_"):
                continue
            provider_by_cat[prov][c] += 1

    PROVIDERS_FILE.write_text(json.dumps({
        "total_games": len(slim),
        "providers": dict(provider_counts.most_common()),
        "categories": dict(cat_counts.most_common()),
    }, ensure_ascii=False, indent=2), encoding="utf-8")

    # Markdown inventory
    lines = []
    lines.append(f"# Oshi.io Catalog Inventory\n")
    lines.append(f"Total games: **{len(slim)}**  ")
    lines.append(f"Providers: **{len(provider_counts)}**\n")

    lines.append("## Providers (by game count)\n")
    lines.append("| # | Provider | Games |")
    lines.append("|---|---|---:|")
    for i, (p, c) in enumerate(provider_counts.most_common(), 1):
        lines.append(f"| {i} | `{p}` | {c} |")
    lines.append("")

    lines.append("## Top-level categories\n")
    lines.append("| Category | Games |")
    lines.append("|---|---:|")
    for c, n in cat_counts.most_common():
        lines.append(f"| {c} | {n} |")
    lines.append("")

    INVENTORY_FILE.write_text("\n".join(lines), encoding="utf-8")
    print(f"\nDone. {len(slim)} games. Files:\n  {RAW_FILE}\n  {PROVIDERS_FILE}\n  {INVENTORY_FILE}")


if __name__ == "__main__":
    main()
