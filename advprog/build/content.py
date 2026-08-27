# -*- coding: utf-8 -*-
"""10 個單元的內文（基本版草稿）。每個 uNN() 回傳完整的 <section class="unit-hero">…</section>
   加上後續所有 block，交給 common.page() 組成完整頁面。
   （改編自「資訊安全導論」課程網站的內容架構，套用到「進階程式設計」課程。
    Python 前導複習的單元編排參考「明道中學．資訊科技」課程網站的 Python 單元 8–14。）"""
from common import (esc, goals, callout, grid, tile, card, table_wrap, resource_link,
                     video_block, code_block, reveal_table, exercise,
                     two_options, block, hero, diagram_card, timeline)


def R(code, label="python"):
    return code_block(code, lang="python", label=label)


def T(code, label="終端機"):
    return code_block(code, lang="text", label=label)


def quizrow(code, answer_bool, answer_note):
    tf = "T" if answer_bool else "F"
    tf_word = "True" if answer_bool else "False"
    return ("""<div class="quizrow"><code>""" + esc(code) + """</code>"""
            """<button type="button" class="quiz-btn" """
            """onclick="var a=this.nextElementSibling;a.hidden=!a.hidden;"""
            """this.textContent=a.hidden?'\U0001f914 看答案':'\U0001f648 收起'">"""
            """\U0001f914 看答案</button>"""
            """<span class="quiz-ans" hidden>→ <span class=\"""" + tf + """\">""" + tf_word + """</span>：""" + answer_note + """</span></div>""")


# =================================================================
# Part 1 · 課程總覽（單元 1）
# =================================================================

def u01():
    h = hero("unit01")
    g = goals([
        "認識這學期的學習地圖：Python 複習 → Vibe Coding 體驗 → pandas → Matplotlib → 專題實作 → 成果發表",
        "預先了解期末專題的樣子與評量方式，建立學習的目標感",
        "學會安裝與基本操作 VS Code，作為這學期所有課程的開發工具",
        "看過一份學長姐的專題範例，知道「做得好」大概是什麼樣子",
    ])

    s1 = block(1, "這學期的學習地圖", """
<p>這門課是「進階程式設計」的其中一段旅程：我們會先花一點時間把 Python 基礎複習一輪，接著用一次很不一樣的方式體驗程式開發——Vibe Coding，最後把重心放在資料分析最實用的兩個工具：<strong>pandas</strong>（整理資料）與 <strong>Matplotlib</strong>（畫出資料）。整學期的內容，最終都會匯集成你自己的一份專題作品。</p>
""" + timeline([
        ("單元 2–4", "Python 前導複習"),
        ("單元 5", "Vibe Coding 體驗：pygame 小遊戲"),
        ("單元 6", "pandas 基礎操作"),
        ("單元 7", "Matplotlib 基本使用"),
        ("單元 8–10", "專題實作與發表"),
    ]) + """
<p style="margin-top:14px">前面單元學到的每一項技能，最後都會用在同一件事情上：<strong>做出一份你自己的資料分析專題</strong>。</p>
""")

    s2 = block(2, "期末專題預告", """
<p>這學期最終的成果，會是一份<strong>你自己選題、自己動手做</strong>的資料視覺化專題，整個流程大致是這樣：</p>
""" + grid(2, [
        tile("1️⃣", "到政府公開資料平台找資料", "選一個你有興趣的主題（例如空氣品質、超商分布、電影票房、人口變化⋯），到政府公開資料平台下載相關的原始資料。"),
        tile("2️⃣", "用 pandas 整理資料", "讀取資料、檢視欄位、篩選與清理，把原始資料整理成可以分析的表格。"),
        tile("3️⃣", "用 Matplotlib 做視覺化分析", "依資料的特性選擇合適的圖表（折線／長條／圓餅⋯），畫出至少兩種圖表，並寫下你的觀察與解讀。"),
        tile("4️⃣", "整理成一份 PDF 專題報告", "把「資料來源、分析過程、圖表、結論」整理成一份 PDF，並上台做簡短發表。"),
    ]) + """
<div class="callout tip"><span class="t">💡 現在還不用會，先有個印象就好</span>
<p>接下來的每個單元，都是在為這份專題累積能力——現在你可能還看不懂圖表怎麼畫、資料怎麼抓，但走到單元 8 的時候，你會發現自己其實已經準備好了。</p></div>
""")

    s3 = block(3, "專題範例參觀", """
<p>先看一份範例，讓你對「做得好的專題」有一點畫面。這是用政府公開的景氣指標資料，畫出領先、同時、落後指標長期走勢的折線圖分析：</p>
""" + grid(1, [
        resource_link("📄", "範例作品：景氣指標綜合分析",
                       "assets/examples/景氣指標綜合分析.pdf",
                       "用政府公開的景氣指標資料，畫出領先／同時／落後指標的長期趨勢折線圖，並搭配文字說明資料的走勢與意義——資料來源、程式碼、圖表、解讀一應俱全，是很好的格式參考。"),
    ]) + """
<p style="margin-top:18px">下面這四份，是學長姐這學期實際繳交的專題成果，主題各不相同，可以看看他們怎麼選題、怎麼設計圖表、遇到問題怎麼解決。</p>
<div class="callout tip"><span class="t">🌟 老師特別推薦：中油太陽能案場分析</span>
<p>這份是目前看過完成度最高的一份——用「玫瑰圖」呈現各案場的發電效率、用地圖畫出案場的地理分布與發電量、用長條圖比較各縣市的發電量，還進一步用「等效發電效率」的概念，找出效率好但產出少的案場，以及可能需要維護的異常案場。從圖表設計的思考過程到挑戰反思，寫得非常完整，很值得參考。</p>
<p style="margin-top:10px">特別是「挑戰反思與學習」的部分，把整個專題過程中卡關的地方講得很具體，不是隨便帶過：</p>
<ul class="tidy">
  <li><strong>問題意識的缺乏</strong>——一開始是為了學畫圖表而做，不是真的從資料分析出發；後來調整思路，才發現這組資料真正需要的是玫瑰圖而不是圓餅圖，也因此學到「目標導向思考」與「數據轉譯與洞察」的能力。</li>
  <li><strong>程式可複製性缺乏</strong>——一開始每個人畫圖的方式、資料匯入方式都不一樣，很難互相套用；後來把解決問題的程式模組分享到群組讓大家直接套用，體會到「低耦合、高內聚」的模組化設計精神。</li>
  <li><strong>團隊溝通的缺乏</strong>——一開始各自研究、缺乏進度共享，導致重複做工、浪費時間；後來改成同步在群組反映問題並動態分工，學到即時溝通、彈性調整分工的敏捷開發習慣。</li>
  <li><strong>技術面的小坑</strong>——例如日發電量與月發電量的數值差距太大，畫在同一張圖上完全看不出日發電量的變化，後來查到要用 <code>twinx()</code> 另外建立第二條 Y 軸；地圖一開始會把整個台灣都畫出來，後來用 <code>plt.xlim()</code> / <code>plt.ylim()</code> 限制經緯度範圍，才聚焦到南部三個案場所在的縣市。</li>
</ul>
</div>
""" + grid(1, [
        resource_link("📄", "範例作品：中油太陽能案場分析",
                       "assets/examples/中油太陽能案場分析.pdf",
                       "以政府公開資料分析南部三縣市加油站太陽能案場的發電量，結合玫瑰圖、地理散點圖、長條圖等多種視覺化方式，並用「等效發電效率」找出表現異常的案場。"),
    ]) + """
<p style="margin-top:18px">另外三份主題也各有特色，同樣值得一看：</p>
""" + grid(2, [
        resource_link("📄", "台中市充電槍座標與統計資料",
                       "assets/examples/台中市充電槍座標與統計資料.pdf",
                       "用政府開放資料畫出台中市充電樁的座標分布圖與各行政區數量統計，過程中遇到座標系統、字體、套件版本等問題，除錯過程記錄得很真實。"),
        resource_link("📄", "2024台灣PM2.5濃度數據分析與地理視覺化",
                       "assets/examples/2024台灣PM2.5濃度數據分析與地理視覺化.pdf",
                       "用一整年、逐月的空氣品質測站資料，畫出 PM2.5 濃度的地理分布散點圖，並討論季節變化背後可能的成因。"),
        resource_link("📄", "勞工職業災害保險投保人數分析",
                       "assets/examples/勞工職業災害保險投保人數分析.pdf",
                       "比較各地區、各薪資級距的職災保險投保人數趨勢，並誠實反思了圖表在呈現極端值時的不足之處。"),
    ]) + """
<div class="callout"><span class="t">🙈 關於範例中的姓名</span>
<p>為保護學生隱私，以上範例作品中出現的學生姓名，都已依照「王O翔」的方式處理過（保留姓氏與名字最後一字，中間字改為 O），不影響閱讀報告內容。</p></div>

<div class="callout tip"><span class="t">🔎 想找自己的專題資料？從這裡挖</span>
<p>政府公開資料平台 <a href="https://data.gov.tw/" target="_blank" rel="noopener">data.gov.tw</a> 上有非常多不同領域的資料集，想分析什麼資料，就去這邊挖！<strong>建議可以找和你未來想念的科系相關的資料來做分析</strong>——例如想念資工的可以找科技相關資料、想念護理的可以找公衛或醫療資源資料、想念財金的可以找景氣或金融相關資料，這樣專題做完，也順便更了解那個領域一點。</p>
<p style="margin-top:10px">PS　我們這堂課主軸教學的是<strong>程式碼</strong>的部分；資料統整以及資料解讀，需要額外請教老師，或是自主學習喔。</p>
</div>

<div class="callout"><span class="t">📬 範例持續更新中</span>
<p>之後只要看到不錯的專題成果，老師都會陸續整理、補充在這一頁，讓大家有更多不同主題的參考。</p></div>
""")

    s4 = block(4, "開發工具：VS Code", """
<p>這學期我們統一使用 <strong>VS Code</strong>（Visual Studio Code）當作開發工具，它是目前業界與教學都最常用的免費程式編輯器。</p>
""" + grid(2, [
        tile("⬇️", "安裝 VS Code", "到 code.visualstudio.com 下載安裝，並確認電腦已安裝 Python（可從 python.org 下載）。"),
        tile("🧩", "安裝 Python 延伸套件", "在 VS Code 左側「Extensions」搜尋 <code>Python</code>（Microsoft 出的），安裝後才有語法提示與執行按鈕。"),
        tile("⌨️", "打開終端機", "功能表「Terminal → New Terminal」，或快捷鍵 <code>Ctrl</code>+<code>`</code>，之後安裝套件（如 pandas）都在這裡輸入指令。"),
        tile("▶️", "建立並執行 .py 檔", "新增一個 <code>xxx.py</code> 檔案，寫完程式後按右上角的 ▶ 執行鈕，或在終端機輸入 <code>python xxx.py</code>。"),
    ]) + """
""" + R("""print("Hello, 進階程式設計！")
print("這是我用 VS Code 執行的第一支程式。")""") + """
""")

    s5 = block(5, "評量方式", """
<p>這門課的評量方式很單純：</p>
""" + table_wrap(["項目", "次數", "配分"], [
        ["平時成績", "1 次", "20%"],
        ["作業", "1 次", "80%"],
    ]) + """
<p style="margin-top:14px"><strong>作業，就是專題。</strong>沒有另外的小考或隨堂測驗，你這學期最主要的產出，就是一份你自己做出來的專題。</p>

<div class="callout tip"><span class="t">🗓️ 上學期 vs 下學期，節奏不一樣</span>
<p><strong>上學期</strong>的「作業」是複習 Python 的程式碼——最終要手打出一份作業，再加上 Vibe Coding 的 pygame 小遊戲。</p>
<p style="margin-top:6px"><strong>下學期</strong>大家考完學測之後，才會正式開始製作期末專題（也就是單元 8–10 教的：找資料、用 pandas + Matplotlib 分析、整理成 PDF 報告）。</p>
</div>

<div class="callout"><span class="t">📌 這學期比較特別的地方</span>
<p>上學期同時會有兩門課：老師這邊的「進階程式設計」，還有<strong>順陞工程師</strong>教的 SQL。上面這張評量表，只占你上學期總成績的 <strong>50%</strong>，另外 50% 來自 SQL 那門課，兩邊的成績會合併計算。</p>
</div>
""")

    s6 = block(6, "課堂約定", callout("🤝 一起把這堂課上好", """
<ul class="tidy">
  <li>遇到紅字錯誤訊息不要慌——那是電腦在告訴你「哪裡怪怪的」，把錯誤訊息完整看完，通常答案就在裡面。</li>
  <li>可以善用 AI 工具協助除錯與學習，但要看得懂自己貼上去的程式碼在做什麼。</li>
  <li>作業與練習誠實完成，卡關時主動提問，比自己硬憋更快進步。</li>
  <li>專題主題盡早想、資料盡早找，越早開始遇到的坑越有時間解決。</li>
</ul>"""))

    ex = exercise("課前小暖身", """
<p>先不用寫程式，動動腦就好：想想看，有沒有什麼你平常就很好奇的「數據類」問題？例如「我們縣市的空氣品質是不是越來越差？」「最近哪些電影賣最好？」「超商到底哪一家開最多間？」把 2–3 個你感興趣的題目寫下來，之後找專題主題時會用得上。</p>
""")

    return h + g + s1 + s2 + s3 + s4 + s5 + s6 + ex


