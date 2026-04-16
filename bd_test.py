"""
Test deposit sum for newsletter/broadcast 194119 (in-app).
"""
import sys, io, json, time
from urllib.parse import quote
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

API_KEY = "e22bae722fdd70a705135c9fa2270e1d"
ID = 194119
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
        print(f"  CONN ERROR: {e}")
        return None
    if r.status_code != 200:
        print(f"  ERROR {r.status_code}: {url}")
        print(f"  {r.text[:300]}")
        return None
    return r.json()

print("=" * 60)
print(f"ID #{ID} - Testing")
print("=" * 60)

# 1. Try as newsletter
print("\n[1] Try as newsletter...")
info = api_get(f"{BETA}/newsletters/{ID}")
if info:
    nl = info.get("newsletter", info)
    print(f"  Name: {nl.get('name', '?')}")
    print(f"  Type: {nl.get('type', '?')}")
    print(f"  State: {nl.get('state', '?')}")

# 2. Try as campaign
print("\n[2] Try as campaign...")
info2 = api_get(f"{BETA}/campaigns/{ID}")
if info2:
    c = info2.get("campaign", info2)
    print(f"  Name: {c.get('name', '?')}")
    print(f"  Type: {c.get('type', '?')}")
    print(f"  State: {c.get('state', '?')}")

# 3. Get metrics as newsletter
print("\n[3] Metrics as newsletter...")
metrics = api_get(f"{BASE}/newsletters/{ID}/metrics?version=2")
if metrics:
    m = metrics.get("metric", metrics)
    if "series" in m:
        totals = {k: sum(v) for k, v in m["series"].items()}
        print(f"  Totals: {json.dumps(totals, indent=2)}")

# 4. Get metrics as campaign
print("\n[4] Metrics as campaign...")
metrics2 = api_get(f"{BASE}/campaigns/{ID}/metrics?version=2")
if metrics2:
    m2 = metrics2.get("metric", metrics2)
    if "series" in m2:
        totals2 = {k: sum(v) for k, v in m2["series"].items()}
        print(f"  Totals: {json.dumps(totals2, indent=2)}")

# 5. Try messages with different types
print("\n[5] Getting messages...")
for msg_type in ['email', 'in_app', 'push', '']:
    params = {"newsletter_id": ID, "limit": 5}
    if msg_type:
        params["type"] = msg_type
    data = api_get(f"{BASE}/messages", params)
    if data:
        msgs = data.get("messages", [])
        label = msg_type or "any"
        print(f"  type={label}: {len(msgs)} messages")
        if msgs:
            sample = msgs[0]
            print(f"    sample type: {sample.get('type')}")
            print(f"    sample metrics: {sample.get('metrics')}")
            print(f"    sample keys: {list(sample.keys())}")
    time.sleep(0.3)

# 6. Try with metric=converted
print("\n[6] Getting converted messages...")
for msg_type in ['email', 'in_app', 'push', '']:
    params = {"newsletter_id": ID, "metric": "converted", "limit": 100}
    if msg_type:
        params["type"] = msg_type
    data = api_get(f"{BASE}/messages", params)
    if data:
        msgs = data.get("messages", [])
        label = msg_type or "any"
        print(f"  type={label} + converted: {len(msgs)} messages")
        if msgs:
            for ms in msgs[:3]:
                print(f"    cust: {ms.get('customer_id')} | metrics: {ms.get('metrics')} | type: {ms.get('type')}")
    time.sleep(0.3)

# 7. Also try via beta
print("\n[7] Beta API messages...")
for msg_type in ['in_app', '']:
    params = {"newsletter_id": ID, "metric": "converted", "limit": 100}
    if msg_type:
        params["type"] = msg_type
    data = api_get(f"{BETA}/newsletters/{ID}/messages", params)
    if data:
        msgs = data.get("messages", [])
        label = msg_type or "any"
        print(f"  beta type={label}: {len(msgs)} messages")
        if msgs:
            sample = msgs[0]
            print(f"    sample keys: {list(sample.keys())}")
            print(f"    sample metrics: {sample.get('metrics')}")
            print(f"    sample type: {sample.get('type')}")
            # Check for converted
            conv = [m for m in msgs if m.get("metrics", {}).get("converted")]
            print(f"    converted in batch: {len(conv)}")
    time.sleep(0.3)

# 8. Get ALL beta messages to find converted
print("\n[8] Fetching ALL beta messages for newsletter...")
all_msgs = []
start = ""
page = 0
while True:
    page += 1
    params = {"limit": 100}
    if start:
        params["start"] = start
    data = api_get(f"{BETA}/newsletters/{ID}/messages", params)
    if not data:
        break
    msgs = data.get("messages", [])
    if not msgs:
        break
    all_msgs.extend(msgs)
    if page <= 3 or page % 10 == 0:
        print(f"  Page {page}: +{len(msgs)} (total: {len(all_msgs)})")
    start = data.get("next", "")
    if not start:
        break
    time.sleep(0.5)

print(f"  Total: {len(all_msgs)}")
if all_msgs:
    types = {}
    for m in all_msgs:
        t = m.get("type", "?")
        types[t] = types.get(t, 0) + 1
    print(f"  By type: {types}")
    
    converted = [m for m in all_msgs if m.get("metrics", {}).get("converted")]
    print(f"  Converted: {len(converted)}")
    
    if converted:
        print(f"\n[9] Fetching deposits for {len(converted)} converted users...")
        total_amount = 0
        for i, msg in enumerate(converted):
            cio_id = msg.get("customer_identifiers", {}).get("cio_id")
            cust_id = msg.get("customer_id")
            if not cio_id:
                print(f"  {cust_id}: no cio_id, skipping")
                continue
            
            met = msg.get("metrics", {})
            ref_time = met.get("opened") or met.get("sent") or met.get("created") or 0
            window_end = ref_time + (2 * 86400) if ref_time else 0
            
            ev_data = api_get(f"{BETA}/customers/{cio_id}/activities", {"type": "event", "name": "deposit_made", "limit": 50})
            if not ev_data:
                continue
            
            activities = ev_data.get("activities", [])
            user_total = 0
            user_count = 0
            for ev in activities:
                ev_time = ev.get("timestamp", ev.get("created_at", 0))
                if ref_time and window_end:
                    if ev_time < ref_time or ev_time > window_end:
                        continue
                d = ev.get("data", ev.get("attributes", {}))
                amount = float(d.get("human_amount_total_rounded", d.get("human_amount_total", d.get("human_amount", 0))) or 0)
                user_total += amount
                user_count += 1
            
            total_amount += user_total
            print(f"  {cust_id} (cio:{cio_id}): {user_count}x deposits, {user_total:.0f} EUR")
            time.sleep(0.3)
        
        print(f"\n  TOTAL: {total_amount:.0f} EUR from {len(converted)} converted users")
