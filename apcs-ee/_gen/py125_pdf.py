"""從吳邦一〈Python 程式識讀 125 題〉PDF 剪出指定題目（題目本，不含解答），組成新的講義 PDF。
保留原本的向量字體與題號；題目順序由小到大。"""
import pymupdf, re, os, json

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets", "reading", "wu-python-reading-125.pdf")
if not os.path.exists(SRC):
    SRC = "/home/claude/w/py125/p.pdf"
FONT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cjk-subset.ttf")   # 文泉驛正黑，只保留講義用到的字

def _hlines(pg):
    ys = []
    for d in pg.get_drawings():
        r = d["rect"]
        f = d.get("fill")
        if r.width > 200 and r.height < 2 and f and max(f) < 0.2:
            ys.append(round(r.y0, 1))
    ys.sort()
    out = []
    for y in ys:
        if not out or y - out[-1] > 2:
            out.append(y)
    return out

def question_segments(doc, qpages, last_qpage=48):
    """回傳 {題號: [(頁索引, 上緣, 下緣), ...]}（一題可能跨兩頁）。"""
    marks = []   # (page_index, y, q)
    for pno in range(2, last_qpage):
        for w in doc[pno].get_text("words"):
            m = re.fullmatch(r"Q\.(\d{3})\.?", w[4])
            if m:
                marks.append((pno, w[1], int(m.group(1))))
    marks.sort()
    lines = {pno: _hlines(doc[pno]) for pno in range(2, last_qpage + 1)}
    segs = {}
    for k, (pno, y, q) in enumerate(marks):
        L = lines[pno]
        top = max([v for v in L if v <= y], default=y - 12)
        nxt = marks[k + 1] if k + 1 < len(marks) else None
        seg = []
        if nxt and nxt[0] == pno:
            ntop = max([v for v in L if v <= nxt[1]])
            bottom = max([v for v in L if v < ntop - 2])
            seg.append((pno, top, bottom))
        else:
            seg.append((pno, top, max(L)))
            # 下一頁開頭如果還有這一題的內容（跨頁），也要接上
            p2 = pno + 1
            if p2 <= last_qpage:
                L2 = lines[p2]
                first_mark = nxt[1] if (nxt and nxt[0] == p2) else None
                if L2:
                    cont_top = min(L2)
                    if first_mark is None:
                        seg.append((p2, cont_top, max(L2)))
                    else:
                        ntop = max([v for v in L2 if v <= first_mark])
                        if ntop - cont_top > 8:      # 下一題的方框上面還有一段 → 是這題的續頁
                            bottom = max([v for v in L2 if v < ntop - 2])
                            seg.append((p2, cont_top, bottom))
        segs[q] = seg
    return segs

def build(qs, out_path, title, subtitle, answer_sheet=True, note=None, tags=None):
    src = pymupdf.open(SRC)
    segs = question_segments(src, None)
    out = pymupdf.open()
    W, H = 595.32, 841.92
    LM, RM, TOP, BOT = 40, 40, 48, 40
    x0, x1 = 71, 534           # 原 PDF 方框左右邊界
    scale = (W - LM - RM) / (x1 - x0)
    pageno = 0

    def new_page():
        nonlocal pageno
        pg = out.new_page(width=W, height=H)
        pageno += 1
        pg.insert_font(fontname="cjk", fontfile=FONT)
        pg.insert_text((LM, 26), f"{title}　｜　吳邦一〈APCS Python 程式識讀 125 題〉", fontname="cjk", fontsize=8, color=(0.4, 0.4, 0.4))
        pg.insert_text((W - RM - 30, H - 18), f"- {pageno} -", fontname="cjk", fontsize=8, color=(0.4, 0.4, 0.4))
        return pg

    pg = new_page()
    # 封面資訊
    pg.insert_text((LM, 70), title, fontname="cjk", fontsize=18)
    pg.insert_text((LM, 92), subtitle, fontname="cjk", fontsize=10, color=(0.25, 0.25, 0.25))
    pg.insert_text((LM, 118), "班級：__________　座號：______　姓名：______________　得分：________", fontname="cjk", fontsize=11)
    y = 132
    if note:
        for i, line in enumerate(note):
            pg.insert_text((LM, y + 4 + i * 14), line, fontname="cjk", fontsize=9, color=(0.3, 0.3, 0.3))
        y += 8 + len(note) * 14

    if answer_sheet:
        # 作答欄：每格「題號 (   )」
        cols = 6
        cw = (W - LM - RM) / cols
        rows = (len(qs) + cols - 1) // cols
        pg.insert_text((LM, y + 14), "作答欄（把答案的英文字母寫在括號裡）", fontname="cjk", fontsize=10)
        y += 22
        for i, q in enumerate(qs):
            r, c = divmod(i, cols)
            pg.insert_text((LM + c * cw, y + 16 + r * 20), f"Q{q:03d}（　　）", fontname="cjk", fontsize=10)
        y += rows * 20 + 16
        pg.draw_line((LM, y), (W - RM, y), color=(0.6, 0.6, 0.6), width=0.6)
        y += 10

    for q in qs:
        parts = segs[q]
        hs = [(b - t) * scale for _, t, b in parts]
        total = sum(hs) + 6 * (len(parts) - 1)
        if y + total > H - BOT and y > TOP + 40:
            pg = new_page()
            y = TOP
        first = True
        for (pno, t, b), h in zip(parts, hs):
            if y + h > H - BOT:
                pg = new_page()
                y = TOP
            if first and tags and q in tags:
                tg = tags[q]
                col = {"易": (0.1, 0.5, 0.25), "中": (0.75, 0.45, 0.0), "難": (0.8, 0.1, 0.25)}[tg]
                pg.insert_text((LM + (302 - x0) * scale - 52, y + 13), f"難度：{tg}", fontname="cjk", fontsize=9, color=col)
            first = False
            clip = pymupdf.Rect(x0 - 1, t - 1, x1 + 1, b + 1)
            dest = pymupdf.Rect(LM, y, W - RM, y + h)
            pg.show_pdf_page(dest, src, pno, clip=clip)
            y += h - 0.5          # 跨頁的題目接在一起，看起來像同一個方框
        y += 8
    out.save(out_path, garbage=4, deflate=True)
    return pageno

if __name__ == "__main__":
    src = pymupdf.open(SRC)
    segs = question_segments(src, None)
    multi = {q: s for q, s in segs.items() if len(s) > 1}
    print(len(segs), "questions;", len(multi), "span two pages:", sorted(multi))
