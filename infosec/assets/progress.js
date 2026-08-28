/* ===========================================================
   課程進度設定 —— 這一份已經改成從共用總表讀取！
   ===========================================================
   真正的數字現在統一寫在 ../shared/core/progress.js（五科同一份），
   老師要調整進度，直接改那個檔案裡「infosec」後面的數字就好，
   這裡不用再手動改。

   如果你只想讓「這一科」自己控制進度、不要跟著共用總表一起變動，
   把下面 unlockedUpTo 那一行改成直接寫死的數字（例如 unlockedUpTo: 5,），
   這一科就會脫鉤，不再受 shared/core/progress.js 影響。

   要預覽全部單元，在網址後加上 ?key=你的密鑰（例如 index.html?key=ji32k7au4a83）。
   =========================================================== */
window.COURSE_PROGRESS = {
  unlockedUpTo: (window.ALL_COURSE_PROGRESS && window.ALL_COURSE_PROGRESS["infosec"]) || 0,
  teacherKey: (window.ALL_COURSE_PROGRESS && window.ALL_COURSE_PROGRESS.teacherKey) || "ji32k7au4a83"
};
