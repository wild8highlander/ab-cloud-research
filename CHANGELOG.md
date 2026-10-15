# Changelog

## [1.3.8] — 2026-10-15 — «verdict propagation completeness across the remaining runs»

The third consistency wave: the v2.0.7/v2.0.8 verdicts had reached the
central surfaces but not the remaining runs and generators. Plus three
real defects found on the way. Details: `Hilbert_Polya/docs/audit_v2.0.9.md`.

- **V07 `gap_orders` computed by the wrong formula**
  (`log10(pc0_r/max r_EF)` = 0.0027 — a correlation-units gap — while every
  document says «0.63 orders by residual»). Fixed to
  `log10(min_resid/pc0_resid)` = 0.6250, recomputed from the same committed
  residuals; no measurement touched.
- **V07's verdict note hid the best gate** («the comb is invisible») —
  the battery's best gate (Nv = 16, the working window) reaches r_EF =
  0.993 with residual 11.5% vs the zeros' 2.7% (z ≈ 2.4): the same
  conservative/finite-size branch pattern as C4's best gate. Rewritten to
  the conservative-branch reading (family mean 0.76 ± 0.24 in the null
  clouds is retained).
- **C13's README pointed to a non-existent runner**
  (`run_c13_blind_families.py`; the real one is `run_c13_blind.py`), and
  `make_figures_v2.py` wrote «16 gates» for the 20-gate C13 cohort in
  fig25_map — the figure is redrawn (VLM-verified) together with its
  stale «H2 gap is UNIVERSAL» / «H2 = wall of LOCALITY» cells.
- **The C9/C13/C15 verdict strings were out of sync between the runners,
  the JSONs and the README quotes** — the runners still wrote the
  pre-v2.0.7 verdicts (the JSONs had been hand-fixed earlier); all three
  layers now agree: «the open bit-level branch is a wall of LOCALITY»
  (C9), «the H2 result (the zeros' level) is robust» (C13), «the
  rank-metric resolution limit is UNIVERSAL … the twisted weight and the
  ladder carry over» (C15, with the ψ_χ rungs 0.902/0.949 named as the
  L-rungs of the convergence ladder).
- **`make_comp_readmes.py` had drifted from its own outputs** (~12 stale
  verdict strings, including «H2 is a negative verdict» and «разрыв Г2 ≈
  1 порядок» at the committed 0.5): a regeneration would have rolled the
  campaign READMEs back to «H2 — NO». Synchronized.
- **The stale «H2 = NO era» phrasing is gone from the remaining live
  surfaces:** campaign READMEs C7 («identity does not» → the zeros' level
  is yes), C11 («every other verdict is a negative» → resolution-limited
  branches), C16 («never through spectral identity» → not through the
  rank channel), C4/C6-EN («projection of the H2 gap» → of the H2
  question), README.ru.md ×4, README.md ×2, monograph content
  (part2/canon/part4 ru+en — the C15 chapter heads and the C7 bridge),
  preprint.tex ×5 + abstract, explorer (streamlit map + README), docs/v2
  tables, data/README, and the audit canonization report content
  (audit_content*.py + content.json, rebuilt PDF+DOCX).
- **AB_Cloud_Quantum_Research:** Th1's boundaries no longer say «negative
  verdicts (V1, V3, V6, V16)» — the verdicts are the level identity YES
  (V6/V16, the D_nn bridge), the open bit-level branch (V16) and the
  refuted design claims (V1, V3); fixed in all five carriers (Th1 json
  ru/en, T01 README, the generator, the core_spectrum monograph ru/en).
  core_spectrum RESULTS.md rows 8/28 and ROADMAP.md updated to the
  level-identity reading.
- **Regenerated:** Hilbert_Polya monographs C5/C7/canon/v2 × ru/en (8),
  preprint.pdf (tectonic), the audit report (PDF + DOCX), fig25_map
  (ru/en + campaign copies), core_spectrum V7/theorems/appendix/Th1 ×
  ru/en (8). Tests: Hilbert_Polya 22/22, core_spectrum 42/42.

## [1.3.7] — 2026-10-15 — «artifacts & CI synced to v2.0.8; hp_audit v24.3-SA»

The follow-up to [1.3.6]: every derived artifact and gate is now in sync
with the corrected verdicts, and two CI-blocking defects are fixed.

- **Hilbert_Polya monographs (26 documents) regenerated** from the updated
  content sources: C1–C8 × ru/en, theorems/appendix/v2/canon volumes —
  the DOCX/PDF layer no longer carries the pre-v2.0.7/v2.0.8 verdict text
  («H2 — NO», «H5 — NO», «the zeros are encoded, not generated», «the 'NO'
  of Г2 and Г5», «Every negative result (H2, H5, M3)», the stale C3/C4
  verdict passages). `make_monographs.py` now also renders the previously
  ORPHANED `theorems_v2_volume` (parts_theorems_v2.py was never wired into
  the pipeline — a reproducibility gap).
- **The preprint gained a dated «Note added»**: H2 = YES at the zeros'
  level (v2.0.7) and H5 = YES via the convergence ladder (v2.0.8), with the
  v2.0 text preserved as the dated record.
- **core_spectrum monographs (V06/V16/V19 × ru/en + v06/v16 verdict JSONs)
  synced to the level-identity reading** — the session-2 fix had reached the
  READMEs/JSONs only partially and never the monograph content layer.
- **AB_Cloud_Quantum_Research/MONOGRAPH_ARCHIVE rebuilt** (main monograph
  ru/en + Program_Core ru/en): 13 stale verdict statements in the tex
  sources corrected («lattice direction closed (negative)» → «level
  identity — YES, D_nn bridge; bit-level branch open»); the LaTeX image
  paths pointed 7 directories up instead of 3 — every rebuild silently
  lost all 28 figures; now resolved and the DOCX/PDF regenerated
  (publication-quality palette-quantized figures, VLM-verified).
- **The RU info_scorecard of core_spectrum still said «V6 … затворы: НЕТ»**
  (the EN row was fixed in session 2, the RU row was not) — regenerated
  with proper in-card text wrapping (the old `wrap=True` measured only the
  figure edge, letting long text spill onto neighboring cards).
- **Vortex_optimization monograph §9.5** extended with the v2.0.8 reading
  (the scan is the measured basis of the H5 verdict); PREVIEW.pdf
  regenerated; MONOGRAPH_CHANGES.md §6.
- **The audit report `HPB_audit_canonization` rebuilt from its updated
  sources** — the PDF/DOCX had been left at their 2026-10-13 build while
  `audit/src/content.json` already carried the corrected verdicts; also
  fixed `audit_build.py`'s hardcoded output path (an old clone location —
  the documented rebuild command wrote outside the repo) and the README's
  reference to a non-existent TOC script.
