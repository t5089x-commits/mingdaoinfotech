# 資訊科技教學網 — 架構說明（給老師 / 給接手的對話窗看）

這份文件是整個網站的「地圖」。之後不管是你自己看，還是把某一科的資料夾丟回當初
做那一科的對話去改，都先看這份文件，了解目前的共用規則，避免改壞其他科或共用檔案。

## 1. 資料夾結構

```
/ (repo 根目錄 = GitHub Pages 首頁)
├── index.html              ← 總首頁，連到五科＋apcs-ee 共六個課程首頁
├── MANIFEST.md              ← 就是這份文件
├── shared/                  ← 五科共用的檔案，任何一科的對話都「不要」單獨修改，
│                               要改請先確認會不會影響其他科
│   ├── core/
│   │   ├── progress.js      ← ★ 五科進度總表，老師改這一個檔案就能調整全部科目
│   │   │                       （見第 3 節）
│   │   └── README.md        ← 共用底層樣式／腳本的現況與後續規劃（見第 4 節）
│   └── video/                  ← 影片資源庫（五科共用同一頁，見第 5 節）
│       ├── video-library.html  ← 唯一一份影片資源庫頁面，目前收錄四科（不含 APCS）的內容
│       ├── video-access.html   ← 密鑰關卡頁（五科首頁的「🔒 教師專區」都連到這）
│       ├── access-mechanism.html ← 給學生的「前端密碼」教學彩蛋頁
│       ├── (一個小型 .js 檔案) ← 共用教師密鑰設定，檔名故意不寫在文件裡（見 access-mechanism.html）
│       ├── video-library.css／video-library.js ← 影片資源庫的版型與篩選引擎
│       ├── gate.css            ← 密鑰關卡頁／彩蛋頁的樣式
│       └── README.md           ← 影片資源庫的資料結構與分類規則
├── it-tech/                 ← 高一資訊科技（原「資訊科技_課程網站」）
│   ├── index.html, unit01~unit14.html
│   ├── assets/ (style.css, script.js, progress.js), images/, build/
│   └── README.txt
├── algo/                    ← 高二演算法（原「algo-site-full」）
│   ├── index.html, unit01~unit18.html, unit01b.html, unit02b.html, unit06b.html（補充單元）
│   ├── assets/ (style.css, script.js, progress.js ← 本次新增)
│   └── （沒有 build/，是手刻的靜態 HTML，不是 Python 生成）
├── infosec/                 ← 高三資訊安全導論
│   ├── index.html, unit01~unit20.html
│   ├── assets/, build/
│   └── README.txt
├── advprog/                 ← 高三進階程式設計
│   ├── index.html, unit01~unit10.html
│   ├── assets/, build/
│   └── README.txt
├── apcs/                    ← APCS 先修班（第五科，高一多元選修，每週三下午 2 節）
│   ├── index.html, judge.html, mock.html, functions.html
│   ├── unit01~unit09.html ＋ unit01b／unit02b／unit04b／unit06b／unit07b 五個補充單元
│   │   （上課順序：01→01b→02→02b→03→04→04b→05→06→07→07b→06b→08→09；
│   │   鎖定序號：01b 跟 01、02b 跟 02、04b 跟 04、06b 跟 06、07b 跟 07、09 跟 08
│   │   一起開放，共用總表的 "apcs" 最大值仍是 8）
│   ├── assets/ (style.css, script.js, progress.js, tabs.css, plan.css, judge.css,
│   │   reading-viewer.js, loop-trace.css/js), assets/reading/, assets/handouts/, images/
│   └── README.txt
└── apcs-ee/                 ← 資電 APCS 週六培訓班（⚠️ 不是正式五科之一，見下方第 1.1 節）
    ├── index.html, schedule.html, mock.html, functions.html
    ├── unit01~unit09.html ＋ unit01b／unit02b／unit04b／unit06b／unit07b 五個補充單元
    │   （跟 apcs/ 同一套順序與鎖定序號，但 assets/progress.js 已寫死 unlockedUpTo:99，
    │   跟共用總表脫鉤——教材預設全部開放）
    ├── assets/ (style.css, script.js, progress.js, tabs.css, plan.css,
    │   reading-viewer.js, loop-trace.css/js, mock.css/js, mock-data.js),
    │   assets/reading/, assets/handouts/, images/
    ├── _gen/                 ← 產生 unit02b／06b／07b／09、課程規劃頁、回家作業 PDF 的
    │   Python 程式（開發工具，不是網站的一部分，教學使用不需理會）
    └── README.txt
```

