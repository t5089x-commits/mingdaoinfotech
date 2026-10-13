"""產生 schedule.html（課程規劃／練習題目表）。"""
from lib import *
import py125 as W

ZJT = {
    "a001": "哈囉", "d049": "中華民國萬歲！", "d060": "還要等多久啊？", "k200": "三人行必有我師", "a621": "Powers of Two",
    "b971": "等差數列", "d065": "三人行必有我師（1 行版）", "a005": "Eva 的回家作業", "b964": "成績指標", "c290": "秘密差",
    "f312": "人力分配", "f818": "物競天擇", "c295": "最大和", "j605": "程式考試", "c462": "交錯字串", "q182": "字串操作",
    "f579": "購物車", "i400": "字串解碼", "j606": "造字程式", "h027": "矩陣總和", "o712": "蒐集寶石", "m932": "蜜蜂觀察",
    "k732": "特殊位置", "o077": "電子畫布", "b965": "矩陣轉換", "c292": "數字龍捲風", "r488": "彗星撞擊", "r489": "航空拍照圖",
    "r490": "商品包裝地", "h026": "猜拳", "c294": "三角形辨別", "o711": "裝飲料", "m931": "遊戲選角", "e313": "最少相異字母",
    "g275": "七言對聯", "g276": "魔王迷宮", "f580": "骰子", "d212": "東東爬階梯",
}
OFFICIAL = {"i400", "o712", "k732"}
CHALLENGE = {"c292"}

def zj(i, lvl=True):
    bonus = i.startswith("+")
    i = i.lstrip("+")
    cls = "zj" + (" official" if i in OFFICIAL else "") + (" challenge" if i in CHALLENGE else "") + (" bonus" if bonus else " must")
    tag = "<small>★官方範例</small>" if i in OFFICIAL else ("<small>挑戰</small>" if i in CHALLENGE else "")
    if lvl:
        tag += "<small class=\"lvl\">加分</small>" if bonus else "<small class=\"lvl\">必寫</small>"
    return f'<a class="{cls}" href="https://zerojudge.tw/ShowProblem?problemid={i}" target="_blank" rel="noopener"><b>{i}</b>{ZJT[i]}{tag}</a>'

def qc(qs):
    if not qs:
        return '<span class="muted">—</span>'
    return '<div class="qchips">' + "".join(f'<button type="button" class="qchip" data-q="{q}" title="看第 {q} 題">{q}</button>' for q in qs) + "</div>"

TYPE = {"intro": "導論", "impl": "實作", "read": "識讀", "both": "實作＋識讀"}
c = lambda t: "".join(f"<code>{E(p)}</code>" if k % 2 else E(p) for k, p in enumerate(t.split("`")))

