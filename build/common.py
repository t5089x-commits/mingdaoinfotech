# -*- coding: utf-8 -*-
"""共用骨架：頁面 wrapper、單元中繼資料、首頁產生器、程式碼區塊小工具。"""
import html as _html
from urllib.parse import quote as _q


def wm_img(filename, alt, caption, width=760):
    """嵌入 Wikimedia Commons 的實體照片（穩定連結 Special:FilePath）。
    filename：Commons 上的檔名（不含 File: 前綴）。附圖說、來源連結與載入失敗備援。"""
    src = "https://commons.wikimedia.org/wiki/Special:FilePath/" + _q(filename) + "?width=%d" % width
    page = "https://commons.wikimedia.org/wiki/File:" + _q(filename.replace(" ", "_"))
    a = esc(alt)
    return f'''<figure class="fig">
  <img src="{src}" alt="{a}" loading="lazy"
       onerror="this.closest('figure').classList.add('img-fail')">
  <div class="img-fallback">🖼️ 圖片需連網載入<br><span>{a}</span></div>
  <figcaption>{caption} <a class="credit" href="{page}" target="_blank" rel="noopener">圖片來源：Wikimedia Commons ↗</a></figcaption>
</figure>'''

def wm_thumb(filename, alt, width=460):
    """單元卡片(tile)用的小型實體照片。點圖可到 Commons 來源頁；載入失敗顯示替代字。"""
    src = "https://commons.wikimedia.org/wiki/Special:FilePath/" + _q(filename) + "?width=%d" % width
    page = "https://commons.wikimedia.org/wiki/File:" + _q(filename.replace(" ", "_"))
    a = esc(alt)
    return f'''<a class="tile-imgwrap" href="{page}" target="_blank" rel="noopener" title="圖片來源：Wikimedia Commons ↗（點圖看原始出處）">
  <img class="tile-img" src="{src}" alt="{a}" loading="lazy" onerror="this.closest('.tile-imgwrap').classList.add('img-fail')">
  <span class="tile-imgfb">🖼️ {a}<br><small>需連網載入</small></span>
</a>'''


def bit_bulbs(wid, bases=False, note=""):
    """8 顆燈泡的二進位計數器（可按 ＋1／－1／自動／歸零）。
    bases=True 時同時顯示十／二／八／十六進位；note 為上方說明。"""
    cells = ""
    for _ in range(8):
        cells += ('<div class="bitb-cell"><span class="bitb-bulb">💡</span>'
                  '<span class="bitb-d">0</span></div>')
    if bases:
        read = ('<div class="bitb-bases">'
                '<div><span class="bk">十進位 dec</span><span class="bv" data-b="dec">0</span></div>'
                '<div><span class="bk">二進位 bin</span><span class="bv" data-b="bin">00000000</span></div>'
                '<div><span class="bk">八進位 oct</span><span class="bv" data-b="oct">0</span></div>'
                '<div><span class="bk">十六進位 hex</span><span class="bv" data-b="hex">0</span></div>'
                '</div>')
    else:
        read = ('<div class="bitb-simple">二進位 <span class="bv" data-b="bin">00000000</span>'
                ' ＝ <b class="bv" data-b="dec">0</b>（十進位）</div>')
    note_html = f'<div class="bitb-note">{note}</div>' if note else ''
    return (f'<div class="bitb" id="{wid}" data-val="0" data-bits="8">{note_html}'
            f'<div class="bitb-row">{cells}</div>{read}'
            f'<div class="bitb-btns">'
            f'<button type="button" onclick="bitStep(\'{wid}\',-1)">－1</button>'
            f'<button type="button" class="primary" onclick="bitStep(\'{wid}\',1)">＋1</button>'
            f'<button type="button" class="bitb-play" onclick="bitPlay(\'{wid}\',this)">▶ 自動</button>'
            f'<button type="button" onclick="bitZero(\'{wid}\')">歸零</button>'
            f'</div></div>')


COURSE = "明道中學 · 資訊科技"
TERM = "115 學年度第一學期 · 高中部"
TEACHER = "陳楷翔 老師"

