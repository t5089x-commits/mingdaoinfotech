from lib import *

body = ""

body += section("01", "識讀怎麼考？", f'''
{table(["項目", "內容"], [
    ["題數與時間", "30 題單選、90 分鐘，平均 <b>3 分鐘一題</b>"],
    ["4 級分門檻", "70 分以上，大約要答對 <b>21 題</b>"],
    ["題型", "程式追蹤（印出什麼、回傳什麼）、程式填空、找錯與設計測資、效能分析（執行幾次、時間複雜度 O( )）"],
    ["語言", "選 Python 題本；題目程式都是 Python"],
])}
  <h3>作答四招</h3>
  <div class="grid cols-2">
    <div class="tile"><h4><span class="ico">🎯</span>先猜程式在做什麼</h4><p>看到 <code>if a[i] &gt; p: p = a[i]</code> 就知道在找最大值，不用一行一行追。認得越多「經典小程式」越快（見單元 8 的經典小程式庫）。</p></div>
    <div class="tile"><h4><span class="ico">📝</span>追不出來就畫追蹤表</h4><p>每一列是一次迴圈，每一欄是一個變數。不要只靠腦袋記，寫在紙上最不容易錯。</p></div>
    <div class="tile"><h4><span class="ico">🔁</span>把選項代回去</h4><p>填空題、找錯題，把四個選項分別代進去試，比自己想答案還快。</p></div>
    <div class="tile"><h4><span class="ico">⏱️</span>卡住就跳過</h4><p>一題超過 5 分鐘先做記號跳過。簡單題和難題的分數一樣，先把會的拿完。</p></div>
  </div>''')

body += section("02", "追蹤表：把電腦做的事寫在紙上", f'''
  <p>追蹤表的寫法：<strong>每一欄是一個變數，每一列是迴圈跑完一次之後的狀態</strong>。迴圈條件、印出的東西也可以一起寫。</p>
{code("""s = 0
i = 1
while i < 20:
    s = s + i
    i = i * 3
print(s, i)""", label="要追蹤的程式")}
{table(["第幾次", "條件 i &lt; 20", "s = s + i", "i = i * 3"], [
    ["開始前", "—", "s = 0", "i = 1"],
    ["1", "1 &lt; 20 ✓", "s = 1", "i = 3"],
    ["2", "3 &lt; 20 ✓", "s = 4", "i = 9"],
    ["3", "9 &lt; 20 ✓", "s = 13", "i = 27"],
    ["4", "27 &lt; 20 ✗，離開迴圈", "", ""],
], cls="center")}
  <p>所以印出 <code>13 27</code>。單元 4 有<a href="unit04.html">巢狀迴圈的逐步動畫</a>，單元 7 有<a href="unit07.html">函式呼叫的互動追蹤</a>，可以回去複習追蹤的節奏。</p>''')

