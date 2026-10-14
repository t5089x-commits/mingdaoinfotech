/* ===================================================================
   資訊安全導論 · 虛擬貨幣交易所（課堂模擬）  —— 後端 Apps Script
   作者：陳楷翔 老師的教材網站　｜　這支程式貼進 Google Apps Script 使用
   -------------------------------------------------------------------
   這是一個「課堂模擬」用的後端：全班同學用學號＋PIN 登入，用虛擬美元
   買賣 BTC／ETH（真實市場即時價格），老師可以一鍵開關「交易時段」與
   「資安事件（釣魚演練）」。所有資料都存在這份試算表裡，打開就是報表。

   ⚠ 這是教學用系統，不是真正的金融系統，也不是真正的身分認證：
      - 幣是虛擬的、錢是虛擬的，不涉及任何真實金流。
      - 學號＋PIN 只是「課堂等級」的防止非本人操作，擋得住同學隨手冒用，
        但擋不住真的想破解的人 —— 這件事本身就是課程要教的（前端身分 vs
        真實認證）。正式系統請用 OAuth／Passkey 等機制。

   【釣魚演練的安全設計 · 很重要】
      資安事件是一個「資安意識演練」：假廣告→假頁面→教學揭露。
      這支後端在整個流程中「絕對不會收取、也不會儲存任何密碼內容」。
      學生在假頁面輸入框打的字，前端根本不會送出來；後端只記錄「這位學號
      點了、送了這個動作」，用來上課檢討，並套用遊戲內後果（虛擬美元被
      模擬駭客轉走）。詳見 phishSubmit()。
   =================================================================== */

/* ---------- 一次性設定：第一次使用請在試算表選單執行 setupSheets() ---------- */

function setupSheets() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  ensureSheet(ss, '名冊', ['學號','姓名','PIN','起始資金USD','班級']);
  ensureSheet(ss, '帳戶', ['學號','姓名','現金USD','BTC數量','ETH數量','已中招關卡(USDT/BTC/ETH)','最後更新']);
  ensureSheet(ss, '交易紀錄', ['時間','學號','姓名','買/賣','幣種','數量','成交價USD','金額USD','成交後現金USD','備註','下單理由（學生填）']);
  ensureSheet(ss, '事件紀錄', ['時間','學號','姓名','事件','說明','影響金額USD']);
  var settings = ensureSheet(ss, '設定', ['參數','值','說明']);
  // 用 ensureSetting_ 逐一補齊：之後程式新增參數，再跑一次本功能就會補上缺的列，不會覆蓋你已改的值
  ensureSetting_(settings,'tradingOpen','FALSE','交易時段開關：TRUE=開放下單、FALSE=關閉（上課才打開）');
  ensureSetting_(settings,'eventUsdt','FALSE','特別活動① 現領USDT 這一關：TRUE=會出現（內容見老師設定說明.txt，刻意不寫明以免學生看後台就猜到）');
  ensureSetting_(settings,'eventBtc','FALSE','特別活動② 辨識領BTC 這一關：TRUE=會出現');
  ensureSetting_(settings,'eventEth','FALSE','特別活動③ 智能合約ETH 這一關：TRUE=會出現');
  ensureSetting_(settings,'startingCapital','100000','新同學的起始虛擬資金（USD）');
  ensureSetting_(settings,'phishBaitUSD','50000','假廣告號稱可以「免費領取」的投資金（USD）');
  ensureSetting_(settings,'phishTakePct','30','上鉤後現金與持倉(BTC/ETH)各被轉走的比例（%）');
  ensureSetting_(settings,'teacherPassword','au/62l4xu.62k6cj86','老師控制台密碼（請務必改成只有你知道的）');
  ensureSetting_(settings,'coins','BTC,ETH','可交易幣種（目前支援 BTC,ETH）');
  ensureSetting_(settings,'autoWindow','','（進階/可留空）自動交易時段，例如 3@14:00-16:00 代表每週三 14-16 點；留空=只用手動開關');
  ensureSheet(ss, '價格快取', ['幣種','最新價USD','更新時間']);
  SpreadsheetApp.getUi().alert('✅ 完成！已建立／檢查所有工作表。\n\n接下來：\n1. 到「名冊」貼上學號、姓名、PIN。\n2. 部署成網路應用程式（說明見設定檔）。');
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
/* 若「設定」裡還沒有這個參數，就補一列（不覆蓋已存在的值） */
function ensureSetting_(sh, key, val, desc) {
  var data = sh.getDataRange().getValues();
  for (var i=1;i<data.length;i++){ if (String(data[i][0]).trim()===key) return; }
  sh.appendRow([key, val, desc]);
}
function on_(v){ return String(v).toUpperCase()==='TRUE'; }

