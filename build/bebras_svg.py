# -*- coding: utf-8 -*-
"""單元7 Bebras 題目的逐步圖解（inline SVG，離線可用、隨主題變色）。"""

def _wrap(inner, vb, cls="diagram bebras-svg"):
    return f'<svg class="{cls}" viewBox="{vb}" xmlns="http://www.w3.org/2000/svg" role="img">{inner}</svg>'


def _queue_row(y, label, seq, moved_k, box=34, gap=6, x0=118):
    parts = [f'<text x="8" y="{y+box/2+5}" class="bq-label">{label}</text>']
    n = len(seq)
    for i, ch in enumerate(seq):
        x = x0 + i * (box + gap)
        hot = moved_k is not None and i >= n - moved_k
        cls = "bq-box hot" if hot else "bq-box"
        parts.append(f'<rect class="{cls}" x="{x}" y="{y}" width="{box}" height="{box}" rx="7"/>')
        parts.append(f'<text x="{x+box/2}" y="{y+box/2+6}" class="bq-num" text-anchor="middle">{ch}</text>')
    return "".join(parts)


def hike2_svg():
    rows = [("出發", "123456", None), ("① 3 階", "456321", 3),
            ("② 4 階", "213654", 4), ("③ 2 階", "365412", 2)]
    box, gap, x0, rowh, top = 34, 6, 118, 52, 30
    inner = ['<text x="8" y="16" class="bq-title">規則：一座 k 階的山 → 把最前面 k 隻「倒序」接到隊伍最後面</text>']
    for r, (label, seq, k) in enumerate(rows):
        y = top + r * rowh
        inner.append(_queue_row(y, label, seq, k, box, gap, x0))
        if r < len(rows) - 1:
            inner.append(f'<text x="{x0+3*(box+gap)-2}" y="{y+box+12}" class="bq-chev" text-anchor="middle">▼</text>')
    inner.append('<text x="118" y="{}" class="bq-note">最後在第三座山頂的順序 ＝ '.format(top + 4 * rowh - 6)
                 + '<tspan class="bq-ans">3 6 5 4 1 2</tspan></text>')
    return _wrap("".join(inner), vb=f"0 0 {x0 + 6*(box+gap) + 8} {top + 4*rowh + 6}")


def hike1_svg():
    box, gap, x0, y = 34, 6, 20, 40
    inner = ['<text x="8" y="18" class="bq-title">1 號第一個扶梯子，會被「倒序」排到隊尾 → 最後下山</text>']
    for i, ch in enumerate("123456"):
        x = x0 + i * (box + gap)
        cls = "bq-box hot" if ch == "1" else "bq-box"
        inner.append(f'<rect class="{cls}" x="{x}" y="{y}" width="{box}" height="{box}" rx="7"/>')
        inner.append(f'<text x="{x+box/2}" y="{y+box/2+6}" class="bq-num" text-anchor="middle">{ch}</text>')
    inner.append(f'<text x="{x0}" y="{y+box+22}" class="bq-note">最前面的 <tspan class="bq-ans">1 號</tspan> → 倒序後跑到最後 → 答案 <tspan class="bq-ans">1 號</tspan></text>')
    return _wrap("".join(inner), vb=f"0 0 366 {y+box+34}")