TRAPS = [
    ("① <code>b = a</code> 不是複製",
     "兩個名字指向<strong>同一個</strong>串列，改 b 等於改 a。要複製一份新的，用 <code>a[:]</code> 或 <code>a.copy()</code>。",
     "a = [1, 2, 3]\nb = a\nc = a[:]\nb.append(4)\nprint(a)\nprint(c)"),
    ("② <code>//</code> 是「往下取整」，負數要小心",
     "<code>//</code> 不是「去掉小數」，而是取<strong>比較小的那個整數</strong>。正數看不出差別，負數就不一樣了。<code>%</code> 的結果正負號跟除數一樣。",
     "print(7 // 2, -7 // 2)\nprint(7 % 3, -7 % 3)\nprint(int(-7 / 2))   # 這個才是去掉小數"),
    ("③ <code>and</code>、<code>or</code> 回傳的是「值」",
     "<code>a and b</code>：a 是假就回傳 a，否則回傳 b。<code>a or b</code>：a 是真就回傳 a，否則回傳 b。不一定是 True／False。",
     "print(3 and 5)\nprint(0 and 5)\nprint(3 or 5)\nprint(0 or 5)"),
    ("④ <code>range</code> 不包含終點",
     "<code>range(a, b)</code> 跑到 b-1。<code>range(0, 101, 5)</code> 有 21 個數，不是 20 個（官方範例第 26 題）。",
     "print(len(range(0, 101, 5)))\nprint(list(range(6, 0, -2)))"),
    ("⑤ 字串不能直接修改",
     "<code>s[0] = 'X'</code> 會出錯。要改字串，用切片組出新字串。",
     "s = 'apcs'\ns = 'A' + s[1:]\nprint(s)"),
    ("⑥ <code>0</code>、<code>''</code>、<code>[]</code> 都是假",
     "放在 <code>if</code> 或 <code>while</code> 後面時，0、空字串、空串列、None 都當成 False，其他都是 True（官方範例第 10 題）。",
     "for x in [0, 5, '', 'a', [], [0]]:\n    print(repr(x), bool(x))"),
    ("⑦ 在 for 迴圈裡改 i，不會影響下一輪",
     "<code>for i in range(...)</code> 每一輪都會重新從 range 拿下一個值，裡面改 i 只影響這一輪。while 迴圈才會被影響。",
     "for i in range(5):\n    print(i, end=' ')\n    i = i + 10\nprint()"),
    ("⑧ 交換兩個變數",
     "Python 可以直接 <code>a, b = b, a</code>。用暫存變數的寫法要注意順序（官方範例第 7、9 題）。",
     "a, b = 1, 2\na, b = b, a\nprint(a, b)\nx, y = 1, 2\nx = y      # 錯誤示範：x 原本的值不見了\ny = x\nprint(x, y)"),
    ("⑨ 函式裡改參數",
     "傳進函式的如果是數字或字串，函式裡改它不會影響外面；如果是串列，用 append 或改元素會影響外面。",
     "def f(n, lst):\n    n = n + 1\n    lst.append(9)\n\nx = 1\na = [1]\nf(x, a)\nprint(x, a)"),
    ("⑩ 比較運算可以連寫",
     "<code>0 &lt;= x &lt; 10</code> 等於 <code>0 &lt;= x and x &lt; 10</code>。",
     "x = 5\nprint(0 <= x < 10, 10 < x < 20)"),
    ("⑪ <code>round()</code> 不是課本的四捨五入",
     "<code>round()</code> 遇到剛好 .5 時取<strong>偶數</strong>那一邊；<code>int()</code> 則是直接去掉小數（負數也一樣往 0 靠）。",
     "print(round(2.5), round(3.5), round(4.6))\nprint(int(3.9), int(-3.9))"),
]
tbody = ""
REFS = {'① <code>b = a</code> 不是複製': ('unit05.html#s05', '單元 5 §05'), '② <code>//</code> 是「往下取整」，負數要小心': ('unit03.html#s01', '單元 3 §01'), '③ <code>and</code>、<code>or</code> 回傳的是「值」': ('unit03.html#s02', '單元 3 §02'), '④ <code>range</code> 不包含終點': ('unit04.html#s02', '單元 4 §02'), '⑤ 字串不能直接修改': ('unit06.html#s01', '單元 6 §01'), "⑥ <code>0</code>、<code>''</code>、<code>[]</code> 都是假": ('unit04.html#s01', '單元 3 §02、單元 4 §01'), '⑧ 交換兩個變數': ('unit05.html#s04', '單元 5 §04'), '⑨ 函式裡改參數': ('unit07.html#s03', '單元 7 §03'), '⑩ 比較運算可以連寫': ('unit03.html#s02', '單元 3 §02'), '⑪ <code>round()</code> 不是課本的四捨五入': ('unit02.html#s03', '單元 2 §03')}
for t, d, src in TRAPS:
    ref = f' <a class="muted" href="{REFS[t][0]}">（回去看：{REFS[t][1]}）</a>' if t in REFS else ""
    tbody += f"  <h3>{t}</h3>\n  <p>{d}{ref}</p>\n" + code(src, label="執行看看")
