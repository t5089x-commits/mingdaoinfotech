# -*- coding: utf-8 -*-
"""這個課程網站用到的向量示意圖（inline SVG，離線可用、隨深淺色主題變色）。
   沿用「資訊科技」課程網站 diagrams.py 的視覺語言（.dev/.devt 方框、.flow/.arh 箭頭）。"""


def _wrap(inner, vb="0 0 300 120", cls="diagram"):
    return f'<svg class="{cls}" viewBox="{vb}" xmlns="http://www.w3.org/2000/svg" role="img">{inner}</svg>'


def _arrow_defs(id_="ar"):
    return (f'<defs><marker id="{id_}" markerWidth="9" markerHeight="9" refX="7" refY="3" orient="auto">'
            f'<path d="M0,0 L8,3 L0,6 Z" class="arh"/></marker></defs>')


def _badge(cx, cy, num, title):
    """紅色警示徽章：圓圈 + 編號，滑鼠移上去可看到說明（title tooltip）。"""
    return (f'<g style="cursor:default"><title>{title}</title>'
            f'<circle cx="{cx}" cy="{cy}" r="12" style="fill:var(--danger)" />'
            f'<text x="{cx}" y="{cy+4}" text-anchor="middle" style="fill:#fff;font-size:12px;font-weight:800">{num}</text>'
            f'</g>')


# ---------- 單元 1：網路書店下訂單流程圖（標出可能被攻擊的位置） ----------
def bookstore_flow():
    nodes = [
        (10, "🧑", "Jay", "瀏覽並送出訂單"),
        (152, "🌐", "網路書店", "Web Server"),
        (294, "🏦", "金流／銀行", "確認付款"),
        (436, "📦", "書籍倉儲", "出貨"),
        (578, "📬", "Jay", "收到書籍（2-3 天後）"),
    ]
    w, h, y = 110, 62, 46
    cy = y + h / 2
    parts = [_arrow_defs("bkar")]
    for x, icon, title, sub in nodes:
        cx = x + w / 2
        parts.append(f'<rect class="dev" x="{x}" y="{y}" width="{w}" height="{h}" rx="9"/>')
        parts.append(f'<text x="{cx}" y="{y+22}" text-anchor="middle" style="font-size:18px">{icon}</text>')
        parts.append(f'<text x="{cx}" y="{y+38}" text-anchor="middle" class="devt" style="font-size:13px">{title}</text>')
        parts.append(f'<text x="{cx}" y="{y+52}" text-anchor="middle" class="cap2" style="font-size:9.5px">{sub}</text>')
    # 箭頭（相鄰節點間）
    gaps = []
    for i in range(len(nodes) - 1):
        x1 = nodes[i][0] + w
        x2 = nodes[i + 1][0]
        parts.append(f'<line class="flow" x1="{x1}" y1="{cy}" x2="{x2-2}" y2="{cy}" marker-end="url(#bkar)"/>')
        gaps.append((x1 + x2) / 2)
    # 警示徽章：①Jay↔書店連線　②書店伺服器本身　③書店↔銀行金流　④書店↔倉儲資料
    parts.append(_badge(gaps[0], cy - 26, "①", "① 連線可能被竊聽、竄改、偽造"))
    parts.append(_badge(nodes[1][0] + w - 6, y - 6, "②", "② 伺服器本身可能被入侵、植入病毒、DoS 攻擊"))
    parts.append(_badge(gaps[1], cy - 26, "③", "③ 金流往來可能被盜用"))
    parts.append(_badge(gaps[2], cy - 26, "④", "④ 轉交倉儲的訂單資料可能被竄改、偽造"))
    parts.append(f'<text x="344" y="16" text-anchor="middle" class="cap" style="font-size:11px">🔴 紅色徽章＝可能被攻擊的位置</text>')
    return _wrap("".join(parts), vb="0 0 688 128", cls="diagram")


