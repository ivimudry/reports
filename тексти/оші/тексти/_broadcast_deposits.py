"""
Calculate total deposit amounts from converted users of broadcast #194166.
Steps:
1. Get broadcast messages (sent emails)
2. Filter converted recipients
3. For each converted user, fetch deposit_made events within conversion window
4. Sum human_amount_total_rounded
"""
import sys, io, json, time
import requests

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

API_KEY = "e22bae722fdd70a705135c9fa2270e1d"
BROADCAST_ID = 194166
BASE = "https://api.customer.io/v1"
BETA = "https://beta-api.customer.io/v1"

HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

def api_get(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params, timeout=30)
    if r.status_code != 200:
        print(f"  ERROR {r.status_code}: {url}")
        print(f"  {r.text[:500]}")
        return None
    return r.json()

# Step 1: Get broadcast info
print("=" * 60)
print(f"BROADCAST #{BROADCAST_ID} - Deposit Analysis")
print("=" * 60)

print("\n[1] Getting broadcast info...")
info = api_get(f"{BETA}/newsletters/{BROADCAST_ID}")
if info:
    nl = info.get("newsletter", info)
    print(f"  Name: {nl.get('name', '?')}")
    print(f"  Subject: {nl.get('subject', '?')}")
    print(f"  Created: {nl.get('created', '?')}")
    print(f"  Type: {nl.get('type', '?')}")
else:
    # Try campaigns endpoint
    info = api_get(f"{BETA}/campaigns/{BROADCAST_ID}")
    if info:
        c = info.get("campaign", info)
        print(f"  Name: {c.get('name', '?')}")

# Step 2: Get metrics
print("\n[2] Getting broadcast metrics...")
metrics = api_get(f"{BETA}/newsletters/{BROADCAST_ID}/metrics")
if not metrics:
    metrics = api_get(f"{BASE}/newsletters/{BROADCAST_ID}/metrics")
if metrics:
    m = metrics.get("metric", metrics.get("metrics", metrics))
    print(f"  Metrics: {json.dumps(m, indent=2)[:1000]}")

# Step 3: Get messages (recipients)
print("\n[3] Getting broadcast messages (recipients)...")
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
        # Try campaigns endpoint
        data = api_get(f"{BETA}/campaigns/{BROADCAST_ID}/messages", params)
    if not data:
        break
    
    messages = data.get("messages", [])
    if not messages:
        break
    
    all_messages.extend(messages)
    print(f"  Page {page}: +{len(messages)} messages (total: {len(all_messages)})")
    
    # Check for next page
    start = data.get("next", "")
    if not start:
        break
    
    time.sleep(0.2)  # rate limit

print(f"\n  Total messages: {len(all_messages)}")

if not all_messages:
    print("\nNo messages found. Trying alternative approach...")
    # Try to list via actions endpoint
    actions = api_get(f"{BETA}/newsletters/{BROADCAST_ID}/metrics/actions")
    if actions:
        print(f"  Actions: {json.dumps(actions, indent=2)[:2000]}")
    sys.exit(0)

# Step 4: Find converted recipients
converted = [m for m in all_messages if m.get("converted")]
opened = [m for m in all_messages if m.get("opened")]
print(f"  Opened: {len(opened)}")
print(f"  Converted: {len(converted)}")

if not converted:
    print("\nNo converted users found.")
    # Show sample message structure
    if all_messages:
        print(f"\nSample message keys: {list(all_messages[0].keys())}")
        print(f"Sample: {json.dumps(all_messages[0], indent=2)[:1000]}")
    sys.exit(0)

# Step 5: For each converted user, get deposit_made events
print(f"\n[4] Fetching deposit_made events for {len(converted)} converted users...")

total_deposits = 0.0
total_count = 0
user_deposits = []

for i, msg in enumerate(converted):
    cust_id = msg.get("customer_id", msg.get("customer", {}).get("id"))
    if not cust_id:
        continue
    
    opened_at = msg.get("opened")
    sent_at = msg.get("sent")
    ref_time = opened_at or sent_at
    
    if ref_time:
        window_start = ref_time
        window_end = ref_time + (2 * 86400)  # 2 days in seconds
    else:
        window_start = None
        window_end = None
    
    # Get customer events
    events_data = api_get(
        f"{BETA}/customers/{cust_id}/events",
        {"name": "deposit_made", "limit": 50}
    )
    
    if not events_data:
        # Try activities endpoint
        events_data = api_get(
            f"{BETA}/customers/{cust_id}/activities",
            {"type": "event", "name": "deposit_made", "limit": 50}
        )
    
    if not events_data:
        continue
    
    events = events_data.get("events", events_data.get("activities", []))
    
    user_total = 0.0
    user_count = 0
    
    for ev in events:
        ev_time = ev.get("timestamp", ev.get("created_at", 0))
        ev_data = ev.get("data", ev.get("attributes", {}))
        
        # Check if within conversion window
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
        user_deposits.append({
            "customer_id": cust_id,
            "deposits": user_count,
            "total": user_total
        })
        total_deposits += user_total
        total_count += user_count
    
    if (i + 1) % 10 == 0:
        print(f"  Processed {i+1}/{len(converted)} users...")
    
    time.sleep(0.15)  # rate limit

# Results
print("\n" + "=" * 60)
print("RESULTS")
print("=" * 60)
print(f"Total converted users: {len(converted)}")
print(f"Users with deposits in window: {len(user_deposits)}")
print(f"Total deposit count: {total_count}")
print(f"Total deposit amount: {total_deposits:.2f} EUR")
print(f"Average per depositor: {total_deposits / len(user_deposits):.2f} EUR" if user_deposits else "")

if user_deposits:
    print(f"\nTop depositors:")
    user_deposits.sort(key=lambda x: x["total"], reverse=True)
    for u in user_deposits[:20]:
        print(f"  {u['customer_id']}: {u['deposits']} deposits, {u['total']:.2f} EUR")
