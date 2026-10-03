"""
abcloud.report — report writer + plot engine of the Python clone.

Generates, per test: report.md, plots/plot_01.png (and plot_02.png where the
test has a second panel) — mirroring the ABPlotV23 artefact layout of the
Julia suite, in matplotlib style adapted for print (light background).
"""

from __future__ import annotations

import datetime
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.font_manager as fm
import matplotlib.pyplot as plt
import numpy as np

# CJK-safe font setup (the clone ships English labels; DejaVu covers math glyphs)
for _fp in ("/usr/share/fonts/truetype/chinese/NotoSansSC-Regular.ttf",
            "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"):
    try:
        fm.fontManager.addfont(_fp)
    except Exception:
        pass
plt.rcParams["font.sans-serif"] = ["DejaVu Sans", "Noto Sans SC"]
plt.rcParams["axes.unicode_minus"] = False

ACCENT = "#2E5C8A"
ACCENT2 = "#B0533A"
MUTED = "#5B6B7D"
GRID = "#C9D2DC"

SLUGS = {
    1: "bN_convergence", 2: "bN_monotonicity", 3: "bN_rate",
    4: "gue_ks_full", 5: "gue_ks_highT", 6: "chi2_hist", 7: "decay_slope",
    8: "residuals", 9: "bootstrap_ci", 10: "cross_validation",
    11: "anderson_darling", 12: "two_sample_ks", 13: "number_variance",
    14: "spectral_rigidity", 15: "ab_construction", 16: "ab_gue_class",
    17: "connes_self_duality", 18: "chiral_AIII", 19: "dirac_cone",
    20: "chern_tknn", 21: "gamma_phase", 22: "ab_phase", 23: "fractal_factor",
    24: "dirac_string_flux", 25: "byers_yang", 26: "pbc_torus",
    27: "binary_chiral", 28: "f_gue_merit", 29: "dirac_dip", 30: "vf_scaling",
    31: "hatano_nelson", 32: "rmean_bootstrap", 33: "l_scaling_rmean",
    34: "direct_vs_zeta", 35: "form_factor_Kt", 36: "byte_robust",
    37: "half_factorial_gamma", 38: "curie_point",
}


def _style(ax):
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.grid(True, color=GRID, lw=0.6, alpha=0.6)
    ax.set_axisbelow(True)


