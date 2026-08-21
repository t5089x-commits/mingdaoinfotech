# -*- coding: utf-8 -*-
"""理論篇單元 1–7 的頁面內容。"""
from common import hero, goals, code_block, exercise, wm_img, video_block, reveal_table, local_img, esc, wm_thumb, bit_bulbs
from diagrams import gate_svg, audio_wave, analog_vs_digital, transmission, moore_huang, ui_evolution, switch_logic
from bebras_svg import hike1_svg, hike2_svg, tournament_svg, errand_svg, banana_svg, sprinkler_svg, banana_problem_svg, hike_trail_svg

def sec(n, title, inner):
    return f'''<section class="block" id="sec{n}">
  <h2><span class="num">{n:02d}</span>{title}</h2>
  {inner}
</section>'''

BODIES = {}

# =====================================================================
# 單元 01：課程介紹
# =====================================================================
BODIES["unit01"] = hero("unit01") + goals([
    "了解學習資訊科技對升學與未來職涯的重要性",
    "掌握本學期的課程地圖：電腦科學理論、硬體與 Python 程式設計",
    "清楚本課程的評量方式與配分",
]) + sec(1, "為什麼要學好資訊科技？", '''
<div class="grid cols-2">
  <div class="tile"><h4><span class="ico">🎓</span>升學採計</h4>
    <p>108 課綱後，大學申請入學會參採高中的<strong>學習歷程檔案</strong>；資訊科技的實作作品、專題與學習單，都是可以放進學習歷程、展現能力的素材。</p></div>
  <div class="tile"><h4><span class="ico">💹</span>經濟主力</h4>
    <p>資訊科技（尤其半導體與電子資訊）是台灣經濟的<strong>最大支柱</strong>，也是出口的主力。</p></div>
</div>
<div class="callout"><span class="t">📊 補充數據與來源</span>
<ul class="tidy">
  <li><strong>常聽到的說法：</strong>「資訊科技產業約佔台灣 GDP 三分之一」——這是<strong>概略講法</strong>，實際比例會因「資訊科技」的定義範圍而不同。</li>
  <li><strong>較精確的近期數據（主計總處，2024）：</strong>台灣<strong>製造業約佔 GDP 35%</strong>，其中<strong>電子資訊／半導體是最大支柱</strong>；電子與資通視聽產品更佔台灣出口的<strong>一半以上</strong>。</li>
</ul>
<p style="margin-bottom:0;font-size:.82rem;color:var(--text-faint)">資料來源：行政院主計總處國情統計、產業結構分析（2024）。數字逐年變動，此為 2024 年前後資料。</p></div>
''' + '''
<h3>未來十年最被需要的工作</h3>
<p>根據美國國家統計局提出的「未來重要職業」列表，其中有許多與資訊科技高度相關：</p>
<div class="grid cols-3">
  <div class="tile"><h4>🔐 網路安全專家</h4><p>Cyber security expert</p></div>
  <div class="tile"><h4>🤖 機器人工程師</h4><p>Robotics engineer</p></div>
  <div class="tile"><h4>💻 軟體開發</h4><p>Software developer</p></div>
  <div class="tile"><h4>🎨 用戶體驗設計師</h4><p>User experience designer</p></div>
  <div class="tile"><h4>📊 資料科學家</h4><p>Data scientist</p></div>
  <div class="tile"><h4>☁️ 雲端工程師</h4><p>Cloud engineer</p></div>
</div>
<div class="callout tip"><span class="t">💡 老師的話</span>
<p>學資訊科技不是要你們每個人都成為工程師，而是培養<strong>運算思維</strong>——用有邏輯、有系統的方式拆解問題、解決問題。這是任何行業都用得到的能力。</p></div>
<h3>🎬 AI 對未來職業的影響</h3>
<p>科技（尤其是 AI）正在改變各行各業，有些工作被取代，也有全新的工作出現。看看下面的影片，一起思考：<strong>未來我們該培養哪些能力？</strong></p>
<div class="grid cols-2">
''' + video_block(youtube_id="wB8AxVnLOnM", title="2029 年 AI 就會超越人類？哪些工作會被取代（志祺七七）",
                  caption="從「工作被取代」的角度看 AI 對就業的衝擊。") + video_block(
      youtube_id="wYKvePtJUkY", title="黃仁勳：會奪走你工作的不是 AI，而是…",
                  caption="產業領袖看 AI 帶來的挑戰與新機會。") + video_block(
      youtube_id="ADiJIMRR8QU", title="AI 正在創造「一人公司」黃金時代（Kelly Tsai）",
                  caption="AI 也創造出全新的賺錢方式與工作型態。") + '''
</div>
<p style="font-size:.85rem;color:var(--text-faint)">看完想一想：哪些工作可能被 AI 取代？又有哪些「新工作」因為 AI 而出現？我們現在該培養什麼能力？</p>
''') + sec(2, "課程地圖", '''
<p>本學期就是<strong>高一上學期</strong>，課程分成兩個階段：<strong>高一上學期前半</strong>先建立電腦科學的基礎理論與硬體概念，<strong>高一上學期後半</strong>就開始進入 <strong>Python 程式設計</strong>實作。<span style="color:var(--text-faint)">（注意：這裡的「前半／後半」都是指<strong>高一上這一個學期之內</strong>，不是下學期喔！）</span></p>
<div class="timeline"><div class="tl-row">
  <div class="tl-block a"><span class="tl-when">高一上學期 · 前半</span><span class="tl-what">📘 理論篇</span></div>
  <div class="tl-arrow">➜</div>
  <div class="tl-block b"><span class="tl-when">高一上學期 · 後半</span><span class="tl-what">🐍 開始學 Python</span></div>
  <div class="tl-arrow">➜</div>
  <div class="tl-block c"><span class="tl-when">高一下學期 · 持續精進</span><span class="tl-what">🎯 目標：APCS</span></div>
</div></div>
<div class="grid cols-2">
  <div class="card">
    <h3>📘 高一上學期・前半（理論篇）</h3>
    <ul>
      <li>數字系統（各種進位）</li>
      <li>資料運算與儲存（邏輯運算、加法器）</li>
      <li>電腦歷史與未來展望</li>
      <li>電腦五大單元</li>
      <li>電腦硬體與組裝</li>
      <li>BEBRAS 運算思維</li>
    </ul>
  </div>
  <div class="card">
    <h3>🐍 高一上學期・後半（Python 篇）</h3>
    <ul>
      <li>Python 開發環境、變數與資料型態</li>
      <li>基礎輸入與輸出（input／print／格式化）</li>
      <li>運算子（算術、比較、邏輯…）</li>
      <li>選擇結構（條件判斷）</li>
      <li>重複結構（迴圈）</li>
      <li>迴圈進階與綜合練習</li>
      <li>函式與綜合應用</li>
    </ul>
  </div>
</div>
<div class="callout tip"><span class="t">🎯 更長遠的目標（高一下持續往前）</span>
<p style="margin-bottom:0">把 Python 基礎打好之後，希望能一路練到 <strong>APCS（大學程式設計先修檢測）</strong> 的水準——<strong>希望目標：實作題 3 級分、觀念題 4 級分</strong>。這是高一上打底、<strong>高一下持續加強</strong>的方向。</p></div>
<div class="callout"><span class="t">🧭 導覽提示</span>
<p>本學習網站已把全部單元都做成獨立頁面，隨時可以回到<a href="index.html">課程首頁</a>切換到任何單元，方便課前預習與課後複習。</p></div>
''') + sec(3, "評量方式與配分", '''
<div class="table-wrap">
<table class="center">
  <thead><tr><th>評量項目</th><th>佔比</th><th>說明</th></tr></thead>
  <tbody>
    <tr><td><strong>學習單</strong></td><td>60%</td><td>各單元的課堂學習單與作業</td></tr>
    <tr><td><strong>運算思維</strong></td><td>30%</td><td>BEBRAS 題型與運算思維測驗</td></tr>
    <tr><td><strong>課堂表現</strong></td><td>10%</td><td>出席、參與討論與實作態度</td></tr>
  </tbody>
</table>
</div>
<div class="callout warn"><span class="t">⚠ 提醒</span>
<p>本課程<strong>沒有紙筆期中/期末考的配分</strong>，因此<strong>每一次學習單與課堂參與都很重要</strong>，請務必按進度完成。</p></div>
''')

# =====================================================================
# 單元 02：數字系統
# =====================================================================
_conv_widget = '''
<div class="widget">
  <div class="w-title">🧮 進位轉換器</div>
  <div class="w-sub">輸入一個數字並選擇它目前的進位，立即看到 2 / 8 / 10 / 16 進位的結果。</div>
  <div class="field-row">
    <div class="field">
      <label for="conv-input">數值</label>
      <input id="conv-input" type="text" value="156" oninput="convertBase()" autocomplete="off">
    </div>
    <div class="field">
      <label>目前進位（點選）</label>
      <div class="base-btns">
        <button type="button" class="base-btn active" onclick="setConvBase(this,'10')">十進位 (0-9)</button>
        <button type="button" class="base-btn" onclick="setConvBase(this,'2')">二進位 (0-1)</button>
        <button type="button" class="base-btn" onclick="setConvBase(this,'8')">八進位 (0-7)</button>
        <button type="button" class="base-btn" onclick="setConvBase(this,'16')">十六進位 (0-F)</button>
      </div>
      <input type="hidden" id="conv-base" value="10">
    </div>
  </div>
  <div class="conv-err" id="conv-err"></div>
  <div class="conv-out" id="conv-out">
    <div class="conv-cell"><div class="k">二進位 BIN₂</div><div class="v" id="out-2">—</div></div>
    <div class="conv-cell"><div class="k">八進位 OCT₈</div><div class="v" id="out-8">—</div></div>
    <div class="conv-cell"><div class="k">十進位 DEC₁₀</div><div class="v" id="out-10">—</div></div>
    <div class="conv-cell"><div class="k">十六進位 HEX₁₆</div><div class="v" id="out-16">—</div></div>
  </div>
</div>'''

