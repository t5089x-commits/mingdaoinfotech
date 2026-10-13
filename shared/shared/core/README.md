---
name: shared/core
---

# 共用底層樣式／腳本 — 現況：style.css／script.js 尚未合併，progress.js 已經共用

## `progress.js`：五科進度總表，已經合併成一份

`shared/core/progress.js` 是五科共用的「單元進度總表」，老師只要打開**這一個檔案**，
就能一次調整五科各自開放到第幾單元，不用再分別打開五個 `assets/progress.js`。運作方式：

- 每個單元頁面的 `<script>` 都改成先載入 `../shared/core/progress.js`（設定
  `window.ALL_COURSE_PROGRESS = {"it-tech": 2, "algo": 2, ...}`），再載入該科自己
  的 `assets/progress.js`（讀 `ALL_COURSE_PROGRESS["科目名"]`，組成
  `window.COURSE_PROGRESS` 給 `script.js` 的鎖定邏輯用）。
- 老師平常只需要改 `shared/core/progress.js` 裡對應科目後面的數字即可。
- 如果某一科想要「脫鉤」、不想再跟著總表變動，直接把該科 `assets/progress.js`
  裡 `unlockedUpTo` 那一行改成寫死的數字就行，該檔案裡也有寫這段說明。
- 這個檔案已經用 Playwright 在 `file://` 通訊協定下實測過（老師平常用滑鼠雙擊
  `index.html` 開啟的情境），改總表一個數字，對應科目會立刻反映、其他科目不受影響；
  單元鎖定畫面與 `?key=ji32k7au4a83` 預覽模式也都正常運作（這把解鎖單元用的
  密鑰，跟影片資源庫另外用的那把密鑰現在是兩把互相獨立的，故意設成不同值；
  影片資源庫那把密鑰放在哪個檔案，故意不寫在這份文件裡，詳見
  `shared/video/access-mechanism.html`）。

`style.css`、`script.js` 目前**還沒有**做這件事，原因見下面。

## style.css／script.js：尚未合併（Phase 2 待辦）

比對 it-tech／advprog／infosec 三科目前各自的 `assets/style.css`（約 1200 行）、
`assets/script.js`，發現：

- **顏色變數（CSS custom properties）幾乎是唯一有意義的差異**：`--brand`、
  `--accent`、`--hero-bg` 這些每科配色不同，其餘排版規則逐字重複。
- **但不是 100% 只有配色差異**，還有結構性 drift：
  - it-tech 的 `.compiler-cta` 需要搭配 `.cta-fixed` 修飾 class 才會固定在畫面角落；
    advprog／infosec 已經把這個行為簡化成 `.compiler-cta` 自己就好，等於同一個元件、
    兩種不相容的 class 命名慣例。
  - it-tech 還有 `.bootflow`（開機資料流動示意圖，unit06 有用到）、`.dual-term`
    （兩岸用語對照表，unit06 有用到）這兩個 advprog／infosec 已經拿掉的元件。
  - `common.py`（Python 生成器）三科也各自有一份，差異沒有全部比對過。

## 為什麼這次沒有直接合併

貿然把某一科的版本當作「共用基準」，會讓另外幾科用到的元件（`.bootflow` 等）消失，
或讓 it-tech 的按鈕失去固定定位效果。要安全合併，需要：

1. 把三份 `style.css` 逐段對過，抓出「所有科目都有用到」的部分當共用底，
   「只有某科用到」的部分留在該科自己的 `assets/style.css`（或做成可選的擴充區塊）。
2. 顏色相關的變數（`:root` 裡那一段）抽成各科自己的 `theme.css`，共用底不含顏色。
3. 合併後要逐頁檢查（尤其 it-tech 有用到 `.bootflow` / `.dual-term` / `.compiler-cta.cta-fixed`
   的那幾頁：unit06、unit08~unit14）畫面有沒有跑掉。

## 建議

這件事適合另外找一次時間，一頁一頁對，而不是現在混在架構調整裡一起做。
目前五科的 `assets/style.css`、`assets/script.js` 都還是各自獨立的檔案
（apcs 是直接從 it-tech 複製後改品牌色，血緣上跟 it-tech 那份最接近），
功能上完全沒問題，只是還沒「共用」。準備好要做這件事時再回來這裡繼續。