# =================================================================
# Part 2 · Python 前導複習（單元 2-4）
# =================================================================

def u02():
    h = hero("unit02")
    g = goals([
        "能在 VS Code 建立並執行一支 .py 程式",
        "能正確宣告變數，並遵守變數命名規則",
        "認識 int／float／bool／str／list／dict 等基本資料型態，並用 type() 查詢",
        "能做型別轉換（casting），並用 f-string 做格式化輸出",
    ])

    s1 = block(1, "先動手：VS Code 快速上手", """
<p>這三個單元是「複習」，節奏會比較快，重點放在動手寫、動手跑。先確認你能完成這個流程：</p>
""" + grid(2, [
        tile("📁", "建立資料夾", "在桌面或文件夾建立一個 <code>python_review</code> 資料夾，之後的程式都存在這裡。"),
        tile("📄", "新增 .py 檔", "在 VS Code 開啟這個資料夾，新增 <code>review01.py</code>。"),
        tile("▶️", "執行程式", "存檔後按右上角 ▶，或在終端機輸入 <code>python review01.py</code>。"),
        tile("🔁", "邊改邊跑", "改一行、存檔、再執行一次，養成「小步快跑」的習慣，比一次寫完整支程式再測試更容易抓到問題。"),
    ]) + """
""")

    s2 = block(2, "變數 Variable", """
<p>變數用來<strong>存放資料</strong>，可以想成一個貼了名字的箱子：用指定運算子 <code>=</code> 把右邊的值放進左邊的箱子。</p>
""" + R("""x = 1
print(x)          # 1

a = b = c = 20    # 一次把 20 指定給 a、b、c
age, name = 17, "小明"   # 同時指定不同的值

a = 10
a = a + 5         # 取出 a、加 5、再存回 a
print(a)          # 15""") + """
<h3>命名規則</h3>
<ul class="tidy">
  <li>首字必須是字母、底線 <code>_</code> 或中文，其後可加數字。</li>
  <li>區分大小寫：<code>age</code> 與 <code>Age</code> 是不同變數。</li>
  <li>不能使用 Python 保留字（如 <code>if</code>、<code>for</code>）當變數名。</li>
  <li>盡量避免用內建函式名稱當變數（如 <code>list</code>、<code>str</code>、<code>print</code>），否則會把它的原本功能蓋掉。</li>
</ul>
""" + table_wrap(["合法命名 ✅", "不合法命名 ❌", "為什麼不合法"], [
        ["<code>score</code>", "<code>2score</code>", "首字不能是數字"],
        ["<code>total_price</code>", "<code>total price</code>", "名稱中不能有空白"],
        ["<code>my_list</code>", "<code>list</code>", "與內建函式同名，會蓋掉原本功能"],
    ]))

    s3 = block(3, "資料型態 Data Type", """
<p>用 <code>type()</code> 可以查看某個值是什麼型別：</p>
""" + table_wrap(["分類", "型別", "說明", "範例"], [
        ["數值型", "<code>int</code> 整數", "沒有小數點", "<code>1</code>、<code>-20</code>"],
        ["數值型", "<code>float</code> 浮點數", "帶小數點", "<code>1.5</code>、<code>3.14</code>"],
        ["數值型", "<code>bool</code> 布林值", "只有真／假兩種", "<code>True</code>、<code>False</code>"],
        ["字串型", "<code>str</code> 字串", "用引號括住的文字", "<code>\"Hello\"</code>"],
        ["容器型", "<code>list</code> 串列", "一串有順序的資料", "<code>[1, 2, 3]</code>"],
        ["容器型", "<code>dict</code> 字典", "「鍵 → 值」對應的資料", "<code>{\"name\": \"小明\"}</code>"],
    ]) + """
""" + R("""x = 1
print(x, type(x))          # int

y = 1.5
print(y, type(y))          # float

flag = True
print(flag, type(flag))    # bool

name = "小明"
print(name, type(name))    # str""") + """
<div class="callout tip"><span class="t">🔎 動態型別</span>
<p>Python 是<strong>動態型別</strong>：型態由「指派的值」決定，同一個變數之後可以改放不同型態的值，不需要事先宣告。</p>
""" + R("""a = 10
print(a, type(a))   # int
a = 3.2
print(a, type(a))   # float —— 同一個 a，型別跟著「值」改變
a = "換成字串了"
print(a, type(a))   # str""") + """</div>
""")

    s4 = block(4, "型別轉換 Casting", """
<p>把一個值從一種型態轉成另一種，稱為<strong>轉型（casting）</strong>：</p>
""" + table_wrap(["函式", "作用", "例子"], [
        ["<code>int(x)</code>", "轉成整數（小數<strong>直接捨去</strong>）", "<code>int(3.9)</code> → <code>3</code>"],
        ["<code>float(x)</code>", "轉成浮點數", "<code>float(5)</code> → <code>5.0</code>"],
        ["<code>bool(x)</code>", "轉成布林值", "<code>bool(0)</code> → <code>False</code>"],
        ["<code>str(x)</code>", "轉成字串", "<code>str(100)</code> → <code>\"100\"</code>"],
    ]) + """
""" + R("""x = 54.87
y = int(x)
print(x)   # 54.87
print(y)   # 54  （.87 被直接丟掉，不是四捨五入！）""") + """
<p>💭 <strong>先自己猜猜看：</strong>下面這幾行 <code>bool()</code> 會印出 <code>True</code> 還是 <code>False</code>？</p>
""" + quizrow('print(bool(""))', False, "空字串（裡面完全沒有字）算 False。") + """
""" + quizrow("print(bool(0))", False, "數字 0 算 False。") + """
""" + quizrow('print(bool("False"))', True, "小心陷阱！<code>\"False\"</code> 是「非空字串」，只要字串裡有字就是 True，跟裡面寫的字是不是「False」無關。") + """
<div class="callout"><span class="t">規則</span>
<p>空字串、<code>0</code>、<code>None</code>（還有空的容器，如 <code>[]</code>、<code>{}</code>）會是 <code>False</code>；其餘全部都是 <code>True</code>。</p></div>
""")

    s5 = block(5, "格式化輸出：f-string", """
<p>要把變數的值「排版」進一段文字裡，最方便的方式是 <strong>f-string</strong>：在字串前面加上 <code>f</code>，用 <code>{變數}</code> 把值嵌進去。</p>
""" + R("""name = "小明"
age = 17
score = 88.666

print(f"我是{name}，今年{age}歲。")
print(f"我的分數是{score:.1f}分")   # :.1f 保留小數點後 1 位 → 88.7分""") + """
<div class="callout tip"><span class="t">💡 小技巧：:.1f／:.2f</span>
<p><code>{變數:.1f}</code> 表示四捨五入到小數點後 1 位，<code>.2f</code> 就是 2 位，畫圖表、算平均分數時非常常用。</p></div>
""")

    ex = exercise("小挑戰", """
<ol>
  <li>用 <code>input()</code> 讀取使用者輸入的姓名與年齡（年齡記得轉成 <code>int</code>）。</li>
  <li>用 f-string 印出一句自我介紹，例如「我是小明，今年 17 歲」。</li>
  <li>算出「10 年後的年齡」並印出來。</li>
</ol>""", """
""" + R("""name = input("你的名字是？")
age = int(input("你的年齡是？"))

print(f"我是{name}，今年{age}歲。")
print(f"10 年後我 {age + 10} 歲。")"""))

    return h + g + s1 + s2 + s3 + s4 + s5 + ex