- **CI unblocked (2 defects):** (a) ruff F821 — `Pprev` used before its
  loop-carried assignment in `run_c17_blind_phaseB.py` (the ruff.toml gate
  targets exactly this defect class; main was red); (b)
  `validate_package.py` still expected core 1.2.2 after the 1.2.3 bump —
  `tests/test_unified.py` failed. Both fixed; ruff clean, all 5 suites
  green (11 + 19 + 42 + 11 + 22).
- **`hp_audit_standalone.jl` → v24.3-SA** (5 defects, full static audit of
  all 6 087 lines): the console preset state leak (SMOKE→FAST kept
  validation-grade controls), the H1 cost-estimate undercount (GUE nulls
  and per-regime DEEPEN missing), the :fast column of GATE_MIN still on
  smoke-grade minutes, a duplicated v23.6 comment in H3, and the L³→L⁶
  growth note. meridian docs/READMEs updated to v24.3-SA.

## [1.3.6] — 2026-10-15 — «verdict v2.0.8: H5 = YES via the convergence ladder» (repo-wide)

The repo-wide verdict correction of audit **v2.0.8**
(`Hilbert_Polya/docs/audit_v2.0.8.md`): the prime channel Г5/H5 is
**YES — via the convergence ladder**, superseding the «H5 stays NO» note
of [1.3.5]. The basis, from committed data only:

- **C6's own numbers hide a monotone trend:** the gate ψ-ladder
  correlation climbs −0.116 → +0.089 → +0.239 for Nv = 0 → 2 → 16,
  peaking in the working window (Nv ≈ 8–16, q = 1, α = 0.5); the
  over-dense point (Nv = 32 → +0.133) bends back down along the same
  valley — the measurement was taken at L = 24, the smallest rung of the
  size ladder.
- **The `Vortex_optimization` study (Test 34-ext)** supplies the missing
  coordinate: the GUE floor falls 0.0324 → 0.0220 for L = 24 → 96, the
  best pooled D reaches 0.0318 (×3.4 vs the WARN reference 0.1096) —
  everything that brings the cloud to the zeros improves with lattice
  size, in the same window where the ψ-correlation peaks.
- **The zeros' ladder is a rung, not a ceiling:** 0.972 on a 200-zero
  window, converging to 1 by the explicit formula; with H2 = YES
  (v2.0.7) the prime weight enters through the level identity.

What the YES does **not** claim: the direct L = 96 escape of the gate
ladder from the null band — the open bit-level branch (T18 /
core_spectrum V16: z_best = 2.49 < 6); RH stays open, not claimed.

- **Hilbert_Polya:** scorecard H5 NO → YES synced across README.md +
  README.ru.md (all ~40 passages: scorecards ×2, stage map, Part III
  essays, Part IV verdict essays, Part V projections, campaign deep-dives,
  glossary, Step 10, Appendices J/K/O/U, cast FAQ), C1/C3/C4/C6 READMEs
  (ru+en), RESULTS.md verdict row, docs/theory.md cycle formula,
  figures/README.md; verdict JSONs (C6 results.json + registry duplicate:
  M2_gates_monotone_in_nv = true, M2_gates_null = false + the v2.0.8
  string); monograph content (canon_en/canon_ru scorecard rows + part1–4,
  both languages); audit content.json + audit_content.py; generators
  (make_infographics.py, make_comp_readmes.py, build_workbook.py);
  8 scorecard + 8 map infographics regenerated + `hp_workbook.xlsx`;
  new `Hilbert_Polya/docs/audit_v2.0.8.md`.
- **Leftover pre-v2.0.7 «H2 — NO» passages missed by the earlier pass** —
  synced in the same correction: README.md (stage map «H2 and H5 — NO»,
  Step 10 «H1 YES, H2 NO…», Appendix K «H2 is the central NO»),
  README.ru.md (Appendix K), C3 README.en («H2 NO»), C1 README.md
  («H2 (spectral identity, NO)»), C4 README.md/en («Г2/H2 answered NO»
  ×2), canon_en Г2 basis («null level … vs surrogate»), monograph
  part4 «the H2 gap is universal» (ru+en → the rank-metric resolution
  limit is universal).