body += section("03", "Python 識讀陷阱整理", "  <p>下面這些是 Python 題本最容易出陷阱的地方，大部分在前面的單元都學過，這裡集中複習。每一個都附上程式和真正的執行結果。</p>\n" + tbody)

ERRS = [
    ("IndentationError", "縮排錯誤", "if 後面那一行沒有縮排，或空白、Tab 混用。", "x = 5\nif x > 3:\nprint(x)"),
    ("SyntaxError", "語法錯誤", "少了冒號、括號沒成對、用了全形符號。", "for i in range(3)\n    print(i)"),
    ("NameError", "名字沒定義", "變數或函式名稱打錯、還沒指定就使用。", "total = 10\nprint(totl)"),
    ("TypeError", "型態不對", "字串和數字相加，最常見的是忘了把 input() 轉成 int。", "age = '16'\nprint(age + 1)"),
    ("ValueError", "值不能轉換", "一行有好幾個數字卻用 int(input()) 讀。", "line = '3 5'\nn = int(line)"),
    ("IndexError", "索引超出範圍", "串列只有 3 個元素卻拿 a[3]，或迴圈多跑了一次。", "a = [10, 20, 30]\nfor i in range(4):\n    print(a[i])"),
    ("ZeroDivisionError", "除以 0", "平均數時資料筆數是 0。", "scores = []\nprint(sum(scores) / len(scores))"),
    ("KeyError", "字典沒有這個鍵", "還沒放進字典就去讀。用 d.get(k, 0) 可以避免。", "d = {'a': 1}\nprint(d['b'])"),
]
erows = []
ebody = "  <p>程式出錯時，Python 會印出一段紅字。<strong>只要看最後一行</strong>：冒號前面是錯誤種類，後面是原因；往上一行的 <code>line 幾</code> 告訴你錯在第幾行。</p>\n"
for name, zh, why, src in ERRS:
    ebody += f"  <h3><code>{name}</code>：{zh}</h3>\n  <p>{why}</p>\n" + code(src, label="會出錯的程式", expect_error=True)
    erows.append([f"<code>{name}</code>", zh, why])
ebody += "  <h3>對照表</h3>\n" + table(["錯誤", "意思", "常見原因"], erows)
ebody += callout("🔎 識讀也會考", "「下列哪一組輸入會讓程式出錯」這類題目，其實就是在問會不會發生 IndexError 或 ZeroDivisionError。看到串列索引和除法，就要想想邊界情況。", "tip")
body += section("04", "看懂錯誤訊息", ebody)

body += section("05", "常考題型：找錯與設計測資", f'''
  <p>官方範例裡大約有 6 題是「這段程式有錯，哪一個輸入可以測出來」或「哪一行永遠不會執行」。解法是<strong>專挑邊界情況</strong>去試：</p>
{table(["測資類型", "例子", "常抓到的錯"], [
    ["最小／最大值", "n = 1、分數 0 和 100", "迴圈範圍少一個、比較用 &lt; 還是 &lt;="],
    ["剛好在分界上", "成績剛好 60、70、80", "<code>&gt;</code> 和 <code>&gt;=</code> 寫錯、判斷順序錯（第 17 題）"],
    ["找不到的情況", "要找的數比全部都大", "二分搜尋的邊界（第 22 題）"],
    ["排列順序不同", "遞增、遞減、全部一樣", "只處理了某一種順序（第 29 題）"],
], cls="")}
{code("""def grade(s):
    if s >= 90:
        return 'A'
    elif s >= 80:
        return 'B'
    elif s > 60:          # 應該要先判斷 70
        return 'D'
    elif s > 70:          # 永遠不會執行到
        return 'C'
    else:
        return 'F'

print([grade(s) for s in [95, 85, 75, 65, 60, 30]])""", label="官方範例第 17 題的程式：分數區間判斷順序錯了")}
  <p>75 應該是 C，卻被判成 D；60 應該是 D，卻被判成 F。只要把 60、70、75 這些分界附近的數代進去，錯誤馬上出現。{qchips([17, 22, 27, 29, 26])}</p>''')