def u03():
    h = hero("unit03")
    g = goals([
        "能正確使用算術、比較、邏輯與複合指定運算子",
        "能寫出 if、if-else、if-elif-else 條件判斷",
        "能用 and／or／not 組合多個條件",
    ])

    s1 = block(1, "運算子 Operator", """
""" + table_wrap(["類別", "運算子", "說明"], [
        ["算術運算子", "<code>+ - * / // % **</code>", "加、減、乘、除、整數除、取餘數、次方"],
        ["比較運算子", "<code>== != > < >= <=</code>", "回傳 <code>True</code>／<code>False</code>"],
        ["邏輯運算子", "<code>and or not</code>", "組合多個條件"],
        ["複合指定運算子", "<code>+= -= *= /=</code>", "「先運算、再存回自己」的簡寫"],
    ]) + """
""" + R("""a = 7
print(a // 2)   # 3   整數除（無條件捨去）
print(a % 2)    # 1   取餘數
print(a ** 2)   # 49  7 的平方

score = 88
score += 2       # 等同 score = score + 2
print(score)     # 90

print(3 > 2 and 5 > 4)   # True：兩個條件都成立
print(3 > 2 or 1 > 4)    # True：至少一個成立
print(not (3 > 2))       # False：把 True 反過來""") + """
""" + quizrow("print(10 % 3 == 1)", True, "10 除以 3 餘 1，1 == 1 為 True。") + """
""" + quizrow("print(5 > 3 and 2 > 3)", False, "5 > 3 是 True，但 2 > 3 是 False，and 要兩個都 True 才成立。") + """
""")

    s2 = block(2, "單向判斷 if", """
<p>條件成立（True）才執行縮排內的程式碼：</p>
""" + R("""score = 85
if score >= 60:
    print("及格了！")
print("程式繼續往下跑")""") + """
<div class="callout warn"><span class="t">⚠ 縮排很重要</span>
<p>Python 用<strong>縮排</strong>（通常是 4 個空白）來表示「這行屬於 if 底下」，縮排錯了程式邏輯就會跑掉，甚至直接報錯。</p></div>
""")

    s3 = block(3, "雙向判斷 if–else", """
""" + R("""score = 55
if score >= 60:
    print("及格了！")
else:
    print("不及格，再加油！")""") + """
""")

    s4 = block(4, "多向判斷 if–elif–else", """
<p>有多個條件要依序檢查時，用 <code>elif</code>（else if 的縮寫）：</p>
""" + R("""score = 76

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"分數 {score} 分，等第是 {grade}")""") + """
<div class="callout tip"><span class="t">💡 由上往下、符合第一個就停</span>
<p><code>elif</code> 會<strong>由上往下依序檢查</strong>，一旦符合某一條就執行該區塊、不再往下比對。所以條件通常要「由嚴格排到寬鬆」，順序寫反答案就會錯。</p></div>
""")

    ex = exercise("課堂練習：分數等第判斷", """
<p>寫一支程式：用 <code>input()</code> 讀入一個 0–100 的分數（記得轉成 <code>int</code>），依照下表印出等第與是否及格：</p>
""" + table_wrap(["分數範圍", "等第"], [
        ["90 以上", "A"], ["80–89", "B"], ["70–79", "C"], ["60–69", "D"], ["60 以下", "F（不及格）"],
    ]), """
""" + R("""score = int(input("請輸入分數："))

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

result = "及格" if score >= 60 else "不及格"
print(f"等第：{grade}（{result}）")"""))

    return h + g + s1 + s2 + s3 + s4 + ex


