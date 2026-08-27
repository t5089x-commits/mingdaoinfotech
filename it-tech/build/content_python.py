# -*- coding: utf-8 -*-
"""Python 篇單元 8–12 的頁面內容（範例參考明道中學 HackMD Python 基礎教學）。"""
from common import hero, goals, code_block, exercise, PROGRAMIZ

def sec(n, title, inner):
    return f'''<section class="block">
  <h2><span class="num">{n:02d}</span>{title}</h2>
  {inner}
</section>'''

def R(code, label="python"):
    # 僅提供「複製」按鈕，不含執行（上課搭配 Programiz 線上編譯器）
    return code_block(code, lang="python", label=label, runnable=False)

_CTA_NOTE = f'''<div class="callout tip"><span class="t">💻 如何執行這些程式？</span>
<p>每個範例右上角有 <strong>⧉ 複製</strong> 按鈕，點一下就能複製程式碼。上課時把它貼到頁面最下方的
<a href="{PROGRAMIZ}" target="_blank" rel="noopener"><strong>Programiz 線上 Python 編譯器</strong></a>
（免安裝、開瀏覽器就能跑）即可看到執行結果。</p></div>'''

BODIES = {}

# =====================================================================
# 單元 08：Python（一）開發環境、變數與輸入輸出
# =====================================================================
BODIES["unit08"] = hero("unit08") + goals([
    "建立並認識 Python 的開發環境",
    "認識變數、命名規則與四種基本資料型態",
    "會用 type() 查型別，並做 int／float／bool／str 型別轉換",
    "認識動態型別，以及 0o／0x 進位表示",
]) + _CTA_NOTE + sec(1, "開發環境", '''
<p>要寫 Python，你需要一個能編輯與執行程式的環境。本課程上課採用<strong>免安裝的線上編譯器</strong>，方便隨開隨用：</p>
<div class="grid cols-2">
  <div class="tile"><h4>🌐 Programiz（本課推薦）</h4><p>開瀏覽器即可寫、即可執行，免安裝。<a href="https://www.programiz.com/python-programming/online-compiler/" target="_blank" rel="noopener"><strong>點我開啟線上編譯器 ↗</strong></a></p></div>
  <div class="tile"><h4>🐍 官方 Python</h4><p>從 python.org 下載，搭配 IDLE 使用。</p></div>
</div>
<h3>你的第一支程式</h3>
''' + R('print("我是陳楷翔，大家可以叫我阿翔")\nprint("明道的阿翔開始學 Python 了！")\nprint("我最喜歡的數字是 9487")')
) + sec(2, "變數 Variable", '''
<p>變數用來<strong>存放資料</strong>，可以把它想成一個<strong>貼了名字的箱子</strong>：用指定運算子 <code>=</code> 把右邊的值放進左邊的箱子。Python 也支援一次指定多個變數。</p>
''' + R('''x = 1
print(x)

a = b = c = 20            # 一次把 20 指定給 a、b、c
age, name = 18, "陳楷翔"  # 同時指定不同的值

a = 10
print(a)
a = a + 5                 # 取出 a、加 5、再存回 a
print(a)                  # 15''') + '''
<div class="varstep" id="varstep">
  <div class="vs-stage">
      <div class="vs-boxes">
        <div class="vs-box empty" id="vs-x"><span class="vs-name">x</span><span class="vs-val"></span></div>
        <div class="vs-box empty" id="vs-a"><span class="vs-name">a</span><span class="vs-val"></span></div>
        <div class="vs-box empty" id="vs-b"><span class="vs-name">b</span><span class="vs-val"></span></div>
        <div class="vs-box empty" id="vs-c"><span class="vs-name">c</span><span class="vs-val"></span></div>
        <div class="vs-box empty wide" id="vs-age"><span class="vs-name">age</span><span class="vs-val"></span></div>
        <div class="vs-box empty wide" id="vs-name"><span class="vs-name">name</span><span class="vs-val"></span></div>
      </div>
      <div class="vs-calc" id="vs-calc"></div>
  </div>
  <div class="vs-cc"><div class="vs-srccard">
    <div class="vs-srchead"><span class="vsdot r"></span><span class="vsdot y"></span><span class="vsdot g"></span><span class="vs-srclabel">變數.py　—　目前執行的那一行會反白</span></div>
    <div class="vs-src" id="vs-src">
      <div class="vs-ln" data-ln="0">x = 1</div>
      <div class="vs-ln" data-ln="1">print(x)</div>
      <div class="vs-ln blank"></div>
      <div class="vs-ln" data-ln="2">a = b = c = 20            # 一次把 20 指定給 a、b、c</div>
      <div class="vs-ln" data-ln="3">age, name = 18, "陳楷翔"  # 同時指定不同的值</div>
      <div class="vs-ln blank"></div>
      <div class="vs-ln" data-ln="4">a = 10</div>
      <div class="vs-ln" data-ln="5">print(a)</div>
      <div class="vs-ln" data-ln="6">a = a + 5                 # 取出 a、加 5、再存回 a</div>
      <div class="vs-ln" data-ln="7">print(a)                  # 15</div>
    </div>
  </div>
    <div class="vs-console">
      <div class="vs-console-h">🖥️ 程式輸出</div>
      <div class="vs-console-body" id="vs-out"></div>
    </div>
  </div>
  <div class="vs-cap" id="vs-cap">點下面的「下一步 ▶」，程式會一行一行執行；上面程式碼會<strong>反白</strong>目前跑到的那一行，箱子是變數，右邊會顯示 print 印出來的結果。</div>
  <div class="vs-controls">
    <button type="button" class="vs-btn" id="vs-next">下一步 ▶</button>
    <button type="button" class="vs-btn ghost" id="vs-reset">↺ 重來</button>
  </div>
</div>
<script>
(function(){
  var steps=[
    {x:"",a:"",b:"",c:"",age:"",name:"",ln:-1,calc:"",cap:"點下面的「下一步 ▶」，程式會一行一行執行；上面程式碼會反白目前跑到的那一行，箱子是變數，右邊會顯示 print 印出來的結果。",hi:[],out:[]},
    {x:"1",a:"",b:"",c:"",age:"",name:"",ln:0,calc:"",cap:"把 1 放進箱子 x。",hi:["x"],out:[]},
    {x:"1",a:"",b:"",c:"",age:"",name:"",ln:1,calc:"",cap:"print(x)：把 x 箱子裡的值印到畫面上 → 右邊輸出區出現 1。",hi:["x"],out:["1"]},
    {x:"1",a:"20",b:"20",c:"20",age:"",name:"",ln:2,calc:"",cap:"一次把 20 放進 a、b、c 三個箱子。",hi:["a","b","c"],out:["1"]},
    {x:"1",a:"20",b:"20",c:"20",age:"18",name:'"陳楷翔"',ln:3,calc:"",cap:'一次指定「不同」的值：18 放進 age、字串 "陳楷翔" 放進 name（左邊對左邊、右邊對右邊，一次配好兩個箱子）。',hi:["age","name"],out:["1"]},
    {x:"1",a:"10",b:"20",c:"20",age:"18",name:'"陳楷翔"',ln:4,calc:"",cap:"重新指定：把 10 放進 a，直接蓋掉原本的 20 → a 變成 10。",hi:["a"],out:["1"]},
    {x:"1",a:"10",b:"20",c:"20",age:"18",name:'"陳楷翔"',ln:5,calc:"",cap:"print(a)：印出 a 現在的值 → 右邊輸出區出現 10。",hi:["a"],out:["1","10"]},
    {x:"1",a:"10",b:"20",c:"20",age:"18",name:'"陳楷翔"',ln:6,calc:"取出 a 現在的值 → 10",cap:"a = a + 5 第 1 步：先把 a 現在的值「取出來」，是 10。",hi:["a"],out:["1","10"]},
    {x:"1",a:"10",b:"20",c:"20",age:"18",name:'"陳楷翔"',ln:6,calc:"10（原本的）＋ 5（現在的）＝ 15",cap:"第 2 步：拿原本的 10，加上現在的 5，算出 15。",hi:[],out:["1","10"]},
    {x:"1",a:"15",b:"20",c:"20",age:"18",name:'"陳楷翔"',ln:6,calc:"把 15 存回 a",cap:"第 3 步：把 15 存回箱子 a → a 變成 15。",hi:["a"],out:["1","10"]},
    {x:"1",a:"15",b:"20",c:"20",age:"18",name:'"陳楷翔"',ln:7,calc:"",cap:"print(a)：再印一次 a → 右邊輸出區出現 15。程式跑完囉！",hi:["a"],out:["1","10","15"]}
  ];
  var root=document.getElementById("varstep");
  if(!root) return;
  var i=0;
  var boxes={x:document.getElementById("vs-x"),a:document.getElementById("vs-a"),b:document.getElementById("vs-b"),c:document.getElementById("vs-c"),age:document.getElementById("vs-age"),name:document.getElementById("vs-name")};
  var vals={};for(var k in boxes){vals[k]=boxes[k].querySelector(".vs-val");}
  var calc=document.getElementById("vs-calc"),cap=document.getElementById("vs-cap"),out=document.getElementById("vs-out");
  var srclns=root.querySelectorAll(".vs-ln");
  var next=document.getElementById("vs-next"),reset=document.getElementById("vs-reset");
  function one(k,val,hi,prev){
    var b=boxes[k];vals[k].textContent=val;
    if(val===""){b.classList.add("empty");}else{b.classList.remove("empty");}
    b.classList.toggle("hi",hi);
    if(prev!==val){b.classList.remove("pop");void b.offsetWidth;b.classList.add("pop");}
  }
  function render(prev){
    var s=steps[i],p=prev!=null?steps[prev]:{x:null,a:null,b:null,c:null,age:null,name:null,out:[]};
    one("x",s.x,s.hi.indexOf("x")>=0,p.x);
    one("a",s.a,s.hi.indexOf("a")>=0,p.a);
    one("b",s.b,s.hi.indexOf("b")>=0,p.b);
    one("c",s.c,s.hi.indexOf("c")>=0,p.c);
    one("age",s.age,s.hi.indexOf("age")>=0,p.age);
    one("name",s.name,s.hi.indexOf("name")>=0,p.name);
    for(var q=0;q<srclns.length;q++){ srclns[q].classList.toggle("hi", srclns[q].getAttribute("data-ln")===String(s.ln)); }
    calc.textContent=s.calc;calc.style.visibility=s.calc?"visible":"hidden";
    cap.textContent=s.cap;
    var prevLen=(p.out||[]).length;
    out.innerHTML="";
    if(s.out.length===0){
      var ph=document.createElement("div");ph.className="vs-outph";ph.textContent="（還沒有 print 輸出）";out.appendChild(ph);
    } else {
      for(var j=0;j<s.out.length;j++){
        var line=document.createElement("div");
        line.className="vs-outline"+(j>=prevLen?" fresh":"");
        line.textContent=s.out[j];
        out.appendChild(line);
      }
    }
    next.textContent=(i>=steps.length-1)?"✓ 完成":"下一步 ▶";
    next.disabled=(i>=steps.length-1);
  }
  next.addEventListener("click",function(){if(i<steps.length-1){var pv=i;i++;render(pv);}});
  reset.addEventListener("click",function(){var pv=i;i=0;render(pv);});
  render(null);
})();
</script>
<p style="font-size:.86rem;color:var(--text-soft);margin-top:12px">💡 這段程式示範了：<strong>指定</strong>（把值放進箱子，如 <code>x = 1</code>）、<strong>重新指定</strong>（<code>a = 10</code>，蓋掉舊值）、<strong>用自己的值算新值再存回</strong>（<code>a = a + 5</code>），以及 <code>print()</code> 把箱子裡的值印到右邊的輸出區。</p>
<h3>變數命名規則</h3>
<ul>
  <li>名稱<strong>首字必須是字母、底線 <code>_</code> 或中文</strong>，其後可加數字。</li>
  <li><strong>區分大小寫</strong>：<code>age</code> 與 <code>Age</code> 是不同變數。</li>
  <li>不要使用 Python 保留字（如 <code>if</code>、<code>for</code>、<code>print</code>）當變數名。</li>
  <li>取有意義的名字，例如 <code>score</code> 比 <code>s</code> 好懂。</li>
</ul>
<p>把上面的規則對照著看，就能判斷一個名字合不合法：</p>
<div class="table-wrap"><table class="center">
<thead><tr><th>合法命名 ✅</th><th>不合法命名 ❌</th><th>為什麼不合法</th></tr></thead>
<tbody>
<tr><td><code>age</code></td><td><code>2age</code></td><td>首字不能是數字。</td></tr>
<tr><td><code>name9487</code></td><td><code>9487name</code></td><td>數字不能放在最前面。</td></tr>
<tr><td><code>_score</code></td><td><code>my score</code></td><td>名稱中間不能有空白。</td></tr>
<tr><td><code>total_price</code></td><td><code>total-price</code></td><td>不能有 <code>-</code> 等運算符號（會被當成減法）。</td></tr>
<tr><td><code>class_no</code></td><td><code>class</code></td><td>是 Python 保留字（關鍵字），不能拿來當變數名。</td></tr>
<tr><td><code>my_list</code></td><td><code>list</code></td><td><strong>與 Python 內建函式同名</strong>：<code>list</code> 本身是內建函式，拿來當變數會把它蓋掉。</td></tr>
<tr><td><code>total</code></td><td><code>print</code></td><td><strong>與 Python 內建函式同名</strong>：<code>print</code> 也是內建函式，別拿來當變數名。</td></tr>
<tr><td><code>text_str</code></td><td><code>str</code></td><td><strong>與 Python 內建函式同名</strong>：<code>str</code> 也是內建函式，別拿來當變數名。</td></tr>
</tbody></table></div>
<div class="callout"><span class="t">⚠ 特別注意「與內建函式同名」</span>
<p>像 <code>list</code>、<code>str</code>、<code>print</code>、<code>type</code>、<code>sum</code>、<code>input</code> 這些名字，Python <strong>不會報錯</strong>，程式還是能執行——但你一旦拿它們當變數名，原本的功能就被「蓋掉」了。例如寫了 <code>list = 5</code> 之後，再想用 <code>list()</code> 建立串列就會出錯。所以雖然合法，仍<strong>強烈建議避免</strong>。</p></div>
<div class="reveal" onclick="toggleWork(this)"><span class="wk-arrow">▶</span> 🧪 親眼看看「把 <code>str</code> 蓋掉」會發生什麼事（點開）</div>
<div class="answer">
<p style="margin-top:0"><code>str()</code> 本來是把東西<strong>轉成字串</strong>的內建函式。一旦你拿 <code>str</code> 當變數名，它就從「函式」變成「一個字串」，之後再呼叫 <code>str(1)</code> 就會壞掉。左右對照看看：</p>
<div class="grid cols-2">
  <div>
    <p class="cmp-h ok">✅ 正常：沒有蓋掉 str</p>
''' + R('''a = 1
print(str(1))''') + '''
    <p class="cmp-note ok">→ 印出 <code>1</code>：<code>str(1)</code> 正常把數字 1 轉成字串。</p>
  </div>
  <div>
    <p class="cmp-h bad">❌ 壞掉：str 被蓋成字串</p>
''' + R('''str = '1'
a = 1

print(str(1))''') + '''
    <p class="cmp-note bad">→ 執行錯誤 <code>TypeError: 'str' object is not callable</code>：<code>str</code> 現在是字串 <code>'1'</code>，不能再被當函式呼叫。</p>
  </div>
</div>
</div>
''') + sec(3, "資料型態 Data Type", '''
<p>Python 內建型態主要分三類，用 <code>type()</code> 可以查看某個值是什麼型別：</p>
<div class="table-wrap"><table class="center">
<thead><tr><th>分類</th><th>型別</th><th>說明</th><th>範例</th></tr></thead>
<tbody>
<tr><td rowspan="3">數值型</td><td><code>int</code> 整數</td><td>沒有小數點的整數</td><td><code>1</code>、<code>-20</code></td></tr>
<tr><td><code>float</code> 浮點數</td><td>帶小數點的數</td><td><code>1.5</code>、<code>3.14</code></td></tr>
<tr><td><code>bool</code> 布林值</td><td>只有「真／假」兩種</td><td><code>True</code>、<code>False</code></td></tr>
<tr><td>字串型</td><td><code>str</code> 字串</td><td>用引號括住的文字</td><td><code>"Hello"</code>、<code>'陳楷翔'</code></td></tr>
<tr><td rowspan="2">容器型</td><td><code>list</code> 串列</td><td>一串有順序的資料</td><td><code>[1, 2, 3]</code></td></tr>
<tr><td><code>dict</code> 字典</td><td>用「鍵 → 值」對應的資料</td><td><code>{"name": "阿翔"}</code></td></tr>
</tbody></table></div>
''' + R('''x = 1
print(x, type(x))          # int 整數

y = 1.5
print(y, type(y))          # float 浮點數

a = True
print(a, type(a))          # bool 布林值

jinsong = "Hello, 87"
print(jinsong, type(jinsong))    # str 字串''') + '''
<div class="callout"><span class="t">🔎 動態型別</span>
<p>Python 是<strong>動態型別</strong>：型態由「指派的值」決定，同一個變數之後可以改放不同型態的值，不需事先宣告。</p>
''' + R('''a = 10
print(a, type(a))     # int
a = 3.2
print(a, type(a))     # float —— 同一個 a，型別跟著「值」改變
a = "abcd狗咬豬"
print(a, type(a))     # str''') + '''</div>
<div class="reveal" onclick="toggleWork(this)"><span class="wk-arrow">▶</span> 🆚 如果換成 C++ 會怎麼寫？（點開看「靜態型別」對照）</div>
<div class="answer">
<p style="margin-top:0">像 <strong>C／C++、Java</strong> 這些語言是<strong>靜態型別</strong>：變數<strong>宣告時就要先寫死型別</strong>，之後只能放同一種型別的值。同樣「先放整數、再放小數」，C++ 得這樣寫：</p>
''' + R('''// C++（靜態型別）：宣告時就決定型別，不能亂換
int a = 10;         // a 一出生就被定成「整數」
a = 3;              // OK，還是整數
// a = 3.2;         // ✗ 會被截成 3，或依情況警告；a 永遠是 int
double b = 3.2;     // 想放小數，要另外宣告一個 double''', "C++ 靜態型別") + '''
<p style="margin-bottom:0">對照之下，Python 是<strong>動態型別</strong>：不用宣告型別，同一個變數想放什麼型別都行，型別跟著「目前的值」走。<strong>C++</strong> 比較嚴謹、執行快；<strong>Python</strong> 比較彈性、寫起來快。各有優缺點，沒有絕對好壞。</p></div>
''') + sec(4, "型別轉換 Casting", '''
<p>把一個值從一種型態轉成另一種，就叫做<strong>轉型（casting）</strong>。常用這四個函式：</p>
<div class="table-wrap"><table class="center">
<thead><tr><th>函式</th><th>作用</th><th>例子</th></tr></thead>
<tbody>
<tr><td><code>int(物件)</code></td><td>轉成<strong>整數</strong>（小數會<strong>直接捨去</strong>）</td><td><code>int(3.9)</code> → <code>3</code></td></tr>
<tr><td><code>float(物件)</code></td><td>轉成<strong>浮點數</strong></td><td><code>float(5)</code> → <code>5.0</code></td></tr>
<tr><td><code>bool(物件)</code></td><td>轉成<strong>布林值</strong></td><td><code>bool(0)</code> → <code>False</code></td></tr>
<tr><td><code>str(物件)</code></td><td>轉成<strong>字串</strong></td><td><code>str(100)</code> → <code>"100"</code></td></tr>
</tbody></table></div>
''' + R('''x = 54.87
y = int(x)          # 浮點轉整數：小數點後「直接捨去」，不是四捨五入！
print(x)            # 54.87
print(y)            # 54    （.87 被直接丟掉，不會進位成 55）
print(type(x), type(y))''') + '''
<p>💭 <strong>先自己猜猜看：</strong>下面每一行 <code>bool()</code> 會印出 <code>True</code> 還是 <code>False</code>？<strong>一題一題</strong>先想過、再點各自的「看答案」對照。</p>
<div class="quizrow"><code>print(bool(""))</code><button type="button" class="quiz-btn" onclick="var a=this.nextElementSibling;a.hidden=!a.hidden;this.textContent=a.hidden?'🤔 看答案':'🙈 收起'">🤔 看答案</button><span class="quiz-ans" hidden>→ <span class="F">False</span>：空字串（裡面完全沒有字）算 False。</span></div>
<div class="quizrow"><code>print(bool(0))</code><button type="button" class="quiz-btn" onclick="var a=this.nextElementSibling;a.hidden=!a.hidden;this.textContent=a.hidden?'🤔 看答案':'🙈 收起'">🤔 看答案</button><span class="quiz-ans" hidden>→ <span class="F">False</span>：數字 <code>0</code> 算 False。</span></div>
<div class="quizrow"><code>print(bool(None))</code><button type="button" class="quiz-btn" onclick="var a=this.nextElementSibling;a.hidden=!a.hidden;this.textContent=a.hidden?'🤔 看答案':'🙈 收起'">🤔 看答案</button><span class="quiz-ans" hidden>→ <span class="F">False</span>：<code>None</code>（代表「空值／沒有東西」）算 False。</span></div>
<div class="quizrow"><code>print(bool("False"))</code><button type="button" class="quiz-btn" onclick="var a=this.nextElementSibling;a.hidden=!a.hidden;this.textContent=a.hidden?'🤔 看答案':'🙈 收起'">🤔 看答案</button><span class="quiz-ans" hidden>→ <span class="T">True</span>：<strong>小心陷阱！</strong><code>"False"</code> 是「<strong>非空字串</strong>」，只要字串裡有字就是 True，跟裡面寫的字是不是「False」無關。</span></div>
<div class="quizrow"><code>print(bool(100))</code><button type="button" class="quiz-btn" onclick="var a=this.nextElementSibling;a.hidden=!a.hidden;this.textContent=a.hidden?'🤔 看答案':'🙈 收起'">🤔 看答案</button><span class="quiz-ans" hidden>→ <span class="T">True</span>：非 0 的數字都算 True。</span></div>
<div class="reveal" onclick="toggleWork(this)"><span class="wk-arrow">▶</span> 五題都做完了？點我看「總規則」</div>
<div class="answer">
<p style="margin:0"><strong>規則：</strong>空字串、<code>0</code>、<code>None</code>（還有空的容器，如 <code>[]</code>、<code>{}</code>）會是 <code>False</code>；<strong>其餘全部都是 <code>True</code></strong>。</p></div>
<div class="callout tip"><span class="t">🔢 進位表示</span>
<p><code>0o</code> 開頭是八進位、<code>0x</code> 開頭是十六進位、<code>0b</code> 開頭是二進位；<code>oct()</code>、<code>hex()</code>、<code>bin()</code> 可把數字轉回各進位的字串表示。</p></div>
<div class="callout"><span class="t">🔗 呼應「數字系統」單元：進位轉換有內建函式！</span>
<p>還記得「數字系統」單元手算的十進位 ↔ 二／八／十六進位嗎？Python 有<strong>內建函式</strong>可以直接轉，不用自己慢慢除：</p>
''' + R('''# 十進位 → 其他進位（回傳「字串」，含 0b／0o／0x 前綴）
print(bin(13))    # 0b1101   （13 的二進位）
print(oct(13))    # 0o15     （13 的八進位）
print(hex(255))   # 0xff     （255 的十六進位）

# 其他進位（字串）→ 十進位：int(字串, 進位)
print(int("1101", 2))   # 13
print(int("ff", 16))    # 255

# 也可以「直接用其他進位寫一個整數」，存進變數時 Python 會自動換算成十進位
a = 0o10      # 八進位的 10 → 十進位 8
b = 0x1f      # 十六進位的 1f → 十進位 31
c = 0b1010    # 二進位的 1010 → 十進位 10
print(a, b, c)   # 8 31 10''') + '''
</div>
'''
) + exercise("課堂練習", '''
<ol>
  <li>用 <code>type()</code> 查一下：<code>x = 3.14</code> 是什麼型別？<code>name = "Hi"</code> 呢？<code>flag = True</code> 呢？</li>
  <li><code>int("100")</code> 和 <code>int(3.9)</code> 各會得到什麼？（float 轉 int 是四捨五入，還是直接捨去？）</li>
  <li><code>bool("")</code>、<code>bool(0)</code>、<code>bool("False")</code> 各是 True 還是 False？</li>
</ol>''', '''
<ol>
<li><code>float</code>、<code>str</code>、<code>bool</code>。</li>
<li><code>int("100")</code> → <code>100</code>（字串轉整數）；<code>int(3.9)</code> → <code>3</code>（直接<strong>捨去</strong>小數，不是四捨五入）。</li>
<li><code>bool("")</code>＝False、<code>bool(0)</code>＝False、<code>bool("False")</code>＝<strong>True</strong>（只要是「非空字串」就是 True）。</li>
</ol>''')