/* 選單：方便老師自己在試算表產生 PIN / 重設一輪 */
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
  var r = ui.alert('重設一輪','所有同學的帳戶會回到起始資金，交易紀錄會保留。確定嗎？', ui.ButtonSet.YES_NO);
  if (r !== ui.Button.YES) return;
  var acc = sheet_('帳戶');
  if (acc.getLastRow()>1) acc.getRange(2,1,acc.getLastRow()-1,acc.getLastColumn()).clearContent();
  toast_('已重設，所有人下次登入會重新拿到起始資金');
}

/* ---------- Web App 入口 ---------- */

function doGet(e) {
  // 健康檢查 / 價格查詢
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
  var sid = authStudent_(req);
  var acc = getAccount_(sid.sid);
  var roster = findRoster_(sid.sid);
  return {ok:true, name: sid.name, start: round2_(roster?roster.start:100000),
          account: acc, prices: getPrices_(), settings: publicSettings_()};
}

function order(req) {
  var au = authStudent_(req);
  var S = getSettings_();
  if (!tradingIsOpen_(S)) return {ok:false,error:'現在不是交易時段，老師還沒開放下單'};
  var side = (req.side==='sell') ? 'sell':'buy';
  var coin = String(req.coin||'').toUpperCase();
  if (coin!=='BTC' && coin!=='ETH') return {ok:false,error:'幣種只支援 BTC／ETH'};
  var reason = String(req.reason||'').trim();
  if (reason.length < 5) return {ok:false,error:'下單前請先寫下你的理由（至少 5 個字，可貼新聞連結或自己說明）'};
  if (reason.length > 500) reason = reason.slice(0,500);
  var prices = getPrices_();
  var price = (coin==='BTC') ? prices.btc : prices.eth;
  if (!price || price<=0) return {ok:false,error:'目前抓不到幣價，請稍後再試'};

  var lock = LockService.getScriptLock();
  lock.waitLock(8000);
  try {
    var acc = getAccount_(au.sid);
    var qty, usd;
    // 支援兩種下單：給金額(amountUSD) 或 給數量(qty)
    if (req.amountUSD != null) { usd = Number(req.amountUSD); qty = usd/price; }
    else if (req.qty != null)  { qty = Number(req.qty);       usd = qty*price; }
    else return {ok:false,error:'請輸入下單金額或數量'};
    if (!(qty>0) || !(usd>0)) return {ok:false,error:'數量／金額要大於 0'};

    if (side==='buy') {
      if (usd > acc.cash + 1e-9) return {ok:false,error:'現金不足（現有 $'+fmt_(acc.cash)+'）'};
      acc.cash -= usd;
      if (coin==='BTC') acc.btc += qty; else acc.eth += qty;
    } else {
      var have = (coin==='BTC')? acc.btc : acc.eth;
      if (qty > have + 1e-12) return {ok:false,error:'持有的 '+coin+' 不夠賣（現有 '+fmt8_(have)+'）'};
      acc.cash += usd;
      if (coin==='BTC') acc.btc -= qty; else acc.eth -= qty;
    }
    saveAccount_(acc);
    appendRow_('交易紀錄',[new Date(), au.sid, au.name, (side==='buy'?'買':'賣'), coin,
                           round8_(qty), round2_(price), round2_(usd), round2_(acc.cash), '', reason]);
    return {ok:true, account: acc, prices: prices, filled:{side:side,coin:coin,qty:round8_(qty),price:round2_(price),usd:round2_(usd)}};
  } finally { lock.releaseLock(); }
}