def u04():
    h = hero("unit04")
    g = goals([
        "能用 for 迴圈搭配 range() 重複執行程式",
        "能用 while 迴圈寫出條件式重複，並使用 break／continue",
        "能定義函式、傳入參數、使用回傳值",
        "能分辨區域變數與全域變數的差異",
    ])

    s1 = block(1, "for 迴圈", """
""" + R("""for i in range(5):
    print(i)          # 0 1 2 3 4

total = 0
for i in range(1, 101):   # 1~100
    total += i
print(f"1 加到 100 的總和是 {total}")

fruits = ["蘋果", "香蕉", "芭樂"]
for f in fruits:
    print(f"我喜歡吃{f}")""") + """
""")

    s2 = block(2, "while 迴圈與 break／continue", """
""" + R("""n = 1
while n <= 5:
    print(n)
    n += 1     # 別忘記讓條件有機會變成 False，不然會無窮迴圈！

# break：符合條件就直接跳出整個迴圈
for i in range(10):
    if i == 5:
        break
    print(i)          # 0 1 2 3 4

# continue：符合條件就跳過這一輪，繼續下一輪
for i in range(6):
    if i % 2 == 0:
        continue
    print(i)          # 1 3 5（跳過偶數）""") + """
""")

    s3 = block(3, "函式 Function", """
<p>函式可以把「一段常用的邏輯」包裝起來，重複呼叫、不用重複寫：</p>
""" + R("""def calc_average(scores):
    return sum(scores) / len(scores)

my_scores = [88, 92, 76, 84]
avg = calc_average(my_scores)
print(f"平均分數：{avg:.1f}")""") + """
<h3>區域變數 vs 全域變數</h3>
""" + R("""x = 10          # 全域變數：整支程式都看得到

def show():
    x = 99      # 這是函式「內部」的區域變數，跟外面的 x 是不同的箱子
    print(f"函式內的 x = {x}")

show()
print(f"函式外的 x = {x}")   # 還是 10，沒有被函式內部影響""") + """
""")

    ex = exercise("綜合練習", """
<p>寫一個函式 <code>find_max(nums)</code>，<strong>不能用內建的 <code>max()</code></strong>，自己用迴圈找出串列中的最大值並回傳。</p>
""", """
""" + R("""def find_max(nums):
    biggest = nums[0]
    for n in nums:
        if n > biggest:
            biggest = n
    return biggest

print(find_max([23, 88, 5, 61, 40]))   # 88""") + """
<p style="margin-top:12px">👀 這種「一個一個掃過去、邊比較邊記錄」的寫法，之後在 pandas 裡只要一個 <code>.max()</code> 就搞定了——下一個單元就會看到！</p>
""")

    wrap = """<p style="margin-top:10px;color:var(--text-soft)">Python 語法複習到這裡告一段落。接下來，我們要進入一個很不一樣的體驗——<strong>Vibe Coding</strong>，用 AI 協作打造一款屬於你自己的 pygame 小遊戲！</p>"""

    return h + g + s1 + s2 + s3 + ex + wrap


# =================================================================
# Part 3 · Vibe Coding 體驗（單元 5）
# =================================================================