# =====================================================================
# 單元 09：Python（二）選擇結構與運算子
# =====================================================================
BODIES["unit09"] = hero("unit09") + goals([
    "看懂流程圖，理解程式怎麼「判斷條件、決定走哪一條路」",
    "會用 if 撰寫單向判斷、雙向判斷（if–else）與多向判斷（if–elif–else）",
    "知道 Python 用「縮排」表示一個程式區塊",
]) + sec(1, "單向判斷 if", '''
<p>條件成立（<code>True</code>）時才執行縮排區塊；不成立就<strong>直接跳過</strong>。<strong>Python 用縮排（通常 4 個空格）表示一個程式區塊。</strong></p>
<div class="cf-row"><div class="flowwrap"><svg class="flow" viewBox="0 0 320 254" role="img" style="max-width:410px" aria-label="單向判斷 if 流程圖">
  <defs><marker id="fa1" markerWidth="9" markerHeight="9" refX="7" refY="3" orient="auto"><path d="M0,0 L7,3 L0,6 Z" fill="var(--text-faint)"/></marker></defs>
  <rect x="110" y="6" width="100" height="30" rx="15" fill="var(--surface-2)" stroke="var(--border)" stroke-width="1.4"/>
  <text x="160" y="26" text-anchor="middle" style="font-size:19px;fill:var(--text)">開始</text>
  <line x1="160" y1="36" x2="160" y2="58" stroke="var(--text-faint)" stroke-width="1.6" marker-end="url(#fa1)"/>
  <polygon points="160,60 228,95 160,130 92,95" fill="var(--warn-soft)" stroke="var(--warn)" stroke-width="1.6"/>
  <text x="160" y="92" text-anchor="middle" style="font-size:18px;fill:var(--text);font-weight:700">分數 ≥ 60 ？</text>
  <text x="160" y="108" text-anchor="middle" style="font-size:16px;fill:var(--text-soft)">條件成立？</text>
  <line x1="160" y1="130" x2="160" y2="154" stroke="var(--text-faint)" stroke-width="1.6" marker-end="url(#fa1)"/>
  <text x="150" y="147" text-anchor="end" style="font-size:17px;fill:var(--ok);font-weight:800">是</text>
  <rect x="96" y="154" width="128" height="38" rx="8" fill="var(--brand-soft)" stroke="var(--brand)" stroke-width="1.6"/>
  <text x="160" y="178" text-anchor="middle" style="font-size:18px;fill:var(--brand-strong);font-weight:700">執行縮排的程式</text>
  <line x1="160" y1="192" x2="160" y2="216" stroke="var(--text-faint)" stroke-width="1.6" marker-end="url(#fa1)"/>
  <path d="M228,95 H294 V232 H226" fill="none" stroke="var(--text-faint)" stroke-width="1.6" marker-end="url(#fa1)"/>
  <text x="250" y="88" text-anchor="middle" style="font-size:17px;fill:var(--danger);font-weight:800">否</text>
  <rect x="96" y="216" width="128" height="32" rx="8" fill="var(--surface-2)" stroke="var(--border)" stroke-width="1.4"/>
  <text x="160" y="236" text-anchor="middle" style="font-size:18px;fill:var(--text)">繼續後面的程式</text>
</svg></div>
''' + R('''score = int(input("請輸入你的分數："))
if score >= 60:
    print("恭禧你及格了！")
    print(score)

# 區間判斷
number = int(input("請輸入一個數:"))
if number >= 10 and number <= 20:
    print(f"{number}在10~20區間")''') + '''
</div>
'''
) + sec(2, "雙向判斷 if–else", '''
<p>條件成立走 <code>if</code> 區塊、不成立走 <code>else</code> 區塊——<strong>兩條路一定會走到其中一條</strong>，走完再合流繼續。</p>
<div class="cf-row"><div class="flowwrap"><svg class="flow" viewBox="0 0 360 250" role="img" style="max-width:450px" aria-label="雙向判斷 if-else 流程圖">
  <defs><marker id="fa2" markerWidth="9" markerHeight="9" refX="7" refY="3" orient="auto"><path d="M0,0 L7,3 L0,6 Z" fill="var(--text-faint)"/></marker></defs>
  <rect x="130" y="6" width="100" height="30" rx="15" fill="var(--surface-2)" stroke="var(--border)" stroke-width="1.4"/>
  <text x="180" y="26" text-anchor="middle" style="font-size:19px;fill:var(--text)">開始</text>
  <line x1="180" y1="36" x2="180" y2="56" stroke="var(--text-faint)" stroke-width="1.6" marker-end="url(#fa2)"/>
  <polygon points="180,58 248,92 180,126 112,92" fill="var(--warn-soft)" stroke="var(--warn)" stroke-width="1.6"/>
  <text x="180" y="88" text-anchor="middle" style="font-size:18px;fill:var(--text);font-weight:700">分數 ≥ 60 ？</text>
  <text x="180" y="104" text-anchor="middle" style="font-size:16px;fill:var(--text-soft)">條件成立？</text>
  <path d="M112,92 H62 V150" fill="none" stroke="var(--text-faint)" stroke-width="1.6" marker-end="url(#fa2)"/>
  <text x="80" y="84" text-anchor="middle" style="font-size:17px;fill:var(--ok);font-weight:800">是</text>
  <rect x="8" y="150" width="108" height="38" rx="8" fill="var(--brand-soft)" stroke="var(--brand)" stroke-width="1.6"/>
  <text x="62" y="173" text-anchor="middle" style="font-size:18px;fill:var(--brand-strong);font-weight:700">印「及格」</text>
  <path d="M248,92 H298 V150" fill="none" stroke="var(--text-faint)" stroke-width="1.6" marker-end="url(#fa2)"/>
  <text x="280" y="84" text-anchor="middle" style="font-size:17px;fill:var(--danger);font-weight:800">否</text>
  <rect x="244" y="150" width="108" height="38" rx="8" fill="var(--brand-soft)" stroke="var(--brand)" stroke-width="1.6"/>
  <text x="298" y="173" text-anchor="middle" style="font-size:18px;fill:var(--brand-strong);font-weight:700">印「被當了」</text>
  <path d="M62,188 V218 H126" fill="none" stroke="var(--text-faint)" stroke-width="1.6" marker-end="url(#fa2)"/>
  <path d="M298,188 V218 H234" fill="none" stroke="var(--text-faint)" stroke-width="1.6" marker-end="url(#fa2)"/>
  <rect x="126" y="204" width="108" height="30" rx="8" fill="var(--surface-2)" stroke="var(--border)" stroke-width="1.4"/>
  <text x="180" y="224" text-anchor="middle" style="font-size:18px;fill:var(--text)">繼續程式</text>
</svg></div>
''' + R('''score = int(input("請輸入你的分數："))
if score >= 60:
    print("恭禧你及格了！")
else:
    print("天啊，你被當了！")''') + '''
</div>
<h3>再看一個：判斷奇數／偶數</h3>
<p>同樣是雙向判斷：餘數（<code>%</code>）是 1 就印「奇數」，否則印「偶數」。</p>
<div class="cf-row">''' + R('''# 奇偶判斷
number = int(input("請輸入一個數:"))
if number % 2 == 1:
    print(f"{number}是奇數")
else:
    print(f"{number}是偶數")''') + '''
<div class="flowwrap"><svg class="flow" viewBox="0 0 360 250" role="img" style="max-width:450px" aria-label="奇偶判斷 if-else 流程圖">
  <defs><marker id="fa2b" markerWidth="9" markerHeight="9" refX="7" refY="3" orient="auto"><path d="M0,0 L7,3 L0,6 Z" fill="var(--text-faint)"/></marker></defs>
  <rect x="130" y="6" width="100" height="30" rx="15" fill="var(--surface-2)" stroke="var(--border)" stroke-width="1.4"/>
  <text x="180" y="26" text-anchor="middle" style="font-size:19px;fill:var(--text)">開始</text>
  <line x1="180" y1="36" x2="180" y2="52" stroke="var(--text-faint)" stroke-width="1.6" marker-end="url(#fa2b)"/>
  <polygon points="180,52 262,92 180,132 98,92" fill="var(--warn-soft)" stroke="var(--warn)" stroke-width="1.6"/>
  <text x="180" y="90" text-anchor="middle" style="font-size:16px;fill:var(--text);font-weight:700">number % 2 == 1 ？</text>
  <text x="180" y="110" text-anchor="middle" style="font-size:14px;fill:var(--text-soft)">餘數是 1 ？</text>
  <path d="M98,92 H58 V150" fill="none" stroke="var(--text-faint)" stroke-width="1.6" marker-end="url(#fa2b)"/>
  <text x="76" y="84" text-anchor="middle" style="font-size:17px;fill:var(--ok);font-weight:800">是</text>
  <rect x="6" y="150" width="108" height="38" rx="8" fill="var(--brand-soft)" stroke="var(--brand)" stroke-width="1.6"/>
  <text x="60" y="174" text-anchor="middle" style="font-size:18px;fill:var(--brand-strong);font-weight:700">印「奇數」</text>
  <path d="M262,92 H302 V150" fill="none" stroke="var(--text-faint)" stroke-width="1.6" marker-end="url(#fa2b)"/>
  <text x="284" y="84" text-anchor="middle" style="font-size:17px;fill:var(--danger);font-weight:800">否</text>
  <rect x="248" y="150" width="108" height="38" rx="8" fill="var(--brand-soft)" stroke="var(--brand)" stroke-width="1.6"/>
  <text x="302" y="174" text-anchor="middle" style="font-size:18px;fill:var(--brand-strong);font-weight:700">印「偶數」</text>
  <path d="M60,188 V218 H126" fill="none" stroke="var(--text-faint)" stroke-width="1.6" marker-end="url(#fa2b)"/>
  <path d="M302,188 V218 H234" fill="none" stroke="var(--text-faint)" stroke-width="1.6" marker-end="url(#fa2b)"/>
  <rect x="126" y="204" width="108" height="30" rx="8" fill="var(--surface-2)" stroke="var(--border)" stroke-width="1.4"/>
  <text x="180" y="224" text-anchor="middle" style="font-size:18px;fill:var(--text)">繼續程式</text>
</svg></div>
</div>
'''
) + sec(3, "多向判斷 if–elif–else", '''
<p>用 <code>elif</code> 處理多個條件，<strong>由上往下依序檢查</strong>，符合就執行那一塊並跳出、不再往下檢查；全部都不符合才走 <code>else</code>。</p>
<div class="cf-row"><div class="flowwrap"><svg class="flow" viewBox="0 0 400 372" role="img" style="max-width:470px" aria-label="多向判斷 if-elif-else 流程圖">
  <defs><marker id="fa3" markerWidth="9" markerHeight="9" refX="7" refY="3" orient="auto"><path d="M0,0 L7,3 L0,6 Z" fill="var(--text-faint)"/></marker></defs>
  <rect x="25" y="6" width="90" height="26" rx="13" fill="var(--surface-2)" stroke="var(--border)" stroke-width="1.4"/>
  <text x="70" y="24" text-anchor="middle" style="font-size:18px;fill:var(--text)">開始</text>
  <line x1="70" y1="32" x2="70" y2="46" stroke="var(--text-faint)" stroke-width="1.6" marker-end="url(#fa3)"/>
  <polygon points="70,46 130,70 70,94 10,70" fill="var(--warn-soft)" stroke="var(--warn)" stroke-width="1.5"/>
  <text x="70" y="74" text-anchor="middle" style="font-size:17px;fill:var(--text);font-weight:700">分數 ≥ 90 ？</text>
  <line x1="130" y1="70" x2="246" y2="70" stroke="var(--text-faint)" stroke-width="1.6" marker-end="url(#fa3)"/>
  <text x="152" y="63" text-anchor="middle" style="font-size:16.5px;fill:var(--ok);font-weight:800">是</text>
  <rect x="248" y="54" width="120" height="32" rx="8" fill="var(--brand-soft)" stroke="var(--brand)" stroke-width="1.5"/>
  <text x="308" y="74" text-anchor="middle" style="font-size:18px;fill:var(--brand-strong);font-weight:700">印「甲等」</text>
  <line x1="70" y1="94" x2="70" y2="116" stroke="var(--text-faint)" stroke-width="1.6" marker-end="url(#fa3)"/>
  <text x="80" y="110" text-anchor="start" style="font-size:16.5px;fill:var(--danger);font-weight:800">否</text>
  <polygon points="70,116 130,140 70,164 10,140" fill="var(--warn-soft)" stroke="var(--warn)" stroke-width="1.5"/>
  <text x="70" y="144" text-anchor="middle" style="font-size:17px;fill:var(--text);font-weight:700">分數 ≥ 80 ？</text>
  <line x1="130" y1="140" x2="246" y2="140" stroke="var(--text-faint)" stroke-width="1.6" marker-end="url(#fa3)"/>
  <text x="152" y="133" text-anchor="middle" style="font-size:16.5px;fill:var(--ok);font-weight:800">是</text>
  <rect x="248" y="124" width="120" height="32" rx="8" fill="var(--brand-soft)" stroke="var(--brand)" stroke-width="1.5"/>
  <text x="308" y="144" text-anchor="middle" style="font-size:18px;fill:var(--brand-strong);font-weight:700">印「乙等」</text>
  <line x1="70" y1="164" x2="70" y2="186" stroke="var(--text-faint)" stroke-width="1.6" marker-end="url(#fa3)"/>
  <text x="80" y="180" text-anchor="start" style="font-size:16.5px;fill:var(--danger);font-weight:800">否</text>
  <polygon points="70,186 130,210 70,234 10,210" fill="var(--warn-soft)" stroke="var(--warn)" stroke-width="1.5"/>
  <text x="70" y="214" text-anchor="middle" style="font-size:17px;fill:var(--text);font-weight:700">分數 ≥ 70 ？</text>
  <line x1="130" y1="210" x2="246" y2="210" stroke="var(--text-faint)" stroke-width="1.6" marker-end="url(#fa3)"/>
  <text x="152" y="203" text-anchor="middle" style="font-size:16.5px;fill:var(--ok);font-weight:800">是</text>
  <rect x="248" y="194" width="120" height="32" rx="8" fill="var(--brand-soft)" stroke="var(--brand)" stroke-width="1.5"/>
  <text x="308" y="214" text-anchor="middle" style="font-size:18px;fill:var(--brand-strong);font-weight:700">印「丙等」</text>
  <line x1="70" y1="234" x2="70" y2="256" stroke="var(--text-faint)" stroke-width="1.6" marker-end="url(#fa3)"/>
  <text x="80" y="250" text-anchor="start" style="font-size:16.5px;fill:var(--danger);font-weight:800">否</text>
  <polygon points="70,256 130,280 70,304 10,280" fill="var(--warn-soft)" stroke="var(--warn)" stroke-width="1.5"/>
  <text x="70" y="284" text-anchor="middle" style="font-size:17px;fill:var(--text);font-weight:700">分數 ≥ 60 ？</text>
  <line x1="130" y1="280" x2="246" y2="280" stroke="var(--text-faint)" stroke-width="1.6" marker-end="url(#fa3)"/>
  <text x="152" y="273" text-anchor="middle" style="font-size:16.5px;fill:var(--ok);font-weight:800">是</text>
  <rect x="248" y="264" width="120" height="32" rx="8" fill="var(--brand-soft)" stroke="var(--brand)" stroke-width="1.5"/>
  <text x="308" y="284" text-anchor="middle" style="font-size:18px;fill:var(--brand-strong);font-weight:700">印「丁等」</text>
  <line x1="70" y1="304" x2="70" y2="328" stroke="var(--text-faint)" stroke-width="1.6" marker-end="url(#fa3)"/>
  <text x="80" y="322" text-anchor="start" style="font-size:16.5px;fill:var(--danger);font-weight:800">否（else）</text>
  <rect x="10" y="328" width="140" height="34" rx="8" fill="var(--surface-2)" stroke="var(--border)" stroke-width="1.4"/>
  <text x="80" y="349" text-anchor="middle" style="font-size:18px;fill:var(--text);font-weight:700">印「你被當了！」</text>
</svg></div>
''' + R('''score = int(input("請輸入你的分數："))
if score >= 90:
    print("甲等")
elif score >= 80:
    print("乙等")
elif score >= 70:
    print("丙等")
elif score >= 60:
    print("丁等")
else:
    print("你被當了！")''') + '''
</div>
'''
) + exercise("課堂練習", '''
<ol>
  <li>輸入一個整數，判斷它是<strong>奇數還是偶數</strong>。</li>
  <li>輸入 BMI 值，印出「過輕 / 正常 / 過重」（過輕 &lt;18.5、正常 18.5–24、過重 &gt;24）。</li>
  <li>輸入三科成績，若三科都 ≥ 60 印「全部及格」，否則印「有不及格」。</li>
</ol>''', '''
''' + R('''# 第 1 題
n = int(input("請輸入一個整數："))
if n % 2 == 0:
    print("偶數")
else:
    print("奇數")''', "第 1 題參考解") + R('''# 第 2 題
bmi = float(input("BMI："))
if bmi < 18.5:
    print("過輕")
elif bmi <= 24:
    print("正常")
else:
    print("過重")''', "第 2 題參考解") + R('''# 第 3 題
chi = int(input("國文："))
eng = int(input("英文："))
mat = int(input("數學："))
if chi >= 60 and eng >= 60 and mat >= 60:
    print("全部及格")
else:
    print("有不及格")''', "第 3 題參考解"))

