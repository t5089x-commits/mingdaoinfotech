---
name: shared/video
---

# 共用影片資源庫（五科共用同一頁）

這裡放的是整個「影片資源庫」——五科課程共用**同一份** `video-library.html`，
不是每一科各自一份。頁面、密鑰關卡、彩蛋說明頁、樣式跟篩選引擎全部都在
`shared/video/` 這個資料夾裡，不屬於任何單一科目。

⚠️ **APCS（`apcs/`）目前只共用「密鑰＋教師專區入口」這套機制，`video-library.html`
裡還沒有幫它新增專屬的影片分類**——下面第「分類規則」一節列的四大類是目前實際
收錄的內容，之後要幫 APCS 補影片，照同樣的格式新增一個分類即可（見下面的資料格式）。

## 資料夾內容

- `video-library.html` —— 唯一一份影片資源庫頁面，目前收錄的四科影片資料都在
  這一份檔案裡，用四個 `<section class="sec" data-b="...">` 區分。
- `video-access.html` —— 密鑰關卡頁。五科課程首頁右下角的「🔒 教師專區」
  按鈕都連到這一頁。
- `access-mechanism.html` —— 給學生的「前端密碼」教學彩蛋頁（藏在
  `video-access.html` 角落的 `· ? ·` 連結點進去可以找到）。
- `teacher-key.js` —— 共用教師密鑰設定，`video-access.html` 讀的是這裡，
  不是任何一科自己的 `assets/progress.js`。
- `video-library.css` / `video-library.js` —— 影片資源庫的版型（外觀）與
  篩選／搜尋引擎，不含任何影片內容，五科通用。
- `gate.css` —— `video-access.html`、`access-mechanism.html` 這兩頁自己的
  樣式，跟任何一科的 `assets/style.css` 無關（避免共用頁面被某一科的樣式
  改動牽連）。

## 分類規則：四大類（尚不含 APCS）

`video-library.html` 裡的影片用「哪一科最適合」分成四大類，對應頁面上的
分類篩選鈕（`data-f`）跟每個影片列的 class（`data-b` 所在的 `<section>`）：

| 分類代號 | 對應科目 | 說明 |
|---|---|---|
| `ALGO` | 高二演算法 | 遞迴、複雜度、排序搜尋等演算法核心概念 |
| `ADVPROG` | 高三進階程式設計 | Python、pandas／Matplotlib、AI 工具與 Agent 操作 |
| `INFOSEC` | 高三資訊安全導論 | 密碼學、區塊鏈、資安攻防、數位信任相關 |
| `ITTECH` | 高一資訊科技 | 電腦硬體、AI 通識、社會經濟、創客等，依原本的單元／
  補充主題再用 `<h3 class="subhead">` 細分小節（例如「單元1｜課程介紹」
  「補充｜AI 通識與社會議題」） |

判斷原則：內容跟哪一科的課程性質最接近就歸哪一類；找不到明顯對應、
原本就屬於高一資訊科技單元／補充主題的內容，留在 `ITTECH` 底下依單元呈現。

## 資料格式（新增／調整影片時要照這個結構）

- 篩選按鈕：`<button class="chip" data-f="ALGO" onclick="flt(this)">演算法 <span class="c">6</span></button>`
- 每個分類一個區塊：`<section class="sec" data-b="ALGO">...</section>`，
  區塊內第一個是 `<h2>` 標題，`ITTECH`／`ADVPROG` 這種還有子分類的，
  用 `<h3 class="subhead">小節名稱 <span class="subn">N 部</span></h3>`
  把同一大類底下的影片再分組。
- 影片資料放在 `<table><tbody>` 裡，每部影片一列：
  `<tr class="row ALGO">`（class 要跟所在 `<section>` 的 `data-b` 一致），
  五個欄位固定是 `<td class="ttl">`（影片標題＋連結）、`<td class="ch">`
  （頻道）、`<td class="dur">`（長度）、`<td class="pub">`（發布日期）、
  `<td class="use">`（建議課堂用途）。
- 需要提醒「內容需斟酌」的影片，`<tr>` 的 class 多加一個 `hasWarn`
  （例如 `class="row ITTECH hasWarn"`），並在 `.use` 欄位開頭加上警示文字。
- `data-f`（篩選鈕）／`data-b`（區塊）／`row` 後面的代號三者要對得起來
  （都用同一個大寫代號，例如 `ALGO`），篩選引擎（`video-library.js`）是用
  字串完全相等比對，打錯字或大小寫不一致會篩不出來。

## 密鑰與存取流程

密鑰只有一把、五科通用，目前是 `t5089x`（跟每一科單元鎖定用的
`teacherKey` 現在是兩把互相獨立的密鑰，故意設成不同值、互不相通，各自
要換密鑰都可以）：課程首頁的「🔒 教師專區」→ `video-access.html` 輸入
密鑰 → 正確就跳轉到同資料夾的 `video-library.html`。網址帶
`?key=t5089x` 也能直接跳過輸入直接放行。這一把密鑰刻意用「前端明碼比對」
這種不安全的做法（`access-mechanism.html` 裡有完整教學說明），是特意設計
的資安教材，不是漏洞。要換這把密鑰，只要改 `teacher-key.js` 這一個檔案
就好，不會影響單元鎖定用的那一把。

## 現況

Phase 2（單一共用頁）已完成：150 部影片（原本 130 部＋新整理進來的 20 部）
都已分類收錄。之後要新增或調整影片、微調分類，都直接編輯這一份
`video-library.html`，不用再去改任何一科自己的資料夾。
