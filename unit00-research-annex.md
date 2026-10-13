# Unit 00 教學設計｜利潤與財務數據查證附錄

> **給老師的說明（先讀這段）**
>
> 你的訊息裡「【Unit 00 教學單元設計需求】」這一段，開頭明確寫著「要交給另一個 AI 處理，先不用動網站」，所以我沒有去產出你列的那 12 項完整教學設計（教學大綱、活動設計、盧德運動教案、Google 表單反思題等等）——那些我理解成你會另外交給別的 AI 工具去做。
>
> 但你在最上面給的這句話，是直接對我下的指令：「以下如果有提到利潤的，請務必上網找公開資料佐證(要附上連結)」。所以我實際做的事情是：針對你教案裡會用到的「iPhone 100 元供應鏈分配」這個活動，**上網查證 Apple、台積電、鴻海（組裝廠）、以及主要零件供應商（Sony、SK Hynix）的公開財報數據**，整理成這份「數據查證附錄」，你可以連同你原本那份教案需求，一起丟給你要用的另一個 AI，讓它在設計活動時直接引用這些有來源、有連結的真實數字，不用自己再去查或（更糟）憑印象亂編數字。
>
> 如果你原本是希望我直接做完整的教學設計，請跟我說一聲，我可以接著做。
>
> 另外提醒：网站結構的兩項異動（「虛擬貨幣交易所」卡片、Unit 00 骨架頁面）已經照你的要求做完了，Unit01／02 完全沒有被動到。

---

## 0. 名詞先講清楚（你特別交代不要混為一談）

這份文件會反覆出現四個容易搞混的詞，先定義一次：

| 名詞 | 意思 | 舉例 |
|---|---|---|
| **BOM 成本**（Bill of Materials） | 只算「零件本身」的成本，不含研發、組裝、行銷、物流、通路等費用 | iPhone 的螢幕、晶片、電池等零件加起來的成本 |
| **營收**（Revenue） | 賣出商品／服務收到的總金額，還沒扣任何成本 | Apple 一整季賣 iPhone 收到的錢 |
| **毛利／毛利率**（Gross Profit / Gross Margin） | 營收 − 銷貨成本（COGS，含零件+組裝等直接生產成本），再除以營收 | Apple 財報揭露的 Products 毛利率 36.2% |
| **淨利／淨利率**（Net Profit / Net Margin） | 毛利再扣掉研發、行銷、管理費用、利息、稅之後剩下的錢，再除以營收 | 鴻海財報揭露的稅後淨利率 2.34% |

**BOM 成本不能直接拿去換算毛利率或淨利率**——BOM 只是「材料錢」，跟「這家公司到底賺不賺錢」是兩件事。這份文件裡，凡是零件成本一律標「BOM」，凡是公司財報數字一律清楚標明是「毛利率」還是「淨利率」還是「營業利益率」。

另外，凡是不是公司自己財報揭露、而是研調機構（TechInsights、Counterpoint Research、IHS Markit 等）用拆解手機的方式估出來的數字，一律標註「⚠ 研究機構估算」，跟公司官方揭露的精確數字分開處理，不假裝兩者一樣精確。

---

## 1. Apple：品牌／設計端拿走多少？

**官方揭露數字**（來源：Apple 2025 年 Q4 財報電話會議逐字稿）：

- Products（iPhone＋iPad＋Mac＋穿戴裝置合併）毛利率：**36.2%**（較上季+170個基點）
- Services（App Store、雲端服務等）毛利率：**75.3%**（較上季−30個基點）
- 公司整體毛利率：**47.2%**
- 當季總營收：$102.5B（年增8%）；iPhone 營收：$49B（年增6%）
- 當季稅後淨利：$27.5B
- 當季約有 $11億 美元的關稅相關成本影響

⚠ **重要限制**：Apple **從未單獨揭露「iPhone 專屬毛利率」**，官方只公布「Products」這個大類別（iPhone+iPad+Mac+手錶耳機全部混在一起）。所以上面 36.2% 只是「最接近 iPhone 毛利率」的官方代理數字，不是 iPhone 本身的精確毛利率。教學上可以誠實跟學生講這個限制——這本身也是很好的資訊揭露/公司治理討論點。

補充歷史趨勢（來源：Macrotrends）：Apple 整體毛利率 2023 財年 45.03% → 2024 財年 46.52% → 2025 財年（至3月）46.63%，呈逐年上升趨勢。

