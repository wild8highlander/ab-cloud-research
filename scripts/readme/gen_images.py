#!/usr/bin/env python3
"""AB-Cloud Research — AI asset generation driver (29 images).
Uses z-ai CLI. Resumable: skips existing outputs. Retries 3x per image.
Staging dir: /home/z/my-project/img-staging/raw/
"""
import subprocess, sys, time, os, json

STAGE = os.environ.get("GEN_STAGE", ".gen-staging")
os.makedirs(STAGE, exist_ok=True)

STYLE_TAIL = ("high detail, elegant, no text, no letters, no numbers, "
              "no watermark, no logo, no signature")
CENTER_BAND = "subject centered in the middle horizontal band of the image"

ASSETS = [
    # ============ BANNERS 2048x1024 (later center-cropped to 4:1) ============
    ("hero-main", "1344x768",
     "Ultra-wide cinematic hero banner for a mathematical physics research project, dark navy background hex 05060f, "
     "a glowing phase resonator visualized as concentric toroidal waves in electric cyan hex 00e5ff and vivid magenta hex ff2ec4, "
     "Riemann zeta function zeros rendered as tiny luminous cyan dots aligned along a glowing vertical critical line, "
     "subtle holographic grid, floating particle field, volumetric light, scientific visualization aesthetic, elegant futurism, "
     f"cinematic depth, {STYLE_TAIL}"),
    ("banner-verification", "1344x768",
     "Thin horizontal banner, minimalist, dark slate navy background hex 05060f, a single glowing checkmark composed of orbiting "
     "luminous particles in electric cyan hex 00e5ff, faint scan-line pattern, subtle circuit traces along the edges, "
     f"elegant scientific UI style, {CENTER_BAND}, {STYLE_TAIL}"),
    ("banner-formal", "1344x768",
     "Thin horizontal banner, dark navy background hex 05060f, a geometric formal proof tree drawn in glowing violet hex a78bfa "
     "lines with luminous node links and softly floating abstract mathematical geometry, subtle holographic depth, "
     f"minimalist scientific aesthetic, {CENTER_BAND}, {STYLE_TAIL}"),
    ("banner-monographs", "1344x768",
     "Thin horizontal banner, dark warm brown background hex 1a1208, an old open book morphing into glowing golden hex ffd60a "
     "digital particles rising like embers, elegant gold and amber accents with faint cyan sparkles, scholarly meets futuristic, "
     f"{CENTER_BAND}, {STYLE_TAIL}"),
    ("banner-quantum", "1344x768",
     "Thin horizontal banner, dark navy background hex 05060f, a live quantum laboratory console glowing with holographic "
     "oscilloscope traces and graphs in cyan hex 00e5ff and magenta hex ff2ec4, a holographic wireframe toroidal resonator "
     f"floating above the console, cyberpunk scientific aesthetic, {CENTER_BAND}, {STYLE_TAIL}"),
    ("banner-hilbert-polya", "1344x768",
     "Thin horizontal banner, dark navy background hex 05060f, a luminous spectral staircase of quantum energy levels rising along "
     "a glowing vertical critical line, harmonic oscillator parabola with evenly spaced eigenvalue dots, wavefunctions rippling, "
     f"violet and cyan gradient glow, subtle particle field, {CENTER_BAND}, {STYLE_TAIL}"),
    ("banner-dirac-lab", "1344x768",
     "Thin horizontal banner, dark navy background hex 05060f, a glowing double-cone Dirac cone with a luminous wave packet "
     "orbiting its apex, relativistic energy ladder rungs in cyan, a dial of glowing arcs, magenta particle trails, "
     f"scientific visualization aesthetic, {CENTER_BAND}, {STYLE_TAIL}"),
    ("banner-lab-3d", "1344x768",
     "Thin horizontal banner, dark navy background hex 05060f, an isometric three-dimensional cubic lattice wireframe with a "
     "pulsing vortex node and a glowing orbit ring inside, cyan grid lines with magenta energy accents, holographic depth, "
     f"scientific visualization aesthetic, {CENTER_BAND}, {STYLE_TAIL}"),
    ("banner-results", "1344x768",
     "Thin horizontal banner, dark navy background hex 05060f, a glowing holographic terminal window with luminous checkmark "
     "verdict lines appearing row by row, a pulsing round seal stamp, small data crystal artifacts glowing green and cyan, "
     f"floating particles, scientific UI aesthetic, {CENTER_BAND}, {STYLE_TAIL}"),
    ("banner-academic", "1344x768",
     "Thin horizontal banner, dark navy background hex 05060f with warm gold accents, classical academic pillars in glowing "
     "golden light standing on a luminous plinth, a pulsing spherical node floating above, tiny luminous dots drifting along "
     f"a vertical critical line, elegant scholarly futurism, {CENTER_BAND}, {STYLE_TAIL}"),
    ("banner-code", "1344x768",
     "Thin horizontal banner, dark navy background hex 05060f, a glowing holographic code terminal with rising progress bars, "
     "a triple-loop emblem of interlinked luminous rings in violet hex a78bfa, floating code fragment particles in cyan, "
     f"scientific software aesthetic, {CENTER_BAND}, {STYLE_TAIL}"),
    ("banner-apps", "1344x768",
     "Thin horizontal banner, dark navy background hex 05060f, two glowing holographic browser windows side by side, one with "
     "live dashboard bars and a grid of green status cells, one with a rotating three-dimensional lattice, cyan and magenta "
     f"neon glow, futuristic UI aesthetic, {CENTER_BAND}, {STYLE_TAIL}"),
    ("banner-wave-attractors", "1344x768",
     "Thin horizontal banner, dark navy background hex 05060f, a hyperbolic elliptical cavity with a light ray cascading onto a "
     "closed chiral attractor route and its mirror twin trace, expanding luminous wavefronts, a cone of light, thin cyan and "
     f"violet lines, scientific visualization aesthetic, {CENTER_BAND}, {STYLE_TAIL}"),
    ("banner-vortex", "1344x768",
     "Thin horizontal banner, dark navy background hex 05060f, a luminous vortex lattice with circulating glowing flow lines "
     "converging into a spiraling optimization funnel, magenta and cyan gradient streams, depth of field, particle trails, "
     f"scientific visualization aesthetic, {CENTER_BAND}, {STYLE_TAIL}"),
    ("banner-meridian", "1344x768",
     "Thin horizontal banner, dark navy background hex 05060f, a spectral observatory with a luminous meridian compass rose, "
     "a vertical critical line with rising glowing dots, a smooth bell-shaped density curve glowing in cyan, holographic star "
     f"map, elegant scientific aesthetic, {CENTER_BAND}, {STYLE_TAIL}"),
    ("banner-docs", "1344x768",
     "Thin horizontal banner, dark navy background hex 05060f, a glowing documentation site browser window with a luminous "
     "sidebar navigation tree, a floating math formula box with soft glow, rising page cards, blue and cyan gradient, "
     f"futuristic knowledge base aesthetic, {CENTER_BAND}, {STYLE_TAIL}"),
    # ============ ICONS 1024x1024 ============
    ("icon-resonator", "1024x1024",
     "Minimalist flat-line icon, a toroidal phase resonator with concentric wave rings, thin neon cyan hex 00e5ff strokes on a "
     f"very dark navy background hex 05060f, subtle magenta glow accent, consistent thin line weight, vector-like, high contrast, "
     f"centered, generous margins, {STYLE_TAIL}"),
    ("icon-zeta", "1024x1024",
     "Minimalist flat-line icon, a spiral curve with tiny dots aligned along a vertical line crossing it, thin neon cyan hex "
     "00e5ff strokes on a very dark navy background hex 05060f, subtle magenta glow accent, consistent thin line weight, "
     f"vector-like, high contrast, centered, generous margins, {STYLE_TAIL}"),
    ("icon-julia", "1024x1024",
     "Minimalist flat-line icon, a fractal spiral boundary curve of a Julia set, thin neon cyan hex 00e5ff strokes on a very "
     "dark navy background hex 05060f, subtle violet glow accent, consistent thin line weight, vector-like, high contrast, "
     f"centered, generous margins, {STYLE_TAIL}"),
    ("icon-verify", "1024x1024",
     "Minimalist flat-line icon, a shield containing a checkmark, thin neon cyan hex 00e5ff strokes on a very dark navy "
     f"background hex 05060f, subtle green glow accent, consistent thin line weight, vector-like, high contrast, centered, "
     f"generous margins, {STYLE_TAIL}"),
    ("icon-book", "1024x1024",
     "Minimalist flat-line icon, an open book with a bookmark, thin neon gold hex ffd60a strokes on a very dark navy background "
     f"hex 05060f, subtle amber glow, consistent thin line weight, vector-like, high contrast, centered, generous margins, {STYLE_TAIL}"),
    ("icon-chip", "1024x1024",
     "Minimalist flat-line icon, a microchip square with circuit pins and inner traces, thin neon cyan hex 00e5ff strokes on a "
     f"very dark navy background hex 05060f, subtle magenta glow accent, consistent thin line weight, vector-like, high contrast, "
     f"centered, generous margins, {STYLE_TAIL}"),
    ("icon-globe", "1024x1024",
     "Minimalist flat-line icon, a wireframe globe with latitude and longitude lines, thin neon cyan hex 00e5ff strokes on a "
     f"very dark navy background hex 05060f, subtle violet glow accent, consistent thin line weight, vector-like, high contrast, "
     f"centered, generous margins, {STYLE_TAIL}"),
    ("icon-crystal", "1024x1024",
     "Minimalist flat-line icon, a faceted crystal gem, thin neon violet hex a78bfa strokes on a very dark navy background hex "
     f"05060f, subtle cyan glow accent, consistent thin line weight, vector-like, high contrast, centered, generous margins, {STYLE_TAIL}"),
    ("icon-atom", "1024x1024",
     "Minimalist flat-line icon, an atom with three elliptical electron orbits around a nucleus, thin neon cyan hex 00e5ff "
     f"strokes on a very dark navy background hex 05060f, subtle magenta glow accent, consistent thin line weight, vector-like, "
     f"high contrast, centered, generous margins, {STYLE_TAIL}"),
    # ============ BACKGROUNDS 1024x1024 ============
    ("bg-starfield", "1024x1024",
     "Seamless dark cosmic background texture, tiny scattered stars, a very faint nebula wash in deep blue and violet, extremely "
     "subtle, low contrast, uniform, no focal point, no bright areas, flat style, tileable texture, dark navy hex 05060f, "
     "no text, no watermark"),
    ("bg-matrix", "1024x1024",
     "Seamless dark navy background texture hex 05060f, a faint grid of softly glowing abstract mathematical curves and symbols "
     "at very low opacity, cyan tint, extremely subtle, uniform low contrast, no focal point, tileable texture, no text, "
     "no letters, no watermark"),
    # ============ OG + AVATAR ============
    ("og-image", "1152x864",
     "Social preview card for a mathematical physics research project, dark navy background hex 05060f, a central glowing "
     "faceted crystal with tiny luminous dots aligned on its faces, cyan hex 00e5ff and magenta hex ff2ec4 gradient lighting, "
     "volumetric particles, cinematic elegant composition with empty dark space on the left side, high detail, "
     "no text, no letters, no watermark"),
    ("avatar", "1024x1024",
     "Square minimal logo icon, very dark navy background hex 05060f, a glowing abstract monogram of two interlocked angular "
     "shapes made of thin luminous circuit traces forming a toroidal resonator symbol, cyan gradient glow with subtle magenta "
     "accent, high contrast, vector-like, centered, generous margins, no other elements, no text, no watermark"),
]