# =====================================================================
# 單元 10：Python（三）重複結構
# =====================================================================
BODIES["unit10"] = hero("unit10") + goals([
    "會用 for 迴圈搭配 range() 重複執行",
    "會用 while 迴圈依條件重複",
    "理解 break 與 continue 的差別",
]) + sec(1, "for 迴圈", '''
<p><strong>先認識 <code>list</code>（串列）：</strong>用中括號 <code>[ ]</code> 把多個資料<strong>依序</strong>裝起來、中間用逗號 <code>,</code> 分隔，例如 <code>["香蕉", "蘋果", "橘子"]</code>。它就像「一排有順序的箱子」：第 1 個是 <code>list1[0]</code>（<strong>從 0 開始數</strong>）、第 2 個是 <code>list1[1]</code>、第 3 個是 <code>list1[2]</code>。</p>
<p><code>for</code> 迴圈最方便的用法，就是把 list 裡的元素<strong>一個一個取出來</strong>處理——每繞一圈，<code>s</code> 就依序變成「香蕉 → 蘋果 → 橘子」，各印一次：</p>
''' + R('''list1 = ["香蕉", "蘋果", "橘子"]
for s in list1:
    print(s)''') + '''
<h3>搭配 range()</h3>
<p><code>range(start, stop, step)</code> 產生數字序列（不含 stop），預設 start=0、step=1。</p>
<div class="table-wrap"><table class="center">
<thead><tr><th>寫法</th><th>產生的數字</th></tr></thead>
<tbody>
<tr><td><code>range(5)</code></td><td>0, 1, 2, 3, 4</td></tr>
<tr><td><code>range(1, 11)</code></td><td>1, 2, …, 10</td></tr>
<tr><td><code>range(0, 10, 2)</code></td><td>0, 2, 4, 6, 8</td></tr>
</tbody></table></div>
''' + R('''# 計算 1+2+…+10
sum = 0
for i in range(1, 11, 1):
    sum += i
print(sum)   # 55''') + '''
<p style="margin:10px 0 2px;color:var(--text-soft);font-size:.9rem">👇 看不懂 <code>i</code> 怎麼跑、<code>sum</code> 怎麼越加越大嗎？點「下一步」一圈一圈跑跑看：</p>
<div class="loopstep" id="loopstep">
  <div class="vs-cc">
    <div class="vs-srccard" style="max-width:none;margin:0">
      <div class="vs-srchead"><span class="vsdot r"></span><span class="vsdot y"></span><span class="vsdot g"></span><span class="vs-srclabel">加總.py　—　目前執行的那一行會反白</span></div>
      <div class="vs-src">
        <div class="vs-ln" data-ln="init">sum = 0</div>
        <div class="vs-ln" data-ln="loop">for i in range(1, 11, 1):</div>
        <div class="vs-ln" data-ln="loop">    sum += i</div>
        <div class="vs-ln" data-ln="end">print(sum)   # 55</div>
      </div>
    </div>
    <div class="vs-console"><div class="vs-console-h">🖥️ 程式輸出</div><div class="vs-console-body" id="ls-out"></div></div>
  </div>
  <div class="ls-body">
    <div class="ls-left">
      <div class="ls-vars">
        <div class="ls-chip">i ＝ <b id="ls-i">－</b></div>
        <div class="ls-chip">sum ＝ <b id="ls-sum">0</b></div>
      </div>
      <div class="ls-say" id="ls-say">按「下一步 ▶」開始跑迴圈：i 會從 1 一路數到 10，每一圈把 i 加進 sum。</div>
      <div class="ls-tablewrap">
        <table class="ls-table"><thead><tr><th>第幾圈</th><th>i</th><th>sum ＋ i</th><th>sum 變成</th></tr></thead>
        <tbody id="ls-rows"></tbody></table>
      </div>
    </div>
    <div class="ls-right">
      <button type="button" class="vs-btn" id="ls-next">下一步 ▶</button>
      <button type="button" class="vs-btn ghost" id="ls-auto">▶▶ 自動播放</button>
      <button type="button" class="vs-btn ghost" id="ls-reset">↺ 重來</button>
    </div>
  </div>
</div>
<script>
(function(){
  var root=document.getElementById("loopstep"); if(!root) return;
  var iEl=document.getElementById("ls-i"),sumEl=document.getElementById("ls-sum"),say=document.getElementById("ls-say"),rows=document.getElementById("ls-rows");
  var next=document.getElementById("ls-next"),auto=document.getElementById("ls-auto"),reset=document.getElementById("ls-reset");
  var i=0,sum=0,timer=null;
  var srclns=root.querySelectorAll(".vs-ln"),out=document.getElementById("ls-out");
  function setHi(v){ for(var q=0;q<srclns.length;q++){ srclns[q].classList.toggle("hi", srclns[q].getAttribute("data-ln")===v); } }
  function setOut(v){ out.innerHTML = (v!=="") ? '<div class="vs-outline fresh">'+v+'</div>' : '<div class="vs-outph">（迴圈跑完才會 print，還沒有輸出）</div>'; }
  function stop(){ if(timer){clearInterval(timer);timer=null;auto.textContent="▶▶ 自動播放";} }
  function finish(){
    stop(); next.disabled=true; next.textContent="✓ 迴圈結束"; setHi("end"); setOut(sum);
    say.innerHTML="迴圈跑完 10 圈，i 走過 1→10，最後 <b>sum = "+sum+"</b>。所以 <code>print(sum)</code> 會印出 <b>"+sum+"</b>（看右邊）。";
  }
  function step(){
    if(i>=10){ finish(); return; }
    i++; var before=sum; sum=before+i;
    iEl.textContent=i; sumEl.textContent=sum;
    var tr=document.createElement("tr"); tr.className="fresh";
    tr.innerHTML="<td>第 "+i+" 圈</td><td>"+i+"</td><td>"+before+" ＋ "+i+"</td><td><b>"+sum+"</b></td>";
    rows.appendChild(tr);
    say.textContent="第 "+i+" 圈：i = "+i+"，把 "+i+" 加進 sum → sum 從 "+before+" 變成 "+sum+"。";
    setHi("loop");
    if(i>=10){ finish(); }
  }
  function resetAll(){ stop(); i=0;sum=0; iEl.textContent="－"; sumEl.textContent="0"; rows.innerHTML=""; next.disabled=false; next.textContent="下一步 ▶"; say.textContent="按「下一步 ▶」開始跑迴圈：i 會從 1 一路數到 10，每一圈把 i 加進 sum。"; setHi("init"); setOut(""); }
  next.addEventListener("click",step);
  auto.addEventListener("click",function(){ if(timer){stop();return;} if(i>=10)resetAll(); auto.textContent="⏸ 暫停"; timer=setInterval(step,700); });
  reset.addEventListener("click",resetAll);
  setHi("init"); setOut("");
})();
</script>
<h3>應用：倍數判斷</h3>
''' + R('''n = int(input("請輸入一個數："))
for i in range(1, n + 1):
    if i % 6 == 0:
        print(f"{i}是2和3的倍數")
    elif i % 3 == 0:
        print(f"{i}是3的倍數")
    elif i % 2 == 0:
        print(f"{i}是2的倍數")''')
) + sec(2, "while 迴圈", '''
<p><code>while</code> 在<strong>條件成立時</strong>一直重複，適合「次數由條件決定」的情況。</p>
''' + R('''total = 0
n = 0
while n < 10:
    n += 1
    total = total + n
print(total)   # 55''') + '''
<div class="callout warn"><span class="t">⚠ 小心無窮迴圈</span>
<p>while 的條件<strong>一定要有機會變成 False</strong>（記得讓變數遞增／遞減），否則程式會停不下來。</p></div>
''') + sec(3, "break 與 continue", '''
<div class="callout"><span class="t">⏱️ 提醒：動畫是「慢動作」</span>
<p>下面的動畫為了讓大家<strong>看懂程式的邏輯</strong>，是把數字<strong>一個一個、慢慢地</strong>顯示出來。但實際執行時，因為電腦跑得<strong>非常非常非常快</strong>，你會看到輸出<strong>幾乎一瞬間就全部跳出來</strong>，不會像動畫這樣一格一格慢慢跑。</p></div>
<h3>⛔ break：強制離開迴圈</h3>
<p>遇到 <code>break</code> 就<strong>立刻跳出整個迴圈</strong>，後面的圈數都不再跑。點「下一步」跑跑看：</p>
<div class="looptrace" id="brk">
  <div class="vs-cc">
    <div class="vs-srccard" style="max-width:none;margin:0">
      <div class="vs-srchead"><span class="vsdot r"></span><span class="vsdot y"></span><span class="vsdot g"></span><span class="vs-srclabel">break.py　—　目前執行的那一行會反白</span></div>
      <div class="vs-src">
        <div class="vs-ln" data-ln="0">for i in range(1, 11):</div>
        <div class="vs-ln" data-ln="1">    if i == 6:</div>
        <div class="vs-ln" data-ln="2">        break</div>
        <div class="vs-ln" data-ln="3">    print(i, end=",")</div>
      </div>
    </div>
    <div class="vs-console"><div class="vs-console-h">🖥️ 程式輸出</div><div class="vs-console-body ltout"></div></div>
  </div>
  <div class="lt-row"><span class="lt-i">i ＝ <b>–</b></span></div>
  <div class="lt-say">按「下一步 ▶」開始。</div>
  <div class="vs-controls"><button type="button" class="vs-btn ltn">下一步 ▶</button><button type="button" class="vs-btn ghost ltr">↺ 重來</button></div>
</div>
<h3 style="margin-top:22px">⏭️ continue：跳過本次</h3>
<p>遇到 <code>continue</code> 就<strong>跳過這一圈剩下的動作</strong>，直接進入下一圈（迴圈本身不會停）。點「下一步」跑跑看：</p>
<div class="looptrace" id="cont">
  <div class="vs-cc">
    <div class="vs-srccard" style="max-width:none;margin:0">
      <div class="vs-srchead"><span class="vsdot r"></span><span class="vsdot y"></span><span class="vsdot g"></span><span class="vs-srclabel">continue.py　—　目前執行的那一行會反白</span></div>
      <div class="vs-src">
        <div class="vs-ln" data-ln="0">for i in range(1, 11):</div>
        <div class="vs-ln" data-ln="1">    if i == 6:</div>
        <div class="vs-ln" data-ln="2">        continue</div>
        <div class="vs-ln" data-ln="3">    print(i, end=",")</div>
      </div>
    </div>
    <div class="vs-console"><div class="vs-console-h">🖥️ 程式輸出</div><div class="vs-console-body ltout"></div></div>
  </div>
  <div class="lt-row"><span class="lt-i">i ＝ <b>–</b></span></div>
  <div class="lt-say">按「下一步 ▶」開始。</div>
  <div class="vs-controls"><button type="button" class="vs-btn ltn">下一步 ▶</button><button type="button" class="vs-btn ghost ltr">↺ 重來</button></div>
</div>
<script>
(function(){
  function mk(id,steps){
    var root=document.getElementById(id); if(!root) return;
    var iEl=root.querySelector(".lt-i b"),outEl=root.querySelector(".ltout"),say=root.querySelector(".lt-say");
    var next=root.querySelector(".ltn"),reset=root.querySelector(".ltr"),srclns=root.querySelectorAll(".vs-ln");
    var i=0;
    function render(){
      var s=steps[i];
      iEl.textContent=s.i;
      outEl.innerHTML = s.out ? '<div class="vs-outline">'+s.out+'</div>' : '<div class="vs-outph">（還沒有 print 輸出）</div>';
      say.innerHTML=s.say;
      for(var q=0;q<srclns.length;q++){srclns[q].classList.toggle("hi",(s.lns||[]).indexOf(srclns[q].getAttribute("data-ln"))>=0);}
      var end=i>=steps.length-1;
      next.textContent=end?"✓ 結束":"下一步 ▶"; next.disabled=end;
    }
    next.addEventListener("click",function(){if(i<steps.length-1){i++;render();}});
    reset.addEventListener("click",function(){i=0;render();});
    render();
  }
  mk("brk",[
    {i:"–",lns:[],out:"",say:"按「下一步 ▶」開始。"},
    {i:"–",lns:["0"],out:"",say:"先看 <code>for i in range(1, 11)</code>：接下來 <b>i 會依序拿到 1、2、3、…、10</b>，一個一個進迴圈。每個 i 進來，都會先做下面的 <code>if i == 6</code> 判斷。"},
    {i:"1",lns:["1","3"],out:"1,",say:"i = 1，判斷 <code>if i == 6</code>：<b>不等於 6</b>（不符合 if）→ 就跳過 if 裡的 break，改做 if 後面的 print，印出 1。"},
    {i:"2",lns:["1","3"],out:"1,2,",say:"i = 2，判斷 <code>if i == 6</code>：<b>不等於 6</b> → 跳過 if 裡的 break，印出 2。"},
    {i:"3",lns:["1","3"],out:"1,2,3,",say:"i = 3，判斷 <code>if i == 6</code>：<b>不等於 6</b> → 印出 3。"},
    {i:"4",lns:["1","3"],out:"1,2,3,4,",say:"i = 4，判斷 <code>if i == 6</code>：<b>不等於 6</b> → 印出 4。"},
    {i:"5",lns:["1","3"],out:"1,2,3,4,5,",say:"i = 5，判斷 <code>if i == 6</code>：<b>不等於 6</b> → 印出 5。"},
    {i:"6",lns:["1","2"],out:"1,2,3,4,5,",say:"i = 6，判斷 <code>if i == 6</code>：<b>等於 6</b> → 執行 <b>break</b>，立刻跳出整個迴圈，後面的 7、8、9、10 都不再做。"}
  ]);
  mk("cont",[
    {i:"–",lns:[],out:"",say:"按「下一步 ▶」開始。"},
    {i:"–",lns:["0"],out:"",say:"先看 <code>for i in range(1, 11)</code>：接下來 <b>i 會依序拿到 1、2、3、…、10</b>，一個一個進迴圈。每個 i 進來，都會先做下面的 <code>if i == 6</code> 判斷。"},
    {i:"1",lns:["1","3"],out:"1,",say:"i = 1，判斷 <code>if i == 6</code>：<b>不成立</b> → 不 continue，改做 if 後面的 print，印出 1。"},
    {i:"2",lns:["1","3"],out:"1,2,",say:"i = 2，判斷 <code>if i == 6</code>：<b>不成立</b> → 印出 2。"},
    {i:"3",lns:["1","3"],out:"1,2,3,",say:"i = 3，判斷 <code>if i == 6</code>：<b>不成立</b> → 印出 3。"},
    {i:"4",lns:["1","3"],out:"1,2,3,4,",say:"i = 4，判斷 <code>if i == 6</code>：<b>不成立</b> → 印出 4。"},
    {i:"5",lns:["1","3"],out:"1,2,3,4,5,",say:"i = 5，判斷 <code>if i == 6</code>：<b>不成立</b> → 印出 5。"},
    {i:"6",lns:["1","2"],out:"1,2,3,4,5,",say:"i = 6，判斷 <code>if i == 6</code>：<b>成立</b> → 執行 <b>continue</b>，跳過這一圈剩下的 print（不印 6），直接進下一圈。"},
    {i:"7",lns:["1","3"],out:"1,2,3,4,5,7,",say:"i = 7，判斷 <code>if i == 6</code>：<b>不成立</b> → 印出 7。"},
    {i:"8",lns:["1","3"],out:"1,2,3,4,5,7,8,",say:"i = 8，判斷不成立 → 印出 8。"},
    {i:"9",lns:["1","3"],out:"1,2,3,4,5,7,8,9,",say:"i = 9，判斷不成立 → 印出 9。"},
    {i:"10",lns:["1","3"],out:"1,2,3,4,5,7,8,9,10,",say:"i = 10，判斷不成立 → 印出 10。迴圈跑完，結束。"}
  ]);
})();
</script>
''') + exercise("課堂練習", '''
<ol>
  <li>用 for 迴圈印出 1~10 的<strong>平方</strong>。</li>
  <li>用 while 迴圈算出 <strong>1×2×3×…×10</strong>（10 的階乘）。</li>
  <li>用迴圈印出 1~50 中所有<strong>7 的倍數</strong>。</li>
</ol>''', '''
''' + R('''# 第 2 題
result = 1
n = 1
while n <= 10:
    result *= n
    n += 1
print("10! =", result)   # 3628800''', "第 2 題參考解") + R('''# 第 3 題
for i in range(1, 51):
    if i % 7 == 0:
        print(i, end=" ")
# 7 14 21 28 35 42 49''', "第 3 題參考解"))

