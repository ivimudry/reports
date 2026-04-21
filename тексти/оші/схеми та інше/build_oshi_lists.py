# Builds 3 plain-text lists from Oshi catalog data.
# - all games (from oshi-games-all.json already on disk)
# - popular games (fetched via API filter)
# - recommended games (fetched via API filter)
import json
import time
import sys
import urllib.request
from pathlib import Path

OUT_DIR = Path(__file__).parent
ALL_JSON = OUT_DIR / "oshi-games-all.json"

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


def fetch_category(category: str) -> list:
    games = []
    page = 1
    while True:
        body = json.dumps({
            "device": "desktop",
            "page": page,
            "filter": {"categories": {"identifiers": [category], "strategy": "OR"}, "providers": []},
            "sort": {"direction": "ASC", "type": "global"},
            "page_size": 48,
            "without_territorial_restrictions": False,
        }).encode("utf-8")
        req = urllib.request.Request(URL, data=body, headers=HEADERS, method="POST")
        with urllib.request.urlopen(req, timeout=30) as r:
            payload = json.loads(r.read().decode("utf-8"))
        data = payload.get("data", [])
        games.extend(data)
        pg = payload.get("pagination", {})
        print(f"  {category} page {page}/{pg.get('total_pages')} -> {len(data)} (total {len(games)}/{pg.get('total_count')})")
        if not pg.get("next_page"):
            break
        page = pg["next_page"]
        time.sleep(0.15)
    return games


def write_list(games: list, out_path: Path):
    lines = []
    seen = set()
    for g in games:
        title = (g.get("title") or "").strip()
        prov = (g.get("provider") or "").strip()
        key = (title, prov)
        if key in seen:
            continue
        seen.add(key)
        lines.append(f"{title} ({prov})")
    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {len(lines)} entries -> {out_path.name}")


def main():
    # 1. All
    all_games = json.loads(ALL_JSON.read_text(encoding="utf-8"))
    write_list(all_games, OUT_DIR / "Усі ігри оші.txt")

    # 2. Popular
    popular = fetch_category("popular")
    write_list(popular, OUT_DIR / "Популярні ігри оші.txt")

    # 3. Recommended
    recommended = fetch_category("recommended")
    write_list(recommended, OUT_DIR / "Рекомендовані ігри оші.txt")


if __name__ == "__main__":
    main()