def banana_svg():
    box, gap, x0, y = 40, 10, 40, 44
    inner = ['<text x="8" y="18" class="bq-title">媽媽的五串香蕉：只有「3」是 3 的倍數</text>']
    for i, v in enumerate([1, 2, 3, 4, 5]):
        x = x0 + i * (box + gap)
        cls = "bq-box hot" if v == 3 else "bq-box"
        inner.append(f'<rect class="{cls}" x="{x}" y="{y}" width="{box}" height="{box}" rx="8"/>')
        inner.append(f'<text x="{x+box/2}" y="{y+box/2+7}" class="bq-num" text-anchor="middle">{v}</text>')
        if v == 3:
            inner.append(f'<text x="{x+box/2}" y="{y+box+16}" class="bq-ans" text-anchor="middle" style="font-size:11px">✓ 選這串</text>')
    ny = y + box + 40
    inner.append(f'<text x="8" y="{ny}" class="bq-note">小麥的總數是 3 的倍數；要分成三等份，加入的一串必須讓總數<tspan class="bq-ans"> 仍是 3 的倍數</tspan>。</text>')
    inner.append(f'<text x="8" y="{ny+18}" class="bq-note">加 1、2、4、5 都會破壞可被 3 整除，只有加「<tspan class="bq-ans">3</tspan>」可行 → 答案 <tspan class="bq-ans">D</tspan></text>')
    return _wrap("".join(inner), vb=f"0 0 {max(x0 + 5*(box+gap) + 8, 452)} {ny+30}")


def banana_problem_svg():
    # 示意圖：香蕉旁標上「該串數量」；上排小麥 8 串、下排媽媽 5 串、中間 3 個背包
    num = 'fill:var(--text);font-size:12px;font-weight:800;font-family:var(--mono);text-anchor:middle'
    parts = ['<text x="12" y="42" style="font-size:30px">🐵</text>']
    for i, n in enumerate([4, 5, 8, 3, 6, 8, 4, 4]):
        x = 66 + i * 40
        parts.append(f'<text x="{x}" y="36" style="font-size:20px" text-anchor="middle">🍌</text>')
        parts.append(f'<text x="{x}" y="54" style="{num}">{n}</text>')
    for x in [150, 196, 242]:
        parts.append(f'<text x="{x}" y="102" style="font-size:26px" text-anchor="middle">🎒</text>')
    parts.append('<text x="12" y="152" style="font-size:30px">🐵</text>')
    for i, n in enumerate([1, 2, 3, 4, 5]):
        x = 66 + i * 40
        parts.append(f'<text x="{x}" y="146" style="font-size:20px" text-anchor="middle">🍌</text>')
        parts.append(f'<text x="{x}" y="164" style="{num}">{n}</text>')
    return _wrap("".join(parts), vb="0 0 400 178")


def errand_svg():
    nodes = {"五金行": (58, 52), "公園": (182, 40), "藥房": (322, 52),
             "麵包店": (52, 132), "教堂": (186, 120), "學校": (318, 130),
             "市場": (72, 214), "家": (198, 214)}
    edges = [("五金行", "公園", 9), ("公園", "藥房", 7), ("五金行", "麵包店", 3),
             ("公園", "教堂", 6), ("藥房", "學校", 3), ("麵包店", "教堂", 4),
             ("教堂", "學校", 4), ("麵包店", "市場", 6), ("教堂", "家", 10),
             ("市場", "家", 4), ("學校", "家", 6)]
    hot = {frozenset(p) for p in [("家", "市場"), ("市場", "麵包店"), ("麵包店", "五金行"),
                                   ("麵包店", "教堂"), ("教堂", "學校"), ("學校", "藥房"), ("學校", "家")]}
    shops = {"五金行", "藥房", "市場"}
    inner = ['<text x="8" y="15" class="bq-title">小艾的任務：最短封閉路線 ＝ 步行 36 ＋ 採買 3 ＝ 39 分</text>']
    for a, b, w in edges:
        (x1, y1), (x2, y2) = nodes[a], nodes[b]
        cls = "eg-edge hot" if frozenset((a, b)) in hot else "eg-edge"
        inner.append(f'<line class="{cls}" x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}"/>')
        mx, my = (x1 + x2) / 2, (y1 + y2) / 2
        inner.append(f'<circle class="eg-wbg" cx="{mx}" cy="{my}" r="9"/>')
        inner.append(f'<text class="eg-w" x="{mx}" y="{my+4}" text-anchor="middle">{w}</text>')
    for name, (x, y) in nodes.items():
        w = len(name) * 15 + 14
        cls = "eg-node home" if name == "家" else ("eg-node shop" if name in shops else "eg-node")
        inner.append(f'<rect class="{cls}" x="{x-w/2}" y="{y-14}" width="{w}" height="28" rx="8"/>')
        pre = "🏠" if name == "家" else ("🛒" if name in shops else "")
        inner.append(f'<text class="eg-label" x="{x}" y="{y+5}" text-anchor="middle">{pre}{name}</text>')
    inner.append('<text x="8" y="248" class="bq-note">🛒 ＝ 要採買的三站；🏠 ＝ 出發／回家；粗綠線 ＝ 最短走法</text>')
    return _wrap("".join(inner), vb="0 0 384 258")


