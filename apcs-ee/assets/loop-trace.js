/* ===========================================================
   巢狀迴圈逐步追蹤動畫
   頁面上放 <div class="lt" data-lt-outer="3" data-lt-inner="3"></div>
   就會產生一個「點一下走一步」的追蹤器：
     for i in range(1, outer+1):
         for j in range(1, inner+1):
             print(f"({i},{j})", end=" ")
         print()
   =========================================================== */
(function () {
  function build(box) {
    var N = parseInt(box.getAttribute("data-lt-outer") || "3", 10);
    var M = parseInt(box.getAttribute("data-lt-inner") || "3", 10);
    var code = [
      "for i in range(1, " + (N + 1) + "):",
      "    for j in range(1, " + (M + 1) + "):",
      "        print(f\"({i},{j})\", end=\" \")",
      "    print()"
    ];

    // 產生每一步的狀態
    var steps = [{ line: -1, i: "—", j: "—", out: "", add: "", cnt: 0,
      cap: "按「下一步」開始。黃色那一行是「現在正要執行」的程式碼，右邊會即時顯示變數和印出的結果。" }];
    var out = "", cnt = 0, jv = "—";
    for (var i = 1; i <= N; i++) {
      steps.push({ line: 0, i: i, j: jv, out: out, add: "", cnt: cnt, chg: "i",
        cap: "外層迴圈：i = " + i + "。接下來內層迴圈會把 j 從 1 跑到 " + M + "，整圈跑完才會回到外層。" });
      for (var j = 1; j <= M; j++) {
        jv = j;
        steps.push({ line: 1, i: i, j: j, out: out, add: "", cnt: cnt, chg: "j",
          cap: "內層迴圈：j = " + j + "（i 還是 " + i + "，外層在等內層跑完）。" });
        var piece = "(" + i + "," + j + ") ";
        out += piece; cnt++;
        steps.push({ line: 2, i: i, j: j, out: out, add: piece, cnt: cnt, chg: "cnt",
          cap: "印出 (" + i + "," + j + ")，因為 end=\" \"，所以不換行、只補一個空白。內層的 print 已經執行 " + cnt + " 次。" });
      }
      out += "\n";
      steps.push({ line: 3, i: i, j: jv, out: out, add: "\n", cnt: cnt,
        cap: "內層跑完 " + M + " 次了，這行 print() 只負責換行。接著回到外層，看 i 還能不能再往下跑。" });
    }
    steps.push({ line: -1, i: N, j: jv, out: out, add: "", cnt: cnt,
      cap: "外層跑完 " + N + " 次，程式結束。內層的 print 一共執行了 " + N + " × " + M + " ＝ " + (N * M) + " 次：外層幾次 × 內層幾次。" });

    box.innerHTML =
      '<div class="lt-grid">' +
        '<pre class="lt-code" aria-label="程式碼">' + code.map(function (c, k) {
          return '<span class="lt-line" data-ln="' + k + '"><span class="ln">' + (k + 1) + '</span>' + esc(c) + '</span>';
        }).join("") + '</pre>' +
        '<div class="lt-side">' +
          '<div class="lt-vars">' +
            '<div class="lt-var" data-v="i"><b>i（外層）</b><span>—</span></div>' +
            '<div class="lt-var" data-v="j"><b>j（內層）</b><span>—</span></div>' +
            '<div class="lt-var" data-v="cnt"><b>print 次數</b><span>0</span></div>' +
          '</div>' +
          '<div><div class="lt-out-label">執行結果</div><div class="lt-out" aria-live="polite"></div></div>' +
        '</div>' +
      '</div>' +
      '<div class="lt-cap" aria-live="polite"></div>' +
      '<div class="lt-ctrl">' +
        '<button type="button" class="lt-btn primary" data-a="next">▶ 下一步</button>' +
        '<button type="button" class="lt-btn" data-a="play">⏩ 自動播放</button>' +
        '<button type="button" class="lt-btn" data-a="prev">◀ 上一步</button>' +
        '<button type="button" class="lt-btn" data-a="reset">↺ 重來</button>' +
        '<span class="lt-step"></span>' +
      '</div>';

    var k = 0, timer = null;
    var lines = box.querySelectorAll(".lt-line");
    var vI = box.querySelector('[data-v="i"]'), vJ = box.querySelector('[data-v="j"]'), vC = box.querySelector('[data-v="cnt"]');
    var outEl = box.querySelector(".lt-out"), cap = box.querySelector(".lt-cap"), stepEl = box.querySelector(".lt-step");
    var bNext = box.querySelector('[data-a="next"]'), bPrev = box.querySelector('[data-a="prev"]'), bPlay = box.querySelector('[data-a="play"]');

    function render(animate) {
      var s = steps[k];
      lines.forEach(function (l, n) { l.classList.toggle("on", n === s.line); });
      setVar(vI, s.i, animate && s.chg === "i");
      setVar(vJ, s.j, animate && s.chg === "j");
      setVar(vC, s.cnt, animate && s.chg === "cnt");
      if (animate && s.add && s.add !== "\n") {
        outEl.innerHTML = esc(s.out.slice(0, s.out.length - s.add.length)) + '<span class="new">' + esc(s.add) + '</span>';
      } else {
        outEl.textContent = s.out;
      }
      cap.textContent = s.cap;
      stepEl.textContent = "步驟 " + k + " / " + (steps.length - 1);
      bNext.disabled = k >= steps.length - 1;
      bPrev.disabled = k <= 0;
    }
    function setVar(el, v, changed) {
      el.querySelector("span").textContent = v;
      el.classList.remove("changed");
      if (changed) { void el.offsetWidth; el.classList.add("changed"); }
    }
    function stop() { if (timer) { clearInterval(timer); timer = null; bPlay.textContent = "⏩ 自動播放"; } }

    box.querySelector(".lt-ctrl").addEventListener("click", function (e) {
      var b = e.target.closest("[data-a]"); if (!b) return;
      var a = b.getAttribute("data-a");
      if (a === "next" && k < steps.length - 1) { stop(); k++; render(true); }
      else if (a === "prev" && k > 0) { stop(); k--; render(false); }
      else if (a === "reset") { stop(); k = 0; render(false); }
      else if (a === "play") {
        if (timer) { stop(); return; }
        if (k >= steps.length - 1) k = 0;
        bPlay.textContent = "⏸ 暫停";
        timer = setInterval(function () {
          if (k >= steps.length - 1) { stop(); return; }
          k++; render(true);
        }, 900);
      }
    });
    render(false);
  }
  function esc(s) { return String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;"); }
  function init() { document.querySelectorAll(".lt[data-lt-outer]").forEach(build); }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init); else init();
})();
