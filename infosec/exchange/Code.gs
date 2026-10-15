/* ===================================================================
   資訊安全導論 · 幣圈模擬交易所（課堂模擬）  —— 後端 Apps Script
   作者：陳楷翔 老師的教材網站　｜　這支程式貼進 Google Apps Script 使用
   -------------------------------------------------------------------
   幣種模型：起始資金是「台幣 TWD」，學生可自由把 TWD 兌換成
             USDT／BTC／ETH 三種幣（以 CoinGecko 的即時台幣報價成交）。
   資料全部存在這份試算表裡，打開就是報表。

   ⚠ 教學用系統，不是真正金融系統：幣與錢都是虛擬的，不涉及任何真實金流。
     學號＋PIN 只是課堂等級的防止非本人操作（這本身就是課程要教的）。

   【特別活動＝釣魚演練 · 安全設計】
     三個關卡（USDT／BTC／ETH）各自獨立開關。整個流程「絕不收取、也不儲存
     任何密碼內容」：學生在假頁面打的字，前端根本不會送出來；後端只記錄
     「這位學號完成了這個動作」並套用遊戲內後果。
   =================================================================== */

/* ---------- 一次性設定：第一次使用請執行 setupSheets() ---------- */

function setupSheets() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  ensureSheet(ss, '名冊', ['學號','姓名','PIN','起始資金TWD','班級']);
  ensureSheet(ss, '帳戶', ['學號','姓名','TWD現金','USDT數量','BTC數量','ETH數量','已中招關卡(USDT/BTC/ETH)','最後更新']);
  ensureSheet(ss, '交易紀錄', ['時間','學號','姓名','買/賣','幣種','數量','成交價TWD','金額TWD','成交後TWD現金','備註','下單理由（學生填）']);
  ensureSheet(ss, '事件紀錄', ['時間','學號','姓名','事件','說明','影響金額TWD']);
  var settings = ensureSheet(ss, '設定', ['參數','值','說明']);
  ensureSetting_(settings,'tradingOpen','FALSE','交易時段開關：TRUE=開放下單、FALSE=關閉（上課才打開）');
  ensureSetting_(settings,'eventUsdt','FALSE','特別活動① 現領USDT 這一關：TRUE=會出現（內容見老師設定說明.txt）');
  ensureSetting_(settings,'eventBtc','FALSE','特別活動② 領BTC 這一關：TRUE=會出現');
  ensureSetting_(settings,'eventEth','FALSE','特別活動③ 智能合約ETH 這一關：TRUE=會出現');
  ensureSetting_(settings,'startingCapital','1000000','新同學的起始虛擬資金（TWD 台幣）');
  ensureSetting_(settings,'phishBait','50000','假廣告號稱可以「免費領取」的投資金（顯示用數字）');
  ensureSetting_(settings,'phishTakePct','30','上鉤後被偷走「該關那種幣」的比例（%）');
  ensureSetting_(settings,'teacherPassword','au/62l4xu.62k6cj86','老師控制台密碼（請務必改成只有你知道的）');
  ensureSetting_(settings,'coins','USDT,BTC,ETH','可交易幣種');
  ensureSetting_(settings,'autoWindow','','（進階/可留空）自動交易時段，例如 3@14:00-16:00；留空=只用手動開關');
  ensureSheet(ss, '價格快取', ['幣種','最新價TWD','更新時間']);
  SpreadsheetApp.getUi().alert('✅ 完成！已建立／檢查所有工作表。\n\n接下來：\n1. 到「名冊」貼上學號、姓名、PIN。\n2. 部署成網路應用程式（說明見設定檔）。\n\n⚠ 若你是從舊版（美元版）升級：請執行一次「⚠ 重設一輪」把帳戶清空，\n   讓大家用新的台幣模型重新開始。');
}

function ensureSheet(ss, name, headers) {
  var sh = ss.getSheetByName(name);
  if (!sh) sh = ss.insertSheet(name);
  if (sh.getLastRow() === 0) {
    sh.getRange(1,1,1,headers.length).setValues([headers]).setFontWeight('bold');
    sh.setFrozenRows(1);
  }
  return sh;
}
function ensureSetting_(sh, key, val, desc) {
  var data = sh.getDataRange().getValues();
  for (var i=1;i<data.length;i++){ if (String(data[i][0]).trim()===key) return; }
  sh.appendRow([key, val, desc]);
}
function on_(v){ return String(v).toUpperCase()==='TRUE'; }

