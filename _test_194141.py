import requests, json

API_KEY = 'e22bae722fdd70a705135c9fa2270e1d'
APP = 'https://api.customer.io/v1'
BETA = 'https://beta-api.customer.io/v1'
h = {'Authorization': 'Bearer ' + API_KEY}

# Get converted messages
r = requests.get(f'{APP}/messages?newsletter_id=194141&metric=converted&limit=5', headers=h)
msgs = r.json().get('messages', [])
print(f'Converted messages: {len(msgs)}')

for i, m in enumerate(msgs[:5]):
    ci = m.get('customer_identifiers') or {}
    cio_id = ci.get('cio_id', '')
    ci_email = ci.get('email', '')
    recipient = m.get('recipient', '')
    mtype = m.get('type', '')
    
    print(f'\n--- msg {i+1} ---')
    print(f'  type:       {mtype}')
    print(f'  recipient:  {recipient}')
    print(f'  ci.email:   {ci_email}')
    print(f'  ci.cio_id:  {cio_id}')
    
    # Check if email resolves
    email = ci_email or recipient or cio_id
    has_at = '@' in email
    print(f'  chosen:     {email} (has @: {has_at})')
    
    if not has_at and cio_id:
        r2 = requests.get(f'{BETA}/customers/{cio_id}/attributes', headers=h)
        if r2.status_code == 200:
            d = r2.json()
            cust = d.get('customer', d)
            resolved = cust.get('email') or (cust.get('attributes') or {}).get('email')
            print(f'  RESOLVED:   {resolved}')
        else:
            print(f'  resolve ERR: {r2.status_code}')