# =====================================================================
# 單元 11：Python（四）迴圈進階與綜合
# =====================================================================
BODIES["unit11"] = hero("unit11") + goals([
    "會使用巢狀迴圈處理二維的重複",
    "掌握累加、計數、找最大值等常見樣式",
    "會用「程式追蹤」預測程式的輸出",
]) + sec(1, "巢狀迴圈", '''
<p>迴圈裡再放迴圈稱為<strong>巢狀迴圈</strong>：外層跑一次，內層就整個跑完一輪。常用於表格與圖形。</p>
''' + R('''# 九九乘法表（部分）
for i in range(1, 4):
    for j in range(1, 10):
        print(f"{i}x{j}={i*j}", end="\\t")
    print()      # 換行''') + '''
<div class="callout"><span class="t">🔎 <code>\\t</code> 是什麼？</span>
<p><code>\\t</code> 是「Tab（跳格／定位）」字元，會讓游標<strong>跳到下一個定位停格</strong>，把後面的字對齊成整齊的欄位——比用空格更容易對齊。所以這裡把 <code>end="\\t"</code> 當每個算式之間的分隔，印出來的乘法表就會像用「表格欄位」一樣<strong>上下對齊</strong>。（<code>\\t</code> 跟 <code>\\n</code> 一樣是「一個字元」，不是兩個字；<code>\\n</code> 是換行、<code>\\t</code> 是跳格。）</p></div>
<h3>印出三角形圖案</h3>
''' + R('''for i in range(1, 6):
    print("*" * i)''') + '''
<div class="callout"><span class="t">🔎 <code>"*" * i</code> 是什麼意思？</span>
<p>字串乘以整數（<code>字串 * 數字</code>）代表把這個字串<strong>重複串接幾次</strong>。例如 <code>"*" * 3</code> 會得到 <code>"***"</code>、<code>"ab" * 2</code> 會得到 <code>"abab"</code>。所以迴圈裡 <code>i</code> 從 1 變到 5，<code>"*" * i</code> 就依序印出 1、2、3、4、5 個星號，疊成一個三角形。<br>（注意：<code>*</code> 一定要「<strong>字串 × 整數</strong>」；寫成 <code>"*" * 3.0</code> 或 <code>"*" * "3"</code> 都會出錯。）</p></div>
'''
) + sec(2, "常見迴圈樣式", '''
<div class="grid cols-2">
<div class="card"><h3>➕ 累加 / 計數</h3>
''' + R('''nums = [12, 7, 25, 9, 30]
total = 0
count = 0
for n in nums:
    total += n            # 累加
    if n > 10:
        count += 1        # 計數
print("總和 =", total)     # 83
print("大於 10 的有", count, "個")''', "累加與計數") + '''</div>
<div class="card"><h3>🔝 找最大值</h3>
''' + R('''nums = [12, 7, 25, 9, 30]
biggest = nums[0]
for n in nums:
    if n > biggest:
        biggest = n
print("最大值 =", biggest)  # 30''', "找最大值") + '''</div>
</div>
<div class="callout"><span class="t">🧭 從「找最大值」延伸：排序與搜尋</span>
<p>「用一個迴圈掃過所有資料、隨時記住目前最好的那一個」這個想法，正是很多<strong>演算法</strong>的起點：</p>
<ul class="tidy">
  <li><strong>排序（Sorting）</strong>：把一堆資料<strong>由小到大（或由大到小）排好</strong>。最直覺的「選擇排序」就是不斷「找出最小的、放到最前面」——等於把上面的「找最大／最小值」重複做很多次。</li>
  <li><strong>搜尋（Searching）</strong>：在資料裡<strong>找出某個目標</strong>。最基本的「線性搜尋」就是用迴圈一個一個比對；如果資料<strong>已經排好序</strong>，還能用更快的「二分搜尋」，每次把範圍砍一半。</li>
</ul>
<p style="margin-bottom:0">這些「排序、搜尋」正式的演算法（怎麼寫、怎麼比較快慢）會在<strong>高二選修的「演算法」</strong>課程更完整地介紹。現在先體會「原來一個 <code>for</code> 迴圈就能做到這些事」就可以了。</p></div>
''') + sec(3, "程式追蹤（Trace）", '''
<p>「程式追蹤」是<strong>一行一行在紙上模擬執行</strong>、記錄變數變化，是讀懂程式與抓錯的重要能力。</p>
<div class="card"><h3>試著追蹤，猜猜輸出：</h3>
''' + R('''x = 0
for i in range(1, 5):
    x = x + i
    print(i, x)''', "先追蹤再對答案") + '''
<div class="reveal" onclick="toggleAnswer(this)">▶ 顯示追蹤表</div>
<div class="answer">
<div class="table-wrap"><table class="center">
<thead><tr><th>i</th><th>x = x + i</th><th>印出</th></tr></thead>
<tbody>
<tr><td>1</td><td>0+1=1</td><td>1 1</td></tr>
<tr><td>2</td><td>1+2=3</td><td>2 3</td></tr>
<tr><td>3</td><td>3+3=6</td><td>3 6</td></tr>
<tr><td>4</td><td>6+4=10</td><td>4 10</td></tr>
</tbody></table></div>
</div>
</div>
''') + exercise("課堂練習", '''
<ol>
  <li>用巢狀迴圈印出完整的<strong>九九乘法表</strong>（1×1 到 9×9）。</li>
  <li>印出底邊 5 的<strong>直角三角形</strong>（第 1 列 1 顆星、第 5 列 5 顆星）。</li>
  <li>給分數 <code>[55, 88, 72, 90, 47]</code>，算出<strong>平均</strong>並數出<strong>及格人數</strong>。</li>
</ol>''', '''
''' + R('''# 第 3 題
scores = [55, 88, 72, 90, 47]
total = 0
passed = 0
for s in scores:
    total += s
    if s >= 60:
        passed += 1
print("平均 =", total / len(scores))
print("及格人數 =", passed)''', "第 3 題參考解"))

