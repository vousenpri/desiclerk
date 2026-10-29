#!/usr/bin/env python3
"""
check_photo.py — validate a photo for Indian consular applications (USA / VFS)
and emit compliant upload + print files.

Usage:
    python3 check_photo.py PHOTO [--for oci|surrender] [--out DIR]

Checks (OCI upload, both VFS specs at once):
    JPEG, square, 360–900 px, <= 30 KB  (also satisfies 200–1500 px, <= 500 KB)
Checks (background):
    surrender -> white expected
    oci       -> light but NOT white expected (Govt of India instruction)
Emits:
    <name>_upload.jpg     600x600, JPEG, <= 30 KB
    <name>_print_2x2.jpg  600x600 at 300 DPI (= 2 x 2 inch)

Requires: Pillow (pip install pillow).
"""
import argparse
import io
import os
import sys

try:
    from PIL import Image, ImageOps
except ImportError:
    sys.exit("Pillow missing: pip install pillow")

UPLOAD_PX = 600
UPLOAD_MAX_BYTES = 30 * 1024
PRINT_DPI = 300


def border_stats(img):
    """Mean brightness and saturation of a 6% border ring, as 0-255."""
    g = img.convert("RGB")
    w, h = g.size
    if w < 8 or h < 8:
        return 0.0, 0.0  # too small to have a border; caller fails it on size anyway
    b = max(2, int(min(w, h) * 0.06))
    b = min(b, (min(w, h) - 1) // 2)  # never let the ring cover the whole image
    px = []
    for x in range(w):
        for y in list(range(b)) + list(range(h - b, h)):
            px.append(g.getpixel((x, y)))
    for y in range(b, h - b):
        for x in list(range(b)) + list(range(w - b, w)):
            px.append(g.getpixel((x, y)))
    n = len(px)
    lum = sum(0.299 * r + 0.587 * gg + 0.114 * bb for r, gg, bb in px) / n
    sat = sum(max(p) - min(p) for p in px) / n
    return lum, sat


def squarify(img):
    w, h = img.size
    if w == h:
        return img
    s = min(w, h)
    left = (w - s) // 2
    top = max(0, (h - s) // 3)  # bias upward: faces sit high
    return img.crop((left, top, left + s, top + s))


def to_jpeg_under(img, max_bytes):
    for q in range(92, 30, -4):
        buf = io.BytesIO()
        img.save(buf, "JPEG", quality=q, optimize=True, progressive=False)
        if buf.tell() <= max_bytes:
            return buf.getvalue(), q
    return buf.getvalue(), q


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("photo")
    ap.add_argument("--for", dest="purpose", choices=["oci", "surrender"], default="oci")
    ap.add_argument("--out", default=None)
    a = ap.parse_args()

    try:
        src = Image.open(a.photo)
        src.load()
    except (OSError, ValueError) as e:
        print(f"FAIL  cannot read {a.photo}: {e}. Not an image, or a corrupt file.")
        sys.exit(2)
    fmt = (src.format or "").upper()
    src = ImageOps.exif_transpose(src)
    w, h = src.size
    size = os.path.getsize(a.photo)
    base = os.path.splitext(os.path.basename(a.photo))[0]
    out = a.out or os.path.dirname(os.path.abspath(a.photo))
    os.makedirs(out, exist_ok=True)

    fails, warns = [], []

    # --- as-submitted checks ---
    if fmt not in ("JPEG", "JPG"):
        fails.append(f"format {fmt or 'unknown'}: portal accepts JPEG/JPG only")
    if w != h:
        fails.append(f"not square: {w}x{h}")
    if not (360 <= w <= 900 and 360 <= h <= 900):
        fails.append(f"{w}x{h}: outside 360–900 px (strict VFS spec; lenient is 200–1500)")
    if size > UPLOAD_MAX_BYTES:
        fails.append(f"{size//1024} KB: over 30 KB (strict VFS spec; lenient is 500 KB)")
    if min(w, h) < 600:
        warns.append(f"source only {min(w,h)} px on the short side; 600 px needed for a sharp 2x2 print")

    lum, sat = border_stats(src)
    if a.purpose == "surrender":
        if lum < 215 or sat > 18:
            fails.append(f"background not white (lum {lum:.0f}, sat {sat:.0f}); surrender requires white only")
    else:
        if lum >= 225 and sat < 12:
            fails.append(f"background reads as white (lum {lum:.0f}); Govt of India OCI spec says light-coloured, NOT white")
        elif lum < 170:
            fails.append(f"background too dark (lum {lum:.0f}); OCI wants a plain light background")

    # --- emit compliant files ---
    sq = squarify(src.convert("RGB"))
    up = sq.resize((UPLOAD_PX, UPLOAD_PX), Image.LANCZOS)
    up_bytes, q = to_jpeg_under(up, UPLOAD_MAX_BYTES)
    too_big = len(up_bytes) > UPLOAD_MAX_BYTES
    up_path = os.path.join(out, f"{base}_upload.jpg")
    if not too_big:
        with open(up_path, "wb") as f:
            f.write(up_bytes)

    pr = sq.resize((UPLOAD_PX, UPLOAD_PX), Image.LANCZOS)
    pr_path = os.path.join(out, f"{base}_print_2x2.jpg")
    pr.save(pr_path, "JPEG", quality=95, dpi=(PRINT_DPI, PRINT_DPI))

    # --- report ---
    print(f"photo: {a.photo}  {w}x{h}  {fmt}  {size//1024} KB  purpose={a.purpose}")
    print(f"background: lum {lum:.0f}/255, sat {sat:.0f}")
    for m in fails:
        print(f"FAIL  {m}")
    for m in warns:
        print(f"WARN  {m}")
    if not fails:
        print("PASS  as submitted")
    print()
    if too_big:
        print(f"FAIL  could not get the upload under 30 KB (best was {len(up_bytes)//1024} KB at q={q}). No upload file written. Busy backgrounds and patterned clothing do this; retake against a plain wall.")
        fails.append("upload cannot be made under 30 KB")
    else:
        print(f"wrote {up_path}  ({len(up_bytes)//1024} KB, q={q})  -> upload to portal")
    print(f"wrote {pr_path}  (600 px @ 300 DPI = 2x2 in) -> print on photo paper; at the kiosk choose 'actual size' / 2x2, never 'fit to page'")
    print("NOTE  background check reads the border pixels only; it cannot judge the face, the crop, or shadows. The portal does.")
    if fails and any("background" in m for m in fails):
        print("NOTE  background fails cannot be fixed by resizing; retake against the right backdrop")
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
