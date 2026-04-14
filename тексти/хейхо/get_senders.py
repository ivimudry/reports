import urllib.request, json

req = urllib.request.Request(
    'https://api.customer.io/v1/sender_identities',
    headers={'Authorization': 'Bearer 6cea0aa9f8e5397fbe67d93f8871730c'}
)
resp = urllib.request.urlopen(req)
data = json.loads(resp.read())

for s in data.get('sender_identities', []):
    sid = s['id']
    name = s.get('name', '')
    email = s.get('email', '')
    addr = s.get('address', '')
    ttype = s.get('template_type', '')
    auto = s.get('auto_generated', False)
    print(f"ID: {sid}  |  type: {ttype}  |  name: {name}  |  email: {email}  |  auto: {auto}")
    print(f"          address: {addr}")
    print()