def u05():
    h = hero("unit05")
    g = goals([
        "理解 Vibe Coding 的核心精神：描述需求 → AI 生成 → 執行測試 → 對話除錯",
        "能在 VS Code 安裝 pygame 並執行一支會動的遊戲視窗程式",
        "能用 Vibe Coding 的方式，請 AI 幫你的小遊戲迭代加入至少一個新功能",
        "培養「AI 生成的程式碼，要看得懂再用」的協作態度",
    ])

    s1 = block(1, "什麼是 Vibe Coding？", callout("🎮 用「感覺」寫程式，而不是逐行手刻", """
<p><strong>Vibe Coding</strong> 是這幾年因為 AI 程式助理（如 ChatGPT、Claude、GitHub Copilot）興起的一種開發方式：你不用把每一行語法都背得滾瓜爛熟，而是<strong>用自然語言描述你想要的東西</strong>，讓 AI 幫你生成程式碼，你負責執行、測試、判斷「對不對、好不好」，再用白話文請 AI 修改。</p>
<p>這不是偷懶，而是現在業界工程師真實在用的協作方式——但前提是：你要看得懂 AI 給你的程式碼在做什麼，才有辦法判斷它對不對、抓出問題在哪裡。今天我們就用一款 pygame 小遊戲，體驗一次完整的 Vibe Coding 流程。</p>"""))

    s2 = block(2, "事前準備", """
""" + grid(3, [
        tile("📦", "安裝 pygame", "在 VS Code 終端機輸入下面的指令安裝遊戲開發套件："),
        tile("🤖", "準備一個 AI 對話工具", "Claude、ChatGPT 或其他你熟悉的 AI 助理，開一個新對話視窗。"),
        tile("📁", "建立專案資料夾", "新增 <code>vibe_game</code> 資料夾，裡面放一個 <code>main.py</code>。"),
    ]) + """
""" + T("pip install pygame") + """
""")

    s3 = block(3, "Vibe Coding 的四個步驟", """
""" + grid(4, [
        tile("①", "描述你想要的遊戲", "用一段話講清楚：主角是什麼、怎麼操作、目標是什麼、贏或輸的條件。"),
        tile("②", "請 AI 生成完整程式碼", "把描述貼給 AI，請它直接給你一份「可以執行」的完整程式碼。"),
        tile("③", "貼到 VS Code 執行測試", "存成 <code>main.py</code>，執行看看，實際玩玩看有沒有照你想的運作。"),
        tile("④", "用白話文請 AI 除錯／加功能", "有錯誤訊息就整段貼給 AI；想加功能就直接說「幫我加上⋯」，然後回到步驟③再測一次。"),
    ]) + """
<p style="margin-top:12px">③ 和 ④ 會反覆循環好幾次——這就是 Vibe Coding 的精神：<strong>小步快跑、邊玩邊改</strong>，而不是一次就要求 AI 生出完美成品。</p>
""" + """<div class="ai-demo">
  <span class="chat u">幫我寫一個 pygame 小遊戲：一個方塊可以用方向鍵移動，畫面上有一顆紅點，方塊碰到紅點就加 1 分，紅點消失後在隨機位置重新出現。</span>
  <span class="chat b">好的，這是一份可以直接執行的完整程式碼：<br>import pygame, random ⋯（完整程式碼如下）</span>
  <span class="chat u">執行後出現 <code>pygame.error: No available video device</code>，這是什麼意思？</span>
  <span class="chat b">這通常代表執行環境沒有畫面輸出。請確認是在自己電腦的 VS Code 執行，而不是在雲端終端機執行 pygame 視窗程式喔。</span>
</div>
""")

    s4 = block(4, "起手範例：會動的 pygame 小遊戲", """
<p>就算你今天 AI 工具不方便使用，也可以直接用這份範例當作起點——它是一個可以用方向鍵移動方塊、吃到紅點加分的小遊戲骨架：</p>
""" + R("""import pygame
import random

pygame.init()
WIDTH, HEIGHT = 480, 360
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("吃紅點小遊戲")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 32)

player = pygame.Rect(WIDTH // 2, HEIGHT // 2, 30, 30)
speed = 5
score = 0

def new_dot():
    return pygame.Rect(random.randint(0, WIDTH - 16), random.randint(0, HEIGHT - 16), 16, 16)

dot = new_dot()
running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= speed
    if keys[pygame.K_RIGHT]:
        player.x += speed
    if keys[pygame.K_UP]:
        player.y -= speed
    if keys[pygame.K_DOWN]:
        player.y += speed

    if player.colliderect(dot):
        score += 1
        dot = new_dot()

    screen.fill((30, 30, 30))
    pygame.draw.rect(screen, (234, 88, 12), player)
    pygame.draw.ellipse(screen, (220, 40, 40), dot)
    text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(text, (10, 10))
    pygame.display.flip()

pygame.quit()""") + """
""")

    s5 = block(5, "迭代任務：向 AI 提出下一個需求", """
<p>選 1–2 個你想要的功能，用「描述需求 → 請 AI 修改 → 執行測試」的方式加進你的小遊戲：</p>
""" + grid(3, [
        tile("⏱️", "加上倒數計時", "限時 30 秒，時間到就結束遊戲並顯示最終分數。"),
        tile("🏆", "加上最高分紀錄", "遊戲結束時比較這次分數與歷史最高分，並顯示出來。"),
        tile("🎨", "換掉外觀", "把方塊換成你喜歡的顏色，或用圖片取代方塊與紅點。"),
        tile("🧱", "加上障礙物", "畫面上多幾個不能穿越的方塊，增加遊戲難度。"),
        tile("🔊", "加上音效", "吃到紅點時播放一個提示音（<code>pygame.mixer</code>）。"),
        tile("🚀", "自由發揮", "任何你想加的功能都可以，重點是練習「向 AI 提需求」的過程。"),
    ]) + """
""")

    s6 = block(6, "使用 AI 協作的提醒", callout("🧭 看得懂再用", """
<ul class="tidy">
  <li>AI 給的程式碼<strong>先讀過一遍</strong>，猜猜看每一段在做什麼，再執行——這樣出錯時你才知道從哪裡下手。</li>
  <li>遇到報錯訊息，把<strong>完整的錯誤訊息</strong>複製貼給 AI，比只說「壞掉了」更容易得到有用的答案。</li>
  <li>AI 偶爾也會寫錯或給過時的用法，執行結果才是最終判斷標準，不要照單全收。</li>
</ul>"""))

    ex = exercise("挑戰任務", """
<p>用 Vibe Coding 的方式，為你的小遊戲<strong>至少加入一個新功能</strong>，並能簡短說明：你請 AI 加的是什麼功能？中間有沒有出現錯誤訊息？你是怎麼跟 AI 溝通解決的？</p>
""")

    return h + g + s1 + s2 + s3 + s4 + s5 + s6 + ex


# =================================================================
# Part 4 · pandas 應用（單元 6）
# =================================================================

def u06():
    h = hero("unit06")
    g = goals([
        "能安裝 pandas 並在 VS Code 執行含 pandas 的程式",
        "能建立與操作 Series（單維度資料）：運算、觀察、存取、增刪",
        "能建立與操作 DataFrame（雙維度資料）：取欄、取列、取值",
        "能分辨 Series 與 DataFrame 的差異，為專題資料分析做準備",
    ])

    s1 = block(1, "安裝 pandas", """
<p>在 VS Code 的終端機（<code>Ctrl</code>+<code>`</code>）輸入：</p>
""" + T("pip install pandas") + """
<p>安裝完成後，就可以在程式最上面用 <code>import pandas as pd</code> 載入它了。</p>
""")

    s2 = block(2, "Series：單維度的資料", """
<p>Series 就像 Excel 中<strong>直向的一欄資料</strong>。</p>
<h3>建立 Series</h3>
""" + R("""import pandas as pd

data = pd.Series([10, 20, 30])
print(data)""") + """
<h3>使用 Series</h3>
""" + R("""import pandas as pd

data = pd.Series([10, 20, 30])
print(data.max())      # 找到最大值 → 30
print(data.median())   # 計算中位數 → 20
data = data * 2         # 放大兩倍
print(data)             # 0:20  1:40  2:60""") + """
<h3>觀察資料</h3>
""" + R("""import pandas as pd

data = pd.Series([10, 20, 30])
print(data.dtype)   # 資料型態
print(data.size)    # 資料筆數
print(data.index)   # 資料的索引""") + """
<h3>取得資料</h3>
<p>可以依「順序」或依「索引」取值：</p>
""" + R("""import pandas as pd

data = pd.Series([10, 20, 30], index=["a", "b", "c"])
print(data[0])     # 依順序：10
print(data["c"])   # 依索引：30""") + """
<h3>資料增刪</h3>
""" + R("""import pandas as pd

data1 = pd.Series([10, 20, 30])
data2 = pd.Series([40, 50])

data1 = pd.concat([data1, data2])                     # 新增資料（索引值不連續）
data1 = pd.concat([data1, data2], ignore_index=True)  # 新增資料（索引值重新排列，連續）

data1.drop([5], inplace=True)          # 刪除索引為 5 的資料
data1 = data1.reset_index(drop=True)   # 重新整理索引
print(data1)""") + """
<h3>數字運算</h3>
""" + table_wrap(["方法", "說明"], [
        ["<code>data.sum()</code>", "總和"],
        ["<code>data.max()</code> / <code>data.min()</code>", "最大值／最小值"],
        ["<code>data.prod()</code>", "乘法總和"],
        ["<code>data.mean()</code> / <code>data.median()</code>", "平均／中位數"],
        ["<code>data.std()</code>", "標準差"],
        ["<code>data.nlargest(n)</code> / <code>data.nsmallest(m)</code>", "取前 n 大／前 m 小的數字"],
    ]) + """
<h3>字串運算</h3>
<p>字串相關操作都定義在 <code>.str</code> 底下：</p>
""" + table_wrap(["方法", "說明"], [
        ["<code>data.str.lower()</code> / <code>.upper()</code>", "全部轉小寫／大寫"],
        ["<code>data.str.len()</code>", "每個字串的長度"],
        ["<code>data.str.cat(sep=\",\")</code>", "把每個字串用逗號串起來"],
        ["<code>data.str.contains(\"P\")</code>", "判斷字串是否包含 P"],
        ["<code>data.str.replace(\"你好\", \"Hello\")</code>", "用 Hello 取代「你好」"],
    ]))

    s3 = block(3, "DataFrame：雙維度的資料", """
<p>DataFrame 就像一個<strong>表格</strong>，有「欄」與「列」的概念。</p>
<h3>建立 DataFrame</h3>
""" + R("""import pandas as pd

data = pd.DataFrame({"name": ["jeff", "emma"], "age": [10, 15]})
print(data)""") + """
<h3>取得前後筆資料</h3>
""" + R("""data.head(3)   # 取得最前面 3 筆資料
data.tail(3)   # 取得最後面 3 筆資料""") + """
<h3>取得特定欄（直向）</h3>
""" + R("""data["name"]   # 取得「name」這一欄""") + """
<h3>取得特定列（橫向）</h3>
""" + R("""data.iloc[0]   # 根據「順序」取一整列（第 1 列）
data.loc[0]    # 根據「索引」取一整列""") + """
<div class="callout tip"><span class="t">💡 iloc 跟 loc 差在哪？</span>
<p><code>iloc</code> 看的是「第幾個」（永遠是 0, 1, 2 ⋯的順序），<code>loc</code> 看的是「索引標籤」本身——如果資料的索引被重新排過或不是預設的 0,1,2⋯，兩者取到的結果可能不一樣，要特別小心。</p></div>
<h3>取得單一值</h3>
""" + R("""data.at[0, "name"]    # 根據列索引與欄位名稱，取得單一值
data.iat[0, 0]        # 根據列與欄的「順序」，取得單一值""") + """
<h3>資料的索引</h3>
<p>索引（Index）就像 Excel 最左邊那一排編號，每一列資料都對應一個索引值，可以用它來精準定位一列資料。</p>
""")

    s4 = block(4, "小結", """
""" + grid(1, [
        resource_link("📚", "pandas 官方文件", "https://pandas.pydata.org/", "遇到沒教過的功能，第一個查詢的地方。"),
    ]) + """
<p style="margin-top:10px">Series 是「一直欄」，DataFrame 是「一整張表」——你下載下來的政府開放資料，通常一讀進來就是 DataFrame，而 DataFrame 裡的每一欄，其實就是一個 Series。</p>
""")

    ex = exercise("課堂練習", """
<p>用 <code>pd.DataFrame</code> 建立一個含有 3 位同學姓名與分數的表格，印出「平均分數」與「最高分同學的姓名」。</p>
""", """
""" + R("""import pandas as pd

data = pd.DataFrame({
    "name": ["小明", "小華", "小美"],
    "score": [88, 95, 76],
})

print("平均分數：", data["score"].mean())

top_row = data.loc[data["score"].idxmax()]
print("最高分同學：", top_row["name"])"""))

    return h + g + s1 + s2 + s3 + s4 + ex


