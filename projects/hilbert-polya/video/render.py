#!/usr/bin/env python3
"""'Zeros & Gates: an experiment in pixels' — 210 s cinematic render.
1920x1080 output (internal 960x540 -> lanczos upscale + grain + vignette via ffmpeg).
The zeros emerge ONLY from combining noisy exposures during the montage scene;
direct input of zeros is shown as the forbidden shortcut (red error).
Frames are piped raw to ffmpeg stdin and muxed with the ambient WAV.
"""
import numpy as np, subprocess, math, sys, os
from PIL import Image, ImageDraw, ImageFont

# ---------------- config ----------------
W, H = 960, 540
FPS = 24
DUR = 210.0
NF = int(DUR * FPS)
OUT = "zeros_and_gates_1080p.mp4"
AUD = "video_audio.wav"

NAVY = np.array([11, 30, 58], float)
NAVY2 = np.array([18, 42, 74], float)
AMBER = np.array([232, 163, 61], float)
CREAM = np.array([245, 237, 224], float)
TEAL = np.array([46, 160, 143], float)
RED = np.array([205, 60, 45], float)

rng = np.random.default_rng(96)
F_TIT = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"
F_ITA = "/usr/share/fonts/truetype/liberation/LiberationSerif-Italic.ttf"
F_CAP = "/usr/share/fonts/truetype/english/Carlito-Regular.ttf"
F_CAPB = "/usr/share/fonts/truetype/english/Carlito-Bold.ttf"
f_title = ImageFont.truetype(F_TIT, 58)
f_sub = ImageFont.truetype(F_ITA, 27)
f_cap = ImageFont.truetype(F_CAP, 21)
f_capb = ImageFont.truetype(F_CAPB, 24)
f_small = ImageFont.truetype(F_CAP, 17)

# ---------------- real zeta zeros ----------------
import mpmath
mpmath.mp.dps = 15
NZ = 24
gammas = [float(mpmath.im(mpmath.zetazero(n))) for n in range(1, NZ + 1)]
print("zeros:", ["%.2f" % g for g in gammas[:5]], "...")

# glow sprite cache
SPR = {}
def sprite(radius):
    r = int(radius)
    if r in SPR: return SPR[r]
    d = 2 * r + 1
    yy, xx = np.mgrid[0:d, 0:d] - r
    g = np.exp(-(xx**2 + yy**2) / (2 * (radius / 2.1)**2))
    g /= g.max()
    SPR[r] = g.astype(np.float32)
    return SPR[r]

def add_glow(img, x, y, color, radius, amp):
    s = sprite(radius)
    r = s.shape[0] // 2
    x0, x1 = int(x) - r, int(x) + r + 1
    y0, y1 = int(y) - r, int(y) + r + 1
    cx0, cy0 = max(0, -x0), max(0, -y0)
    x0, y0 = max(0, x0), max(0, y0)
    x1, y1 = min(W, x1), min(H, y1)
    if x1 <= x0 or y1 <= y0: return
    s = s[cy0:cy0 + (y1 - y0), cx0:cx0 + (x1 - x0)]
    img[y0:y1, x0:x1] += s[..., None] * color[None, None, :] * amp

def vgrad(c1, c2, tilt=0.3):
    y = np.linspace(0, 1, H)[:, None]
    x = np.linspace(0, 1, W)[None, :]
    t = np.clip(y * (1 - tilt) + x * tilt, 0, 1)[..., None]
    return c1 * (1 - t) + c2 * t

def ease(k):
    k = np.clip(k, 0, 1)
    return k * k * (3 - 2 * k)

def text_frame(img_u8, draw_fn):
    im = Image.fromarray(img_u8)
    d = ImageDraw.Draw(im, "RGBA")
    draw_fn(d)
    return np.asarray(im, float)

def smoothstep(e0, e1, x):
    k = np.clip((x - e0) / (e1 - e0), 0, 1)
    return k * k * (3 - 2 * k)

# zero line geometry (shared by S1, S5, S6)
ZX = int(W * 0.5)
ZTOP, ZBOT = int(H * 0.10), int(H * 0.92)
def zy(n_idx):
    return ZTOP + (gammas[n_idx] / (gammas[-1] * 1.06)) * (ZBOT - ZTOP)

def glyph_pattern():
    """Hidden zeros comb encoded in exposures (S5)."""
    p = np.zeros((H, W))
    # faint vertical line
    p[:, ZX - 3:ZX + 3] += 0.5
    for i in range(NZ):
        y = int(zy(i))
        p[y - 4:y + 4, ZX - 16:ZX + 16] += 0.55
    return p

