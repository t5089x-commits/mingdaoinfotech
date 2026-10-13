from lib import *

GRID = [[1,3,4,1,3,1],[1,1,4,1,3,1],[1,1,3,2,5,3],[4,3,3,1,4,1],[5,2,1,1,1,1]]

body = ""

body += section("01", "二維串列：串列裡面裝串列", f'''
  <p>表格、地圖、棋盤、圖片這類「有列有行」的資料，在 Python 用<strong>串列裡面裝串列</strong>來存。外層每一個元素是一整列，<code>g[i][j]</code> 就是第 i 列、第 j 行（都從 0 開始數）。</p>
{code("""g = [[1, 2, 3],
     [4, 5, 6]]
print(g[0])        # 第 0 列（一整列）
print(g[1][2])     # 第 1 列、第 2 行
print(len(g), len(g[0]))   # 列數、行數""", label="建立與取值")}
  <div class="grid cols-2">
    <div class="tile"><h4><span class="ico">↕️</span>列（row）</h4><p>橫的一排。<code>g[i]</code> 是第 i 列，列數是 <code>len(g)</code>，題目常叫它 n 或 M。</p></div>
    <div class="tile"><h4><span class="ico">↔️</span>行（column）</h4><p>直的一排。第 j 行要用迴圈一格一格拿 <code>g[i][j]</code>，行數是 <code>len(g[0])</code>，常叫 m 或 N。</p></div>
  </div>

  <h3>建立一個全部是 0 的 n×m 表格</h3>
{code("""n, m = 3, 4
g = [[0] * m for _ in range(n)]
g[0][1] = 9
print(g)""", label="✅ 正確寫法")}
{code("""n, m = 3, 4
g = [[0] * m] * n      # 看起來一樣，其實三列是「同一個串列」
g[0][1] = 9
print(g)""", label="❌ 常見錯誤：三列全部一起變了")}
{callout("⚠ 為什麼 <code>[[0] * m] * n</code> 會出錯？", "<code>* n</code> 是把「同一個串列」複製 n 次參照，三列其實指向同一個東西，改一格就三列一起變。建立二維串列一律用 <code>[[0] * m for _ in range(n)]</code>。這個陷阱也是識讀常考題。", "warn")}''')

body += section("02", "讀入與印出", f'''
  <p>讀法在<a href="unit04b.html">附錄：多行輸入</a>學過：先讀 n、m，再讀 n 行。印出時，每一列用 <code>print(*row)</code>：</p>
{code("""n, m = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(n)]
for row in g:
    print(*row)""", label="讀入並照原樣印出", stdin="2 3\n1 2 3\n4 5 6")}
  <h3>print(*row) 的星號是什麼意思？</h3>
  <p><code>row</code> 是一個串列，例如 <code>[1, 2, 3]</code>。前面加上 <code>*</code>，意思是「<strong>把串列拆開，一個一個傳給 print</strong>」，所以 <code>print(*row)</code> 等於 <code>print(1, 2, 3)</code>。print 收到好幾個值時，預設用一個空白隔開，剛好就是題目要的輸出格式。</p>
{code("""row = [1, 2, 3]
print(row)                   # 沒有 *：把整個串列當成一個東西印，有中括號和逗號
print(*row)                  # 有 *：等於 print(1, 2, 3)
print(row[0], row[1], row[2])   # 跟上一行完全一樣，只是要自己一個一個寫
print(*row, sep=",")         # 拆開之後，一樣可以用 sep 指定分隔符號""", label="有 * 和沒有 * 的差別")}
{callout("📌 星號只能用在「傳進函式」的時候", "<code>print(*row)</code> 是在呼叫函式時把串列拆開。單獨寫 <code>x = *row</code> 會出錯。單元 7 的 <code>def f(*args)</code> 也有星號，但方向剛好相反：那是把傳進來的很多個值「收集」成一個 tuple。", "tip")}''')

body += section("03", "走訪：一列一列、一行一行", f'''
  <p>雙層迴圈：外層跑列 <code>i</code>、內層跑行 <code>j</code>。這樣的順序叫「列優先」（row-major），跟讀書一樣由左到右、由上到下。</p>
{code("""g = [[3, 1, 4],
     [1, 5, 9]]
n, m = len(g), len(g[0])

total = 0
for i in range(n):
    for j in range(m):
        total += g[i][j]
print("全部總和", total)

for i in range(n):                 # 每一列的總和
    print("第", i, "列", sum(g[i]))

for j in range(m):                 # 每一行的總和：固定 j，讓 i 跑
    s = 0
    for i in range(n):
        s += g[i][j]
    print("第", j, "行", s)""", label="總和、列總和、行總和")}
{code("""g = [[3, 1, 4],
     [1, 5, 9],
     [2, 6, 5]]
best, bi, bj = g[0][0], 0, 0
for i in range(len(g)):
    for j in range(len(g[0])):
        if g[i][j] > best:
            best, bi, bj = g[i][j], i, j
print(best, "在", bi, bj)""", label="找最大值和它的位置")}''')