def gen_one(name, size, prompt, retries=3):
    out = os.path.join(STAGE, f"{name}.png")
    if os.path.exists(out) and os.path.getsize(out) > 20_000:
        print(f"[skip] {name} exists", flush=True)
        return True
    for attempt in range(1, retries + 1):
        try:
            r = subprocess.run(
                ["z-ai", "image", "-p", prompt, "-o", out, "-s", size],
                capture_output=True, text=True, timeout=300)
            if r.returncode == 0 and os.path.exists(out) and os.path.getsize(out) > 20_000:
                print(f"[ok] {name} ({os.path.getsize(out)//1024} KB)", flush=True)
                return True
            print(f"[retry {attempt}] {name}: rc={r.returncode} {r.stderr[:200]}", flush=True)
        except subprocess.TimeoutExpired:
            print(f"[retry {attempt}] {name}: timeout", flush=True)
        time.sleep(3 * attempt)
    print(f"[FAIL] {name}", flush=True)
    return False

def main():
    only = sys.argv[1:] if len(sys.argv) > 1 else None
    results = {}
    for name, size, prompt in ASSETS:
        if only and name not in only:
            continue
        results[name] = gen_one(name, size, prompt)
    ok = sum(results.values())
    total = len(results)
    print(f"\n=== DONE: {ok}/{total} ===", flush=True)
    with open(os.path.join(STAGE, "_results.json"), "w") as f:
        json.dump(results, f, indent=1)
    sys.exit(0 if ok == total else 1)

if __name__ == "__main__":
    main()