# (節次, 類型, 主題, [(連結, 章節名)], 內容重點, 官方範例, ZeroJudge)
WEEKS = [
  ("1", "Python 基礎與程式流程", "從變數、判斷、迴圈到 APCS 最常見的輸入寫法，同時開始練習追蹤程式。", [
    ("1", "intro", "APCS 介紹與考場環境", [("unit01.html", "單元 1"), ("unit01b.html", "單元 1 附")], "新制架構、題本與級分、技高升學用途、報名時程、IDLE 操作", [], []),
    ("2", "impl", "變數與輸出入", [("unit02.html", "單元 2"), ("unit02b.html", "單元 2 附")], "資料型態、`input()`（一律空括號）、`print()`、`sep` / `end`、f-string；Judge 的輸出格式", [], ["a001", "+d049"]),
    ("3", "both", "運算子", [("unit03.html#s01", "單元 3 §01–03（§02 只到真值表）")], "算術、`//` 與 `%`（含負數）、比較、邏輯 `and`／`or`／`not`、複合指定 `+=`", [20], ["d060"]),
    ("4", "both", "條件判斷＋看懂錯誤訊息", [("unit04.html#s01", "單元 4 §01"), ("unit09.html#s04", "單元 9 §04")], "`if` / `elif` / `else`、巢狀判斷、`if n:`（0 與空字串視為假）；第一次看到紅字：縮排、語法、名字錯誤", [10, 27], ["k200"]),
    ("5", "both", "迴圈", [("unit04.html#s02", "單元 4 §02")], "`for`、`while`、`range()` 起點／終點／間隔（含負數）、break／continue", [19, 26], ["b971", "+a621"]),
    ("6", "read", "程式追蹤：巢狀迴圈與運算子細節", [("unit02.html#s05", "單元 2 §05"), ("unit04.html#s03", "單元 4 §03"), ("unit03.html#s02", "單元 3 §02 真假值與回傳值、§04"), ("unit09.html#s02", "單元 9 §02")], "開頭 5 分鐘：字串的 `+` 與 `*`、`True` 當 1（印圖形要用到）；追蹤表技巧、字串乘法印圖形；用識讀題帶 `and`／`or` 的回傳值與運算子優先順序", [2, 5, 12], []),
    ("7", "both", "輸入技巧＋識讀題組", [("unit04b.html", "單元 4 附"), ("unit08.html#s04", "單元 8 §04")], "`split()`、`map()`、串列生成式、多行輸入、`sorted()`；經典迴圈：費氏數列、GCD", [7, 9], ["d065", "+a005", "+b964", "+c290", "+f312"]),
  ]),
  ("2", "串列、字串與函式", "中級題本的前兩大類：串列與字串。最後把函式學起來，替第 3 次課的遞迴打底。", [
    ("1", "both", "串列基礎", [("unit05.html#s01", "單元 5 §01–03")], "`[0] * n`、索引、切片、`len()`、`append()`、`a, b = b, a` 交換", [15], ["f818"]),
    ("2", "both", "串列常見樣式", [("unit05.html#s04", "單元 5 §04–05"), ("unit08.html#s04", "單元 8 §04")], "`max()`、`min()`、`sum()`、`count()`、`index()`、`in`、索引用 `%` 繞圈；前綴和", [24, 25, 30], ["j605", "+c295"]),
    ("3", "impl", "字元判斷與轉換", [("unit06.html#s01", "單元 6 §01–02")], "`s[i]`、`for c in s`、`isupper()`、`isdigit()`、`int(c)`、`str(n)`（ASCII 與 `ord()`／`chr()` 為補充）", [], []),
    ("4", "impl", "字串處理", [("unit06.html#s03", "單元 6 §03–04")], "切片、`split()`、`join()`、`replace()`、`find()`", [], ["q182", "+c462"]),
    ("5", "impl", "字典計數＋字串實作", [("unit06.html#s05", "單元 6 §05")], "`dict`、`get()`、`max(d, key=d.get)`；字串模擬題（官方範例 i400 先拿第 1 子題）", [], ["i400", "+f579", "+j606"]),
    ("6", "read", "函式基礎", [("unit07.html", "單元 7 §01–06")], "`def`、`return`、參數、區域與全域變數", [], []),
    ("7", "both", "小測＋識讀題組", [("unit09.html#s03", "單元 9 §03")], "字串實作題；串列與函式追蹤題", [17], []),
  ]),
  ("3", "遞迴與二維資料", "上午趁精神最好時追遞迴（識讀的重點題型，官方識讀範例 30 題中有 9 題）；下午動手寫中級題本最常卡人的二維模擬與矩陣操作。", [
    ("1", "read", "遞迴（一）：呼叫追蹤", [("unit07.html#s06", "單元 7 §06（複習）"), ("unit07.html#s07", "單元 7 §07"), ("unit07b.html#s01", "單元 7 附 §01–03")], "開場 10 分鐘複習函式：`return`、參數、區域變數（用單元 7 的互動追蹤）；終止條件、呼叫樹、由小算到大；階乘、次方、GCD、費氏", [11, 14, 21, 23], []),
    ("2", "read", "遞迴（二）：進階題型", [("unit07b.html#s04", "單元 7 附 §04–07")], "列表法、print 的順序、互相呼叫、遞迴填空與除錯", [1, 3, 8, 13, 16], []),
    ("3", "impl", "二維串列", [("unit06b.html#s01", "單元 6 附 §01–03")], "`[[0]*m for _ in range(n)]`、讀取矩陣、雙層走訪", [], ["h027"]),
    ("4", "impl", "範圍枚舉與邊界", [("unit06b.html#s04", "單元 6 附 §04")], "座標出界檢查、`abs()` 計算距離、雙層 `range()` 枚舉範圍、用 `max()` / `min()` 夾範圍；官方範例 k732 先拿第 1 子題 60 分", [], ["k732", "+o077"]),
    ("5", "both", "網格模擬", [("unit06b.html#s05", "單元 6 附 §05")], "方向陣列與轉向、撞牆轉彎的移動模擬；官方範例 o712 先拿第 1 子題", [18], ["o712", "+m932"]),
    ("6", "impl", "矩陣操作", [("unit06b.html#s06", "單元 6 附 §06")], "矩陣旋轉、翻轉、逐格比對、`[::-1]`", [], ["b965"]),
    ("7", "both", "小測＋識讀題組", [("unit06b.html#s07", "單元 6 附 §07")], "二維實作題；遞迴追蹤題", [], ["+c292"]),
  ]),
  ("4", "APCS 模擬與補強", "上午補齊搜尋與執行次數，接著識讀模擬考與檢討；午休後連排實作模擬考。", [
    ("1", "read", "搜尋與執行次數", [("unit09.html#s05", "單元 9 §05–06")], "找錯與設計測資、循序 vs 二分搜尋、迴圈與搜尋的執行次數、寫成 `O( )`（時間複雜度）、佇列模擬（錯誤訊息第 1 次課已教，快速複習）", [4, 6, 22, 28, 29], []),
    ("2–3", "read", "程式識讀模擬考", [("mock.html", "線上作答頁"), ("unit09.html#s07", "單元 9 §07")], "吳邦一 125 題保留的 30 題（易、中、難各 10 題），限時 90 分鐘，兩節連排：中間下課照常計時，可以上廁所，不交談、題目不帶出教室。紙本或線上作答頁擇一", [], []),
    ("4", "read", "識讀模擬考檢討", [("unit09.html#s03", "單元 9 §03")], "對答案、講解錯最多的題目、訂正；對照統整表找出要回去複習的單元。順口帶課程沒講過的兩個寫法：`.clear()` 清空串列、`for t in (-5, -1, 5)` 走訪 tuple（單元 5 §03、§05 有補充）", [], []),
    ("5–7", "impl", "程式實作模擬考", [("unit02b.html#s05", "單元 2 附 §05–06")], "午休後連排：2025 年 10 月中級真題 3 題，限時 120 分鐘，剩下約 30 分鐘檢討", [], ["r488", "r489", "r490"]),
  ]),
]
DATES = {"1": ("115/10/31（六）", "115/11/7（六）"), "2": ("115/11/14（六）", "115/11/21（六）"),
         "3": ("115/12/5（六）", "115/12/12（六）"), "4": ("115/12/19（六）", "116/1/9（六）")}