BODIES["unit02"] = hero("unit02") + goals([
    "認識生活中常見的各種進位系統及其應用",
    "熟悉 2 / 8 / 10 / 16 進位的可用數字與表示方式",
    "學會十進位與其他進位互相轉換的方法",
    "能進行二進位的加法與減法運算",
]) + sec(1, "生活中的進位系統", '''
<p>世界上只有 10 進位嗎？其實生活中處處是不同的進位系統。<strong>先想想看，再點一下右邊欄位看答案</strong>（右上角可一鍵全開）：</p>
''' + reveal_table(
    ["進位", "生活應用"],
    [
        ["2 進位", "電腦內部（0／1）、邏輯真假值（True／False）、電路開關（開／關）"],
        ["8 進位", "Linux 檔案權限（chmod 755）、早期電腦與迷你電腦"],
        ["16 進位", "記憶體位址、網頁色碼（#FF8800）、MAC 位址、Unicode 編碼（U+4E2D）"],
        ["12 進位", "一年 12 個月、時鐘鐘面、一打＝12 個、1 英尺＝12 英寸"],
        ["24 進位", "一天 24 小時、時區換算"],
        ["60 進位", "時間的分與秒、角度（1 度＝60 分＝3600 秒）"],
    ]) + '''
''') + sec(2, "各種數字系統的表示方式", '''
<div class="table-wrap">
<table class="center">
  <thead><tr><th>進位系統</th><th>英文</th><th>縮寫</th><th>可用的數字</th><th>逢幾進位</th></tr></thead>
  <tbody>
    <tr><td>十進位</td><td>decimal</td><td><code>dec</code></td><td>0 1 2 3 4 5 6 7 8 9</td><td>逢 10 進 1</td></tr>
    <tr><td>二進位</td><td>binary</td><td><code>bin</code></td><td>0 1</td><td>逢 2 進 1</td></tr>
    <tr><td>八進位</td><td>octal</td><td><code>oct</code></td><td>0 1 2 3 4 5 6 7</td><td>逢 8 進 1</td></tr>
    <tr><td>十六進位</td><td>hexadecimal</td><td><code>hex</code></td><td>0 1 2 3 4 5 6 7 8 9 A B C D E F</td><td>逢 16 進 1</td></tr>
  </tbody>
</table>
</div>
''' + bit_bulbs("bitb-bases", bases=True, note="🔢 <b>從 0 一路數到 255</b>（8 顆燈泡＝8 位元，共 2⁸ = 256 種；一直按「＋1」或按「自動」）：同一個數字，四種進位怎麼寫，一次看清楚。") + '''
<div class="callout"><span class="t">📺 延伸影片＆冷知識</span>
<p style="margin:0 0 8px"><a class="vidlink" href="https://www.youtube.com/shorts/0jXjPgjJFXQ" target="_blank" rel="noopener">▶ 機關二進位（看二進位怎麼「數」）↗</a></p>
<div class="reveal" onclick="toggleWork(this)"><span class="wk-arrow">▶</span> 💡 冷知識：八卦 與二進位，驚人的相似？</div>
<div class="answer">
<p>三千年前《易經》的<strong>八卦</strong>，用「陰爻 ⚋」和「陽爻 ⚊」兩種符號、每卦疊三層，剛好排出 2³ = <strong>8 種</strong>卦象——這其實就跟電腦用 <strong>0 和 1</strong> 兩種狀態組合資料的想法一模一樣。十七世紀的數學家<strong>萊布尼茲（Leibniz）</strong>看到八卦時大為驚訝，因為它和他正在研究的<strong>二進位</strong>不謀而合。</p>
<p style="margin-bottom:0"><a class="vidlink" href="https://www.youtube.com/shorts/hTtUzqN7euQ" target="_blank" rel="noopener">▶ 看短片：八卦 與二進位 驚人的相似？↗</a></p>
</div></div>
<div class="callout"><span class="t">🔎 如何區辨不同進位？</span>
<p>常用<strong>下標</strong>或<strong>英文簡寫</strong>來標示，例如：</p>
<ul class="tidy">
  <li>二進位　→　下標 <code>2</code>　或　<code>bin</code>　，例如 <code>1101₂</code></li>
  <li>八進位　→　下標 <code>8</code>　或　<code>oct</code>　，例如 <code>17₈</code></li>
  <li>十六進位　→　下標 <code>16</code>　或　<code>hex</code>　，例如 <code>3A₁₆</code></li>
</ul>
<p style="margin-bottom:0">這些縮寫也正是 Python 內建函式的名稱（<code>bin()</code>、<code>oct()</code>、<code>hex()</code>）。</p></div>
''') + sec(3, "十進位 → 其他進位（除法取餘）", '''
<p><strong>整數部份：</strong>將十進位整數<strong>連除以該進位</strong>，直到商數為 0，再<strong>從下往上</strong>依序取出餘數。</p>
<p><strong>小數部份：</strong>將十進位小數<strong>連乘以該進位</strong>，直到適當位數為止，<strong>從上往下</strong>依序取整數部份。</p>
<div class="grid cols-2">
  <div class="card"><h3>例：92 → 二進位</h3>
  ''' + code_block("""92 ÷ 2 = 46 ... 餘 0  ↑
46 ÷ 2 = 23 ... 餘 0  |
23 ÷ 2 = 11 ... 餘 1  | 由下
11 ÷ 2 =  5 ... 餘 1  | 往上
 5 ÷ 2 =  2 ... 餘 1  | 讀取
 2 ÷ 2 =  1 ... 餘 0  |
 1 ÷ 2 =  0 ... 餘 1  |
結果：92 = 1011100₂""", lang="text", label="除法取餘", copy=False) + '''
  </div>
  <div class="card"><h3>更多練習答案</h3>
  <p style="color:var(--text-faint);font-size:.9rem">先自己算算看，再點一下答案格對答案（或按右上角「一鍵全開」）：</p>
  ''' + reveal_table(["十進位", "轉換目標", "答案（點一下看）"], [["92", "二進位", "1011100₂"], ["108", "二進位", "1101100₂"], ["0.453125", "二進位", "0.011101₂"], ["0.21875", "二進位", "0.00111₂"], ["108", "八進位", "134₈"], ["108", "十六進位", "6C₁₆"]], reveal_col=2) + '''
  </div>
</div>
''') + sec(4, "其他進位 → 十進位（位值展開）", '''
<p>方法：將每一位數<strong>分別乘以其位值</strong>（基底的次方），再全部加起來。<br><span style="color:var(--text-faint);font-size:.9rem">👆 教學用：點一下算式會逐步高亮——先亮整個數字，再一位一位對到它的位值，最後全部亮起（預設不上色，可一直點循環）。</span></p>
''' + '''<div class="pv-exp" onclick="pvStep(this)" data-step="0" data-max="10"><div class="pv-line"><span data-lit="1 2 10">1</span><span data-lit="1 3 10">0</span><span data-lit="1 4 10">0</span><span data-lit="1 5 10">1</span><span data-lit="1 6 10">1</span><span data-lit="1 7 10">0</span><span data-lit="1 8 10">0</span><span data-lit="1 9 10">1</span>₂ = <span data-lit="2 10">1</span>×2⁷ + <span data-lit="3 10">0</span>×2⁶ + <span data-lit="4 10">0</span>×2⁵ + <span data-lit="5 10">1</span>×2⁴ + <span data-lit="6 10">1</span>×2³ + <span data-lit="7 10">0</span>×2² + <span data-lit="8 10">0</span>×2¹ + <span data-lit="9 10">1</span>×2⁰ = 128 + 16 + 8 + 1 = <b>153</b></div><div class="pv-hint">👆 點一下逐步講解</div></div>
<div class="pv-exp" onclick="pvStep(this)" data-step="0" data-max="5"><div class="pv-line"><span data-lit="1 2 5">3</span><span data-lit="1 3 5">4</span><span data-lit="1 4 5">7</span>₈ = <span data-lit="2 5">3</span>×8² + <span data-lit="3 5">4</span>×8¹ + <span data-lit="4 5">7</span>×8⁰ = 192+32+7 = <b>231</b></div><div class="pv-hint">👆 點一下逐步講解</div></div>
<div class="pv-exp" onclick="pvStep(this)" data-step="0" data-max="5"><div class="pv-line"><span data-lit="1 2 5">A</span><span data-lit="1 3 5">5</span><span data-lit="1 4 5">1</span>₁₆ = <span data-lit="2 5">10</span>×16² + <span data-lit="3 5">5</span>×16¹ + <span data-lit="4 5">1</span>×16⁰ = 2560+80+1 = <b>2641</b></div><div class="pv-hint">👆 點一下逐步講解</div></div>'''
) + sec(5, "2 / 8 / 16 進位互換", '''
<div class="grid cols-2">
  <div class="card"><h3>二進位 ↔ 八進位</h3>
  <p>二進位由<strong>右向左每 3 位</strong>一組（3 位二進位＝1 位八進位）。</p>
  ''' + '''<div class="pv-exp" onclick="pvStep(this)" data-step="0" data-max="5"><div class="pv-line"><span data-lit="1 2 5">1</span><span data-lit="1 2 5">0</span><span data-lit="1 3 5">0</span><span data-lit="1 3 5">1</span><span data-lit="1 3 5">1</span><span data-lit="1 4 5">0</span><span data-lit="1 4 5">0</span><span data-lit="1 4 5">1</span>₂
→ <span data-lit="2 5">0</span><span data-lit="2 5">1</span><span data-lit="2 5">0</span> / <span data-lit="3 5">0</span><span data-lit="3 5">1</span><span data-lit="3 5">1</span> / <span data-lit="4 5">0</span><span data-lit="4 5">0</span><span data-lit="4 5">1</span>
→  <span data-lit="2 5">2</span>  /  <span data-lit="3 5">3</span>  /  <span data-lit="4 5">1</span> 
= <span data-lit="2 5">2</span><span data-lit="3 5">3</span><span data-lit="4 5">1</span>₈</div><div class="pv-hint">👆 點一下逐步講解</div></div>''' + '''
  </div>
  <div class="card"><h3>二進位 ↔ 十六進位</h3>
  <p>二進位由<strong>右向左每 4 位</strong>一組（4 位二進位＝1 位十六進位）。</p>
  ''' + '''<div class="pv-exp" onclick="pvStep(this)" data-step="0" data-max="4"><div class="pv-line"><span data-lit="1 2 4">1</span><span data-lit="1 2 4">1</span><span data-lit="1 2 4">0</span><span data-lit="1 2 4">0</span><span data-lit="1 3 4">1</span><span data-lit="1 3 4">0</span><span data-lit="1 3 4">0</span><span data-lit="1 3 4">1</span>₂
→ <span data-lit="2 4">1</span><span data-lit="2 4">1</span><span data-lit="2 4">0</span><span data-lit="2 4">0</span> / <span data-lit="3 4">1</span><span data-lit="3 4">0</span><span data-lit="3 4">0</span><span data-lit="3 4">1</span>
→  <span data-lit="2 4">C</span>   /  <span data-lit="3 4">9</span>  
= <span data-lit="2 4">C</span><span data-lit="3 4">9</span>₁₆</div><div class="pv-hint">👆 點一下逐步講解</div></div>''' + '''
  </div>
</div>
''') + sec(6, "二進位加減運算", '''
<div class="grid cols-2">
<div class="card"><h3>加法法則</h3>
<div class="table-wrap"><table class="truth"><tbody>
<tr><td>0 + 0 = 0</td></tr><tr><td>0 + 1 = 1</td></tr>
<tr><td>1 + 0 = 1</td></tr><tr><td>1 + 1 = <strong>10</strong>（進位）</td></tr>
</tbody></table></div>
</div>
<div class="card"><h3>減法法則</h3>
<div class="table-wrap"><table class="truth"><tbody>
<tr><td>0 − 0 = 0</td></tr><tr><td>1 − 0 = 1</td></tr>
<tr><td>1 − 1 = 0</td></tr><tr><td>0 − 1 = 1（<strong>借位</strong>）</td></tr>
</tbody></table></div>
</div>
</div>
<div class="callout"><span class="t">✋ 「借位」是什麼意思？</span>
<p>當某一位<strong>不夠減</strong>（例如 <code>0 − 1</code>）時，就要向<strong>左邊更高的一位「借 1」</strong>。</p>
<ul class="tidy">
  <li>在二進位裡，借來的這個 1 到了低位就相當於 <strong>2</strong>，所以 <code>0 − 1</code> 變成 <code>2 − 1 = 1</code>。</li>
  <li>被借的那一位，記得要<strong>減掉 1</strong>。</li>
</ul>
<p style="margin-bottom:0">道理和十進位一樣：十進位 <code>10 − 1</code> 時，個位向十位借 1（借來的 1＝10），變成 <code>10 − 1 = 9</code>。</p></div>
''' + '''<div style="display:flex;gap:22px;flex-wrap:wrap;align-items:flex-start"><div style="flex:1;min-width:150px">''' + code_block("  1010₂\n+ 0011₂\n------\n  1101₂", lang="text", label="二進位加法", copy=False) + '''</div><div style="flex:1;min-width:150px">''' + code_block("  1101₂\n- 0011₂\n------\n  1010₂", lang="text", label="二進位減法", copy=False) + '''</div></div>''' + '''
<div class="callout tip"><span class="t">💡 提示</span><p>八進位、十六進位的加減同理，只是「逢 8 進 1」「逢 16 進 1」。</p></div>
''') + exercise("課堂練習", '''
<ol>
  <li>將十進位 <strong>200</strong> 轉換成二進位、八進位與十六進位。</li>
  <li>將 <strong>11010110₂</strong> 轉換成十進位與十六進位。</li>
  <li>計算 <strong>1011₂ + 1101₂</strong>（結果以二進位表示）。</li>
  <li>色碼 <code>#1E90FF</code> 中的 <strong>1E</strong>（十六進位）等於十進位多少？</li>
</ol>''', '''
<ol>
<li>200 = 11001000₂ = 310₈ = C8₁₆</li>
<li>11010110₂ = 214₁₀ = D6₁₆</li>
<li>1011₂ + 1101₂ = 11000₂（＝24₁₀）</li>
<li>1E₁₆ = 1×16 + 14 = 30₁₀</li>
</ol>
<p style="color:var(--text-faint)">算完後，可用頁面最下方「課堂互動工具」的進位轉換器對答案！</p>''')

# =====================================================================
# 單元 03：資料運算與儲存
# =====================================================================
_gate_widget = '''
<div class="widget">
  <div class="w-title">🔌 邏輯閘互動實驗</div>
  <div class="w-sub">選擇一個邏輯閘，點擊開關切換 A、B 的 0/1，即時看到輸出結果。</div>
  <div class="gate-btns">
    <button onclick="setGate('AND', this)">AND</button>
    <button onclick="setGate('OR', this)">OR</button>
    <button onclick="setGate('XOR', this)">XOR</button>
    <button onclick="setGate('NOT', this)">NOT</button>
    <button onclick="setGate('NAND', this)">NAND</button>
    <button onclick="setGate('NOR', this)">NOR</button>
  </div>
  <div class="switch-row">
    <div class="switch"><span class="lbl">輸入 A</span>
      <div class="sw-row">
        <button class="toggle" id="sw-a" onclick="flipSwitch('a')" aria-label="切換輸入 A"></button>
        <span class="sw-val" id="val-a">0</span>
      </div></div>
    <div class="switch" id="sw-b-wrap"><span class="lbl">輸入 B</span>
      <div class="sw-row">
        <button class="toggle" id="sw-b" onclick="flipSwitch('b')" aria-label="切換輸入 B"></button>
        <span class="sw-val" id="val-b">0</span>
      </div></div>
  </div>
  <div class="gate-result">
    <span class="eq" id="gate-eq">0 AND 0 =</span>
    <span class="out v0" id="gate-out">0</span>
  </div>
</div>'''