# (檔名, 標題, 副標, 分類 theory/python, 卡片描述, 標籤list)
UNITS = [
    ("unit01", "課程介紹", "為什麼要學資訊科技？課程地圖與評量", "theory",
     "認識整學期的學習地圖、資訊科技的重要性與課程配分方式。",
     ["學習動機", "課程規劃", "評量方式"]),
    ("unit02", "數字系統", "各種進位系統、進位轉換與二進位運算", "theory",
     "2 / 8 / 10 / 16 進位的表示、互相轉換與二進位加減；附即時進位轉換器。",
     ["進位系統", "進位轉換", "互動工具"]),
    ("unit03", "資料運算與儲存", "邏輯閘、加法器、資料單位與訊號傳輸", "theory",
     "AND/OR/XOR/NOT 邏輯閘、半加器與全加器、資料儲存單位、類比與數位訊號、資料傳輸。",
     ["邏輯閘", "加法器", "互動真值表"]),
    ("unit04", "電腦簡介", "計算機發展史、電腦世代與種類", "theory",
     "從算盤到 AI 的發展歷程、四代電腦、摩爾定律與各類型電腦的應用。",
     ["發展史", "電腦世代", "電腦種類"]),
    ("unit05", "電腦五大單元", "輸入 / 輸出 / 控制 / ALU / 記憶", "theory",
     "電腦的組成、五大單元的功能、指令運作週期與影響 CPU 效能的因素。",
     ["五大單元", "CPU", "指令週期"]),
    ("unit06", "電腦硬體與組裝", "主機板、CPU、RAM、顯示卡、儲存裝置", "theory",
     "認識各主要零組件的規格與品牌，建立挑選與組裝一台電腦的觀念。",
     ["硬體規格", "選購", "組裝"]),
    ("unit07", "BEBRAS 運算思維", "運算思維與題型演練", "theory",
     "認識運算思維的四大支柱與 BEBRAS 國際挑戰賽，透過題型培養解題能力。",
     ["運算思維", "解題", "競賽"]),
    ("unit08", "Python（一）開發環境與變數", "開發環境、變數、資料型態、型別轉換", "python",
     "建立 Python 環境、認識變數與資料型態、型別轉換。",
     ["變數", "型別", "資料型態"]),
    ("unit13", "Python（二）基礎輸入與輸出", "input() 讀取、print() 與四種格式化輸出", "python",
     "用 input() 讀取輸入、print() 的 sep／end，以及 %、format、f-string 四種格式化輸出。",
     ["input", "print", "格式化輸出"]),
    ("unit14", "Python（三）運算子", "算術、比較、邏輯、複合指定與成員運算子", "python",
     "算術、比較、邏輯、身分與成員、複合指定運算子，搭配 BMI、判斷奇數等範例。",
     ["算術", "比較邏輯", "複合指定"]),
    ("unit09", "Python（四）選擇結構", "條件判斷 if / elif / else", "python",
     "單向、雙向、多向條件判斷 if / elif / else 與巢狀判斷。",
     ["if 判斷", "elif", "巢狀判斷"]),
    ("unit10", "Python（五）重複結構", "for 迴圈、while 迴圈與迴圈控制", "python",
     "for 與 while 迴圈、range、break 與 continue 的用法。",
     ["for", "while", "迴圈控制"]),
    ("unit11", "Python（六）迴圈進階與綜合", "巢狀迴圈、迴圈追蹤與綜合練習", "python",
     "巢狀迴圈、累加與計數樣式、迴圈追蹤技巧與綜合實作題。",
     ["巢狀迴圈", "程式追蹤", "實作"]),
    ("unit12", "Python（七）函式與綜合應用", "函式定義、參數、回傳值與整合專題", "python",
     "自訂函式、參數與回傳值、區域與全域變數，以及整合前面單元的綜合應用。",
     ["函式", "參數", "綜合專題"]),
]

IDX = {u[0]: i for i, u in enumerate(UNITS)}


def esc(s):
    return _html.escape(s, quote=False)


