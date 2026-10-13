from lib import *

body = ""

body += section("01", "Judge 是怎麼改你的程式？", f'''
  <p>ZeroJudge 和 APCS 考場的程式實作，都是由電腦自動評分。流程是這樣的：</p>
  <div class="timeline"><div class="tl-row">
    <div class="tl-block a"><span class="tl-when">①</span><span class="tl-what">把測資當成「鍵盤輸入」餵給你的程式</span></div>
    <div class="tl-arrow">➜</div>
    <div class="tl-block b"><span class="tl-when">②</span><span class="tl-what">收集你 print 出來的每一個字</span></div>
    <div class="tl-arrow">➜</div>
    <div class="tl-block c"><span class="tl-when">③</span><span class="tl-what">跟標準答案逐字比對</span></div>
  </div></div>
  <p>重點在第 ③ 步：電腦不會「看懂」你的答案，它只會<strong>逐字比對</strong>。所以多印一個字、少一個空白、多一行，都會被判錯。一題通常有好幾筆測資（APCS 每題 20 筆），每通過一筆就拿那一筆的分數。</p>
{table(["結果", "意思", "通常是哪裡出問題"], [
    ["<strong>AC</strong>　Accepted", "全部測資都通過", "🎉"],
    ["<strong>NA</strong>　Not Accepted", "部分測資通過（ZeroJudge 的說法），會拿到部分分數", "子題只寫了簡單版、邊界情況沒處理"],
    ["<strong>WA</strong>　Wrong Answer", "有執行完，但輸出跟答案不一樣", "邏輯錯、<strong>輸出格式錯</strong>、多印了提示文字"],
    ["<strong>TLE</strong>　Time Limit Exceeded", "跑太久，超過時間限制", "無窮迴圈、迴圈層數太多、在等一筆不存在的輸入"],
    ["<strong>RE</strong>　Runtime Error", "執行到一半當掉", "索引超出範圍、轉型失敗、除以 0（看下面的錯誤訊息）"],
    ["<strong>CE</strong>　Compile Error", "程式根本沒辦法執行", "語法錯誤、縮排錯誤、選錯語言"],
])}''')

body += section("02", "陷阱一：input() 括號裡不要放任何文字", f'''
  <p>很多課本和網路範例會寫 <code>input("請輸入數字:")</code>，讓使用者知道要輸入什麼；寫給人用的程式這樣很好。但是在 Judge 上，<strong>括號裡的提示文字會被印到輸出裡</strong>，跟答案混在一起，結果就是 WA。</p>
  <div class="grid cols-2">
    <div>
      <p><strong>❌ 會被判 WA</strong></p>
{code('a = int(input("請輸入 a:"))\nb = int(input("請輸入 b:"))\nprint(a + b)', label="錯誤寫法", stdin="3\n5")}
    </div>
    <div>
      <p><strong>✅ 正確</strong></p>
{code('a = int(input())\nb = int(input())\nprint(a + b)', label="正確寫法", stdin="3\n5")}
    </div>
  </div>
  <p>左邊的執行結果就是 Judge 收到的輸出：「<code>請輸入 a:請輸入 b:8</code>」，跟正確答案「<code>8</code>」不一樣。在 IDLE 裡自己打字時，提示文字和你輸入的數字會分在不同行，看起來很正常，所以這個錯誤很難自己發現。</p>
{callout("📌 規則", "寫 Judge 題目時，<code>input()</code> 一律<strong>空括號</strong>。也不要印「答案是：」「請輸入」這類說明文字——<strong>題目要求印什麼，就只印什麼</strong>。<br>不是送 Judge 的程式（寫給別人用的小工具、專題作品），才在括號裡放提示文字，例如 <code>input(\"請輸入分數：\")</code>。", "warn")}''')