BODIES["unit03"] = hero("unit03") + goals([
    "理解 AND / OR / XOR / NOT 邏輯運算與真值表",
    "認識半加器與全加器的運作",
    "熟悉資料儲存單位與圖像、音檔容量的計算",
    "分辨類比訊號與數位訊號，了解資料傳輸方式",
]) + sec(1, "邏輯運算與邏輯閘", '''
<p>邏輯閘是數位電路中最基本的元件，用來實現邏輯運算。</p>
<div class="callout tip"><span class="t">🔦 先用「開關」來想：邏輯閘是怎麼來的</span>
<p>邏輯閘聽起來很抽象，其實可以先想成<strong>電燈開關</strong>：<strong>通（1）＝ 電流過得去、斷（0）＝ 過不去</strong>。把開關<strong>接的方式</strong>換一換，就得到不同的邏輯閘——</p>
<div class="grid cols-3 sw2gate">
  <div class="card"><h3>串聯 ＝ AND</h3>
  <div class="diagram-card">''' + switch_logic("series") + '''</div>
  <p>兩個開關<strong>「串聯」</strong>（一個接一個）：<strong>A、B 都通(1)，燈才亮</strong>。只要有一個沒通就滅 → 這就是 <strong>AND</strong>。</p>
  <div class="diagram-card">''' + gate_svg("AND") + '''</div></div>
  <div class="card"><h3>並聯 ＝ OR</h3>
  <div class="diagram-card">''' + switch_logic("parallel") + '''</div>
  <p>兩個開關<strong>「並聯」</strong>（各走各的）：<strong>只要有一個通(1)，燈就亮</strong> → 這就是 <strong>OR</strong>。</p>
  <div class="diagram-card">''' + gate_svg("OR") + '''</div></div>
  <div class="card"><h3>反相 ＝ NOT</h3>
  <div class="diagram-card">''' + gate_svg("NOT") + '''</div>
  <p>把訊號<strong>「反過來」</strong>：<strong>進 1 出 0、進 0 出 1</strong> → 這就是 <strong>NOT</strong>（反閘）。</p></div>
</div>
<p style="margin:6px 0 0">有了這個「開關」的直覺，下面再看正式的<strong>符號</strong>和<strong>真值表</strong>就會清楚很多 👇</p></div>
<p>以下是四種基本邏輯閘的符號與真值表：</p>
<div class="grid cols-2">
  <div class="card"><h3>AND（及閘，邏輯「與」）</h3>
  <p>兩個輸入<strong>都是 1</strong> 時輸出才是 1。</p>
  <div class="diagram-card">''' + gate_svg("AND") + '''</div>
  <div class="table-wrap"><table class="truth"><thead><tr><th>A</th><th>B</th><th>A AND B</th></tr></thead>
  <tbody><tr><td>0</td><td>0</td><td>0</td></tr><tr><td>0</td><td>1</td><td>0</td></tr>
  <tr><td>1</td><td>0</td><td>0</td></tr><tr><td>1</td><td>1</td><td>1</td></tr></tbody></table></div>
  </div>
  <div class="card"><h3>OR（或閘，邏輯「或」）</h3>
  <p>只要有<strong>一個輸入是 1</strong> 就輸出 1。</p>
  <div class="diagram-card">''' + gate_svg("OR") + '''</div>
  <div class="table-wrap"><table class="truth"><thead><tr><th>A</th><th>B</th><th>A OR B</th></tr></thead>
  <tbody><tr><td>0</td><td>0</td><td>0</td></tr><tr><td>0</td><td>1</td><td>1</td></tr>
  <tr><td>1</td><td>0</td><td>1</td></tr><tr><td>1</td><td>1</td><td>1</td></tr></tbody></table></div>
  </div>
  <div class="card"><h3>XOR（互斥或閘）</h3>
  <p>兩個輸入<strong>不同</strong>時輸出 1，相同時輸出 0。</p>
  <div class="diagram-card">''' + gate_svg("XOR") + '''</div>
  <div class="table-wrap"><table class="truth"><thead><tr><th>A</th><th>B</th><th>A XOR B</th></tr></thead>
  <tbody><tr><td>0</td><td>0</td><td>0</td></tr><tr><td>0</td><td>1</td><td>1</td></tr>
  <tr><td>1</td><td>0</td><td>1</td></tr><tr><td>1</td><td>1</td><td>0</td></tr></tbody></table></div>
  </div>
  <div class="card"><h3>NOT（反相器 / 反閘，邏輯「非」）</h3>
  <p>把輸入<strong>反過來</strong>：0 變 1、1 變 0。</p>
  <div class="diagram-card">''' + gate_svg("NOT") + '''</div>
  <div class="table-wrap"><table class="truth"><thead><tr><th>A</th><th>NOT A</th></tr></thead>
  <tbody><tr><td>0</td><td>1</td></tr><tr><td>1</td><td>0</td></tr></tbody></table></div>
  </div>
</div>
''') + sec(2, "加法器", '''
<p>加法器是執行加法運算的數位電路，是 CPU 中算術邏輯單元（ALU）的基礎。</p>
<div class="grid cols-2">
  <div class="card"><h3>半加器 Half Adder</h3>
  <p>兩個輸入 A、B，輸出<strong>和 S</strong> 與<strong>進位 C</strong>。（S＝A XOR B，C＝A AND B）</p>
  ''' + local_img("images/half_adder.png", "半加器邏輯電路圖：一個 XOR 閘產生和 S、一個 AND 閘產生進位 C",
                  "半加器電路：XOR → 和 S；AND → 進位 C。") + '''
  <div class="table-wrap"><table class="truth"><thead><tr><th>A</th><th>B</th><th>C</th><th>S</th></tr></thead>
  <tbody><tr><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>0</td><td>1</td><td>0</td><td>1</td></tr>
  <tr><td>1</td><td>0</td><td>0</td><td>1</td></tr><tr><td>1</td><td>1</td><td>1</td><td>0</td></tr></tbody></table></div>
  </div>
  <div class="card"><h3>全加器 Full Adder</h3>
  <p>多了一個<strong>進位輸入 Cin</strong>，可串接處理多位元加法。</p>
  ''' + local_img("images/full_adder.png", "全加器邏輯電路圖：由兩個 XOR、兩個 AND 與一個 OR 閘組成",
                  "全加器電路：兩個 XOR 求和 S、兩個 AND 加一個 OR 求進位 Cout。") + '''
  <div class="table-wrap"><table class="truth"><thead><tr><th>A</th><th>B</th><th>Cin</th><th>Cout</th><th>S</th></tr></thead>
  <tbody>
  <tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr>
  <tr><td>0</td><td>0</td><td>1</td><td>0</td><td>1</td></tr>
  <tr><td>0</td><td>1</td><td>0</td><td>0</td><td>1</td></tr>
  <tr><td>0</td><td>1</td><td>1</td><td>1</td><td>0</td></tr>
  <tr><td>1</td><td>0</td><td>0</td><td>0</td><td>1</td></tr>
  <tr><td>1</td><td>0</td><td>1</td><td>1</td><td>0</td></tr>
  <tr><td>1</td><td>1</td><td>0</td><td>1</td><td>0</td></tr>
  <tr><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr>
  </tbody></table></div>
  </div>
</div>
''') + sec(3, "資料儲存的單位", '''
<p>電腦中最基本的儲存單位是<strong>位元 (bit)</strong>，只能存 0 或 1；最小的資料儲存單位是<strong>位元組 (Byte)</strong>。</p>
''' + bit_bulbs("bitb-byte", bases=False, note="一顆燈泡＝一個 bit（亮＝1、暗＝0）。<b>8 顆燈泡就是 1 個位元組（Byte）</b>——按按鈕從 00000000 一路數到 11111111，共 2⁸ = <b>256</b> 種。") + '''
<div class="callout"><span class="t">1 Byte = 8 bits = 2⁸ = 256 種狀態</span>
<p>1 個位元組可以用來儲存 1 個英文字母、數字或特殊符號（ASCII 編碼）。</p></div>
<div style="display:flex;gap:34px;flex-wrap:wrap;justify-content:center">
<table class="unit-table"><thead><tr><th>單位</th><th>換算</th></tr></thead><tbody>
<tr><td>1 KB</td><td>= 1024 Byte</td></tr>
<tr><td>1 MB</td><td>= 1024 KB</td></tr>
<tr><td>1 GB</td><td>= 1024 MB</td></tr>
<tr><td>1 TB</td><td>= 1024 GB</td></tr>
</tbody></table>
<table class="unit-table"><thead><tr><th>單位</th><th>換算</th></tr></thead><tbody>
<tr><td>1 PB</td><td>= 1024 TB</td></tr>
<tr><td>1 EB</td><td>= 1024 PB</td></tr>
<tr><td>1 ZB</td><td>= 1024 EB</td></tr>
<tr><td>1 YB</td><td>= 1024 ZB</td></tr>
</tbody></table>
</div>
''') + sec(4, "圖像與音檔容量計算", '''
<div class="card"><h3>🖼️ 圖像檔案大小</h3>
<p>數位圖像其實是由一格一格的<strong>像素（點）</strong>組成的。放大來看就像下面這張明道校徽——每一格都是一個像素：</p>
<div class="part">
''' + local_img("images/mingdao_pixel_labeled.png",
                "明道中學校徽以 32×32 像素方格呈現，標示寬 32、高 32 像素",
                "把明道校徽縮成寬 32、高 32：共 32 × 32 = 1024 個像素，每一格就是一個像素，都要用位元記錄它的顏色。",
                bg="#fff") + '''
  <div>
    <p><strong>圖像儲存空間<br>＝ 圖像高(點) × 圖像寬(點) × 像素深度(位元組)</strong></p>
    <p>像素深度看<strong>色彩模式</strong>——顏色越多，每個像素要用越多位元來記錄。</p>
  </div>
</div>
<div class="table-wrap"><table class="center">
<thead><tr><th>色彩模式</th><th>可表示的顏色數</th><th>每個像素需要</th></tr></thead>
<tbody>
<tr><td>單色</td><td>2 色（黑／白）</td><td>1 bit</td></tr>
<tr><td>16 色</td><td>2⁴ ＝ 16 色</td><td>4 bit</td></tr>
<tr><td>256 色</td><td>2⁸ ＝ 256 色</td><td>8 bit（＝ 1 Byte）</td></tr>
<tr><td><strong>全彩 True Color</strong></td><td>2²⁴ ≈ 1677 萬色</td><td><strong>24 bit（＝ 3 Byte，RGB 各 8 bit）</strong></td></tr>
</tbody></table></div>
''' + code_block("""例：寬 10 公分、高 8 公分、解析度 28 點/公分、全彩儲存
高(點) = 8 × 28 = 224
寬(點) = 10 × 28 = 280
所需空間 = 224 × 280 × (24 / 8)
        = 224 × 280 × 3
        = 188160 bytes""", lang="text", label="圖像計算範例", copy=False) + '''
</div>
<div class="card"><h3>🎵 音檔大小</h3>
<p>聲音是連續的類比波形，電腦要每隔固定時間「取樣」一次，把振幅記成數字，才能變成數位音檔：</p>
<div class="diagram-card">''' + audio_wave() + '''</div>
<p><strong>資料量 = 取樣頻率 × 取樣位數 × 聲道數 × 時間 ÷ 8</strong></p>
''' + code_block("""例：5 分鐘、雙聲道、16 位取樣、44.1 kHz、不壓縮
= 44100 × 16 × 2 × (5×60) ÷ 8 ÷ 1024 ÷ 1024
≈ 50.47 MB""", lang="text", label="音檔計算", copy=False) + '''
</div>
''') + sec(5, "類比訊號 vs 數位訊號", '''
<div class="grid cols-2">
  <div class="tile"><h4>🌊 類比訊號</h4>
  <div class="diagram-card">''' + analog_vs_digital()[0] + '''</div>
  <p>連續值，大自然的訊號都屬於類比（聲音、光、溫度、壓力）。<strong>缺點：容易被雜訊影響而失真</strong>，長距離傳輸或多次複製尤其明顯。</p></div>
  <div class="tile"><h4>💠 數位訊號</h4>
  <div class="diagram-card">''' + analog_vs_digital()[1] + '''</div>
  <p>不連續值，以二進位 0/1 表示（0＝低電位、1＝高電位）。<strong>優點：容易處理</strong>——儲存、傳輸、壓縮、加密、偵錯都方便。</p></div>
</div>
''') + sec(6, "資料傳輸方式", '''
<h3>依傳輸方向分類</h3>
<div class="grid cols-3">
  <div class="diagram-card">''' + transmission("simplex") + '''<div class="tx-desc"><div class="tx-name">單工 Simplex</div><div>只能單向傳送</div><div class="tx-eg">🔊 生活實例：AM/FM 廣播、喇叭播放</div></div></div>
  <div class="diagram-card">''' + transmission("half") + '''<div class="tx-desc"><div class="tx-name">半雙工 Half-duplex</div><div>可雙向，但同時只能單向</div><div class="tx-eg">📻 生活實例：無線電對講機</div></div></div>
  <div class="diagram-card">''' + transmission("full") + '''<div class="tx-desc"><div class="tx-name">全雙工 Full-duplex</div><div>同時可雙向傳輸</div><div class="tx-eg">📞 生活實例：電話、通訊軟體聊天</div></div></div>
</div>

<h3>基頻與寬頻、交換方式</h3>
<ul class="tidy">
  <li><strong>基頻 (baseband)</strong>：以<strong>數位</strong>方式直接傳送，一次傳送一個訊號、佔用整個媒介（例如區域網路 LAN）。</li>
  <li><strong>寬頻 (broadband)</strong>：以<strong>類比載波調變、分頻多工</strong>，可同時傳送多個訊號／頻道（例如有線電視 Cable）。</li>
</ul>
<div class="callout warn"><span class="t">⚠ 容易混淆：學術定義 vs 日常用語</span>
<p>上面是<strong>教科書/考試</strong>的定義（寬頻＝類比多工）。但日常說的「<strong>寬頻上網</strong>」（光纖、ADSL、第四台網路）是指「<strong>高速的網路存取服務</strong>」，本身其實是<strong>數位</strong>傳輸——這是口語用法，著重「速度快」，和學術上「寬頻＝類比」的意義不同，兩者不要混為一談。</p></div>
<p><strong>電路交換</strong>建立專用實體線路（速度快、錯誤率低，但不共用頻寬）；<strong>訊息交換</strong>先儲存再轉送、可選路徑（線路使用率高，但大量資料時易壅塞）。</p>

<div style="margin-top:30px;padding-top:14px;border-top:2px solid var(--brand)">
  <span style="font-size:1.35rem;font-weight:800;color:var(--brand-strong)">🌐 網路速度</span>
</div>
<h3>計算網路速度：下載檔案要多久？</h3>
<p>網路速率的單位是 <strong>bps（每秒位元數）</strong>，檔案大小的單位是 <strong>Byte（位元組）</strong>，換算時<strong>別忘了 1 Byte = 8 bits</strong>。</p>
''' + code_block("""基本例：網路速率 2 Mbps，傳送 150 MB 檔案需多久？
150 MB = 150 × 1024 × 1024 × 8 bits = 1,258,291,200 bits
時間 = 1,258,291,200 ÷ 2,000,000 ≈ 629 秒 ≈ 10.5 分鐘""", lang="text", label="範例一", copy=False) + '''
<p>換個生活情境：假設你家是<strong>中華電信 100M 光纖</strong>（下載 100 Mbps），要下載《俠盜獵車手 6》（GTA 6，假設檔案 <strong>150 GB</strong>），理想狀況下要多久？</p>
''' + code_block("""生活例：中華電信 100M（100 Mbps）下載 GTA 6（150 GB）
檔案大小 = 150 GB
        = 150 × 1024 × 1024 × 1024 Bytes
        = 150 × 1024 × 1024 × 1024 × 8 bits
        ≈ 1,288,490,188,800 bits

下載速率 = 100 Mbps = 100 × 1,000,000 = 100,000,000 bps

時間 = 1,288,490,188,800 ÷ 100,000,000
     ≈ 12,885 秒
     ≈ 214.7 分鐘
     ≈ 約 3.6 小時

※ 這是「理論最快」值。實際上還會受到伺服器速度、
   線路壅塞、Wi-Fi 訊號等影響，通常會更久。""", lang="text", label="範例二：中華電信 100M 下載 GTA 6", copy=False) + '''
<div class="reveal" onclick="toggleWork(this)"><span class="wk-arrow">▶</span> 💡 小提示：為什麼有時候 GB 好像不是 1024？</div>
<div class="answer">
<p>其實「1 GB」有<strong>兩種算法</strong>，這就是混亂的來源：</p>
<ul class="tidy">
<li><strong>二進位（每級 ×1024）</strong>：1 GB＝1024 MB＝1024×1024 KB…，正式名稱其實叫 <strong>GiB</strong>（Gibibyte）。電腦內部、Windows、Steam 都用這種算。</li>
<li><strong>十進位（每級 ×1000）</strong>：1 GB＝1000 MB…，硬碟廠商、網路速率、蘋果 macOS 用的是這種。</li>
</ul>
<p>麻煩的是：大家畫面上都寫「GB」，但有人心裡是 1024、有人是 1000，數字自然對不起來。三個最常見的例子：</p>
<ol class="tidy">
<li><strong>Windows／Steam ＶＳ macOS</strong>：Windows 和 Steam 骨子裡用 1024（其實是 GiB）算容量，畫面卻寫「GB」；蘋果 macOS 從 2009 年起改成「畫面寫 GB 就是真的 1000」。所以同一個檔案，在 Windows 和 Mac 上顯示的數字會不一樣。</li>
<li><strong>買硬碟／隨身碟</strong>：包裝寫「1 TB＝1000 GB」（廠商用 1000），插上 Windows 後系統改用 1024 去算、單位又還是寫「GB」，於是 1,000,000,000,000 Bytes 就變成畫面上看到的 <strong>931 GB</strong>。硬碟沒有縮水，只是換算基準不同。</li>
<li><strong>雲端服務（Google Cloud、AWS、Azure）</strong>：規格書裡 GB（1000）和 GiB（1024）常常混用——記憶體用 GiB 算、網路流量或硬碟空間又用 GB，工程師估容量和費用時很容易搞錯。</li>
</ol>
<p style="margin-bottom:0"><strong>一句話記住：</strong>看到 GB，先想一下「這是 1024 的、還是 1000 的？」——電腦內部／Windows／Steam 多半是 1024（其實是 GiB）；硬碟包裝／網速／雲端流量多半是 1000。</p>
</div>
'''
) + exercise("課堂練習", '''
<ol>
  <li>先自己<strong>對照上面的邏輯閘符號與真值表</strong>，寫出 <strong>A=1, B=0</strong> 時 XOR 與 NAND 的輸出各是多少；寫完後，可再用頁面最下方「課堂互動工具」的邏輯閘實驗<strong>驗證答案</strong>。</li>
  <li>一張寬 15 公分、高 10 公分、解析度 30 點/公分的<strong>全彩</strong>圖片，先算出需要多少 bytes，再換算成 <strong>KB 與 MB</strong>（記得 1 KB＝1024 bytes、1 MB＝1024 KB）。</li>
  <li>1 GB 等於多少 Byte？（以 1024 換算）</li>
  <li>「使用 LINE 視訊通話」屬於單工、半雙工還是全雙工？</li>
</ol>''', '''
<ol>
<li>A=1,B=0：XOR=1、NAND=1。</li>
<li>高(點)=10×30=300，寬(點)=15×30=450，全彩每點 3 bytes。<br>
→ 300 × 450 × 3 = <strong>405,000 bytes</strong><br>
→ 405,000 ÷ 1024 ≈ <strong>395.5 KB</strong><br>
→ 395.5 ÷ 1024 ≈ <strong>0.39 MB</strong>（約 0.4 MB）</li>
<li>1 GB = 1024×1024×1024 = 1,073,741,824 Byte。</li>
<li>全雙工（雙方可同時收發）。</li>
</ol>''')