def code_block(code, lang="python", label=None, runnable=False, copy=True):
    """產生一個帶標題列與複製/執行按鈕的程式碼區塊。code 內容原樣（未跳脫）由 JS 上色。"""
    if label is None:
        label = {"python": "python", "text": "範例", "output": "輸出"}.get(lang, lang)
    code = code.strip("\n")
    # 於 HTML 中安全嵌入（JS 會讀 textContent 再處理）
    safe = _html.escape(code, quote=False)
    btns = ""
    if runnable:
        btns += '<button class="code-btn run" onclick="runCode(this)">▶ 執行</button>'
    if copy:
        btns += '<button class="code-btn" onclick="copyCode(this)">⧉ 複製</button>'
    return f'''<div class="code-card">
  <div class="code-head">
    <span class="dot r"></span><span class="dot y"></span><span class="dot g"></span>
    <span class="label">{esc(label)}</span>
    <span class="actions">{btns}</span>
  </div>
  <pre><code data-lang="{lang}">{safe}</code></pre>
</div>'''


def video_block(youtube_id=None, url=None, title="", caption="", placeholder_note=""):
    """影片區塊：給 youtube_id 就內嵌播放器；給 url 就放連結按鈕；都沒給則顯示占位框。"""
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
                 f'<a class="video-link-btn" href="{esc(url)}" target="_blank" rel="noopener">▶ 觀看影片 ↗</a></div>')
    else:
        note = placeholder_note or "把 YouTube 影片網址給我，我就幫你嵌進來（或改成連結按鈕）。"
        inner = (f'<div class="video-placeholder"><span class="vp-ico">🎬</span>'
                 f'<span class="vp-t">{esc(title or "影片區（待放入）")}</span>'
                 f'<span style="font-size:.85rem">{esc(note)}</span></div>')
    cap = f'<figcaption>{caption}</figcaption>' if caption else ''
    return f'<figure class="video-embed">{inner}{cap}</figure>'


def local_img(src, alt, caption="", bg="#fff"):
    """嵌入本站 images/ 內的圖片（離線可用）。"""
    a = esc(alt)
    cap = f'<figcaption>{caption}</figcaption>' if caption else ''
    return f'''<figure class="fig">
  <img src="{src}" alt="{a}" loading="lazy" style="background:{bg}">
  {cap}
</figure>'''


def reveal_table(headers, rows, reveal_col=1):
    """課堂互動表格：reveal_col 那一欄要點一下才顯示。附「一鍵全開」按鈕。
    headers: [th...]；rows: [[cell, cell...], ...]"""
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
        ans = f'''<div class="reveal" onclick="toggleAnswer(this)">▶ 顯示解答</div>
    <div class="answer">{answer_html}</div>'''
    return f'''<div class="exercise">
  <h3>✏️ {esc(title)}</h3>
  {items_html}
  {ans}
</div>'''


def _topbar():
    return f'''<header class="topbar">
  <div class="topbar-inner">
    <a class="brand" href="index.html">
      <span class="logo">IT</span>
      <span>{esc(COURSE)}<small>{esc(TERM)}</small></span>
    </a>
    <span class="spacer"></span>
    <a class="nav-link" href="index.html">課程首頁</a>
    <button class="theme-toggle" onclick="toggleTheme()" aria-label="切換深淺色" title="切換深淺色">🌙</button>
  </div>
</header>'''


PROGRAMIZ = "https://www.programiz.com/python-programming/online-compiler/"

def _tools_zone(tools_html):
    if not tools_html or not tools_html.strip():
        return ""
    return f'''<section class="tools-zone">
  <div class="wrap">
    <h2>🧪 課堂互動工具</h2>
    <p class="tz-note">先自己動手算算看／推推看，再用下面的工具對答案，學習效果最好。</p>
    {tools_html}
  </div>
</section>'''


def _compiler_cta():
    return f'''<a class="compiler-cta" href="{PROGRAMIZ}" target="_blank" rel="noopener" title="開啟 Programiz 線上 Python 編譯器：把上面的程式碼複製過去就能執行（另開新分頁）">
  <span class="ic">🐍</span>
  <span class="tx">Programiz<br>線上執行</span>
</a>'''

def _footer():
    return f'''<footer class="site">
  {esc(COURSE)}　{esc(TERM)}　{esc(TEACHER)}<br>
  本教材網站供課堂教學使用 · 聯絡信箱 <a href="mailto:t5089x@ms.mingdao.edu.tw">t5089x@ms.mingdao.edu.tw</a>
</footer>'''