body += section("04", "範圍與邊界：不要走出地圖", f'''
  <p>網格題最常見的錯誤是<strong>索引超出範圍</strong>（<code>IndexError</code>）。還有一個更隱藏的錯：Python 的負數索引不會報錯，<code>g[-1]</code> 會拿到最後一列，結果算錯卻不知道。所以要自己檢查座標合不合法：</p>
{code("""n, m = 3, 4
def inside(r, c):
    return 0 <= r < n and 0 <= c < m

print(inside(0, 0), inside(2, 3), inside(3, 0), inside(1, -1))""", label="判斷座標有沒有在地圖裡")}
  <h3>方法一：枚舉＋檢查（距離範圍，特殊位置的寫法）</h3>
  <p>兩格的「曼哈頓距離」是 <code>|i - s| + |j - t|</code>。要算「距離 x 以內」的所有格子，最直接的方法是<strong>把整張圖每一格都看一次</strong>，距離符合就加進來：</p>
{code("""g = [[1, 3, 4, 1, 3, 1],
     [1, 1, 4, 1, 3, 1],
     [1, 1, 3, 2, 5, 3],
     [4, 3, 3, 1, 4, 1],
     [5, 2, 1, 1, 1, 1]]
n, m = len(g), len(g[0])
i, j = 2, 3
x = g[i][j]                   # 距離上限就是這格的值
total = 0
for s in range(n):
    for t in range(m):
        if abs(i - s) + abs(j - t) <= x:
            total += g[s][t]
print("距離", x, "以內的總和", total)""", label="距離 x 以內的總和")}
  <p>這種寫法不會超出邊界，因為 <code>s</code>、<code>t</code> 本來就只在地圖範圍裡跑。地圖最大 50×50，每一格都看一次也很快。</p>

  <div class="widget" id="dist-widget">
    <h3 style="margin-top:0">🧪 互動：點一格，看「距離不超過它的值」的範圍</h3>
    <p style="margin-top:0;color:var(--text-soft);font-size:.92rem">這是官方中級範例「特殊位置」的地圖。點任何一格，會標出距離不超過該格數字的所有格子、算出總和，並判斷是不是特殊位置（總和 % 10 等於自己 % 10）。</p>
    <div class="dw-grid" role="grid" aria-label="特殊位置範例地圖"></div>
    <div class="dw-info" aria-live="polite">點上面任何一格開始。</div>
  </div>

  <h3>方法二：用 max、min 把範圍夾在地圖裡（正方形範圍）</h3>
  <p>如果範圍是「以 (r, c) 為中心、邊長 k 的正方形」，可以直接算出上下左右的邊界，再用 <code>max</code>、<code>min</code> 夾住，不讓它超出地圖：</p>
{code("""n, m = 5, 6
r, c, k = 0, 4, 3             # 中心在第 0 列第 4 行，邊長 3
r1, r2 = max(0, r - k // 2), min(n - 1, r + k // 2)
c1, c2 = max(0, c - k // 2), min(m - 1, c + k // 2)
print("列", r1, "到", r2, "；行", c1, "到", c2)
for i in range(r1, r2 + 1):
    for j in range(c1, c2 + 1):
        print((i, j), end=" ")
print()""", label="正方形範圍取交集")}''')

body += section("05", "方向陣列：在地圖上移動和轉彎", f'''
  <p>機器人、蜜蜂、棋子在格子上移動的題目，用兩個串列記錄「每個方向要走的列差和行差」，叫做<strong>方向陣列</strong>：</p>
{table(["d", "方向", "dr[d]（列）", "dc[d]（行）"], [["0", "東（右）", "0", "+1"], ["1", "南（下）", "+1", "0"], ["2", "西（左）", "0", "-1"], ["3", "北（上）", "-1", "0"]], cls="center")}
{code("""dr = [0, 1, 0, -1]      # 東 南 西 北
dc = [1, 0, -1, 0]
names = ["東", "南", "西", "北"]
d = 0                    # 一開始面向東
print(names[d])
d = (d + 1) % 4          # 右轉（順時針）
print("右轉後", names[d])
d = (d + 3) % 4          # 左轉：等於右轉三次
print("左轉後", names[d])
d = (d + 2) % 4          # 迴轉
print("迴轉後", names[d])""", label="方向與轉向")}
  <p>把方向陣列和「邊界檢查」放在一起，就是網格模擬題的骨架。下面這個機器人從左上角出發面向東，<strong>前方是牆（-1）或界外就右轉，否則前進一格</strong>，記錄走過的格子：</p>
{code("""g = [[0, 0, 0],
     [0, -1, 0],
     [0, 0, 0]]
n, m = len(g), len(g[0])
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
r, c, d = 0, 0, 0
path = [(r, c)]
for step in range(6):
    nr, nc = r + dr[d], c + dc[d]
    while not (0 <= nr < n and 0 <= nc < m) or g[nr][nc] == -1:
        d = (d + 1) % 4                  # 前方不能走 → 右轉，再看一次
        nr, nc = r + dr[d], c + dc[d]
    r, c = nr, nc
    path.append((r, c))
print(path)""", label="撞牆就右轉的機器人")}
{callout("💡 寫模擬題的順序", "① 先把規則逐條寫成註解；② 決定要記錄哪些狀態（位置、方向、分數……）；③ 一條規則寫一段程式；④ 用範例輸入<strong>一步一步印出狀態</strong>，跟題目的說明對照。官方範例「蒐集寶石」（o712）就是照這個骨架加上「撿寶石、計分、分數是 K 的倍數就右轉」。", "tip")}''')