# =====================================================================
# 單元 04：電腦簡介（發展史與種類）
# =====================================================================
BODIES["unit04"] = hero("unit04") + goals([
    "認識計算機從機械式到電子式的發展歷程",
    "了解四個世代電腦的關鍵元件與特色",
    "認識摩爾定律及其對晶片發展的影響",
    "分辨超級電腦、大型電腦、工作站、個人電腦與嵌入式電腦",
]) + sec(1, "計算機的歷史", '''
<div class="grid cols-2">
  <div class="tile"><h4>🧮 算盤</h4>''' + wm_thumb("Chinese Suanpan Abacus.jpg", "中國算盤（算珠計算工具）") + '''<p>三千多年前中國人發明，是人類最早的機械計算設備之一。</p></div>
  <div class="tile"><h4>➕ 巴斯卡計算機（1642）</h4>''' + wm_thumb("Blaise pascal.jpg", "巴斯卡 Blaise Pascal 畫像") + '''<p>法國數學家<strong>巴斯卡（Blaise Pascal）</strong>發明機械計算器，可直接做加減運算。</p></div>
  <div class="tile"><h4>🧵 打孔卡織布機（1801）</h4>''' + wm_thumb("A la mémoire de J.M. Jacquard.jpg", "雅卡爾 Joseph Marie Jacquard 織像（用他發明的織布機織成）") + '''<p><strong>雅卡爾（Joseph Marie Jacquard）</strong>用打孔卡控制織布機，帶來「資訊可編碼」與「卡片可當程式指令」兩個重要概念。（這張人像其實就是用他發明的織布機「織」出來的）</p></div>
  <div class="tile"><h4>⚙️ 差分機／分析機（1833）</h4>''' + wm_thumb("Charles Babbage 1860.jpg", "巴貝奇 Charles Babbage 照片") + '''<p>英國數學家<strong>巴貝奇（Charles Babbage）</strong>的設計概念與現代電腦極相似，被尊稱為「<strong>電腦之父</strong>」。</p></div>
  <div class="tile"><h4>🗳️ 何樂禮普查機（1890）</h4>''' + wm_thumb("Hollerith.jpg", "何樂禮 Herman Hollerith 照片") + '''<p>由<strong>何樂禮（Herman Hollerith）</strong>設計，以打孔卡儲存資料、電力驅動，協助美國人口普查，把耗時 10 年的工作縮短到 1 年。</p></div>
  <div class="tile"><h4>💡 內儲程式（1945）</h4>''' + wm_thumb("JohnvonNeumann-LosAlamos.jpg", "范紐曼 John von Neumann 照片") + '''<p><strong>范紐曼（John von Neumann，另譯 馮·諾伊曼）</strong>提出把程式全部儲存在電腦內部的概念，開啟「內儲程式」的先河。</p></div>
</div>
''') + sec(2, "四個世代的電腦", '''
<div class="table-wrap"><table>
<thead><tr><th>世代</th><th>關鍵元件</th><th>年代</th><th>特色</th></tr></thead>
<tbody>
<tr><td>第一代</td><td><strong>真空管</strong></td><td>1946～</td><td>ENIAC 第一台電子電腦，體積龐大、耗電高、易損壞</td></tr>
<tr><td>第二代</td><td><strong>電晶體</strong></td><td>1947～</td><td>比真空管小 20 倍、省電、故障率低，體積大幅縮小</td></tr>
<tr><td>第三代</td><td><strong>積體電路 (IC)</strong></td><td>1964～</td><td>IBM 360 代表，把多種元件整合在矽晶片上</td></tr>
<tr><td>第四代</td><td><strong>超大型積體電路 (VLSI)</strong></td><td>1972～</td><td>一晶片容納數千至數萬個元件，效能飛躍</td></tr>
</tbody></table></div>
<div class="callout"><span class="t">💡 這些元件怎麼變成 0 與 1？</span>
<p>家裡的電燈開關，要用<strong>「人的手指」</strong>去按，燈才會亮。但電腦裡有<strong>幾億個開關</strong>，人的手根本來不及一個一個去按——所以我們需要一種「<strong>不用人手、用電就能控制電</strong>」的魔法開關。真空管、電晶體就是這種<strong>「電子開關」</strong>：<strong>接通（電流過得去）＝ 1、斷開（電流過不去）＝ 0</strong>。</p>
<ul class="tidy">
  <li><strong>真空管：</strong>像一道需要<strong>「加熱」才會打開的門</strong>。給燈絲一點電去加熱，它產生的熱就會讓「大門」打開、放電流通過。缺點是體積大、耗電、容易燒壞。</li>
  <li><strong>電晶體：</strong>像一道<strong>「電子感應門」</strong>。只要在控制端給一點小小的電壓（就像刷一下感應卡），大門立刻打開、放電流通過。又小、又省電、又耐用，因此取代了真空管。</li>
  <li><strong>積體電路／VLSI：</strong>把幾百萬到幾百億個電晶體（開關）塞進一小片晶片，就成了現在的 CPU。</li>
</ul>
<p style="margin:10px 0 0">重點：它們的作用<strong>不是「自己發電」</strong>，而是扮演那隻<strong>「隱形的手」</strong>，用極快的速度去控制後面電路的<strong>通與不通</strong>——通就是 <strong>1</strong>，不通就是 <strong>0</strong>。</p>
<div class="swx" role="img" aria-label="電子開關示意動畫：開機供電後，控制端給電時開關接通、電流從供電經過燈與開關流到接地、燈亮為 1；控制端沒電時開關斷開、燈滅為 0">
  <div class="swx-row">
    <div class="swx-cell">
      <span class="swx-pwr"><svg class="swx-sym" viewBox="0 0 26 26" width="26" height="26" aria-hidden="true"><g fill="none" stroke="var(--brand)" stroke-width="2.4" stroke-linecap="round"><path d="M13 3.5 V12.5"/><path d="M7.7 6.6 A8 8 0 1 0 18.3 6.6"/></g></svg></span>
      <div class="swx-cap">供電（開機）<br><small>電流從這裡來</small></div>
    </div>
    <div class="swx-arrow swx-fa">➜</div>
    <div class="swx-cell swx-gcell">
      <div class="swx-ctrlbox"><span class="swx-ctrl">⚡</span><span class="swx-cdown">↓</span></div>
      <div class="swx-track">
        <div class="swx-wire"></div>
        <div class="swx-dots"><span class="swx-dot d1"></span><span class="swx-dot d2"></span><span class="swx-dot d3"></span></div>
        <span class="swx-door l"></span><span class="swx-door r"></span>
      </div>
      <div class="swx-cap">電子開關（電晶體）<br><small>控制端＝隱形的手</small></div>
    </div>
    <div class="swx-arrow swx-fa">➜</div>
    <div class="swx-cell">
      <div class="swx-bulb">💡</div>
      <div class="swx-num"><span class="one">1</span><span class="zero">0</span></div>
      <div class="swx-cap">燈（輸出）</div>
    </div>
    <div class="swx-arrow swx-fa">➜</div>
    <div class="swx-cell">
      <span class="swx-gnd"><svg class="swx-sym" viewBox="0 0 26 26" width="26" height="26" aria-hidden="true"><g fill="none" stroke="var(--text-faint)" stroke-width="2.2" stroke-linecap="round"><line x1="13" y1="3" x2="13" y2="12"/><line x1="4.5" y1="12" x2="21.5" y2="12"/><line x1="7.5" y1="17" x2="18.5" y2="17"/><line x1="10.5" y1="22" x2="15.5" y2="22"/></g></svg></span>
      <div class="swx-cap">接地<br><small>電流回到大地</small></div>
    </div>
  </div>
  <p class="swx-cap2">電腦一<b>開機（供電）</b>，電流就準備好從左邊流向右邊的<b>接地</b>。中間的開關由<b>控制端</b>（那隻「隱形的手」）決定通不通：控制端一<b>給電</b> → 開關接通、電流通過 → 燈亮 ＝ <b>1</b>；控制端<b>沒電</b> → 開關斷開、電流被擋 → 燈滅 ＝ <b>0</b>。</p>
</div></div>
<div class="callout tip"><span class="t">🔗 這種開關，就是拿來做邏輯閘的</span>
<p>還記得上一單元嗎？我們用開關的<strong>串聯＝AND、並聯＝OR、反相＝NOT</strong> 介紹過邏輯閘——這裡的真空管、電晶體，正是那種<strong>「電子開關」</strong>。整條脈絡是：<strong>電晶體（開關）→ 拼成邏輯閘（AND／OR／NOT）→ 再組成加法器、記憶體…… → 整台電腦</strong>。現在一顆 CPU 裡面，就是<strong>幾百億個這種開關</strong>在飛快地運算。</p></div>
<div class="grid cols-2">
''' + wm_img("Eniac (cropped).jpg",
             "第一代電腦 ENIAC，由大量真空管組成、佔滿整個房間",
             "第一代：ENIAC（1946），用真空管製造，體積龐大、耗電驚人。", width=560) + '''
''' + wm_img("Replica-of-first-transistor.jpg",
             "1947 年貝爾實驗室發明的第一顆電晶體複製品",
             "第二代：第一顆電晶體（1947，貝爾實驗室），比真空管小又省電。", width=560) + '''
</div>
<div class="callout"><span class="t">🔔 冷知識：電晶體與我們的前校長</span>
<p>把電腦推進第二代的<strong>電晶體</strong>，是 1947 年在美國<strong>貝爾實驗室（Bell Labs）</strong>發明的——這間實驗室誕生過無數改變世界的發明。</p>
<p style="margin-bottom:0">而我們明道的<strong>明道文教基金會汪董－汪大久（前校長）</strong>，當年也曾是<strong>貝爾實驗室的員工</strong>！
（<a href="https://www.google.com/search?q=%E6%B1%AA%E5%A4%A7%E4%B9%85+%E8%B2%9D%E7%88%BE%E5%AF%A6%E9%A9%97%E5%AE%A4" target="_blank" rel="noopener">搜尋：汪大久 貝爾實驗室</a>）</p></div>
<div class="callout tip"><span class="t">📈 摩爾定律 Moore's Law</span>
<p>1965 年<strong>高登·摩爾（Gordon Moore）</strong>提出：晶片上的電晶體數量約<strong>每兩年翻一倍</strong>。1971 年 Intel 4004 只有 2300 個電晶體，2023 年的 A16 晶片已達<strong>約 160 億個</strong>電晶體。</p>
<p style="margin-bottom:0">不過近年電晶體越做越小、逼近物理極限，摩爾定律的速度已<strong>明顯放緩</strong>，有人甚至說它「快走到盡頭」。</p></div>
<div class="diagram-card">''' + moore_huang() + '''</div>
<div class="callout"><span class="t">🚀 輝達定律 Huang's Law（黃氏定律）</span>
<p>以 NVIDIA 創辦人<strong>黃仁勳（Jensen Huang）</strong>命名。他指出：靠著 GPU 架構、軟體與製程的整體進步，<strong>GPU 用於 AI 的運算效能大約每年就翻倍</strong>，換算下來約<strong>十年提升 1000 倍</strong>——遠比摩爾定律（每兩年 2 倍）快得多。這也是為什麼 AI 這幾年進步這麼快。</p>
<p style="margin-bottom:0;font-size:.82rem;color:var(--text-faint)">來源：黃氏定律（維基百科）、《數位時代》《INSIDE》等報導；此為 NVIDIA 提出的觀察，非嚴格科學定律。</p></div>
''') + sec(3, "電腦的種類", '''
<div class="grid cols-2">
  <div class="tile">''' + wm_thumb("Frontier Supercomputer (3).jpg", "Frontier 超級電腦機櫃") + '''<h4>🖥️ 超級電腦</h4><p>處理速度最快，強調<strong>浮點運算</strong>。用於氣象預報、國防、太空研究（見 TOP500 榜單）。圖為美國橡樹嶺國家實驗室的 <strong>Frontier</strong>，全球首部突破每秒百億億次（Exascale）的超級電腦。</p></div>
  <div class="tile">''' + wm_thumb("IBM Z15 mainframe.jpg", "IBM z15 大型主機") + '''<h4>🏦 大型電腦</h4><p>傾向<strong>整數運算</strong>，重視安全性、可靠性與穩定性。用於銀行、訂單等海量交易資料。圖為 <strong>IBM z15</strong> 大型主機。</p></div>
  <div class="tile">''' + wm_thumb("Dell Precision T3500 Workstation - IPAS Research.jpeg", "Dell Precision 工作站") + '''<h4>🛠️ 工作站</h4><p>專注數學計算與圖形運算，常用於工程設計與科研分析。外型像高階個人電腦，但零件更專業、更耐操。</p></div>
  <div class="tile">''' + wm_thumb("Desktop personal computer.jpg", "桌上型個人電腦") + '''<h4>💻 個人電腦</h4><p>體積小、價格低、易用。桌機、筆電、平板皆屬之，是你我日常最常接觸的電腦。</p></div>
  <div class="tile">''' + wm_thumb("Arduino Uno - R3.jpg", "Arduino Uno 微控制板") + '''<h4>📟 嵌入式電腦</h4><p>藏在裝置裡的控制核心：機器人、智慧穿戴、汽車電子、智慧家電。圖為常見於自造課程的 <strong>Arduino</strong> 控制板。</p></div>
  <div class="tile">''' + wm_thumb("BrainGate.jpg", "BrainGate 腦機介面晶片") + '''<h4>🤖 AI 與電腦結合</h4><p>智慧醫療、自動駕駛、智能助理，甚至<strong>腦機介面（BCI）</strong>——把大腦的神經訊號直接連上電腦。像馬斯克的 <strong>Neuralink</strong> 就是這類技術；圖為同屬腦機介面的 <strong>BrainGate</strong> 神經晶片。</p></div>
  <div class="tile">''' + wm_thumb("Cern datacenter.jpg", "資料中心大量伺服器機房") + '''<h4>☁️ 雲端電腦（Cloud Computing）</h4><p>不需要自己買高性能電腦，而是<strong>透過網路</strong>使用遠端伺服器的運算與儲存。用途如 Google Drive、線上 AI、影音串流、企業系統；代表業者有 Amazon Web Services、Microsoft Azure、Google Cloud。</p></div>
  <div class="tile">''' + wm_thumb("Servers in a Rack.jpg", "機櫃中的伺服器") + '''<h4>🖥️ 伺服器（Server）</h4><p>專門<strong>提供服務</strong>給其他電腦，例如網站、遊戲、電子郵件、AI 推論伺服器。和大型主機不同，伺服器通常由<strong>許多台一起運作</strong>。</p></div>
  <div class="tile">''' + wm_thumb("Assorted smartphones.jpg", "各式智慧型手機") + '''<h4>📱 行動裝置（Mobile Computing）</h4><p>智慧型手機和平板其實也是<strong>完整的電腦</strong>。特色：低耗電、採 <strong>ARM 處理器</strong>、觸控操作，還內建 GPS、相機、陀螺儀等感測器。</p></div>
  <div class="tile">''' + wm_thumb("Waymo self-driving car front view.gk.jpg", "Waymo 自動駕駛車") + '''<h4>🤖 邊緣電腦（Edge Computing）</h4><p>資料<strong>直接在設備附近就地處理</strong>，不必全部送到雲端，反應更快。例如自動駕駛、工廠自動化、智慧攝影機、AI 監控。圖為自動駕駛車。</p></div>
  <div class="tile">''' + wm_thumb("Tensor Processing Unit 3.0.jpg", "Google TPU 張量處理器") + '''<h4>🧠 AI 專用電腦</h4><p>專門<strong>訓練與執行人工智慧</strong>，常見硬體有 <strong>GPU、TPU、NPU</strong>（AI 加速器）。像手機裡的 NPU 就能快速完成拍照、人臉辨識和語音辨識。圖為 Google 的 TPU。</p></div>
  <div class="tile">''' + wm_thumb("IBM Quantum System One.jpg", "IBM Quantum System One 量子電腦") + '''<h4>⚛️ 量子電腦（Quantum Computer）</h4><p>利用<strong>量子位元（Qubit）</strong>運算，目前仍在研究與早期商業化階段。適合密碼學、新藥研發、材料科學、最佳化問題，但還無法取代一般個人電腦。圖為 IBM Quantum System One。</p></div>
  <div class="tile">''' + wm_thumb("DNA Double Helix by NHGRI.jpg", "DNA 雙螺旋結構") + '''<h4>🧬 生物電腦（Biological Computer）</h4><p>利用 <strong>DNA、蛋白質或活細胞</strong>進行運算，目前大多仍在研究階段。未來可能應用於醫療、生物工程、分子計算。</p></div>
</div>
''') + sec(4, "電腦的優點與使用注意", '''
<div class="grid cols-2">
<div class="card"><h3>✅ 電腦的優點</h3>
<ul><li><strong>高速處理</strong>：每百萬分之一秒可執行多個運算。</li>
<li><strong>準確性高</strong>：輸入正確，結果精準無誤。</li>
<li><strong>儲存量大</strong>：小型裝置即可存海量資料。</li>
<li><strong>傳輸便利</strong>：透過網路快速交換資訊。</li></ul>
</div>
<div class="card"><h3>⚠️ 使用注意事項</h3>
<ul><li><strong>確保輸入正確</strong>：避免「垃圾進、垃圾出」(GIGO)。</li>
<li><strong>資訊查證</strong>：網路資訊未必可靠，使用前要驗證。</li>
<li><strong>防止資料遺失</strong>：注意軟硬體維護。</li>
<li><strong>定期備份</strong>：建立備份機制防止意外損失。</li></ul>
</div>
</div>
<div class="callout"><span class="t">🖱️ 使用者介面的演進</span>
<p>從純文字的 <strong>DOS</strong> 命令列 → 圖形化介面 <strong>GUI</strong>（圖示、視窗、滑鼠）→ 自然語言介面（語音／文字與 AI 互動）→ 未來的腦機介面。核心趨勢：介面越來越貼近「人本來就習慣的方式」——從背指令 → 用點的 → 用說的 → 用想的。</p>
<p class="uigif-hint">👆 把滑鼠移到下面四個方框（手機點一下），看看每個階段「怎麼操作」。</p>
<div class="uievo-flow">
  <div class="uigif uievo-card" onclick="this.classList.toggle('on')" tabindex="0">
    <div class="uievo-ic">⌨️</div><div class="uievo-nm">文字命令列</div><div class="uievo-tg">DOS・1980s</div><div class="uievo-nt">打指令、背指令操作</div>
    <div class="uigif-pop"><img src="https://commons.wikimedia.org/wiki/Special:FilePath/MS-DOS%20Deutsch.png?width=320" alt="早期 MS-DOS 黑底命令列畫面" loading="lazy" onerror="this.closest('.uigif-pop').classList.add('nogif')"><div class="uigif-cap">早期的 <b>DOS</b>：黑底白字，整台電腦都要靠「打指令」操作，指令還得自己背（圖：維基百科）</div></div>
  </div>
  <div class="uievo-ar">→</div>
  <div class="uigif uievo-card" onclick="this.classList.toggle('on')" tabindex="0">
    <div class="uievo-ic">🖱️</div><div class="uievo-nm">圖形介面</div><div class="uievo-tg">GUI・1990s</div><div class="uievo-nt">視窗、圖示、滑鼠點選</div>
    <div class="uigif-pop"><img src="https://commons.wikimedia.org/wiki/Special:FilePath/Ubuntu%2020.04%20Desktop%20animated%20GIF.gif?width=320" alt="圖形介面桌面操作示範" loading="lazy" onerror="this.closest('.uigif-pop').classList.add('nogif')"><div class="uigif-cap">其實你<b>現在正在看的這個網頁</b>——有視窗、圖示、按鈕，還能用滑鼠點——就是 <b>GUI</b>（圖形使用者介面）！不用背指令，用點的、拖的就能操作（圖：Ubuntu 桌面，Wikimedia Commons）</div></div>
  </div>
  <div class="uievo-ar">→</div>
  <div class="uigif uievo-card" onclick="this.classList.toggle('on')" tabindex="0">
    <div class="uievo-ic">💬</div><div class="uievo-nm">自然語言</div><div class="uievo-tg">AI・2020s</div><div class="uievo-nt">用說的跟 AI 對話</div>
    <div class="uigif-pop"><div class="uigif-demo ai-demo"><span class="chat u">幫我整理明天的行程</span><span class="chat b">好，我幫你排好了 <span class="dots"><i></i><i></i><i></i></span></span></div><div class="uigif-cap">直接用「說的」或「打字」跟 AI 對話，電腦就聽得懂（自製示意動畫）</div></div>
  </div>
  <div class="uievo-ar">→</div>
  <div class="uigif uievo-card" onclick="this.classList.toggle('on')" tabindex="0">
    <div class="uievo-ic">🧠</div><div class="uievo-nm">腦機介面</div><div class="uievo-tg">BCI・未來</div><div class="uievo-nt">用腦波操控（發展中）</div>
    <div class="uigif-pop"><div class="uigif-demo bci-demo"><span class="brain">🧠</span><span class="wav">〜〜〜</span><span class="mon">💻</span></div><div class="uigif-cap">用腦波直接操控電腦，連手都不用動（發展中，自製示意動畫）。<br>延伸影片：<a class="uigif-vid" href="https://www.youtube.com/watch?v=23zW_jXC14g" target="_blank" rel="noopener">▶ TVBS：馬斯克腦機介面突破，助漸凍症患者自主進食 ↗</a><a class="uigif-vid" href="https://www.youtube.com/watch?v=sRmglNd1NuI" target="_blank" rel="noopener">▶ GQ：腦機介面專家解析常見疑問 ↗</a></div></div>
  </div>
</div></div>
''') + exercise("課堂練習", '''
<ol>
  <li>家裡的電燈開關要用「手」去按；但電腦裡有幾億個開關，為什麼<strong>不能</strong>用這種要用手按的開關？真空管、電晶體又是怎麼在<strong>「沒有人手」</strong>的情況下做出 <strong>1 和 0</strong> 的？（提示：用「電去控制電」「隱形的手」來想）</li>
  <li><strong>電晶體</strong>比真空管好在哪裡？為什麼第二代電腦要用它取代真空管？</li>
  <li>「摩爾定律」和「輝達定律」各在講什麼？兩者的成長速度差在哪？</li>
  <li>氣象局做數值天氣預報，最適合用哪一種電腦？為什麼？</li>
</ol>''', '''
<ol>
<li>因為幾億個開關，人的手根本按不完、也太慢。真空管／電晶體是<strong>「電子開關」</strong>：只要在控制端給一點電（真空管靠<strong>加熱</strong>、電晶體靠<strong>一點電壓</strong>，就像刷感應卡），就能像一隻<strong>「隱形的手」</strong>把電路<strong>接通或斷開</strong>——<strong>接通（電流通過）＝ 1、斷開（不通）＝ 0</strong>，而且速度極快。</li>
<li>電晶體比真空管<strong>小很多、更省電、故障率低、又耐用</strong>，所以第二代電腦用它取代真空管。</li>
<li>摩爾定律：晶片上電晶體數量約<strong>每 2 年翻一倍</strong>；輝達定律：GPU 的 AI 效能約<strong>每年翻一倍</strong>（約 10 年 1000 倍），比摩爾定律快很多。</li>
<li>超級電腦，因其<strong>浮點運算</strong>效能最強，適合大量數值運算。</li>
</ol>''')