# =================================================================
# Part 5 · Matplotlib 基本使用（單元 7）
# =================================================================

def u07():
    h = hero("unit07")
    g = goals([
        "能匯入 matplotlib.pyplot 並繪製基本圖表（標題／軸標題／格線／刻度）",
        "能畫出折線圖、直方圖、柱狀圖、圓餅圖",
        "能用 savefig() 將圖表存成圖檔",
        "能依資料特性選擇合適的圖表類型，為專題做準備",
    ])

    s1 = block(1, "匯入 Matplotlib", """
<p>就像之前用 <code>pd</code> 作為 pandas 的簡寫，Matplotlib 也習慣用簡寫匯入：</p>
""" + R("""import matplotlib.pyplot as plt

plt.plot()
plt.show()""") + """
""")

    s2 = block(2, "標題、軸標題、格線與刻度", """
""" + R("""plt.title("uniform accelerated motion")  # 表格標題
plt.xlabel("Time")                        # x 軸標題
plt.ylabel("Velocity")                    # y 軸標題
plt.grid(True)                            # 格線
plt.plot()
plt.show()""") + """
<p>調整刻度可以用 <code>xticks</code>／<code>yticks</code>，或是用 <code>axis</code> 一次設定 x、y 軸的顯示範圍：</p>
""" + R("""plt.xticks([0, 1, 2, 3, 4])
plt.yticks([0, 0.8, 1.0, 1.3, 1.7])
plt.show()

plt.axis([0, 4, 0, 2])   # [xmin, xmax, ymin, ymax]
plt.show()""") + """
""")

    s3 = block(3, "折線圖", """
<p>只給 Y 值時，X 會自動被設成 0, 1, 2, ⋯：</p>
""" + R("""plt.plot([0, 1, 4, 9, 16])
plt.show()""") + """
<p>也可以同時給 X 值和 Y 值：</p>
""" + R("""x = [0, 0.2, 0.4, 0.6, 0.8]
y = [i ** 2 for i in x]
plt.plot(x, y)
plt.show()""") + """
<p>修改樣式（顏色、線條種類、線寬）：</p>
""" + R("""x = [0, 0.2, 0.4, 0.6, 0.8]
y = [i ** 2 for i in x]
plt.plot(x, y, 'r:', linewidth=5)   # 紅色、虛線、線寬 5
plt.show()""") + """
""")

    s4 = block(4, "直方圖 Histogram", """
<p>直方圖描述的是<strong>連續型</strong>資料（例如年齡、金額、身高），X 軸上的區間彼此有順序性。</p>
""" + R("""import matplotlib.pyplot as plt
import numpy as np

x = np.random.randint(100, size=10)
plt.hist(x, bins=10)
plt.show()""") + """
""" + R("""import matplotlib.pyplot as plt
import numpy as np

z = np.random.randn(10000)
plt.hist(z, bins='auto')
plt.show()""") + """
""")

    s5 = block(5, "柱狀圖 Bar Chart", """
<p>柱狀圖（長條圖）描述的是<strong>確切的類別</strong>，類別之間沒有順序關係，可以依需要調整排列順序：</p>
""" + R("""import matplotlib.pyplot as plt
import numpy as np

x = np.random.randint(1000, size=10)
y = np.random.randint(1000, size=10)
plt.bar(x, y)
plt.show()""") + """
""")

    s6 = block(6, "圓餅圖 Pie Chart", """
<p>圓餅圖利用<strong>百分比</strong>呈現每個資料的比例：</p>
""" + R("""import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame([
    ['Czech Republic', 10228744], ['France', 61083916],
    ['Germany', 82400996], ['Greece', 10706290]],
    columns=['country', 'pop'])

separated = [0, 0, 0, 0.3]
plt.pie(df['pop'], labels=df['country'], autopct='%1.2f%%',
        pctdistance=0.7, explode=separated)
plt.title('Population')
plt.show()""") + """
""")

    s7 = block(7, "儲存檔案", """
<p>用 <code>savefig()</code> 可以把圖表直接存成圖檔（記得放在 <code>plt.show()</code> 之前）：</p>
""" + R("""import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame([
    ['Czech Republic', 10228744], ['France', 61083916],
    ['Germany', 82400996], ['Greece', 10706290]],
    columns=['country', 'pop'])

separated = [0, 0.1, 0, 0.3]
plt.pie(df['pop'], labels=df['country'], autopct='%.3f%%',
        pctdistance=0.5, explode=separated)
plt.title('Population')
plt.savefig('plot.png')
plt.show()""") + """
""")

    s8 = block(8, "VS Code 操作站", """
""" + grid(2, [
        tile("🖼️", "圖表視窗跳出來了？", "一般直接執行 .py 檔，<code>plt.show()</code> 會另外跳出一個圖表視窗，關掉視窗程式才會繼續往下跑。"),
        tile("📓", "想在編輯器裡直接看圖？", "安裝 VS Code 的 <strong>Jupyter</strong> 延伸套件，用 Interactive Window（互動視窗）執行，圖表會直接顯示在編輯器右側，很適合一邊調整一邊看結果。"),
        tile("💾", "存檔在哪裡？", "<code>savefig(\"plot.png\")</code> 預設會存在你目前 .py 檔案所在的資料夾，可以打開檔案總管確認。"),
        tile("🎨", "中文字變成方框？", "圖表標題若用中文出現亂碼，可以加上 <code>matplotlib.rcParams[\"font.family\"] = [\"Microsoft JhengHei\"]</code>（Windows）指定中文字型。"),
    ]) + """
""")

    ex = exercise("課堂練習", """
<p>想像一組資料：一週五個上課天（一～五），某飲料店每天的來客數分別是 <code>[42, 35, 58, 61, 77]</code>。畫出柱狀圖呈現這組資料，並存成 <code>drink_sales.png</code>。</p>
""", """
""" + R("""import matplotlib.pyplot as plt

days = ["一", "二", "三", "四", "五"]
customers = [42, 35, 58, 61, 77]

plt.title("本週每日來客數")
plt.xlabel("星期")
plt.ylabel("來客數")
plt.bar(days, customers)
plt.savefig("drink_sales.png")
plt.show()"""))

    return h + g + s1 + s2 + s3 + s4 + s5 + s6 + s7 + s8 + ex


