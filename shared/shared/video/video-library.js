/* ============================================================
   共用影片瀏覽區 — 篩選／搜尋引擎（各科通用）
   來源：高一資訊科技 video-library.html 抽出
   只依賴 .chip / .sec[data-b] / tbody tr 這些通用的 class／屬性，
   不含任何一科的影片資料，可以直接被四科共用。
   ============================================================ */
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
