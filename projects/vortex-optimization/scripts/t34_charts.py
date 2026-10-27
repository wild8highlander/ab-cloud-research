"""
t34_charts.py — визуализации исследования для PDF-отчёта (русские подписи).
Запускать ПОСЛЕ завершения стадии C. Палитра = cascade (cold/minimal, seed 34).
Внутренние заголовки НЕ ставятся (подписи рисунков — в PDF, правило charts.md).
"""
import csv
import json
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.font_manager as fm
for f in ("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
          "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"):
    if os.path.exists(f):
        fm.fontManager.addfont(f)
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.sans-serif"] = ["DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False
plt.rcParams["figure.dpi"] = 150
plt.rcParams["axes.spines.top"] = False
plt.rcParams["axes.spines.right"] = False

OUT = "/home/z/my-project/download/t34_research"
CH = os.path.join(OUT, "charts")
os.makedirs(CH, exist_ok=True)

# ── палитра (cascade, cold/minimal, seed 34) ─────────────────────────────────
ACCENT = "#256a8c"       # XS series_1
ACCENT2 = "#ce7354"      # XS series_2 (geometric hue)
HEADER = "#3d4e56"       # M
ICON = "#496b7c"         # S
BORDER = "#a5bac4"
MUTED = "#83898d"
SUCCESS = "#458d5d"
ERROR = "#99534d"


def read_rows(path):
    with open(path) as f:
        return list(csv.DictReader(f))


def style_ax(ax):
    ax.grid(True, linestyle="--", alpha=0.2, linewidth=0.5)
    ax.spines["bottom"].set_color(BORDER)
    ax.spines["left"].set_color(BORDER)
    ax.tick_params(colors=HEADER)


def base_rows(rows, L):
    out = []
    for r in rows:
        if int(r["L"]) == L and r["placement"] == "protocol" and \
           r["bc"] == "open" and abs(float(r["alpha"]) - 0.5) < 1e-9 and \
           int(r["Nv"]) > 0:
            out.append(r)
    return out


rowsA = read_rows(os.path.join(OUT, "sweep_A_L24.csv"))
ctlA = 0.0324

# ── Рис. 1. Heatmap D(Nv × q) при W=1.0 и W=0.5 ─────────────────────────────
fig, axes = plt.subplots(1, 2, figsize=(11, 4.0), constrained_layout=True)
for ax, W in zip(axes, (1.0, 0.5)):
    Nvs = sorted({int(r["Nv"]) for r in base_rows(rowsA, 24)})
    Qs = sorted({float(r["q"]) for r in base_rows(rowsA, 24)})
    Z = np.full((len(Nvs), len(Qs)), np.nan)
    for r in base_rows(rowsA, 24):
        if abs(float(r["W"]) - W) < 1e-9:
            Z[Nvs.index(int(r["Nv"])), Qs.index(float(r["q"]))] = \
                float(r["D_pooled"])
    im = ax.imshow(Z, cmap="RdYlGn_r", aspect="auto", origin="lower",
                   vmin=0.0, vmax=0.55)
    ax.set_xticks(range(len(Qs)), [f"{q:g}" for q in Qs])
    ax.set_yticks(range(len(Nvs)), [str(n) for n in Nvs])
    ax.set_xlabel("заряд вихря q", fontsize=10)
    ax.set_ylabel("число вихрей Nv", fontsize=10)
    ax.set_title(f"W = {W:g}", fontsize=11, color=HEADER)
    for i in range(len(Nvs)):
        for j in range(len(Qs)):
            if np.isfinite(Z[i, j]):
                ax.text(j, i, f"{Z[i,j]:.2f}", ha="center", va="center",
                        fontsize=6.8, color="black")
    cb = fig.colorbar(im, ax=ax, shrink=0.85)
    cb.set_label("KS D", fontsize=9)
fig.savefig(os.path.join(CH, "01_heatmap_D_Nv_q.png"), bbox_inches="tight")
plt.close(fig)

# ── Рис. 2. Кривые D(Nv) при q=1.0 ───────────────────────────────────────────
fig, ax = plt.subplots(figsize=(8.0, 4.6), constrained_layout=True)
for W, col in ((0.0, MUTED), (0.5, SUCCESS), (1.0, ACCENT)):
    pts = {}
    for r in base_rows(rowsA, 24):
        if abs(float(r["q"]) - 1.0) < 1e-9 and abs(float(r["W"]) - W) < 1e-9:
            pts[int(r["Nv"])] = float(r["D_pooled"])
    xs = sorted(pts)
    ax.plot(xs, [pts[x] for x in xs], "o-", color=col, label=f"W = {W:g}",
            lw=2.2, ms=4.5)
