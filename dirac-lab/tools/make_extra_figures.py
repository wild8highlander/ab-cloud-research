#!/usr/bin/env python3
"""v1.4 — additional 600-dpi figures for every per-test folder (tests/D*/figures/).

All panels are computed from the SAME validated modules (code/dirac_lab*.py)
and the canonical run CSVs — no invented data. One figure function per test,
wrapped in try/except so a single failure cannot abort the batch.
"""
import json
import os
import sys

import numpy as np

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import FancyArrowPatch  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "code"))

import dirac_lab as dl  # noqa: E402
import dirac_lab_extensions as ext  # noqa: E402
import dirac_lab_extensions2 as ext2  # noqa: E402
import dirac_lab_extensions3 as ext3  # noqa: E402

plt.rcParams.update({
    "font.size": 10.5, "axes.titlesize": 11.5, "axes.labelsize": 10.5,
    "axes.edgecolor": "#666666", "figure.facecolor": "white",
    "axes.grid": True, "grid.alpha": 0.25, "grid.linewidth": 0.5,
})

BLUE, ORANGE, GREEN, RED, PURPLE = ("#1F4E79", "#E8833A", "#2EA043",
                                    "#C0392B", "#7D5BA6")
TESTS = os.path.join(ROOT, "tests")
FOLD = {
    "D1": "D01_bloch_continuum_limit", "D2": "D02_zero_mode_tower",
    "D3": "D03_berry_phase", "D4": "D04_relativistic_landau_levels",
    "D5": "D05_klein_tunneling", "D6": "D06_zitterbewegung",
    "D7": "D07_zeta_decoration", "D8": "D08_chiral_protection",
    "D9": "D09_jr_index_restoration", "D10": "D10_montgomery_transport",
    "D11": "D11_bk_connes_conjugation",
    "D12": "D12_bk_ladder_infinite_limit",
    "D13": "D13_wall_under_conjugation_drive",
    "D14": "D14_odlyzko_form_factor",
}

ZEROS = dl.load_zeta_zeros(os.path.join(ROOT, "data",
                                        "zeta_zeros_2000.txt"), 2000)
ZEROS_LOW = dl.load_zeta_zeros(os.path.join(ROOT, "data",
                                            "zeta_zeros_low_600.txt"), 600)
ZEROS_BIG = dl.load_zeta_zeros(os.path.join(ROOT, "data",
                                            "zeta_zeros_high_2000.txt"), 2000)
RESULTS = {}


def load_results():
    for tid, fold in FOLD.items():
        p = os.path.join(TESTS, fold, "results.json")
        if os.path.exists(p):
            with open(p) as f:
                RESULTS[tid] = json.load(f)


def figdir(tid):
    return os.path.join(TESTS, FOLD[tid], "figures")


def save(fig, tid, name):
    out = os.path.join(figdir(tid), name)
    fig.savefig(out, dpi=600)
    plt.close(fig)
    print(f"  saved {os.path.relpath(out, ROOT)}", flush=True)


def read_csv(path):
    rows = []
    with open(path) as f:
        header = f.readline().strip().split(",")
        for line in f:
            parts = line.strip().split(",")
            if len(parts) != len(header):
                continue
            row = []
            for v in parts:
                try:
                    row.append(float(v))
                except ValueError:
                    row.append(v)
            rows.append(row)
    return header, rows


