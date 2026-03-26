import re, os

folder = r'C:\Projects\REPORTS\тексти\пантери нова праця'
files = ['welcome - Table data.txt', 'nut 1 - Table data.txt', 'nut 2 - Table data.txt']

# Fields to KEEP by exact name
KEEP_FIELDS = {
    'name', 'locale',
    'instagram_href', 'facebook_href',
    'banner_href', 'logo_href', 'button_href_1',
}

# All known field labels
FIELD_RE = re.compile(
    r'^(name|locale|subject|preheader|from_id'
    r'|text_\d+|button_text_\d+|button_href_\d+'
    r'|promocode_button_\d+'
    r'|logo_src|logo_href|banner_src|banner_href'
    r'|instagram_src|instagram_href|facebook_src|facebook_href): '
)

for fname in files:
    path = os.path.join(folder, fname)
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Map field boundaries: (start_line, end_line, field_name)
    fields = []
    current_field = None
    current_start = None

    for i, line in enumerate(lines):
        m = FIELD_RE.match(line)
        if m:
            if current_field is not None:
                fields.append((current_start, i, current_field))
            current_field = m.group(1)
            current_start = i
    if current_field is not None:
        fields.append((current_start, len(lines), current_field))

    # Decide what to keep
    keep_lines = set()
    kept_count = 0
    removed_names = []

    for start, end, field_name in fields:
        content = ''.join(lines[start:end])

        keep = False
        if field_name in KEEP_FIELDS:
            keep = True
        elif field_name.startswith('text_') and 'es-text-1774' in content:
            keep = True  # copyright block

        if keep:
            kept_count += 1
            for i in range(start, end):
                keep_lines.add(i)
        else:
            removed_names.append(field_name)

    # Keep blank separator lines (not part of any field)
    all_field_lines = set()
    for start, end, _ in fields:
        for i in range(start, end):
            all_field_lines.add(i)

    for i in range(len(lines)):
        if i not in all_field_lines:
            keep_lines.add(i)

    new_lines = [lines[i] for i in sorted(keep_lines)]

    with open(path, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)

    print(f'\n{fname}:')
    print(f'  Kept {kept_count} fields, removed {len(removed_names)} fields')
    # Show unique removed field names
    unique_removed = sorted(set(removed_names))
    print(f'  Removed types: {", ".join(unique_removed)}')

print('\nDone')
