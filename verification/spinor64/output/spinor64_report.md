# 64 Spinor Structures of the Klein Quartic — Verification Report

Generated: 2026-09-03 09:54:16

Author of the monograph: Isaev Iskhak Khamzatovich (ORCID 0009-0003-7299-0701, DOI 10.5281/zenodo.21825394)

This run corrects the v21 monograph claim (section 3.1) that only idx=38 of the 64 spinor structures shows GUE agreement. Two independent experiments below show that **all 64 structures give the same (GUE-consistent) statistics**; no structure is unique.

## E1 — Klein graph {3,7}: exact symmetry (all 64 structures)

Tessellation: 56 vertices, 84 edges, 24 heptagonal faces; PSL(2,7) = Aut(K4), order 168.

| orbit | size | Arf | zero modes | max spectral distance within orbit |
|---|---|---|---|---|
| 0 | 28 | 1 | 2 | 7.99e-15 |
| 1 | 21 | 0 | 3 | 8.88e-15 |
| 2 | 7 | 0 | 3 | 6.22e-15 |
| 3 | 7 | 0 | 3 | 5.77e-15 |
| 4 | 1 | 0 | 7 | 0.00e+00 |

* Orbit sizes **[28, 21, 7, 7, 1]**: the 28 odd (Arf=1) structures form ONE orbit — PSL(2,7) is transitive on them (the classical bitangent theorem, verified numerically).
* Worst pairwise spectral distance over all 64 structures: 8.88e-15 (machine precision). **Conjugate structures are exactly isospectral.**
* Gauge invariance: 7.11e-15.
* Zero modes of the discrete Dirac operator (spin part): 2 (odd orbit) / 3 (even orbits) / 7 (trivial class).
* Spacing-ratio statistics of the clean graph spectra are Poisson-like (the deterministic single-graph spectrum); the GUE class emerges from the AB-cloud dynamics (E2) — consistent with the monograph's own conclusion in section 4.1 that the source of GUE is the cloud dynamics, not the geometry of the substrate.

## E2 — AB-cloud Hofstadter torus: GUE statistics of all 64 structures

Config: L=44, alpha=0.5, Nv=54 (density-scaled), W=0.0, torus, :monumental vortex gauge, seed=96; bulk window 0.6.

Size-matched GUE ensemble (100 matrices of 1936x1936): median <r> = 0.6013, 95% CI [0.5847, 0.6140] (analytic GUE reference 0.5997).