def page(unit_id, body, tools_html="", wip=False, extra_head=""):
    """組合單元頁：hero 由 body 提供，這裡負責上下框架、上一頁/下一頁、頁尾工具區。"""
    i = IDX[unit_id]
    fn, title, sub, cat, desc, tags = UNITS[i]
    wip_banner = ('<div class="wip-banner">🚧 <strong>待修改</strong>　此頁內容老師稍後會再補充／調整</div>'
                  if wip else "")
    # 上/下一頁
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
{extra_head}
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
{_tools_zone(tools_html)}
{_compiler_cta() if cat == "python" else ""}
{_footer()}
<script src="assets/progress.js"></script>
<script src="assets/script.js"></script>
</body>
</html>'''


def hero(unit_id):
    i = IDX[unit_id]
    fn, title, sub, cat, desc, tags = UNITS[i]
    kicker = ("理論篇" if cat == "theory" else "Python 程式設計篇") + f"　單元 {i+1}"
    return f'''<section class="unit-hero">
  <span class="kicker">{esc(kicker)}</span>
  <h1>{esc(title)}</h1>
  <p>{esc(sub)}</p>
</section>'''


def goals(items):
    lis = "\n".join(f"<li>{it}</li>" for it in items)
    return f'''<div class="goals">
  <h2>🎯 學習目標</h2>
  <ul>
{lis}
  </ul>
</div>'''


def build_gate():
    """教師專區入口頁：輸入密鑰後跳轉到影片資源庫。學生無密鑰無法進入。"""
    return f'''<!DOCTYPE html>
<html lang="zh-Hant" data-theme="light">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>教師專區 · 需要密鑰｜{esc(COURSE)}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@400;500;700;800;900&family=JetBrains+Mono:wght@400;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/style.css">
</head>
<body>
{_topbar()}
<main class="wrap">
  <div class="gate-card">
    <div class="gate-ico">🔒</div>
    <h1>教師專區</h1>
    <p class="gate-sub">影片資源庫為教學規劃用，需要<strong>密鑰</strong>才能進入。<br>請輸入密鑰後按「進入」。</p>
    <div class="gate-form">
      <input id="pw" type="password" placeholder="請輸入密鑰" autocomplete="off" aria-label="密鑰">
      <button class="btn" onclick="tryEnter()">進入 →</button>
    </div>
    <div class="gate-err" id="err"></div>
    <a class="gate-back" href="index.html">← 返回課程首頁</a>
  </div>
</main>
<a href="access-mechanism.html" title="?" aria-label="機制說明"
   style="position:fixed;right:7px;bottom:7px;z-index:60;font-size:11px;line-height:1;
          color:var(--text-faint);opacity:.07;text-decoration:none;letter-spacing:1px;
          padding:6px;border-radius:6px;transition:opacity .25s"
   onmouseover="this.style.opacity='.9'" onmouseout="this.style.opacity='.07'">· ? ·</a>
<!-- 你正在找密碼嗎? 有興趣你就努力試試看吧~ -->
<div hidden aria-hidden="true" data-note="nothing-to-see-here"><!-- …確定沒有嗎？這個 ▶ 點開看看 -->
  <div><!-- 咦你居然點開了。還沒到，再往下一層 ▽ -->
    <div><!-- 有耐心喔。繼續 ▽ -->
      <div><!-- 快到了，再一層就好 ▽ -->
        <div><!-- 最後一層，恭喜你挖到了 ▽ -->
          <!--
            接下來使用 Base64 即可破解：

            6Kej6ZaL5LqG77yM5YGa5b6X5aW977yB5o6l5LiL5L6G6KaB5omT6ZaL57ay56uZ55qEIGFzc2V0cy9wcm9ncmVzcy5qcyDmqpTmoYjvvIzlhanlgIvmlrnms5Xmk4fkuIDvvJooMSkg5oqK54++5Zyo57ay5Z2A5YiX5pyA5b6M55qEIHZpZGVvLWFjY2Vzcy5odG1sIOaUueaIkCBhc3NldHMvcHJvZ3Jlc3MuanMg5YaN5oyJIEVudGVy77ybKDIpIOaMiSBGMTIg6YG444CM5L6G5rqQIFNvdXJjZXPjgI3liIbpoIHvvIzlnKggYXNzZXRzIOizh+aWmeWkvuijoem7numWiyBwcm9ncmVzcy5qc+OAguWvhueivOWSjOiAgeW4q+aDs+i3n+S9oOiqqueahOipsemDveWcqOijoemdouOAgg==
          -->
        </div>
      </div>
    </div>
  </div>