APPLY = {
    "1": ("預告：2027/1/10 的 APCS 檢測，報名期間是 <b>11/23～12/11</b>（每天 9:00～18:00）。參加培訓班不等於報名，要自己上 APCS 官網報名。",
          "預告：2027/1/10 的 APCS 檢測，報名期間是 <b>11/23～12/11</b>（每天 9:00～18:00）。參加培訓班不等於報名，要自己上 APCS 官網報名。"),
    "2": ("1/10 檢測 <b>11/23 開放報名</b>，下次上課（12/5）會再確認誰報好了。",
          "後天 <b>11/23 開放報名、12/11 截止</b>，這段期間沒有上課，請回家自己報名，收到「報名完成通知」email 後截圖傳到班級群組。"),
    "3": ("1/10 檢測報名 <b>12/11 截止</b>，還沒報的今天下課前確認；3/14 檢測的報名是 12/7～12/25。",
          "1/10 檢測的報名已在 12/11 截止；想考的同學請報 <b>3/14 檢測（12/7～12/25 報名）</b>。"),
    "4": ("1/10 檢測 <b>1/4 起可查考場</b>；沒報到 1 月的同學，3/14 檢測報名到 <b>12/25</b>。",
          "<b>明天（1/10）就是檢測</b>：確認考場、帶證件，考場只算最後一次上傳。沒考到或想再考的，下一次是 6/13（報名日期看官網）。"),
}

