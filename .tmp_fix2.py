from pathlib import Path
p = Path("тексти/оші/тексти/oshi welcome flow texts EN-DE.txt")
text = p.read_text(encoding="utf-8")
key = "\u0440\u045F\u2019\u040B"
print("count diamond mojibake:", text.count(key))
text = text.replace(key, "\U0001F48E")
p.write_text(text, encoding="utf-8")
for marker in ("\u0440\u045F", "\u0432\u040F", "\u0432\u00AD", "\u0413\u00B6"):
    print("REMAIN", repr(marker), text.count(marker))
print("--- Subject lines ---")
for line in text.splitlines():
    if line.startswith("Subject:"):
        print(line)