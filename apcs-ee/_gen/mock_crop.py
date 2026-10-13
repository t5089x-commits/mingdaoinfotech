"""把模擬考 30 題從吳邦一 125 題 PDF 剪成圖片（只剪左半邊的題目，不含右邊的「答案與說明」欄）。"""
import pymupdf, io, base64
from PIL import Image
import py125 as W
from py125_pdf import question_segments, SRC

def crop_images(qs, dpi=150):
    src = pymupdf.open(SRC)
    segs = question_segments(src, None)
    out = {}
    for q in qs:
        parts = []
        for pno, t, b in segs[q]:
            xs = sorted({round(d["rect"].x0) for d in src[pno].get_drawings()
                         if d["rect"].height > 20 and d["rect"].width < 2 and d["rect"].y0 <= b and d["rect"].y1 >= t})
            left, mid = (xs[0], xs[1]) if len(xs) >= 3 else (71, 534)
            pix = src[pno].get_pixmap(clip=pymupdf.Rect(left - 1, t - 1, mid + 1, b + 1), dpi=dpi)
            parts.append(Image.open(io.BytesIO(pix.tobytes("png"))).convert("RGB"))
        w = max(p.width for p in parts); h = sum(p.height for p in parts)
        im = Image.new("RGB", (w, h), "white"); y = 0
        for p in parts:
            im.paste(p, (0, y)); y += p.height
        buf = io.BytesIO(); im.save(buf, "WEBP", quality=82)
        out[q] = buf.getvalue()
    return out

if __name__ == "__main__":
    imgs = crop_images(W.MOCK)
    for q, b in imgs.items():
        open(f"/tmp/claude-0/mock/q{q:03d}.webp", "wb").write(b)
    print(sum(len(b) for b in imgs.values()) // 1024, "KB")
