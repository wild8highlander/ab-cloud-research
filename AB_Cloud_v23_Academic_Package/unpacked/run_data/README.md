# `run_data/` — The Run Archives: Every Number's Raw Home
> Four complete run archives — the 38-test reference run and the three September 2026 Test 34 addendum runs — plus the audit-tier reading guide.

_Location: [unpacked/](../README.md) › [run_data/](README.md)_

Every statistic quoted in the monograph, the Academic Essence and the preprints was produced by one of the four runs archived here, and this folder preserves the archives in full: reports in four formats, computation logs, console captures, plots, spacing arrays, configurations and verdict registers. It is the evidence base of the package — the folder a referee reaches for first, and the folder the monograph's Appendix E (the audit-tier data guide) documents page by page.

## The four runs

| Folder | Run | What happened | Headline |
|---|---|---|---|
| [`run_20260914_234626/`](run_20260914_234626/README.md) | **The reference run** (14–16 Sep 2026, 26.04 h) | All 38 tests, two-pass protocol, four-format FINAL_REPORT, 9,921-line consolidated log | 79 verdict entries: 66 PASS / 13 FAIL; 127 audit sub-checks, 121 passed |
| [`run_20260917_080329_m2/`](run_20260917_080329_m2/README.md) | **MODE 2 HARDCORE**, torus 96×96 (17 Sep) | Test 34 ensemble: 20 realizations, 91,360 pooled spacings | pooled D = 0.0970; composite GUE-CONSISTENT |
| [`run_20260917_084900_m3/`](run_20260917_084900_m3/README.md) | **MODE 3 DEEP DIAG** (17 Sep) | Differential CDF, short-range zone, seed forensics, finite-size probe, bootstrap | D(L) flat; mixture w* ≈ 0.25; residual = GUE floor |
| [`run_20260919_085734_m2/`](run_20260919_085734_m2/README.md) | **Klein quartic PSL(2,7)** (19 Sep) | Test 34 on the Hurwitz surface, 5 realizations, 100,000 zeros | pooled D = 0.0808, d_GUE = 0.0044 — GUE-CONSISTENT |

## How to work with this folder

Start with the reading guide [`AUDIT_DATA.md`](AUDIT_DATA.md) — the package's own manual for navigating the archives, from the audit-tier census to the per-test lettered sub-checks (H0–H7, K1–K3, S1–S4, R1–R4, Z1–Z5). Then enter the reference run: its README maps all 38 test folders, each of which carries its own detailed README with verdicts, verification statement, log excerpts and the verbatim console capture. The three September runs document the addendum chain (Add.1–Add.8 of the monograph) that re-examined Test 34 and closed it on the Klein quartic.

A note on what "reconstructed" means for run 20260919_085734_m2: that pass executed on the operator's device, the console capture survived, and the device-side result directory did not; the shipped folder is the console's own numbers with provenance-flagged derived configuration — nothing re-simulated. The distinction is documented in the run's README and in the monograph's addendum chapter Add.8.

## Complete contents inventory

| File | Size | Description |
|---|---|---|
| `AUDIT_DATA.md` | 5.5 KB · 87 lines | The audit-tier reading guide for the run archives: census, per-test navigation, how to verify any number in the monograph. |

## Subfolders

| Subfolder | Contents | What it is |
|---|---|---|
| [`run_20260914_234626/`](run_20260914_234626/README.md) | 1 files, 39 subfolders | See its README |
| [`run_20260917_080329_m2/`](run_20260917_080329_m2/README.md) | 9 files, 1 subfolders | See its README |
| [`run_20260917_084900_m3/`](run_20260917_084900_m3/README.md) | 8 files | See its README |
| [`run_20260919_085734_m2/`](run_20260919_085734_m2/README.md) | 4 files, 1 subfolders | See its README |

---
_This README is part of the GitHub edition of the AB-Cloud v23 package (v34). Package overview: [../README.md](../README.md)._