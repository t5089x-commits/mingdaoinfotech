"""吳邦一〈APCS Python 程式識讀 125 題〉依單元分類（題號、難度、PDF 頁碼）。
分類依據：每題解答裡作者寫的「出題用意」，再對照題目程式內容。"""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
_d = json.load(open(os.path.join(HERE, "py125_pages.json"), encoding="utf-8"))
QP = {int(k): v for k, v in _d["q"].items()}     # 題目所在頁
AP = {int(k): v for k, v in _d["a"].items()}     # 解答所在頁
DIFF = {i + 1: c for i, c in enumerate(_d["diff"])}
ANS = {int(k): v for k, v in _d["ans"].items()}

# 第 4 次課識讀模擬考：保留 30 題，不放進回家作業與單元頁（易、中、難各 10 題）
MOCK = sorted([1, 7, 16, 17, 30, 32, 57, 100, 111, 115,        # 易
               6, 38, 52, 56, 63, 65, 67, 79, 93, 117,          # 中
               22, 45, 50, 70, 73, 77, 83, 91, 97, 103])        # 難

PDF = "assets/reading/wu-python-reading-125.pdf"
DRIVE = "https://drive.google.com/file/d/1WaZOpxgcz23vEil2UOzLWXrtYeUr0Nnc/view?usp=drive_link"

# 單元 → (主題說明, 題號)；「ext」是本課程沒教或屬於中高級的延伸題
UNITS = [
    ("unit02.html",  "單元 2", "變數、型態轉換、字串的 + 與 *", [3, 5, 7, 10, 17, 18, 20, 24, 25, 26, 27]),
    ("unit03.html",  "單元 3", "算術、// 與 %、比較與邏輯、and／or 回傳值", [1, 2, 6, 15, 16, 21, 22, 23]),
    ("unit04.html",  "單元 4", "if／elif、for range、while、巢狀迴圈", [30, 31, 32, 33, 34, 35, 38, 40, 43, 45, 111]),
    ("unit04b.html", "單元 4 附", "input().split()、串列生成式與轉型", [12, 13, 14, 28]),
    ("unit05.html",  "單元 5", "串列：sum／max、in、走訪、切片、複製、排序、生成式", [29, 46, 47, 48, 49, 50, 51, 52, 53, 55, 56, 57, 58, 86, 87, 89, 113, 114, 115, 120, 121, 125]),
    ("unit06.html",  "單元 6", "字串：切片、迴文、逐字處理、字典序、sorted", [19, 62, 63, 69, 82, 90, 91, 92, 95, 108, 109, 122, 123, 124]),
    ("unit06b.html", "單元 6 附", "二維串列、串列裡的串列", [88, 93, 94, 118]),
    ("unit07.html",  "單元 7", "函式：參數傳遞、區域與全域變數", [36, 37, 64, 65, 66, 67, 68, 72, 74, 77]),
    ("unit07b.html", "單元 7 附", "遞迴：追蹤與推理", [70, 71, 73, 75, 97, 116, 117]),
    ("unit09.html",  "單元 9", "常見執行錯誤、除錯、執行次數與時間複雜度、用 head 模擬佇列", [4, 9, 54, 78, 79, 80, 81, 83, 84, 85, 98, 99, 100, 101, 103, 105, 106, 107]),
]
EXT = [
    ("for／while 搭配 else（本課程沒教，Python 才有的語法）", [39, 41, 42, 44]),
    ("位元運算與二進位（單元 3 補充）", [59, 60, 61, 110]),
    ("佇列進階與堆疊（中高級）", [8, 11, 76, 112]),
    ("遞迴的時間複雜度、DFS（中高級）", [96, 102, 104, 119]),
]

def all_assigned():
    got = [q for _, _, _, qs in UNITS for q in qs] + [q for _, qs in EXT for q in qs]
    return got

if __name__ == "__main__":
    got = all_assigned()
    dup = sorted({q for q in got if got.count(q) > 1})
    miss = [q for q in range(1, 126) if q not in got]
    print("total", len(got), "dup", dup, "missing", miss)

LABEL = {"易": "易", "中": "中", "難": "難"}
CLS = {"易": "d1", "中": "d2", "難": "d3"}

def chip(q):
    d = DIFF[q]
    return (f'<a class="wq {CLS[d]}" href="{PDF}#page={QP[q]}" target="_blank" rel="noopener" '
            f'title="Q{q:03d}・{d}・題目在第 {QP[q]} 頁，解答在第 {AP[q]} 頁">{q}</a>')

def chips(qs):
    return '<span class="wqs">' + "".join(chip(q) for q in qs) + "</span>"

