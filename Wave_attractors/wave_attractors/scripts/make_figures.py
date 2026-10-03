#!/usr/bin/env python3
"""
make_figures.py — publication figures for study W1 (Hyperbolic wave
attractors), following the T34 chart conventions of the repository
(DejaVu Sans, muted palette, no in-figure titles, 300 dpi).

Figures (data consumed from ../data, produced by run_experiments.py,
e4_frequency.py, wave_directional.py, ab_water.py, e6_eta_scan.py,
e7_time_domain.py):

  01_chambers_and_cone.png   chamber + reference route; propagation cone
  02_cascade.png             wavelength cascade |k| and geometric convergence
  03_attractor_vs_control.png  hyperbolic (converging) vs isotropic (chaotic)
  04_phase_diagram.png       attractor phase diagram in (s, y_v)
  05_chirality.png           chamber vs mirror: attractor loops and C index
  06_wave_maps.png           band-averaged |E|^2 (anisotropic Helmholtz)
  07_ray_density.png         geometric-acoustics energy density + route
  08_ab_water.png            companion study: AB water waves (OIST)
  09_cross_verification.png  Python vs Julia short-horizon agreement
  10_eta_scan.png            E6: attractor window collapse in u = s*sqrt(eta)
  11_time_domain.png         E7a: pulsed TD, funneling + IFC-locked cascade
  12_truncation.png          E7b: corridor capture vs unit cells; kx front

Languages: --lang en (default) | ru. Output dir override: --out.
"""

from __future__ import annotations

import csv
import json
import math
import os
import sys
from collections import defaultdict

import matplotlib
matplotlib.use("Agg")
import matplotlib.font_manager as fm
for f in ("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
          "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"):
    if os.path.exists(f):
        fm.fontManager.addfont(f)
import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ray_billiard import Medium, chamber_hexagon_asym, chirality_index, \
    distance_to_loop, propagate_ray

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, ".."))
DATA = os.path.join(ROOT, "data")
FIG = os.path.join(ROOT, "figures")
os.makedirs(FIG, exist_ok=True)

