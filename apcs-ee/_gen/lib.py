"""共用的頁面產生工具：所有程式範例都會真的執行一次，執行結果直接寫進頁面，保證跟教材一致。"""
import html, io, contextlib, builtins, traceback, re

E = html.escape
import os
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..") + "/"

def _run(src, stdin=None):
    buf = io.StringIO()
    lines = iter((stdin or "").split("\n"))
    def fake_input(*a):
        if a:
            print(a[0], end="")   # 跟真的 Python 一樣：提示文字會印到輸出
        try:
            return next(lines)
        except StopIteration:
            raise EOFError("EOF when reading a line")
    g = {"__builtins__": builtins, "__name__": "__main__"}
    orig = builtins.input
    builtins.input = fake_input
    err = None
    try:
        with contextlib.redirect_stdout(buf):
            exec(compile(src, "<程式>", "exec"), g)
    except SyntaxError as e:
        err = (e.lineno, f"{type(e).__name__}: {e.msg}", None, (e.text or "").rstrip("\n"))
    except Exception as e:
        tb = traceback.extract_tb(e.__traceback__)
        ln = [f for f in tb if f.filename == "<程式>"]
        lineno = ln[-1].lineno if ln else "?"
        fname = ln[-1].name if ln else "<module>"
        msg = "".join(traceback.TracebackException.from_exception(e).format_exception_only()).strip().splitlines()[-1]
        err = (lineno, msg, fname)   # 跟 IDLE 一樣，NameError 會附上「Did you mean」提示
    finally:
        builtins.input = orig
    return buf.getvalue().rstrip("\n"), err

def run_out(src, stdin=None):
    out, err = _run(src, stdin)
    assert err is None, (src, err)
    return out

def code(src, label="python", stdin=None, show=True, expect_error=False):
    """程式卡片＋實際執行結果。expect_error=True 時，顯示錯誤訊息（模擬 Python 的紅字最後一行）。"""
    src = src.strip("\n")
    out, err = _run(src, stdin)
    if err and not expect_error:
        raise AssertionError(f"範例執行失敗：{err}\n{src}")
    if expect_error and not err:
        raise AssertionError(f"預期要出錯但沒出錯：\n{src}")
    h = f'''  <div class="code-card">
    <div class="code-head"><span class="dot r"></span><span class="dot y"></span><span class="dot g"></span>
      <span class="label">{E(label)}</span>
      <span class="actions"><button class="code-btn" onclick="copyCode(this)">⧉ 複製</button></span></div>
    <pre><code data-lang="python">{E(src)}</code></pre>
'''
    if show:
        parts = []
        if stdin is not None:
            parts.append(f'<span class="muted">▼ 輸入（測資）</span>\n{E(stdin)}\n')
        parts.append('<span class="muted">▼ 執行結果</span>\n' + (E(out) if out else '<span class="muted">（沒有輸出）</span>'))
        if err and len(err) == 4:      # 語法錯誤：Python 不會印 Traceback 那一行
            parts.append(f'\n<span class="err">  File "程式.py", line {err[0]}\n    {E(err[3].strip())}\n{E(err[1])}</span>')
        elif err:
            parts.append(f'\n<span class="err">Traceback (most recent call last):\n  File "程式.py", line {err[0]}, in {E(err[2])}\n{E(err[1])}</span>')
        h += f'    <div class="code-output show">{"".join(parts)}</div>\n'
    h += "  </div>\n"
    return h

def err_of(src, stdin=None):
    out, err = _run(src, stdin)
    assert err, src
    return err[1]

def qa(items):
    """識讀練習：items = [(題目文字, 程式碼 或 None, 解答說明, stdin 或 None)]；解答會自動附上真正的輸出。"""
    h = '<div class="exercise qa-list">\n  <h3>✏️ 識讀練習：先自己追蹤，再按「顯示解答」</h3>\n  <ol>\n'
    for q, src, expl, stdin in items:
        h += f'    <li>{q}'
        if src:
            src = src.strip("\n")
            h += f'\n      <pre class="workpre">{E(src)}</pre>'
            out = run_out(src, stdin)
            res = f'<p>執行結果：</p><pre class="workpre">{E(out)}</pre>'
        else:
            res = ""
        h += f'\n      <div class="reveal" onclick="toggleAnswer(this)">▶ 顯示解答</div>\n      <div class="answer">{res}<p style="margin-bottom:0">{expl}</p></div>\n    </li>\n'
    h += '  </ol>\n</div>\n'
    return h

def section(num, title, body, sid=None):
    idattr = f' id="{sid}"' if sid else ""
    return f'''
<section class="block"{idattr}>
  <h2><span class="num">{num}</span>{title}</h2>
{body}
</section>
'''

def callout(title, text, kind=""):
    k = f" {kind}" if kind else ""
    return f'  <div class="callout{k}"><span class="t">{title}</span>\n  <p style="margin-bottom:0">{text}</p></div>\n'