# =====================================================================
# 單元 05：電腦五大單元
# =====================================================================
BODIES["unit05"] = hero("unit05") + goals([
    "用生活比喻理解電腦「輸入 → 運算 → 輸出」的運作",
    "認識電腦五大單元各自負責什麼工作",
    "知道 CPU 是什麼，以及哪些因素會影響它的快慢",
]) + sec(1, "電腦怎麼運作？用「一家餐廳」來想", '''
<p>電腦做任何事，都逃不出三個步驟：<strong>輸入 → 運算 → 輸出</strong>。這其實跟一家餐廳出餐的流程一模一樣：</p>
<div class="callout"><span class="t">🍜 餐廳流程</span>
<p>客人點餐（<strong>輸入</strong>）→ 廚房做菜（<strong>運算</strong>）→ 把菜端上桌（<strong>輸出</strong>）</p></div>
<p>電腦裡負責這整個流程的，就是接下來要介紹的<strong>五大單元</strong>。</p>
''') + sec(2, "電腦的五大單元（配餐廳比喻）", '''
<p>把電腦想成一家餐廳，五大單元就是餐廳裡的五種角色：</p>
<div class="table-wrap"><table>
<thead><tr><th>五大單元</th><th>餐廳裡的角色</th><th>負責什麼</th><th>實際例子</th></tr></thead>
<tbody>
<tr><td>⌨️ <strong>輸入單元</strong></td><td>點餐服務生</td><td>接收外面來的資料與指令</td><td>鍵盤、滑鼠</td></tr>
<tr><td>💾 <strong>記憶單元</strong></td><td>冰箱／倉庫</td><td>暫時存放要處理的資料與半成品</td><td>記憶體 RAM</td></tr>
<tr><td>🧠 <strong>控制單元</strong></td><td>店長</td><td>指揮大家：誰先做、做什麼</td><td rowspan="2">在 CPU 裡</td></tr>
<tr><td>🧮 <strong>算術邏輯單元</strong></td><td>廚師</td><td>真正動手「運算」（加減乘除、判斷）</td></tr>
<tr><td>🖥️ <strong>輸出單元</strong></td><td>上菜</td><td>把做好的結果送出來給人看</td><td>螢幕、印表機、喇叭</td></tr>
</tbody></table></div>
<div class="callout tip"><span class="t">🧩 CPU 就是「廚房」</span>
<p>其中<strong>控制單元（店長）＋ 算術邏輯單元（廚師）</strong>合在一起，就是電腦的大腦——<strong>CPU（中央處理器）</strong>。所以買電腦時 CPU 好不好，影響很大。</p></div>
''') + sec(3, "CPU 的快慢看什麼？", '''
<p>同樣是「廚房」，有的出餐快、有的出餐慢。CPU 的快慢主要看三件事：</p>
<div class="grid cols-3">
  <div class="tile"><h4>⏱️ 時脈（速度）</h4><p>廚師手腳多快。單位是 GHz，數字越大、每秒能做的事越多。</p></div>
  <div class="tile"><h4>👥 核心數</h4><p>有幾個廚師同時做菜。核心越多，越能一次處理多件事（多工）。</p></div>
  <div class="tile"><h4>⚡ 快取記憶體</h4><p>廚師手邊的小備料檯。快取越大，越不用一直跑遠去倉庫拿東西。</p></div>
</div>
<div class="callout"><span class="t">🔎 想更深入（可略過）</span>
<p>CPU 每做一個指令，其實會經過「擷取 → 解碼 → 執行 → 儲存」四個小步驟（合稱一個機器週期）。這部分是進階內容，先知道「CPU 一步步照指令做事」就夠了。</p></div>
''') + sec(4, "資料放哪裡？儲存單元金字塔", '''
<p>電腦裡存放資料的地方不只一種，它們像金字塔一樣分層：<strong>越上面越快、越貴、容量越小；越下面越慢、越便宜、容量越大</strong>。</p>
<p>另外要記得：暫存器、快取、主記憶體是<strong>揮發性</strong>（一斷電資料就不見），硬碟／SSD 是<strong>非揮發性</strong>（斷電資料還在）——這也是為什麼打字要記得存檔！</p>
''' + local_img("images/storage_pyramid.png",
                "儲存單元金字塔：暫存器、快取(SRAM)、主記憶體(DRAM)、硬碟，越上面越快越貴",
                "儲存單元金字塔：處理速度／價格由上到下遞減，容量由上到下遞增。") + '''
''') + exercise("課堂練習", '''
<ol>
  <li>電腦做任何事都包含哪三個步驟？</li>
  <li>用餐廳比喻：負責「運算（做菜）」的是哪個單元？負責「指揮」的又是哪個？</li>
  <li>CPU 是由哪兩個單元合起來的？</li>
  <li>其他條件相同時，時脈 3.5 GHz 與 2.0 GHz 的 CPU 哪個比較快？</li>
  <li>為什麼打字打到一半突然停電，沒存檔的內容會不見？（提示：揮發性）</li>
</ol>''', '''
<ol>
<li>輸入 → 運算 → 輸出。</li>
<li>做菜（運算）＝算術邏輯單元（廚師）；指揮＝控制單元（店長）。</li>
<li>控制單元 ＋ 算術邏輯單元。</li>
<li>3.5 GHz 較快（時脈較高）。</li>
<li>因為打字的內容暫時放在「記憶體（RAM）」，它是揮發性的，一斷電就消失；存檔是把它寫進非揮發性的硬碟／SSD。</li>
</ol>''')