/* ---------- 資安事件（釣魚演練） ----------
   phishClick：學生點了假廣告（第 1 步，只記錄）
   phishSubmit：學生在假頁面「送出」了（完全上鉤，套用後果）
   ★ 前端不會把任何輸入框的內容送過來，這裡也不接收、不儲存任何密碼。 */

function anyEventOn_(S){ return on_(S.eventUsdt)||on_(S.eventBtc)||on_(S.eventEth); }
function eventFlagFor_(S, variant){ return variant==='btc'?S.eventBtc : (variant==='eth'?S.eventEth : S.eventUsdt); }

function phishClick(req) {
  var au = authStudent_(req);
  var S = getSettings_();
  if (!anyEventOn_(S)) return {ok:false,error:'目前沒有進行中的活動'};
  appendRow_('事件紀錄',[new Date(), au.sid, au.name, '點了假廣告', '看到「免費領取投資金」廣告並點進去', '']);
  return {ok:true, baitUSD: Number(S.phishBaitUSD||50000), events: publicSettings_().events};
}

function phishSubmit(req) {
  var au = authStudent_(req);
  var S = getSettings_();
  var variant = String(req.variant||'usdt').slice(0,20);
  if (!on_(eventFlagFor_(S, variant))) return {ok:false,error:'這個活動目前沒有開放'};
  var prices = getPrices_();
  var pct = Number(S.phishTakePct||30)/100;
  var lock = LockService.getScriptLock(); lock.waitLock(8000);
  try {
    var acc = getAccount_(au.sid);
    // 前提：BTC / ETH 關卡必須持有該幣才會中招（USDT 關不限）
    if (variant==='btc' && !(acc.btc>0)) return {ok:false, error:'nohold', need:'BTC'};
    if (variant==='eth' && !(acc.eth>0)) return {ok:false, error:'nohold', need:'ETH'};
    var caught = acc.caught ? acc.caught.split(',').filter(String) : [];
    if (caught.indexOf(variant) >= 0) {   // 同一關每人只會中招一次
      return {ok:true, already:true, lost:{cash:0,btc:0,eth:0}, lostUsd:0, pct:Math.round(pct*100), account:acc, prices:prices};
    }
    // 各關只扣「自己那種資產」的比例（預設 30%）：USDT關扣現金、BTC關扣BTC、ETH關扣ETH
    var lc=0, lb=0, le=0;
    if (variant==='btc')      lb = round8_(acc.btc * pct);
    else if (variant==='eth') le = round8_(acc.eth * pct);
    else                      lc = round2_(acc.cash * pct);
    acc.cash = round2_(acc.cash - lc);
    acc.btc  = round8_(acc.btc  - lb);
    acc.eth  = round8_(acc.eth  - le);
    caught.push(variant); acc.caught = caught.join(',');
    saveAccount_(acc);
    var usdTotal = round2_(lc + lb*prices.btc + le*prices.eth);
    var vname = variant==='btc' ? '辨識領BTC' : (variant==='eth' ? '智能合約ETH' : '現領USDT');
    appendRow_('事件紀錄',[new Date(), au.sid, au.name, '完全上鉤（'+vname+'）',
      '完成任務／按下領取 —— 系統只記錄這個動作，未收取任何輸入內容；被轉走 現金$'+lc+'、BTC '+lb+'、ETH '+le, -usdTotal]);
    appendRow_('交易紀錄',[new Date(), au.sid, au.name, '—', '—', '', '', usdTotal, round2_(acc.cash),
      '⚠ 特別活動('+vname+')：現金與持倉各被轉走 '+Math.round(pct*100)+'%', '']);
    return {ok:true, already:false, lost:{cash:lc,btc:lb,eth:le}, lostUsd:usdTotal, pct:Math.round(pct*100), account:acc, prices:prices};
  } finally { lock.releaseLock(); }
}