REG = '''<section class="block" id="apply">
  <h2><span class="num">📣</span>APCS 檢測報名時程（請學生自己報名）</h2>
  <p>培訓班和 APCS 檢測是分開的，<strong>學生要自己到 <a href="https://apcs.csie.ntnu.edu.tw/" target="_blank" rel="noopener">APCS 官網 ↗</a> 報名</strong>。下面是官網公告的日程（以官網最新公告為準），每一次課的表格上方也有當天要提醒的事。</p>
''' + table(["檢測日期", "報名期間（每天 9:00～18:00）", "第一梯", "第二梯"], [
    ["<strong>2027/1/10（日）</strong>", "2026/11/23～12/11<br><small>考場查詢 1/4～1/10，成績 1/22 公布</small>", "第 3 次課（12/5）在報名期間內，當天確認", "上課日 11/21、12/12 <strong>都不在報名期間內</strong>：11/21 先說明，回家自己報名"],
    ["<strong>2027/3/14（日）</strong>", "2026/12/7～12/25", "第 4 次課（12/19）還來得及報", "第 3 次課（12/12）在報名期間內"],
    ["<strong>2027/6/13（日）</strong>", "依官網公告", "1、3 月沒考好可以再考", "1、3 月沒考好可以再考"],
]) + callout("⚠ 報名要注意", "報完請到信箱確認「報名完成通知」；要改資料或取消，也是在報名期間內上官網辦理。證件號碼、姓名填錯，要在報名截止後 3 日內把證件掃描檔寄到 apcs@ntnu.edu.tw 更正。", "warn") + '''</section>

'''

HW_ZJ = {"1": [("h026", "APCS 第1題・判斷"), ("c294", "APCS 第1題・排序＋判斷"), ("o711", "APCS 第1題・迴圈模擬")],
         "2": [("m931", "APCS 第1題・串列"), ("e313", "字串・計數"), ("g275", "APCS 第1題・字串規則")],
         "3": [("g276", "APCS 第2題・二維模擬"), ("f580", "APCS 第2題・模擬"), ("d212", "遞迴／由小算到大")]}
HW_UNITS = {"1": ["unit02.html", "unit03.html", "unit04.html", "unit04b.html"],
            "2": ["unit05.html", "unit06.html", "unit07.html"],
            "3": ["unit06b.html", "unit07b.html"]}

HANDOUT = {"1": "hw1-reading.pdf", "2": "hw2-reading.pdf", "3": "hw3-reading.pdf"}

HW_TITLE = {"1": "第 1 次課　回家識讀練習", "2": "第 2 次課　回家識讀練習", "3": "第 3 次課　回家識讀練習＋考前加練"}

def homework(wk):
    if wk == "4":
        return ""
    zrows = "".join(f'<li>{zj(i, False)}<span class="hw-kind">{k}</span></li>' for i, k in HW_ZJ[wk])
    units = HW_UNITS[wk] + (["unit09.html"] if wk == "3" else [])
    qs = sorted(q for f in units for q in W.open_qs(W.unit_qs(f)[2]))
    cnt = {d: sum(W.DIFF[q] == d for q in qs) for d in "易中難"}
    labels = "、".join(W.unit_qs(f)[0] for f in units)
    return f'''  <div class="homework">
    <h3>🏠 本週回家練習題目（下次上課前完成）</h3>
    <p class="hw-row"><strong>實作 ZeroJudge</strong></p>
    <ul class="hw-list">{zrows}</ul>
    <p class="hw-row"><strong>識讀 125 題回家作業</strong></p>
    <a class="hw-pdf" href="assets/handouts/{HANDOUT[wk]}" target="_blank" rel="noopener">📄 {HW_TITLE[wk]}（PDF）<small>共 {len(qs)} 題：易 {cnt['易']}、中 {cnt['中']}、難 {cnt['難']}</small></a>
    <p class="hw-read">範圍：{labels}{"（單元 9 是第 4 次課前的考前加練）" if wk == "3" else ""}。上課會發紙本，題號與吳邦一原題本相同，第一頁有作答欄。</p>
  </div>
'''