### 1.1　⚠️ `apcs/` 跟 `apcs-ee/`：兩個完全獨立的課程，名字很像，千萬不要混用

這是目前整個網站裡**唯一一組命名容易混淆**的資料夾，之後不管是回到原本的對話改，
還是開新對話處理，都先看這一段：

- **`apcs/`** = 高一多元選修「APCS 先修班」，每週三下午 2 節，是正式的**第五科**，
  進度跟著 `shared/core/progress.js` 共用總表的 `"apcs"` 一起走。
- **`apcs-ee/`** = 另外獨立的「資電 APCS 週六培訓班」，專為資電群二年級開設、
  分兩梯次的週六密集課程，**不算在五科之內**，進度已經跟共用總表脫鉤
  （`assets/progress.js` 的 `unlockedUpTo` 寫死為 `99`，全部開放）。
- 兩個資料夾內部結構幾乎一樣（都有 `unit01.html`～`unit09.html`、`unit01b.html` 等
  補充單元、`functions.html`、`mock.html`，連 `assets/` 底下的檔名都大多相同），
  這是因為 `apcs/` 是從 `apcs-ee` 的內容調整長度與用詞後產生的，**但兩者之間完全
  沒有互相連結**，所有連結都是資料夾內的相對路徑，不會互相牽動。
- 混用的典型事故：把 `apcs-ee/` 的某個檔案複製貼到 `apcs/` 底下（或反過來），
  或是在編輯器裡開錯資料夾改到另一邊的檔案而不自知。改之前務必看清楚網址列／
  檔案路徑最前面是 `apcs/` 還是 `apcs-ee/`。
- 兩科的 `teacherKey`（單元鎖定）都是 `ji32k7au4a83`，跟其他科一致；影片資源庫
  的密鑰是另一把，兩個資料夾共用同一個入口 `shared/video/video-access.html`，
  細節見第 5 節。

五科（加上 `apcs-ee/` 共六個資料夾）各自是完全獨立的資料夾，內部連結全部是相對路徑
（`unit01.html`、`assets/style.css` 這種寫法），所以放在同一個 repo 底下的子資料夾，
彼此互相不會衝突、也不會互相覆蓋。**這回答了你原本擔心的「單元一二三重複命名會不會
造成 GitHub 瀏覽 bug」：不會**，因為瀏覽器是照「資料夾/檔名」找頁面，`it-tech/unit01.html`
跟 `algo/unit01.html` 是兩個完全不同的網址，不會互相干擾；`apcs/unit01.html` 跟
`apcs-ee/unit01.html` 同理也是兩個完全不同的網址。真正該注意的是上面第 1.1 節、
下面第 2、3 節這種「同名但邏輯不同」的地方。

`apcs/` 的 `assets/style.css`、`assets/script.js` 是直接從 `it-tech/` 複製後只調整
品牌色（改成玫瑰紅＋琥珀金，跟其他四科都不撞色）跟頁首註解，沿用同一套元件（`.code-card`、
`.callout`、`.exercise`／`.reveal`、`.timeline`、`.varstep` 互動追蹤等）。內容延續
`it-tech/` 的 Python 教材（變數、輸出入、運算子、條件、迴圈），但加深加廣到 APCS
中級範圍（陣列／串列、字元／字串），並新增上機評測、二維串列、遞迴追蹤、識讀總整理
等補充單元（`02b／04b／06b／07b`）。`apcs-ee/` 是同一套內容的資電群週六密集班版本
（技高角度、梯次制，詳見 `apcs-ee/README.txt` 的版本調整紀錄），額外多了 `schedule.html`
（課程規劃）、`_gen/`（產生補充單元與 PDF 講義的 Python 程式，不是網站本身的一部分）。

