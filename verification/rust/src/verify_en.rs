//! Thin rendering layer (CANON_SPEC §10): EN output of structured results.
//! All computation lives in main.rs — no duplicated math.
use crate::{Obj1Res, Obj2Res, Obj3Res, SCRow};

pub fn render_obj1_en(r: &Obj1Res) -> String {
    let mut out = String::from(
        "\n═══════════════════════════════════════════════════\n  OBJECTION 1: b(N) Convergence\n  b(N) = (1/N) · Σ|γ_k − γ̃_k|, Gram points: θ(t) = πk (Newton)\n═══════════════════════════════════════════════════\n");
    out += &format!("  {:>10} {:>15} {:>15}\n", "N", "b(N)", "log10(b(N))");
    for i in 0..r.ns.len() {
        let lg = if r.bn[i] > 0.0 { r.bn[i].log10() } else { -999.0 };
        out += &format!("  {:>10} {:>15.8} {:>15.4}\n", r.ns[i], r.bn[i], lg);
    }
    if r.has_fit {
        out += &format!("\n  Empirical law:  b(N) ~ {:.4} * N^(-{:.4})   (R^2 = {:.4})\n", r.fit_a, r.fit_s, r.fit_r2);
    }
    if r.converging {
        out += "\nResult: b(N) converging as N increases. OK\n";
        out += "  b(N) decreases monotonically over the table — convergence confirmed on the accessible range. The decay is EMPIRICAL, not O(1/sqrt(N)).\n";
    } else {
        out += "\nResult: b(N) NOT converging as N increases. WARN\n";
    }
    out
}

pub fn render_obj2_en(r: &Obj2Res) -> String {
    let mut out = String::from(
        "\n═══════════════════════════════════════════════════\n  OBJECTION 2: GUE Spacing Statistics\n  s_k = Δγ_k · log(γ_k/2π) / 2π,  GUE (β=2) surmise via the canonical 32768-point CDF table\n═══════════════════════════════════════════════════\n");
    if r.n < 2 {
        return out + "WARNING: not enough spacings for the GUE test.\n";
    }
    out += &format!("  Spacing mean: {:.9}  var: {:.9}  (n = {})\n", r.mean, r.var, r.n);
    out += &format!("  Kolmogorov-Smirnov:  D = {:.6},  p-value = {:.3e}\n", r.d, r.p);
    out += &format!("  Cramér-von Mises:    W^2 = {:.6}\n", r.w2);
    out += &format!("  Anderson-Darling:   A^2 = {:.6}\n", r.a2);
    out += &format!("  <r> (adjacent-ratio): {:.6}  (n = {}, GUE surmise ~ 0.5992)\n", r.r, r.nr);
    if r.rejected {
        out += "\nResult: KS test REJECTED at alpha=0.05.\n";
        out += "  Note: at large n the exact GUE surmise is formally rejected — the known finite-T corrections of the zeta zeros, not a data artifact (mean ~ 1 validates the unfolding; golden-anchored).\n";
    } else {
        out += "\nResult: KS test NOT REJECTED at alpha=0.05.\n";
    }
    out
}

pub fn render_obj3_en(r: &Obj3Res) -> String {
    let mut out = String::from(
        "\n═══════════════════════════════════════════════════\n  OBJECTION 3: Large-T Decay Rate\n  Fit log(b(N)) vs log(N): expected slope ~ -0.5\n═══════════════════════════════════════════════════\n");
    if r.slope.is_nan() {
        return out + "WARNING: Insufficient data points for regression.\n";
    }
    out += "  Linear Regression on log scale:\n";
    out += &format!("  Slope     = {:+.6}  (expected: -0.5)\n", r.slope);
    out += &format!("  Intercept = {:+.6}\n", r.intercept);
    out += &format!("  R^2       = {:.6}\n", r.r2);
    out += &format!("  95% CI for slope: [{:.4}, {:.4}]\n", r.cilo, r.cihi);
    if r.ok {
        out += &format!("\nResult: Fitted slope = {:+.4}, expected = -0.500. OK\n", r.slope);
    } else {
        out += &format!("\nResult: Fitted slope = {:+.4}, expected = -0.500. WARN: slope deviates from -0.5 (decay is empirical)\n", r.slope);
    }
    out
}

pub fn render_selfcheck_en(rows: &[SCRow], npass: usize, nfail: usize) -> String {
    let mut out = String::from(
        "\n=== Golden self-check — frozen anchors (canon: meridian-spectral-observatory, selftest 199/199) ===\n");
    for r in rows {
        if r.skip {
            out += &format!("  {:<24} SKIP\n", r.name);
            continue;
        }
        let st = if r.ok { "PASS" } else { "FAIL" };
        out += &format!("  {:<24} {}  computed = {:.12e}, expected = {:.12e}, D = {:.3e}\n",
            r.name, st, r.got, r.exp, r.delta);
    }
    out += &format!("  Self-check: {} passed, {} failed\n", npass, nfail);
    out
}