def table(head, rows, cls=""):
    c = f' class="{cls}"' if cls else ""
    h = f'  <div class="table-wrap">\n    <table{c}>\n      <thead><tr>' + "".join(f"<th>{x}</th>" for x in head) + "</tr></thead>\n      <tbody>\n"
    for r in rows:
        h += "        <tr>" + "".join(f"<td>{x}</td>" for x in r) + "</tr>\n"
    return h + "      </tbody>\n    </table>\n  </div>\n"

def qchips(qs):
    return '<span class="qchips" style="display:inline-flex">' + "".join(
        f'<button type="button" class="qchip" data-q="{q}" title="看官方識讀範例第 {q} 題">{q}</button>' for q in qs) + "</span>"

HEAD = """<!DOCTYPE html>
<html lang="zh-Hant" data-theme="light">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}｜明道中學 · 資電APCS週六課程</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@400;500;700;800;900&family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/style.css">
<link rel="stylesheet" href="assets/tabs.css">
<link rel="stylesheet" href="assets/plan.css">
{extra_css}</head>
<body>
<header class="topbar">
  <div class="topbar-inner">
    <a class="brand" href="index.html">
      <span class="logo">AP</span>
      <span>明道中學 · 資電APCS週六課程<small>115 學年度第一學期 · 資電群二年級</small></span>
    </a>
    <span class="spacer"></span>
    <button class="theme-toggle" onclick="toggleTheme()" aria-label="切換深淺色" title="切換深淺色">🌙</button>
  </div>
  <nav class="page-tabs" aria-label="課程分頁"><div class="page-tabs-inner">
    <a href="index.html">🏠 課程首頁</a>
    <a href="schedule.html">📅 課程規劃（練習題目表）</a>
    <a href="functions.html">𝑓x 函式統整表</a>
  </div></nav>
</header>

<main class="wrap" data-unit="{unit}">
  <nav class="crumbs"><a href="index.html">課程首頁</a> ／ <span>{crumb}</span></nav>
  <section class="unit-hero">
  <span class="kicker">{kicker}</span>
  <h1>{h1}</h1>
  <p>{sub}</p>
</section>

<div class="goals">
  <h2>🎯 學習目標</h2>
  <ul>
{goals}  </ul>
</div>
"""

FOOT = """
  <nav class="unit-nav">
    {prev}
    {next}
  </nav>
</main>

<footer class="site">
  明道中學 · 資電APCS週六課程（APCS 程式設計能力培訓班）　115 學年度第一學期　陳楷翔 老師<br>
  本教材網站供課堂教學使用 · 聯絡信箱 <a href="mailto:t5089x@ms.mingdao.edu.tw">t5089x@ms.mingdao.edu.tw</a>
</footer>
<script src="../shared/core/progress.js"></script>
<script src="assets/progress.js"></script>
<script src="assets/script.js"></script>
<script src="assets/reading-viewer.js"></script>
{extra_js}</body>
</html>
"""

def nav(href, title, kind):
    if not href:
        return f'<a class="{kind} disabled"><div class="dir">{"← 上一單元" if kind=="prev" else "下一單元 →"}</div><div class="ttl">{"已是第一個" if kind=="prev" else "已是最後一個"}</div></a>'
    return f'<a class="{kind}" href="{href}"><div class="dir">{"← 上一單元" if kind=="prev" else "下一單元 →"}</div><div class="ttl">{title}</div></a>'

def add_ids(html_text):
    """每個章節加上 id="sNN"（NN 是章節編號），讓其他頁面可以連到「單元 X 的第 NN 節」。"""
    def fix(m):
        tag, body = m.group(1), m.group(2)
        n = re.search(r'<span class="num">(\d{2})</span>', body[:400])
        if not n:
            return m.group(0)
        sid = "s" + n.group(1)
        if f'id="{sid}"' in tag or f'id="{sid}"' in body[:200]:
            return m.group(0)
        if 'id="' in tag:
            return tag + f'<span id="{sid}" class="anchor"></span>' + body
        return tag.replace('<section class="block"', f'<section class="block" id="{sid}"', 1) + body
    return re.sub(r'(<section class="block"[^>]*>)(.*?)(?=</section>)', lambda m: fix(m), html_text, flags=re.S)

def page(fn, *, title, crumb, kicker, h1, sub, goals, body, unit, prev, next, extra_css="", extra_js=""):
    g = "".join(f"    <li>{x}</li>\n" for x in goals)
    s = HEAD.format(title=title, crumb=crumb, kicker=kicker, h1=h1, sub=sub, goals=g, unit=unit, extra_css=extra_css)
    s += body
    s += FOOT.format(prev=nav(*prev, "prev"), next=nav(*next, "next"), extra_js=extra_js)
    s = add_ids(s)
    import py125
    s = py125.add_unit_block(s, fn)
    open(ROOT + fn, "w", encoding="utf-8").write(s)
    print("wrote", fn, len(s))