body += section("06", "矩陣的旋轉與翻轉", f'''
  <p>旋轉、翻轉的關鍵是找出「新位置」和「舊位置」的對應公式。原本 n 列 m 行的 A，<strong>轉 90 度之後會變成 m 列 n 行</strong>：</p>
{table(["操作", "新表格大小", "對應關係"], [
    ["順時針轉 90 度", "m × n", "<code>B[j][n-1-i] = A[i][j]</code>"],
    ["逆時針轉 90 度", "m × n", "<code>B[m-1-j][i] = A[i][j]</code>"],
    ["轉 180 度", "n × m", "<code>B[n-1-i][m-1-j] = A[i][j]</code>"],
    ["左右翻轉", "n × m", "<code>B[i][m-1-j] = A[i][j]</code>"],
    ["上下翻轉", "n × m", "<code>B[n-1-i][j] = A[i][j]</code>"],
    ["轉置（行列互換）", "m × n", "<code>B[j][i] = A[i][j]</code>"],
])}
{code("""A = [[1, 2, 3],
     [4, 5, 6]]
n, m = len(A), len(A[0])

B = [[0] * n for _ in range(m)]          # 轉 90 度後是 m × n
for i in range(n):
    for j in range(m):
        B[j][n - 1 - i] = A[i][j]
for row in B:
    print(*row)""", label="順時針轉 90 度")}
{code("""A = [[1, 2, 3],
     [4, 5, 6]]
print([row[::-1] for row in A])          # 左右翻轉：每一列反轉
print(A[::-1])                           # 上下翻轉：列的順序反轉
print([row[::-1] for row in A[::-1]])    # 轉 180 度：兩個都做""", label="用切片做翻轉")}
  <h3>比對兩個表格有幾格相同</h3>
{code("""A = [[1, 2], [3, 4]]
B = [[1, 0], [3, 4]]
same = 0
if len(A) == len(B) and len(A[0]) == len(B[0]):    # 大小不同就不用比
    for i in range(len(A)):
        for j in range(len(A[0])):
            if A[i][j] == B[i][j]:
                same += 1
total = len(A) * len(A[0])
print(same, "/", total, "＝", same * 100 // total, "%")""", label="逐格比對")}
{callout("🔎 怎麼確定公式沒寫錯？", "拿一個 2×3 的小例子，在紙上畫出轉完的樣子，再把幾格代進公式檢查。例如 <code>A[0][0]=1</code> 順時針轉完應該在右上角，代入 <code>B[0][n-1-0] = B[0][1]</code>，2 列的話右上角就是 <code>B[0][1]</code>，對了。")}''')

body += section("07", "識讀常考：二維串列與方向陣列", f'''
  <p>官方識讀範例第 18 題就是方向陣列：在迷宮裡數每一格上下左右有幾個 1。追這種題目時，<strong>把地圖畫在紙上</strong>，一格一格數，比在腦中想快很多。按題號可以直接看題目：{qchips([18])}</p>
{qa([
    ("這段程式印出什麼？",
     "g = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]\ns = 0\nfor i in range(3):\n    s += g[i][i]\nprint(s)",
     "<code>g[0][0] + g[1][1] + g[2][2] = 1 + 5 + 9 = 15</code>，這是「對角線總和」。", None),
    ("這段程式印出什麼？",
     "g = [[1, 2, 3], [4, 5, 6]]\nfor j in range(3):\n    for i in range(2):\n        print(g[i][j], end=' ')\nprint()",
     "外層跑行 j、內層跑列 i，所以是一行一行往下讀：1 4 2 5 3 6。", None),
    ("這段程式印出什麼？",
     "g = [[0] * 3] * 2\ng[1][2] = 7\nprint(g[0][2])",
     "<code>[[0] * 3] * 2</code> 的兩列是同一個串列，改 <code>g[1][2]</code> 等於也改了 <code>g[0][2]</code>，所以印出 7。", None),
    ("機器人在 4×4 的地圖上，從 (0, 0) 面向東出發，這段程式最後印出什麼？",
     "dr = [0, 1, 0, -1]\ndc = [1, 0, -1, 0]\nr, c, d = 0, 0, 0\nfor step in range(5):\n    nr, nc = r + dr[d], c + dc[d]\n    if not (0 <= nr < 4 and 0 <= nc < 4):\n        d = (d + 1) % 4\n        nr, nc = r + dr[d], c + dc[d]\n    r, c = nr, nc\nprint(r, c, d)",
     "往東走 3 步到 (0, 3)；第 4 步前方出界，右轉朝南走到 (1, 3)；第 5 步到 (2, 3)。最後 d = 1（南）。", None),
])}''')