**Sources:**
- [Apple Q4 2025 Earnings Call Transcript – Investing.com](https://www.investing.com/news/transcripts/earnings-call-transcript-apple-beats-q4-2025-forecasts-stock-rises-93CH-4322156)
- [Apple Gross Margin 2010-2025 – Macrotrends](https://www.macrotrends.net/stocks/charts/AAPL/apple/gross-margin)

---

## 2. 台積電（TSMC）：晶片製造端拿走多少？

**官方揭露數字**（來源：台積電官方新聞稿，2025 Q4）：

- 毛利率：**62.3%**，財務長黃仁昭表示由先進製程需求帶動
- 當季晶圓營收結構：3nm 佔 28%、5nm 佔 35%、7nm 以上先進製程合計佔 77%

台積電是 Apple 晶片（A系列、M系列）的獨家代工廠，62.3% 的毛利率遠高於組裝廠（見下方鴻海數據），也高於 Apple 自己揭露的 Products 毛利率——這是一個很好的課堂對比點：「做晶片的」比「賣手機品牌的」毛利率還高，打破「品牌商一定拿最多」的直覺。

**Sources:**
- [TSMC 2025 Q4 Results Press Release](https://pr.tsmc.com/english/news/3281)

---

## 3. 鴻海（Foxconn／Hon Hai）：組裝端拿走多少？

**官方揭露數字**（來源：鴻海官方法說會資料，2025 全年及 Q4）：

| 期間 | 營收 | 營業利益 | 稅後淨利 | 營業利益率 | 淨利率 |
|---|---|---|---|---|---|
| 2025 全年 | 新台幣 8.1 兆 | 2,592 億 | 1,894 億 | **3.20%** | **2.34%** |
| 2025 Q4 | 新台幣 2.61 兆 | 856 億 | 452 億 | **3.28%** | **1.73%** |

這組數字是整份文件裡最關鍵的教學對比：**組裝廠（鴻海）淨利率只有 2%多，Apple 整體毛利率卻有 47%，台積電毛利率 62%**——同樣是「做出一支 iPhone」，組裝環節賺的錢跟設計/晶片環節完全不成比例，這正好呼應教案裡要學生思考「利潤怎麼分配」的核心提問。

⚠ 補充限制：鴻海財報公司自己說「儘管 AI 伺服器等高單價產品稀釋了毛利率，營業利益率仍成長」——代表鴻海近年營收與獲利已經有很大一部分來自 AI 伺服器代工，不是純粹只做 iPhone 組裝，數字會被這部分業務影響，不是 100% 反映「組裝一支 iPhone」的獲利狀況。

**Sources:**
- [Hon Hai FY2025 & 4Q25 Results](https://www.honhai.com/en-us/press-center/press-releases/latest-news/1978)

---

## 4. 主要零件供應商：晶片、記憶體、感光元件端拿走多少？

### 4.1 SK Hynix（記憶體，非 iPhone 特定，但可作為「零件供應商很賺錢」的例證）

**官方揭露數字**（來源：SK Hynix 官方法說會新聞稿，2025）：

| 期間 | 營收 | 營業利益 | 營業利益率 |
|---|---|---|---|
| 2025 全年 | 97.15 兆韓元 | 47.21 兆韓元 | **49%** |
| 2025 Q4 | 32.83 兆韓元 | 19.17 兆韓元 | **58%** |

SK Hynix 官方公告指出「HBM（高頻寬記憶體，AI 用）營收年增超過一倍，是這次創紀錄表現的主要貢獻來源」，並提到伺服器用傳統記憶體需求也大幅成長。

⚠ 這組驚人的高營業利益率（Q4 高達 58%）主要是被 **AI 伺服器用的 HBM 記憶體**這波需求帶動，不是特別針對「iPhone 用的記憶體」——教學上要跟學生說清楚：這不是「iPhone 讓記憶體廠商賺很多」，而是「AI 熱潮讓記憶體廠商賺很多」，剛好可以呼應教案第4段「2050 AI 情境」的鋪陳。

**Sources:**
- [SK hynix Announces FY25 Financial Results – PR Newswire](https://www.prnewswire.com/news-releases/sk-hynix-announces-fy25-financial-results-posts-record-high-results-and-delivers-highest-shareholder-returns-302672384.html)
- [SK hynix Posts Record Annual Financial Results in 2025 – SK hynix Newsroom](https://news.skhynix.com/en/sk-hynix-announces-fy25-financial-results/)

### 4.2 Sony（影像感測元件／iPhone 鏡頭感光元件的主要供應商之一）

**官方揭露數字**（來源：Sony 2025 財年法說會資料）：

- 影像與感測解決方案（I&SS）事業部營收：約 2,151.5 億日圓（約 138 億美元）
- 該事業部營業利益：約 357.3 億日圓（約 23 億美元）
- 營業利益率：約 **16.6%**
- 該事業部營業利益較上一財年**成長 37%**，主因是產品組合改善與手機鏡頭感光元件需求強勁

Sony 是 iPhone 鏡頭感光元件（CMOS image sensor）的主要供應商之一。16.6% 的營業利益率遠低於台積電（62.3%）與 SK Hynix（49%），顯示不同零件供應商之間的獲利能力也差異很大，不是「所有零件供應商都跟台積電一樣賺」。

**Sources:**
- [Sony's image sensors drive record profits – Digital Camera World](https://www.digitalcameraworld.com/cameras/sonys-image-sensors-drive-record-us-usd9-6-billion-profits-as-electronics-division-slumps)

---

## 5. iPhone BOM（零件成本）歷代估算 —— 全部為研究機構估算，非 Apple 官方數字

⚠ **這整節都是第三方研究機構用拆解手機的方式估算出來的數字，Apple 從未官方公布任何一支 iPhone 的零件成本或組裝成本。** 教學上務必跟學生強調這個差異：這是「研究機構的合理估算」，不是「精確的官方數字」。

| 機型 | BOM 估算 | 建議售價 | BOM／售價比 | 資料來源 |
|---|---|---|---|---|
| iPhone X | 約 $370.25 | $999 | 37.06% | TechInsights／IHS Markit（BankMyCell 彙整） |
| iPhone XS Max | 約 $390 | $1,099 | 35.49% | 同上 |
| iPhone 11 Pro Max | 約 $450.50 | $1,099 | 44.63%（該資料集中最高） | TechInsights／S&P Global／Statista |
| iPhone 14 Pro Max | $464（128GB 版；含毫米波版最高 $474） | $1,099 | 約42% | Counterpoint Research |
| iPhone 15 Pro Max | 較 14 Pro Max 高約 $37.7（推估約 $501.7） | $1,199 | 約42% | Counterpoint Research |
| iPhone 17 Pro Max | 約 $408.13（⚠ 未經驗證） | $1,199 | 約34% | ⚠ 來源未明確揭露拆解機構身分，僅供參考 |

**幾個值得帶進課堂的細節**（均為研究機構估算）：

- iPhone 14 Pro Max：A16 仿生晶片約佔整體 BOM 的 20%；Apple 自行設計的零組件（觸控晶片、連接性晶片、音訊、電源管理電路）約佔 BOM 的 22%。
- iPhone 15 Pro Max：A17 Pro 晶片讓成本多了約 $30；相機系統成本年增 34%；鈦金屬機身成本年增 18%；Apple 自行設計零件占比提高到 25%。
- iPhone 17 Pro Max 的估算數字（$408.13，含 A19 Pro 晶片 $90.85、5G 數據機 $90、相機模組 $80、螢幕 $80、記憶體 $21.80、儲存 $20.59、外殼 $20.79、電池 $4.10）**來源文章沒有明確說明是哪一家拆解機構做的分析，可信度低於上面幾代有明確標註 Counterpoint／TechInsights 的數字，建議在課堂上標示「未經驗證的網路估算」，不要當作精確數字使用。**
- TechInsights 官方針對 iPhone 17 的免費拆解頁面只揭露「相機系統約佔 BOM 總支出的近三分之一」這個比例，沒有公布美元金額（完整報告要付費）。

**BOM 占售價比重要提醒**：即使 BOM／售價比看起來高達 40%多，這**不代表 Apple 只賺不到 60%**——因為 BOM 不含研發、組裝、行銷、物流、通路、稅務等費用，這些都要從剩下的錢裡再扣，才會得到前面第1節看到的「毛利率」。這正是這份文件開頭要特別強調「BOM ≠ 毛利率」的原因，教案設計時務必避免讓學生把兩者混為一談。

**Sources:**
- [How Much Do iPhones Cost To Make? – BankMyCell](https://www.bankmycell.com/blog/how-much-do-iphones-cost-to-make)
- [iPhone 14 Pro Max BOM is $464 – GSMArena](https://m.gsmarena.com/cr_iphone_14_pro_max_bom_is_464_nearly_4_more_than_13_pro_max-news-57532.php)
- [iPhone 15 Pro Max BOM Analysis – Counterpoint Research](https://counterpointresearch.com/en/insights/bom-analysis-iphone-15-pro-max-costs-37-7)
- [iPhone 17 Pro Max cost breakdown (unverified) – SuperCarBlondie Tech](https://tech.supercarblondie.com/iphone-17-pro-max-apple-iphone-cost/)
- [Inside Apple iPhone 17 Teardown – TechInsights](https://www.techinsights.com/inside-apple-iphone-17-teardown)

---

## 6. 一張總表：從晶片到組裝，誰賺得比較多？

把前面官方揭露的財報數字放在同一張表比較（注意：這是不同性質的利潤率並列比較，僅供課堂直覺對照，不是同一種計算基礎的精確比較——已在指標欄位標明）：

| 環節 | 公司 | 指標 | 數字 |
|---|---|---|---|
| 晶片代工 | 台積電 | 毛利率 | 62.3% |
| AI／記憶體 | SK Hynix | 營業利益率 | 49%（全年）／58%（Q4，受 AI／HBM 帶動） |
| 品牌／設計 | Apple | 毛利率（Products，非 iPhone 專屬） | 36.2% |
| 感光元件 | Sony（I&SS） | 營業利益率 | 16.6% |
| 組裝代工 | 鴻海 | 淨利率／營業利益率 | 2.34%／3.20% |

這張表最適合直接拿給學生看：**同樣圍繞著一支 iPhone 在賺錢，賺錢能力可以從 2% 到 62%，差距超過 25 倍。** 這正是教案裡「100 元怎麼分配」活動的數據骨幹，也直接呼應後面盧德運動段落要討論的「誰真正拿走了生產力提升的果實」。

---

## 7. 盧德運動歷史查證（結論：你原本的說法完全正確，以下只是補上來源）

你在訊息裡自己整理的那段盧德運動說明，經查證**內容正確、觀點也適當**（正確地把抗爭核心定位在「資方利用機械剝削勞工」而非單純反科技），不需要修改，以下補上兩個可引用的可靠來源：

- **時間與地點**：1811–1816 年，起源於諾丁漢附近，蔓延到約克夏、蘭開夏、德比郡、萊斯特郡；主要針對紡織機械（來源：大英百科全書）。
- **Ned Ludd**：「盧德王」／Ned Ludd 很可能是虛構人物，被工人塑造成反抗資本家的精神象徵（大英百科全書）。
- **政府鎮壓的法律細節**：1812 年《毀壞織襪機法案》（Frame Breaking Act）把破壞機器列為**唯一死刑**的重罪（capital felony），比 1788 年舊法規定的 7-14 年流放刑罰更重；首相 Spencer Perceval 與內政大臣 Richard Ryder 支持此法，詩人拜倫（Lord Byron）在上議院處女演說中反對此法案；此法為暫時性法案，1814 年到期／廢止（來源：維基百科）。有個值得補充的細節：儘管鎮壓期間約有 60-70 名盧德分子被處以絞刑，但「似乎沒有任何一件死刑判決是依據這條 1812 年法案本身，法官普遍還是引用既有法律」——這個細節可以讓課堂討論更細緻，避免把「1812年法案→死刑」講得過於機械化。
- **運動衰退原因**：鎮壓 + 拿破崙戰爭結束後經濟復甦，運動在 1817 年左右式微（大英百科全書）。
- **現代延伸意涵**：「Luddite」現在廣泛用來指稱反對科技變革的人，近年隨生成式 AI 興起，衍生「新盧德主義」（Neo-Luddism）一詞，用來描述對 AI 取代創作／工程等工作的集體焦慮——與你教案第8段設計的「AI 時代會不會出現新盧德運動」討論完全吻合。

**Sources:**
- [Luddite – Britannica](https://www.britannica.com/event/Luddite)
- [Destruction of Stocking Frames, etc. Act 1812 – Wikipedia](https://en.wikipedia.org/wiki/Destruction_of_Stocking_Frames,_etc._Act_1812)

---

## 8. 給另一個 AI 的查證備忘（教案裡列的「需要查證的數據」項目，目前狀態）

| 教案要求查證的項目 | 狀態 |
|---|---|
| iPhone BOM 成本分布 | ✅ 已查（第5節），但 2024 年後機型公開細節較少，2025新機（17系列）目前只有未經驗證來源 |
| Apple 在價值鏈拿走多少營收／毛利／淨利 | ✅ 已查（第1節），但無 iPhone 專屬數字，只有 Products 大類別 |
| 組裝廠代工收入與利潤率 | ✅ 已查（第3節，鴻海） |
| 台積電在 Apple 晶片供應鏈中的毛利率 | ✅ 已查（第2節），但為公司整體毛利率，非 Apple 訂單專屬 |
| 其他主要零件在 iPhone 成本中比例 | ✅ 部分查（第4節：Sony、SK Hynix 財報；第5節：BOM 拆解中個別零件占比），記憶體與感光元件數字非 iPhone 專屬業務數字 |

**共同限制**：以上所有公司財報數字（Apple、台積電、鴻海、SK Hynix、Sony）都是「公司整體」或「事業部整體」的財務數字，**沒有一家公司會公布「這顆晶片／這片鏡頭專門賣給 Apple 賺多少錢」這種訂單層級的利潤數字**（商業機密）。這是設計「100元分配」活動時務必讓學生理解的限制：我們是用「這家公司整體有多賺錢」去合理推論「這家公司在 iPhone 供應鏈裡大概拿走多少」，而不是精確的訂單利潤數字。