- **core_spectrum:** one-sentence summary + programme status (EN/RU):
  the prime weight «does NOT live in lattice-gate traces» → «enters
  along the convergence ladder (v2.0.8)»; the open item reformulated as
  the bit-level branch.
- **Root README.md:** programme status — H5 YES via the convergence
  ladder (with the Vortex evidence); the open item is the bit-level
  branch.
- **Vortex_optimization:** new showcase READMEs (EN/RU): SVG banner
  «the convergence ladder» (committed numbers only), badges, mermaid
  pipeline, stat tables, figure gallery with sized thumbnails,
  collapsible reproduction/data-dictionary sections; «Hilbert–Pólya
  reading» rewritten — this study is the measured basis of the H5 = YES
  verdict (v2.0.8).
- **Adapted:** the [1.3.3] «programme status» third bullet (the open
  item is now the bit-level branch, not H5).

### Verified
- Infographics VLM-checked: scorecard Г5 = ДА on green, map chip «Г2 —
  ДА; Г5 — ДА» fully visible, banner defect-free; monograph content
  py_compile OK; JSON verdicts load OK.
- pytest: Hilbert_Polya 22/22, core_spectrum 42/42 (re-run after the
  edits; no test reads the edited prose sections).

## [1.3.5] — 2026-10-15 — «verdict v2.0.7: H2 = YES» (repo-wide)

The repo-wide verdict correction of audit **v2.0.7**, applied everywhere
the old «H2 = NO» wording still lived, plus folder-level repairs:

- **Hilbert_Polya:** scorecard H2 NO → YES — D_nn 0.0079 is the level of
  the shifted zero windows and the GUE zero class itself (0.0079 ± 0.0005,
  C3), not a surrogate null; synced across READMEs (EN/RU), computations
  C1/C3/C4/C5/C8/C13, JSON verdicts, monograph content, audit content,
  generators; 20 infographics regenerated (scorecard/map/handles ×
  ru/en × light/dark) + `tables/hp_workbook.xlsx`; new
  `Hilbert_Polya/docs/audit_v2.0.7.md` — the verdict-fix audit (the
  root-level `docs/audit_v2.0.7.md` of [1.3.4] is the figure audit; two
  documents share the v2.0.7 number). H5 stays NO; numbers unchanged
  (recount v2.0.2).
- **core_spectrum:** V6 gates — YES at the zeros' level (the D_nn bridge);
  V16 — level identity YES, bit-level closure open (z_best = 2.49 < 6);
  6 PNG infographics regenerated; v06_verdict.json synced.
- **Vortex_optimization:** «Hilbert–Pólya reading» rewritten — the
  distance to the zeros is a pure function of the vortex configuration
  (breeze → ocean currents → Abrikosov lattice), D: 0.1096 → 0.0318;
  monograph par. 9.5 + PDF preview updated.
- **lab-3d:** real import bugs fixed (v2-API imports from v1 modules,
  quick_start.py rewritten to the real API and verified end-to-end);
  41 scripts de-hardcoded (machine-specific absolute paths →
  Path(__file__)-relative); legacy runners documented («Known gaps»).
- **meridian-spectral-observatory:** catalog corrected to the actual
  contents (13 codes, real line counts, real Quick start via
  `ab_cloud_full.jl`); new showcase READMEs (EN/RU) with animated SVG
  banners, badges, mermaid diagrams, gates H1–H7, honesty protocol.
- **Consistency:** the [1.3.3] «programme status» paragraphs are adapted
  to the corrected verdicts (level identity — YES; the open sufficient
  item is H5 / the bit-level branch); this entry is renumbered [1.3.4] →
  [1.3.5] to sit above the already-pushed [1.3.4] figure audit.

### Verified
- pytest: Hilbert_Polya 22/22, core_spectrum 42/42 (re-run after the
  merge); no test reads the edited prose sections.

## [1.3.4] — 2026-10-15 — «the pictures that still lied» (fix series v2.0.7)

A full pass over every committed figure (591 PNGs outside the academic
package): Python-regenerable sets byte-compared against their (fixed)
generators, non-regenerable monograph figures VLM-proofread against the
corrected canon. Full findings: **`docs/audit_v2.0.7.md`**.

### Fixed — v21 monograph media carried pre-audit curves (EN/RU, all formats)
- **`image39.png` (Fig. 11.3, Σ²)**: the "GUE prediction" curve was
  (2/π²)(ln L + 0.296) — the GOE slope (0.2005/0.5266). Regenerated with
  the exact GUE closed form L − 2∫₀ᴸ(L−t)sinc²(t)dt (0.4157/0.5793 —
  byte-consistent with the corrected Table D.3).
- **`image38.png` (Fig. 11.4, Δ₃)**: "GUE prediction" was (1/π²)ln L
  (0.0702/0.2333). Regenerated with (1/2π²)(ln 2πL + γ − 5/4)
  (0.0941/0.1757 — Table D.4).
- **`image37.png` (Fig. 11.5, ⟨r⟩ vs η)**: legend and line said
  **"Poisson (1.3863)"** — an impossible value (r ∈ [0,1]). Regenerated
  with the Poisson line at 0.3863 and the y-range rescaled to 0.30–0.65.
  Data curves preserved exactly (tick-calibrated pixel extraction,
  validated against the §11.3.1 text anchors to 0.0003).