/* ---------- 老師 API ---------- */

function teacherLogin(req) {
  if (!teacherOk_(req)) return {ok:false,error:'老師密碼不正確'};
  return {ok:true, settings: getSettings_()};
}
function teacherSet(req) {
  if (!teacherOk_(req)) return {ok:false,error:'老師密碼不正確'};
  var allow = {tradingOpen:1, eventUsdt:1, eventBtc:1, eventEth:1, startingCapital:1, phishBaitUSD:1, phishTakePct:1};
  if (!allow[req.key]) return {ok:false,error:'不允許修改這個參數'};
  setSetting(req.key, String(req.value));
  return {ok:true, settings: getSettings_()};
}
function teacherReport(req) {
  if (!teacherOk_(req)) return {ok:false,error:'老師密碼不正確'};
  var prices = getPrices_();
  var rows = sheet_('帳戶').getDataRange().getValues(); rows.shift();
  var list = rows.filter(function(r){return r[0];}).map(function(r){
    var cash=Number(r[2])||0, btc=Number(r[3])||0, eth=Number(r[4])||0;
    var equity = cash + btc*prices.btc + eth*prices.eth;
    var raw=String(r[5]||''); if(raw==='TRUE'||raw==='FALSE')raw='';
    return {sid:r[0], name:r[1], cash:round2_(cash), btc:round8_(btc), eth:round8_(eth),
            equity:round2_(equity), caught: raw, phished: raw!==''};
  });
  list.sort(function(a,b){return b.equity-a.equity;});
  var phishedCount = list.filter(function(x){return x.phished;}).length;
  return {ok:true, prices:prices, leaderboard:list, phishedCount:phishedCount, total:list.length};
}

/* ---------- 工具：名冊 / 帳戶 / 設定 / 價格 / 權杖 ---------- */

function sheet_(n){ return SpreadsheetApp.getActiveSpreadsheet().getSheetByName(n); }
function appendRow_(n,row){ sheet_(n).appendRow(row); }