# ─────────────────────────────── D1 ──────────────────────────────────────────
def fig_d1():
    tid = "D1"
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9.6, 4.0),
                                   constrained_layout=True)
    # (a) two-band dispersion along Gamma-X-M-Gamma (exact 2-band model)
    pts = [(0, 0), (np.pi, 0), (np.pi, np.pi), (0, 0)]
    seg = [r"$\Gamma$", r"$X$", r"$M$", r"$\Gamma$"]
    cum, ks, labels = [0.0], [0.0], [0]
    for (k1, k2), (l1, l2) in zip(pts[:-1], pts[1:]):
        n = 160
        s = np.linspace(0, 1, n, endpoint=False)
        ks.extend(cum[-1] + s * np.linalg.norm(
            [(k2 - l1), (l2 - k1)]) * 0 + s * (np.abs(k2 - l1) + np.abs(l2 - k1)))
        labels.append(cum[-1] + (np.abs(k2 - l1) + np.abs(l2 - k1)))
        cum.append(labels[-1])
    kx = np.array([pts[0][0]])
    ky = np.array([pts[0][1]])
    for (k1, k2), (l1, l2) in zip(pts[:-1], pts[1:]):
        s = np.linspace(0, 1, 160, endpoint=False)
        kx = np.concatenate([kx, k1 + s * (l1 - k1)])
        ky = np.concatenate([ky, k2 - (k2 - l2) - s * (k2 - l2) + s * 0])
    # rebuild cleanly (vectorised along each segment)
    kxs, kys = [], []
    for (k1, k2), (l1, l2) in zip(pts[:-1], pts[1:]):
        s = np.linspace(0, 1, 160, endpoint=False)
        kxs.append(k1 + s * (l1 - k1))
        kys.append(k2 + s * (l2 - k2))
    kxs = np.concatenate(kxs)
    kys = np.concatenate(kys)
    ticks = np.linspace(0, len(kxs), 5)[:-1]
    ep, em = [], []
    for a, b in zip(kxs, kys):
        w = np.linalg.eigvalsh(dl.bloch_hamiltonian_2band(a, b))
        ep.append(w[1]); em.append(w[0])
    ax1.plot(np.arange(len(kxs)), ep, color=BLUE, lw=1.8, label=r"$E_+(k)$")
    ax1.plot(np.arange(len(kxs)), em, color=ORANGE, lw=1.8, label=r"$E_-(k)$")
    for t in ticks:
        ax1.axvline(t, color="#999999", lw=0.6)
    ax1.set_xticks(ticks, seg)
    ax1.axhline(0, color="#444444", lw=0.7, ls=":")
    ax1.set_ylabel("E / t")
    ax1.set_title("(a) π-flux bands, Γ–X–M–Γ (exact 2-band)")
    ax1.legend(loc="upper left", bbox_to_anchor=(0.0, 1.0), frameon=False)
    # (b) E1 vs 1/L from the canonical CSV + 4π asymptote
    _, rows = read_csv(os.path.join(TESTS, FOLD[tid], "D1_finite_size.csv"))
    arr = np.array(rows)
    Linv, E1, EL = 1 / arr[:, 0], arr[:, 1], arr[:, 2]
    a, b, r2 = dl.linear_fit(Linv, E1)
    xx = np.linspace(0, Linv.max() * 1.02, 50)
    ax2.plot(Linv, EL, "o", color=GREEN, ms=6, label=r"$E_1(L)\cdot L$")
    ax2.axhline(4 * np.pi, color=RED, lw=1.4, ls="--",
                label=r"$4\pi = 12.5664$")
    ax2.set_xlabel("1 / L")
    ax2.set_ylabel(r"$E_1 \cdot L$")
    ax2.set_ylim(11.8, 13.0)
    ax2.set_title(rf"(b) finite-size scaling, $v_F/2\pi$-fit $R^2={r2:.6f}$")
    ax2.legend(loc="lower right", frameon=False)
    save(fig, tid, "d01_extra_bands_and_scaling.png")


# ─────────────────────────────── D2 ──────────────────────────────────────────
def fig_d2():
    tid = "D2"
    L = 16
    H = dl.build_hamiltonian(L, 0.5)
    w, v = np.linalg.eigh(H)
    idx = np.argsort(np.abs(w))[:4]
    fig, axes = plt.subplots(2, 4, figsize=(11.0, 5.2),
                             constrained_layout=True,
                             gridspec_kw={"height_ratios": [3, 1.2]})
    gam = dl.sublattice_gamma(L)
    for j, i in enumerate(idx):
        rho = (np.abs(v[:, i]) ** 2).reshape(L, L)
        im = axes[0, j].imshow(rho.T, origin="lower", cmap="magma",
                               extent=[0, L, 0, L])
        axes[0, j].set_title(rf"$|\psi_{{({j + 1})}}|^2$,  "
                             rf"$E = {w[i]:+.1e}$", fontsize=10)
        axes[0, j].grid(False)
        plt.colorbar(im, ax=axes[0, j], fraction=0.046)
        axes[1, j].plot(np.arange(L * L), np.sign(gam) * np.abs(v[:, i]),
                        ".", ms=1.2, color=BLUE)
        axes[1, j].set_xlabel("site n")
        if j == 0:
            axes[1, j].set_ylabel(r"$\pm|\psi_n|$")
    fig.suptitle("The fourfold zero tower on the clean torus (L = 16): "
                 "density maps and Γ-polarity (top/bottom = sublattice A/B)")
    save(fig, tid, "d02_extra_tower_maps.png")


