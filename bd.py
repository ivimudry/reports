"""
Calculate total deposit amounts from converted users of broadcast #194166.
"""
import sys, io, json, time
from urllib.parse import quote
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

API_KEY = "e22bae722fdd70a705135c9fa2270e1d"
BROADCAST_ID = 194166
BETA = "https://beta-api.customer.io/v1"

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
        print(f"  CONN ERROR: {e}")
        time.sleep(5)
        try:
            r = session.get(url, params=params, timeout=30)
        except Exception as e2:
            print(f"  RETRY FAILED: {e2}")
            return None
    if r.status_code == 429:
        print("  Rate limited, waiting 10s...")
        time.sleep(10)
        r = session.get(url, params=params, timeout=30)
    if r.status_code != 200:
        print(f"  ERROR {r.status_code}: {url}")
        print(f"  {r.text[:500]}")
        return None
    return r.json()

print("=" * 60)
print(f"BROADCAST #{BROADCAST_ID} - Deposit Analysis")
print("=" * 60)

# Step 1: Get broadcast info
print("\n[1] Getting broadcast info...")
info = api_get(f"{BETA}/newsletters/{BROADCAST_ID}")
if info:
    nl = info.get("newsletter", info)
    print(f"  Name: {nl.get('name', '?')}")
    print(f"  Subject: {nl.get('subject', '?')}")

# Step 2: Get metrics
print("\n[2] Getting broadcast metrics...")
metrics = api_get(f"{BETA}/newsletters/{BROADCAST_ID}/metrics")
if metrics:
    m = metrics.get("metric", metrics.get("metrics", metrics))
    # Just show totals, not full series
    if "series" in m:
        totals = {k: sum(v) for k, v in m["series"].items()}
        print(f"  Totals: {json.dumps(totals, indent=2)}")
    else:
        print(f"  {json.dumps(m, indent=2)[:500]}")

# Step 3: Get messages
print("\n[3] Getting messages...")
all_messages = []
start = ""
page = 0

while True:
    page += 1
    params = {"limit": 100}
    if start:
        params["start"] = start
    data = api_get(f"{BETA}/newsletters/{BROADCAST_ID}/messages", params)
    if not data:
        break
    messages = data.get("messages", [])
    if not messages:
        break
    all_messages.extend(messages)
    print(f"  Page {page}: +{len(messages)} (total: {len(all_messages)})")
    start = data.get("next", "")
    if not start:
        break
    time.sleep(0.5)

print(f"  Total messages: {len(all_messages)}")

if not all_messages:
    print("\nNo messages. Showing sample structure...")
    sys.exit(0)

# Step 4: Find converted
# converted/opened are inside metrics dict
converted = [m for m in all_messages if m.get("metrics", {}).get("converted")]
opened_msgs = [m for m in all_messages if m.get("metrics", {}).get("opened")]
print(f"  Opened: {len(opened_msgs)}")
print(f"  Converted: {len(converted)}")

# Show sample metrics to understand structure
if all_messages:
    samples_with_conv = [m for m in all_messages if m.get("metrics", {}).get("converted")][:2]
    if samples_with_conv:
        print(f"\n  Sample converted msg metrics:")
        for s in samples_with_conv:
            print(f"    customer: {s.get('customer_id')} | metrics: {s.get('metrics')}")
    else:
        # Show a few different metrics to understand
        unique_keys = set()
        for m in all_messages:
            unique_keys.update(m.get("metrics", {}).keys())
        print(f"  All metric keys across messages: {sorted(unique_keys)}")
        # Find messages that have more than basic metrics
        rich = [m for m in all_messages if len(m.get("metrics", {})) > 4][:3]
        if rich:
            print(f"  Messages with extra metrics:")
            for r in rich:
                print(f"    {r.get('customer_id')}: {r.get('metrics')}")

if not converted:
    print("\nNo converted flag in messages. Will check ALL opened users for deposit events.")
    # Fallback: use opened users
    target_users = opened_msgs if opened_msgs else all_messages
    # For opened: use opened timestamp. For all: use sent timestamp.
    print(f"  Target users for deposit check: {len(target_users)}")