body += section("06", "常考題型：執行幾次？時間複雜度 O( )", f'''
  <p>效能分析題會問「迴圈執行了幾次」或「比較了幾次」。記住這幾個常見的模式：</p>
{table(["程式", "執行次數", "寫成 O( )", "說明"], [
    ["<code>for i in range(n)</code>", "n", "O(n)", "最基本"],
    ["<code>for i in range(n): for j in range(n)</code>", "n × n", "O(n²)", "兩層都跑 n 次"],
    ["<code>for i in range(n): for j in range(m)</code>", "n × m", "O(mn)", "兩層各跑各的，兩個變數都要留著"],
    ["<code>for i in range(n): for j in range(i, n)</code>", "n + (n-1) + … + 1 = n(n+1)/2", "O(n²)", "內層越跑越少，但還是 n² 等級"],
    ["<code>k = 1; while k &lt;= n: k *= 2</code>", "⌊log₂n⌋ + 1", "O(log n)", "每次翻倍，n = 20 跑 5 次"],
    ["循序搜尋 n 筆資料", "最多 n 次", "O(n)", "從頭一個一個比"],
    ["二分搜尋 n 筆已排序資料", "最多約 log₂n + 1 次", "O(log n)", "每次砍掉一半，100 筆最多 7 次"],
])}
{code("""a = [3 * k + 1 for k in range(100)]      # 官方範例第 6 題的資料
target = 100

n1 = 0
for i in range(100):                     # 循序搜尋
    n1 += 1
    if a[i] == target:
        break

n2, low, high = 0, 0, 99                 # 二分搜尋
while low <= high:
    n2 += 1
    mid = (low + high) // 2
    if a[mid] == target:
        break
    elif a[mid] < target:
        low = mid + 1
    else:
        high = mid - 1
print("循序", n1, "次；二分", n2, "次")""", label="循序搜尋 vs. 二分搜尋")}
{code("""n = 20
cnt, k = 0, 1
while k <= n:
    cnt += 1
    k *= 2
print(cnt)""", label="每次翻倍的迴圈")}
  <h3>把執行次數寫成 O( )：時間複雜度</h3>
  <p>識讀題常不問「剛好幾次」，而是問「<strong>時間複雜度</strong>是哪一個」，選項長得像 <code>O(n)</code>、<code>O(n²)</code>、<code>O(mn)</code>。O( ) 只看「資料變大時，次數長多快」，寫法只要記兩條規則：</p>
  <ol>
    <li><strong>只留最大的那一項</strong>：<code>n² + 3n + 5</code> → <code>O(n²)</code>。n 很大時，n² 比 3n 大太多，後面的項可以不管。</li>
    <li><strong>常數倍數拿掉</strong>：<code>3n</code> → <code>O(n)</code>；<code>n(n+1)/2 = n²/2 + n/2</code> → <code>O(n²)</code>。</li>
  </ol>
  <p>題目有兩個變數（例如 n 列、m 行）時，兩個都要留著：兩層迴圈各跑 n 次、m 次是 <code>O(mn)</code>，不能寫成 <code>O(n²)</code>；兩個迴圈<strong>一前一後</strong>（不是包在一起）各跑 n、m 次，是 <code>O(m + n)</code>。</p>
{table(["寫法", "唸法", "例子（n = 1000 大約跑幾次）"], [
    ["O(1)", "常數", "<code>a[i]</code>、<code>x + y</code>：跟 n 無關，1 次"],
    ["O(log n)", "對數", "二分搜尋、每次翻倍的迴圈：約 10 次"],
    ["O(n)", "線性", "一層迴圈、循序搜尋：1000 次"],
    ["O(n log n)", "", "<code>sorted()</code> 排序：約 1 萬次"],
    ["O(n²)", "平方", "兩層迴圈：100 萬次"],
    ["O(2ⁿ)", "指數", "沒有記錄的費氏數列遞迴：多到跑不完"],
])}
  <p><strong>迴圈裡呼叫函式</strong>時，要把函式本身跑幾次也算進去。下面的 <code>g(k)</code> 自己有一層 <code>range(k)</code> 的迴圈，外面再呼叫 n 次，總次數是 0 + 1 + … + (n-1)，所以是 <code>O(n²)</code>，不是 <code>O(n)</code>：</p>
{code("""def g(k):
    c = 0
    for i in range(k):      # 跑 k 次
        c += 1
    return c

for n in [10, 100, 1000]:
    total = 0
    for i in range(n):      # 呼叫 n 次，第 i 次跑 i 次
        total += g(i)
    print(n, total)""", label="函式裡的迴圈也要算：n 變 10 倍，次數約變 100 倍")}
  <div class="callout"><span class="t">🔎 用「n 變 10 倍」來檢查</span>
  <p style="margin-bottom:0">不確定答案時，想像 n 變成 10 倍：次數也變 10 倍是 <code>O(n)</code>，變 100 倍是 <code>O(n²)</code>，只多跑幾次是 <code>O(log n)</code>。如果函式裡的迴圈只跑到 <code>i * i &gt; k</code> 就停（大約 √k 次），外面再呼叫 n 次，總共就是 n × √n ＝ <code>O(n<sup>1.5</sup>)</code>。</p></div>
  <p>{qchips([6, 28, 4])}（第 4 題是用 head／tail 兩個索引模擬佇列，追蹤時把串列畫出來，標出 head、tail 指到哪裡）</p>''')

