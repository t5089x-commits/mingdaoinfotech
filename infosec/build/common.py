# -*- coding: utf-8 -*-
"""共用骨架：頁面 wrapper、單元中繼資料、首頁產生器、內容小工具。
   （改編自「資訊科技」課程網站的產生器架構，套用到「資訊安全導論」課程。）"""
import html as _html

COURSE = "資訊安全導論"
TEACHER = "陳楷翔 老師"
CONTACT = "t5089x@ms.mingdao.edu.tw"

# (檔名, 標題, 副標, 分類代碼, 卡片描述, 標籤list)
# 分類代碼對應下面 PARTS 的 key，用來分組＋算「單元 x／y」
UNITS = [
    ("unit01", "課程介紹＋2050 未來情境", "課程地圖預告、評量說明；從 2050 回推資訊安全", "map",
     "認識整學期的學習地圖、評量方式，並用「2050 年的一天」描繪未來資訊科技情境，帶出資安主題。",
     ["課程地圖", "評量方式", "2050情境"]),
    ("unit02", "Web1.0 → 3.0 演進", "把「未來資訊科技」拆成資安主題，建立全學期主軸", "map",
     "從唯讀的 Web1.0、互動共享的 Web2.0，到強調自主與去中心化的 Web3.0，建立本學期主軸。",
     ["Web演進", "去中心化", "主軸地圖"]),
    ("unit03", "數位身分與數位錢包", "數位身分、去中心化帳號；生活案例", "map",
     "從帳號密碼到去中心化身分（DID），認識數位身分與數位錢包的生活案例。",
     ["數位身分", "數位錢包", "DID"]),
    ("unit04", "區塊鏈是什麼", "區塊、鏈結、不可竄改 —— 比特幣、交易所、Web3.0 背後的共同技術", "map",
     "認識區塊鏈技術目前實際應用在哪些地方，再拆解區塊、鏈結、雜湊如何組成「不可竄改」的帳本，以及 Merkle Tree 的驗證概念。",
     ["區塊", "鏈結", "不可竄改"]),
    ("unit05", "虛擬貨幣與比特幣", "Bitcoin、錢包、公私鑰直覺", "map",
     "比特幣的誕生故事、專有名詞、挖礦與工作證明機制，建立公私鑰的直覺。",
     ["Bitcoin", "錢包", "公私鑰"]),
    ("unit06", "Ethereum 與智能合約", "DApp、智能合約", "map",
     "從「帳本」進化到「可執行程式」，認識以太坊、智能合約與 DApp 的概念。",
     ["Ethereum", "智能合約", "DApp"]),
    ("unit07", "定期評量", "定期評量", "core",
     "第一階段（未來情境／數位信任地圖）學習內容的定期評量。",
     ["評量"]),
    ("unit08", "專題啟動（PBL）", "題目發想、分組、定位為學習歷程成果", "core",
     "專題式學習啟動：三種路線（技術實作／議題研究／未來機制發想）任選，題目發想、分組。",
     ["PBL", "三種路線", "學習歷程"]),
    ("unit09", "Hash 與資料完整性", "數位指紋、不可竄改（專題並行：資料蒐集）", "core",
     "雜湊函數的單向特性、SHA-256 實作體驗、Merkle Tree 如何驗證巨型檔案完整性。",
     ["雜湊函數", "SHA-256", "資料完整性"]),
    ("unit10", "古典密碼學（傳統密碼）", "凱薩、維吉尼亞、破解實作（專題並行）", "core",
     "換位法、替代法、凱薩加密、單字母／多字母加密到轉輪機 Enigma，體驗密碼與破密的攻防。",
     ["凱薩加密", "維吉尼亞", "Enigma"]),
    ("unit11", "公開金鑰密碼學（非對稱）", "公私鑰加解密、回扣比特幣（專題並行）", "core",
     "非對稱加密的公私鑰概念、RSA 的數學原理與實例演算，回扣比特幣的地址／私鑰。",
     ["RSA", "公私鑰", "非對稱加密"]),
    ("unit12", "電子簽章與數位憑證", "CA、HTTPS、信任鏈（專題並行）", "core",
     "數位簽章如何證明「你是你」、憑證中心（CA）與信任鏈，以及 HTTPS 連線的四個步驟。",
     ["數位簽章", "CA憑證", "HTTPS"]),
    ("unit13", "成果製作（一）", "架構設計與內容產出；分組指導", "make",
     "專題成果的架構設計與內容產出，分組實作與老師巡迴指導。",
     ["架構設計", "分組指導"]),
    ("unit14", "成果製作（二）", "架構設計與內容產出；分組指導", "make",
     "延續上一堂的架構與內容產出，持續完善專題素材與呈現方式。",
     ["內容產出", "分組指導"]),
    ("unit15", "成果製作（三）＋發表", "簡報完成、口頭發表；多元評量", "make",
     "完成簡報、進行口頭發表，並以多元評量方式互評與總結。",
     ["簡報", "口頭發表", "多元評量"]),
    ("unit16", "AI 與資訊安全", "Deepfake、AI 詐騙", "future",
     "生成式 AI 帶來的深偽（Deepfake）與 AI 詐騙手法，以及可以怎麼辨識與防範。",
     ["Deepfake", "AI詐騙", "辨識技巧"]),
    ("unit17", "Web3 資安風險", "釣魚錢包、Rug Pull、165 在地案例", "future",
     "釣魚錢包、Rug Pull 等 Web3 特有的詐騙手法，搭配 165 反詐騙的在地案例。",
     ["釣魚錢包", "RugPull", "165反詐騙"]),
    ("unit18", "零信任與未來資安", "Passkey、生物辨識、無密碼登入", "future",
     "從「猜密碼」走向零信任架構：Passkey、生物辨識與無密碼登入的設計思維。",
     ["零信任", "Passkey", "生物辨識"]),
    ("unit19", "未來數位社會", "CBDC、數位皮夾、數位身分治理；回到 2050 收束", "future",
     "央行數位貨幣（CBDC）、數位皮夾與數位身分治理，回到 2050 情境收束全學期。",
     ["CBDC", "數位皮夾", "身分治理"]),
    ("unit20", "課程總整理＋期末複習", "從未來回看密碼學如何撐起數位信任", "future",
     "從 2050 的未來回看：這學期學過的密碼學與資安機制，如何一路撐起數位信任。",
     ["總複習", "數位信任", "學期回顧"]),
]

