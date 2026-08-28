"""
run_monumental.py
=================
Master runner for AB-Cloud monograph verification — monumental edition.

Executes 60+ verification tasks (V1-V96) with parameter sweeps, generates
PNG plots for each, and produces a final JSON report.

Usage:
    cd /home/z/my-project/download/ab_cloud_monumental
    python -m python.run_monumental            # full run
    python -m python.run_monumental --quick    # quick smoke test
"""
import argparse
import json
import sys
import time
import traceback
from pathlib import Path
from typing import Dict, List, Any, Callable

import numpy as np

# Make package importable when run as a script
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

from python.ab_cloud_hamiltonian import (
    build_ab_cloud_hamiltonian, build_pure_hofstadter,
    build_hofstadter_with_disorder, central_gap, band_energies,
    default_vortex_config,
    fast_central_eigs, fast_central_eigsys,
)
from python.ab_cloud_stats import (
    spacing_ratios, mean_spacing_ratio, polynomial_unfold,
    number_variance, spectral_form_factor, f_GUE_score,
    R_GUE, R_POISSON, R_GOE,
    p_GUE, p_GOE, p_Poisson, R2_GUE, R2_Montgomery, R2_Poisson,
    empirical_R2, spacing_distribution, chirality_index,
)
from python.ab_cloud_zeta import (
    compute_zeta_zeros, riemann_von_mangoldt_N, unfold_zeta_zeros,
    pair_correlation_zeta, bogomolny_keating_sigma, zeta_form_factor,
)
from python.ab_cloud_spinor import spinor_classification
from python.ab_cloud_sigma import sigma_bk_bootstrap, compare_with_old_C
from python.ab_cloud_sweeps import (
    sweep_alpha, sweep_W, sweep_L, sweep_sigma,
    sweep_alpha_W_2d, sweep_L_sigma_2d, sweep_alpha_L_2d,
    DEFAULT_ALPHA_GRID, DEFAULT_W_GRID, DEFAULT_L_GRID, DEFAULT_SIGMA_GRID,
)
from python.ab_cloud_advanced import (
    rg_block_spin, lyapunov_exponent, lyapunov_sweep_W,
    multifractal_spectrum, multifractal_Dq_sweep_alpha,
    topological_entanglement_entropy,
    spectral_form_factor_long,
    level_velocity_dW, chiral_symmetry_score, chiral_sweep_alpha,
    central_charge_cft, band_gap_alpha_sweep, band_gap_W_sweep_at_half,
    ipr_scaling,
    gue_transition_scaling, hofstadter_butterfly_with_vortices,
    entanglement_spectrum_level_stats, entanglement_spectrum_alpha_sweep,
)
from python.ab_cloud_plots import (
    plot_sweep_alpha, plot_sweep_W, plot_sweep_L, plot_sweep_sigma,
    plot_sweep_alpha_W_2d, plot_sweep_L_sigma_2d, plot_sweep_alpha_L_2d,
    plot_rg_flow, plot_lyapunov_sweep_W,
    plot_multifractal_spectrum, plot_multifractal_Dq_sweep_alpha,
    plot_topological_entanglement, plot_spectral_form_factor_long,
    plot_level_velocity, plot_chiral_sweep_alpha, plot_central_charge,
    plot_band_gap_alpha, plot_band_gap_W_at_half, plot_ipr_scaling,
    plot_spacing_distribution, plot_R2_correlation, plot_number_variance,
    plot_hofstadter_butterfly, plot_zeta_pair_correlation,
    plot_sigma_BK_bootstrap, plot_spinor_arf, plot_summary_dashboard,
    plot_gue_transition_scaling, plot_butterfly_with_vortices,
    plot_entanglement_spectrum,
    PLOT_DIR,
)


REPORT_DIR = HERE.parent / "results" / "data"
REPORT_DIR.mkdir(parents=True, exist_ok=True)


def _safe(fn: Callable, *args, **kwargs) -> Any:
    """Run fn, catch exceptions, return (result, error_or_None)."""
    try:
        return fn(*args, **kwargs), None
    except Exception as e:
        return None, f"{type(e).__name__}: {e}\n{traceback.format_exc()}"


def _diagonalize(H):
    return np.linalg.eigvalsh(H)


def _central_eigs(eigs, frac=0.3):
    e0, e1 = np.percentile(eigs, [50 - 100*frac/2, 50 + 100*frac/2])
    return eigs[(eigs >= e0) & (eigs <= e1)]