</div>
<script src="assets/progress.js"></script>
<script>
function tkey(){{ return (window.COURSE_PROGRESS && COURSE_PROGRESS.teacherKey) || ""; }}
function param(n){{ var m=new RegExp("[?&]"+n+"=([^&#]*)").exec(location.search); return m?decodeURIComponent(m[1]):null; }}
function enter(){{ location.href="video-library.html"; }}
function tryEnter(){{
  var v=(document.getElementById("pw").value||"").trim();
  // 這個比對是在「你的瀏覽器」裡做的（前端）——這正是它擋不住高手的地方。
  //     正確密鑰是怎麼來的？順著 tkey() 追追看它讀的是哪個變數、那個變數又是誰給的 :)
  if(v && v===tkey()){{ enter(); }}
  else{{ document.getElementById("err").textContent="✗ 密鑰錯誤，請再試一次。"; }}
}}
// 網址已帶正確 key 就直接放行
if(tkey() && param("key")===tkey()){{ enter(); }}
document.addEventListener("DOMContentLoaded", function(){{
  var i=document.getElementById("pw");
  i.focus();
  i.addEventListener("keydown", function(e){{ if(e.key==="Enter") tryEnter(); }});
}});
</script>
</body>
</html>'''


def build_access_info():
    """密碼機制說明頁：給靠自己找到的同學。含流程圖 + 前端/後端密碼的資安差異。"""
    # 流程圖用內嵌樣式的方塊堆疊，會跟著深淺色主題變色
    box = ("display:block;background:var(--surface);border:1.5px solid var(--border);"
           "border-radius:10px;padding:12px 16px;max-width:560px;margin:0 auto;"
           "box-shadow:0 2px 8px rgba(0,0,0,.06)")
    arrow = ('<div style="text-align:center;color:var(--brand);font-size:1.4rem;'
             'line-height:1;margin:6px 0">▼</div>')
    step = lambda n, t: (f'<div style="{box}"><span style="display:inline-block;min-width:26px;height:26px;'
                         f'line-height:26px;text-align:center;background:var(--brand);color:#fff;border-radius:50%;'
                         f'font-weight:800;font-size:.85rem;margin-right:10px">{n}</span>{t}</div>')
    return f'''<!DOCTYPE html>