/* 選單 */
function onOpen() {
  SpreadsheetApp.getUi()
    .createMenu('🏦 交易所管理')
    .addItem('① 初始化／檢查工作表', 'setupSheets')
    .addItem('② 幫名冊沒有 PIN 的人自動產生 4 位數 PIN', 'fillMissingPins')
    .addSeparator()
    .addItem('開啟交易時段', 'menuOpenTrading')
    .addItem('關閉交易時段', 'menuCloseTrading')
    .addItem('⛔ 關閉全部特別活動', 'menuAllEventsOff')
    .addSeparator()
    .addItem('⚠ 重設一輪（所有人回到起始資金）', 'resetRound')
    .addToUi();
}
function menuOpenTrading(){ setSetting('tradingOpen','TRUE');  toast_('交易時段已開啟'); }
function menuCloseTrading(){ setSetting('tradingOpen','FALSE'); toast_('交易時段已關閉'); }
function menuAllEventsOff(){ setSetting('eventUsdt','FALSE'); setSetting('eventBtc','FALSE'); setSetting('eventEth','FALSE'); toast_('已關閉全部特別活動'); }
function toast_(m){ SpreadsheetApp.getActiveSpreadsheet().toast(m,'交易所',4); }

function fillMissingPins() {
  var sh = sheet_('名冊'); var data = sh.getDataRange().getValues();
  for (var i=1;i<data.length;i++){
    if (data[i][0] && !data[i][2]) {
      var pin = ('000'+Math.floor(Math.random()*10000)).slice(-4);
      sh.getRange(i+1,3).setValue("'"+pin);
    }
  }
  toast_('已為沒有 PIN 的同學產生 4 位數 PIN');
}
function resetRound() {
  var ui = SpreadsheetApp.getUi();
  var r = ui.alert('重設一輪','所有同學的帳戶會回到起始資金（TWD），交易紀錄會保留。確定嗎？', ui.ButtonSet.YES_NO);
  if (r !== ui.Button.YES) return;
  var acc = sheet_('帳戶');
  if (acc.getLastRow()>1) acc.getRange(2,1,acc.getLastRow()-1,acc.getLastColumn()).clearContent();
  toast_('已重設，所有人下次登入會重新拿到起始資金');
}

/* ---------- Web App 入口 ---------- */
function doGet(e) {
  var action = (e && e.parameter && e.parameter.action) || 'ping';
  if (action === 'prices') return json_({ ok:true, prices: getPrices_() });
  return json_({ ok:true, service:'infosec-exchange', time:new Date().toISOString() });
}
function doPost(e) {
  var req = {};
  try { req = JSON.parse(e.postData.contents || '{}'); } catch (err) { return json_({ok:false,error:'bad_json'}); }
  var action = req.action || '';
  try {
    switch (action) {
      case 'login':         return json_(login(req));
      case 'state':         return json_(state(req));
      case 'order':         return json_(order(req));
      case 'history':       return json_(history(req));
      case 'board':         return json_(board(req));
      case 'phishClick':    return json_(phishClick(req));
      case 'phishSubmit':   return json_(phishSubmit(req));
      case 'teacherLogin':  return json_(teacherLogin(req));
      case 'teacherSet':    return json_(teacherSet(req));
      case 'teacherReport': return json_(teacherReport(req));
      default:              return json_({ok:false,error:'unknown_action'});
    }
  } catch (err) {
    return json_({ ok:false, error:'server_error', detail: String(err) });
  }
}

/* ---------- 學生 API ---------- */
function login(req) {
  var sid = String(req.sid||'').trim();
  var pin = String(req.pin||'').trim();
  if (!sid || !pin) return {ok:false,error:'缺少學號或 PIN'};
  var roster = findRoster_(sid);
  if (!roster) return {ok:false,error:'查無此學號，請確認或問老師'};
  if (String(roster.pin).trim() !== pin) return {ok:false,error:'PIN 不正確'};
  var acc = getOrCreateAccount_(sid, roster.name, roster.start);
  return {ok:true, token: makeToken_(sid, pin), name: roster.name, start: round2_(roster.start),
          account: acc, prices: getPrices_(), settings: publicSettings_()};
}
function state(req) {
  var au = authStudent_(req);
  var acc = getAccount_(au.sid);
  var roster = findRoster_(au.sid);
  return {ok:true, name: au.name, start: round2_(roster?roster.start:1000000),
          account: acc, prices: getPrices_(), settings: publicSettings_()};
}

