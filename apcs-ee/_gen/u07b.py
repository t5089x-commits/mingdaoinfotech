from lib import *

body = ""

body += section("01", "追蹤遞迴的三個步驟", f'''
  <p>官方識讀範例 30 題裡有 9 題是遞迴，比例很高，是能不能拿到 4 級分的關鍵。追遞迴不用硬記技巧，照這三步做就好：</p>
  <div class="grid cols-3">
    <div class="tile"><h4><span class="ico">①</span>找終止條件</h4><p>哪一行<strong>不會再呼叫自己</strong>？那就是 base case，例如 <code>if n == 0: return 1</code>。</p></div>
    <div class="tile"><h4><span class="ico">②</span>寫出關係式</h4><p>把程式翻成數學式，例如 <code>f(n) = n × f(n-1)</code>。看清楚是 <code>n-1</code> 還是 <code>n-2</code>、是加還是乘。</p></div>
    <div class="tile"><h4><span class="ico">③</span>由小算到大</h4><p>從 base case 開始，<strong>列表</strong>算出 f(0)、f(1)、f(2)……一路往上，直到題目問的那個。</p></div>
  </div>
{callout("💡 為什麼要「由小算到大」？", "如果從 f(10) 往下展開，會寫出一長串等待的算式，很容易漏掉或算錯。反過來從最小的開始列表，每一格只需要用前面算好的數字，又快又不容易錯。單元 7 的 factorial(4) 動畫，就是「往下呼叫、再往回算」的過程。", "tip")}''')

body += section("02", "單一呼叫的遞迴：階乘、次方、最大公因數", f'''
  <p>每次只呼叫自己一次的遞迴，就像一條鏈子，往下走到底再往回算。</p>
{code("""def G(a, x):              # a 的 x 次方
    if x == 0:
        return 1
    return a * G(a, x - 1)

print(G(3, 4))""", label="次方：G(a, x) = a × G(a, x-1)")}
{table(["呼叫", "a", "x", "x == 0？", "接下來", "回傳值（往回算）"], [
    ["G(3, 4)", "3", "4", "否", "要算 3 × G(3, 3)，先呼叫 G(3, 3)", "3 × 27 = <b>81</b>"],
    ["G(3, 3)", "3", "3", "否", "要算 3 × G(3, 2)，先呼叫 G(3, 2)", "3 × 9 = 27"],
    ["G(3, 2)", "3", "2", "否", "要算 3 × G(3, 1)，先呼叫 G(3, 1)", "3 × 3 = 9"],
    ["G(3, 1)", "3", "1", "否", "要算 3 × G(3, 0)，先呼叫 G(3, 0)", "3 × 1 = 3"],
    ["G(3, 0)", "3", "0", "是", "終止條件，不再呼叫", "1"],
], cls="center")}
  <p>由上往下看「接下來」欄是<strong>往下呼叫</strong>的過程；碰到終止條件之後，再<strong>由下往上</strong>看「回傳值」欄，一層一層把答案算回來，最上面的 G(3, 4) 就是 81。</p>
{code("""def gcd(a, b):
    r = a % b
    if r == 0:
        return b
    return gcd(b, r)

print(gcd(76, 48))""", label="最大公因數：輾轉相除法")}
{table(["呼叫", "a", "b", "r = a % b", "接下來"], [
    ["gcd(76, 48)", "76", "48", "28", "呼叫 gcd(48, 28)"],
    ["gcd(48, 28)", "48", "28", "20", "呼叫 gcd(28, 20)"],
    ["gcd(28, 20)", "28", "20", "8", "呼叫 gcd(20, 8)"],
    ["gcd(20, 8)", "20", "8", "4", "呼叫 gcd(8, 4)"],
    ["gcd(8, 4)", "8", "4", "0", "r 是 0，回傳 b = <b>4</b>"],
], cls="center")}
  <p>官方識讀範例相關題目：{qchips([11, 21, 23])}（11 是階乘的終止條件除錯、21 是次方、23 是 GCD 填空）</p>''')