# =====================================================================
# 單元 06：電腦硬體與組裝
# =====================================================================
BODIES["unit06"] = hero("unit06") + goals([
    "認識主機板、CPU、RAM、顯示卡等主要零組件",
    "了解各零組件的品牌、規格與等級差異",
    "認識 SSD / HDD 的介面與差異",
    "建立依需求挑選與組裝一台電腦的觀念",
]) + '''
<nav class="part-nav" aria-label="零件快速跳轉">
  <div class="part-nav-t">🧭 零件跳轉</div>
  <a href="#sec1">🟩 主機板</a>
  <a href="#sec2">🧠 CPU</a>
  <a href="#sec3">🧩 RAM／顯卡</a>
  <a href="#sec4">💽 儲存裝置</a>
  <a href="#sec5">⚡ 電源／機殼／螢幕</a>
  <a href="#sec6">🛠️ 需求分析與組裝</a>
</nav>
<div class="part">
''' + local_img("images/case_inside.jpg",
                "電腦主機內部圖，標示電源供應器、風扇、CPU、主機板、顯示卡、記憶體、光碟機、硬碟",
                "打開機殼看內部的樣子。") + '''
  <div>
    <p>先打開一台桌機看看裡面有什麼——各個零組件都裝在機殼裡，並接到主機板上：</p>
    <ul class="tidy">
      <li>🔌 電源供應器（供電）</li>
      <li>🧠 CPU（上面有散熱風扇）</li>
      <li>🟩 主機板（把一切連在一起）</li>
      <li>🧩 記憶體、🎮 顯示卡、💽 硬碟／光碟機</li>
    </ul>
  </div>
</div>
''' + sec(1, "主機板 Motherboard", '''
<div class="part">
''' + local_img("images/mb_annotated.jpg",
                "主機板各部位標示圖：PCIE x16 接顯卡、M.2 接口、SATA 接口、CPU 插槽、記憶體插槽等",
                "主機板各部位標示。") + '''
  <div>
    <p>主機板是電腦的<strong>中樞</strong>，各種周邊都要與它連結才能發揮功能，是 CPU 與外界溝通的橋樑。</p>
    <p>圖中標出了各插槽與接口的位置，對照下表就能看懂每個接口是做什麼的。</p>
  </div>
</div>
<div class="table-wrap"><table>
<thead><tr><th>接口 / 插槽</th><th>用途</th></tr></thead>
<tbody>
<tr><td>PCIe x16</td><td>主要接<strong>顯示卡</strong></td></tr>
<tr><td>PCIe x1</td><td>接網路卡、音效卡等</td></tr>
<tr><td>CPU 插槽</td><td>安裝 CPU</td></tr>
<tr><td>記憶體插槽</td><td>安裝 RAM</td></tr>
<tr><td>M.2 接口</td><td>安裝 M.2 SSD（新、速度快）</td></tr>
<tr><td>SATA 接口</td><td>接 SATA SSD / HDD（舊）</td></tr>
</tbody></table></div>
<ul class="tidy">
  <li><strong>品牌：</strong>華碩、技嘉、微星、華擎</li>
  <li><strong>晶片組等級（低→高）：</strong>Intel 為 B → H → Z；AMD 為 A → B → X</li>
  <li><strong>板型：</strong>特大、大板、小板、迷你板</li>
</ul>
''') + sec(2, "CPU 中央處理器", '''
<div class="part">
''' + wm_img("AMD Ryzen 9 9950X.jpg",
             "AMD Ryzen 9 桌上型處理器正面",
             "CPU（中央處理器）：電腦的大腦，負責運算與控制。", width=560) + '''
  <div>
    <p>CPU 是電腦的運算核心。市面上主要有兩大品牌，各自有由低（入門）到高（高階）的產品線：</p>
    <div class="tile" style="margin-bottom:12px"><h4>🔵 Intel</h4>
      <p style="margin:0">目前（2024 年起）改用 <strong>Core Ultra</strong> 命名：</p>
      <p style="margin:2px 0">Core Ultra 5 → Ultra 7 → <strong>Ultra 9</strong>（例：Ultra 7 265K）</p>
      <p style="margin:2px 0 0;font-size:.86rem;color:var(--text-faint)">舊命名（前幾代）：Core i3 → i5 → i7 → i9</p></div>
    <div class="tile"><h4>🔴 AMD</h4>
      <p style="margin:0">Ryzen 5 → Ryzen 7 → <strong>Ryzen 9</strong></p>
      <p style="margin:2px 0 0;font-size:.86rem;color:var(--text-faint)">目前為 9000 系列（Zen 5）；遊戲最強是 X3D 版，如 Ryzen 7 9800X3D</p></div>
  </div>
</div>
<h3>看懂型號後面的英文字母（尾碼）</h3>
<p>CPU 型號後面的字母代表它的<strong>功能定位</strong>，挑選時很重要：</p>
<div class="grid cols-2">
  <div class="card"><h4>🔵 Intel 常見尾碼</h4>
  <div class="table-wrap"><table>
  <thead><tr><th>尾碼</th><th>意義</th></tr></thead>
  <tbody>
  <tr><td><strong>K</strong></td><td>不鎖倍頻、可超頻（如 Core Ultra 7 265K）</td></tr>
  <tr><td><strong>F</strong></td><td><strong>沒有內建顯示晶片</strong>，一定要搭獨立顯卡（如 Ultra 5 245F）</td></tr>
  <tr><td><strong>U</strong></td><td>筆電專用，極低功耗</td></tr>
  </tbody></table></div></div>
  <div class="card"><h4>🔴 AMD 常見尾碼</h4>
  <div class="table-wrap"><table>
  <thead><tr><th>尾碼</th><th>意義</th></tr></thead>
  <tbody>
  <tr><td><strong>X</strong></td><td>標準效能版，頻率通常較高</td></tr>
  <tr><td><strong>X3D</strong></td><td>內建大容量快取（3D V-Cache），<strong>遊戲效能最強</strong>（如 9800X3D）</td></tr>
  <tr><td><strong>F</strong></td><td>沒有內建顯示晶片，要搭獨立顯卡</td></tr>
  </tbody></table></div></div>
</div>
<div class="callout tip"><span class="t">💡 記一個重點</span><p>看到 <strong>F</strong>（Intel）或 <strong>F</strong>（AMD）結尾＝<strong>沒有內顯</strong>，這台電腦就<strong>一定要裝獨立顯卡</strong>才有畫面；其餘型號多半有內顯，文書、上網、看影片不必另外買顯卡。</p></div>
''') + sec(3, "RAM 主記憶體與顯示卡", '''
<div class="grid cols-2">
  <div class="card"><h3>🧩 RAM 主記憶體</h3>
  <figure class="fig"><img src="https://pimg.1px.tw/ofeyhong/1730720226-1135020535-g.jpg" alt="DDR5 記憶體實體照片" loading="lazy" onerror="this.closest('figure').classList.add('img-fail')"><div class="img-fallback">🖼️ 圖片需連網載入<br><span>DDR5 記憶體實體照</span></div><figcaption>DDR5 記憶體實體照。<a class="credit" href="https://ofeyhong.pixnet.net/blog/posts/12059851482" target="_blank" rel="noopener">圖片來源：ofeyhong 痞客邦 ↗</a></figcaption></figure>
  <p><strong>品牌：</strong>美光、金士頓、威剛、芝奇、十銓、海盜船等。</p>
  <p><strong>容量：</strong>4G、8G、16G、32G…（越大越能同時開多個程式）。</p></div>
  <div class="card"><h3>🎮 顯示卡</h3>
  ''' + local_img("images/gpu_naming.jpg",
                  "顯示卡型號解讀：RTX 3060 Ti 的系列、世代、等級、後綴",
                  "看懂顯示卡型號：以 RTX 3060 Ti 為例＝系列＋世代＋等級＋後綴。") + '''
  <ul class="tidy">
    <li><strong>GPU 晶片廠：</strong>NVIDIA、AMD</li>
    <li><strong>板卡品牌：</strong>華碩、技嘉、微星等</li>
    <li><strong>等級（看型號中間數字）：</strong>2~4 低階、5 中階、6~9 高階</li>
  </ul></div>
</div>
''') + sec(4, "儲存裝置：HDD 與 SSD", '''
<div class="grid cols-2">
<div class="card"><h3>💽 HDD 傳統硬碟</h3>
''' + wm_img("Laptop-hard-drive-exposed.jpg",
             "拆開外殼的傳統硬碟，可看到碟片與讀寫磁頭",
             "傳統硬碟（HDD）：靠碟片旋轉＋磁頭讀寫（機械式），容量大、便宜。") + '''
<ul class="tidy">
  <li><strong>品牌：</strong>Seagate（希捷）、WD（威騰）、Toshiba（東芝）</li>
  <li><strong>依用途分：</strong>家用型（三年保）、企業型（五年保）、監控型、NAS 型</li>
</ul></div>
<div class="card"><h3>⚡ SSD 固態硬碟</h3>
''' + wm_img("1TB 2280 NVME SSD.jpg",
             "一條 M.2 2280 規格的 NVMe 固態硬碟",
             "M.2 NVMe SSD：用快閃記憶體（無機械），體積小、速度快。") + '''
<ul class="tidy">
  <li><strong>儲存顆粒（壽命/成本）：</strong>SLC → MLC → TLC → QLC</li>
  <li>沒有機械結構，較耐震、安靜、省電</li>
</ul></div>
</div>
<h3>三種儲存裝置比較</h3>
<div class="table-wrap"><table class="center">
<thead><tr><th>項目</th><th>傳統硬碟 HDD</th><th>SATA SSD</th><th>M.2 NVMe SSD</th></tr></thead>
<tbody>
<tr><td>介面</td><td>SATA</td><td>SATA</td><td><strong>M.2</strong></td></tr>
<tr><td>通道</td><td>SATA（窄）</td><td>SATA（窄）</td><td><strong>PCIe（寬）</strong></td></tr>
<tr><td>協議</td><td>AHCI</td><td>AHCI</td><td><strong>NVMe</strong></td></tr>
<tr><td>讀取速度（約）</td><td>100～200 MB/s</td><td>約 500 MB/s</td><td><strong>3500 MB/s 以上</strong></td></tr>
<tr><td>運作原理</td><td>碟片旋轉＋磁頭（機械）</td><td colspan="2">快閃記憶體（無機械）</td></tr>
<tr><td>優點</td><td>容量大、最便宜</td><td>比 HDD 快、耐震</td><td><strong>最快</strong>、體積最小</td></tr>
<tr><td>缺點</td><td>慢、怕震、有噪音</td><td>比 NVMe 慢</td><td>單位容量較貴</td></tr>
</tbody></table></div>
<div class="callout tip"><span class="t">💡 速度差多少？</span><p>HDD ＜ SATA SSD ＜ M.2 NVMe SSD。從 HDD 換成 NVMe SSD，開機和開程式的速度感受最明顯。</p></div>
''') + sec(5, "電源、機殼與螢幕", '''
<div class="grid cols-3">
  <div class="tile"><h4>🔌 電源供應器</h4>
  ''' + local_img("images/psu_80plus.jpg",
                  "80 PLUS 效率認證等級：白牌、銅牌、銀牌、金牌、白金、鈦金",
                  "80 PLUS 效率等級（低→高）：白牌→銅→銀→金→白金→鈦金。") + '''
  <ul class="tidy" style="margin-top:6px">
    <li>常見瓦數：450／550／650／750／850W</li>
    <li>等級越高越省電、用料通常越好</li>
  </ul>
  <p style="font-size:.85rem;margin:6px 0 0"><strong>怎麼選瓦數／等級？</strong></p>
  <ul class="tidy" style="font-size:.85rem">
    <li>文書機（無獨顯）：450～550W、白牌／銅牌就夠</li>
    <li>中階遊戲機（有獨顯）：650～750W、銅牌～金牌</li>
    <li>高階／高瓦顯卡：750W 以上、金牌以上較穩</li>
  </ul></div>
  <div class="tile"><h4>🗄️ 機殼</h4>
  ''' + local_img("images/case_types.jpg",
                  "三種機殼款式：一般型、側透型、側透 +RGB",
                  "機殼款式：一般型、側透型、側透 +RGB。") + '''
  <ul class="tidy" style="margin-top:6px">
    <li>款式：一般型、側透型、側透 +RGB</li>
    <li>規格：ATX、mATX</li>
  </ul>
  <div class="callout warn" style="margin-top:8px"><span class="t">⚠ 要對到主機板大小！</span>
  <p style="font-size:.85rem;margin-bottom:0">買機殼要看能不能裝下你的主機板：<br>
  ・<strong>ATX 機殼</strong>：可裝 ATX 大板（約 30.5 × 24.4 cm）<br>
  ・<strong>mATX 機殼</strong>：裝 mATX 小板（約 24.4 × 24.4 cm）<br>
  大機殼通常能裝小板，反過來則不行。</p></div></div>
  <div class="tile"><h4>🖥️ 螢幕</h4>
  ''' + local_img("images/monitor_ports.jpg",
                  "螢幕接頭比較：D-Sub(VGA)、DVI-D、HDMI、DisplayPort",
                  "常見螢幕接頭：D-Sub(VGA)、DVI、HDMI、DisplayPort。") + '''
  <ul class="tidy" style="margin-top:6px">
    <li>面板色彩：IPS ＞ VA ＞ TN</li>
    <li>反應速度：TN ＞ IPS ＞ VA</li>
    <li>解析度：常見 1920×1080（Full HD）</li>
    <li>更新率：電競建議 120Hz 以上</li>
    <li>接頭：建議具備 HDMI／DP</li>
  </ul></div>
</div>
<h3>認識兩種主流螢幕接頭：HDMI 與 DP</h3>
<div class="grid cols-2">
  <div class="tile"><h4>📺 HDMI</h4><p>最普及的影音接頭，<strong>影像＋聲音一條線搞定</strong>。電視、螢幕、遊戲機幾乎都有，接電視、投影機很方便。</p></div>
  <div class="tile"><h4>🖥️ DisplayPort（DP）</h4><p>電腦與顯示卡上更常見，<strong>高解析度、高更新率</strong>（如 2K/4K 144Hz 以上）表現通常更好，打電競、接多螢幕常用它。</p></div>
</div>
<div class="grid cols-2">
''' + wm_img("HDMI connector-male 2 sharp PNr°0059.jpg", "HDMI 接頭：左右對稱的倒梯形", "<strong>HDMI</strong>：接頭是<strong>左右對稱的倒梯形</strong>。", width=440) + '''
''' + wm_img("DisplayPort connector-male-front PNr°0442.jpg", "DisplayPort 接頭正面：有一角是斜切的（缺一角）", "<strong>DisplayPort（DP）</strong>：注意接頭<strong>有一角是斜切的（缺一角）</strong>。", width=440) + '''
</div>
<p style="font-size:.85rem;color:var(--text-faint);margin:2px 0 0">看接頭形狀就能分辨：<strong>HDMI 左右對稱、DP 缺一角</strong>。（兩張圖皆取自 Wikimedia Commons，可自由使用，沒有版權疑慮）</p>
<div class="reveal" onclick="toggleWork(this)"><span class="wk-arrow">▶</span> 🕹️ 冷知識：為什麼會有 DP？</div>
<div class="answer">
<p>HDMI 由幾家消費電子大廠主導，<strong>廠商每年要付授權金（權利金）</strong>。於是電腦業界的 VESA 組織在 2006 年推出 <strong>DisplayPort</strong>，主打<strong>「免權利金」的開放標準</strong>，用來取代老舊的 VGA／DVI，也讓電腦廠不必再付 HDMI 授權費——這就是 DP 出現的主因。</p>
<p style="margin-bottom:0;font-size:.82rem;color:var(--text-faint)">說法來源：DisplayPort vs HDMI 比較（新基科技、EcLife 等）；DisplayPort 為 VESA 於 2006 年發布的免權利金標準。</p></div>
''') + sec(6, "需求分析與組裝專題", '''
<p>組裝一台電腦前，先做<strong>需求分析</strong>：這台電腦要拿來做什麼？再依需求與預算配置零組件。</p>
<div class="table-wrap"><table>
<thead><tr><th>用途</th><th>配置重點</th></tr></thead>
<tbody>
<tr><td>文書上網</td><td>CPU <strong>內顯即可</strong>、<strong>16GB RAM</strong>（8GB 已偏緊）、<strong>NVMe SSD</strong>；不需獨立顯卡</td></tr>
<tr><td>遊戲電競</td><td>中高階<strong>獨立顯卡</strong>（如 RTX 5060 以上）、<strong>16～32GB RAM</strong>（32GB 逐漸成主流）、<strong>高更新率螢幕</strong>（144Hz 以上）</td></tr>
<tr><td>影音剪輯 / 繪圖</td><td>多核心 CPU、<strong>32GB 以上 RAM</strong>、大容量高速 <strong>NVMe SSD</strong>；建議搭獨立顯卡做 GPU 加速</td></tr>
</tbody></table></div>
<p style="font-size:.82rem;color:var(--text-faint);margin:6px 0 0">※ 依 <strong>2026 年</strong>市場現況調整：文書機的 RAM 已從 8GB 提升到 <strong>16GB</strong> 較安心；遊戲／剪輯的 <strong>32GB</strong> 正逐漸成為新標準，NVMe SSD 也幾乎是標配。（參考：歐飛先生、無尾熊電腦、renjoyit 等 2026 組裝指南）</p>
<div class="callout warn"><span class="t">🧰 組裝提醒</span><p>組裝時注意：CPU 與主機板腳位相容、電源瓦數足夠、記憶體與主機板相容、機殼容納得下顯示卡長度。</p></div>
<a class="compiler-cta" href="https://www.coolpc.com.tw/evaluate.php" target="_blank" rel="noopener">
  <span class="ic">🛒</span>
  <span class="tx"><strong>原價屋線上估價系統（作業要用）</strong><small>用它挑選零組件、配一台電腦並估算價格（另開新分頁）</small></span>
  <span class="go">↗</span>
</a>
''') + exercise("課堂練習", '''
<ol>
  <li>顯示卡通常安裝在主機板的哪個插槽？</li>
  <li>M.2 NVMe SSD 與 SATA SSD，哪個速度較快？</li>
  <li>Intel 目前的 <strong>Core Ultra</strong> 處理器，由低到高排列：Ultra 9、Ultra 5、Ultra 7，正確順序是？</li>
  <li>CPU 型號結尾是 <strong>F</strong>（例：Ultra 5 245F）代表什麼？裝機時要注意什麼？</li>
  <li>幫「只用來<strong>文書上網、看 YouTube／Netflix</strong>」的長輩配一台電腦，需要加獨立顯卡嗎？為什麼？</li>
</ol>''', '''
<ol>
<li>PCIe x16。</li>
<li>M.2 NVMe SSD。</li>
<li>Ultra 5 → Ultra 7 → Ultra 9（數字越大越高階）。</li>
<li>F ＝<strong>沒有內建顯示晶片</strong>，所以這台電腦<strong>一定要另外裝獨立顯卡</strong>才有畫面。</li>
<li><strong>不用加獨立顯卡。</strong>現在的 CPU 大多內建顯示（內顯），播 YouTube／Netflix、甚至 4K 影片、文書上網都沒問題；獨立顯卡主要是給<strong>遊戲、3D 繪圖、影片剪輯</strong>用的。把省下的錢放在 SSD 或 RAM 更有感。（但若選到結尾 <strong>F</strong> 的 CPU 就沒內顯，那就非裝獨顯不可。）
<div class="callout" style="margin-top:8px"><span class="t">🖥️ 哪些 CPU 的內顯就能應付 4K 影音？（截至 2026 年 7 月）</span>
<ul class="tidy" style="margin-bottom:0">
  <li><strong>Intel：</strong>Core Ultra 200 系列（內建 <strong>Arc 內顯</strong>）、以及較新一代帶內顯的 Core／Core Ultra（非 F 版），都可輸出並硬體解碼 4K 影片。</li>
  <li><strong>AMD：</strong>Ryzen 8000G 系列、以及 Ryzen 7000／9000 帶 <strong>Radeon 內顯</strong>的型號（非 F 版），同樣支援 4K 影音。</li>
  <li><strong>更省的選擇：</strong>其實只要「有內顯」，連入門的 Intel UHD、AMD Radeon 內顯都能靠硬體解碼順播 4K 串流——文書＋看影片用這種就非常夠。</li>
</ul></div></li>
</ol>''')