IDX = {u[0]: i for i, u in enumerate(UNITS)}

PARTS = [
    ("map", "Part 1 · 2050 未來與數位信任地圖", "單元 1–6"),
    ("core", "Part 2 · 密碼學與信任技術（專題並行）", "單元 7–12"),
    ("make", "Part 3 · 專題成果製作與發表", "單元 13–15"),
    ("future", "Part 4 · 未來資安與數位社會", "單元 16–20"),
]


def esc(s):
    return _html.escape(s, quote=False)


# ---------------------------------------------------------------
# 內容小工具
# ---------------------------------------------------------------

def goals(items):
    lis = "\n".join(f"<li>{it}</li>" for it in items)
    return f'''<div class="goals">
  <h2>🎯 學習目標</h2>
  <ul>
{lis}
  </ul>
</div>'''


def callout(title, body_html, kind=""):
    cls = "callout" + (" " + kind if kind else "")
    return f'<div class="{cls}"><span class="t">{title}</span>\n{body_html}\n</div>'


def grid(cols, tiles_html):
    inner = "\n  ".join(tiles_html)
    return f'<div class="grid cols-{cols}">\n  {inner}\n</div>'


def tile(a, b, c=None):
    """兩種呼叫方式都支援：
       tile(icon, title, body) —— icon 是單一符號
       tile("icon 標題", body) —— icon 與標題寫在同一個字串裡"""
    if c is None:
        return f'<div class="tile"><h4>{a}</h4><p>{b}</p></div>'
    return f'<div class="tile"><h4><span class="ico">{a}</span>{b}</h4><p>{c}</p></div>'


