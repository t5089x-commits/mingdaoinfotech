# -*- coding: utf-8 -*-
"""產生 index.html 與 12 個單元頁。"""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import common
from common import UNITS, page, build_index, build_gate, build_access_info
import content_theory
import content_python

OUT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

BODIES = {}
BODIES.update(content_theory.BODIES)
BODIES.update(content_python.BODIES)

TOOLS = {}
TOOLS.update(getattr(content_theory, "TOOLS", {}))
TOOLS.update(getattr(content_python, "TOOLS", {}))

# 首頁
with open(os.path.join(OUT, "index.html"), "w", encoding="utf-8") as f:
    f.write(build_index())
print("寫入 index.html")

with open(os.path.join(OUT, "video-access.html"), "w", encoding="utf-8") as f:
    f.write(build_gate())
print("寫入 video-access.html")

with open(os.path.join(OUT, "access-mechanism.html"), "w", encoding="utf-8") as f:
    f.write(build_access_info())
print("寫入 access-mechanism.html")

# 各單元頁（與首頁同層，方便相對連結）
for u in UNITS:
    uid = u[0]
    if uid not in BODIES:
        print("!! 缺少內容：", uid)
        continue
    WIP = set()  # 待修改橫幅已全部移除
    html = page(uid, BODIES[uid], TOOLS.get(uid, ""), wip=(uid in WIP))
    with open(os.path.join(OUT, uid + ".html"), "w", encoding="utf-8") as f:
        f.write(html)
    print("寫入 %s.html  (%d 字元)" % (uid, len(html)))

print("完成，共", len(BODIES), "個單元頁 + 首頁")