body += section("03", "陷阱二：輸出格式要一字不差", f'''
  <p>題目的「輸出說明」和「範例輸出」就是格式規定。最常見的錯誤是把串列直接印出來：</p>
{code('a = [3, 1, 4]\nprint(a)          # 會印出中括號和逗號', label="❌ 直接印串列")}
  <p>題目通常要的是「用一個空白隔開」。有三種寫法都可以：</p>
{code('a = [3, 1, 4]\nprint(*a)                      # 寫法 1：* 把串列拆開，預設用空白隔開\nprint(" ".join(map(str, a)))   # 寫法 2：先轉成字串，再用空白接起來\nfor x in a:                    # 寫法 3：一個一個印，不換行\n    print(x, end=" ")\nprint()', label="✅ 用空白隔開")}
  <p><strong>寫法 1 的 <code>*</code> 是什麼？</strong>在串列前面加 <code>*</code>，意思是把串列「拆開」，一個一個傳給 print：<code>print(*[3, 1, 4])</code> 就等於 <code>print(3, 1, 4)</code>。print 收到好幾個值時，預設用一個空白隔開，所以剛好是 Judge 要的格式。</p>
{table(["想要的格式", "寫法", "印出"], [
    ["同一行、空白隔開", "<code>print(a, b)</code> 或 <code>print(*lst)</code>", "<code>3 5</code>"],
    ["同一行、不要空白", "<code>print(a, b, sep=\"\")</code>", "<code>35</code>"],
    ["用逗號隔開", "<code>print(*lst, sep=\",\")</code>", "<code>3,1,4</code>"],
    ["每個一行", "<code>for x in lst: print(x)</code>", "3<br>1<br>4"],
    ["數字後面接符號", "<code>print(f\"{p}%\")</code>", "<code>50%</code>"],
    ["小數點後兩位", "<code>print(f\"{x:.2f}\")</code>", "<code>3.14</code>"],
])}
  <p>另一個常見錯誤是<strong>除法</strong>：題目要整數，你卻用 <code>/</code>，結果印出 <code>2.0</code>。</p>
{code('total, n = 10, 5\nprint(total / n)    # 2.0  ← 多了 .0，WA\nprint(total // n)   # 2    ← 整數除法', label="/ 和 // 印出來不一樣")}
{callout("✅ 送出前的檢查清單", "① 範例輸入跑出來的結果，跟範例輸出<strong>逐字</strong>比對過嗎？ ② 有沒有多印說明文字或提示文字？ ③ 空白、換行、大小寫、標點跟範例一樣嗎？ ④ 該印整數的地方有沒有變成小數？", "tip")}''')

body += section("04", "用範例測資自己先測", f'''
  <p>每一題都會附「範例輸入／範例輸出」。在 IDLE 裡按 <kbd>F5</kbd> 執行後，把範例輸入<strong>整段複製、貼到 Shell 視窗</strong>，再按 Enter，就能看到你的程式印出什麼。</p>
  <ol>
    <li>範例都對了，<strong>不代表一定 AC</strong>。範例通常很小，真正的測資會有更多情況。</li>
    <li>自己再想幾組「邊界測資」測一下：只有 1 筆資料、全部一樣、最大值、最小值、0、負數。</li>
    <li>多行的範例輸入可以一次貼上，<code>input()</code> 會一行一行讀。</li>
  </ol>
{callout("💡 為什麼範例對了還是錯？", "最常見的原因：① 只處理了範例剛好有的情況（例如範例沒有平手，你就沒處理平手）；② 迴圈範圍少算一個（<code>range(n)</code> 和 <code>range(1, n)</code>）；③ 題目說「保證」的條件你沒有用到，或是題目沒保證的你卻假設了。")}''')

body += section("05", "APCS 考場規則：只算最後一次上傳", f'''
  <p>APCS 官方〈作答系統說明〉有幾條規則一定要知道：</p>
{table(["規則", "代表什麼"], [
    ["每一題<strong>只保留並評分最後一次上傳</strong>的檔案", "改到一半上傳，會蓋掉之前會過的版本。上傳前一定要先測過。"],
    ["可以重複上傳，直到時間結束", "可以先上傳簡單版拿部分分，之後再上傳更好的版本。"],
    ["程式檔名要照題目規定", "檔名錯了，系統找不到你的程式。"],
    ["程式存在桌面的 backup 資料夾", "系統會自動備份到伺服器，不要存到別的地方。"],
    ["提早交卷之後就不能再上傳", "確定每一題都上傳完成再交卷。"],
])}
  <p style="font-size:.88rem;color:var(--text-faint)">資料來源：<a href="https://apcs.csie.ntnu.edu.tw/wp-content/uploads/2025/08/APCS%E4%BD%9C%E7%AD%94%E7%B3%BB%E7%B5%B1%E8%AA%AA%E6%98%8E.pdf" target="_blank" rel="noopener">APCS 作答系統說明（官方）↗</a>，實際規定以當次考試公告為準。</p>''')