# =====================================================================
# 單元 12：Python（五）函式與綜合應用
# =====================================================================
BODIES["unit12"] = hero("unit12") + goals([
    "會定義與呼叫自訂函式",
    "理解參數 (parameter) 與回傳值 (return)",
    "分辨區域變數與全域變數",
    "能整合變數、判斷、迴圈與函式完成綜合題",
]) + sec(1, "為什麼要用函式？", '''
<p><strong>函式</strong>是一段<strong>包裝好、可重複使用</strong>的程式碼。把常用功能寫成函式，可讓程式更簡潔、好維護。</p>
''' + R('''def say_hello():
    print("哈囉！我是阿翔，歡迎學 Python")

# 呼叫函式（可重複呼叫）
say_hello()
say_hello()''')
) + sec(2, "參數與回傳值", '''
<p><strong>參數</strong>讓函式能接收外部資料；<code>return</code> 把結果傳回給呼叫者。</p>
''' + R('''def add(a, b):        # a, b 是參數
    return a + b       # 回傳（相加的結果）

def multiply(a, b):   # 再定義一個「相乘」的函式
    return a * b       # 回傳（相乘的結果）

print("8 + 9 =", add(8, 9))        # 17
print("7 × 4 =", multiply(7, 4))   # 28''') + '''
<h3>再看一個：判斷是否及格</h3>
''' + R('''def is_pass(score):
    if score >= 60:
        return "及格"
    else:
        return "不及格"

print(is_pass(85))   # 及格
print(is_pass(40))   # 不及格''')
) + sec(3, "區域變數與全域變數", '''
<p>函式<strong>裡面</strong>定義的是<strong>區域變數</strong>，只在函式內有效；函式<strong>外面</strong>定義的是<strong>全域變數</strong>。</p>
''' + R('''total = 100          # 全域變數

def show():
    msg = "函式內部"    # 區域變數
    print(msg, total)

show()
print(total)
# print(msg)   # ← 這行會出錯，msg 只存在於函式內''')
) + sec(4, "綜合應用專題", '''
<p>整合前面學過的<strong>變數、輸入輸出、判斷、迴圈、函式</strong>，做一個成績計算小工具：</p>
<div class="card"><h3>🧮 成績計算小工具</h3>
''' + R('''def grade(score):
    if score >= 90: return "A"
    elif score >= 80: return "B"
    elif score >= 70: return "C"
    elif score >= 60: return "D"
    else: return "F"

scores = [92, 78, 55, 88, 63]
total = 0
for s in scores:
    total += s
    print(f"分數 {s} → 等第 {grade(s)}")

avg = total / len(scores)
print("-" * 20)
print(f"平均分數：{avg:.1f}")
print("平均等第：", grade(avg))''', "成績計算小工具") + '''
</div>
<div class="callout"><span class="t">💡 小技巧：只有一行的 if 可以寫在同一行</span>
<p>如果 <code>if</code>／<code>elif</code>／<code>else</code> 裡<strong>只有一行</strong>程式碼，可以直接寫在冒號 <code>:</code> 後面，像上面 <code>grade()</code> 那樣 <code>if score >= 90: return "A"</code>，程式更精簡好讀。<br>但如果 if 裡面有<strong>好幾行</strong>要做，就還是要<strong>換行、縮排</strong>寫，不能全部擠在同一行。</p></div>
''') + exercise("課堂練習", '''
<ol>
  <li>寫函式 <code>square(n)</code> 回傳 n 的平方，並印出 1~5 的平方。</li>
  <li>寫函式 <code>bigger(a, b)</code> 回傳兩數中<strong>較大</strong>的那個。</li>
  <li>綜合題：寫函式 <code>is_prime(n)</code> 判斷 n 是否為<strong>質數</strong>，並找出 2~30 之間所有質數。</li>
</ol>''', '''
''' + R('''# 第 3 題
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

for n in range(2, 31):
    if is_prime(n):
        print(n, end=" ")
# 2 3 5 7 11 13 17 19 23 29''', "第 3 題參考解"))


