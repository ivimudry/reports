"""
Test: verify that limit=50 is the problem for old broadcasts.
Check one converted user from 194089 (March 1st) - paginate all deposits.
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
    r = session.get(url, params=params, timeout=30)
    if r.status_code != 200:
        print(f"  ERROR {r.status_code}: {url}")
        return None
    return r.json()

# Step 1: Get converted messages from 194089
print("=== BROADCAST 194089 (01.03.2026 in_app) ===\n")
data = api_get(f"{BASE}/messages", {"newsletter_id": 194089, "metric": "converted", "limit": 100})
msgs = data.get("messages", [])
print(f"Converted messages: {len(msgs)}")

# Pick first 3 users to test
test_users = msgs[:3]

for msg in test_users:
    cio_id = msg.get("customer_identifiers", {}).get("cio_id")
    cust_id = msg.get("customer_id", "?")
    met = msg.get("metrics", {})
    ref_time = met.get("opened") or met.get("delivered") or met.get("sent") or 0
    conv_time = met.get("converted", 0)
    window_end = ref_time + (2 * 86400)
    
    from datetime import datetime
    ref_dt = datetime.fromtimestamp(ref_time) if ref_time else "?"
    conv_dt = datetime.fromtimestamp(conv_time) if conv_time else "?"
    
    print(f"\n--- {cust_id} (cio:{cio_id}) ---")
    print(f"  Opened: {ref_dt} (ts: {ref_time})")
    print(f"  Converted: {conv_dt} (ts: {conv_time})")
    print(f"  Window: {ref_dt} to {datetime.fromtimestamp(window_end)}")
    
    # Method A: limit=50 (current broken approach)
    ev_data = api_get(f"{BETA}/customers/{cio_id}/activities", {
        "type": "event", "name": "deposit_made", "limit": 50
    })
    activities_50 = ev_data.get("activities", []) if ev_data else []
    
    oldest_50 = None
    newest_50 = None
    in_window_50 = 0
    for ev in activities_50:
        t = ev.get("timestamp", 0)
        if oldest_50 is None or t < oldest_50: oldest_50 = t
        if newest_50 is None or t > newest_50: newest_50 = t
        if ref_time <= t <= window_end:
            in_window_50 += 1
    
    print(f"\n  [limit=50] Got {len(activities_50)} events")
    if activities_50:
        print(f"    Oldest: {datetime.fromtimestamp(oldest_50)} (ts: {oldest_50})")
        print(f"    Newest: {datetime.fromtimestamp(newest_50)} (ts: {newest_50})")
        print(f"    In window: {in_window_50}")
        print(f"    Oldest reaches ref_time? {'YES' if oldest_50 <= ref_time else 'NO - TOO RECENT!'}")
    
    # Method B: Paginate ALL deposits
    all_activities = []
    start = ""
    pages = 0
    while True:
        pages += 1
        params = {"type": "event", "name": "deposit_made", "limit": 50}
        if start:
            params["start"] = start
        ev_data = api_get(f"{BETA}/customers/{cio_id}/activities", params)
        if not ev_data:
            break
        batch = ev_data.get("activities", [])
        if not batch:
            break
        all_activities.extend(batch)
        
        # Check if we've gone past our window
        oldest_in_batch = min(e.get("timestamp", 0) for e in batch)
        if oldest_in_batch < ref_time:
            break  # We have enough
        
        start = ev_data.get("next", "")
        if not start:
            break
        time.sleep(0.3)
    
    oldest_all = min(e.get("timestamp", 0) for e in all_activities) if all_activities else 0
    newest_all = max(e.get("timestamp", 0) for e in all_activities) if all_activities else 0
    in_window_all = 0
    window_sum = 0
    for ev in all_activities:
        t = ev.get("timestamp", 0)
        if ref_time <= t <= window_end:
            in_window_all += 1
            d = ev.get("data", {})
            amount = float(d.get("human_amount_total_rounded", d.get("human_amount_total", d.get("human_amount", 0))) or 0)
            window_sum += amount
    
    print(f"\n  [PAGINATED] Got {len(all_activities)} events in {pages} pages")
    if all_activities:
        print(f"    Oldest: {datetime.fromtimestamp(oldest_all)} (ts: {oldest_all})")
        print(f"    Newest: {datetime.fromtimestamp(newest_all)} (ts: {newest_all})")
        print(f"    In window: {in_window_all}")
        print(f"    Window sum: {window_sum:.0f} EUR")
        print(f"    Oldest reaches ref_time? {'YES' if oldest_all <= ref_time else 'NO'}")
    
    time.sleep(0.5)

print("\n\n=== CONCLUSION ===")
print("If limit=50 shows 'TOO RECENT' but PAGINATED finds deposits in window,")
print("the bug is confirmed: we need to paginate activities, not just limit=50.")
