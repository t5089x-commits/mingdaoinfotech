# -*- coding: utf-8 -*-
"""單元3 用的向量示意圖（inline SVG，離線可用、隨主題變色）。"""

def _wrap(inner, vb="0 0 300 120", cls="diagram"):
    return f'<svg class="{cls}" viewBox="{vb}" xmlns="http://www.w3.org/2000/svg" role="img">{inner}</svg>'

# ---------- 邏輯閘符號 ----------
def gate_svg(kind):
    body = {
        "AND": '<path d="M45,15 H80 A25,25 0 0 1 80,65 H45 Z"/>',
        "OR":  '<path d="M40,15 C62,15 88,24 106,40 C88,56 62,65 40,65 C52,50 52,30 40,15 Z"/>',
        "XOR": '<path d="M46,15 C58,15 84,24 102,40 C84,56 58,65 46,65 C58,50 58,30 46,15 Z"/>'
               '<path d="M35,15 C47,30 47,50 35,65" fill="none"/>',
        "NOT": '<path d="M46,15 L46,65 L92,40 Z"/><circle cx="99" cy="40" r="6"/>',
    }[kind]
    if kind == "NOT":
        ins = '<line x1="12" y1="40" x2="46" y2="40"/>'
        out = '<line x1="105" y1="40" x2="135" y2="40"/>'
        labelin = '<text x="8" y="35" class="pin">A</text>'
    else:
        xin = 8 if kind == "XOR" else 12
        x2 = 35 if kind == "XOR" else (40 if kind == "OR" else 45)
        ins = (f'<line x1="{xin}" y1="28" x2="{x2}" y2="28"/>'
               f'<line x1="{xin}" y1="52" x2="{x2}" y2="52"/>')
        out = '<line x1="106" y1="40" x2="135" y2="40"/>'
        labelin = '<text x="2" y="24" class="pin">A</text><text x="2" y="58" class="pin">B</text>'
    inner = f'<g class="body">{body}</g><g class="wire">{ins}{out}</g>{labelin}'
    inner += f'<text x="75" y="92" class="glabel">{kind}</text>'
    return _wrap(inner, vb="0 0 150 100", cls="diagram gate-svg")

# ---------- 音波（類比→取樣→數位）----------
def audio_wave():
    import math
    pts = []
    for x in range(0, 301, 3):
        t = x / 300.0
        y = 55 - 30 * math.sin(t * math.pi * 6) * math.exp(-((t-0.5)**2)*1.5) - 8*math.sin(t*math.pi*22)
        pts.append(f"{x},{y:.1f}")
    wave = '<polyline class="wave" points="' + " ".join(pts) + '" fill="none"/>'
    # 取樣垂直虛線
    bars = ""
    for x in range(15, 300, 22):
        bars += f'<line class="samp" x1="{x}" y1="55" x2="{x}" y2="90"/><circle class="dot" cx="{x}" cy="55" r="2.5"/>'
    axis = '<line class="axis" x1="0" y1="55" x2="300" y2="55"/>'
    labels = ('<text x="6" y="14" class="cap">聲音波形（連續的類比訊號）</text>'
              '<text x="6" y="30" class="cap2" style="font-size:9px">↕ 波的高低 ＝ 振幅（音量大小）</text>'
              '<text x="256" y="52" class="cap2" style="font-size:9px">時間 →</text>'
              '<text x="150" y="106" class="cap2" text-anchor="middle" style="font-size:8.5px">↑ 每隔固定時間取樣一次 ＝ 取樣頻率（例：每秒 44100 次 = 44.1 kHz）</text>'
              '<text x="150" y="120" class="cap2" text-anchor="middle" style="font-size:8.5px">每次用幾 bit 記錄振幅 ＝ 取樣位數（例：16 bit）→ 變成數位訊號</text>')
    return _wrap(axis + wave + bars + labels, vb="0 0 300 128", cls="diagram wave-svg")