def card(title_html, body_html):
    return f'<div class="card"><h3>{title_html}</h3>{body_html}</div>'


def table_wrap(headers, rows, css="center"):
    ths = "".join(f"<th>{h}</th>" for h in headers)
    trs = ""
    for r in rows:
        tds = "".join(f"<td>{c}</td>" for c in r)
        trs += f"<tr>{tds}</tr>"
    return f'''<div class="table-wrap">
<table class="{css}">
  <thead><tr>{ths}</tr></thead>
  <tbody>{trs}</tbody>
</table>
</div>'''


def video_block(youtube_id=None, url=None, title="", caption="", placeholder_note=""):
    """影片區塊：給 youtube_id 就顯示可點縮圖；給 url 就放連結按鈕；都沒給則顯示占位框。"""
    if youtube_id:
        watch = "https://www.youtube.com/watch?v=" + youtube_id
        thumb = "https://img.youtube.com/vi/" + youtube_id + "/hqdefault.jpg"
        inner = (f'<a class="video-facade" href="{watch}" target="_blank" rel="noopener" title="{esc(title)}">'
                 f'<img class="video-thumb" src="{thumb}" alt="{esc(title)}" loading="lazy" onerror="this.style.display=&apos;none&apos;">'
                 f'<span class="video-play">&#9654;</span></a>'
                 f'<a class="video-title-link" href="{watch}" target="_blank" rel="noopener">&#9654; {esc(title)} <span class="vt-ext">在 YouTube 觀看 &#8599;</span></a>')
    elif url:
        inner = (f'<div class="video-placeholder"><span class="vp-ico">🎬</span>'
                 f'<span class="vp-t">{esc(title)}</span>'
                 f'<a class="video-link-btn" href="{esc(url)}" target="_blank" rel="noopener">▶ 開啟連結 ↗</a></div>')
    else:
        note = placeholder_note or "把連結給我，我就幫你嵌進來。"
        inner = (f'<div class="video-placeholder"><span class="vp-ico">🎬</span>'
                 f'<span class="vp-t">{esc(title or "資源區（待放入）")}</span>'
                 f'<span style="font-size:.85rem">{esc(note)}</span></div>')
    cap = f'<figcaption>{caption}</figcaption>' if caption else ''
    return f'<figure class="video-embed">{inner}{cap}</figure>'


def resource_link(icon, title, url, desc=""):
    """給非影片的外部連結（線上工具、PDF…）用的小卡片，避免套用 16:9 的影片占位框太佔版面。"""
    d = f'<p>{desc}</p>' if desc else ''
    return (f'<div class="tile"><h4><span class="ico">{icon}</span>{esc(title)}</h4>{d}'
            f'<a class="video-link-btn" href="{esc(url)}" target="_blank" rel="noopener">▶ 開啟連結 ↗</a></div>')


def code_block(code, lang="text", label=None, copy=True):
    if label is None:
        label = {"python": "python", "text": "範例", "output": "輸出"}.get(lang, lang)
    code = code.strip("\n")
    safe = _html.escape(code, quote=False)
    btns = '<button class="code-btn" onclick="copyCode(this)">⧉ 複製</button>' if copy else ""
    return f'''<div class="code-card">
  <div class="code-head">
    <span class="dot r"></span><span class="dot y"></span><span class="dot g"></span>
    <span class="label">{esc(label)}</span>
    <span class="actions">{btns}</span>
  </div>
  <pre><code data-lang="{lang}">{safe}</code></pre>
</div>'''


