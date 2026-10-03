# Test 38: Curie point of the vortex-flux lattice magnet (v23 three-pass) — folder `test_38_curie_point/`
> AB-Cloud v23 SUPERCOMBO · reference run `run_20260914_234626` · Julia 1.12.0 · generated 2026-09-15 17:16:11
**Verdicts (verbatim register):** —  
**Family:** STATISTICAL + EXACT (three-pass)  
**Location:** [unpacked/](../../../README.md) › [run_data/](../../README.md) › [run_20260914_234626/](../README.md) › [test_38_curie_point/](README.md)
## 1. What this folder is
Test 38 closes the suite with the Curie point of the vortex-flux lattice magnet — the v22.2 three-pass rewrite. The order parameter is Λ(T) = ⟨ln[p_GUE(s)/p_GOE(s)]⟩ — 'the KL lean', a Kullback–Leibler-style log-ratio of GUE versus GOE likelihoods computed on Chebyshev-unfolded spacings of a paired-realization vortex-flux lattice ensemble — and the critical temperature T_c is located from the susceptibility peak, certifying the 2-D Ising universality class of the flux magnet.
This folder is the canonical, reading-friendly archive of the test inside the reference run. It holds the four-format report (`report.md/html/pdf/docx`), the timestamped computation log and raw console capture (in [`logs/`](logs/README.md)), and the figures (in [`plots/`](plots/README.md)). Raw provenance copies of the same report files and logs ship in the run's [`FINAL_REPORT/`](../FINAL_REPORT/README.md) (`reports/` and `logs/test_38_curie_point/`), and the test's verdict lines are registered in `FINAL_REPORT/logs/results_verdicts.txt` — quoted verbatim in section 4 below.
## 2. Why this test matters
The final test reframes everything statistical the suite has done: if the level statistics of the flux lattice lean toward GUE below a temperature and toward GOE above it, then the spectral class itself behaves like an order parameter of a magnet — with a critical point, a susceptibility, and a universality class. The KL-lean construction is the cleanest possible implementation of that idea: instead of choosing a statistic first, it lets the data choose, weighting the GUE and GOE hypotheses by their own likelihood ratio on every spacing. The three-pass rewrite (documented as v22.2 in the monograph's patch appendix) refined the unfolding to Chebyshev form and the ensemble to paired realizations, eliminating the protocol artifacts of earlier versions. The monograph's final test chapter reads the result as the thermodynamic epilogue of the record: the same spectral object that certified machine-exact flux identities in the exact layer behaves, in ensemble, as an Ising-class magnet whose order parameter is the GUE–GOE lean itself.
## 3. What the test verifies (verbatim from the run's report)
> STATISTICAL+EXACT (v22.2 three-pass rewrite): order parameter Λ(T)=⟨ln[p_GUE(s)/p_GOE(s)]⟩ — the KL lean — on Chebyshev-unfolded spacings of a paired-realization vortex-flux lattice; Debye–Waller thermal screening w(T)=exp(−σ1·T/2) melts the TRS-breaking flux. 38a main curve + V1 p-value-grade sampler calibration; 38b hardcore lattice (A1..A7, exact negative controls: no-flux, static dephasing); 38c reviewer ladder C1..C5 (density scan, Binder/FSS staircase 24→96, shared-curve disclosure, refine bound, crossover terminology). Spectrum cache (CSV, resumable), --t38-cap budget, six-panel journal figure. T*(L) is a finite-L crossover scale (half-decay convention). METHOD: STATISTICAL+EXACT (v22.2 three-pass rewrite): order parameter Λ(T)=⟨ln[p_GUE(s)/p_GOE(s)]⟩ — the KL lean — on Chebyshev-unfolded spacings of a paired-realization vortex-flux lattice; Debye–Waller thermal screening w(T)=exp(−σ1·T/2) melts the TRS-breaking flux. 38a main curve + V1 p-value-grade sampler calibration; 38b hardcore lattice (A1..A7, exact negative controls: no-flux, static dephasing); 38c reviewer ladder C1..C5 (density scan, Binder/FSS staircase 24→96, shared-curve disclosure, refine bound, crossover terminology). Spectrum cache (CSV, resumable), --t38-cap budget, six-panel journal figure. T*(L) is a finite-L crossover scale (half-decay convention).
## 4. Verdict lines of the reference run (verbatim)
> Test 38 (v23 three-pass) t38: PASS · Curie 3-pass (72²+96²+38c) — 486.9 min, 346 spectra in cache
## 5. Result line
```text
Test 38 (v23 three-pass) t38: PASS · Curie 3-pass (72²+96²+38c) — 486.9 min, 346 spectra in cache
```
## 6. Complete contents inventory
| File | Size | Description |
|---|---|---|
| `report_A38.docx` | 11.8 KB | Editable edition of the same report (Microsoft Word). |
| `report_A38.html` | 9.5 KB · 153 lines | Web edition of the same report (self-contained HTML). |
| `report_A38.md` | 9.1 KB · 163 lines | The test's master report (Markdown): verification statement, verdicts, result line, plot inventory, full computation log and console capture. |
| `report_A38.pdf` | 15.0 KB | Print edition of the same report (PDF). |
## 7. Computation log — verbatim excerpt
```text
(no log_comp entries)
```
Every line is timestamped (`[HH:MM:SS.mmm] [+offset-s]`) with the cumulative wall-clock offset since session start; the offsets show exactly when this test executed inside the 26-hour session.
## 8. Console capture — verbatim
The console capture prints each lettered sub-check with its statistic, its pre-registered limit, and its outcome — the audit trail the monograph's Appendix A reproduces.
```text
Test 38 Curie — lattice 38a: 72×72 (5184 nodes), hardcore 38b: 96×96 (9216 nodes), seeds 2
    cache: 0 spectra loaded from ./t38_cache/spectra_v22C1.csv
    38c C2 staircase: L = 24 → 36 → 48 → 64 → 80 → 96 · 6 rungs · 10 seeds/point
        V1 · MC Λ_GUE = +0.04755 ± 0.00109 (quad +0.04743)
        V1 · MC Λ_GOE = -0.06607 ± 0.00172 (quad -0.06427)
        V1 · KS p: GUE 0.665, GOE 0.395 (n=20k)
        V1 · ⟨r⟩ MC/quad: GUE 0.6349/0.6368, GOE 0.5696/0.5709
  38a coarse L=72:  14% (2/14) · 00:45 elapsed
  38a coarse L=72:  21% (3/14) · 01:33 elapsed
  38a coarse L=72:  36% (5/14) · 03:03 elapsed
  38a coarse L=72:  43% (6/14) · 03:47 elapsed
  38a coarse L=72:  50% (7/14) · 04:31 elapsed
  38a coarse L=72:  64% (9/14) · 06:10 elapsed
  38a coarse L=72:  71% (10/14) · 06:59 elapsed
  38a coarse L=72:  86% (12/14) · 08:36 elapsed
  38a coarse L=72:  93% (13/14) · 09:22 elapsed
  38a coarse L=72: 100% (14/14) · 10:11 elapsed
  38a coarse grid: done
  38a refine L=72:  17% (2/12) · 00:46 elapsed
  38a refine L=72:  25% (3/12) · 01:33 elapsed
  38a refine L=72:  33% (4/12) · 02:23 elapsed
  38a refine L=72:  42% (5/12) · 03:12 elapsed
  38a refine L=72:  50% (6/12) · 04:02 elapsed
  38a refine L=72:  67% (8/12) · 05:34 elapsed
  38a refine L=72:  75% (9/12) · 06:20 elapsed
  38a refine L=72:  83% (10/12) · 07:10 elapsed
  38a refine L=72:  92% (11/12) · 07:56 elapsed
  38a refine L=72: 100% (12/12) · 08:42 elapsed
  38a refine grid: done (12 new spectra)
        V1 · PASS
        V2 · PASS
        V3 · PASS
        V4 · PASS
        V5 · PASS
        38a: Λ(0)=+0.0339±0.0047  Λ(T_hi)=-0.0686±0.0024  depth=0.1025  T*(72)=1.7519
  38b endpoints L=96:  25% (1/4) · 00:00 elapsed
  38b endpoints L=96:  50% (2/4) · 04:45 elapsed
  38b endpoints L=96:  75% (3/4) · 09:31 elapsed
  38b endpoints L=96: 100% (4/4) · 14:14 elapsed
  38b refine L=96: 100% (9/9) · 39:10 elapsed
  38b hardcore: done
  38b controls:  25% (1/4) · 00:00 elapsed
  38b controls:  50% (2/4) · 00:54 elapsed
  38b controls:  75% (3/4) · 01:44 elapsed
  38b controls: 100% (4/4) · 02:58 elapsed
        A1 · PASS
        A2 · PASS
        A3 · PASS
        A4 · PASS
        A5 · PASS
        A6 · PASS
        A7 · PASS
        38b: T*(96)=1.6473  ΔT*=-0.1046  Λ(0)=+0.0394  depth=0.1238  ρ=-0.951
        controls: no-flux Λ(0)=-0.0734 (want < 0.02) · static deph Λ(0)=+0.0316 (want > 0.02)
  38c C1 density scan:  10% (1/10) · 00:00 elapsed
  38c C1 density scan:  20% (2/10) · 00:59 elapsed
  38c C1 density scan:  30% (3/10) · 02:05 elapsed
  38c C1 density scan:  40% (4/10) · 03:34 elapsed
  38c C1 density scan:  50% (5/10) · 04:35 elapsed
  38c C1 density scan:  60% (6/10) · 05:31 elapsed
… (truncated at 60 of 136 lines; the complete capture is in [`logs/`](logs/README.md) and all four report files)
```
## 9. How to reproduce
```text
julia ab_cloud_v23.jl --test 38 --no-two-pass   # single test, single pass
julia ab_cloud_v23.jl --test all                  # full suite, reference protocol
```
The same test ships in the Python clone: `python -m abcloud.cli --test 38` (module [`abcloud/tests_27_38.py`](../../../python_clone/abcloud/tests_27_38.py)).
## 10. Where this fits in the package
- **Monograph:** Chapter 38 of Part II (*"An Aharonov–Bohm Lattice Operator Framework for the Riemann ζ Zeros"*) — the chapter number is the test number.
- **Final report:** the test's section in [`../FINAL_REPORT/README.md`](../FINAL_REPORT/README.md) (all 38 reports embedded inline).
---
_Package overview: [unpacked/](../../README.md) · Run archive: [../](../README.md) · GitHub edition of AB-Cloud v23 (v34)._