<html lang="zh-Hant" data-theme="light">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>密碼機制是怎麼運作的？｜{esc(COURSE)}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@400;500;700;800;900&family=JetBrains+Mono:wght@400;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/style.css">
</head>
<body>
{_topbar()}
<main class="wrap" style="max-width:820px">

  <div class="callout" style="border-left:4px solid var(--brand);margin-top:22px">
    <span class="t">👋 如果你是靠自己找到這裡的</span>
    <p>能找到那個藏起來的入口，代表你有觀察力也夠好奇——這正是資安領域最需要的特質。這一頁就好好把「你剛剛想破解的那個密碼」到底怎麼運作、以及它<strong>為什麼擋不住高手</strong>講清楚。看完歡迎來找{esc(TEACHER)}聊聊，或加入 <strong>明道 SIG 資安社</strong>。</p>
  </div>

  <h1 style="margin-top:26px">🔍 密碼機制是怎麼運作的？</h1>
  <p>「教師專區」那一頁，從你按下「進入 →」到畫面跳轉，中間發生的事情其實可以拆成幾個步驟：</p>

  <h2>一、密碼輸入的流程圖</h2>
  <div style="background:var(--surface-2);border:1px solid var(--border);border-radius:14px;padding:22px 16px;margin:18px 0">
    {step("1", "你在輸入框打入密鑰，按下「進入 →」按鈕。")}
    {arrow}
    {step("2", "網頁裡的 JavaScript 函式 <code>tryEnter()</code> 讀出你打的那串字。")}
    {arrow}
    {step("3", '程式再從 <code>assets/progress.js</code> 讀出正確密鑰 <code>teacherKey</code>（老師事先設定好、<strong>明碼</strong>存著）。')}
    {arrow}
    <div style="text-align:center;margin:2px 0">
      <div style="display:inline-block;background:var(--warn-soft);border:1.5px solid var(--warn);color:var(--warn);
                  font-weight:800;padding:12px 20px;border-radius:12px;max-width:560px">
        ❓ 判斷：你輸入的字　<code style="background:transparent;border:none;color:inherit">===</code>　teacherKey　嗎？
      </div>
    </div>
    <div style="display:flex;gap:12px;justify-content:center;flex-wrap:wrap;margin-top:14px">
      <div style="flex:1;min-width:220px;background:var(--surface);border:1.5px solid var(--ok);border-radius:10px;padding:12px 14px">
        <div style="font-weight:800;color:var(--ok);margin-bottom:4px">✓ 一樣（正確）</div>
        執行 <code>location.href = "video-library.html"</code>，把你的瀏覽器<strong>跳轉</strong>到影片資源庫。
      </div>
      <div style="flex:1;min-width:220px;background:var(--surface);border:1.5px solid var(--danger);border-radius:10px;padding:12px 14px">
        <div style="font-weight:800;color:var(--danger);margin-bottom:4px">✗ 不一樣（錯誤）</div>
        在畫面上顯示「密鑰錯誤，請再試一次」，停在原地。
      </div>
    </div>
  </div>
  <div class="callout"><span class="t">💡 關鍵一句話</span>
    <p>上面<strong>每一個步驟</strong>——讀你的輸入、讀正確密碼、做比對、決定跳不跳轉——<strong>全部都在「你自己的電腦（瀏覽器）」裡執行</strong>。沒有任何一步是送到老師的伺服器去問的。記住這句話，下一段就懂為什麼它不安全了。</p>
  </div>

  <h2>二、前端密碼 vs. 真正的後端密碼</h2>
  <p>「密碼比對到底在哪裡做」是資安裡很重要的分水嶺。分成兩種：</p>

  <div class="table-wrap"><table class="center">
  <thead><tr><th style="width:20%"></th><th>前端密碼<br><span style="font-weight:400;font-size:.85rem">（就是這一頁現在用的方式）</span></th><th>後端密碼<br><span style="font-weight:400;font-size:.85rem">（真正安全的做法）</span></th></tr></thead>
  <tbody>
  <tr><td><strong>比對在哪裡做</strong></td><td>在<strong>你的瀏覽器</strong>裡（前端 JavaScript）。</td><td>在<strong>伺服器</strong>裡（你碰不到的另一台電腦）。</td></tr>
  <tr><td><strong>正確密碼存在哪</strong></td><td>就寫在 <code>progress.js</code> 裡，<strong>打開原始碼就看得到</strong>。</td><td>存在伺服器資料庫，而且通常存的是<strong>雜湊值 (hash)</strong> 不是明碼。</td></tr>
  <tr><td><strong>受保護的內容</strong></td><td><code>video-library.html</code> 是獨立網頁，<strong>知道網址直接開就看得到</strong>，根本不需要密碼。</td><td>驗證通過前，內容<strong>根本不會送到</strong>你的瀏覽器，繞不過去。</td></tr>
  <tr><td><strong>能不能被繞過</strong></td><td>可以。看原始碼、改 JavaScript、或直接打網址都能繞過。</td><td>很難。因為關鍵判斷不在使用者手上。</td></tr>
  <tr><td><strong>優點</strong></td><td>不用伺服器、做起來超簡單。</td><td>真正擋得住人。</td></tr>
  <tr><td><strong>缺點</strong></td><td><strong>幾乎沒有安全性</strong>，擋君子不擋小人。</td><td>要架伺服器、寫後端程式，比較複雜。</td></tr>
  </tbody></table></div>

  <div class="callout" style="border-left:4px solid var(--warn)">
    <span class="t">🧩 那「我現在這種方式」屬於哪一種？</span>
    <p>老實說：<strong>就是「前端密碼」</strong>。密鑰 <code>t…x</code> 明碼放在 <code>progress.js</code>，比對在你的瀏覽器裡跑，而影片頁又是一個直接打網址就能開的獨立網頁。所以它比較像是「在門上貼一張紙寫『非教師請勿進入』」——擋得住願意守規矩的人，但擋不住真的想進去、又懂一點技術的人。</p>
    <p>老師<strong>故意</strong>用這種簡單方式，一來影片庫本來就只是教學規劃用、不是什麼機密；二來，它剛好是最好的資安教材：讓你親眼看到「看起來有上鎖，其實鎖在自己手上」是什麼意思。</p>
  </div>

  <div class="callout">
    <span class="t">🚩 想做出真正安全的密碼，方向是？</span>
    <p>把「決定放不放行」這件事搬到<strong>伺服器</strong>去做，內容在驗證成功前不要送出；密碼不要存明碼，改存<strong>雜湊值</strong>（可以去看影片庫裡「密碼雜湊」那部影片）；再加上防止一直猜的機制。這些就是<strong>資安社</strong>會一起玩的東西。</p>
  </div>

  <p style="margin-top:26px"><a class="gate-back" href="video-access.html">← 返回教師專區</a>　　<a class="gate-back" href="index.html">回課程首頁</a></p>