# =================================================================
# Part 6 · 專題實作與發表（單元 8-10）
# =================================================================

def u08():
    h = hero("unit08")
    g = goals([
        "認識台灣常見的政府開放資料平台與用途",
        "能在平台上搜尋、篩選、下載 CSV 等格式的資料",
        "能用 pandas 讀取下載的資料並用 head() 初步檢視",
        "能依「時間趨勢／類別比較／地理分布」等角度發想專題主題",
    ])

    s1 = block(1, "為什麼用「政府開放資料」？", callout("✅ 真實、公開、可信、免費", """
<p>政府開放資料平台上的資料，來自各政府機關的統計與調查，通常附有清楚的<strong>欄位說明文件</strong>，資料來源明確、品質有把關，很適合作為專題分析的素材——比自己隨便從網路上找一份不知道出處的資料可靠得多。</p>"""))

    s2 = block(2, "常用平台", """
""" + grid(2, [
        resource_link("🗂️", "政府資料開放平臺", "https://data.gov.tw", "全國性的資料入口，各部會的公開資料集大多可以在這裡找到，支援關鍵字搜尋與格式篩選（CSV／JSON／API⋯）。"),
        resource_link("🌤️", "氣象資料開放平臺", "https://opendata.cwa.gov.tw", "中央氣象署提供的氣象觀測、天氣預報、地震等資料，時間序列資料很適合拿來畫折線圖。"),
        resource_link("🏙️", "臺北市資料大平臺", "https://data.taipei", "台北市政府的開放資料平台，各縣市大多也有類似的平台，可以搜尋「縣市名 + 開放資料」找到。"),
        resource_link("🏛️", "內政部資料開放平臺", "https://data.moi.gov.tw", "人口、土地、戶政等資料，適合做人口變化、地理分布類的專題。"),
    ]) + """
""")

    s3 = block(3, "資料蒐集流程", """
""" + grid(4, [
        tile("①", "找主題", "先想一個你感興趣的問題（見單元 1 的暖身），再去想「哪個機關可能有這種資料」。"),
        tile("②", "搜尋關鍵字", "到平台首頁用關鍵字搜尋（如「空氣品質」「電影票房」），篩選檔案格式為 CSV。"),
        tile("③", "下載資料", "把 CSV 檔下載到你的專題資料夾，順手看一下平台附的欄位說明文件。"),
        tile("④", "用 pandas 檢視", "讀進來後先用 <code>head()</code> 看看長什麼樣子，確認欄位、資料筆數符合預期。"),
    ]) + """
""" + R("""import pandas as pd

df = pd.read_csv("你下載的檔案.csv")
print(df.head())        # 看前 5 筆，確認欄位對不對
print(df.shape)         # (列數, 欄數)
print(df.columns)       # 有哪些欄位""") + """
<div class="callout warn"><span class="t">⚠ 常見小狀況</span>
<p>政府資料的編碼有時不是 UTF-8（尤其舊資料），讀取時若出現亂碼，可以試試看 <code>pd.read_csv("檔名.csv", encoding="big5")</code> 或 <code>encoding="utf-8-sig"</code>。</p></div>
""")

    s4 = block(4, "專題主題發想", """
<p>還沒想法的話，可以參考這些方向：</p>
""" + grid(3, [
        tile("🌫️", "空氣品質", "各縣市 PM2.5 濃度隨時間的變化"),
        tile("🏪", "超商分布", "各縣市超商家數比較，畫成柱狀圖"),
        tile("🎬", "電影票房", "近期上映電影的票房排行"),
        tile("👪", "人口變化", "縣市人口逐年增減的趨勢"),
        tile("🌡️", "氣候變遷", "某地區近年均溫的長期走勢"),
        tile("🚲", "交通觀察", "YouBike 各站點的借還車熱點"),
    ]) + """
""")

    s5 = block(5, "回顧範例作品", """
<p>回到單元 1 看過的範例：<strong>景氣指標綜合分析</strong>，它的資料來自政府公開的景氣指標統計，用折線圖呈現領先、同時、落後指標的長期走勢——這正是「時間趨勢型」專題的一個好示範。</p>
""" + grid(1, [
        resource_link("📄", "再看一次範例作品", "assets/examples/景氣指標綜合分析.pdf", "留意它是怎麼說明資料來源、怎麼描述圖表看到的重點。"),
    ]))

    ex = exercise("專題檢核表", """
<p>在動手畫圖之前，先確認以下幾件事：</p>
<ol>
  <li>我的主題是什麼？我想回答什麼問題？</li>
  <li>資料從哪個平台、哪個資料集下載？</li>
  <li>用 <code>df.head()</code> 看過了嗎？欄位名稱、資料型態合理嗎？</li>
  <li>這份資料有幾筆？涵蓋的時間範圍／類別範圍是什麼？</li>
  <li>我打算用哪種圖表呈現？為什麼？（下一單元會有完整的選圖指南）</li>
</ol>
""")

    return h + g + s1 + s2 + s3 + s4 + s5 + ex