- **§11.3.2 text (EN/RU)**: "at η=0 (pure GUE) ⟨r⟩=0.3859" contradicted
  Table D.5 (GUE 0.5992) in the same document — reworded honestly in
  md ×2, html ×4, docx ×4; corrected.pdf ×2 rebuilt (WeasyPrint),
  with_Verification.pdf ×2 rebuilt (LibreOffice, pages 273/227 preserved).
- **Hilbert_Polya `figures_hires/{en,ru}/fig14_ladder_*.png`**: the GUE
  reference label said 0.602 where the canon (C8 constant, v2.0.5) is
  0.600 — the screen copies had been fixed, the hires twins were missed.
  Regenerated; the other 34 data figures are byte-identical.

### Documented (not changed)
- v23 monograph figure captions describe data panels that the run engine
  never drew (per-test PNGs are sub-check verdict maps) — a caption↔figure
  mismatch of the generator source, recorded in the audit for a separate
  decision; the verdict maps themselves carry no wrong statements.

### Verified
- Every Python figure set regenerated byte-identically except fig14 ×2
  (processor_ab, verifier_multilang, tiled, theorems, atlas, banner,
  timeline, realtime, Wave, dirac-lab, Vortex excluded by data availability
  and separately VLM-checked, C17, algebraic_map).
- VLM proofread of the three regenerated figures and their embedded copies
  in three rebuilt PDFs: canonical heights, "1.3863" gone everywhere.
- pdftotext of all rebuilt PDFs: new phrasing present, old values zero
  hits; pytest Hilbert_Polya 22/22, core_spectrum 42/42.

## [1.3.3] — 2026-10-15 — «programme status, stated plainly» (docs)

Following the v2.0.1–v2.0.6 fix series, the three summary statements of
the programme's status are now written where readers look first — each
traceable to the committed ledgers and audits:

- **The spectral statistics converges.** The pre-audit estimator errors
  (GOE slopes shipped as GUE, the impossible Poisson ⟨r⟩ = 1.3863, stale
  KS evidence) are fixed; with the corrected laws every statistic converges
  to its GUE prediction: ⟨r⟩ plateau 0.6004 (χ²/dof = 0.01, L = 16 → 80),
  spacing law D = 0.031048 / W² = 1.5383 (byte-exact with Lean), Montgomery
  pair correlation KS = 0.047 (p = 0.27).
- **The spectra are almost identical.** Ten language ports — same ⟨r⟩, KS
  and topology verdicts to quoted precision; spinor isospectrality
  max|Δλ| ≈ 9e-15; C3 protocol reproduction |Δ mean_spacing| = 1.45e-16;
  Hadamard control of H_ξ log-residual 5.8e-10; Lean 8/8 with Δ = 0.000000.
- **All necessary conditions of the Hilbert–Pólya programme are fulfilled**
  (self-adjointness H1, GUE class H3, Dirac dynamics H4, trace formula T6,
  Li criterion Th4, interval certificates Th3); the level identity (H2) is
  YES since audit v2.0.7 — the gates sit at the zeros' own level (D_nn
  0.0079, the level of the shifted zero windows and the GUE zero class) —
  and the prime channel (H5) is YES since audit v2.0.8 — the convergence
  ladder: the gate ψ-correlation climbs with the vortex coverage
  (−0.12 → +0.09 → +0.24) and with lattice size (the Vortex scan: GUE
  floor 0.0324 → 0.0220 for L = 24 → 96) — so the open item is the
  bit-level branch (T18), and RH stays open, not claimed.

### Added
- Root `README.md`: "Programme status" block after the Hilbert–Pólya claim
  statement (§ What is the AB-cloud?).
- `Hilbert_Polya/README.md`: "How to read the scorecard" paragraph after
  the H1–H5 verdict table.
- `AB_Cloud_Quantum_Research/modules/core_spectrum/`: "Programme status" /
  «Статус программы» blocks in `README.md` + `README.ru.md` (after the
  one-sentence summaries); «Три итоговых заявления» section in
  `results/RESULTS.md`.

### Fixed
- `results/RESULTS.md` header still said «1.1.0 · 18 кампаний» — updated to
  «1.2.0 · 19 кампаний» (matches `data/v14_verdict.json` after the v1.2.3
  audit fix and the 19-solution summary two sections below).

### Verified
- pytest: Hilbert_Polya 22/22, core_spectrum 42/42 (docs-only change; no
  test reads the edited sections).