ax.axhline(ctlA, color=ERROR, ls="--", lw=1.4,
           label=f"GUE-контроль, D = {ctlA:.3f}")
ax.axhline(0.10, color=MUTED, ls=":", lw=1.4, label="порог теста 34, D = 0.10")
ax.set_xlabel("число вихрей Nv  (L = 24, q = 1.0, α = 0.5)", fontsize=10)
ax.set_ylabel("KS D (pooled vs 50k нулей ζ)", fontsize=10)
ax.set_yscale("log")
style_ax(ax)
ax.legend(fontsize=9, frameon=False, loc="upper right")
fig.savefig(os.path.join(CH, "02_D_of_Nv.png"), bbox_inches="tight")
plt.close(fig)

# ── Рис. 3. D(q) при Nv=16 ───────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(8.0, 4.6), constrained_layout=True)
for W, col in ((0.0, MUTED), (0.5, SUCCESS), (1.0, ACCENT)):
    pts = {}
    for r in base_rows(rowsA, 24):
        if int(r["Nv"]) == 16 and abs(float(r["W"]) - W) < 1e-9:
            pts[float(r["q"])] = float(r["D_pooled"])
    xs = sorted(pts)
    ax.plot(xs, [pts[x] for x in xs], "s-", color=col, label=f"W = {W:g}",
            lw=2.2, ms=4.5)
ax.axhline(ctlA, color=ERROR, ls="--", lw=1.4, label="GUE-контроль (пол)")
ax.axhline(0.10, color=MUTED, ls=":", lw=1.4, label="порог теста 34")
ax.set_xlabel("заряд вихря q  (L = 24, Nv = 16 — плотность 2.8%, α = 0.5)",
              fontsize=10)
ax.set_ylabel("KS D (pooled vs ζ)", fontsize=10)
style_ax(ax)
ax.legend(fontsize=9, frameon=False)
fig.savefig(os.path.join(CH, "03_D_of_q.png"), bbox_inches="tight")
plt.close(fig)

# ── Рис. 4. L-лестница топ-кандидатов (стадия B) ─────────────────────────────
rowsB = read_rows(os.path.join(OUT, "sweep_B_refine.csv"))
fig, ax = plt.subplots(figsize=(8.4, 4.8), constrained_layout=True)


def key_of(r):
    return (int(r["Nv"]), float(r["q"]), float(r["W"]), float(r["alpha"]),
            r["bc"], r["placement"])


series = {}
for r in rowsB:
    series.setdefault(key_of(r), {})[int(r["L"])] = float(r["D_pooled"])
best_of = {k: min(v.values()) for k, v in series.items()}
top = sorted(best_of, key=best_of.get)[:6]
palette = [ACCENT, ACCENT2, SUCCESS, "#937a48", ICON, MUTED]
for k, col in zip(top, palette):
    Nv, q, W, al, bc, pl = k
    pts = series[k]
    xs = sorted(pts)
    lab = f"Nv={Nv}, q={q:g}, W={W:g}"
    if abs(al - 0.5) > 1e-9:
        lab += f", α={al:g}"
    if bc != "open" or pl != "protocol":
        lab += f", {bc}/{pl}"
    ax.plot(xs, [pts[x] for x in xs], "o-", color=col, lw=2.0, ms=4.5,
            label=lab)
floor = {24: 0.0324, 32: 0.0331, 48: 0.0309, 64: 0.0257}
Ls = sorted(floor)
ax.plot(Ls, [floor[L] for L in Ls], "--", color="black", lw=1.4,
        label="GUE-контроль (пол)")
ax.set_xlabel("размер решётки L", fontsize=10)
ax.set_ylabel("KS D (pooled vs ζ)", fontsize=10)
style_ax(ax)
ax.legend(fontsize=8, frameon=False, loc="upper left", bbox_to_anchor=(0, 1))
fig.savefig(os.path.join(CH, "04_L_ladder.png"), bbox_inches="tight")
plt.close(fig)

# ── Рис. 5. α-скан (L=32, Nv=16, q=1.0, W=0.5) ──────────────────────────────
fig, ax = plt.subplots(figsize=(7.2, 4.2), constrained_layout=True)
alpha_pts = {}
for r in rowsB:
    if int(r["L"]) == 32 and int(r["Nv"]) == 16 and abs(float(r["q"]) - 1.0) < 1e-9 \
       and abs(float(r["W"]) - 0.5) < 1e-9 and r["placement"] == "protocol" \
       and r["bc"] == "open":
        alpha_pts[float(r["alpha"])] = float(r["D_pooled"])