# ---------- 單元 4：區塊鏈基本結構示意圖 ----------
def blockchain_basic():
    blocks = [
        ("創世區塊 #0", "前一區塊雜湊：－", "資料：（初始化）"),
        ("區塊 #1", "前一區塊雜湊：0x4a7f…", "資料：交易 A、B…"),
        ("區塊 #2", "前一區塊雜湊：0x9c21…", "資料：交易 C、D…"),
    ]
    w, h, y = 178, 108, 14
    gap = 46
    parts = [_arrow_defs("bcar")]
    for i, (title, prev, data) in enumerate(blocks):
        x = 10 + i * (w + gap)
        parts.append(f'<rect class="dev" x="{x}" y="{y}" width="{w}" height="{h}" rx="9"/>')
        parts.append(f'<text x="{x+w/2}" y="{y+24}" text-anchor="middle" class="devt" style="font-size:13.5px">{title}</text>')
        parts.append(f'<line class="samp" x1="{x+12}" y1="{y+34}" x2="{x+w-12}" y2="{y+34}"/>')
        parts.append(f'<text x="{x+12}" y="{y+54}" class="cap2" style="font-size:9.5px">{prev}</text>')
        parts.append(f'<text x="{x+12}" y="{y+72}" class="cap2" style="font-size:9.5px">{data}</text>')
        parts.append(f'<text x="{x+12}" y="{y+94}" class="cap2" style="font-size:9.5px;fill:var(--brand)">本區塊雜湊：{"0x4a7f…" if i==0 else ("0x9c21…" if i==1 else "0xe83b…")}</text>')
        if i < len(blocks) - 1:
            ax1 = x + w
            ax2 = ax1 + gap
            parts.append(f'<line class="flow" x1="{ax1}" y1="{y+h/2}" x2="{ax2-2}" y2="{y+h/2}" marker-end="url(#bcar)"/>')
            parts.append(f'<text x="{(ax1+ax2)/2}" y="{y+h/2-8}" text-anchor="middle" class="cap2" style="font-size:8.5px">帶著前一區塊的雜湊值</text>')
    total_w = 10 + len(blocks) * w + (len(blocks) - 1) * gap + 10
    return _wrap("".join(parts), vb=f"0 0 {total_w} 136", cls="diagram")


