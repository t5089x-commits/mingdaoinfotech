/* ===========================================================
   課程進度設定  ——  這一份已經改成從共用總表讀取！
   ===========================================================
   真正的數字現在統一寫在 ../shared/core/progress.js（五科同一份），
   老師要調整進度，直接改那個檔案裡「apcs」後面的數字就好，
   這裡不用再手動改。

   如果你只想讓「這一科」自己控制進度、不要跟著共用總表一起變動，
   把下面 unlockedUpTo 那一行改成直接寫死的數字（例如 unlockedUpTo: 5,），
   這一科就會脫鉤，不再受 shared/core/progress.js 影響。

   teacherKey   : 老師預覽用的密鑰。在任何頁面網址後面加上
                  ?key=你的密鑰   （例如 index.html?key=ji32k7au4a83）
                  就能解鎖並預覽全部單元，方便自己備課；
                  學生沒有這個密鑰，看到的仍是鎖住的狀態。
   =========================================================== */
window.COURSE_PROGRESS = {
  unlockedUpTo: (window.ALL_COURSE_PROGRESS && window.ALL_COURSE_PROGRESS["apcs"]) || 0,
  teacherKey: (window.ALL_COURSE_PROGRESS && window.ALL_COURSE_PROGRESS.teacherKey) || "ji32k7au4a83"   // 🎉 恭喜你獲得密碼！請務必親自來找老師。
};