# =====================================================================
# 單元 07：BEBRAS 運算思維
# =====================================================================
BODIES["unit07"] = hero("unit07") + goals([
    "認識運算思維（Computational Thinking）常用的四種解題方式",
    "了解 BEBRAS 國際運算思維挑戰賽",
    "透過題型練習培養拆解與解題的能力",
]) + sec(1, "認識 BEBRAS", '''
<p><strong>BEBRAS（海狸）</strong>是一項起源於立陶宛、風行全球的<strong>國際運算思維挑戰賽</strong>。題目多為情境式趣味題，<strong>不需先會寫程式</strong>，重點在推理與邏輯。</p>
<div class="callout tip"><span class="t">🇹🇼 和「108 課綱」的關係</span>
<p style="margin-bottom:0">教育部把<strong>運算思維（Computational Thinking）</strong>列為十二年國民基本教育（<strong>108 課綱</strong>）「<strong>科技領域</strong>」的核心素養，透過<strong>問題分解、樣式識別、抽象化與演算法規劃</strong>等邏輯，培養學生利用資訊科技工具解決生活與學習問題的能力。這正是本課程與 BEBRAS 練習想幫大家培養的能力。</p></div>
<div class="reveal" onclick="toggleWork(this)"><span class="wk-arrow">▶</span> 🦫 冷知識：為什麼是海狸？（其實正名是「河狸」）</div>
<div class="answer">
<p>海狸以「勤奮、聰明地築水壩」聞名，正好象徵運算思維——用巧妙的方法解決複雜的工程問題。</p>
<p>不過這裡有個常見的<strong>翻譯／命名小陷阱</strong>：BEBRAS 是立陶宛文的「<strong>beaver</strong>」，指的就是<strong>會築水壩</strong>、尾巴扁平像船槳的那種齧齒動物——牠正式的中文名其實是「<strong>河狸</strong>」（英文 <strong>Beaver</strong>）。比賽常被翻成「海狸」，但嚴格來說，很多資料裡的「<strong>海狸／海狸鼠</strong>」指的是另一種<strong>尾巴像老鼠、原產南美</strong>的動物「<strong>Coypu（Nutria）</strong>」。所以 BEBRAS 的吉祥物，其實就是築壩高手<strong>河狸（Beaver）</strong>，只是中文常沿用「海狸」這個俗稱。</p>
<p style="margin-bottom:0">💡 延伸小新聞：曾有報導寫「捷克某水壩籌備七年還沒動工，<strong>海狸</strong>兩晚就建好、省下四千多萬元」——其實真正的築壩高手是<strong>河狸（Beaver）</strong>喔！<a href="https://www.natgeomedia.com/environment/article/content-17921.html" target="_blank" rel="noopener">（延伸閱讀：國家地理 ↗）</a></p>
<p style="font-size:.88rem;color:var(--text-soft);margin:10px 0 2px"><strong>🦫 這就是會築壩的「河狸（Beaver）」本尊：</strong></p>
<div style="max-width:360px;margin:0 auto">
''' + wm_img("American Beaver.jpg", "美洲河狸 Castor canadensis，尾巴扁平像船槳", "美洲河狸（<em>Castor canadensis</em>）——注意<strong>尾巴扁平像船槳</strong>，這正是河狸的招牌特徵。", width=380) + '''
</div>
<p style="font-size:.88rem;color:var(--text-soft);margin:12px 0 2px"><strong>🏗️ 河狸的「水壩工程」——同一座水壩，四個月就變大了：</strong></p>
<div class="grid cols-2">
''' + local_img("images/beaver_dam_1.jpg", "河狸建造的水壩", "河狸水壩") + '''
''' + local_img("images/beaver_dam_2.jpg", "同一座河狸水壩四個月後變得更大", "四個月後，變大了") + '''
</div>
<p style="font-size:.78rem;color:var(--text-faint);margin:4px 0 0">圖片來源：維基百科（<a href="https://zh.wikipedia.org/zh-tw/%E6%B2%B3%E7%8B%B8" target="_blank" rel="noopener">河狸</a>、<a href="https://zh.wikipedia.org/zh-tw/%E6%B2%B3%E7%8B%B8%E5%9D%9D" target="_blank" rel="noopener">河狸坝</a>）</p>
</div>
''') + exercise("課堂練習（暖身：先做這裡，再往下看內容、最後做表單）", '''
<p>這幾題是本單元的暖身。<strong>先自己想想看</strong>（可先作答、再點開對照解答），有感覺之後再往下閱讀內容，最後到表單作答。這些解題方式<strong>不用背</strong>，會用就好。</p>
<ol>
  <li>運算思維常用的<strong>四種解題方式</strong>是哪四個？</li>
  <li>數列 2, 4, 6, 8, … 第 20 個數字是多少？（找規律）</li>
  <li>有個有名的冷笑話：<strong>「怎麼把大象放進冰箱？」</strong>答案是三個步驟——① 打開冰箱門 ② 把大象放進去 ③ 關上冰箱門。這其實就是「<strong>演算法</strong>」（照著步驟做）。<br>換你試試：<strong>「怎麼把長頸鹿放進冰箱？」</strong>請寫出步驟（小提示：冰箱裡已經有一隻大象了）。</li>
</ol>''', '''
<ol>
<li>拆解、找規律、抽象化、演算法（<strong>會用就好，不必背名詞</strong>）。</li>
<li>規律是「第 n 個 = 2n」，第 20 個 = 40。</li>
<li>長頸鹿版要多一步，因為<strong>前一個狀態</strong>（冰箱裡已經有大象）會影響接下來的動作：① 打開冰箱門 ② <strong>把大象拿出來</strong> ③ 把長頸鹿脖子折一折 ④ 把長頸鹿放進去 ⑤ 關上冰箱門。<br>😆 加碼：森林之王獅子召開森林大會，卻有一種動物沒到，是誰？——<strong>長頸鹿</strong>，因為牠還在冰箱裡！</li>
</ol>''') + '''
<a class="compiler-cta" href="https://forms.gle/RxDWW78HNt3xAhpt6" target="_blank" rel="noopener">
  <span class="ic">📝</span>
  <span class="tx"><strong>本單元練習表單（點我作答）</strong><small>老師指定的 Bebras 題目，請在這裡作答（另開新分頁）</small></span>
  <span class="go">↗</span>
</a>
''' + sec(2, "什麼是運算思維？", '''
<p>運算思維是一種<strong>像電腦科學家一樣思考</strong>的解題方法，重點不在寫程式，而在<strong>有系統地分析、解決問題</strong>。它<strong>不是要背的名詞</strong>，而是四種<strong>好用的解題方式</strong>，遇到難題時可以拿出來用：</p>
<div class="grid cols-2">
  <div class="tile"><h4>🧩 拆解 Decomposition</h4><p>把大問題拆成一個個小問題，各個擊破。</p></div>
  <div class="tile"><h4>🔍 找規律 Pattern Recognition</h4><p>找出問題中重複出現的規律與相似之處。</p></div>
  <div class="tile"><h4>🎯 抽象化 Abstraction</h4><p>忽略無關細節，只保留解決問題所需的關鍵資訊。</p></div>
  <div class="tile"><h4>📝 演算法 Algorithm</h4><p>設計一步步、照著做就能得到答案的步驟。</p></div>
</div>
<div class="callout tip"><span class="t">🧭 遇到 Bebras 題，怎麼想？</span>
<p style="margin-bottom:0">不用先會寫程式，重點是「有系統地想」——其實就是把上面四種方式<strong>串起來用</strong>：<strong>① 讀懂題目、拆解</strong>問題（到底要我求什麼？）→ <strong>② 抽象化</strong>，丟掉故事包裝、只留關鍵，找出<strong>規律</strong> → <strong>③ 設計步驟（演算法）</strong>，不確定就拿小例子先試一遍 → <strong>④ 驗證</strong>：把答案代回去檢查有沒有違反規則。</p></div>
<div class="callout tip"><span class="t">🍌 用「香蕉背包」那題示範一次</span>
<p><strong>題目：</strong>小麥手邊有八串香蕉：<strong>4、5、8、3、6、8、4、4</strong>（加起來 42）；媽媽手邊有五串：<strong>1、2、3、4、5</strong>。要在<strong>不拆開任何一串</strong>的情況下，把小麥的香蕉<strong>平均分裝到 3 個背包</strong>；如果需要，可以請媽媽再給<strong>一串</strong>加進來。請問分得成嗎？</p>
''' + banana_problem_svg() + '''
<p style="margin-bottom:0"><strong>怎麼用這四種方式想：</strong><br><strong>拆解</strong>——先把所有數量加起來算總數；<br><strong>找規律</strong>——要平均分成 3 份，總數一定得是 <strong>3 的倍數</strong>；<br><strong>演算法</strong>——如果不是 3 的倍數，就看加媽媽的哪一串，能剛好變成 3 的倍數、又真的能分成相等三堆；<br><strong>驗證</strong>——把分好的三堆各自加起來，確認每堆一樣多、且沒有拆開任何一串。<br>（完整算式與答案在本頁最下方「表單題目解答」的 🍌 香蕉背包）</p></div>
<div class="callout"><span class="t">📚 想深入了解「運算思維」？（參考來源）</span>
<ul class="tidy" style="margin-bottom:0">
  <li>運算思維奠基論文（英文）：Jeannette M. Wing,「Computational Thinking」, Communications of the ACM, 2006。</li>
  <li>臺灣師大 <strong>Bebras 國際運算思維挑戰賽</strong> 官網（中文）：bebras.csie.ntnu.edu.tw</li>
  <li>教育部 <strong>運算思維推動計畫</strong>（中文）：compthinking.csie.ntnu.edu.tw</li>
  <li>呂聰賢《運算思維簡報》（中文 PDF，可搜尋取得）。</li>
</ul></div>
''') + sec(3, "表單題目解答", '''
<p>下面是表單各題的<strong>詳解</strong>。<strong>建議先自己作答，再點開對照。</strong></p>
<div class="reveal" onclick="toggleAnswer(this)">▶ 顯示表單題目解答</div>
<div class="answer">
  <h3>💧 灑水器 —— 答案：25 台</h3>
  <p>每台灑水器只能覆蓋一塊<strong>同一種作物</strong>的正方形（可用 4×4、2×2 或 1×1，大正方形較省），要把整片 8×8 農場<strong>不重疊地蓋滿</strong>，求最少台數。作物分佈其實很破碎，能塞進的大正方形不多，所以要用很多小正方形補。下圖是用程式算出的<strong>最省鋪法</strong>：只有 1 個 4×4（左上玉米）、8 個 2×2、16 個 1×1，合計 <strong>25 台</strong>。分作物看：🌽玉米 5、🍎蘋果 5、🍇葡萄 6、🍊橘子 9 台。</p>
  ''' + sprinkler_svg() + '''
  <p class="bf-note">🧮 <strong>窮舉法（暴力破解）會怎樣：</strong>把每一格用 1×1／2×2／4×4 的各種鋪法全部試一遍，組合數是天文數字，電腦硬試也要很久；用「<strong>大正方形優先、依作物切割</strong>」的策略，一下就找到最省的 25 台。</p>

  <h3>🍌 香蕉背包 —— 答案：D（媽媽給三根的香蕉串）</h3>
  <p>小麥八串是 <strong>4、5、8、3、6、8、4、4</strong>，加起來 <strong>42</strong>（本身就是 3 的倍數）。但 42÷3＝14，在<strong>不拆開任何一串</strong>的條件下卻湊不出三個都剛好 14 的背包。所以要請媽媽加一串——加入後總數<strong>仍要是 3 的倍數</strong>才分得成：媽媽的五串 <strong>1、2、3、4、5</strong> 中，只有加「<strong>3</strong>」能維持 3 的倍數（42＋3＝<strong>45</strong>，每包 15）；加 1、2、4、5 都會破壞整除。加了 3 之後就分得出來：<strong>8＋4＋3、8＋4＋3、6＋5＋4</strong>，三個背包都是 15。所以答案 <strong>D</strong>。</p>
  ''' + banana_problem_svg() + '''
  <p class="bf-note">🧮 <strong>窮舉法（暴力破解）會怎樣：</strong>把 8 串各自丟進 3 個背包，共有 3⁸ ＝ 6561 種分法，再乘上「跟媽媽拿哪一串」5 種 ≈ 3 萬多種都要試；用「總和一定要是 3 的倍數」這條規律，一步就把大部分不可能的情況篩掉，快很多。</p>

  <h3>🚆 列車 —— 答案：B</h3>
  <p>規則：主線軌道與每個車庫最多只能放 3 輛；OUT／IN 都從「靠主線那一端」進出（像堆疊）。目標是把 1、2、3 由左至右放進車庫1。因為車庫1原本有 5 號、且最多放 3 輛，要先把 5 移走，再依序放 1、2、3。</p>
  <ul class="tidy"><li>A 只放進 1、2，3 號還卡在車庫3，沒完成。</li><li>C 中途把 7 號誤放進車庫1，順序錯。</li><li>D 讓主線同時出現 4 輛車，違反「不能超過 3 輛」。</li><li>B 剛好用 IN(2) 先把擋路的 6 號暫存到車庫2，再取出 3 號放進車庫1，全程沒超過 3 輛 ✓。</li></ul>
  <p>答案 <strong>B</strong>。</p>
  <p class="bf-note">🧮 <strong>窮舉法會怎樣：</strong>把每一步能做的 OUT／IN 操作全部展開成一棵樹，會指數成長、上千種以上；靠「主線與每個車庫都不能超過 3 輛」這條規則一路剪枝，合法路線其實剩沒幾條。</p>

  <h3>🏔️ 爬山訓練 第一題（誰最後下山）—— 答案：1 號</h3>
  <p>規則：每遇到一道「牆（階）」，最前面的海狸留下扶梯子，其他人先上；最後扶梯子的人再上去，並倒著排到隊伍最後面。下山依相同順序，所以隊伍最後一個就是最後下山的。6 隻海狸 123456，不論山有幾階，扶梯子的都是最前面幾號、最後倒序接到隊尾，倒序的最後一定是 <strong>1 號</strong> → 最後下山的是 1 號。</p>
  ''' + hike1_svg() + '''


  <h3>🏔️ 爬山訓練 第二題（登 3 座山的抵達順序）—— 答案：365412</h3>
  <p>萬用公式：一座有 k 道牆（k 階）的山，會把「最前面 k 隻」倒過來丟到隊尾，其餘往前遞補：<br><strong>新隊伍 ＝ 〔第 k+1 隻以後照原順序〕＋〔前 k 隻倒序〕</strong>。三座山的階數為 <strong>3、4、2</strong>，出發 123456 依序套用：</p>
  <ul class="tidy"><li>第一座（3 階）：123456 → <strong>456321</strong>（前 3 隻 123 倒序接到隊尾）</li><li>第二座（4 階）：456321 → <strong>213654</strong>（前 4 隻 4563 倒序接到隊尾）</li><li>第三座（2 階）：213654 → <strong>365412</strong>（前 2 隻 21 倒序接到隊尾）</li></ul>
  <p>所以抵達第三座山頂時的排序是 <strong>365412</strong>。</p>
  ''' + hike2_svg() + '''
  <p class="bf-note">🧮 這題照規則「<strong>模擬</strong>」一次（三座山各套一次倒序）就能得到答案，<strong>根本不必窮舉</strong>；真要窮舉，6 隻海狸的排列有 6! ＝ 720 種要一一比對。</p>

  <h3>🥾 徒步旅行 —— 答案：6</h3>
  <p>米亞每天走 1 或 2 個路段，而且<strong>每晚只能睡在房子（A～E）</strong>。用<strong>拆解</strong>把整段行程切成三小段，各段走法數<strong>相乘</strong>：</p>
  <ul class="tidy">
    <li>① <strong>起點 → B</strong>：<strong>2</strong> 種（就是圖上畫的路線 1、路線 2）</li>
    <li>② <strong>B → C</strong>：只有 <strong>1</strong> 種</li>
    <li>③ <strong>C → 終點</strong>：<strong>3</strong> 種（C→D→E→終點、C→E→終點、C→D→終點）</li>
  </ul>
  <p>所以共 <strong>2 × 1 × 3 ＝ 6</strong> 種走法，答案 <strong>6</strong>。</p>
  ''' + hike_trail_svg() + '''
  <p class="bf-note">🧮 <strong>窮舉法會怎樣：</strong>把「每天走 1 或 2 段」的所有走法一條一條列出來數，會隨路程<strong>指數成長</strong>；用「到每個點的走法數 ＝ 前一點 ＋ 前兩點」的遞推（像費氏數列），一次就數完。</p>

  <h3>🏆 淘汰賽 —— 答案：Beth（貝絲）</h3>
  <p>8 隊單淘汰，每隊在總表的出現次數 ＝ 1 +（贏的場數）。正確的紀錄要同時通過<strong>兩道關卡</strong>：</p>
  <ul class="tidy"><li><strong>次數分布</strong>：必須剛好是「一個 4（冠軍）、一個 3（亞軍）、兩個 2（四強）、四個 1（首輪淘汰）」。</li><li><strong>與賽程一致</strong>：光是數字對還不夠——出現 4 次的隊必須真的能沿著賽程表（第一輪 1–8、5–4、3–6、7–2）一路獲勝到冠軍；出現 3 次的要是它在決賽擊敗的對手，且兩人分屬上、下半區；出現 2 次的兩隊要各在一個半區打進四強。把每一欄的數字「還原成一張對戰樹」去驗證。</li></ul>
  <p>四位海狸逐一還原後，只有 <strong>Beth</strong> 的紀錄能拼出一張前後不矛盾的賽程樹（其他人會出現「同一組首輪對手兩隊都晉級」之類的矛盾）。答案 <strong>Beth</strong>。</p>
  ''' + tournament_svg() + '''
  <p class="bf-note">🧮 <strong>窮舉法會怎樣：</strong>8 隊的可能排列有 8! ＝ 40320 種要一一還原比對；用「<strong>出現次數 ＝ 1 ＋ 贏的場數</strong>」直接檢查每筆紀錄，快很多。</p>

  <h3>🚚 果汁車 —— 答案：D</h3>
  <p>目標：新增 1 台果汁車後，全城<strong>每個路口都在某台果汁車的 2 步內</strong>（最多經過 1 個中間路口就能買到）。做法：先標出現有果汁車能涵蓋（2 步內）的路口，找出還沒被涵蓋的「空白區」，再看 A／B／C／D 四個候選位置，哪一個放下去能把剩下的空白路口全部補進 2 步內。答案是放在 <strong>D</strong>——只有 D 能讓所有路口都被涵蓋，A／B／C 都各自漏掉至少一個路口。</p>
  <p class="bf-note">🧮 <strong>窮舉法會怎樣：</strong>把 A／B／C／D 四個候選位置都放放看，再檢查是不是「每個路口都在 2 條街內」；候選少時可行，但每一個都要掃過全城所有路口。</p>

  <h3>🧺 小艾的任務 —— 答案：C（39 分鐘）</h3>
  <p>要跑五金行、藥房、市場三處，從家出發、完成後直接回家，這是一個<strong>最短路線</strong>問題：把地圖畫成節點與帶權重的邊，比較「不同造訪順序＋每段走哪條路」的總花費，取最小值。最短走法是 <strong>家→市場→五金行→藥房→家</strong>，步行 36 分（家→市場 4；市場經麵包店到五金行 6＋3；五金行經麵包店·教堂·學校到藥房 3＋4＋4＋3；藥房經學校回家 3＋6），再加三次採買 3 分 ＝ <strong>39 分鐘</strong>，答案 <strong>C</strong>（比題目示範的 41 分少 2 分）。</p>
  ''' + errand_svg() + '''
  <p class="bf-note">🧮 <strong>窮舉法會怎樣：</strong>3 個要採買的點有 3! ＝ 6 種造訪順序，一一算總時間取最小就好；但點一多，n 個點就有約 (n−1)!÷2 種順序，會<strong>爆炸性成長</strong>——這正是有名的「旅行推銷員問題（TSP）」。</p>

</div>
''')