| idx | holonomy | orbit | Arf | phi_x/pi | phi_y/pi | <r> | p_mc(GUE) | verdict |
|---|---|---|---|---|---|---|---|---|
| 0 | 100011 | 0 | 1 | 0 | 1 | 0.5968 | 0.550 | GUE-consistent |
| 1 | 000011 | 1 | 0 | 1 | 1 | 0.5935 | 0.360 | GUE-consistent |
| 2 | 000001 | 1 | 0 | 0 | 1 | 0.5968 | 0.550 | GUE-consistent |
| 3 | 100001 | 1 | 0 | 1 | 1 | 0.5935 | 0.360 | GUE-consistent |
| 4 | 001111 | 2 | 0 | 0 | 0 | 0.6005 | 0.910 | GUE-consistent |
| 5 | 101111 | 1 | 0 | 1 | 0 | 0.6027 | 0.830 | GUE-consistent |
| 6 | 101101 | 3 | 0 | 0 | 0 | 0.6005 | 0.910 | GUE-consistent |
| 7 | 001101 | 0 | 1 | 1 | 0 | 0.6027 | 0.830 | GUE-consistent |
| 8 | 001011 | 3 | 0 | 0 | 1 | 0.5968 | 0.550 | GUE-consistent |
| 9 | 101011 | 0 | 1 | 1 | 1 | 0.5935 | 0.360 | GUE-consistent |
| 10 | 101001 | 0 | 1 | 0 | 1 | 0.5968 | 0.550 | GUE-consistent |
| 11 | 001001 | 0 | 1 | 1 | 1 | 0.5935 | 0.360 | GUE-consistent |
| 12 | 100111 | 0 | 1 | 0 | 0 | 0.6005 | 0.910 | GUE-consistent |
| 13 | 000111 | 0 | 1 | 1 | 0 | 0.6027 | 0.830 | GUE-consistent |
| 14 | 000101 | 0 | 1 | 0 | 0 | 0.6005 | 0.910 | GUE-consistent |
| 15 | 100101 | 2 | 0 | 1 | 0 | 0.6027 | 0.830 | GUE-consistent |
| 16 | 010010 | 1 | 0 | 1 | 1 | 0.5935 | 0.360 | GUE-consistent |
| 17 | 110010 | 1 | 0 | 0 | 1 | 0.5968 | 0.550 | GUE-consistent |
| 18 | 110000 | 0 | 1 | 1 | 1 | 0.5935 | 0.360 | GUE-consistent |
| 19 | 010000 | 2 | 0 | 0 | 1 | 0.5968 | 0.550 | GUE-consistent |
| 20 | 111110 | 0 | 1 | 1 | 0 | 0.6027 | 0.830 | GUE-consistent |
| 21 | 011110 | 3 | 0 | 0 | 0 | 0.6005 | 0.910 | GUE-consistent |
| 22 | 011100 | 0 | 1 | 1 | 0 | 0.6027 | 0.830 | GUE-consistent |
| 23 | 111100 | 0 | 1 | 0 | 0 | 0.6005 | 0.910 | GUE-consistent |
| 24 | 111010 | 2 | 0 | 1 | 1 | 0.5935 | 0.360 | GUE-consistent |
| 25 | 011010 | 1 | 0 | 0 | 1 | 0.5968 | 0.550 | GUE-consistent |
| 26 | 011000 | 0 | 1 | 1 | 1 | 0.5935 | 0.360 | GUE-consistent |
| 27 | 111000 | 3 | 0 | 0 | 1 | 0.5968 | 0.550 | GUE-consistent |
| 28 | 010110 | 0 | 1 | 1 | 0 | 0.6027 | 0.830 | GUE-consistent |
| 29 | 110110 | 1 | 0 | 0 | 0 | 0.6005 | 0.910 | GUE-consistent |
| 30 | 110100 | 0 | 1 | 1 | 0 | 0.6027 | 0.830 | GUE-consistent |
| 31 | 010100 | 0 | 1 | 0 | 0 | 0.6005 | 0.910 | GUE-consistent |
| 32 | 010011 | 1 | 0 | 1 | 0 | 0.6027 | 0.830 | GUE-consistent |
| 33 | 110011 | 4 | 0 | 0 | 0 | 0.6005 | 0.910 | GUE-consistent |
| 34 | 110001 | 1 | 0 | 1 | 0 | 0.6027 | 0.830 | GUE-consistent |
| 35 | 010001 | 0 | 1 | 0 | 0 | 0.6005 | 0.910 | GUE-consistent |
| 36 | 111111 | 0 | 1 | 1 | 1 | 0.5935 | 0.360 | GUE-consistent |
| 37 | 011111 | 1 | 0 | 0 | 1 | 0.5968 | 0.550 | GUE-consistent |
| 38 | 011101 | 1 | 0 | 1 | 1 | 0.5935 | 0.360 | GUE-consistent |
| 39 | 111101 | 1 | 0 | 0 | 1 | 0.5968 | 0.550 | GUE-consistent |
| 40 | 111011 | 1 | 0 | 1 | 0 | 0.6027 | 0.830 | GUE-consistent |
| 41 | 011011 | 1 | 0 | 0 | 0 | 0.6005 | 0.910 | GUE-consistent |
| 42 | 011001 | 2 | 0 | 1 | 0 | 0.6027 | 0.830 | GUE-consistent |
| 43 | 111001 | 0 | 1 | 0 | 0 | 0.6005 | 0.910 | GUE-consistent |
| 44 | 010111 | 0 | 1 | 1 | 1 | 0.5935 | 0.360 | GUE-consistent |
| 45 | 110111 | 1 | 0 | 0 | 1 | 0.5968 | 0.550 | GUE-consistent |
| 46 | 110101 | 1 | 0 | 1 | 1 | 0.5935 | 0.360 | GUE-consistent |
| 47 | 010101 | 3 | 0 | 0 | 1 | 0.5968 | 0.550 | GUE-consistent |
| 48 | 100010 | 1 | 0 | 0 | 0 | 0.6005 | 0.910 | GUE-consistent |
| 49 | 000010 | 0 | 1 | 1 | 0 | 0.6027 | 0.830 | GUE-consistent |
| 50 | 000000 | 3 | 0 | 0 | 0 | 0.6005 | 0.910 | GUE-consistent |
| 51 | 100000 | 1 | 0 | 1 | 0 | 0.6027 | 0.830 | GUE-consistent |
| 52 | 001110 | 0 | 1 | 0 | 1 | 0.5968 | 0.550 | GUE-consistent |
| 53 | 101110 | 0 | 1 | 1 | 1 | 0.5935 | 0.360 | GUE-consistent |
| 54 | 101100 | 2 | 0 | 0 | 1 | 0.5968 | 0.550 | GUE-consistent |
| 55 | 001100 | 0 | 1 | 1 | 1 | 0.5935 | 0.360 | GUE-consistent |
| 56 | 001010 | 0 | 1 | 0 | 0 | 0.6005 | 0.910 | GUE-consistent |
| 57 | 101010 | 1 | 0 | 1 | 0 | 0.6027 | 0.830 | GUE-consistent |
| 58 | 101000 | 0 | 1 | 0 | 0 | 0.6005 | 0.910 | GUE-consistent |
| 59 | 001000 | 0 | 1 | 1 | 0 | 0.6027 | 0.830 | GUE-consistent |
| 60 | 100110 | 3 | 0 | 0 | 1 | 0.5968 | 0.550 | GUE-consistent |
| 61 | 000110 | 2 | 0 | 1 | 1 | 0.5935 | 0.360 | GUE-consistent |
| 62 | 000100 | 0 | 1 | 0 | 1 | 0.5968 | 0.550 | GUE-consistent |
| 63 | 100100 | 1 | 0 | 1 | 1 | 0.5935 | 0.360 | GUE-consistent |

**64/64 structures are GUE-consistent** (MC p > 0.05). <r> over all 64 structures: 0.5984 +- 0.0035 (spread 0.5935..0.6027) — statistically indistinguishable across structures.

## Conclusion

1. The spinor structures of the Klein quartic split under PSL(2,7) into orbits of sizes 28 (odd, Arf=1) / 21 / 7 / 7 / 1 (even, Arf=0); the 28-element orbit confirms the classical Riemann-Klein bitangent theorem.
2. Conjugate structures have EXACTLY identical spectra (machine precision) — no spin structure can be statistically unique.
3. In the AB-cloud Hofstadter setting ALL 64 structures give GUE-consistent level statistics. The v21 claim that only idx=38 shows GUE agreement was a computation artifact.
4. Internal inconsistency of v21 documented: by the monograph's own formula Arf(e) = e1*e2 + e3*e4 + e5*e6, the vector e(38) = (0,1,1,0,0,1) has Arf = 0, not 1 as claimed in sections 3.2.1 and 12.4.

## Reproducibility

```
python3 verification/spinor64/run_spinor64.py
```

Full log and machine-readable results: `output/` (spinor64_results.json, spinor64_table.csv).