xs = sorted(alpha_pts)
ax.plot(xs, [alpha_pts[x] for x in xs], "D-", color=ACCENT, lw=2.2, ms=6)
for x in xs:
    ax.annotate(f"{alpha_pts[x]:.3f}", (x, alpha_pts[x]),
                textcoords="offset points", xytext=(0, 9), ha="center",
                fontsize=9, color=HEADER)
ax.axvline(0.5, color=SUCCESS, ls="--", lw=1.4, alpha=0.8)
ax.text(0.5, ax.get_ylim()[1] * 0.02, "критическая линия α = 0.5", ha="center",
        fontsize=9, color=SUCCESS)
ax.set_xlabel("магнитный поток α на ячейку", fontsize=10)
ax.set_ylabel("KS D (pooled vs ζ)", fontsize=10)
ax.set_xticks(xs)
style_ax(ax)
fig.savefig(os.path.join(CH, "05_alpha_scan.png"), bbox_inches="tight")
plt.close(fig)

# ── Рис. 6-7 из стадии C (если завершена) ────────────────────────────────────
pathC = os.path.join(OUT, "sweep_C_L96.csv")
if os.path.exists(pathC):
    rowsC = read_rows(pathC)
    # Рис. 6. R₂(s): победитель + референс vs ζ и GUE
    fig, ax = plt.subplots(figsize=(8.2, 4.8), constrained_layout=True)
    npz_files = sorted(f for f in os.listdir(OUT) if f.startswith("R2_L96_"))
    colors6 = [ACCENT, ACCENT2, SUCCESS, MUTED]
    for i, f in enumerate(npz_files[:4]):
        d = np.load(os.path.join(OUT, f))
        tag = f.replace("R2_L96_", "").replace(".npz", "")
        ax.plot(d["s_grid"], d["R2_ab"], "-", color=colors6[i], lw=1.8,
                label=f"AB: {tag}")
    d0 = np.load(os.path.join(OUT, npz_files[0]))
    ax.plot(d0["s_grid"], d0["R2_zeta"], "o", color="black", ms=3.5,
            label="ζ (50k нулей)")
    ax.plot(d0["s_grid"], d0["R2_gue"], "--", color=MUTED, lw=1.6,
            label="GUE: 1 − sinc²(πs)")
    ax.set_xlabel("s (в средних расстояниях)", fontsize=10)
    ax.set_ylabel("R₂(s) — корреляция пар", fontsize=10)
    style_ax(ax)
    ax.legend(fontsize=7.6, frameon=False, loc="upper right")
    fig.savefig(os.path.join(CH, "06_R2_s.png"), bbox_inches="tight")
    plt.close(fig)

    # Рис. 7. Стабильность: per-realization D для 4 конфигураций 96×96
    fig, ax = plt.subplots(figsize=(8.2, 4.4), constrained_layout=True)
    labels, mins, meds, maxs = [], [], [], []
    for r in rowsC:
        labels.append(f"Nv={r['Nv']}, q={float(r['q']):g}\n"
                      f"α={float(r['alpha']):g}, {r['bc']}/{r['placement']}")
        mins.append(float(r["D_min"]))
        meds.append(float(r["D_med"]))
        maxs.append(float(r["D_max"]))
    x = np.arange(len(labels))
    ax.vlines(x, mins, maxs, color=BORDER, lw=6, alpha=0.55,
              label="разброс D по реализациям")
    ax.plot(x, meds, "o", color=ACCENT, ms=8, label="медиана D")
    ax.plot(x, meds, "_", color="white", ms=14, markeredgewidth=0)
    ax.axhline(0.10, color=ERROR, ls="--", lw=1.4, label="порог теста 34 = 0.10")
    ctlC = 0.0062
    if os.path.exists(os.path.join(OUT, "gue_control_L96.json")):
        ctlC = json.load(open(os.path.join(OUT, "gue_control_L96.json")))["D_gue_vs_zeta"]
    ax.axhline(ctlC, color=SUCCESS, ls=":", lw=1.4,
               label=f"GUE-контроль L=96, D = {ctlC:.4f}")
    for i, m in enumerate(meds):
        ax.annotate(f"{m:.4f}", (x[i], m), textcoords="offset points",
                    xytext=(14, -4), fontsize=9, color=HEADER)
    ax.set_xticks(x, labels, fontsize=8.5)
    ax.set_ylabel("KS D vs ζ (96×96, 5 реализаций)", fontsize=10)
    style_ax(ax)
    ax.legend(fontsize=8.5, frameon=False, loc="upper right")
    fig.savefig(os.path.join(CH, "07_stability.png"), bbox_inches="tight")
    plt.close(fig)

print("графики готовы:", sorted(os.listdir(CH)))
