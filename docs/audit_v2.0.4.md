# Audit v2.0.4 — «the rigidity-slope purge»

**Scope.** A complete pass over every README (439 files), every table and
every monograph of the repository, following the earlier fix series
(v2.0.1: D_nn metric; v2.0.2: C3 data + text tails; v2.0.3: the
GOE-as-GUE spacing-law purge). The trigger: rounded/stale numbers and
wrong-slope formulas still visible in the documents other people read.

**Method.** Pattern scanners over all md/tex/typ/txt/html sources
(9 error classes), precise-context PDF extraction (`pdftotext`) for every
built monograph, XML-level inspection of every docx, and byte-exact
(`od`-verified) source inspection for the Julia suite. Every fix was
applied with occurrence-count assertions; every rebuilt artifact was
content-verified.

---

## 1. The physics that was wrong (and is now right)

The v2.0.3 audit fixed the *spacing* laws. This audit found the same
disease in the *long-range* statistics — the rigidity/number-variance
slopes — plus stale evidence quotes and one impossible table value.

| Quantity | What documents said | Correct (validated) |
|---|---|---|
| Δ₃^GUE slope | (1/π²)ln L — **the GOE slope** | **(1/2π²)(ln 2πL + γ − 5/4)** |
| Δ₃^GOE | mislabeled as GUE | (1/π²)(ln 2πL + γ − 5/4 − π²/8) |
| Σ²_GUE slope | (2/π²)ln L + const — **the GOE slope** | **(1/π²)(ln 2πL + γ + 1)** |
| Σ²_GUE exact (v21 tables) | (2/π²)(ln L + 0.296) | L − (2/π²)\[πL·Si − ½(1−cos x) − ½(γ+ln x−Ci)\] |
| Poisson ⟨r⟩ (Table D.5) | **1.3863 — impossible (> 1)** | **0.3863** (= 2ln2 − 1) |

**Numerical re-validation (this audit, `scripts/verify_delta3_theory.py`
methodology).** GOE/GUE 140×140, 40 matrices each, semicircle-CDF
unfolding, exact Dyson–Mehta window integral (step-function least
squares, incommensurate stride L/9.7):

```
GOE  L= 10..40:  sim/GOE-B = 1.02 1.02 1.02 0.96   (GOE-A without −π²/8: 0.66–0.75)
GUE  L= 10..40:  sim/GUE   = 1.01 0.96 0.98 0.98
```

This settles the constant: **GOE Δ₃ carries the −π²/8 shift, GUE does
not, and the GUE slope is half the GOE slope** (the Δ₃ ≈ Σ²/2 relation).

## 2. Where each error lived (the fix map)

### 2.1 Canonical v22 monograph (EN/RU/ZH × md, tex, html, pdf, docx; base + v221)
`GUE ≈ (1/π²)ln L` in the definitions paragraph of **all three
languages**, in every format. Also the phrase "relative excess … falls
from 0.99 to 0.48" (a ratio below 1 is not an excess) — reworded to
"ratio". Fixed: md ×3, tex ×3, html ×6, pdf ×6 (v22 base rebuilt with
tectonic/LaTeX — the ZH edition with a proper CJK main font, Noto Serif
SC, after FandolSong proved unavailable; v221 rebuilt with WeasyPrint),
docx ×6 (OMML equation surgery on the `≈1/π2lnL` object →
`≈(1/(2π2))ln(2πL)`).

### 2.2 v21 monograph, Appendix D (EN/RU × md, html ×2, docx ×2, pdf ×2 each)
- `Σ²_GUE(L) ≈ (2/π²)·ln(L) + const` (D.2.1) → correct slope;
- Table D.3 "GUE pred" column (0.0600/0.2005/0.2826/0.3861/0.4543/0.5266)
  was (2/π²)(ln L + 0.296) — the GOE slope; replaced by the exact GUE
  closed form (0.3442/0.4157/0.4571/0.5090/0.5431/0.5793);
- `Δ3(L) ≈ (1/π²)·ln(L)` (D.2.2) → (1/2π²)(ln 2πL + γ − 5/4);
- Table D.4 "GUE pred" column was exactly (1/π²)ln L
  (0.1113/0.1631/0.1972/0.2333) → (0.1147/0.1406/0.1576/0.1757);
- Table D.5 Poisson ⟨r⟩ = 1.3863 → **0.3863**;
- the D.2.1 narrative ("systematically above the GUE prediction")
  rewritten to the honest statement (below theory at L ≤ 5, above at
  L ≥ 7); D.2.2 "~30-40% below" → "15–41% below".

### 2.3 v21 monograph, §11.3.1 (EN/RU, all formats)
The N=200 rigidity check quoted GOE-slope numbers as "GUE":
Σ²(2) vs 0.2005 (−78.4%) / Σ²(10) vs 0.5266 (−87.9%) /
Δ₃(2) vs 0.0702 (−97.9%) / Δ₃(10) vs 0.2333 (−98.8%). Correct GUE
references: 0.4157 / 0.5793 / 0.0941 / 0.1757 → deviations
−89.6% / −89.0% / −98.4% / −98.4% (the qualitative conclusion — the
zeros are *more* rigid than GUE — is unchanged and now honestly
quantified).