body += section("06", "子題配分：先拿 60 分，再拚 100 分", f'''
  <p>中級每一題都分成兩個子題，例如官方範例「特殊位置」：</p>
{table(["子題", "配分", "限制"], [["第 1 子題", "60 分", "<code>n = 1</code>（只有一列）"], ["第 2 子題", "40 分", "無額外限制"]])}
  <p>意思是：<strong>就算你只會處理「只有一列」的情況，也能拿 60 分</strong>。中級 3 級分只要 150 分，三題都先拿到 60 分就有 180 分了。</p>
  <ol>
    <li>先讀子題限制，寫出能過第 1 子題的版本，測過範例後<strong>上傳</strong>。</li>
    <li>把這個版本<strong>另存一份</strong>（例如 <code>p1_60.py</code>），再改進完整版。</li>
    <li>完整版測過才上傳；如果時間不夠、改壞了，就把 60 分的版本再上傳回去。</li>
  </ol>
{callout("⚠ 不要卡在一題", "實作考 120 分鐘、3 題，平均一題 40 分鐘。卡住超過 15 分鐘就先換下一題，回頭再寫。", "warn")}''')

body += section("07", "ZeroJudge 送出步驟", f'''
  <ol>
    <li>到 <a href="https://zerojudge.tw/" target="_blank" rel="noopener">zerojudge.tw ↗</a> 註冊、登入（可以用 Google 帳號）。</li>
    <li>打開題目（課程規劃頁的題號都可以直接點）。</li>
    <li>先在 IDLE 寫好、用範例測過。</li>
    <li>按題目頁的「解題」，語言選 <strong>Python</strong>，把整個程式貼上，送出。</li>
    <li>看結果：AC 就完成；不是 AC 就點進去看是哪一筆測資錯、錯誤訊息是什麼。</li>
  </ol>
{callout("📌 第一題就從這裡開始", "ZeroJudge <a href='https://zerojudge.tw/ShowProblem?problemid=a001' target='_blank' rel='noopener'>a001 哈囉</a>：讀入一個字串，印出 <code>hello, 字串</code>。注意逗號後面有一個空白——這就是「輸出格式要一字不差」的第一次練習。", "tip")}''')

body += qa([
    ("題目要求：讀入兩個整數（各一行），輸出兩數相加的結果。下面這個程式送上 Judge 會得到什麼結果？為什麼？",
     'x = int(input("x="))\ny = int(input("y="))\nprint("x+y =", x + y)',
     "會是 <strong>WA</strong>。兩個 <code>input()</code> 的提示文字和 <code>\"x+y =\"</code> 都會被印出來，跟答案只有一個數字不一樣。改成 <code>x = int(input())</code>、<code>print(x + y)</code>。", "4\n6"),
    ("題目要求：一行讀入 n 個整數，<strong>由小到大</strong>輸出，用一個空白隔開。這個程式哪裡會錯？",
     'a = list(map(int, input().split()))\na.sort()\nprint(a)',
     "印出了中括號和逗號，會被判 <strong>WA</strong>。改成 <code>print(*a)</code>。", "5 2 9 1"),
    ("題目要求：輸入 n 個成績，輸出平均（保證整除）。範例輸入 <code>80 90 100</code>，範例輸出 <code>90</code>。這個程式會印出什麼？",
     'a = list(map(int, input().split()))\nprint(sum(a) / len(a))',
     "印出 <code>90.0</code>，多了 <code>.0</code>，<strong>WA</strong>。題目保證整除時用 <code>//</code>。", "80 90 100"),
    ("題目的輸入是「第一行一個整數 n，第二行 n 個整數」，要輸出 n 個整數的總和。範例輸入第一行是 <code>3</code>、第二行是 <code>5 2 9</code>。下面這個程式會印出什麼？",
     'a = list(map(int, input().split()))\nprint(sum(a))',
     "這個程式想算總和，卻只印出 <code>3</code>：<code>a = list(map(int, input().split()))</code> 只讀了第一行，把 n 當成資料，第二行根本沒讀到。要先 <code>n = int(input())</code>，再讀第二行。<a href='unit04b.html'>單元 4 附</a>的「多行輸入」會整理所有常見格式。", "3\n5 2 9"),
])

page("unit02b.html", title="單元 2 附：上機評測基本功（ZeroJudge 與考場規則）", crumb="單元 2 附",
     kicker="起點篇　補充單元", h1="上機評測基本功：ZeroJudge 與考場規則",
     sub="邏輯都對卻拿 0 分？大多是輸入輸出格式的問題。第一次上 ZeroJudge 之前先讀這一頁。",
     goals=["知道 Judge 怎麼評分，看得懂 AC、WA、TLE、RE、CE 是什麼意思",
            "寫 Judge 題目時，<code>input()</code> 不放提示文字、輸出不多印說明文字",
            "會用 <code>print(*a)</code>、<code>sep</code>、<code>end</code> 控制輸出格式",
            "知道 APCS 考場只評分最後一次上傳的檔案，懂得「先拿子題分數」的作答策略"],
     body=body, unit=2,
     prev=("unit02.html", "變數、資料型態與輸出入"), next=("unit03.html", "運算子大全：算術・比較・邏輯・位元"))
