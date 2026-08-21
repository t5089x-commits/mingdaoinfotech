# -*- coding: utf-8 -*-
"""把老師蒐集的 YouTube 影片分類，產生可篩選的對照表 video-library.html。"""
import html as _h, os, re, datetime

def esc(s): return _h.escape(str(s), quote=True)

# 蒐集清單的參考日期（最新一支為「12 天前」，今日約 2026-07-14）
REF = datetime.date(2026, 7, 13)

def rel_to_abs(rel):
    """把相對時間（X 天/個月/年前）換算成約估的絕對日期字串。"""
    if not rel or rel == "—":
        return "日期不詳"
    m = re.match(r"(\d+)\s*天前", rel)
    if m:
        d = REF - datetime.timedelta(days=int(m.group(1)))
        return f"{d.year}年{d.month}月{d.day}日"
    m = re.match(r"(\d+)\s*個月前", rel)
    if m:
        total = REF.year * 12 + (REF.month - 1) - int(m.group(1))
        y, mo = total // 12, total % 12 + 1
        return f"約 {y}年{mo}月"
    m = re.match(r"(\d+)\s*年前", rel)
    if m:
        # 以「X 年 = X×12 個月」初估到月份（錨定參考月份）
        total = REF.year * 12 + (REF.month - 1) - int(m.group(1)) * 12
        y, mo = total // 12, total % 12 + 1
        return f"約 {y}年{mo}月"
    return rel

# 分類桶（顯示順序）：key -> (顯示名稱, 類型 unit/supp)
BUCKETS = [
    ("U1", "單元1｜課程介紹・AI 與未來職業", "unit"),
    ("U2", "單元2｜數字系統・編碼（0 與 1）", "unit"),
    ("U3", "單元3｜資料運算與儲存・傳輸", "unit"),
    ("U4", "單元4｜電腦簡介・發展史", "unit"),
    ("U5", "單元5｜電腦五大單元・CPU／記憶體", "unit"),
    ("U6", "單元6｜電腦硬體與組裝", "unit"),
    ("U7", "單元7｜運算思維・演算法", "unit"),
    ("PY", "單元8–12｜Python・程式設計", "unit"),
    ("AI", "補充｜AI 通識與社會議題", "supp"),
    ("SEC", "補充｜資訊安全與駭客", "supp"),
    ("TOOL", "補充｜AI 工具與 Agent 教學", "supp"),
    ("MAKER", "補充｜創客・趣味（Minecraft／DIY）", "supp"),
    ("BLOCK", "補充｜區塊鏈與加密貨幣（課外延伸）", "supp"),
    ("SOC", "補充｜社會・經濟・其他（課外延伸）", "supp"),
    ("SCH", "補充｜校內活動／競賽", "supp"),
]
BNAME = {k: n for k, n, t in BUCKETS}

