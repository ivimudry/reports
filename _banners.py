"""Set banner_src per (email_num, geo)."""
import re
from pathlib import Path

DST = Path(r"c:\Projects\REPORTS\тексти\оші\тексти\Welcome Flow - Table data.txt")

BANNERS = {
    ("1","DEFAULT"): "https://userimg-assets.customeriomail.com/images/client-env-47372/01KPXKDQYHZ1PTBJNQ78RK4F2T.png",
    ("1","DE"):      "https://userimg-assets.customeriomail.com/images/client-env-47372/01KPXKEBNAJ92HC51JVQT1Z4GS.png",
    ("1","AU"):      "https://userimg-assets.customeriomail.com/images/client-env-47372/01KPXKK6FJFHEQ81JDF7D7863H.png",
    ("1","CA"):      "https://userimg-assets.customeriomail.com/images/client-env-47372/01KPXKF0M1SG3CE53Z508Q195M.png",
    ("2","DEFAULT"): "https://userimg-assets.customeriomail.com/images/client-env-47372/01KPXKDQJ11EA158XQ4YJ23P00.png",
    ("2","DE"):      "https://userimg-assets.customeriomail.com/images/client-env-47372/01KPXKEB53PA2F634SV2DHKM7C.png",
    ("2","AU"):      "https://userimg-assets.customeriomail.com/images/client-env-47372/01KPXKK6BHGNE93CEEEVMJMJPY.png",
    ("2","CA"):      "https://userimg-assets.customeriomail.com/images/client-env-47372/01KPXKF06E0ZZPYE400BS3EWJY.png",
    ("3","DEFAULT"): "https://userimg-assets.customeriomail.com/images/client-env-47372/01KPXKDR0KPFACE22X44JX9ARM.png",
    ("3","DE"):      "https://userimg-assets.customeriomail.com/images/client-env-47372/01KPXKEBK9ZWT1XCVX5WH4K2ZZ.png",
    ("3","AU"):      "https://userimg-assets.customeriomail.com/images/client-env-47372/01KPXKK6FW2BT71NBQZ3E1S5DA.png",
    ("3","CA"):      "https://userimg-assets.customeriomail.com/images/client-env-47372/01KPXKF0NV7K3KTM2GZY7K676D.png",
    ("4","DEFAULT"): "https://userimg-assets.customeriomail.com/images/client-env-47372/01KPXKDRD5BZBM6D0VWBX6QE8K.png",
    ("4","DE"):      "https://userimg-assets.customeriomail.com/images/client-env-47372/01KPXKEBXFPM2KW26RCJVFQ26G.png",
    ("4","AU"):      "https://userimg-assets.customeriomail.com/images/client-env-47372/01KPXKK6RYGM1FC50DYKDP1334.png",
    ("4","CA"):      "https://userimg-assets.customeriomail.com/images/client-env-47372/01KPXKF1F2KQPRV67YXKST59GZ.png",
    ("5","DEFAULT"): "https://userimg-assets.customeriomail.com/images/client-env-47372/01KPXKDRRWVFD4TRAHH37K5ZQB.png",
    ("5","DE"):      "https://userimg-assets.customeriomail.com/images/client-env-47372/01KPXKEC1KCT3THA47F88GF2ZZ.png",
    ("5","AU"):      "https://userimg-assets.customeriomail.com/images/client-env-47372/01KPXKK7917S87KMY1G7GH12DV.png",
    ("5","CA"):      "https://userimg-assets.customeriomail.com/images/client-env-47372/01KPXKF1HB6XMXFS3G7JE0MES7.png",
    ("6","DEFAULT"): "https://userimg-assets.customeriomail.com/images/client-env-47372/01KPXKDSW2SWPS657W91KD8JT1.png",
    ("6","DE"):      "https://userimg-assets.customeriomail.com/images/client-env-47372/01KPXKEE0TM0M5JY960B04HQCP.png",
    ("6","AU"):      "https://userimg-assets.customeriomail.com/images/client-env-47372/01KPXKK9HQYNZYA3Z7CZB0SF6Y.png",
    ("6","CA"):      "https://userimg-assets.customeriomail.com/images/client-env-47372/01KPXKF2YXKHNV13BR9ZAHEJJJ.png",
    ("7","DEFAULT"): "https://userimg-assets.customeriomail.com/images/client-env-47372/01KPXKDTS5XY5JR8BMKNTD5JCP.png",
    ("7","DE"):      "https://userimg-assets.customeriomail.com/images/client-env-47372/01KPXKEEB16MZEQQAE4PY8S455.png",
    ("7","AU"):      "https://userimg-assets.customeriomail.com/images/client-env-47372/01KPXKK8QMV24PGS2MA1VFCCX0.png",
    ("7","CA"):      "https://userimg-assets.customeriomail.com/images/client-env-47372/01KPXKF3C9P9XMKRJJ3VJ91591.png",
    ("8","DEFAULT"): "https://userimg-assets.customeriomail.com/images/client-env-47372/01KPXKDTV3X5J68J7YQ6P26D9D.png",
    ("8","DE"):      "https://userimg-assets.customeriomail.com/images/client-env-47372/01KPXKEECY31Z4721WX5SHT7K3.png",
    ("8","AU"):      "https://userimg-assets.customeriomail.com/images/client-env-47372/01KPXKK9HPEGWAPGBTMX6YFNX2.png",
    ("8","CA"):      "https://userimg-assets.customeriomail.com/images/client-env-47372/01KPXKF3DXMQ64FZKSBNT9Z7NT.png",
}

# Sanity: all unique
assert len(set(BANNERS.values())) == 32, "Duplicate URL detected"

lines = DST.read_text(encoding="utf-8").splitlines(keepends=True)
name_re = re.compile(r"^name:\s*Email\s+(\d+)(?:\s+(AU|CA|DE))?\s*$")

email_num = None
geo = "DEFAULT"
changes = 0

for i, line in enumerate(lines):
    m = name_re.match(line)
    if m:
        email_num = m.group(1)
        geo = m.group(2) or "DEFAULT"
        continue
    if line.startswith("banner_src:") and email_num:
        url = BANNERS.get((email_num, geo))
        if not url:
            continue
        eol = "\r\n" if line.endswith("\r\n") else "\n"
        new = f"banner_src: {url}{eol}"
        if new != line:
            lines[i] = new
            changes += 1

DST.write_text("".join(lines), encoding="utf-8", newline="")
print(f"Updated {changes} banner_src lines")
