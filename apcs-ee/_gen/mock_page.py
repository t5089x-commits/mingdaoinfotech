"""產生線上識讀模擬考：mock.html ＋ assets/mock-data.js（題目圖片與答案用密碼加密）。

用法（密碼不要寫進任何檔案）：
    MOCK_PASSWORD='你的密碼' python3 mock_page.py
沒有密碼就讀不到題目和答案；換密碼就是用新密碼重新執行一次。
"""
import os, sys, json, base64, secrets
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from lib import ROOT, HEAD, FOOT, E
import py125 as W
from mock_crop import crop_images

ITER = 250_000

def encrypt(obj, password):
    salt, iv = secrets.token_bytes(16), secrets.token_bytes(12)
    key = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=ITER).derive(password.encode("utf-8"))
    ct = AESGCM(key).encrypt(iv, json.dumps(obj, ensure_ascii=False).encode("utf-8"), None)
    b = lambda x: base64.b64encode(x).decode()
    return {"v": 1, "iter": ITER, "salt": b(salt), "iv": b(iv), "ct": b(ct)}

def main():
    pw = os.environ.get("MOCK_PASSWORD") or (sys.argv[1] if len(sys.argv) > 1 else "")
    if not pw:
        sys.exit("請用 MOCK_PASSWORD='密碼' python3 mock_page.py 執行（密碼不要寫進檔案）")
    imgs = crop_images(W.MOCK)
    data = {"title": "第 4 次課　程式識讀模擬考",
            "qs": [{"q": q, "d": W.DIFF[q], "img": "data:image/webp;base64," + base64.b64encode(imgs[q]).decode()} for q in W.MOCK],
            "ans": {str(q): W.ANS[q] for q in W.MOCK}}
    enc = encrypt(data, pw)
    os.makedirs(ROOT + "assets", exist_ok=True)
    open(ROOT + "assets/mock-data.js", "w", encoding="utf-8").write(
        "/* 識讀模擬考題目與答案（AES-GCM 加密，需要老師公布的密碼才能解開） */\nwindow.MOCK_ENC = " + json.dumps(enc) + ";\n")

    head = HEAD.split('<div class="goals">')[0].split('  <section class="unit-hero">')[0]
    s = head.format(title="識讀模擬考（線上作答）", crumb="識讀模擬考（線上作答）", unit="", extra_css='<link rel="stylesheet" href="assets/mock.css">\n')
    s = s.replace('<main class="wrap" data-unit="">', '<main class="wrap">')
    s += open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "mock_body.html"), encoding="utf-8").read()
    s += FOOT.format(prev='<a class="prev" href="schedule.html"><div class="dir">← 課程規劃</div><div class="ttl">第 4 次課</div></a>',
                     next='<a class="next" href="unit09.html"><div class="dir">考前複習 →</div><div class="ttl">識讀基本觀念與總整理</div></a>',
                     extra_js='<script src="assets/mock-data.js"></script>\n<script src="assets/mock.js"></script>\n')
    s = s.replace('<script src="assets/reading-viewer.js"></script>\n', '')
    open(ROOT + "mock.html", "w", encoding="utf-8").write(s)
    print("wrote mock.html, assets/mock-data.js", len(json.dumps(enc)) // 1024, "KB")

if __name__ == "__main__":
    main()