def reveal_table(headers, rows, reveal_col=1):
    ths = "".join(f"<th>{esc(h)}</th>" for h in headers)
    trs = ""
    for r in rows:
        tds = ""
        for ci, cell in enumerate(r):
            if ci == reveal_col:
                tds += f'<td class="hide-cell" onclick="revealCell(this)">{cell}</td>'
            else:
                tds += f'<td>{cell}</td>'
        trs += f"<tr>{tds}</tr>"
    return f'''<div class="reveal-table-wrap">
  <div class="reveal-table-bar"><button class="reveal-all-btn" onclick="revealAll(this)">👁️ 一鍵全開</button></div>
  <div class="table-wrap"><table class="reveal-table center">
    <thead><tr>{ths}</tr></thead>
    <tbody>{trs}</tbody>
  </table></div>
</div>'''


def exercise(title, items_html, answer_html=None):
    ans = ""
    if answer_html:
        ans = f'''<div class="reveal" onclick="toggleAnswer(this)">▶ 顯示解答／參考方向</div>
    <div class="answer">{answer_html}</div>'''
    return f'''<div class="exercise">
  <h3>✏️ {esc(title)}</h3>
  {items_html}
  {ans}
</div>'''


def diagram_card(svg_html, caption=""):
    cap = f'<div class="cap" style="margin-top:8px;font-size:.84rem;color:var(--text-soft)">{caption}</div>' if caption else ""
    return f'<div class="diagram-card">{svg_html}{cap}</div>'


def block(num, title, body_html, sec_id=None):
    sid = sec_id or f"sec{num}"
    return f'''<section class="block" id="{sid}">
  <h2><span class="num">{num:02d}</span>{title}</h2>
  {body_html}
</section>'''


def two_options(intro, a_title, a_html, b_title, b_html, note=""):
    """本單元的兩種教學方案，並排呈現供老師之後挑選／混用。"""
    body = f'''<p>{intro}</p>
<div class="grid cols-2">
  <div class="card"><h3>🅰️ {esc(a_title)}</h3>{a_html}</div>
  <div class="card"><h3>🅱️ {esc(b_title)}</h3>{b_html}</div>
</div>'''
    if note:
        body += f'<p style="font-size:.85rem;color:var(--text-faint);margin-top:10px">{note}</p>'
    return callout("🧭 這個單元的兩種教學方案（先都放上來，之後再挑一種調整／混用）", body, kind="tip")


# ---------------------------------------------------------------
# 版面骨架
# ---------------------------------------------------------------

def _topbar():
    return f'''<header class="topbar">
  <div class="topbar-inner">
    <a class="brand" href="index.html">
      <span class="logo">資安</span>
      <span>{esc(COURSE)}</span>
    </a>
    <span class="spacer"></span>
    <a class="nav-link" href="index.html">課程首頁</a>
    <button class="theme-toggle" onclick="toggleTheme()" aria-label="切換深淺色" title="切換深淺色">🌙</button>
  </div>
</header>'''


def _footer():
    return f'''<footer class="site">
  {esc(COURSE)}　{esc(TEACHER)}<br>
  本教材網站供課堂教學使用（基本版草稿，內容會持續調整） · 聯絡信箱 <a href="mailto:{CONTACT}">{CONTACT}</a>
</footer>'''