body = '''  <section class="unit-hero">
    <span class="kicker">資電APCS週六課程　4 次 × 7 節</span>
    <h1>課程規劃（練習題目表）</h1>
    <p>每一次課的節次安排、對應的教材章節、課堂練習題，以及回家要寫的題目，都整理在這一頁。</p>
  </section>

<div class="goals">
  <h2>🎯 課程目標</h2>
  <ul>
    <li><strong>程式識讀：4 級分</strong>（70 分以上，30 題至少答對 21 題），選考 Python 題本</li>
    <li><strong>程式實作：報考中級題本，目標 3 級分</strong>（150 分以上；中級三題中至少穩拿兩題）</li>
    <li>全程使用 Python，從基礎語法開始教起</li>
  </ul>
</div>

''' + REG + '''<section class="block">
  <h2><span class="num">ℹ️</span>怎麼看這張表</h2>
  <div class="grid cols-3">
    <div class="tile"><h4><span class="ico">🗓️</span>28 節課</h4><p>每次 7 節、每節 50 分鐘，共 4 次（星期六 08:15～16:10）。前段講解搭配隨堂練習，後段實作。第 1 次最後一節是識讀題組，第 2、3 次最後一節小測，第 4 次是兩場模擬考與檢討。</p></div>
    <div class="tile"><h4><span class="ico">📖</span>主題下方的小標籤</h4><p>是這一節對應的教材章節，例如「單元 4 §02」就是單元 4 的第 02 節，按一下直接跳過去。</p></div>
    <div class="tile"><h4><span class="ico">⚖️</span>依進度調整</h4><p>這是初步規劃，實際上課會依學生程度與學習進度，彈性調整各單元內容與練習比重。</p></div>
  </div>
''' + table(["欄位", "題目來源", "按下去會"], [
    ["官方識讀範例", "APCS 官方《程式識讀題目範例（Python 題本）》30 題，當作課堂例題", "跳出那一題的題目（預設隱藏答案）"],
    ["ZeroJudge 練習", "ZeroJudge 解題系統的 APCS 歷屆題與基礎題，課堂實作用。<strong>實線框「必寫」</strong>每節一定要完成；<strong>虛線框「加分」</strong>寫完必寫題再挑戰", "開啟 ZeroJudge 題目頁"],
    ["🏠 回家練習", "第 1～3 次課後：ZeroJudge 3 題＋吳邦一〈Python 程式識讀 125 題〉（每次課後發一份紙本 PDF）", "ZeroJudge 題目頁／回家作業 PDF"],
]) + '''</section>

<nav class="week-jump" aria-label="課次快速跳轉">
'''
for wk, name, _, _ in WEEKS:
    body += f'  <a href="#week{wk}"><b>第 {wk} 次</b><span>{name}</span></a>\n'
body += '  <a href="#resources"><b>資源</b><span>練習資源與使用說明</span></a>\n</nav>\n'

for wk, name, desc, rows in WEEKS:
    trs = ""
    for p, t, topic, chaps, detail, qs, zjs in rows:
        ch = '<span class="chap">' + "".join(f'<a href="{h}">📖 {l}</a>' for h, l in chaps) + "</span>"
        z = "".join(zj(i, wk != "4") for i in zjs) if zjs else '<span class="muted">—</span>'
        trs += (f'        <tr><td>{p}</td><td><span class="type {t}">{TYPE[t]}</span></td>'
                f'<td class="topic">{E(topic)}{ch}</td><td class="detail">{c(detail)}</td>'
                f'<td class="refs">{qc(qs)}</td><td>{z}</td></tr>\n')
    body += f'''
<section class="block" id="week{wk}">
  <h2><span class="num">#{wk}</span>第 {wk} 次・{name}</h2>
  <p class="dates">📅 第一梯 {DATES[wk][0]}　｜　第二梯 {DATES[wk][1]}</p>
  <div class="apply-note">📣 <b>報名提醒</b><ul><li>第一梯：{APPLY[wk][0]}</li><li>第二梯：{APPLY[wk][1]}</li></ul></div>
  <p>{desc}</p>
  <div class="table-wrap">
    <table class="plan">
      <thead><tr><th>節次</th><th>類型</th><th>主題（對應章節）</th><th>內容重點</th><th>官方識讀範例</th><th>ZeroJudge 練習</th></tr></thead>
      <tbody>
{trs}      </tbody>
    </table>
  </div>
{homework(wk)}</section>
'''