def tournament_svg():
    first = ["1", "8", "5", "4", "3", "6", "7", "2"]
    x0, dx, yb = 40, 62, 150
    y2, y3, y4 = 108, 66, 30
    inner = ['<text x="8" y="16" class="bq-title">賽程樹：出現次數 ＝ 1 ＋ 贏的場數</text>']
    xs = [x0 + i * dx for i in range(8)]
    for i, t in enumerate(first):
        x = xs[i]
        inner.append(f'<rect class="bq-box" x="{x-15}" y="{yb}" width="30" height="26" rx="6"/>')
        inner.append(f'<text x="{x}" y="{yb+18}" class="bq-num" text-anchor="middle">{t}</text>')

    def bracket(pairs, y_from, y_to, boxy):
        out, cxs = [], []
        for (a, b) in pairs:
            cx = (a + b) / 2
            cxs.append(cx)
            out.append(f'<path class="bq-line" d="M{a},{y_from} V{y_to} H{b} V{y_from}" fill="none"/>')
            out.append(f'<rect class="bq-slot" x="{cx-15}" y="{boxy}" width="30" height="24" rx="6"/>')
        return out, cxs
    l1, c1 = bracket([(xs[0], xs[1]), (xs[2], xs[3]), (xs[4], xs[5]), (xs[6], xs[7])], yb, y2 + 24, y2)
    inner += l1
    l2, c2 = bracket([(c1[0], c1[1]), (c1[2], c1[3])], y2, y3 + 22, y3)
    inner += l2
    l3, c3 = bracket([(c2[0], c2[1])], y3, y4 + 22, y4)
    inner += l3
    for cx, wtxt in zip(c1, ["1", "5", "6", "7"]):
        inner.append(f'<text x="{cx}" y="{y2+17}" class="bq-num" text-anchor="middle">{wtxt}</text>')
    for cx, wtxt in zip(c2, ["5", "6"]):
        inner.append(f'<text x="{cx}" y="{y3+16}" class="bq-num" text-anchor="middle">{wtxt}</text>')
    inner.append(f'<text x="{c3[0]}" y="{y4+16}" class="bq-num" text-anchor="middle">6</text>')
    inner.append(f'<text x="{c3[0]}" y="{y4-4}" text-anchor="middle" style="font-size:15px">🏆</text>')
    rx = xs[7] + 40
    inner.append(f'<text x="{rx}" y="46" class="bq-side">示範（6 號奪冠）：</text>')
    for j, s in enumerate(["出現次數 ＝ 1 ＋ 贏場數", "・6 號贏 3 場 → 4 次", "・5 號贏 2 場 → 3 次",
                            "・1、7 號各 2 次", "・其餘 4 隊各 1 次", "對照四人紀錄，", "只有 Beth 全對"]):
        inner.append(f'<text x="{rx}" y="{66 + j*20}" class="bq-side2">{s}</text>')
    return _wrap("".join(inner), vb=f"0 0 {rx + 150} 190")