## 2. 單元命名規則（統整後）

五科現在統一用 `unit01.html`、`unit02.html`…… 的格式：

- **it-tech**：`unit01.html` ~ `unit14.html`（原本就是這個格式，沒有動）。
  ⚠️ **已知小地雷，這次先不動**：`unit08.html` 之後的檔名跟畫面上顯示的「單元幾」
  對不太上（例如 `unit13.html` 顯示的是「單元 9」）。這是舊版排序調整留下的痕跡，
  不影響功能，但之後如果要規則化重新命名，記得這個檔案本身也要跟著調整，
  且要連動修改 `build/content.py` 這個生成來源，不能只改輸出的 html。
- **algo**：原本是 `01-overview.html`、`02b-function.html` 這種描述性命名，**這次已經
  重新命名成 `unit01.html` ~ `unit18.html`**，另外三個「附」補充單元命名為
  `unit01b.html`（IDLE 操作入門）、`unit02b.html`（函式補充）、`unit06b.html`
  （堆疊 vs 佇列比較）——這三個補充單元分別跟著單元 01／02／06 一起鎖／解鎖
  （早期版本曾讓 unit02b／unit06b 不計入鎖定序號、永遠開放，後來已修正為跟主線
  單元同步）。所有內部連結（首頁卡片、上一/下一單元、總複習頁）都已經同步改好。
- **infosec**：`unit01.html` ~ `unit20.html`（原本就是這個格式，沒有動）。
- **advprog**：`unit01.html` ~ `unit10.html`（原本就是這個格式，沒有動）。
- **apcs**：`unit01.html` ~ `unit09.html`，另外五個補充單元 `unit01b`／`unit02b`／
  `unit04b`／`unit06b`／`unit07b` 分別跟著單元 01／02／04／06／07 一起鎖／解鎖
  （`unit09` 則跟著單元 08 一起鎖／解鎖，所以共用總表 `"apcs"` 的最大值仍是 8）。
  另外新增 `judge.html`（Judge／識讀練習總表）、`mock.html`（線上識讀模擬考）、
  `functions.html`（函式與語法統整表）三個沒有 `data-unit`、不會被鎖定的工具頁。
- **apcs-ee**（不算五科之一，見第 1.1 節）：跟 `apcs` 完全相同的單元命名與鎖定序號
  （`unit01.html` ~ `unit09.html` ＋ 五個 `b` 補充單元），但多了 `schedule.html`
  （課程規劃，沒有 `data-unit`），且 `assets/progress.js` 已把 `unlockedUpTo`
  寫死為 `99`，不受共用總表影響，所以共用總表裡**不需要**也**沒有** `"apcs-ee"`
  這個鍵。

## 3. 共用的單元鎖定機制 —— 進度總表已經合併成一份

五科都用同一套機制（`shared/core/progress.js` + 各科 `assets/progress.js` +
`assets/script.js` 裡的鎖定邏輯）。**`apcs-ee/` 不在這套共用總表裡**——它的
`assets/progress.js` 已經把 `unlockedUpTo` 寫死為 `99`（教材全部開放，配合
短期培訓班的性質），跟下面這份總表完全脫鉤，改總表裡的數字不會影響它：

- **★ 老師平常只需要改一個檔案：`shared/core/progress.js`。** 裡面是一個物件，
  五科各一行：
  ```js
  window.ALL_COURSE_PROGRESS = {
    "it-tech": 2,
    "algo": 2,
    "infosec": 2,
    "advprog": 2,
    "apcs": 2,
    teacherKey: "ji32k7au4a83"
  };
  ```
  每上完一科的一個單元，把那一科後面的數字 +1，存檔、push 上 GitHub 就生效，
  不用再一科一科找 `assets/progress.js` 改。
