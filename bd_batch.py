"""
Batch test: deposit sums for all IDs with conversions > 0.
Compares with expected values from the spreadsheet.
"""
import sys, io, json, time
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

API_KEY = "e22bae722fdd70a705135c9fa2270e1d"
BETA = "https://beta-api.customer.io/v1"
BASE = "https://api.customer.io/v1"

session = requests.Session()
retries = Retry(total=5, backoff_factor=2, status_forcelist=[429, 500, 502, 503, 504])
session.mount("https://", HTTPAdapter(max_retries=retries))
session.headers.update({
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
})

def api_get(url, params=None):
    try:
        r = session.get(url, params=params, timeout=30)
    except Exception as e:
        return None
    if r.status_code != 200:
        return None
    return r.json()

# All IDs with conversions > 0 from the table
# Format: (id, type, conversions, expected_eur_from_sheet)
TEST_IDS = [
    # EMAILS with deposits (should work)
    (194109, "email", 5, 63),
    (194113, "email", 3, 457),
    (194115, "email", 3, 248),
    (194117, "email", 6, 556),
    (194120, "email", 10, 520),
    (194166, "email", 19, 1438),
    # EMAILS with conversions but 0 in sheet
    (194088, "email", 3, 0),
    (194098, "email", 9, 0),
    (194100, "email", 11, 0),
    (194102, "email", 5, 0),
    (194107, "email", 4, 0),
    # IN-APP with conversions but 0 in sheet (sample)
    (194089, "in_app", 21, 0),
    (194099, "in_app", 39, 0),
    (194101, "in_app", 22, 0),
    (194103, "in_app", 32, 0),
    (194119, "in_app", 22, 0),   # We know this is 1500!
    (194167, "in_app", 62, 0),
    (194175, "in_app", 61, 0),
    (194165, "in_app", 64, 0),
    (194149, "in_app", 50, 0),
    (194156, "in_app", 51, 0),
]

def calc_deposit_sum(newsletter_id):
    """Same logic as our Google Apps Script CIONSUM."""
    # Step 1: Get converted messages
    all_converted = []
    start = ""
    while True:
        params = {"newsletter_id": newsletter_id, "metric": "converted", "limit": 100}
        if start:
            params["start"] = start
        data = api_get(f"{BASE}/messages", params)
        if not data:
            break
        msgs = data.get("messages", [])
        if not msgs:
            break
        all_converted.extend(msgs)
        start = data.get("next", "")
        if not start:
            break
        time.sleep(0.3)
    
    if not all_converted:
        return 0, 0, "no converted messages"

    # Step 2: For each converted user, get deposits
    total = 0
    deposit_count = 0
    details = []
    
    for msg in all_converted:
        cio_id = msg.get("customer_identifiers", {}).get("cio_id")
        cust_id = msg.get("customer_id", "?")
        if not cio_id:
            details.append(f"  {cust_id}: NO cio_id!")
            continue
        
        met = msg.get("metrics", {})
        ref_time = met.get("opened") or met.get("delivered") or met.get("sent") or met.get("created") or 0
        window_end = ref_time + (2 * 86400) if ref_time else 0
        
        ev_data = api_get(f"{BETA}/customers/{cio_id}/activities", {
            "type": "event", "name": "deposit_made", "limit": 50
        })
        if not ev_data:
            details.append(f"  {cust_id}: no activities data")
            continue
        
        activities = ev_data.get("activities", [])
        user_sum = 0
        user_deps = 0
        for ev in activities:
            ev_time = ev.get("timestamp", ev.get("created_at", 0))
            if ref_time and window_end:
                if ev_time < ref_time or ev_time > window_end:
                    continue
            d = ev.get("data", ev.get("attributes", {}))
            amount = float(d.get("human_amount_total_rounded", d.get("human_amount_total", d.get("human_amount", 0))) or 0)
            user_sum += amount
            user_deps += 1
        
        total += user_sum
        deposit_count += user_deps
        if user_deps > 0:
            details.append(f"  {cust_id}: {user_deps}x = {user_sum:.0f} EUR")
    
    return total, deposit_count, details

print("=" * 80)
print(f"BATCH DEPOSIT SUM TEST — {len(TEST_IDS)} IDs")
print("=" * 80)
print(f"{'ID':<10} {'Type':<8} {'Conv':<6} {'Sheet':<8} {'Actual':<10} {'Deps':<6} {'Match'}")
print("-" * 80)

results = []
for nid, ntype, conv, expected in TEST_IDS:
    total, deps, info = calc_deposit_sum(nid)
    match = "✓" if abs(total - expected) < 1 else ("DIFF!" if expected > 0 else f"+{total:.0f}")
    print(f"{nid:<10} {ntype:<8} {conv:<6} {expected:<8} {total:<10.0f} {deps:<6} {match}")
    results.append((nid, ntype, conv, expected, total, deps, info))
    time.sleep(0.5)

print("\n" + "=" * 80)
print("DETAILS FOR MISMATCHES:")
print("=" * 80)
for nid, ntype, conv, expected, total, deps, info in results:
    if abs(total - expected) >= 1 and total > 0:
        print(f"\n--- {nid} ({ntype}) — Sheet: {expected}, Actual: {total:.0f} ---")
        if isinstance(info, list):
            for line in info[:10]:
                print(line)

print("\n" + "=" * 80)
print("SUMMARY")
print("=" * 80)
emails_zero = [(r[0], r[4]) for r in results if r[1] == "email" and r[3] == 0]
inapp_zero = [(r[0], r[4]) for r in results if r[1] == "in_app" and r[3] == 0]
print(f"Emails with sheet=0: {len(emails_zero)}")
for eid, actual in emails_zero:
    print(f"  {eid}: actual = {actual:.0f} EUR")
print(f"In-apps with sheet=0: {len(inapp_zero)}")
for eid, actual in inapp_zero:
    print(f"  {eid}: actual = {actual:.0f} EUR")