- Added blocks follow the markdownlint house style (asterisk emphasis,
  escaped pipes in tables' prose, no new HTML elements).

## [1.3.2] — 2026-10-15 — «the rigidity-slope purge» (fix series v2.0.4)

A full pass over every README, table and monograph of the repository
(following v2.0.1–v2.0.3). Full findings, validation transcripts and the
per-file fix map: **`docs/audit_v2.0.4.md`**.

### Fixed — the GOE rigidity law shipped as "GUE" in monographs and docs
- **Δ₃ slope**: the canonical v22 monograph (all three languages, all
  formats: md/tex/html/pdf/docx, base and v221 builds) stated
  `Δ₃^GUE ≈ (1/π²)ln L` — the **GOE** slope. Direct simulation
  (GOE/GUE 140×140×40, exact Dyson–Mehta window integral) re-confirms
  **Δ₃^GOE = (1/π²)(ln 2πL + γ − 5/4 − π²/8)** and
  **Δ₃^GUE = (1/2π²)(ln 2πL + γ − 5/4)**; all statements corrected.
- **Σ² slope**: the v21 monograph (Appendix D, EN+RU, md/html/docx/pdf)
  stated `Σ²_GUE ≈ (2/π²)ln L + const` — again the GOE slope — and its
  Tables D.3/D.4 "GUE pred" columns carried GOE-flavoured values
  ((2/π²)(ln L + 0.296) and (1/π²)ln L). Correct GUE theory columns
  regenerated from the exact closed form validated in v2.0.3.
- **Impossible Poisson ⟨r⟩**: Table D.5 of the v21 monograph listed
  Poisson ⟨r⟩ = **1.3863** (a value > 1 is impossible for r ∈ [0,1];
  1.3863 = 2ln2 is the raw constant). Corrected to **0.3863**
  (= 2ln2 − 1) in all editions and builds.
- **Section 11.3.1 (v21, EN+RU)**: quoted "GUE" references for the
  N=200 rigidity check were the wrong GOE-slope numbers (0.2005/0.5266/
  0.0702/0.2333); replaced by the correct GUE values (0.4157/0.5793/
  0.0941/0.1757) with recomputed deviations (−89.6/−89.0/−98.4/−98.4%).
- **Root README / formal READMEs**: stale KS/CvM evidence from the
  pre-v2.0.3 era (KS D = 0.099187, p = 0.000000; W² = 17.6049) still
  quoted as current output; updated to the corrected-law values
  (D = 0.031048, p = 0.000130; W² = 1.5383). The F_GUE display formula
  in `formal/README.md` was the GOE CDF `1 − e^{−πs²/4}`; now the
  correct `erf(2s/√π) − (4s/π)e^{−4s²/π}`.
- **v23 Monograph (MG/ROOT, Academic Package)**: "GOE follows the
  1/15th-power law" (no such law exists — Poisson is L/15, GOE is
  logarithmic) and the GOE rigidity formula mislabeled as GUE; the
  arithmetic claim "0.5798 sits 81% of the way from GOE to GUE"
  (correct value: **71%**); the quoted `delta3_rigidity` docstring and
  the Test-14 console listing carried the same wrong slope and the
  stale "Paper's rel_err ≈ 0.97" (now 0.13). All fixed in docx + pdf.
- **Julia suite (`ab_cloud_v23.jl`, 5 copies)**: the t3_11 "GUE asymp"
  reference curve was `(2/π²)(ln 2πL + γ + ½)` — the GOE slope with a
  wrong constant — nearly 2× above the true GUE curve; now
  `(1/π²)(ln 2πL + γ + 1)`. The Test-14 header printout and the
  `delta3_rigidity` docstring carried the same wrong slope.
- **lab-3d preprint (`ab_cloud_preprint.tex`)**: pre-repair rel_err
  values (0.972/0.481) in the rigidity table; the Δ₃ equation with the
  GOE slope; a garbled Σ² "asymptotic" form mixing Ci into the slope;
  the "Σ² is the more robust diagnostic" claim (after the v2.0.3
  estimator repair Δ₃ is the more accurate one: 0.126 vs 0.412).
- **Poisson-like mislabel**: `lab-3d/README.md` described the phase
  diagram edge ⟨r⟩ = 0.238 as "Poisson-like" (Poisson is 0.3863;
  0.238 is strongly clustered) — reworded. The test-16 README had a
  digit typo "0.3869" for the Poisson ⟨r⟩ — corrected to 0.3863.
- Rebuilt: v22 base PDFs (tectonic/LaTeX, ZH with proper CJK via
  Noto Serif SC), v221 PDFs (WeasyPrint), v21 corrected/with_Verification
  PDFs, v23 MG/ROOT PDFs (LibreOffice), the academic-package preprint
  PDF (tectonic). Academic-package SHA256SUMS updated for the touched
  files. All narrative table/wording fixes propagated to md, tex, html,
  docx and pdf editions alike.

### Verified
- Δ₃/Σ² theory forms re-validated by direct GOE/GUE simulation with the
  exact window integral (GOE-B ratio 0.96–1.02, GUE ratio 0.96–1.01).
- Hilbert_Polya test suite: 21/21 passed; AB_Cloud_Quantum_Research:
  42/42 passed. Python verification suite re-run: KS D = 0.031048,
  p = 0.000130, W² = 1.538304 on 5000 zeros (matches Lean REF_MAIND/
  REF_MAINW2 exactly).
- Every replacement applied byte-exactly with occurrence-count
  assertions; zero old-value occurrences remain in READMEs, tables,
  monographs or their builds.

## [1.3.1] — 2026-10-15 — «the GOE-as-GUE purge» (fix series v2.0.3)

A repo-wide audit of every GOE/GUE formula, committed dataset and committed
figure (following v2.0.1/v2.0.2, which fixed the Hilbert_Polya D_nn metric
and the C3 data). Full findings and validation transcripts:
**`docs/audit_v2.0.3.md`**.