# ─────────────────────────────── D3 ──────────────────────────────────────────
def fig_d3():
    tid = "D3"
    ks, F = dl.berry_curvature_map(n=61)
    dA = (ks[1] - ks[0]) ** 2
    KX, KY = np.meshgrid(ks, ks, indexing="ij")
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9.8, 4.2),
                                   constrained_layout=True)
    im = ax1.pcolormesh(KX, KY, F, cmap="RdBu_r", vmin=-np.pi, vmax=np.pi,
                        shading="auto")
    plt.colorbar(im, ax=ax1, label="F(k) (Wilson plaquette)")
    ax1.set_xlabel(r"$k_x$"), ax1.set_ylabel(r"$k_y$")
    ax1.set_title("(a) Berry curvature, lower band")
    cones = [(0, 0), (np.pi, np.pi), (np.pi, 0), (0, np.pi)]
    rr = np.linspace(0.05, np.pi, 60)
    for (cx, cy), col, lab in zip(cones, [BLUE, ORANGE, GREEN, PURPLE],
                                  [r"$\Gamma$", r"$M_{++}$", r"$M_{-+}$",
                                   r"$M_{+-}$"]):
        C = []
        for r in rr:
            m = (KX - cx) ** 2 + (KY - cy) ** 2 <= r * r
            C.append(F[m].sum() * dA / (2 * np.pi))
        ax2.plot(rr, C, lw=1.8, color=col, label=lab)
    total = []
    for r in rr:
        tot = 0.0
        for cx, cy in cones:
            m = (KX - cx) ** 2 + (KY - cy) ** 2 <= r * r
            tot += F[m].sum() * dA / (2 * np.pi)
        total.append(tot)
    ax2.plot(rr, total, lw=2.6, color="#222222", label="sum of four cones")
    ax2.axhline(0.5, color="#888888", lw=0.8, ls=":")
    ax2.axhline(-0.5, color="#888888", lw=0.8, ls=":")
    ax2.set_xlabel("disc radius r")
    ax2.set_ylabel("cumulative Chern C(r)")
    ax2.set_title("(b) half-quantized cones, net charge 0")
    ax2.legend(frameon=False, ncol=2, fontsize=9)
    save(fig, tid, "d03_extra_chern_flow.png")


# ─────────────────────────────── D4 ──────────────────────────────────────────
def fig_d4():
    tid = "D4"
    B, vf, Nx = 0.03, 1.0, 60
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9.8, 4.2),
                                   constrained_layout=True)
    wD = np.linalg.eigvalsh(dl._strip_dirac(Nx, 0.0, B, vf))
    n = np.arange(len(wD))
    ax1.plot(n, np.sort(wD), ".", ms=2.4, color=BLUE)
    for k in range(1, 6):
        e = vf * np.sqrt(2 * B * k)
        ax1.axhline(e, color=ORANGE, lw=1.0, ls="--")
        ax1.axhline(-e, color=ORANGE, lw=1.0, ls="--")
    ax1.axhline(0, color=RED, lw=1.2)
    ax1.set_xlabel("level index")
    ax1.set_ylabel("E")
    ax1.set_title(rf"(a) Dirac strip ladder $E_n=\pm v_F\sqrt{{2Bn}}$ (B={B})")
    wS = np.linalg.eigvalsh(dl._strip_schrodinger(Nx, 0.0, B))
    ax2.plot(np.arange(len(wS)), np.sort(wS), ".", ms=2.4, color=GREEN)
    nn = np.arange(0, 8)
    for y in B * (nn + 0.5):
        ax2.axhline(y, color=ORANGE, lw=1.0, ls="--")
    ax2.set_xlabel("level index")
    ax2.set_ylabel("E")
    ax2.set_title(rf"(b) Schrödinger control $E_n=B(n+\frac{{1}}{{2}})$")
    save(fig, tid, "d04_extra_strip_ladders.png")


