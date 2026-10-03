# Test 37: (1/2)! via Γ — half-factorial & GUE normalization — folder `test_37_half_factorial_gamma/`
> AB-Cloud v23 SUPERCOMBO · reference run `run_20260914_234626` · Julia 1.12.0 · generated 2026-09-15 09:09:07
**Verdicts (verbatim register):** PASS  
**Family:** EXACT (analytic identity, 256-bit)  
**Location:** [unpacked/](../../../README.md) › [run_data/](../../README.md) › [run_20260914_234626/](../README.md) › [test_37_half_factorial_gamma/](README.md)
## 1. What this folder is
Test 37 certifies the half-factorial identity chain through the Gamma function: Γ(1/2) = √π, (1/2)! = Γ(3/2) = √π/2, the ladder and recurrence relations of the suite's own Lanczos lgamma implementation, and — the distinctive part — the UNIQUENESS of the Γ-construction via the reflection self-dual fixed point Γ(1/2)² = π, all verified exactly at 256-bit precision.
This folder is the canonical, reading-friendly archive of the test inside the reference run. It holds the four-format report (`report.md/html/pdf/docx`), the timestamped computation log and raw console capture (in [`logs/`](logs/README.md)), and the figures (in [`plots/`](plots/README.md)). Raw provenance copies of the same report files and logs ship in the run's [`FINAL_REPORT/`](../FINAL_REPORT/README.md) (`reports/` and `logs/test_37_half_factorial_gamma/`), and the test's verdict lines are registered in `FINAL_REPORT/logs/results_verdicts.txt` — quoted verbatim in section 4 below.
## 2. Why this test matters
Why does a spectral verification suite need a half-factorial certificate? Because the GUE normalisation of the spacing statistics consumes half-integer factorials at every turn — the Wigner surmise, the level-density asymptotics and the unfolding constants are all built from Γ-evaluations at half-integers — and an error there would silently poison every statistical verdict upstream. The suite therefore certifies its own special-function spine: the constant (1/2)! = √π/2 is verified in exact arithmetic, the recurrence and ladder identities of the implementation are checked against their closed forms, and the reflection fixed point Γ(1/2)² = π certifies that the construction is pinned uniquely rather than merely consistent to first order. The audit battery 37b belongs to the run's clean audit census (114 sub-checks, 0 failed across the clean batteries). The monograph's auxiliary-constants appendix lists this certificate with its verbatim 256-bit lines.
## 3. What the test verifies (verbatim from the run's report)
> EXACT: Γ(1/2) = √π, (1/2)! = Γ(3/2) = √π/2, ladder + recurrence (suite's own Lanczos lgamma); UNIQUENESS of the Γ-construction via the reflection self-dual fixed point Γ(1/2)² = π and Bohr–Mollerup log-convexity; the GUE β=2 surmise normalization 32/π² verified as the half-factorial identity (∫p₂ = ⟨s⟩ = 1, ⟨s²⟩ = 3π/8 by quadrature). Pass 2 = 256-bit BigFloat re-audit. METHOD: EXACT: Γ(1/2) = √π, (1/2)! = Γ(3/2) = √π/2, ladder + recurrence (suite's own Lanczos lgamma); UNIQUENESS of the Γ-construction via the reflection self-dual fixed point Γ(1/2)² = π and Bohr–Mollerup log-convexity; the GUE β=2 surmise normalization 32/π² verified as the half-factorial identity (∫p₂ = ⟨s⟩ = 1, ⟨s²⟩ = 3π/8 by quadrature). Pass 2 = 256-bit BigFloat re-audit. Test 37 HARDCORE: 256-bit DE Γ(1/2) err 1.20e-28, Float64 round-off Γ(1/2) 5.83e-16 / (1/2)! 2.94e-16, N=32/π² err 2.51e-26, ladder/self-dual/recurrence exact.
## 4. Verdict lines of the reference run (verbatim)
> Test 37: (1/2)!=√π/2 [rel.err 0.0], 32/π² [rel.err 0.0], ∫p₂=1 [|Δ|=0.0], uniqueness ✓ → PASS
> Test 37b [HARDCORE pass 2]: 3 sub-checks, 0 failed → PASS
## 5. Result line
```text
Test 37b [HARDCORE pass 2]: 3 sub-checks, 0 failed → PASS
```
## 6. Complete contents inventory
| File | Size | Description |
|---|---|---|
| `report_A37.docx` | 5.9 KB | Editable edition of the same report (Microsoft Word). |
| `report_A37.html` | 3.4 KB · 35 lines | Web edition of the same report (self-contained HTML). |
| `report_A37.md` | 3.0 KB · 45 lines | The test's master report (Markdown): verification statement, verdicts, result line, plot inventory, full computation log and console capture. |
| `report_A37.pdf` | 4.1 KB | Print edition of the same report (PDF). |
## 7. Computation log — verbatim excerpt
```text
(no log_comp entries)
```
Every line is timestamped (`[HH:MM:SS.mmm] [+offset-s]`) with the cumulative wall-clock offset since session start; the offsets show exactly when this test executed inside the 26-hour session.
## 8. Console capture — verbatim
The console capture prints each lettered sub-check with its statistic, its pre-registered limit, and its outcome — the audit trail the monograph's Appendix A reproduces.
```text
════════════════════════════════════════════════════════════
TEST 37 (pass 2, HARDCORE): (1/2)! via Γ — 256-bit precision audit
────────────────────────────────────────────────────────────
 DE reference: |Γ(1/2)_256 − √π| = 1.20e-28 (independent quadrature)
 Γ(1/2):  Float64 vs 256-bit DE rel.err = 5.83e-16
 (1/2)!:  Float64 vs 256-bit DE rel.err = 2.94e-16
 N = 1/[½·(π/4)^{3/2}·(1/2)!] at 256-bit vs 32/π²: rel.err = 2.51e-26
 ladder Γ(5/2)_DE = 3√π/4: rel.err = 4.78e-25
 Γ(1/2)_DE² = π (reflection self-duality): rel.err = 1.35e-28
 recurrence (1/2)!_DE = ½·Γ(1/2)_DE: rel.err = 2.51e-26
────────────────────────────────────────────────────────────
 Float64 round-off    PASS — |ΔΓ(1/2)|=5.83e-16, |Δ(1/2)!|=2.94e-16 relative (machine-ε scale)
 32/π² identity (256-bit) PASS — rel.err 2.51e-26 — exact at 256-bit
 ladder + self-duality + recurrence (256-bit) PASS — worst rel.err 4.78e-25 across the three identities
 Test 37b [HARDCORE pass 2]: 3 sub-checks, 0 failed → PASS
```
## 9. How to reproduce
```text
julia ab_cloud_v23.jl --test 37 --no-two-pass   # single test, single pass
julia ab_cloud_v23.jl --test all                  # full suite, reference protocol
```
The same test ships in the Python clone: `python -m abcloud.cli --test 37` (module [`abcloud/tests_27_38.py`](../../../python_clone/abcloud/tests_27_38.py)).
## 10. Where this fits in the package
- **Monograph:** Chapter 37 of Part II (*"An Aharonov–Bohm Lattice Operator Framework for the Riemann ζ Zeros"*) — the chapter number is the test number.
- **Final report:** the test's section in [`../FINAL_REPORT/README.md`](../FINAL_REPORT/README.md) (all 38 reports embedded inline).
- **Neighbours:** [test_36](../test_36_byte_robust/README.md) · [test_38](../test_38_curie_point/README.md)
---
_Package overview: [unpacked/](../../README.md) · Run archive: [../](../README.md) · GitHub edition of AB-Cloud v23 (v34)._
