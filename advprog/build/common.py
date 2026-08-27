# -*- coding: utf-8 -*-
"""共用骨架：頁面 wrapper、單元中繼資料、首頁產生器、內容小工具。
   （改編自「資訊安全導論」課程網站的產生器架構，重新配色套用到「進階程式設計」課程。）"""
import html as _html

COURSE = "進階程式設計"
TEACHER = "陳楷翔 老師"
CONTACT = "t81710@gmail.com"

# (檔名, 標題, 副標, 分類代碼, 卡片描述, 標籤list)
# 分類代碼對應下面 PARTS 的 key，用來分組＋算「單元 x／y」
UNITS = [
    ("unit01", "課程總覽＋專題預告", "這學期的學習地圖：從 Python 複習到專題發表", "overview",
     "認識整學期的學習地圖與評量方式，預告期末專題（政府開放資料 × pandas × Matplotlib），並認識 VS Code 開發環境。",
     ["課程地圖", "專題預告", "VS Code"]),
    ("unit02", "Python 前導複習（一）變數與資料型態", "變數、命名規則、資料型態、型別轉換、f-string", "pyreview",
     "快速複習變數、四種基本資料型態、type() 查型別、型別轉換（casting），以及 f-string 格式化輸出。",
     ["變數", "資料型態", "f-string"]),
    ("unit03", "Python 前導複習（二）運算子與判斷", "算術／比較／邏輯運算子、if／elif／else", "pyreview",
     "複習算術、比較、邏輯與複合指定運算子，並複習 if、if-else、if-elif-else 條件判斷結構。",
     ["運算子", "if判斷", "條件式"]),
    ("unit04", "Python 前導複習（三）迴圈與函式", "for／while 迴圈、break／continue、函式", "pyreview",
     "複習 for 迴圈、while 迴圈、break／continue，以及函式的定義、參數與回傳值，銜接後面的資料分析程式。",
     ["迴圈", "函式", "綜合複習"]),
    ("unit05", "Vibe Coding 體驗——用 AI 打造你的 pygame 小遊戲", "AI協作開發、pygame基礎、除錯與迭代", "vibe",
     "體驗「用自然語言描述需求、讓 AI 生成程式碼、執行測試、再用對話除錯與加功能」的 Vibe Coding 開發模式，用 pygame 做出一款小遊戲。",
     ["Vibe Coding", "pygame", "AI協作"]),
    ("unit06", "pandas 基礎操作", "Series 與 DataFrame：資料的直向欄位與表格操作", "pandas",
     "學會安裝 pandas，操作單維度的 Series（建立、運算、增刪、字串處理）與雙維度的 DataFrame（建立、取欄取列、索引）。",
     ["Series", "DataFrame", "pandas"]),
    ("unit07", "Matplotlib 基本使用", "折線圖、直方圖、柱狀圖、圓餅圖與存檔", "matplotlib",
     "學會用 Matplotlib 畫折線圖、直方圖、柱狀圖、圓餅圖，調整標題／刻度／樣式，並將圖表存檔。",
     ["折線圖", "圓餅圖", "savefig"]),
    ("unit08", "專題啟動——政府開放資料探索", "認識開放資料平台、下載資料、選定專題主題", "project",
     "認識政府公開資料平台，學會搜尋、下載並用 pandas 初步檢視資料，發想並選定自己的專題主題。",
     ["開放資料", "data.gov.tw", "主題發想"]),
    ("unit09", "專題實作工作坊——pandas × Matplotlib 視覺化分析", "資料清理、分析、選圖與實作", "project",
     "動手清理與篩選自己的專題資料，依資料特性選擇合適的圖表類型，用 pandas＋Matplotlib 完成視覺化分析。",
     ["資料清理", "視覺化", "實作工作坊"]),
    ("unit10", "專題成果整理與發表", "彙整分析結果、匯出 PDF 成果、口頭發表", "project",
     "把程式、圖表與文字解讀整合成一份 PDF 專題報告，練習簡短發表與同儕互評。",
     ["PDF報告", "發表", "總結"]),
]

IDX = {u[0]: i for i, u in enumerate(UNITS)}

PARTS = [
    ("overview", "Part 1 · 課程總覽", "單元 1"),
    ("pyreview", "Part 2 · Python 前導複習", "單元 2–4"),
    ("vibe", "Part 3 · Vibe Coding 體驗", "單元 5"),
    ("pandas", "Part 4 · pandas 應用", "單元 6"),
    ("matplotlib", "Part 5 · Matplotlib 基本使用", "單元 7"),
    ("project", "Part 6 · 專題實作與發表", "單元 8–10"),
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


def timeline(items):
    """課程流程時間軸。items: list of (when, what) tuples。每三個一循環 a/b/c 上色。"""
    cls_cycle = ["a", "b", "c"]
    blocks = []
    for i, (when, what) in enumerate(items):
        blocks.append(f'<div class="tl-block {cls_cycle[i % 3]}"><span class="tl-when">{esc(when)}</span><span class="tl-what">{esc(what)}</span></div>')
        if i < len(items) - 1:
            blocks.append('<span class="tl-arrow">→</span>')
    return f'<div class="timeline"><div class="tl-row">{"".join(blocks)}</div></div>'


# ---------------------------------------------------------------
# 版面骨架
# ---------------------------------------------------------------

def _topbar():
    return f'''<header class="topbar">
  <div class="topbar-inner">
    <a class="brand" href="index.html">
      <span class="logo">進階</span>
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
    <a class="brand" href="index.html"><span class="logo">進階</span>
      <span>{esc(COURSE)}</span></a>
    <span class="spacer"></span>
    <button class="theme-toggle" onclick="toggleTheme()" title="切換深淺色">🌙</button>
  </div>
</header>

<section class="hero">
  <span class="badge">{esc(TEACHER)}</span>
  <h1>{esc(COURSE)}　<span class="grad">學習網站</span></h1>
  <p>這學期我們從 Python 語法複習出發，體驗一次「Vibe Coding」用 AI 協作開發 pygame 小遊戲，接着學會 pandas 資料整理與 Matplotlib 視覺化，最後到政府開放資料平台找一份自己感興趣的資料，做出一份圖文並茂的專題 PDF 報告。點選下方單元開始學習，每個單元都是獨立頁面。</p>
  <div class="meta">
    <span>📘 10 個教學單元</span>
    <span>🐍 Python 複習＋Vibe Coding</span>
    <span>🐼 pandas＋Matplotlib</span>
    <span>📊 開放資料專題</span>
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
