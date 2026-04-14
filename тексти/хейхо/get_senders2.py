import urllib.request, json, sys

try:
    req = urllib.request.Request(
        'https://api.customer.io/v1/sender_identities',
        headers={'Authorization': 'Bearer 6cea0aa9f8e5397fbe67d93f8871730c'}
    )
    resp = urllib.request.urlopen(req, timeout=30)
    raw = resp.read()
    print(f"Status: {resp.status}")
    data = json.loads(raw)
    senders = data.get('sender_identities', [])
    print(f"Found {len(senders)} senders\n")
    
    for s in senders:
        sid = s.get('id', '?')
        name = s.get('name', '')
        email = s.get('email', '')
        addr = s.get('address', '')
        ttype = s.get('template_type', '')
        auto = s.get('auto_generated', False)
        print(f"ID: {sid}  |  type: {ttype}  |  auto: {auto}")
        print(f"  name: {name}")
        print(f"  email: {email}")
        print(f"  address: {addr}")
        print()

except Exception as e:
    print(f"ERROR: {e}", file=sys.stderr)
    import traceback
    traceback.print_exc()