PATTERN = glyph_pattern()

# ---------------- S1 prologue (0-20) ----------------
stars = np.array([[rng.uniform(0, W), rng.uniform(0, H), rng.uniform(0.3, 1.0)] for _ in range(260)])
def s1(t):
    img = vgrad(NAVY * 0.8, NAVY2, 0.15)
    k = ease(t / 3.0)
    img *= (0.35 + 0.65 * k)
    for (sx, sy, sa) in stars:
        tw = 0.55 + 0.45 * np.sin(2 * np.pi * 0.4 * t + sx)
        add_glow(img, sx, sy, CREAM, 2.2, 0.05 * sa * tw * k)
    lk = ease((t - 2.5) / 4.0)
    if lk > 0:
        img[:, ZX - 2:ZX + 2] = img[:, ZX - 2:ZX + 2] * (1 - 0.7 * lk) + AMBER * 0.7 * lk
        add_glow(img, ZX, H / 2, AMBER, 90, 0.10 * lk)
    for i in range(min(NZ, int(max(0, (t - 5)) / 1.6))):
        yy = zy(i)
        kk = ease((t - 5 - i * 1.6) / 1.2)
        img = img.copy() if False else img
        add_glow(img, ZX, yy, CREAM, 7, 0.5 * kk)
        add_glow(img, ZX, yy, AMBER, 16, 0.16 * kk)
    return img