def hike_trail_svg():
    parts = ['<line x1="6" y1="88" x2="414" y2="88" style="stroke:var(--text-faint);stroke-width:2.5;stroke-linecap:round"/>']
    parts.append('<text x="30" y="80" style="font-size:12px;font-weight:800;fill:var(--brand-strong)" text-anchor="middle">起點</text>')
    for i, h in enumerate(['A', 'B', 'C', 'D', 'E']):
        x = 92 + i * 55
        parts.append(f'<text x="{x}" y="78" style="font-size:26px" text-anchor="middle">🏠</text>')
        parts.append(f'<text x="{x}" y="104" style="font-size:13px;font-weight:800;fill:var(--text)" text-anchor="middle">{h}</text>')
    parts.append('<text x="384" y="78" style="font-size:23px" text-anchor="middle">🚌</text>')
    parts.append('<text x="384" y="104" style="font-size:12px;font-weight:800;fill:var(--brand-strong)" text-anchor="middle">終點</text>')
    parts.append('<text x="210" y="132" style="font-size:12.5px;font-weight:700;fill:var(--brand-strong)" text-anchor="middle">起點→B：2 種 × B→C：1 種 × C→終點：3 種 ＝ 6 種</text>')
    return _wrap(''.join(parts), vb='0 0 420 146')


_FARM =["玉玉玉玉蘋蘋葡葡", "玉玉玉玉蘋蘋葡葡", "玉玉玉玉葡葡橘葡", "玉玉玉玉葡葡橘橘",
         "玉玉玉玉玉葡橘橘", "橘橘玉玉蘋蘋橘橘", "橘橘橘橘橘橘葡葡", "橘橘橘橘橘橘蘋蘋"]
_TILING = [(0, 0, 4), (0, 4, 2), (0, 6, 2), (2, 4, 2), (2, 6, 1), (2, 7, 1), (3, 6, 2),
           (4, 0, 1), (4, 1, 1), (4, 2, 2), (4, 4, 1), (4, 5, 1), (5, 0, 2), (5, 4, 1),
           (5, 5, 1), (5, 6, 1), (5, 7, 1), (6, 2, 2), (6, 4, 2), (6, 6, 1), (6, 7, 1),
           (7, 0, 1), (7, 1, 1), (7, 6, 1), (7, 7, 1)]
_CROP_FILL = {"玉": "#7aa35a", "蘋": "#c25550", "葡": "#8467ad", "橘": "#d69236"}
_CROP_EMOJI = {"玉": "🌽", "蘋": "🍎", "葡": "🍇", "橘": "🍊"}


def sprinkler_svg():
    cell, x0, y0 = 30, 8, 30
    inner = ['<text x="8" y="16" class="bq-title">最省鋪法：合計 25 台</text>']
    for r in range(8):
        for c in range(8):
            crop = _FARM[r][c]
            x, y = x0 + c * cell, y0 + r * cell
            inner.append(f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" fill="{_CROP_FILL[crop]}" stroke="#0d1117" stroke-width="1"/>')
            inner.append(f'<text x="{x+cell/2}" y="{y+cell/2+6}" text-anchor="middle" style="font-size:15px">{_CROP_EMOJI[crop]}</text>')
    for (r, c, s) in _TILING:
        x, y = x0 + c * cell, y0 + r * cell
        inner.append(f'<rect class="sp-tile" x="{x+1.5}" y="{y+1.5}" width="{s*cell-3}" height="{s*cell-3}" rx="3"/>')
    ly = y0 + 8 * cell + 20
    lx = 8
    for name, n in [("🌽 玉米", "5"), ("🍎 蘋果", "5"), ("🍇 葡萄", "6"), ("🍊 橘子", "9")]:
        inner.append(f'<text x="{lx}" y="{ly}" class="bq-note">{name} {n} 台</text>')
        lx += 66
    inner.append(f'<text x="8" y="{ly+18}" class="bq-note">白框 ＝ 一台灑水器蓋的正方形；同框只含一種作物。合計 <tspan class="bq-ans">25 台</tspan></text>')
    return _wrap("".join(inner), vb=f"0 0 {max(x0 + 8*cell + 8, 350)} {ly+30}")
