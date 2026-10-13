/* ===================================================================
   交易所設定檔 —— 老師只要改這一行！
   部署完 Apps Script 網路應用程式後，會拿到一個網址，長得像：
     https://script.google.com/macros/s/AKfy............/exec
   把那個網址整段貼到下面的引號裡，存檔、重新上傳到 GitHub 即可。
   （詳細步驟見同資料夾的「老師設定說明.txt」）
   =================================================================== */
window.EXCHANGE_API = "https://script.google.com/macros/s/AKfycbzsawmkym4WI83RSCBAONyLiSLZJO172OJvQelBwt3vS7JinvgXKvfARGmltTWkdh1Y/exec";

/* 以下通常不用改 */
window.EXCHANGE_CFG = {
  title: "資安幣圈模擬交易所",
  coins: ["BTC", "ETH"],
  pollSeconds: 20           // 每隔幾秒自動更新一次幣價與帳戶
};