# (vid, 標題, 頻道, 長度, 桶, 課堂用途)
V = [
("CmcTKacenIM","資安駭客親自解答網友疑問！Google 是史上最強駭客工具？","GQ Taiwan","11:53","SEC","駭客真人問答，適合資安議題引起動機。"),
("PpeCur6fEXc","我的 AI agent 連續跑了 27 個小時，/goal 功能怎麼用？","Gary Chen","15:59","TOOL","展示 AI Agent 自動化能力。"),
("XkzmO83RWzw","我們，該如何面對這個充滿 Token 的世界？ft. Genspark","大時叔叔","31:53","AI","AI 時代思辨，適合開學導論。"),
("I6OHP7EtqWM","为什么游戏显卡抛弃了玩家？","林亦LYi","17:26","U6","顯示卡市場與規格，接單元6顯卡。"),
("lMLRlOpnaQ0","用 AI 卖袜子，狂赚 270 万美金，普通人真的有机会","昌健胡说","2:59","U1","AI 創造新職涯機會，短片引起動機。"),
("an7Dbkh7no4","六个 AI 相互入侵服务器！谁能杀死对方？","林亦LYi","12:54","SEC","AI＋資安攻防，趣味切入。"),
("bPWcSxkD6Uo","【硬核科普】WiFi 是怎么传递信息的？把信息装进电磁波有多难？","硬件茶谈","12:16","U3","資料傳輸／訊號，接單元3傳輸方式。"),
("BN53Q82_ZNQ","我的留言區變成資安戰場｜AI 遇到 Prompt Injection 攻擊","蝦說 AI (小金老師)","2:56","SEC","AI 提示注入攻擊，短片資安案例。"),
("e6_arlqoq1E","YouTube 留言大災難｜AI 龍蝦的自動化翻車實錄","蝦說 AI (小金老師)","4:26","TOOL","AI 自動化的風險與失控實例。"),
("i8CVb7-c0lY","如何保证发出去的微信和 QQ 消息不被篡改？详解 RSA 加密算法","硬件茶谈","14:49","SEC","RSA 加密原理，資訊安全延伸。"),
("sq5nbne5tao","Polymarket 是什麼？全世界最瘋的『賭場』竟成預測未來的方式","腦哥 Chill塊鏈","17:52","BLOCK","預測市場／區塊鏈應用，課外延伸。"),
("fBtnqkVSg_I","数学不好也能听懂的算法 - RSA 加密和解密原理和过程","技术蛋老师","7:34","SEC","淺白版 RSA，適合入門加密。"),
("cpGo6Dg66qk","一群草臺班子，讓 99% 的門禁卡都在裸奔：如何破解門禁卡？","柴知道","9:56","SEC","門禁卡（RFID）安全，生活化資安。"),
("uaOeOw0ZnKw","量子電腦對比特幣的真正威脅","腦哥 Chill塊鏈","16:46","BLOCK","量子運算 vs 加密／區塊鏈，課外延伸。"),
("FR3q4mGQRUI","Vibe Coding 做產品為什麼失敗？營收 $0 全解析","Debug 土撥鼠","9:05","PY","AI 寫程式的現實限制，程式設計反思。"),
("ZO39ITfwpkU","台灣頂尖駭客現身說法！連馬桶也能駭 ft. DEVCORE 翁浩正｜志祺七七","志祺七七","27:12","SEC","本土駭客深度訪談，資安職涯。"),
("cDkRlcsBK2c","AI 智能體要造反了，它們自立先知，創造了甲殼神教｜尼可拉斯楊","尼可拉斯楊","24:24","AI","多智能體湧現行為，AI 議題討論。"),
("zTCwgHw1fLw","這一次，我害怕了...","大時叔叔","19:52","AI","AI 發展的隱憂，思辨用。"),
("JTQ6NH2twMg","Seedance 2.0 到底强在哪？","林亦LYi","9:37","AI","AI 生成影片工具的進展。"),
("QejszE7Wof0","Moltbook 保母等級部署教學：本機執行 AI Agent（OpenClaw 對接）","零度解说","11:16","TOOL","AI Agent 本機部署教學（進階）。"),
("OQ_EhCtNc2M","電腦科學教授解答程式設計問題！vibe coding、Rust、討厭數學也能寫程式？GQ","GQ Taiwan","33:49","PY","程式設計常見疑問總整理，導論極佳。"),
("sc7Na07TdfM","聽我說，也許火星殖民是個壞主意","大時叔叔","27:52","SOC","科學社會思辨，課外延伸。"),
("bxm-Gt00-R4","我們做了一台魔法鋼琴...","老师好我叫何同学","14:01","MAKER","軟硬整合創客專題，啟發實作。"),
("uVEI7rfVB2I","【Huan】高價記憶體未來恐成常態？來聊聊記憶體漲價","Huan","10:11","U6","RAM 市場與規格，接單元6記憶體。"),
("3ibjoqBngl8","8 小时让 AI 做 3 个游戏！居然还挺好玩？","林亦LYi","8:38","TOOL","用 AI 快速做遊戲，AI 工具展示。"),
("zd5g0-fpSQA","人類社會，可以沒有黃金嗎？","大時叔叔","25:32","SOC","經濟社會議題，課外延伸。"),
("4_TDUv5528s","b-money 比特币的前身？神秘的密码学家 Wei Dai 是否是中本聪？","Aaron J","7:10","BLOCK","區塊鏈前史，課外延伸。"),
("bXe8Ea3W298","Google AI Studio 新功能爆炸！AI 直接『看』螢幕手把手教你","小in分享","13:57","TOOL","AI 螢幕理解工具教學。"),
("AEUBCul1MEo","我們的經濟出了什麼問題？","大時叔叔","20:54","SOC","總體經濟議題，課外延伸。"),
("9eH1_G0QVt0","【漫士】没有这个算法，我们将在网络上裸奔","漫士沉思录","22:12","SEC","公鑰加密／網路安全的數學基礎。"),
("IcoLXCwdvZc","洋人丢的电子垃圾，都去哪了？","影视飓风","22:39","SOC","電子廢棄物議題，可融入硬體＋環境。"),
("-IojK8dGQeA","AI 炒币 48 小时：DeepSeek 赚 4000 刀，GPT 亏到 6000！","神烦老狗","4:20","AI","AI 決策比較，趣味切入。"),
("8-B6ryuBkCM","Simulating Black Holes in C++","kavan","12:28","PY","以程式模擬物理，綜合應用（進階）。"),
("lXUZvyajciY","Andrej Karpathy — We're summoning ghosts, not building animals","Dwarkesh Patel","2:26:08","AI","AI 大師深度訪談（進階，選段播）。"),
("5ACrx4l7_fM","【漫士】红蓝眼谜题：大家都知道，为何却不能说？","漫士沉思录","17:27","U7","經典邏輯推理謎題，運算思維。"),
("CE4qk8eTsI8","矽谷的『中國恐懼症』，Palmer Luckey 認為殺手機器人比人類士兵更道德？","fOx Hsiao","26:29","SOC","AI 國防倫理，課外議題。"),
("B5iIbdCpjCc","一口氣搞懂 ETH 以太坊","腦哥 Chill塊鏈","46:12","BLOCK","以太坊全解，課外延伸。"),
("9Xj3l3NVFrQ","Palmer Luckey 於 TED 演講：人工智慧如何避免台海戰爭","fOx Hsiao","15:17","SOC","AI 與地緣政治，課外議題。"),
("eA6EJhsdBXo","對半導體貢獻最多卻沒得諾貝爾獎！矽谷之父是誰？【晶片崛起 EP6】","PanSci 泛科學","12:02","U4","半導體發展史，接單元4。"),
("0HlzvDZmZr0","AI 終有覺醒之日 麻煩的是它不會告訴我們｜1K 圖解","1K圖解","20:41","AI","AI 風險議題，思辨用。"),
("mqv_aLeTW6w","黃仁勳公開拋出驚人預言，未來人們要面臨的問題與機會","獨孤軒轅策","6:44","U1","產業領袖看未來職涯，導論動機。"),
("rKC4LQ3s0lQ","用最好的动画为你讲解 — 机械硬盘的原理","Redknot-乔红","13:29","U6","HDD 運作動畫，接單元6儲存裝置。"),
("f-m9FEFbF4c","最重要又最狗血的諾貝爾獎！第一顆半導體電晶體【晶片崛起 EP4】","PanSci 泛科學","10:26","U4","電晶體誕生（第二代電腦），接單元4。"),
("C-zH721QoQ4","IBM 靠人口普查？19 世紀沒電腦就能寫程式？誰決定用 0、1【晶片崛起 EP2】","PanSci 泛科學","11:06","U4","打孔卡與二進位起源，接單元4／數字系統。"),
("SdwTmXHwFBQ","沒有晶片，靠『真空管』怎麼做出第一台通用電腦？【晶片崛起 EP3】","PanSci 泛科學","11:51","U4","真空管與第一代電腦，接單元4。"),
("D2ibL6z_Cns","AI 的想法已脫離人類掌控？『可解釋 AI』是什麼？ft. 鼎新數智","PanSci 泛科學","13:36","AI","可解釋 AI 議題。"),
("i_obtyz-zdQ","AI 叛乱！当一个 AI 劝一群 AI 造反...","林亦LYi","8:19","AI","多智能體實驗，AI 議題。"),
("Rc11UDVg4_s","计算机的 0 和 1 是怎么变成图片、视频和声音的？（最新版）","Hao Chen","4:04","U2","資料如何用 0/1 表示，超適合單元2。"),
("uSsVThszLtA","一万年以后，你的电脑还能正常使用吗？","Z极客","6:29","U3","資料長期保存與儲存媒介，趣味切入。"),
("ObjMFpqh3L4","轻了，然后呢？vivo Vision 首发体验！","林亦LYi","5:22","MAKER","新一代穿戴／VR 硬體開箱。"),
("ONfntZrrwtM","『電腦』由它開始！19 世紀不吃電的『電腦』如何運作？【晶片崛起 EP1】","PanSci 泛科學","12:01","U4","巴貝奇機械式電腦，接單元4發展史。"),
("uAIzEJVG3Bs","电脑的 0 和 1 是怎么变成我们屏幕上看到的东西的？","Hao Chen","3:05","U2","0/1 到畫面，單元2資料表示短片。"),
("glPLK4Kh6ds","為了做動畫特效，他不小心做了影響世界的算法，這三條規則【差評君】","差评君","9:49","U7","Boids 群聚演算法，運算思維。"),
("khv0xWIHXEo","影片製作流程公開｜AI 動畫能賺錢嗎｜一隻土撥鼠","一隻土撥鼠MrMarmot","13:23","U1","AI 創作變現，職涯延伸。"),
("Kk0EG-ZuVOw","CL1 是人類縮影？我們本就是高維文明的活體計算機｜總裁聊聊","總裁聊聊","13:44","SOC","偽科學色彩重，課外（慎用）。"),
("FzlLmp-vFvg","【漫士】AI 幻觉是如何产生的？如何解决？","漫士沉思录","7:30","AI","AI 幻覺原理，理解生成式 AI。"),
("cvR0FaI486k","【漫士】数学读心术：大数据猜你喜欢为什么这么准？","漫士沉思录","23:37","U7","推薦演算法背後的數學，運算思維。"),
("gIfD6YtY0ts","為了不用擦白板，我們做了這個...","老师好我叫何同学","3:27","MAKER","創客解決生活問題，啟發實作。"),
("3bWFWbaEQqA","不只打電動！癱瘓者『心控』特斯拉機器人！Neuralink 發表會","fOx Hsiao","1:00:00","AI","腦機介面與 AI 未來（選段播）。"),
("zSstXi-j7Qc","錕斤拷是怎樣煉成的 — 中文顯示『入』門指南【柴知道】","柴知道","14:59","U2","字元編碼與亂碼，超適合單元2。"),
("s01Dr1IzKQQ","【AI 失业潮】我们离大规模失业有多远？","秋芝2046","23:43","U1","AI 對就業的衝擊，導論動機。"),
("r3ScrY7rMO4","CIH：計算機史上的車諾比！陳盈豪的炫技之作，連續 5 年全球癱瘓｜總裁聊聊","總裁聊聊","11:56","SEC","台灣 CIH 病毒史，資安＋歷史。"),
("tPAnFz01ieY","【何同學】我們做了個特別的鍵盤...","老师好我叫何同学","5:18","MAKER","輸入裝置創客專題。"),
("9KYcnxYldXY","【城】当你在注册时，系统怎样偷偷保护你的密码","网络小白_Uncle城","14:43","SEC","密碼雜湊與儲存安全。"),
("9YUZkvh-nSE","梯度，伪装，想要活下去的 AI","秋芝2046","18:40","AI","AI 對齊／安全，議題討論。"),
("Zdg-GgMMaBA","我还原了百年前的显示器！Split Flap Display","黑人黑科技","5:30","MAKER","輸出裝置創客，機械顯示。"),
("9DRkrGinuLo","我让 AI 教我学习，结果她骂我！","林亦LYi","11:02","TOOL","AI 學習助手體驗。"),
("CiPOdxa15VI","世上無人能破解！量子力學為何是最強之盾？量子糾纏｜量子熊 ✕ 泛科學 EP11","PanSci 泛科學","15:14","SEC","量子加密，資安進階延伸。"),
("utMZwhNZYVk","一鍵擁有吉卜力頭貼？AI 模仿是藝術還盜版？【TODAY 看世界】","TODAY 看世界","8:36","AI","生成式 AI 著作權倫理。"),
("jz4SxHZhJok","MCP 幼儿园级教程，让你的 AI 自己干活！","秋芝2046","8:14","TOOL","MCP 概念入門教學。"),
("hsooOhxJ7Nc","聊聊 MCP：AI 大一统要来了？","林亦LYi","5:37","TOOL","MCP 生態解說。"),
("qmcDiYvp1wE","AI 模型通过三方图灵测试｜加州大学圣迭戈分校研究报告","最佳拍档","9:46","AI","圖靈測試與 AI 擬人，議題。"),
("dHUjmvP0uog","AI 快燒壞了？伺服器頻繁過熱！熱力學決定了 AI 的極限？ft. 高柏科技","PanSci 泛科學","12:23","AI","AI 基礎設施與能耗議題。"),
("kE3Xb-XH8NU","【不止遊戲】二戰德軍號稱『謎』的密碼機，究竟是如何使用的？","森纳映画","16:52","SEC","Enigma 密碼機，密碼學史。"),
("9T1GVtvig2g","【吉卜力 AI 濾鏡】為何爭議不斷？宮崎駿：這是對生命的侮辱｜井川一","Inokawa Hajime井川一","12:03","AI","AI 生成與創作倫理爭議。"),
("lvH4-4iYjgs","Python 6 小時初學者課程（2023）#python教學 #完整課程","（YouTube 課程）","5:53:04","PY","完整 Python 教學，可當自學／補課主教材。"),
("TF7VyjFSLcY","64 位计数器的尽头是什么？等你老了它还没数完！","爱上半导体","2:05","U2","二進位與位元數的直覺，單元2短片。"),
("Ur8MbOj17Gs","图灵测试大逃杀！七大顶级 AI 伪装人类！","林亦LYi","13:43","AI","圖靈測試趣味實測。"),
("7kB9-nQJR44","DDoS 技术鉴赏","Ele实验室","18:06","SEC","阻斷服務攻擊，網路安全。"),
("FSpg3x2EVF4","(寫程式玩數學#7) 遞迴的力量(一)：快速排序演算法","（寫程式玩數學）","17:52","U7","遞迴與排序演算法，運算思維／程式。"),
("jskNDYe1E-0","这就是 1MB 的大小？航拍画面刷新你的认知！","爱上半导体","1:48","U3","資料儲存單位的具象化，單元3短片。"),
("J41EIsUkaYE","一口气搞懂二进制漏洞攻防对抗史！","轩辕的编程宇宙","16:06","SEC","二進位漏洞與資安攻防史。"),
("F68COu2nm3k","AI 大神 Karpathy『直覺程式開發』Vibe Coding，YC 團隊 95% 程式碼 AI 產","fOx Hsiao","31:34","PY","AI 協作寫程式的新型態。"),
("5yAbVkIMl_M","Most Popular Programming Languages 1955 - 2025","Captain Gizmo","8:28","PY","程式語言演變史，程式設計導論。"),
("zI8GCxlGZIA","台積電看了都害怕的工藝？我在 Minecraft 裡蓋了電腦！","早安鍵圈","27:34","MAKER","以紅石理解邏輯閘與電腦組成。"),
("kjG92Mb76s8","新一代 Python 打包 + 加速神器：nuitka","Crossin的编程教室","4:58","PY","Python 打包工具（進階）。"),
("EFmxPMdBqmU","Animation vs. Coding","Alan Becker","9:27","PY","程式概念動畫化，超吸睛引起動機。"),
("h_nytkSJv3I","【漫士】火柴人 vs 编程详细解析！我覺得我在上 python 课","漫士沉思录","26:02","PY","逐格解析上片的程式概念，延伸教學。"),
("PvyQVCp0aVI","我记录了半年的 B 站热门，最火的 UP 主竟然是...","林亦LYi","9:56","TOOL","資料蒐集與分析實作。"),
("bqImyyk1bMQ","用最好的动画为你讲解 — 内存的原理","Redknot-乔红","13:29","U5","記憶體運作動畫，接單元5記憶單元。"),
("MzblDVVmnmU","【小貝】僅 13KB 大小的奇葩遊戲，玩家越弱角色越強","小贝的游戏食堂","8:09","PY","極小程式的巧思，程式趣味。"),
("dsi8Fmd3BEg","为什么安卓们开始轮流兼容苹果？","林亦LYi","8:33","SOC","作業系統生態與產業，課外。"),
("7W4I6HMH558","連電腦都能土炮？DIY 惡搞一體式箱型電腦！【胡思亂搞】","胡子Huzi","18:22","U6","裝機實作趣味版，接單元6組裝。"),
("CW9N6kGbu2I","I Made a Working Computer with just Redstone!","mattbatwings","15:37","MAKER","純紅石電腦，理解邏輯／CPU 組成。"),
("itWVd6uAxYE","实测用 GPT 代替我的眼睛！会翻车吗？","AI-Fan 帆哥","7:02","TOOL","AI 視覺輔助應用實測。"),
("jot6X0pFMCk","遞迴只應天上有，凡人應當用迴圈！程式寫十次不如演一次","宇先程式","11:28","PY","遞迴 vs 迴圈，接單元10／11。"),
("G-6zD_B_Ewk","人类最伟大的发明 — PN 结","Redknot-乔红","9:59","U4","半導體 PN 接面原理，接單元4。"),
("6ZraACggaBU","【Direct3D 篇】为什么游戏总要编译着色器？","Redknot-乔红","12:08","U6","GPU 與繪圖管線（進階）。"),
("x7_LSjWe2rc","【OpenGL 篇】为什么游戏总要编译着色器？","Redknot-乔红","16:04","U6","GPU 著色器原理（進階）。"),
("kEB11PQ9Eo8","非歐幾里德世界的引擎","CodeParade","5:15","PY","遊戲引擎與程式創意（進階）。"),
("H8MFw0qxY84","为了让电脑更快，他们把『乘法』玩到了极致","量子位","9:09","U5","CPU 運算與演算法優化，接單元5。"),
("g1r3iLejTw0","没有显卡的年代，这群程序员用 4 行代码优化游戏","量子位","14:38","U6","繪圖與硬體限制下的最佳化。"),
("1fYPDlWwUkE","我在 Minecraft 裡用紅石打造一個人工智慧？耗時二個月","早安鍵圈","18:10","MAKER","紅石邏輯打造 AI，理解運算。"),
("EIGY_j3p3KU","我用紅石做出了可以學習的人工智慧，預測我頻道的流量！","早安鍵圈","18:59","MAKER","紅石實作機器學習概念。"),
("n_ItIpBB5zM","我让六个 AI 合租，居然出了个海王？","林亦LYi","24:26","AI","多智能體互動實驗，趣味。"),
("N5uCJDc-KYo","Google 反壟斷敗訴 搜尋引擎不再一方獨霸？｜投資 IN 總經 EP44","財訊","7:32","SOC","科技產業與反壟斷，課外時事。"),
("YHGkp6HUEmo","404 錯誤是什麼意思？資工教授回答網友『編碼』提問｜GQ","GQ Taiwan","17:13","PY","程式／網路常見概念問答，導論。"),
("glZ9JVTuolk","我被同事戴上了測謊儀…何同學工作室 8 月開箱","老师好我叫何同学","9:28","MAKER","工作室開箱，創客氛圍。"),
("yOiPE1-F45w","【寫程式實測】用最好的 prompt 讓 ChatGPT 4o 考上台大醫科嗎？","軟體工程師 Roger","15:28","TOOL","提示工程實測 AI 能力。"),
("-BP7DhHTU-I","I made Minecraft in Minecraft with redstone!","sammyuri","3:05","MAKER","紅石邏輯的極致，理解電腦本質。"),
("5YADlrSJUqA","Minecraft 裡玩 Minecraft？世上第一台紅石 3D 電腦！","杯子蛋糕實驗室","4:01","MAKER","紅石電腦，理解邏輯與運算。"),
("eraWvfD_Ihg","一小時略懂 AI｜GPT、Sora、Diffusion、圖靈測試、人工智慧史","PanSci 泛科學","55:34","AI","AI 通識完整版，適合專題導論。"),
("Za0qBVv5GlE","阿里数赛难度如何？我用 AI 拿了 18 分","林亦LYi","15:16","AI","AI 解數學競賽，能力邊界。"),
("OMuxeHgE1f0","這是我見過最精緻的電子產品...何同學工作室 5 月開箱","老师好我叫何同学","11:40","MAKER","電子產品開箱，創客氛圍。"),
("ezgKJhi0Czc","我们把 AI 剖开，可视化还原文生图到底发生了什么？Stable Diffusion 原理","AI-Fan 帆哥","6:25","AI","生成式 AI 原理可視化。"),
("j5N2j6Ydhao","【漫士科普】GPT 是如何運作的？為什麼要學習接下一個字？","漫士沉思录","18:52","AI","GPT 運作原理，理解大型語言模型。"),
("Y88lf8jinb0","救命！我被 AI 控制了！","茶里","7:42","AI","AI 融入日常的趣味觀察。"),
("vuvckBQ1bME","How To Make A CPU","（科普短片）","1:40","U5","一分鐘看懂 CPU 組成，接單元5。"),
("PXzhBBhwyt0","坚守在 Windows 中 30 年的古董文件，是做什么用的？","epcdiy","5:30","SOC","作業系統冷知識，課外。"),
("2moxIRlqXkM","セルフ給油機の仕組み／How a Fueling Nozzle Works","Mr. Denjiro's Happy Energy","3:01","SOC","機械原理（非資訊），課外備用。"),
("SfKXHCJDGKM","【何同學】我用 108 天开了个灯......","老师好我叫何同学","7:33","MAKER","長期創客專題，毅力與整合。"),
("acQlmpUBKCY","免費使用 ChatGPT-4 的 4 種方法！Dalle3、GPTs 完全免費","學長Ethan","9:06","TOOL","免費 AI 工具取得教學。"),
("aPUvpgpM6vc","10 岁小孩也能写原神？低代码编程是噱头吗？","林亦LYi","9:19","PY","低代碼 vs 傳統程式的思辨。"),
("7K0WeptIrm0","我后悔让 AI 看 B 站了…","林亦LYi","9:06","AI","AI 觀看理解影片的實驗。"),
("5ieOxxXcl8U","人工智能与人类终局","林亦LYi","30:32","AI","AI 長期影響的深度討論。"),
("bOGJw9-NqiI","Google 最強 AI Gemini｜你覺得算是造假嗎？","今天比昨天厲害","8:01","AI","AI 行銷與真實性議題。"),
("d3gHFesPc_E","【算法】Huffman 编码","从0开始数","5:05","U3","霍夫曼壓縮編碼，接單元3資料壓縮。"),
("ST65L4pG_6w","【裝機教程】全網最好的裝機教程，沒有之一","硬件茶谈","1:16:45","U6","超完整實機組裝教學，接單元6組裝（可分段播）。"),
("FcwRSCjweUQ","如何花 20 美元掘一下互联网的根？","量子位","9:41","SEC","DNS 與網路根伺服器安全，資安延伸。"),
("YX40hbAHx3s","P vs. NP and the Computational Complexity Zoo","hackerdashery","—","U7","計算複雜度經典科普，運算思維進階。"),
]


