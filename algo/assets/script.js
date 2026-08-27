/* ===========================================================
   資訊科技課程網站  共用腳本
   =========================================================== */
(function () {
  "use strict";

  window.setConvBase = function (btn, base) {
    document.getElementById("conv-base").value = base;
    btn.parentElement.querySelectorAll(".base-btn").forEach(function (b) { b.classList.remove("active"); });
    btn.classList.add("active");
    window.convertBase();
  };

  window.pvStep = function (el) {
    var mx = +el.getAttribute("data-max");
    var s = (+el.getAttribute("data-step")) + 1; if (s > mx) s = 0;
    el.setAttribute("data-step", s);
    el.querySelectorAll("[data-lit]").forEach(function (sp) {
      var steps = sp.getAttribute("data-lit").split(" ");
      if (steps.indexOf(String(s)) >= 0) sp.classList.add("pv-lit"); else sp.classList.remove("pv-lit");
    });
    var h = el.querySelector(".pv-hint");
    if (h) h.textContent = s === 0 ? "👆 點一下逐步講解" : ("步驟 " + s + " / " + mx + "（再點繼續）");
  };

  window.toggleFlow = function (wrap) { wrap.classList.toggle("on"); };

  window.toggleDuplex = function (wrap) {
    var ab = wrap.querySelector(".hd-ab"), ba = wrap.querySelector(".hd-ba"), cap = wrap.querySelector(".hd-cap");
    if (!ab || !ba) return;
    if (!ab.classList.contains("dim")) { ab.classList.add("dim"); ba.classList.remove("dim"); if (cap) cap.textContent = "半雙工：現在 B \u2192 A 傳送中"; }
    else { ba.classList.add("dim"); ab.classList.remove("dim"); if (cap) cap.textContent = "半雙工：現在 A \u2192 B 傳送中"; }
  };

  /* ---------- 深/淺色切換 ---------- */
  // 為符合平台限制不使用 localStorage；預設淺色，單頁內切換。
  window.toggleTheme = function () {
    var html = document.documentElement;
    var cur = html.getAttribute("data-theme") === "dark" ? "dark" : "light";
    var next = cur === "dark" ? "light" : "dark";
    html.setAttribute("data-theme", next);
    var btn = document.querySelector(".theme-toggle");
    if (btn) btn.textContent = next === "dark" ? "☀️" : "🌙";
  };

  /* ---------- 極簡 Python / 通用語法上色 ---------- */
  var PY_KW = ["False","None","True","and","as","assert","async","await","break","class",
    "continue","def","del","elif","else","except","finally","for","from","global","if",
    "import","in","is","lambda","nonlocal","not","or","pass","raise","return","try","while",
    "with","yield","match","case"];
  var PY_BI = ["print","input","int","float","str","bool","len","range","list","dict","set",
    "tuple","abs","sum","max","min","round","type","sorted","enumerate","zip","map","filter",
    "format","open","chr","ord","bin","hex","oct","pow","divmod"];

  function escapeHtml(s) {
    return s.replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;");
  }

  function highlightPython(raw) {
    var lines = raw.split("\n");
    return lines.map(function (line) {
      // 註解
      var comment = "";
      var hashIdx = findCommentIndex(line);
      if (hashIdx > -1) {
        comment = '<span class="tok-com">' + escapeHtml(line.slice(hashIdx)) + "</span>";
        line = line.slice(0, hashIdx);
      }
      var out = "";
      // 依 token 掃描：字串、數字、單字
      var re = /("""[\s\S]*?"""|'''[\s\S]*?'''|"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|\b0[xXoObB][0-9A-Fa-f_]+\b|\b\d+\.?\d*\b|[A-Za-z_]\w*|\s+|[^\sA-Za-z_0-9])/g;
      var m;
      var prevWord = "";
      while ((m = re.exec(line)) !== null) {
        var t = m[0];
        if (/^['"]/.test(t)) {
          out += '<span class="tok-str">' + escapeHtml(t) + "</span>";
        } else if (/^\d/.test(t)) {
          out += '<span class="tok-num">' + escapeHtml(t) + "</span>";
        } else if (/^[A-Za-z_]\w*$/.test(t)) {
          if (PY_KW.indexOf(t) > -1) out += '<span class="tok-kw">' + t + "</span>";
          else if (PY_BI.indexOf(t) > -1) out += '<span class="tok-bi">' + t + "</span>";
          else if (prevWord === "def" || prevWord === "class") out += '<span class="tok-fn">' + t + "</span>";
          else out += escapeHtml(t);
          prevWord = t;
        } else if (/^\s+$/.test(t)) {
          out += t;
        } else {
          out += '<span class="tok-op">' + escapeHtml(t) + "</span>";
        }
        if (!/^\s+$/.test(t) && !/^[A-Za-z_]/.test(t)) prevWord = "";
      }
      return out + comment;
    }).join("\n");
  }
  function findCommentIndex(line) {
    var inStr = false, q = "";
    for (var i = 0; i < line.length; i++) {
      var c = line[i];
      if (inStr) { if (c === q && line[i-1] !== "\\") inStr = false; }
      else { if (c === '"' || c === "'") { inStr = true; q = c; } else if (c === "#") return i; }
    }
    return -1;
  }

  /* ---------- 建構所有 .code-card ---------- */
  function initCodeBlocks() {
    document.querySelectorAll("pre code[data-lang]").forEach(function (codeEl) {
      var raw = codeEl.textContent.replace(/\s+$/, "");
      codeEl.setAttribute("data-raw", raw);
      var lang = codeEl.getAttribute("data-lang");
      if (lang === "python") {
        codeEl.innerHTML = highlightPython(raw);
      } else {
        codeEl.innerHTML = escapeHtml(raw);
      }
    });
  }

  /* ---------- 語言切換（預設 Python，可切換 C++）---------- */
  window.switchLang = function (btn, lang) {
    var card = btn.closest(".code-card");
    card.querySelectorAll(".lang-btn").forEach(function (b) { b.classList.remove("active"); });
    btn.classList.add("active");
    card.querySelectorAll(".lang-pane").forEach(function (p) { p.classList.remove("show"); });
    var pane = card.querySelector(".lang-pane.lang-" + lang);
    if (pane) pane.classList.add("show");
    var out = card.querySelector(".code-output");
    if (out) { out.classList.remove("show"); out.innerHTML = ""; }
  };

  /* ---------- 複製按鈕（會找目前顯示中的那個語言分頁） ---------- */
  window.copyCode = function (btn) {
    var card = btn.closest(".code-card");
    var code = card.querySelector(".lang-pane.show code") || card.querySelector("code");
    var text = code.getAttribute("data-raw") || code.textContent;
    var done = function () {
      var old = btn.innerHTML;
      btn.classList.add("copied");
      btn.innerHTML = "✓ 已複製";
      setTimeout(function () { btn.classList.remove("copied"); btn.innerHTML = old; }, 1600);
    };
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(text).then(done, function () { fallbackCopy(text, done); });
    } else { fallbackCopy(text, done); }
  };
  function fallbackCopy(text, cb) {
    var ta = document.createElement("textarea");
    ta.value = text; ta.style.position = "fixed"; ta.style.opacity = "0";
    document.body.appendChild(ta); ta.select();
    try { document.execCommand("copy"); } catch (e) {}
    document.body.removeChild(ta); cb();
  }

  /* ---------- 進位轉換器 ---------- */
  window.convertBase = function () {
    var val = document.getElementById("conv-input").value.trim();
    var base = parseInt(document.getElementById("conv-base").value, 10);
    var err = document.getElementById("conv-err");
    var box = document.getElementById("conv-out");
    err.textContent = "";
    if (val === "") { box.style.visibility = "hidden"; return; }
    var valid = { 2: /^[01]+$/, 8: /^[0-7]+$/, 10: /^[0-9]+$/, 16: /^[0-9a-fA-F]+$/ };
    if (!valid[base].test(val)) {
      err.textContent = "⚠ 「" + val + "」不是合法的 " + baseName(base) + "數字。";
      box.style.visibility = "hidden";
      return;
    }
    var dec = parseInt(val, base);
    box.style.visibility = "visible";
    document.getElementById("out-2").textContent = dec.toString(2);
    document.getElementById("out-8").textContent = dec.toString(8);
    document.getElementById("out-10").textContent = dec.toString(10);
    document.getElementById("out-16").textContent = dec.toString(16).toUpperCase();
  };
  function baseName(b){ return {2:"二進位",8:"八進位",10:"十進位",16:"十六進位"}[b]; }

  /* ---------- 邏輯閘互動 ---------- */
  var gateState = { a: 0, b: 0, gate: "AND" };
  var GATES = {
    AND:  function (a, b) { return a & b; },
    OR:   function (a, b) { return a | b; },
    XOR:  function (a, b) { return a ^ b; },
    NAND: function (a, b) { return (a & b) ? 0 : 1; },
    NOR:  function (a, b) { return (a | b) ? 0 : 1; },
    NOT:  function (a) { return a ? 0 : 1; }
  };
  window.setGate = function (g, btn) {
    gateState.gate = g;
    document.querySelectorAll(".gate-btns button").forEach(function (x) { x.classList.remove("active"); });
    btn.classList.add("active");
    var bWrap = document.getElementById("sw-b-wrap");
    if (bWrap) bWrap.style.display = (g === "NOT") ? "none" : "";
    updateGate();
  };
  window.flipSwitch = function (which) {
    gateState[which] = gateState[which] ? 0 : 1;
    var t = document.getElementById("sw-" + which);
    t.classList.toggle("on", !!gateState[which]);
    var v = document.getElementById("val-" + which);
    if (v) { v.textContent = gateState[which]; v.classList.toggle("hi", !!gateState[which]); }
    updateGate();
  };
  function updateGate() {
    var g = gateState.gate, a = gateState.a, b = gateState.b;
    var res = (g === "NOT") ? GATES.NOT(a) : GATES[g](a, b);
    var eq = document.getElementById("gate-eq");
    var outEl = document.getElementById("gate-out");
    if (!eq || !outEl) return;
    eq.textContent = (g === "NOT") ? ("NOT " + a + " =") : (a + " " + g + " " + b + " =");
    outEl.textContent = res;
    outEl.className = "out " + (res ? "v1" : "v0");
  }
  window.__initGate = function () {
    var b = document.querySelector(".gate-btns button");
    if (b) { b.classList.add("active"); updateGate(); }
  };

  /* ---------- 練習題答案顯示 ---------- */
  window.toggleAnswer = function (el) {
    var ans = el.nextElementSibling;
    var open = ans.classList.toggle("show");
    el.innerHTML = open ? "🔽 收合解答" : "▶ 顯示解答";
  };

  /* 保留自訂標題的收合（只切換箭頭，不覆蓋文字） */
  window.toggleWork = function (el) {
    var ans = el.nextElementSibling;
    var open = ans.classList.toggle("show");
    var arrow = el.querySelector(".wk-arrow");
    if (arrow) arrow.textContent = open ? "🔽" : "▶";
  };

  /* ---------- 可點擊揭示表格 ---------- */
  window.revealCell = function (td) {
    td.classList.add("shown");
    syncRevealBtn(td.closest(".reveal-table-wrap"));
  };
  window.revealAll = function (btn) {
    var wrap = btn.closest(".reveal-table-wrap");
    var cells = wrap.querySelectorAll("td.hide-cell");
    var anyHidden = wrap.querySelector("td.hide-cell:not(.shown)") !== null;
    cells.forEach(function (c) { c.classList.toggle("shown", anyHidden); });
    btn.textContent = anyHidden ? "🙈 全部收合" : "👁️ 一鍵全開";
  };
  function syncRevealBtn(wrap) {
    if (!wrap) return;
    var btn = wrap.querySelector(".reveal-all-btn");
    if (!btn) return;
    var anyHidden = wrap.querySelector("td.hide-cell:not(.shown)") !== null;
    btn.textContent = anyHidden ? "👁️ 一鍵全開" : "🙈 全部收合";
  }

  /* ---------- 組裝估價器 ---------- */
  function estRows() { return document.querySelectorAll("#est-body tr"); }
  function estPrice(tr, sel) {
    var el = tr.querySelector(sel || ".est-price");
    return el ? (parseFloat((el.value || "0").toString().replace(/,/g, "")) || 0) : 0;
  }
  window.estCalc = function () {
    var sum = 0, now = 0, n = 0;
    estRows().forEach(function (tr) {
      var chk = tr.querySelector(".est-inc");
      if (chk && chk.checked) { sum += estPrice(tr, ".est-price"); now += estPrice(tr, ".est-now"); n++; }
    });
    var s = document.getElementById("est-sum"); if (s) s.textContent = sum.toLocaleString();
    var ns = document.getElementById("est-now-sum"); if (ns) ns.textContent = now.toLocaleString();
    var c = document.getElementById("est-count"); if (c) c.textContent = n;
    var d = document.getElementById("est-diff");
    if (d) {
      if (now === 0) { d.textContent = "（請先填現在價）"; d.style.color = "var(--text-faint)"; }
      else {
        var diff = now - sum;
        d.textContent = (diff > 0 ? "+" : "") + diff.toLocaleString() + " 元" + (diff > 0 ? "（變貴）" : diff < 0 ? "（變便宜）" : "（一樣）");
        d.style.color = diff > 0 ? "var(--danger)" : diff < 0 ? "var(--ok)" : "var(--text-soft)";
      }
    }
  };
  window.estAddRow = function () {
    var tb = document.getElementById("est-body");
    if (!tb) return;
    var tr = document.createElement("tr");
    tr.innerHTML =
      '<td><input type="checkbox" class="est-inc" checked onchange="estCalc()"></td>' +
      '<td><input class="est-cat" placeholder="類別"></td>' +
      '<td><input class="est-name" placeholder="品項／規格"></td>' +
      '<td class="est-pcell"><input type="number" class="est-price" value="0" oninput="estCalc()"> 元</td>' +
      '<td class="est-pcell"><input type="number" class="est-now" value="0" oninput="estCalc()"> 元</td>' +
      '<td><button class="est-del" onclick="estDel(this)" title="刪除">✕</button></td>';
    tb.appendChild(tr);
  };
  window.estDel = function (btn) { btn.closest("tr").remove(); window.estCalc(); };
  window.estGenSpec = function () {
    var rows = estRows(), sum = 0, nowsum = 0, body = "";
    rows.forEach(function (tr) {
      var chk = tr.querySelector(".est-inc");
      if (!chk || !chk.checked) return;
      var cat = (tr.querySelector(".est-cat").value || "").trim();
      var name = (tr.querySelector(".est-name").value || "").trim();
      var price = estPrice(tr, ".est-price"); var now = estPrice(tr, ".est-now"); sum += price; nowsum += now;
      body += "<tr><td>" + escapeHtml(cat) + "</td><td>" + escapeHtml(name) +
              "</td><td style='text-align:right'>" + price.toLocaleString() + " 元</td>" +
              "<td style='text-align:right'>" + now.toLocaleString() + " 元</td></tr>";
    });
    var diff = nowsum - sum;
    var html = '<div class="est-spec-title">📋 我的電腦規格表（一月 vs 現在）</div>' +
      '<div class="table-wrap"><table class="est-spec-table"><thead><tr><th>類別</th><th>品項／規格</th><th style="text-align:right">一月價</th><th style="text-align:right">現在價</th></tr></thead>' +
      '<tbody>' + body + '</tbody>' +
      '<tfoot><tr><td colspan="2"><strong>總計</strong></td><td style="text-align:right"><strong>' + sum.toLocaleString() + ' 元</strong></td><td style="text-align:right"><strong>' + nowsum.toLocaleString() + ' 元</strong></td></tr>' +
      '<tr><td colspan="2"><strong>價差</strong></td><td colspan="2" style="text-align:right"><strong>' + (diff>0?"+":"") + diff.toLocaleString() + ' 元' + (diff>0?"（變貴）":diff<0?"（變便宜）":"") + '</strong></td></tr></tfoot>' +
      '</table></div>';
    var out = document.getElementById("est-spec");
    if (out) { out.innerHTML = html; out.scrollIntoView({ behavior: "smooth", block: "nearest" }); }
  };

  /* ---------- 單元鎖定 / 進度解鎖 ---------- */
  function progress() {
    return window.COURSE_PROGRESS || { unlockedUpTo: 12, teacherKey: "" };
  }
  function urlParam(name) {
    var m = new RegExp("[?&]" + name + "=([^&#]*)").exec(window.location.search);
    return m ? decodeURIComponent(m[1]) : null;
  }
  function isTeacher() {
    var key = progress().teacherKey;
    return !!key && urlParam("key") === key;
  }
  // 老師模式時，顯示所有 .teacher-only 元素（學生看不到）
  function showTeacherOnly() {
    if (!isTeacher()) return;
    document.querySelectorAll(".teacher-only").forEach(function (e) {
      e.style.display = e.getAttribute("data-tdisplay") || "inline-flex";
    });
  }
  // 首頁：把超過進度的單元卡片鎖起來
  function applyLockToIndex() {
    var cards = document.querySelectorAll(".ucard[data-unit]");
    if (!cards.length) return;
    var upto = progress().unlockedUpTo || 0;
    var teacher = isTeacher();
    var keyQS = teacher ? ("?key=" + encodeURIComponent(progress().teacherKey)) : "";
    cards.forEach(function (card) {
      var no = parseInt(card.getAttribute("data-unit"), 10);
      var locked = no > upto;
      if (locked && !teacher) {
        card.classList.add("locked");
        card.setAttribute("aria-disabled", "true");
        card.removeAttribute("href");
        if (!card.querySelector(".lock-badge")) {
          var b = document.createElement("span");
          b.className = "lock-badge";
          b.textContent = "🔒";
          card.appendChild(b);
          var tip = document.createElement("span");
          tip.className = "lock-tip";
          tip.textContent = "尚未開放";
          card.appendChild(tip);
        }
        card.addEventListener("click", function (e) { e.preventDefault(); });
      } else {
        // 老師模式：讓連結帶著密鑰，點進去內頁才不會被擋
        if (teacher) {
          var href = card.getAttribute("href");
          if (href && href.indexOf("?") < 0) card.setAttribute("href", href + keyQS);
        }
        if (teacher && locked) card.classList.add("teacher-open");
      }
    });
    if (teacher) showTeacherBanner();
  }
  // 內頁：擋掉「直接打網址」進入尚未開放的單元
  function guardUnitPage() {
    var main = document.querySelector("main[data-unit]");
    if (!main) return;
    var no = parseInt(main.getAttribute("data-unit"), 10);
    var upto = progress().unlockedUpTo || 0;
    if (no <= upto || isTeacher()) {
      if (isTeacher()) { rewriteNavWithKey(); showTeacherBanner(); }
      return;
    }
    // 鎖住：以提示畫面取代內容
    document.title = "尚未開放｜" + document.title;
    main.innerHTML =
      '<div class="locked-screen">' +
      '<div class="ls-ico">🔒</div>' +
      '<h1>本單元尚未開放</h1>' +
      '<p>這個單元老師還沒上到，等課程進度到了就會開放。<br>先回課程首頁看看已開放的單元吧！</p>' +
      '<a class="btn" href="index.html">← 返回課程首頁</a>' +
      '</div>';
  }
  function rewriteNavWithKey() {
    var qs = "?key=" + encodeURIComponent(progress().teacherKey);
    document.querySelectorAll('a[href$=".html"]').forEach(function (a) {
      var href = a.getAttribute("href");
      if (href && href.indexOf("?") < 0 && /unit\d+\.html$|index\.html$/.test(href))
        a.setAttribute("href", href + qs);
    });
  }
  function showTeacherBanner() {
    if (document.querySelector(".teacher-banner")) return;
    var d = document.createElement("div");
    d.className = "teacher-banner";
    d.innerHTML = "🧑‍🏫 老師預覽模式：已解鎖全部單元（學生看到的仍是鎖住狀態）";
    document.body.appendChild(d);
  }

  /* ---------- 互動開關電路（串聯=AND、並聯=OR）---------- */
  function swRender(el) {
    var a = +el.getAttribute("data-a"), b = +el.getAttribute("data-b");
    var out = el.getAttribute("data-kind") === "series" ? (a && b ? 1 : 0) : (a || b ? 1 : 0);
    el.classList.toggle("aon", a === 1);
    el.classList.toggle("bon", b === 1);
    el.classList.toggle("lit", out === 1);
    var va = el.querySelector(".va"), vb = el.querySelector(".vb"), vo = el.querySelector(".vo");
    if (va) va.textContent = a;
    if (vb) vb.textContent = b;
    if (vo) vo.textContent = out ? "亮（1）" : "滅（0）";
  }
  function swCycle(el) {
    var a = +el.getAttribute("data-a"), b = +el.getAttribute("data-b");
    var n = ((a * 2 + b) + 1) % 4;
    el.setAttribute("data-a", (n >> 1) & 1);
    el.setAttribute("data-b", n & 1);
    swRender(el);
  }
  window.swCycle = swCycle;

  /* ---------- 燈泡二進位計數器 ---------- */
  var _bitTimers = {};
  function bitRender(id) {
    var el = document.getElementById(id); if (!el) return;
    var bits = +(el.getAttribute("data-bits") || 8);
    var max = 1 << bits;
    var v = ((+el.getAttribute("data-val")) % max + max) % max;
    el.setAttribute("data-val", v);
    var bin = v.toString(2); while (bin.length < bits) bin = "0" + bin;
    var cells = el.querySelectorAll(".bitb-cell");
    for (var i = 0; i < bits; i++) {
      var on = bin.charAt(i) === "1";
      cells[i].classList.toggle("on", on);
      cells[i].querySelector(".bitb-d").textContent = on ? "1" : "0";
    }
    el.querySelectorAll(".bv").forEach(function (s) {
      var b = s.getAttribute("data-b");
      s.textContent = b === "bin" ? bin : b === "oct" ? v.toString(8)
        : b === "hex" ? v.toString(16).toUpperCase() : "" + v;
    });
  }
  function bitStep(id, d) {
    var el = document.getElementById(id); if (!el) return;
    el.setAttribute("data-val", (+el.getAttribute("data-val")) + d);
    bitRender(id);
  }
  function bitStop(id) {
    if (_bitTimers[id]) { clearInterval(_bitTimers[id]); _bitTimers[id] = null; }
    var el = document.getElementById(id); if (!el) return;
    var pb = el.querySelector(".bitb-play");
    if (pb) { pb.classList.remove("on"); pb.textContent = "▶ 自動"; }
  }
  function bitPlay(id, btn) {
    if (_bitTimers[id]) { bitStop(id); return; }
    btn.classList.add("on"); btn.textContent = "⏸ 暫停";
    _bitTimers[id] = setInterval(function () { bitStep(id, 1); }, 550);
  }
  function bitZero(id) { bitStop(id); var el = document.getElementById(id); if (el) { el.setAttribute("data-val", 0); bitRender(id); } }
  window.bitStep = bitStep; window.bitPlay = bitPlay; window.bitZero = bitZero;

  /* ---------- 啟動 ---------- */
  document.addEventListener("DOMContentLoaded", function () {
    guardUnitPage();          // 內頁先擋，避免鎖住的內容閃現
    applyLockToIndex();
    showTeacherOnly();
    initCodeBlocks();
    if (document.querySelector(".gate-btns")) window.__initGate();
    if (document.getElementById("conv-input")) window.convertBase();
    if (document.getElementById("est-body")) window.estCalc();
    document.querySelectorAll(".swint").forEach(swRender);
    document.querySelectorAll(".bitb").forEach(function (el) { bitRender(el.id); });
  });
})();