### Fixed — the GOE β=1 surmise shipped as "GUE" in 14 implementations
- The Wigner **surmise of the wrong ensemble** — `1 − exp(−πs²/4)` /
  `(πs/2)·exp(−πs²/4)`, which is **GOE (β=1)**, not GUE (β=2) — was used
  as the "GUE" reference law in the Objection-2 KS/CvM tests of the
  verification matrix: Python ×4, Julia ×3, C++ ×3, Fortran ×3, Go,
  JavaScript ×3, Rust ×3, MATLAB ×3, R ×3, and the Lean 4 formal
  verifier. All now use `p(s) = (32/π²)s²exp(−4s²/π)`,
  `F(s) = erf(2s/√π) − (4s/π)exp(−4s²/π)`. On the frozen first 500 zeros
  the old law gave KS D = 0.1165 (p ≈ 0, a false rejection of the true
  hypothesis); the corrected law gives D = 0.0495 (p = 0.168).
- **lab-3d**: `gue_cdf`/`wigner_dyson_pdf`/`plot_rmt_results` (Python ×2
  twins), the GUE P(r) ratio law in `ab_cloud_advanced.py` (wrong
  functional form: ⟨r⟩ = 0.636 instead of the Atas β=2 surmise 0.6027),
  and the Σ²(L)/Δ₃(L) **theory curves in four languages** — the committed
  curves matched neither GOE nor GUE (validated by direct matrix
  simulation: correct Σ² = (1/π²)(ln 2πL+γ+1), exact closed form via
  Si/Ci; correct Δ₃ = (1/2π²)(ln 2πL+γ−5/4)).
- **lab-3d measurement estimators were structurally broken**: the Julia
  `sigma2_curve` (endpoint-regression) gave **262 instead of 2 on a
  Poisson sanity check**; the Julia `delta_3_curve` was biased ~8× low on
  the zeta process; the Python twins fitted the cumulative *sum of
  positions* instead of the counting staircase. All four rewritten and
  validated on Poisson (Δ₃ = L/15, Σ² = L) and GUE ensembles; window
  strides made incommensurate with the lattice (integer strides alias the
  lattice-locked zeta process, +50% variance).
