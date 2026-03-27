"""Download unique Stripo payment icons as PNG."""
import os, urllib.request

OUT = r'C:\Projects\REPORTS\тексти\пантери нова праця\stripo_icons'

# Unique icon URLs with descriptive names
ICONS = {
    'capitec_pay.png': 'https://ebhum.stripocdn.email/content/guids/CABINET_09fae30a7f570fc256d68035eca0ce1825ea46286e748934b00abc3781ad7c61/images/frame_1353_1.png',
    'apple_pay.png': 'https://ebhum.stripocdn.email/content/guids/CABINET_09fae30a7f570fc256d68035eca0ce1825ea46286e748934b00abc3781ad7c61/images/frame_1352.png',
    'visa.png': 'https://ebhum.stripocdn.email/content/guids/CABINET_09fae30a7f570fc256d68035eca0ce1825ea46286e748934b00abc3781ad7c61/images/frame_1357.png',
    'ozow.png': 'https://ebhum.stripocdn.email/content/guids/CABINET_09fae30a7f570fc256d68035eca0ce1825ea46286e748934b00abc3781ad7c61/images/frame_1359.png',
    'scan_to_pay.png': 'https://ebhum.stripocdn.email/content/guids/CABINET_09fae30a7f570fc256d68035eca0ce1825ea46286e748934b00abc3781ad7c61/images/frame_1360.png',
    'mastercard.png': 'https://ebhum.stripocdn.email/content/guids/CABINET_09fae30a7f570fc256d68035eca0ce1825ea46286e748934b00abc3781ad7c61/images/frame_1354.png',
    'eftsecure.png': 'https://ebhum.stripocdn.email/content/guids/CABINET_09fae30a7f570fc256d68035eca0ce1825ea46286e748934b00abc3781ad7c61/images/frame_1356.png',
    'ott_voucher.png': 'https://ebhum.stripocdn.email/content/guids/CABINET_09fae30a7f570fc256d68035eca0ce1825ea46286e748934b00abc3781ad7c61/images/frame_1361.png',
    '1voucher.png': 'https://ebhum.stripocdn.email/content/guids/CABINET_09fae30a7f570fc256d68035eca0ce1825ea46286e748934b00abc3781ad7c61/images/frame_1362.png',
    'shop2shop.png': 'https://ebhum.stripocdn.email/content/guids/CABINET_09fae30a7f570fc256d68035eca0ce1825ea46286e748934b00abc3781ad7c61/images/frame_1363.png',
    # Email 2 has a different CABINET for capitec_pay
    'capitec_pay_v2.png': 'https://ebhum.stripocdn.email/content/guids/CABINET_df25bb8b647418aef0bda0514cbf2842ee8f30cbc5f44ba54c3485f68dd01773/images/frame_1353_1.png',
}

for name, url in ICONS.items():
    fpath = os.path.join(OUT, name)
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as resp, open(fpath, 'wb') as f:
            f.write(resp.read())
        size = os.path.getsize(fpath)
        print(f'  OK  {name} ({size:,} bytes)')
    except Exception as e:
        print(f'  FAIL {name}: {e}')

print(f'\nDone: {len(ICONS)} icons downloaded to stripo_icons/')
