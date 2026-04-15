"""Download all banner images from Celsius campaign Default locales."""
import os
import urllib.request
import ssl

DIR = r'c:\Projects\REPORTS\тексти\Celsius'
OUT = r'c:\Projects\REPORTS\тексти\Celsius\Банери'

# Skip SSL verification for CDN URLs
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def parse_blocks(filepath):
    blocks = []
    current = {}
    for line in open(filepath, 'r', encoding='utf-8'):
        line = line.rstrip('\n')
        if not line.strip():
            if current:
                blocks.append(current)
                current = {}
            continue
        if ':' in line:
            key, val = line.split(':', 1)
            current[key.strip()] = val.strip()
    if current:
        blocks.append(current)
    return blocks

def clean_url(url):
    return url.split('?')[0] if '?' in url else url

def download(url, dest):
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        resp = urllib.request.urlopen(req, context=ctx)
        with open(dest, 'wb') as f:
            f.write(resp.read())
        return True
    except Exception as e:
        print(f'  ERROR: {e}')
        return False

files = sorted(f for f in os.listdir(DIR) if f.endswith('.txt'))
total = 0
ok = 0

for fname in files:
    campaign = fname.replace(' - Table data.txt', '')
    campaign_dir = os.path.join(OUT, campaign)
    os.makedirs(campaign_dir, exist_ok=True)

    blocks = parse_blocks(os.path.join(DIR, fname))

    seen = set()
    for b in blocks:
        if b.get('locale') != 'Default':
            continue
        name = b.get('name', '')
        banner = b.get('banner_src', '')
        if not banner or name in seen:
            continue
        seen.add(name)

        clean = clean_url(banner)
        ext = '.png'
        lower = clean.lower()
        if '.jpg' in lower or '.jpeg' in lower:
            ext = '.jpg'
        elif '.gif' in lower:
            ext = '.gif'
        elif '.webp' in lower:
            ext = '.webp'

        dest = os.path.join(campaign_dir, f'{name}{ext}')
        total += 1
        print(f'[{campaign}] {name} ... ', end='', flush=True)
        if download(clean, dest):
            size_kb = os.path.getsize(dest) / 1024
            print(f'OK ({size_kb:.0f} KB)')
            ok += 1
        else:
            print('FAILED')

print(f'\nDone: {ok}/{total} banners downloaded to {OUT}')
"""Download all Default-locale banner images from Celsius campaign files."""
import os, re, urllib.request, urllib.parse, ssl

DIR = r'c:\Projects\REPORTS\тексти\Celsius'
OUT = r'c:\Projects\REPORTS\тексти\Celsius\Банери'

# Allow HTTPS without cert issues
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

files = sorted(f for f in os.listdir(DIR) if f.endswith('.txt'))

total = 0
errors = []

for fn in files:
    campaign = fn.replace(' - Table data.txt', '')
    path = os.path.join(DIR, fn)
    lines = open(path, 'r', encoding='utf-8').readlines()

    # Parse blocks
    blocks = []
    current = {}
    for line in lines:
        line = line.rstrip('\n')
        if not line.strip():
            if current:
                blocks.append(current)
                current = {}
            continue
        if ':' in line:
            key, val = line.split(':', 1)
            current[key.strip()] = val.strip()
    if current:
        blocks.append(current)

    # Group by email name, pick Default locale
    for b in blocks:
        if b.get('locale') != 'Default':
            continue
        name = b.get('name', '').strip()
        banner_src = b.get('banner_src', '').strip()
        if not banner_src:
            print(f'  [SKIP] {campaign}/{name} — no banner_src')
            continue

        # Strip UTM params for clean download URL
        url_clean = banner_src.split('?')[0]

        # Determine extension from URL
        ext = '.png'
        lower = url_clean.lower()
        if lower.endswith('.jpg') or lower.endswith('.jpeg'):
            ext = '.jpg'
        elif lower.endswith('.gif'):
            ext = '.gif'
        elif lower.endswith('.webp'):
            ext = '.webp'

        # Create output dir
        out_dir = os.path.join(OUT, campaign)
        os.makedirs(out_dir, exist_ok=True)

        out_file = os.path.join(out_dir, f'{name}{ext}')
        print(f'  [{campaign}] {name}{ext} ... ', end='', flush=True)
        try:
            req = urllib.request.Request(url_clean, headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
            })
            resp = urllib.request.urlopen(req, context=ctx, timeout=30)
            data = resp.read()
            with open(out_file, 'wb') as f:
                f.write(data)
            size_kb = len(data) / 1024
            print(f'OK ({size_kb:.0f} KB)')
            total += 1
        except Exception as e:
            print(f'ERROR: {e}')
            errors.append(f'{campaign}/{name}: {e}')

print(f'\nDone! Downloaded {total} banners.')
if errors:
    print(f'\nErrors ({len(errors)}):')
    for e in errors:
        print(f'  - {e}')