function coinPriceInQuote_(p, coin, quote){
  if (quote==='TWD') return priceOf_(p, coin);        // coin 的台幣價
  if (coin==='BTC') return p.usdt ? p.btc/p.usdt : 0; // coin 的 USDT 價 = 台幣價 / USDT台幣價
  if (coin==='ETH') return p.usdt ? p.eth/p.usdt : 0;
  return 0;
}
function order(req) {
  var au = authStudent_(req);
  var S = getSettings_();
  if (!tradingIsOpen_(S)) return {ok:false,error:'現在不是交易時段，老師還沒開放下單'};
  var coin = String(req.coin||'').toUpperCase();
  if (coin!=='USDT' && coin!=='BTC' && coin!=='ETH') return {ok:false,error:'幣種只支援 USDT／BTC／ETH'};
  var quote = String(req.quote||'TWD').toUpperCase();
  if (coin==='USDT') quote='TWD';                 // USDT 只能跟台幣兌換
  if (quote!=='TWD' && quote!=='USDT') return {ok:false,error:'計價幣別只支援 TWD／USDT'};
  if (quote===coin) return {ok:false,error:'計價幣別不能跟購入幣種相同'};
  var reason = String(req.reason||'').trim();
  if (reason.length < 5) return {ok:false,error:'下單前請先寫下你的理由（至少 5 個字，可貼新聞連結或自己說明）'};
  if (reason.length > 500) reason = reason.slice(0,500);
  var side = (req.side==='sell') ? 'sell':'buy';
  var prices = getPrices_();
  var price = coinPriceInQuote_(prices, coin, quote);   // 1 個 coin 值多少「quote」
  if (!price || price<=0) return {ok:false,error:'目前抓不到幣價，請稍後再試'};

  var lock = LockService.getScriptLock(); lock.waitLock(8000);
  try {
    var acc = getAccount_(au.sid);
    var amount = Number(req.amount != null ? req.amount : req.amountTWD);   // 以 quote 計價
    if (!(amount>0)) return {ok:false,error:'金額要大於 0'};
    var qty = amount/price;
    var qbal = quote==='TWD' ? acc.twd : acc.usdt;    // 用來付款/收款的餘額

    if (side==='buy') {
      if (amount > qbal + 1e-6) return {ok:false,error:(quote==='TWD'?'台幣不足（現有 NT$'+fmt_(qbal)+'）':'USDT 不足（現有 '+qbal.toFixed(2)+' USDT）')};
      if (quote==='TWD') acc.twd -= amount; else addCoin_(acc,'USDT',-amount);
      addCoin_(acc, coin, qty);
    } else {
      var have = coinOf_(acc, coin);
      if (qty > have + 1e-12) return {ok:false,error:'持有的 '+coin+' 不夠賣（現有 '+fmt8_(have)+'）'};
      addCoin_(acc, coin, -qty);
      if (quote==='TWD') acc.twd += amount; else addCoin_(acc,'USDT',amount);
    }
    saveAccount_(acc);
    var note = quote==='USDT' ? '以USDT計價' : '';
    appendRow_('交易紀錄',[new Date(), au.sid, au.name, (side==='buy'?'買':'賣'), coin,
                           round8_(qty), round2_(price), round2_(amount), round2_(acc.twd), note, reason]);
    return {ok:true, account: acc, prices: prices,
            filled:{side:side, coin:coin, quote:quote, qty:round8_(qty), price:round2_(price), amount:round2_(amount)}};
  } finally { lock.releaseLock(); }
}

/* 這位學生的完整歷史交易紀錄（含被詐騙那幾筆） */
function history(req) {
  var au = authStudent_(req);
  var data = sheet_('交易紀錄').getDataRange().getValues();
  var out = [];
  for (var i=1;i<data.length;i++){
    if (String(data[i][1]).trim()===au.sid){
      out.push({ t: fmtTime_(data[i][0]), act:data[i][3], coin:data[i][4],
                 qty:data[i][5], price:data[i][6], amt:data[i][7], note:data[i][9] });
    }
  }
  out.reverse();            // 新的在前
  return {ok:true, rows: out.slice(0,200)};
}