### 2.4 Root README and the formal layer
- Root README quoted the pre-v2.0.3 suite output: `KS D = 0.099187,
  p-value = 0.000000` and the Lean tail `KS D = 0.099187 ref 0.099187`.
  The corrected suite (re-run for this audit on 5000 zeros) prints
  `D = 0.031048, p-value = 0.000130`, `W² = 1.538304` — quoted now.
- `formal/README.md`: the displayed `F_GUE(s) = 1 − e^{−πs²/4}` was the
  **GOE** CDF; now `erf(2s/√π) − (4s/π)e^{−4s²/π}`.
- `formal/lean4/ABCloud/README.md` coverage table: rounded old frozen
  values `KS D = 0.099187`, `W² = 17.6049` → `0.031048`, `1.5383`
  (the full-precision table was already fixed in v2.0.3; these rounded
  twins had escaped).

### 2.5 v23 Monograph (Academic Package, MG/ROOT — 516 pp, docx + pdf)
- "GOE follows the **1/15th-power law**" — no such law exists;
- the GOE formula `(π⁻²)(ln 2πL + γ − 5/4 − π²/8)` was labeled GUE;
- "**81%** of the way from GOE (0.5307) to GUE (0.5996)" for the mean
  0.5798 — arithmetic error, the correct fraction is **71%**
  ((0.5798−0.5307)/(0.5996−0.5307) = 0.713);
- the quoted `delta3_rigidity` docstring and the Test-14 console
  listing (with the stale "Paper's rel_err ≈ 0.97").
All fixed by XML surgery on the docx (math objects preserved, the GOE
formula reassigned to GOE, the GUE formula rebuilt from copied math
elements) and the PDFs regenerated with LibreOffice.

### 2.6 The Julia suite itself (`ab_cloud_v23.jl` — 5 copies)
- t3_11 "GUE asymp" curve: `[2.0/π² · (log(2πL) + 0.5 + γ)]` — GOE
  slope, wrong constant, ~1.8× above the true GUE curve →
  `[1.0/π² · (log(2πL) + 1.0 + γ)]`;
- Test-14 header println: `GUE: ~(1/π²)ln L. (Paper's rel_err ≈ 0.97.)`
  → `GUE: ~(1/2π²)ln L. (Paper's rel_err ≈ 0.13.)`;
- the `delta_3_rigidity` docstring (quoted verbatim by the v23
  monograph): same slope fix.
(The suite's *verdicts* compare against simulated GUE references, not
these display curves — no verdict changes.)

### 2.7 lab-3d preprint and READMEs
- `lab-3d/preprint/ab_cloud_preprint.tex`: rigidity table carried the
  pre-repair rel_errs (0.972/0.481 → 0.126/0.412); the Δ₃ equation had
  the GOE slope; the Σ² "asymptotic" form mixed Ci into the slope;
  "Σ² is the more robust diagnostic" inverted after the repair.
- `lab-3d/README.md`: ⟨r⟩ = 0.238 described as "Poisson-like" (Poisson
  is 0.3863; 0.238 is strongly clustered) → "strongly clustered".
- Academic-package test-16 README: "0.3869 (Poisson)" — digit typo →
  0.3863.

### 2.8 Historical run logs — deliberately untouched
`results/*.txt` execution logs contain the same wrong printouts, but
they are timestamped records of what the code printed at run time;
rewriting them would falsify provenance. The code is fixed; future runs
print correctly. (The monographs no longer quote the old values.)

## 3. Rebuild provenance

| Artifact family | Engine | Verified |
|---|---|---|
| v22 base pdf ×3 | tectonic (LaTeX; ZH: xeCJK + Noto Serif SC) | slope text + ratio wording, page counts 32/33/26 |
| v221 pdf ×3 | WeasyPrint from fixed html | slope text, pages 38/41/34 |
| v21 corrected pdf ×2 | WeasyPrint from fixed html | tables D.3–D.5, §11.3.1 |
| v21 with_Verification pdf ×2 | LibreOffice from fixed docx | same, pages 273/227 (match originals) |
| v23 MG/ROOT pdf ×2 | LibreOffice from fixed docx | all four fix points, 516 pp |
| package preprint pdf | tectonic (37+2 figure symlinks resolved to run_data) | 71%, logarithmic law, 305 pp |
| docx surgeries | python zipfile XML-level | occurrence-count assertions, zero collateral |
| SHA256SUMS | recomputed for touched package files | 9 sum lines verified |

## 4. Verification summary

- Hilbert_Polya: **21/21** tests pass; AB_Cloud_Quantum_Research:
  **42/42** tests pass.
- Python verification suite re-run (5000 zeros): KS D = 0.031048,
  p = 0.000130, W² = 1.538304 — matches the Lean frozen refs
  (REF_MAIND 0.0310483738, REF_MAINW2 1.5383040905) exactly.
- Repo-wide scanners re-run: zero hits for the 9 error classes in all
  READMEs, tables, monographs and their builds.
- False positives investigated and cleared: spinor64 empirical ⟨r⟩
  values (0.6027 measured), run-log mixed 0.5992/0.5996 references
  (surmise vs large-N canon, both published), zeta-zero data listings,
  GOE/GUE spacing formulas in lab-3d and AB_CLOUD_ALL_HYPOTHESES.