WIDGET_JS = f"""<script>
(function(){{
  var G = {GRID};
  var box = document.getElementById("dist-widget"); if(!box) return;
  var gridEl = box.querySelector(".dw-grid"), info = box.querySelector(".dw-info");
  var n = G.length, m = G[0].length;
  gridEl.style.gridTemplateColumns = "repeat(" + m + ", 1fr)";
  var cells = [];
  for (var i = 0; i < n; i++) for (var j = 0; j < m; j++) {{
    var b = document.createElement("button");
    b.type = "button"; b.className = "dw-cell"; b.textContent = G[i][j];
    b.setAttribute("aria-label", "第 " + i + " 列第 " + j + " 行，值 " + G[i][j]);
    b.dataset.i = i; b.dataset.j = j;
    gridEl.appendChild(b); cells.push(b);
  }}
  gridEl.addEventListener("click", function(e){{
    var b = e.target.closest(".dw-cell"); if(!b) return;
    var i = +b.dataset.i, j = +b.dataset.j, x = G[i][j], sum = 0, cnt = 0;
    cells.forEach(function(c){{
      var s = +c.dataset.i, t = +c.dataset.j;
      var inR = Math.abs(i - s) + Math.abs(j - t) <= x;
      c.classList.toggle("in", inR); c.classList.toggle("me", s === i && t === j);
      if (inR) {{ sum += G[s][t]; cnt++; }}
    }});
    var ok = sum % 10 === x % 10;
    info.innerHTML = "(" + i + ", " + j + ") 的值是 <b>" + x + "</b>，距離 ≤ " + x + " 的格子有 <b>" + cnt + "</b> 格，總和 <b>" + sum +
      "</b>。" + sum + " % 10 = " + (sum % 10) + "，" + x + " % 10 = " + (x % 10) + " → " +
      (ok ? "<b style='color:var(--ok)'>是特殊位置 ✓</b>" : "<b>不是</b>特殊位置");
  }});
}})();
</script>
"""

CSS = """<style>
.dw-grid { display: grid; gap: 4px; max-width: 420px; margin: 8px 0 12px; }
.dw-cell { aspect-ratio: 1; font: inherit; font-family: var(--mono); font-weight: 800; font-size: 1.05rem; cursor: pointer;
  border: 1px solid var(--border); border-radius: 8px; background: var(--surface-2); color: var(--text); }
.dw-cell:hover { border-color: var(--brand); }
.dw-cell.in { background: color-mix(in srgb, var(--accent) 40%, var(--surface)); }
.dw-cell.me { background: var(--brand); color: #fff; border-color: var(--brand); }
.dw-cell:focus-visible { outline: 3px solid var(--brand); outline-offset: 2px; }
.dw-info { font-size: .93rem; min-height: 3em; }
</style>
"""

page("unit06b.html", title="單元 6 附：二維串列與網格模擬", crumb="單元 6 附",
     kicker="挑戰篇　補充單元（中級主力）", h1="二維串列與網格模擬",
     sub="中級題本最常考的題型：表格、地圖、機器人移動、矩陣旋轉。官方中級範例三題裡有兩題是這一類。",
     goals=["會建立、讀入、印出二維串列，知道 <code>[[0]*m]*n</code> 為什麼是錯的",
            "會用雙層迴圈走訪，算出列總和、行總和、最大值位置",
            "會檢查座標有沒有出界，能用「枚舉＋距離判斷」或「max／min 夾範圍」處理範圍題",
            "會用方向陣列和 <code>(d+1)%4</code> 寫出網格移動模擬",
            "會寫矩陣的旋轉、翻轉與逐格比對"],
     body=body, unit=6,
     prev=("unit07b.html", "遞迴追蹤：識讀的重點題型"), next=("unit08.html", "綜合實戰、經典小程式與進階學習地圖"),
     extra_css=CSS, extra_js=WIDGET_JS)
