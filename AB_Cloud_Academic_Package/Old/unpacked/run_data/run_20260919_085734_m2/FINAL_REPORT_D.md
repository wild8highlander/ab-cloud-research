# Test 34 — FINAL REPORT

**Run:** `20260919_085734_m2` · **Mode:** 2 — HARDCORE · **Generated:** 2026-09-19 08:57:34

> **Provenance.** This report is reconstructed from the operator console capture of the
> run (see `logs/console_output.txt`). Every statistic is verbatim from the protocol.
> The geometry identification and the full 14-digit seeds are derived deterministically
> from the laboratory source arithmetic (`finite-size_lab.jl` v1.3, `lab_seed`,
> `cayley_lift_k`, `geom_site_label`) and cross-checked against the console truncations;
> they are marked "derived" in `config.json`. The device-side plots and raw arrays were
> not captured in the transfer and live in the operator's
> `/mnt/sdcard/Download/results/run_20260919_085734_m2/`.

## Configuration

| parameter | value |
|---|---|
| zeros loaded | 100000 |
| geometry | Klein quartic PSL(2,7) — magnetic Cayley graph \|G\|=168 ×56 lift (9408 sites, 102% of the 9216-site budget; genus 3, HURWITZ) — *derived* |
| L budget | 96 (autoscale/stretch ON) |
| window fraction | 0.5 (central window 4705 levels → 4664 unfolded spacings per realization) |
| vortices Nv | 2 |
| charge q | 1.0000 |
| flux alpha | 0.5000 |
| disorder W | 1.0000 |
| realizations | 5 (MODE 2) |
| seed ladder | seed_base 20260916, mode 2, k = 1…5 — *derived, exact* |

## Composite verdict (v23-compatible)

[OK] **GUE-CONSISTENT — Test 34 composite criterion satisfied**

| criterion | rule | status |
|---|---|---|
| c1 | (p > 0.01 OR D < 0.10) | [OK] (D = 0.0808 < 0.10) |
| c2 | d_GUE < d_Pois | [OK] (0.0044 < 0.2817, factor 64) |
| c3 | 0.75 <= R2 plateau <= 1.25 | [OK] (0.9734) |

## Pooled statistics (23,320 spacings vs 100,000-zero reference)

| metric | value |
|---|---|
| pooled D (two-sample KS vs zeta) | 0.0808 |
| pooled p | 1.187e-107 |
| d_GUE | 0.0044 |
| d_Pois | 0.2817 |
| R2 plateau (1.0-2.0) | 0.9734 |
| mean \|R2-GUE\| band 0.2-2.0 | 0.0299 |
| spacings | 23320 |

## Realizations

| # | seed | spacings | D | p | d_GUE | d_Pois | plateau | time | flag |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 20260976802863 | 4664 | 0.0828 | 6.2e-27 | 0.0095 | 0.2838 | 0.9747 | 04:07 | - |
| 2 | 20260976802964 | 4664 | 0.0811 | 7.3e-26 | 0.0068 | 0.2808 | 0.9723 | 05:24 | - |
| 3 | 20260976803065 | 4664 | 0.0817 | 2.7e-26 | 0.0078 | 0.2824 | 0.9736 | 05:16 | - |
| 4 | 20260976803166 | 4664 | 0.0804 | 2.0e-25 | 0.0065 | 0.2801 | 0.9743 | 05:34 | - |
| 5 | 20260976803267 | 4664 | 0.0846 | 3.8e-28 | 0.0128 | 0.2860 | 0.9713 | 05:50 | - |

- **ensemble median D:** 0.0817
- **ensemble IQR:** 0.0017
- **min / max D:** 0.0804 / 0.0846
- **MAD outliers:** none
- **ensemble stability:** STABLE
- **per-realization wall time:** 04:07 / 05:24 / 05:16 / 05:34 / 05:50 · **total 26:15**

## Reading (see monograph Addendum Add.8)

The confrontation signature — a residual AB−ζ distance near 0.08–0.10 with the lattice
on the GUE side of every class statistic — reproduces on a genus-3 Hurwitz surface after
the torus ensemble of run 20260917_080329_m2 (D = 0.0970 → 0.0808 here, −17%): the gap is
a property of the chaotic phase, not of the geometry. Within the laboratory metric the
AB cloud is statistically indistinguishable from pure GUE (d_GUE = 0.0044 at n = 23,320,
inside the one-sample KS 1% critical value ≈ 0.011), while the ζ zeros sit at the
GUE-vs-ζ calibration floor 0.0242 — the residual distance remains dominated by the
reference side, consistent with the effective-Poisson-admixture decomposition
(w* ≈ 0.28) of the September addendum.