# ---------- 單元 4：Merkle Tree 空白樹狀圖（上課動手填，三層：葉節點→兩兩配對→root） ----------
def merkle_tree_blank():
    leaves = [("A", 8), ("B", 116), ("C", 224), ("D", 332)]
    lw, lh, ly = 80, 62, 178
    mw, mh, my = 96, 54, 96
    rw, rh, ry = 118, 54, 16

    parts = []
    leaf_cx = []
    for label, x in leaves:
        cx = x + lw / 2
        leaf_cx.append(cx)
        parts.append(f'<rect class="dev" x="{x}" y="{ly}" width="{lw}" height="{lh}" rx="8"/>')
        parts.append(f'<text x="{cx}" y="{ly+19}" text-anchor="middle" class="devt" style="font-size:12.5px">資料 {label}</text>')
        parts.append(f'<rect x="{x+9}" y="{ly+27}" width="{lw-18}" height="{lh-36}" rx="4" class="samp" fill="none"/>')
        parts.append(f'<text x="{cx}" y="{ly+lh-13}" text-anchor="middle" class="cap2" style="font-size:8.3px">Hash({label}) 待填</text>')

    pairs = [(0, 1, "H(A,B)"), (2, 3, "H(C,D)")]
    mid_cx = []
    for a, b, label in pairs:
        cx = (leaf_cx[a] + leaf_cx[b]) / 2
        x = cx - mw / 2
        mid_cx.append(cx)
        parts.append(f'<line class="flow" x1="{leaf_cx[a]}" y1="{ly}" x2="{cx-16}" y2="{my+mh}"/>')
        parts.append(f'<line class="flow" x1="{leaf_cx[b]}" y1="{ly}" x2="{cx+16}" y2="{my+mh}"/>')
        parts.append(f'<rect class="dev" x="{x}" y="{my}" width="{mw}" height="{mh}" rx="8"/>')
        parts.append(f'<text x="{cx}" y="{my+18}" text-anchor="middle" class="devt" style="font-size:12.5px">{label}</text>')
        parts.append(f'<rect x="{x+9}" y="{my+25}" width="{mw-18}" height="{mh-34}" rx="4" class="samp" fill="none"/>')
        parts.append(f'<text x="{cx}" y="{my+mh-12}" text-anchor="middle" class="cap2" style="font-size:8.3px">待填</text>')

    root_cx = (mid_cx[0] + mid_cx[1]) / 2
    root_x = root_cx - rw / 2
    parts.append(f'<line class="flow" x1="{mid_cx[0]}" y1="{my}" x2="{root_cx-18}" y2="{ry+rh}"/>')
    parts.append(f'<line class="flow" x1="{mid_cx[1]}" y1="{my}" x2="{root_cx+18}" y2="{ry+rh}"/>')
    parts.append(f'<rect class="dev" x="{root_x}" y="{ry}" width="{rw}" height="{rh}" rx="8" style="stroke:var(--brand);stroke-width:2.4"/>')
    parts.append(f'<text x="{root_cx}" y="{ry+19}" text-anchor="middle" class="devt" style="font-size:12.5px">Merkle Root</text>')
    parts.append(f'<rect x="{root_x+9}" y="{ry+26}" width="{rw-18}" height="{rh-35}" rx="4" class="samp" fill="none"/>')
    parts.append(f'<text x="{root_cx}" y="{ry+rh-12}" text-anchor="middle" class="cap2" style="font-size:8.3px">待填</text>')

    total_w = max(leaves[-1][1] + lw, root_x + rw) + 8
    return _wrap("".join(parts), vb=f"0 0 {total_w} 250", cls="diagram")


# ---------- 單元 5：挖礦與獎勵流程示意圖 ----------
def mining_reward_flow():
    nodes = [
        (10, "📥", "蒐集交易", "打包成候選區塊"),
        (162, "🧮", "競猜 Nonce", "反覆試算，找出符合難度的雜湊"),
        (314, "📢", "廣播新區塊", "全網其他節點驗證後接受"),
        (466, "🎁", "獲得獎勵", "新發行比特幣＋區塊內所有手續費"),
    ]
    w, h, y = 138, 66, 44
    cy = y + h / 2
    parts = [_arrow_defs("mnar")]
    for x, icon, title, sub in nodes:
        cx = x + w / 2
        parts.append(f'<rect class="dev" x="{x}" y="{y}" width="{w}" height="{h}" rx="9"/>')
        parts.append(f'<text x="{cx}" y="{y+22}" text-anchor="middle" style="font-size:19px">{icon}</text>')
        parts.append(f'<text x="{cx}" y="{y+39}" text-anchor="middle" class="devt" style="font-size:13px">{title}</text>')
        parts.append(f'<text x="{cx}" y="{y+54}" text-anchor="middle" class="cap2" style="font-size:8.8px">{sub}</text>')
    for i in range(len(nodes) - 1):
        x1 = nodes[i][0] + w
        x2 = nodes[i + 1][0]
        parts.append(f'<line class="flow" x1="{x1}" y1="{cy}" x2="{x2-2}" y2="{cy}" marker-end="url(#mnar)"/>')
    parts.append(f'<text x="{(10+466+138)/2}" y="16" text-anchor="middle" class="cap" style="font-size:11px">⛏️ 誰先解出 Nonce，誰就記帳並拿走這個區塊的獎勵</text>')
    total_w = 466 + 138 + 10
    return _wrap("".join(parts), vb=f"0 0 {total_w} 126", cls="diagram")
