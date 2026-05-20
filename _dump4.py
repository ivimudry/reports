from openpyxl import load_workbook
import sys
sys.stdout.reconfigure(encoding='utf-8')
wb = load_workbook(r"c:\Projects\CLIENTS\CHEEL4REEL\інше\Loyalty_Program_Adjustment_C4R.xlsx", data_only=True)
ws = wb["Loyalty Program"]
for i,row in enumerate(ws.iter_rows(values_only=True),1):
    vals = list(row)
    while vals and (vals[-1] is None or not str(vals[-1]).strip()):
        vals.pop()
    if not vals: continue
    print(f"R{i}: " + " | ".join("" if v is None else str(v).replace("\n"," / ") for v in vals))