def open_qs(qs):
    """去掉保留給模擬考的題目"""
    return [q for q in qs if q not in MOCK]

def split(qs):
    qs = open_qs(qs)
    easy = [q for q in qs if DIFF[q] in "易中"]
    hard = [q for q in qs if DIFF[q] == "難"]
    return easy, hard

LEGEND = ('<span class="wq-legend"><span class="wq d1">易</span><span class="wq d2">中</span><span class="wq d3">難</span>'
          '按題號會開啟 PDF 並跳到題目那一頁；解答在 PDF 後半（第 50 頁起），題號相同。</span>')

def unit_qs(fn):
    for f, label, topic, qs in UNITS:
        if f == fn:
            return label, topic, qs
    return None

UNIT_EXT = {"unit03.html": 1, "unit04.html": 0, "unit09.html": None}

# 各單元課後練習改放「APCS 官方識讀範例」（吳邦一 125 題改成每次課後一次發紙本）
OFFICIAL_TOPIC = {
    1: "遞迴：依條件分支的回傳值", 2: "迴圈：while 條件填空", 3: "遞迴：依回傳值反推參數", 4: "佇列：head／tail 模擬",
    5: "迴圈：印星號圖形除錯", 6: "搜尋：循序 vs 二分的執行次數", 7: "迴圈：費氏數列填空", 8: "遞迴：兩個函式互相呼叫",
    9: "經典：輾轉相除法（迴圈）", 10: "條件：巢狀 if 與 0 視為假", 11: "遞迴：階乘的終止條件除錯", 12: "迴圈：依輸出反推 while 參數",
    13: "遞迴：迴圈中呼叫遞迴函式", 14: "遞迴：費氏數列", 15: "串列：對稱交換兩次", 16: "遞迴：依回傳值反推終止條件",
    17: "條件：判斷順序錯誤（除錯）", 18: "二維串列：方向陣列", 19: "迴圈：range 負的間隔", 20: "運算子：% 與 // 找零",
    21: "遞迴：次方", 22: "搜尋：二分搜尋除錯與測資", 23: "遞迴：最大公因數 GCD", 24: "串列：最大值與最小值",
    25: "串列：用 % 讓索引循環", 26: "迴圈：range 的執行次數", 27: "條件：永遠不會執行的程式碼", 28: "複雜度：巢狀迴圈次數",
    29: "串列：設計測資找出錯誤", 30: "串列：前綴和",
}
OFFICIAL_BY_UNIT = {
    "unit03.html": [20],
    "unit04.html": [2, 5, 10, 12, 19, 26, 27],
    "unit04b.html": [7, 9],
    "unit05.html": [15, 24, 25, 29, 30],
    "unit06b.html": [18],
    "unit07b.html": [1, 3, 8, 11, 13, 14, 16, 21, 23],
    "unit09.html": [4, 6, 17, 22, 28, 29],
}

def unit_block(fn):
    qs = OFFICIAL_BY_UNIT.get(fn)
    if not qs:
        return ""
    items = "".join(
        f'<li><button type="button" class="qchip" data-q="{q}" title="看官方識讀範例第 {q} 題">{q}</button>'
        f'<span>{OFFICIAL_TOPIC[q]}</span></li>' for q in qs)
    return f'''
<section class="block py125" id="py125">
  <h2><span class="num">📝</span>課後識讀練習：APCS 官方識讀範例</h2>
  <p>APCS 官方《程式識讀題目範例（Python 題本）》裡跟這一單元有關的 {len(qs)} 題，跟<a href="schedule.html">課程規劃</a>上課用的是同一批。按題號會跳出題目（預設隱藏答案），先自己用紙筆追蹤，再按「顯示官方答案」對答案。</p>
  <ul class="official-list">{items}</ul>
  <p class="muted">吳邦一〈Python 程式識讀 125 題〉會在每次課後一次發紙本，見課程規劃各次課的「本週回家練習題目」。</p>
</section>
'''

def add_unit_block(html_text, fn):
    import re
    html_text = re.sub(r'[ \t]*<section class="block py125" id="py125">.*?</section>\s*', "", html_text, flags=re.S)
    b = unit_block(fn)
    if not b:
        return html_text
    if "assets/reading-viewer.js" not in html_text:
        html_text = html_text.replace('<script src="assets/script.js"></script>',
                                      '<script src="assets/script.js"></script>\n<script src="assets/reading-viewer.js"></script>', 1)
    i = html_text.find('<nav class="unit-nav">')
    return html_text[:i] + b.lstrip("\n") + "\n  " + html_text[i:]