- 運作原理：每個頁面的 `<script>` 現在是**先**載入
  `<script src="../shared/core/progress.js">`（設定上面那個共用總表），
  **再**載入 `<script src="assets/progress.js">`（該科自己的檔案，讀
  `ALL_COURSE_PROGRESS["科目名"]` 組成 `window.COURSE_PROGRESS`），最後才是
  `assets/script.js`（實際做鎖定判斷）。三個 `<script>` 標籤的順序不能打亂。
  這個設計在 `file://`（老師雙擊 `index.html` 開啟）情境下也實測正常，因為
  用的是 `<script src>` 標籤而不是 `fetch()`——後者在本機檔案模式下會被瀏覽器
  的 CORS 規則擋掉，前者不會。
- 如果某一科想要「脫鉤」、不想再跟著總表一起變動（例如想手動保留某科的進度、
  不受集體調整影響），把該科 `assets/progress.js` 裡 `unlockedUpTo` 那一行
  改成寫死的數字即可，檔案裡也寫了這段說明；改完之後那一科就不會再讀
  `shared/core/progress.js` 的值。
- `teacherKey`：解鎖單元用的老師密鑰，**五科統一為 `ji32k7au4a83`**，設定
  在 `shared/core/progress.js` 裡；影片資源庫另外用一把獨立的密鑰，放在
  `shared/video/` 資料夾裡（實際檔名跟數值都故意不寫在這份文件裡，避免
  公開 repo 被直接搜尋到就找到答案——理由跟找法見
  `shared/video/access-mechanism.html`）
  ——**這兩把密鑰現在刻意設成不同的值、互不相通**，要換密鑰只要改對應
  那一個檔案就好，不用保持一致。在任何頁面網址後面加 `?key=ji32k7au4a83`
  就能解鎖預覽全部單元，五科通用同一把。
- 頁面要吃到這套鎖定，需要兩個標記：
  - 首頁的單元卡片：`<a class="ucard" data-unit="3" href="unit03.html">`
  - 該單元內頁的 `<main>`：`<main class="wrap" data-unit="3">`
  - 沒有 `data-unit` 的頁面永遠不會被鎖——早期版本 algo 科的 unit02b／unit06b
    就是因為漏了這個屬性才變成「永遠開放」，後來已經補上 `data-unit`
    （分別對應單元 02、06）修正。新增頁面時要記得補上這個屬性，才會跟著
    進度一起鎖／解鎖。

## 4. 共用樣式／腳本（`shared/core/`）—— 目前還沒合併，原因見 `shared/core/README.md`

比對過 it-tech／advprog／infosec 三科的 `assets/style.css`、`assets/script.js`，
八成以上是逐字重複（顏色變數不同、少數 class 命名有drift，例如 it-tech 還在用
`.compiler-cta.cta-fixed`，advprog／infosec 已經簡化成 `.compiler-cta`；it-tech
還有 `.bootflow`、`.dual-term` 這兩個 advprog／infosec 已經拿掉的元件）。這代表
「可以合併」，但不是無腦合併就安全——貿然抽成同一份共用檔案，可能讓 it-tech
既有頁面的樣式跑掉。這次先不動，把發現的細節記在 `shared/core/README.md`，
列成下一階段的任務，等你要動的時候我們再仔細對過一輪、逐頁檢查再合併。

## 5. 共用影片瀏覽區（`shared/video/`）—— 六個課程資料夾現在共用同一頁

原本影片資源庫只有 it-tech 有、放在 it-tech 資料夾裡。**統整後改成共用同一份**：
整個影片資源庫（頁面、密鑰關卡、彩蛋說明頁）都搬到 `shared/video/`，不再屬於任何
單一科目。五科＋`apcs-ee` 課程首頁右下角的「🔒 教師專區」按鈕都連到同一個網址
`shared/video/video-access.html`，輸入密鑰後一起進到同一份 `video-library.html`
——**這是目前唯一一個 `apcs-ee` 也掛進來的共用機制**，其他共用機制（進度總表）
`apcs-ee` 都沒有參與，見上面第 1.1、3 節。