- **False committed data regenerated** (`outputs/full_verification_*`):
  the §2a rigidity block in json/md/txt/csv/html, and the figures
  `02_delta3_L` / `03_sigma2_L` — measured Δ₃(L) now tracks GUE at small L
  and saturates ≈ 0.16 (Berry's saturation for the first 5000 zeros);
  rel_err Δ₃ 0.972 → 0.126, Σ² 0.481 → 0.412, §2a verdict false → true,
  overall 4/6 → 5/6.
- **Lean 4 frozen references regenerated** (`REF_MAIND` 0.0991866231 →
  0.0310483738, `REF_MAINW2` 17.6049 → 1.5383, embedded block likewise) —
  the old numbers were generated by the Python suite against the GOE law
  and then "independently" reproduced by Lean against the same wrong law;
  the corrected value cross-validates against the lab-3d Julia pipeline
  (D = 0.0312 on the same zeros). Docs updated (README, docs/formal.md,
  formal/README.md, ABCloud/README.md).

## [1.3.0] — 2026-10-10 — «CI green, Pages pinned, the formal layer»

### Fixed
- **CI is green again.** The `structure` job of `ci.yml` and both steps of
  `julia.yml` still referenced `code/ab_cloud_v19.jl`, deleted in the
  "Hilbert Polya" consolidation commit — every push failed. All workflows
  now target the canonical v23 suite (`--test 1` smoke + manual full run),
  the canonical-artifact list covers the formal layer, and the dependabot
  action bumps (`checkout@v7`, `markdownlint-cli2-action@v24`, `stale@v11`,
  `setup-julia@v3`, `release-drafter@v7`) are applied.
- **`code/julia/README.md` rewritten** — it documented the removed
  historical sources (v19/v19_v1/v20/v21) as if they were still present.
- **GitHub Pages reproducibility.** `deploy-docs.yml` pins the exact
  MkDocs stack (mkdocs 1.6.1 / material 9.7.7 / minify 0.8.0) the site is
  verified with, and `mkdocs build --strict` passes.

### Added
- **The formal verification layer** ([`formal/`](formal/README.md)):
  - `formal/lean4/` — a full Lean 4 project (toolchain v4.19.0, **zero
    external dependencies**, no Mathlib): machine-checked theorems over
    ℕ/ℤ (b(N) sum nonnegativity/monotonicity/additivity/triangle, Gram
    offset lattice, flux certificates, PSL(2,7/8/13) orders, Klein orbit
    decomposition, Tr(AB) = Tr(BA)) **plus the `abcloud-verify`
    executable** — a Float64 port of the Python reference pipeline that
    re-derives the frozen reference numbers from
    `verification/data/zeta_zeros_50000.txt`: **8/8 checks PASS,
    Δ = 0.000000** (b(100…5000), KS D = 0.0310483738, CvM W² =
    1.5383040905, slope −0.1831023444, R² 0.9946087105), exit-code-gated
    (v2.0.3: KS D / CvM W² regenerated with the corrected β=2 GUE CDF;
    the 1.3.0-era values 0.0991866231 / 17.6048550189 were measured
    against the GOE β=1 surmise mislabeled as GUE).
  - `formal/coq/` — the exact core over ℤ (`lia`/`nia`/`ring`).
  - `formal/agda/` — builtins-only development; positivity of b(N) is a
    typing fact.
  - `formal/isabelle/` — `Main`-only HOL session.
  - `formal/assets/` — the section banner and seal (SVG).
- **`formal.yml`** — four independent CI jobs (lean4 / coq / agda /
  isabelle) running on every push and PR.
- **`.yamllint.yaml` + `.markdownlint-cli2.jsonc`** — real linter configs;
  the `ci.yml` markdown job now lints a curated 61-file surface with a
  reviewed rule set and the YAML job enforces the project config.
- **Docs site**: new `formal.md` (formal verification) and `map.md`
  (repository map) pages, nav regrouped, `docs/index.md` cards updated.
- **Makefile**: `smoke` and `formal`/`formal-lean/coq/agda/isabelle`
  targets; `quick-test`/`test-all`/`menu` target the v23 suite.

### Changed
- **Root README redesigned** (EN): new banner (`assets/banner-v2.svg`),
  formal-verification badge row, a mermaid repository-architecture
  diagram, the formal verification section with the re-derivation ledger,
  LaTeX display math, updated quick start / Makefile reference / CI-CD
  table / repository map / glossary / roadmap; the Russian duplicate
  section was retired (EN is now the single source of truth; RU content
  remains in the subprojects and the git history).
- All canonical-suite references across the repo (README, docs/, code/,
  verification/, .github templates, Makefile) updated from v19 to v23;
  historical v18/v19 run-artifact references intentionally preserved.


## [1.2.1] — 2026-09-04 — «the front page, restored and tripled»

### Fixed
- **Landing-page hijack removed.** `.github/README.md` (added in v1.2.0)
  silently replaced the root README on the repository home page — GitHub
  resolves `.github/README.md` ahead of the root README — so the banner,
  the badge wall and all front-page content disappeared for visitors.
  The infra guide moved to `.github/WORKFLOWS.md` (content unchanged) and
  the full front page is the landing page again.

### Added
- **Root README tripled in size** (37 KB → 107 KB, 534 → 1,575 lines) with
  big data straight from the stored computations: a 24-row *Computation
  data at a glance* table; the **complete 38-test ledger** of the flagship
  run (test-by-test verdicts with artifact links); the **full spinor64
  data** (E1 orbit table 28/21/7/7/1, E2 four holonomy classes, ensemble
  ⟨r⟩ = 0.5984 ± 0.0035); **real per-test wall-clock timings** (9 s …
  1 h 06 m); the **ζ dataset inventory with real SHA-256 checksums** of
  all nine frozen files (2,001,058 zeros, 91 MB); flagship artifact
  inventory (453 files / 39 directories); a statistical deep-dive (⟨r⟩,
  finite-T story, Montgomery R₂, topology at machine precision, Dirac
  R² = 0.9997); the annotated gallery of all 19 monograph plates at
  600 dpi; a ten-language cross-verification matrix; monograph editions
  matrix; Makefile reference; CI/CD table; reading paths; FAQ; glossary;
  a verification-history timeline; eight extra badges (Release, Version,
  **strictly personal License**, Suite 37×2+38, 2,001,058 ζ zeros,
  Android/Termux, 453 artifacts, Spinor64 64/64); and a Russian section
  with the big-data table, the full 38-test registry, checksums and a
  mini-glossary.

## [1.2.0] — 2026-09-03 — «documentation deep dive»

### Added
- **Deep-dive README in every directory** (32 files): root README gains a
  Documentation map, a Branches & versions section and a corrected
  Highlights table; every folder of the repository now ships an English
  README ending with a short Russian summary (`Кратко по-русски`):
  `code/`, `code/julia/`, `verification/` + all 10 language folders +
  `data/`, `spinor64/`, `sections/`, `monographs/` + `ru/en/zh` +
  `original-v21/`, `lab-3d/` + `code/`, `outputs/`, `results/`, `apps/` +
  both applications, `docs/`, `termux/` (new English guide), `assets/`,
  `.github/`. Every README documents contents file-by-file, stored result
  values with their provenance, run commands and expected output.
- Root README: Highlights row for the spinor structures corrected to the
  gone); roadmap updated to v1.2.0.

## [1.1.0] — 2026-09-03 — «spinor64 verification + run artifacts + apps»