# 練習資源：說明＋125 題分類表（不再重複列 ZeroJudge 題目）
urows = []
for f, label, topic, qs in W.UNITS:
    easy, hard = W.split(W.open_qs(qs))
    urows.append([f'<a href="{f}#py125">{label}</a>', topic, W.chips(easy), W.chips(hard) if hard else '<span class="muted">—</span>'])
for t, qs in W.EXT:
    urows.append(["延伸", t, W.chips(qs), '<span class="muted">—</span>'])

body += section("📚", "練習資源與使用說明", f'''
  <h3>🧩 ZeroJudge（實作）</h3>
  <p>ZeroJudge 送出後由系統自動用測資評分，跟 APCS 正式考試一樣。請先到 <a href="https://zerojudge.tw/" target="_blank" rel="noopener">zerojudge.tw ↗</a> 註冊帳號，送出時語言選 <strong>Python</strong>。第一次送出前，先讀 <a href="unit02b.html">單元 2 附：上機評測基本功</a>。上面各次課的表格裡，「ZeroJudge 練習」欄就是課堂題目，按題號可以直接開啟。</p>
{table(["題目類型", "難度", "怎麼練"], [
    ["基礎題庫（a001、d049…）", "入門", "練輸入輸出、運算、判斷、迴圈的基本寫法"],
    ["APCS 第 1 題（b964、c290…）", "約等於現在的初級", "練熟迴圈與串列，每題 20～30 分鐘內寫完"],
    ["APCS 第 2 題（標 <strong>★官方範例</strong> 的三題就是官方中級題本範例）", "約等於現在的中級", "先拿子題的 60 分，再拚完整解"],
    ["標「挑戰」的題目（c292）", "舊制第 3 題，比中級難", "學有餘力再寫"],
])}
  <p>2025 年 10 月的三題中級真題（r488～r490）保留到第 4 次課的模擬考，之前先不要寫。</p>

  <h3>📝 吳邦一〈APCS Python 程式識讀 125 題〉（識讀回家作業）</h3>
  <p>中正大學資工系吳邦一教授為 Python 初學者寫的程式識讀模擬題，難度分易、中、難，每一題的解答都附說明（作者同意教學使用與分享，<a href="{W.DRIVE}" target="_blank" rel="noopener">作者原始連結 ↗</a>）。我們把題目依單元分好，<strong>每次課後一次發一份紙本</strong>，就是各次課「本週回家練習題目」裡的 PDF；另外保留 30 題（易、中、難各 10 題）當第 4 次課的識讀模擬考，不會出現在回家作業裡。</p>
{callout("💡 怎麼寫回家作業", "① 每一題都用紙筆追蹤，不要用電腦跑；② 先做「易」「中」，「難」是挑戰題（每題右上方有標）；③ 下次上課對答案，錯的題目回去看對應單元。", "tip")}

  <h3>📄 官方識讀範例 30 題</h3>
  <p>各次課表格裡的「官方識讀範例」欄。30 題依主題、依單元的完整對照，在 <a href="unit09.html#s07">單元 9 §07 各單元的識讀重點統整</a>。</p>
''', sid="resources")

HEAD_S = HEAD.split("<div class=\"goals\">")[0]
HEAD_S = HEAD_S.split("  <section class=\"unit-hero\">")[0]
s = HEAD_S.format(title="課程規劃（練習題目表）", crumb="課程規劃（練習題目表）", unit="", extra_css="")
s = s.replace('<main class="wrap" data-unit="">', '<main class="wrap">')
s = s.replace('<a href="schedule.html">', '<a href="schedule.html" class="on" aria-current="page">', 1)
s += body
s += FOOT.format(prev='<a class="prev" href="index.html"><div class="dir">← 回課程首頁</div><div class="ttl">資電APCS週六課程</div></a>',
                 next='<a class="next" href="functions.html"><div class="dir">下一頁 →</div><div class="ttl">函式與語法統整表</div></a>', extra_js="")
open(ROOT + "schedule.html", "w", encoding="utf-8").write(s)
print("wrote schedule.html", len(s))