def u09():
    h = hero("unit09")
    g = goals([
        "能用 pandas 檢查缺失值、篩選與清理資料",
        "能依資料特性選擇合適的圖表類型",
        "能用 pandas + Matplotlib 完成至少兩種圖表的視覺化分析",
        "能寫出簡短、扣題的圖表解讀文字",
    ])

    s1 = block(1, "資料清理基本功", """
<p>下載下來的原始資料，通常不能直接拿來畫圖，要先做基本的檢查與清理：</p>
""" + R("""import pandas as pd

df = pd.read_csv("你的資料.csv")

print(df.isnull().sum())     # 每一欄有幾個缺失值（NaN）

df = df.dropna()             # 直接刪除有缺失值的列
# 或者：df["欄位"] = df["欄位"].fillna(0)   # 用 0 補上缺失值

df = df.rename(columns={"原欄名": "新欄名"})   # 欄位改名，方便後續使用

df = df[df["數值欄位"] > 0]   # 篩選：只留下數值大於 0 的資料列""") + """
<div class="callout tip"><span class="t">💡 延伸：groupby 與 sort_values</span>
<p>想依類別分組統計（例如「各縣市的總數」），可以用 <code>df.groupby("縣市")["數值"].sum()</code>；想依大小排序，用 <code>df.sort_values("數值", ascending=False)</code>。這兩個是專題階段很常用到的延伸技巧，用到時再查文件慢慢熟悉即可。</p></div>
""")

    s2 = block(2, "選圖指南", """
<p>依照你的資料想呈現的重點，選擇合適的圖表：</p>
""" + table_wrap(["想呈現什麼？", "適合的圖表", "範例"], [
        ["隨時間變化的趨勢", "折線圖 <code>plt.plot()</code>", "空氣品質逐月變化、景氣指標走勢"],
        ["類別之間的比較", "柱狀圖 <code>plt.bar()</code>", "各縣市超商家數、各電影票房"],
        ["整體中各部分的占比", "圓餅圖 <code>plt.pie()</code>", "各類別占總數的百分比"],
        ["資料的分布狀況", "直方圖 <code>plt.hist()</code>", "分數分布、年齡分布"],
    ]) + """
""")

    s3 = block(3, "實作：從資料到圖表", """
<p>一個完整的小範例，把清理過的資料畫成柱狀圖並加上解讀：</p>
""" + R("""import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("超商家數.csv")
df = df.dropna()
df = df.sort_values("家數", ascending=False)

plt.figure(figsize=(8, 5))
plt.title("各縣市超商家數比較")
plt.xlabel("縣市")
plt.ylabel("家數")
plt.bar(df["縣市"], df["家數"])
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("超商家數比較.png")
plt.show()

print(f"家數最多的是{df.iloc[0]['縣市']}，共{df.iloc[0]['家數']}家。")""") + """
<div class="callout"><span class="t">✍️ 別忘了寫解讀</span>
<p>圖畫出來只是一半，專題真正有價值的地方是<strong>你從圖表看出了什麼</strong>：最高／最低是誰？有沒有明顯的成長或下降？跟你原本的猜測一不一樣？這些觀察都要用文字寫下來。</p></div>
""")

    s4 = block(4, "VS Code 操作站", """
""" + grid(2, [
        tile("📓", "用 Interactive Window 邊看邊調", "改一行程式碼就重跑一次太慢了，用 Jupyter 延伸套件的互動視窗，可以只重跑改動的那一段，很適合調圖表樣式。"),
        tile("🖼️", "同時輸出多張圖", "每張圖用不同檔名 <code>savefig(\"圖1.png\")</code>、<code>savefig(\"圖2.png\")</code>，記得在 <code>plt.show()</code> 之後要重新 <code>plt.figure()</code> 才會開新的一張。"),
    ]) + """
""")

    ex = exercise("實作任務", """
<p>用你在單元 8 找到的專題資料，完成：</p>
<ol>
  <li>用 pandas 檢查並處理缺失值。</li>
  <li>依照選圖指南，畫出<strong>至少兩種</strong>不同類型的圖表。</li>
  <li>每張圖搭配 2–3 句話的文字解讀。</li>
</ol>
""")

    return h + g + s1 + s2 + s3 + s4 + ex


def u10():
    h = hero("unit10")
    g = goals([
        "能將分析過程、圖表與文字整合成一份 PDF 專題報告",
        "認識幾種在 VS Code 產出 PDF 的方法",
        "能上台做簡短發表，並具備欣賞、回饋同儕作品的能力",
    ])

    s1 = block(1, "PDF 報告的基本架構", """
<p>參考單元 1 的範例作品，一份完整的專題報告大致包含：</p>
""" + grid(2, [
        tile("📌", "封面", "專題名稱、姓名（或組員）、資料來源"),
        tile("💡", "動機與問題意識", "為什麼選這個主題？想回答什麼問題？"),
        tile("🧹", "資料處理過程", "資料筆數、欄位、怎麼清理／篩選的（附關鍵程式碼）"),
        tile("📊", "圖表與解讀", "至少兩種圖表，每張搭配文字說明"),
        tile("🧾", "結論", "整體發現、跟原本猜測的異同、還可以怎麼延伸"),
    ]) + """
""")

    s2 = block(2, "在 VS Code 產出 PDF：三種方法", """
""" + grid(1, [
        tile("A. Jupyter Notebook 匯出", "在 VS Code 用 <code>.ipynb</code> 筆記本邊寫程式、邊寫說明文字（Markdown 儲存格），完成後用右上角「Export」→「PDF」直接匯出，最適合已經熟悉 Notebook 的同學。"),
        tile("B. 用 Python 套件組合成 PDF", "把圖表存成 png 之後，用 <code>fpdf2</code> 套件把文字與圖片組進同一份 PDF，適合想要完全用程式自動化產出報告的同學。"),
        tile("C. Word／PowerPoint 排版後另存 PDF", "把程式碼截圖、圖表 png、文字整理進 Word 或 PowerPoint，用「另存新檔→PDF」匯出，最直覺、最適合排版新手。"),
    ]) + """
<h3>方法 B 範例：用 fpdf2 組出簡單報告</h3>
""" + T("pip install fpdf2") + """
""" + R("""from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("Helvetica", "B", 18)
pdf.cell(0, 12, "My Project Report", ln=True)

pdf.set_font("Helvetica", "", 12)
pdf.multi_cell(0, 8, "Data source: data.gov.tw\\nThis report analyzes ...")

pdf.image("chart1.png", w=160)   # 放入單元 9 存好的圖表

pdf.output("my_project_report.pdf")""") + """
<div class="callout tip"><span class="t">💡 中文字型提醒</span>
<p><code>fpdf2</code> 預設字型不支援中文，若報告要放中文內文，需要另外用 <code>pdf.add_font()</code> 載入一套中文字型（如思源黑體），這部分老師會在課堂上示範。若不想處理字型問題，方法 A、C 是更省事的選擇。</p></div>
""")

    s3 = block(3, "再看一次範例作品", """
""" + grid(1, [
        resource_link("📄", "景氣指標綜合分析", "assets/examples/景氣指標綜合分析.pdf", "留意它的篇幅不長，但「圖表＋一段文字解讀」的組合把重點都說清楚了——你的報告不需要很長，但要扣題、有觀察。"),
    ]) + """
<div class="callout"><span class="t">📬 更多範例陸續加入</span>
<p>老師之後整理好其他優秀範例，會補充回單元 1 的「專題範例參觀」，大家可以隨時回去參考。</p></div>
""")

    s4 = block(4, "發表與互評", """
""" + table_wrap(["評核項目", "說明"], [
        ["主題與動機", "有沒有清楚說明為什麼選這個題目"],
        ["資料處理", "資料來源明確、有做基本的清理"],
        ["圖表選擇", "圖表類型是否符合想呈現的重點"],
        ["解讀與結論", "有沒有從圖表提出具體觀察，而不只是「圖表如上」"],
        ["口頭表達", "3–5 分鐘內講清楚重點，能回答同學的提問"],
    ]) + """
""")

    s5 = block(5, "課程總結", callout("🎉 從語法複習到獨立完成一份專題", """
<p>回頭看看這學期走過的路：從最基礎的變數、迴圈開始複習，中間體驗了用 AI 協作開發遊戲的 Vibe Coding，學會了 pandas 整理資料、Matplotlib 畫圖，最後獨立完成一份從「找資料」到「做出結論」的完整專題。這一整套「資料蒐集 → 整理 → 分析 → 視覺化 → 表達」的能力，不只在這門課用得到，未來不管做什麼主題的探究，都會是很扎實的基本功。</p>"""))

    ex = exercise("最後一哩路", """
<p>把你的專題整理成 PDF，並準備一份 3–5 分鐘的口頭發表大綱：主題與動機、資料來源、圖表與發現、結論。發表當天別忘了認真聽同學的分享，準備至少一個問題或一句回饋。</p>
""")

    return h + g + s1 + s2 + s3 + s4 + s5 + ex


BODIES = {
    "unit01": u01, "unit02": u02, "unit03": u03, "unit04": u04, "unit05": u05,
    "unit06": u06, "unit07": u07, "unit08": u08, "unit09": u09, "unit10": u10,
}