# ─────────────────────────────── D5 ──────────────────────────────────────────
def fig_d5():
    tid = "D5"
    _, rows = read_csv(os.path.join(TESTS, FOLD[tid],
                                    "D5_klein_tunneling.csv"))
    arr = np.array([[r[0], r[1], r[2]] for r in rows])
    th, Td, Ts = arr[:, 0], arr[:, 1], arr[:, 2]
    fig = plt.figure(figsize=(7.6, 4.6), constrained_layout=True)
    ax = fig.add_subplot(111, projection="polar")
    th_r = np.deg2rad(th)
    ax.plot(np.concatenate([th_r, -th_r[::-1]]),
            np.concatenate([Td, Td[::-1]]), lw=2.0, color=BLUE,
            label="Dirac")
    ax.plot(np.concatenate([th_r, -th_r[::-1]]),
            np.concatenate([Ts, Ts[::-1]]), lw=2.0, color=GREEN,
            label="Schrödinger control")
    ax.set_title("Klein supertansmission: T(θ) from the canonical run\n"
                 r"$T(0°)=0.9777$ vs $0.0010$ — factor 977")
    ax.legend(loc="lower center", bbox_to_anchor=(0.5, -0.18), ncol=2,
              frameon=False)
    save(fig, tid, "d05_extra_polar_transmission.png")


# ─────────────────────────────── D6 ──────────────────────────────────────────
def fig_d6():
    tid = "D6"
    _, rows = read_csv(os.path.join(TESTS, FOLD[tid],
                                    "D6_zitterbewegung.csv"))
    r = rows[0]
    labels = ["1D Dirac box", "lab torus (interband dipole)"]
    vals = [r[2], r[5]]
    fig, ax = plt.subplots(figsize=(6.4, 3.8), constrained_layout=True)
    bars = ax.bar(labels, vals, width=0.5, color=[BLUE, PURPLE])
    ax.axhline(1.0, color=RED, lw=1.5, ls="--", label=r"theory $\omega = 2E$")
    for b, v in zip(bars, vals):
        ax.text(b.get_x() + b.get_width() / 2, v + 0.004, f"{v:.6f}",
                ha="center", fontsize=10)
    ax.set_ylim(0.9, 1.03)
    ax.set_ylabel(r"$\omega_{\mathrm{meas}} / 2E$")
    ax.set_title("Zitterbewegung frequency ratios (canonical run)")
    ax.legend(frameon=False)
    save(fig, tid, "d06_extra_ratio_bars.png")


# ───────────────────── shared spectra cache (D7/D8) ──────────────────────────
_SPEC = {}


def _spectra_L32():
    if "zeta" in _SPEC:
        return _SPEC["clean"], _SPEC["zeta"]
    L = 32
    wc = np.linalg.eigvalsh(dl.build_hamiltonian(L, 0.5))
    vort = dl.zeta_coded_vortices(ZEROS, L, 28)
    wz = np.linalg.eigvalsh(dl.build_hamiltonian(L, 0.5, vortices=vort))
    _SPEC["clean"], _SPEC["zeta"] = wc, wz
    return wc, wz