def page(unit_id, body, wip=False):
    i = IDX[unit_id]
    fn, title, sub, cat, desc, tags = UNITS[i]
    wip_banner = ('<div class="wip-banner">🚧 <strong>基本版草稿</strong>　本頁內容為第一版，之後可依課堂需求調整</div>'
                  if wip else "")
    prev_a = next_a = ""
    if i > 0:
        p = UNITS[i - 1]
        prev_a = f'<a class="prev" href="{p[0]}.html"><div class="dir">← 上一單元</div><div class="ttl">{esc(p[1])}</div></a>'
    else:
        prev_a = '<a class="prev disabled"><div class="dir">← 上一單元</div><div class="ttl">已是第一個</div></a>'
    if i < len(UNITS) - 1:
        n = UNITS[i + 1]
        next_a = f'<a class="next" href="{n[0]}.html"><div class="dir">下一單元 →</div><div class="ttl">{esc(n[1])}</div></a>'
    else:
        next_a = '<a class="next disabled"><div class="dir">下一單元 →</div><div class="ttl">已是最後一個</div></a>'

    unit_no = i + 1
    return f'''<!DOCTYPE html>
<html lang="zh-Hant" data-theme="light">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>單元 {unit_no}：{esc(title)}｜{esc(COURSE)}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@400;500;700;800;900&family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/style.css">
</head>
<body>
{_topbar()}
{wip_banner}
<main class="wrap" data-unit="{unit_no}">
  <nav class="crumbs"><a href="index.html">課程首頁</a> ／ <span>單元 {unit_no}</span></nav>
  {body}
  <nav class="unit-nav">
    {prev_a}
    {next_a}
  </nav>
</main>
{_footer()}
<script src="assets/progress.js"></script>
<script src="assets/script.js"></script>
</body>
</html>'''


def hero(unit_id, kicker_extra=""):
    i = IDX[unit_id]
    fn, title, sub, cat, desc, tags = UNITS[i]
    part_label = {p[0]: p[1] for p in PARTS}[cat]
    kicker = part_label.split(" · ")[0] + f"　單元 {i+1}"
    return f'''<section class="unit-hero">
  <span class="kicker">{esc(kicker)}</span>
  <h1>{esc(title)}</h1>
  <p>{esc(sub)}</p>
</section>'''


def build_index():
    def unit_card(u, n):
        fn, title, sub, cat, desc, tags = u
        tagspan = "".join(f"<span>{esc(t)}</span>" for t in tags)
        return f'''<a class="ucard" href="{fn}.html" data-unit="{n}">
      <span class="arrow">→</span>
      <div class="n">{n:02d}</div>
      <h3>{esc(title)}</h3>
      <p>{esc(desc)}</p>
      <div class="tags">{tagspan}</div>
    </a>'''

    sections = ""
    for key, label, cnt in PARTS:
        cards = "\n    ".join(unit_card(u, IDX[u[0]] + 1) for u in UNITS if u[3] == key)
        sections += f'''
  <div class="section-title">
    <span class="bar"></span><h2>{esc(label)}</h2>
    <span class="cnt">{esc(cnt)}</span>
  </div>
  <div class="unit-cards">
    {cards}
  </div>
'''

    return f'''<!DOCTYPE html>
<html lang="zh-Hant" data-theme="light">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{esc(COURSE)}｜課程首頁</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@400;500;700;800;900&family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/style.css">
</head>
<body>
<header class="topbar">
  <div class="topbar-inner">
    <a class="brand" href="index.html"><span class="logo">資安</span>
      <span>{esc(COURSE)}</span></a>
    <span class="spacer"></span>
    <button class="theme-toggle" onclick="toggleTheme()" title="切換深淺色">🌙</button>
  </div>
</header>

<section class="hero">
  <span class="badge">{esc(TEACHER)}</span>
  <h1>{esc(COURSE)}　<span class="grad">學習網站</span></h1>
  <p>從 2050 年的未來情境出發，一路回推到今天：數位身分、區塊鏈、比特幣、密碼學、數位簽章……這學期我們一起拆解「數位信任」是怎麼被一層層打造出來的。點選下方單元開始學習，每個單元都是獨立頁面。</p>
  <div class="meta">
    <span>📘 20 個教學單元</span>
    <span>🔐 古典密碼到 RSA</span>
    <span>⛓️ 區塊鏈與比特幣</span>
    <span>🎯 專題式學習（PBL）</span>
  </div>
</section>

<main class="wrap">
{sections}
</main>

<footer class="site">
  {esc(COURSE)}　{esc(TEACHER)}　·　教材網站（基本版草稿）
</footer>
<script src="assets/progress.js"></script>
<script src="assets/script.js"></script>
</body>
</html>'''
