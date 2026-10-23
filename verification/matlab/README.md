<!-- AB-ENRICHED:v1 · sub -->
<div align="center">

<img src="https://capsule-render.vercel.app/api?type=venice&height=48&color=0:00e5ff,100:05060f&section=header" alt="" width="100%"/>

**🧭 [⬆ verification/](../README.md) · [🏠 Root README](../../README.md)**

</div>
# MATLAB / Octave Verification

> **🧭 Navigation:** [verification/](../README.md) · [Root README](../../README.md) · [CANON_SPEC](../CANON_SPEC.md)

Canonical MATLAB — and GNU Octave — port of the AB-Cloud Verification Suite
kernel, spec `../CANON_SPEC.md` (v3.0). Bit-compatible with the frozen golden
reference `../data/abcloud_golden.json` (meridian-spectral-observatory canon,
selftest 199/199, Julia 1.10.9, first 50 000 Odlyzko zeros).

## Files

| File | What it is |
|---|---|
| `ab_cloud_verify.m` | the single canonical kernel: loader, Lambert W (§1), Gram points (§2), b(N) (§3), GUE table CDF (§5), KS/CvM/AD/⟨r⟩ (§6), objections (§7), frozen-anchor selfcheck (§8) |
| `ab_cloud_verify_en.m` | THIN wrapper pinning `lang='en'` (§10 — no duplicated math) |
| `ab_cloud_verify_ru.m` | THIN wrapper pinning `lang='ru'` (§10 — no duplicated math) |
| `run_verify.m` | thin CLI runner: shared flag language + exit-status mapping |
| `spinor38/` | Test 38 port (separate companion, unchanged) |

## Requirements

- **MATLAB R2014b+** or **GNU Octave 4.4+** — base only, no toolboxes.
  `erf` and `gunzip` are core in both; `lambert_w` is implemented manually
  per spec §1 (Newton, tol `1e-14*(1+|w|)`, up to 50 iterations).
- Octave-safe by construction: no `string` class, no `arguments` blocks,
  no `inputParser`, no tables, no `readtable` — char arrays, cell arrays,
  manual name/value and flag loops only.

## Run

```matlab
cd verification/matlab
run_verify                                          % defaults: 50000 zeros, auto source, all objections
run_verify('--zeros', 50000, '--objection', 'all')
run_verify('--source', '50k_full', '--lang', 'ru')
```

From the shell:

```bash
matlab -batch "run_verify('--zeros', 50000)"
octave --eval "run_verify('--zeros', 50000)"
octave run_verify.m -- --zeros 50000                  # argv() pickup
AB_CLOUD_ARGS='--zeros 50000 --lang ru' octave --eval run_verify
```

## Flags (CANON_SPEC §9)

| Flag | Values | Meaning |
|---|---|---|
| `--zeros N` | integer | how many ordinates to use (default 50 000; `0` = all loaded) |
| `--source NAME` | `auto`, `50k`, `50k_full`, `500k`, `2M`, `highT`, `2M_gz`, `csv`, `zeros6` | which frozen dataset from `../data/` to load; `auto` = smallest registered file with count ≥ zeros; `highT` = BLOCK-offset format; `2M_gz` unpacked via `gunzip` into a temp dir |
| `--objection X` | `1`, `2`, `3`, `all` | run the full suite or one objection |
| `--lang L` | `en`, `ru` | report language (default: auto-detect from `LANG`) |
| `--data-dir DIR` | path | data directory (default `../data` resolved next to this file) |
| `--no-selfcheck` | — | skip the frozen-anchor self-check |

## Self-check (CANON_SPEC §8)

Before any objection runs, the kernel prints a PASS/FAIL/Δ table against the
frozen golden anchors embedded as literals:

- `lambert_w` — 6 anchors, tol 1e-12 rel;
- `gram_point` — 8 anchors (n = 1 … 50000), tol 1e-6 abs;
- `bN(N)` — 6 anchors + `bN(N=1000,off=500)`, tol 1e-6 abs (SKIP if not
  enough zeros are loaded);
- statistics on the FIRST 50 000 zeros — `spacings.mean/var`, `ks.D`,
  `ks.p` (1e-6 rel), `cvm.W2`, `ad.A2` (both 1e-9 rel, as in the canon
  Python selfcheck), `rmean.r`, tol 1e-9
  (SKIP with a printed SKIP line if fewer than 50 000 zeros are loaded).

