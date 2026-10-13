這個資料夾是產生教材頁面的 Python 程式（學生不會看到）。在這個資料夾裡執行：
  python3 schedule.py → 重新產生 ../schedule.html（課程規劃／練習題目表）
  python3 u02b.py     → ../unit02b.html
  python3 u06b.py     → ../unit06b.html
  python3 u07b.py     → ../unit07b.html
  python3 u09.py      → ../unit09.html
範例程式都會真的執行一次，執行結果自動寫進頁面。
py125.py 是吳邦一〈Python 程式識讀 125 題〉的單元分類（題號、難度、PDF 頁碼），
改分類後重新執行上面的程式，各單元頁最後的「課後識讀練習」和課程規劃頁會一起更新
（手寫的單元頁 unit02～07 的題號區塊，需要另外執行一次 py125.add_unit_block）。
其他單元頁面是手寫的 HTML，直接改 .html 檔。
  python3 handouts.py → 重新產生 ../assets/handouts/ 的三份回家作業；模擬考與解答寫到課程資料夾外的 apcs-ee-teacher-only/
                         （三份回家識讀練習、第 4 次課模擬考、教師用解答）
  模擬考的 30 題寫在 py125.py 的 MOCK；改了之後重新執行 handouts.py、schedule.py 和各單元頁。
  MOCK_PASSWORD='密碼' python3 mock_page.py → 重新產生 ../mock.html 和 ../assets/mock-data.js（線上識讀模擬考）
                         題目圖片與答案用這個密碼加密（AES-GCM），密碼不會寫進任何檔案；
                         要換密碼，用新密碼重新執行一次即可。改了 py125.py 的 MOCK 也要重新執行。