/* 全班持有資產排行榜（學生可看；姓名遮罩成 劉O華） */
function board(req) {
  authStudent_(req);        // 要登入才能看
  var prices = getPrices_();
  var rows = sheet_('帳戶').getDataRange().getValues(); rows.shift();
  var list = rows.filter(function(r){return r[0];}).map(function(r){
    var acc = {twd:Number(r[2])||0, usdt:Number(r[3])||0, btc:Number(r[4])||0, eth:Number(r[5])||0};
    return { sid:String(r[0]), name: maskName_(r[1]), twd: round2_(equityTWD_(acc, prices)) };
  });
  list.sort(function(a,b){return b.twd-a.twd;});
  return {ok:true, board:list, asof:prices.asof};
}

/* ---------- 特別活動（釣魚演練） ---------- */
function anyEventOn_(S){ return on_(S.eventUsdt)||on_(S.eventBtc)||on_(S.eventEth); }
function eventFlagFor_(S, v){ return v==='btc'?S.eventBtc : (v==='eth'?S.eventEth : S.eventUsdt); }

function phishClick(req) {
  var au = authStudent_(req);
  var S = getSettings_();
  if (!anyEventOn_(S)) return {ok:false,error:'目前沒有進行中的活動'};
  appendRow_('事件紀錄',[new Date(), au.sid, au.name, '點了假廣告', '看到「免費領取投資金」廣告並點進去', '']);
  return {ok:true, baitUSD: Number(S.phishBait||50000), events: publicSettings_().events};
}

function phishSubmit(req) {
  var au = authStudent_(req);
  var S = getSettings_();
  var variant = String(req.variant||'usdt').slice(0,20);
  if (!on_(eventFlagFor_(S, variant))) return {ok:false,error:'這個活動目前沒有開放'};
  var coin = variant==='btc'?'BTC':(variant==='eth'?'ETH':'USDT');
  var prices = getPrices_();
  var pct = Number(S.phishTakePct||30)/100;
  var lock = LockService.getScriptLock(); lock.waitLock(8000);
  try {
    var acc = getAccount_(au.sid);
    // 前提：要持有該幣才能參加（沒有的話擋下，提示去取得）
    if (!(coinOf_(acc, coin) > 0)) return {ok:false, error:'nohold', need:coin};
    var caught = acc.caught ? acc.caught.split(',').filter(String) : [];
    if (caught.indexOf(variant) >= 0) {
      return {ok:true, already:true, lost:0, lostTWD:0, coin:coin, pct:Math.round(pct*100), account:acc, prices:prices};
    }
    var lost = round8_(coinOf_(acc, coin) * pct);     // 只偷「該關那種幣」的 30%
    addCoin_(acc, coin, -lost);
    caught.push(variant); acc.caught = caught.join(',');
    saveAccount_(acc);
    var lostTWD = round2_(lost * priceOf_(prices, coin));
    var vname = variant==='btc'?'領BTC':(variant==='eth'?'智能合約ETH':'現領USDT');
    appendRow_('事件紀錄',[new Date(), au.sid, au.name, '完全上鉤（'+vname+'）',
      '完成任務／按下領取 —— 系統只記錄這個動作，未收取任何輸入內容；被偷走 '+lost+' '+coin, -lostTWD]);
    appendRow_('交易紀錄',[new Date(), au.sid, au.name, '—', coin, round8_(lost), round2_(priceOf_(prices,coin)),
      round2_(lostTWD), round2_(acc.twd), '⚠ 特別活動('+vname+')：'+coin+' 被偷走 '+Math.round(pct*100)+'%', '']);
    return {ok:true, already:false, lost:lost, lostTWD:lostTWD, coin:coin, pct:Math.round(pct*100), account:acc, prices:prices};
  } finally { lock.releaseLock(); }
}