# ---------- 類比 vs 數位 ----------
def analog_vs_digital():
    import math
    apts = []
    for x in range(0, 141, 2):
        t = x/140.0
        y = 45 - 26*math.sin(t*math.pi*3)
        apts.append(f"{x+5},{y:.1f}")
    analog = '<polyline class="wave" points="'+ " ".join(apts) +'" fill="none"/>'
    # 數位方波 / 階梯
    lv = [0,1,1,0,1,0,0,1]
    dp = []
    x = 5
    step = 17
    for i,b in enumerate(lv):
        y = 22 if b else 68
        dp.append(f"{x},{y}"); x+=step; dp.append(f"{x},{y}")
    digital = '<polyline class="wave dg" points="'+ " ".join(dp) +'" fill="none"/>'
    la = '<text x="78" y="98" class="cap2" text-anchor="middle">類比：連續、平滑的波</text>'
    ld = '<text x="78" y="98" class="cap2" text-anchor="middle">數位：一格一格（0 與 1）</text>'
    # 類比：0V 就是波上下擺動的中心線
    left_extra = ('<text x="2" y="43" class="cap2" style="font-size:9px">0V</text>'
                  '<text x="120" y="20" class="cap2" style="font-size:9px">+</text>'
                  '<text x="120" y="76" class="cap2" style="font-size:9px">−</text>')
    # 數位：高電位＝1、低電位＝0（0V）
    dig_ref = ('<line class="samp" x1="5" y1="22" x2="150" y2="22"/>'
               '<line class="samp" x1="5" y1="68" x2="150" y2="68"/>'
               '<text x="6" y="18" class="cap2" style="font-size:9px">1（高電位）</text>'
               '<text x="6" y="80" class="cap2" style="font-size:9px">0（低電位 = 0V）</text>')
    left = _wrap('<line class="axis" x1="0" y1="45" x2="150" y2="45"/>'+analog+left_extra+la, vb="0 0 150 105", cls="diagram")
    right = _wrap(dig_ref+digital+ld, vb="0 0 150 105", cls="diagram")
    return left, right

# ---------- 摩爾定律 vs 輝達定律（示意圖）----------
def moore_huang():
    axis = ('<line class="axis" x1="42" y1="150" x2="305" y2="150"/>'
            '<line class="axis" x1="42" y1="150" x2="42" y2="18"/>'
            '<text x="150" y="172" class="cap2" text-anchor="middle">年份 →</text>'
            '<text x="10" y="90" class="cap2" transform="rotate(-90 10 90)" text-anchor="middle">效能 →</text>')
    ticks = ''
    for yr, x in [(1970,42),(1990,120),(2010,210),(2025,285)]:
        ticks += f'<line class="samp" x1="{x}" y1="150" x2="{x}" y2="153"/><text x="{x}" y="164" class="cap2" text-anchor="middle" style="font-size:9px">{yr}</text>'
    moore = ('<polyline class="wave" points="42,148 120,138 180,120 225,96 262,66 295,40" fill="none"/>'
             '<text x="132" y="116" style="font-size:9px;fill:var(--brand)">摩爾定律（約每 2 年 ×2）</text>')
    huang = ('<polyline class="wave dg" points="205,148 240,120 262,84 282,50 298,24" fill="none"/>'
             '<text x="150" y="38" style="font-size:9px;fill:var(--accent)">輝達定律（GPU AI 效能約每年 ×2）</text>')
    note = '<text x="150" y="182" class="cap2" text-anchor="middle" style="font-size:8px">※ 示意圖：實際為對數成長，此處僅比較兩者的成長速度</text>'
    return _wrap(axis + ticks + moore + huang + note, vb="0 0 320 188", cls="diagram")


# ---------- 使用者介面的演進：DOS → GUI → 自然語言 → 腦機 ----------
def ui_evolution():
    stages = [
        ("1980s", "文字命令列", "DOS", "⌨️", "打指令、背指令操作"),
        ("1990s", "圖形介面", "GUI", "🖱️", "視窗圖示、滑鼠點選"),
        ("2020s", "自然語言", "AI", "💬", "用說的跟 AI 對話"),
        ("未來", "腦機介面", "BCI", "🧠", "用腦波操控（發展中）"),
    ]
    cardw, gap, x0, y0, h = 128, 22, 8, 26, 96
    parts = []
    for i, (era, name, tag, icon, desc) in enumerate(stages):
        x = x0 + i * (cardw + gap)
        cx = x + cardw / 2
        parts.append(f'<rect class="ui-card" x="{x}" y="{y0}" width="{cardw}" height="{h}" rx="10"/>')
        parts.append(f'<text x="{cx}" y="{y0+26}" text-anchor="middle" style="font-size:20px">{icon}</text>')
        parts.append(f'<text x="{cx}" y="{y0+50}" text-anchor="middle" class="ui-name">{name}</text>')
        parts.append(f'<text x="{cx}" y="{y0+66}" text-anchor="middle" class="ui-tag">{tag}・{era}</text>')
        parts.append(f'<text x="{cx}" y="{y0+84}" text-anchor="middle" class="ui-desc">{desc}</text>')
        if i < len(stages) - 1:
            ax = x + cardw + 3
            parts.append(f'<line class="flow" x1="{ax}" y1="{y0+h/2}" x2="{ax+gap-6}" y2="{y0+h/2}" marker-end="url(#uiar)"/>')
    head = ('<text x="8" y="16" class="ui-title">越來越貼近「人習慣的方式」——從背指令 → 用點的 → 用說的 → 用想的</text>')
    defs = ('<defs><marker id="uiar" markerWidth="9" markerHeight="9" refX="7" refY="3" orient="auto">'
            '<path d="M0,0 L8,3 L0,6 Z" class="arh"/></marker></defs>')
    total_w = x0 + 4 * cardw + 3 * gap + x0
    return _wrap(defs + head + "".join(parts), vb=f"0 0 {total_w} 132", cls="diagram ui-evo")