Anchor highlights on the 50k canon data: `b(50000) = 1.2125526772588608`,
KS `D = 0.021619`, `p ≈ 9.57e-21` (H₀ formally rejected — the printed note
explains this as the known finite-T corrections of the zeta zeros; the
spacing mean ≈ 1 validates the unfolding), `W² = 8.177703`, `A² = 61.492426`,
`⟨r⟩ = 0.6118798907208398` (n_r = 49998) against the GUE surmise 0.5992.

**Exit status: 1 if any anchor fails** (`exit(1)` under a shell launch,
`error` otherwise — both give status 1 in `matlab -batch` / `octave` CLI
runs), 0 otherwise. Every verdict in the report is printed only in the
branch chosen by the computed numbers — no canned verdict strings.

## Canon kernel notes

- `gram_point(k)`: seed `2πk / W(k/e)`, then EXACTLY 8 Newton iterations on
  the 5-term Riemann–Siegel theta (§2) — the old seed-only formula was wrong.
- `bN`: strictly sequential accumulation (§3); the printed tables use the
  prefix array, which is bit-identical to the direct sum.
- `gue_cdf`: 32768-point interpolation table, SMAX = 5, built lazily once and
  cached (`persistent`); outside [0, 5) the exact closed form is used (§5).
- KS two-sided D + λ-corrected p-value (two branches), Cramér–von Mises,
  Anderson–Darling with `1e-300 / 1-1e-16` clamps, ⟨r⟩ adjacent-gap ratio,
  sample variance (n−1) — all §6, sequential summation order.
- Objections: §7 verdicts — monotone-decrease criterion for Obj 1 (decay is
  EMPIRICAL, not O(1/√N)), p < 0.05 rejection with the honest finite-T note
  for Obj 2, |slope − (−0.5)| ≤ 0.1 for Obj 3.

## Deliberate deviations (documented)

- `--zeros 0` loads ALL available zeros (the Python CLI has no `0` case).
- If the b(N) table is not monotonically decreasing, an explicit honest
  "NOT confirmed" line is printed instead of the monotone note.
- No figure export; the runner is console-only.
- `ab_cloud_verify_en.m` / `ab_cloud_verify_ru.m` pin the language even if
  the caller passes `--lang` (the pinned value is appended last and wins).

## spinor38/ — Test 38 port

`spinor38/spinor38.m` reads the frozen classes from `../spinor64/data/` and
rebuilds the 28 odd-orbit spectra with a MATLAB-native cyclic-Jacobi
eigensolver (deliberately not `eig`, so the isospectrality check is
independent of LAPACK):

```matlab
cd verification/matlab/spinor38
spinor38
```

## Summary

- Canonical MATLAB/Octave port of the kernel per `../CANON_SPEC.md` (v3.0), bit-compatible
  with the frozen golden reference `../data/abcloud_golden.json`.
- Gram points: seed `2πk/W(k/e)` + EXACTLY 8 Newton iterations on the 5-term theta
  expansion; `lambert_w` — Newton, tolerance `1e-14*(1+|w|)`, up to 50 iterations.
- GUE CDF via the 32768-point table (SMAX = 5, lazy build + `persistent` cache); KS
  (two-sided D + λ-corrected p), Cramér–von Mises, Anderson–Darling with
  `1e-300 / 1-1e-16` clamps, ⟨r⟩ over adjacent gaps.
- The §8 self-check prints a PASS/FAIL/Δ table over all frozen anchors and exits 1 on any
  mismatch; `ab_cloud_verify_en.m` / `ab_cloud_verify_ru.m` are thin wrappers (§10) with
  all the math in one kernel.
- Run: `run_verify('--zeros', 50000)` from MATLAB/Octave, or
  `octave --eval "run_verify('--zeros', 50000)"` from the shell.
- `spinor38/` — the Test 38 port: its own Jacobi algorithm (not `eig`), data read from
  `../spinor64/data/`.

<div align="center">

<img src="../../assets/svg/divider-cyan.svg" alt="—" width="100%" height="12"/>
<sub>⚡ Part of <a href="../../README.md">AB-Cloud Research</a> — numbers are verbatim from the unified registry; no result on this page is a claim about the Riemann hypothesis · <a href="../README.md">⬆ parent section</a></sub>

</div>