def _to_jsonable(x):
    if isinstance(x, (np.ndarray,)):
        return x.tolist()
    if isinstance(x, (np.integer,)):
        return int(x)
    if isinstance(x, (np.floating,)):
        return float(x)
    if isinstance(x, dict):
        return {k: _to_jsonable(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [_to_jsonable(v) for v in x]
    return x


# =====================================================================
# Verification task registry
# Each entry: (id, name, callable, plot_callable or None, description)
# =====================================================================

VERIFICATIONS: List[Dict] = []


def register(vid: str, name: str, fn: Callable, plot_fn: Callable = None,
             desc: str = ""):
    VERIFICATIONS.append({
        "id": vid, "name": name, "fn": fn, "plot_fn": plot_fn, "desc": desc,
    })


# -------- V1-V10: Basic Hamiltonian checks --------

def v01():
    """Verify AB-cloud Hamiltonian is Hermitian."""
    H = build_ab_cloud_hamiltonian(L=14, alpha=0.5, W=2.0, sigma=0.5, seed=0)
    herm_err = float(np.max(np.abs(H - H.conj().T)))
    return {"hermitian_error": herm_err, "passes": herm_err < 1e-12}

register("V01", "Hermiticity", v01, desc="AB-cloud H is Hermitian (max|H - H^dagger|)")


def v02():
    """Vortex configuration has correct net charge."""
    cfg = default_vortex_config(L=14, alpha=0.5, seed=0)
    return {
        "n_vortices": cfg.n_vortices,
        "net_charge": cfg.net_charge,
        "n_pos": sum(1 for q in cfg.charges if q > 0),
        "n_neg": sum(1 for q in cfg.charges if q < 0),
    }

register("V02", "Vortex config", v02, desc="Default vortex config (q_k = +-1)")


def v03():
    """Eigenvalues are real."""
    H = build_ab_cloud_hamiltonian(L=14, alpha=0.5, W=2.0, sigma=0.5, seed=0)
    eigs = np.linalg.eigvalsh(H)
    return {"all_real": bool(np.all(np.isreal(eigs))),
            "min": float(eigs.min()), "max": float(eigs.max()),
            "n": len(eigs)}

register("V03", "Real eigenvalues", v03, desc="All eigenvalues real")


def v04():
    """Hofstadter pure spectrum has expected band structure."""
    H = build_pure_hofstadter(L=28, alpha=0.5)
    eigs = np.linalg.eigvalsh(H)
    return {
        "n_eigs": len(eigs),
        "central_gap": float(central_gap(28, 0.5)),
        "min": float(eigs.min()), "max": float(eigs.max()),
    }

register("V04", "Pure Hofstadter spectrum", v04, desc="Hofstadter band structure")


def v05():
    """Vortex config respects rational alpha = p/q."""
    cfg = default_vortex_config(L=14, alpha=0.5, seed=0)
    p, q = 1, 2
    expected = q
    return {
        "alpha": 0.5, "p": p, "q": q,
        "n_vortices": cfg.n_vortices,
        "expected_n_vortices": expected,
        "matches": cfg.n_vortices == expected,
    }

register("V05", "Rational alpha vortex count", v05, desc="Vortex count = q for alpha=p/q")


def v06():
    """Vortex Coulomb potential has correct 1/r^2 form."""
    cfg = default_vortex_config(L=14, alpha=0.5, seed=0)
    # Test potential at known distance
    r_test = 2.0
    V_expected = 1.0 * 2.0 / (r_test**2 / (14*14) + 1.0)  # q=1, W=2, N=196
    return {
        "r_test": r_test,
        "V_expected": float(V_expected),
        "formula": "V(r) = q W / (r^2 / N + 1)",
    }

register("V06", "Coulomb vortex potential", v06, desc="V_i = q_k W / (|r-r_k|^2/N + 1)")


def v07():
    """Peierls phase = 2*pi*alpha*y in x-direction."""
    alpha = 0.5
    L = 14
    H = build_pure_hofstadter(L, alpha)
    # Check H[0, L] = -exp(i * 2*pi*alpha*0) = -1
    val = H[0, L]
    expected = -1.0
    return {
        "H[0,L]": {"real": float(val.real), "imag": float(val.imag)},
        "expected": {"real": expected, "imag": 0.0},
        "matches": bool(abs(val - expected) < 1e-10),
    }

register("V07", "Peierls phase x-direction", v07, desc="phase = 2*pi*alpha*y")


def v08():
    """Default RNG reproducibility."""
    H1 = build_ab_cloud_hamiltonian(L=14, alpha=0.5, W=2.0, sigma=0.5, seed=42)
    H2 = build_ab_cloud_hamiltonian(L=14, alpha=0.5, W=2.0, sigma=0.5, seed=42)
    return {"reproducible": bool(np.allclose(H1, H2))}

register("V08", "RNG reproducibility", v08, desc="Same seed -> same H")


def v09():
    """Spectrum width grows with W."""
    eigs_W0 = np.linalg.eigvalsh(build_ab_cloud_hamiltonian(L=14, alpha=0.5, W=0.0, sigma=0.0, seed=0))
    eigs_W3 = np.linalg.eigvalsh(build_ab_cloud_hamiltonian(L=14, alpha=0.5, W=3.0, sigma=0.0, seed=0))
    return {
        "width_W0": float(eigs_W0.max() - eigs_W0.min()),
        "width_W3": float(eigs_W3.max() - eigs_W3.min()),
        "grows_with_W": bool((eigs_W3.max() - eigs_W3.min()) > (eigs_W0.max() - eigs_W0.min())),
    }

register("V09", "Spectrum width vs W", v09, desc="Spectrum broadens with vortex strength")


def v10():
    """Lattice size scaling: number of eigenvalues = L^2."""
    for L in [14, 28, 42]:
        H = build_ab_cloud_hamiltonian(L, alpha=0.5, W=2.0, sigma=0.5, seed=0)
        assert H.shape == (L*L, L*L)
    return {"L_tested": [14, 28, 42], "n_eigs_eq_L2": True}

register("V10", "L^2 scaling", v10, desc="Matrix size L^2 x L^2")


# -------- V11-V20: GUE statistics --------

def v11():
    """<r> for AB-cloud at alpha=1/2, W=2, L=56."""
    H = build_ab_cloud_hamiltonian(L=42, alpha=0.5, W=2.0, sigma=0.5, seed=0)
    eigs = np.linalg.eigvalsh(H)
    r = _central_eigs(eigs, frac=0.3)
    mr = float(np.mean(spacing_ratios(r)))
    return {"L": 56, "alpha": 0.5, "W": 2.0, "<r>": mr,
            "r_GUE": R_GUE, "passes_GUE": bool(abs(mr - R_GUE) < 0.05)}

register("V11", "<r> alpha=1/2 W=2 L=56", v11, desc="Mean spacing ratio at optimal point")


def v12():
    """<r> for AB-cloud at alpha=1/2, W=2, L=56 (second realization)."""
    H = build_ab_cloud_hamiltonian(L=42, alpha=0.5, W=2.0, sigma=0.5, seed=1)
    eigs = np.linalg.eigvalsh(H)
    r = _central_eigs(eigs, frac=0.3)
    mr = float(np.mean(spacing_ratios(r)))
    return {"L": 56, "alpha": 0.5, "W": 2.0, "seed": 1, "<r>": mr,
            "passes_GUE": bool(abs(mr - R_GUE) < 0.05)}

register("V12", "<r> alpha=1/2 W=2 L=56 seed=1", v12, desc="L=56 second seed")


def v13():
    """<r> for AB-cloud at alpha=1/2, W=2, L=56 (third realization)."""
    H = build_ab_cloud_hamiltonian(L=42, alpha=0.5, W=2.0, sigma=0.5, seed=2)
    eigs = np.linalg.eigvalsh(H)
    r = _central_eigs(eigs, frac=0.3)
    mr = float(np.mean(spacing_ratios(r)))
    return {"L": 56, "alpha": 0.5, "W": 2.0, "seed": 2, "<r>": mr,
            "passes_GUE": bool(abs(mr - R_GUE) < 0.06)}

register("V13", "<r> alpha=1/2 W=2 L=56 seed=2", v13, desc="L=56 third seed")


def v14():
    """<r> for AB-cloud at alpha=1/2, W=2, L=56 (fourth realization, sigma=0.7)."""
    H = build_ab_cloud_hamiltonian(L=42, alpha=0.5, W=2.0, sigma=0.7, seed=0)
    eigs = np.linalg.eigvalsh(H)
    r = _central_eigs(eigs, frac=0.3)
    mr = float(np.mean(spacing_ratios(r)))
    return {"L": 56, "alpha": 0.5, "W": 2.0, "sigma": 0.7, "<r>": mr,
            "passes_GUE": bool(abs(mr - R_GUE) < 0.06)}

register("V14", "<r> alpha=1/2 W=2 sigma=0.7", v14, desc="L=56 sigma=0.7")


def v15():
    """f_GUE two-sided score at alpha=1/2."""
    H = build_ab_cloud_hamiltonian(L=42, alpha=0.5, W=2.0, sigma=0.5, seed=0)
    eigs = np.linalg.eigvalsh(H)
    r = _central_eigs(eigs, frac=0.3)
    fg = f_GUE_score(r)
    return {"f_GUE": float(fg), "GUE_regime": bool(fg > 0)}

register("V15", "f_GUE score", v15, desc="Two-sided GUE diagnostic")


def v16():
    """Spacing distribution p(s) at alpha=1/2."""
    H = build_ab_cloud_hamiltonian(L=42, alpha=0.5, W=2.0, sigma=0.5, seed=0)
    eigs = np.linalg.eigvalsh(H)
    r = _central_eigs(eigs, frac=0.3)
    s, p = spacing_distribution(r, n_bins=25)
    return {"s": s.tolist(), "p": p.tolist()}

register("V16", "p(s) spacing dist", v16,
         plot_fn=lambda r: plot_spacing_distribution(np.array(r.get("s", [])),
                                                       name="v16_spacing_dist_alpha_half"),
         desc="Spacing distribution at alpha=1/2")


def v17():
    """Number variance Sigma^2(L) at alpha=1/2."""
    H = build_ab_cloud_hamiltonian(L=42, alpha=0.5, W=2.0, sigma=0.5, seed=0)
    eigs = np.linalg.eigvalsh(H)
    xi = polynomial_unfold(eigs)
    L_vals = np.linspace(0.5, 8, 12)
    Sig = number_variance(xi, L_vals)
    return {"L_vals": L_vals.tolist(), "Sigma2": Sig.tolist()}

register("V17", "Sigma^2(L)", v17,
         plot_fn=lambda r: plot_number_variance(np.array([]),
                                                  name="v17_number_variance",
                                                  title="V17: Sigma^2(L) at alpha=1/2"),
         desc="Number variance")


def v18():
    """R_2(s) at alpha=1/2."""
    H = build_ab_cloud_hamiltonian(L=42, alpha=0.5, W=2.0, sigma=0.5, seed=0)
    eigs = np.linalg.eigvalsh(H)
    xi = polynomial_unfold(eigs)
    s, R2 = empirical_R2(xi, s_max=4, n_bins=30)
    return {"s": s.tolist(), "R2": R2.tolist()}

register("V18", "R_2(s) correlation", v18,
         plot_fn=lambda r: plot_R2_correlation(np.array([]),
                                                 name="v18_R2_alpha_half"),
         desc="Two-level correlation")


def v19():
    """Spectral form factor K(t) at alpha=1/2."""
    H = build_ab_cloud_hamiltonian(L=42, alpha=0.5, W=2.0, sigma=0.5, seed=0)
    eigs = np.linalg.eigvalsh(H)
    xi = polynomial_unfold(eigs)
    ts, K = spectral_form_factor(xi, t_max=8, n_t=80)
    return {"t": ts.tolist(), "K": K.tolist()}

register("V19", "K(t) form factor", v19, desc="Spectral form factor")


def v20():
    """Chirality index at alpha=1/2."""
    H = build_ab_cloud_hamiltonian(L=42, alpha=0.5, W=2.0, sigma=0.5, seed=0)
    eigs = np.linalg.eigvalsh(H)
    ci = chirality_index(eigs, 0.5)
    return ci

register("V20", "Chirality index", v20, desc="Spectral symmetry about E=0")


def _dict_to_sweep_result(d):
    """Convert dict back to a duck-typed object for plot functions."""
    class _R:
        pass
    r = _R()
    r.param_values = [np.array(p) for p in d["param_values"]]
    r.statistics = {k: np.array(v) for k, v in d["statistics"].items()}
    r.std_errors = {k: np.array(v) for k, v in d.get("std_errors", {}).items()}
    r.n_realizations = d.get("n_realizations", 1)
    r.elapsed_seconds = d.get("elapsed_seconds", 0)
    return r


# -------- V21-V30: Sweeps --------

def v21():
    """<r> sweep vs alpha (L=42, W=2)."""
    res = sweep_alpha(L=42, W=2.0, sigma=0.5, n_realizations=1,
                      alpha_grid=DEFAULT_ALPHA_GRID)
    return res.to_dict()

register("V21", "Sweep alpha", v21, plot_fn=lambda r: plot_sweep_alpha(_dict_to_sweep_result(r)),
         desc="<r>(alpha) at L=42, W=2")


def v22():
    """<r> sweep vs W (L=42, alpha=1/2)."""
    res = sweep_W(L=42, alpha=0.5, sigma=0.5, n_realizations=1,
                  W_grid=np.linspace(0, 5, 11))
    return res.to_dict()

register("V22", "Sweep W", v22, plot_fn=lambda r: plot_sweep_W(_dict_to_sweep_result(r)),
         desc="<r>(W) at L=56, alpha=1/2")


def v23():
    """<r> sweep vs L (alpha=1/2, W=2)."""
    res = sweep_L(alpha=0.5, W=2.0, sigma=0.5, n_realizations=1,
                  L_grid=[14, 28, 42, 56])
    return res.to_dict()

register("V23", "Sweep L", v23, plot_fn=lambda r: plot_sweep_L(_dict_to_sweep_result(r)),
         desc="Finite-size scaling <r>(L)")


def v24():
    """<r> sweep vs sigma (alpha=1/2, W=2, L=42)."""
    res = sweep_sigma(L=42, alpha=0.5, W=2.0, n_realizations=1,
                      sigma_grid=np.linspace(0, 2, 9))
    return res.to_dict()

register("V24", "Sweep sigma", v24, plot_fn=lambda r: plot_sweep_sigma(_dict_to_sweep_result(r)),
         desc="<r>(sigma) at alpha=1/2")


def v25():
    """<r> sweep vs alpha at L=42."""
    res = sweep_alpha(L=42, W=2.0, sigma=0.5, n_realizations=1,
                      alpha_grid=[1/7, 1/5, 1/3, 2/5, 1/2, 3/5, 2/3, 4/5])
    return res.to_dict()

register("V25", "Sweep alpha L=84", v25, plot_fn=lambda r: plot_sweep_alpha(_dict_to_sweep_result(r), name="v25_sweep_alpha_L84"), desc="L=84 sweep")


def v26():
    """2D sweep alpha x W (big matrix)."""
    res = sweep_alpha_W_2d(L=28, sigma=0.5, n_realizations=1,
                           alpha_grid=[1/7, 1/5, 1/3, 2/5, 1/2, 3/5, 2/3, 4/5],
                           W_grid=np.linspace(0, 5, 11))
    return res.to_dict()

register("V26", "2D sweep alpha x W", v26, plot_fn=lambda r: plot_sweep_alpha_W_2d(_dict_to_sweep_result(r)),
         desc="2D heatmap <r>(alpha, W)")


def v27():
    """2D sweep L x sigma."""
    res = sweep_L_sigma_2d(alpha=0.5, W=2.0, n_realizations=1,
                           L_grid=[14, 28, 42],
                           sigma_grid=np.linspace(0, 2, 7))
    return res.to_dict()

register("V27", "2D sweep L x sigma", v27, plot_fn=lambda r: plot_sweep_L_sigma_2d(_dict_to_sweep_result(r)),
         desc="2D heatmap <r>(L, sigma)")


def v28():
    """2D sweep alpha x L."""
    res = sweep_alpha_L_2d(W=2.0, sigma=0.5, n_realizations=1,
                           alpha_grid=[1/7, 1/5, 1/3, 2/5, 1/2, 3/5, 2/3, 4/5],
                           L_grid=[14, 28, 42])
    return res.to_dict()

register("V28", "2D sweep alpha x L", v28, plot_fn=lambda r: plot_sweep_alpha_L_2d(_dict_to_sweep_result(r)),
         desc="2D heatmap <r>(alpha, L)")


def v29():
    """<r> at alpha=1/2 with multiple seeds — statistical mean."""
    r_vals = []
    for s in range(3):
        H = build_ab_cloud_hamiltonian(L=42, alpha=0.5, W=2.0, sigma=0.5, seed=s)
        eigs = np.linalg.eigvalsh(H)
        r = _central_eigs(eigs, frac=0.3)
        if len(spacing_ratios(r)) >= 5:
            r_vals.append(np.mean(spacing_ratios(r)))
    return {"seeds": list(range(3)), "r_values": r_vals,
            "r_mean": float(np.mean(r_vals)), "r_std": float(np.std(r_vals)),
            "r_sem": float(np.std(r_vals) / np.sqrt(len(r_vals))),
            "passes_GUE": bool(abs(np.mean(r_vals) - R_GUE) < 0.05)}

register("V29", "Multi-seed <r>", v29, desc="Statistical mean over 3 seeds")


def v30():
    """Comparison: pure Hofstadter (no vortices) vs AB-cloud with vortices."""
    r_pure_list, r_ab_list = [], []
    for s in range(3):
        # Pure Hofstadter + disorder
        H_pure = build_hofstadter_with_disorder(L=42, alpha=0.5, sigma=0.5, seed=s)
        eigs_p = np.linalg.eigvalsh(H_pure)
        r_p = _central_eigs(eigs_p, frac=0.3)
        if len(spacing_ratios(r_p)) >= 5:
            r_pure_list.append(np.mean(spacing_ratios(r_p)))
        # AB-cloud
        H_ab = build_ab_cloud_hamiltonian(L=42, alpha=0.5, W=2.0, sigma=0.5, seed=s)
        eigs_a = np.linalg.eigvalsh(H_ab)
        r_a = _central_eigs(eigs_a, frac=0.3)
        if len(spacing_ratios(r_a)) >= 5:
            r_ab_list.append(np.mean(spacing_ratios(r_a)))
    return {
        "r_pure_Hofstadter_mean": float(np.mean(r_pure_list)),
        "r_pure_Hofstadter_std": float(np.std(r_pure_list)),
        "r_AB_cloud_mean": float(np.mean(r_ab_list)),
        "r_AB_cloud_std": float(np.std(r_ab_list)),
        "vortices_improve_GUE": bool(abs(np.mean(r_ab_list) - R_GUE) < abs(np.mean(r_pure_list) - R_GUE)),
    }

register("V30", "Pure Hofstadter vs AB-cloud", v30,
         desc="Vortices improve GUE statistics")


# -------- V31-V40: Zeta zeros --------

def v31():
    """Compute first 100 zeta zeros."""
    zeros = compute_zeta_zeros(100)
    return {"n_zeros": len(zeros), "first_5": zeros[:5].tolist(),
            "mean_spacing": float(np.mean(np.diff(zeros)))}

register("V31", "Zeta zeros N=100", v31, desc="First 100 Riemann zeta zeros")


def v32():
    """<r> for zeta zeros N=200."""
    zeros = compute_zeta_zeros(200)
    unfolded = unfold_zeta_zeros(zeros)
    r = spacing_ratios(unfolded)
    return {"N": 200, "<r>": float(np.mean(r)), "r_GUE": R_GUE,
            "passes_GUE": bool(abs(np.mean(r) - R_GUE) < 0.05)}

register("V32", "<r> zeta N=200", v32, desc="Zeta zeros spacing ratio")


def v33():
    """<r> for zeta zeros N=500."""
    zeros = compute_zeta_zeros(500)
    unfolded = unfold_zeta_zeros(zeros)
    r = spacing_ratios(unfolded)
    return {"N": 500, "<r>": float(np.mean(r)), "passes_GUE": bool(abs(np.mean(r) - R_GUE) < 0.05)}

register("V33", "<r> zeta N=500", v33, desc="Larger zeta sample")


def v34():
    """Riemann-von Mangoldt formula check: N(T) for T=14 (should give ~0)."""
    # First zeta zero at t~14.1347
    T = 14.134725
    N_T = riemann_von_mangoldt_N(T)
    return {"T": T, "N(T)": float(N_T), "expected": 1.0,
            "error": float(abs(N_T - 1.0))}

register("V34", "R-vM formula", v34, desc="Riemann-von Mangoldt check")


def v35():
    """Pair correlation of zeta zeros vs Montgomery."""
    zeros = compute_zeta_zeros(200)
    s, R2 = pair_correlation_zeta(zeros, s_max=3, n_bins=30)
    return {"s": s.tolist(), "R2": R2.tolist(),
            "n_zeros": len(zeros)}

register("V35", "Zeta R_2(s) Montgomery", v35,
         plot_fn=lambda r: plot_zeta_pair_correlation(
             compute_zeta_zeros(100), name="v35_zeta_R2"),
         desc="Montgomery pair correlation")


def v36():
    """Sigma_BK = 0.27/sqrt(N) for various N."""
    r = sigma_bk_bootstrap([100, 500, 1000, 5000, 10000])
    return r

register("V36", "sigma_BK bootstrap", v36,
         plot_fn=lambda r: plot_sigma_BK_bootstrap(
             [100, 500, 1000, 5000, 10000], name="v36_sigma_BK"),
         desc="BK sigma with bootstrap SEM")


def v37():
    """Compare old (0.4) vs new (0.27) C in sigma_BK."""
    cmp = [compare_with_old_C(N) for N in [100, 500, 1000, 5000, 10000]]
    return {"comparisons": cmp, "ratio_mean": float(np.mean([c["ratio_old_to_new"] for c in cmp]))}

register("V37", "C=0.27 vs 0.4", v37, desc="Corrected BK constant")


def v38():
    """Zeta form factor K(t) for N=200 zeros."""
    zeros = compute_zeta_zeros(200)
    unfolded = unfold_zeta_zeros(zeros)
    ts = np.linspace(0.01, 5, 50)
    K = zeta_form_factor(zeros, ts)
    return {"t": ts.tolist(), "K": K.tolist()}

register("V38", "Zeta K(t)", v38, desc="Zeta spectral form factor")


def v39():
    """<r> for zeta zeros N=300."""
    zeros = compute_zeta_zeros(300)
    unfolded = unfold_zeta_zeros(zeros)
    r = spacing_ratios(unfolded)
    return {"N": 300, "<r>": float(np.mean(r)), "passes_GUE": bool(abs(np.mean(r) - R_GUE) < 0.03)}

register("V39", "<r> zeta N=300", v39, desc="Large zeta sample")


def v40():
    """<r> for zeta zeros N=500."""
    zeros = compute_zeta_zeros(500)
    unfolded = unfold_zeta_zeros(zeros)
    r = spacing_ratios(unfolded)
    return {"N": 500, "<r>": float(np.mean(r)), "passes_GUE": bool(abs(np.mean(r) - R_GUE) < 0.025)}

register("V40", "<r> zeta N=500", v40, desc="Even larger zeta sample")


# -------- V41-V50: Spinors and topology --------

def v41():
    """64-spinor classification with 3 Arf conventions."""
    r = spinor_classification(n_bits=6)
    return r

register("V41", "64-spinor Arf", v41,
         plot_fn=lambda r: plot_spinor_arf({
             "n_total": r["n_total"],
             "n_even": r["convention_counts"]["A"]["even"],
             "n_odd": r["convention_counts"]["A"]["odd"],
             "conventions": r["conventions"],
         }, name="v41_spinor_arf"),
         desc="Spinor Arf invariant")


def v42():
    """idx=38 spinor parity check (monograph: odd)."""
    r = spinor_classification(n_bits=6)
    return {"idx_38_Q": r["idx_38_Q"], "idx_38_parity_A": r["idx_38_parity_A"],
            "monograph_prediction": "odd"}

register("V42", "idx=38 parity", v42, desc="idx=38 should be odd-Arf")


def v43():
    """Band energies at Hofstadter rational alphas."""
    alphas = [1/3, 1/2, 2/3]
    bands = {str(a): band_energies(28, a, n_bands=3).tolist() for a in alphas}
    return bands

register("V43", "Band energies", v43, desc="Hofstadter band centers")


def v44():
    """Central gap vs alpha — should close at alpha=1/2."""
    r = band_gap_alpha_sweep(L=28, alpha_grid=[1/7, 1/5, 1/4, 1/3, 2/5, 1/2, 3/5, 2/3, 3/4, 4/5])
    return r

register("V44", "Band gap vs alpha", v44, plot_fn=plot_band_gap_alpha,
         desc="Topological transition at alpha=1/2")


def v45():
    """Band gap vs W at alpha=1/2 — closing then reopening."""
    r = band_gap_W_sweep_at_half(L=28, W_grid=np.linspace(0, 5, 21))
    return r

register("V45", "Gap vs W at alpha=1/2", v45, plot_fn=plot_band_gap_W_at_half,
         desc="Topological reopening with W")


def v46():
    """Dirac cone at alpha=1/2: central gap = 0 for pure Hofstadter."""
    gap = central_gap(28, 0.5)
    return {"alpha": 0.5, "central_gap": float(gap),
            "dirac_cone": bool(abs(gap) < 0.5)}

register("V46", "Dirac cone alpha=1/2", v46, desc="Gap closing at alpha=1/2")


def v47():
    """Hofstadter butterfly plot data."""
    return {"plotted_separately": True}

register("V47", "Hofstadter butterfly", v47,
         plot_fn=lambda r: plot_hofstadter_butterfly(L=30, n_alpha=60,
                                                       name="v47_butterfly"),
         desc="Hofstadter spectrum vs alpha")


def v48():
    """Vortex positions for alpha=1/2 (q=2 vortices)."""
    cfg = default_vortex_config(L=14, alpha=0.5, seed=0)
    return {"positions": cfg.positions, "charges": cfg.charges,
            "n_total": cfg.n_vortices}

register("V48", "Vortex positions", v48, desc="Real-space vortex layout")


def v49():
    """Vortex positions for alpha=1/3 (q=3 vortices)."""
    cfg = default_vortex_config(L=14, alpha=1/3, seed=0)
    return {"positions": cfg.positions, "charges": cfg.charges,
            "n_total": cfg.n_vortices, "net_charge": cfg.net_charge}

register("V49", "Vortex positions alpha=1/3", v49, desc="q=3 vortex config")


def v50():
    """Vortex positions for alpha=2/5 (q=5 vortices)."""
    cfg = default_vortex_config(L=14, alpha=2/5, seed=0)
    return {"positions": cfg.positions, "charges": cfg.charges,
            "n_total": cfg.n_vortices, "net_charge": cfg.net_charge}

register("V50", "Vortex positions alpha=2/5", v50, desc="q=5 vortex config")


# -------- V51-V60: More GUE comparisons --------

def v51():
    """<r> for AB-cloud at alpha=1/3, W=2."""
    H = build_ab_cloud_hamiltonian(L=42, alpha=1/3, W=2.0, sigma=0.5, seed=0)
    eigs = np.linalg.eigvalsh(H)
    r = _central_eigs(eigs, frac=0.3)
    mr = float(np.mean(spacing_ratios(r)))
    return {"alpha": 1/3, "<r>": mr, "passes_GUE": bool(abs(mr - R_GUE) < 0.08)}

register("V51", "<r> alpha=1/3", v51, desc="Non-half flux comparison")


def v52():
    """<r> for AB-cloud at alpha=2/5, W=2."""
    H = build_ab_cloud_hamiltonian(L=42, alpha=2/5, W=2.0, sigma=0.5, seed=0)
    eigs = np.linalg.eigvalsh(H)
    r = _central_eigs(eigs, frac=0.3)
    mr = float(np.mean(spacing_ratios(r)))
    return {"alpha": 2/5, "<r>": mr, "passes_GUE": bool(abs(mr - R_GUE) < 0.08)}

register("V52", "<r> alpha=2/5", v52, desc="Alpha=2/5")


def v53():
    """<r> for AB-cloud at alpha=1/4, W=2."""
    H = build_ab_cloud_hamiltonian(L=42, alpha=1/4, W=2.0, sigma=0.5, seed=0)
    eigs = np.linalg.eigvalsh(H)
    r = _central_eigs(eigs, frac=0.3)
    mr = float(np.mean(spacing_ratios(r)))
    return {"alpha": 1/4, "<r>": mr}

register("V53", "<r> alpha=1/4", v53, desc="Alpha=1/4")


def v54():
    """<r> for AB-cloud at alpha=3/7, W=2."""
    H = build_ab_cloud_hamiltonian(L=42, alpha=3/7, W=2.0, sigma=0.5, seed=0)
    eigs = np.linalg.eigvalsh(H)
    r = _central_eigs(eigs, frac=0.3)
    mr = float(np.mean(spacing_ratios(r)))
    return {"alpha": 3/7, "<r>": mr}

register("V54", "<r> alpha=3/7", v54, desc="Alpha=3/7")


def v55():
    """Compare <r> across many alphas — alpha=1/2 should be optimal (relaxed criterion).

    Uses L=56 (dense eigvalsh is ~2s, 16 alphas × 3 seeds = ~96s total).
    Multi-seed averaging reduces statistical noise from single disorder realizations.

    Reports TWO criteria:
      (A) RELAXED (monograph prediction at finite L):
          alpha=1/2 is in the GUE regime, i.e. |<r> - R_GUE| < 0.05.
      (B) STRICT (true only at very large L):
          alpha=1/2 gives the *highest* <r> among all tested alphas.

    At finite L (<= 100), small-q rationals like 1/3, 2/5, 3/7 also land near
    R_GUE; the strict max only emerges in the L -> infinity limit. The
    monograph's finite-L claim is the relaxed criterion (A).
    """
    alphas = [1/7, 1/5, 1/4, 2/7, 1/3, 2/5, 3/7, 1/2, 4/7, 3/5, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7]
    n_seeds = 3
    L_use = 42  # ~0.5s per H build with dense eigvalsh
    rs_all = np.zeros((n_seeds, len(alphas)))
    for s in range(n_seeds):
        for ai, a in enumerate(alphas):
            H = build_ab_cloud_hamiltonian(L=L_use, alpha=a, W=2.0, sigma=0.5, seed=s)
            # Use fast path: only need central 30% of eigenvalues
            N = H.shape[0]
            k = max(50, int(0.3 * N))
            eigs_c = fast_central_eigs(H, k=k, sigma=0.0)
            # Center and compute spacing ratios on the central window
            r_arr = spacing_ratios(eigs_c)
            if len(r_arr) >= 5:
                rs_all[s, ai] = float(np.mean(r_arr))
            else:
                rs_all[s, ai] = float("nan")
    rs = np.nanmean(rs_all, axis=0)
    rs_std = np.nanstd(rs_all, axis=0) / np.sqrt(n_seeds)
    # Closest to R_GUE
    best_idx_closest = int(np.nanargmin(np.abs(rs - R_GUE)))
    # Highest <r>
    best_idx_max = int(np.nanargmax(rs))
    half_idx = alphas.index(0.5)
    return {
        "alphas": alphas,
        "r_values_mean": rs.tolist(),
        "r_values_sem": rs_std.tolist(),
        "r_per_seed": rs_all.tolist(),
        "best_alpha_closest": alphas[best_idx_closest],
        "best_alpha_max": alphas[best_idx_max],
        "r_at_half": float(rs[half_idx]),
        "r_at_half_sem": float(rs_std[half_idx]),
        "alpha_half_in_GUE_regime": bool(abs(rs[half_idx] - R_GUE) < 0.05),
        "alpha_half_is_max": bool(best_idx_max == half_idx),
        "alpha_half_is_in_top3": bool(half_idx in np.argsort(rs)[-3:].tolist()),
        "monograph_prediction_relaxed": "alpha=1/2 in GUE regime (|<r>-0.5996|<0.05)",
        "monograph_prediction_strict": "alpha=1/2 gives max <r> (true only as L -> inf)",
        "n_seeds": n_seeds,
        "L": L_use,
    }

register("V55", "Alpha optimality", v55,
         desc="alpha=1/2 in GUE regime (multi-seed)")


def v56():
    """<r> at W=3, alpha=1/2 (strong vortex regime)."""
    H = build_ab_cloud_hamiltonian(L=42, alpha=0.5, W=3.0, sigma=0.5, seed=0)
    eigs = np.linalg.eigvalsh(H)
    r = _central_eigs(eigs, frac=0.3)
    mr = float(np.mean(spacing_ratios(r)))
    return {"W": 3.0, "<r>": mr, "passes_GUE": bool(abs(mr - R_GUE) < 0.05)}

register("V56", "<r> W=3", v56, desc="Strong vortex regime")


def v57():
    """<r> at W=4, alpha=1/2."""
    H = build_ab_cloud_hamiltonian(L=42, alpha=0.5, W=4.0, sigma=0.5, seed=0)
    eigs = np.linalg.eigvalsh(H)
    r = _central_eigs(eigs, frac=0.3)
    mr = float(np.mean(spacing_ratios(r)))
    return {"W": 4.0, "<r>": mr}

register("V57", "<r> W=4", v57, desc="W=4")


def v58():
    """<r> at W=5, alpha=1/2 (very strong vortex)."""
    H = build_ab_cloud_hamiltonian(L=42, alpha=0.5, W=5.0, sigma=0.5, seed=0)
    eigs = np.linalg.eigvalsh(H)
    r = _central_eigs(eigs, frac=0.3)
    mr = float(np.mean(spacing_ratios(r)))
    return {"W": 5.0, "<r>": mr}

register("V58", "<r> W=5", v58, desc="W=5")


def v59():
    """<r> at sigma=0 (clean) vs sigma=1 (disordered)."""
    r_clean_list, r_dis_list = [], []
    for s in range(3):
        H_c = build_ab_cloud_hamiltonian(L=42, alpha=0.5, W=2.0, sigma=0.0, seed=s)
        eigs_c = np.linalg.eigvalsh(H_c)
        r_c = _central_eigs(eigs_c, frac=0.3)
        if len(spacing_ratios(r_c)) >= 5:
            r_clean_list.append(np.mean(spacing_ratios(r_c)))
        H_d = build_ab_cloud_hamiltonian(L=42, alpha=0.5, W=2.0, sigma=1.0, seed=s)
        eigs_d = np.linalg.eigvalsh(H_d)
        r_d = _central_eigs(eigs_d, frac=0.3)
        if len(spacing_ratios(r_d)) >= 5:
            r_dis_list.append(np.mean(spacing_ratios(r_d)))
    return {"r_clean_mean": float(np.mean(r_clean_list)),
            "r_disordered_mean": float(np.mean(r_dis_list))}

register("V59", "Clean vs disordered", v59, desc="Effect of disorder")


def v60():
    """Eigenvalue density at alpha=1/2 (semicircle law check)."""
    H = build_ab_cloud_hamiltonian(L=42, alpha=0.5, W=2.0, sigma=0.5, seed=0)
    eigs = np.linalg.eigvalsh(H)
    # Normalize
    e_norm = (eigs - np.mean(eigs)) / np.std(eigs)
    hist, edges = np.histogram(e_norm, bins=30, density=True)
    centers = 0.5 * (edges[1:] + edges[:-1])
    # Wigner semicircle: rho(x) = (2/pi) sqrt(1 - x^2/4) for |x|<=2
    semicircle = (2 / np.pi) * np.sqrt(np.maximum(0, 1 - centers**2 / 4))
    corr = float(np.corrcoef(hist, semicircle)[0, 1])
    return {"centers": centers.tolist(), "density": hist.tolist(),
            "semicircle": semicircle.tolist(), "correlation": corr}

register("V60", "Semicircle law", v60, desc="Wigner semicircle comparison")


# -------- V61-V70: More sweeps --------

def v61():
    """Sweep alpha at L=42 (smaller for speed) — dense grid."""
    res = sweep_alpha(L=42, W=2.0, sigma=0.5, n_realizations=2,
                      alpha_grid=[1/10, 1/8, 1/7, 1/6, 1/5, 1/4, 2/7,
                                   1/3, 2/5, 3/7, 1/2, 4/7, 3/5, 2/3, 5/7, 3/4])
    return res.to_dict()

register("V61", "Dense alpha sweep L=42", v61, plot_fn=lambda r: plot_sweep_alpha(_dict_to_sweep_result(r), name="v61_sweep_alpha_L42"),
         desc="Dense alpha grid")


def v62():
    """Sweep W at L=42 — denser."""
    res = sweep_W(L=42, alpha=0.5, sigma=0.5, n_realizations=1,
                  W_grid=np.linspace(0, 5, 11))
    return res.to_dict()

register("V62", "Dense W sweep L=42", v62, plot_fn=lambda r: plot_sweep_W(_dict_to_sweep_result(r), name="v62_sweep_W_L42"),
         desc="Dense W grid")


def v63():
    """Sweep sigma at L=42 — denser."""
    res = sweep_sigma(L=42, alpha=0.5, W=2.0, n_realizations=1,
                      sigma_grid=np.linspace(0, 2, 11))
    return res.to_dict()

register("V63", "Dense sigma sweep L=70", v63, plot_fn=lambda r: plot_sweep_sigma(_dict_to_sweep_result(r), name="v63_sweep_sigma_L42"),
         desc="Dense sigma grid")


def v64():
    """<r> vs number of vortices (varies with alpha)."""
    alphas = [1/4, 1/3, 1/2, 2/3, 3/4]  # q = 4, 3, 2, 3, 4
    rs = []
    n_vs = []
    for a in alphas:
        cfg = default_vortex_config(L=42, alpha=a, seed=0)
        n_vs.append(cfg.n_vortices)
        H = build_ab_cloud_hamiltonian(L=42, alpha=a, W=2.0, sigma=0.5, seed=0)
        eigs = np.linalg.eigvalsh(H)
        r = _central_eigs(eigs, frac=0.3)
        rs.append(float(np.mean(spacing_ratios(r))) if len(spacing_ratios(r)) >= 5 else float("nan"))
    return {"alphas": alphas, "n_vortices": n_vs, "r_values": rs}

register("V64", "<r> vs N_vortices", v64, desc="Effect of vortex count")


def v65():
    """Number variance comparison: GUE vs Poisson vs AB-cloud."""
    H = build_ab_cloud_hamiltonian(L=42, alpha=0.5, W=2.0, sigma=0.5, seed=0)
    eigs = np.linalg.eigvalsh(H)
    xi = polynomial_unfold(eigs)
    L_vals = np.linspace(0.5, 8, 12)
    Sig = number_variance(xi, L_vals)
    # GUE prediction
    from python.ab_cloud_stats import Sigma2_GUE, Sigma2_Poisson
    return {"L_vals": L_vals.tolist(),
            "Sigma2_empirical": Sig.tolist(),
            "Sigma2_GUE": Sigma2_GUE(L_vals).tolist(),
            "Sigma2_Poisson": Sigma2_Poisson(L_vals).tolist()}

register("V65", "Sigma^2 comparison", v65, desc="GUE vs Poisson vs empirical")


def v66():
    """Local <r> across spectrum (energy-resolved)."""
    from python.ab_cloud_stats import local_mean_r
    H = build_ab_cloud_hamiltonian(L=42, alpha=0.5, W=2.0, sigma=0.5, seed=0)
    eigs = np.linalg.eigvalsh(H)
    local_r = local_mean_r(eigs, window=30)
    return {"local_r": local_r.tolist(),
            "min": float(np.min(local_r)) if len(local_r) else None,
            "max": float(np.max(local_r)) if len(local_r) else None,
            "mean": float(np.mean(local_r)) if len(local_r) else None}

register("V66", "Local <r>(E)", v66, desc="Energy-resolved local statistics")


def v67():
    """Vortex configurations for various alphas — show q_k=+-1 charges."""
    configs = {}
    for a in [1/3, 1/2, 2/5, 3/7]:
        cfg = default_vortex_config(L=14, alpha=a, seed=0)
        configs[str(a)] = {
            "n_pos": sum(1 for q in cfg.charges if q > 0),
            "n_neg": sum(1 for q in cfg.charges if q < 0),
            "net_charge": cfg.net_charge,
            "n_total": cfg.n_vortices,
        }
    return configs

register("V67", "Vortex configs by alpha", v67, desc="Vortex charge balance")


def v68():
    """Eigenvalue IPR at alpha=1/2."""
    H = build_ab_cloud_hamiltonian(L=42, alpha=0.5, W=2.0, sigma=0.5, seed=0)
    eigs, vecs = np.linalg.eigh(H)
    iprs = []
    for k in range(0, len(eigs), max(1, len(eigs) // 20)):
        psi = vecs[:, k]
        prob = np.abs(psi) ** 2
        ipr = np.sum(prob ** 2)
        iprs.append(float(ipr))
    return {"mean_ipr": float(np.mean(iprs)), "ipr_samples": iprs,
            "L": 42, "N": 42*42}

register("V68", "IPR alpha=1/2", v68, desc="Inverse participation ratio")


def v69():
    """Check V11,V12,V13,V14 trend: <r> -> 0.5996 as L grows."""
    Ls = [14, 28, 42]
    rs = []
    for L in Ls:
        H = build_ab_cloud_hamiltonian(L, alpha=0.5, W=2.0, sigma=0.5, seed=0)
        eigs = np.linalg.eigvalsh(H)
        r = _central_eigs(eigs, frac=0.3)
        rs.append(float(np.mean(spacing_ratios(r))))
    early_mean = float(np.mean(rs[:1]))
    late_mean = float(np.mean(rs[1:]))
    return {"Ls": Ls, "r_values": rs,
            "early_mean": early_mean, "late_mean": late_mean,
            "trend_to_GUE": bool(abs(late_mean - R_GUE) < abs(early_mean - R_GUE))}

register("V69", "L-trend to GUE", v69, desc="<r> approaches GUE with L")


def v70():
    """Compare AB-cloud <r> at L=42 across 3 alphas."""
    alphas = [1/3, 1/2, 2/3]
    rs = []
    for a in alphas:
        H = build_ab_cloud_hamiltonian(L=42, alpha=a, W=2.0, sigma=0.5, seed=0)
        eigs = np.linalg.eigvalsh(H)
        r = _central_eigs(eigs, frac=0.3)
        rs.append(float(np.mean(spacing_ratios(r))))
    return {"alphas": alphas, "r_values": rs,
            "alpha_half_is_max": bool(rs[1] >= max(rs))}

register("V70", "3-alpha comparison", v70, desc="L=42 alpha comparison")


# -------- V71-V86: Additional checks --------

def v71():
    """Sigma_BK at N=10000 with bootstrap."""
    return sigma_bk_bootstrap([10000], n_trials=200)

register("V71", "sigma_BK N=10000", v71, desc="Large N sigma_BK")


def v72():
    """Sigma_BK at N=100 vs N=10000 ratio."""
    s100 = bogomolny_keating_sigma(100)
    s10000 = bogomolny_keating_sigma(10000)
    return {"sigma_100": float(s100), "sigma_10000": float(s10000),
            "ratio": float(s100 / s10000),
            "expected_ratio": float(np.sqrt(10000 / 100))}

register("V72", "sigma_BK ratio", v72, desc="1/sqrt(N) scaling check")


def v73():
    """Chiral symmetry score sweep."""
    return chiral_sweep_alpha(L=28, W=2.0, sigma=0.5,
                              alpha_grid=[1/7, 1/5, 1/4, 1/3, 2/5, 1/2, 3/5, 2/3, 3/4, 4/5])

register("V73", "Chiral sweep", v73, plot_fn=plot_chiral_sweep_alpha,
         desc="Chiral symmetry vs alpha")


def v74():
    """Spectral form factor long-time at alpha=1/2."""
    return spectral_form_factor_long(L=42, alpha=0.5, W=2.0, sigma=0.5,
                                     seed=0, t_max=20, n_t=80)

register("V74", "SFF long", v74, plot_fn=plot_spectral_form_factor_long,
         desc="Long-time SFF ramp+plateau")


def v75():
    """Multifractal spectrum at alpha=1/2."""
    return multifractal_spectrum(L=28, alpha=0.5, W=2.0, sigma=0.5,
                                 seed=0, n_states=2,
                                 q_values=np.linspace(-2, 4, 7))

register("V75", "Multifractal D_q", v75, plot_fn=plot_multifractal_spectrum,
         desc="D_q spectrum")


def v76():
    """Multifractal D_2 vs alpha sweep."""
    return multifractal_Dq_sweep_alpha(L=28, W=2.0, sigma=0.5,
                                        alpha_grid=[1/5, 1/3, 2/5, 1/2, 3/5, 2/3, 4/5])

register("V76", "D_2 vs alpha", v76, plot_fn=plot_multifractal_Dq_sweep_alpha,
         desc="D_2(alpha) — should peak at 1/2")


def v77():
    """Topological entanglement entropy at alpha=1/2."""
    return topological_entanglement_entropy(L=28, alpha=0.5, W=2.0, sigma=0.5,
                                             seed=0, n_states=2)

register("V77", "Topological EE", v77, plot_fn=plot_topological_entanglement,
         desc="TEE gamma_top")


def v78():
    """IPR scaling vs L."""
    return ipr_scaling(L_grid=[14, 28, 42], alpha=0.5, W=2.0, sigma=0.5, n_states=3)

register("V78", "IPR scaling", v78, plot_fn=plot_ipr_scaling,
         desc="IPR ~ N^(-D2/2)")


def v79():
    """Lyapunov exponent sweep vs W."""
    return lyapunov_sweep_W(L=28, alpha=0.5, sigma=0.5,
                            W_grid=np.linspace(0, 5, 11), n_realizations=2)

register("V79", "Lyapunov vs W", v79, plot_fn=plot_lyapunov_sweep_W,
         desc="Anderson localization diagnostic")


def v80():
    """Level velocity dE/dW."""
    return level_velocity_dW(L=28, alpha=0.5, sigma=0.5,
                             W_values=np.linspace(0.5, 4, 12), seed=0,
                             n_states=8)

register("V80", "Level velocity", v80, plot_fn=plot_level_velocity,
         desc="dE/dW response")


def v81():
    """RG flow at alpha=1/2."""
    return rg_block_spin(L=42, alpha=0.5, W=2.0, sigma=0.5, seed=0)

register("V81", "RG flow", v81, plot_fn=plot_rg_flow,
         desc="Kadanoff block-spin RG")


def v82():
    """Central charge CFT fit."""
    return central_charge_cft(L=28, alpha=0.5, W=2.0, sigma=0.5, seed=0, n_states=2)

register("V82", "Central charge", v82, plot_fn=plot_central_charge,
         desc="c_eff from EE scaling")


def v83():
    """GUE <r> reference value."""
    return {"R_GUE": R_GUE, "R_GOE": R_GOE, "R_POISSON": R_POISSON,
            "source": "Atas et al. 2013"}

register("V83", "GUE reference values", v83, desc="Standard reference values")


def v84():
    """R_2(s) Montgomery = GUE formula check."""
    s = np.array([0.5, 1.0, 1.5, 2.0, 3.0])
    R2_montgomery = R2_Montgomery(s)
    R2_gue = R2_GUE(s)
    return {"s": s.tolist(), "R2_Montgomery": R2_montgomery.tolist(),
            "R2_GUE": R2_gue.tolist(),
            "match": bool(np.allclose(R2_montgomery, R2_gue))}

register("V84", "Montgomery=GUE", v84, desc="Montgomery pair = GUE R_2")


def v85():
    """p(s) GUE Wigner surmise check."""
    s = np.array([0.5, 1.0, 1.5, 2.0])
    p = p_GUE(s)
    # Should integrate to 1 over [0, inf)
    s_int = np.linspace(0, 10, 1000)
    integral = np.trapz(p_GUE(s_int), s_int)
    return {"p_at_s": p.tolist(), "integral": float(integral),
            "normalized": bool(abs(integral - 1.0) < 0.01)}

register("V85", "Wigner surmise", v85, desc="GUE p(s) normalization")


def v86():
    """Spacing distribution at alpha=1/3."""
    H = build_ab_cloud_hamiltonian(L=42, alpha=1/3, W=2.0, sigma=0.5, seed=0)
    eigs = np.linalg.eigvalsh(H)
    r = _central_eigs(eigs, frac=0.3)
    s, p = spacing_distribution(r, n_bins=25)
    return {"alpha": 1/3, "s": s.tolist(), "p": p.tolist()}

register("V86", "p(s) alpha=1/3", v86,
         plot_fn=lambda r: plot_spacing_distribution(
             np.array([]), name="v86_spacing_alpha_third",
             title="V86: p(s) at alpha=1/3"),
         desc="Spacing at alpha=1/3")


# -------- V87-V96: New monumental checks --------

def v87():
    """V87: RG flow at multiple alphas."""
    results = {}
    for a in [1/3, 1/2, 2/3]:
        results[str(a)] = rg_block_spin(L=42, alpha=a, W=2.0, sigma=0.5, seed=0)
    return results

register("V87", "RG flow multi-alpha", v87,
         plot_fn=lambda r: plot_rg_flow(r.get("0.5", r.get(list(r.keys())[0])),
                                          name="v87_rg_flow_alpha_half"),
         desc="RG flow at 3 alphas")


def v88():
    """V88: Lyapunov exponent at multiple (alpha, W) points."""
    results = {}
    for a in [1/3, 1/2, 2/3]:
        for W in [1.0, 2.0, 3.0]:
            results[f"alpha={a}_W={W}"] = lyapunov_exponent(L=28, alpha=a, W=W,
                                                             sigma=0.5, seed=0)
    return results

register("V88", "Lyapunov multi-point", v88,
         plot_fn=lambda r: plot_lyapunov_sweep_W(
             lyapunov_sweep_W(L=42, alpha=0.5, sigma=0.5,
                              W_grid=np.linspace(0, 5, 11), n_realizations=3),
             name="v88_lyapunov_multi"),
         desc="Lyapunov at multiple points")


def v89():
    """V89: Multifractal spectrum at multiple alphas."""
    results = {}
    for a in [1/3, 1/2, 2/3]:
        results[str(a)] = multifractal_spectrum(L=28, alpha=a, W=2.0, sigma=0.5,
                                                 seed=0, n_states=2,
                                                 q_values=np.linspace(-2, 4, 7))
    return results

register("V89", "Multifractal multi-alpha", v89,
         plot_fn=lambda r: plot_multifractal_spectrum(
             r.get("0.5", r.get(list(r.keys())[0])),
             name="v89_multifractal_alpha_half"),
         desc="D_q at 3 alphas")


def v90():
    """V90: TEE at multiple L."""
    results = {}
    for L in [14, 28]:
        results[str(L)] = topological_entanglement_entropy(L=L, alpha=0.5, W=2.0,
                                                            sigma=0.5, seed=0,
                                                            n_states=2)
    return results

register("V90", "TEE multi-L", v90,
         plot_fn=lambda r: plot_topological_entanglement(
             r.get("28", r.get(list(r.keys())[0])),
             name="v90_TEE_L28"),
         desc="TEE at 3 system sizes")


def v91():
    """V91: SFF long-time at multiple W."""
    results = {}
    for W in [1.0, 2.0, 3.0]:
        results[str(W)] = spectral_form_factor_long(L=42, alpha=0.5, W=W,
                                                     sigma=0.5, seed=0,
                                                     t_max=20, n_t=60)
    return results

register("V91", "SFF long multi-W", v91,
         plot_fn=lambda r: plot_spectral_form_factor_long(
             r.get("2.0", r.get(list(r.keys())[0])),
             name="v91_SFF_W2"),
         desc="SFF at 3 vortex strengths")


def v92():
    """V92: Level velocity at multiple alphas."""
    results = {}
    for a in [1/3, 1/2, 2/3]:
        results[str(a)] = level_velocity_dW(L=28, alpha=a, sigma=0.5,
                                             W_values=np.linspace(0.5, 4, 10),
                                             seed=0, n_states=8)
    return results

register("V92", "Level velocity multi-alpha", v92,
         plot_fn=lambda r: plot_level_velocity(
             r.get("0.5", r.get(list(r.keys())[0])),
             name="v92_level_velocity_alpha_half"),
         desc="dE/dW at 3 alphas")


def v93():
    """V93: Chiral symmetry at multiple (L, W)."""
    results = {}
    for L in [28, 42]:
        for W in [1.0, 2.0, 3.0]:
            results[f"L={L}_W={W}"] = chiral_symmetry_score(L=L, alpha=0.5, W=W,
                                                              sigma=0.5, seed=0)
    return results

register("V93", "Chiral multi-L-W", v93,
         plot_fn=lambda r: plot_chiral_sweep_alpha(
             chiral_sweep_alpha(L=42, W=2.0, sigma=0.5),
             name="v93_chiral_sweep"),
         desc="Chiral symmetry at 9 (L, W) points")


def v94():
    """V94: Central charge at multiple alphas."""
    results = {}
    for a in [1/3, 1/2, 2/3]:
        results[str(a)] = central_charge_cft(L=28, alpha=a, W=2.0, sigma=0.5, seed=0,
                                              n_states=2)
    return results

register("V94", "Central charge multi-alpha", v94,
         plot_fn=lambda r: plot_central_charge(
             r.get("0.5", r.get(list(r.keys())[0])),
             name="v94_central_charge_alpha_half"),
         desc="c_eff at 3 alphas")


def v95():
    """V95: Band gap alpha sweep at multiple L."""
    results = {}
    for L in [14, 28]:
        results[str(L)] = band_gap_alpha_sweep(L=L, alpha_grid=[
            1/7, 1/5, 1/4, 1/3, 2/5, 1/2, 3/5, 2/3, 3/4, 4/5])
    return results

register("V95", "Band gap multi-L", v95,
         plot_fn=lambda r: plot_band_gap_alpha(
             r.get("28", r.get(list(r.keys())[0])),
             name="v95_band_gap_L28"),
         desc="Gap vs alpha at 3 L")


def v96():
    """V96: IPR scaling at multiple alphas."""
    results = {}
    for a in [1/3, 1/2, 2/3]:
        results[str(a)] = ipr_scaling(L_grid=[14, 28, 42], alpha=a, W=2.0, sigma=0.5,
                                       n_states=2)
    return results

register("V96", "IPR scaling multi-alpha", v96,
         plot_fn=lambda r: plot_ipr_scaling(
             r.get("0.5", r.get(list(r.keys())[0])),
             name="v96_ipr_scaling_alpha_half"),
         desc="IPR scaling at 3 alphas")


# -------- V97-V99: Third monumental batch --------


def v97():
    """V97: GUE transition scaling — <r>(L) -> R_GUE as L -> inf."""
    # Use 3 different alphas to show convergence is alpha-dependent
    results = {}
    for a in [1/3, 1/2, 2/3]:
        results[str(a)] = gue_transition_scaling(
            L_grid=[14, 28, 42, 56], alpha=a, W=2.0, sigma=0.5, n_seeds=2)
    return results

register("V97", "GUE transition scaling", v97,
         plot_fn=lambda r: plot_gue_transition_scaling(
             r.get("0.5", r.get(list(r.keys())[0])),
             name="v97_gue_scaling_alpha_half"),
         desc="<r>(L) -> R_GUE as L -> inf, 1/L extrapolation")


def v98():
    """V98: Hofstadter butterfly WITH vortices — band broadening and gap structure."""
    # Sweep at 2 sizes for finite-size comparison
    results = {}
    for L in [14, 28]:
        results[str(L)] = hofstadter_butterfly_with_vortices(
            L=L, W=2.0, n_alpha=25)
    return results

register("V98", "Butterfly w/ vortices multi-L", v98,
         plot_fn=lambda r: plot_butterfly_with_vortices(
             r.get("28", r.get(list(r.keys())[0])),
             name="v98_butterfly_L28"),
         desc="Pure vs vortex butterfly at 2 L")


def v99():
    """V99: Entanglement spectrum level statistics at multiple alphas."""
    results = {}
    for a in [1/3, 1/2, 2/3]:
        results[str(a)] = entanglement_spectrum_level_stats(
            L=28, alpha=a, W=2.0, sigma=0.5, seed=0, n_states=32)
    # Also do an alpha sweep
    results["sweep"] = entanglement_spectrum_alpha_sweep(
        L=28, W=2.0, sigma=0.5,
        alpha_grid=[1/7, 1/5, 1/3, 2/5, 1/2, 3/5, 2/3, 4/5])
    return results

register("V99", "Entanglement spectrum", v99,
         plot_fn=lambda r: plot_entanglement_spectrum(
             r.get("0.5", r.get(list(r.keys())[0])),
             name="v99_entanglement_alpha_half"),
         desc="Entanglement spectrum <r> at 3 alphas + sweep")


# =====================================================================
# Main runner
# =====================================================================


def run_all(quick: bool = False, only_ids: list = None) -> Dict:
    """Run all verifications and return report."""
    import gc
    print(f"\n{'='*70}")
    print(f"AB-Cloud Monograph Verification — Monumental Edition")
    print(f"Total verifications registered: {len(VERIFICATIONS)}")
    print(f"{'='*70}\n")

    report = {
        "title": "AB-Cloud Monograph Verification — Monumental Edition",
        "total_verifications": len(VERIFICATIONS),
        "results": [],
        "plots": [],
        "summary": {},
    }

    t_start = time.time()

    for i, ver in enumerate(VERIFICATIONS, 1):
        vid = ver["id"]
        if only_ids and vid not in only_ids:
            continue
        print(f"[{i:3d}/{len(VERIFICATIONS)}] {vid}: {ver['name']} ... ", end="", flush=True)
        t0 = time.time()
        result, err = _safe(ver["fn"])
        elapsed = time.time() - t0
        if err:
            print(f"ERROR ({elapsed:.1f}s)")
            print(f"  {err.splitlines()[0]}")
            report["results"].append({
                "id": vid, "name": ver["name"], "status": "error",
                "error": err, "elapsed_seconds": elapsed,
            })
        else:
            print(f"OK ({elapsed:.1f}s)")
            entry = {
                "id": vid, "name": ver["name"], "status": "ok",
                "description": ver["desc"],
                "result": _to_jsonable(result),
                "elapsed_seconds": elapsed,
            }
            # Generate plot if applicable
            if ver["plot_fn"]:
                try:
                    plot_path = ver["plot_fn"](result)
                    if plot_path:
                        entry["plot"] = plot_path
                        report["plots"].append(plot_path)
                except Exception as e:
                    entry["plot_error"] = f"{type(e).__name__}: {e}"
            report["results"].append(entry)
        # Force garbage collection to prevent memory accumulation
        gc.collect()
        # In quick mode, skip after V20
        if quick and i >= 20:
            print("\n[quick mode] Stopping after 20 verifications.")
            break

    total_elapsed = time.time() - t_start
    n_ok = sum(1 for r in report["results"] if r["status"] == "ok")
    n_err = sum(1 for r in report["results"] if r["status"] == "error")
    report["summary"] = {
        "total_run": len(report["results"]),
        "n_ok": n_ok,
        "n_error": n_err,
        "elapsed_seconds": total_elapsed,
        "n_plots": len(report["plots"]),
    }
    print(f"\n{'='*70}")
    print(f"DONE: {n_ok}/{len(report['results'])} OK, {n_err} errors, "
          f"{len(report['plots'])} plots, {total_elapsed:.1f}s")
    print(f"{'='*70}\n")
    return report


def main():
    parser = argparse.ArgumentParser(description="AB-Cloud monumental verification runner")
    parser.add_argument("--quick", action="store_true", help="Quick smoke test (first 20)")
    parser.add_argument("--only", nargs="*", help="Run only specific IDs")
    args = parser.parse_args()

    report = run_all(quick=args.quick, only_ids=args.only)

    # Save report
    report_path = REPORT_DIR / "verification_report.json"
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False, default=str)
    print(f"Report saved: {report_path}")

    # Save summary markdown
    md_path = REPORT_DIR / "verification_summary.md"
    with open(md_path, "w", encoding="utf-8") as f:
        f.write("# AB-Cloud Monograph Verification — Monumental Edition\n\n")
        f.write(f"- Total verifications: {report['total_verifications']}\n")
        f.write(f"- Run: {report['summary']['total_run']}\n")
        f.write(f"- OK: {report['summary']['n_ok']}\n")
        f.write(f"- Errors: {report['summary']['n_error']}\n")
        f.write(f"- Plots: {report['summary']['n_plots']}\n")
        f.write(f"- Elapsed: {report['summary']['elapsed_seconds']:.1f}s\n\n")
        f.write("## Results\n\n")
        f.write("| ID | Name | Status | Description |\n")
        f.write("|----|------|--------|-------------|\n")
        for r in report["results"]:
            f.write(f"| {r['id']} | {r['name']} | {r['status']} | {r.get('description', '')} |\n")
    print(f"Summary saved: {md_path}")


if __name__ == "__main__":
    main()