# ---------- 開關 → 邏輯閘：串聯＝AND、並聯＝OR ----------
def switch_logic(kind, interactive=True):
    # 可點擊：預設 A=0,B=0（開關斷開、燈滅）；每點一下循環 00→01→10→11→00
    wire   = 'stroke:var(--text-faint);stroke-width:2.4;fill:none;stroke-linecap:round'
    leverC = 'stroke:var(--text);stroke-width:3.2;fill:none;stroke-linecap:round'
    leverO = 'stroke:var(--text-faint);stroke-width:2.6;fill:none;stroke-linecap:round'
    cond   = 'stroke:var(--brand);stroke-width:3.6;fill:none;stroke-linecap:round;stroke-linejoin:round'
    hinge  = 'fill:var(--text)'
    hole   = 'fill:var(--bg-elev);stroke:var(--text-faint);stroke-width:1.6'
    pw     = 'fill:var(--text-faint)'
    bBase  = 'stroke:var(--text-faint);stroke-width:2.2;fill:none'
    bLit   = 'stroke:var(--brand);stroke-width:2.6;fill:var(--brand);fill-opacity:.28'
    lab    = 'fill:var(--text);font-size:12px;font-weight:700;font-family:inherit;text-anchor:middle'

    def sw(x, y, which, lift):
        # 兩種狀態都畫好，用 CSS 依 A/B 決定顯示哪一個
        return (f'<circle cx="{x}" cy="{y}" r="3" style="{hinge}"/>'
                f'<circle cx="{x+20}" cy="{y}" r="3" style="{hole}"/>'
                f'<g class="sw {which}">'
                f'<line class="lo" x1="{x}" y1="{y}" x2="{x+16}" y2="{y+lift}" style="{leverO}"/>'
                f'<line class="lc" x1="{x}" y1="{y}" x2="{x+20}" y2="{y}" style="{leverC}"/>'
                f'</g>')

    if kind == "series":
        base = (f'<circle cx="8" cy="34" r="3.4" style="{pw}"/>'
                f'<line x1="8" y1="34" x2="40" y2="34" style="{wire}"/>'
                f'<line x1="60" y1="34" x2="82" y2="34" style="{wire}"/>'
                f'<line x1="102" y1="34" x2="122" y2="34" style="{wire}"/>'
                f'<circle cx="136" cy="34" r="12" style="{bBase}"/>'
                f'<line x1="131" y1="30" x2="141" y2="38" style="{bBase}"/><line x1="141" y1="30" x2="131" y2="38" style="{bBase}"/>')
        sws = sw(40, 34, 'a', -12) + sw(82, 34, 'b', -12)
        condm = (f'<line class="cond cond-main" x1="8" y1="34" x2="122" y2="34" style="{cond}"/>')
        bulbLit = (f'<g class="bulb-lit"><circle cx="136" cy="34" r="12" style="{bLit}"/>'
                   f'<line x1="131" y1="30" x2="141" y2="38" style="stroke:var(--brand);stroke-width:2.6"/>'
                   f'<line x1="141" y1="30" x2="131" y2="38" style="stroke:var(--brand);stroke-width:2.6"/></g>')
        labels = f'<text x="50" y="18" style="{lab}">A</text><text x="92" y="18" style="{lab}">B</text>'
        svg = _wrap(base + sws + condm + bulbLit + labels, vb="0 0 160 62", cls="diagram swint-svg")
        state0 = 'A=<b class="va">0</b>、B=<b class="vb">0</b> → 燈 <b class="vo">滅（0）</b>'
    else:
        base = (f'<circle cx="10" cy="40" r="3.4" style="{pw}"/>'
                f'<line x1="10" y1="40" x2="34" y2="40" style="{wire}"/>'
                f'<line x1="34" y1="18" x2="34" y2="62" style="{wire}"/>'
                f'<line x1="34" y1="18" x2="46" y2="18" style="{wire}"/><line x1="66" y1="18" x2="96" y2="18" style="{wire}"/>'
                f'<line x1="34" y1="62" x2="46" y2="62" style="{wire}"/><line x1="66" y1="62" x2="96" y2="62" style="{wire}"/>'
                f'<line x1="96" y1="18" x2="96" y2="62" style="{wire}"/>'
                f'<line x1="96" y1="40" x2="118" y2="40" style="{wire}"/>'
                f'<circle cx="132" cy="40" r="12" style="{bBase}"/>'
                f'<line x1="127" y1="36" x2="137" y2="44" style="{bBase}"/><line x1="137" y1="36" x2="127" y2="44" style="{bBase}"/>')
        sws = sw(46, 18, 'a', 12) + sw(46, 62, 'b', -12)
        conds = (f'<path class="cond cond-a" d="M34,40 L34,18 L96,18 L96,40" style="{cond}"/>'
                 f'<path class="cond cond-b" d="M34,40 L34,62 L96,62 L96,40" style="{cond}"/>'
                 f'<path class="cond cond-out" d="M10,40 L34,40 M96,40 L118,40" style="{cond}"/>')
        bulbLit = (f'<g class="bulb-lit"><circle cx="132" cy="40" r="12" style="{bLit}"/>'
                   f'<line x1="127" y1="36" x2="137" y2="44" style="stroke:var(--brand);stroke-width:2.6"/>'
                   f'<line x1="137" y1="36" x2="127" y2="44" style="stroke:var(--brand);stroke-width:2.6"/></g>')
        labels = f'<text x="56" y="12" style="{lab}">A</text><text x="56" y="90" style="{lab}">B</text>'
        svg = _wrap(base + sws + conds + bulbLit + labels, vb="0 0 160 100", cls="diagram swint-svg")
        state0 = 'A=<b class="va">0</b>、B=<b class="vb">0</b> → 燈 <b class="vo">滅（0）</b>'

    if not interactive:
        return svg
    return (f'<div class="swint" data-kind="{kind}" data-a="0" data-b="0" tabindex="0" role="button" '
            f'aria-label="點一下切換 A、B 的輸入，看燈會不會亮" onclick="swCycle(this)" '
            f'onkeydown="if(event.key===\' \'||event.key===\'Enter\'){{event.preventDefault();swCycle(this);}}">'
            f'{svg}'
            f'<div class="swint-state">{state0}</div>'
            f'<div class="swint-hint">👆 點一下，換下一組輸入</div></div>')