body += section("03", "兩個分支的遞迴：費氏數列與呼叫樹", f'''
  <p>如果一次呼叫自己<strong>兩次</strong>，展開就不是一條鏈子，而是一棵「呼叫樹」：</p>
{code("""def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

print([fib(i) for i in range(10)])""", label="費氏數列")}
  <div class="code-card"><div class="code-head"><span class="dot r"></span><span class="dot y"></span><span class="dot g"></span><span class="label">fib(4) 的呼叫樹</span></div>
  <pre><code>fib(4)
├── fib(3)
│   ├── fib(2)
│   │   ├── fib(1) → 1
│   │   └── fib(0) → 0
│   └── fib(1) → 1
└── fib(2)
    ├── fib(1) → 1
    └── fib(0) → 0</code></pre></div>
  <p>畫出呼叫樹，就可以回答識讀很愛問的「<strong>總共呼叫了幾次</strong>」：數樹上有幾個節點就好，fib(4) 一共呼叫 9 次。也可以用程式驗證：</p>
{code("""count = 0
def fib(n):
    global count
    count += 1
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

for k in range(1, 7):
    count = 0
    fib(k)
    print(f"fib({k}) 呼叫了 {count} 次")""", label="數呼叫次數")}
{callout("🔎 觀察", "fib(2) 在樹裡被算了兩次、fib(1) 被算了三次——同樣的東西一直重算，所以 n 稍微變大，呼叫次數就暴增。這也是識讀「效能分析」題的考點：兩個分支的遞迴，次數大約每多 1 就變成將近兩倍。")}
  <p>官方識讀範例相關題目：{qchips([14])}（填出費氏數列的遞迴式）</p>''')

body += section("04", "由小算到大：列表法", f'''
  <p>遇到看不出在算什麼的遞迴，就直接列表。官方識讀範例第 16 題：<code>F(a) = F(a-2) + F(a-3)</code>，問終止條件是什麼才會讓 F(7) = 12。我們先假設終止條件是 <code>a &lt; 0</code>：</p>
{code("""def F(a):
    if a < 0:
        return 1
    return F(a - 2) + F(a - 3)

print([F(a) for a in range(8)])""", label="先把每一個值算出來")}
{table(["a", "-3", "-2", "-1", "0", "1", "2", "3", "4", "5", "6", "7"],
       [["F(a)", "1", "1", "1", "F(-2)+F(-3) = 2", "F(-1)+F(-2) = 2", "F(0)+F(-1) = 3", "F(1)+F(0) = 4", "F(2)+F(1) = 5", "F(3)+F(2) = 7", "F(4)+F(3) = 9", "F(5)+F(4) = <b>12</b>"]], cls="center")}
  <p>F(7) = 12，所以終止條件是 <code>a &lt; 0</code>。考試時換成別的條件，一樣把表重列一次，就能刪去錯的選項。{qchips([16, 3])}</p>''')

body += section("05", "遞迴裡有 print：注意印出的順序", f'''
  <p><code>print</code> 放在遞迴呼叫的<strong>前面</strong>還是<strong>後面</strong>，印出的順序完全不一樣：</p>
{code("""def down(n):
    if n == 0:
        return
    print(n, end=" ")      # 先印，再往下呼叫
    down(n - 1)

def up(n):
    if n == 0:
        return
    up(n - 1)              # 先往下呼叫，回來才印
    print(n, end=" ")

down(3); print()
up(3); print()""", label="print 在呼叫前 vs. 呼叫後")}
{code("""def both(n):
    if n == 0:
        return
    print(n, end=" ")
    both(n - 1)
    print(n, end=" ")

both(3)""", label="前後都有 print：像照鏡子")}
  <p>追這種題目，可以把呼叫樹畫出來，<strong>進入一個呼叫時寫下前面的 print，離開時寫下後面的 print</strong>。</p>''')