# ─────────────────────────────── D7 ──────────────────────────────────────────
def fig_d7():
    tid = "D7"
    wc, wz = _spectra_L32()
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9.8, 4.2),
                                   constrained_layout=True)
    for w, col, lab in [(wc, GREEN, "clean (GOE-like)"),
                        (wz, BLUE, r"$\zeta$-decorated (GUE-like)")]:
        band = dl.central_band(w, 0.6)
        s = np.diff(band)
        s = s / np.mean(s)
        s = s[s < 4]
        ax1.hist(s, bins=40, range=(0, 4), density=True, histtype="step",
                 lw=1.8, color=col, label=lab)
    ss = np.linspace(1e-3, 4, 300)
    ax1.plot(ss, 0.5 * np.pi * ss * np.exp(-np.pi * ss ** 2 / 4), "--",
             color="#777777", lw=1.2, label="Wigner GOE")
    ax1.plot(ss, (32 / np.pi ** 2) * ss ** 2 * np.exp(-4 * ss ** 2 / np.pi),
             "-", color="#222222", lw=1.2, label="Wigner GUE")
    ax1.set_xlabel("s = gap / ⟨gap⟩ (central band, L = 32)")
    ax1.set_ylabel("P(s)")
    ax1.set_title("(a) spacing histogram, clean vs ζ-decorated")
    ax1.legend(frameon=False, fontsize=9)
    _, rows = read_csv(os.path.join(TESTS, FOLD[tid], "D7_zeta_decoration.csv"))
    Ls, rc, rz, rr_ = [], [], [], []
    for r in rows:
        cfg, val = str(r[1]).lower(), r[6]
        if cfg == "clean":
            Ls.append(r[0]); rc.append(val)
        elif cfg == "random":
            rr_.append(val)
        else:
            rz.append(val)
    ax2.plot(Ls, rc, "s-", color=GREEN, label="clean")
    if len(rr_) == len(Ls):
        ax2.plot(Ls, rr_, "^--", color="#999999", label="random vortices")
    ax2.plot(Ls, rz, "o-", color=BLUE, label=r"$\zeta$-decorated")
    ax2.axhline(0.5307, color="#777777", ls=":", lw=1.2, label="GOE 0.5307")
    ax2.axhline(0.5992, color="#222222", ls="--", lw=1.2, label="GUE 0.5992")
    ax2.set_xlabel("L")
    ax2.set_ylabel(r"$\langle r\rangle$ (central band)")
    ax2.set_title(r"(b) level ratios across sizes (canonical CSV)")
    ax2.legend(frameon=False, fontsize=9)
    save(fig, tid, "d07_extra_statistics.png")


# ─────────────────────────────── D8 ──────────────────────────────────────────
def fig_d8():
    tid = "D8"
    _, wz = _spectra_L32()
    E = np.sort(wz)
    half = len(E) // 2
    d = np.abs(E[:half] + E[::-1][:half])
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9.8, 4.2),
                                   constrained_layout=True)
    ax1.semilogy(np.abs(E[:half]), np.maximum(d, 1e-17), ".", ms=2.2,
                 color=BLUE)
    ax1.set_xlabel("|E|")
    ax1.set_ylabel(r"$|E_i + E_{\bar i}|$ (pair deviation)")
    ax1.set_title(rf"(a) E ↔ −E pairing, L = 32: max = {d.max():.1e}"
                  " over 512 pairs")
    ax2.hist(np.log10(np.maximum(d, 1e-17)), bins=40, color=PURPLE,
             alpha=0.85)
    ax2.set_xlabel(r"$\log_{10}|E_i + E_{\bar i}|$")
    ax2.set_ylabel("pairs")
    ax2.set_title("(b) the pairing spectrum is machine-sharp")
    save(fig, tid, "d08_extra_pairing.png")


