"""產生紙本講義：第 1～3 次課回家識讀練習、第 4 次課識讀模擬考，以及教師用解答。"""
import os, pymupdf
import py125 as W
from py125_pdf import build, FONT

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets", "handouts")
if not os.path.isdir(OUT):
    OUT = "/home/claude/w/out/apcs-ee/assets/handouts"
os.makedirs(OUT, exist_ok=True)
# 模擬考與教師用解答「不要」放進網站資料夾（GitHub repo 是公開的），寫到課程資料夾外面
TEACHER = os.path.normpath(os.path.join(OUT, "..", "..", "..", "apcs-ee-teacher-only"))
os.makedirs(TEACHER, exist_ok=True)

SETS = [
    ("hw1", "第 1 次課　回家識讀練習", ["unit02.html", "unit03.html", "unit04.html", "unit04b.html"]),
    ("hw2", "第 2 次課　回家識讀練習", ["unit05.html", "unit06.html", "unit07.html"]),
    ("hw3", "第 3 次課　回家識讀練習（含考前加練）", ["unit06b.html", "unit07b.html", "unit09.html"]),
]
FILES = {"hw1": "hw1-reading.pdf", "hw2": "hw2-reading.pdf", "hw3": "hw3-reading.pdf",
         "mock": "mock-reading-30.pdf", "key": "answer-key-teacher.pdf"}

def set_qs(units):
    return sorted(q for f in units for q in W.open_qs(W.unit_qs(f)[2]))

def make_all():
    info = {}
    for key, title, units in SETS:
        qs = set_qs(units)
        labels = "、".join(W.unit_qs(f)[0] for f in units)
        cnt = {d: sum(W.DIFF[q] == d for q in qs) for d in "易中難"}
        n = build(qs, os.path.join(OUT, FILES[key]), "資電APCS週六課程　" + title,
                  f"範圍：{labels}　共 {len(qs)} 題（易 {cnt['易']}、中 {cnt['中']}、難 {cnt['難']}），題號與原題本相同",
                  note=["作答方式：每一題都用紙筆追蹤，不要用電腦執行。先做「易」「中」，「難」是挑戰題。",
                        "題目右上方標有難度。寫完後對照吳邦一〈Python 程式識讀 125 題〉後半的解答，錯的題目回去看對應單元。"],
                  tags={q: W.DIFF[q] for q in qs})
        info[key] = (qs, n)
    qs = W.MOCK
    n = build(qs, os.path.join(TEACHER, FILES["mock"]), "資電APCS週六課程　第 4 次課　程式識讀模擬考",
              "共 30 題單選，限時 90 分鐘。題目選自吳邦一〈APCS Python 程式識讀 125 題〉，題號與原題本相同",
              note=["作答時不可使用電腦，可以在題目旁邊空白處畫追蹤表。每題的選項中，「執行錯誤」表示程式執行時會出錯。",
                    "計分參考：每題 1 分，答對 21 題以上約等於 APCS 程式識讀 4 級分（70 分）。"])
    info["mock"] = (qs, n)
    # 教師用解答
    doc = pymupdf.open()
    pg = doc.new_page(width=595.32, height=841.92)
    pg.insert_font(fontname="cjk", fontfile=FONT)
    y = 56
    pg.insert_text((40, y), "教師用解答　資電APCS週六課程（吳邦一〈APCS Python 程式識讀 125 題〉）", fontname="cjk", fontsize=13)
    y += 18
    pg.insert_text((40, y), "詳解請看原題本後半（第 50 頁起），題號相同。答案由原題本解答整理。", fontname="cjk", fontsize=9, color=(0.35, 0.35, 0.35))
    y += 14
    for key, title in [("hw1", "第 1 次課回家練習"), ("hw2", "第 2 次課回家練習"), ("hw3", "第 3 次課回家練習"), ("mock", "第 4 次課識讀模擬考")]:
        qs = info[key][0]
        cols = 8
        rows = (len(qs) + cols - 1) // cols
        if y + 30 + rows * 17 > 800:
            pg = doc.new_page(width=595.32, height=841.92); pg.insert_font(fontname="cjk", fontfile=FONT); y = 56
        y += 22
        pg.insert_text((40, y), f"{title}（{len(qs)} 題）", fontname="cjk", fontsize=11)
        y += 6
        cw = (595.32 - 80) / cols
        for i, q in enumerate(qs):
            r, c = divmod(i, cols)
            pg.insert_text((40 + c * cw, y + 15 + r * 17), f"Q{q:03d}  {W.ANS[q]}  {W.DIFF[q]}", fontname="cjk", fontsize=9.5)
        y += 15 + rows * 17
    doc.save(os.path.join(TEACHER, FILES["key"]), garbage=4, deflate=True)
    return info

if __name__ == "__main__":
    for k, (qs, n) in make_all().items():
        print(k, len(qs), "題", n, "頁")