# ---------- 傳輸方向：單工 / 半雙工 / 全雙工 ----------
def transmission(kind):
    A = '<rect class="dev" x="8" y="30" width="52" height="40" rx="7"/><text x="34" y="55" class="devt" text-anchor="middle">A</text>'
    B = '<rect class="dev" x="180" y="30" width="52" height="40" rx="7"/><text x="206" y="55" class="devt" text-anchor="middle">B</text>'
    defs = ('<defs><marker id="ar" markerWidth="9" markerHeight="9" refX="7" refY="3" orient="auto">'
            '<path d="M0,0 L8,3 L0,6 Z" class="arh"/></marker></defs>')
    if kind == "simplex":
        arr = '<line class="flow" x1="66" y1="50" x2="174" y2="50" marker-end="url(#ar)"/>'
        cap = '<text x="120" y="92" class="cap2" text-anchor="middle">單工：只能 A → B 單向</text>'
        _svg = _wrap(defs + A + B + arr + cap, vb="0 0 240 105", cls="diagram trans-svg")
        return ('<div class="flow-demo" onclick="toggleFlow(this)" title="點一下看資料流動">' + _svg + '<span class="hd-hint">👆 點圖看資料流動</span></div>')
    elif kind == "half":
        arr = ('<line class="flow hd-ab" x1="66" y1="40" x2="174" y2="40" marker-end="url(#ar)"/>'
               '<line class="flow dim hd-ba" x1="174" y1="62" x2="66" y2="62" marker-end="url(#ar)"/>')
        cap = '<text x="120" y="92" class="cap2 hd-cap" text-anchor="middle">半雙工：現在 A → B 傳送中</text>'
        _svg = _wrap(defs + A + B + arr + cap, vb="0 0 240 105", cls="diagram trans-svg")
        return ('<div class="hd-wrap" onclick="toggleDuplex(this)" title="點一下切換傳送方向">' + _svg + '<span class="hd-hint">👆 點圖切換方向（半雙工：一次只能一個方向）</span></div>')
    else:
        arr = ('<line class="flow" x1="66" y1="40" x2="174" y2="40" marker-end="url(#ar)"/>'
               '<line class="flow" x1="174" y1="62" x2="66" y2="62" marker-end="url(#ar)"/>')
        cap = '<text x="120" y="92" class="cap2" text-anchor="middle">全雙工：同一時間可雙向傳輸</text>'
        _svg = _wrap(defs + A + B + arr + cap, vb="0 0 240 105", cls="diagram trans-svg")
        return ('<div class="flow-demo" onclick="toggleFlow(this)" title="點一下看資料流動">' + _svg + '<span class="hd-hint">👆 點圖看資料流動（雙向同時）</span></div>')