body += section("06", "兩個函式互相呼叫", f'''
  <p>官方識讀範例第 8 題是 <code>f1</code> 呼叫 <code>f2</code>、<code>f2</code> 又呼叫 <code>f1</code>。追蹤方法一樣：把每一次呼叫寫成一行，記下參數和印出的東西。</p>
{code("""def f1(m):
    if m > 3:
        print(m)
        return
    print(m)
    f2(m + 2)
    print(m)

def f2(n):
    if n > 3:
        print(n)
        return
    print(n)
    f1(n - 1)
    print(n)

f1(1)""", label="官方識讀範例第 8 題的程式")}
{table(["呼叫順序", "參數", "做了什麼"], [
    ["f1(1)", "m = 1", "印 1，呼叫 f2(3)，等它回來再印 1"],
    ["　f2(3)", "n = 3", "印 3，呼叫 f1(2)，等它回來再印 3"],
    ["　　f1(2)", "m = 2", "印 2，呼叫 f2(4)，等它回來再印 2"],
    ["　　　f2(4)", "n = 4", "4 > 3，印 4，直接結束"],
], cls="")}
  <p>所以印出順序是 1、3、2、4、2、3、1。f1 被呼叫 2 次、f2 被呼叫 2 次。{qchips([8, 13])}</p>''')

body += section("07", "遞迴的除錯：沒有終止條件會怎樣？", f'''
  <p>終止條件寫錯，遞迴就停不下來，Python 會在呼叫太多層之後當掉：</p>
{code("""def fac(n):
    return n * fac(n - 1)     # 忘了寫終止條件

print(fac(3))""", label="❌ 沒有終止條件", expect_error=True)}
  <p>另一種常見錯誤是終止條件「放錯位置」。官方識讀範例第 11 題：<code>if n &gt;= 0:</code> 會讓 n = 0 時繼續呼叫 <code>fun(-1)</code>，乘到 0，結果永遠是 0。{qchips([11, 1])}</p>
{code("""def fun(n):
    fac = 1
    if n >= 0:              # 錯：n = 0 時還會繼續往下
        fac = n * fun(n - 1)
    return fac

print(fun(4))""", label="終止條件寫錯：答案永遠是 0")}''')

body += qa([
    ("<code>f(5)</code> 回傳多少？", "def f(n):\n    if n == 1:\n        return 1\n    return n + f(n - 1)\n\nprint(f(5))", "f(n) = n + f(n-1)，f(1) = 1，所以是 1+2+3+4+5 = 15。", None),
    ("<code>g(4)</code> 回傳多少？", "def g(n):\n    if n <= 1:\n        return 1\n    return g(n - 1) + 2 * g(n - 2)\n\nprint(g(4))", "列表：g(0)=1、g(1)=1、g(2)=1+2×1=3、g(3)=3+2×1=5、g(4)=5+2×3=11。", None),
    ("這段程式印出什麼？", "def p(n):\n    if n <= 0:\n        return\n    p(n - 2)\n    print(n, end=' ')\n\np(7)", "print 在呼叫之後，所以會先一路呼叫到 p(-1)，再往回印：1 3 5 7。", None),
    ("<code>h(1234)</code> 回傳多少？這個函式在算什麼？", "def h(n):\n    if n < 10:\n        return n\n    return h(n // 10) + n % 10\n\nprint(h(1234))", "每次取出最後一位加起來：h(1234) = h(123) + 4 = h(12) + 3 + 4 = h(1) + 2 + 3 + 4 = 10，這個函式在算「各位數字的和」。", None),
    ("<code>fib(6)</code> 的值是多少？呼叫 <code>fib(5)</code> 一共會呼叫 fib 幾次（包含自己）？", None, "fib(6) = 8。fib(5) 一共呼叫 15 次，可以畫呼叫樹，或用第 03 節的程式驗證。", None),
])

page("unit07b.html", title="單元 7 附：遞迴追蹤", crumb="單元 7 附",
     kicker="挑戰篇　補充單元（識讀主力）", h1="遞迴追蹤：識讀的重點題型",
     sub="官方識讀範例 30 題裡有 9 題是遞迴。學會「找終止條件、寫出關係式、由小算到大」三步驟，就能穩穩拿分。",
     goals=["會用「找終止條件 → 寫關係式 → 由小算到大」追蹤遞迴",
            "會畫兩個分支的呼叫樹，算出呼叫次數",
            "看得出 print 放在遞迴呼叫前後，印出順序有什麼不同",
            "會追蹤兩個函式互相呼叫，會找出終止條件的錯誤"],
     body=body, unit=7,
     prev=("unit07.html", "函式使用規則大全"), next=("unit06b.html", "二維串列與網格模擬"))
