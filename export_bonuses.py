import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from collections import defaultdict

# Read original file
wb = openpyxl.load_workbook('C:/Projects/REPORTS/Book1.xlsx')
ws = wb.active

# Find all data rows
rows_data = []
current_section = None

for row in ws.iter_rows(min_row=1, max_col=20, values_only=False):
    cells = [c.value for c in row]
    
    # Detect section headers (merged cells or bold text in first column)
    first_val = str(cells[0]).strip() if cells[0] else ''
    
    # Check if this is a header/section row
    if row[0].font and row[0].font.bold and first_val and not any(c for c in cells[1:] if c):
        current_section = first_val
        continue
    
    # Skip empty rows
    if not any(c for c in cells if c):
        continue
    
    rows_data.append((current_section, cells, row))

print(f"Total rows found (excluding headers/empty): {len(rows_data)}")

# Let me just read ALL rows properly
wb2 = openpyxl.load_workbook('C:/Projects/REPORTS/Book1.xlsx')
ws2 = wb2.active

print(f"\nSheet dimensions: {ws2.dimensions}")
print(f"Max row: {ws2.max_row}, Max col: {ws2.max_column}")

# Print all rows to understand the structure
print("\n=== ALL ROWS ===")
for i, row in enumerate(ws2.iter_rows(min_row=1, max_row=ws2.max_row, max_col=ws2.max_column, values_only=True), 1):
    vals = [str(v) if v is not None else '' for v in row]
    non_empty = [v for v in vals if v]
    if non_empty:
        print(f"Row {i}: {' | '.join(vals[:10])}")
