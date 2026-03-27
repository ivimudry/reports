import os

base = os.path.join("тексти", "пантери нова праця")

# Check what's in the problematic fields
print("DEP RET — Email #1, text_10 (line 14):")
with open(os.path.join(base, "DEP ret - Table data.txt"), "r", encoding="utf-8") as f:
    lines = f.readlines()
print(f"  {lines[14].strip()[:200]}")
print(f"\nDEP RET — Email #10, text_9 (line 274):")
print(f"  {lines[274].strip()[:200]}")
print(f"\nDEP RET — Email #9, text_10 (line 246):")
print(f"  {lines[246].strip()[:200]}")

print("\n\nNUT 1 — Email #1, text_10 (line 14):")
with open(os.path.join(base, "nut 1 - Table data.txt"), "r", encoding="utf-8") as f:
    lines = f.readlines()
print(f"  {lines[14].strip()[:200]}")

print("\n\nNUT 2 — Email #3, text_10 (line 14):")
with open(os.path.join(base, "nut 2 - Table data.txt"), "r", encoding="utf-8") as f:
    lines = f.readlines()
print(f"  {lines[14].strip()[:200]}")
print(f"\nNUT 2 — Email #1, text_9 (line 129):")
print(f"  {lines[129].strip()[:200]}")
