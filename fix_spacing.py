"""
Fix empty lines between email blocks in the Unsuccessful Deposit file.
Ensures exactly one empty line separates each block (block starts with 'name: ').
Also verifies all rich_text fields are single-line.
"""
import pathlib

fp = pathlib.Path(r"тексти\хейхо\Unsuccessful Deposit - Table data.txt")
lines = fp.read_text(encoding="utf-8").splitlines()

print(f"Total lines before: {len(lines)}")

# Check for multiline rich_text first
multiline_issues = []
for i, line in enumerate(lines, 1):
    if not line.startswith("rich_text:") and not line.startswith("name:") and \
       not line.startswith("locale:") and not line.startswith("subject:") and \
       not line.startswith("preheader:") and not line.startswith("from_id:") and \
       not line.startswith("text_") and not line.startswith("button_") and \
       not line.startswith("promocode_") and not line.startswith("logo_") and \
       not line.startswith("pirat_girl_") and not line.startswith("banner_") and \
       not line.startswith("monkey_") and not line.startswith("bottom_logo_") and \
       line.strip() != "":
        multiline_issues.append((i, line[:80]))

if multiline_issues:
    print(f"\nWARNING: {len(multiline_issues)} potential multiline issues:")
    for ln, txt in multiline_issues:
        print(f"  Line {ln}: {txt}")
else:
    print("No multiline issues found - all fields are single-line.")

# Now fix spacing: ensure exactly one empty line before each 'name:' line (except the first)
new_lines = []
for i, line in enumerate(lines):
    if line.startswith("name: ") and i > 0:
        # Remove any trailing empty lines before this block
        while new_lines and new_lines[-1] == "":
            new_lines.pop()
        # Add exactly one empty line
        new_lines.append("")
    new_lines.append(line)

# Remove trailing empty lines at end of file
while new_lines and new_lines[-1] == "":
    new_lines.pop()

print(f"Total lines after: {len(new_lines)}")

# Count blocks
blocks = sum(1 for l in new_lines if l.startswith("name: "))
print(f"Total blocks: {blocks}")

# Verify all blocks are separated by empty lines
for i, line in enumerate(new_lines):
    if line.startswith("name: ") and i > 0:
        if new_lines[i-1] != "":
            print(f"ERROR: Block at line {i+1} not preceded by empty line!")

fp.write_text("\n".join(new_lines) + "\n", encoding="utf-8")
print("\nFile updated successfully!")