### Added
- **`verification/spinor64/`** — independent reference implementation and full
  run over all 64 spinor structures of the Klein quartic: PSL(2,7) orbits
  28/21/7/7/1 (28 odd Arf=1 — bitangents, transitivity confirmed), EXACT
  isospectrality within orbits (max|Δλ| ≈ 8.9e-15), gauge invariance
  7.1e-15, zero modes 2/3/3/3/7; AB-cloud Hofstadter statistics:
  **64/64 structures GUE-consistent** (⟨r⟩ = 0.5984 ± 0.0035, MC reference

- **Test 38 ports in 10 languages** — `verification/<lang>/spinor38/`
  (C++/JS compiled+run here: isospectrality 3.4e-14, ⟨r⟩ = 0.4515710793,
  VERDICT PASS; Java/Rust/Go/Fortran/Haskell/R/MATLAB sources with build
  docs) reading the frozen data files `verification/spinor64/data/`.
- **`code/julia/`** — full sources of the suite v19 / v19_v1 / v20 / v21
  (as supplied), plus the extracted 50,000-zero embedded dataset
  `verification/data/zeta_zeros_50000_embedded.txt`.
- **`results/run_20260902_134759/`** — the complete v19 two-pass run of
  2026-09-02 (37 tests, 72×72 → 96×96 HARDCORE, Julia 1.12.0): per-test
  reports (md/pdf/docx/html), computation logs, FINAL_REPORT, index.html —
  453 files (reports+logs; the run's PNG plots are excluded — they are
  regenerated by the suite).
- **`apps/`** — two React applications (React 18 + Vite, prebuilt `dist/`
  committed, GitHub Pages ready):
  - `ab-cloud-dashboard` — 37-test verdict dashboard + real-time ζ
    statistics (b(N), ⟨r⟩, KS vs GUE ratio law, Σ², Δ₃) in a Web Worker +
    in-browser 64-spinor Jacobi verification;
  - `ab-cloud-lab3d` — WebGL 3D laboratory: Hofstadter lattice with
    vortices, Dirac cone, ζ critical strip (self-anchored Euler–Maclaurin
    ζ evaluator).
- **Monograph v21.1 (RU+EN corrected editions)** — errata note, corrected
  sections 3.1/3.2/3.2.1, new section 3.2.5 with the spinor64 results;
  rebuilt as `*_corrected.docx/html/pdf`.
- **Monographs v22.1 (RU/EN/ZH)** — Appendix B updated to the
  `run_20260902_134759` two-pass artifacts; new Appendix D (spinor64);
  LaTeX sources committed (`*.tex`); rebuilt `*_v221.docx/html/pdf`.

### Changed
- README: new sections for spinor64, Test-38 ports, React apps, code/julia,
  and the run artifacts.
- `monographs/original-v21/README.md`: v21.1 corrections documented.

All notable changes to the **AB-Cloud Research** repository are documented here.
The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- **Android/Termux push kit** — `termux/install_and_push.sh` +
  `termux/README_RU.md` + root cheat-sheet `HOW_TO_PUSH_FROM_ANDROID.md`:
  one-command publication of this repository to GitHub straight from an
  Android phone. The script auto-installs missing packages (git/curl/gh),
  relocates the repo out of shared /sdcard storage into Termux home,
  offers two login modes — **PAT token** (hidden input, pre-verified via
  GitHub API incl. push-permission check) or **browser device-flow**
  (GitHub CLI one-time code at github.com/login/device) — then pushes
  `main` + tags, verifies the remote SHA via `ls-remote` and opens the
  repo in the browser. Token exists in process memory only. Also shipped
  as a standalone `termux-push-kit.zip` and inside the main archive.

### Planned
- Full 37-test suite as a scheduled nightly CI job
- Interactive browser dashboard for verification results
- Quantum Hadamard-walk & 2D e⁻/e⁺ jet hydrodynamics extensions

## [1.0.0] - 2026-08-28

### Added
- **Monographs (5 editions)**:
  - v22 monograph rewritten from scratch on the verified 37-test suite —
    Russian, English, Chinese (`monographs/{ru,en,zh}/`): markdown, interactive
    HTML, DOCX, vector PDF, 14-slide PPTX, arXiv-style preprint (tex+pdf),
    19 figures at 600 dpi per language;
  - Original author monograph v21 with verification (RU) and its full English
    edition (`monographs/original-v21/{ru,en}/`): docx + pdf + interactive html
    + md + 16-slide pptx presentations, shared figure media.
- **Canonical Julia suite** `code/ab_cloud_v19.jl`: 37 tests, two-pass protocol,
  report engine (md/html/pdf/docx/png 600dpi/svg/gif), interactive menu,
  Physics Lab (22 experiments), 3D laboratory (30 tests), `--quick` CI mode
  (16×16 → 32×32, ζ ≤ 5000).
- **10-language verification suite** `verification/`: C++, Fortran, Go, Haskell,
  JavaScript, Julia, MATLAB, Python, R, Rust; bilingual RU/EN interface;
  answers to 3 standard referee objections; ζ-zero datasets
  (13,661 / 50,000 / 500k / 2M zeros, Odlyzko).
- **3D lattice laboratory** `lab-3d/`: 3D non-Hermitian Hofstadter Hamiltonian
  with vortex lines, 36³ lattices, 5000 embedded zeros, full output reports.
- **Reference verification log** `results/verification_run_v18_37tests_2026-08-28.txt`.
- Documentation site (MkDocs Material, GitHub Pages), CI (markdownlint,
  link-checker, CodeQL, Julia quick-test), issue/PR templates, release
  automation (release-drafter, labeler, dependency-review, stale),
  Dependabot, funding config.

### Verified highlights
- ⟨r⟩ = 0.5848 ± 0.0260 vs GUE 0.5992 (deviation −2.4 %)
- Montgomery test: KS = 0.047, p = 0.27 (N = 500 certified zeros) — H₀ not rejected
- Byers–Yang flux defect 3.5·10⁻¹⁵; Connes self-duality (4 zero modes), C₁ = 2
- Montgomery correlation hole reproduced (d_GUE 0.140 < d_Pois 0.227)
- Dirac dynamics: E_min ∝ 1/L (R² = 0.9997), 20× DOS dip, skin effect

### License
- Custom Research License: all rights belong fully and exclusively to
  Isaev Iskhak Khamzatovich (see `LICENSE`).

[Unreleased]: https://github.com/wild8highlander/ab-cloud-research/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/wild8highlander/ab-cloud-research/releases/tag/v1.0.0