</main>
<script src="assets/progress.js"></script>
<script src="assets/script.js"></script>
</body>
</html>'''


def build_index():
    theory = [u for u in UNITS if u[3] == "theory"]
    python = [u for u in UNITS if u[3] == "python"]

    def card(u, n):
        fn, title, sub, cat, desc, tags = u
        tagspan = "".join(f"<span>{esc(t)}</span>" for t in tags)
        cls = "ucard py" if cat == "python" else "ucard"
        return f'''<a class="{cls}" href="{fn}.html" data-unit="{n}">
      <span class="arrow">→</span>
      <div class="n">{n:02d}</div>
      <h3>{esc(title)}</h3>
      <p>{esc(desc)}</p>
      <div class="tags">{tagspan}</div>
    </a>'''

    theory_cards = "\n    ".join(card(u, IDX[u[0]] + 1) for u in theory)
    python_cards = "\n    ".join(card(u, IDX[u[0]] + 1) for u in python)

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
    <a class="brand" href="index.html"><span class="logo">IT</span>
      <span>{esc(COURSE)}<small>{esc(TERM)}</small></span></a>
    <span class="spacer"></span>
    <button class="theme-toggle" onclick="toggleTheme()" title="切換深淺色">🌙</button>
  </div>
</header>

<section class="hero">
  <span class="badge">{esc(TERM)}　·　{esc(TEACHER)}</span>
  <h1>資訊科技　<span class="grad">學習網站</span></h1>
  <p>從數字系統、電腦硬體到 Python 程式設計，一整個學期的課程都在這裡。點選下方單元開始學習，每個單元都是獨立頁面，內含教學說明、圖表、互動工具與課堂練習。</p>
  <div class="meta">
    <span>📘 14 個教學單元</span>
    <span>🧮 進位轉換器</span>
    <span>🔌 邏輯閘互動</span>
    <span>🐍 Python 範例可複製</span>
  </div>
</section>

<main class="wrap">
  <div class="section-title">
    <span class="bar"></span><h2>理論篇 · 電腦科學基礎</h2>
    <span class="cnt">單元 1–7</span>
  </div>
  <div class="unit-cards">
    {theory_cards}
  </div>

  <div class="section-title py">
    <span class="bar"></span><h2>Python 程式設計篇</h2>
    <span class="cnt">單元 8–14</span>
  </div>
  <div class="unit-cards">
    {python_cards}
  </div>
</main>

<footer class="site">
  {esc(COURSE)}　{esc(TERM)}　{esc(TEACHER)}　·　教材網站
</footer>
<a class="teacher-fab" href="video-access.html" title="教師專區：需密鑰才能進入影片資源庫">🔒 教師專區<small>影片資源庫</small></a>
<script src="assets/progress.js"></script>
<script src="assets/script.js"></script>
</body>
</html>'''