plt.rcParams["font.sans-serif"] = ["DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False
plt.rcParams["figure.dpi"] = 150
plt.rcParams["axes.spines.top"] = False
plt.rcParams["axes.spines.right"] = False

# palette (T34 conventions)
ACCENT = "#256a8c"
ACCENT2 = "#ce7354"
HEADER = "#3d4e56"
BORDER = "#a5bac4"
MUTED = "#83898d"
SUCCESS = "#458d5d"
ERROR = "#99534d"

ETA = 100.0
HYP = Medium("hyperbolic", eta=ETA)
ISO = Medium("isotropic")
CH = chamber_hexagon_asym(s_left=0.03, s_right=0.06, y_v=0.35)

# ------------------------------------------------------------------ labels --
LABELS = {
    "ru": {
        "fig01_a": "(а) камера и аттрактор (период 22)",
        "fig01_hyperbola": "дисперсионная гипербола",
        "fig01_b": r"(б) конус групповой скорости, $\alpha_{max}$ = 5.71°",
        "bounce_no": "номер отражения",
        "k_before_slope": r"$|k|$ перед отражением от склона",
        "q_conv": "показатель геометрической сходимости q",
        "n_rays": "число лучей",
        "median_q": "медиана q = {v:.3f}",
        "attractor": "аттрактор",
        "fig03_a": "(а) гиперболическая среда: захват на маршрут",
        "fig03_b": "(б) изотропный контроль: хаос без захвата",
        "slope_len": "длина склона s",
        "yv_label": "нижняя граница вертикальной стены $y_v$",
        "lock_share": "доля лучей, захваченных аттрактором",
        "fig05_a": "(а) исходная камера",
        "fig05_b": "(б) зеркальная камера",
        "band": "полоса f = {band}",
        "route": "маршрут аттрактора",
        "ray_density": "плотность пути лучей (норм.)",
        "alpha_circ": r"$|\alpha|$ (циркуляция вихря)",
        "winding": "фазовый вигвун W (обороты)",
        "pj_dev": "Python ↔ Julia, макс. откл. (100 отражений)",
        "tol": "допуск 10⁻⁸",
        "freq_inv": "K = 1 ↔ K = 7 (частотная инвариантность)",
        "ray_no": "номер луча",
        "max_dev": "макс. отклонение точек отскока",
        "u_var": r"$u = s\,\sqrt{\eta}$",
        "lock_frac": "доля захваченных лучей",
        "resonance": r"резонанс $s^{*} = 1/\sqrt{\eta}$",
        "window_fit": "окно аттрактора (фит)",
        "eta_label": r"$\eta$",
        "channel_H": "анизотропия каналализации H",
        "iso_base": "изотропный уровень 0.5",
        "wave_eta": r"полосно-усреднённая $|E|^2$",
        "time": "время t",
        "corridor_F": r"доля энергии в коридоре $F(t)$",
        "hyp_med": "гиперболическая среда",
        "iso_med": "изотропный контроль",
        "kspec": r"$|E_{\mathbf{k}}|^2$ (log$_{10}$)",
        "ifc": r"IFC: $k_y^2 - k_x^2/\eta = k_0^2$",
        "n_cells": "число ячеек $N$",
        "cap_peak": "пиковый захват коридора",
        "wavelengths": "длин волн поперёк камеры $L/\\lambda_0$",
        "kx_front": r"фронт каскада $|k_x|_{99}$",
        "fold": r"складка IFC $\approx\omega_p/c$",
        "nyquist": "Найквист сетки",
        "snap_t": "t = {t:g}",
    },
    "en": {
        "fig01_a": "(a) chamber and attractor (period 22)",
        "fig01_hyperbola": "dispersion hyperbola",
        "fig01_b": r"(b) group-velocity cone, $\alpha_{max}$ = 5.71°",
        "bounce_no": "bounce number",
        "k_before_slope": r"$|k|$ before slope bounce",
        "q_conv": "geometric convergence exponent q",
        "n_rays": "number of rays",
        "median_q": "median q = {v:.3f}",
        "attractor": "attractor",
        "fig03_a": "(a) hyperbolic medium: capture onto the route",
        "fig03_b": "(b) isotropic control: chaos without capture",
        "slope_len": "slope length s",
        "yv_label": r"vertical-wall lower bound $y_v$",
        "lock_share": "fraction of rays captured by the attractor",
        "fig05_a": "(a) original chamber",
        "fig05_b": "(b) mirrored chamber",
        "band": "band f = {band}",
        "route": "attractor route",
        "ray_density": "ray path density (norm.)",
        "alpha_circ": r"$|\alpha|$ (vortex circulation)",
        "winding": "phase winding W (turns)",
        "pj_dev": "Python ↔ Julia, max deviation (100 bounces)",
        "tol": "tolerance 10⁻⁸",
        "freq_inv": "K = 1 ↔ K = 7 (frequency invariance)",
        "ray_no": "ray index",
        "max_dev": "max deviation of bounce points",
        "u_var": r"$u = s\,\sqrt{\eta}$",
        "lock_frac": "locked-ray fraction",
        "resonance": r"resonance $s^{*} = 1/\sqrt{\eta}$",
        "window_fit": "attractor window (fit)",
        "eta_label": r"$\eta$",
        "channel_H": "channeling anisotropy H",
        "iso_base": "isotropic baseline 0.5",
        "wave_eta": r"band-averaged $|E|^2$",
        "time": "time t",
        "corridor_F": r"corridor energy fraction $F(t)$",
        "hyp_med": "hyperbolic medium",
        "iso_med": "isotropic control",
        "kspec": r"$|E_{\mathbf{k}}|^2$ (log$_{10}$)",
        "ifc": r"IFC: $k_y^2 - k_x^2/\eta = k_0^2$",
        "n_cells": "unit cells $N$",
        "cap_peak": "peak corridor capture",
        "wavelengths": r"wavelengths across chamber $L/\lambda_0$",
        "kx_front": r"cascade front $|k_x|_{99}$",
        "fold": r"IFC fold $\approx\omega_p/c$",
        "nyquist": "grid Nyquist",
        "snap_t": "t = {t:g}",
    },
}


def get_cli():
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--lang", choices=["en", "ru"], default="en")
    ap.add_argument("--out", default=None,
                    help="output dir (default: ../figures)")
    return ap.parse_args()


ARGS = get_cli()
L = LABELS[ARGS.lang]
# --out is CWD-relative (standard behaviour); the Makefile targets pass
# paths relative to wave_attractors/scripts, e.g. --out ../figures
FIG = ARGS.out or os.path.join(ROOT, "figures")
os.makedirs(FIG, exist_ok=True)


def style_ax(ax):
    ax.grid(True, linestyle="--", alpha=0.2, linewidth=0.5)
    ax.spines["bottom"].set_color(BORDER)
    ax.spines["left"].set_color(BORDER)
    ax.tick_params(colors=HEADER)


def read_rows(path):
    with open(path) as f:
        return list(csv.DictReader(f))


def draw_chamber(ax, ch, color=HEADER, lw=1.4):
    v = ch.vertices
    ax.plot(v[:, 0], v[:, 1], color=color, lw=lw, zorder=3)
    ax.set_aspect("equal")
    ax.set_xlim(-0.05, 1.05)
    ax.set_ylim(-0.05, 1.05)
    ax.set_xticks([])
    ax.set_yticks([])


# ── reference route (one ray, deterministic) ────────────────────────────────
def reference_route():
    rng = np.random.default_rng(1000)
    p0 = np.array([0.25 + 0.5 * rng.uniform(), 0.85])
    kx = rng.uniform(-1.5, 1.5)
    ky = math.sqrt(1.0 + kx * kx / ETA)
    res = propagate_ray(CH, HYP, p0, np.array([kx, -ky]), 1.0,
                        max_bounces=1600, loop_tol=1e-7, loop_window=100)
    return res


# ════════════════════════════════════════════════════════════════════════════
# Fig 01 — chamber, route, cone
# ════════════════════════════════════════════════════════════════════════════
def fig01():
    res = reference_route()
    loop = res.closed_loop
    lp = np.vstack([loop, loop[:1]])

    fig, axes = plt.subplots(1, 2, figsize=(10.5, 4.6),
                             constrained_layout=True)
    ax = axes[0]
    draw_chamber(ax, CH)
    ax.plot(lp[:, 0], lp[:, 1], color=ACCENT, lw=1.1, alpha=0.9)
    ax.plot(loop[:, 0], loop[:, 1], "o", color=ACCENT2, ms=4, zorder=4)
    ax.set_title(L["fig01_a"], fontsize=11, color=HEADER)

    ax = axes[1]
    eta = 100.0
    kx = np.linspace(-4, 4, 401)
    ky = np.sqrt(1.0 + kx * kx / eta)
    ax.plot(kx, ky, color=ACCENT, lw=2.0, label=L["fig01_hyperbola"])
    ax.plot(kx, -ky, color=ACCENT, lw=2.0)
    for sgn in (1, -1):
        xs = np.linspace(0, 3.4, 10)
        ax.plot(sgn * xs / math.sqrt(eta) * math.sqrt(eta) / math.sqrt(eta),
                sgn * xs, color=MUTED, ls=":", lw=1.2)
    vg = np.column_stack([-kx / eta, ky])
    ang = np.degrees(np.arctan2(vg[:, 0], vg[:, 1]))
    cone = math.degrees(math.atan(1.0 / math.sqrt(eta)))
    th = np.linspace(0, 2 * np.pi, 241)
    ax.fill_between([-0.9, 0.9], [0, 0], [1.6, 1.6], color="#f2f2f2",
                    zorder=0)
    for sgn in (1, -1):
        xs = np.array([0, sgn * math.sin(math.radians(cone)) * 1.5])
        ys = np.array([0, math.cos(math.radians(cone)) * 1.5])
        ax.plot(xs, ys, color=ERROR, lw=1.8)
    ax.set_xlim(-4, 4); ax.set_ylim(-4, 4)
    ax.set_xlabel(r"$k_x$", fontsize=10)
    ax.set_ylabel(r"$k_y$", fontsize=10)
    ax.set_title(L["fig01_b"], fontsize=11, color=HEADER)
    style_ax(ax)
    fig.savefig(os.path.join(FIG, "01_chambers_and_cone.png"), dpi=300)
    plt.close(fig)


# ════════════════════════════════════════════════════════════════════════════
# Fig 02 — cascade
# ════════════════════════════════════════════════════════════════════════════
def fig02():
    rows = read_rows(os.path.join(DATA, "E1_cascade_slope_hits.csv"))
    conv = read_rows(os.path.join(DATA, "E1_convergence.csv"))

    fig, axes = plt.subplots(1, 2, figsize=(10.5, 4.2),
                             constrained_layout=True)
    ax = axes[0]
    by_ray = defaultdict(list)
    for r in rows:
        by_ray[int(r["ray"])].append((int(r["bounce"]), float(r["k_before"])))
    for ir in sorted(by_ray)[:10]:
        pts = sorted(by_ray[ir])
        ax.plot([p[0] for p in pts], [p[1] for p in pts], color=ACCENT,
                lw=0.8, alpha=0.5)
    ax.set_yscale("log")
    ax.set_xlabel(L["bounce_no"], fontsize=10)
    ax.set_ylabel(L["k_before_slope"], fontsize=10)
    style_ax(ax)

    ax = axes[1]
    qs = []
    for r in conv:
        if r["q_fit"] not in ("", "nan"):
            qs.append(float(r["q_fit"]))
    ax.hist(qs, bins=14, color=ACCENT, alpha=0.75, edgecolor="white")
    ax.axvline(float(np.median(qs)), color=ERROR, ls="--", lw=1.6,
               label=L["median_q"].format(v=float(np.median(qs))))
    ax.set_xlabel(L["q_conv"], fontsize=10)
    ax.set_ylabel(L["n_rays"], fontsize=10)
    ax.legend(fontsize=9, frameon=False)
    style_ax(ax)
    fig.savefig(os.path.join(FIG, "02_cascade.png"), dpi=300)
    plt.close(fig)


# ════════════════════════════════════════════════════════════════════════════
# Fig 03 — attractor vs isotropic control
# ════════════════════════════════════════════════════════════════════════════
def fig03():
    res_ref = reference_route()
    loop = res_ref.closed_loop
    lp = np.vstack([loop, loop[:1]])

    fig, axes = plt.subplots(1, 2, figsize=(10.5, 4.6),
                             constrained_layout=True)
    rng = np.random.default_rng(2000)
    ax = axes[0]
    draw_chamber(ax, CH)
    for ir in range(14):
        p0 = np.array([0.25 + 0.5 * rng.uniform(), 0.85])
        kx = rng.uniform(-1.5, 1.5)
        ky = math.sqrt(1.0 + kx * kx / ETA)
        try:
            res = propagate_ray(CH, HYP, p0, np.array([kx, -ky]), 1.0,
                                max_bounces=250)
        except RuntimeError:
            continue
        pts = res.bounce_points
        ax.plot(pts[:, 0], pts[:, 1], color=ACCENT, lw=0.5, alpha=0.45)
    ax.plot(lp[:, 0], lp[:, 1], color=ERROR, lw=1.8, label=L["attractor"])
    ax.legend(fontsize=9, frameon=False, loc="lower right")
    ax.set_title(L["fig03_a"], fontsize=11, color=HEADER)

    ax = axes[1]
    draw_chamber(ax, CH)
    rng = np.random.default_rng(2000)
    for ir in range(14):
        p0 = np.array([0.25 + 0.5 * rng.uniform(), 0.85])
        kx = rng.uniform(-1.5, 1.5)
        ky = math.sqrt(max(1e-6, 1.0 - 0.3 * kx * kx))
        try:
            res = propagate_ray(CH, ISO, p0, np.array([kx, -ky]), 1.0,
                                max_bounces=250)
        except RuntimeError:
            continue
        pts = res.bounce_points
        ax.plot(pts[:, 0], pts[:, 1], color=MUTED, lw=0.5, alpha=0.45)
    ax.set_title(L["fig03_b"], fontsize=11, color=HEADER)
    fig.savefig(os.path.join(FIG, "03_attractor_vs_control.png"), dpi=300)
    plt.close(fig)


# ════════════════════════════════════════════════════════════════════════════
# Fig 04 — phase diagram
# ════════════════════════════════════════════════════════════════════════════
def fig04():
    rows = read_rows(os.path.join(DATA, "E5_phase_diagram.csv"))
    ss = sorted({float(r["s_slope"]) for r in rows})
    yv = sorted({float(r["y_v"]) for r in rows})
    ZL = np.zeros((len(yv), len(ss)))
    ZC = np.zeros((len(yv), len(ss)))
    for r in rows:
        i = yv.index(float(r["y_v"]))
        j = ss.index(float(r["s_slope"]))
        n = int(r["n_loop"]) + int(r["n_corner"]) + int(r["n_channel"])
        ZL[i, j] = int(r["n_loop"]) / n
        ZC[i, j] = int(r["n_corner"]) / n
    fig, ax = plt.subplots(figsize=(7.6, 4.6), constrained_layout=True)
    im = ax.imshow(ZL, cmap="YlGnBu", origin="lower", aspect="auto",
                   vmin=0, vmax=1)
    ax.set_xticks(range(len(ss)), [f"{s:g}" for s in ss])
    ax.set_yticks(range(len(yv)), [f"{v:g}" for v in yv])
    ax.set_xlabel(L["slope_len"], fontsize=10)
    ax.set_ylabel(L["yv_label"], fontsize=10)
    for i in range(len(yv)):
        for j in range(len(ss)):
            ax.text(j, i, f"{ZL[i, j]:.2f}", ha="center", va="center",
                    fontsize=8,
                    color="white" if ZL[i, j] > 0.55 else "black")
    cb = fig.colorbar(im, ax=ax, shrink=0.85)
    cb.set_label(L["lock_share"], fontsize=9)
    style_ax(ax)
    fig.savefig(os.path.join(FIG, "04_phase_diagram.png"), dpi=300)
    plt.close(fig)


# ════════════════════════════════════════════════════════════════════════════
# Fig 05 — chirality
# ════════════════════════════════════════════════════════════════════════════
def fig05():
    # mirror chamber
    v = CH.vertices.copy()
    xc = 0.5 * (v[:, 0].min() + v[:, 0].max())
    v[:, 0] = 2 * xc - v[:, 0]
    CHM = type(CH)(vertices=v[::-1], name="mirror")

    rng = np.random.default_rng(3000)
    p0 = np.array([0.25 + 0.5 * rng.uniform(), 0.85])
    kx = rng.uniform(-1.5, 1.5)
    ky = math.sqrt(1.0 + kx * kx / ETA)
    r1 = propagate_ray(CH, HYP, p0, np.array([kx, -ky]), 1.0,
                       max_bounces=1600, loop_tol=1e-7, loop_window=100)
    pm, km = p0.copy(), np.array([-kx, -ky])
    pm[0] = 2 * xc - pm[0]
    r2 = propagate_ray(CHM, HYP, pm, km, 1.0, max_bounces=1600,
                       loop_tol=1e-7, loop_window=100)
    c1 = chirality_index(r1.closed_loop)
    c2 = chirality_index(r2.closed_loop)

    fig, axes = plt.subplots(1, 2, figsize=(10.5, 4.6),
                             constrained_layout=True)
    for ax, ch, res, c, ttl in (
            (axes[0], CH, r1, c1, L["fig05_a"]),
            (axes[1], CHM, r2, c2, L["fig05_b"])):
        draw_chamber(ax, ch)
        lp = np.vstack([res.closed_loop, res.closed_loop[:1]])
        ax.plot(lp[:, 0], lp[:, 1], color=ACCENT if c < 0 else ACCENT2,
                lw=1.4)
        ax.set_title(f"{ttl}, C = {c:+.4f}", fontsize=11, color=HEADER)
    fig.savefig(os.path.join(FIG, "05_chirality.png"), dpi=300)
    plt.close(fig)


# ════════════════════════════════════════════════════════════════════════════
# Fig 06 — wave maps (band-averaged Helmholtz)
# ════════════════════════════════════════════════════════════════════════════
def fig06():
    d = np.load(os.path.join(DATA, "E4_wave_maps.npz"))
    res_ref = reference_route()
    loop = res_ref.closed_loop
    lp = np.vstack([loop, loop[:1]])
    keys = [k for k in d.files if k.startswith("f")]
    fig, axes = plt.subplots(1, len(keys), figsize=(11.2, 4.0),
                             constrained_layout=True)
    for ax, key in zip(axes, keys):
        inten = d[key]
        im = ax.imshow(inten.T, origin="lower", extent=[0, 1, 0, 1],
                       cmap="magma", vmax=np.percentile(inten, 99.0),
                       aspect="equal")
        v = CH.vertices
        ax.plot(v[:, 0], v[:, 1], color="white", lw=1.0, alpha=0.8)
        ax.plot(lp[:, 0], lp[:, 1], color="cyan", lw=1.0, alpha=0.9)
        ax.set_xticks([]); ax.set_yticks([])
        band = {"f6": "5.6–6.8", "f9": "8.6–9.8", "f14": "13.2–14.4"}.get(key, key)
        ax.set_title(L["band"].format(band=band), fontsize=10, color=HEADER)
        fig.colorbar(im, ax=ax, shrink=0.8)
    fig.savefig(os.path.join(FIG, "06_wave_maps.png"), dpi=300)
    plt.close(fig)


# ════════════════════════════════════════════════════════════════════════════
# Fig 07 — ray-density energy map
# ════════════════════════════════════════════════════════════════════════════
def fig07():
    d = np.load(os.path.join(DATA, "E4_ray_density.npz"))
    H, D = d["H"], d["D"]
    res_ref = reference_route()
    loop = res_ref.closed_loop
    lp = np.vstack([loop, loop[:1]])
    fig, ax = plt.subplots(figsize=(6.4, 5.6), constrained_layout=True)
    im = ax.imshow(H.T, origin="lower", extent=[0, 1, 0, 1], cmap="inferno",
                   aspect="equal")
    v = CH.vertices
    ax.plot(v[:, 0], v[:, 1], color="white", lw=1.2, alpha=0.9)
    ax.plot(lp[:, 0], lp[:, 1], color="cyan", lw=1.2, alpha=0.9,
            label=L["route"])
    ax.legend(fontsize=9, frameon=False, loc="upper right")
    ax.set_xticks([]); ax.set_yticks([])
    fig.colorbar(im, ax=ax, shrink=0.85, label=L["ray_density"])
    fig.savefig(os.path.join(FIG, "07_ray_density.png"), dpi=300)
    plt.close(fig)


# ════════════════════════════════════════════════════════════════════════════
# Fig 08 — AB water companion
# ════════════════════════════════════════════════════════════════════════════
def fig08():
    sys.path.insert(0, HERE)
    from ab_water import ab_state, N_R, N_TH, R_CORE, R_MAX
    metrics = json.load(open(os.path.join(DATA, "AB_water_metrics.json")))
    alphas = metrics["alphas"]
    wind = metrics["phase_winding"]

    r = np.linspace(0.05, R_MAX, N_R)
    th = np.linspace(0.0, 2.0 * np.pi, N_TH, endpoint=False)
    Rg, THg = np.meshgrid(r, th, indexing="ij")
    Xg, Yg = Rg * np.cos(THg), Rg * np.sin(THg)

    fig = plt.figure(figsize=(11.0, 4.4), constrained_layout=True)
    gs = fig.add_gridspec(1, 3)
    for col, alpha in ((0, 0.3), (1, -0.3)):
        ax = fig.add_subplot(gs[0, col])
        psi = ab_state(alpha, 0.0, r, th) + ab_state(alpha, np.pi, r, th)
        psi = psi * np.exp(-1j * 8.0 * 0.125 * 2 * np.pi / 8.0)
        f = psi.real
        vmax = np.percentile(np.abs(f), 99)
        ax.pcolormesh(Xg, Yg, f, cmap="RdBu_r", vmin=-vmax, vmax=vmax,
                      shading="nearest", rasterized=True)
        ax.plot(0, 0, "k+", ms=10)
        ax.set_aspect("equal")
        ax.set_xlim(-6, 6); ax.set_ylim(-6, 6)
        ax.set_title(f"$\\psi_{{total}}$, α = {alpha:+.1f} (t = T/8)",
                     fontsize=10, color=HEADER)
        ax.set_xticks([]); ax.set_yticks([])

    ax = fig.add_subplot(gs[0, 2])
    a_list = sorted({abs(a) for a in alphas})
    w_pos = [wind[alphas.index(a)] for a in a_list]
    w_neg = [wind[alphas.index(-a)] for a in a_list]
    ax.plot(a_list, w_neg, "o-", color=ACCENT, label=r"$W(\alpha{<}0)$")
    ax.plot(a_list, w_pos, "s-", color=ACCENT2, label=r"$W(\alpha{>}0)$")
    ax.plot(a_list, a_list, ":", color=MUTED, lw=1.2, label=r"$W = |\alpha|$")
    ax.set_xlabel(L["alpha_circ"], fontsize=10)
    ax.set_ylabel(L["winding"], fontsize=10)
    ax.legend(fontsize=8, frameon=False)
    style_ax(ax)
    fig.savefig(os.path.join(FIG, "08_ab_water.png"), dpi=300)
    plt.close(fig)


# ════════════════════════════════════════════════════════════════════════════
# Fig 09 — cross verification
# ════════════════════════════════════════════════════════════════════════════
def fig09():
    cv_path = os.path.join(DATA, "cross_verification.json")
    if not os.path.exists(cv_path):
        # Python-vs-Julia cross-verification is produced by the optional Julia
        # tier (`make wave-attractors-julia`). Without it, fig 09 is skipped so
        # the pure-Python pipeline stays reproducible end to end.
        print("[fig] 09 SKIPPED (cross_verification.json missing — "
              "run 'make wave-attractors-julia' first)", flush=True)
        return
    cv = json.load(open(cv_path))
    inv = json.load(open(os.path.join(DATA, "E4_frequency_invariance.json")))
    dev = cv["level1_short_horizon"]["per_ray_max_dev"]
    rays = sorted(dev, key=int)
    vals = [dev[r] for r in rays]

    fig, ax = plt.subplots(figsize=(8.4, 4.2), constrained_layout=True)
    ax.semilogy(rays, [max(v, 1e-18) for v in vals], "o", color=ACCENT,
                ms=6, label=L["pj_dev"])
    ax.axhline(1e-8, color=MUTED, ls="--", lw=1.3, label=L["tol"])
    ax.axhline(inv["max_position_deviation"], color=SUCCESS, ls=":", lw=1.6,
               label=L["freq_inv"])
    ax.set_xlabel(L["ray_no"], fontsize=10)
    ax.set_ylabel(L["max_dev"], fontsize=10)
    ax.set_ylim(1e-17, 1e-6)
    ax.legend(fontsize=9, frameon=False)
    style_ax(ax)
    fig.savefig(os.path.join(FIG, "09_cross_verification.png"), dpi=300)
    plt.close(fig)


# ════════════════════════════════════════════════════════════════════════════
# Fig 10 — E6: eta scan, universal window in u = s*sqrt(eta)
# ════════════════════════════════════════════════════════════════════════════
def fig10():
    rows = read_rows(os.path.join(DATA, "E6_eta_scan.csv"))
    summ = json.load(open(os.path.join(DATA, "E6_summary.json")))
    fit = summ["ray_scan"]["window_fit"]
    coll = fit.get("collapse", {})
    wsum = summ["wave_scan"]["runs"]

    fig, axes = plt.subplots(1, 3, figsize=(13.6, 4.3),
                             constrained_layout=True)

    # (a) collapse of lock curves in u
    ax = axes[0]
    colors = {9.0: ACCENT, 16.0: ACCENT2, 25.0: SUCCESS, 100.0: HEADER,
              400.0: ERROR}
    for eta in sorted({float(r["eta"]) for r in rows}):
        rs = sorted([r for r in rows if float(r["eta"]) == eta],
                    key=lambda r: float(r["u"]))
        ax.plot([float(r["u"]) for r in rs], [float(r["lock_frac"]) for r in rs],
                "o-", ms=3.5, lw=1.0, color=colors[eta],
                label=fr"$\eta$ = {eta:g}")
    if coll:
        ax.axvspan(coll["u1_mean"], coll["u2_mean"], color=SUCCESS, alpha=0.10,
                   label=L["window_fit"])
    ax.axvline(1.0, color=MUTED, ls=":", lw=1.4)
    ax.text(1.02, 0.06, L["resonance"], rotation=90, fontsize=8, color=MUTED)
    ax.set_xlabel(L["u_var"], fontsize=10)
    ax.set_ylabel(L["lock_frac"], fontsize=10)
    ax.legend(fontsize=7.5, frameon=False, loc="upper right")
    style_ax(ax)

    # (b) per-eta windows in u
    ax = axes[1]
    etas = sorted(int(k) for k in fit if k.isdigit())
    for i, eta in enumerate(etas):
        lo = fit[str(eta)]["window_lo_u"]
        hi = fit[str(eta)]["window_hi_u"]
        if lo is None:
            continue
        ax.barh(i, hi - lo, left=lo, height=0.55, color=colors[float(eta)],
                alpha=0.75)
    if coll:
        ax.axvline(coll["u1_mean"], color=HEADER, lw=1.6)
        ax.axvline(coll["u2_mean"], color=HEADER, lw=1.6)
        ax.axvspan(coll["u1_mean"] - coll["u1_std"],
                   coll["u1_mean"] + coll["u1_std"], color=HEADER, alpha=0.12)
        ax.axvspan(coll["u2_mean"] - coll["u2_std"],
                   coll["u2_mean"] + coll["u2_std"], color=HEADER, alpha=0.12)
        ax.text(coll["u1_mean"], len(etas) - 0.3,
                f"$u_1$ = {coll['u1_mean']:.2f}±{coll['u1_std']:.2f}",
                fontsize=8.5, ha="center", color=HEADER)
        ax.text(coll["u2_mean"], len(etas) - 0.3,
                f"$u_2$ = {coll['u2_mean']:.2f}±{coll['u2_std']:.2f}",
                fontsize=8.5, ha="center", color=HEADER)
    ax.set_yticks(range(len(etas)), [fr"$\eta$ = {e}" for e in etas])
    ax.set_xlabel(L["u_var"], fontsize=10)
    ax.set_ylim(-0.6, len(etas) + 0.4)
    style_ax(ax)

    # (c) wave-model channeling anisotropy vs eta
    ax = axes[2]
    we = sorted(int(k) for k in wsum)
    Hs = [wsum[str(e)]["channeling_anisotropy_H"] for e in we]
    ax.plot(we, Hs, "s-", color=ACCENT, ms=6, lw=1.4)
    ax.axhline(0.5, color=MUTED, ls=":", lw=1.3, label=L["iso_base"])
    ax.set_xscale("log")
    ax.set_ylim(0.4, 1.0)
    ax.set_xlabel(L["eta_label"], fontsize=10)
    ax.set_ylabel(L["channel_H"], fontsize=10)
    ax.legend(fontsize=8, frameon=False)
    style_ax(ax)
    fig.savefig(os.path.join(FIG, "10_eta_scan.png"), dpi=300)
    plt.close(fig)


# ════════════════════════════════════════════════════════════════════════════
# Fig 11 — E7a: pulsed time domain, funneling + IFC-locked cascade
# ════════════════════════════════════════════════════════════════════════════
def fig11():
    d = np.load(os.path.join(DATA, "E7_td_snapshots.npz"))
    ks = np.load(os.path.join(DATA, "E7_kspectra.npz"))
    summ = json.load(open(os.path.join(DATA, "E7_summary.json")))
    mr = summ["main_run"]
    res_ref = reference_route()
    loop = res_ref.closed_loop
    lp = np.vstack([loop, loop[:1]])
    route = np.minimum(d["route"], 0.5)

    fig, axes = plt.subplots(2, 3, figsize=(13.6, 8.0),
                             constrained_layout=True)
    # (a,b) hyperbolic snapshots; (c) isotropic control
    panels = [("hyp_t6", "hyp_med"), ("hyp_t40", "hyp_med"),
              ("iso_t40", "iso_med")]
    for ax, (key, med_key) in zip(axes[0], panels):
        I = d[key]
        t = key.split("_")[1]
        im = ax.imshow(I.T, origin="lower", extent=[0, 1, 0, 1], cmap="magma",
                       vmin=0, vmax=np.percentile(I, 99.6), aspect="equal")
        ax.plot(lp[:, 0], lp[:, 1], color="cyan", lw=0.9, alpha=0.85)
        ax.set_xticks([]); ax.set_yticks([])
        ax.set_title(f"{L[med_key]}, {L['snap_t'].format(t=float(t[1:]))}",
                     fontsize=10, color=HEADER)
        fig.colorbar(im, ax=ax, shrink=0.8)

    # (d) corridor fraction curves
    ax = axes[1, 0]
    fr = read_rows(os.path.join(DATA, "E7_route_fraction.csv"))
    ts = [float(r["t"]) for r in fr]
    ax.plot(ts, [float(r["route_fraction_hyper"]) for r in fr], "-",
            color=ACCENT, lw=1.4, label=L["hyp_med"])
    ax.plot(ts, [float(r["route_fraction_iso"]) for r in fr], "-",
            color=MUTED, lw=1.4, label=L["iso_med"])
    ax.axhline(mr["corridor_area_fraction"], color=BORDER, ls=":", lw=1.2)
    ax.set_xlabel(L["time"], fontsize=10)
    ax.set_ylabel(L["corridor_F"], fontsize=10)
    ax.legend(fontsize=8, frameon=False)
    style_ax(ax)

    # (e) k-space spectrum with IFC overlay
    ax = axes[1, 1]
    k = ks["k"]
    F = ks["t24"] if "t24" in ks.files else ks[ks.files[-1]]
    ax.imshow(np.log10(F + 1e-40).T, origin="lower",
              extent=[-k.max(), k.max(), -k.max(), k.max()], cmap="viridis",
              vmin=-16, vmax=-5, aspect="equal")
    kxs = np.linspace(0, 0.45 * k.max(), 120)
    k0 = mr["omega0"]
    eta = mr["eta_eff"]
    ax.plot(kxs, np.sqrt(k0**2 + kxs**2 / eta), "r--", lw=1.0, label=L["ifc"])
    ax.plot(-kxs, np.sqrt(k0**2 + kxs**2 / eta), "r--", lw=1.0)
    ax.plot(kxs, -np.sqrt(k0**2 + kxs**2 / eta), "r--", lw=1.0)
    ax.plot(-kxs, -np.sqrt(k0**2 + kxs**2 / eta), "r--", lw=1.0)
    ax.set_xlim(-0.5 * k.max(), 0.5 * k.max())
    ax.set_ylim(-0.5 * k.max(), 0.5 * k.max())
    ax.set_xlabel(r"$k_x$", fontsize=10)
    ax.set_ylabel(r"$k_y$", fontsize=10)
    ax.legend(fontsize=7.5, frameon=False, loc="upper right")
    style_ax(ax)

    # (f) kx marginal at two times
    ax = axes[1, 2]
    for key, col in (("t3", ACCENT), ("t40", ERROR)):
        if key not in ks.files:
            continue
        Fs = ks[key]
        marg = Fs.sum(axis=1)
        sel = (k >= 0) & (k <= 500)
        ax.plot(k[sel], marg[sel] / marg[sel].max(), "-", color=col, lw=1.2,
                label=L["snap_t"].format(t=float(key[1:])))
    ax.axvline(mr["kx_fold_edge"], color=HEADER, ls="--", lw=1.3,
               label=L["fold"])
    ax.set_xlabel(r"$k_x$", fontsize=10)
    ax.set_ylabel(L["kspec"], fontsize=10)
    ax.legend(fontsize=8, frameon=False)
    style_ax(ax)
    fig.savefig(os.path.join(FIG, "11_time_domain.png"), dpi=300)
    plt.close(fig)


# ════════════════════════════════════════════════════════════════════════════
# Fig 12 — E7b: unit-cell truncation scan + cascade front saturation
# ════════════════════════════════════════════════════════════════════════════
def fig12():
    rows = read_rows(os.path.join(DATA, "E7_truncation_scan.csv"))
    summ = json.load(open(os.path.join(DATA, "E7_summary.json")))
    mr = summ["main_run"]

    fig, axes = plt.subplots(1, 2, figsize=(11.6, 4.4),
                             constrained_layout=True)
    # (a) peak capture vs N_cells
    ax = axes[0]
    ns = [int(r["n_cells"]) for r in rows]
    cap = [float(r["capture_peak"]) for r in rows]
    ax.plot(ns, cap, "o-", color=ACCENT, ms=6, lw=1.5)
    ax.set_xlabel(L["n_cells"], fontsize=10)
    ax.set_ylabel(L["cap_peak"], fontsize=10)
    ax.set_xscale("log")
    ax.set_yscale("log")
    for r in rows:
        ax.annotate(f"{float(r['wavelengths_across_chamber']):.1f} $\\lambda$",
                    (int(r["n_cells"]), float(r["capture_peak"])),
                    textcoords="offset points", xytext=(6, -3), fontsize=8,
                    color=MUTED)
    style_ax(ax)

    # (b) cascade front saturation
    ax = axes[1]
    kf = mr.get("kx_front", {})
    ts = sorted(float(k[1:]) for k in kf)
    vals = [kf[f"t{t:g}"] for t in ts]
    ax.plot(ts, vals, "s-", color=ACCENT2, ms=6, lw=1.5)
    ax.axhline(mr["kx_fold_edge"], color=HEADER, ls="--", lw=1.4,
               label=L["fold"])
    ax.axhline(math.pi * (mr["n_grid"] - 1), color=MUTED, ls=":", lw=1.3,
               label=L["nyquist"])
    ax.set_xlabel(L["time"], fontsize=10)
    ax.set_ylabel(L["kx_front"], fontsize=10)
    ax.set_ylim(0, math.pi * (mr["n_grid"] - 1) * 1.05)
    ax.legend(fontsize=8, frameon=False)
    style_ax(ax)
    fig.savefig(os.path.join(FIG, "12_truncation.png"), dpi=300)
    plt.close(fig)


if __name__ == "__main__":
    print(f"[fig] lang={ARGS.lang}, out={FIG}", flush=True)
    print("[fig] 01 ...", flush=True); fig01()
    print("[fig] 02 ...", flush=True); fig02()
    print("[fig] 03 ...", flush=True); fig03()
    print("[fig] 04 ...", flush=True); fig04()
    print("[fig] 05 ...", flush=True); fig05()
    print("[fig] 06 ...", flush=True); fig06()
    print("[fig] 07 ...", flush=True); fig07()
    print("[fig] 08 ...", flush=True); fig08()
    print("[fig] 09 ...", flush=True); fig09()
    print("[fig] 10 ...", flush=True); fig10()
    print("[fig] 11 ...", flush=True); fig11()
    print("[fig] 12 ...", flush=True); fig12()
    print("[fig] all figures done ->", FIG, flush=True)