# 影片發布時間（老師蒐集當時的相對時間；vid -> 發布）
PUB = {
"CmcTKacenIM":"12 天前","PpeCur6fEXc":"1 個月前","XkzmO83RWzw":"1 個月前","I6OHP7EtqWM":"1 個月前",
"lMLRlOpnaQ0":"3 個月前","an7Dbkh7no4":"2 個月前","bPWcSxkD6Uo":"2 個月前","BN53Q82_ZNQ":"3 個月前",
"e6_arlqoq1E":"4 個月前","i8CVb7-c0lY":"5 年前","sq5nbne5tao":"2 個月前","fBtnqkVSg_I":"1 年前",
"cpGo6Dg66qk":"4 個月前","uaOeOw0ZnKw":"3 個月前","FR3q4mGQRUI":"3 個月前","ZO39ITfwpkU":"3 個月前",
"cDkRlcsBK2c":"4 個月前","zTCwgHw1fLw":"5 個月前","JTQ6NH2twMg":"4 個月前","QejszE7Wof0":"5 個月前",
"OQ_EhCtNc2M":"6 個月前","sc7Na07TdfM":"6 個月前","bxm-Gt00-R4":"6 個月前","uVEI7rfVB2I":"7 個月前",
"3ibjoqBngl8":"7 個月前","zd5g0-fpSQA":"8 個月前","4_TDUv5528s":"7 個月前","bXe8Ea3W298":"1 年前",
"AEUBCul1MEo":"7 個月前","9eH1_G0QVt0":"8 個月前","IcoLXCwdvZc":"8 個月前","-IojK8dGQeA":"8 個月前",
"8-B6ryuBkCM":"11 個月前","lXUZvyajciY":"8 個月前","5ACrx4l7_fM":"8 個月前","CE4qk8eTsI8":"9 個月前",
"B5iIbdCpjCc":"9 個月前","9Xj3l3NVFrQ":"1 年前","eA6EJhsdBXo":"9 個月前","0HlzvDZmZr0":"1 年前",
"mqv_aLeTW6w":"9 個月前","LQfIAetYc5g":"9 個月前","rKC4LQ3s0lQ":"10 個月前","f-m9FEFbF4c":"9 個月前",
"C-zH721QoQ4":"10 個月前","SdwTmXHwFBQ":"10 個月前","D2ibL6z_Cns":"1 年前","i_obtyz-zdQ":"2 年前",
"Rc11UDVg4_s":"8 年前","uSsVThszLtA":"10 個月前","ObjMFpqh3L4":"10 個月前","ONfntZrrwtM":"10 個月前",
"uAIzEJVG3Bs":"8 年前","glPLK4Kh6ds":"10 個月前","khv0xWIHXEo":"11 個月前","Kk0EG-ZuVOw":"1 年前",
"FzlLmp-vFvg":"11 個月前","cvR0FaI486k":"11 個月前","gIfD6YtY0ts":"11 個月前","3bWFWbaEQqA":"1 年前",
"zSstXi-j7Qc":"3 年前","s01Dr1IzKQQ":"1 年前","r3ScrY7rMO4":"2 年前","tPAnFz01ieY":"1 年前",
"9KYcnxYldXY":"1 年前","9YUZkvh-nSE":"1 年前","Zdg-GgMMaBA":"1 年前","9DRkrGinuLo":"1 年前",
"CiPOdxa15VI":"2 年前","utMZwhNZYVk":"1 年前","jz4SxHZhJok":"1 年前","hsooOhxJ7Nc":"1 年前",
"qmcDiYvp1wE":"1 年前","dHUjmvP0uog":"1 年前","kE3Xb-XH8NU":"4 年前","9T1GVtvig2g":"1 年前",
"lvH4-4iYjgs":"2 年前","TF7VyjFSLcY":"1 年前","Ur8MbOj17Gs":"1 年前","7kB9-nQJR44":"2 年前",
"FSpg3x2EVF4":"3 年前","jskNDYe1E-0":"1 年前","J41EIsUkaYE":"1 年前","F68COu2nm3k":"1 年前",
"5yAbVkIMl_M":"1 年前","zI8GCxlGZIA":"1 年前","kjG92Mb76s8":"1 年前","EFmxPMdBqmU":"1 年前",
"h_nytkSJv3I":"1 年前","KJe07T_r0cQ":"1 年前","PvyQVCp0aVI":"1 年前","bqImyyk1bMQ":"1 年前",
"MzblDVVmnmU":"3 年前","dsi8Fmd3BEg":"1 年前","7W4I6HMH558":"1 年前","CW9N6kGbu2I":"3 年前",
"itWVd6uAxYE":"1 年前","jot6X0pFMCk":"3 年前","G-6zD_B_Ewk":"1 年前","6ZraACggaBU":"1 年前",
"x7_LSjWe2rc":"1 年前","ST65L4pG_6w":"3 年前","FcwRSCjweUQ":"1 年前","kEB11PQ9Eo8":"7 年前",
"H8MFw0qxY84":"1 年前","g1r3iLejTw0":"2 年前","1fYPDlWwUkE":"2 年前","EIGY_j3p3KU":"1 年前",
"n_ItIpBB5zM":"1 年前","N5uCJDc-KYo":"1 年前","YHGkp6HUEmo":"3 年前","glZ9JVTuolk":"1 年前",
"yOiPE1-F45w":"1 年前","-BP7DhHTU-I":"3 年前","5YADlrSJUqA":"3 年前","eraWvfD_Ihg":"2 年前",
"Za0qBVv5GlE":"2 年前","OMuxeHgE1f0":"2 年前","4G7BxUz7tqA":"2 年前","ezgKJhi0Czc":"2 年前",
"j5N2j6Ydhao":"2 年前","Y88lf8jinb0":"2 年前","vuvckBQ1bME":"4 年前","PXzhBBhwyt0":"2 年前",
"2moxIRlqXkM":"3 年前","SfKXHCJDGKM":"3 年前","acQlmpUBKCY":"2 年前","aPUvpgpM6vc":"2 年前",
"7K0WeptIrm0":"2 年前","5ieOxxXcl8U":"2 年前","bOGJw9-NqiI":"2 年前","d3gHFesPc_E":"5 年前",
"YX40hbAHx3s":"—",
}