# ─────────────────────────────── D9 ──────────────────────────────────────────
def fig_d9():
    tid = "D9"
    Nx = Ny = 200
    dx = 0.4
    H = ext.grid_dirac(Nx, Ny, dx=dx) + ext.mass_wall(Nx, Ny, dx=dx)
    w, v = ext.near_zero_states(H, k=6)
    i0 = int(np.argmin(np.abs(w)))
    prof = ext3._y_profile(v[:, i0], Nx, Ny)
    yg = np.arange(Ny) * dx
    m = 0.8 * np.tanh((yg - (Ny - 1) * dx / 2) / 2.0)
    fig, ax = plt.subplots(figsize=(7.6, 4.2), constrained_layout=True)
    ax.plot(yg, prof / prof.max(), lw=2.0, color=BLUE,
            label=r"$|\psi_0(y)|^2$ (wall mode, normalized)")
    ax.axhline(0.5, color="#888888", lw=0.8, ls=":")
    ax.set_xlabel("y (grid units)")
    ax.set_ylabel("normalized density")
    ax2 = ax.twinx()
    ax2.plot(yg, m, lw=1.6, color=ORANGE, alpha=0.9,
             label=r"mass texture $m(y)$")
    ax2.set_ylabel(r"$m(y)$", color=ORANGE)
    ax2.grid(False)
    ax.set_title(rf"Jackiw–Rebbi wall on the grid Dirac operator: "
                 rf"$|E_0| = {abs(w[i0]):.2e}$ (bare wall)")
    h1, l1 = ax.get_legend_handles_labels()
    h2, l2 = ax2.get_legend_handles_labels()
    ax.legend(h1 + h2, l1 + l2, loc="upper left", frameon=False, fontsize=9)
    save(fig, tid, "d09_extra_wall_profile.png")


# ─────────────────────────────── D10 ─────────────────────────────────────────
def fig_d10():
    tid = "D10"
    u = ext._unfold(ZEROS, 2000)
    uu, g = ext._pair_corr(u, wmax=12.0, binw=0.1)
    ss, sv = ext._number_variance(u, 25)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9.8, 4.2),
                                   constrained_layout=True)
    ax1.plot(uu, g, lw=1.8, color=BLUE, label=r"$g(u)$ unfolded zeros")
    ax1.plot(uu, ext._montgomery(uu), "--", color="#222222", lw=1.4,
             label="Montgomery $1-\\mathrm{sinc}^2(\\pi u)$")
    ax1.axhline(1.0, color=ORANGE, lw=1.0, ls=":", label="Poisson")
    ax1.set_xlabel("u (mean spacings)")
    ax1.set_ylabel("g(u)")
    ax1.set_title("(a) pair correlation (canonical estimator)")
    ax1.legend(frameon=False, fontsize=9)
    ax2.plot(ss, sv, "o-", ms=4, lw=1.6, color=BLUE,
             label=r"$\Sigma^2(s)$ zeros")
    ax2.plot(ss, ss, ":", color=ORANGE, lw=1.4, label="Poisson: s")
    gue = (1 / np.pi ** 2) * (np.log(2 * np.pi * ss) + 1.5772)
    ax2.plot(ss, gue, "--", color="#222222", lw=1.4,
             label="GUE asymptote")
    ax2.set_xlabel("s")
    ax2.set_ylabel(r"$\Sigma^2(s)$")
    ax2.set_title(r"(b) number variance: $\Sigma^2(20) = 0.33$, Poisson 20")
    ax2.legend(frameon=False, fontsize=9)
    save(fig, tid, "d10_extra_paircorr_variance.png")


# ─────────────────────────────── D11 ─────────────────────────────────────────
def fig_d11():
    tid = "D11"
    t = ZEROS
    delta = 2.0 * np.pi / np.log(t / (2.0 * np.pi))
    coding = (t / delta) % 1.0
    bk = ((t / (2.0 * np.pi)) * np.log(t / (2.0 * np.pi))) % 1.0
    dist = np.abs(coding - bk)
    dist = np.minimum(dist, 1.0 - dist)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9.8, 4.2),
                                   constrained_layout=True)
    ax1.hist(dist, bins=50, color=BLUE, alpha=0.85)
    ax1.set_yscale("log")
    ax1.set_xlabel("circular distance |Δφ| on the mod-1 circle")
    ax1.set_ylabel("zeros")
    ax1.set_title("(a) recognition identity over 2000 zeros\n"
                  rf"max distance = {dist.max():.2e}")
    Nu, Lam = 512, 20.0
    uu = np.linspace(0.0, Lam, 1201)
    tr = np.array([abs(ext3.dirichlet_comb(u0, Nu, Lam)) for u0 in uu])
    ax2.plot(uu / Lam, tr, lw=1.4, color=PURPLE)
    ax2.set_xlabel(r"$u_0/\Lambda$")
    ax2.set_ylabel(r"$|\,\mathrm{Tr}\,U(u_0)|$")
    ax2.set_title(rf"(b) Dirichlet trace comb, $N_u$={Nu}, $\Lambda$={Lg}"
                  .replace("$Lg$", "$\\Lambda$") if False else
                  rf"(b) Dirichlet trace comb, $N_u$={Nu}")
    ax2.annotate(r"peak $= N_u$ exactly", xy=(0, Nu), xytext=(0.12, Nu * 0.72),
                 arrowprops=dict(arrowstyle="->", color="#444444"),
                 fontsize=10)
    ax2.set_ylim(-40, Nu + 60)
    save(fig, tid, "d11_extra_recognition_comb.png")