SUM = [
    ["單元 2、附", "變數、輸入輸出", "<code>print</code> 的 <code>sep</code>、<code>end</code>；f-string；字串的 <code>+</code> 與 <code>*</code>；<code>True</code> 當 1", [], "<code>end=''</code> 不換行、<code>round(2.5)</code> 是 2、<code>'py' + 2</code> 會出錯"],
    ["單元 3", "運算子", "<code>//</code> 與 <code>%</code>（含負數）、優先順序、真假值、<code>and</code>／<code>or</code> 回傳值", [20], "<code>-7 // 2</code> 是 -4、<code>-2 ** 2</code> 是 -4"],
    ["單元 4", "條件與迴圈", "巢狀判斷、<code>if n:</code>、range 範圍、字串乘法印圖形、break／continue", [2, 5, 10, 12, 19, 26, 27], "<code>if</code> 與 <code>elif</code> 的差別、0 視為假"],
    ["單元 4 附", "輸入與經典迴圈", "<code>split()</code>、<code>map()</code>、串列生成式；費氏數列、GCD 的迴圈寫法", [7, 9], "交換的順序、左右變數個數不同"],
    ["單元 5", "一維串列", "最大最小值、交換、索引用 % 循環、前綴和、<code>in</code>", [15, 24, 25, 29, 30], "<code>b = a</code> 共用、索引從 0 開始"],
    ["單元 6", "字元與字串", "字元判斷、字串方法、字典計數", [], "<code>s[0] = 'X'</code> 不能改字串、<code>int('0309')</code> 開頭的 0 不見"],
    ["單元 6 附", "二維串列", "雙層走訪、方向陣列", [18], "<code>[[0]*m]*n</code>、列與行搞反"],
    ["單元 7", "函式", "參數、回傳值、區域與全域變數", [], "函式裡改參數會不會影響外面"],
    ["單元 7 附", "遞迴", "終止條件、由小算到大、呼叫樹、互相呼叫", [1, 3, 8, 11, 13, 14, 16, 21, 23], "終止條件的邊界"],
    ["單元 8", "經典小程式", "最大值、GCD、質數、前綴和、二分搜尋……一眼認出程式在做什麼", '<a href="unit08.html#classics">見單元 8 §04 各小程式</a>', "初始值設成 0（全部負數就錯）"],
    ["本單元", "搜尋、效能、除錯", "二分搜尋次數、迴圈次數、設計測資、佇列模擬", [4, 6, 17, 22, 28, 29], "邊界值、找不到的情況"],
]
rows = [[a, b, c, (q if isinstance(q, str) else qchips(q)) if q else "—", d] for a, b, c, q, d in SUM]
body += section("07", "各單元的識讀重點統整", f'''
  <p>把官方《程式識讀題目範例（Python 題本）》30 題對回各單元。考前照這張表複習，按題號可以直接看題目。</p>
{table(["單元", "主題", "識讀會考什麼", "官方範例題號", "最常錯在"], rows)}''')