# =====================================================================
# 單元 13：Python（二）基礎輸入與輸出　（顯示為單元 9）
# =====================================================================
BODIES["unit13"] = hero("unit13") + goals([
    "會用 input() 讀取輸入，並知道它一定是字串（str）",
    "熟悉 print() 的多項輸出、sep 分隔字元與 end 結束字元",
    "會用 %、str.format() 與 f-string 三種方式格式化輸出",
    "能控制欄寬、對齊、小數位數與進位前綴",
]) + sec(1, "輸入 input()", '''
<p><code>input()</code> 會讀進使用者輸入的一行文字，<strong>回傳的一定是字串（str）</strong>。語法：</p>
<p><code>變數 = input([提示字串])</code></p>
''' + R('''a = input('請輸入數字：')
print(a)
print(type(a))        # <class 'str'>  —— input 讀進來是「字串」''') + '''
<div class="callout warn"><span class="t">⚠️ 常見陷阱</span>
<p><code>input()</code> 讀到的是<strong>字串</strong>，不能直接拿來算數學。要當數字用，得先轉型別：<code>int(input())</code> 或 <code>float(input())</code>。</p></div>
''') + sec(2, "輸出 print()", '''
<p>語法：<code>print(項目1 [, 項目2, … , sep=分隔字元, end=結束字元])</code>。多個項目用逗號隔開；字串也可以用 <code>+</code> 組合，但<strong>不同型別要先轉成字串</strong>。</p>
''' + R('''print(87, "吃水果會過敏", 87)
print(str(87) + "吃水果會過敏" + str(87))          # 用 + 組合，數字要先 str()
print(87, "吃水果會過敏", 87, sep="&")             # 用 & 當分隔字元
print("不要叫我吃水果了啦", 87, sep="&", end=".")   # 結尾不換行、改成 .''') + '''
<h4><code>\\n</code>：在字串裡換行</h4>
<p>在字串中間放一個 <code>\\n</code>，印出來時那個位置就會<strong>換到下一行</strong>。它是「一個字元」，不是兩個字。</p>
''' + R('''print("吃水果會過敏\\n不要叫我吃水果了啦")     # \\n 的位置會換行
print("都沒有人相信我吃水果會過敏")''') + '''
<p class="hint">上面第一行會印成兩行：先印「吃水果會過敏」，再換行印「不要叫我吃水果了啦」；第二行再自成一行。</p>
<div class="callout"><span class="t">🔎 sep 與 end</span>
<p><code>sep</code>：各項目之間的<strong>分隔字元</strong>（預設是一個空格）。<code>end</code>：整行輸出後的<strong>結束字元</strong>（預設是換行 <code>\\n</code>，所以每個 <code>print()</code> 才會各自成一行）。</p></div>
''') + sec(3, "格式化輸出：統一用 f-string", '''
<p>把變數和數字「漂亮地」放進字串裡（對齊、補零、指定小數位數、轉進位…）就叫<strong>格式化輸出</strong>。Python 有三種寫法：最舊的 <code>%</code>、後來的 <code>.format()</code>，和現在最推薦的 <strong>f-string</strong>。<strong>本課之後一律用 f-string 就好</strong>——只要在字串前面加一個 <code>f</code>，再把變數直接寫進 <code>{ }</code> 裡：</p>
''' + R('''name = "阿翔"
math = 87
print(f"{name}的數學成績是 {math} 分")   # 直接把變數塞進 { }''') + '''
<h3>在 <code>{ }</code> 裡加格式：<code>{值:格式}</code></h3>
<p>在大括號裡、變數後面加一個冒號 <code>:</code>，就能指定<strong>寬度、對齊、小數位數、補零、進位</strong>。以 <code>math</code> 為例：</p>
<div class="table-wrap"><table class="center">
<thead><tr><th>想做什麼</th><th>寫法</th><th>印出來（<code>█</code> 代表空格）</th></tr></thead>
<tbody>
<tr><td>寬度 8、靠右（數值預設）</td><td><code>{math:&gt;8}</code></td><td><code>██████87</code></td></tr>
<tr><td>寬度 8、靠左</td><td><code>{math:&lt;8}</code></td><td><code>87██████</code></td></tr>
<tr><td>寬度 8、置中</td><td><code>{math:^8}</code></td><td><code>███87███</code></td></tr>
<tr><td>保留 2 位小數</td><td><code>{math:.2f}</code></td><td><code>87.00</code></td></tr>
<tr><td>共 6 格、2 位小數、前面補 0</td><td><code>{math:06.2f}</code></td><td><code>087.00</code></td></tr>
<tr><td>轉二／八／十六進位</td><td><code>{n:b}</code>／<code>{n:o}</code>／<code>{n:x}</code></td><td>11 → <code>1011</code>／13 → <code>15</code>／11 → <code>b</code></td></tr>
<tr><td>進位再加前綴 <code>0b/0o/0x</code></td><td><code>{n:#x}</code></td><td>11 → <code>0xb</code></td></tr>
</tbody></table></div>
<p class="hint">對齊符號：<code>&lt;</code> 靠左、<code>&gt;</code> 靠右、<code>^</code> 置中；字串預設靠左、數值預設靠右。</p>
''' + R('''name = "阿翔"
math = 87.67
print(f"{name}數學成績{math:06.2f}")   # 補 0、共 6 格、2 位小數 → 087.67
print(f"{0b1011:#x}")                  # 二進位 1011 = 11 → 十六進位 0xb''') + '''
<p style="margin:10px 0 2px;color:var(--text-soft);font-size:.9rem">👇 f-string 怎麼把變數和格式「填」進字串？點「下一步」一行一行看：</p>
<div class="varstep" id="fstep">
  <div class="vs-stage">
    <div class="vs-boxes">
      <div class="vs-box empty wide" id="fs-name"><span class="vs-name">name</span><span class="vs-val"></span></div>
      <div class="vs-box empty wide" id="fs-math"><span class="vs-name">math</span><span class="vs-val"></span></div>
    </div>
  </div>
  <div class="vs-cc"><div class="vs-srccard">
    <div class="vs-srchead"><span class="vsdot r"></span><span class="vsdot y"></span><span class="vsdot g"></span><span class="vs-srclabel">格式化.py　—　目前執行的那一行會反白</span></div>
    <div class="vs-src">
      <div class="vs-ln" data-ln="0">name = "阿翔"</div>
      <div class="vs-ln" data-ln="1">math = 87.67</div>
      <div class="vs-ln" data-ln="2">print(f"{name}數學成績{math:06.2f}")   # 補 0、共 6 格、2 位小數 → 087.67</div>
      <div class="vs-ln" data-ln="3">print(f"{0b1011:#x}")                  # 二進位 1011 = 11 → 十六進位 0xb</div>
    </div>
  </div>
    <div class="vs-console"><div class="vs-console-h">🖥️ 程式輸出</div><div class="vs-console-body" id="fs-out"></div></div>
  </div>
  <div class="vs-cap" id="fs-cap">點「下一步 ▶」，看看 f-string 怎麼把變數和格式填進字串、再印到右邊。</div>
  <div class="vs-controls">
    <button type="button" class="vs-btn" id="fs-next">下一步 ▶</button>
    <button type="button" class="vs-btn ghost" id="fs-reset">↺ 重來</button>
  </div>
</div>
<script>
(function(){
  var root=document.getElementById("fstep"); if(!root) return;
  var steps=[
    {name:"",math:"",ln:-1,cap:"點「下一步 ▶」，看看 f-string 怎麼把變數和格式填進字串、再印到右邊。",hi:[],out:[]},
    {name:'"阿翔"',math:"",ln:0,cap:'把字串 "阿翔" 放進 name。',hi:["name"],out:[]},
    {name:'"阿翔"',math:"87.67",ln:1,cap:"把 87.67 放進 math。",hi:["math"],out:[]},
    {name:'"阿翔"',math:"87.67",ln:2,cap:"f-string：{name} 換成「阿翔」；{math:06.2f} 把 87.67 補成「共 6 格、2 位小數、前面補 0」→ 087.67。",hi:["name","math"],out:["阿翔數學成績087.67"]},
    {name:'"阿翔"',math:"87.67",ln:3,cap:"{0b1011:#x}：0b1011 是二進位（= 11），:#x 把它轉成十六進位、加上前綴 → 0xb。",hi:[],out:["阿翔數學成績087.67","0xb"]}
  ];
  var i=0;
  var nameB=document.getElementById("fs-name"),mathB=document.getElementById("fs-math");
  var nameV=nameB.querySelector(".vs-val"),mathV=mathB.querySelector(".vs-val");
  var cap=document.getElementById("fs-cap"),out=document.getElementById("fs-out");
  var srclns=root.querySelectorAll(".vs-ln");
  var next=document.getElementById("fs-next"),reset=document.getElementById("fs-reset");
  function one(box,el,val,hi,prev){
    el.textContent=val;
    if(val===""){box.classList.add("empty");}else{box.classList.remove("empty");}
    box.classList.toggle("hi",hi);
    if(prev!==val){box.classList.remove("pop");void box.offsetWidth;box.classList.add("pop");}
  }
  function render(prev){
    var s=steps[i],p=prev!=null?steps[prev]:{name:null,math:null,out:[]};
    one(nameB,nameV,s.name,s.hi.indexOf("name")>=0,p.name);
    one(mathB,mathV,s.math,s.hi.indexOf("math")>=0,p.math);
    for(var q=0;q<srclns.length;q++){srclns[q].classList.toggle("hi",srclns[q].getAttribute("data-ln")===String(s.ln));}
    cap.textContent=s.cap;
    var prevLen=(p.out||[]).length; out.innerHTML="";
    if(s.out.length===0){var ph=document.createElement("div");ph.className="vs-outph";ph.textContent="（還沒有 print 輸出）";out.appendChild(ph);}
    else{for(var j=0;j<s.out.length;j++){var l=document.createElement("div");l.className="vs-outline"+(j>=prevLen?" fresh":"");l.textContent=s.out[j];out.appendChild(l);}}
    next.textContent=(i>=steps.length-1)?"✓ 完成":"下一步 ▶"; next.disabled=(i>=steps.length-1);
  }
  next.addEventListener("click",function(){if(i<steps.length-1){var pv=i;i++;render(pv);}});
  reset.addEventListener("click",function(){var pv=i;i=0;render(pv);});
  render(null);
})();
</script>
<div class="reveal" onclick="toggleWork(this)"><span class="wk-arrow">▶</span> 📜 想看看舊寫法 <code>%</code> 和 <code>.format()</code> 嗎？（了解就好，平常一律用 f-string）</div>
<div class="answer">
<p style="margin-top:0">在 f-string 出現前，Python 用 <code>%</code>（最舊）和 <code>.format()</code> 來格式化。同樣一句「阿翔數學成績 69.00」，三種寫法對照：</p>
''' + R('''name = "阿翔"
math = 69

# 舊寫法 1：%（最舊）
print("%s數學成績%6.2f" % (name, math))

# 舊寫法 2：.format()
print("{}數學成績{:6.2f}".format(name, math))

# 推薦：f-string（最直覺，變數直接寫在字串裡）
print(f"{name}數學成績{math:6.2f}")''') + '''
<p style="margin-bottom:0">三種印出來完全一樣，但 f-string <strong>最好讀、最不容易寫錯</strong>——所以本課之後<strong>一律用 f-string</strong>，另外兩種看得懂就好。</p></div>
''') + exercise("課堂練習", '''
<ol>
  <li><code>input()</code> 讀進來的資料是什麼型別？要當數字算，該怎麼做？</li>
  <li>寫一行 <code>print()</code>，讓 <code>100</code> 和 <code>60</code> 中間用 <code>&amp;</code> 分隔、結尾不換行。</li>
  <li>用 f-string 把 <code>3.14159</code> 印成寬度 8、保留 2 位小數、靠右對齊。</li>
</ol>''', '''
<ol>
<li>字串（str）；要先用 <code>int()</code> 或 <code>float()</code> 轉型別，例如 <code>int(input())</code>。</li>
<li><code>print(100, 60, sep="&", end="")</code>。</li>
<li><code>print(f"{3.14159:>8.2f}")</code>。</li>
</ol>''')