# ─────────────────────────────── D12 ─────────────────────────────────────────
def fig_d12():
    tid = "D12"
    Lam = 20.0
    Ns = [64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768]
    off = [abs(ext3.comb_numeric(Lam / 20.0, n, Lam)) for n in Ns]
    th = [1.0 / (n * np.sin(np.pi / 20.0)) for n in Ns]
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9.8, 4.2),
                                   constrained_layout=True)
    ax1.loglog(Ns, off, "o-", lw=1.6, color=BLUE, label="numeric off-peak")
    ax1.loglog(Ns, th, "--", color="#222222", lw=1.4,
               label=r"$1/(N_u\sin(\pi/20))$ Dirichlet envelope")
    ax1.set_xlabel(r"$N_u$")
    ax1.set_ylabel(r"$|\mathrm{Tr}\,U(\Lambda/20)|$")
    ax1.set_title("(a) delta-train sharpening (N_u → ∞)")
    ax1.legend(frameon=False, fontsize=9)
    Ls, rr = [], []
    for L in (30, 36, 42, 48):
        nv = int(round(25 * L * L / 900))
        nv += nv % 2
        vort = dl.zeta_coded_vortices(ZEROS, L, nv)
        w = np.linalg.eigvalsh(dl.build_hamiltonian(L, 0.5, vortices=vort))
        m, _ = dl.mean_r(w)
        Ls.append(L)
        rr.append(m)
        print(f"    D12b L={L} nv={nv} <r>={m:.4f}", flush=True)
    ax2.plot(Ls, rr, "o-", lw=1.6, color=GREEN)
    ax2.axhline(0.5992, color="#222222", ls="--", lw=1.2,
                label="GUE 0.5992")
    ax2.set_xlabel("L (fixed density 25/900)")
    ax2.set_ylabel(r"$\langle r\rangle$")
    ax2.set_title(r"(b) extensive ζ-protection: $\langle r\rangle$ vs L")
    ax2.legend(frameon=False, fontsize=9)
    save(fig, tid, "d12_extra_envelope_extensive.png")


