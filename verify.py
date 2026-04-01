fp = open(r"тексти\хейхо\Unsuccessful Deposit - Table data.txt", encoding="utf-8")
lines = fp.readlines()
fp.close()
for i, line in enumerate(lines, 1):
    s = line.rstrip("\n")
    if s.startswith("name:") or s == "":
        label = s[:60] if s else "(empty)"
        print(f"Line {i}: {label}")