# ---- 組裝估價器（放在單元6最底部，可收合、預設收起）----
_EST_ITEMS = [
    ("處理器 CPU", "AMD R5 7500F(含風扇)【6核12緒】3.7G↑5.0G 代理三年保", 4690),
    ("主機板 MB", "華擎 B650M-H/M.2+ WiFi(M-ATX/LAN 1G+無線/註四年/2DIMM)", 2990),
    ("記憶體 RAM", "金士頓 32GB(16G×2) DDR5-5600 CL36 FURY Beast RGB 黑", 9100),
    ("固態硬碟 SSD", "威剛 XPG MARS 980Blade 1TB Gen5 讀14000/寫10000(五年)", 5999),
    ("顯示卡 VGA", "藍寶石 黑鑽版 RX7650GRE GAMING OC 8GB(三風扇/三年)", 7990),
    ("電源 PSU", "海韻 S12III-650W 銅牌/智慧溫控風扇(五年)", 1950),
]

def _est_rows():
    out = ""
    for cat, name, price in _EST_ITEMS:
        out += (
            '<tr>'
            '<td><input type="checkbox" class="est-inc" checked onchange="estCalc()"></td>'
            f'<td><input class="est-cat" value="{esc(cat)}"></td>'
            f'<td><input class="est-name" value="{esc(name)}"></td>'
            f'<td class="est-pcell"><input type="number" class="est-price" value="{price}" oninput="estCalc()"> 元</td>'
            '<td class="est-pcell"><input type="number" class="est-now" value="0" oninput="estCalc()"> 元</td>'
            '<td><button class="est-del" onclick="estDel(this)" title="刪除">✕</button></td>'
            '</tr>'
        )
    return out

_ESTIMATOR = '''
<section class="block">
  <h2>🛒 組裝估價器（點開使用）</h2>
  <p>把「現在價」填成<a href="https://www.coolpc.com.tw/evaluate.php" target="_blank" rel="noopener">原價屋</a>今天的價格，下面會<strong>即時算出一月總價、現在總價與價差</strong>，用來比較同規格現在變貴還是變便宜。</p>
  <div class="reveal" onclick="toggleAnswer(this)">▶ 打開組裝估價器</div>
  <div class="answer">
    <div class="callout"><span class="t">💡 使用說明</span>
    <p style="margin-bottom:0">預設放入的是<strong>老師 2026 年 1 月的實際配單</strong>（當時總報價 <strong>32,719 元</strong>，含稅）。<strong>「你的一月價」是當時的成交價；「現在價」請自己到<a href="https://www.coolpc.com.tw/evaluate.php" target="_blank" rel="noopener">原價屋</a>查今天同規格的價格填進去</strong>，下面會自動算出<strong>兩邊的總價與價差</strong>，就能比較同規格現在是變貴還是變便宜。（預設「現在價」先等於一月價，改了才會看到差額。）</p></div>
    <div class="estimator">
      <div class="table-wrap"><table class="est-table">
        <thead><tr><th>計入</th><th>類別</th><th>品項／規格</th><th>你的一月價</th><th>現在價（原價屋）</th><th></th></tr></thead>
        <tbody id="est-body">
''' + _est_rows() + '''
        </tbody>
      </table></div>
      <div class="est-bar">
        <button class="btn ghost" onclick="estAddRow()">＋ 新增品項</button>
        <div class="est-total">已計入 <span id="est-count">0</span> 項　·　一月總計：<span id="est-sum">0</span> 元　·　現在總計：<span id="est-now-sum">0</span> 元　·　價差：<span id="est-diff" class="est-diff">0</span></div>
      </div>
    </div>
  </div>
</section>'''

BODIES["unit06"] += _ESTIMATOR


# ---- 課堂互動工具（渲染在頁尾「先算再驗證」區）----
TOOLS = {
    "unit02": _conv_widget,
    "unit03": _gate_widget,
}