/* ---------- 老師 API ---------- */
function teacherLogin(req) {
  if (!teacherOk_(req)) return {ok:false,error:'老師密碼不正確'};
  return {ok:true, settings: getSettings_()};
}
function teacherSet(req) {
  if (!teacherOk_(req)) return {ok:false,error:'老師密碼不正確'};
  var allow = {tradingOpen:1, eventUsdt:1, eventBtc:1, eventEth:1, startingCapital:1, phishBait:1, phishTakePct:1};
  if (!allow[req.key]) return {ok:false,error:'不允許修改這個參數'};
  setSetting(req.key, String(req.value));
  return {ok:true, settings: getSettings_()};
}
function teacherReport(req) {
  if (!teacherOk_(req)) return {ok:false,error:'老師密碼不正確'};
  var prices = getPrices_();
  var rows = sheet_('帳戶').getDataRange().getValues(); rows.shift();
  var list = rows.filter(function(r){return r[0];}).map(function(r){
    var acc = {twd:Number(r[2])||0, usdt:Number(r[3])||0, btc:Number(r[4])||0, eth:Number(r[5])||0};
    var raw = String(r[6]||''); if(raw==='TRUE'||raw==='FALSE')raw='';
    return {sid:r[0], name:r[1], twd:round2_(acc.twd), usdt:round8_(acc.usdt), btc:round8_(acc.btc), eth:round8_(acc.eth),
            equity:round2_(equityTWD_(acc, prices)), caught:raw, phished: raw!==''};
  });
  list.sort(function(a,b){return b.equity-a.equity;});
  var phishedCount = list.filter(function(x){return x.phished;}).length;
  return {ok:true, prices:prices, leaderboard:list, phishedCount:phishedCount, total:list.length};
}

/* ---------- 帳戶 / 名冊 / 設定 ---------- */
function sheet_(n){ return SpreadsheetApp.getActiveSpreadsheet().getSheetByName(n); }
function appendRow_(n,row){ sheet_(n).appendRow(row); }

function coinOf_(acc, coin){ return coin==='BTC'?acc.btc : (coin==='ETH'?acc.eth : acc.usdt); }
function addCoin_(acc, coin, d){
  if (coin==='BTC') acc.btc = round8_(acc.btc + d);
  else if (coin==='ETH') acc.eth = round8_(acc.eth + d);
  else acc.usdt = round8_(acc.usdt + d);
}
function priceOf_(p, coin){ return coin==='BTC'?p.btc : (coin==='ETH'?p.eth : p.usdt); }
function equityTWD_(acc, p){ return acc.twd + acc.usdt*p.usdt + acc.btc*p.btc + acc.eth*p.eth; }