# 需老師斟酌／慎用的影片：vid -> 警語原因
WARN = {
"Kk0EG-ZuVOw": "偽科學／玄學臆測（阿卡西紀錄等），建議當「媒體識讀」反例，勿當知識傳授。",
"sq5nbne5tao": "涉賭博／預測市場，請明確說明「非投資建議」。",
"-IojK8dGQeA": "涉加密貨幣投機，請明確說明「非投資建議」。",
"CE4qk8eTsI8": "戰爭／國防倫理且帶政治立場（標題「中國恐懼症」），宜兩面並陳、保持中立。",
"utMZwhNZYVk": "AI 生成的著作權／倫理爭議，立場較主觀，宜呈現不同觀點。",
"9T1GVtvig2g": "AI 創作倫理爭議，立場較主觀，宜呈現不同觀點。",
}


def build():
    # 統計
    counts = {}
    for v in V:
        counts[v[4]] = counts.get(v[4], 0) + 1
    total = len(V)

    # 篩選鈕
    chips = ['<button class="chip active" data-f="all" onclick="flt(this)">全部 <span class="c">%d</span></button>' % total]
    for k, name, t in BUCKETS:
        if counts.get(k):
            chips.append('<button class="chip %s" data-f="%s" onclick="flt(this)">%s <span class="c">%d</span></button>'
                         % (t, k, esc(name), counts[k]))
    chips_html = "\n".join(chips)

    # 分組表格
    sections = []
    for k, name, t in BUCKETS:
        rows = [v for v in V if v[4] == k]
        if not rows:
            continue
        trs = ""
        for vid, title, ch, dur, bk, use in rows:
            url = "https://www.youtube.com/watch?v=" + vid
            pub = PUB.get(vid, "—")
            pub_abs = rel_to_abs(pub)
            warn = WARN.get(vid)
            warn_html = f'<div class="warn-note">⚠ 需斟酌：{esc(warn)}</div>' if warn else ""
            rowcls = "row " + bk + (" hasWarn" if warn else "")
            trs += (f'<tr class="{rowcls}">'
                    f'<td class="ttl"><a href="{url}" target="_blank" rel="noopener">{esc(title)} ↗</a>{warn_html}</td>'
                    f'<td class="ch">{esc(ch)}</td>'
                    f'<td class="dur">{esc(dur)}</td>'
                    f'<td class="pub" title="蒐集當時：{esc(pub)}">{esc(pub_abs)}</td>'
                    f'<td class="use">{esc(use)}</td></tr>')
        sec_cls = "sec unit" if t == "unit" else "sec supp"
        sections.append(f'''<section class="{sec_cls}" data-b="{k}">
  <h2><span class="tag">{esc(k)}</span>{esc(name)} <span class="n">{len(rows)} 部</span></h2>
  <div class="tw"><table>
    <thead><tr><th>影片（點擊開啟）</th><th>頻道</th><th>長度</th><th>發布日期</th><th>建議課堂用途</th></tr></thead>
    <tbody>{trs}</tbody>
  </table></div>
</section>''')
    sections_html = "\n".join(sections)

    return TEMPLATE.replace("{{CHIPS}}", chips_html).replace("{{SECTIONS}}", sections_html).replace("{{TOTAL}}", str(total))


