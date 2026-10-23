#!/usr/bin/env python3
"""Post-process generated PNGs -> optimized repo assets.
- hero-main: 1344x768 -> center-crop 1344x756 (exact 16:9) -> WebP q85
- banner-*:  1344x768 -> center-crop 1344x336 (exact 4:1) -> WebP q82
- og-image:  1152x864 -> center-crop 1152x605 (~1200x630 ratio) -> PNG + WebP
- icons:     1024x1024 PNG as-is (already compact)
- bg-*:      1024x1024 -> WebP q75
- avatar:    PNG full-res + 256px copy
"""
from PIL import Image
import os, shutil

RAW = os.environ.get("GEN_STAGE", ".gen-staging")
REPO = os.environ.get("REPO_ROOT", ".")
B = os.path.join(REPO, "assets", "banners")
I = os.path.join(REPO, "assets", "icons")
BG = os.path.join(REPO, "assets", "backgrounds")
OG = os.path.join(REPO, "assets", "og")
AV = os.path.join(REPO, "assets", "avatar")
for d in (B, I, BG, OG, AV):
    os.makedirs(d, exist_ok=True)

def center_crop(im, tw, th):
    w, h = im.size
    # scale target box: crop as much height/width as needed keeping center
    target_ratio = tw / th
    ratio = w / h
    if ratio > target_ratio:      # too wide -> crop width
        nw = int(h * target_ratio)
        x0 = (w - nw) // 2
        box = (x0, 0, x0 + nw, h)
    else:                          # too tall -> crop height
        nh = int(w / target_ratio)
        y0 = (h - nh) // 2
        box = (0, y0, 0 + w, y0 + nh)
    return im.crop(box)

report = []

# 1) hero-main
im = Image.open(f"{RAW}/hero-main.png").convert("RGB")
hero = center_crop(im, 16, 9)  # -> 1344x756
hero.save(f"{B}/hero-main.webp", "WEBP", quality=85, method=6)
report.append(f"hero-main.webp {hero.size}")

# 2) section banners -> 4:1
for f in sorted(os.listdir(RAW)):
    if f.startswith("banner-") and f.endswith(".png"):
        sec = f[len("banner-"):-len(".png")]
        im = Image.open(os.path.join(RAW, f)).convert("RGB")
        b = center_crop(im, 4, 1)  # -> 1344x336
        out = os.path.join(B, f"banner-{sec}.webp")
        b.save(out, "WEBP", quality=82, method=6)
        report.append(f"banner-{sec}.webp {b.size} {os.path.getsize(out)//1024} KB")

# 3) og-image
im = Image.open(f"{RAW}/og-image.png").convert("RGB")
og = center_crop(im, 1200, 630)
og.save(f"{OG}/og-image.png", "PNG", optimize=True)
og.save(f"{OG}/og-image.webp", "WEBP", quality=85, method=6)
report.append(f"og-image {og.size}")

# 4) icons as-is
for f in sorted(os.listdir(RAW)):
    if f.startswith("icon-") and f.endswith(".png"):
        shutil.copy(os.path.join(RAW, f), os.path.join(I, f))
        report.append(f"{f} {Image.open(os.path.join(RAW,f)).size}")

# 5) backgrounds
for f in ("bg-starfield.png", "bg-matrix.png"):
    im = Image.open(os.path.join(RAW, f)).convert("RGB")
    out = os.path.join(BG, f[:-4] + ".webp")
    im.save(out, "WEBP", quality=75, method=6)
    report.append(f"{os.path.basename(out)} {os.path.getsize(out)//1024} KB")

# 6) avatar
im = Image.open(f"{RAW}/avatar.png").convert("RGB")
im.save(f"{AV}/avatar.png", "PNG", optimize=True)
im.resize((256, 256), Image.LANCZOS).save(f"{AV}/avatar-256.png", "PNG", optimize=True)
report.append("avatar.png + avatar-256.png")

print("POST-PROCESS DONE:")
for r in report:
    print(" ", r)
tot = 0
for root, _, files in os.walk(REPO, topdown=True):
    if ".git" in root:
        continue
    for f in files:
        if f.endswith((".webp", ".png")) and root.startswith(REPO + "/assets/"):
            tot += os.path.getsize(os.path.join(root, f))
print(f"TOTAL new raster assets: {tot//1024} KB")
