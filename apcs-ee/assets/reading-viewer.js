/* ===========================================================
   程式識讀範例題 檢視器 ＋ 函式統整表搜尋
   - 任何 <button class="qchip" data-q="11"> 點下去，會跳出第 11 題的題目圖片
   - 題目圖片預設「隱藏官方答案」（紅字已轉成黑字），老師可按「顯示答案」切換
   - 「開啟 PDF 原檔」會在新分頁打開官方 PDF 並跳到該題所在頁（#page=N）
   - 題目圖片放在 assets/reading/qNN.webp（無答案）、qNN-ans.webp（含答案）
   =========================================================== */
(function () {
  var PDF = "assets/reading/apcs-reading-sample-python.pdf";

  // 題號 → [PDF 頁碼, 主題]
  var Q = {
    1: [1, "遞迴：依條件分支的回傳值"],
    2: [1, "迴圈：while 條件填空"],
    3: [1, "遞迴：依回傳值反推參數"],
    4: [2, "佇列：head／tail 模擬"],
    5: [3, "迴圈：印星號圖形除錯"],
    6: [4, "搜尋：循序 vs 二分的執行次數"],
    7: [5, "迴圈：費氏數列填空"],
    8: [6, "遞迴：兩個函式互相呼叫"],
    9: [7, "經典：輾轉相除法（迴圈）"],
    10: [8, "條件：巢狀 if 與 0 視為假"],
    11: [9, "遞迴：階乘的終止條件除錯"],
    12: [9, "迴圈：依輸出反推 while 參數"],
    13: [10, "遞迴：迴圈中呼叫遞迴函式"],
    14: [10, "遞迴：費氏數列"],
    15: [11, "串列：對稱交換兩次"],
    16: [11, "遞迴：依回傳值反推終止條件"],
    17: [12, "條件：判斷順序錯誤（除錯）"],
    18: [13, "二維串列：方向陣列"],
    19: [14, "迴圈：range 負的間隔"],
    20: [15, "運算子：% 與 // 找零"],
    21: [16, "遞迴：次方"],
    22: [16, "搜尋：二分搜尋除錯與測資"],
    23: [17, "遞迴：最大公因數 GCD"],
    24: [17, "串列：最大值與最小值"],
    25: [18, "串列：用 % 讓索引循環"],
    26: [18, "迴圈：range 的執行次數"],
    27: [19, "條件：永遠不會執行的程式碼"],
    28: [19, "複雜度：巢狀迴圈次數"],
    29: [20, "串列：設計測資找出錯誤"],
    30: [20, "串列：前綴和"]
  };
  window.READING_QUESTIONS = Q;

  var cur = 0, showAns = false, modal, img, title, topic, pdfLink, ansBtn, lastFocus;

  function pad(n) { return n < 10 ? "0" + n : "" + n; }

  function build() {
    modal = document.createElement("div");
    modal.className = "rv-backdrop";
    modal.setAttribute("role", "dialog");
    modal.setAttribute("aria-modal", "true");
    modal.innerHTML =
      '<div class="rv-panel">' +
        '<div class="rv-head">' +
          '<h3 id="rv-title"></h3><span class="rv-topic"></span><span class="spacer"></span>' +
          '<button class="rv-btn" data-act="prev" title="上一題（←）">← 上一題</button>' +
          '<button class="rv-btn" data-act="next" title="下一題（→）">下一題 →</button>' +
          '<button class="rv-btn" data-act="close" title="關閉（Esc）">✕ 關閉</button>' +
        '</div>' +
        '<div class="rv-body"><img alt=""></div>' +
        '<div class="rv-foot">' +
          '<span>來源：APCS 官方《程式識讀 題目範例（Python 題本）》</span><span class="spacer"></span>' +
          '<button class="rv-btn" data-act="ans" aria-pressed="false">顯示官方答案</button>' +
          '<a class="rv-btn" data-act="pdf" target="_blank" rel="noopener">開啟 PDF 原檔</a>' +
        '</div>' +
      '</div>';
    document.body.appendChild(modal);
    modal.setAttribute("aria-labelledby", "rv-title");
    img = modal.querySelector("img");
    title = modal.querySelector("h3");
    topic = modal.querySelector(".rv-topic");
    pdfLink = modal.querySelector('[data-act="pdf"]');
    ansBtn = modal.querySelector('[data-act="ans"]');

    modal.addEventListener("click", function (e) {
      if (e.target === modal) { close(); return; }
      var b = e.target.closest("[data-act]");
      if (!b) return;
      var act = b.getAttribute("data-act");
      if (act === "close") close();
      else if (act === "prev") show(cur > 1 ? cur - 1 : 30);
      else if (act === "next") show(cur < 30 ? cur + 1 : 1);
      else if (act === "ans") { showAns = !showAns; render(); }
    });
    document.addEventListener("keydown", function (e) {
      if (!modal.classList.contains("open")) return;
      if (e.key === "Escape") close();
      else if (e.key === "ArrowLeft") show(cur > 1 ? cur - 1 : 30);
      else if (e.key === "ArrowRight") show(cur < 30 ? cur + 1 : 1);
    });
  }

  function render() {
    var info = Q[cur];
    title.textContent = "程式識讀範例　第 " + cur + " 題";
    topic.textContent = info[1];
    img.src = "assets/reading/q" + pad(cur) + (showAns ? "-ans" : "") + ".webp";
    img.alt = "程式識讀範例第 " + cur + " 題題目" + (showAns ? "（含官方答案）" : "");
    pdfLink.href = PDF + "#page=" + info[0];
    pdfLink.textContent = "開啟 PDF 原檔（第 " + info[0] + " 頁）";
    ansBtn.textContent = showAns ? "隱藏官方答案" : "顯示官方答案";
    ansBtn.classList.toggle("on", showAns);
    ansBtn.setAttribute("aria-pressed", showAns ? "true" : "false");
  }

  function show(n) {
    if (!Q[n]) return;
    if (!modal) build();
    cur = n;
    render();
    if (!modal.classList.contains("open")) {
      lastFocus = document.activeElement;
      modal.classList.add("open");
      document.body.classList.add("rv-lock");
      modal.querySelector('[data-act="close"]').focus();
    }
    modal.scrollTop = 0;
  }

  function close() {
    modal.classList.remove("open");
    document.body.classList.remove("rv-lock");
    showAns = false;
    if (lastFocus && lastFocus.focus) lastFocus.focus();
  }

  window.openReadingQ = show;

  document.addEventListener("click", function (e) {
    var chip = e.target.closest(".qchip[data-q]");
    if (!chip) return;
    e.preventDefault();
    show(parseInt(chip.getAttribute("data-q"), 10));
  });

  // 網址帶 #q11 時，直接打開第 11 題（方便上課時直接貼連結）
  function fromHash() {
    var m = location.hash.match(/^#q(\d{1,2})$/);
    if (m) show(parseInt(m[1], 10));
  }
  window.addEventListener("hashchange", fromHash);
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", fromHash);
  else fromHash();

  /* ---------- 函式統整表：關鍵字搜尋 ---------- */
  function initSearch() {
    var box = document.querySelector(".fn-search");
    if (!box) return;
    var rows = Array.prototype.slice.call(document.querySelectorAll("table.fn tbody tr"));
    var blocks = Array.prototype.slice.call(document.querySelectorAll("section.block[data-fn-cat]"));
    var count = document.querySelector(".fn-count");
    var empty = document.querySelector(".fn-empty");
    rows.forEach(function (r) { r._t = r.textContent.toLowerCase(); });
    function apply() {
      var q = box.value.trim().toLowerCase();
      var shown = 0;
      rows.forEach(function (r) {
        var hit = !q || r._t.indexOf(q) !== -1;
        r.style.display = hit ? "" : "none";
        if (hit) shown++;
      });
      blocks.forEach(function (b) {
        var any = b.querySelector("tbody tr:not([style*='none'])");
        b.classList.toggle("fn-hide", !any);
      });
      if (count) count.textContent = q ? "找到 " + shown + " 筆" : "共 " + rows.length + " 筆";
      if (empty) empty.classList.toggle("show", shown === 0);
    }
    box.addEventListener("input", apply);
    apply();
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", initSearch);
  else initSearch();
})();