TEMPLATE = r'''<!DOCTYPE html>
<html lang="zh-Hant" data-theme="light">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>影片資源庫｜明道資訊科技</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@400;500;700;800;900&family=JetBrains+Mono:wght@400;700&display=swap" rel="stylesheet">
<style>
:root{--bg:#f6f8fb;--elev:#ffffff;--surf:#ffffff;--surf2:#eef2f7;--bd:#d8e0ea;--tx:#24303f;--txs:#55657a;--txf:#8695a8;--br:#12a066;--brs:#0e8a58;--ac:#2f8fa8;--mono:"JetBrains Mono",monospace;--f:"Noto Sans TC",system-ui,sans-serif}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--tx);font-family:var(--f);line-height:1.7}
a{color:var(--brs)}
.top{position:sticky;top:0;z-index:20;background:rgba(246,248,251,.92);backdrop-filter:blur(8px);border-bottom:1px solid var(--bd);padding:16px 20px}
.wrap{max-width:1040px;margin:0 auto;padding:0 20px}
.head{padding:30px 0 10px}
.head h1{margin:0 0 6px;font-size:1.7rem}
.head h1 .g{background:linear-gradient(120deg,var(--br),var(--ac));-webkit-background-clip:text;background-clip:text;color:transparent}
.head p{color:var(--txs);margin:0}
.tools{display:flex;gap:10px;flex-wrap:wrap;align-items:center;margin-top:14px}
#q{flex:1;min-width:200px;font:inherit;padding:9px 14px;border:1px solid var(--bd);border-radius:10px;background:var(--elev);color:var(--tx)}
#q:focus{outline:2px solid var(--br);border-color:var(--br)}
.toggle-chips{font:inherit;font-weight:800;font-size:.86rem;cursor:pointer;white-space:nowrap;
  padding:9px 16px;border-radius:10px;border:1px solid var(--br);background:var(--surf2);color:var(--brs)}
.toggle-chips:hover{background:rgba(53,216,150,.12)}
.chips{display:flex;gap:8px;flex-wrap:wrap;margin-top:12px;padding:12px;border:1px solid var(--bd);border-radius:12px;background:var(--elev)}
.chips[hidden]{display:none}
.chip{font:inherit;font-size:.8rem;font-weight:700;cursor:pointer;padding:6px 12px;border-radius:999px;border:1px solid var(--bd);background:var(--surf2);color:var(--txs)}
.chip .c{font-family:var(--mono);opacity:.7;margin-left:3px}
.chip.active{background:var(--br);color:#04150e;border-color:var(--br)}
.chip.supp.active{background:var(--ac);border-color:var(--ac)}
.sec{margin:26px 0}
.sec h2{display:flex;align-items:center;gap:10px;font-size:1.15rem;padding-bottom:8px;border-bottom:2px solid var(--bd);flex-wrap:wrap}
.sec h2 .tag{font-family:var(--mono);font-size:.72rem;font-weight:800;color:#04150e;background:var(--br);padding:2px 8px;border-radius:6px}
.sec.supp h2 .tag{background:var(--ac)}
.sec h2 .n{margin-left:auto;font-size:.8rem;color:var(--txf);font-weight:500}
.tw{overflow-x:auto;border:1px solid var(--bd);border-radius:12px;margin-top:12px}
table{width:100%;border-collapse:collapse;font-size:.92rem}
th,td{padding:10px 12px;text-align:left;border-bottom:1px solid var(--bd);vertical-align:top}
thead th{background:var(--surf2);position:sticky;top:0;white-space:nowrap;color:var(--tx);font-weight:700}
tbody tr:last-child td{border-bottom:none}
tbody tr:hover{background:rgba(53,216,150,.06)}
.ttl{min-width:260px}
.ttl a{text-decoration:none;font-weight:600}
.ttl a:hover{text-decoration:underline}
.ch{color:var(--txs);white-space:nowrap;font-size:.85rem}
.dur{font-family:var(--mono);color:var(--txf);white-space:nowrap;font-size:.85rem}
.pub{color:var(--txs);white-space:nowrap;font-size:.83rem}
.use{color:var(--txs);min-width:200px}
tr.hasWarn td{background:rgba(217,161,90,.07)}
.warn-note{margin-top:6px;font-size:.8rem;font-weight:600;color:#a86412;
  background:rgba(217,161,90,.14);border:1px solid rgba(217,161,90,.5);
  border-radius:8px;padding:5px 9px;line-height:1.5}
.empty{display:none;text-align:center;color:var(--txf);padding:40px}
.hint{color:var(--txf);font-size:.82rem;margin-top:6px}
footer{border-top:1px solid var(--bd);color:var(--txf);text-align:center;padding:24px;font-size:.82rem;margin-top:30px}
.home-fab{position:fixed;left:18px;bottom:18px;z-index:50;display:inline-flex;align-items:center;gap:7px;text-decoration:none;
  background:var(--br);color:#04150e;font-weight:800;font-size:.85rem;padding:10px 16px;border-radius:999px;
  box-shadow:0 8px 22px rgba(18,160,102,.28);transition:.16s}
.home-fab:hover{background:var(--brs);transform:translateY(-2px)}
@media(max-width:520px){.home-fab{left:12px;bottom:12px;padding:9px 13px;font-size:.8rem}}
</style>
</head>
<body>
<div class="top">
  <div class="wrap" style="padding:0">
    <div class="tools">
      <button class="toggle-chips" id="chipToggle" onclick="toggleChips()">🗂️ 分類：全部 ▾</button>
      <input id="q" type="text" placeholder="🔍 搜尋影片標題、頻道、用途…" oninput="search()">
    </div>
    <div class="chips" id="chips" hidden>{{CHIPS}}</div>
  </div>
</div>

<div class="wrap">
  <div class="head">
    <h1>影片<span class="g">資源庫</span></h1>
    <p>老師蒐集的 {{TOTAL}} 部影片，依「建議放在哪個單元／補充分類」整理。點分類鈕篩選、用搜尋框找關鍵字，點影片標題開新分頁觀看。</p>
    <p class="hint">※ 分類是建議，方便你規劃；同一部可能適合多處，覺得不合適隨時可以跟我說調整。<br>※「發布日期」為<strong>約估值</strong>：依你清單的相對時間（X 天／個月／年前）換算，日以下為概略（滑鼠移到日期可看原始「XX 前」）。需要精確到日的日期可再跟我說。<br>※ 標<span style="color:#a86412;font-weight:700">⚠ 需斟酌</span>的影片為敏感題材（偽科學、賭博/投機、政治/國防、著作權倫理等），建議搭配說明或當議題討論再播放。</p>
  </div>
  {{SECTIONS}}
  <div class="empty" id="empty">找不到符合的影片，換個關鍵字試試。</div>
</div>

<a class="home-fab" href="index.html" title="回到課程網站首頁">🏠 課程首頁</a>
<footer>明道中學 · 資訊科技　影片資源庫（教學規劃用）</footer>

<script>
var curF="all";
function toggleChips(){
  var c=document.getElementById("chips");
  c.hidden=!c.hidden;
  updateToggle();
}
function updateToggle(){
  var t=document.getElementById("chipToggle");
  var open=!document.getElementById("chips").hidden;
  t.textContent=(t.dataset.label||"🗂️ 分類：全部")+(open?" ▴":" ▾");
}
function flt(btn){
  document.querySelectorAll(".chip").forEach(function(c){c.classList.remove("active")});
  btn.classList.add("active");
  curF=btn.getAttribute("data-f");
  var name=(btn.firstChild&&btn.firstChild.textContent||"全部").trim();
  document.getElementById("chipToggle").dataset.label="🗂️ 分類："+name;
  apply();
  document.getElementById("chips").hidden=true;   // 選完自動收合
  updateToggle();
}
function search(){apply();}
function apply(){
  var q=document.getElementById("q").value.trim().toLowerCase();
  var anyVisible=false;
  document.querySelectorAll(".sec").forEach(function(sec){
    var b=sec.getAttribute("data-b");
    var secOk=(curF==="all"||curF===b);
    var rowsVisible=0;
    sec.querySelectorAll("tbody tr").forEach(function(tr){
      var txt=tr.innerText.toLowerCase();
      var match=secOk && (q===""||txt.indexOf(q)>=0);
      tr.style.display=match?"":"none";
      if(match)rowsVisible++;
    });
    sec.style.display=(secOk&&rowsVisible>0)?"":"none";
    if(rowsVisible>0)anyVisible=true;
  });
  document.getElementById("empty").style.display=anyVisible?"none":"block";
}
document.getElementById("chipToggle").dataset.label="🗂️ 分類：全部";
updateToggle();
</script>
</body>
</html>'''


if __name__ == "__main__":
    out = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "video-library.html"))
    with open(out, "w", encoding="utf-8") as f:
        f.write(build())
    print("寫入", out, "共", len(V), "部影片")
