/* 線上識讀模擬考：用密碼解開題目，計時作答，交卷後計分（僅供參考） */
(function () {
  "use strict";
  var KEY = "apcsee-mock-v1";
  var LIMIT = 90 * 60 * 1000;
  var $ = function (id) { return document.getElementById(id); };
  var data = null, state = null, tick = null;

  function load() {
    try { return JSON.parse(localStorage.getItem(KEY)) || null; } catch (e) { return null; }
  }
  function save() {
    try { localStorage.setItem(KEY, JSON.stringify(state)); } catch (e) { /* 無痕模式等情況存不了，不影響作答 */ }
  }
  function b64(s) {
    var bin = atob(s), u = new Uint8Array(bin.length);
    for (var i = 0; i < bin.length; i++) u[i] = bin.charCodeAt(i);
    return u;
  }

  async function decrypt(pw) {
    var enc = window.MOCK_ENC;
    var base = await crypto.subtle.importKey("raw", new TextEncoder().encode(pw), "PBKDF2", false, ["deriveKey"]);
    var key = await crypto.subtle.deriveKey(
      { name: "PBKDF2", salt: b64(enc.salt), iterations: enc.iter, hash: "SHA-256" },
      base, { name: "AES-GCM", length: 256 }, false, ["decrypt"]);
    var plain = await crypto.subtle.decrypt({ name: "AES-GCM", iv: b64(enc.iv) }, key, b64(enc.ct));
    return JSON.parse(new TextDecoder().decode(plain));
  }

  function show(id, on) { $(id).classList.toggle("mk-hidden", !on); }

  /* ---------- 題目 ---------- */
  function buildPaper() {
    var paper = $("mk-paper"), grid = $("mk-grid");
    paper.innerHTML = ""; grid.innerHTML = "";
    data.qs.forEach(function (item, k) {
      var q = item.q;
      var card = document.createElement("section");
      card.className = "mk-q"; card.id = "mkq" + q;
      var h = document.createElement("h3");
      h.innerHTML = "第 " + (k + 1) + " 題 <span class=\"mk-tag diff\">原題號 Q" + String(q).padStart(3, "0") + "</span><span class=\"mk-res\"></span>";
      card.appendChild(h);
      var box = document.createElement("div"); box.className = "mk-img";
      var img = document.createElement("img"); img.src = item.img; img.alt = "第 " + (k + 1) + " 題題目"; img.loading = "lazy";
      box.appendChild(img); card.appendChild(box);
      var opts = document.createElement("div"); opts.className = "mk-opts"; opts.setAttribute("role", "radiogroup");
      opts.setAttribute("aria-label", "第 " + (k + 1) + " 題的答案");
      "ABCDE".split("").forEach(function (c) {
        var lab = document.createElement("label"); lab.className = "mk-opt"; lab.dataset.c = c;
        var r = document.createElement("input"); r.type = "radio"; r.name = "q" + q; r.value = c;
        if (state.answers[q] === c) r.checked = true;
        r.addEventListener("change", function () { state.answers[q] = c; save(); refreshGrid(); });
        var sp = document.createElement("span"); sp.textContent = "(" + c + ")";
        lab.appendChild(r); lab.appendChild(sp); opts.appendChild(lab);
      });
      card.appendChild(opts);
      paper.appendChild(card);

      var cell = document.createElement("button");
      cell.type = "button"; cell.className = "mk-cell"; cell.textContent = k + 1; cell.dataset.q = q;
      cell.title = "跳到第 " + (k + 1) + " 題";
      cell.addEventListener("click", function () { $("mkq" + q).scrollIntoView({ behavior: "smooth", block: "start" }); });
      grid.appendChild(cell);
    });
    refreshGrid();
  }

  function answeredCount() {
    return data.qs.filter(function (it) { return state.answers[it.q]; }).length;
  }
  function refreshGrid() {
    var n = answeredCount();
    $("mk-count").textContent = state.done ? "已交卷" : "已作答 " + n + "／" + data.qs.length;
    Array.prototype.forEach.call($("mk-grid").children, function (cell) {
      var q = cell.dataset.q;
      cell.classList.remove("done", "ok", "ng");
      if (state.done) cell.classList.add(state.answers[q] === data.ans[q] ? "ok" : "ng");
      else if (state.answers[q]) cell.classList.add("done");
    });
  }

  /* ---------- 計時 ---------- */
  function fmt(ms) {
    var s = Math.max(0, Math.ceil(ms / 1000));
    return String(Math.floor(s / 60)).padStart(2, "0") + ":" + String(s % 60).padStart(2, "0");
  }
  function runTimer() {
    clearInterval(tick);
    var t = $("mk-timer");
    function step() {
      var left = state.start + LIMIT - Date.now();
      t.textContent = fmt(left);
      t.classList.toggle("low", left < 10 * 60 * 1000);
      if (left <= 0) { clearInterval(tick); finish(true); }
    }
    step(); tick = setInterval(step, 1000);
  }

  function placeBar() {
    var head = document.querySelector(".topbar");
    $("mk-bar").style.top = ((head ? head.offsetHeight : 0) + 8) + "px";
  }

  /* ---------- 流程 ---------- */
  function startExam() {
    if (!state.start) {
      state.start = Date.now();
      state.seat = $("mk-seat").value.trim();
      state.name = $("mk-name").value.trim();
      save();
    }
    show("mk-intro", false); show("mk-bar", true); show("mk-paper", true);
    placeBar(); buildPaper(); runTimer();
  }

  function askSubmit() {
    var miss = data.qs.length - answeredCount();
    $("mk-modal-msg").textContent = miss ? "還有 " + miss + " 題沒有作答，交卷之後就不能再改。" : "30 題都作答了，交卷之後就不能再改。";
    show("mk-modal", true); $("mk-yes").focus();
  }

  function level(score) {
    if (score >= 90) return 5;
    if (score >= 70) return 4;
    if (score >= 50) return 3;
    if (score >= 30) return 2;
    return 1;
  }

  function finish(timeout) {
    clearInterval(tick);
    if (!state.done) {
      state.done = true; state.end = Math.min(Date.now(), state.start + LIMIT); save();
    }
    show("mk-modal", false);
    $("mk-timer").textContent = timeout ? "時間到" : "已交卷";
    markPaper(); refreshGrid(); renderResult();
    show("mk-result", true);
    $("mk-result").scrollIntoView({ behavior: "smooth" });
  }

  function markPaper() {
    data.qs.forEach(function (it) {
      var q = it.q, right = data.ans[q], mine = state.answers[q];
      var card = $("mkq" + q);
      card.querySelectorAll("input").forEach(function (r) { r.disabled = true; });
      card.querySelectorAll(".mk-opt").forEach(function (l) { l.classList.toggle("correct", l.dataset.c === right); });
      card.querySelector(".mk-res").innerHTML = (mine === right ? "<span class=\"mk-tag ok\">✓ 答對</span>" :
        "<span class=\"mk-tag ng\">✗ " + (mine ? "你選 " + mine : "沒作答") + "，正確答案 " + right + "</span>") +
        " <span class=\"mk-tag diff\">難度：" + it.d + "</span>";
    });
  }

  function renderResult() {
    var total = data.qs.length, right = 0, by = { "易": [0, 0], "中": [0, 0], "難": [0, 0] };
    data.qs.forEach(function (it) {
      var ok = state.answers[it.q] === data.ans[it.q];
      if (ok) right++;
      by[it.d][1]++; if (ok) by[it.d][0]++;
    });
    var score = Math.round(right / total * 100);
    var used = state.end && state.start ? fmt(state.end - state.start) : "—";
    var who = [state.seat, state.name].filter(Boolean).join("　");
    $("mk-score").innerHTML =
      (who ? "<p><strong>" + who.replace(/[<>&]/g, "") + "</strong></p>" : "") +
      "<div class=\"mk-scorebox\">" +
      "<div class=\"tile\"><div class=\"big\">" + right + " / " + total + "</div><div class=\"lbl\">答對題數</div></div>" +
      "<div class=\"tile\"><div class=\"big\">" + score + "</div><div class=\"lbl\">換算分數（滿分 100）</div></div>" +
      "<div class=\"tile\"><div class=\"big\">約 " + level(score) + " 級分</div><div class=\"lbl\">對照官方級分區間，僅供參考</div></div>" +
      "<div class=\"tile\"><div class=\"big\">" + used + "</div><div class=\"lbl\">作答時間</div></div></div>" +
      "<p>易：答對 " + by["易"][0] + "／" + by["易"][1] + "　中：答對 " + by["中"][0] + "／" + by["中"][1] +
      "　難：答對 " + by["難"][0] + "／" + by["難"][1] + "。目標 4 級分約是答對 21 題以上。</p>";
    var rows = data.qs.map(function (it, k) {
      var mine = state.answers[it.q] || "—", ok = mine === data.ans[it.q];
      return "<tr><td>" + (k + 1) + "</td><td>Q" + String(it.q).padStart(3, "0") + "</td><td>" + it.d + "</td><td>" + mine +
        "</td><td>" + data.ans[it.q] + "</td><td>" + (ok ? "<span class=\"mk-tag ok\">✓</span>" : "<span class=\"mk-tag ng\">✗</span>") + "</td></tr>";
    }).join("");
    $("mk-table").innerHTML = "<div class=\"table-wrap\"><table class=\"center\"><thead><tr><th>題</th><th>原題號</th><th>難度</th><th>你的答案</th><th>正確答案</th><th>對錯</th></tr></thead><tbody>" + rows + "</tbody></table></div>";
  }

  function reset() {
    try { localStorage.removeItem(KEY); } catch (e) { /* ignore */ }
    state = { answers: {} };
    show("mk-result", false); show("mk-bar", false); show("mk-paper", false); show("mk-intro", true);
    $("mk-timer").textContent = "90:00";
    window.scrollTo(0, 0);
  }

  function afterUnlock() {
    show("mk-gate", false);
    state = load() || { answers: {} };
    if (!state.answers) state.answers = {};
    if (state.start) {           // 重新整理後接著作答
      startExam();
      if (state.done || Date.now() > state.start + LIMIT) finish(!state.done);
    } else {
      $("mk-seat").value = state.seat || ""; $("mk-name").value = state.name || "";
      show("mk-intro", true);
    }
  }

  document.addEventListener("DOMContentLoaded", function () {
    if (!window.MOCK_ENC) { $("mk-pw-msg").textContent = "找不到題目資料（assets/mock-data.js）。"; return; }
    if (!(window.crypto && crypto.subtle)) { $("mk-pw-msg").textContent = "這個瀏覽器不支援解密，請改用 Chrome 或 Edge。"; return; }
    $("mk-pw-form").addEventListener("submit", async function (ev) {
      ev.preventDefault();
      var msg = $("mk-pw-msg"); msg.textContent = "解鎖中…";
      try { data = await decrypt($("mk-pw").value); msg.textContent = ""; afterUnlock(); }
      catch (e) { msg.textContent = "密碼不正確，請再確認一次。"; }
    });
    $("mk-start").addEventListener("click", startExam);
    $("mk-submit").addEventListener("click", askSubmit);
    $("mk-yes").addEventListener("click", function () { finish(false); });
    $("mk-no").addEventListener("click", function () { show("mk-modal", false); });
    $("mk-review").addEventListener("click", function () { $("mk-paper").scrollIntoView({ behavior: "smooth" }); });
    $("mk-reset").addEventListener("click", reset);
    document.addEventListener("keydown", function (e) { if (e.key === "Escape") show("mk-modal", false); });
    window.addEventListener("resize", function () { if (!$("mk-bar").classList.contains("mk-hidden")) placeBar(); });
  });
})();