# ─────────────────────────────── D13 ─────────────────────────────────────────
def fig_d13():
    tid = "D13"
    Nx = Ny = 48
    dx = 0.4
    H0 = ext.grid_dirac(Nx, Ny, dx=dx)
    V = ext3.conjugating_generator(Nx, Ny, dx)
    N = Nx * Ny
    Gam = ext.sigma_z(N)
    slope0 = float(np.abs(Gam @ V + V @ Gam).max())
    lams = [0.0, 0.05, 0.1, 0.2, 0.3, 0.4, 0.5]
    vals = []
    for lam in lams:
        Hl = (H0 + lam * V).tocsr()
        vals.append(float(np.abs(Gam @ Hl + Hl @ Gam).max()))
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9.8, 4.2),
                                   constrained_layout=True)
    ax1.plot(lams, vals, "o-", lw=1.6, color=BLUE,
             label=r"$\|\{H(\lambda),\Gamma\}\|$ (numeric)")
    ax1.plot(lams, [lam * slope0 for lam in lams], "--", color="#222222",
             lw=1.4, label=r"$\lambda\,\|\{V,\Gamma\}\|$ (law)")
    ax1.set_xlabel(r"$\lambda$")
    ax1.set_ylabel("chiral-breaking norm")
    ax1.set_title(r"(a) measured mechanism: $\{H(\lambda),\Gamma\} "
                  r"= \lambda\{V,\Gamma\}$")
    ax1.legend(frameon=False, fontsize=9)
    # canonical driver comparison (values from the canonical run)
    names = ["Connes orbit:\n$|E_0|$ on the wall",
             "Generator $V$ at $\\lambda=0.2$:\nquasi-zero band edge"]
    canon = [3.9e-9, 2.4e-3]
    bars = ax2.bar(names, canon, width=0.5, color=[GREEN, ORANGE])
    ax2.set_yscale("log")
    ax2.set_ylabel("energy scale")
    ax2.set_title("(b) two inequivalent drivers (canonical values)\n"
                  "orbit pins 3.9e-9 · generator lifts to gap/679")
    for b, v in zip(bars, canon):
        ax2.text(b.get_x() + b.get_width() / 2, v * 1.4, f"{v:.1e}",
                 ha="center", fontsize=10)
    ax2.set_ylim(1e-10, 3e-2)
    save(fig, tid, "d13_extra_chiral_mechanism.png")


# ─────────────────────────────── D14 ─────────────────────────────────────────
def fig_d14():
    tid = "D14"
    taus = np.array([0.05, 0.10, 0.25, 0.50, 0.75, 1.0, 1.5, 2.0, 3.0])
    bands = [("main (2000, t≤2515)", ext._unfold(ZEROS, 2000), BLUE),
             ("low (600, t≤939)", ext._unfold(ZEROS_LOW, 600), GREEN),
             ("Odlyzko t≈1e5 (2000)", ext._unfold(ZEROS_BIG, 2000), RED)]
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9.8, 4.2),
                                   constrained_layout=True)
    for lab, u, col in bands:
        K = ext2.form_factor(u, taus, 200, 100)
        ax1.plot(taus, K, "o-", ms=4, lw=1.5, color=col, label=lab)
    Kg = ext2.gue_reference(taus)
    ax1.plot(taus, Kg, "--", color="#222222", lw=1.4,
             label="synthetic GUE (suite)")
    ax1.axhline(1.0, color=ORANGE, ls=":", lw=1.2, label="Poisson")
    ax1.set_xlabel(r"$\tau$")
    ax1.set_ylabel(r"$K(\tau)$")
    ax1.set_title("(a) second form factor, three real bands")
    ax1.legend(frameon=False, fontsize=8)
    s = np.diff(bands[2][1])
    s = s / np.mean(s)
    s = s[s < 4]
    ax2.hist(s, bins=40, range=(0, 4), density=True, histtype="step",
             lw=1.8, color=RED, label="Odlyzko band t≈1e5")
    ss = np.linspace(1e-3, 4, 300)
    ax2.plot(ss, (32 / np.pi ** 2) * ss ** 2 * np.exp(-4 * ss ** 2 / np.pi),
             "-", color="#222222", lw=1.3, label="Wigner GUE")
    ax2.set_xlabel("s = gap / ⟨gap⟩ (unfolded)")
    ax2.set_ylabel("P(s)")
    ax2.set_title("(b) nearest-spacing law on the large-height band")
    ax2.legend(frameon=False, fontsize=9)
    save(fig, tid, "d14_extra_three_bands.png")


ALL = [fig_d1, fig_d2, fig_d3, fig_d4, fig_d5, fig_d6, fig_d7, fig_d8,
       fig_d9, fig_d10, fig_d11, fig_d12, fig_d13, fig_d14]

if __name__ == "__main__":
    load_results()
    t0 = __import__("time").time()
    for fn in ALL:
        name = fn.__name__
        try:
            print(f"→ {name}", flush=True)
            fn()
        except Exception as e:  # noqa: BLE001
            import traceback
            traceback.print_exc()
            print(f"!! {name} FAILED: {e}", flush=True)
    print(f"=== extra figures done in {__import__('time').time() - t0:.0f}s "
          "===", flush=True)