body += qa([
    ("印出什麼？", "a = [5, 3, 8]\nb = a\nb[0] = 1\nprint(a[0] + b[0])", "b 和 a 是同一個串列，<code>b[0] = 1</code> 也改了 <code>a[0]</code>，所以是 1 + 1 = 2。", None),
    ("印出什麼？", "x = -9\nprint(x // 4, x % 4)", "-9 ÷ 4 = -2.25，往下取整是 -3；餘數 = -9 - 4×(-3) = 3。", None),
    ("印出什麼？", "count = 0\nfor i in range(1, 10, 3):\n    for j in range(i):\n        count += 1\nprint(count)", "i 依序是 1、4、7，內層分別跑 1、4、7 次，合計 12 次。", None),
    ("印出什麼？", "s = 0\nfor i in range(10):\n    if i % 3 == 0:\n        continue\n    if i == 8:\n        break\n    s += i\nprint(s)", "跳過 0、3、6，i 到 8 時結束，只加了 1、2、4、5、7，合計 19。", None),
    ("印出什麼？", "def f(x):\n    x = x * 2\n    return x\n\nx = 3\nf(x)\nprint(x)", "函式裡的 x 是區域變數，而且沒有用回傳值，外面的 x 還是 3。", None),
    ("下面程式想找串列的最大值，但有錯。輸入哪一組資料可以測出錯誤？<br>(A) <code>[3, 5, 7]</code>　(B) <code>[-3, -5, -7]</code>　(C) <code>[7, 5, 3]</code>　(D) <code>[5, 7, 3]</code>",
     "def biggest(a):\n    m = 0\n    for x in a:\n        if x > m:\n            m = x\n    return m\n\nprint(biggest([-3, -5, -7]))",
     "答案是 (B)。<code>m</code> 從 0 開始，資料全部是負數時，沒有任何數比 0 大，回傳 0 是錯的。正確寫法是 <code>m = a[0]</code>。", None),
])

page("unit09.html", title="單元 9：識讀基本觀念與總整理", crumb="單元 9",
     kicker="識讀篇　總整理", h1="識讀基本觀念與總整理",
     sub="Python 題本最常見的陷阱、看懂錯誤訊息、除錯與效能題型，以及各單元的識讀重點對照。考前從這一頁開始複習。",
     goals=["知道識讀的題型、時間分配與作答四招",
            "會畫追蹤表，認得 11 個 Python 識讀陷阱",
            "看得懂常見的錯誤訊息，知道是哪裡出問題",
            "會用邊界測資找出程式的錯，會算迴圈與搜尋的執行次數，並寫成 O( )",
            "能用統整表把官方範例 30 題對回各單元複習"],
     body=body, unit=8,
     prev=("unit08.html", "綜合實戰、經典小程式與進階學習地圖"), next=(None, None))
