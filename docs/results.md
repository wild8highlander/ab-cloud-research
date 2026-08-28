---
title: Reference results & reproducibility
---

# Reference results

The reference full-suite run:
[`results/verification_run_v18_37tests_2026-08-28.txt`](https://github.com/wild8highlander/ab-cloud-research/blob/main/results/verification_run_v18_37tests_2026-08-28.txt)

| # | Test | Verdict | Key value |
|---|---|---|---|
| 1 | Gram points | PASS | machine precision |
| 17 | Byers–Yang (q → q+1) | PASS | defect 3.5e-15 |
| 20 | Connes self-duality | PASS | 4 zero modes |
| 28 | Berry R₂(0) at finite N | PASS | two-pass ζ loop |
| 32 | Hatano–Nelson skin | PASS | 5040 complex eigs |
| 33 | ⟨r⟩ GUE | PASS/WARN | 0.5848 ± 0.0260 |
| 36 | Montgomery correlation hole | PASS | d_GUE 0.140 < d_Pois 0.227 |
| … | full table | 37 tests | see the log |

## Reproducibility guarantees

- **Deterministic seeds** — `MersenneTwister(12345)` everywhere;
- **Certified zeros** — mpmath, 50 digits, provenance recorded;
- **Two-pass verdicts** — a test must agree at two lattice sizes;
- **Full logs** — every run writes computation logs + console tee;
- **CI** — the quick protocol runs on every push
  ([julia.yml](https://github.com/wild8highlander/ab-cloud-research/blob/main/.github/workflows/julia.yml)).