else:
    target_users = converted

# Step 5: Fetch deposit events
print(f"\n[4] Fetching deposits for {len(target_users)} users...")
total_deposits = 0.0
total_count = 0
user_deposits = []

for i, msg in enumerate(target_users):
    cust_id = msg.get("customer_id", msg.get("customer", {}).get("id"))
    if not cust_id:
        continue
    
    m = msg.get("metrics", {})
    opened_at = m.get("opened")
    sent_at = m.get("sent")
    ref_time = opened_at or sent_at
    window_start = ref_time if ref_time else None
    window_end = ref_time + (2 * 86400) if ref_time else None

    # Get cio_id from customer_identifiers (preferred) or customer_id
    cio_id = msg.get("customer_identifiers", {}).get("cio_id")
    
    # URL-encode customer_id (contains ':')
    cust_id_enc = quote(cust_id, safe='')
    
    # Try cio_id first, then id-based endpoints
    events_data = None
    endpoints = []
    if cio_id:
        endpoints.append(f"{BETA}/customers/{cio_id}/activities")
    endpoints.extend([
        f"{BETA}/customers/id:{cust_id_enc}/activities",
        f"{BETA}/customers/cio_id:{cio_id}/activities" if cio_id else None,
    ])
    endpoints = [e for e in endpoints if e]
    
    for endpoint in endpoints:
        events_data = api_get(endpoint, {"type": "event", "name": "deposit_made", "limit": 50})
        if events_data:
            if i == 0:
                print(f"  Working endpoint pattern: .../{endpoint.split('customers/')[1]}")
                evs = events_data.get("events", events_data.get("activities", []))
                if evs:
                    print(f"  Events found: {len(evs)}")
                    ev_data = evs[0].get("data", evs[0].get("attributes", {}))
                    print(f"  Event data keys: {sorted(ev_data.keys())}")
                    print(f"  Sample: {json.dumps(ev_data, indent=2)[:500]}")
                else:
                    print(f"  No deposit events for first user")
            break
    if not events_data:
        continue
    events = events_data.get("activities", events_data.get("events", []))
    
    # Filter only deposit_made events
    deposit_events = [e for e in events if e.get("name") == "deposit_made" or e.get("type") == "event"]
    user_total = 0.0
    user_count = 0
    for ev in deposit_events:
        ev_time = ev.get("timestamp", ev.get("created_at", 0))
        ev_data = ev.get("data", ev.get("attributes", {}))
        if window_start and window_end:
            if ev_time < window_start or ev_time > window_end:
                continue
        amount = ev_data.get("human_amount_total_rounded",
                 ev_data.get("human_amount_total",
                 ev_data.get("human_amount", 0)))
        try:
            amount = float(amount) if amount else 0
        except (ValueError, TypeError):
            amount = 0
        currency = ev_data.get("currency", "?")
        user_total += amount
        user_count += 1

    if user_count > 0:
        user_deposits.append({"customer_id": cust_id, "deposits": user_count, "total": user_total})
        total_deposits += user_total
        total_count += user_count
    if (i + 1) % 10 == 0:
        print(f"  Processed {i+1}/{len(target_users)}...")
    time.sleep(0.3)

print("\n" + "=" * 60)
print("RESULTS")
print("=" * 60)
print(f"Converted users: {len(converted)}")
print(f"Target users checked: {len(target_users)}")
print(f"Users with deposits: {len(user_deposits)}")
print(f"Total deposits: {total_count}")
print(f"Total amount: {total_deposits:.2f} EUR")
if user_deposits:
    print(f"Avg per depositor: {total_deposits / len(user_deposits):.2f} EUR")
    print(f"\nTop depositors:")
    user_deposits.sort(key=lambda x: x["total"], reverse=True)
    for u in user_deposits[:20]:
        print(f"  {u['customer_id']}: {u['deposits']}x, {u['total']:.2f} EUR")