function findRoster_(sid){
  var data = sheet_('名冊').getDataRange().getValues();
  var S = getSettings_();
  for (var i=1;i<data.length;i++){
    if (String(data[i][0]).trim()===sid){
      return {sid:sid, name:data[i][1]||sid, pin:String(data[i][2]).replace(/^'/,''),
              start: Number(data[i][3]) || Number(S.startingCapital) || 100000};
    }
  }
  return null;
}
function getOrCreateAccount_(sid,name,start){
  var acc = getAccount_(sid);
  if (acc) return acc;
  var row = [sid,name,round2_(start),0,0,'',new Date()];
  sheet_('帳戶').appendRow(row);
  return {sid:sid,name:name,cash:round2_(start),btc:0,eth:0,caught:''};
}
function getAccount_(sid){
  var data = sheet_('帳戶').getDataRange().getValues();
  for (var i=1;i<data.length;i++){
    if (String(data[i][0]).trim()===sid){
      var raw=String(data[i][5]||''); if(raw==='TRUE'||raw==='FALSE')raw='';  // 相容舊的布林值
      return {sid:sid,name:data[i][1],cash:Number(data[i][2])||0,
              btc:Number(data[i][3])||0,eth:Number(data[i][4])||0,
              caught:raw, _row:i+1};
    }
  }
  return null;
}
function saveAccount_(acc){
  var sh=sheet_('帳戶'); var r=acc._row; var c=acc.caught||'';
  if (!r){ sh.appendRow([acc.sid,acc.name,round2_(acc.cash),round8_(acc.btc),round8_(acc.eth),c,new Date()]); return; }
  sh.getRange(r,3,1,5).setValues([[round2_(acc.cash),round8_(acc.btc),round8_(acc.eth),c,new Date()]]);
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
  return { tradingOpen: tradingIsOpen_(S),
           events: ev,
           anyEvent: ev.usdt||ev.btc||ev.eth,
           phishBaitUSD: Number(S.phishBaitUSD||50000) };
}
function tradingIsOpen_(S){
  if (String(S.tradingOpen).toUpperCase()==='TRUE') {
    // 若有設定 autoWindow，且現在不在時段內，仍視為關閉（進階，可留空）
    if (S.autoWindow) return inAutoWindow_(S.autoWindow);
    return true;
  }
  return false;
}
function inAutoWindow_(spec){
  // 格式 例：3@14:00-16:00  (週幾 1-7 @ 起-迄)；多段用逗號
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

function getPrices_(){
  var cache=CacheService.getScriptCache();
  var hit=cache.get('prices');
  if (hit){ try{return JSON.parse(hit);}catch(e){} }
  var p=fetchPrices_();
  if (p){ cache.put('prices', JSON.stringify(p), 60); writePriceCache_(p); return p; }
  // 抓不到就用試算表上一次的快取
  return readPriceCache_();
}
function fetchPrices_(){
  try{
    var url='https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd';
    var res=UrlFetchApp.fetch(url,{muteHttpExceptions:true});
    if (res.getResponseCode()!==200) return null;
    var d=JSON.parse(res.getContentText());
    return {btc:d.bitcoin.usd, eth:d.ethereum.usd, asof:new Date().toISOString()};
  }catch(e){ return null; }
}
function writePriceCache_(p){
  try{ var sh=sheet_('價格快取');
    sh.getRange(2,1,2,3).setValues([['BTC',p.btc,new Date()],['ETH',p.eth,new Date()]]);
  }catch(e){}
}
function readPriceCache_(){
  try{ var d=sheet_('價格快取').getDataRange().getValues();
    var o={btc:0,eth:0,asof:null};
    for(var i=1;i<d.length;i++){ if(d[i][0]==='BTC')o.btc=Number(d[i][1]); if(d[i][0]==='ETH')o.eth=Number(d[i][1]); if(d[i][2])o.asof=d[i][2]; }
    return o;
  }catch(e){ return {btc:0,eth:0,asof:null}; }
}

function teacherOk_(req){ var S=getSettings_(); return String(req.teacherPassword||'')===String(S.teacherPassword||''); }

/* 課堂等級權杖：hash(學號+PIN+試算表ID)。不是強認證，足夠擋同學隨手冒用。 */
function makeToken_(sid,pin){
  var secret=SpreadsheetApp.getActiveSpreadsheet().getId();
  var raw=sid+'|'+pin+'|'+secret;
  var bytes=Utilities.computeDigest(Utilities.DigestAlgorithm.SHA_256, raw);
  return Utilities.base64EncodeWebSafe(bytes).slice(0,22);
}
function authStudent_(req){
  var sid=String(req.sid||'').trim();
  var roster=findRoster_(sid);
  if(!roster) throw '查無此學號';
  if(String(req.token||'')!==makeToken_(sid, String(roster.pin).trim())) throw '登入已失效，請重新登入';
  return {sid:sid, name:roster.name};
}

/* ---------- 小工具 ---------- */
function json_(o){ return ContentService.createTextOutput(JSON.stringify(o)).setMimeType(ContentService.MimeType.JSON); }
function round2_(n){ return Math.round((Number(n)||0)*100)/100; }
function round8_(n){ return Math.round((Number(n)||0)*1e8)/1e8; }
function fmt_(n){ return (Number(n)||0).toFixed(2); }
function fmt8_(n){ return (Number(n)||0).toFixed(8); }
