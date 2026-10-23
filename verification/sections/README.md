<!-- AB-ENRICHED:v1 · sub -->
<div align="center">

<img src="https://capsule-render.vercel.app/api?type=venice&height=48&color=0:00e5ff,100:05060f&section=header" alt="" width="100%"/>

**🧭 [⬆ verification/](../README.md) · [🏠 Root README](../../README.md)**

</div>
# Per-Section Micro-Verifications

> **🧭 Navigation:** [verification/](../README.md) · [Root README](../../README.md)

Self-contained Python checks (stdlib only, no data files, no dependencies)
that verify concrete numeric claims in under a second. Every check prints its
raw numbers and exits non-zero on failure, so they double as CI smoke tests.

> **v3.0 honesty note.** The previous section-3 and section-6 scripts were
> the *same* two-line assert (`0 < b < 1`) on the same expression — a
> placeholder, not a verification, and the README even quoted a wrong sample
> value (0.0707… instead of the true 0.0624…). Both checks are now real and
> independent of the suite's own kernels.

| Path | What is actually verified |
|---|---|
| `section3_ab_cloud/python/verify.py` | the section-3 closed form `b = π/(4π² + 2π√3)`: π is re-computed to 50 digits with an independent Machin series (integer arithmetic, no `math.pi`), the closed form is evaluated with `Decimal` at 50 digits, and the float64 evaluation used across the suite must match the reference to < 1e-15 relative; the defining relation `4π²b + 2π√3·b − π = 0` must hold to < 1e-48. True value: `b = 0.06238119412102823`. |
| `section6_riemann_zeros/python/verify.py` | the Gram-point canon `gram_point(k)` for k = 1, 2, 3 against the frozen golden constants `23.17028270133466 / 27.670182217848343 / 31.71797995477886`, re-derived by **pure bisection** of `θ(t) = πk` with the 5-term Riemann–Siegel theta — an independent root-finding path (no Lambert W, no Newton) that would have caught the seed-only and `2π·W(n/e)` bugs of v2.x. Tolerance 1e-9; measured Δ ≤ 3.6e-15. |

## Run

```bash
python3 verification/sections/section3_ab_cloud/python/verify.py
python3 verification/sections/section6_riemann_zeros/python/verify.py
```

---

<!-- enriched-r3 -->

This folder is a small but functional **shelf of its module**: it keeps a focused set of artifacts that the parent README references. The listing below is generated from the folder itself, so it is exact; the parent README explains how these pieces fit into the study. Nothing here is a compiled binary or an external download — everything is committed source, data or documentation.

Per-section micro-verifications: one folder per monograph section, each checking that section's claims in isolation.

## Folder contents

**Subfolders:** `section3_ab_cloud/` · `section6_riemann_zeros/`

<div align="center">

<img src="../../assets/svg/divider-cyan.svg" alt="—" width="100%" height="12"/>
<sub>⚡ Part of <a href="../../README.md">AB-Cloud Research</a> — numbers are verbatim from the unified registry; no result on this page is a claim about the Riemann hypothesis · <a href="../README.md">⬆ parent section</a></sub>

</div>