function findRoster_(sid){
  var data = sheet_('名冊').getDataRange().getValues();
  var S = getSettings_();
  for (var i=1;i<data.length;i++){
    if (String(data[i][0]).trim()===sid){
      return {sid:sid, name:data[i][1]||sid, pin:String(data[i][2]).replace(/^'/,''),
              start: Number(data[i][3]) || Number(S.startingCapital) || 1000000};
    }
  }
  return null;
}
function getOrCreateAccount_(sid,name,start){
  var acc = getAccount_(sid);
  if (acc) return acc;
  sheet_('帳戶').appendRow([sid,name,round2_(start),0,0,0,'',new Date()]);
  return {sid:sid,name:name,twd:round2_(start),usdt:0,btc:0,eth:0,caught:''};
}
function getAccount_(sid){
  var data = sheet_('帳戶').getDataRange().getValues();
  for (var i=1;i<data.length;i++){
    if (String(data[i][0]).trim()===sid){
      var raw=String(data[i][6]||''); if(raw==='TRUE'||raw==='FALSE')raw='';
      return {sid:sid,name:data[i][1],twd:Number(data[i][2])||0,usdt:Number(data[i][3])||0,
              btc:Number(data[i][4])||0,eth:Number(data[i][5])||0,caught:raw,_row:i+1};
    }
  }
  return null;
}
function saveAccount_(acc){
  var sh=sheet_('帳戶'); var r=acc._row; var c=acc.caught||'';
  var vals=[round2_(acc.twd),round8_(acc.usdt),round8_(acc.btc),round8_(acc.eth),c,new Date()];
  if (!r){ sh.appendRow([acc.sid,acc.name].concat(vals)); return; }
  sh.getRange(r,3,1,6).setValues([vals]);
}

function getSettings_(){
  var data = sheet_('設定').getDataRange().getValues(); var o={};
  for (var i=1;i<data.length;i++){ if(data[i][0]) o[String(data[i][0]).trim()]=String(data[i][1]).trim(); }
  return o;
}
function setSetting(key,val){
  var sh=sheet_('設定'); var data=sh.getDataRange().getValues();
  for (var i=1;i<data.length;i++){ if(String(data[i][0]).trim()===key){ sh.getRange(i+1,2).setValue(val); return; } }
  sh.appendRow([key,val,'']);
}
function publicSettings_(){
  var S=getSettings_();
  var ev={ usdt:on_(S.eventUsdt), btc:on_(S.eventBtc), eth:on_(S.eventEth) };
  return { tradingOpen: tradingIsOpen_(S), events: ev, anyEvent: ev.usdt||ev.btc||ev.eth,
           phishBait: Number(S.phishBait||50000) };
}
function tradingIsOpen_(S){
  if (on_(S.tradingOpen)) { if (S.autoWindow) return inAutoWindow_(S.autoWindow); return true; }
  return false;
}
function inAutoWindow_(spec){
  try{
    var now=new Date(); var dow=now.getDay()===0?7:now.getDay();
    var mins=now.getHours()*60+now.getMinutes();
    return spec.split(',').some(function(seg){
      var m=seg.trim().match(/^(\d)@(\d{1,2}):(\d{2})-(\d{1,2}):(\d{2})$/); if(!m)return false;
      if(Number(m[1])!==dow)return false;
      var a=Number(m[2])*60+Number(m[3]), b=Number(m[4])*60+Number(m[5]);
      return mins>=a && mins<=b;
    });
  }catch(e){ return true; }
}

/* ---------- 價格（CoinGecko，以台幣 TWD 計價，快取 60 秒） ---------- */
function getPrices_(){
  var cache=CacheService.getScriptCache();
  var hit=cache.get('pricesTWD');
  if (hit){ try{return JSON.parse(hit);}catch(e){} }
  var p=fetchPrices_();
  if (p){ cache.put('pricesTWD', JSON.stringify(p), 60); writePriceCache_(p); return p; }
  return readPriceCache_();
}
function fetchPrices_(){
  try{
    var url='https://api.coingecko.com/api/v3/simple/price?ids=tether,bitcoin,ethereum&vs_currencies=twd';
    var res=UrlFetchApp.fetch(url,{muteHttpExceptions:true});
    if (res.getResponseCode()!==200) return null;
    var d=JSON.parse(res.getContentText());
    return {usdt:d.tether.twd, btc:d.bitcoin.twd, eth:d.ethereum.twd, asof:new Date().toISOString()};
  }catch(e){ return null; }
}
function writePriceCache_(p){
  try{ sheet_('價格快取').getRange(2,1,3,3).setValues([['USDT',p.usdt,new Date()],['BTC',p.btc,new Date()],['ETH',p.eth,new Date()]]); }catch(e){}
}
function readPriceCache_(){
  try{ var d=sheet_('價格快取').getDataRange().getValues(); var o={usdt:0,btc:0,eth:0,asof:null};
    for(var i=1;i<d.length;i++){ var k=String(d[i][0]).toUpperCase();
      if(k==='USDT')o.usdt=Number(d[i][1]); if(k==='BTC')o.btc=Number(d[i][1]); if(k==='ETH')o.eth=Number(d[i][1]);
      if(d[i][2])o.asof=d[i][2]; }
    return o;
  }catch(e){ return {usdt:0,btc:0,eth:0,asof:null}; }
}

/* ---------- 權杖 / 工具 ---------- */
function teacherOk_(req){ var S=getSettings_(); return String(req.teacherPassword||'')===String(S.teacherPassword||''); }
function makeToken_(sid,pin){
  var secret=SpreadsheetApp.getActiveSpreadsheet().getId();
  var bytes=Utilities.computeDigest(Utilities.DigestAlgorithm.SHA_256, sid+'|'+pin+'|'+secret);
  return Utilities.base64EncodeWebSafe(bytes).slice(0,22);
}
function authStudent_(req){
  var sid=String(req.sid||'').trim();
  var roster=findRoster_(sid);
  if(!roster) throw '查無此學號';
  if(String(req.token||'')!==makeToken_(sid, String(roster.pin).trim())) throw '登入已失效，請重新登入';
  return {sid:sid, name:roster.name};
}
function maskName_(n){
  n=String(n||''); if(n.length<=1) return n;
  if(n.length===2) return n.charAt(0)+'O';
  return n.charAt(0)+'O'+n.charAt(n.length-1);
}
function fmtTime_(d){ try{ return Utilities.formatDate(new Date(d), Session.getScriptTimeZone()||'Asia/Taipei', 'MM/dd HH:mm'); }catch(e){ return String(d); } }
function json_(o){ return ContentService.createTextOutput(JSON.stringify(o)).setMimeType(ContentService.MimeType.JSON); }
function round2_(n){ return Math.round((Number(n)||0)*100)/100; }
function round8_(n){ return Math.round((Number(n)||0)*1e8)/1e8; }
function fmt_(n){ return (Number(n)||0).toFixed(0); }
function fmt8_(n){ return (Number(n)||0).toFixed(8); }