- 影片資料以「哪一科最適合」分成四大類（頁面上的分類篩選鈕）：**演算法**、
  **進階程式設計**、**資安**、**高一資訊科技**（這一類再依原本的單元／補充主題
  細分成好幾個小節，如「單元1｜課程介紹」「補充｜AI 通識與社會議題」等）。
  ⚠️ **apcs 跟 apcs-ee 都還沒有專屬分類**——兩者都共用同一把教師密鑰、同一個
  「🔒 教師專區」入口，但 `video-library.html` 裡還沒有幫它們新增分類與影片。
  之後如果要補 APCS 相關的影片，可以在這份檔案裡新增一個 `data-b="APCS"` 的
  section，規則跟其他四類一樣，詳見下面的 `shared/video/README.md`（如果
  apcs 跟 apcs-ee 的影片需要分開列，記得另外取不同的 `data-b` 代號，例如
  `APCS` 跟 `APCSEE`，避免兩邊影片混在一起篩選不出來）。
- 分類的判斷原則：內容跟哪一科的課程性質最接近就歸哪一類（例如原本歸在「資安」
  補充的影片，現在直接是資安這個大類；跟 AI 工具/Agent 操作有關的影片歸進階程式
  設計；跟遞迴、複雜度、排序搜尋等演算法概念有關的歸演算法）；其餘偏電腦硬體、
  AI 通識、社會經濟、創客這類原本就是高一資訊科技單元／補充主題的，留在高一資訊
  科技這一類底下依單元呈現。
- 密鑰關卡（`video-access.html`）跟教學彩蛋頁（`access-mechanism.html`）也搬到
  `shared/video/`，密鑰讀的是同資料夾裡另一個小檔案（不再是某一科的
  `assets/progress.js`，實際檔名故意不寫在這份文件裡），彩蛋頁裡的說明文字
  跟藏起來的提示都已同步更新成新路徑。
- 分類與影片資料現在都直接寫在 `shared/video/video-library.html` 這一份檔案裡
  （四大類混在同一個檔案的不同 section 裡，不是分成四個檔案），要新增或調整某科的
  影片，就是編輯這一個檔案裡對應那個分類的區塊。詳細的資料格式規則看
  `shared/video/README.md`。
- **你提到「這個頁面之後要在這裡再跟你調整」——這份共用頁面已經做好、可以直接用，
  之後要新增影片、調整分類，都可以直接在這個對話繼續處理。**

## 6. 「丟回原本對話去改」的建議做法

每個資料夾裡的 `README.txt` 都已經加上一段「本資料夾是『資訊科技教學網』的一部分」
的說明（六個資料夾都有）。丟回原本那個對話時，建議這樣做：

1. 只丟該資料夾（例如整個 `it-tech/`），不用整個 repo。
2. 附上一句話提醒：「這個資料夾現在是明道資訊科技教學網的一部分，解鎖單元用的
   `teacherKey` 統一是 `ji32k7au4a83`（跟影片資源庫的密鑰是兩把不同的，互不
   相通），影片資源庫的版型已經搬到 `shared/video/`，請看資料夾裡的
   README.txt。」
3. 如果那次要改的東西完全在單元內容本身（像文字、例題、圖片），不涉及檔名或共用機制，
   基本上不太會出事；如果會動到檔名、鎖定機制、或影片資源庫，記得回來這邊或跟我確認
   一下會不會影響其他科。
4. **`apcs/` 跟 `apcs-ee/` 特別要多附一句**：「這是 `apcs/`／`apcs-ee/`（兩者擇一
   講清楚），跟另一個資料夾是完全獨立的課程，請不要互相參照或複製檔案」——這兩個
   資料夾結構太像，光講「APCS 那個資料夾」很容易讓對話誤會成另一邊，務必把資料夾
   名稱打清楚（見第 1.1 節）。

## 7. GitHub 部署備忘

- 建議整個 `/` 資料夾就是一個 repo 的根目錄，GitHub Pages 設定成從根目錄（`/`）發布，
  `index.html`（總首頁）就會是 `https://你的帳號.github.io/repo名稱/` 的首頁。
- 所有連結都是相對路徑，本地端直接雙擊 `index.html` 或整個資料夾丟上 GitHub Pages
  都可以直接動，不需要額外設定。
- 之後如果哪一科的內容變大想拆成獨立 repo，記得那樣做之後總首頁的卡片連結要從
  `it-tech/index.html` 這種相對路徑，改成完整網址（例如
  `https://你的帳號.github.io/it-tech-repo/`）。