# ---------------- S2 shutter wall (20-50) ----------------
CELL = 68
cells = [(cx, cy) for cy in range(6, H - CELL, CELL) for cx in range(6, W - CELL, CELL)]
ncells = len(cells)
def s2(t):
    img = vgrad(NAVY, NAVY2 * 1.05, 0.1)
    openk = smoothstep(1.0, 26.0, t)
    n_open = int(openk * ncells)
    for i, (cx, cy) in enumerate(cells):
        if i < n_open:
            warm = 0.75 + 0.25 * np.sin(2 * np.pi * 0.5 * t + i * 0.7)
            col = AMBER * (0.45 + 0.3 * warm)
            img[cy:cy + CELL - 6, cx:cx + CELL - 6] = img[cy:cy + CELL - 6, cx:cx + CELL - 6] * 0.25 + col
            add_glow(img, cx + CELL // 2, cy + CELL // 2, AMBER, 8, 0.05 * warm)
        else:
            img[cy:cy + CELL - 6, cx:cx + CELL - 6] = img[cy:cy + CELL - 6, cx:cx + CELL - 6] * 0.55 + (NAVY * 1.25 + 10) * 0.45
        mid = (CELL - 6) // 2
        img[cy + mid - 1:cy + mid + 1, cx:cx + CELL - 6] *= 0.5
        img[cy:cy + CELL - 6, cx + mid - 1:cx + mid + 1] *= 0.5
    return img

# ---------------- S3 forbidden shortcut (50-76) ----------------
typed_zeros = [(0.42, 0.34), (0.53, 0.44), (0.44, 0.56), (0.57, 0.62), (0.49, 0.72)]
def s3(t):
    img = vgrad(NAVY * 1.05, np.array([48, 22, 30], float), 0.45)
    # film sheet
    fx0, fx1 = int(W * 0.27), int(W * 0.73)
    fy0, fy1 = int(H * 0.16), int(H * 0.86)
    sheet = np.array([224, 214, 196], float)
    img[fy0:fy1, fx0:fx1] = sheet * (0.82 + 0.06 * np.sin(2 * np.pi * 0.9 * t))
    img_u8 = np.clip(img, 0, 255).astype(np.uint8)
    def dfn(d):
        for li in range(1, 9):
            yy = fy0 + li * (fy1 - fy0) / 9
            d.line([fx0 + 14, yy, fx1 - 14, yy], fill=(150, 140, 120), width=2)
        for zi, (tx, ty) in enumerate(typed_zeros):
            kk = smoothstep(2.0 + zi * 2.2, 3.2 + zi * 2.2, t)
            if kk <= 0: continue
            x, y = W * tx, H * ty
            col = (90, 60, 40, int(255 * kk)) if zi < 3 else (196, 60, 45, int(255 * kk))
            wdt = 7 if zi < 3 else 9
            d.ellipse([x - 24, y - 38, x + 24, y + 38], outline=col, width=wdt)
    img = text_frame(img_u8, dfn).astype(float)
    # red alarm sweep
    sweep = np.exp(-((np.arange(W) - (W * 0.1 + (W * 0.8) * (0.5 + 0.5 * np.sin(2 * np.pi * 0.5 * t))))**2) / (2 * (W / 5)**2))
    img += (RED - NAVY)[None, None, :] * (0.30 * sweep[None, :, None] * np.linspace(0.5, 1.0, H)[:, None, None])
    # film burns at edges after 8 s
    bk = smoothstep(8, 22, t)
    if bk > 0:
        edge = np.zeros((H, W))
        for e in range(30):
            a = (1 - e / 30) * 0.5
            edge[e, :] = a; edge[H - 1 - e, :] = a
            edge[:, e] = a * 0.7; edge[:, W - 1 - e] = a * 0.7
        img += RED[None, None, :] * edge[..., None] * bk
        shake = bk * 2.2
        dx, dy = int(rng.uniform(-shake, shake)), int(rng.uniform(-shake, shake))
        img = np.roll(np.roll(img, dy, axis=0), dx, axis=1)
    return img

# ---------------- S4 exposure noise (76-110) ----------------
def s4(t):
    img = vgrad(NAVY, NAVY * 1.2, 0.12)
    # shutter cells half open, projecting NOISE frames
    cell = 86
    for cy in range(4, H - cell, cell):
        for cx in range(4, W - cell, cell):
            blk = rng.normal(0.45, 0.28, (cell - 8, cell - 8, 1)) * np.array([[0.7, 0.85, 1.05]])
            img[cy + 4:cy + cell - 4, cx + 4:cx + cell - 4] = blk
    # flashes of faint pattern glimpses (never enough to see)
    g = 0.03 + 0.02 * np.sin(2 * np.pi * 0.8 * t)
    img += PATTERN[..., None] * g * np.array([1.0, 0.85, 0.6])[None, None, :]
    # frame counter flicker
    return img

# ---------------- S5 montage accumulator (110-160) ----------------
ACC = np.zeros((H, W))
acc_count = 0
def s5_reset():
    global ACC, acc_count
    ACC[:] = 0; acc_count = 0
def s5(t):
    global ACC, acc_count
    lt = t - 110.0
    # accumulate 12 exposures per second -> the 600-frame budget is reached
    # exactly at the end of the scene (closed form: the sum of k iid
    # N(0.5, 0.5^2) fields is a single N(0.5k, 0.25k) field)
    target = min(int(lt * 12.0), 600)
    k = min(target, 600) - acc_count
    if k > 0:
        ACC += rng.normal(0.5 * k, 0.5 * math.sqrt(k), (H, W)) + PATTERN * (0.85 * k)
        acc_count += k
    acc = ACC / max(acc_count, 1)
    # noise cancels as 1/sqrt(N); pattern persists
    acc = (acc - 0.5) * (1 + 3.2 * smoothstep(0, 50, lt))
    acc = np.clip(acc + 0.5, 0, 1)
    img = vgrad(NAVY * 0.9, NAVY2, 0.1) * 0.6
    img += acc[..., None] * np.array([1.0, 0.82, 0.55])[None, None, :] * 0.95
    # zero lock-ins with teal rings
    emerged = int(min(NZ, lt / 2.0))
    for i in range(emerged):
        yy = zy(i)
        add_glow(img, ZX, yy, CREAM, 8, 0.55)
        add_glow(img, ZX, yy, AMBER, 20, 0.18)
        if i == emerged - 1:
            k = (lt % 2.0) / 2.0
            add_glow(img, ZX, yy, TEAL, 26 * (0.4 + k), 0.5 * (1 - k))
    # timeline bar
    bk = lt / 50.0
    img[int(H * 0.955):int(H * 0.975), int(W*0.08):int(W*0.08 + W*0.84*bk)] += TEAL * 0.8
    img[int(H * 0.955):int(H * 0.975), int(W*0.08):int(W*0.92)] *= 0.5
    return img

# ---------------- S6 spectrum emerges (160-190) ----------------
def s6(t):
    img = vgrad(NAVY * 0.85, NAVY2 * 1.1, 0.12)
    lt = t - 160.0
    img[:, ZX - 3:ZX + 3] = img[:, ZX - 3:ZX + 3] * 0.3 + AMBER * 0.7
    add_glow(img, ZX, H / 2, AMBER, 120, 0.12)
    for i in range(NZ):
        kk = ease((lt - i * 0.5) / 1.4)
        if kk <= 0: continue
        yy = zy(i)
        pulse = 0.75 + 0.25 * np.sin(2 * np.pi * 0.6 * t + i)
        add_glow(img, ZX, yy, CREAM, 9, 0.65 * kk * pulse)
        add_glow(img, ZX, yy, AMBER, 22, 0.20 * kk * pulse)
    # side histogram of gaps (GUE-like shimmer)
    for i in range(NZ - 1):
        gy = (zy(i) + zy(i + 1)) / 2
        gap = gammas[i + 1] - gammas[i]
        bw = 30 + gap * 26
        add_glow(img, W * 0.82, gy, TEAL, 6, 0.10 * ease(lt / 8))
        img[int(gy - 2):int(gy + 2), int(W * 0.80 - bw / 2 + 200 * 0):int(W * 0.80 + bw / 2)] += TEAL * 0.10 * ease(lt / 8)
    return img

# ---------------- S7 epilogue (190-210) ----------------
obs_cx = int(W * 0.5)
def s7(t):
    img = vgrad(NAVY * 0.9, np.array([30, 44, 76], float), 0.0)
    for (sx, sy, sa) in stars:
        tw = 0.5 + 0.5 * np.sin(2 * np.pi * 0.3 * t + sy)
        add_glow(img, sx, sy * 0.62, CREAM, 1.8, 0.05 * sa * tw)
    # sky comb
    for i in range(14):
        ang = math.pi * (0.10 + 0.062 * i)
        px = obs_cx - W * 0.42 * math.cos(ang)
        py = H * 0.60 - H * 0.46 * math.sin(ang) * 0.85
        kk = ease((t - 190 - i * 0.4) / 1.2)
        if kk > 0:
            add_glow(img, px, py, AMBER, 6, 0.5 * kk)
            add_glow(img, px, py, CREAM, 2.5, 0.3 * kk)
    img_u8 = np.clip(img, 0, 255).astype(np.uint8)
    d0 = ImageDraw.Draw(Image.fromarray(img_u8))
    d0.pieslice([obs_cx - 150, int(H * 0.62), obs_cx + 150, int(H * 1.1)], 180, 360, fill=(8, 20, 40))
    d0.rectangle([obs_cx - 150, int(H * 0.84), obs_cx + 150, H], fill=(8, 20, 40))
    d0.rectangle([obs_cx - 12, int(H * 0.55), obs_cx + 12, int(H * 0.88)], fill=(210, 150, 58))
    img = np.asarray(Image.fromarray(img_u8), float)
    add_glow(img, obs_cx, H * 0.68, AMBER, 14, 0.4)
    return img

# ---------------- timeline with crossfades ----------------
SCENES = [
    (0.0, 20.0, s1), (20.0, 50.0, s2), (50.0, 76.0, s3), (76.0, 110.0, s4),
    (110.0, 160.0, s5), (160.0, 190.0, s6), (190.0, 210.0, s7),
]
FADE = 1.6
def render_timeline(t):
    active = []
    for (a, b, fn) in SCENES:
        if t >= a - FADE / 2 and t <= b + FADE / 2:
            active.append((a, b, fn))
    if not active:
        return SCENES[-1][2](SCENES[-1][1] - 0.01)
    if len(active) == 1:
        a, b, fn = active[0]
        return fn(np.clip(t, a + 0.001, b - 0.001))
    (a1, b1, f1), (a2, b2, f2) = active[:2]
    k = smoothstep(a2 - FADE / 2, a2 + FADE / 2, t)
    i1 = f1(np.clip(t, a1 + 0.001, b1 - 0.001))
    i2 = f2(np.clip(t, a2 + 0.001, b2 - 0.001))
    return i1 * (1 - k) + i2 * k

# ---------------- titles & captions overlay ----------------
def overlay(u8, t):
    def dfn(d):
        def center(txt, y, font, fill, alpha):
            bb = d.textbbox((0, 0), txt, font=font)
            d.text(((W - (bb[2] - bb[0])) / 2, y), txt, font=font, fill=fill + (int(alpha),))
        if t < 20:  # S1 titles
            a1 = smoothstep(8, 10.5, t) * (1 - smoothstep(17.5, 19.8, t))
            a2 = smoothstep(10.5, 12.5, t) * (1 - smoothstep(18.0, 19.8, t))
            center("ZEROS  &  GATES", H * 0.30, f_title, (245, 237, 224), 255 * a1)
            center("an experiment in pixels  ·  Hilbert–Pólya Bridge", H * 0.30 + 78, f_sub, (232, 163, 61), 255 * a2)
        elif t < 50:
            a = smoothstep(21, 23.5, t) * (1 - smoothstep(47, 49.5, t))
            center("the wall of gates", H * 0.06, f_capb, (245, 237, 224), 220 * a)
            center("87 vortex-lattice configurations · Hermitian · half flux", H * 0.06 + 30, f_cap, (160, 190, 210), 200 * a)
        elif t < 76:
            a = smoothstep(51, 53.5, t) * (1 - smoothstep(73, 75.5, t))
            center("direct input of zeros is an error", H * 0.07, f_capb, (232, 163, 61), 230 * a)
            center("injected zeros are not evidence — the frames burn", H * 0.07 + 30, f_cap, (220, 130, 110), 200 * a)
        elif t < 110:
            a = smoothstep(77, 79.5, t) * (1 - smoothstep(107, 109.5, t))
            center("the exposure", H * 0.06, f_capb, (245, 237, 224), 220 * a)
            n_fr = int((t - 76) * 2.4)
            center(f"frame {n_fr} · a single exposure contains no zeros", H * 0.06 + 30, f_cap, (160, 190, 210), 200 * a)
        elif t < 160:
            a = smoothstep(111, 113.5, t) * (1 - smoothstep(157, 159.5, t))
            center("the montage experiment", H * 0.06, f_capb, (46, 160, 143), 230 * a)
            lt = t - 110.0
            n_acc = min(600, int(max(0, lt) * 12.0))
            emerged = int(min(24, max(0, lt) / 2.0))
            center(f"combining {n_acc} exposures · zeros locked: {emerged}/24", H * 0.06 + 30, f_cap, (160, 190, 210), 210 * a)
        elif t < 190:
            a = smoothstep(161, 163.5, t) * (1 - smoothstep(187, 189.5, t))
            center("the spectrum emerges", H * 0.06, f_capb, (232, 163, 61), 230 * a)
            center("γ₁ = 14.1347 …  the comb stands  ·  verified strip T ≤ 5000", H * 0.06 + 30, f_cap, (160, 190, 210), 200 * a)
        else:
            a = smoothstep(191, 194, t) * (1 - smoothstep(206, 209.5, t))
            center("zeros are measured, not typed", H * 0.16, f_title, (245, 237, 224), 255 * a)
            a2 = smoothstep(196, 199, t) * (1 - smoothstep(206.5, 209.5, t))
            center("Hilbert–Pólya Bridge · v2.0.0 · 2026", H * 0.16 + 80, f_cap, (160, 190, 210), 220 * a2)
            center("an original study of the graph ↔ operator passage", H * 0.16 + 108, f_small, (120, 150, 175), 200 * a2)
    return np.asarray(text_frame(u8, dfn), float)

# ---------------- render loop ----------------
def build_cmd(outfile, with_audio=True):
    inputs = ["-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-"]
    fc = ("[0:v]scale=1920:1080:flags=lanczos,vignette=PI/4.6,"
          "eq=saturation=1.07:contrast=1.05,format=yuv420p[v]")
    maps = ["-map", "[v]"]
    if with_audio:
        inputs += ["-i", AUD]
        maps += ["-map", "1:a", "-c:a", "aac", "-b:a", "192k", "-shortest"]
    return ["ffmpeg", "-y"] + inputs + ["-filter_complex", fc] + maps + \
           ["-c:v", "libx264", "-preset", "superfast", "-crf", "21", "-maxrate", "4.5M", "-bufsize", "9M", "-g", "60", "-pix_fmt", "yuv420p", outfile]

def main():
    start_frame = int(sys.argv[1]) if len(sys.argv) > 1 else 0
    end_frame = int(sys.argv[2]) if len(sys.argv) > 2 else NF
    outfile = sys.argv[3] if len(sys.argv) > 3 else OUT
    with_audio = len(sys.argv) <= 4  # segment mode: 4 args -> no audio
    cmd = build_cmd(outfile, with_audio=with_audio and (start_frame == 0 and end_frame == NF))
    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    for f in range(start_frame, end_frame):
        t = f / FPS
        img = render_timeline(t)
        img = np.clip(img, 0, 255).astype(np.uint8)
        img = overlay(img, t)
        img[..., 0] = np.clip(img[..., 0].astype(float) * 1.02, 0, 255)
        img[..., 2] = np.clip(img[..., 2].astype(float) * 0.985, 0, 255)
        img = img + rng.uniform(-1.8, 1.8, img.shape)  # baked soft film grain
        proc.stdin.write(np.clip(img, 0, 255).astype(np.uint8).tobytes())
        if f % 240 == 0:
            print(f"frame {f}/{NF} (t={t:.1f}s)", flush=True)
    proc.stdin.close()
    proc.wait()
    print("done:", outfile, flush=True)

if __name__ == "__main__":
    main()