def make_plots(entry: dict, cfg, gammas, grams, out_dir: Path):
    """Two-panel plot per test (statistic + verdict map)."""
    slug = SLUGS.get(entry["number"], f"test_{entry['number']}")
    pdir = out_dir / f"test_{entry['number']:02d}_{slug}" / "plots"
    pdir.mkdir(parents=True, exist_ok=True)
    tid = entry["number"]
    res = entry["passes"][0]
    m = res.get("metrics", {})

    fig, ax = plt.subplots(figsize=(8.0, 5.0), dpi=200, constrained_layout=True)
    plotted = True
    try:
        if tid in (1, 3, 7):
            n = cfg.zeros
            diffs = np.abs(gammas[:n] - grams[:n])
            grid = np.unique(np.round(np.geomspace(25, n, 60)).astype(int))
            b = np.array([np.mean(diffs[:k]) for k in grid])
            ax.loglog(grid, b, color=ACCENT, lw=2)
            ax.set_xlabel("N"); ax.set_ylabel("b(N)")
            ax.set_title(f"Test {tid}: b(N) convergence")
        elif tid in (4, 5):
            from .core import normalized_spacings, wigner_surmise_gue
            sp = normalized_spacings(gammas)
            ax.hist(sp[sp <= 3.5], bins=60, density=True, color=ACCENT, alpha=0.75, label="ζ zeros")
            s = np.linspace(0, 3.5, 400)
            ax.plot(s, wigner_surmise_gue(s), color=ACCENT2, lw=2, label="GUE surmise")
            ax.set_xlabel("s"); ax.set_ylabel("p(s)"); ax.legend()
            ax.set_title(f"Test {tid}: spacing distribution vs GUE (D = {m.get('D', float('nan')):.4f})")
        elif tid == 6:
            from .core import normalized_spacings, chi2_binned
            sp = normalized_spacings(gammas)
            chi2, dof, p, obs = chi2_binned(sp)
            ax.bar(range(len(obs)), obs, color=ACCENT, alpha=0.8)
            ax.set_xlabel("bin"); ax.set_ylabel("count")
            ax.set_title(f"Test 6: χ² histogram (χ²/dof = {chi2/max(dof,1):.2f})")
        elif tid == 2:
            n = cfg.zeros
            diffs = np.abs(gammas[:n] - grams[:n])
            grid = np.unique(np.round(np.geomspace(50, n, 500)).astype(int))
            b = np.array([np.mean(diffs[:k]) for k in grid])
            ax.semilogx(grid, b, color=ACCENT, lw=1.2)
            ax.set_xlabel("N"); ax.set_ylabel("b(N)")
            ax.set_title(f"Test 2: monotonicity ({m.get('violations', 0)} violations)")
        elif tid in (8,):
            n = cfg.zeros
            diffs = np.abs(gammas[:n] - grams[:n])
            grid = np.unique(np.round(np.geomspace(50, n, 60)).astype(int))
            b = np.array([np.mean(diffs[:k]) for k in grid])
            resid = np.log(b) - np.polyval(np.polyfit(np.log(grid), np.log(b), 1), np.log(grid))
            ax.plot(grid, resid, "o-", color=ACCENT, ms=4)
            ax.axhline(0, color=ACCENT2, lw=1)
            ax.set_xscale("log"); ax.set_xlabel("N"); ax.set_ylabel("residual")
            ax.set_title("Test 8: fit residuals")
        elif tid == 13:
            from .core import (number_variance_curve, sigma2_gue_reference,
                               sigma2_poisson_reference)
            Ls = [2, 3, 5, 8, 12, 20, 33, 54]
            _, sv = number_variance_curve(gammas, [L for L in Ls if L < len(gammas)//4])
            Lf = np.asarray([L for L in Ls if L < len(gammas)//4], dtype=float)
            ax.loglog(Lf, sv, "o-", color=ACCENT, label="data")
            ax.loglog(Lf, sigma2_gue_reference(Lf), "--", color=ACCENT2, label="GUE")
            ax.loglog(Lf, sigma2_poisson_reference(Lf), ":", color=MUTED, label="Poisson")
            ax.set_xlabel("L"); ax.set_ylabel("Σ²(L)"); ax.legend()
            ax.set_title("Test 13: number variance")
        elif tid == 14:
            from .core import (spectral_rigidity_curve, delta3_gue_reference,
                               delta3_poisson_reference)
            Ls = [2, 3, 5, 8, 12, 20, 33, 54]
            Lf2 = [L for L in Ls if L < len(gammas)//4]
            _, dv = spectral_rigidity_curve(gammas, Lf2)
            Lf = np.asarray(Lf2, dtype=float)
            ax.loglog(Lf, dv, "o-", color=ACCENT, label="data")
            ax.loglog(Lf, delta3_gue_reference(Lf), "--", color=ACCENT2, label="GUE")
            ax.loglog(Lf, delta3_poisson_reference(Lf), ":", color=MUTED, label="Poisson")
            ax.set_xlabel("L"); ax.set_ylabel("Δ₃(L)"); ax.legend()
            ax.set_title("Test 14: spectral rigidity")
        elif tid == 35:
            from .core import spectral_form_factor, k_gue_reference
            taus, K = spectral_form_factor(gammas, n_tau=80, t_max=3.0)
            ax.plot(taus, K, color=ACCENT, lw=2, label="K(t) data")
            ax.plot(taus, k_gue_reference(taus), "--", color=ACCENT2, lw=2, label="GUE")
            ax.set_xlabel("t"); ax.set_ylabel("K(t)"); ax.legend()
            ax.set_title("Test 35: spectral form factor")
        elif tid == 38:
            # re-run the quick magnetization curve for the plot
            rng = np.random.default_rng(cfg.seed)
            T_grid = np.linspace(1.6, 3.2, 9)
            L = 12
            mags = []
            for T in T_grid:
                s = np.ones((L, L), dtype=int)
                for _ in range(30):
                    for _ in range(L * L):
                        x, y = rng.integers(L), rng.integers(L)
                        nb = s[(x+1) % L, y] + s[(x-1) % L, y] + s[x, (y+1) % L] + s[x, (y-1) % L]
                        dE = 2 * s[x, y] * nb
                        if dE <= 0 or rng.random() < np.exp(-dE / T):
                            s[x, y] *= -1
                mags.append(float(np.mean(np.abs(s.mean()))))
            ax.plot(T_grid, mags, "o-", color=ACCENT)
            ax.axvline(2.0 / np.log(1 + np.sqrt(2)), color=ACCENT2, ls="--", label="2-D Ising $T_c$")
            ax.set_xlabel("T"); ax.set_ylabel("⟨|m|⟩"); ax.legend()
            ax.set_title("Test 38: vortex-flux lattice magnet")
        elif tid == 12:
            from .core import normalized_spacings, ab_spectrum, ABConfig
            sp_z = normalized_spacings(gammas)
            spec = ab_spectrum(cfg, L=12, Nv=0, W=0.0)
            sp_a = normalized_spacings(spec["eigs"])
            bins = np.linspace(0, 3.0, 40)
            ax.hist(sp_z, bins=bins, density=True, alpha=0.6, color=ACCENT, label="ζ")
            ax.hist(sp_a, bins=bins, density=True, alpha=0.6, color=ACCENT2, label="GUE matrix")
            ax.set_xlabel("s"); ax.set_ylabel("p(s)"); ax.legend()
            ax.set_title("Test 12: two-sample comparison")
        elif tid in (19, 30):
            from scipy.linalg import eigvalsh
            from .core import ab_lattice_hamiltonian
            Ls = [8, 10, 12, 14, 16] if cfg.fast else [12, 18, 24, 30]
            gaps = []
            for L in Ls:
                H, _ = ab_lattice_hamiltonian(L, 0.5, 0, 0, cfg.q)
                E = eigvalsh(H)
                gaps.append(np.min(np.abs(E - 0.5 * (E.min() + E.max()))))
            ax.plot(1.0 / np.asarray(Ls), gaps, "o-", color=ACCENT)
            ax.set_xlabel("1/L"); ax.set_ylabel("gap")
            ax.set_title(f"Test {tid}: Dirac gap vs 1/L")
        else:
            plotted = False
    except Exception as e:
        plotted = False
        print(f"[report] plot panel 1 for test {tid} skipped: {e}")
    finally:
        if plotted:
            fig.savefig(pdir / "plot_01.png")
        plt.close(fig)

    # panel 2: verdict map (always)
    fig, ax = plt.subplots(figsize=(8.0, 5.0), dpi=200, constrained_layout=True)
    names = [s[0] for s in res["sub_checks"]]
    vals = [1 if s[1] else 0 for s in res["sub_checks"]]
    colors = ["#3A7D44" if v else "#B0533A" for v in vals]
    ax.bar(range(len(names)), vals, color=colors, width=0.55)
    ax.set_xticks(range(len(names)))
    ax.set_xticklabels(names, rotation=45, ha="right", fontsize=8)
    ax.set_ylim(-0.1, 1.1)
    ax.set_ylabel("verdict (1 pass / 0 fail)")
    ax.set_title(f"Test {tid} — sub-check verdict map ({res['pass_label']})")
    _style(ax)
    fig.savefig(pdir / "plot_02.png")
    plt.close(fig)
    return pdir


def write_reports(suite: dict, out_dir: Path):
    """Write report.md per test + master final_report.md."""
    cfg_d = suite["config"]
    from .core import ABConfig

    cfg = ABConfig(**{k: v for k, v in cfg_d.items() if k in ABConfig.__dataclass_fields__})
    from .core import zeta_zeros, gram_points

    gammas = zeta_zeros(cfg.zeros)
    grams = gram_points(cfg.zeros)

    for entry in suite["results"]:
        slug = SLUGS.get(entry["number"], f"test_{entry['number']}")
        tdir = out_dir / f"test_{entry['number']:02d}_{slug}"
        tdir.mkdir(parents=True, exist_ok=True)
        res = entry["passes"][0]
        rel = res["verdict"] if len(entry["passes"]) == 1 else entry["overall"]
        lines = [
            f"# Test {entry['number']}: {entry['title']}",
            f"Verdict: {rel}   |   Generated: {suite['generated']}   |   "
            f"Suite: {suite['suite']} (Python clone)",
            "",
            "## What this test verifies",
            f"Clone reimplementation of Julia Test {entry['number']} — same statistic, "
            "same acceptance windows, same verdict algebra (see monograph Appendix D).",
            "",
            "## Result",
            f" Test {entry['number']} [{res['pass_label']}]: {len(res['sub_checks'])} sub-checks, "
            f"{len([s for s in res['sub_checks'] if not s[1]])} failed → {res['verdict']}",
            "",
            "## Plots",
            "- `plots/plot_01.png` — statistic panel",
            "- `plots/plot_02.png` — sub-check verdict map",
            "",
            "## CONSOLE CAPTURE",
            "",
            "```text",
            *res["lines"],
            "```",
            "",
        ]
        (tdir / "report.md").write_text("\n".join(lines), encoding="utf-8")
        make_plots(entry, cfg, gammas, grams, out_dir)

    # master report
    master = [
        "# FINAL REPORT — AB-Cloud v23 SUPERCOMBO — Python clone",
        f"Generated: {suite['generated']}   |   wall: {suite['wall_seconds']} s",
        "",
        f"Verdicts — {suite['totals']['entries']} entries: "
        f"{suite['totals']['pass']} PASS, {suite['totals']['fail']} FAIL",
        "",
    ]
    for entry in suite["results"]:
        for pp in entry["passes"]:
            master.append(f"Test {entry['number']:2d} [{pp['verdict']}] "
                          f"{entry['title']} — {pp['pass_label']}")
    master += ["", "## Run log", "", "```text", *suite["log"], "```", ""]
    (out_dir / "final_report.md").write_text("\n".join(master), encoding="utf-8")
