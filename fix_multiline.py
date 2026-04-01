import os

fp = os.path.join('тексти/хейхо', 'Unsuccessful Deposit - Table data.txt')
with open(fp, 'r', encoding='utf-8') as f:
    content = f.read()
    lines = content.split('\n')

# Find all rich_text fields and check which are multiline
KNOWN_KEYS = {'name', 'locale', 'subject', 'preheader', 'from_id', 'rich_text',
              'button_text_1', 'button_href_1', 'button_text_2', 'button_href_2',
              'button_text_3', 'button_href_3',
              'logo_src', 'logo_href', 'banner_src', 'banner_href',
              'monkey_src', 'monkey_href', 'logo_botom_src', 'logo_botom_href',
              'bottom_logo_src', 'bottom_logo_href',
              'pirat_girl_src', 'pirat_girl_href',
              'promocode_button_1', 'text', 'text_2'}

new_lines = []
i = 0
fixes = 0

while i < len(lines):
    line = lines[i]
    
    # Check if this is a rich_text line
    if line.startswith('rich_text:'):
        rich_text_line = line
        # Collect continuation lines (lines that don't start a new known field)
        j = i + 1
        continuation_count = 0
        while j < len(lines):
            next_line = lines[j]
            # Check if this line starts a new field
            if ':' in next_line:
                key = next_line.split(':', 1)[0].strip()
                if key in KNOWN_KEYS:
                    break
            # This is a continuation of rich_text
            continuation_count += 1
            j += 1
        
        if continuation_count > 0:
            # Join all continuation lines with <br> replacement
            continuation_lines = lines[i+1:j]
            # Replace empty lines with <br> and join
            merged = rich_text_line
            for cl in continuation_lines:
                if cl.strip() == '':
                    merged += '<br>'
                else:
                    merged += cl
            
            new_lines.append(merged)
            fixes += 1
            print(f'Fixed multiline rich_text at line {i+1} ({continuation_count} extra lines merged)')
            # Show first 200 chars
            val = merged.split(':', 1)[1].strip()
            print(f'  Starts: {val[:100]}...')
            print(f'  Ends: ...{val[-100:]}')
            i = j
            continue
        else:
            new_lines.append(line)
    else:
        new_lines.append(line)
    
    i += 1

with open(fp, 'w', encoding='utf-8') as f:
    f.write('\n'.join(new_lines))

print(f'\nTotal fixes: {fixes}')
print(f'Lines before: {len(lines)}, after: {len(new_lines)}')