# =====================================================================
# 單元 14：Python（三）運算子　（顯示為單元 10）
# =====================================================================
BODIES["unit14"] = hero("unit14") + goals([
    "認識算術、比較、邏輯三大類運算子",
    "認識身分（is）與成員（in）運算子",
    "會用複合指定運算子（+=、-= …）簡化寫法",
    "能用運算子解決 BMI、判斷奇數等小問題",
]) + sec(1, "算術運算子", '''
<p><code>+</code> 加、<code>-</code> 減、<code>*</code> 乘、<code>/</code> 除、<code>%</code> 餘數、<code>//</code> 商（整數除）、<code>**</code> 指數。</p>
''' + R('''a = 5
b = 2
print(a + b)   # 加 → 7
print(a - b)   # 減 → 3
print(a * b)   # 乘 → 10
print(a / b)   # 除 → 2.5
print(a % b)   # 餘數 → 1
print(a // b)  # 商數 → 2
print(a ** b)  # 指數 → 25''') + '''
<h3>應用：BMI 計算</h3>
''' + R('''w = float(input("體重(KG):"))
h = float(input("身高(CM):"))
print(f"BMI:{w/((h/100)**2):.2f}")''') + '''
''') + sec(2, "比較運算子", '''
<p><code>==</code> 等於、<code>!=</code> 不等於、<code>&gt;</code>、<code>&gt;=</code>、<code>&lt;</code>、<code>&lt;=</code>。比較的結果是<strong>布林值 True／False</strong>。</p>
''' + R('''a = 5
b = 2
print(a == b)  # a 等於 b？ False
print(a != b)  # a 不等於 b？ True
print(a >= b)  # a 大於等於 b？ True
print(a < b)   # a 小於 b？ False''') + '''
<h3>應用：判斷奇數</h3>
''' + R('''a = int(input("請輸入一個數:"))
print(f"{a}是否為奇數:{a % 2 == 1}")''') + '''
''') + sec(3, "邏輯運算子", '''
<p><code>not</code>（否定）、<code>and</code>（且）、<code>or</code>（或），常用來把多個條件組合起來。</p>
''' + R('''a = 5
b = 2
c = 3
print((a > b) and (b > c))  # a>b 且 b>c → False
print((a > b) or (b > c))   # a>b 或 b>c → True
print(not (a > b))          # 否定 a>b → False''') + '''
''') + sec(4, "身分與成員運算子", '''
<p><code>is</code>：兩個變數是不是<strong>指向同一個物件</strong>。<code>in</code>：某個元素<strong>在不在容器裡</strong>。</p>
''' + R('''a = [1, 2, 3]
b = [1, 2, 3]
c = a
print(b is a)      # b 和 a 是同一個物件嗎？ False
print(c is a)      # c 和 a 是同一個物件嗎？ True
print(b is not a)  # b 和 a 不同物件嗎？ True
print(1 in a)      # 1 在 a 裡面嗎？ True
print(4 in a)      # 4 在 a 裡面嗎？ False
print(4 not in a)  # 4 不在 a 裡面嗎？ True''') + '''
<div class="callout"><span class="t">🔎 == 和 is 差在哪？</span>
<p><code>==</code> 比的是「<strong>值一不一樣</strong>」；<code>is</code> 比的是「<strong>是不是同一個物件</strong>」。上面 <code>a</code> 和 <code>b</code> 值一樣，但它們是兩個不同的串列，所以 <code>b is a</code> 是 False。</p></div>
<div class="callout"><span class="t">🧮 <code>in</code> 就像數學的「集合」</span>
<p>數學裡我們會問「某個東西<strong>屬不屬於</strong>一個集合」，寫成 <code>3 ∈ {1, 2, 3}</code>（讀作「3 屬於這個集合」）。Python 的 <code>in</code> 就是同一個概念：<code>3 in [1, 2, 3]</code> 就是在問「<strong>3 在不在這堆資料裡</strong>」，答案是 <code>True</code>。所以 <code>x in 資料</code> 可以直接讀成「<strong>x 屬於這堆資料嗎？</strong>」，<code>not in</code> 就是「不屬於」。它能用在串列、字串、字典等各種容器，例如 <code>"a" in "cat"</code> 也會是 <code>True</code>。</p></div>
''') + sec(5, "複合指定運算子", '''
<p>把「運算」和「指定」合在一起的簡寫：<code>+=</code>、<code>-=</code>、<code>*=</code>、<code>/=</code>、<code>%=</code>、<code>//=</code>、<code>**=</code>。例如 <code>a += b</code> 等同 <code>a = a + b</code>。</p>
''' + R('''a = 5
b = 2
a += b
print(a)   # a = a + b  → 7
a -= b
print(a)   # a = a - b  → 5
a *= b
print(a)   # a = a * b  → 10
a /= b
print(a)   # a = a / b  → 5.0
a //= b
print(a)   # a = a // b → 2.0
a %= b
print(a)   # a = a % b  → 0.0''') + '''
<p style="margin:10px 0 2px;color:var(--text-soft);font-size:.9rem">👇 每個複合指定其實都是「先算、再存回 a」。點「下一步」一步一步看 a 怎麼變：</p>
<div class="varstep" id="cstep">
  <div class="vs-stage">
    <div class="vs-boxes">
      <div class="vs-box empty" id="cs-a"><span class="vs-name">a</span><span class="vs-val"></span></div>
      <div class="vs-box empty" id="cs-b"><span class="vs-name">b</span><span class="vs-val"></span></div>
    </div>
    <div class="vs-calc" id="cs-calc"></div>
  </div>
  <div class="vs-cc"><div class="vs-srccard">
    <div class="vs-srchead"><span class="vsdot r"></span><span class="vsdot y"></span><span class="vsdot g"></span><span class="vs-srclabel">複合指定.py　—　目前執行的那一行會反白</span></div>
    <div class="vs-src">
      <div class="vs-ln" data-ln="0">a = 5</div>
      <div class="vs-ln" data-ln="1">b = 2</div>
      <div class="vs-ln" data-ln="2">a += b</div>
      <div class="vs-ln" data-ln="2">print(a)   # a = a + b  → 7</div>
      <div class="vs-ln" data-ln="3">a -= b</div>
      <div class="vs-ln" data-ln="3">print(a)   # a = a - b  → 5</div>
      <div class="vs-ln" data-ln="4">a *= b</div>
      <div class="vs-ln" data-ln="4">print(a)   # a = a * b  → 10</div>
      <div class="vs-ln" data-ln="5">a /= b</div>
      <div class="vs-ln" data-ln="5">print(a)   # a = a / b  → 5.0</div>
      <div class="vs-ln" data-ln="6">a //= b</div>
      <div class="vs-ln" data-ln="6">print(a)   # a = a // b → 2.0</div>
      <div class="vs-ln" data-ln="7">a %= b</div>
      <div class="vs-ln" data-ln="7">print(a)   # a = a % b  → 0.0</div>
    </div>
  </div>
    <div class="vs-console"><div class="vs-console-h">🖥️ 程式輸出</div><div class="vs-console-body" id="cs-out"></div></div>
  </div>
  <div class="vs-cap" id="cs-cap">點「下一步 ▶」開始：看每個複合指定怎麼「先算、再存回 a」。</div>
  <div class="vs-controls">
    <button type="button" class="vs-btn" id="cs-next">下一步 ▶</button>
    <button type="button" class="vs-btn ghost" id="cs-reset">↺ 重來</button>
  </div>
</div>
<script>
(function(){
  var root=document.getElementById("cstep"); if(!root) return;
  var steps=[
    {a:"",b:"",ln:-1,calc:"",cap:"點「下一步 ▶」開始：看每個複合指定怎麼「先算、再存回 a」。",hi:[],out:[]},
    {a:"5",b:"",ln:0,calc:"",cap:"把 5 放進 a。",hi:["a"],out:[]},
    {a:"5",b:"2",ln:1,calc:"",cap:"把 2 放進 b。之後 b 一直是 2。",hi:["b"],out:[]},
    {a:"7",b:"2",ln:2,calc:"a += b → a = a + b = 5 + 2 = 7",cap:"a += b 等同 a = a + b。印出 7。",hi:["a"],out:["7"]},
    {a:"5",b:"2",ln:3,calc:"a -= b → a = a - b = 7 - 2 = 5",cap:"a -= b 等同 a = a - b。印出 5。",hi:["a"],out:["7","5"]},
    {a:"10",b:"2",ln:4,calc:"a *= b → a = a * b = 5 * 2 = 10",cap:"a *= b 等同 a = a * b。印出 10。",hi:["a"],out:["7","5","10"]},
    {a:"5.0",b:"2",ln:5,calc:"a /= b → a = a / b = 10 / 2 = 5.0",cap:"a /= b 等同 a = a / b。注意：<code>/</code> 一定得到小數，所以是 5.0。",hi:["a"],out:["7","5","10","5.0"]},
    {a:"2.0",b:"2",ln:6,calc:"a //= b → a = a // b = 5.0 // 2 = 2.0",cap:"a //= b 是「整數除法」。但因為 a 已經是小數 5.0，結果也是小數 2.0。",hi:["a"],out:["7","5","10","5.0","2.0"]},
    {a:"0.0",b:"2",ln:7,calc:"a %= b → a = a % b = 2.0 % 2 = 0.0",cap:"a %= b 是「取餘數」。2.0 除以 2 剛好整除，餘數 0.0。程式跑完囉！",hi:["a"],out:["7","5","10","5.0","2.0","0.0"]}
  ];
  var i=0;
  var aB=document.getElementById("cs-a"),bB=document.getElementById("cs-b");
  var aV=aB.querySelector(".vs-val"),bV=bB.querySelector(".vs-val");
  var calc=document.getElementById("cs-calc"),cap=document.getElementById("cs-cap"),out=document.getElementById("cs-out");
  var srclns=root.querySelectorAll(".vs-ln");
  var next=document.getElementById("cs-next"),reset=document.getElementById("cs-reset");
  function one(box,el,val,hi,prev){
    el.textContent=val;
    if(val===""){box.classList.add("empty");}else{box.classList.remove("empty");}
    box.classList.toggle("hi",hi);
    if(prev!==val){box.classList.remove("pop");void box.offsetWidth;box.classList.add("pop");}
  }
  function render(prev){
    var s=steps[i],p=prev!=null?steps[prev]:{a:null,b:null,out:[]};
    one(aB,aV,s.a,s.hi.indexOf("a")>=0,p.a);
    one(bB,bV,s.b,s.hi.indexOf("b")>=0,p.b);
    for(var q=0;q<srclns.length;q++){srclns[q].classList.toggle("hi",srclns[q].getAttribute("data-ln")===String(s.ln));}
    calc.textContent=s.calc;calc.style.visibility=s.calc?"visible":"hidden";
    cap.innerHTML=s.cap;
    var prevLen=(p.out||[]).length; out.innerHTML="";
    if(s.out.length===0){var ph=document.createElement("div");ph.className="vs-outph";ph.textContent="（還沒有 print 輸出）";out.appendChild(ph);}
    else{for(var j=0;j<s.out.length;j++){var l=document.createElement("div");l.className="vs-outline"+(j>=prevLen?" fresh":"");l.textContent=s.out[j];out.appendChild(l);}}
    next.textContent=(i>=steps.length-1)?"✓ 完成":"下一步 ▶"; next.disabled=(i>=steps.length-1);
  }
  next.addEventListener("click",function(){if(i<steps.length-1){var pv=i;i++;render(pv);}});
  reset.addEventListener("click",function(){var pv=i;i=0;render(pv);});
  render(null);
})();
</script>
<div class="callout"><span class="t">🔎 為什麼後面 a 一直是「小數」？</span>
<p>Python 的變數<strong>沒有固定型別</strong>，型別是看它「<strong>目前存的值</strong>」。上面從 <code>a /= b</code> 開始，因為<strong>除法 <code>/</code> 一定回傳浮點數（小數）</strong>，<code>a</code> 就變成 <code>float</code>；之後 <code>a //= b</code>、<code>a %= b</code> 都是「浮點數和整數」一起算，結果<strong>還是浮點數</strong>，所以印出來是 <code>2.0</code>、<code>0.0</code> 這種帶小數點的。</p>
<p style="margin-bottom:0">要注意：這<strong>不是「這個變數名從此永遠是浮點數」</strong>。Python 只看目前的值——只要之後再存一個整數（例如 <code>a = 7</code>），<code>a</code> 就又變回 <code>int</code> 了。</p></div>
''') + exercise("課堂練習", '''
<ol>
  <li><code>7 // 2</code> 和 <code>7 % 2</code> 各是多少？<code>2 ** 5</code> 呢？</li>
  <li>用比較與邏輯運算子，寫出「a 是不是介於 1 到 100 之間」的判斷式。</li>
  <li><code>a = 10</code>，執行 <code>a *= 3</code> 後 <code>a</code> 是多少？</li>
</ol>''', '''
<ol>
<li><code>7 // 2 = 3</code>（商）、<code>7 % 2 = 1</code>（餘數）、<code>2 ** 5 = 32</code>。</li>
<li><code>(a >= 1) and (a <= 100)</code>。</li>
<li><code>a = 30</code>（等同 <code>a = a * 3</code>）。</li>
</ol>''')
