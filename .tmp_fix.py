from pathlib import Path
import os
fname = "oshi welcome flow texts EN-DE.txt"
# locate file
target = None
for root, dirs, files in os.walk("."):
    if fname in files:
        target = Path(root)/fname
        break
print("FILE:", target)
p = target
text = p.read_text(encoding="utf-8")
mapping = {
    "\u0440\u045F\u040B\u00B0": "\U0001F3B0",
    "\u0440\u045F\u040F\u2020": "\U0001F3C6",
    "\u0440\u045F\u040B\u040E": "\U0001F3A1",
    "\u0432\u00AD\u0452": "\u2B50",
    "\u0432\u040F\u0456": "\u23F3",
    "\u0440\u045F\u201D\u0490": "\U0001F525",
    "\u0440\u045F\u2019\u040E": "\U0001F48E",
    "n\u0413\u00B6tig": "n\u00F6tig",
}
counts = {k: text.count(k) for k in mapping}
for k, v in mapping.items():
    text = text.replace(k, v)
p.write_text(text, encoding="utf-8")
print("REPLACED:", counts)
for marker in ("\u0440\u045F", "\u0432\u040F", "\u0432\u00AD", "\u0413\u00B6"):
    print("REMAIN", repr(marker), text.count(marker))
print("--- Subject lines ---")
for line in text.splitlines():
    if line.startswith("Subject:"):
        print(line)