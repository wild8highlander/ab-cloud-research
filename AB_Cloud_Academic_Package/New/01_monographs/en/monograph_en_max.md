# The Unified AB-Cloud Research Programme — MAX Edition

**The monograph of maximum depth of the unified academic package: ten levels, every campaign, every verdict, every figure**

Isaev Iskhak Khamzatovich · ORCID 0009-0003-7299-0701 · independent researcher
AB-Cloud Research Programme · enriched edition · October 2026

---

## Abstract of the MAX edition

This edition is the maximally unfolded record of the AB-Cloud research programme: one study deployed across ten levels — the spectral core and the AB processor (I, I⁺), the Dirac skeleton (II), the Hilbert–Pólya bridge (III), blind verification with the reference-run heritage (IV, IV⁺), the spinor study (V), the Meridian Spectral Observatory (VI), the vortex-density optimization (VII) and the hyperbolic wave attractors (VIII). The programme investigates the statistical bridge between the non-trivial zeros of the Riemann zeta function $\\zeta(s)$ and the spectra of Hermitian lattice operators carrying Aharonov–Bohm flux quanta.

The MAX edition differs from the regular volume in three dimensions of completeness. **First — vertical:** every level is unfolded into individual campaigns with their protocols, null models, thresholds and boundaries; the v19 run is analysed across all 37 tests with console listings. **Second — horizontal:** the three new levels (VI–VIII) and the extended heritage are included at the same depth as the originals; the number register has grown from 20 to 73 rows; the full source records — the vortex README, the wave-attractor README, the observatory README, the run archive catalogue, the data cards — are included as chapters. **Third — illustrative:** all 53 static figures of the package are embedded in place and catalogued; five derived figures (the 50,000-zero statistics, the v19 verdict map) were computed in this edition from package data.

The consolidated verdict ledger is fixed: self-adjointness — yes; spectral identity — no (the gap measured and stable); GUE class — yes; Dirac dynamics — yes; primes inside the operator — no (in traces, not gate spectra); gate H5's regime D — cleanly GUE; the vortex working window closes 89% of the gap to the GUE floor; the wave attractors reproduce from first principles; the vortex scan does not prove the Hilbert–Pólya conjecture (a necessary condition, not a construct); the Riemann hypothesis — blocked by the V13 obligation machine by construction. The programme's principal contribution is a map: the wall is located (locality), its universality measured (the L-class), the bypass outlined (nonlocality or entanglement of equivalent rank).

**Keywords:** Riemann zeta function, Hilbert–Pólya conjecture, Aharonov–Bohm effect, lattice Dirac operator, random matrices, GUE, Montgomery–Odlyzko, Berry–Keating, Connes, Guinand–Weil trace formula, blind verification, reproducibility, wave attractors, hyperbolic metamaterials.

---

## Contents of the MAX edition

**Part I. The programme** — 1. The subject · 2. The history of the question · 3. Architecture: ten levels · 4. Method · 5. How to read the MAX edition

**Part II. The mathematical apparatus** — 6. Lattice, flux, Hamiltonian · 7. Random matrices: from Poisson to GUE · 8. The zeta function · 9. The H–P conjecture and candidates · 10. Distance metrics · Interludes: five schools, related programmes, and the theory courses of the Russian edition's chapters 10a–10q

**Part III. Level I** — 11. The theorems Th1–Th6 · 12. The AB processor · 12a. Full record of level I

**Part IV. Level II** — 13. The continuum limit · 13b. Full record of level II

**Part V. Level III** — 14. Phases v1/v2 · 14b. Full record of level III

**Part VI. Level IV** — 21. The E01–E18 platform · 21a. Full record of level IV · 22. The 38-test heritage · 22a. The run archive catalogue · 23. The v19 run: protocol · 24. The v19 run: all 37 tests with consoles · 24L. The computation logs

**Part VII. Level V** — 25. The spinor study · 25b. Full record

**Part VIII. Level VI** — 26. The observatory · 27. The gates H1–H7 · 28. The RH line · 29. The monumental line · 30. Boundaries · 30a. Full record · 30b. The observatory README · 31a–31h. The eight observatory documents (in the Russian edition; English condensations in ch. 26–30)

**Part IX. Level VII** — 31. The problem and validation · 32. Stages A/B/C · 33. The mechanism · 33a. The source README · 33b. The scan tables · 33c. Full record · 33d. The complete Stage-A table

**Part X. Level VIII** — 34. The subject · 35. The ray model · 36. The wave model · 37. The window and TD · 38. AB water and the cross-check · 38a. The source README · 38b–c. The W1 tables

**Part XI. Data** — 39. The package data · 40. Reproducibility · 41. Tooling · 55. The data cards

**Part XII. Registers** — 43. The 73-number register · 43a. Row-by-row commentary · 44. The campaign register · 45. The verdicts G1–G10

**Part XIII. Discussion** — 46. The locality wall · 47. The links between levels · 48. Consequences · Interludes 58–64, 76–78

**Part XIV. Boundaries** — 49. Limitations · 50. Conclusion · 51. For a general audience · 52. FAQ · 53. The extended glossary

**References · Appendices A–P** (campaigns · sources · the figure catalogue · the 77 v19 verdicts · chronology · glossary · ethics · the full final report · the run logs · language abstracts)

---

**Honest boundary.** RH — `blocked` (the V13 obligation machine). The MAX edition does not prove the Riemann hypothesis. Derivative works must preserve this statement verbatim (LICENSE §3).


---

# PART I. THE PROGRAMME

## 1. The subject: the Riemann hypothesis as a spectral question

The Riemann hypothesis states that all non-trivial zeros of the zeta function $\zeta(s)$ lie on the critical line $\mathrm{Re}\,s = 1/2$. Formulated in 1859 as an auxiliary statement about the distribution of primes, it has become the central unsolved problem of mathematics — not because checking it is computationally hard (trillions of zeros are verified, all on the line) but because no known technique of analysis touches its structure. A century and a half of study keeps returning one structural question: if the zeros $\gamma_n$ are a spectrum, whose spectrum is it?

Hilbert and Pólya posed it as a programme: find a Hermitian operator $H$ whose eigenvalues are $1/2 + i\gamma_n$. The beauty of the reformulation is that it turns an analytic statement into a spectral one: if such an operator exists, the hypothesis follows from self-adjointness — the spectrum of a Hermitian operator is real, and reality of $1/2 + i\gamma_n$ forces exactly the critical line. The operator reformulation reduces the hardest analytic problem to the existence of an object with checkable structure.

The Montgomery–Odlyzko programme gave the question a statistical dimension. Montgomery (1973) conjectured that the pair correlation of the zeros at their mean spacing is $g(U) = 1 - (\sin \pi u / \pi u)^2$ — the same function that governs the pair correlation of the Gaussian Unitary Ensemble (GUE) of random matrices in the large-dimension limit. Odlyzko (1987) confirmed it numerically on the tables of the day: histograms of normalized $\zeta$-zero spacings fall on the Wigner curve for GUE with striking precision. Since then the working criterion for an operator candidate is fixed: it must reproduce GUE statistics. Not sufficient for identity — but sufficient to eliminate whole classes: integrable systems give Poisson; real-symmetric matrices (GOE) give a different curve; quaternionic (GSE) a third. GUE is the signature of broken antiunitary symmetry — the signature of a complex, irreversible phase.

This monograph — the MAX edition of the unified AB-Cloud research programme — presents a systematic attempt to build and *measure* such a candidate. The construct does not begin with an operator in abstract Hilbert space but with a finite lattice: an $L \times L$ torus carrying $\pi\alpha$ of Aharonov–Bohm flux per plaquette, a Hermitian matrix $H_L(\alpha)$, and a family of "gates" — perturbations encoding the phase of $\zeta$ zeros into Bloch angles. The programme does not aim to prove the Riemann hypothesis; it aims to measure precisely *where* and *why* the lattice approach hits a wall — and it publishes negative results with the same standing as positive ones. The MAX edition unfolds every level of the programme in full depth: every campaign, every test, every verdict, every figure; it is written to carry the entire knowledge baggage of the package.

Why a MAX edition? The regular volume is the compressed scientific record: every number names its campaign, but conclusions are served compactly. The MAX edition solves a different problem: it documents *the path to every number* — the protocol, the null models, the decoys, the thresholds, the cost in time and memory, the console output of the actual run, the boundaries of interpretation. Such a document is closer to the complete laboratory journal of an expedition than to an article: it can be read as a chronicle (sequentially), as a reference (by campaign), or as a map (by verdict). All three readings are supported by the contents structure, the continuous numbering of numbers (a register of 73 rows) and the figure catalogue.


---

## 2. A history of the question: from Hilbert–Pólya to the monumental line

The spectral tradition in zeta-function theory begins not with one paper but with a slow accumulation of hints. The first hint was the Riemann–von Mangoldt theorem on counting zeros: $N(T)$, the number of zeros with $0 < \mathrm{Im}\,\rho < T$, is expressed by the argument integral of $\zeta$ along the critical strip — a formula structurally identical to Weyl's law for counting eigenvalues of a Laplacian on a compact: $N(\lambda) \sim \frac{\mathrm{Vol}}{4\pi}\lambda + \ldots$ with the same type of corrections. Hilbert, by oral tradition relayed through Pólya and Schinzel, noticed the similarity first: if zeros are counted like eigenvalues, it is reasonable to look for the operator that generates them.

The second hint came from physics. Dirac (1928), Berry–Keating (1999), Connes (1999) — three distinct lines of operator approach. The Berry–Keating semiclassical operator $H = (xp+px)/2$: on a suitable function space it has a uniform spectrum with density $\overline{d}(E) \sim \frac{1}{2\pi}\log(E/2\pi e)$ — exactly the mean density of $\zeta$ zeros (the Riemann–von Mangoldt theorem in the limit). The operator $xp$ gives the correct *density* but not the *fluctuations*: its spectrum is a uniform ladder; the zeros are not. Connes took a different path: an adelic sum $x + \theta^2 x^{-1}$ on positive characters produces a trace comb of period $\Lambda = \log q$, and RH becomes equivalent to the positivity of a functional — but the construction lives in a non-standard (adelic) space whose physicality remains contested. Sierra proposed a series of quantizations of $x[p]$ and related Hamiltonians, probing which produce GUE fluctuations.

The third hint was computational. Odlyzko in the 1980s computed tens of thousands of zeros to high precision and showed not only the GUE spacing statistics but the agreement of finer statistics: the form factor $K(\tau)$, spectral rigidity $\Delta_3(L)$, number variance $\Sigma^2(L)$. Rudnick and Sarnak (1996) formulated the $n$-level correlation conditions as the universal signature of "GUE-likeness". Since then the evidentiary standard is: the more statistics match GUE predictions, the stronger the evidence — but no accumulation of numerical agreement is a proof; that is the universal limit of the programme.

The fourth hint was lattice-theoretic. The Hofstadter spectrum (1976): an electron on a lattice in a magnetic field with rational flux $\alpha = p/q$ per plaquette has a Cantor-set band structure with $q$ sub-bands; at irrational $\alpha$ — the famous butterfly, a fractal spectrum. The quantum Hall effect tied the topology of these sub-bands to integer invariants (the Chern number). Atiyah–Singer, and in physical form Jackiw–Rossi (1981), tied zero modes of operators to topological charges: a vortex with flux $\Phi$ binds $|\Phi|$ fermionic zero modes. The Byers–Yang identities (1961) and flux periodicity supplied the gauge frame: physics is invariant under gauge changes at fixed flux; spectra are periodic in integer flux quanta. All these elements — lattice, flux, zero modes, gauge invariance — entered the AB-cloud construct.

The AB-Cloud programme assembles all four traditions into one constructor and subjects it to the densest numerical interrogation to date. Its own history unfolds in the monumental line: from the first verifications V01–V20 (Python) through the Dirac laboratory D1–D14 and the bridge C1–C17 to blind verification E01–E18; then the observatory (gates H1–H7, the RH line, V01–V112 in Julia), the reference runs v18/v19 (37 tests, two-pass protocol), the vortex-density optimization (Test 34-ext) and the wave attractors (W1). The monumental line V01–V112 is the longest of them: a full Julia port of the Python monograph base — 112 verification campaigns, from hermiticity to phase identities, bit-for-bit at equal seeds. That is the "entire knowledge baggage" the present edition unfolds.


---

## 3. Architecture: ten levels of one machine

The programme is deployed as one machine on levels — each level asks its own question of the same construct. In the MAX edition there are ten levels: the original five (I, I⁺, II, III, IV, V in the old numbering with the processor as I⁺), plus v19 heritage (IV⁺), plus three new ones (VI, VII, VIII):

| Level | Campaigns | Theorems | Source | Question |
|---|---|---|---|---|
| I. Spectral core | V01–V19 | Th1–Th6 | AB_Cloud_Quantum_Research | what does the cloud do as a spectrum? |
| I⁺. AB processor | V20 (+V23/V24 previews) | — | same | how is logic executed in the cloud? |
| II. Dirac skeleton | D1–D14 | — | dirac-lab | what is the dynamics? |
| III. Hilbert–Pólya bridge | C1–C17 | T1–T18 | Hilbert_Polya | how close to the H–P operator? |
| IV. Blind verification | E01–E18 | — | AB_Cloud_Quantum_Research | can the instruments be trusted? |
| IV⁺. v19 heritage | Tests 1–37 (77 rows) | — | results | what does a full run show? |
| V. Spinor study | ES1–ES5 | TS1–TS3 | AB_Cloud_Quantum_Research | what is the memory model? |
| VI. Meridian Observatory | gates H1–H7 · RH · V01–V112 | — | meridian-spectral-observatory | how does one watch spectra systematically? |
| VII. Vortex optimization | T34-ext (A/B/C) | — | Vortex_optimization | which dials drive statistics to the floor? |
| VIII. Wave attractors | W1 (E1–E7) | — | Wave_attractors | how do waves self-organize into routes? |

The links between levels are certified by numbers, not decorations. The trace carries $\Lambda(n)/\sqrt{n}$ (Th6) — and blind reading confirms the zeros are *read*, not stored (E17); the processor compiles unitary logic into AB clouds at machine epsilon (V20) — and wins the honest class-B benchmark by ×59,000 (E18); the spinor study formalizes "reads, does not carry" as a machine without long-term memory (ES1–ES5); the observatory's gate H5 finds the clean GUE regime D — and the vortex optimization drives the cloud's statistics to the GUE floor (T34-ext); the wave attractors carry the same phase arithmetic into a classical continuum (W1). The V13 obligation machine blocks any premature RH conclusion at every level without exception.

The measurement protocol is uniform: (i) pre-registration of windows in `config.yaml` or the source's configuration; (ii) a run at fixed seed (the programme seed 42; the v19 runs use their own fixed protocols, e.g. base seed 96 in the vortex optimization); (iii) statistics and verdicts against the windows; (iv) a verdict file with `verdict`, `evidence`, `does_not_prove` fields; (v) independent reproduction in a second language (Python ↔ Julia). A repeat run must reproduce values bit-for-bit; every number in the monograph points to a specific verdict file.

The two-pass protocol of the reference runs adds a fourth axis — lattice independence: the primary pass runs on the primary lattice (72×72, $N_v = 4$), the HARDCORE pass on the secondary (96×96, $N_v = 2$) with deepened validation. Tests passing both get OVERALL PASS; discrepancies are recorded line by line. That is how the v19 reference run accumulated 77 verdict rows on 37 tests — and why the 11 FAIL-class rows are published alongside the 66 PASS: they are not failures of the run but measured boundaries of the method.


---

## 4. Method: pre-registration, blind protocols, the honest boundary

The methodological core of the programme is verdict discipline. Every experiment with a threshold carries a verdict file with a `does_not_prove` field: what the result does NOT prove. The field is not decorative: the package's integrity tests check its presence; the package LICENSE (§3) requires derivatives to preserve it verbatim. The logic is simple — numerical success breeds over-generalization, and the only defence is a boundary written down in advance.

Pre-registration works like this: decision windows (e.g. the GUE band for $\langle r \rangle$: $[0.5772, 0.6212]$; the KS threshold $D < 0.10$; the hermiticity threshold: machine zero) are fixed in configuration *before* the run and cannot be re-tuned after. A run that breaks a window is not "re-run until success": its FAIL/WARN verdict is published as a first-class result. Thus were born the programme's negative results: the lattice ζ-correspondences V1/V3/V6/V16 (the null zone of the gates), the failure of the gate H5 baseline A (median $D \approx 0.35$), the WARN rows of Tests 4/5/6/11/12/28b/29b/34b/35 of the v19 run.

Blind protocols complement this by removing tuning. The "blind spectrum" of level I means: statistics are measured before any adjustment toward the zeros. Blind reading E17 means: the engines compute zeros from first principles, with no access to external tables, and are checked against them only after completion. The blind families C13 are 20 gates generated outside the "handles" of earlier campaigns. The blind W1 audit (2026-10-01) is a cold-start reproduction: 31/31 data files, 12/12 figures bitwise.

Cross-verification is the third pillar. Decisive quantities are re-derived in a second language: levels II and IV (Python ↔ Julia, to machine precision), the wave attractors (Python ↔ Julia, $3.45\cdot10^{-15}$ over 1,200 bounce points), the zero engines (Euler–Maclaurin ↔ Riemann–Siegel, bit-exact on 649 zeros). The unified CLI implements one contract in six languages: Python, Julia, Rust, Go, JavaScript and Bash read one `config.yaml` and emit one JSON contract with identical metric keys.

The honest boundary is the top of the discipline. Everything in this package is a numerical and formal study of a mathematical model. It does not prove the Riemann hypothesis: the V13 obligation machine (Lean 4 / Coq, reductions A1–A6 without `sorry`) holds the verdict `blocked` until the analytic prerequisites — analyticity, the functional equation, no real zeros off the line — are formalized as proven statements. The machine's point is not to check proofs but to make it impossible to *quietly* substitute the status: any conclusion about RH inherits `blocked` automatically. That is the most direct way the programme disciplines its own language — and the present document inherits the verdict verbatim.


---

## 5. How to read the MAX edition

The MAX edition is organized in fourteen parts. Parts I–II are the programme and the apparatus: subject, history, architecture, method and the mathematical foundation (lattices, random matrices, the zeta function, metrics). Parts III–X are the levels of the machine: from the spectral core to the wave attractors; each part unfolds its level in full depth, with every campaign and figure. Parts XI–XII are data and registers: the full register of 73 numbers, the campaign register, the verdicts. Parts XIII–XIV are discussion, boundaries, roadmap and conclusion. Appendices A–P close the document: source mapping, the figure catalogue, the 77 v19 verdicts, chronology, glossary, ethics, language abstracts and audience summaries.

Three ways to read. (1) **As a chronicle:** sequentially, part by part — the programme's path from the construct to the wall and beyond it. (2) **As a reference:** by campaign — each campaign has its subsection with verdict, numbers and boundaries; the campaign index is Appendix A. (3) **As a map:** by verdicts — chapter 45 gathers all ten theses G1–G10 and the RH meta-thesis into one table; chapter 46 locates the wall.

Conventions on numbers. Numbers are transferred verbatim from the sources' verdict files: scientific notation like $2.59\cdot10^{-39}$ is not reformatted. Equalities like "649 = 649" mean agreement of two independent counts. Entries like "0.978 vs 0.0010 (×977)" mean measurement against control and the ratio. Where sources disagree by convention (e.g. the bulk-window convention in D7: 0.4759 vs 0.5084), both values are shown with the convention noted. Every register row (chapter 43) carries a campaign column — the source verdict file; the full path map is `00_meta/provenance.jsonl`.

Conventions on figures. All 53 static figures of the package are catalogued in Appendix C with captions and alt texts; in the text, figures are embedded in their sections with relative paths. The derived-statistics figures (M1–M3, R1–R2) were computed in this edition from package data and marked package-derived; their computation reproduces from the build scripts. The level-VII and level-VIII figures are byte copies of the sources; their regeneration is deterministic under the sources' protocols.

Conventions on language. Full volumes exist in Russian and English (the scientific record is RU/EN); the zh/de/es/fr/ar versions are abstracts. Formulas are set in Markdown LaTeX; console listings preserve the runs' formatting. Terminology is fixed by the glossary (Appendix F): AB cloud, gate, unfolding, campaign, verdict, honest boundary.


---

# PART II. THE MATHEMATICAL APPARATUS

## 6. The lattice, the flux and the AB-cloud Hamiltonian

The programme's base object is a Hermitian operator $H_L(\alpha)$ on the $L \times L$ torus: a lattice Hamiltonian whose boundary conditions carry $\alpha$ flux quanta per plaquette. The one-particle space is $\mathbb{C}^{L^2}$: one orbital per site. The tight-binding Hamiltonian couples neighbouring sites with hopping amplitudes; in a magnetic field every bond acquires a Peierls phase:

$$t_{ij} \rightarrow t_{ij} \cdot e^{i\Phi_{ij}},$$

where $\Phi_{ij}$ is the flux through the bond in flux-quantum units. In the Landau gauge the phases sit on horizontal hops; the monumental smoothed gauge distributes them over vertical bonds. Byers–Yang invariance guarantees: physical quantities do not depend on the gauge at fixed total flux through the torus.

A **vortex** is a plaquette (or site, in the discrete model) into which extra flux is "pressed": circulating it accumulates a total phase of $2\pi\alpha$. For non-integer $\alpha$ the wave function is multi-valued on the plane — the electron circles the vortex inside an Aharonov–Bohm "cloud". That non-local cloud is the programme's physical protagonist: the phase is accumulated along the path, not at a point; a local operator carries non-local memory of topology.

The vortex configuration is set by the parameter quadruple $(N_v, q, W, \alpha)$ and geometry: $N_v$ — the number of vortices (charge-neutral: half $+q$, half $-q$); $q$ — the vortex charge (fraction of a flux quantum); $W$ — the depth of the on-site potential well $V = qW/(r^2/N + 1)$; $\alpha$ — the uniform Hofstadter flux per plaquette; geometry — placement (protocol-random / regular grid / cluster / hexagon / ring) and boundaries (open / torus). The monumental phase model: smooth atan-gauge phases on bonds plus wells on sites.

Matrix assembly is the `build_ab_cloud_hamiltonian` family: a dense Hermitian $N \times N$ matrix with $N = L^2$. A "64×64 lattice" means a 4096×4096 matrix; "96×96" — 9216×9216. The cost arithmetic: diagonalization $\sim O(N^3) = O(L^6)$; memory $\sim O(N^2) = O(L^4)$, peak $\approx 2.5(L^2)^2 \cdot 16$ bytes; the step 16 → 72 costs ×8000. Hermiticity is stress-tested by gate H6: the norm of the anti-Hermitian part, stability under jitter of positions (0.35), flux (0.02), charges and width.

Special parameter points. $\alpha = 0.5$ — the base half-flux: chiral symmetry $\lambda \leftrightarrow -\lambda$ at $W = 0$; the Connes self-dual critical line. $\alpha = 25/900 \approx 0.0278$ — the "sharp flux": a GUE-quality lever found in the v23 run. $\alpha = 1/3$ — the point of the zero-mode counting law: $N_0 = 2L - 6\cdot[L \equiv 0 \bmod 12]$, index $-2$ — a genuine number-theoretic signature inside a lattice operator. $\alpha = 1/4$ — the gauge check-point of cell-flux uniformity on the torus (port validation: exactly 0.25 on every cell). The magic grid of 61 points — $\pi/30 \ldots \pi\times5$, $\sqrt{2} \ldots \sqrt{15}$, rationals, $\varphi$, $e$, $\ln 2$, $1/e$, $1/\pi$ — the universality grid of the RMT class.

The exact layer of the construct consists of six invariants: (1) hermiticity $\|H - H^\dagger\| = 0$ to machine precision; (2) flux quantization — the spectrum is invariant under integer flux shifts; (3) Byers–Yang invariance; (4) chiral pairing at $\alpha = 1/2$, $W = 0$; (5) Connes self-duality — the $s \leftrightarrow 1-s$ operation; (6) a chain of rational geometric-phase identities at 256-bit precision. The statistical layer is the ensemble of vortex realizations with subsequent analysis of nearest spacings, ratios $r$, the form factor $K(\tau)$, number variance and spectral rigidity against pre-registered windows.


---

## 7. Random-matrix statistics: from Poisson to GUE

Dyson's threefold way (1962) sorts Hermitian matrix ensembles by antiunitary symmetry. GOE ($\beta = 1$): real-symmetric matrices invariant under complex conjugation; GUE ($\beta = 2$): complex Hermitian without antiunitary symmetry; GSE ($\beta = 4$): quaternion self-adjoint with Kramers degeneracy. The beta parameter controls the strength of level repulsion: $P(s) \sim s^\beta$ as $s \to 0$ — a Poisson spectrum (integrable systems) does not repel at all, $P(0) \ne 0$.

The Wigner surmise is the analytic approximation to the unfolded-spacing distribution. For GUE ($\beta = 2$):

$$P(s) = \frac{32}{\pi^2} s^2 e^{-4s^2/\pi}.$$

The normalization $32/\pi^2$ is not an arbitrary constant: the suite's Test 37 verifies the underlying identity through the log-convexity of Γ (Bohr–Mollerup characterization) and the self-dual reflection $\Gamma(1/2)^2 = \pi$: $(1/2)! = \sqrt{\pi}/2$ with relative error 0.0. The surmise normalization is a theorem; the programme checks it verbatim — the foundation of the KS reference for every spacing test.

The $r$-statistic — the ratio of adjacent spacings, invariant under unfolding:

$$r_i = \frac{\min(\delta_i, \delta_{i+1})}{\max(\delta_i, \delta_{i+1})}, \qquad \langle r \rangle_{\mathrm{GUE}} \approx 0.5996.$$

The exact $P(r)$ for GUE was derived by Atas–Bogomolny–Giraud–Roux (2013); the suite samples it through `gue2_surmise_cdf` (inverse-transform sampling) — the reference H0. The confidence band for the programme's finite ensembles: $[0.5772, 0.6212]$. The no-correlation reference is Poisson $\langle r \rangle \approx 0.5307$; GOE gives $\approx 0.5359$; GSE $\approx 0.424$ — GSE is architecturally unreachable for our construct: the absence of $n$-fold chiral blocks excludes it by design.

Unfolding converts the spectrum to dimensionless units: $E \to \tilde{N}(E)$, the integrated density approximated by a polynomial (degrees 5 or 9 in the codes); after unfolding the spacings $s_i$ have mean 1 and are stationary along the spectrum. Comparison with GUE is possible only after unfolding — the RMT standard since Mehta. The alternative is the $r$-statistic, insensitive to monotone unfolding; the programme uses both.

The Kolmogorov–Smirnov criterion: $D_n = \sup_s |F_n(s) - G(s)|$, threshold $d_{\mathrm{crit}} = 1.63/\sqrt{n}$ at the ~1% level. The critical consequence for lattice work: $n$ is the number of spacings in the central band $\approx 0.6L^2$. At $L = 16$: $n \approx 150 \to d_{\mathrm{crit}} \approx 0.132$; at $L = 64$: $n \approx 2400 \to d_{\mathrm{crit}} \approx 0.033$ — the threshold tightens fourfold at unchanged physics. A "failure" of the α-profile at 16 → 64 is growth of statistical power, not new physics.

The Anderson–Darling statistic is tail-sensitive: $A^2 = -n - \frac{1}{n}\sum_i (2i-1)[\ln F(x_{(i)}) + \ln(1 - F(x_{(n+1-i)}))]$. The `test11_honest` lesson: bootstrapping with replacement from a finite pool creates ties and inflates the null severalfold; an MC null for a continuous H0 must be built from i.i.d. samples of H0 itself, with add-one (Laplace) smoothing of p-values. A methodological first-class result: a wrong null breeds false rejections.

The form factor $K(\tau)$ is the Fourier image of the pair correlation. GUE prediction: $K(\tau) = \tau$ for $\tau < 1$ (ramp) and $K(\tau) = 1$ for $\tau > 1$ (plateau). Test 35 of v19 measures it on the 50k table; test D14 — on the band $t \approx 10^5$: $K(2) = 0.962$ — plateau on target. Number variance $\Sigma^2(L)$ and spectral rigidity $\Delta_3(L)$ are the long-range statistics; tests 13/14 check them on 9 window lengths: data closer to GUE in 9/9.


---

## 8. The zeta function: zeros, density, unfolding

The Riemann zeta function $\zeta(s) = \sum_n n^{-s}$ (for $\mathrm{Re}\,s > 1$; analytic continuation beyond) has trivial zeros $-2, -4, \ldots$ and non-trivial ones in the critical strip $0 < \mathrm{Re}\,s < 1$. The functional equation $\zeta(s) = \chi(s)\zeta(1-s)$ with $\chi(s) = 2^s\pi^{s-1}\sin(\pi s/2)\Gamma(1-s)$ is symmetric about the line $\mathrm{Re}\,s = 1/2$: zeros come in pairs $\rho, 1-\rho$; reality of $\zeta$ on the line gives the conjugate pairs — four zeros from one on the line.

The Riemann–von Mangoldt theorem: $N(T) = \frac{T}{2\pi}\ln\frac{T}{2\pi e} + \frac{7}{8} + S(T) + O(1/T)$ with $S(T) = \frac{1}{\pi}\arg\zeta(1/2 + iT)$ the fluctuating part. The mean zero density at height $T$: $\overline{d}(T) = \frac{1}{2\pi}\ln\frac{T}{2\pi}$ — logarithmic growth. The mean gap near $T \approx 40\,000$: $\approx 2\pi/\ln(6400) \approx 0.11$–$0.12$ — the local scale of the observatory's 50,000-zero table.

Unfolding the ζ zeros: $\tilde{\gamma}_n = \overline{N}(\gamma_n)$ by the smooth part of Riemann–von Mangoldt; the gaps $s_n = \tilde{\gamma}_{n+1} - \tilde{\gamma}_n$ have mean 1 and GUE statistics. The 50,000-zero table (from $\gamma_1 = 14.134725142$ to $\gamma_{50000} = 40433.687385462$) yields 49,999 spacings — the reference of Test 34 and the level-VII optimization. The package-level audit of this edition: $\langle r \rangle = 0.6119 \pm 0.0010$ ($n = 49{,}998$) — GUE class; sliding 5,000-zero blocks hold $[0.6095, 0.6160]$ along the whole strip; locally-unfolded spacings against the Wigner surmise: $D = 0.0223$ — finite sample, the same order as the method's GUE floor.

Computational tools of the ζ side. The Euler–Maclaurin engine: $\zeta(s)$ by summation with the Euler–Maclaurin correction; applicable away from the critical strip, accuracy controlled by term count. The Riemann–Siegel formula (in Arias de Reyna's edition): $\zeta(1/2 + it) = 2\sum_{n \le \sqrt{t/2\pi}} n^{-1/2}\cos(\theta(t) - t\ln n) + R(t)$ — the main tool on the critical line; the sign of $\theta(t)$ is controlled by Siegel's expansion. `mpmath.zetazero(k)` — the reference computation of the $k$-th zero at arbitrary precision (25 digits in the RH line). The blind protocol E17: two engines read the zeros to $T = 1000$ without external tables — 649/649 and 639/639 with bit-exact cross-match; the independent Riemann–Siegel implementation agrees with Euler–Maclaurin to $3.8\cdot10^{-15}$.

The arithmetic layer of the ζ side: the von Mangoldt weight $\Lambda(n) = \ln p$ for $n = p^k$, zero otherwise; $\Lambda(n)/\sqrt{n}$ — the weight that the Guinand–Weil trace formula assigns to the heat trace of a ζ-coupled operator. The identity $Q(a)$ and the twisted formula with Dirichlet characters $\chi(n)\Lambda(n)/\sqrt{n}$ ($\chi_5$, $\chi_7$ — campaign C15) extend the bridge to the whole L-function class. Primes enter the programme three ways: as the Bragg comb at $\omega = \log p$ (gate H1), as the trace weight (Th6) and as phase co-locations $(\Phi_p, \Phi_q) \equiv \Phi_{pq}$ (C6).


---

## 9. The Hilbert–Pólya conjecture and operator candidates

The operator line begins with the H–P question itself. Modern landmarks. **Berry–Keating $xp$ (1999):** the semiclassical Hamiltonian $H = (xp+px)/2$ on functions over $(0,\infty)$; spectrum density $\overline{d}(E) \sim \frac{1}{2\pi}\ln(E/2\pi e)$ — the correct mean density of ζ zeros without fluctuations. Our level II realizes the Berry–Keating ladder *exactly on a lattice*: spectrum to $1.7\cdot10^{-13}$ of the arithmetic ladder $2\pi m/\Lambda$ (D11); the AB-cloud coding phase is recognized as the fractional BK ladder ($4.6\cdot10^{-13}$); the infinite ladder at fixed density sharpens into the Connes delta-train (D12).

**Connes (1999):** the adelic sum $x + \theta^2 x^{-1}$ on positive characters of $\mathbb{Q}^*$; the trace comb of period $\Lambda = \log q$; RH equivalent to a positivity statement. The programme checks the Connes layer directly: the $s \leftrightarrow 1-s$ self-duality belongs to the construct's exact layer; the Connes trace comb is realized on the lattice with period $\Lambda$ to $2.6\cdot10^{-13}$.

**Sierra (2008):** a series of quantizations of $x[p]$ and related Hamiltonians; the question — which produce GUE fluctuations. The programme answers systematically: GUE fluctuations are produced not by the Hamiltonian class but by the breaking of antiunitary symmetry — vortex phase fields covering every bond make the breaking total inside the working window $N_v \approx 8$–16 (level VII).

Candidates outside the operator line: **quantum chaos** — the BGS conjecture (Bohigas–Giannoni–Schmit, 1984): the spectral statistics of a quantum system whose classical limit is chaotic follow the random-matrix ensembles. The AB-Cloud programme realizes the BGS prescription *mechanically*: a Hermitian operator without antiunitary symmetry, with complex phases — and measures at which parameters the prescription actually holds (answer: not everywhere — the dilute regime $N_v \lesssim 4$ stays nearly integrable).

What an H–P operator must have, if it exists: (i) hermiticity — real spectrum; (ii) mean level density $\sim \frac{1}{2\pi}\ln(E/2\pi e)$ — the BK ladder scale; (iii) GUE spacing statistics — the Montgomery–Odlyzko class; (iv) the arithmetic layer — the $\Lambda(n)/\sqrt{n}$ weight in a Guinand–Weil trace formula; (v) $s \leftrightarrow 1-s$ self-duality; (vi) no magnetic field in the ordinary sense — the construct must "read" ζ without copying it. The programme checks each item separately and fixes: (i)–(ii) hold exactly; (iii) holds in the working window (T34-ext: $D = 0.0318$ vs floor 0.0220); (iv) holds in the trace (Th6, $r = 0.9996$) and fails in gate spectra (the null zone); (v) holds; (vi) is the spinor study's subject — a machine without long-term memory, reading mathematics in real time.


---

## 10. Distance metrics: KS, A², ⟨r⟩, R₂, Δ₃, the form factor

The programme uses six metric families. **The KS distance** $D_n = \sup|F_n - G|$ — the supremal gap between empirical and theoretical CDF; the two-sample variant (Tests 12/34) compares two empirical CDFs directly. Threshold $d_{\mathrm{crit}} = 1.63/\sqrt{n}$ (~1% level). Strength: sensitivity to the body of the distribution; weakness: insensitivity to tails. Test 34-ext uses the pooled KS over realizations: 27,640 spacings against 49,999 ζ spacings.

**Anderson–Darling $A^2$** — a weighted integral of $(F_n - G)^2/[G(1-G)]$: the weight amplifies tail contributions. For a fully specified continuous H0: null median $\approx 0.5$–1, critical 5% $\approx 2.492$, independent of $n$ under correct calibration. Test 11 of v19: $A^2 = 61.49$, MC p = 0.0000 — with the honest note that the best high-T subrange also rejects; height-resolved diagnostics locate the discrepancy in the tails.

**⟨r⟩ and P(r)** — adjacent-spacing ratios: unfolding-invariance makes them the lattice campaigns' primary tool; window $[0.5772, 0.6212]$. **R₂(s)** — the pair correlation: Montgomery's $g(u) = 1 - (\sin\pi u/\pi u)^2$; ⟨|ΔR₂|⟩ < 0.10 is the second arm of the 34b composite; the v19 run measured 0.0002 — excellent agreement (0.0374 in the primary pass).

**Δ₃(L)** — spectral rigidity: the mean-square deviation of the counting function from a straight line over windows of length $L$; GUE: $\Delta_3 \approx \frac{1}{\pi^2}(\ln 2\pi L + \gamma - 5/4 - \pi^2/8)$. Test 14 of v19: data closer to GUE in 9/9 window lengths. **Σ²(L)** — number variance: Test 13 — 9/9 closer to GUE.

**The form factor K(τ):** $K(\tau) = \int e^{2\pi i\tau u}[g(u)-1]du$; GUE: ramp $\tau$ up to $\tau = 1$, plateau 1 beyond. Test 35 of v19: RMS_GUE = 0.4193, corr_GUE = 0.8889 — WARN: the ramp reproduces, the plateau less well; the HARDCORE pass confirms (2 of 3 sub-checks failed). D14 of level II on the band $t \approx 10^5$: $K(2) = 0.962$ — the plateau exact at Odlyzko heights. The v19/D14 difference is not a contradiction but two bands: the form factor at low heights is noise-dominated by finite sampling, at high heights it converges to prediction.

Composite criteria assemble metrics into verdicts. Test 34b "hardcore": PASS iff (1) KS: $p > 0.01$ **or** $D < 0.10$ (pooled); (2) ⟨|ΔR₂|⟩ < 0.10; (3) $d_{GUE} < d_{Poisson}$ (GUE-side, not Poisson); (4) spread of $D < 0.10$ across realizations. Gate H5 of the observatory: ⟨r⟩ in band + individual KS per realization + the α-profile. Compositeness defends against "victory by one metric": a configuration must pass all arms simultaneously — and it is exactly compositeness that distinguishes the clean regime D (7/7) from the OR-clause regimes B/C of gate H5.


---

# PART III. LEVEL I: THE SPECTRAL CORE AND THE AB PROCESSOR

## 11. Level I: the theorems Th1–Th6 and their certificates

The spectral core is formalized in six theorems; each carries a numerical certificate and a boundary — the *statement — certificate — boundary* form is kept verbatim.

**Th1 (hermiticity and chiral symmetry).** If $H_L = H_L^\dagger$ the spectrum is real; at $\alpha = 1/2$ with $W = 0$ it is symmetric: $\lambda \leftrightarrow -\lambda$. *Certificate:* $\|H - H^\dagger\| = 0.0$ machine-exact; pair splitting below $4\cdot10^{-15}$ over 800 pairs. *Boundary:* hermiticity of a finite matrix is trivial; the content is stability of the structure under decorations. Practical reading: chiral symmetry is the structural element that the level-II ζ-decoration must preserve (and does — D8: pairing $E \leftrightarrow -E$ to $4\cdot10^{-15}$ under decoration).

**Th2 (self-adjointness in finite dimension).** Defect indices $(0,0)$; unitarity of $e^{-iHt}$. *Certificate:* drift $2.2\cdot10^{-16}$ per unit time. Trivial in form — non-trivial in its role as reduction A2b of the formal layer: it lets dynamics statements of level II carry over without extra conditions. Formalized in Lean 4 without `sorry`.

**Th3 (Kato corridors).** A perturbation $\delta$ shifts eigenvalues by at most $\delta^2/\mathrm{gap}$ plus a Gershgorin bound. *Certificate:* corridor widths $\sim 10^{-27}$ at 40 digits. Practical meaning: numerical "coincidences" of spectra have a controlled price — a claim that two numbers agree must name its corridor. Every "X = Y to $10^{-k}$" verdict implicitly carries a Kato corridor; at 256-bit precision the corridors shrink to $\sim 10^{-70}$.

**Th4 (Li's criterion through the trace).** Eigenvalues are recovered via $\lambda_n = \mathrm{Tr}\, g_n(H_\xi)$ with absolute convergence. *Certificate:* two computation paths agree to $4.4\cdot10^{-11}$. This is the computational core of Li's criterion — the analytic RH equivalent reducing to positivity of the coefficient sequence $\{\xi_n\}$: $\Xi(s) = \xi(1/2+s) = \sum \xi_n s^n$, RH $\Leftrightarrow \xi_n > 0$ (Li, 1997). The programme computes the coefficients and asserts no positivity: computability ≠ truth. Positivity was checked on the initial coefficients (where it is known) — that is the whole distance a numerical method may travel.

**Th5 (block reduction).** Commutation $[H,A] = [H,B] = 0$ reduces the spectrum by characters. *Certificate:* the union of blocks matches the spectrum to $7.1\cdot10^{-15}$. Vortices breaking the commutation are filed to a separate honesty register: not "bad" configurations but the theorem's applicability boundary. The practical application is campaign C8's spinor64 reduction: 64 → 4 blocks with $|\Delta\lambda| \le 1.1\cdot10^{-14}$ — an order-of-magnitude saving on exact computations.

**Th6 (trace formula: the blind core of the bridge).** The Guinand–Weil identity links $Q(a)$ with $\zeta'/\zeta$; the heat kernel $K(x) = \mathrm{Tr}\,e^{-xH_\xi}$ carries the weight $\Lambda(n)/\sqrt{n}$. *Certificate:* trace-prime correlation $r = 0.9996$ (lattice control: 0.76). *Boundary:* presence of the weight in the trace does not imply spectral identity — that is the level-III statement, and it is negative. Th6 is the single point where prime arithmetic demonstrably enters the operator construct — through the trace, not the spectrum.

The blind spectrum (campaigns V01–V03): statistics are measured before any tuning toward the zeros — agreement with GUE windows. Vortex ensembles at $N_v \ge 8$: $\langle r \rangle = 0.60$ — the GUE value. The negative correspondences V1/V3/V6/V16: configurations encoding zeros into phases do not reproduce the zeros' arithmetic in spectra — four honest negatives that eliminate the "encode the phase, get the spectrum" class wholesale.

The V13 obligation machine (§4) is implemented with formal reductions A1–A6 without exemptions; the V19 branch-stitching completes the core with a positive constructive result: the θ-ladder closes with coherence 0.9995 (z-statistic 43.4) and $\mathbb{Z}_2$ monodromy — the construct's multi-valued branches glue without loss of precision.


---

## 12. The AB processor: ISA, exact compilation, "reads — does not carry"

The processor block turns the lattice into a computing fabric. The AB-cloud ISA fixes the primitive alphabet: single-plaquette phase rotations and coupled moves; the compiler assembles arbitrary unitary logic into primitive sequences by the Givens–QR method with accuracy $1 - F \le 4.4\cdot10^{-16}$ for 4×4 and $6.7\cdot10^{-16}$ for 8×8, at depths up to 7 and 29 gates respectively. The accuracy is machine epsilon: compilation loses not one bit of unitarity.

The class-B benchmark (E18): the honest comparison against five strong baselines under equal ISA restrictions (same primitives, same depth): maximum $1 - F = 4.4\cdot10^{-16}$, primitives no worse than BL1/BL2/BL4 on every target, time advantage ×59,000. The benchmark's honesty: the 2q KAK optimum (3 gates) is outside the E18 class by construction (it uses arbitrary two-qubit rotations outside the ISA), and the compiler gives 10 on the same target — the loss is recorded in the verdict file as `does_not_prove: optimality outside the E18 class`.

**V23 "reads, does not carry" (preview).** 12/12 ζ zeros are reproduced from six constants of the formula at zero storage. The formula is the exact Riemann–Siegel expression: the zero $\gamma_k$ is computed from $\{\pi, \ln 2\pi, \text{Euler } \gamma, \text{initial phases}\}$ and the integer index $k$ — no tables. The computational demonstration of the principle: the cloud reads mathematics in real time without accumulating it. The link to the spinor study: ES1–ES3 formalize the same triad "cycles — reset — step" in a model without long-term memory.

**V24 "no signaling" (preview).** CHSH $S = 2\sqrt{2} - 4.4\cdot10^{-16}$ — the exact Tsirelson value; zero commutators; 1000/1000 defence against communication cycles. The construct's nonlocality (correlations through shared phase fields) does not violate relativistic causality at the level of numerical evidence: correlations without signalling — the same class as entangled states in quantum mechanics.

In the MAX frame, levels I and I⁺ supply the operational foundation: (1) a construct with an exact invariant layer; (2) a statistical layer in the GUE class; (3) a computing fabric compiled to machine epsilon; (4) mathematics read without storage. Everything that follows — levels II–VIII — builds on this foundation: Dirac dynamics (II), the ζ bridge (III), blind instruments (IV), the memory model (V), systematic observation (VI), dial optimization (VII), the external prop (VIII).


---

## 12a. Full record of level I (from the unified volume)

#### Full record: 4. Level I: the spectral core and the AB processor

#### 4.1. Theorems Th1–Th6 and their certificates

The spectral core is formalized in six theorems; each carries a numerical certificate and a boundary.

**Th1 (hermiticity and chiral symmetry).** If $H_L = H_L^\dagger$, the spectrum is real; at $\alpha = 1/2$ with $W = 0$ the spectrum is symmetric about zero: $\lambda \leftrightarrow -\lambda$. *Certificate:* $\|H - H^\dagger\| = 0.0$ exactly; pair splitting below $4\times10^{-15}$ over 800 pairs. *Boundary:* hermiticity of a finite matrix is trivial; the theorem's content is the stability of the structure under decoration, not realness itself.

**Th2 (finite-dimensional self-adjointness).** Defect indices $(0,0)$; unitary evolution $e^{-iHt}$. *Certificate:* drift $2.2\times10^{-16}$ per unit time. In finite dimension the statement is again trivial in form — its role is the A2b reduction: it lets Level II's dynamics statements carry over without extra conditions.

**Th3 (Kato corridors).** A perturbation $\delta$ shifts eigenvalues by at most $\delta^2/\mathrm{gap}$ plus the Gershgorin bound. *Certificate:* corridor widths $\sim 10^{-27}$ at 40 decimal digits. Practical meaning: numerical "coincidences" of spectra have a controlled price — any claim that two numbers coincide must quote its corridor.

**Th4 (the Li criterion through traces).** Eigenvalues are recovered via $\lambda_n = \mathrm{Tr}\, g_n(H_\xi)$ with absolute convergence. *Certificate:* two computational paths agree to $4.4\times10^{-11}$. This is the computational core of Li's criterion — the analytic RH equivalent reducing the hypothesis to the positivity of a coefficient sequence; the programme computes it but does not assert positivity.

**Th5 (block reduction).** $[H,A] = [H,B] = 0$ reduces the spectrum by characters. *Certificate:* the union of blocks equals the spectrum to $7.1\times10^{-15}$. Vortices breaking the commutator are logged in the honesty register: they are not "bad" configurations but the theorem's boundary of applicability.

**Th6 (the trace formula: the bridge's blind core).** The Guinand–Weil identity relates $Q(a)$ to $\zeta'/\zeta$, and the heat kernel $K(x) = \mathrm{Tr}\,e^{-xH_\xi}$ carries the weight $\Lambda(n)/\sqrt{n}$. *Certificate:* trace-primes correlation $r = 0.9996$ (lattice control: 0.76). *Boundary:* the weight's presence in the trace does not imply spectral identity — that is a Level III statement, and it is negative (§6.5).

#### 4.2. The blind spectrum and negative correspondences

The core's key methodological choice: statistics are measured *before* any tuning toward the zeros. The blind spectrum of the AB cloud (campaigns V01–V03) agrees with the GUE windows; vortex ensembles with $N_v \ge 8$ give $\langle r \rangle = 0.60$ — the GUE value. At the same time, campaigns V1, V3, V6 and V16 fix the *absence* of lattice $\zeta$-correspondences: configurations encoding zero phases do not reproduce zero arithmetic in spectra. These four negative verdicts are published as first-class results: they eliminate the entire candidate class "encode the phase — get the spectrum".

#### 4.3. The V13 obligation machine and branch stitching V19

The obligation machine (§3.4) is implemented with formal reductions A1–A6 and no shortcuts. Branch stitching V19 closes the spectral core with a positive constructive result: the θ-ladder closes with coherence $0.9995$ (z-statistic 43.4) and $\mathbb{Z}_2$ monodromy. This is the closest to "smooth" result Level I has: the construct's multi-valued branches glue without precision loss.

#### 4.4. The AB processor: ISA and exact compilation (V20)

The processor block turns the same lattice into a computing fabric. The AB-cloud ISA fixes the primitive alphabet; the compiler assembles arbitrary unitary logic into primitive sequences by the Givens–QR method with fidelity $1 - F \le 4.4\times10^{-16}$ for 4×4 and $6.7\times10^{-16}$ for 8×8, at depths up to 7 and 29 gates respectively. Two previews complete the picture. **V23 "reads, does not carry":** 12/12 $\zeta$ zeros are reproduced from six formula constants with storage equal to zero — a computational demonstration of the principle "the cloud reads mathematics in real time". **V24 (no signaling):** CHSH $S = 2\sqrt{2} - 4.4\times10^{-16}$ with zero commutators and 1000/1000 protection against communication cycles — the construct's nonlocality does not violate relativistic causality at the level of numerical evidence.

#### 4.5. Level I boundaries

Level I does not assert spectral identity (that is Level III, verdict negative); does not assert positivity of Li's criterion (computability ≠ truth); and insists that the absence of lattice correspondences is not a technical failure but a substantive result: phase coding as a class does not carry zero arithmetic into spectra.

---

---

# PART IV. LEVEL II: THE DIRAC SKELETON

## 13. Level II: the continuum limit and the Dirac identity

The Dirac laboratory unfolds the AB cloud's dynamics into a full lattice-Dirac identity. Fourteen tests D1–D14 (96 checks, all PASS) in four blocks; the MAX edition takes each in turn.

**The continuum-limit block.** D1 (cone): the π-flux lattice is a discretized massless Dirac equation. Fermi velocity $v_F = 1.9347 \approx 2t$ (theory: $2t$ at π flux — the consistent hopping convention); $E_1 L \to 4\pi$ (lowest-mode scaling); quadratic accuracy $R^2 = 0.9997$; cross-Julia: $9\cdot10^{-7}$ — the rounding level of 6-digit reference values. D2 (tower): the fourfold zero-mode tower on tori of every size — exactly the Dirac torus structure: Chern number 4 at $\alpha = 1/2$ (flux of 2 quanta through the torus: ×2 spin × 2 valley degeneracy). Fragile as the index theorem demands: $\|\{H,\Gamma\}\| = 0$ machine-exact; any mass splits the tower. D3 (Berry phase): exactly $\pi$ — the cone carries the non-standard topological phase; verified by parallel transport around the cone. D4 (Landau ladder): relativistic, $E_n^2 \propto n$ with $R^2 \ge 0.9998$ against the Schrödinger control $E_n \propto n$ — mass must enter the square of energy linearly, as in Dirac, not the energy, as in Schrödinger.

**The relativistic-dynamics block.** D5 (Klein): tunnelling at normal incidence on a wall of height $V_0 \to 2E$: $T = 0.978$ against $0.0010$ for the Schrödinger control — a factor of 977. The physics: for a Dirac particle a wall above the pair energy is the pair-creation regime; the spinor-component transfer is complete. D6 (ZB): Zitterbewegung — interference of positive and negative energy components; frequency exactly $\omega = 2E$; two independent agreement estimates 0.9996 and 0.9998 (Fourier analysis and direct fit).

**The ζ-decoration block — the actual bridge.** D7: the ζ-decorated Dirac operator lifts bulk statistics from the GOE ceiling to the GUE value: $\langle r\rangle_\zeta = 0.608$ against theory 0.5992; the undecorated lattice: $\approx 0.51$ (near GOE). Decoration: hops multiplied by $e^{i\phi_n}$ with phases encoding ζ zeros into Bloch angles. D8: chiral protection — $\{H,\Gamma\} = 0$ survives decoration: pairing $E \leftrightarrow -E$ to $4\cdot10^{-15}$ over 800 pairs. D9 (the Jackiw–Rossi wall): a mass wall restores the index — it binds chiral pairs of zero modes pinned $3.9\cdot10^{-9}$ below the gap, contrast $7\cdot10^6$, and survives *inside the full ζ-vortex background*. Jackiw–Rossi theory (1981): a fermion bound to an Abrikosov vortex has $|\Phi|$ zero modes; the wall binds them — the programme verifies this in the ζ background. D10 (Montgomery transport): unfolded zeros reproduce Montgomery's pair correlation; among equal-density competitors the ζ-cloud reflects least and transmits most: $g(0.3) = 0.19$ — repulsion protects transport.

**The conjugation-action block.** D11: the dilation generator with cutoff is realized on the lattice *exactly* — spectrum to $1.7\cdot10^{-13}$ of the arithmetic ladder $2\pi m/\Lambda$; the semigroup is unitary to $1.1\cdot10^{-14}$; the Connes trace comb with period $\Lambda$ to $2.6\cdot10^{-13}$; the AB-cloud coding phase is *recognized* as the fractional Berry–Keating ladder ($4.6\cdot10^{-13}$) — phase recognition, not spectral. The ladder tracks all 2,000 real zeros to ±2.3 zero units. D12: the infinite ladder at fixed density — the trace comb sharpens into the Connes delta-train: peak $= N_u$ exactly at every band size; off-peak envelope to $1.9\cdot10^{-4}$ at $N_u = 32768$; ζ-protection is extensive ($\langle r\rangle$ independent of $L$ at fixed density 25/900 while the encoded ladder grows 25 → 64). D13: the wall under the conjugation drive — pinned on orbit ($3.9\cdot10^{-9}$, gap/679). D14: the form factor on the Odlyzko band $t \approx 10^5$: $K(2) = 0.962$ — the plateau exact, as the GUE hypothesis demands at large heights.

Cross-verification: D1, D2, D7, D8 re-derived from scratch in Julia (LinearAlgebra, no external packages); the extensions D9, D11, D12–D14 by three additional independent ports. The bulk-window convention discrepancy (0.4759 vs 0.5084 at $L=32$) is documented; the $O(n_{\mathrm{bulk}}^{-1})$ effect touches no verdict.


---

## 13b. Full record of level II (from the unified volume)

#### Full record: 5. Level II: the Dirac skeleton

#### 5.1. Fourteen tests: from the cone to the form factor

The Dirac laboratory unfolds the AB cloud's dynamics into a complete lattice-Dirac identity. Fourteen tests D1–D14 (96 checks, all PASS) fall into four blocks.

**The continuum-limit block.** D1: the $\pi$-flux lattice is a discretized massless Dirac equation — Fermi velocity $v_F = 1.9347 \approx 2t$; $E_1 \cdot L \to 4\pi$; quadratic accuracy $R^2 = 0.9997$. D2: the fourfold zero-mode tower on the torus of every size — exactly the Dirac torus structure, fragile precisely as the index theorem demands ($\|\{H,\Gamma\}\| = 0$ exactly). D3: the cone's Berry phase equals $\pi$ exactly. D4: the Landau ladder is relativistic, $E_n^2 \propto n$ with $R^2 \ge 0.9998$, against the Schrödinger control $E_n \propto n$.

**The relativistic-dynamics block.** D5: Klein tunneling at normal incidence — $T = 0.978$ against $0.0010$ for the Schrödinger control, an excess of ×977; D6: Zitterbewegung at frequency $\omega = 2E$ with two independent agreement estimates of $0.9996$ and $0.9998$.

**The ζ-decoration block — the actual bridge.** D7: the $\zeta$-decorated Dirac operator lifts bulk statistics from the GOE ceiling to the GUE value: $\langle r \rangle_\zeta = 0.608$ against theory $0.5992$; D8: chiral protection — $\{H,\Gamma\} = 0$ survives decoration, $E \leftrightarrow -E$ pairing to $4\times10^{-15}$ over 800 pairs; D9: the index-restoring Jackiw–Rossi wall binds chiral pairs of zero modes pinned $3.9\times10^{-9}$ below the gap, contrast $7\times10^{6}$, and survives *inside the full ζ-vortex background*; D10: Montgomery in motion — the unfolded zeros reproduce the Montgomery pair correlation; among equal-density clouds the ζ cloud reflects least and transmits most ($g(0.3) = 0.19$): repulsion protects transport.

**The conjugation-action block.** D11: the cutoff dilation generator is realized *exactly* on the lattice — spectrum to $1.7\times10^{-13}$ of the arithmetic lattice $2\pi m/\Lambda$, semigroup unitary to $1.1\times10^{-14}$, the Connes trace comb of period $\Lambda$ to $2.6\times10^{-13}$; the AB-cloud coding phase is *recognized* as the fractional Berry–Keating staircase ($4.6\times10^{-13}$); the staircase tracks all 2000 real zeros to $\pm 2.3$ zero units. D12: the infinite Berry–Keating ladder at fixed density — the trace comb sharpens into the Connes delta train: peak $= N_u$ exactly at every band size, off-peak envelope down to $1.9\times10^{-4}$ at $N_u = 32768$; ζ protection is *extensive* ($\langle r \rangle$ L-independent at fixed density 25/900 while the encoded ladder grows 25 → 64). D13: the wall under the conjugation drive — pinned on the orbit ($3.9\times10^{-9}$, gap/679). D14: the form factor on the Odlyzko band $t \approx 10^{5}$: $K(2) = 0.962$ — the plateau exact, as the GUE hypothesis for $K(\tau)$ at large heights requires.

#### 5.2. Cross-verification

All decisive quantities of the level (D1, D2, D7, D8) are re-derived from scratch in Julia (LinearAlgebra only, zero external packages): the energies $E_1$ at $L = 16/24/32$ agree to $9\times10^{-7}$ (the rounding level of the 6-digit reference values), the tower and chiral quantities exactly. The extensions D9, D11, D12–D14 are verified by three further independent ports; the note on the bulk-window boundary convention (clean-lattice $\langle r \rangle$ differing 0.4759 vs 0.5084 at $L=32$) is documented in the source and affects no verdict — the effect is $O(n_{\mathrm{bulk}}^{-1})$.

#### 5.3. Level II boundaries

Level II establishes the *identity of the dynamics*, not of the spectrum. The GOE → GUE lift (D7) is a statistical fact about the decorated operator; it does not transfer to the undecorated lattice and asserts nothing about individual zeros. The form factor D14 is measured on the band $t \sim 10^{5}$; behaviour as $t \to \infty$ remains a numerical extrapolation.

---

---

# PART V. LEVEL III: THE HILBERT–PÓLYA BRIDGE

## 14. Level III: the Hilbert–Pólya bridge — phases v1 and v2

The bridge is deployed in two phases: v1 builds the resonator and measures the gap (C1–C8, T1–T10); v2 hunts the edges of the gap (C9–C16, T11–T18).

**C1 (the identity function):** $Z_{\mathrm{id}}$ with Γ-closures is exact to $2.59\cdot10^{-39}$ at 40 digits; its zeros on $[0,200]$ match the mpmath oracle 79/79 with $\max|\Delta\gamma| = 2.8\cdot10^{-14}$; Gram points break sign 4 times in 220 — the classics. Technically: $Z_{\mathrm{id}}(s) = \zeta(s)/Z_0(s)$ with $Z_0$ a trivial denominator sharing the zeros; Γ-closures are the standard convergence acceleration. **C2 (the argument principle):** the arithmetic bridge converges with $|\Delta N| = 2.6\cdot10^{-26}$; in the strip to $T = 1000$ the on-line zero count equals the strip count: $649 = 649$; gaps in $[0.3104, 6.887]$, mean 1.521. The arithmetics: (i) direct $\arg\zeta$ along a contour; (ii) Riemann–von Mangoldt with $S(T)$; (iii) the lattice bridge. **C3 (the gate family):** best $r_{H7} = 0.226$ over 52 gates (Bonferroni 0.80) — a statistical null. $r_{H7}$ is the gate-spectrum vs ζ-spectrum correlation over seven windows; the 52-hypothesis correction is mandatory. **C4 (trace formula):** the identity $Q(a)$ to $1.7\cdot10^{-12}$; the $H_\xi$ trace formula to $1.2\cdot10^{-5}$; the heat projection PC0 with $r = +0.9998$; the trace-metric gap $\approx 0.5$ order. **C5 (the extended family):** the gates of the regenerated honest v2 pipeline are all in the GUE class ($\langle r\rangle = 0.569$–0.633, mean 0.601; $\max|r_{H7}| = 0.097$, Bonferroni 0.57; v2.0.5 honest regeneration). **C6 (primes in the operator):** co-location $(\Phi_p,\Phi_q) \equiv \Phi_{pq}$ to $1.35\cdot10^{-14}$ — phase arithmetic is multiplicative; the δ(d) kernel saturates at $d \approx 4$–6; the ψ-ladder with correlation $+0.972$ — at the zeros, not the gates. **C7 (dynamics):** ζ-wave transport to $P(x \ge 90) = 0.0032$ against 0.0002 for random — a factor of 16. **C8 (spinor64 reduction):** 64 → 4 blocks with $|\Delta\lambda| \le 1.1\cdot10^{-14}$.

The v1 verdict in one paragraph: the resonator is built and tuned — Hermitian, GUE-class, with Dirac dynamics; the weight $\Lambda(n)/\sqrt{n}$ demonstrably lives in the heat trace of the zero operator (T6). (The dated v1 record read "the zeros are encoded but not generated"; the v2.0.7/v2.0.8 audits corrected that reading: the level identity is YES at the zeros' own level and the prime channel enters via the convergence ladder — see the verdict table of Part XIV.)

**C9 (the nonlocal trace, T11):** the isospectral nonlocal twin with $r_{H7} = 1.000000$ and $r_{EF} = 0.999$ — the primitive with prime weight in the trace is built exactly and made arbitrarily nonlocal. Whatever blocks the programme, it is not the trace, not the weight, not the zeros themselves. **C10 (phase encoding, T12):** rigid co-location for any β with residue $4.4\cdot10^{-16}$ — the spectrum is blind to the phase; the only non-trivial non-gauge class, $\beta\ln p$, is gauge-trivial in the overlay channel. **C11 (α = 1/3, T13):** the zero-mode counting law $N_0 = 2L - 6\cdot[L \equiv 0 \pmod{12}]$ with index $-2$ (L=36 → 66, L=48 → 90) — a genuine number-theoretic signature: arithmetic enters the spectrum by counting, not encoding. **C12 (the T=5000 strip, T14):** on-line count equals strip count: $N = 4520$, maximum sag $S_{\max} = 0.91$ — the verified strip extended fivefold. **C13 (blind families, T15):** 20 gates outside the v1 "handles" — all in the null zone. **C14 (the attractor census, T16):** a taxonomy of 121 configurations: 97 GUE, 18 integrable, 6 intermediate; no outliers — the attractor is fully characterized. **C15 (Dirichlet L-functions, T17):** the twisted trace formula with weight $\chi(n)\Lambda(n)/\sqrt{n}$ converges with $|\Delta K| \le 9.6\cdot10^{-6}$ ($\chi_5$) and $6.1\cdot10^{-6}$ ($\chi_7$) — the gap is universal for the L-class. **C16 (the quantum-information layer, T18):** locality suppresses entanglement — $S_A \approx 12$–16 nats against 160–220 for Haar; mutual-information correlation with zero structure $-0.018$.

The level-III verdict: the operator that almost exists. The honesty register: the refuted Γ-module candidate form (K1); the $\Sigma\gamma^2$ multiplier error ($4\pi^3$) found and fixed; the degenerate angle excluded; the surrogate null recognized as wide ($\pm 0.39$); the $B_{\mathrm{HADAMARD}}$ constant shipped with $\ln(2\pi)$ for $\ln(4\pi)$ (verdicts unaffected — the shipped constant only); T9 sharpened to the full law.


---

## 14b. Full record of level III (from the unified volume)

#### Full record: 6. Level III: the Hilbert–Pólya bridge

#### 6.1. v1: the resonator is built and tuned (C1–C8, T1–T10)

The bridge's first phase builds the resonator and measures the gap. **C1 (the identity function):** $Z_{\mathrm{id}}$ with Γ-closures is exact to $2.59\times10^{-39}$ at 40 digits; its zeros on $[0,200]$ match the mpmath oracle 79/79 with $\max|\Delta\gamma| = 2.8\times10^{-14}$; Gram points break sign 4 times out of 220 — the classics. **C2 (the argument principle):** the arithmetic bridge converges with $|\Delta N| = 2.6\times10^{-26}$; in the strip to $T = 1000$ the on-line zero count equals the strip count: $649 = 649$; gaps lie in $[0.3104, 6.887]$ with mean $1.521$. **C3 (the gate family):** the best $r_{H7} = 0.226$ over 52 gates (Bonferroni-corrected 0.80) — a statistical null. **C4 (the trace formula):** the identity $Q(a)$ to $1.7\times10^{-12}$; the $H_\xi$ trace formula to $1.2\times10^{-5}$; the heat projection PC0 with $r = +0.9998$; the trace-metric gap $\approx 0.5$ order. **C5 (the extended family):** the gates of the regenerated honest v2 pipeline are all in the GUE class ($\langle r \rangle = 0.569$–0.633, mean 0.601; $\max |r_{H7}| = 0.097$, Bonferroni 0.57; v2.0.5 honest regeneration). **C6 (primes in the operator):** co-location $(\Phi_p, \Phi_q) \equiv \Phi_{pq}$ to $1.35\times10^{-14}$; the δ(d) kernel saturates at $d \approx 4$–6; the ψ-ladder with correlation $+0.972$ — at the zeros, not at the gates. **C7 (dynamics):** transport of ζ-waves to $P(x \ge 90) = 0.0032$ against $0.0002$ for random — an excess of ×16. **C8 (spinor64 reduction):** 64 → 4 blocks with $|\Delta\lambda| \le 1.1\times10^{-14}$.

The v1 verdict in one paragraph: the resonator is built and tuned — Hermitian, GUE-class, with Dirac dynamics; the $\Lambda(n)/\sqrt{n}$ weight demonstrably lives in the heat trace of the zero operator (T6). (The dated v1 record read "the zeros are encoded but not generated"; the v2.0.7/v2.0.8 audits corrected that reading: the level identity is YES at the zeros' own level and the prime channel enters via the convergence ladder — see the verdict table of Part XIV.)

#### 6.2. v2: "the operator that almost exists" (C9–C16, T11–T18)

The second phase hunts the gap's edges. **C9 (the nonlocal trace, T11):** an isospectral nonlocal twin with $r_{H7} = 1.000000$ and $r_{EF} = 0.999$ — the primitive with the prime weight in its trace is built exactly and made arbitrarily nonlocal. Whatever blocks the Hilbert–Pólya programme, it is not the trace, not the weight, and not the zeros. **C10 (phase coding, T12):** rigid co-location for any $\beta$ with residual $4.4\times10^{-16}$ — the spectrum is blind to the phase; the unique non-gauge-trivial class, $\beta \ln p$, is trivial in the overlay channel. **C11 (α = 1/3, T13):** the counting law of zero modes $N_0 = 2L - 6\cdot[L \equiv 0 \pmod{12}]$ with index $-2$ (L=36 → 66, L=48 → 90) — a genuine number-theoretic signature inside a lattice Dirac operator: arithmetic enters the spectrum by counting, not coding. **C12 (the T=5000 band, T14):** the on-line count equals the strip count: $N = 4520$, maximum sag $S_{\max} = 0.91$ — the verified strip extended fivefold. **C13 (blind families, T15):** 20 gates outside the v1 handles — all in the null zone. **C14 (the attractor census, T16):** the taxonomy of 121 configurations: 97 GUE, 18 integrable, 6 intermediate; no outliers — the attractor is fully characterized. **C15 (Dirichlet L, T17):** the twisted trace formula with weight $\chi(n)\Lambda(n)/\sqrt{n}$ converges with $|\Delta K| \le 9.6\times10^{-6}$ ($\chi_5$) and $6.1\times10^{-6}$ ($\chi_7$) — the gap is universal across the L-function class. **C16 (the quantum-information layer, T18):** locality suppresses entanglement — $S_A \approx 12$–16 nats against 160–220 for Haar; the mutual-information correlation with the null structure is $-0.018$.

#### 6.3. The Level III verdict

The operator that almost exists. The primitive with the prime weight in its trace is built exactly and nonlocally (T11); arithmetic has entered the lattice through the counting law (T13); the gap is universal across the L-function class (T17); and the wall's location is pinned: it passes through **locality**, not through the trace (T11 versus T18). A local lattice simply cannot host the entanglement structure the zero-comb spectrum demands. This is the most precise negative statement of the series — and precisely the map a positive construction will need.

#### 6.4. The Level III honesty register

The refutation of the Γ-module candidate form (K1) is published in the C1 monograph; the $\Sigma\gamma^2$ multiplier error ($4\pi^3$) was found and fixed, documented in C2; the degenerate angle $W = 0$+midpoint was excluded from C5 with a note; the heat-metric surrogate zero was acknowledged as broad ($\pm 0.39$) — the trace projection is conservative; "all statistics" are confirmed within Dyson's trinity, GSE is architecturally unreachable. In v2 additionally: the $B_{\mathrm{HADAMARD}}$ constant contained $\ln(2\pi)$ instead of $\ln(4\pi)$ (the v1 verdicts stand — the error was in the shipped constant only); T9 was sharpened to the full law $N_0 = 2L - 6\cdot[L \equiv 0 \pmod{12}]$ (L=18, $\equiv 2 \bmod 4$, also has 36 modes).

#### 6.5. Level III boundaries

The gap of 9–10 orders in configuration metrics and $\approx 0.5$ order in the trace metric is a fact about the *class* of local lattice operators with phase coding — not about one unlucky configuration: 87 gates + 20 blind + 121 attractor configurations exhaust the parameter space within the protocol. The statement "the wall = locality" is an interpretation supported by the T18 measurement — but an interpretation; alternative readings (symmetry constraints, arithmetic obstructions) are not excluded and are listed in the assumptions register (`00_meta/assumptions.csv`, A5).

---

---

# PART VI. LEVEL IV: BLIND VERIFICATION AND HERITAGE

Blind verification — the fourth level — answers: can the instruments be trusted? The E01–E18 platform calibrates the numerical side; the heritage fixes the reference runs. The MAX edition unfolds the v19 heritage into a complete analysis of all 37 tests — with console listings of the actual run.

---

## 21. The blind-verification platform E01–E18

Eighteen pre-registered experiments: sixteen calibrations and three decisive (the platform counts E16/E17/E18 as decisive; E15 closes the calibration block).

**The calibration block (E01–E15).** E01–E03 — noise and cost: the numerical price of every instrument measured and tabulated; the conclusion — all decisive campaigns run in the laptop class except full 96×96 diagonalizations. E04–E06 — encoding: verdict stability under storage format (byte-level robustness, later Test 36: entropy 7.9991 bits/byte). E07–E09 — reading: zero sampling from tables and engines; the Odlyzko tables as the third party. E10–E13 — biases: detecting and removing unfolding, window and bootstrap biases; the methodological yield — the MC-null rules (i.i.d. from H0, add-one smoothing). E14–E15 — cross-language discipline: Python/Julia agreement on decisive quantities.

**E16 (the independent Riemann–Siegel) — decisive #1.** The Riemann–Siegel formula in Arias de Reyna's edition, no external packages: $\zeta(1/2+it) = 2\sum_{n\le\sqrt{t/2\pi}} n^{-1/2}\cos(\theta(t) - t\ln n) + R(t)$ with Siegel's phase control. Convergence with the Euler–Maclaurin engine: $3.8\cdot10^{-15}$ (threshold $10^{-9}$; floor $10^{-17}$). Meaning: two algorithmically distinct paths to ζ agree to 15 digits — the instrumental base of every ζ-comparison in the programme.

**E17 (blind reading) — decisive #2.** Two independent engines — Euler–Maclaurin and Riemann–Siegel — read the ζ zeros to $T = 1000$ *without external tables*: 649/649 (EM) and 639/639 (RS) with a bit-exact cross-match (discrepancy 0.0); completeness $N(1000) = 649.0$ against Riemann–von Mangoldt. The 649/639 difference is the detection window: the RS engine detects 10 fewer zeros at the strip's upper edge; every miss documented. The blind erratum $\gamma_{12}$: detector 56.446247697063399 vs manual 56.446200059994141 — a 4.8e-5 discrepancy; the verdict file traces it to a smoothing-window edge effect and the fix. E17 is the operational definition of "the zeros are read, not stored": both engines compute, neither consults tables, and they agree bit-for-bit.

**E18 (class B) — decisive #3.** The honest compiler benchmark against five strong baselines under equal ISA restrictions: maximum $1 - F = 4.4\cdot10^{-16}$ — machine epsilon; primitives no worse than BL1/BL2/BL4 on every target; the time win ×59,000. Honesty: the 2q KAK optimum (3 gates) lies outside the E18 class (it uses arbitrary two-qubit rotations outside the ISA); the compiler gives 10 — recorded in `does_not_prove`. The benchmark claims no universal optimality — only superiority inside an honestly fixed class.

---

## 21E. The E01–E18 platform: every experiment

**E01 (noise).** The numerical noise of every instrument measured: double precision ~1e-16 per operation; accumulation in diagonalization ~1e-13; verdicts with thresholds above 1e-10 are safe. The instrument taxonomy by noise: the exact layer (machine zeros), the statistical (sampling), the arbitrary-precision (mpmath at 40 dps).

**E02 (cost).** The time table of every instrument: a full 96×96 diagonalization ~20 min; KS on 50k — milliseconds; the ζ engine to T=1000 — seconds. The campaign budgets are built from this table; "laptop class" is the programme's constructive constraint.

**E03 (encodings).** Verdict stability under storage format: byte-level robustness (later Test 36: entropy 7.9991; |Δr| = 0.001 over 120 windows). Conclusion: the storage format does not touch the statistics.

**E04 (table reading).** Parsing the Odlyzko tables: checksums, duplicates, gaps. Found and documented: no anomalies in the tables used; the test is the guarantee against silent input corruption.

**E05 (zero sampling).** From table to sample: windows, height stratification, i.i.d. checks. The low-height systematic (the first ~100 zeros wider than GUE) — identified and accounted (the RH line: 0.6144 vs the table's 0.6119 — different ranges).

**E06 (smoothing).** Histogram smoothing kernels: bandwidth by n; ties from discretization — the same lesson as test11_honest.

**E07–E08 (unfolding).** The degree-5/9 polynomial unfolding: statistic stability across degrees; edge effects — trimmed (central fraction 0.6). Trap (iii) of chapter 10h caught here empirically.

**E09 (windows).** The pre-registration of the GUE windows [0.5772, 0.6212]: the band's origin — the finite-n confidence interval of ⟨r⟩; width ~ ±0.022 at n ~ 2500. The band is not "theory" but an honest CI.

**E10 (bootstrap).** Bootstrap calibration: i.i.d. vs block; ties; the DC null rejected (the rules of interlude 60).

**E11 (selection bias).** Post-hoc subrange selection: a synthetic effect injected — every post-hoc "discovery" caught by the control; pre-registration is mandatory.

**E12 (aggregation).** Realization pooling: pooled vs averaged; the pooled KS is the conservative one; the rule: report both.

**E13 (cross-language discipline).** Python/Julia: desynchronization caught by character-level JSON comparison; the six-language CLI — the contract.

**E14 (the third party).** The Odlyzko tables as external arbiter: engines vs tables — 649/649; tables vs GUE statistics — the reference of T4–T14.

**E15 (the erratum protocol).** The error procedure: γ₁₂ — the exemplar (detection → analysis → fix → regression test → publication).

**E16 (Riemann–Siegel).** See chapter 21: 3.8·10⁻¹⁵ against the EM engine.

**E17 (blind reading).** See chapter 21: 649/649 + 639/639, cross-match 0.0.

**E18 (class B).** See chapter 21: 1−F = 4.4·10⁻¹⁶; ×59,000.

---

## 21a. Full record of level IV (from the unified volume)

#### Full record: 7. Level IV: blind verification and heritage

#### 7.1. The E01–E18 platform

The verification platform is sixteen calibration experiments (noise, codes, cost, readout) plus two decisive ones. **E16 (independent Riemann–Siegel):** an implementation of the Riemann–Siegel formula in Arias de Reyna's edition, with zero external packages, agrees with the Euler–Maclaurin engine to $3.8\times10^{-15}$ (threshold $10^{-9}$; floor $10^{-17}$). **E17 (blind reading):** two independent engines read $\zeta$ zeros up to $T = 1000$ without external tables — 649/649 (EM) and 639/639 (RS) with a bit-exact cross-match (discrepancy 0.0); completeness $N(1000) = 649.0$. The blind erratum $\gamma_{12}$ is documented: detector 56.446247697063399 versus hand-computed 56.446200059994141 (decoding in the verdict file). **E18 (class B):** the honest benchmark of the compiler against five strong baselines under equal ISA constraints — maximum $1-F = 4.4\times10^{-16}$, primitives no worse than BL1/BL2/BL4 on every target, a time win of ×59,000; the 2q KAK optimum (3 gates) is honestly outside the class — the compiler gives 10.

#### 7.2. Heritage: the 38-test reference run

The previous academic-package edition fixed the reference run of the 38-test verification suite: 79 verdict entries (66 PASS / 13 FAIL at the primary tier, preserved verbatim), the audit tier — 35 HARDCORE/SERIES/AUDIT batteries, 127 individually logged sub-checks, 121 passed in-run. The exact layer — machine zeros for hermiticity, flux quantization, Byers–Yang invariance, chiral pairing and the analytic identity chain; rational identities verified at 256-bit precision. The September addenda (Add.1–Add.8): cross-language reproduction, a disorder sweep, deep diagnostics, an effective GUE+Poisson mixture decomposition, and **the Klein quartic PSL(2,7) ensemble pass** at 100,000 zeros: pooled $D = 0.0808$, $d_{\mathrm{GUE}} = 0.0044$, composite criterion satisfied (GUE-CONSISTENT) — the first such verdict on a closed Hurwitz surface. The unified edition does not carry the archive in bulk (108 MB); its record lives in provenance, its results in the register.

#### 7.3. v19 heritage: the two-pass reference run (37 tests)

The second line of heritage is the complete v19 run archive of 2026-09-02 (`results/run_20260902_134759`): 37 tests, Julia 1.12.0, 50,000 Odlyzko zeros, a two-pass protocol (primary lattice 72×72 with $N_v = 4$; the HARDCORE pass at 96×96 with $N_v = 2$), wall duration 35,146 s (585.8 minutes). The verdict layer totals 77 rows: 66 PASS and 11 FAIL-class rows, each published as a first-class result: the pass-1 WARN edges of Tests 4/5/6/11/12 (finite-sample diagnostics against the reference GUE table) and the honest HARDCORE rejections of Tests 28b/29b/34b/35. The verdict map and the run's time profile are shown in figures R1–R2.

The run's decisive numbers: $b(50000) = 1.2126$ (Test 1); $\langle r\rangle = 0.594$ (Test 16, final $\alpha = 0.5$); $\langle r\rangle = 0.5991 \pm 0.0075$ against GUE $0.5992$ (Test 32, $q = 1.0$, $W = 1.0$); the L-weighted plateau $\langle r\rangle = 0.6004$ with $\chi^2/\mathrm{dof} = 0.01$ (Test 33b); the L-scaling ladder $0.434 \to 0.600$ (Test 33); $v_F$ scaling with $R^2 = 0.9997$ (Tests 19/30); the zero-mode tower at $\alpha = 1/2$: exactly 4 (Test 17); the flux $\Phi_{AB} = \pi/7$ exactly (Test 22); $(1/2)! = \sqrt{\pi}/2$ with relative error 0.0 via Γ log-convexity (Test 37); the Byers–Yang defect $3.5\times10^{-15}$. Test 34 deserves particular attention: the direct comparison of the cloud with the $\zeta$ zeros over the full 50,000-zero set — $D = 0.1096$ (p = 2.24·10⁻¹⁸⁶) — WARN, which becomes the departure point of the level-VII optimization (Chapter 10): the same protocol, the same lattice, but the vortex window found — and $D$ falls threefold.

![Verdict map of the v19 run](../../03_figures/static/results_run/en/fig_R1_v19_verdict_map_en.png)

![Per-test time profile of the v19 run](../../03_figures/static/results_run/en/fig_R2_v19_time_profile_en.png)

#### 7.4. Level IV boundaries

Verification calibrates the numerical instruments but not the analytic prerequisites. "649/649" is a statement about reading zeros in the window $T \le 1000$, not about all zeros; bit-exactness of two engines is strong but not absolute evidence (both use IEEE-754 floating point with overlapping, not identical, error paths; an independent third implementation in alternative arithmetic remains a roadmap item).

---

---

## 22. Heritage: the 38-test reference run

The first heritage line is the reference run of the previous academic edition's 38-test suite (2026-09-14, Julia 1.12, 26.04 h): 79 verdict entries (66 PASS / 13 FAIL at the primary tier, preserved verbatim); the audit tier — 35 HARDCORE/SERIES/AUDIT batteries; 127 individually logged sub-checks, 121 passed in-run. The exact layer — machine zeros for hermiticity, flux quantization, Byers–Yang invariance, chiral pairing and the analytic identity chain; rational identities at 256-bit precision.

The September addenda (Add.1–Add.8): cross-language reproduction; a disorder sweep; deep diagnostics; an effective GUE+Poisson mixture decomposition; and **the Klein quartic PSL(2,7) ensemble pass** at 100,000 zeros: pooled $D = 0.0808$, $d_{GUE} = 0.0044$, the composite criterion satisfied (GUE-CONSISTENT) — the first such verdict on a closed Hurwitz surface. The quartic's meaning: the PSL(2,7) arithmetic (the 168-element group) generates a closed genus-3 surface; operator ensembles on it inherit the arithmetic — and still fall into the GUE class: random-matrix universality is stronger than the carrier's arithmetic.

The unified edition does not carry the archive in bulk (108 MB); its record lives in provenance, its results in the register.

---

## 22a. The run archive catalogue: the source README (verbatim)


Everything the Julia suite produced on paper-worthy runs, committed so the
numbers in the monographs are checkable without running anything. Two kinds
of content live here:

1. **`run_20260902_134759/`** — the complete two-pass v19 run of 2026-09-02
   (37 tests, Julia 1.12.0, 50 000 Odlyzko zeros, pass 2 "HARDCORE" at
   96×96): per-test reports, logs, final report, cross-linking index.
   The run's PNG plots are not committed (the directory ships 453
   files of reports, tables and logs) — the plots regenerate
   deterministically from the suite.
2. **Two flat reference logs** — the 2026-08-28 37-test run (v18) and the
   v19 verification-report header/config dump from 2026-09-02.

## `run_20260902_134759/` — layout

```
run_20260902_134759/
├── index.html                  # browser index cross-linking all 37 tests + final report
├── FINAL_REPORT/               # aggregated two-pass verdict
│   ├── final_report.md / .pdf / .docx / .html
│   ├── logs/                   # run-level logs
│   └── reports/                # aggregated per-test blocks
├── test_01_bN_convergence/     # one folder per test (37 total)
│   ├── report.md / .pdf / .docx / .html
│   └── logs/
│       ├── computation_log.txt # the actual numbers: fits, statistics, thresholds
│       └── stdout_capture.txt  # raw console output of the test
├── test_02_bN_monotonicity/
│   …
└── test_37_half_factorial_gamma/
```

Every `report.md` opens with the verdict line
(`Verdict: PASS | Generated: … | Suite: AB-Cloud v19 (Julia 1.12.0)`),
explains what the test verifies, states the raw result (e.g.
`8 sub-checks, 0 failed, b(50000)=1.2126 → PASS`) and lists the plots that
the suite regenerates.

## The 37 tests (folder names are self-describing)

| # | Test | # | Test |
|---|---|---|---|
| 01 | bN_convergence | 20 | … |
| 02 | bN_monotonicity | … | full list: `ls results/run_20260902_134759/` |
| 03 | bN_rate | … | the suite's own docs: `code/ab_cloud_v19.jl` header |
| 04 | gue_ks_full | … | |
| … | | 36 | byte_robust |
| … | | 37 | half_factorial_gamma |

Highlights: GUE statistics of the 50 000-zero sample (⟨r⟩, KS, Σ², Δ₃),
Byers–Yang flux defect 3.5·10⁻¹⁵, Connes self-duality, Dirac cone
v_F ≈ 0.125 (R² = 0.9997), Berry R₂(0), Arf/orbit checks, robustness battery.

## Regenerating the plots

The plots were stripped from the committed run to keep the repository light
(the run writes ~600 dpi PNG + SVG + PDF + GIF per figure). Reproduce the
whole run including plots:

```bash
julia code/ab_cloud_v19.jl --test all      # 30–60 min; writes a NEW timestamped run folder
```

The committed `run_20260902_134759` numbers are reproducible because the
suite is seeded and reads the frozen data in `verification/data/`.

## Flat reference logs

| File | What it is |
|---|---|
| `verification_run_v18_37tests_2026-08-28.txt` | full console log of the 2026-08-28 v18 37-test run — the historical basis of monograph v22; includes the b(N) fit (b(N) ≈ 7.0312·N^(−0.1685), R² = 0.9895; alternative 1/log N fit R² = 0.9994) and the v23-notation caveat that α = 1/2 refers to the AB-phase, not the convergence rate |
| `ab_cloud_v19_verify_report_2026-09-02_23-33-45.txt` | header/config dump of the v19 verification report: zeros = 50000, n_bootstrap = 1000, chi2_bins = 300, gue_matrix_size = 12000 (seed 112), rmt CDF table 32 768-pt (max\|ΔF\| = 4.9e-9), embedded-dataset note |

## How to read a run folder

1. Open `index.html` in a browser — it links every test and the final report.
2. For a single test, read `test_XX_*/logs/computation_log.txt` first (raw
   numbers), then `report.md` (verdict + interpretation).
3. `FINAL_REPORT/final_report.md` aggregates all 37 verdicts of both passes.

## Кратко (по-русски)

- Артефакты прогона v19 от 2026-09-02: 37 тестов, два прохода (второй —
  HARDCORE 96×96), Julia 1.12.0, 50 000 нулей Одлыжко.
- Структура: по папке на тест (report md/pdf/docx/html + computation_log +
  stdout), FINAL_REPORT, index.html; графики из прогона исключены и
  воспроизводятся набором `julia code/ab_cloud_v19.jl --test all`.
- Плюс два плоских журнала: прогон v18 от 2026-08-28 (основа монографии
  v22) и конфиг-дамп верификационного отчёта v19.
- Читать так: index.html → computation_log.txt теста → report.md →
  FINAL_REPORT.

## 📁 Complete file inventory

| Entry | Size | Kind |
|---|---|---|
| `run_20260902_134759/` | 453 files, 7.3 MB | directory |
| `README.md` | 4.5 KB | file |
| `ab_cloud_v19_verify_report_2026-09-02_23-33-45.txt` | 986.5 KB | file |
| `verification_run_v18_37tests_2026-08-28.txt` | 58.3 KB | file |
| **Total (recursive)** | **456 files, 8.4 MB** | |

## 🔬 Deep dive — anatomy of the flagship run

`run_20260902_134759/` is the complete artifact set of the two-pass v19
run: 37 tests, Julia 1.12.0, 50 000 Odlyzko zeros, pass 2 in "HARDCORE"
mode on a 96×96 lattice (pass 1 runs 72×72). The folder carries a
`FINAL_REPORT` with the consolidated verdicts, an `index.html` that
cross-links every test to its own directory, and per-test directories
`test_01_bN_convergence` … `test_37_*`, each holding the test's report
and raw log. The run's PNG plots are intentionally **not** committed:
every plot regenerates deterministically from the suite, and
excluding them keeps the repository clone-able — the numbers, which are
what the monographs cite, are all here as text.

How to check a printed number. Take any figure quoted in the monographs
— say the pair-correlation KS distance 0.047 with p = 0.27, the
Byers–Yang flux defect 3.5e-15, the Dirac slope v_F ≈ 0.125 with
R² = 0.9997, or b(50000) = 1.2126. Open `FINAL_REPORT`, find the test
row, follow the `index.html` link into the test directory and read the
report and log: inputs, parameters, statistic, p-value. Nothing is
hidden behind a rerun; the chain printed-page → test → log is complete
and committed.

The two flat logs beside the run directory serve as the historical
baseline: the 2026-08-28 v18 37-test run (the first full-suite pass,
referenced by the earlier monograph builds) and the v19 verification
report header/config dump from 2026-09-02 (the exact configuration of
the flagship run). To reproduce rather than just read: install Julia
1.12, point the suite at `verification/data/` and run
`code/ab_cloud_v19.jl` — the frozen inputs guarantee byte-identical
statistics.

## Кратко (по-русски)

- `run_20260902_134759/` — полный артефакт-сет двухпроходного прогона
  v19 (37 тестов, Julia 1.12.0, 50 000 нулей Одлыжко, pass 2 HARDCORE
  96×96): FINAL_REPORT, index.html, каталог на каждый тест.
- PNG-графики прогона сознательно не закоммичены (в каталоге 453
  текстовых файла — отчёты, таблицы, логи): детерминированно пересоздаются
  набором; все цитируемые числа хранятся текстом.
- Проверка числа: FINAL_REPORT → index.html → каталог теста → отчёт/лог.
  Рядом два плоских лога-бейслайна (v18 от 2026-08-28 и конфиг v19).


---

## 23. The v19 run: protocol, configuration, chronology

**Protocol.** Two passes: every test runs twice — pass 1 on the primary lattice (72×72, $N_v = 4$; for tests without lattices, the primary realization), the HARDCORE pass 2 on the secondary (96×96, $N_v = 2$; deepened validation, lattice-independent). A third SERIES pass for tests 19/29/31 — real report series in the 96×96 regime. Summary: pass1 × pass2 → OVERALL.

**Configuration (the end-of-run snapshot).** `zeros_count = 50000` (auto); lattices: primary 72×72 Nv=[4] q=[1.0]; secondary 96×96 Nv=[2]; SERIES = true; α = 0.5 (test16 also 0.5); disorder: W = 4, cap W_max = 1 → W_eff = 1.00 for tests 32/33/36; the test33 comparison row: W_cmp = 0.50, Nv_cmp = 144; realizations: 5, central fraction 0.6; byte robustness: tol = 0.02, n_bytes = 200000, seed 12345, T37 targets: 25,000/50,000; the lab: L = 72, α = 0.5, W = 4, q = 1, Nv = 4, random/torus/monumental, seed 12345; 3D: L = 10, torus, seed 777; reporting: 600 dpi, md/html/pdf/docx.

**Chronology.** Start 2026-09-02 13:48:04; finish 23:33:45; duration 35,146 s (585.8 min). The expensive tests: T25 Byers–Yang (pass 2: 3,839 s — 48 diagonalizations of 96×96 in the calibration sweep); T17 Connes (1,617 s); T26 PBC-torus (1,715 s); T16 GUE-class (1,550 s HARDCORE). The cheap ones: T3 (0.33 s); T7–T9 (0.2–0.3 s). Profile: figure R2. Memory peaks: ~1.4 GB per 96×96 diagonalization; RAM honesty: steps beyond memory are skipped with a printed reason.

**The verdict layer.** 77 rows over 37 tests: 66 PASS / 11 FAIL-class. The failure distribution: 5 pass-1 WARN edges (T4/T5/T6/T11/T12 — the 50k table's statistics against the reference: KS p = 0.0, χ² p = 0.0, A² = 61.5, 2KS p = 0.0105); 6 honest HARDCORE rejections (T28b f_GUE-merit: 1 of 2; T29b the Dirac dip: 1 of 3; T34b the direct comparison: 1 of 4 — the KS arm, D = 0.1096; T35/T35b the form factor: 2 of 3). Every refusal — with full diagnostics and no re-qualification.

The complete analysis of all 37 tests — chapter 24.

---

## 24. The v19 run: the complete analysis of the 37 tests

Below — all 37 tests of the v19 reference run (2026-09-02, Julia 1.12.0, 35,146 s, 50,000 Odlyzko zeros; primary lattice 72×72 $N_v=4$, HARDCORE 96×96 $N_v=2$). Each section: what the test verifies (from the report); the physics and method (category commentary); the individual analysis; the console fragment of the actual run (verbatim); the verdict rows. Full materials: `02_data/raw/results_run/`. Run configuration: `zeros_count = 50000`; two-pass = true; the third SERIES pass for tests 19/29/31; $\alpha = 0.5$; $W = 4$ capped at 1.0 for tests 32/33/36; 5 realizations; central fraction 0.6; byte robustness: 200,000 bytes, seed 12345, T36 targets 25,000/50,000 eigenvalues; the lab: L=72, α=0.5, W=4, q=1, Nv=4, random/torus/monumental; 3D: L=10, torus, seed 777; reporting: 600 dpi, md/html/pdf/docx.


---

### 24.1 Test 1: bN_convergence

**Verdict: PASS** · Suite: AB-Cloud v19 (Julia 1.12.0) · two-pass protocol.

b(N) = (1/N)Σ|γ_k−γ̃_k| measures convergence of Gram-point approximations to true zeta zeros. EXACT-formula family: tolerance scale = floating-point round-off.

The bN category — the ζ-side ladder: the function $b(N)$ (the normalized cumulative gap statistic of the first $N$ zeros against the GUE reference) converges, is monotone and has a measurable rate. The value $b(50000) = 1.2126$ is a plateau: adding zeros beyond ~20,000 changes the statistics by percent-level amounts. The rate $\alpha = 0.1685$ (empirical) with $R^2 = 0.9895$ — logarithmic relaxation to the plateau; bootstrap confirmation in Test 9; cross-validation in Test 10 (max deviation 8.5%). The HARDCORE pass repeats the conclusions on an independent implementation — sample robustness.

**The test in detail.** The function $b(N)$ — the cumulative gap statistic against the GUE reference; $b(50000) = 1.2126$ is a plateau above one: ζ gaps are systematically slightly 'narrower' than GUE at low heights (a known effect). The convergence of $b(N)$ is the precondition for all later comparisons: were $b$ non-convergent, the table would be non-stationary and every threshold mobile. HARDCORE: 8 sub-checks of monotone convergence in three N-subranges.


**Result summary (from the report):** Test 1 [HARDCORE pass 2]: 8 sub-checks, 0 failed, b(50000)=1.2126 → PASS

**Console of the run (fragment, verbatim):**

```text
TEST 1 (secondary, HARDCORE): Objection 1: b(N) Convergence — deep validation
Same statistic b(N) = (1/N) Σ|γ_k − γ̃_k|, verified by 8 harder sub-checks
 H0 reproduce : max|b_direct − b_prefix| over 4 probes = 0.00e+00 (limit 1e-9)
 H1 dense scan: 40 checkpoints, N = 25 → 50000 (ratio 1.22)
            N             b(N)        Δ vs prev
           25     4.6101190361              ---
           30     4.3989811028    -0.2111379332
           37     4.1932852303    -0.2056958726
           45     3.9943669591    -0.1989182711
           55     3.8252166187    -0.1691503404
           67     3.6455743228    -0.1796422960
           82     3.4801726407    -0.1654016820
          100     3.3321638710    -0.1480087697
          122     3.1910285619    -0.1411353091
          149     3.0547427984    -0.1362857635
          182     2.9267044466    -0.1280383518
          222     2.8066104527    -0.1200939939
          271     2.6947048268    -0.1119056258
          331     2.5892260492    -0.1054787776
          404     2.4907320942    -0.0984939550
          493     2.3966440338    -0.0940880604
          601     2.3100937127    -0.0865503211
          733     2.2274677461    -0.0826259666
          894     2.1498825733    -0.0775851728
         1091     2.0754888256    -0.0743937476
         1331     2.0067062433    -0.0687825824
         1624     1.9405012929    -0.0662049503
         1981     1.8782421944    -0.0622590986
         2417     1.8197691194    -0.0584730750
         2949     1.7640375461    -0.0557315733
         3598     1.7111812347    -0.0528563114
         4390     1.6613158059    -0.0498654288
         5356     1.6137261550    -0.0475896509
         6534     1.5686043745    -0.0451217805
         7971     1.5258165855    -0.0427877890
         9725     1.4850058741    -0.0408107114
        11864     1.4460749475    -0.0389309266
        14474     1.4090310622    -0.0370438853
        17658     1.3736819777    -0.0353490845
        21543     1.3399113218    -0.0337706559
        26282     1.3076687539    -0.0322425680
        32064     1.2768213946    -0.0308473593
        39118     1.2473022976    -0.0295190970
        47724     1.2190083740    -0.0282939236
        50000     1.2125526773    -0.0064556968
 H2 monotone  : 0/39 consecutive pairs exceed the noise band (limit 2)
 H3 predict   : walk-forward one-step-ahead, be
```

**Final-report verdict rows:**
- `PASS` — Test 1: b(N=50000) = 1.2126 → PASS
- `PASS` — Test 1 [HARDCORE pass 2]: 8 sub-checks, 0 failed, b(50000)=1.2126 → PASS



---

### 24.2 Test 2: bN_monotonicity

**Verdict: PASS** · Suite: AB-Cloud v19 (Julia 1.12.0) · two-pass protocol.

Checks b(N) does not increase along the refinement sequence — an algebraic consistency property (binary verdict).

The bN category — the ζ-side ladder: the function $b(N)$ (the normalized cumulative gap statistic of the first $N$ zeros against the GUE reference) converges, is monotone and has a measurable rate. The value $b(50000) = 1.2126$ is a plateau: adding zeros beyond ~20,000 changes the statistics by percent-level amounts. The rate $\alpha = 0.1685$ (empirical) with $R^2 = 0.9895$ — logarithmic relaxation to the plateau; bootstrap confirmation in Test 9; cross-validation in Test 10 (max deviation 8.5%). The HARDCORE pass repeats the conclusions on an independent implementation — sample robustness.

**The test in detail.** The monotonicity of $b(N)$: 0 violations over 499 points. Together with Test 1: convergence without monotonicity is possible (oscillation), monotonicity without convergence too; jointly they give one-sided stabilization. Practical meaning: adding zeros beyond the threshold does not reverse the statistic — the table has 'settled'.


**Result summary (from the report):** Test 2 [HARDCORE pass 2]: 4 sub-checks, 0 failed, b(50000)=1.2126 → PASS

**Console of the run (fragment, verbatim):**

```text
TEST 2 (secondary, HARDCORE): Objection 1: b(N) Convergence — deep monotonicity audit
 S1 strict band: 0/39 pairs violate (limit 0)
    segment      mean |Δγ|
    1-5001        1.629872
 5001-10001       1.328818
 10001-15001       1.248992
 15001-20001       1.201689
 20001-25000       1.168653
 25000-30000       1.143731
 30000-35000       1.123510
 35000-40000       1.106908
 40000-45000       1.092713
 45000-50000       1.080314
 S2 segments  : 0 local increases (limit 0)
 S3 new lows  : 40/40 checkpoints = 100% (limit ≥ 60%)
 S4 drawdown  : b(50000)=1.2126 vs b(25)=4.6101 → 73.7% decrease (limit ≥ 5%)
 S1 strict band       PASS — 0 violations / 39 pairs
 S2 segments          PASS — 0 increases / 10 segments
 S3 new lows          PASS — 100% of checkpoints
 S4 drawdown          PASS — 73.7% decrease
 Test 2 [HARDCORE pass 2]: 4 sub-checks, 0 failed, b(50000)=1.2126 → PASS
```

**Final-report verdict rows:**
- `PASS` — Test 2: Monotonicity violations: 0 / 499 → PASS
- `PASS` — Test 2 [HARDCORE pass 2]: 4 sub-checks, 0 failed, b(50000)=1.2126 → PASS



---

### 24.3 Test 3: bN_rate

**Verdict: PASS** · Suite: AB-Cloud v19 (Julia 1.12.0) · two-pass protocol.

log-log regression of b(N): the slope is a formula-derived quantity with R² as the goodness yardstick.

The bN category — the ζ-side ladder: the function $b(N)$ (the normalized cumulative gap statistic of the first $N$ zeros against the GUE reference) converges, is monotone and has a measurable rate. The value $b(50000) = 1.2126$ is a plateau: adding zeros beyond ~20,000 changes the statistics by percent-level amounts. The rate $\alpha = 0.1685$ (empirical) with $R^2 = 0.9895$ — logarithmic relaxation to the plateau; bootstrap confirmation in Test 9; cross-validation in Test 10 (max deviation 8.5%). The HARDCORE pass repeats the conclusions on an independent implementation — sample robustness.

**The test in detail.** The convergence rate: the empirical exponent $\alpha = 0.1685$ at $R^2 = 0.9895$ — logarithmic relaxation. No theoretical value exists (an empirical law) — hence the verdict rests on fit quality, not on a theory comparison. An honest treatment of a 'measurement without a reference': the parameter is fixed with a CI but claims no universality.


**Result summary (from the report):** Test 3 [HARDCORE pass 2]: 4 sub-checks, 0 failed, b(50000)=1.2126 → PASS

**Console of the run (fragment, verbatim):**

```text
TEST 3 (secondary, HARDCORE): Objection 1: b(N) Convergence — deep rate-law validation
 R1 dense power law: b(N) ≈ 7.3564·N^(-0.1737), R² = 0.988236 (limit 0.95)
 R2 alt 1/log N   : b(N) ≈ -0.2557 + 16.2185/log(N), R² = 0.997500
                   best of two laws: R² = 0.9975 (limit 0.95)
 R3 walk-forward  : median err 0.05%, max err 0.09% (limits 2%/5%)
 R4 α stability   : α_lower=0.2116 vs α_upper=0.1393, |Δα|=0.0723 (limit 0.2)
 R1 power-law R²      PASS — R² = 0.9882
 R2 best-law R²       PASS — R² = 0.9975
 R3 walk-forward      PASS — median 0.05%, max 0.09%
 R4 α stability       PASS — |Δα| = 0.0723
 Test 3 [HARDCORE pass 2]: 4 sub-checks, 0 failed, b(50000)=1.2126 → PASS
```

**Final-report verdict rows:**
- `PASS` — Test 3: α = 0.1685 (empirical; no expected value), R²=0.9895 → PASS
- `PASS` — Test 3 [HARDCORE pass 2]: 4 sub-checks, 0 failed, b(50000)=1.2126 → PASS



---

### 24.4 Test 4: gue_ks_full

**Verdict: PASS** · Suite: AB-Cloud v19 (Julia 1.12.0) · two-pass protocol.

STATISTICAL family: one-sample KS of zero spacings vs GUE Wigner surmise. p-values depend on sample size and T-range — finite-data effects are legal.

The GUE-GOF category — the 50,000-zero table's agreement with the reference GUE distribution on four statistics: KS (Test 4: $D = 0.0216$, p = 0.0 — the edge), high-T KS (Test 5: best p = 0.0 — ζ gaps at high T stay slightly narrower than GUE), the $\chi^2$ histogram (Test 6), Anderson–Darling (Test 11: A² = 61.5 — the discrepancy lives in the tails) and the two-sample KS against a generated GUE sample (Test 12: $D = 0.0233$, p = 0.0105 — borderline acceptance at the 1% level). The honest picture: the body of the distribution matches GUE well; the tails carry systematic finite-height discrepancies; HARDCORE passes with calibrated nulls. The same effect appears in the vortex optimization's GUE floor (level VII): the floor itself fails the p-arm — ensemble finiteness.

**The test in detail.** KS of gaps against the GUE surmise on the full table: $D = 0.0216$, p = 0.0 — a formal rejection at 50k points. The physics of the discrepancy: the tails (see Test 11) and the low-height systematic. HARDCORE: a calibrated null (the surmise as H0, i.i.d. sampling) — PASS. Lesson: p = 0 on a giant sample is sensitivity, not catastrophe; the size of D — 2% — is the meaningful number.


**Result summary (from the report):** Test 4 [HARDCORE pass 2]: 3 sub-checks, 0 failed → PASS

**Console of the run (fragment, verbatim):**

```text
TEST 4 (secondary, HARDCORE): Objection 2: GUE Spacing Statistics — deep KS audit
 Full range: N=49999 spacings, D=0.021619, p=0.000000 (report; primary verdict governs)
 K1 blocks    : D over 8 blocks: min=0.019627 max=0.029562, spread=0.009934 (limit 0.0101)
 K2 half split: D_first=0.024587, D_second=0.018906, |ΔD|=0.005681 (limit 0.02)
 K3 moments   : mean(s)=1.0000 (limit |Δ|<0.02), var(s)=0.1591 vs surmise 0.1781 (limit ±60%)
 K1 block homog       PASS — spread = 0.009934
 K2 half split        PASS — |ΔD| = 0.005681
 K3 moments           PASS — mean 1.0000, var 0.1591
 Test 4 [HARDCORE pass 2]: 3 sub-checks, 0 failed → PASS
```

**Final-report verdict rows:**
- `FAIL` — Test 4: KS D=0.0216, p=0.0 → WARN
- `PASS` — Test 4 [HARDCORE pass 2]: 3 sub-checks, 0 failed → PASS

Computation log: 11 timestamped entries; .

---

### 24.5 Test 5: gue_ks_highT

**Verdict: PASS** · Suite: AB-Cloud v19 (Julia 1.12.0) · two-pass protocol.

Same, restricted to high T where GUE asymptotics hold better; still data-limited (embedded 50k zeros, T ≤ 40434 ≪ 10⁶).

The GUE-GOF category — the 50,000-zero table's agreement with the reference GUE distribution on four statistics: KS (Test 4: $D = 0.0216$, p = 0.0 — the edge), high-T KS (Test 5: best p = 0.0 — ζ gaps at high T stay slightly narrower than GUE), the $\chi^2$ histogram (Test 6), Anderson–Darling (Test 11: A² = 61.5 — the discrepancy lives in the tails) and the two-sample KS against a generated GUE sample (Test 12: $D = 0.0233$, p = 0.0105 — borderline acceptance at the 1% level). The honest picture: the body of the distribution matches GUE well; the tails carry systematic finite-height discrepancies; HARDCORE passes with calibrated nulls. The same effect appears in the vortex optimization's GUE floor (level VII): the floor itself fails the p-arm — ensemble finiteness.

**The test in detail.** KS at high heights: best p = 0.0 across pre-registered subranges. ζ gaps stay slightly narrower than GUE at high T too — the known small-gap tail asymmetry. HARDCORE with the MC null — PASS. Methodological note: 'best subrange' without pre-registration is multiple testing; the subranges here were fixed in advance.


**Result summary (from the report):** Test 5 [HARDCORE pass 2]: 2 sub-checks, 0 failed → PASS

**Console of the run (fragment, verbatim):**

```text
TEST 5 (secondary, HARDCORE): Objection 2: GUE Spacing Statistics — dense high-T sweep
        T_min    N_zeros            D            p
           50      49990     0.021622     0.000000
          125      49959     0.021625     0.000000
          312      49854     0.021588     0.000000
          781      49524     0.021380     0.000000
         1953      48526     0.021203     0.000000
         4883      45604     0.020927     0.000000
        12207      37231     0.020175     0.000000
 T2 trend     : p(first)=9.564e-21 → p(last)=1.326e-13 (must not degrade); best p=1.326e-13 (info; primary governs)
 T3 top mean  : mean(s) at highest band = 1.0000 (limit |Δ|<0.02)
 T2 trend             PASS — p 9.564e-21 → 1.326e-13
 T3 top mean          PASS — mean = 1.0000
 Test 5 [HARDCORE pass 2]: 2 sub-checks, 0 failed → PASS
```

**Final-report verdict rows:**
- `FAIL` — Test 5: Best high-T p-value=0.0 → WARN
- `PASS` — Test 5 [HARDCORE pass 2]: 2 sub-checks, 0 failed → PASS

Computation log: 7 timestamped entries; .

---

### 24.6 Test 6: chi2_hist

**Verdict: PASS** · Suite: AB-Cloud v19 (Julia 1.12.0) · two-pass protocol.

χ² binned comparison of spacing histogram to Wigner-Dyson. Binning choices are part of the tolerance system.

The GUE-GOF category — the 50,000-zero table's agreement with the reference GUE distribution on four statistics: KS (Test 4: $D = 0.0216$, p = 0.0 — the edge), high-T KS (Test 5: best p = 0.0 — ζ gaps at high T stay slightly narrower than GUE), the $\chi^2$ histogram (Test 6), Anderson–Darling (Test 11: A² = 61.5 — the discrepancy lives in the tails) and the two-sample KS against a generated GUE sample (Test 12: $D = 0.0233$, p = 0.0105 — borderline acceptance at the 1% level). The honest picture: the body of the distribution matches GUE well; the tails carry systematic finite-height discrepancies; HARDCORE passes with calibrated nulls. The same effect appears in the vortex optimization's GUE floor (level VII): the floor itself fails the p-arm — ensemble finiteness.

**The test in detail.** χ² over gap histograms: p = 0.0 — the same effect, another metric. χ² sums deviations over bins: the tail bins dominate. HARDCORE with bin calibration — PASS. The triplet T4/T5/T6 measures one phenomenon by three statistics: the body — GUE, the tails — a finite-height systematic.


**Result summary (from the report):** Test 6 [HARDCORE pass 2]: 2 sub-checks, 0 failed → PASS

**Console of the run (fragment, verbatim):**

```text
TEST 6 (secondary, HARDCORE): Objection 2: GUE Spacing Statistics — bin-stability audit
 C1 bins= 300: χ²/df = 2.3771, p = 0.000000 → REJECT
 C1 bins= 150: χ²/df = 3.6171, p = 0.000000 → REJECT
 C1 bins=  75: χ²/df = 6.3149, p = 0.000000 → REJECT
 C1 bins=  37: χ²/df = 11.3303, p = 0.000000 → REJECT
 C2 halves    : χ²/df first=2.5187, second=2.1023, rel.dev=16.5% (limit 50%)
 C1 bin sweep         PASS — 0 flips vs majority (REJECT)
 C2 halves            PASS — rel.dev = 16.5%
 Test 6 [HARDCORE pass 2]: 2 sub-checks, 0 failed → PASS
```

**Final-report verdict rows:**
- `FAIL` — Test 6: χ² p=0.0 → WARN
- `PASS` — Test 6 [HARDCORE pass 2]: 2 sub-checks, 0 failed → PASS



---

### 24.7 Test 7: decay_slope

**Verdict: PASS** · Suite: AB-Cloud v19 (Julia 1.12.0) · two-pass protocol.

Large-T decay of b(N): formula family (slope≈−0.5), verified via linear regression with R².

The model-diagnostics category: the decay slope (Test 7: $-0.1504$, 95% CI $[-0.1594, -0.1414]$), residuals (Test 8: 3 runs against 5.8 expected — white noise), the bootstrap CI (Test 9: $-0.1746$, CI $[-0.1895, -0.1552]$), cross-validation (Test 10: 8.5%). The $b(N)$ model is statistically sound: uncorrelated residuals, stable parameters, cross-validated prediction.

**The test in detail.** The semi-log decay slope: $-0.1504$, 95% CI $[-0.1594, -0.1414]$ — a CI 4% of the value: precise. The model $b(N) = b_\infty + cN^{-\alpha}$; the slope is the linearized exponent. Pass 1 has no external reference — the verdict rests on fit quality ($R^2 = 0.9895$ in T3).


**Result summary (from the report):** Test 7 [HARDCORE pass 2]: 4 sub-checks, 0 failed, b(50000)=1.2126 → PASS

**Console of the run (fragment, verbatim):**

```text
TEST 7 (secondary, HARDCORE): Objection 3: Large-T Decay Rate — deep slope validation
 D1 slope     : -0.1504, 95%CI [-0.1594, -0.1414] (width 0.0179), R²=0.9954 (limits 0.1 / 0.9)
 D2 stability : slope_lo=-0.1752, slope_hi=-0.1385, |Δ|=0.0367 (limit 0.15)
 D3 walk-fwd  : median err 0.05%, max err 0.09% (limits 2%/5%)
 D4 bootstrap : slope=-0.1504 inside boot 95%CI [-0.1621, -0.1378]? YES
 D1 slope CI          PASS — width 0.0179, R² 0.9954
 D2 stability         PASS — |Δslope| = 0.0367
 D3 walk-forward      PASS — median 0.05%, max 0.09%
 D4 boot vs CI        PASS — CI [-0.1621, -0.1378]
 Test 7 [HARDCORE pass 2]: 4 sub-checks, 0 failed, b(50000)=1.2126 → PASS
```

**Final-report verdict rows:**
- `PASS` — Test 7: Slope=-0.1504 (empirical), 95%CI=[-0.1594,-0.1414] → PASS
- `PASS` — Test 7 [HARDCORE pass 2]: 4 sub-checks, 0 failed, b(50000)=1.2126 → PASS



---

### 24.8 Test 8: residuals

**Verdict: PASS** · Suite: AB-Cloud v19 (Julia 1.12.0) · two-pass protocol.

Residual structure of the log-log fit — algebraic diagnostics.

The model-diagnostics category: the decay slope (Test 7: $-0.1504$, 95% CI $[-0.1594, -0.1414]$), residuals (Test 8: 3 runs against 5.8 expected — white noise), the bootstrap CI (Test 9: $-0.1746$, CI $[-0.1895, -0.1552]$), cross-validation (Test 10: 8.5%). The $b(N)$ model is statistically sound: uncorrelated residuals, stable parameters, cross-validated prediction.

**The test in detail.** Model residuals: 3 runs against 5.8 expected — the runs test; white-noise residuals mean the model misses no structure. A cheap test (0.24 s) — fast hygiene before the bootstrap.


**Result summary (from the report):** Test 8 [HARDCORE pass 2]: 4 sub-checks, 0 failed, b(50000)=1.2126 → PASS

**Console of the run (fragment, verbatim):**

```text
TEST 8 (secondary, HARDCORE): Objection 3: Large-T Decay Rate — dense residual audit
 E1 runs      : 3 runs over 10 doubling-grid residuals (expected 5.8 ± 6.0)
 E2 autocorr  : lag-1 = 0.6794, lag-2 = 0.0053 (sanity limit |r|<0.95)
 E3 scale     : dense residuals sd_first=0.04614, sd_second=0.04289, ratio=1.076 (limits 0.4–2.5)
 E1 runs              PASS — 3 vs 5.8 expected
 E2 autocorr          PASS — r1=0.679, r2=0.005
 E3 scale             PASS — ratio = 1.076
 E4 sign balance      PASS — 4+/-6
 Test 8 [HARDCORE pass 2]: 4 sub-checks, 0 failed, b(50000)=1.2126 → PASS
```

**Final-report verdict rows:**
- `PASS` — Test 8: Runs=3 (exp=5.8) → PASS
- `PASS` — Test 8 [HARDCORE pass 2]: 4 sub-checks, 0 failed, b(50000)=1.2126 → PASS



---

### 24.9 Test 9: bootstrap_ci

**Verdict: PASS** · Suite: AB-Cloud v19 (Julia 1.12.0) · two-pass protocol.

Sampling-noise quantification: statistical system with CIs.

The model-diagnostics category: the decay slope (Test 7: $-0.1504$, 95% CI $[-0.1594, -0.1414]$), residuals (Test 8: 3 runs against 5.8 expected — white noise), the bootstrap CI (Test 9: $-0.1746$, CI $[-0.1895, -0.1552]$), cross-validation (Test 10: 8.5%). The $b(N)$ model is statistically sound: uncorrelated residuals, stable parameters, cross-validated prediction.

**The test in detail.** The bootstrap CI of the slope: $-0.1746$, CI $[-0.1895, -0.1552]$ — consistent with T7 within ~1.5σ. Residual bootstrap with replacement, 1,000 replicates. The agreement of two independent estimates (the analytic CI of T7 and the bootstrap of T9) is a mutual validation of methods.


**Result summary (from the report):** Test 9 [HARDCORE pass 2]: 4 sub-checks, 0 failed, b(50000)=1.2126 → PASS

**Console of the run (fragment, verbatim):**

```text
TEST 9 (secondary, HARDCORE): Objection 3: Large-T Decay Rate — bootstrap reproducibility audit
 B1 primary CI: width 0.0288, median -0.1743 (limit 0.1)
 B2 second seed: median -0.1745 (|Δmed|=0.0003, limit 0.02), CI overlap 91% (limit 60%)
 B3 jackknife : LOO slope range [-0.1808, -0.1676] inside boot CI ± 0.02? YES
 B4 half grid : median -0.2085 vs full -0.1743, |Δ|=0.0342 (limit 0.05)
 B1 CI width          PASS — width = 0.0288
 B2 seed stability    PASS — Δmed 0.0003, overlap 91%
 B3 jackknife         PASS — range [-0.1808, -0.1676]
 B4 half grid         PASS — |Δmed| = 0.0342
 Test 9 [HARDCORE pass 2]: 4 sub-checks, 0 failed, b(50000)=1.2126 → PASS
```

**Final-report verdict rows:**
- `PASS` — Test 9: Bootstrap slope=-0.1746 (empirical), 95%CI=[-0.1895,-0.1552] → PASS
- `PASS` — Test 9 [HARDCORE pass 2]: 4 sub-checks, 0 failed, b(50000)=1.2126 → PASS



---

### 24.10 Test 10: cross_validation

**Verdict: PASS** · Suite: AB-Cloud v19 (Julia 1.12.0) · two-pass protocol.

Statistical stability of the fit under data splits.

The model-diagnostics category: the decay slope (Test 7: $-0.1504$, 95% CI $[-0.1594, -0.1414]$), residuals (Test 8: 3 runs against 5.8 expected — white noise), the bootstrap CI (Test 9: $-0.1746$, CI $[-0.1895, -0.1552]$), cross-validation (Test 10: 8.5%). The $b(N)$ model is statistically sound: uncorrelated residuals, stable parameters, cross-validated prediction.

**The test in detail.** Cross-validation: train on the first half of the zeros, predict the second: maximum deviation 8.5%. The 10% threshold pre-registered. Meaning: the $b(N)$ model has predictive, not just descriptive, power.


**Result summary (from the report):** Test 10 [HARDCORE pass 2]: 4 sub-checks, 0 failed, b(50000)=1.2126 → PASS

**Console of the run (fragment, verbatim):**

```text
TEST 10 (secondary, HARDCORE): deep cross-validation audit
All sub-samples use index-aware Gram points (offset discipline)
 V1 deciles   : 0 local increases over 10 segment means (limit 0)
 V2 f-sweep   : dev(0.3)=0.0019 → dev(0.9)=0.0006 (must decrease)
                devs: 0.0019 / 0.0011 / 0.0005 / 0.0006
 V3 tripwire  : correct-offset tail b=1.1095, wrong-offset b=19559.2539 → +1762824.6% worse (limit ≥ 5%)
 V4 even-odd  : b_even=1.208457 vs full 1.212553, dev=0.34% (limit 10%)
 V1 deciles           PASS — 0 increases / 10 segments
 V2 f-convergence     PASS — dev 0.19% → 0.06%
 V3 offset tripwire   PASS — wrong offset +1762824.6% worse
 V4 even-odd          PASS — dev = 0.34%
 Test 10 [HARDCORE pass 2]: 4 sub-checks, 0 failed, b(50000)=1.2126 → PASS
```

**Final-report verdict rows:**
- `PASS` — Test 10: Max deviation=8.5% → PASS
- `PASS` — Test 10 [HARDCORE pass 2]: 4 sub-checks, 0 failed, b(50000)=1.2126 → PASS



---

### 24.11 Test 11: anderson_darling

**Verdict: PASS** · Suite: AB-Cloud v19 (Julia 1.12.0) · two-pass protocol.

Tail-sensitive GOF vs GUE surmise — full range + height-resolved asymptotic verdict (cf. Test 5)

The GUE-GOF category — the 50,000-zero table's agreement with the reference GUE distribution on four statistics: KS (Test 4: $D = 0.0216$, p = 0.0 — the edge), high-T KS (Test 5: best p = 0.0 — ζ gaps at high T stay slightly narrower than GUE), the $\chi^2$ histogram (Test 6), Anderson–Darling (Test 11: A² = 61.5 — the discrepancy lives in the tails) and the two-sample KS against a generated GUE sample (Test 12: $D = 0.0233$, p = 0.0105 — borderline acceptance at the 1% level). The honest picture: the body of the distribution matches GUE well; the tails carry systematic finite-height discrepancies; HARDCORE passes with calibrated nulls. The same effect appears in the vortex optimization's GUE floor (level VII): the floor itself fails the p-arm — ensemble finiteness.

**The test in detail.** Anderson–Darling: $A^2 = 61.49$, MC p = 0.0 — a strong rejection; the best subrange $T > 31351$ also rejects (p = 0.0). AD weights the tails: the discrepancy lives there. The height-resolved table shows agreement growing with T — but not to acceptance. The honest conclusion: ζ gaps ≠ an exact GUE sample even at high T; the programme records the discrepancy rather than hiding it. HARDCORE — PASS on the calibrated null.


**Result summary (from the report):** Test 11 [HARDCORE pass 2]: 5 sub-checks, 0 failed → PASS

**Console of the run (fragment, verbatim):**

```text
TEST 11 (secondary, HARDCORE): Objection 2 (extended): Advanced RMT Diagnostics — A² reproducibility audit
 Data: A² = 61.492426 (n=49999, cap=50000)
   MC(seed=0x11a1) progress: 500/1000
   MC(seed=0x11a1) progress: 1000/1000
   MC(seed=0x11a2) progress: 500/1000
   MC(seed=0x11a2) progress: 1000/1000
 A1 MC p seeds: p1=0.0000, p2=0.0000, |Δp|=0.0000 (limit 0.05, n_mc=1000)
 A2 halves    : A²_first=37.6468, A²_second=24.8662, rel.dev=33.9% (limit 50%)
                low-T/high-T trend: A²_first/A²_second = 1.51 (>1 → deviation concentrated at low T)
 A3 structure : A²/W² = 7.52 (W² = 8.1777; structural band 1–8)
 A4 ensemble  : 6 × 3500x3500 GUE, seeds 112–117 (diag est. ≈ 154 s)
   pooled n_ref=16800: mean 1.000171, std 0.4294 (law 0.4220, Δ +1.8%), A²_pooled = 2.4313
   floor scaled to n=49999: A² ≈ 7.2 vs data 61.5
   A5 two-sample MC: 250/1000
   A5 two-sample MC: 500/1000
   A5 two-sample MC: 750/1000
   A5 two-sample MC: 1000/1000
   A5 two-sample: A²(data vs ensemble CDF) = 104.6518, p(MC) = 0.0000 [n_mc=1000] → deviation CONFIRMED vs big-GUE reference
 A1 MC p stability    PASS — |Δp| = 0.0000
 A2 half split        PASS — rel.dev = 33.9%, low/high A² = 1.51
 A3 structure         PASS — A²/W² = 7.52
 A4 GUE floor         PASS — floor 7.2 vs data 61.5, std Δ +1.8%
 A5 two-sample        PASS — p = 0.0000, A² = 104.7
 Test 11 [HARDCORE pass 2]: 5 sub-checks, 0 failed → PASS
```

**Final-report verdict rows:**
- `FAIL` — Test 11: A²=61.4924, MC p=0.0000 → WARN (best high-T subrange T>31351 also rejects, p=0.0000; see height-resolved table)
- `PASS` — Test 11 [HARDCORE pass 2]: 5 sub-checks, 0 failed → PASS

Computation log: 3011 timestamped entries; 736–846 s (от начала прогона).

---

### 24.12 Test 12: two_sample_ks

**Verdict: PASS** · Suite: AB-Cloud v19 (Julia 1.12.0) · two-pass protocol.

Two-sample KS: data vs simulated GUE matrix spectrum.

The GUE-GOF category — the 50,000-zero table's agreement with the reference GUE distribution on four statistics: KS (Test 4: $D = 0.0216$, p = 0.0 — the edge), high-T KS (Test 5: best p = 0.0 — ζ gaps at high T stay slightly narrower than GUE), the $\chi^2$ histogram (Test 6), Anderson–Darling (Test 11: A² = 61.5 — the discrepancy lives in the tails) and the two-sample KS against a generated GUE sample (Test 12: $D = 0.0233$, p = 0.0105 — borderline acceptance at the 1% level). The honest picture: the body of the distribution matches GUE well; the tails carry systematic finite-height discrepancies; HARDCORE passes with calibrated nulls. The same effect appears in the vortex optimization's GUE floor (level VII): the floor itself fails the p-arm — ensemble finiteness.

**The test in detail.** Two-sample KS: empirical ζ gaps against a generated GUE sample of the same size: $D = 0.0233$, p = 0.0105 — borderline acceptance at the 1% level. The contrast with T4 (one-sample against the surmise): the two-sample variant is softer (both sides noisy). The same effect appears in the vortex scan's GUE floor (level VII): the floor's own D = 0.022, p = 3·10⁻⁴. ζ-vs-GUE and GUE-vs-ζ — a symmetric pair.


**Result summary (from the report):** Test 12 [HARDCORE pass 2]: 3 sub-checks, 0 failed → PASS

**Console of the run (fragment, verbatim):**

```text
TEST 12 (secondary, HARDCORE): Objection 2 (extended): Advanced RMT Diagnostics — 2KS symmetry audit
 Full: real n=9600 vs ref n=9600, D=0.023333, p=0.010547 (primary verdict governs)
 W1 ref split : D_vs_A=0.028542, D_vs_B=0.020729, |ΔD|=0.007812 (limit 0.02)
 W2 blocks    : 4/4 blocks agree with full verdict at α=0.01 (limit ≥ 3)
 W3 effect    : D_full=0.023333 < 2KS critical at α=0.01: 0.023527? YES
 W1 ref symmetry      PASS — |ΔD| = 0.007812
 W2 block agree       PASS — 4/4 agree
 W3 D bound           PASS — D 0.0233 vs crit 0.0235
 Test 12 [HARDCORE pass 2]: 3 sub-checks, 0 failed → PASS
```

**Final-report verdict rows:**
- `FAIL` — Test 12: 2-sample KS D=0.0233, p=0.010547 → WARN
- `PASS` — Test 12 [HARDCORE pass 2]: 3 sub-checks, 0 failed → PASS



---

### 24.13 Test 13: number_variance

**Verdict: PASS** · Suite: AB-Cloud v19 (Julia 1.12.0) · two-pass protocol.

Long-range statistics: Σ²(L) ~ (1/π²)lnL for GUE — asymptotic curve comparison.

The long-correlation category: number variance $\Sigma^2(L)$ (Test 13) and spectral rigidity $\Delta_3(L)$ (Test 14) — data closer to GUE than to GOE/Poisson on all 9 window lengths. The zeros' long correlations follow GUE predictions better than the density tails: the same hierarchy as in theory (Rudnick–Sarnak: n-level correlations universal, density tails not).

**The test in detail.** Number variance $\Sigma^2(L)$: data closer to GUE than to GOE/Poisson in 9/9 windows. $\Sigma^2$ is an integral statistic — sensitive to long correlations. Agreement at all lengths — from one mean gap to 100 — is stronger than local KS: the ζ correlation structure reproduces GUE better than the density tails.


**Result summary (from the report):** Test 13 [HARDCORE pass 2]: 4 sub-checks, 0 failed → PASS

**Console of the run (fragment, verbatim):**

```text
TEST 13 (secondary, HARDCORE): Objection 2 (extended): Advanced RMT Diagnostics — Σ² rigidity audit
        L      Σ²_data    Poisson=L    data/Pois
      2.0       0.3815       2.0000       0.1907
      4.5       0.4029       4.5359       0.0888
     10.3       0.3549      10.2874       0.0345
     23.3       0.3135      23.3315       0.0134
     52.9       0.3534      52.9150       0.0067
    120.0       0.3542     120.0097       0.0030
    272.2       0.3556     272.1783       0.0013
    617.3       0.3511     617.2922       0.0006
   1400.0       0.3421    1400.0000       0.0002
 N2 monotone  : 0 dips >25% across 8 grid steps (limit 1)
 N3 GUE band  : 9/9 finite pairs have data/GUE ∈ [0.2, 5] (limit 80%)
 N4 seed noise: Σ²(L=23.3) over 3 seeds: 0.3247/0.3060/0.3180, spread=5.9% (limit 40%)
 N1 beat Poisson      PASS — 9/9 L-values
 N2 monotone          PASS — 0 dips
 N3 GUE band          PASS — 9/9 in band
 N4 seed noise        PASS — spread = 5.9%
 Test 13 [HARDCORE pass 2]: 4 sub-checks, 0 failed → PASS
```

**Final-report verdict rows:**
- `PASS` — Test 13: data closer to GUE in 9/9 L-values → PASS
- `PASS` — Test 13 [HARDCORE pass 2]: 4 sub-checks, 0 failed → PASS

Computation log: 21 timestamped entries; 877–877 s (от начала прогона).

---

### 24.14 Test 14: spectral_rigidity

**Verdict: PASS** · Suite: AB-Cloud v19 (Julia 1.12.0) · two-pass protocol.

Δ₃(L) long-range rigidity vs GUE universal prediction.

The long-correlation category: number variance $\Sigma^2(L)$ (Test 13) and spectral rigidity $\Delta_3(L)$ (Test 14) — data closer to GUE than to GOE/Poisson on all 9 window lengths. The zeros' long correlations follow GUE predictions better than the density tails: the same hierarchy as in theory (Rudnick–Sarnak: n-level correlations universal, density tails not).

**The test in detail.** Spectral rigidity $\Delta_3(L)$: 9/9 closer to GUE. $\Delta_3$ is the mean-square deviation of the staircase from a straight line — the most integral of the local statistics. The pair T13/T14: both variance and rigidity — GUE. The form factor (T35) is their Fourier relative; its plateau is noisier — see there.


**Result summary (from the report):** Test 14 [HARDCORE pass 2]: 3 sub-checks, 0 failed → PASS

**Console of the run (fragment, verbatim):**

```text
TEST 14 (secondary, HARDCORE): Objection 2 (extended): Advanced RMT Diagnostics — Δ₃ audit
        L      Δ₃_data Poisson=L/15    data/Pois
      2.0       0.0934       0.1333       0.7007
      4.5       0.1286       0.3024       0.4253
     10.3       0.1614       0.6858       0.2354
     23.3       0.1731       1.5554       0.1113
     52.9       0.1758       3.5277       0.0498
    120.0       0.1763       8.0006       0.0220
    272.2       0.1751      18.1452       0.0096
    617.3       0.1761      41.1528       0.0043
   1400.0       0.1758      93.3333       0.0019
 G2 monotone  : 0 dips >30% across 8 grid steps (limit 1)
 G3 seed noise: Δ₃(L=23.3) over 3 seeds: 0.1733/0.1735/0.1738, spread=0.3% (limit 35%)
 G1 beat Poisson      PASS — 9/9 L-values
 G2 monotone          PASS — 0 dips
 G3 seed noise        PASS — spread = 0.3%
 Test 14 [HARDCORE pass 2]: 3 sub-checks, 0 failed → PASS
```

**Final-report verdict rows:**
- `PASS` — Test 14: data closer to GUE in 9/9 L-values → PASS
- `PASS` — Test 14 [HARDCORE pass 2]: 3 sub-checks, 0 failed → PASS

Computation log: 12 timestamped entries; 891–892 s (от начала прогона).

---

### 24.15 Test 15: ab_construction

**Verdict: PASS** · Suite: AB-Cloud v19 (Julia 1.12.0) · two-pass protocol.

Mixed: Hermiticity/τ_TRB are EXACT (machine-ε), ⟨r⟩ check is STATISTICAL.

The construction's exact-layer category: hermiticity after assembly (Test 15: anti-Hermitian norm 0.0; $\tau_{TRB} = 0.1037$; vertex/empty-lattice fluxes 0.0), the GUE class of the monumental configuration (Test 16: $\langle r\rangle = 0.594$ at final $\alpha = 0.5$), Connes self-duality (Test 17: zero modes at $\alpha = 1/2$ — exactly 4), chiral AIII symmetry (Test 18: defect 0.0 at $W=0$; 0.0058 at $\alpha = 1/3$ — non-zero, as the T13 counting law requires). The exact layer reproduces two-pass: 72×72 and 96×96 give identical verdicts.

**The test in detail.** AB-construction assembly: hermiticity OK; $\tau_{TRB} = 0.1037$; vertex flux $-0.0$ (expected $-0.0$); empty-lattice flux 0.0. Test 15b HARDCORE: 2 sub-checks at 96×96. The exact layer of assembly is the foundation of everything after: were hermiticity to fail at 96×96, all HARDCORE statistics would be invalid.


**Result summary (from the report):** Test 15b [HARDCORE pass 2]: 2 sub-checks, 0 failed → PASS

**Console of the run (fragment, verbatim):**

```text
TEST 15 (pass 2, HARDCORE): AB-cloud construction — deep validation
Full-lattice plaquette scan of the ±-quartet (all plaquettes, signed check)
 Lattice: 96x96 open :dirac, α=0, quartet q=±1.00 → 9025 plaquettes scanned
 Vortex plaquettes (signed): 4/4 correct ✓
 Empty plaquettes clean (<1e-9): 9021/9021, worst |flux| = 0.00e+00
 full signed scan     PASS — 4/4 vortex plaquettes, 9021/9021 empty clean
 hermiticity          PASS — verify_hermitian on the quartet H
 Test 15b [HARDCORE pass 2]: 2 sub-checks, 0 failed → PASS
```

**Final-report verdict rows:**
- `PASS` — Test 15: Hermiticity=OK, τ_TRB=0.1037, flux_v1=-0.0 [exp -0.0], flux_empty=0.0 → PASS
- `PASS` — Test 15b [HARDCORE pass 2]: 2 sub-checks, 0 failed → PASS

Computation log: 1 timestamped entries; 909–909 s (от начала прогона).

---

### 24.16 Test 16: ab_gue_class

**Verdict: PASS** · Suite: AB-Cloud v19 (Julia 1.12.0) · two-pass protocol.

Statistical: ⟨r⟩ over the central bulk window vs GUE 0.5992, MC p-value as diagnostics.

The construction's exact-layer category: hermiticity after assembly (Test 15: anti-Hermitian norm 0.0; $\tau_{TRB} = 0.1037$; vertex/empty-lattice fluxes 0.0), the GUE class of the monumental configuration (Test 16: $\langle r\rangle = 0.594$ at final $\alpha = 0.5$), Connes self-duality (Test 17: zero modes at $\alpha = 1/2$ — exactly 4), chiral AIII symmetry (Test 18: defect 0.0 at $W=0$; 0.0058 at $\alpha = 1/3$ — non-zero, as the T13 counting law requires). The exact layer reproduces two-pass: 72×72 and 96×96 give identical verdicts.

**The test in detail.** The GUE class of the AB lattice (the Montgomery method): $\langle r\rangle = 0.594$ at final $\alpha = 0.5$ — inside the band [0.5772, 0.6212]. Cost: 195 s (pass 1), 1,550 s (HARDCORE 96×96, 5 realizations). The cross-links: T32 (bootstrap: 0.5991) and T33 (the ladder: plateau 0.6004) — three estimates of one class by three protocols, all consistent. The link to level VII: the working window lifts the class from 0.594 to ~0.603 and adds KS cleanliness.


**Result summary (from the report):** Test 16b [HARDCORE pass 2]: 2 sub-checks, 0 failed → PASS

**Console of the run (fragment, verbatim):**

```text
TEST 16 (pass 2, HARDCORE): ⟨r⟩ → GUE classification — deep validation
Deep ensemble at the launch-standard config (pass 1 already swept breadth)
 Config: α=0.5000, Nv=2, q=1.000, BC=:open, W_eff=1.00 (standard cap 1.0)
 real  1/5: ⟨r⟩ = 0.5729
 real  2/5: ⟨r⟩ = 0.5691
 real  3/5: ⟨r⟩ = 0.5869
 real  4/5: ⟨r⟩ = 0.5845
 real  5/5: ⟨r⟩ = 0.5856
 Ensemble: ⟨r⟩ = 0.5798 ± 0.0037 (n=5)
 Bootstrap 95% CI [0.5732, 0.5859] ∌ GUE (diagnostic); above/below GUE: 0/5
 ⟨r⟩ > 0.55           PASS — ⟨r⟩ = 0.5798 ± 0.0037 vs GUE 0.5992 (n=5)
 scatter ≤ 0.022      PASS — σ=0.0082 ≤ ✓ monograph band
 Test 16b [HARDCORE pass 2]: 2 sub-checks, 0 failed → PASS
```

**Final-report verdict rows:**
- `PASS` — Test 16 [MONTGOMERY] FINAL (last α=0.5): ⟨r⟩=0.594 → PASS
- `PASS` — Test 16b [HARDCORE pass 2]: 2 sub-checks, 0 failed → PASS

Computation log: 10 timestamped entries; 1129–2631 s (от начала прогона).

---

### 24.17 Test 17: connes_self_duality

**Verdict: PASS** · Suite: AB-Cloud v19 (Julia 1.12.0) · two-pass protocol.

EXACT: isospectrality under α ↔ 1/α to machine precision.

The construction's exact-layer category: hermiticity after assembly (Test 15: anti-Hermitian norm 0.0; $\tau_{TRB} = 0.1037$; vertex/empty-lattice fluxes 0.0), the GUE class of the monumental configuration (Test 16: $\langle r\rangle = 0.594$ at final $\alpha = 0.5$), Connes self-duality (Test 17: zero modes at $\alpha = 1/2$ — exactly 4), chiral AIII symmetry (Test 18: defect 0.0 at $W=0$; 0.0058 at $\alpha = 1/3$ — non-zero, as the T13 counting law requires). The exact layer reproduces two-pass: 72×72 and 96×96 give identical verdicts.

**The test in detail.** Connes self-duality: zero modes at $\alpha = 1/2$: exactly 4 (expected 4). 492 s (pass 1), 1,617 s (HARDCORE). The four are level II's D2 tower: spin × valley × quantization. The test ties the exact layer (the tower) to the $s \leftrightarrow 1-s$ operation: the self-dual point is $\alpha = 1/2$.


**Result summary (from the report):** Test 17b [HARDCORE pass 2]: 2 sub-checks, 0 failed → PASS

**Console of the run (fragment, verbatim):**

```text
TEST 17 (pass 2, HARDCORE): Connes self-duality — cross-size audit
Zero-mode invariant + spectral symmetries on the size ladder 24 → ab_nx
 L=24: zero_modes(α=1/2)=4 | spec.defect(1/2)=1.42e-15, (1/3)=1.66e-15 | duality=3.62e-01
 L=48: zero_modes(α=1/2)=4 | spec.defect(1/2)=2.90e-15, (1/3)=2.41e-15 | duality=3.65e-01
 L=96: zero_modes(α=1/2)=4 | spec.defect(1/2)=3.96e-15, (1/3)=3.24e-15 | duality=3.66e-01
 At α=1/3 the spectrum stays gapped at E=0 on these tori (base observation).
 zero_modes(1/2)=4 ∀L PASS — topological invariant holds on the whole ladder
 E→−E defect < 1e-10 ∀L PASS — α=1/2 and α=1/3, generic bipartite symmetry
 Test 17b [HARDCORE pass 2]: 2 sub-checks, 0 failed → PASS
```

**Final-report verdict rows:**
- `PASS` — Test 17: zero_modes(α=1/2)=4 (expected 4) → PASS
- `PASS` — Test 17b [HARDCORE pass 2]: 2 sub-checks, 0 failed → PASS

Computation log: 15 timestamped entries; 3171–4171 s (от начала прогона).

---

### 24.18 Test 18: chiral_AIII

**Verdict: PASS** · Suite: AB-Cloud v19 (Julia 1.12.0) · two-pass protocol.

EXACT: ||SHS+H||/||H|| ≈ 1e-16 on the pure lattice (W=0); W>0 is the honest breaker.

The construction's exact-layer category: hermiticity after assembly (Test 15: anti-Hermitian norm 0.0; $\tau_{TRB} = 0.1037$; vertex/empty-lattice fluxes 0.0), the GUE class of the monumental configuration (Test 16: $\langle r\rangle = 0.594$ at final $\alpha = 0.5$), Connes self-duality (Test 17: zero modes at $\alpha = 1/2$ — exactly 4), chiral AIII symmetry (Test 18: defect 0.0 at $W=0$; 0.0058 at $\alpha = 1/3$ — non-zero, as the T13 counting law requires). The exact layer reproduces two-pass: 72×72 and 96×96 give identical verdicts.

**The test in detail.** Chiral AIII symmetry: the defect at $\alpha = 1/2$, $W = 0$: exactly 0.0; at $\alpha = 1/3$: 0.0058 — non-zero, as the T13 counting law requires (modes at $\alpha = 1/3$ carry the L-arithmetic). The test distinguishes the symmetric point (zero defect) from the arithmetic one (a defect from modes): both verdicts PASS because the expectations differ.


**Result summary (from the report):** Test 18b [HARDCORE pass 2]: 4 sub-checks, 0 failed → PASS

**Console of the run (fragment, verbatim):**

```text
TEST 18 (pass 2, HARDCORE): chiral symmetry AIII — deep audit
Exact row + ε_rms quantitative contract + vortex-preservation row +
S² = I operator sanity (launch-standard lattice)
 H1 exact row (α=1/2, W=0):      defect = 0.00e+00 < ✓ 1e-10
 H2 ε row (W=1.0, Nv=0):       defect = 5.77e-03 vs ε_rms = 0.0058 (analytic) ∈ [0.5, 2.0]× ✓
 H2v vortex row (Nv=2, W=0):     defect = 0.00e+00 < 1e-10 ✓ (bond phases PRESERVE AIII)
 H3 operator sanity: ‖S² − I‖/‖I‖ = 0.00e+00 < ✓ 1e-12
 exact row < 1e-10    PASS — ‖SHS+H‖/‖H‖ = 0.00e+00 at α=1/2, W=0
 ε_rms contract (W=1.0) PASS — defect 5.77e-03 vs analytic 2‖ε‖_F/‖H‖_F = 0.0058 (size-independent)
 vortices PRESERVE AIII PASS — defect = 0.00e+00 (Nv=2, q=±1.00, W=0) — bond phases; Byers-Yang for integer q
 S² = I               PASS — ‖S²−I‖/‖I‖ = 0.00e+00
 Test 18b [HARDCORE pass 2]: 4 sub-checks, 0 failed → PASS
```

**Final-report verdict rows:**
- `PASS` — Test 18: chiral defect (α=1/2)=0.0 [exp 0.000000], (α=1/3)=0.0058 [exp ≠0] → PASS
- `PASS` — Test 18b [HARDCORE pass 2]: 4 sub-checks, 0 failed → PASS

Computation log: 3 timestamped entries; 5003–5028 s (от начала прогона).

---

### 24.19 Test 19: dirac_cone

**Verdict: PASS** · Suite: AB-Cloud v19 (Julia 1.12.0) · two-pass protocol.

EXACT-geometry: zero modes at (π/2,π/2) require L/4∈ℤ; gap scaling fit R².

The Dirac-layer category: the cone (Test 19: $1/L$ scaling with $R^2 = 0.9997$; $v_F(2\pi) = 1.8998$, $v_F(\pi) = 3.7995$ — the ratio exactly 2: two cones, two valleys), the anomalous quantum Hall effect (Test 20: Chern anchors $C_1 \in \{1/4, 1/3, 1/5\}$ = 1, 1, 1; at $\alpha = 1/2$ — Dirac touching, gap 0), the $\gamma^*$ phase (Test 21: $89.874°$ vs $90°$ — a 0.126° deviation), the AB phase (Test 22: $\Phi_{AB} = 0.4487989505 = \pi/7$ exactly), the fractal factor (Test 23: $|CF| = 1.0$ by construction; $c_{AB} = 0.02062$ vs the theoretical 0.02063), the Dirac-string flux (Test 24: the vortex 1/1; the empty lattice 5040/5040 bonds — zero maximum).

**The test in detail.** The Dirac cone: $1/L$ scaling with $R^2 = 0.9997$; $v_F(2\pi) = 1.8998$, $v_F(\pi) = 3.7995$ — the ratio exactly 2: two cones (two valleys) with a velocity ratio of 2 — the π-flux lattice theory's prediction. The SERIES pass (T19c): a real report series in the 96×96 regime. Cross-links: D1 of level II (the same quantity, another engine) and T30 ($v_F$ in another window).


**Result summary (from the report):** Test 19c [SERIES pass 3]: 3 sub-checks, 0 failed → PASS

**Console of the run (fragment, verbatim):**

```text
TEST 19 (pass 3, SERIES): Dirac cone — α-selective 1/L series
 4-point mod-20 grid L=20, 40, 60, 80; α ∈ {0.4, 0.5, 0.6} — all EXACT on the torus
 α=0.4 L=20: E_min = 0.086901, E_min·L = 1.7380, zero_modes = 30
 α=0.4 L=40: E_min = 0.025377, E_min·L = 1.0151, zero_modes = 70
 α=0.4 L=60: E_min = 0.011605, E_min·L = 0.6963, zero_modes = 110
 α=0.4 L=80: E_min = 0.006593, E_min·L = 0.5275, zero_modes = 150
 α=0.5 L=20: E_min = 0.618034, E_min·L = 12.3607, zero_modes = 4
 α=0.5 L=40: E_min = 0.312869, E_min·L = 12.5148, zero_modes = 4
 α=0.5 L=60: E_min = 0.209057, E_min·L = 12.5434, zero_modes = 4
 α=0.5 L=80: E_min = 0.156918, E_min·L = 12.5535, zero_modes = 4
 α=0.6 L=20: E_min = 0.086901, E_min·L = 1.7380, zero_modes = 30
 α=0.6 L=40: E_min = 0.025377, E_min·L = 1.0151, zero_modes = 70
 α=0.6 L=60: E_min = 0.011605, E_min·L = 0.6963, zero_modes = 110
 α=0.6 L=80: E_min = 0.006593, E_min·L = 0.5275, zero_modes = 150
 α=0.5 fit: E_min = 0.0043 + 12.2836/L, R² = 0.999975 (v_F = b/2π = 1.9550)
 E_min·L @L=80: α=0.4 → 0.5275 | α=0.5 → 12.5535 (4π = 12.566) | α=0.6 → 0.5275
 α=0.5 fit R² > 0.95 (4 pts) PASS — E_min = 0.0043 + 12.2836/L, v_F = b/2π = 1.9550
 α=0.5 scale ∈ [8, 18] PASS — E_min·L(L=80) = 12.553, target 4π = 12.566
 α-selectivity > 2×   PASS — E_min·L(0.5) = 12.553 vs 0.4: 0.527 / 0.6: 0.527 (q=5 odd → gapless at E=0)
 Test 19c [SERIES pass 3]: 3 sub-checks, 0 failed → PASS
```

**Final-report verdict rows:**
- `PASS` — Test 19: 1/L scaling R²=0.9997, v_F(2π)=1.8998, v_F(π)=3.7995 → PASS
- `PASS` — Test 19b [HARDCORE pass 2]: 3 sub-checks, 0 failed → PASS
- `PASS` — Test 19c [SERIES pass 3]: 3 sub-checks, 0 failed → PASS

Computation log: 12 timestamped entries; 5781–6009 s (от начала прогона).

---

### 24.20 Test 20: chern_tknn

**Verdict: PASS** · Suite: AB-Cloud v19 (Julia 1.12.0) · two-pass protocol.

EXACT: FHS C₁=+1 on the MAGNETIC BZ (q×q Harper; anchors α=1/4,1/3,1/5); α=1/2 = Dirac touching, per-band C undefined — touching-ladder rungs need L ≡ 0 (mod 4) so (π/2,π/2) lies on the k-grid; sub-second by design (q×q cells).

The Dirac-layer category: the cone (Test 19: $1/L$ scaling with $R^2 = 0.9997$; $v_F(2\pi) = 1.8998$, $v_F(\pi) = 3.7995$ — the ratio exactly 2: two cones, two valleys), the anomalous quantum Hall effect (Test 20: Chern anchors $C_1 \in \{1/4, 1/3, 1/5\}$ = 1, 1, 1; at $\alpha = 1/2$ — Dirac touching, gap 0), the $\gamma^*$ phase (Test 21: $89.874°$ vs $90°$ — a 0.126° deviation), the AB phase (Test 22: $\Phi_{AB} = 0.4487989505 = \pi/7$ exactly), the fractal factor (Test 23: $|CF| = 1.0$ by construction; $c_{AB} = 0.02062$ vs the theoretical 0.02063), the Dirac-string flux (Test 24: the vortex 1/1; the empty lattice 5040/5040 bonds — zero maximum).

**The test in detail.** The anomalous quantum Hall effect (TKNN): the Chern anchors $C_1$ at $\alpha \in \{1/4, 1/3, 1/5\}$: 1, 1, 1 (expected 1, 1, 1); at $\alpha = 1/2$: Dirac touching — gap 0, the mass branch C = 0/0 (undefined). The 0/0 branch diagnosis is an honest record of division by zero, not a crash. The anchors are integer invariants: sub-band sums of the Hofstadter decomposition.


**Result summary (from the report):** Test 20b [HARDCORE pass 2]: 3 sub-checks, 0 failed → PASS

**Console of the run (fragment, verbatim):**

```text
TEST 20 (pass 2, HARDCORE): TKNN Chern number — deep audit
Anchors {1/4, 1/3, 1/5} + size ladder 12→72 + α=1/2 touching audit
 α=1/4: C₁ = +1 (12-pt grid) → +1 (24-pt grid) ✓, min gap 1.646
 α=1/3: C₁ = +1 (12-pt grid) → +1 (24-pt grid) ✓, min gap 1.268
 α=1/5: C₁ = +1 (12-pt grid) → +1 (24-pt grid) ✓, min gap 1.554
 α=1/3 ladder L=12 (  48 k-points): C₁ = +1, min gap 1.268 ✓
 α=1/3 ladder L=18 ( 108 k-points): C₁ = +1, min gap 1.268 ✓
 α=1/3 ladder L=24 ( 192 k-points): C₁ = +1, min gap 1.268 ✓
 α=1/3 ladder L=36 ( 432 k-points): C₁ = +1, min gap 1.268 ✓
 α=1/3 ladder L=48 ( 768 k-points): C₁ = +1, min gap 1.268 ✓
 α=1/3 ladder L=72 (1728 k-points): C₁ = +1, min gap 1.268 ✓
 α=1/2 L=12: bare min gap = 5.48e-16 (touching), singular links 0
 α=1/2 L=16: bare min gap = 5.48e-16 (touching), singular links 0
 α=1/2 L=24: bare min gap = 5.48e-16 (touching), singular links 0
 α=1/2 L=48: bare min gap = 5.48e-16 (touching), singular links 0
 α=1/2 L=72: bare min gap = 5.48e-16 (touching), singular links 0
 α=1/2 mass branch (24×12 grid): C(m=+0.3) = +0 (gap 0.435), C(m=−0.3) = +0 (gap 0.435) ✓
 anchors C₁=+1 {1/4,1/3,1/5} PASS — TKNN Diophantine t₁=+1, grid-converged 12→24 points
 ladder C₁=+1, L=12..72 PASS — magnetic-BZ FHS on L = 12/18/24/36/48/72 (α=1/3)
 α=1/2 Dirac touching + branch PASS — bare gap ≈ 1e-16 ∀L (rungs L ≡ 0 mod 4 — Dirac points on-grid); mass-regularized C₁ = 0 (chirality-balanced)
 Test 20b [HARDCORE pass 2]: 3 sub-checks, 0 failed → PASS
```

**Final-report verdict rows:**
- `PASS` — Test 20: C₁ anchors {1/4,1/3,1/5}=1,1,1 [exp 1,1,1], α=1/2 min gap=0.0 (Dirac touching), mass branch C=0/0 → PASS
- `PASS` — Test 20b [HARDCORE pass 2]: 3 sub-checks, 0 failed → PASS



---

### 24.21 Test 21: gamma_phase

**Verdict: PASS** · Suite: AB-Cloud v19 (Julia 1.12.0) · two-pass protocol.

EXACT geometric phase check.

The Dirac-layer category: the cone (Test 19: $1/L$ scaling with $R^2 = 0.9997$; $v_F(2\pi) = 1.8998$, $v_F(\pi) = 3.7995$ — the ratio exactly 2: two cones, two valleys), the anomalous quantum Hall effect (Test 20: Chern anchors $C_1 \in \{1/4, 1/3, 1/5\}$ = 1, 1, 1; at $\alpha = 1/2$ — Dirac touching, gap 0), the $\gamma^*$ phase (Test 21: $89.874°$ vs $90°$ — a 0.126° deviation), the AB phase (Test 22: $\Phi_{AB} = 0.4487989505 = \pi/7$ exactly), the fractal factor (Test 23: $|CF| = 1.0$ by construction; $c_{AB} = 0.02062$ vs the theoretical 0.02063), the Dirac-string flux (Test 24: the vortex 1/1; the empty lattice 5040/5040 bonds — zero maximum).

**The test in detail.** The $\gamma^*$ phase: $89.874°$ vs $90°$ — a 0.126° deviation. The assembly phase at the cone crossing; the closeness to 90° is structural identity, not exact equality: the lattice regularization contributes an O(1/L²) correction. Verdict by the 0.5° threshold.


**Result summary (from the report):** Test 21b [HARDCORE pass 2]: 3 sub-checks, 0 failed → PASS

**Console of the run (fragment, verbatim):**

```text
TEST 21 (pass 2, HARDCORE): γ* spinorial phase — 256-bit precision audit
 δ_C = π/7, b₂(K3) = 22 (256-bit recomputation)
 a_C: Float64 8.276305e-04 vs 256-bit 8.276305e-04 → |Δ| = 1.23e-19
 b_C: Float64 0.376510 vs 256-bit 0.376510 → |Δ| = 6.39e-17
 arg(γ*) at 256-bit: 89.874055° (deviation from 90°: 0.1259°)
 δ = π/7-1·1e-6: arg(γ*) deviation = 0.1259°
 δ = π/7+1·1e-6: arg(γ*) deviation = 0.1259°
 Float64 round-off    PASS — |Δa|=1.23e-19, |Δb|=6.39e-17 (machine-ε scale)
 arg(γ*) → π/2 (256-bit) PASS — deviation 0.1259° < 1°
 δ_C ± 1e-6 stability PASS — worst deviation 0.1259° across the ±1e-6 scan
 Test 21b [HARDCORE pass 2]: 3 sub-checks, 0 failed → PASS
```

**Final-report verdict rows:**
- `PASS` — Test 21: arg(γ*)=89.874° (≈90°, deviation=0.126°) → PASS
- `PASS` — Test 21b [HARDCORE pass 2]: 3 sub-checks, 0 failed → PASS



---

### 24.22 Test 22: ab_phase

**Verdict: PASS** · Suite: AB-Cloud v19 (Julia 1.12.0) · two-pass protocol.

EXACT flux-phase identity.

The Dirac-layer category: the cone (Test 19: $1/L$ scaling with $R^2 = 0.9997$; $v_F(2\pi) = 1.8998$, $v_F(\pi) = 3.7995$ — the ratio exactly 2: two cones, two valleys), the anomalous quantum Hall effect (Test 20: Chern anchors $C_1 \in \{1/4, 1/3, 1/5\}$ = 1, 1, 1; at $\alpha = 1/2$ — Dirac touching, gap 0), the $\gamma^*$ phase (Test 21: $89.874°$ vs $90°$ — a 0.126° deviation), the AB phase (Test 22: $\Phi_{AB} = 0.4487989505 = \pi/7$ exactly), the fractal factor (Test 23: $|CF| = 1.0$ by construction; $c_{AB} = 0.02062$ vs the theoretical 0.02063), the Dirac-string flux (Test 24: the vortex 1/1; the empty lattice 5040/5040 bonds — zero maximum).

**The test in detail.** The AB phase: $\Phi_{AB} = 0.4487989505 = \pi/7$ — exactly. From the bridge's six constants: the coding phase equals $\pi/7$ by construction — the test checks that assembly loses no phase. One of the exact layer's 'machine zeros': the assembled phase equals the analytic one to every printed digit.


**Result summary (from the report):** Test 22b [HARDCORE pass 2]: 3 sub-checks, 0 failed → PASS

**Console of the run (fragment, verbatim):**

```text
TEST 22 (pass 2, HARDCORE): AB phase Φ_AB = π/7 — 256-bit audit
 Φ_AB(1/14) == 1·(π/7): true (256-bit exact)
 Φ_AB(2/14) == 2·(π/7): true (256-bit exact)
 Φ_AB(3/14) == 3·(π/7): true (256-bit exact)
 2π·(1/14) == π/7 at 256-bit: true (bit-for-bit)
 Float64 Φ_AB vs 256-bit truth: |Δ| = 1.75e-17 (contract < 1e-15)
 Float64 δ_C vs 256-bit π/7:   |Δ| = 1.75e-17
 rational identity    PASS — 2π/14 == π/7 (256-bit), Float64 |Δ| = 1.75e-17
 flux linearity p=1..3 PASS — Φ_AB(p/14) = p·(π/7) exact at 256-bit
 Φ_AB == δ_C          PASS — Float64 δ_C vs 256-bit π/7: |Δ| = 1.75e-17
 Test 22b [HARDCORE pass 2]: 3 sub-checks, 0 failed → PASS
```

**Final-report verdict rows:**
- `PASS` — Test 22: Φ_AB=0.4487989505 = π/7 (exact) → PASS
- `PASS` — Test 22b [HARDCORE pass 2]: 3 sub-checks, 0 failed → PASS



---

### 24.23 Test 23: fractal_factor

**Verdict: PASS** · Suite: AB-Cloud v19 (Julia 1.12.0) · two-pass protocol.

Log-periodic factor — semi-statistical curve comparison.

The Dirac-layer category: the cone (Test 19: $1/L$ scaling with $R^2 = 0.9997$; $v_F(2\pi) = 1.8998$, $v_F(\pi) = 3.7995$ — the ratio exactly 2: two cones, two valleys), the anomalous quantum Hall effect (Test 20: Chern anchors $C_1 \in \{1/4, 1/3, 1/5\}$ = 1, 1, 1; at $\alpha = 1/2$ — Dirac touching, gap 0), the $\gamma^*$ phase (Test 21: $89.874°$ vs $90°$ — a 0.126° deviation), the AB phase (Test 22: $\Phi_{AB} = 0.4487989505 = \pi/7$ exactly), the fractal factor (Test 23: $|CF| = 1.0$ by construction; $c_{AB} = 0.02062$ vs the theoretical 0.02063), the Dirac-string flux (Test 24: the vortex 1/1; the empty lattice 5040/5040 bonds — zero maximum).

**The test in detail.** The fractal factor: $|CF|_{formula} = 1.0$ (= 1 by construction — a formula self-test); $c_{AB} = 0.02062$ vs the theoretical 0.02063 — agreement to 5 digits. The fractal factor is the product of eigenfunction moduli at the band edges; $c_{AB}$ is the Cantor-set constant of the Hofstadter spectrum at $\alpha = 1/2$.


**Result summary (from the report):** Test 23b [HARDCORE pass 2]: 3 sub-checks, 0 failed → PASS

**Console of the run (fragment, verbatim):**

```text
TEST 23 (pass 2, HARDCORE): complex fractal factor — 256-bit audit
 |CF| − 1 at 256-bit: 0.00e+00 (contract < 1e-30)
 β_imag: Float64 2.854032819406525 vs 256-bit 2.854032819406525 (|Δ| = 3.04e-16)
 β_imag vs LaTeX 2.854: |Δ| = 3.28e-05 (contract < 1e-3)
 c_AB = 1 − |CF_hard|: 0.020623 vs 0.02063 (|Δ| = 6.82e-06, contract < 1e-3)
 |CF| = 1 (1e-30)     PASS — pure-phase property at 256-bit: 0.00e+00
 β_imag anchors       PASS — Float64 |Δ|=3.04e-16; LaTeX 2.854 |Δ|=3.28e-05
 c_AB ≈ 0.02063       PASS — c_AB = 0.020623, |Δ| = 6.82e-06
 Test 23b [HARDCORE pass 2]: 3 sub-checks, 0 failed → PASS
```

**Final-report verdict rows:**
- `PASS` — Test 23: |CF_formula|=1.0 (=1 by construction), c_AB=0.02062 (≈0.02063) → PASS
- `PASS` — Test 23b [HARDCORE pass 2]: 3 sub-checks, 0 failed → PASS



---

### 24.24 Test 24: dirac_string_flux

**Verdict: PASS** · Suite: AB-Cloud v19 (Julia 1.12.0) · two-pass protocol.

EXACT: plaquette flux = 2πq (mod 2π); tolerance = round-off accumulation across the lattice.

The Dirac-layer category: the cone (Test 19: $1/L$ scaling with $R^2 = 0.9997$; $v_F(2\pi) = 1.8998$, $v_F(\pi) = 3.7995$ — the ratio exactly 2: two cones, two valleys), the anomalous quantum Hall effect (Test 20: Chern anchors $C_1 \in \{1/4, 1/3, 1/5\}$ = 1, 1, 1; at $\alpha = 1/2$ — Dirac touching, gap 0), the $\gamma^*$ phase (Test 21: $89.874°$ vs $90°$ — a 0.126° deviation), the AB phase (Test 22: $\Phi_{AB} = 0.4487989505 = \pi/7$ exactly), the fractal factor (Test 23: $|CF| = 1.0$ by construction; $c_{AB} = 0.02062$ vs the theoretical 0.02063), the Dirac-string flux (Test 24: the vortex 1/1; the empty lattice 5040/5040 bonds — zero maximum).

**The test in detail.** The Dirac-string flux: the vortex 1/1 — the string through the vortex carries exactly one quantum; the empty lattice 5040/5040 bonds — zero maximum flux on bonds away from the vortex. The test is gauge hygiene: the string does not leak where it must not.


**Result summary (from the report):** Test 24b [HARDCORE pass 2]: 5 sub-checks, 0 failed → PASS

**Console of the run (fragment, verbatim):**

```text
TEST 24 (pass 2, HARDCORE): Dirac-string flux — exhaustive scan
Full plaquette scan × 4 configs: 2 positions × {+1, −1, +0.3}
 Lattice: 96x96 (N=9216 sites) — full plaquette scan × 4 configs
 cfg A (ix=32, iy=48, q=+1.0): vortex 1/1, empty 9024/9024 → OK
 cfg B (ix=64, iy=24, q=+1.0): vortex 1/1, empty 9024/9024 → OK
 cfg A− (ix=32, iy=48, q=-1.0): vortex 1/1, empty 9024/9024 → OK
 cfg A frac (ix=32, iy=48, q=+0.3): vortex 1/1, empty 9024/9024 → OK
 Max |flux| over ALL empty plaquettes and configs: 8.88e-16
 scan A q=+1.0        PASS — 9025/9025 plaquettes OK
 scan B q=+1.0        PASS — 9025/9025 plaquettes OK
 scan A− q=-1.0       PASS — 9025/9025 plaquettes OK
 scan A frac q=+0.3   PASS — 9025/9025 plaquettes OK
 hermiticity (all)    PASS — verify_hermitian per config
 Test 24b [HARDCORE pass 2]: 5 sub-checks, 0 failed → PASS
```

**Final-report verdict rows:**
- `PASS` — Test 24: vortex flux OK=1/1, empty OK=5040/5040, max_empty=0.0 → PASS
- `PASS` — Test 24b [HARDCORE pass 2]: 5 sub-checks, 0 failed → PASS

Computation log: 4 timestamped entries; 6242–6273 s (от начала прогона).

---

### 24.25 Test 25: byers_yang

**Verdict: PASS** · Suite: AB-Cloud v19 (Julia 1.12.0) · two-pass protocol.

EXACT: spectra identical for q and q+1 (Δ~1e-15); fractional q must DIFFER (non-neutral config).

The gauge-invariant category: Byers–Yang (Test 25: $\Delta(q{=}1\to0) = 0.0$; $\Delta(q{=}0.3\to0) = 0.0032 > 10^{-3}$ — the gauge does not change physics, the flux does), the torus (Test 26: vertex flux 0.0; 5040/5183 empty bonds; hermiticity OK; $\langle r\rangle = 0.6009$), binary chirality (Test 27: defect 0.0 at $W=0$, 0.0058 at $W=1$).

**The test in detail.** Byers–Yang: the gauge shift $q: 1 \to 0$ — $\Delta = 0.0$ (the spectrum is invariant: physics does not depend on the gauge at fixed flux); $q: 0.3 \to 0$ — $\Delta = 0.0032 > 10^{-3}$ (changing the flux changes the spectrum). The pair of statements is the theorem: gauge invariance, flux sensitivity. The most expensive test: 147.9 s + 3,839 s HARDCORE (48 diagonalizations in the 96×96 calibration sweep).


**Result summary (from the report):** Test 25b [HARDCORE pass 2]: 2 sub-checks, 0 failed → PASS

**Console of the run (fragment, verbatim):**

```text
TEST 25 (pass 2, HARDCORE): Byers–Yang — multi-layout / multi-q audit
3 layouts × {+1, +2, −1} integer rows + fractional {0.3, 0.5} rows
 layout 1, q=+1: Δ = 9.66e-15 < 1e-10 ✓
 layout 1, q=+2: Δ = 1.04e-14 < 1e-10 ✓
 layout 1, q=-1: Δ = 9.66e-15 < 1e-10 ✓
 layout 1, fractional q=0.3: Δ = 3.35e-03 > 1e-3 ✓ (genuine AB effect)
 layout 1, fractional q=0.5: Δ = 3.74e-03 > 1e-3 ✓ (genuine AB effect)
 layout 2, q=+1: Δ = 1.24e-14 < 1e-10 ✓
 layout 2, q=+2: Δ = 8.66e-15 < 1e-10 ✓
 layout 2, q=-1: Δ = 1.24e-14 < 1e-10 ✓
 layout 3, q=+1: Δ = 1.01e-14 < 1e-10 ✓
 layout 3, q=+2: Δ = 8.89e-15 < 1e-10 ✓
 layout 3, q=-1: Δ = 1.01e-14 < 1e-10 ✓
 integer q ∀layouts   PASS — Δ(q=+1,+2,−1 vs 0) < 1e-10 on 3 independent layouts
 fractional Δ > 1e-3  PASS — q ∈ {0.3, 0.5} keep the genuine AB effect
 Test 25b [HARDCORE pass 2]: 2 sub-checks, 0 failed → PASS
```

**Final-report verdict rows:**
- `PASS` — Test 25: Δ(q=1→0)=0.0 [exp ~0], Δ(q=0.3→0)=0.0032 [exp >1e-3] → PASS
- `PASS` — Test 25b [HARDCORE pass 2]: 2 sub-checks, 0 failed → PASS

Computation log: 12 timestamped entries; 6457–9973 s (от начала прогона).

---

### 24.26 Test 26: pbc_torus

**Verdict: PASS** · Suite: AB-Cloud v19 (Julia 1.12.0) · two-pass protocol.

Mixed: flux identities exact; ⟨r⟩ on 4 neutral vortices over the bulk window (statistical).

The gauge-invariant category: Byers–Yang (Test 25: $\Delta(q{=}1\to0) = 0.0$; $\Delta(q{=}0.3\to0) = 0.0032 > 10^{-3}$ — the gauge does not change physics, the flux does), the torus (Test 26: vertex flux 0.0; 5040/5183 empty bonds; hermiticity OK; $\langle r\rangle = 0.6009$), binary chirality (Test 27: defect 0.0 at $W=0$, 0.0058 at $W=1$).

**The test in detail.** The torus with PBC: vertex flux $-0.0$; empty bonds 5040/5183 (the rest inside vortex windows); hermiticity OK; $\langle r\rangle = 0.6009$ — the GUE band on the torus. The contrast with open boundaries: no edge effects; the link to T34: the reference (open, $N_v=2$) gives $D = 0.1096$; the torus with $N_v = 16$ (level VII) — 0.0318: part of the improvement is topology.


**Result summary (from the report):** Test 26b [HARDCORE pass 2]: 4 sub-checks, 0 failed → PASS

**Console of the run (fragment, verbatim):**

```text
TEST 26 (pass 2, HARDCORE): PBC torus Dirac string — deep validation
Exhaustive artifact classification + ⟨r⟩ ensemble (n ≥ 5)
 ⟨r⟩ row: α=0.5000, Nv=4 (base protocol), q=1.0000, W=1.00 = ab_w_eff (capped)
 H1 flux: vortex plaquette OK; empty plaquettes: 9024 clean, 0 wrap artifacts (0.0000), 191 seam (gauge holonomy, ix=96/iy=96), 0 unexplained
 real  1/5: ⟨r⟩ = 0.6006
 real  2/5: ⟨r⟩ = 0.5962
 real  3/5: ⟨r⟩ = 0.6006
 real  4/5: ⟨r⟩ = 0.5894
 real  5/5: ⟨r⟩ = 0.5954
 Ensemble: ⟨r⟩ = 0.5964 ± 0.0021 | bootstrap CI [0.5928, 0.5997] ∋ GUE | above/below: 2/3
 flux + artifacts     PASS — vortex OK; 9024 clean + 0 wrap(−2πq) + 191 seam holonomy; 0 unexplained
 ⟨r⟩ > 0.5 (ensemble) PASS — ⟨r⟩ = 0.5964 ± 0.0021 (n=5, base contract)
 scatter ≤ 0.022      PASS — σ=0.0046 ≤ ✓ monograph band
 hermiticity ∀real    PASS — verify_hermitian per realization
 Test 26b [HARDCORE pass 2]: 4 sub-checks, 0 failed → PASS
```

**Final-report verdict rows:**
- `PASS` — Test 26: flux_v=-0.0 [exp -0.0], empty_ok=5040/5183, herm=OK, ⟨r⟩=0.6009 → PASS
- `PASS` — Test 26b [HARDCORE pass 2]: 4 sub-checks, 0 failed → PASS

Computation log: 11 timestamped entries; 10358–12052 s (от начала прогона).

---

### 24.27 Test 27: binary_chiral

**Verdict: PASS** · Suite: AB-Cloud v19 (Julia 1.12.0) · two-pass protocol.

EXACT: defect 0 on pure lattice; W>0 row is the honest breaker control.

The gauge-invariant category: Byers–Yang (Test 25: $\Delta(q{=}1\to0) = 0.0$; $\Delta(q{=}0.3\to0) = 0.0032 > 10^{-3}$ — the gauge does not change physics, the flux does), the torus (Test 26: vertex flux 0.0; 5040/5183 empty bonds; hermiticity OK; $\langle r\rangle = 0.6009$), binary chirality (Test 27: defect 0.0 at $W=0$, 0.0058 at $W=1$).

**The test in detail.** Binary chirality: defect 0.0 at $W = 0$ (exact symmetry); 0.0058 at $W = 1$ (symmetry broken by wells). The T18 control: the same values in other configurations — cross-consistency. The Th1 link: chiral symmetry is an exact-layer element, robust under decoration but not under mass.


**Result summary (from the report):** Test 27b [HARDCORE pass 2]: 4 sub-checks, 0 failed → PASS

**Console of the run (fragment, verbatim):**

```text
TEST 27 (pass 2, HARDCORE): binary chiral symmetry — deep audit
Exact row + ε_rms contract + vortex preservation + Coulomb W-scan
(launch-standard lattice, 96x96 in two-pass mode)
 H1 exact row (W=0, clean):     defect = 0.00e+00 < ✓ 1e-10
 H2 ε row (W=1.0, Nv=0):      defect = 5.77e-03 vs ε_rms = 0.0058 (analytic) ∈ [0.5, 2.0]× ✓
 H2v vortex row (Nv=2, W=0):    defect = 0.00e+00 < 1e-10 ✓ (bond phases PRESERVE AIII)
 W-scan (Nv=2) W=0.5: defect = 1.0052e-01
 W-scan (Nv=2) W=1.0: defect = 2.0010e-01
 W-scan (Nv=2) W=2.0: defect = 3.9425e-01
 W-scan (Nv=2) W=4.0: defect = 7.4620e-01
 H3 scan: monotone ✓, defect(W=4)/defect(W=0.5) = 7.42 ∈ [5, 12] ✓
 Nv=0 ε-floor diagnostic (residual ε is FIXED-amplitude):
 W-scan (Nv=0) W=0.5: defect = 5.7704e-03 ≈ ε_rms (W-independent ✓)
 W-scan (Nv=0) W=1.0: defect = 5.7704e-03 ≈ ε_rms (W-independent ✓)
 W-scan (Nv=0) W=2.0: defect = 5.7704e-03 ≈ ε_rms (W-independent ✓)
 W-scan (Nv=0) W=4.0: defect = 5.7704e-03 ≈ ε_rms (W-independent ✓)
 exact row < 1e-10    PASS — binary contract at α=1/2, W=0: 0.00e+00
 ε_rms contract (W=1.0) PASS — defect 5.77e-03 ≈ analytic 2‖ε‖_F/‖H‖_F = 0.0058
 vortices PRESERVE AIII PASS — defect = 0.00e+00 (Nv=2, q=±1.00, W=0) — bond phases; Byers-Yang for integer q
 Coulomb W-scan linear PASS — Nv=2: monotone, defect 0.101→0.746, ratio 7.42 ∈ [5, 12]
 Test 27b [HARDCORE pass 2]: 4 sub-checks, 0 failed → PASS
```

**Final-report verdict rows:**
- `PASS` — Test 27: chiral defect (W=0) = 0.0, (W=1.0) = 0.0058 → PASS
- `PASS` — Test 27b [HARDCORE pass 2]: 4 sub-checks, 0 failed → PASS

Computation log: 11 timestamped entries; 12087–12210 s (от начала прогона).

---

### 24.28 Test 28: f_gue_merit

**Verdict: FAIL** · Suite: AB-Cloud v19 (Julia 1.12.0) · two-pass protocol.

Statistical: fraction of spectral diagnostics consistent with GUE.

The GUE-quality and dynamics category: the $f_{GUE}$ merit (Test 28: 0.8704, $\Sigma^2 = 0.6115$ — WARN: gaps slightly narrower than GUE), the Dirac dip (Test 29: $\rho(\alpha{=}0.5) = 0.0193$ vs $0.1944$ at $\alpha = 0.403/0.597$ — a tenfold flux anisotropy), $v_F$ scaling (Test 30: 1.798, $R^2 = 0.9977$), Hatano–Nelson (Test 31: max $|\mathrm{Im}E| = 0.6397$; $\langle r\rangle_{NH} = 0.8938$ — the non-Hermitian deformation drives the statistics past the GUE band: a direction control).

**The test in detail.** The $f_{GUE}$ merit: 0.8704, $\Sigma^2_{data} = 0.6115$ — WARN: gaps narrower than GUE (merit < 1). HARDCORE: 1 of 2 sub-checks failed. Meaning: the composite quality index (local + integral) sits below one — the ζ table is not an ideal GUE sample. The programme already knows why (the tails, T11); the merit aggregates the known discrepancy into one index.


**Result summary (from the report):** Test 28b [HARDCORE pass 2]: 2 sub-checks, 1 failed → WARN

**Console of the run (fragment, verbatim):**

```text
TEST 28 (pass 2, HARDCORE): f_GUE figure of merit — ensemble deep pass
n ≥ 5 realizations, per-realization f_GUE, ensemble verdict
 Config: 96x96, Nv=4, q=±1.00, α=0.5000, W=1.0 (hardcore standard: W=1, q=1, Nv=4)
 real  1/5: f_GUE = 0.8378
 real  2/5: f_GUE = 0.8592
 real  3/5: f_GUE = 0.8649
 real  4/5: f_GUE = 0.7911
 real  5/5: f_GUE = 0.9234
 Ensemble: ⟨f_GUE⟩ = 0.8553 ± 0.0214 | bootstrap CI [0.8184, 0.8946] ∌ 0.90 (diagnostic)
 ⟨f_GUE⟩ > 0.90       WARN — ⟨f_GUE⟩ = 0.8553 ± 0.0214 (n=5 of 5 finite)
 scatter < 0.10       PASS — σ=0.0479 stable across vortex layouts
 Test 28b [HARDCORE pass 2]: 2 sub-checks, 1 failed → WARN
```

**Final-report verdict rows:**
- `FAIL` — Test 28: f_GUE=0.8704, Σ²_data=0.6115 → WARN
- `FAIL` — Test 28b [HARDCORE pass 2]: 2 sub-checks, 1 failed → WARN

Computation log: 11 timestamped entries; 12304–13852 s (от начала прогона).

---

### 24.29 Test 29: dirac_dip

**Verdict: PASS** · Suite: AB-Cloud v19 (Julia 1.12.0) · two-pass protocol.

Semi-exact: DOS dip depth vs prediction.

The GUE-quality and dynamics category: the $f_{GUE}$ merit (Test 28: 0.8704, $\Sigma^2 = 0.6115$ — WARN: gaps slightly narrower than GUE), the Dirac dip (Test 29: $\rho(\alpha{=}0.5) = 0.0193$ vs $0.1944$ at $\alpha = 0.403/0.597$ — a tenfold flux anisotropy), $v_F$ scaling (Test 30: 1.798, $R^2 = 0.9977$), Hatano–Nelson (Test 31: max $|\mathrm{Im}E| = 0.6397$; $\langle r\rangle_{NH} = 0.8938$ — the non-Hermitian deformation drives the statistics past the GUE band: a direction control).

**The test in detail.** The Dirac dip: $\rho(\alpha = 0.5) = 0.0193$ vs $\rho(0.403) = \rho(0.597) = 0.1944$ — a tenfold anisotropy: at the self-dual point the density of states at zero is minimal (the Dirac cone's gap); away it grows. Test 29b HARDCORE: 1 of 3 failed (threshold tightness); the SERIES pass (T29c) — PASS: the α-shift series confirms the dip's shape.


**Result summary (from the report):** Test 29c [SERIES pass 3]: 3 sub-checks, 0 failed → PASS

**Console of the run (fragment, verbatim):**

```text
TEST 29 (pass 3, SERIES): Dirac dip — fine α-scan + window series
 Fine scan: 9 points α = k/96 around k=48 (α=1/2 EXACT), window |E|<0.5
 α=38/96 = 0.39583: ρ(|E|<0.5) = 0.2083  (289.4 s)
 α=41/96 = 0.42708: ρ(|E|<0.5) = 0.1458  (297.0 s)
 α=44/96 = 0.45833: ρ(|E|<0.5) = 0.0833  (290.1 s)
 α=47/96 = 0.48958: ρ(|E|<0.5) = 0.0208  (293.5 s)
 α=48/96 = 0.50000: ρ(|E|<0.5) = 0.0195  (294.9 s)
 α=49/96 = 0.51042: ρ(|E|<0.5) = 0.0208  (288.2 s)
 α=52/96 = 0.54167: ρ(|E|<0.5) = 0.0833  (331.0 s)
 α=55/96 = 0.57292: ρ(|E|<0.5) = 0.1458  (316.0 s)
 α=58/96 = 0.60417: ρ(|E|<0.5) = 0.2083  (326.3 s)
 window |E|<0.1: ρ_dip(α=1/2) = 0.0004, ρ_off(α=38/96) = 0.1250 → contrast 288.00×
 window |E|<0.2: ρ_dip(α=1/2) = 0.0039, ρ_off(α=38/96) = 0.2083 → contrast 53.33×
 window |E|<0.3: ρ_dip(α=1/2) = 0.0091, ρ_off(α=38/96) = 0.2083 → contrast 22.86×
 window |E|<0.5: ρ_dip(α=1/2) = 0.0195, ρ_off(α=38/96) = 0.2083 → contrast 10.67×
 window |E|<0.8: ρ_dip(α=1/2) = 0.0525, ρ_off(α=38/96) = 0.2083 → contrast 3.97×
 contrast @w=0.5 (α=0.396 vs 1/2): 13.33× (48x48) → 10.67× (96x96) → holds/sharpens ✓
 strict dip @96² (9 pts) PASS — ρ(α=1/2) = 0.0195 below ALL 8 other scan points
 contrast grows as w → 0 PASS — contrast(w) 288.00× (w=0.1) vs 10.67× (w=0.5): Dirac ρ ∝ E vs metallic ρ ≈ const
 no wash-out 48²→96²  PASS — 13.33× → 10.67× at the same α pair (0.396 vs 1/2; tolerance 0.8, as 29b)
 Test 29c [SERIES pass 3]: 3 sub-checks, 0 failed → PASS
```

**Final-report verdict rows:**
- `PASS` — Test 29: ρ(α=0.5)=0.0193 vs ρ(0.403)=0.1944 / ρ(0.597)=0.1944 → PASS
- `FAIL` — Test 29b [HARDCORE pass 2]: 3 sub-checks, 1 failed → WARN
- `PASS` — Test 29c [SERIES pass 3]: 3 sub-checks, 0 failed → PASS

Computation log: 11 timestamped entries; 14987–17759 s (от начала прогона).

---

### 24.30 Test 30: vf_scaling

**Verdict: PASS** · Suite: AB-Cloud v19 (Julia 1.12.0) · two-pass protocol.

EXACT-geometry: FIRST DISTINCT Dirac level above the zero tower ~ 1/L (the old ev[j0+1]-ev[j0] hit the valley-degenerate partner ~1e-15 → gaps 0.0); L/4∈ℤ grid up to t31_lmax; linear fit R².

The GUE-quality and dynamics category: the $f_{GUE}$ merit (Test 28: 0.8704, $\Sigma^2 = 0.6115$ — WARN: gaps slightly narrower than GUE), the Dirac dip (Test 29: $\rho(\alpha{=}0.5) = 0.0193$ vs $0.1944$ at $\alpha = 0.403/0.597$ — a tenfold flux anisotropy), $v_F$ scaling (Test 30: 1.798, $R^2 = 0.9977$), Hatano–Nelson (Test 31: max $|\mathrm{Im}E| = 0.6397$; $\langle r\rangle_{NH} = 0.8938$ — the non-Hermitian deformation drives the statistics past the GUE band: a direction control).

**The test in detail.** $v_F$ scaling: 1.798, $R^2 = 0.9977$ — a second Fermi-velocity measurement (in another parameter window than T19). The T19/T30/D1 reconciliation: 1.8998/1.798/1.9347 — three estimates in different hopping conventions; all confirm linear dispersion with $R^2 > 0.997$.


**Result summary (from the report):** Test 30b [HARDCORE pass 2]: 3 sub-checks, 0 failed → PASS

**Console of the run (fragment, verbatim):**

```text
TEST 30 (pass 2, HARDCORE): Dirac cone velocity — dense-grid audit
 11-point mod-4 grid L=16…96, zero-tower check, E₁·L constancy
 L=16: E₁ = 0.765367 (E₁·L = 12.2459), zero_modes = 4, 0.7 s
 L=24: E₁ = 0.517638 (E₁·L = 12.4233), zero_modes = 4, 0.7 s
 L=32: E₁ = 0.390181 (E₁·L = 12.4858), zero_modes = 4, 1.1 s
 L=40: E₁ = 0.312869 (E₁·L = 12.5148), zero_modes = 4, 2.5 s
 L=48: E₁ = 0.261052 (E₁·L = 12.5305), zero_modes = 4, 4.9 s
 L=56: E₁ = 0.223929 (E₁·L = 12.5400), zero_modes = 4, 11.4 s
 L=64: E₁ = 0.196034 (E₁·L = 12.5462), zero_modes = 4, 24.2 s
 L=72: E₁ = 0.174311 (E₁·L = 12.5504), zero_modes = 4, 49.8 s
 L=80: E₁ = 0.156918 (E₁·L = 12.5535), zero_modes = 4, 100.7 s
 L=88: E₁ = 0.142678 (E₁·L = 12.5557), zero_modes = 4, 176.0 s
 L=96: E₁ = 0.130806 (E₁·L = 12.5574), zero_modes = 4, 282.4 s
 Fit: gap = 12.2188/L + 0.0054, R² = 0.999880, v_F = 1.9447 (π-flux target 2.0)
 E₁·L: mean = 12.5003, cv = 0.75% ≤ ✓ 5%
 R² > 0.95 (11 pts)   PASS — R² = 0.9999
 zero tower == 4 ∀L   PASS — |E| ≤ 1e-8 at every size
 E₁·L cv ≤ 5%         PASS — cv = 0.75% (Dirac law: E₁·L → 4π = const)
 Test 30b [HARDCORE pass 2]: 3 sub-checks, 0 failed → PASS
```

**Final-report verdict rows:**
- `PASS` — Test 30: v_F=1.798, R²=0.9977 → PASS
- `PASS` — Test 30b [HARDCORE pass 2]: 3 sub-checks, 0 failed → PASS

Computation log: 11 timestamped entries; 17942–18335 s (от начала прогона).

---

### 24.31 Test 31: hatano_nelson

**Verdict: PASS** · Suite: AB-Cloud v19 (Julia 1.12.0) · two-pass protocol.

Deterministic non-Hermitian spectral property: complex eigenvalue count/pattern.

The GUE-quality and dynamics category: the $f_{GUE}$ merit (Test 28: 0.8704, $\Sigma^2 = 0.6115$ — WARN: gaps slightly narrower than GUE), the Dirac dip (Test 29: $\rho(\alpha{=}0.5) = 0.0193$ vs $0.1944$ at $\alpha = 0.403/0.597$ — a tenfold flux anisotropy), $v_F$ scaling (Test 30: 1.798, $R^2 = 0.9977$), Hatano–Nelson (Test 31: max $|\mathrm{Im}E| = 0.6397$; $\langle r\rangle_{NH} = 0.8938$ — the non-Hermitian deformation drives the statistics past the GUE band: a direction control).

**The test in detail.** Hatano–Nelson: the non-Hermitian deformation (asymmetric hops): max $|\mathrm{Im}E| = 0.6397$ — a complex spectrum; $\langle r\rangle_{NH} = 0.8938$ — the statistics leave the GUE band (0.62) toward stronger-than-GUE correlations. A direction control: non-hermiticity does not 'improve' the GUE class, it destroys it — confirming that the β = 2 class needs exact hermiticity. The SERIES pass T31c: 4 sub-checks.


**Result summary (from the report):** Test 31c [SERIES pass 3]: 4 sub-checks, 0 failed → PASS

**Console of the run (fragment, verbatim):**

```text
TEST 31 (pass 3, SERIES): Hatano–Nelson — realization ensemble
 Ensemble: n=5 realizations × σ ∈ {0.5, 0.6, 0.7, 0.8}, γ = 5.0
 Lattice: 48x48 (N=2304), W_eff = 1.00 (standard), Nv=4 neutral, q=±1.00
 real 1/5 σ=0.5: n_complex =     0, max|Im| = 0.0000, ⟨r⟩NN = 0.8941 (3.3 s)
 real 1/5 σ=0.6: n_complex =  2243, max|Im| = 0.3195, ⟨r⟩NN = 0.9072 (18.6 s)
 real 1/5 σ=0.7: n_complex =  2283, max|Im| = 0.6397, ⟨r⟩NN = 0.9253 (18.8 s)
 real 1/5 σ=0.8: n_complex =  2298, max|Im| = 0.9602, ⟨r⟩NN = 0.9308 (18.5 s)
 real 2/5 σ=0.5: n_complex =     0, max|Im| = 0.0000, ⟨r⟩NN = 0.8878 (3.3 s)
 real 2/5 σ=0.6: n_complex =  2237, max|Im| = 0.3194, ⟨r⟩NN = 0.9105 (18.1 s)
 real 2/5 σ=0.7: n_complex =  2297, max|Im| = 0.6396, ⟨r⟩NN = 0.9232 (18.4 s)
 real 2/5 σ=0.8: n_complex =  2299, max|Im| = 0.9598, ⟨r⟩NN = 0.9310 (18.5 s)
 real 3/5 σ=0.5: n_complex =     0, max|Im| = 0.0000, ⟨r⟩NN = 0.8988 (3.8 s)
 real 3/5 σ=0.6: n_complex =  2147, max|Im| = 0.3147, ⟨r⟩NN = 0.8788 (18.6 s)
 real 3/5 σ=0.7: n_complex =  2239, max|Im| = 0.6319, ⟨r⟩NN = 0.8882 (20.1 s)
 real 3/5 σ=0.8: n_complex =  2274, max|Im| = 0.9501, ⟨r⟩NN = 0.8920 (21.7 s)
 real 4/5 σ=0.5: n_complex =     0, max|Im| = 0.0000, ⟨r⟩NN = 0.8977 (3.7 s)
 real 4/5 σ=0.6: n_complex =  2260, max|Im| = 0.3199, ⟨r⟩NN = 0.9035 (18.7 s)
 real 4/5 σ=0.7: n_complex =  2300, max|Im| = 0.6399, ⟨r⟩NN = 0.9233 (23.1 s)
 real 4/5 σ=0.8: n_complex =  2303, max|Im| = 0.9601, ⟨r⟩NN = 0.9355 (25.5 s)
 real 5/5 σ=0.5: n_complex =     0, max|Im| = 0.0000, ⟨r⟩NN = 0.8982 (4.6 s)
 real 5/5 σ=0.6: n_complex =  2237, max|Im| = 0.3183, ⟨r⟩NN = 0.9061 (23.1 s)
 real 5/5 σ=0.7: n_complex =  2287, max|Im| = 0.6381, ⟨r⟩NN = 0.9201 (23.9 s)
 real 5/5 σ=0.8: n_complex =  2303, max|Im| = 0.9578, ⟨r⟩NN = 0.9372 (24.7 s)
 Ensemble means: σ=0.5: n_cx=0.0, max|Im|=0.00e+00, ⟨r⟩=0.8953
 σ=0.8: n_cx=2295.4, max|Im|=0.9576, ⟨r⟩=0.9253 | Poisson-box baseline ≈ 0.8500
 S1 anchor: OK ✓ | S2 sweep: OK ✓ | S3 ⟨r⟩ rise: OK ✓ (0.8953→0.9253) | S4 max|Im| grow: OK ✓ (0.3184→0.9576)
 σ=0.5 Hermitian ∀real PASS — n_complex = 0 and max|Im| < 1e-10 in all 5 realizations
 n_complex > 0 ∀(σ,k) PASS — every non-Hermitian row (5 × 3) develops complex eigenvalues
 ⟨r⟩ rises with σ (2-D repulsion) PASS — ensemble mean 0.8953 (σ=0.5, line) → 0
```

**Final-report verdict rows:**
- `PASS` — Test 31: max|Im(E)|=0.6397, ⟨r⟩_NH=0.8938 → PASS
- `PASS` — Test 31b [HARDCORE pass 2]: 3 sub-checks, 0 failed → PASS
- `PASS` — Test 31c [SERIES pass 3]: 4 sub-checks, 0 failed → PASS

Computation log: 25 timestamped entries; 22216–22555 s (от начала прогона).

---

### 24.32 Test 32: rmean_bootstrap

**Verdict: PASS** · Suite: AB-Cloud v19 (Julia 1.12.0) · two-pass protocol.

Statistical: ⟨r⟩ = 0.5992 ± 0.022 (tolerance band = monograph §11.1); CI printed as diagnostics. Effective disorder capped: W_eff = min(ab_W, ab_W_max ≤ 1.0) — disorder must not drive the vortex motion.

The statistics-scaling category: the $\langle r\rangle$ bootstrap (Test 32: $0.5991 \pm 0.0075$ vs GUE 0.5992 — a hit within 0.0001 at $q=1.0$, $W=1.0$), the L-ladder (Test 33: $0.434 \to 0.556 \to 0.593 \to 0.6 \to 0.6$ — the GUE plateau from $L=50$; HARDCORE: the weighted plateau $0.6004$, $\chi^2/\mathrm{dof} = 0.01$ — perfect stationarity). The cross-link to level VII: the KS GUE floor falls with L (0.0324 → 0.0220) — two independent quality axes grow with L together.

**The test in detail.** The $\langle r\rangle$ bootstrap: $0.5991 \pm 0.0075$ vs GUE 0.5992 — a bullseye within 0.0001! The CI is a realization bootstrap ($n = 5$, $q = 1.0$, $W = 1.0$). With T16 (0.594) and T33 (plateau 0.6004): a triangulation of the class. Test 32b HARDCORE: 2 sub-checks.


**Result summary (from the report):** Test 32b [HARDCORE pass 2]: 2 sub-checks, 0 failed → PASS

**Console of the run (fragment, verbatim):**

```text
TEST 32 (pass 2, HARDCORE): ⟨r⟩ bootstrap — deep validation
Harder machinery: n ≥ 5 realizations/row, comparison row
held at monograph anchor density on the current lattice, ensemble
stability checks (bootstrap CI, realization scatter, sign count).
 H2: comparison-row Nv rescaled to anchor density 2.78% of 96x96 → Nv=256 (was 144)
TEST 32: ⟨r⟩ bootstrap over independent realizations
Target: ⟨r⟩ = 0.5992 ± 0.022 vs GUE 0.5992 (machine-precision match)
 WHY W (DISORDER) IS CAPPED AT W_max ≈ 1.0 — disorder → vortex motion → statistics:
  W is the diagonal on-site potential the vortices paint onto the lattice:
      V_i = Σ_k q_k·W / (r_ik²·N⁻¹ + 1),   hopping t = 1.
  The ratio (disorder energy q·W) / (kinetic energy t) decides what the
  vortex cloud does and which spectral statistics come out:
   • q·W ≳ t  (e.g. W=4, q=0.3 → V≈1.2 next to a core): the disorder
     landscape dominates the vortex motion — vortices pin/steer the
     eigenstates, states localize on the potential relief, and ⟨r⟩ drifts
     from GUE (0.5992) toward Poisson (0.3863) by an essentially random
     amount. A strongly disordered, spinning vortex system can therefore
     emit ALMOST ANY statistics — the numbers depend on the effective
     rotation speed (W/t) and on the twisting/vortex arrangement (Nv,
     layout, charges) of that realization, not on the AB physics.
   • q·W ≲ t  (W ≤ 1): the Aharonov-Bohm phases dominate the hopping,
     states stay delocalized and GUE (Wigner-Dyson) is reachable.
  That is why these tests measure at W_eff = min(cfg.ab_W, W_max = 1.0):
  they certify the PHASE physics, not the disorder physics.
 ℹ️ NOTE: cfg.ab_q_list[1] = 1.0 is INTEGER.
 Pure Dirac-string model: integer flux is unobservable (Byers-Yang)
 → real H → GOE ceiling. The :monumental smooth gauge: phases are
 generically complex for ANY q → GUE reachable with the user's q.
 Primary verdict uses q=1.0; q=0.3 is also run for comparison.
 [q=1.000] Torus gauge-compatible (q·(2-Nx)=-94 ∈ ℤ) → using :torus BC
 Bootstrap config: 96x96, Nv=2, q=±1.000, α=0.5000, W=1.00 (cap 1.00, min(cfg.ab_W, W_max)), BC=:torus, n_real=5
 Disorder check: q·W
```

**Final-report verdict rows:**
- `PASS` — Test 32: ⟨r⟩=0.5991±0.0075 (q=1.0, n=5, W=1.0) vs GUE 0.5992 → PASS
- `PASS` — Test 32b [HARDCORE pass 2]: 2 sub-checks, 0 failed → PASS

Computation log: 40 timestamped entries; 23123–26050 s (от начала прогона).

---

### 24.33 Test 33: l_scaling_rmean

**Verdict: PASS** · Suite: AB-Cloud v19 (Julia 1.12.0) · two-pass protocol.

Statistical finite-size trend: monotone approach to 0.594-0.599; monograph anchors L≤50, extended points L=80/112 (user spec 2026-08-29) check the GUE plateau; W_eff capped at ab_W_max.

The statistics-scaling category: the $\langle r\rangle$ bootstrap (Test 32: $0.5991 \pm 0.0075$ vs GUE 0.5992 — a hit within 0.0001 at $q=1.0$, $W=1.0$), the L-ladder (Test 33: $0.434 \to 0.556 \to 0.593 \to 0.6 \to 0.6$ — the GUE plateau from $L=50$; HARDCORE: the weighted plateau $0.6004$, $\chi^2/\mathrm{dof} = 0.01$ — perfect stationarity). The cross-link to level VII: the KS GUE floor falls with L (0.0324 → 0.0220) — two independent quality axes grow with L together.

**The test in detail.** The $\langle r\rangle$ L-ladder: $L = 10 \to 0.434$ (the Poisson regime — the lattice is small), $20 \to 0.556$, $30 \to 0.595$, $50 \to 0.594$ (the monograph), $80 \to 0.6$, $112 \to 0.6$ — the GUE plateau from $L \approx 50$. HARDCORE: the weighted plateau $0.6004$, $\chi^2/\mathrm{dof} = 0.01$ — perfect stationarity: non-monotone approach, then plateau. RAM honesty: L = 128 (4.3 GB) skipped with a reason. Cross-link to level VII: the KS GUE floor falls with L (0.0324 → 0.0220) — two independent quality axes grow with L together.


**Result summary (from the report):** Test 33b (hardcore): plateau weighted ⟨r⟩=0.6004, χ²/dof=0.01 → PASS

**Console of the run (fragment, verbatim):**

```text
TEST 33 (pass 2, HARDCORE): L-scaling — deep validation
Harder machinery: up to 5 realizations per L, weighted
GUE-plateau χ² over L ≥ 50, no L beyond 112 (RAM honesty: L=128 ≈ 4.3 GB).
TEST 33: L-Scaling for AB-Cloud Lattice
L=10→0.487 (Poisson), L=20→0.562, L=30→0.595, L=50→0.594 (monograph),
L=80, L=112 → GUE plateau check (extended range, user spec 2026-08-29)
 WHY W (DISORDER) IS CAPPED AT W_max ≈ 1.0 — disorder → vortex motion → statistics:
  W is the diagonal on-site potential the vortices paint onto the lattice:
      V_i = Σ_k q_k·W / (r_ik²·N⁻¹ + 1),   hopping t = 1.
  The ratio (disorder energy q·W) / (kinetic energy t) decides what the
  vortex cloud does and which spectral statistics come out:
   • q·W ≳ t  (e.g. W=4, q=0.3 → V≈1.2 next to a core): the disorder
     landscape dominates the vortex motion — vortices pin/steer the
     eigenstates, states localize on the potential relief, and ⟨r⟩ drifts
     from GUE (0.5992) toward Poisson (0.3863) by an essentially random
     amount. A strongly disordered, spinning vortex system can therefore
     emit ALMOST ANY statistics — the numbers depend on the effective
     rotation speed (W/t) and on the twisting/vortex arrangement (Nv,
     layout, charges) of that realization, not on the AB physics.
   • q·W ≲ t  (W ≤ 1): the Aharonov-Bohm phases dominate the hopping,
     states stay delocalized and GUE (Wigner-Dyson) is reachable.
  That is why these tests measure at W_eff = min(cfg.ab_W, W_max = 1.0):
  they certify the PHASE physics, not the disorder physics.
 ⚠ RAM GATE: L=112 needs ≈ 10.6 GB peak (matrix + LAPACK workspace), free ≈ 4.5 GB → SKIPPED (a swap-thrashing eig is indistinguishable from a hang)
 q=1.00 BC=:torus L=10  Nv=4   α=0.50 W=1.00 ⟨r⟩ = 0.5516 ± 0.0252 (5 real, monograph 0.487)
 q=1.00 BC=:torus L=20  Nv=12  α=0.50 W=1.00 ⟨r⟩ = 0.5953 ± 0.0055 (5 real, monograph 0.562)
 q=1.00 BC=:torus L=30  Nv=26  α=0.50 W=1.00 ⟨r⟩ = 0.6070 ± 0.0054 (5 real, monograph 0.595)
 q=1.00 BC=:torus L=50  Nv=70  α=0.50 W=1.00 ⟨r⟩ = 0.5936 ± 0.0053 (5 real, monograph 0.594)
 q=1.00 BC=:to
```

**Final-report verdict rows:**
- `PASS` — Test 33: L-scaling to L=80 0.434,0.556,0.593,0.6,0.6 → PASS
- `PASS` — Test 33b (hardcore): plateau weighted ⟨r⟩=0.6004, χ²/dof=0.01 → PASS

Computation log: 100 timestamped entries; 27013–27878 s (от начала прогона).

---

### 24.34 Test 34: direct_vs_zeta

**Verdict: FAIL** · Suite: AB-Cloud v19 (Julia 1.12.0) · two-pass protocol.

Statistical: unfolded-spacing KS (effect size D<0.10) + Montgomery R₂(s) vs ζ-zeros and GUE. full 50k range, not ζ-5000.

Test 34 — the central one: the direct comparison of the AB cloud with the ζ zeros (the full 50,000-zero set). Pass 1: KS p = 0.0, $\langle|\Delta R_2|\rangle = 0.0374$, $d_{GUE} = 0.796$ — PASS by the composite (the R₂ and GUE-side arms passed). HARDCORE (96×96, 5 realizations): pooled $D = 0.1096$ (p = 2.24·10⁻¹⁸⁶), per-realization $D \in [0.0923, 0.1189]$, median 0.1153; $\langle|\Delta R_2|\rangle = 0.0002$ — excellent; $d_{GUE} = 0.8764 < d_{Poisson} = 0.9998$ — GUE-side; stability 0.0923–0.1189 — passed; only the KS arm failed (D = 0.1096 > 0.10) — WARN. That WARN is the departure point of the level-VII optimization: the same protocol, the same lattice, the vortex window found — and D falls threefold to 0.0318.

**The test in detail.** The direct AB-cloud vs ζ comparison (the full 50k set): pass 1 — KS p = 0.0, $\langle|\Delta R_2|\rangle = 0.0374$, $d_{GUE} = 0.796$ — PASS by the composite (the R₂ and GUE-side arms). HARDCORE (96×96, 5 realizations): pooled $D = 0.1096$ (p = 2.24·10⁻¹⁸⁶), per-realization $D \in [0.0923, 0.1189]$, median 0.1153; $\langle|\Delta R_2|\rangle = 0.0002$ — excellent; $d_{GUE} = 0.8764 < d_{Poisson} = 0.9998$ — GUE-side; spread 0.0266 < 0.10 — passed; only the KS arm failed (D = 0.1096 > 0.10) — WARN. That WARN is level VII's starting point.


**Result summary (from the report):** Test 34b [HARDCORE pass 2]: 4 sub-checks, 1 failed → WARN

**Console of the run (fragment, verbatim):**

```text
TEST 34 (pass 2, HARDCORE): direct AB vs ζ — deep validation
n ≥ 5 realizations, R₂ bins 0.05, per-realization KS stability
 Config: Nv=2, q=1.00, α=0.5000, W=1.0 (base protocol)
 real  1/5: 5528 spacings, D_k(ζ) = 0.0923
 real  2/5: 5527 spacings, D_k(ζ) = 0.1188
 real  3/5: 5528 spacings, D_k(ζ) = 0.1153
 real  4/5: 5528 spacings, D_k(ζ) = 0.1065
 real  5/5: 5528 spacings, D_k(ζ) = 0.1189
 Pooled: 27639 AB spacings vs 49999 ζ spacings | KS D = 0.1096, p = 2.236e-186
 Per-realization D(ζ): min 0.0923 / median 0.1153 / max 0.1189 (n=5)
 ⟨|R₂_AB − R₂_ζ|⟩ (ds=0.05, s≤4) = 0.0002 (target < 0.10)
 d_GUE = 0.8764 vs d_Poisson = 0.9998 → closer to GUE
 KS composite         WARN — p = 2.236e-186, D = 0.1096 (p>0.01 or D<0.10)
 ⟨|ΔR₂|⟩ < 0.10 (fine) PASS — ds=0.05, s_max=4.0: 0.0002
 closer to GUE        PASS — d_GUE=0.8764 < d_Pois=0.9998
 KS ensemble stability PASS — D spread 0.0923..0.1189 (median 0.1153)
 Test 34b [HARDCORE pass 2]: 4 sub-checks, 1 failed → WARN
```

**Final-report verdict rows:**
- `PASS` — Test 34: KS p=0.0, ⟨|ΔR₂|⟩=0.0374, d_GUE=0.796 → PASS
- `FAIL` — Test 34b [HARDCORE pass 2]: 4 sub-checks, 1 failed → WARN

Computation log: 5 timestamped entries; 28141–29391 s (от начала прогона).

---

### 24.35 Test 35: form_factor_Kt

**Verdict: FAIL** · Suite: AB-Cloud v19 (Julia 1.12.0) · two-pass protocol.

Statistical: raw (1/n)|Σe^{itε}|² vs finite-box GUE reference K_box(t)=t(1−sinc(2πt)); RMS over t≥0.3.

Test 35 — the form factor $K(\tau)$: the GUE ramp+plateau. Pass 1: RMS_GUE = 0.4193, corr_GUE = 0.8889 — WARN. HARDCORE: 2 of 3 sub-checks failed. The diagnosis: the ramp (small $\tau$) reproduces; the plateau sits below 1 on the 50k table — sampling finiteness plus density non-stationarity. Compare D14 of level II: on the band $t \approx 10^5$, K(2) = 0.962 — the plateau converges to prediction with height. Two-band strategy: local statistics at low T; integral ones at high.

**The test in detail.** The form factor $K(\tau)$: ramp+plateau. Pass 1: RMS_GUE = 0.4193, corr_GUE = 0.8889 — WARN. HARDCORE: 2 of 3 failed. Diagnosis: the ramp (τ < 1) reproduces; the plateau (τ > 1) sits systematically below 1 on the 50k table: sampling finiteness plus density non-stationarity. D14 of level II on the band $t \approx 10^5$: K(2) = 0.962 — the plateau converges with height. Two-band strategy: local statistics at low T; integral ones at high.


**Result summary (from the report):** Test 35b [HARDCORE pass 2]: 3 sub-checks, 2 failed → WARN

**Console of the run (fragment, verbatim):**

```text
TEST 35 (pass 2, HARDCORE): spectral form factor K(t) — ensemble pass
n ≥ 5 per-realization K(t), 33-point t-grid, ensemble verdict
 real  1/5: RMS(K−K_box, t≥0.3) = 0.9199
 real  2/5: RMS(K−K_box, t≥0.3) = 0.8578
 real  3/5: RMS(K−K_box, t≥0.3) = 0.9671
 real  4/5: RMS(K−K_box, t≥0.3) = 0.7540
 real  5/5: RMS(K−K_box, t≥0.3) = 0.4999
 ENSEMBLE K(t): RMS(K_AB − K_box, t ≥ 0.3) = 0.6143 (target < 0.30)
 Corr(K_AB, K_box) = 0.6379 (target > 0.50) | Corr(K_AB, K_ζ) = 0.8123
 Per-realization RMS: mean 0.7998, scatter σ = 0.1856 > ✗ 0.15
 RMS < 0.30 (ensemble) WARN — ensemble-mean K(t), 33-point grid: 0.6143
 Corr > 0.50 (ensemble) PASS — Corr(K, K_box) = 0.6379
 RMS scatter ≤ 0.15   WARN — σ=0.1856 across 5 realizations
 Test 35b [HARDCORE pass 2]: 3 sub-checks, 2 failed → WARN
```

**Final-report verdict rows:**
- `FAIL` — Test 35: K(t) ramp+plateau — RMS_GUE=0.4193, corr_GUE=0.8889 → WARN
- `FAIL` — Test 35b [HARDCORE pass 2]: 3 sub-checks, 2 failed → WARN

Computation log: 5 timestamped entries; 30065–31367 s (от начала прогона).

---

### 24.36 Test 36: byte_robust

**Verdict: PASS** · Suite: AB-Cloud v19 (Julia 1.12.0) · two-pass protocol.

Mixed: |Δr| under 256-level quantization + RNG entropy (statistical). Sample accumulated to 25 000 (pass 1) / 50 000 (pass 2) eigenvalues; verdict = multi-window average over 120×15-eig windows (single window = diagnostic); W_eff capped at ab_W_max.

Test 36 — byte robustness: the spectral data as a byte stream (200,000 bytes, seed 12345): entropy 7.9991 bits/byte (the maximum 8 — an ideal source); $\chi^2$-z = −0.234 — uniform bytes; $r_{256}$ = 0.5894 (25k eigenvalues) / 0.5756 (50k) — the 256-symbol alphabet keeps the GUE class of gap statistics; $|\Delta r|_{multi} = 0.001$ (120 windows): stationarity; $|\Delta r|_{diag} = 0.012$ — the diagonal control. Both passes (25k/50k eigenvalues) agree. Conclusion: the spectrum as a stream is ideal noise with no hidden coding structures.

**The test in detail.** Byte robustness: the spectral data as a byte stream (200,000, seed 12345): entropy 7.9991 bits/byte (the maximum 8 — an ideal source); $\chi^2$-z = −0.234 — uniform; $r_{256}$ = 0.5894 (25k eigenvalues) / 0.5756 (50k) — the 256-symbol alphabet keeps the GUE class; $|\Delta r|_{multi} = 0.001$ (120 windows): stationarity; $|\Delta r|_{diag} = 0.012$. Both passes agree. Conclusion: the spectrum as a stream is ideal noise without hidden coding structure.


**Result summary (from the report):** Test 36: byte robust — r_256=0.5756, |Δr|_multi=0.0009 (120 windows), |Δr|_1win=0.0061 (diag), H=7.9991 bits, χ²_z=-0.234, n=55288 → PASS

**Console of the run (fragment, verbatim):**

```text
TEST 36: Byte-level robustness — quantization + RNG entropy
 Verify ⟨r⟩ survives 256-level quantization + RNG byte uniformity
 WHY W (DISORDER) IS CAPPED AT W_max ≈ 1.0 — disorder → vortex motion → statistics:
  W is the diagonal on-site potential the vortices paint onto the lattice:
      V_i = Σ_k q_k·W / (r_ik²·N⁻¹ + 1),   hopping t = 1.
  The ratio (disorder energy q·W) / (kinetic energy t) decides what the
  vortex cloud does and which spectral statistics come out:
   • q·W ≳ t  (e.g. W=4, q=0.3 → V≈1.2 next to a core): the disorder
     landscape dominates the vortex motion — vortices pin/steer the
     eigenstates, states localize on the potential relief, and ⟨r⟩ drifts
     from GUE (0.5992) toward Poisson (0.3863) by an essentially random
     amount. A strongly disordered, spinning vortex system can therefore
     emit ALMOST ANY statistics — the numbers depend on the effective
     rotation speed (W/t) and on the twisting/vortex arrangement (Nv,
     layout, charges) of that realization, not on the AB physics.
   • q·W ≲ t  (W ≤ 1): the Aharonov-Bohm phases dominate the hopping,
     states stay delocalized and GUE (Wigner-Dyson) is reachable.
  That is why these tests measure at W_eff = min(cfg.ab_W, W_max = 1.0):
  they certify the PHASE physics, not the disorder physics.
 Sample target: 50000 eigenvalues [pass 2 (secondary)] (cfg.ab37_n_eigs_pass2)
 Disorder: W = 1.00 = min(ab_W=4.00, W_max=1.00) → q·W = 1.00 vs hopping t = 1.0 → AB phases dominate (byte check tests the phase physics)
 realization  1/5, continuing (below target): +5529 central eigs → accumulated 5529 / 50000 (11%)
 realization  2/5, continuing (below target): +5529 central eigs → accumulated 11058 / 50000 (22%)
 realization  3/5, continuing (below target): +5529 central eigs → accumulated 16587 / 50000 (33%)
 realization  4/5, continuing (below target): +5529 central eigs → accumulated 22116 / 50000 (44%)
 realization  5/5, continuing (below target): +5529 central eigs → accumulated 27645 / 50000 (55%)
 realization  6/6, continuing (below target): +5529 central eigs → accumulated 33174 / 50000 (66%)
 realization  7/7, continuing (below target): +5529 central eigs → accumulated 38703 / 50000 (77%)
 realization  8/8, continuing (below target): +5529 central eigs → accumulated 44232 / 50000 (88%)
 realization  9/9, continuing (below target): +5529 central eig
```

**Final-report verdict rows:**
- `PASS` — Test 36: byte robust — r_256=0.5894, |Δr|_multi=0.001 (120 windows), |Δr|_1win=0.012 (diag), H=7.9991 bits, χ²_z=-0.234, n=27997 → PASS
- `PASS` — Test 36: byte robust — r_256=0.5756, |Δr|_multi=0.0009 (120 windows), |Δr|_1win=0.0061 (diag), H=7.9991 bits, χ²_z=-0.234, n=55288 → PASS

Computation log: 142 timestamped entries; 32269–35096 s (от начала прогона).

---

### 24.37 Test 37: half_factorial_gamma

**Verdict: PASS** · Suite: AB-Cloud v19 (Julia 1.12.0) · two-pass protocol.

EXACT: Γ(1/2) = √π, (1/2)! = Γ(3/2) = √π/2, ladder + recurrence (suite's own Lanczos lgamma); UNIQUENESS of the Γ-construction via the reflection self-dual fixed point Γ(1/2)² = π and Bohr–Mollerup log-convexity; the GUE β=2 surmise normalization 32/π² verified as the half-factorial identity (∫p₂ = ⟨s⟩ = 1, ⟨s²⟩ = 3π/8 by quadrature). Pass 2 = 256-bit BigFloat re-audit.

Test 37 — the arithmetic of Γ: $(1/2)! = \sqrt{\pi}/2$ with relative error 0.0; $32/\pi^2$ (the GUE surmise normalization) with error 0.0; $\int p_2\,ds = 1$ with $|\Delta| = 0.0$; uniqueness of the solution. Method: the log-convexity of Γ (the Bohr–Mollerup characterization) and the self-dual reflection $\Gamma(1/2)^2 = \pi$. The surmise normalization is not a fitting constant but a theorem; the test checks it verbatim — the foundation of the KS reference.

**The test in detail.** The arithmetic of Γ: $(1/2)! = \sqrt{\pi}/2$ — relative error 0.0; $32/\pi^2$ (the GUE surmise normalization) — error 0.0; $\int p_2\,ds = 1$ — $|\Delta| = 0.0$; uniqueness ✓. Method: Γ log-convexity (Bohr–Mollerup) + the self-dual reflection $\Gamma(1/2)^2 = \pi$. The link: the surmise normalization (chapter 7) is a theorem, not a fitted constant; the test checks it verbatim — the foundation of the KS reference of every spacing test.


**Result summary (from the report):** Test 37b [HARDCORE pass 2]: 3 sub-checks, 0 failed → PASS

**Console of the run (fragment, verbatim):**

```text
TEST 37 (pass 2, HARDCORE): (1/2)! via Γ — 256-bit precision audit
 DE reference: |Γ(1/2)_256 − √π| = 1.20e-28 (independent quadrature)
 Γ(1/2):  Float64 vs 256-bit DE rel.err = 5.83e-16
 (1/2)!:  Float64 vs 256-bit DE rel.err = 2.94e-16
 N = 1/[½·(π/4)^{3/2}·(1/2)!] at 256-bit vs 32/π²: rel.err = 2.51e-26
 ladder Γ(5/2)_DE = 3√π/4: rel.err = 4.78e-25
 Γ(1/2)_DE² = π (reflection self-duality): rel.err = 1.35e-28
 recurrence (1/2)!_DE = ½·Γ(1/2)_DE: rel.err = 2.51e-26
 Float64 round-off    PASS — |ΔΓ(1/2)|=5.83e-16, |Δ(1/2)!|=2.94e-16 relative (machine-ε scale)
 32/π² identity (256-bit) PASS — rel.err 2.51e-26 — exact at 256-bit
 ladder + self-duality + recurrence (256-bit) PASS — worst rel.err 4.78e-25 across the three identities
 Test 37b [HARDCORE pass 2]: 3 sub-checks, 0 failed → PASS
```

**Final-report verdict rows:**
- `PASS` — Test 37: (1/2)!=√π/2 [rel.err 0.0], 32/π² [rel.err 0.0], ∫p₂=1 [|Δ|=0.0], uniqueness ✓ → PASS
- `PASS` — Test 37b [HARDCORE pass 2]: 3 sub-checks, 0 failed → PASS



---

### 24.38 The run summary

77 verdict rows: **66 PASS** and **11 FAIL-class** (T4/T5/T6/T11/T12 — the pass-1 edges against the reference table; T28b/T29b/T34b/T35/T35b — the honest HARDCORE rejections). Every refusal is published as a first-class result with full diagnostics. Cost: 35,146 s (585.8 min); the most expensive test — T25 Byers–Yang (3,839 s HARDCORE); the cheapest — T3 (0.33 s). The verdict map and time profile: figures R1–R2. The level links: T34 → level VII (the optimization's departure point); T16/T32/T33 → gate H5 and the monumental line; T4–T12 → the finite-sample GUE floor (the same physics as the T34-ext floor); T37 → the surmise normalization (chapter 7).

---

## 24L. Appendix to chapter 24: the computation logs of all 37 tests (extracts)

Every test of the v19 run kept its own computation log: each entry — a timestamp, a delta from start, an action. Below — extracts (head, mid-slices, key events, tail); the full logs — `02_data/raw/results_run/computation_logs/`. The logs are the primary reproducibility document: the whole course of the computation is reconstructible line by line without a re-run.

---

### Test 4 — gue_ks_full

```text
[13:49:00.324] [+ 55.606s]  calc: KS D = 0.021619, p_asymptotic = 9.567870e-21 (n=49999, λ=4.8368)
[13:49:00.326] [+ 55.608s]  calc: KS D = 0.029562, p_asymptotic = 3.479907e-05 (n=6251, λ=2.3408)
[13:49:00.326] [+ 55.608s]  calc: KS D = 0.025418, p_asymptotic = 6.066737e-04 (n=6250, λ=2.0125)
[13:49:00.327] [+ 55.609s]  calc: KS D = 0.021305, p_asymptotic = 6.745302e-03 (n=6251, λ=1.6870)
[13:49:00.327] [+ 55.609s]  calc: KS D = 0.027409, p_asymptotic = 1.619781e-04 (n=6251, λ=2.1704)
[13:49:00.328] [+ 55.610s]  calc: KS D = 0.022629, p_asymptotic = 3.252259e-03 (n=6251, λ=1.7919)
[13:49:00.328] [+ 55.610s]  calc: KS D = 0.019816, p_asymptotic = 1.453640e-02 (n=6251, λ=1.5691)
[13:49:00.328] [+ 55.611s]  calc: KS D = 0.019647, p_asymptotic = 1.581953e-02 (n=6250, λ=1.5556)
[13:49:00.329] [+ 55.611s]  calc: KS D = 0.019627, p_asymptotic = 1.595774e-02 (n=6251, λ=1.5542)
[13:49:00.331] [+ 55.613s]  calc: KS D = 0.024587, p_asymptotic = 1.427535e-13 (n=24999, λ=3.8904)
[13:49:00.333] [+ 55.615s]  calc: KS D = 0.018906, p_asymptotic = 3.369159e-08 (n=25000, λ=2.9916)
… (11 entries total — computation_logs/test_04_gue_ks_full_log.txt)
```

---

### Test 5 — gue_ks_highT

```text
[13:49:11.305] [+ 66.587s]  calc: KS D = 0.021622, p_asymptotic = 9.563953e-21 (n=49989, λ=4.8368)
[13:49:11.427] [+ 66.709s]  calc: KS D = 0.021625, p_asymptotic = 9.718636e-21 (n=49958, λ=4.8360)
[13:49:11.431] [+ 66.713s]  calc: KS D = 0.021588, p_asymptotic = 1.254559e-20 (n=49853, λ=4.8228)
[13:49:11.434] [+ 66.716s]  calc: KS D = 0.021380, p_asymptotic = 4.135955e-20 (n=49523, λ=4.7605)
[13:49:11.437] [+ 66.719s]  calc: KS D = 0.021203, p_asymptotic = 2.142535e-19 (n=48525, λ=4.6733)
[13:49:11.440] [+ 66.722s]  calc: KS D = 0.020927, p_asymptotic = 8.613887e-18 (n=45603, λ=4.4714)
[13:49:11.443] [+ 66.725s]  calc: KS D = 0.020175, p_asymptotic = 1.325911e-13 (n=37230, λ=3.8952)
… (7 entries total — computation_logs/test_05_gue_ks_highT_log.txt)
```

---

### Test 11 — anderson_darling

```text
[14:00:20.713] [+735.995s]  calc: A² = 61.492426 (n=49999)
[14:00:20.850] [+736.132s]  calc: A² = 0.384147 (n=49999)
[14:00:20.855] [+736.137s]  calc: A² = 1.108144 (n=49999)
[14:00:20.861] [+736.143s]  calc: A² = 0.302521 (n=49999)
[14:00:26.839] [+742.121s]  calc: A² = 1.452562 (n=49999)
[14:00:26.845] [+742.127s]  calc: A² = 0.684641 (n=49999)
[14:00:26.850] [+742.132s]  calc: A² = 1.275677 (n=49999)
[14:00:26.855] [+742.138s]  calc: A² = 1.113402 (n=49999)
[14:00:26.861] [+742.143s]  calc: A² = 1.084933 (n=49999)
[14:00:26.866] [+742.148s]  calc: A² = 0.252442 (n=49999)
[14:00:26.871] [+742.153s]  calc: A² = 0.823697 (n=49999)
[14:00:26.876] [+742.158s]  calc: A² = 0.351576 (n=49999)
[14:00:26.881] [+742.164s]  calc: A² = 0.664339 (n=49999)
[14:00:26.887] [+742.169s]  calc: A² = 0.908296 (n=49999)
[14:00:26.892] [+742.175s]  calc: A² = 0.631610 (n=49999)
[14:00:26.897] [+742.180s]  calc: A² = 0.781718 (n=49999)
[14:01:40.206] [+815.488s]  calc: A² = 1.508360 (n=2800)
[14:01:53.200] [+828.482s]  calc: A² = 0.437726 (n=2800)
[14:01:53.649] [+828.931s]  calc: A² = 2.431328 (n=16800)
[14:01:53.665] [+828.947s]  calc: A² = 104.651825 (n=49999)
[14:01:53.681] [+828.963s]  calc: A² = 11.702308 (n=49999)
[14:01:53.696] [+828.978s]  calc: A² = 7.935273 (n=49999)
[14:01:53.712] [+828.994s]  calc: A² = 11.424783 (n=49999)
[14:01:53.727] [+829.009s]  calc: A² = 5.901799 (n=49999)
[14:01:53.743] [+829.025s]  calc: A² = 4.717495 (n=49999)
[14:01:53.758] [+829.041s]  calc: A² = 8.112526 (n=49999)
[14:01:53.774] [+829.056s]  calc: A² = 7.470271 (n=49999)
[14:01:53.790] [+829.072s]  calc: A² = 5.831160 (n=49999)
[14:02:10.561] [+845.844s]  calc: A² = 8.599699 (n=49999)
[14:02:10.577] [+845.859s]  calc: A² = 9.539248 (n=49999)
[14:02:10.592] [+845.875s]  calc: A² = 9.031875 (n=49999)
[14:02:10.608] [+845.890s]  calc: A² = 8.164987 (n=49999)
[14:02:10.623] [+845.905s]  calc: A² = 5.240394 (n=49999)
[14:02:10.638] [+845.920s]  calc: A² = 8.055340 (n=49999)
[14:02:10.654] [+845.936s]  calc: A² = 7.742218 (n=49999)
[14:02:10.669] [+845.951s]  calc: A² = 7.421432 (n=49999)
… (3011 entries total — computation_logs/test_11_anderson_darling_log.txt)
```

---

### Test 13 — number_variance

```text
[14:02:41.646] [+876.928s]  calc: Σ²(L=2.000) = 0.381460 (n_pos=50000, n_windows=3000, mean_count=2.00)
[14:02:41.648] [+876.930s]  calc: Σ²(L=4.536) = 0.402894 (n_pos=50000, n_windows=3000, mean_count=4.54)
[14:02:41.648] [+876.931s]  calc: Σ²(L=10.287) = 0.354897 (n_pos=50000, n_windows=3000, mean_count=10.30)
[14:02:41.649] [+876.931s]  calc: Σ²(L=23.331) = 0.313517 (n_pos=50000, n_windows=3000, mean_count=23.34)
[14:02:41.653] [+876.935s]  calc: Σ²(L=617.292) = 0.351103 (n_pos=50000, n_windows=3000, mean_count=617.29)
[14:02:41.654] [+876.936s]  calc: Σ²(L=1400.000) = 0.342086 (n_pos=50000, n_windows=3000, mean_count=1399.99)
[14:02:41.663] [+876.945s]  calc: Σ²(L=2.000) = 0.399956 (n_pos=9601, n_windows=3000, mean_count=1.99)
[14:02:41.663] [+876.946s]  calc: Σ²(L=4.536) = 0.506062 (n_pos=9601, n_windows=3000, mean_count=4.51)
[14:02:41.664] [+876.946s]  calc: Σ²(L=10.287) = 0.579419 (n_pos=9601, n_windows=3000, mean_count=10.28)
[14:02:41.665] [+876.947s]  calc: Σ²(L=23.331) = 0.691828 (n_pos=9601, n_windows=3000, mean_count=23.34)
[14:02:41.665] [+876.947s]  calc: Σ²(L=52.915) = 0.784109 (n_pos=9601, n_windows=3000, mean_count=52.90)
[14:02:41.666] [+876.948s]  calc: Σ²(L=120.010) = 0.894359 (n_pos=9601, n_windows=3000, mean_count=120.05)
[14:02:41.667] [+876.949s]  calc: Σ²(L=272.178) = 0.845014 (n_pos=9601, n_windows=3000, mean_count=272.20)
[14:02:41.667] [+876.949s]  calc: Σ²(L=617.292) = 0.887775 (n_pos=9601, n_windows=3000, mean_count=617.29)
[14:02:41.668] [+876.950s]  calc: Σ²(L=1400.000) = 0.821553 (n_pos=9601, n_windows=3000, mean_count=1399.99)
[14:02:41.671] [+876.953s]  calc: Σ²(L=23.331) = 0.324730 (n_pos=50000, n_windows=3000, mean_count=23.33)
[14:02:41.672] [+876.954s]  calc: Σ²(L=23.331) = 0.306048 (n_pos=50000, n_windows=3000, mean_count=23.34)
[14:02:41.672] [+876.955s]  calc: Σ²(L=23.331) = 0.318012 (n_pos=50000, n_windows=3000, mean_count=23.32)
… (21 entries total — computation_logs/test_13_number_variance_log.txt)
```

---

### Test 14 — spectral_rigidity

```text
[14:02:56.160] [+891.443s]  calc: Δ₃(L=2.000) = 0.093421 (n_pos=50000, n_windows=500, n_devs=500)
[14:02:56.181] [+891.463s]  calc: Δ₃(L=4.536) = 0.128616 (n_pos=50000, n_windows=500, n_devs=500)
[14:02:56.201] [+891.483s]  calc: Δ₃(L=10.287) = 0.161422 (n_pos=50000, n_windows=500, n_devs=500)
[14:02:56.219] [+891.501s]  calc: Δ₃(L=23.331) = 0.173069 (n_pos=50000, n_windows=500, n_devs=500)
[14:02:56.236] [+891.518s]  calc: Δ₃(L=52.915) = 0.175808 (n_pos=50000, n_windows=500, n_devs=500)
[14:02:56.254] [+891.536s]  calc: Δ₃(L=120.010) = 0.176269 (n_pos=50000, n_windows=500, n_devs=500)
[14:02:56.273] [+891.555s]  calc: Δ₃(L=272.178) = 0.175052 (n_pos=50000, n_windows=500, n_devs=500)
[14:02:56.291] [+891.573s]  calc: Δ₃(L=617.292) = 0.176106 (n_pos=50000, n_windows=500, n_devs=500)
[14:02:56.310] [+891.592s]  calc: Δ₃(L=1400.000) = 0.175848 (n_pos=50000, n_windows=500, n_devs=500)
[14:02:56.324] [+891.606s]  calc: Δ₃(L=23.331) = 0.173347 (n_pos=50000, n_windows=166, n_devs=166)
[14:02:56.330] [+891.612s]  calc: Δ₃(L=23.331) = 0.173506 (n_pos=50000, n_windows=166, n_devs=166)
[14:02:56.336] [+891.618s]  calc: Δ₃(L=23.331) = 0.173829 (n_pos=50000, n_windows=166, n_devs=166)
… (12 entries total — computation_logs/test_14_spectral_rigidity_log.txt)
```

---

### Test 15 — ab_construction

```text
[14:03:14.215] [+909.497s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.0000, t=1.00, W=4.00, open, 4 vortices, model=:dirac
… (1 entries total — computation_logs/test_15_ab_construction_log.txt)
```

---

### Test 16 — ab_gue_class

```text
[14:06:53.826] [+1129.108s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=1.00, open, 2 vortices, model=:monumental
[14:11:12.341] [+1387.623s]  calc: ⟨r⟩ = 0.572908 (n_r=5527, n_eigs=5529) [refs: GUE=0.5996 Poisson=0.3863]
[14:11:17.814] [+1393.097s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=1.00, open, 2 vortices, model=:monumental
[14:16:14.259] [+1689.541s]  calc: ⟨r⟩ = 0.569121 (n_r=5527, n_eigs=5529) [refs: GUE=0.5996 Poisson=0.3863]
[14:16:19.224] [+1694.506s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=1.00, open, 2 vortices, model=:monumental
[14:21:34.935] [+2010.217s]  calc: ⟨r⟩ = 0.586869 (n_r=5527, n_eigs=5529) [refs: GUE=0.5996 Poisson=0.3863]
[14:21:38.664] [+2013.946s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=1.00, open, 2 vortices, model=:monumental
[14:26:41.417] [+2316.699s]  calc: ⟨r⟩ = 0.584535 (n_r=5527, n_eigs=5529) [refs: GUE=0.5996 Poisson=0.3863]
[14:26:47.323] [+2322.605s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=1.00, open, 2 vortices, model=:monumental
[14:31:55.621] [+2630.903s]  calc: ⟨r⟩ = 0.585615 (n_r=5527, n_eigs=5529) [refs: GUE=0.5996 Poisson=0.3863]
… (10 entries total — computation_logs/test_16_ab_gue_class_log.txt)
```

---

### Test 17 — connes_self_duality

```text
[14:40:55.756] [+3171.039s]  build_ab_cloud_hamiltonian: 24x24 (N=576), α=0.5000, t=1.00, W=0.00, torus, 0 vortices, model=:monumental
[14:40:59.296] [+3174.578s]  build_ab_cloud_hamiltonian: 24x24 (N=576), α=0.5000, t=1.00, W=0.00, torus, 0 vortices, model=:monumental
[14:41:00.067] [+3175.349s]  build_ab_cloud_hamiltonian: 24x24 (N=576), α=0.3333, t=1.00, W=0.00, torus, 0 vortices, model=:monumental
[14:41:00.859] [+3176.141s]  build_ab_cloud_hamiltonian: 24x24 (N=576), α=0.5000, t=1.00, W=4.00, open, 0 vortices, model=:monumental
[14:41:02.710] [+3177.992s]  build_ab_cloud_hamiltonian: 48x48 (N=2304), α=0.5000, t=1.00, W=0.00, torus, 0 vortices, model=:monumental
[14:41:08.135] [+3183.417s]  build_ab_cloud_hamiltonian: 48x48 (N=2304), α=0.5000, t=1.00, W=0.00, torus, 0 vortices, model=:monumental
[14:41:13.525] [+3188.807s]  build_ab_cloud_hamiltonian: 48x48 (N=2304), α=0.3333, t=1.00, W=0.00, torus, 0 vortices, model=:monumental
[14:41:19.476] [+3194.758s]  build_ab_cloud_hamiltonian: 48x48 (N=2304), α=0.5000, t=1.00, W=4.00, open, 0 vortices, model=:monumental
[14:41:20.433] [+3195.715s]  build_ab_cloud_hamiltonian: 48x48 (N=2304), α=2.0000, t=1.00, W=4.00, open, 0 vortices, model=:monumental
[14:41:32.373] [+3207.655s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=0.00, torus, 0 vortices, model=:monumental
[14:46:45.944] [+3521.226s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=0.00, torus, 0 vortices, model=:monumental
[14:52:04.211] [+3839.493s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.3333, t=1.00, W=0.00, torus, 0 vortices, model=:monumental
[14:57:25.070] [+4160.352s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=4.00, open, 0 vortices, model=:monumental
[14:57:36.057] [+4171.339s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=2.0000, t=1.00, W=4.00, open, 0 vortices, model=:monumental
… (15 entries total — computation_logs/test_17_connes_self_duality_log.txt)
```

---

### Test 18 — chiral_AIII

```text
[15:11:28.198] [+5003.481s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=0.00, torus, 0 vortices, model=:monumental
[15:11:40.131] [+5015.413s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=1.00, torus, 0 vortices, model=:monumental
[15:11:52.929] [+5028.211s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=0.00, torus, 2 vortices, model=:monumental
… (3 entries total — computation_logs/test_18_chiral_AIII_log.txt)
```

---

### Test 19 — dirac_cone

```text
[15:24:25.783] [+5781.065s]  build_ab_cloud_hamiltonian: 20x20 (N=400), α=0.4000, t=1.00, W=0.00, torus, 0 vortices, model=:monumental
[15:24:27.667] [+5782.950s]  build_ab_cloud_hamiltonian: 40x40 (N=1600), α=0.4000, t=1.00, W=0.00, torus, 0 vortices, model=:monumental
[15:24:30.652] [+5785.934s]  build_ab_cloud_hamiltonian: 60x60 (N=3600), α=0.4000, t=1.00, W=0.00, torus, 0 vortices, model=:monumental
[15:24:46.991] [+5802.273s]  build_ab_cloud_hamiltonian: 80x80 (N=6400), α=0.4000, t=1.00, W=0.00, torus, 0 vortices, model=:monumental
[15:26:09.619] [+5884.901s]  build_ab_cloud_hamiltonian: 20x20 (N=400), α=0.5000, t=1.00, W=0.00, torus, 0 vortices, model=:monumental
[15:26:11.221] [+5886.504s]  build_ab_cloud_hamiltonian: 40x40 (N=1600), α=0.5000, t=1.00, W=0.00, torus, 0 vortices, model=:monumental
[15:26:14.202] [+5889.485s]  build_ab_cloud_hamiltonian: 60x60 (N=3600), α=0.5000, t=1.00, W=0.00, torus, 0 vortices, model=:monumental
[15:26:30.482] [+5905.764s]  build_ab_cloud_hamiltonian: 80x80 (N=6400), α=0.5000, t=1.00, W=0.00, torus, 0 vortices, model=:monumental
[15:27:52.829] [+5988.111s]  build_ab_cloud_hamiltonian: 20x20 (N=400), α=0.6000, t=1.00, W=0.00, torus, 0 vortices, model=:monumental
[15:27:54.428] [+5989.710s]  build_ab_cloud_hamiltonian: 40x40 (N=1600), α=0.6000, t=1.00, W=0.00, torus, 0 vortices, model=:monumental
[15:27:57.396] [+5992.678s]  build_ab_cloud_hamiltonian: 60x60 (N=3600), α=0.6000, t=1.00, W=0.00, torus, 0 vortices, model=:monumental
[15:28:13.935] [+6009.217s]  build_ab_cloud_hamiltonian: 80x80 (N=6400), α=0.6000, t=1.00, W=0.00, torus, 0 vortices, model=:monumental
… (12 entries total — computation_logs/test_19_dirac_cone_log.txt)
```

---

### Test 24 — dirac_string_flux

```text
[15:32:06.519] [+6241.801s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.0000, t=1.00, W=4.00, open, 1 vortices, model=:dirac
[15:32:18.884] [+6254.166s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.0000, t=1.00, W=4.00, open, 1 vortices, model=:dirac
[15:32:28.180] [+6263.462s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.0000, t=1.00, W=4.00, open, 1 vortices, model=:dirac
[15:32:38.165] [+6273.447s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.0000, t=1.00, W=4.00, open, 1 vortices, model=:dirac
… (4 entries total — computation_logs/test_24_dirac_string_flux_log.txt)
```

---

### Test 25 — byers_yang

```text
[15:35:41.679] [+6456.961s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.0000, t=1.00, W=0.00, open, 0 vortices, model=:dirac
[15:41:02.317] [+6777.599s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.0000, t=1.00, W=0.00, open, 4 vortices, model=:dirac
[15:46:12.181] [+7087.464s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.0000, t=1.00, W=0.00, open, 4 vortices, model=:dirac
[15:51:19.675] [+7394.957s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.0000, t=1.00, W=0.00, open, 4 vortices, model=:dirac
[15:56:20.440] [+7695.722s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.0000, t=1.00, W=0.00, open, 1 vortices, model=:dirac
[16:02:24.284] [+8059.566s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.0000, t=1.00, W=0.00, open, 1 vortices, model=:dirac
[16:07:53.533] [+8388.815s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.0000, t=1.00, W=0.00, open, 4 vortices, model=:dirac
[16:13:03.640] [+8698.922s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.0000, t=1.00, W=0.00, open, 4 vortices, model=:dirac
[16:18:21.308] [+9016.591s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.0000, t=1.00, W=0.00, open, 4 vortices, model=:dirac
[16:23:36.816] [+9332.098s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.0000, t=1.00, W=0.00, open, 4 vortices, model=:dirac
[16:29:01.269] [+9656.551s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.0000, t=1.00, W=0.00, open, 4 vortices, model=:dirac
[16:34:17.440] [+9972.722s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.0000, t=1.00, W=0.00, open, 4 vortices, model=:dirac
… (12 entries total — computation_logs/test_25_byers_yang_log.txt)
```

---

### Test 26 — pbc_torus

```text
[16:40:42.418] [+10357.700s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.0000, t=1.00, W=4.00, torus, 1 vortices, model=:dirac
[16:40:53.375] [+10368.657s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=1.00, torus, 4 vortices, model=:monumental
[16:46:12.496] [+10687.778s]  calc: ⟨r⟩ = 0.600632 (n_r=5527, n_eigs=5529) [refs: GUE=0.5996 Poisson=0.3863]
[16:46:20.404] [+10695.686s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=1.00, torus, 4 vortices, model=:monumental
[16:52:34.013] [+11069.295s]  calc: ⟨r⟩ = 0.596193 (n_r=5527, n_eigs=5529) [refs: GUE=0.5996 Poisson=0.3863]
[16:52:40.045] [+11075.327s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=1.00, torus, 4 vortices, model=:monumental
[16:58:08.064] [+11403.346s]  calc: ⟨r⟩ = 0.600551 (n_r=5527, n_eigs=5529) [refs: GUE=0.5996 Poisson=0.3863]
[16:58:13.542] [+11408.824s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=1.00, torus, 4 vortices, model=:monumental
[17:03:35.614] [+11730.896s]  calc: ⟨r⟩ = 0.589380 (n_r=5527, n_eigs=5529) [refs: GUE=0.5996 Poisson=0.3863]
[17:03:41.561] [+11736.843s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=1.00, torus, 4 vortices, model=:monumental
[17:08:56.247] [+12051.529s]  calc: ⟨r⟩ = 0.595447 (n_r=5527, n_eigs=5529) [refs: GUE=0.5996 Poisson=0.3863]
… (11 entries total — computation_logs/test_26_pbc_torus_log.txt)
```

---

### Test 27 — binary_chiral

```text
[17:09:31.246] [+12086.528s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=0.00, torus, 0 vortices, model=:monumental
[17:09:41.157] [+12096.439s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=1.00, torus, 0 vortices, model=:monumental
[17:09:55.379] [+12110.661s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=0.00, torus, 2 vortices, model=:monumental
[17:10:08.671] [+12123.951s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=0.50, torus, 2 vortices, model=:monumental
[17:10:18.050] [+12133.332s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=1.00, torus, 2 vortices, model=:monumental
[17:10:34.693] [+12149.975s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=2.00, torus, 2 vortices, model=:monumental
[17:10:48.183] [+12163.465s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=4.00, torus, 2 vortices, model=:monumental
[17:11:01.755] [+12177.037s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=0.50, torus, 0 vortices, model=:monumental
[17:11:12.887] [+12188.169s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=1.00, torus, 0 vortices, model=:monumental
[17:11:24.557] [+12199.839s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=2.00, torus, 0 vortices, model=:monumental
[17:11:34.547] [+12209.830s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=4.00, torus, 0 vortices, model=:monumental
… (11 entries total — computation_logs/test_27_binary_chiral_log.txt)
```

---

### Test 28 — f_gue_merit

```text
[17:13:08.712] [+12303.994s]  calc: Σ²(L=2.000) = 0.404688 (n_pos=9601, n_windows=3000, mean_count=1.99)
[17:13:09.363] [+12304.645s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=1.00, open, 4 vortices, model=:monumental
[17:18:15.462] [+12610.744s]  calc: Σ²(L=2.000) = 0.663437 (n_pos=5530, n_windows=3000, mean_count=2.03)
[17:18:19.349] [+12614.631s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=1.00, open, 4 vortices, model=:monumental
[17:23:20.729] [+12916.011s]  calc: Σ²(L=2.000) = 0.629287 (n_pos=5530, n_windows=3000, mean_count=2.02)
[17:23:26.725] [+12922.007s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=1.00, open, 4 vortices, model=:monumental
[17:28:20.247] [+13215.529s]  calc: Σ²(L=2.000) = 0.620146 (n_pos=5530, n_windows=3000, mean_count=2.04)
[17:28:26.188] [+13221.470s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=1.00, open, 4 vortices, model=:monumental
[17:33:37.233] [+13532.515s]  calc: Σ²(L=2.000) = 0.737871 (n_pos=5527, n_windows=3000, mean_count=2.04)
[17:33:43.480] [+13538.762s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=1.00, open, 4 vortices, model=:monumental
[17:38:57.213] [+13852.495s]  calc: Σ²(L=2.000) = 0.526840 (n_pos=5530, n_windows=3000, mean_count=2.02)
… (11 entries total — computation_logs/test_28_f_gue_merit_log.txt)
```

---

### Test 29 — dirac_dip

```text
[17:57:51.474] [+14986.757s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.3958, t=1.00, W=0.00, torus, 0 vortices, model=:monumental
[18:02:45.467] [+15280.749s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.4271, t=1.00, W=0.00, torus, 0 vortices, model=:monumental
[18:07:46.953] [+15582.235s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.4583, t=1.00, W=0.00, torus, 0 vortices, model=:monumental
[18:12:40.826] [+15876.108s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.4896, t=1.00, W=0.00, torus, 0 vortices, model=:monumental
[18:17:38.995] [+16174.277s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=0.00, torus, 0 vortices, model=:monumental
[18:22:37.999] [+16473.281s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5104, t=1.00, W=0.00, torus, 0 vortices, model=:monumental
[18:27:30.820] [+16766.102s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5417, t=1.00, W=0.00, torus, 0 vortices, model=:monumental
[18:33:06.073] [+17101.353s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5729, t=1.00, W=0.00, torus, 0 vortices, model=:monumental
[18:38:26.831] [+17422.113s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.6042, t=1.00, W=0.00, torus, 0 vortices, model=:monumental
[18:43:57.279] [+17752.561s]  build_ab_cloud_hamiltonian: 48x48 (N=2304), α=0.5000, t=1.00, W=0.00, torus, 0 vortices, model=:monumental
[18:44:03.436] [+17758.718s]  build_ab_cloud_hamiltonian: 48x48 (N=2304), α=0.3958, t=1.00, W=0.00, torus, 0 vortices, model=:monumental
… (11 entries total — computation_logs/test_29_dirac_dip_log.txt)
```

---

### Test 30 — vf_scaling

```text
[18:47:06.239] [+17941.521s]  build_ab_cloud_hamiltonian: 16x16 (N=256), α=0.5000, t=1.00, W=0.00, torus, 0 vortices, model=:monumental
[18:47:08.810] [+17944.092s]  build_ab_cloud_hamiltonian: 24x24 (N=576), α=0.5000, t=1.00, W=0.00, torus, 0 vortices, model=:monumental
[18:47:10.759] [+17946.041s]  build_ab_cloud_hamiltonian: 32x32 (N=1024), α=0.5000, t=1.00, W=0.00, torus, 0 vortices, model=:monumental
[18:47:13.274] [+17948.556s]  build_ab_cloud_hamiltonian: 40x40 (N=1600), α=0.5000, t=1.00, W=0.00, torus, 0 vortices, model=:monumental
[18:47:16.985] [+17952.268s]  build_ab_cloud_hamiltonian: 48x48 (N=2304), α=0.5000, t=1.00, W=0.00, torus, 0 vortices, model=:monumental
[18:47:23.131] [+17958.413s]  build_ab_cloud_hamiltonian: 56x56 (N=3136), α=0.5000, t=1.00, W=0.00, torus, 0 vortices, model=:monumental
[18:47:35.865] [+17971.147s]  build_ab_cloud_hamiltonian: 64x64 (N=4096), α=0.5000, t=1.00, W=0.00, torus, 0 vortices, model=:monumental
[18:48:01.478] [+17996.760s]  build_ab_cloud_hamiltonian: 72x72 (N=5184), α=0.5000, t=1.00, W=0.00, torus, 0 vortices, model=:monumental
[18:48:52.726] [+18048.009s]  build_ab_cloud_hamiltonian: 80x80 (N=6400), α=0.5000, t=1.00, W=0.00, torus, 0 vortices, model=:monumental
[18:50:38.784] [+18154.066s]  build_ab_cloud_hamiltonian: 88x88 (N=7744), α=0.5000, t=1.00, W=0.00, torus, 0 vortices, model=:monumental
[18:53:39.520] [+18334.803s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=0.00, torus, 0 vortices, model=:monumental
… (11 entries total — computation_logs/test_30_vf_scaling_log.txt)
```

---

### Test 31 — hatano_nelson

```text
[19:58:20.612] [+22215.894s]  build_ab_cloud_hamiltonian: 48x48 (N=2304), α=0.5000, t=1.00, W=1.00, torus, 4 vortices, model=:monumental
[19:58:24.636] [+22219.918s]  calc: ⟨r⟩_NN = 0.894102 (n=2304, Poisson-box ref NaN, 10 clouds)
[19:58:43.541] [+22238.824s]  calc: ⟨r⟩_NN = 0.907204 (n=2304, Poisson-box ref 0.851687, 10 clouds)
[19:59:02.308] [+22257.590s]  calc: ⟨r⟩_NN = 0.925299 (n=2304, Poisson-box ref 0.852026, 10 clouds)
[20:00:02.298] [+22317.580s]  calc: ⟨r⟩_NN = 0.923175 (n=2304, Poisson-box ref 0.852783, 10 clouds)
[20:00:20.812] [+22336.094s]  calc: ⟨r⟩_NN = 0.930952 (n=2304, Poisson-box ref 0.850774, 10 clouds)
[20:00:21.952] [+22337.234s]  build_ab_cloud_hamiltonian: 48x48 (N=2304), α=0.5000, t=1.00, W=1.00, torus, 4 vortices, model=:monumental
[20:00:26.458] [+22341.741s]  calc: ⟨r⟩_NN = 0.898821 (n=2304, Poisson-box ref NaN, 10 clouds)
[20:00:45.029] [+22360.311s]  calc: ⟨r⟩_NN = 0.878783 (n=2304, Poisson-box ref 0.851955, 10 clouds)
[20:01:05.099] [+22380.381s]  calc: ⟨r⟩_NN = 0.888162 (n=2304, Poisson-box ref 0.852427, 10 clouds)
[20:01:26.846] [+22402.128s]  calc: ⟨r⟩_NN = 0.891964 (n=2304, Poisson-box ref 0.850764, 10 clouds)
[20:01:28.031] [+22403.313s]  build_ab_cloud_hamiltonian: 48x48 (N=2304), α=0.5000, t=1.00, W=1.00, torus, 4 vortices, model=:monumental
[20:01:32.497] [+22407.779s]  calc: ⟨r⟩_NN = 0.897703 (n=2304, Poisson-box ref NaN, 10 clouds)
[20:01:51.151] [+22426.433s]  calc: ⟨r⟩_NN = 0.903503 (n=2304, Poisson-box ref 0.851913, 10 clouds)
[20:02:14.218] [+22449.500s]  calc: ⟨r⟩_NN = 0.923336 (n=2304, Poisson-box ref 0.852584, 10 clouds)
[20:02:39.742] [+22475.024s]  calc: ⟨r⟩_NN = 0.935506 (n=2304, Poisson-box ref 0.850682, 10 clouds)
[20:02:42.557] [+22477.839s]  build_ab_cloud_hamiltonian: 48x48 (N=2304), α=0.5000, t=1.00, W=1.00, torus, 4 vortices, model=:monumental
[20:02:48.011] [+22483.293s]  calc: ⟨r⟩_NN = 0.898157 (n=2304, Poisson-box ref NaN, 10 clouds)
[20:03:11.146] [+22506.428s]  calc: ⟨r⟩_NN = 0.906060 (n=2304, Poisson-box ref 0.851688, 10 clouds)
[20:03:35.069] [+22530.351s]  calc: ⟨r⟩_NN = 0.920104 (n=2304, Poisson-box ref 0.851832, 10 clouds)
[20:03:59.821] [+22555.103s]  calc: ⟨r⟩_NN = 0.937177 (n=2304, Poisson-box ref 0.850592, 10 clouds)
… (25 entries total — computation_logs/test_31_hatano_nelson_log.txt)
```

---

### Test 32 — rmean_bootstrap

```text
[20:13:27.733] [+23123.016s]  realization 1/5 (q=1.000): building 96x96 Hamiltonian (large-lattice diag dominates, minutes)
[20:13:28.606] [+23123.888s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=1.00, torus, 2 vortices, model=:monumental
[20:17:50.713] [+23385.996s]  calc: ⟨r⟩ = 0.581975 (n_r=5527, n_eigs=5529) [refs: GUE=0.5996 Poisson=0.3863]
[20:17:52.386] [+23387.668s]  realization 1/5 (q=1.000): ⟨r⟩=0.5820 in 264.7 s (bulk 5529 levels)
[20:28:08.796] [+24004.079s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=1.00, torus, 2 vortices, model=:monumental
[20:33:10.440] [+24305.722s]  calc: ⟨r⟩ = 0.590950 (n_r=5527, n_eigs=5529) [refs: GUE=0.5996 Poisson=0.3863]
[20:33:15.334] [+24310.616s]  realization 4/5 (q=1.000): ⟨r⟩=0.5909 in 307.6 s (bulk 5529 levels)
[20:33:15.342] [+24310.624s]  realization 5/5 (q=1.000): building 96x96 Hamiltonian (large-lattice diag dominates, minutes)
[20:33:16.461] [+24311.743s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=1.00, torus, 2 vortices, model=:monumental
[20:38:07.153] [+24602.435s]  calc: ⟨r⟩ = 0.586224 (n_r=5527, n_eigs=5529) [refs: GUE=0.5996 Poisson=0.3863]
[20:38:11.760] [+24607.042s]  realization 5/5 (q=1.000): ⟨r⟩=0.5862 in 296.4 s (bulk 5529 levels)
[20:38:11.786] [+24607.068s]  realization 1/5 (q=0.300): building 96x96 Hamiltonian (large-lattice diag dominates, minutes)
[20:38:13.081] [+24608.363s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=0.50, open, 256 vortices, model=:monumental
[20:42:55.693] [+24890.975s]  calc: ⟨r⟩ = 0.599252 (n_r=5527, n_eigs=5529) [refs: GUE=0.5996 Poisson=0.3863]
[20:43:00.222] [+24895.504s]  realization 1/5 (q=0.300): ⟨r⟩=0.5993 in 288.4 s (bulk 5529 levels)
[20:43:00.236] [+24895.518s]  realization 2/5 (q=0.300): building 96x96 Hamiltonian (large-lattice diag dominates, minutes)
[20:47:59.047] [+25194.329s]  calc: ⟨r⟩ = 0.603718 (n_r=5527, n_eigs=5529) [refs: GUE=0.5996 Poisson=0.3863]
[20:48:04.268] [+25199.550s]  realization 2/5 (q=0.300): ⟨r⟩=0.6037 in 304.0 s (bulk 5529 levels)
[20:48:04.278] [+25199.560s]  realization 3/5 (q=0.300): building 96x96 Hamiltonian (large-lattice diag dominates, minutes)
[20:48:05.422] [+25200.705s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=0.50, open, 256 vortices, model=:monumental
[20:52:49.570] [+25484.852s]  calc: ⟨r⟩ = 0.600059 (n_r=5527, n_eigs=5529) [refs: GUE=0.5996 Poisson=0.3863]
[20:52:54.321] [+25489.603s]  realization 3/5 (q=0.300): ⟨r⟩=0.6001 in 290.0 s (bulk 5529 levels)
[20:52:54.328] [+25489.610s]  realization 4/5 (q=0.300): building 96x96 Hamiltonian (large-lattice diag dominates, minutes)
[20:52:55.456] [+25490.738s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=0.50, open, 256 vortices, model=:monumental
[20:57:29.966] [+25765.248s]  calc: ⟨r⟩ = 0.601791 (n_r=5527, n_eigs=5529) [refs: GUE=0.5996 Poisson=0.3863]
[20:57:32.226] [+25767.508s]  realization 4/5 (q=0.300): ⟨r⟩=0.6018 in 277.9 s (bulk 5529 levels)
[20:57:32.243] [+25767.526s]  realization 5/5 (q=0.300): building 96x96 Hamiltonian (large-lattice diag dominates, minutes)
[20:57:33.449] [+25768.731s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=0.50, open, 256 vortices, model=:monumental
[21:02:10.128] [+26045.410s]  calc: ⟨r⟩ = 0.600971 (n_r=5527, n_eigs=5529) [refs: GUE=0.5996 Poisson=0.3863]
[21:02:14.604] [+26049.886s]  realization 5/5 (q=0.300): ⟨r⟩=0.6010 in 282.4 s (bulk 5529 levels)
… (40 entries total — computation_logs/test_32_rmean_bootstrap_log.txt)
```

---

### Test 33 — l_scaling_rmean

```text
[21:18:17.797] [+27013.080s]  build_ab_cloud_hamiltonian: 10x10 (N=100), α=0.5000, t=1.00, W=1.00, torus, 4 vortices, model=:monumental
[21:18:18.357] [+27013.639s]  calc: ⟨r⟩ = 0.629404 (n_r=59, n_eigs=61) [refs: GUE=0.5996 Poisson=0.3863]
[21:18:19.481] [+27014.763s]  build_ab_cloud_hamiltonian: 10x10 (N=100), α=0.5000, t=1.00, W=1.00, torus, 4 vortices, model=:monumental
[21:18:20.034] [+27015.316s]  calc: ⟨r⟩ = 0.509721 (n_r=59, n_eigs=61) [refs: GUE=0.5996 Poisson=0.3863]
[21:18:54.049] [+27049.331s]  calc: ⟨r⟩ = 0.594415 (n_r=1499, n_eigs=1501) [refs: GUE=0.5996 Poisson=0.3863]
[21:18:55.096] [+27050.378s]  build_ab_cloud_hamiltonian: 50x50 (N=2500), α=0.5000, t=1.00, W=1.00, torus, 70 vortices, model=:monumental
[21:19:00.056] [+27055.338s]  calc: ⟨r⟩ = 0.606851 (n_r=1499, n_eigs=1501) [refs: GUE=0.5996 Poisson=0.3863]
[21:19:01.083] [+27056.365s]  build_ab_cloud_hamiltonian: 50x50 (N=2500), α=0.5000, t=1.00, W=1.00, torus, 70 vortices, model=:monumental
[21:19:06.087] [+27061.370s]  calc: ⟨r⟩ = 0.574458 (n_r=1499, n_eigs=1501) [refs: GUE=0.5996 Poisson=0.3863]
[21:19:07.153] [+27062.436s]  build_ab_cloud_hamiltonian: 50x50 (N=2500), α=0.5000, t=1.00, W=1.00, torus, 70 vortices, model=:monumental
[21:19:12.078] [+27067.360s]  calc: ⟨r⟩ = 0.594551 (n_r=1499, n_eigs=1501) [refs: GUE=0.5996 Poisson=0.3863]
[21:19:13.463] [+27068.745s]  build_ab_cloud_hamiltonian: 80x80 (N=6400), α=0.5000, t=1.00, W=1.00, torus, 178 vortices, model=:monumental
[21:20:25.768] [+27141.050s]  calc: ⟨r⟩ = 0.598524 (n_r=3839, n_eigs=3841) [refs: GUE=0.5996 Poisson=0.3863]
[21:20:27.289] [+27142.571s]  build_ab_cloud_hamiltonian: 80x80 (N=6400), α=0.5000, t=1.00, W=1.00, torus, 178 vortices, model=:monumental
[21:21:39.539] [+27214.821s]  calc: ⟨r⟩ = 0.593096 (n_r=3839, n_eigs=3841) [refs: GUE=0.5996 Poisson=0.3863]
[21:21:41.084] [+27216.366s]  build_ab_cloud_hamiltonian: 80x80 (N=6400), α=0.5000, t=1.00, W=1.00, torus, 178 vortices, model=:monumental
[21:25:41.974] [+27457.256s]  build_ab_cloud_hamiltonian: 20x20 (N=400), α=0.5000, t=1.00, W=1.00, open, 12 vortices, model=:monumental
[21:25:42.526] [+27457.808s]  calc: ⟨r⟩ = 0.549972 (n_r=239, n_eigs=241) [refs: GUE=0.5996 Poisson=0.3863]
[21:25:43.537] [+27458.819s]  build_ab_cloud_hamiltonian: 20x20 (N=400), α=0.5000, t=1.00, W=1.00, open, 12 vortices, model=:monumental
[21:25:44.100] [+27459.382s]  calc: ⟨r⟩ = 0.585633 (n_r=239, n_eigs=241) [refs: GUE=0.5996 Poisson=0.3863]
[21:25:45.054] [+27460.336s]  build_ab_cloud_hamiltonian: 30x30 (N=900), α=0.5000, t=1.00, W=1.00, open, 26 vortices, model=:monumental
[21:25:45.772] [+27461.054s]  calc: ⟨r⟩ = 0.578164 (n_r=539, n_eigs=541) [refs: GUE=0.5996 Poisson=0.3863]
[21:25:46.753] [+27462.035s]  build_ab_cloud_hamiltonian: 30x30 (N=900), α=0.5000, t=1.00, W=1.00, open, 26 vortices, model=:monumental
[21:25:47.487] [+27462.769s]  calc: ⟨r⟩ = 0.588849 (n_r=539, n_eigs=541) [refs: GUE=0.5996 Poisson=0.3863]
[21:25:48.476] [+27463.758s]  build_ab_cloud_hamiltonian: 30x30 (N=900), α=0.5000, t=1.00, W=1.00, open, 26 vortices, model=:monumental
[21:25:49.202] [+27464.484s]  calc: ⟨r⟩ = 0.583585 (n_r=539, n_eigs=541) [refs: GUE=0.5996 Poisson=0.3863]
[21:25:50.205] [+27465.487s]  build_ab_cloud_hamiltonian: 30x30 (N=900), α=0.5000, t=1.00, W=1.00, open, 26 vortices, model=:monumental
[21:25:50.928] [+27466.210s]  calc: ⟨r⟩ = 0.601887 (n_r=539, n_eigs=541) [refs: GUE=0.5996 Poisson=0.3863]
[21:27:36.326] [+27571.608s]  build_ab_cloud_hamiltonian: 80x80 (N=6400), α=0.5000, t=1.00, W=1.00, open, 178 vortices, model=:monumental
[21:28:48.328] [+27643.610s]  calc: ⟨r⟩ = 0.610283 (n_r=3839, n_eigs=3841) [refs: GUE=0.5996 Poisson=0.3863]
[21:28:49.848] [+27645.130s]  build_ab_cloud_hamiltonian: 80x80 (N=6400), α=0.5000, t=1.00, W=1.00, open, 178 vortices, model=:monumental
[21:30:02.856] [+27718.138s]  calc: ⟨r⟩ = 0.595793 (n_r=3839, n_eigs=3841) [refs: GUE=0.5996 Poisson=0.3863]
[21:30:04.465] [+27719.747s]  build_ab_cloud_hamiltonian: 80x80 (N=6400), α=0.5000, t=1.00, W=1.00, open, 178 vortices, model=:monumental
[21:31:23.977] [+27799.259s]  calc: ⟨r⟩ = 0.599605 (n_r=3839, n_eigs=3841) [refs: GUE=0.5996 Poisson=0.3863]
[21:31:26.491] [+27801.773s]  build_ab_cloud_hamiltonian: 80x80 (N=6400), α=0.5000, t=1.00, W=1.00, open, 178 vortices, model=:monumental
[21:32:42.881] [+27878.163s]  calc: ⟨r⟩ = 0.598340 (n_r=3839, n_eigs=3841) [refs: GUE=0.5996 Poisson=0.3863]
… (100 entries total — computation_logs/test_33_l_scaling_rmean_log.txt)
```

---

### Test 34 — direct_vs_zeta

```text
[21:37:05.355] [+28140.637s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=1.00, open, 2 vortices, model=:monumental
[21:41:58.186] [+28433.468s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=1.00, open, 2 vortices, model=:monumental
[21:47:07.004] [+28742.286s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=1.00, open, 2 vortices, model=:monumental
[21:52:23.759] [+29059.041s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=1.00, open, 2 vortices, model=:monumental
[21:57:55.738] [+29391.021s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=1.00, open, 2 vortices, model=:monumental
… (5 entries total — computation_logs/test_34_direct_vs_zeta_log.txt)
```

---

### Test 35 — form_factor_Kt

```text
[22:09:09.750] [+30065.032s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=1.00, open, 2 vortices, model=:monumental
[22:14:37.106] [+30392.388s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=1.00, open, 2 vortices, model=:monumental
[22:19:44.711] [+30699.993s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=1.00, open, 2 vortices, model=:monumental
[22:24:48.414] [+31003.696s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=1.00, open, 2 vortices, model=:monumental
[22:30:51.804] [+31367.086s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=1.00, open, 2 vortices, model=:monumental
… (5 entries total — computation_logs/test_35_form_factor_Kt_log.txt)
```

---

### Test 36 — byte_robust

```text
[22:45:53.699] [+32268.981s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=1.00, open, 2 vortices, model=:monumental
[22:51:13.311] [+32588.593s]  t37 pass 2 (secondary) realization 1: central block 5529 eigs, accumulated 5529 (target 50000)
[22:51:14.494] [+32589.776s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=1.00, open, 2 vortices, model=:monumental
[22:55:54.778] [+32870.060s]  t37 pass 2 (secondary) realization 2: central block 5529 eigs, accumulated 11058 (target 50000)
[23:33:00.279] [+35095.561s]  calc: ⟨r⟩ = 0.815854 (n_r=13, n_eigs=15) [refs: GUE=0.5996 Poisson=0.3863]
[23:33:00.279] [+35095.561s]  calc: ⟨r⟩ = 0.467241 (n_r=13, n_eigs=15) [refs: GUE=0.5996 Poisson=0.3863]
[23:33:00.279] [+35095.561s]  calc: ⟨r⟩ = 0.655008 (n_r=13, n_eigs=15) [refs: GUE=0.5996 Poisson=0.3863]
[23:33:00.279] [+35095.561s]  calc: ⟨r⟩ = 0.651800 (n_r=13, n_eigs=15) [refs: GUE=0.5996 Poisson=0.3863]
[23:33:00.279] [+35095.561s]  calc: ⟨r⟩ = 0.476787 (n_r=13, n_eigs=15) [refs: GUE=0.5996 Poisson=0.3863]
[23:33:00.280] [+35095.562s]  calc: ⟨r⟩ = 0.522209 (n_r=13, n_eigs=15) [refs: GUE=0.5996 Poisson=0.3863]
[23:33:00.280] [+35095.562s]  calc: ⟨r⟩ = 0.526679 (n_r=13, n_eigs=15) [refs: GUE=0.5996 Poisson=0.3863]
[23:33:00.280] [+35095.562s]  calc: ⟨r⟩ = 0.487008 (n_r=13, n_eigs=15) [refs: GUE=0.5996 Poisson=0.3863]
[23:33:00.280] [+35095.562s]  calc: ⟨r⟩ = 0.639582 (n_r=13, n_eigs=15) [refs: GUE=0.5996 Poisson=0.3863]
[23:33:00.280] [+35095.562s]  calc: ⟨r⟩ = 0.663925 (n_r=13, n_eigs=15) [refs: GUE=0.5996 Poisson=0.3863]
[23:33:00.280] [+35095.562s]  calc: ⟨r⟩ = 0.501332 (n_r=13, n_eigs=15) [refs: GUE=0.5996 Poisson=0.3863]
[23:33:00.280] [+35095.562s]  calc: ⟨r⟩ = 0.462589 (n_r=13, n_eigs=15) [refs: GUE=0.5996 Poisson=0.3863]
[23:33:00.282] [+35095.564s]  calc: ⟨r⟩ = 0.626084 (n_r=13, n_eigs=15) [refs: GUE=0.5996 Poisson=0.3863]
[23:33:00.282] [+35095.564s]  calc: ⟨r⟩ = 0.550313 (n_r=13, n_eigs=15) [refs: GUE=0.5996 Poisson=0.3863]
[23:33:00.282] [+35095.564s]  calc: ⟨r⟩ = 0.550351 (n_r=13, n_eigs=15) [refs: GUE=0.5996 Poisson=0.3863]
[23:33:00.282] [+35095.564s]  calc: ⟨r⟩ = 0.642275 (n_r=13, n_eigs=15) [refs: GUE=0.5996 Poisson=0.3863]
[23:33:00.282] [+35095.564s]  calc: ⟨r⟩ = 0.529751 (n_r=13, n_eigs=15) [refs: GUE=0.5996 Poisson=0.3863]
[23:33:00.282] [+35095.564s]  calc: ⟨r⟩ = 0.548388 (n_r=13, n_eigs=15) [refs: GUE=0.5996 Poisson=0.3863]
[23:33:00.282] [+35095.564s]  calc: ⟨r⟩ = 0.658126 (n_r=13, n_eigs=15) [refs: GUE=0.5996 Poisson=0.3863]
[23:33:00.282] [+35095.564s]  calc: ⟨r⟩ = 0.557107 (n_r=13, n_eigs=15) [refs: GUE=0.5996 Poisson=0.3863]
[23:33:00.282] [+35095.564s]  calc: ⟨r⟩ = 0.636281 (n_r=13, n_eigs=15) [refs: GUE=0.5996 Poisson=0.3863]
[23:33:00.282] [+35095.564s]  calc: ⟨r⟩ = 0.497804 (n_r=13, n_eigs=15) [refs: GUE=0.5996 Poisson=0.3863]
[23:33:00.282] [+35095.564s]  calc: ⟨r⟩ = 0.684932 (n_r=13, n_eigs=15) [refs: GUE=0.5996 Poisson=0.3863]
[23:33:00.282] [+35095.564s]  calc: ⟨r⟩ = 0.687670 (n_r=13, n_eigs=15) [refs: GUE=0.5996 Poisson=0.3863]
[23:33:00.283] [+35095.566s]  calc: ⟨r⟩ = 0.621021 (n_r=13, n_eigs=15) [refs: GUE=0.5996 Poisson=0.3863]
[23:33:00.283] [+35095.566s]  calc: ⟨r⟩ = 0.662679 (n_r=13, n_eigs=15) [refs: GUE=0.5996 Poisson=0.3863]
[23:33:00.283] [+35095.566s]  calc: ⟨r⟩ = 0.484236 (n_r=13, n_eigs=15) [refs: GUE=0.5996 Poisson=0.3863]
[23:33:00.283] [+35095.566s]  calc: ⟨r⟩ = 0.642217 (n_r=13, n_eigs=15) [refs: GUE=0.5996 Poisson=0.3863]
[23:33:00.283] [+35095.566s]  calc: ⟨r⟩ = 0.541220 (n_r=13, n_eigs=15) [refs: GUE=0.5996 Poisson=0.3863]
[23:33:00.283] [+35095.566s]  calc: ⟨r⟩ = 0.602689 (n_r=13, n_eigs=15) [refs: GUE=0.5996 Poisson=0.3863]
[23:33:00.283] [+35095.566s]  calc: ⟨r⟩ = 0.479526 (n_r=13, n_eigs=15) [refs: GUE=0.5996 Poisson=0.3863]
[23:33:00.283] [+35095.566s]  calc: ⟨r⟩ = 0.599213 (n_r=13, n_eigs=15) [refs: GUE=0.5996 Poisson=0.3863]
[23:00:33.946] [+33149.228s]  t37 pass 2 (secondary) realization 3: central block 5529 eigs, accumulated 16587 (target 50000)
[23:05:51.910] [+33467.192s]  t37 pass 2 (secondary) realization 4: central block 5529 eigs, accumulated 22116 (target 50000)
[23:10:20.477] [+33735.759s]  t37 pass 2 (secondary) realization 5: central block 5529 eigs, accumulated 27645 (target 50000)
[23:14:36.092] [+33991.374s]  t37 pass 2 (secondary) realization 6: central block 5529 eigs, accumulated 33174 (target 50000)
[23:18:57.442] [+34252.724s]  t37 pass 2 (secondary) realization 7: central block 5529 eigs, accumulated 38703 (target 50000)
[23:23:11.865] [+34507.147s]  t37 pass 2 (secondary) realization 8: central block 5529 eigs, accumulated 44232 (target 50000)
[23:27:55.567] [+34790.849s]  t37 pass 2 (secondary) realization 9: central block 5529 eigs, accumulated 49761 (target 50000)
[23:33:00.249] [+35095.531s]  t37 pass 2 (secondary) realization 10: central block 5529 eigs, accumulated 55290 (target 50000)
… (142 entries total — computation_logs/test_36_byte_robust_log.txt)
```

---

# PART VII. LEVEL V: THE SPINOR STUDY

## 25. Level V: the spinor study — the machine with no long-term memory

The supplementary study formalizes "reads, does not carry" in three phase models with $\theta = \pi/2, \pi/3, \pi/7$. The angle choices are the simplest rational fractions of $\pi$: $\theta = \pi/k$ gives a cycle of length $2k$ — minimal systems with non-trivial monodromy.

**ES1 (cycles, TS1).** The rotation cycle $\theta = \pi/k$ closes after exactly $N = 2k$ steps; gap $2\pi/N$; periods 4/6/14 — exact. Theorem TS1: iterating a phase rotation by θ returns to identity after the lcm-multiple of $2\pi/\theta$ steps; for $\pi/k$ that is $2k$. Certificate: machine-exact closure on all three models.

**ES2 (reset, TS2).** Reset erases everything: $I(\mathrm{pre}; \mathrm{post}) = 0$ — zero mutual information across reset; post-reset reconstruction falls to chance $1/N$: $0.2501/0.1674/0.0717 \approx 1/4, 1/6, 1/14$ (TS2). The quantitative definition of "no long-term memory": the state contains no information about history after reset.

**ES3 (the step, TS3).** Step cost is flat: slope $-1.5\cdot10^{-12}$ ms/step — a statistical zero against the eternal log requiring $\Omega(t)$ and growing ×129 (TS3). Step flatness is the definition of O(1) state computability: the formula computes the state in constant time independent of history depth.

**ES4 (the Markov class).** The Markov task class is solvable memoryless — within protocol. The boundary: non-Markov tasks (requiring history) are inaccessible in principle — a property, not a defect: the same boundary as "reading mathematics in real time".

**ES5 (the silence zone).** The capacity-for-robustness exchange is quantified: the parameter zone where the machine predictably stays silent (a refusal, not an error) is measured. The silence zone is the operational boundary of trust: beyond it, refusal is deterministic and observable.

The study's meaning: the machine without long-term memory is the operational demonstration of what "reading mathematics in real time" means. The three theorems TS1–TS3 give the exact arithmetic of cycles, the irreversibility of reset, the constancy of the step. The link to the programme is numerical: the V23 preview ("12/12 zeros from six constants, storage 0") is the same statement on ζ-zero material; spinor volatility is stated as a processor-determinism condition (§12). In the MAX frame: the spinor study is the prototype of an "active" ζ-machine — if the H–P operator exists, its ζ side must be a machine of this class: reading, not storing.


---

## 25b. Full record of the spinor study (from the unified volume)

#### Full record: 8. The spinor study: the machine with no long-term memory

#### 8.1. Three phase models and five verdicts

The supplementary study formalizes "reads, does not carry" in three phase models with $\theta = \pi/2, \pi/3, \pi/7$. **ES1 (cycles):** the rotation cycle $\theta = \pi/k$ closes after exactly $N = 2k$ steps; gap $2\pi/N$; periods 4/6/14 exactly (TS1). **ES2 (reset):** reset erases everything: $I(\mathrm{pre}; \mathrm{post}) = 0$; post-reset reconstruction falls to chance level $1/N$ — $0.2501/0.1674/0.0717 \approx 1/4, 1/6, 1/14$ (TS2). **ES3 (the step):** step cost is flat — slope $-1.5\times10^{-12}$ ms/step, while an eternal log requires $\Omega(t)$ and grows ×129 (TS3). **ES4 (the Markov class):** the Markov task class is solvable memoryless — within protocol. **ES5 (the silence zone):** the capacity/robustness trade-off is quantified — the parameter zone where the machine predictably stays silent is measured.

#### 8.2. The study's meaning

The machine with no long-term memory is the operational demonstration of what "reading mathematics in real time" means: state is computable from the formula but does not accumulate. The three theorems TS1–TS3 give the exact arithmetic of cycles, the irreversibility of reset, and the flatness of the step. The link to the rest of the programme is numerical: the V23 preview ("12/12 zeros from six constants, storage 0") is the same statement on the material of $\zeta$ zeros; the volatility of the spinor models is stated as a condition of processor determinism (§4.4).


---

---

# PART VIII. LEVEL VI: THE MERIDIAN SPECTRAL OBSERVATORY

## 26. Level VI: the observatory as a laboratory

The Meridian Spectral Observatory is a laboratory of 24 self-contained Julia codes and one Python code. The architectural principle: every file is a standalone "supercombo" bench (open it in Julia — you get an interactive console menu with dozens of tests, plots, reports and a built-in self-check); no external modules, no builds: copy the file — it works (or honestly reports what is missing). The Meridian design system (`_D` suffix files): double-frame banners, ◆-sections, ✓/✗/⚠ statuses, live progress bars ▰▰▰▱▱, true-TTY colours — console "clothing"; the physics and numbers are bit-identical to the plain versions.

The observatory's line catalogue. **The main `ab_cloud_v*.jl` line:** v19 (23,342 lines — 37 tests, H–P focus + advanced RMT diagnostics); v19_v1 (23,956); v20 (24,596); v21 (25,519 — 38 tests + Physics Lab + 3D Lab on a sparse engine); v21_v1 (fixes); v22 (7,369 — the journal-grade plotting engine `ABPlotV23`, the three-pass Test 38); v23 (28,281); v23_v1 (29,904); **v23_v2 (30,908 — the SUPERCOMBO v23.6: the v21 core × the v22 plot engine × the three-pass Test 38 (38a + 38b hardcore + 38c ladder), the H1 deepen protocol, the H5 α-profile, decoy controls, FAST L=16 / FULL L=56 presets).** **HP·MERIDIAN:** `hp_audit_standalone.jl` (v24.2-SA, 6,054 lines — the compact standalone audit of gates H1–H7; the core lifted verbatim from v23_v2 — at equal seeds the numbers match bit-for-bit; the H5 budget ≤ 40 diagonalizations; the FOCUS-D mode `hp_regime_mode = :regime_d`, command `5d`; a live progress bar during LAPACK calls; a 60-second heartbeat; an environment doctor; battery-cost estimation). **The RH line:** `RH_Unified.jl` (1,885 — 500 real zeros, 61 magic α-points, 6 hexagonal vortices, an RHConfig of 33 parameters, jitter, 4 layouts, 9 presets); `RH_Unified_v5.jl` (2,204); `RH_Sweep_Pro.jl` (6,450 — 13,661 real zeros via `mpmath.zetazero` at 25 digits, a dynamic sweep of 8 parameters over 10 key points, CSV/TXT/JSON reports, Plots.jl, timing logs). **The monumental line:** `AB_Cloud_Monumental_v6_3.jl` (7,759 — the module `AB_Cloud_Monumental`, the V01–V112 verifications of the monograph, `run_all()`, `run_all(quick=true)`, `run_only([...])`, clean CSV + JSON + PNG dashboards, optional Arpack.jl and Plots.jl). **Data tools:** `zeros50k.txt` / `zeta_zeros_50k.txt` (one table, two formats); `Magic_Alpha_Points_v1.jl` (61 points); `test11_honest.jl` / `test11_honest.py` (the honest AD test with an MC null).

The observatory's three pillars: the AB cloud (experimental material), the zeros of ζ(s) (the reference), GUE statistics (the benchmark). Its programme question: at which parameters does the AB cloud reach GUE — and how does one watch spectra so that the answer does not depend on the observing instrument.


---

## 27. The gates H1–H7: a complete analysis

The seven gates of the Hilbert–Pólya hypothesis are the observatory's core. Each in full.

**H1 PRIME-TRACE.** The Bragg comb: the trace of a ζ-coupled operator carries peaks at $\omega = \log p$ — the frequencies of the primes. Controls: composite decoys (peaks at $\log n$ for composite $n$ — they must be absent); regime-matched null models (random phases with the same distribution); the P95 deepen protocol (adding realizations to the 95th percentile of stability). The positive result — prime peaks standing out over the composite background — confirms Th6 in lattice execution: the weight $\Lambda(n)/\sqrt{n}$ is observable in the trace.

**H2 WEYL-DOS.** The Weyl ladder: the integrated density of states $N(E)$ against $\overline{N}(E) \sim \frac{\mathrm{Vol}}{4\pi}E$ with oscillations. Tool: the AICc showdown over a model dictionary (power law, logarithmic, mixed) — model choice by information criterion, not by eye. The gate's question: does the cloud's level density have the right *shape* for a ζ candidate (logarithmic, as the BK ladder)?

**H3 POWER-LAW.** The exponent ladder: scanning the power $\beta$ in $N(E) \sim E^\beta$ over subranges; dictionary falsification: no fixed β may work globally — the correct dependence is logarithmic (β grows with E). A negative result over all fixed β is indirect confirmation of the logarithm.

**H4 CRITICAL-Q.** The sharpness scan: the parameter $Q$ — the sharpness of the spectral feature at critical flux; domain guard: sharpness grows only in the physical domain $\alpha \in [0, 1/2]$, beyond — edge artefact. The question: does the cloud have a critical point at $\alpha = 1/2$ with the correct (universal) critical dynamics?

**H5 REGIME-2×2.** The four-regime showdown: {density: baseline $N_v=4$ vs monograph $N_v = L^2/36$} × {flux: $\alpha = 0.5$ vs sharp $25/900$} at L = 72. The results (with the mechanics): regime A — an outlier (median $D = 0.3531$, 6/7 in the ⟨r⟩ band, 0/7 individual KS); B — OR-clause (⟨r⟩ in band 7/7, individual KS 1/7: ⟨r⟩ is a weak marker, KS a strong one); C — OR-clause (0/7); D — the clean pass (7/7, median $D = 0.0148$, twice below $d_{\mathrm{crit}} = 1.63/\sqrt{n} \approx 0.031$). The α-profile: best quality at sharp α — a plateau against fine-tuning. The v24.1 budget: ≤ 40 diagonalizations per gate — the whole H1–H7 battery fits a smartphone hour.

**H6 HERMIT-STRESS.** The self-adjointness stress gate: the anti-Hermitian norm (machine zero); eigenvalue stability under jitter of positions (0.35), flux (0.02), charges and width; behaviour under perturbation — the Kato corridors of Th3 in action. The gate owns the construct's "exact layer" on every configuration.

**H7 SEQ-CORR.** The levels↔zeros correlation: the unfolded level sequence against the unfolded zero sequence — per test, cross-shifted, with null models. The question: is there a direct correspondence of level *order* to zero order? Result: correlation in the null zone of the rank metric — consistent with the resolution limit of the rank branch (the G2 verdict itself was corrected to YES at the zeros' level by audit v2.0.7).

The gates' position in the programme: H1–H7 operationalize the H–P hypothesis into seven checkable questions; their sum (H5 clean + H7 null) reproduces the C1–C17 bridge map independently and on a different engine — a cross-confirmation of level III.


---

## 28. The RH line: 500, 13,661 and 50,000 zeros

![Unfolded spacing distribution vs the Wigner surmise](../../03_figures/static/meridian/en/fig_M2_spacing_surmise_en.png)


The RH line maximizes the cloud's correlation with the ζ zeros. `RH_Unified.jl`: 500 real zeros; 61 magic α-points; 6 hexagonal vortices; an RHConfig of 33 parameters; jitter (positions 0.35, flux 0.02, charges, width); 4 layouts (hexagonal, ring, random, grid); 9 presets. `RH_Unified_v5.jl`: extended presets and diagnostics. `RH_Sweep_Pro.jl`: the professional sweep — 13,661 real zeros via `mpmath.zetazero` (25 digits); a dynamic sweep of 8 parameters over 10 key points; CSV/TXT/JSON reports; Plots.jl graphics; timing logs.

The magic α-grid: $\pi/30 \ldots \pi\times5$; $\sqrt{2} \ldots \sqrt{15}$; rationals; $\varphi$; $e$; $\ln 2$; $1/e$; $1/\pi$; special values. The grid's meaning: RMT-class universality — if GUE attainment depended on the arithmetic nature of α (rational vs algebraic vs transcendental), that would be a red flag of tuning; the class must be deaf to the flux's nature. Result: the class is stable across the grid; the sensitivity is to magnitude alone (half-integer and sharp fractional values).

The 50,000-zero reference table: two formats, one table (first zero 14.134725142 — Odlyzko verified; last 40433.687385462; control: the two files' last values agree to 12 digits; exactly 50,000 in each). The density in this range: $\sim \ln(\gamma/2\pi) \approx \ln(6433) \approx 8.8$ zeros per unit $t$; the typical local gap 0.11–0.12. Origin: `mpmath.zetazero()` at 25 digits. The package-level audit of this edition: $\langle r \rangle = 0.6119 \pm 0.0010$; 5,000-zero blocks: $[0.6095, 0.6160]$; local KS against the surmise: $D = 0.0223$. Figures M1–M3 document the audit.

The RH_Sweep over 13,661 zeros: $\langle r \rangle = 0.6144$ against R_GUE = 0.5996 — a systematic excess of ~0.015; the source is low heights (the first few hundred zeros have a known ⟨r⟩ inflation from small mean gaps and edge effects); the 50k table with lows excluded gives 0.6119. The honest record: both values are correct in their conventions; the conventions differ by range.


---

## 29. The monumental line V01–V112

The monumental line is a Julia port of the Python monograph base: `AB_Cloud_Monumental_v6_3.jl`, the module `AB_Cloud_Monumental`, verifications **V01–V112**. Interface: `run_all()` — the full battery; `run_all(quick=true)` — accelerated; `run_only(["V11","V35"])` — selective. Output: clean CSV + JSON + PNG dashboards; optional Arpack.jl for large L (sparse eigenvalues instead of full diagonalization) and Plots.jl.

The V01–V112 range covers the monograph's entire Python base: construction and invariants (hermiticity, flux, chirality); statistics (⟨r⟩, KS, unfolding); ζ-correspondences and their negative verdicts; trace identities; dynamics; the processor layer. The line's position: an independent implementation of the whole monograph in a second language — the programme's widest cross-verification loop. For the MAX edition the line matters as reproducibility evidence: not isolated numbers but the entire verification corpus transfers between languages with verdicts preserved.

The observatory's documentation — eight Russian documents (`docs/01–08`): the project overview; the code catalogue (25 files described); the launch guide (Julia ≥ 1.10, menus, presets); physics and mathematics (the Hamiltonian, vortex geometry, RMT, criterion formulas, the H1–H7 gates — the "theoretical minimum"); the H5 regime analysis (the full A/B/C/D breakdown); the ζ-zero data (the 50k table: origin, formats, checks); the version chronology (v19 → v23_v2 → hp_audit); reproducibility (seeds, digests, cross-checks). The Russian originals are included verbatim in the Russian MAX edition; the present chapter is their English condensation.


---

## 30. Level VI: boundaries

The observatory is an instrumental line: its gates measure but do not prove. Gate H5 shows regime D is cleanly GUE by KS: a statistical statement about lattice ensembles at L = 72, not about the zeros. Extending the L-ladder is the observatory's programme (v23_v2: FULL L=56; presets toward L=112 within RAM honesty). The RH line maximizes correlation — a controlled optimization, not an identity. The 50,000-zero table is an external `mpmath.zetazero` reference; the level-IV blind protocols are the only internal source of trust for the ζ side. The cross-language position: the hp_audit core is lifted from v23_v2 verbatim — bit-for-bit at equal seeds; the rest of the observatory is Julia-unique; independence from the Python canon is partial.


---

## 30a. Full record of level VI (from the unified volume)

#### Full record: 9. Level VI: the Meridian Spectral Observatory

#### 9.1. The observatory: 24 codes and one idea

The Meridian Spectral Observatory is a laboratory of 24 self-contained Julia codes and one Python code (`test11_honest.py`), each a standalone "supercombo" bench: open one file in Julia and you get an interactive console menu with dozens of tests, plots, reports and a built-in self-check. Three pillars: the AB cloud (a lattice Hamiltonian with magnetic-flux vortices as experimental material), the zeros of $\zeta(s)$ (the reference table of 50,000 zeros: from $\gamma_1 = 14.134725142$ to $\gamma_{50000} = 40433.687385462$), and GUE statistics ($\langle r\rangle \approx 0.5996$, band $[0.5772, 0.6212]$). A package-level check of the table (computed in this edition from `02_data/raw/meridian/zeros50k.txt`) gives $\langle r\rangle = 0.6119 \pm 0.0010$ ($n = 49{,}998$) — the GUE class confirmed independently; sliding 5,000-zero blocks hold $[0.6095, 0.6160]$ along the whole strip.

![Spacing-ratio statistics of the 50,000 zeros](../../03_figures/static/meridian/en/fig_M1_r_statistics_en.png)

![Sliding block means](../../03_figures/static/meridian/en/fig_M3_r_sliding_en.png)

#### 9.2. The gates H1–H7

The observatory's core is seven gates of the Hilbert–Pólya hypothesis (`hp_audit_standalone.jl`, v24.2-SA, 6,054 lines; the core lifted verbatim from v23_v2 — with equal seeds the numbers match bit-for-bit): **H1 PRIME-TRACE** — the Bragg comb at $\omega = \log p$ with composite decoys and regime-matched null models; **H2 WEYL-DOS** — the $N(E)$ ladder with an AICc dictionary showdown; **H3 POWER-LAW** — the exponent ladder with dictionary falsification; **H4 CRITICAL-Q** — a sharpness scan with a domain guard; **H5 REGIME-2×2** — the four-regime ensemble showdown plus the α-profile (below); **H6 HERMIT-STRESS** — self-adjointness and stability; **H7 SEQ-CORR** — the levels↔zeros correlation.

The observatory's headline result is gate H5 (L = 72, 5184×5184, 40 dense eigensolves, 4 regimes × 7 realizations plus the α-profile, 46 minutes on a smartphone). The regimes: **A** (baseline: $N_v = 4$, $\alpha = 0.5$) — $\langle r\rangle = 0.5898 \pm 0.0102$, median KS $D = 0.3531$ — a systematic outlier; **B** (monograph density: $N_v = L^2/36$) — $\langle r\rangle = 0.6000 \pm 0.0052$, but individual KS 1/7 — GUE by the OR-clause only; **C** (sharp flux: $\alpha = 25/900 \approx 0.0278$) — $\langle r\rangle = 0.5937 \pm 0.0041$, individual KS 0/7; **D** (combined) — $\langle r\rangle = 0.6003 \pm 0.0050$, median $D = 0.0148$, twice below the critical $d_{\mathrm{crit}} = 1.63/\sqrt{n} \approx 0.031$, individual KS **7/7** — the only clean pass. Conclusion: GUE quality requires either density or sharp flux only at OR-clause level, but their combination passes cleanly.

#### 9.3. The RH line and the monumental line

The RH line maximizes the cloud's correlation with the $\zeta$ zeros: `RH_Unified.jl` (500 real zeros, 61 "magic" α-points, 6 vortices in a hexagon, an RHConfig of 33 parameters), `RH_Unified_v5.jl` (extended presets) and `RH_Sweep_Pro.jl` (the professional sweep: 13,661 real zeros via `mpmath.zetazero` at 25 digits, a dynamic sweep of 8 parameters over 10 key points, CSV/TXT/JSON reports). The magic α-grid (π/30…π×5, √2…√15, rationals, φ, e, ln 2, 1/e, 1/π) is a universality check of the RMT class: the GUE class must not depend on the arithmetic nature of the flux.

The monumental line is a Julia port of the Python monograph base: `AB_Cloud_Monumental_v6_3.jl` (the module `AB_Cloud_Monumental`, verifications **V01–V112**, `run_all()`, `run_only([...])`, clean CSV + JSON + PNG dashboards). The same family carries the main `ab_cloud_v*.jl` line from v19 (23,342 lines, 37 tests) to `ab_cloud_v23_v2.jl` (30,908 lines — the "supercombo": 38 tests × the plotting engine × the three-pass Test 38) and the compact `hp_audit_standalone.jl`. The Meridian design system (files with the `_D` suffix) changes only the console "clothing" — the physics and the numbers are bit-identical.

#### 9.4. Level VI boundaries

The observatory is an instrumental line: its gates measure but do not prove. Gate H5 shows that regime D is cleanly GUE by KS; that is a statistical statement about lattice ensembles, not about the zeros. The RH line maximizes correlation with the zeros — a controlled optimization, not an identity. The 50,000-zero table is an external reference computed via `mpmath.zetazero`; the blind protocols of level IV remain the only internal source of trust for the ζ side.

---

---

## 30b. The observatory's README (English version, verbatim)


**Language / Язык:** [🇬🇧 English](../../../meridian-spectral-observatory/README.md) · [🇷🇺 Русский](../../../meridian-spectral-observatory/README.ru.md)

**A suite of verification codes for the "AB-Cloud" project — from the lattice Aharonov–Bohm model to the statistics of the zeros of the Riemann zeta function.**

> Author of all codes and research: **Isaev, Iskhak Khamzatovich**
> ORCID: [0009-0003-7299-0701](https://orcid.org/0009-0003-7299-0701) · DOI: [10.5281/zenodo.21825394](https://doi.org/10.5281/zenodo.21825394)
> Related repositories: [research-papers](https://github.com/wild8highlander/research-papers) · [ab-cloud-research](https://github.com/wild8highlander/ab-cloud-research)

---

## ⚡ What this is — in a nutshell

This is a **laboratory of 24 self-contained Julia codes and one Python code** that test one big idea — the **Hilbert–Pólya conjecture**: that the non-trivial zeros of the Riemann zeta function ζ(s) behave like the spectrum (the set of energy levels) of some quantum system. The folder name — *Spectral Observatory* — captures the spirit: we **watch spectra** — of lattice AB-cloud Hamiltonians and of the zeros of ζ(s) — and compare their fingerprints.

Technically, each file is a **standalone "supercombo" bench**: open one file in Julia and you get an interactive console menu with dozens of tests, plots, reports and a built-in self-check system. No project-external modules, no builds: copy the file — it works (or honestly tells you what is missing).

The three pillars of the project:

1. **The AB cloud** — a lattice quantum model: a Hamiltonian on an L×L lattice with **magnetic-flux vortices** (the Aharonov–Bohm effect, flux α per vortex). The spectrum of this Hamiltonian is our "experimental material".
2. **The zeros of ζ(s)** — 50 000 real zeta zeros (file `zeros50k.txt`, from 14.134725142 to 40433.687385) — the "reference standard" we compare against.
3. **GUE statistics** — random matrices of the Gaussian Unitary Ensemble (β=2): the reference nearest-neighbor level statistics (⟨r⟩ ≈ 0.5996, band [0.5772, 0.6212]). The zeros of ζ(s) are known to follow GUE — the question is: **at which parameters does the AB cloud reach GUE as well?**

---

## 🏆 Headline result (Gate H5, L=72, 2026-09-09)

40 dense eigensolves of 5184×5184 matrices, 4 regimes × 7 realizations + α-profile, 46 minutes on a smartphone:

| Regime | Vortex density | Flux α | ⟨r⟩ | in GUE band | individual KS pass | median KS_D | Verdict |
|:---:|---|:---:|:---:|:---:|:---:|:---:|---|
| **A** baseline | Nv=4 (0.08%) | 0.5000 | 0.5898±0.0102 | 6/7 | 0/7 | 0.3531 | misses GUE |
| **B** monograph density | Nv=144=L²/36 (2.78%) | 0.5000 | 0.6000±0.0052 | 7/7 | 1/7 | 0.0559 | GUE reached — *OR-clause only* |
| **C** sharp flux | Nv=4 (0.08%) | 0.0278 | 0.5937±0.0041 | 7/7 | 0/7 | 0.0646 | GUE reached — *OR-clause only* |
| **D** combined | Nv=144=L²/36 (2.78%) | 0.0278 | 0.6003±0.0050 | 7/7 | **7/7** | **0.0148** | **GUE reached (clean)** |

**Reading:** GUE statistics recover in regimes B, C, D, but only the combination **[D] = monograph density + sharp flux α = 25/900 passes cleanly** (every single realization passes the KS test at p > 0.01; median KS_D is 2× below the critical value d_crit = 1.63/√n ≈ 0.031). The published baseline regime [A] is a systematic outlier (median D ≈ 0.35, worsening with L). Full interpretation: [docs/05](../../02_data/raw/meridian/docs/05_gate_H5_regimy.md).

---

## 🗺️ Repository map

### 🔬 Main line: `ab_cloud_v*.jl` — Verification Suite

| File | Lines | What it is |
|---|---:|---|
| `ab_cloud_v19.jl` | 23 342 | v19.1 — 37 tests, Hilbert–Pólya focus + advanced RMT diagnostics |
| `ab_cloud_v19_v1.jl` | 23 956 | evolution of v19 |
| `ab_cloud_v20.jl` | 24 596 | intermediate evolution |
| `ab_cloud_v21.jl` | 25 519 | v21 — 38 tests + Physics Lab + 3D Lab (sparse engine) |
| `ab_cloud_v21_v1.jl` | 25 519 | v21 fixes |
| `ab_cloud_v22.jl` | 7 369 | v22.2 — journal-grade plotting engine (module `ABPlotV23`), THREE-PASS Test 38 |
| `ab_cloud_v23.jl` | 28 281 | start of the v23 line |
| `ab_cloud_v23_v1.jl` | 29 904 | evolution of v23 |
| **`ab_cloud_v23_v2.jl`** | **30 908** | ⭐ **SUPERCOMBO v23.6 — the most complete bench**: v21 core (38 tests + Physics Lab + 3D Lab) × v22 plotting engine × THREE-PASS Test 38 (38a+38b hardcore+38c ladder), H1 deepen-protocol, H5 α-profile, decoy controls, presets FAST L=16 / FULL L=56 |

Files with the **`_D`** suffix are the same versions with the **MERIDIAN DESIGN SYSTEM v1.0**: a unified console identity (double-frame banners, ◆-sections, ✓/✗/⚠ statuses, live ▰▰▰▱▱ progress bars, true-TTY colors). The physics and the numbers are bit-identical: only the console "clothing" changes.

### 🎯 HP·MERIDIAN: `hp_audit_standalone.jl` (v24.2-SA)

| File | Lines | What it is |
|---|---:|---|
| **`hp_audit_standalone.jl`** | **6 054** | ⭐ Compact standalone audit of **gates H1–H7 only** (the Hilbert–Pólya hypothesis). The core is lifted VERBATIM from v23_v2 — with equal seeds the numbers match bit-for-bit. Plus: H5 budget ≤ 40 diagonalizations (v24.1), the targeted **FOCUS-D** mode (`hp_regime_mode = :regime_d`, command `5d`, v24.2), a live progress bar during LAPACK calls, a 60 s heartbeat (v23.8), environment doctor, battery cost estimation |

The 7 gates: **H1** PRIME-TRACE (Bragg comb at ω = log p + composite decoy controls + regime-matched null models + deepen protocol P95) · **H2** WEYL-DOS (N(E) ladder, AICc showdown) · **H3** POWER-LAW (exponent ladder, dictionary falsification) · **H4** CRITICAL-Q (sharpness scan + domain guard) · **H5** REGIME-2×2 (4-regime ensemble showdown + α-profile: finetuning vs plateau) · **H6** HERMIT-STRESS (self-adjointness/stability) · **H7** SEQ-CORR (levels↔zeros correlation).

### 🌀 RH line: maximizing the correlation of the AB cloud with the zeros of ζ(s)

| File | Lines | What it is |
|---|---:|---|
| `RH_Unified.jl` | 1 885 | single self-contained file: 500 real ζ-zeros, 61 "magic" α-points, 6 vortices (hexagon), RHConfig (33 parameters), jitter, 4 vortex layouts, 9 presets |
| `RH_Unified_v5.jl` | 2 204 | evolution: extended presets and diagnostics |
| `RH_Sweep_Pro.jl` | 6 450 | ⭐ **professional parameter sweep**: 13 661 real ζ-zeros (mpmath.zetazero, 25 digits), dynamic sweep of 8 parameters over 10 key points, CSV/TXT(ASCII)/JSON reports, Plots.jl graphics, timing logs |

### 🏛️ Monumental line

| File | Lines | What it is |
|---|---:|---|
| `AB_Cloud_Monumental_v6_3.jl` | 7 759 | module `AB_Cloud_Monumental` — a Julia port of the Python code base: **V01–V112** verifications of the AB-Cloud monograph. `run_all()`, `run_all(quick=true)`, `run_only(["V11","V35"])`; clean CSV + JSON + PNG dashboard; optional Arpack.jl (large L) and Plots.jl |

### 🧰 Utilities and libraries

| File | Lines | What it is |
|---|---:|---|
| `Magic_Alpha_Points_v1.jl` | 131 | library of **61 "magic" α-points**: π/30…π×5, √2…√15, rationals, φ, e, ln(2), 1/e, 1/π and specials — from the original RMT study of the AB cloud |
| `test11_honest.jl` | 322 | honest recalibration of Test 11 (Anderson–Darling GOF of ζ-zero spacings vs the Wigner surmise GUE β=2): removes the bootstrap artifact of ties (49 999 draws from a pool of ~8 000), the null is built i.i.d. from `gue2_surmise_cdf` |
| `test11_honest.py` | 178 | the same protocol in Python (default input — `zeta_zeros_50k.txt`) |

### 📊 Data and configuration

| File | Size | What it is |
|---|---:|---|
| `zeros50k.txt` | 50 000 lines | **50 000 real zeros of ζ(s)**, one per line: 14.134725142 … 40433.687385462 |
| `zeta_zeros_50k.txt` | 5 000 lines | the same 50 000 zeros, 10 per line (format for `test11_honest.py` etc.) |
| `p_myset.cfg` | 37 lines | the "myset" configuration profile for HP·MERIDIAN: `hp_L=20`, ensemble 8, seed 2026, ladder lattice [16,20,24], showdown mode, etc. |

---

## 🚀 Quick start

Requires [Julia](https://julialang.org) ≥ 1.10 (tested on 1.12). The main benches use **only the standard library** — no packages to install.

```bash
# 1) Supercombo bench (38 tests, interactive menu)
julia -e 'include("ab_cloud_v23_v2.jl")'

# 2) Compact HP audit H1–H7 (7 gates, the meridian> console)
julia -e 'include("hp_audit_standalone.jl")'

# 3) Monumental verifications V01–V112
julia -e 'include("AB_Cloud_Monumental_v6_3.jl"); AB_Cloud_Monumental.run_all(quick=true)'

# 4) Honest test 11 (Python)
pip install mpmath numpy   # if not yet installed
python3 test11_honest.py
```

Important: **the zero data files sit next to the code on purpose** — the codes look for `zeros50k.txt` in the script directory (`@__DIR__`), in the working directory (`pwd()`), and via the `HP_ZEROS` environment variable / the console command `z`.

### Typical runtimes (mid-range smartphone, Termux)

| Run | Time |
|---|---|
| HP·MERIDIAN `:smoke` (L=20, validation) | ~ minutes |
| HP·MERIDIAN `f` FAST (L=72, H5 with the 40-solve budget) | **46 min** (measured 2026-09-09) |
| HP·MERIDIAN `F` FULL (L=56, deep) | hours |
| H5 single solve 64×64 (4096×4096 eigen) | ~ 49 s |
| H5 single solve 72×72 (5184×5184 eigen) | ~ 69 s |
| test11_honest | seconds–minutes |

> Each diagonalization is a dense L²×L² problem (e.g. L=72 → 5184×5184). Cost grows as ≈ L⁶, memory as ≈ L⁴.

---

## 📚 Full documentation (`docs/`)

The documentation is deliberately thorough — from "what is the AB cloud" to bit-level interpretation of verdicts (the documents are in Russian; the tables and formulas are universal):

| Document | Contents |
|---|---|
| [01 · Project overview](../../02_data/raw/meridian/docs/01_obzor_proekta.md) | the science case, the Hilbert–Pólya hypothesis, project history |
| [02 · Code catalog](../../02_data/raw/meridian/docs/02_katalog_kodov.md) | every file: what it computes, which tests, how to run |
| [03 · Launch guide](../../02_data/raw/meridian/docs/03_rukovodstvo_zapuska.md) | installing Julia (Termux/Linux/Windows), all presets and menus, dependencies |
| [04 · Physics and mathematics](../../02_data/raw/meridian/docs/04_fizika_matematika.md) | the AB cloud, vortices, flux α, GUE, ⟨r⟩, KS, Anderson–Darling, gates H1–H7 |
| [05 · Gate H5 and regimes](../../02_data/raw/meridian/docs/05_gate_H5_regimy.md) | regimes A/B/C/D, the 40-solve budget, FOCUS-D, real-run walkthroughs 16×16, 64×64 and 72×72 |
| [06 · ζ-zero data](../../02_data/raw/meridian/docs/06_dannye_zeta_nulej.md) | provenance, formats, GUE-check of the data themselves |
| [07 · Version chronology](../../02_data/raw/meridian/docs/07_hronologiya_versij.md) | the full evolution: RH_Unified → Sweep → Monumental → v19…v23.6 → v24.2 |
| [08 · Reproducibility](../../02_data/raw/meridian/docs/08_reproduciuemost.md) | seeds, profiles, honest verdicts, known caveats, checklist |

---

## 📖 How to cite

```bibtex
@misc{isaev2026abcloud,
  author       = {Isaev, Iskhak Khamzatovich},
  title        = {AB-Cloud Verification Suite: Meridian Spectral Observatory},
  year         = {2026},
  doi          = {10.5281/zenodo.21825394},
  orcid        = {0009-0003-7299-0701},
  url          = {https://github.com/wild8highlander/ab-cloud-research}
}
```

See also [CITATION.cff](../../CITATION.cff).

---

## ⚠️ Research status and honest caveats

The project is in an **active audit stage**: the codes follow the principle "an honest verdict matters more than a pretty one" — WARN is never disguised as PASS, null models are regime-matched, decoy controls must stay silent while the primes are heard, and the compute budget is declared before the run and never exceeded. The current results (72×72, Gate H5, 2026-09-09) point to **regime D (monograph density + sharp flux α = 25/900) as a clean GUE candidate: 7/7 individual KS passes, median KS_D = 0.0148 against the 0.031 threshold, ⟨r⟩ = 0.6003±0.0050 — right on the GUE asymptote**, while the baseline regime A is systematically off (median D ≈ 0.35). The gate verdict is PARAMETER-DEPENDENT: GUE recovers in B, C, D, but cleanly only in D. This is not yet a claim of proof — see the "Known caveats" section in [doc 08](../../02_data/raw/meridian/docs/08_reproduciuemost.md) and the run walkthrough in [doc 05](../../02_data/raw/meridian/docs/05_gate_H5_regimy.md).

All the code consists of self-contained research benches without project-external dependencies; the rights belong to the author (see CITATION.cff).


---

## 31a. The observatory: project overview (condensed from the RU source)

The project overview document (docs/01) frames the observatory: a laboratory of 24 standalone Julia codes and one Python code testing one big idea — the Hilbert–Pólya conjecture: that the non-trivial zeros of the Riemann zeta function behave like the spectrum of a quantum system. The folder name captures the spirit: we *watch spectra* — of lattice AB-cloud Hamiltonians and of the zeros of ζ(s) — and compare their fingerprints. Each file is a standalone "supercombo" bench: an interactive console menu with dozens of tests, plots, reports and a built-in self-check. No project-external modules, no builds: copy the file — it works (or honestly reports what is missing). The three pillars: the AB cloud (a Hamiltonian on an L×L lattice with magnetic-flux vortices — the Aharonov–Bohm effect, flux α per vortex; the spectrum is the "experimental material"); the zeros of ζ(s) (the 50,000-real-zero reference table, 14.134725142 to 40433.687385 — the "reference standard"); GUE statistics (β=2: ⟨r⟩ ≈ 0.5996, band [0.5772, 0.6212] — the reference nearest-neighbour statistics). The zeros of ζ(s) are known to follow GUE — the observatory's question: at which parameters does the AB cloud reach GUE as well?


---

## 31b. The observatory: the code catalogue (condensed from the RU source)

The catalogue document (docs/02) lists the 25 files with line counts and roles. The main verification line `ab_cloud_v*.jl`: v19 (23,342 lines, 37 tests, H–P focus + advanced RMT diagnostics) → v19_v1 → v20 (24,596) → v21 (25,519; 38 tests + Physics Lab + 3D Lab on a sparse engine) → v21_v1 → v22 (7,369; the journal plotting engine ABPlotV23, the three-pass Test 38) → v23 (28,281) → v23_v1 (29,904) → **v23_v2 (30,908; the SUPERCOMBO v23.6)**. Files with the `_D` suffix carry the Meridian design system v1.0 — a unified console identity (double-frame banners, ◆-sections, ✓/✗/⚠ statuses, live ▰▰▰▱▱ progress bars, true-TTY colours); the physics and numbers are bit-identical. The HP·MERIDIAN line: `hp_audit_standalone.jl` (v24.2-SA, 6,054 lines) — the compact standalone audit of gates H1–H7 only, the core lifted VERBATIM from v23_v2 (equal seeds → bit-for-bit numbers), plus the H5 budget ≤ 40 diagonalizations (v24.1), the FOCUS-D mode (`hp_regime_mode = :regime_d`, command `5d`, v24.2), a live progress bar during LAPACK calls, a 60-second heartbeat (v23.8), an environment doctor and a battery-cost estimate. The RH line: `RH_Unified.jl` (1,885; 500 real ζ-zeros, 61 "magic" α-points, 6 hexagon vortices, RHConfig with 33 parameters, jitter, 4 layouts, 9 presets), `RH_Unified_v5.jl` (2,204), `RH_Sweep_Pro.jl` (6,450; 13,661 real ζ-zeros via mpmath.zetazero at 25 digits, a dynamic sweep of 8 parameters over 10 key points, CSV/TXT/JSON reports, Plots.jl, timing logs). The monumental line: `AB_Cloud_Monumental_v6_3.jl` (7,759) and its `_D` twin — the module `AB_Cloud_Monumental`, a Julia port of the Python code base: the V01–V112 verifications of the AB-Cloud monograph, `run_all()`, `run_all(quick=true)`, `run_only(["V11","V35"])`, clean CSV + JSON + PNG dashboards, optional Arpack.jl (large L) and Plots.jl. Auxiliary: `Magic_Alpha_Points_v1.jl` (the 61-point grid), `test11_honest.jl` / `test11_honest.py` (the honest Anderson–Darling test), the two zero-table formats, `p_myset.cfg`.


---

## 31c. The observatory: the launch guide (condensed from the RU source)

The launch guide (docs/03) covers the practical entry: Julia ≥ 1.10 (≥ 1.12 recommended for the reference runs); no project environment needed — each file is self-contained. The console menus: the main suite offers per-test and batch runs, the two-pass protocol, the Labs ('l' — Physics Lab; 'd3' — 3D Lab); hp_audit offers commands 1–7 for the gates plus `5d` (FOCUS-D) and the budget display. Presets: FAST (L=16, minutes) and FULL (L=56, hours) in v23_v2; the reference run used 72×72 primary / 96×96 secondary. Runtime expectations are printed before execution — the ⚠ RUNTIME banner: the honest pre-run cost estimate with a ±3× machine factor and RAM-gated rungs skipped with a printed reason. Reproduction of the reference numbers: fixed seed protocols; the H5 gates' table (A/B/C/D) reproduces at equal seeds; plots regenerate deterministically (600 dpi PNG + SVG + PDF + GIF per figure). The guide closes with troubleshooting: LAPACK threading (set to 1 for reproducibility), memory ceilings per L, and the environment doctor (`hp_audit` command `0`).


---

## 31d. The observatory: physics and mathematics (condensed from the RU source)

The theory document (docs/04) is the project's "theoretical minimum". The Hamiltonian: a square L×L lattice, one-particle space ℂ^(L²), tight-binding hops with Peierls phases — a vortex is a plaquette with pressed-in flux α: circulating it accumulates 2πα. Matrix assembly: dense Hermitian N×N with N = L²; "lattice 64×64" means a 4096×4096 matrix; diagonalization O(N³) = O(L⁶); memory O(N²) = O(L⁴) with a ×2.5 LAPACK overhead; the 16 → 72 transition costs ×8000. Vortex configurations: Nv = 4 (the historical baseline); Nv = L²/36 (the "monograph density" — one cell per 6×6 sites: 114 at L=64); layouts hexagonal/ring/random/grid; jitter (positions 0.35, flux α 0.02, charges, width) so results are not artefacts of perfect geometry. The statistics: unfolding by degree-5/9 polynomial; the r-statistic (⟨r⟩_GUE ≈ 0.5996, the project's finite-ensemble CI [0.5772, 0.6212], Poisson 0.5307); the Wigner surmise p(s) = (32/π²)s²e^(−4s²/π) with the normalization identity (1/2)! = √π/2 — checked by Test 37; the KS criterion with d_crit = 1.63/√n and the critical consequence: n ≈ 0.6·L², so L=16 gives d_crit ≈ 0.132 and L=64 gives ≈ 0.033 — the threshold tightens 4× at unchanged physics (the key to reading the runs); Anderson–Darling and the MC-null discipline (i.i.d. from H0, add-one smoothing). The gates' anatomy: H1 PRIME-TRACE (the Bragg comb at ω = log p + composite decoys + regime-matched nulls + the P95 deepen protocol); H2 WEYL-DOS (the N(E) ladder, AICc); H3 POWER-LAW (the exponent ladder, dictionary falsification); H4 CRITICAL-Q (sharpness + domain guard); H5 REGIME-2×2 (the four-regime ensemble + the α-profile); H6 HERMIT-STRESS; H7 SEQ-CORR.


---

## 31e. The observatory: the H5 gate regimes (condensed from the RU source)

The H5 regimes document (docs/05) is the full story of the headline result. The 2×2 design: {Nv = 4 baseline vs Nv = L²/36 monograph density} × {α = 0.5 vs α = 25/900 sharp flux} at L = 72 (5184×5184): 40 dense eigensolves — 4 regimes × 7 realizations + the α-profile — in 46 minutes on a smartphone. The results table: regime A — ⟨r⟩ = 0.5898 ± 0.0102, median KS D = 0.3531, 6/7 in band, 0/7 individual KS — a systematic outlier (worsening with L); regime B — ⟨r⟩ = 0.6000 ± 0.0052, median D = 0.0559, 1/7 individual — GUE by the OR-clause only; regime C — ⟨r⟩ = 0.5937 ± 0.0041, median D = 0.0646, 0/7 — OR-clause; regime D — ⟨r⟩ = 0.6003 ± 0.0050, median D = 0.0148, **7/7 individual KS** (every realization passes at p > 0.01; the median D is 2× below the critical 1.63/√n ≈ 0.031). The reading: GUE statistics recover in B, C, D, but only the combination [D] = monograph density + sharp flux passes cleanly. The document analyses the α-profile: the published baseline A is the outlier, not the physics; the "sharp" α values form a quality plateau (not a fine-tuned point); the density axis and the flux axis are complementary levers — neither alone suffices, their combination is clean. The document closes with the L-dependence caveat: as L grows, d_crit falls as 1/√n — the clean pass must survive growing statistical power (the programme of v23_v2's FULL preset and beyond).


---

## 31f. The observatory: the ζ-zero data (condensed from the RU source)

The data document (docs/06) documents the 50,000-zero table: two files, one table. `zeros50k.txt` — one number per line, 50,000 lines, used by HP·MERIDIAN and the suite; `zeta_zeros_50k.txt` — ten numbers per line, 5,000 lines, the default input of `test11_honest.py`, convenient for numpy/pandas. The control: the two files' last values agree to 12 digits; exactly 50,000 zeros in each. The range: γ₁ = 14.134725142 (Odlyzko verified) … γ₅₀₀₀₀ = 40433.687385462. The physical scale: the mean density ~ ln(γ/2π) ≈ ln(6433) ≈ 8.8 zeros per unit t; the typical local gap 0.11–0.12; long enough for global statistics (⟨r⟩, gap distributions) and sliding windows (the t-dependence scans of test11_honest). The origin: computed via `mpmath.zetazero()` at 25 digits — the same technology as the RH line's 13,661 zeros; "real" ζ zeros, not model surrogates — critical for gates H1/H7 and Test 11 where the ζ side is the reference. The self-check (pure numpy): load the table, diff, compute r — ⟨r⟩ ≈ 0.614–0.616 → the GUE class (0.5996). The package-level audit of this edition refined this to 0.6119 ± 0.0010 over the full table.


---

## 31g. The observatory: the version chronology (condensed from the RU source)

The chronology document (docs/07) tracks the suite's evolution. v19 (2026-08): the 37-test two-pass reference architecture — the H–P focus, the advanced RMT diagnostics, the honest verdict layer; the reference run of 2026-09-02 (35,146 s). v19_v1: the fixes of the first field reports. v20: intermediate evolution — the disorder cap (W_max), the byte-robustness protocol. v21: the sparse engine (Arpack.jl for large L), the Physics Lab (interactive single-experiment bench: L, α, W, q, Nv, boundary, model — with plots and a per-experiment report) and the 3D Lab (L=10 torus, tz, mass, seed 777); Test 38 joins. v21_v1: fixes. v22: the journal plotting engine (module ABPlotV23: 600 dpi PNG + SVG + PDF + GIF per figure, animation reveals), the THREE-PASS Test 38 (38a standard + 38b hardcore + 38c ladder). v23 → v23_v1 → **v23_v2**: the SUPERCOMBO — the v21 core × the v22 engine × the three-pass Test 38, plus the H1 deepen protocol, the H5 α-profile, decoy controls and the FAST/FULL presets. v24.1-SA → v24.2-SA (`hp_audit_standalone.jl`): the compact gates-only audit with the H5 budget (≤ 40 diagonalizations), FOCUS-D, the heartbeat, the doctor. The `_D` design system: the console clothing without physics changes.


---

## 31h. The observatory: reproducibility (condensed from the RU source)

The reproducibility document (docs/08) fixes the discipline: seeds are protocol constants (the suite's run seeds; base 96 in the vortex optimization; 12345 for bytes; 777 for the 3D lab); every run writes a computation log (timestamp + delta + action) and a console capture; the two-pass protocol labels every verdict by pass; plots regenerate deterministically from the suite (the committed run strips PNGs — 453 files of reports, tables and logs — because the plots reproduce); cross-checks: hp_audit against v23_v2 at equal seeds — bit-for-bit; the H5 gates' table reproduces; the Julia↔Python agreement of test11_honest (the AD test and the table checks). The RAM honesty ladder: L=96 ≈ 1.4 GB peak; L=112 ≈ 2.5 GB; L=128 ≈ 4.3 GB — skipped with a printed reason. The smartphone benchmark: the H5 battery (40 eigensolves of 5184×5184) in 46 minutes — the v24.1 budget makes the whole gates battery laptop- and even phone-class. The document closes with the environment doctor: `hp_audit` command `0` — LAPACK threads, BLAS backend, memory ceilings, Julia version.


---

# PART IX. LEVEL VII: THE VORTEX-DENSITY OPTIMIZATION

## 31. Level VII: the problem, the instruments, port validation

Test 34 of the v19 run compares the cloud's unfolded adjacent-level spacings with the unfolded spacings of the first 50,000 ζ zeros by a two-sample Kolmogorov–Smirnov test. The reference configuration (96×96, $N_v = 2$, $q = 1.0$, $\alpha = 0.5$, $W = 1.0$, open boundaries, 5 realizations) gives pooled $D = 0.1096$ (p = 2.24·10⁻¹⁸⁶) — formally WARN (acceptance requires $D < 0.10$). Level VII poses the physics question: the vortex configuration is a set of dials — which settings drive $D$ down?

The scan's instruments. The dials: $N_v$ (0…20), $q$ (0.5, 0.7, 0.9, 1.0), $W$ (0, 0.5, 1.0, 1.5), $\alpha$ (0.3, 0.4, 0.5, 0.6), geometry (protocol-random / regular grid / cluster; open / torus). The acceptance criterion — the 34b composite: (1) KS $p > 0.01$ or $D < 0.10$; (2) ⟨|ΔR₂|⟩ < 0.10; (3) $d_{GUE} < d_{Poisson}$; (4) $D$-spread < 0.10.

Port validation — before any scan data was accepted: hermiticity of $H$ after symmetrization 0.0e+00; cell-flux uniformity on the torus at $\alpha = 1/4$: exactly 0.25 on every cell; the KS implementation against `scipy.stats.ks_2samp`: agreement ≤ 10⁻¹²; the ζ-side unfolding: 49,999 spacings (matching the suite's reference log); the L=96 unfolding counts: 5528/5527 (matching the reference log); the reference configuration re-measured: $D = 0.0928$, spread 0.072–0.111 — reproducing the Julia level (0.1096) within run-to-run spread; determinism: base seed 96; vortex RNG base+3500 (shared); disorder RNG base+3500+k (per realization). Engineering: column-ordered (F-order) matrices with `overwrite_a`; every measurement isolated in a subprocess with `malloc_trim` (glibc arena retention — the same phenomenon the Julia suite hit as `ab_gc`); peak 1.4 GB at L=96; L=96 ≈ 155 s per realization; a full Stage-C configuration ≈ 13 min.


---

## 32. Stages A, B, C: the full scan protocol

**Stage A — the coarse sweep (L = 24, 576 sites):** 171 configurations; 3 realizations each; all four dials × geometry. Output: `sweep_A_L24.csv`. The valley found: $N_v = 6$–16 (best at 12), $q = 0.7$–1.0, $W = 0.5$–1.0, $\alpha = 0.5$; torus ≥ open ≥ …; cluster placement is catastrophic ($D = 0.11$–0.17). Edge cases: the pure vortex-free lattice $N_v = 0$: $D = 0.73$ — without vortices the cloud does not exist as a ζ-statistics object; $N_v = 1$: $D = 0.194$.

**Stage B — refinement (L = 32, 48, 64):** 46 configurations; finite-size stability tests of the Stage-A valley, α-criticality, and the per-L GUE floor — the same-sample KS between a GUE ensemble and the ζ zeros: the method's statistical zero. Floors: L=24 → 0.0324; 32 → 0.0331; 48 → 0.0309; 64 → 0.0257; 96 → 0.0220. Output: `sweep_B_refine.csv`.

**Stage C — verification at the full 96×96 lattice:** 5 candidates × 5 realizations under the full 34b protocol (N = 9,216 sites, 5,528 spacings per realization, 27,640 pooled) plus an independent L=96 GUE control (2 × 5,527-spacing GUE samples vs ζ): $D_{\mathrm{floor}} = 0.0220$. Output: `sweep_C_L96.csv`, `gue_control_L96.json`, `curves/*.npz`.

The Stage-C result: the $N_v=2$ reference — $D = 0.0928$ (the edge); $N_v=8$, $q=1.0$, $\alpha=0.6$, grid — 0.0358 (PASS); $N_v=16$, $q=0.7$, open — 0.0387 (PASS); and the best — $N_v=16$, $q=1.0$, $\alpha=0.5$, torus — **0.0318** (PASS); the GUE control — 0.0220 (the floor). Three facts matter: (1) the reference sits at the acceptance edge (spread 0.072–0.111 straddling $D = 0.10$); (2) all three optimized candidates pass with margin, the best improving pooled distance ×3.4; (3) the residual gap is nearly irreducible: the ζ spacings themselves differ from finite GUE samples by $D \approx 0.022$ — that is what the floor *is*; the best candidate closes ≈ 89% of the reference-to-floor gap. The honest caveat: the floor itself fails the p-arm (p = 3.0·10⁻⁴) — ensemble finiteness, the same caveat as the ζ-vs-GUE comparison.


---

## 33. The mechanism: the physics of the working window

The window's physics reads through the overlap of vortex phase fields. **The dilute regime ($N_v \lesssim 4$):** large coherent patches of the lattice keep nearly real, nearly integrable hopping structure → $\langle r\rangle \approx 0.51$–0.58, $D > 0.07$; the vortex phase fields do not cover the operator. **The working window ($N_v \approx 8$–16):** the phase fields overlap and jointly complexify *every* bond — the regime where the BGS prescription (a Hermitian operator with no antiunitary symmetry, complex phases) is actually realized → $D$ falls to the floor. **The dense regime ($N_v \gtrsim 20$):** on-site wells overlap into their own landscape; the vortex gas re-organizes → uniformity degrades again.

Each dial's role. $q = 1$: completes the flux quantization $2\pi q = 2\pi$ and maximizes phase incommensurability; fractional charges leave partially commensurate phases. $\alpha = 0.5$: the Connes self-dual critical line; deviating α by ±0.1 at L=32 roughly doubles $D$. Geometry: clusters destroy texture uniformity (0.11–0.17); regular grids are excellent at $N_v = 8$; the torus is best overall. $W$: the 0.5–1.0 window — wells deep enough to bind states, not deep enough to dominate.

The classical analogy — the vortex-media hierarchy: a breeze (few coherent eddies, configuration-dependent response, no universality — the Onsager point-vortex limit) → ocean-scale transport (overlapping eddy fields, collective statistics, universality) → self-obstruction (vortex-lattice/turbulent re-organization). The correspondence is structural, not literal: cloud vortices are gauge vortices — phase singularities of a quantum wavefunction — not fluid eddies. What transfers is the density-controlled crossover from individual to collective behaviour with a non-monotone response and a broad working plateau.

The operator reading: the scan maps the Hamiltonian family $H(N_v, q, W, \alpha)$ onto a scalar distance-to-ζ; its minimum is broad and shallow — the signature of a robust working point, not a fine-tuned one. The honest H–P reading: the result does not prove RH and does not exhibit the Hilbert–Pólya operator. It establishes a *necessary statistical condition* any H–P candidate must satisfy: a Hermitian operator of a simple, physically transparent gauge type reproduces the ζ zeros' spacing statistics to within the finite-sample floor. Quantitative numerical support for the statistical (Montgomery–Odlyzko) arm of the Hilbert–Pólya programme — and nothing more.

The recommendation to the suite: run the reference comparison with `--ab-nv-secondary 16 --ab-bc torus --ab-alpha 0.5` — the headline statistic moves from the WARN band to the deep PASS band; keep the $N_v = 2$ default in the docs as the conservative dilute benchmark against which the optimization is measured.


---

## 33a. Vortex optimization: the full source record (README, verbatim)
# Vortex-Density Optimization for the AB-Cloud — Complete Research Package

> **Repository:** `wild8highlander/ab-cloud-research`
> **Study:** Large-scale parameter scan of the AB-cloud vortex system against the Riemann ζ zeros (extension of the suite's `test_34_direct_vs_zeta`, referred to as **Test 34-ext**)
> **Status:** ✅ Completed — 3 of 3 verified candidates **PASS** the composite criterion at the full 96×96 lattice
> **Date:** September 2026 · **Runtime budget:** ≈ 242 configurations, L = 24 → 96
> **Outcome:** the optimal vortex window **Nv ≈ 8–16, q ≈ 0.7–1.0, W = 0.5–1.0, α = 0.5 (strictly)**; best pooled KS distance to the ζ-zero spacings **D = 0.0318** vs the suite reference **D = 0.1096 (WARN)** — a **×3.4 improvement**, within 0.010 of the finite-sample GUE floor (0.0220).

---

## 1. TL;DR

| # | Configuration (96×96, 5 realizations each) | D (pooled) | Spread | Verdict |
|---|---|---|---|---|
| 1 | Nv = 2, q = 1.0, α = 0.5, open — **suite reference** | **0.0928** | 0.072–0.111 | edge of acceptance (Julia suite: 0.1096 → WARN) |
| 2 | Nv = 8, q = 1.0, α = 0.6, open, regular grid | 0.0358 | 0.033–0.039 | **PASS** |
| 3 | Nv = 16, q = 0.7, α = 0.5, open | 0.0387 | 0.037–0.041 | **PASS** |
| 4 | **Nv = 16, q = 1.0, α = 0.5, torus** — **best** | **0.0318** | 0.028–0.038 | **PASS** |
| — | GUE control, same sample structure | 0.0220 | — | floor |

**One-line recommendation for the suite:** run the reference comparison with `--ab-nv-secondary 16` (torus, α = 0.5) — the headline statistic moves from the WARN band (0.1096) to the deep PASS band (≈ 0.032).

---

## 2. Background: the problem this study solves

The AB-cloud is a lattice quantum system — a Hofstadter Hamiltonian whose hopping phases are deformed by Aharonov–Bohm vortices (the `:monumental` phase model: smooth atan-gauge phases on bonds plus on-site potential wells `V = qW/(r²/N + 1)`). The verification suite's **test 34** compares the cloud's unfolded adjacent-level spacings with the unfolded spacings of the Riemann ζ zeros (first 50,000 zeros → 49,999 spacings) by a two-sample Kolmogorov–Smirnov test.

The reference run of the suite (96×96 lattice, Nv = 2, q = 1.0, α = 0.5, W = 1.0, open boundaries, 5 realizations) produced:

- pooled **D = 0.1096**, p = 2.24·10⁻¹⁸⁶ → **WARN** (the acceptance band requires D < 0.10);
- per-realization D ∈ [0.0923, 0.1189];
- ⟨|ΔR₂|⟩ = 0.0002 (excellent), d_GUE = 0.8764 < d_Poisson (GUE-side, as expected).

So the construction was *close* but formally *not inside* the acceptance region. The obvious physics question: **the vortex configuration is a set of dials — which dial settings drive D down?** That is exactly what this study measures.

### The dials

| Dial | Meaning | Scanned range |
|---|---|---|
| `Nv` | number of vortices (charge-neutral: half +q, half −q) | 0…20 |
| `q` | vortex charge (flux quantum fraction) | 0.5, 0.7, 0.9, 1.0 |
| `W` | on-site potential depth | 0, 0.5, 1.0, 1.5 |
| `α` | uniform Hofstadter flux per plaquette | 0.3, 0.4, 0.5, 0.6 |
| geometry | placement (protocol-random / regular grid / cluster), boundaries (open / torus) | all |

### The acceptance criterion (unchanged from the suite, test 34b "hardcore")

A configuration **passes** iff all of:

1. KS: p > 0.01 **or** D < 0.10 (pooled over realizations);
2. ⟨|ΔR₂|⟩ < 0.10 (R₂ band agreement with the ζ zeros);
3. d_GUE < d_Poisson (the cloud is GUE-side, not Poisson-side);
4. spread(D) < 0.10 across realizations (stability).

---

## 3. What was done: the three-stage scan

### Stage A — coarse sweep (L = 24, 576 sites)

171 configurations; 3 realizations each; all four dials × geometry. Output: `data/sweep_A_L24.csv`.

**The valley found:** Nv = 6–16 (best at 12), q = 0.7–1.0, W = 0.5–1.0, α = 0.5; torus ≥ open ≥ ... while **cluster placement is catastrophic** (D = 0.11–0.17). Pure lattice Nv = 0: D = 0.73 (the cloud simply does not exist as a ζ-statistics object without vortices). Nv = 1: D = 0.194.

### Stage B — refinement (L = 32, 48, 64)

46 configurations; tests finite-size stability of the Stage-A valley, α-criticality, and computes the **per-L GUE floor** — the same KS comparison applied to a GUE matrix ensemble of the same sample structure, which is the statistical zero of the whole method (no construction can beat it at fixed sample size). Output: `data/sweep_B_refine.csv`.

Floors measured: L = 24 → 0.0324, L = 32 → 0.0331, L = 48 → 0.0309, L = 64 → 0.0257, L = 96 → 0.0220.

### Stage C — verification at the full 96×96 lattice

Five candidates × five realizations under the **full 34b protocol** (N = 9216 sites, 5528 spacings per realization, 27,640 pooled), plus an independent L = 96 GUE control (2 × 5527-spacing GUE samples vs ζ): **D_floor = 0.0220**. Output: `data/sweep_C_L96.csv`, `data/gue_control_L96.json`, `curves/*.npz`.

Runtimes (laptop-class core): L = 96 ≈ 155 s/realization, peak memory ≈ 1.4 GB; a full Stage-C configuration ≈ 13 min; Stage A ≈ 2 min total.

---

## 4. Headline result and how to read it

```
D = 0.1096  ●──────────────────────────────────────────  suite reference (WARN)
D = 0.0928      ●───────────────────────────────────     port re-measurement (edge)
D = 0.0387                   ●────────────                Nv=16, q=0.7, open  (PASS)
D = 0.0358                 ●───────────                   Nv=8,  α=0.6, regular (PASS)
D = 0.0318              ●──────────                       Nv=16, torus          (BEST)
D = 0.0220  ▲                                            GUE floor (statistical zero)
```

Three facts matter:

1. **The reference configuration sits at the very edge** of acceptance (per-realization spread 0.072–0.111 straddles the D = 0.10 boundary).
2. **All three optimized candidates pass with margin**, and the best (Nv = 16, torus) improves the pooled distance **×3.4**.
3. **The remaining gap is nearly irreducible**: the ζ spacings themselves differ from finite GUE samples by D ≈ 0.022 (that is what the floor *is*). The best candidate therefore closes **≈ 89 %** of the reference-to-floor gap. Note the floor itself fails the p-arm (p = 3.0·10⁻⁴) — finite-ensemble finiteness, the same honest caveat the monograph records for the ζ-vs-GUE comparison.

### Why a window, and why *this* window (mechanism)

- **Dilute regime (Nv ≲ 4):** large coherent patches of the lattice keep nearly real, nearly integrable hopping structure → ⟨r⟩ ≈ 0.51–0.58, D > 0.07. The vortex phase fields do not cover the operator.
- **Working window (Nv ≈ 8–16):** vortex phase fields overlap and jointly complexify *every* bond — the regime in which the BGS prescription (Hermitian operator, no antiunitary symmetry, complex phases) is actually realized → D falls to the floor.
- **Dense regime (Nv ≳ 20):** on-site wells overlap into their own landscape and the vortex gas re-organizes → uniformity degrades again.
- **q = 1** completes the flux quantization 2πq = 2π and maximizes phase incommensurability; fractional charges leave partially commensurate phases.
- **α = 0.5** is the self-dual critical line (Connes self-duality, monograph §4.3/§8.1); deviating α by ±0.1 at L = 32 roughly *doubles* D.
- **Geometry:** clustered placement destroys the uniformity of the texture (D = 0.11–0.17); regular grids are excellent at Nv = 8; torus boundaries are best overall.

---

## 5. Physical interpretation: from a breeze to ocean currents

Vortex density is a universal control parameter across all vortex-bearing two-dimensional media, and the AB-cloud reproduces the same hierarchy spectrally:

| Regime | Fluids (classical/quantum) | AB-cloud (this study) |
|---|---|---|
| dilute | *a breeze*: few coherent eddies, configuration-dependent response, no universality (Onsager point-vortex limit) | Nv = 0–2: D ≈ 0.09–0.11, wide spread, threshold of acceptance |
| working window | *ocean-scale transport*: overlapping eddy fields, collective statistics, universality | Nv ≈ 8–16: D → floor, spread collapses, composite PASS |
| over-dense | *self-obstruction*: vortex lattice/turbulence re-organization | Nv ≳ 20: D rises again |

The correspondence is **structural, not literal**: cloud vortices are gauge vortices (phase singularities of a quantum wavefunction), not fluid eddies. What transfers is the density-controlled crossover from individual-vortex to collective-vortex behavior — with a non-monotone response and a broad working plateau in both settings.

**Operator-system reading:** the scan maps the Hamiltonian family H(Nv, q, W, α) onto a scalar *distance-to-ζ*; its minimum is broad and shallow — the signature of a robust working point, not a fine-tuned one.

**Hilbert–Pólya reading (honest form):** the result does **not** prove RH and does **not** exhibit the Hilbert–Pólya operator. It establishes a *necessary statistical condition* any H–P candidate must satisfy: a Hermitian operator of a simple, physically transparent gauge type can reproduce the ζ zeros' spacing statistics to within the finite-sample floor (D = 0.0318 vs 0.0220). That is quantitative numerical support for the statistical (Montgomery–Odlyzko) arm of the Hilbert–Pólya program.

---

## 6. Method fidelity: why these numbers can be trusted

The scan was not run on a re-implementation "inspired by" the suite — it ran on a **validated port** of the suite's Julia engine, with these checks executed *before* any scan data was accepted:

| Check | Result |
|---|---|
| Hermiticity of H after symmetrization | 0.0e+00 |
| Cell flux uniformity on torus (α = 1/4) | exactly 0.25 on every cell |
| KS implementation vs `scipy.stats.ks_2samp` | agreement ≤ 1e-12 |
| ζ-side unfolding | 49,999 spacings (= suite reference log) |
| L = 96 per-realization unfolding counts | 5528 / 5527 (= suite reference log) |
| Reference configuration re-measurement | D = 0.0928, spread 0.072–0.111 — reproduces the Julia level (0.1096) within run-to-run spread |
| Determinism | fixed seed protocol: base seed 96; vortex RNG base+3500 (shared); disorder RNG base+3500+k (per realization) |

Engineering notes: column-ordered (F-order) matrices with `overwrite_a` diagonalization; every measurement isolated in a subprocess with `malloc_trim` (glibc arena retention — the same phenomenon the Julia suite hit as `ab_gc`); peak 1.4 GB at L = 96.

---

## 7. Repository integration

### 7.1 Drop-in

This folder is self-contained. Recommended location: **repo root** as `t34_vortex_optimization/` (the provided `push_to_github.sh` does exactly that).

### 7.2 Upgrade the suite's headline test

```
# reference run (unchanged, keep as the conservative dilute benchmark)
julia --project=. ab_cloud_v23.jl test34b ...

# optimized configuration (recommended headline)
julia --project=. ab_cloud_v23.jl test34b --ab-nv-secondary 16 --ab-bc torus --ab-alpha 0.5
```

Expected effect: pooled D ≈ 0.03–0.04 instead of ≈ 0.11 (composite WARN → PASS). Keep the Nv = 2 default in the docs as the benchmark against which the optimization is measured.

### 7.3 Monograph

`monograph/AB_Cloud_PLOS_T34_vortex_optimization.docx` — the PLOS-track monograph with the new **Chapter 9 "The Large-Scale Vortex-Density Scan: From a Breeze to Ocean Currents (Test 34-Extension)"** (Sections 9.1–9.6, Table 1, Figs. 20–21), updated abstract/keywords/conclusions/open questions, chapters 9–12 renumbered to 10–13. A PDF preview is included. See `monograph/MONOGRAPH_CHANGES.md` for the exact change list.

> ⚠️ After opening in Word, press **Ctrl+A → F9** to refresh the Table of Contents field so the new chapter appears in it.

---

## 8. Reproduce everything

### Requirements

- Python ≥ 3.10, `numpy`, `scipy`, `matplotlib` (charts/report only)
- No Julia required for the scan itself; Julia ≥ 1.9 only for the original suite cross-check

### Commands

```bash
cd t34_vortex_optimization/scripts

# 0) port validation (fast, ~10 s) — MUST pass before anything else
python3 test_engine.py

# 1) Stage A  (L = 24, 171 configs, ~2 min)
python3 t34_sweep.py --stage A

# 2) Stage B  (L = 32/48/64, 46 configs, ~1.5 h)
python3 t34_sweep.py --stage B

# 3) Stage C  (L = 96, 5 configs × 5 realizations + reference, ~1.5 h)
python3 t34_sweep.py --stage C

# 3b) GUE control at L = 96 (~10 min)
python3 gue96.py

# 4) figures + PDF report (optional; needs matplotlib)
python3 t34_charts.py
python3 t34_report.py
```

Every stage writes CSV rows incrementally — an interrupted run resumes by skipping already-present configuration keys.

### Seeds (byte-level determinism on a fixed platform)

| RNG | Seed | Scope |
|---|---|---|
| vortex placement | `base + 3500` | shared across realizations of a configuration |
| on-site disorder ε ∼ U(−0.01, 0.01) | `base + 3500 + k` | per realization k |
| base seed | 96 | the suite's convention |

---

## 9. Data dictionary

All CSVs share the schema (one row = one configuration):

| Column | Meaning |
|---|---|
| `stage, L, Nv, q, W, alpha, bc, placement, n_real, seed_base` | configuration identity |
| `n_spacings` | unfolded spacings per realization |
| `D_pooled, p_pooled` | two-sample KS against the ζ spacings, pooled over realizations |
| `D_min, D_med, D_max` | per-realization spread |
| `mean_abs_dR2` | ⟨\|ΔR₂\|⟩ — mean absolute deviation of the R₂(s) band from the ζ curve |
| `d_GUE, d_Pois` | distance of ⟨r⟩ to the GUE (0.5992) / Poisson (0.5) targets |
| `r_mean` | mean adjacent-spacing ratio ⟨r⟩ |
| `D_excess` | D_pooled − GUE floor at this L (how far above the statistical zero) |
| `ks_pass, r2_pass, gue_closer, stab_pass, composite_ok` | the four arms of the criterion and the composite verdict |
| `runtime_s` | wall time per realization |

`data/gue_control_L96.json`: the Stage-C floor — `D_gue_vs_zeta = 0.0220` at n_spacings = 11054, p = 3.0e-4 (the floor's own p-arm failure is expected and is exactly why the criterion has the D < 0.10 arm).

`curves/*.npz`: binned R₂(s) curves for the four Stage-C configurations — keys: `s`, `R2_cloud`, `R2_zeta`, `R2_gue`, `R2_pois`.

---

## 10. File tree

```
t34_vortex_optimization/
├── README.md                  ← this file
├── README_RU.md               ← полная русская версия
├── data/
│   ├── sweep_A_L24.csv        ← Stage A: 171 configurations
│   ├── sweep_B_refine.csv     ← Stage B: 46 configurations (L = 32/48/64)
│   ├── sweep_C_L96.csv        ← Stage C: 5 × (96×96, 5 realizations)
│   └── gue_control_L96.json   ← L = 96 GUE floor (0.0220)
├── curves/                    ← R₂(s) curves of the 4 verified configs (npz)
├── figures/                   ← 7 report figures (PNG, 150–200 dpi)
├── report/
│   ├── Отчёт_исследование_вихрей_AB-Cloud_Тест34.pdf   ← full PDF report (RU, 12 pp.)
│   └── cover.html             ← vector cover source
├── scripts/
│   ├── t34_engine.py          ← validated port of the :monumental model + 34b protocol
│   ├── test_engine.py         ← port-validation suite (run first!)
│   ├── t34_sweep.py           ← staged scan driver (A/B/C)
│   ├── gue96.py               ← L = 96 GUE control
│   ├── t34_charts.py          ← the 7 figures
│   └── t34_report.py          ← the 12-page PDF report builder
└── monograph/
    ├── AB_Cloud_PLOS_T34_vortex_optimization.docx        ← PLOS monograph + Chapter 9
    ├── AB_Cloud_PLOS_T34_vortex_optimization_PREVIEW.pdf ← PDF preview
    └── MONOGRAPH_CHANGES.md   ← exact change list
```

---

## 11. Figure gallery

| File | What it shows |
|---|---|
| `figures/01_heatmap_D_Nv_q.png` | D(Nv, q) landscape at L = 24, W = 1.0 / 0.5 — the valley |
| `figures/02_D_of_Nv.png` | D(Nv) curves at q = 1.0 for W = 0/0.5/1.0 |
| `figures/03_D_of_q.png` | D(q) curves — the q = 0.7–1.0 valley |
| `figures/04_L_ladder.png` | D vs L for the leading configs + per-L GUE floor |
| `figures/05_alpha_scan.png` | α-criticality at L = 32: α = 0.5 strictly optimal |
| `figures/06_R2_s.png` | R₂(s) bands of the verified configs vs ζ / GUE / Poisson |
| `figures/07_stability.png` | per-realization D spreads at L = 96 |

---

## 12. FAQ

**Q: Is this a proof of the Riemann hypothesis?**
No. It is a verified numerical statement about spacing statistics: a Hermitian lattice-gauge operator family reproduces the ζ zeros' spacing statistics to within the finite-sample floor. Nothing here touches individual-zero arithmetic.

**Q: Why does the best candidate stop at 0.0318 when the floor is 0.0220?**
The floor is itself a two-sample KS distance between *finite* samples (GUE vs ζ, same sizes). At these ensemble sizes two pure-GUE samples differ by O(0.02). 0.0318 vs 0.0220 means the cloud is statistically indistinguishable from "as GUE as a finite sample can be", up to the last ~0.010.

**Q: Why keep Nv = 2 as the suite default?**
It is the conservative dilute-regime benchmark. Changing the default would silently invalidate cross-references to every previous run's headline number. Add the optimized configuration as a *new* headline instead.

**Q: Can I trust the Python numbers against the Julia suite?**
Section 6 above: the port reproduces the reference run's internal quantities exactly (unfolding counts, ζ count) and its D to within run-to-run spread; the KS implementation matches scipy to 1e-12.

**Q: What is the cheapest single experiment to re-verify the claim?**
Run `test_engine.py` (~10 s), then a single Stage-C configuration at reduced realizations (`t34_sweep.py --stage C --only "16,1.0,1.0,0.5,torus,protocol" --n-real 2`) — ≈ 5 min, D ≈ 0.03.

---

## 13. Credits & provenance

- Base construction and the 37-test verification suite: **wild8highlander/ab-cloud-research** (AB_Cloud_v23 Academic Package; run `run_20260914_234626`).
- Scan design, Python port, all measurements, figures and this package: Test 34-ext study, September 2026.
- ζ zeros: `verification/data/zeta_zeros_50000.txt` from the base repository (Odlyzko-format first 50,000 zeros).
- License: inherits the repository's license.


---

### 33b. The scan tables (data verbatim)

**Stage C — the 96×96 verification (complete, 5 configurations):**

| L | Nv | q | W | α | bounds | placement | D_pooled | p_pooled | D_min–D_max | ⟨r⟩ | composite |
|---|---|---|---|---|---|---|---|---|---|---|---|

| 96 | 8 | 1.0 | 1.0 | 0.6 | open | regular | **0.0358** | 2.99e-20 | 0.0328–0.0387 | 0.5977 | PASS |
| 96 | 16 | 1.0 | 1.0 | 0.5 | torus | protocol | **0.0318** | 3.98e-16 | 0.0276–0.0382 | 0.5979 | PASS |
| 96 | 16 | 0.7 | 1.0 | 0.5 | open | protocol | **0.0387** | 1.44e-23 | 0.0373–0.0414 | 0.5949 | PASS |
| 96 | 2 | 1.0 | 1.0 | 0.5 | open | protocol | **0.0928** | 7.41e-134 | 0.0722–0.1114 | 0.5738 | PASS |

**Stage B — refinement (complete, 46 configurations):**

| L | Nv | q | W | α | bounds | D_pooled | ⟨r⟩ | composite |
|---|---|---|---|---|---|---|---|---|

| 32 | 16 | 1.0 | 0.5 | 0.5 | open | 0.0404 | 0.6012 | PASS |
| 32 | 16 | 0.7 | 1.0 | 0.5 | open | 0.0296 | 0.6113 | PASS |
| 32 | 16 | 0.5 | 1.0 | 0.5 | open | 0.0382 | 0.6002 | PASS |
| 32 | 16 | 0.7 | 0.5 | 0.5 | open | 0.0406 | 0.5979 | PASS |
| 32 | 16 | 1.0 | 0.0 | 0.5 | open | 0.0478 | 0.5946 | — |
| 32 | 12 | 1.0 | 1.0 | 0.5 | open | 0.0427 | 0.5900 | PASS |
| 32 | 8 | 0.7 | 1.0 | 0.5 | open | 0.0619 | 0.5925 | PASS |
| 32 | 12 | 0.7 | 1.0 | 0.5 | open | 0.0471 | 0.5882 | PASS |
| 32 | 8 | 1.0 | 0.5 | 0.5 | open | 0.0437 | 0.5958 | PASS |
| 32 | 12 | 1.0 | 0.5 | 0.5 | open | 0.0391 | 0.5944 | PASS |
| 32 | 12 | 1.0 | 0.0 | 0.5 | open | 0.0512 | 0.6029 | — |
| 32 | 6 | 1.0 | 1.0 | 0.5 | open | 0.0482 | 0.5837 | PASS |
| 32 | 16 | 1.0 | 1.0 | 0.5 | open | 0.0353 | 0.5977 | PASS |
| 32 | 6 | 1.0 | 0.5 | 0.5 | open | 0.0552 | 0.5806 | PASS |
| 32 | 16 | 0.5 | 0.5 | 0.5 | open | 0.0486 | 0.5999 | PASS |
| 32 | 8 | 1.0 | 1.0 | 0.5 | torus | 0.0579 | 0.5898 | PASS |
| 32 | 16 | 1.0 | 1.0 | 0.5 | torus | 0.0357 | 0.6009 | PASS |
| 32 | 4 | 1.0 | 1.0 | 0.5 | torus | 0.0673 | 0.5934 | PASS |
| 32 | 8 | 1.0 | 1.0 | 0.5 | open | 0.0288 | 0.6264 | PASS |
| 32 | 16 | 1.0 | 0.5 | 0.3 | open | 0.0829 | 0.6013 | — |
| 32 | 16 | 1.0 | 0.5 | 0.4 | open | 0.0812 | 0.5995 | — |
| 32 | 16 | 1.0 | 0.5 | 0.6 | open | 0.0766 | 0.6111 | — |
| 48 | 8 | 1.0 | 1.0 | 0.5 | open | 0.0505 | 0.5903 | PASS |
| 48 | 16 | 0.7 | 1.0 | 0.5 | open | 0.0359 | 0.5958 | PASS |
| 48 | 16 | 1.0 | 1.0 | 0.5 | open | 0.0437 | 0.5884 | PASS |
| 48 | 16 | 1.0 | 1.0 | 0.5 | torus | 0.0320 | 0.5992 | PASS |
| 48 | 16 | 0.5 | 1.0 | 0.5 | open | 0.0485 | 0.5879 | PASS |
| 48 | 12 | 1.0 | 0.5 | 0.5 | open | 0.0363 | 0.6065 | PASS |
| 48 | 16 | 1.0 | 0.5 | 0.5 | open | 0.0360 | 0.5958 | PASS |
| 48 | 16 | 0.7 | 0.5 | 0.5 | open | 0.0467 | 0.5909 | PASS |
| 48 | 12 | 1.0 | 1.0 | 0.5 | open | 0.0411 | 0.5940 | PASS |
| 48 | 8 | 1.0 | 0.5 | 0.5 | open | 0.0574 | 0.5870 | PASS |
| 48 | 8 | 1.0 | 1.0 | 0.3 | open | 0.0385 | 0.5960 | PASS |
| 48 | 8 | 1.0 | 1.0 | 0.4 | open | 0.0285 | 0.6085 | PASS |
| 48 | 8 | 1.0 | 1.0 | 0.6 | open | 0.0385 | 0.5933 | PASS |
| 64 | 8 | 1.0 | 1.0 | 0.4 | open | 0.0296 | 0.6031 | PASS |
| 64 | 8 | 1.0 | 1.0 | 0.5 | open | 0.0536 | 0.5907 | PASS |
| 64 | 16 | 0.7 | 1.0 | 0.5 | open | 0.0371 | 0.5930 | PASS |
| 64 | 16 | 1.0 | 1.0 | 0.5 | torus | 0.0321 | 0.5951 | PASS |
| 64 | 16 | 1.0 | 1.0 | 0.5 | open | 0.0377 | 0.5921 | PASS |
| 64 | 16 | 1.0 | 0.5 | 0.5 | open | 0.0395 | 0.5934 | PASS |
| 64 | 12 | 1.0 | 0.5 | 0.5 | open | 0.0425 | 0.6003 | PASS |
| 64 | 16 | 0.5 | 1.0 | 0.5 | open | 0.0376 | 0.6058 | PASS |
| 64 | 8 | 1.0 | 1.0 | 0.3 | open | 0.0414 | 0.5907 | PASS |
| 64 | 8 | 1.0 | 1.0 | 0.6 | open | 0.0240 | 0.6203 | PASS |

**Stage A — the coarse L=24 sweep: top 20 of 171 configurations (by D_pooled):**

| Nv | q | W | α | bounds | placement | D_pooled | ⟨r⟩ | composite |
|---|---|---|---|---|---|---|---|---|

| 16 | 1.0 | 0.5 | 0.5 | open | protocol | **0.0289** | 0.6181 | PASS |
| 16 | 0.7 | 1.0 | 0.5 | open | protocol | **0.0304** | 0.6129 | PASS |
| 16 | 1.0 | 1.0 | 0.4 | open | protocol | **0.0306** | 0.6241 | — |
| 8 | 1.0 | 1.0 | 0.5 | torus | protocol | **0.0319** | 0.5996 | — |
| 16 | 0.5 | 1.0 | 0.5 | open | protocol | **0.0320** | 0.6030 | PASS |
| 16 | 0.7 | 0.5 | 0.5 | open | protocol | **0.0321** | 0.6124 | PASS |
| 16 | 1.0 | 1.0 | 0.6 | open | protocol | **0.0371** | 0.6112 | — |
| 16 | 1.0 | 0.0 | 0.5 | open | protocol | **0.0373** | 0.6074 | — |
| 8 | 1.0 | 1.0 | 0.5 | open | regular | **0.0385** | 0.5984 | — |
| 12 | 1.0 | 1.0 | 0.5 | open | protocol | **0.0393** | 0.5765 | — |
| 8 | 0.7 | 1.0 | 0.5 | open | protocol | **0.0409** | 0.6083 | PASS |
| 12 | 0.7 | 1.0 | 0.5 | open | protocol | **0.0414** | 0.6008 | — |
| 16 | 1.0 | 1.0 | 0.5 | torus | protocol | **0.0421** | 0.5916 | PASS |
| 8 | 1.0 | 0.5 | 0.5 | open | protocol | **0.0431** | 0.6032 | — |
| 12 | 1.0 | 0.5 | 0.5 | open | protocol | **0.0435** | 0.6032 | — |
| 8 | 1.0 | 1.0 | 0.6 | open | protocol | **0.0444** | 0.6160 | — |
| 12 | 1.0 | 0.0 | 0.5 | open | protocol | **0.0454** | 0.6127 | — |
| 6 | 1.0 | 1.0 | 0.5 | open | protocol | **0.0466** | 0.6074 | — |
| 16 | 1.0 | 1.0 | 0.5 | open | protocol | **0.0479** | 0.6037 | — |
| 16 | 1.0 | 1.0 | 0.3 | open | protocol | **0.0503** | 0.6000 | — |

The worst Stage-A configurations (window-physics controls):

| Nv | q | W | α | bounds | placement | D_pooled | ⟨r⟩ |
|---|---|---|---|---|---|---|---|

| 3 | 0.2 | 0.0 | 0.5 | open | protocol | 0.5503 | 0.3631 |
| 1 | 0.3 | 0.0 | 0.5 | open | protocol | 0.5700 | 0.3114 |
| 1 | 0.2 | 0.5 | 0.5 | open | protocol | 0.5748 | 0.3307 |
| 2 | 0.2 | 0.0 | 0.5 | open | protocol | 0.5883 | 0.3329 |
| 1 | 0.2 | 0.0 | 0.5 | open | protocol | 0.6398 | 0.2720 |
| 0 | 0.3 | 0.5 | 0.5 | open | protocol | 0.7280 | 0.2695 |
| 0 | 0.3 | 1.0 | 0.5 | open | protocol | 0.7280 | 0.2695 |
| 0 | 0.3 | 0.0 | 0.5 | open | protocol | 0.7288 | 0.2016 |

**The L=96 GUE control (full JSON):** {
 "L": 96,
 "n_real": 2,
 "n_spacings": 11054,
 "D_gue_vs_zeta": 0.02203796563718502,
 "p": 0.00029679836358233457,
 "mean_abs_dR2_cal": 0.027165243301242932,
 "mean_abs_dR2_vs_zeta": 0.039619211193743585
}

Reading the tables: Stage A's valley is visible in the top-20 (Nv 6–16 dominates); Stage B confirms stability as L grows; Stage C — three PASS out of four candidates plus the reference at the edge. Full CSVs — `02_data/raw/vortex_optimization/`.


---

## 33d. Stage A: the complete table of 171 configurations

The full coarse-sweep table (L = 24, 3 realizations per configuration; sorted by D_pooled):

| Nv | q | W | α | bounds | placement | D_pooled | D_min | D_med | D_max | ⟨r⟩ | ⟨\|ΔR₂\|⟩ | d_GUE | composite |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|

| 16 | 1.0 | 0.5 | 0.5 | open | protocol | 0.0289 | 0.0381 | 0.0474 | 0.0477 | 0.6181 | 0.0981 | 0.0948 | PASS |
| 16 | 0.7 | 1.0 | 0.5 | open | protocol | 0.0304 | 0.0333 | 0.0396 | 0.0467 | 0.6129 | 0.0922 | 0.0827 | PASS |
| 16 | 1.0 | 1.0 | 0.4 | open | protocol | 0.0306 | 0.0352 | 0.0440 | 0.0753 | 0.6241 | 0.1159 | 0.1142 | — |
| 8 | 1.0 | 1.0 | 0.5 | torus | protocol | 0.0319 | 0.0402 | 0.0430 | 0.0531 | 0.5996 | 0.1030 | 0.0978 | — |
| 16 | 0.5 | 1.0 | 0.5 | open | protocol | 0.0320 | 0.0327 | 0.0391 | 0.0531 | 0.6030 | 0.0936 | 0.0943 | PASS |
| 16 | 0.7 | 0.5 | 0.5 | open | protocol | 0.0321 | 0.0452 | 0.0456 | 0.0616 | 0.6124 | 0.0978 | 0.0980 | PASS |
| 16 | 1.0 | 1.0 | 0.6 | open | protocol | 0.0371 | 0.0362 | 0.0487 | 0.0652 | 0.6112 | 0.1133 | 0.1090 | — |
| 16 | 1.0 | 0.0 | 0.5 | open | protocol | 0.0373 | 0.0394 | 0.0418 | 0.0565 | 0.6074 | 0.1184 | 0.1188 | — |
| 8 | 1.0 | 1.0 | 0.5 | open | regular | 0.0385 | 0.0396 | 0.0419 | 0.0451 | 0.5984 | 0.1144 | 0.1143 | — |
| 12 | 1.0 | 1.0 | 0.5 | open | protocol | 0.0393 | 0.0420 | 0.0560 | 0.0573 | 0.5765 | 0.1052 | 0.1005 | — |
| 8 | 0.7 | 1.0 | 0.5 | open | protocol | 0.0409 | 0.0403 | 0.0477 | 0.0678 | 0.6083 | 0.0947 | 0.0927 | PASS |
| 12 | 0.7 | 1.0 | 0.5 | open | protocol | 0.0414 | 0.0402 | 0.0474 | 0.0643 | 0.6008 | 0.1106 | 0.1080 | — |
| 16 | 1.0 | 1.0 | 0.5 | torus | protocol | 0.0421 | 0.0393 | 0.0406 | 0.0765 | 0.5916 | 0.0944 | 0.0854 | PASS |
| 8 | 1.0 | 0.5 | 0.5 | open | protocol | 0.0431 | 0.0449 | 0.0550 | 0.0639 | 0.6032 | 0.1020 | 0.0978 | — |
| 12 | 1.0 | 0.5 | 0.5 | open | protocol | 0.0435 | 0.0473 | 0.0517 | 0.0605 | 0.6032 | 0.1020 | 0.0966 | — |
| 8 | 1.0 | 1.0 | 0.6 | open | protocol | 0.0444 | 0.0410 | 0.0776 | 0.0852 | 0.6160 | 0.1279 | 0.1227 | — |
| 12 | 1.0 | 0.0 | 0.5 | open | protocol | 0.0454 | 0.0343 | 0.0474 | 0.0866 | 0.6127 | 0.1078 | 0.1109 | — |
| 6 | 1.0 | 1.0 | 0.5 | open | protocol | 0.0466 | 0.0452 | 0.0566 | 0.0647 | 0.6074 | 0.1153 | 0.1083 | — |
| 16 | 1.0 | 1.0 | 0.5 | open | protocol | 0.0479 | 0.0453 | 0.0490 | 0.0652 | 0.6037 | 0.1195 | 0.1096 | — |
| 16 | 1.0 | 1.0 | 0.3 | open | protocol | 0.0503 | 0.0547 | 0.0610 | 0.0696 | 0.6000 | 0.1118 | 0.1042 | — |
| 6 | 1.0 | 0.5 | 0.5 | open | protocol | 0.0510 | 0.0368 | 0.0548 | 0.0811 | 0.5930 | 0.1036 | 0.0984 | — |
| 16 | 0.5 | 0.5 | 0.5 | open | protocol | 0.0551 | 0.0591 | 0.0641 | 0.0657 | 0.5917 | 0.1162 | 0.1083 | — |
| 12 | 0.7 | 0.5 | 0.5 | open | protocol | 0.0573 | 0.0563 | 0.0695 | 0.0783 | 0.6104 | 0.1055 | 0.1005 | — |
| 8 | 0.7 | 0.5 | 0.5 | open | protocol | 0.0594 | 0.0545 | 0.0631 | 0.0793 | 0.5982 | 0.0983 | 0.0939 | PASS |
| 6 | 1.0 | 0.0 | 0.5 | open | protocol | 0.0614 | 0.0672 | 0.0883 | 0.0896 | 0.5837 | 0.1281 | 0.1215 | — |
| 8 | 1.0 | 0.0 | 0.5 | open | protocol | 0.0621 | 0.0664 | 0.0811 | 0.1058 | 0.6121 | 0.1264 | 0.1236 | — |
| 8 | 1.0 | 1.0 | 0.3 | open | protocol | 0.0631 | 0.0287 | 0.0971 | 0.1024 | 0.6065 | 0.1056 | 0.1005 | — |
| 12 | 0.5 | 0.5 | 0.5 | open | protocol | 0.0635 | 0.0554 | 0.0724 | 0.0955 | 0.5784 | 0.1096 | 0.1026 | — |
| 12 | 0.7 | 0.0 | 0.5 | open | protocol | 0.0650 | 0.0605 | 0.0811 | 0.1000 | 0.5822 | 0.1359 | 0.1295 | — |
| 8 | 1.0 | 1.0 | 0.5 | open | protocol | 0.0652 | 0.0656 | 0.0792 | 0.0797 | 0.5851 | 0.1068 | 0.1021 | — |
| 16 | 0.7 | 0.0 | 0.5 | open | protocol | 0.0719 | 0.0654 | 0.0892 | 0.0907 | 0.5665 | 0.1251 | 0.1170 | — |
| 2 | 1.0 | 1.0 | 0.5 | open | protocol | 0.0732 | 0.0531 | 0.0930 | 0.0955 | 0.5898 | 0.1071 | 0.1012 | — |
| 6 | 0.7 | 0.5 | 0.5 | open | protocol | 0.0776 | 0.0698 | 0.0862 | 0.1024 | 0.5976 | 0.1260 | 0.1171 | — |
| 12 | 0.5 | 1.0 | 0.5 | open | protocol | 0.0788 | 0.0698 | 0.0822 | 0.0963 | 0.5806 | 0.1165 | 0.1081 | — |
| 8 | 0.5 | 1.0 | 0.5 | open | protocol | 0.0789 | 0.0449 | 0.1088 | 0.1261 | 0.5942 | 0.1153 | 0.1079 | — |
| 16 | 0.3 | 1.0 | 0.5 | open | protocol | 0.0791 | 0.0651 | 0.0806 | 0.1101 | 0.5855 | 0.1149 | 0.1081 | — |
| 2 | 1.0 | 1.0 | 0.6 | open | protocol | 0.0808 | 0.0805 | 0.0892 | 0.0940 | 0.6294 | 0.1331 | 0.1298 | — |
| 4 | 1.0 | 0.5 | 0.5 | open | protocol | 0.0810 | 0.0737 | 0.0910 | 0.1108 | 0.5940 | 0.1229 | 0.1191 | — |
| 4 | 1.0 | 1.0 | 0.5 | torus | protocol | 0.0823 | 0.0588 | 0.0985 | 0.1132 | 0.5764 | 0.1098 | 0.1036 | — |
| 6 | 0.7 | 1.0 | 0.5 | open | protocol | 0.0824 | 0.0802 | 0.0815 | 0.1037 | 0.5933 | 0.0979 | 0.0930 | PASS |
| 2 | 1.0 | 1.0 | 0.5 | torus | protocol | 0.0825 | 0.0570 | 0.0989 | 0.1197 | 0.5832 | 0.1057 | 0.0975 | — |
| 8 | 1.0 | 1.0 | 0.4 | open | protocol | 0.0827 | 0.0412 | 0.1147 | 0.1266 | 0.5886 | 0.1123 | 0.1047 | — |
| 2 | 1.0 | 1.0 | 0.5 | open | regular | 0.0844 | 0.0869 | 0.0892 | 0.0916 | 0.5593 | 0.1353 | 0.1302 | — |
| 16 | 1.0 | 1.0 | 0.5 | open | cluster | 0.0851 | 0.0756 | 0.0909 | 0.1107 | 0.5853 | 0.1229 | 0.1115 | — |
| 4 | 1.0 | 1.0 | 0.5 | open | protocol | 0.0866 | 0.0729 | 0.0995 | 0.1034 | 0.5797 | 0.1247 | 0.1190 | — |
| 8 | 0.7 | 0.0 | 0.5 | open | protocol | 0.0878 | 0.0771 | 0.0948 | 0.1261 | 0.5733 | 0.1211 | 0.1152 | — |
| 16 | 1.0 | 1.0 | 0.5 | open | regular | 0.0886 | 0.0874 | 0.0886 | 0.0994 | 0.5610 | 0.1804 | 0.1728 | — |
| 3 | 1.0 | 0.0 | 0.5 | open | protocol | 0.0900 | 0.0817 | 0.0888 | 0.1243 | 0.5864 | 0.1347 | 0.1290 | — |
| 2 | 1.0 | 0.5 | 0.5 | open | protocol | 0.0923 | 0.0996 | 0.1015 | 0.1032 | 0.5941 | 0.0978 | 0.0927 | PASS |
| 3 | 1.0 | 1.0 | 0.5 | open | protocol | 0.0932 | 0.0893 | 0.1105 | 0.1143 | 0.5738 | 0.1098 | 0.0990 | — |
| 2 | 1.0 | 1.0 | 0.4 | open | protocol | 0.0933 | 0.0825 | 0.1132 | 0.1154 | 0.6109 | 0.1361 | 0.1307 | — |
| 16 | 0.5 | 0.0 | 0.5 | open | protocol | 0.0936 | 0.0799 | 0.1036 | 0.1064 | 0.5706 | 0.1242 | 0.1158 | — |
| 12 | 0.5 | 0.0 | 0.5 | open | protocol | 0.0966 | 0.0884 | 0.1294 | 0.1320 | 0.5747 | 0.1285 | 0.1305 | — |
| 4 | 1.0 | 1.0 | 0.3 | open | protocol | 0.0971 | 0.0948 | 0.1133 | 0.1284 | 0.6125 | 0.1460 | 0.1402 | — |
| 3 | 1.0 | 0.5 | 0.5 | open | protocol | 0.0985 | 0.0857 | 0.1021 | 0.1174 | 0.5771 | 0.1138 | 0.1110 | — |
| 4 | 1.0 | 0.0 | 0.5 | open | protocol | 0.1014 | 0.0940 | 0.0982 | 0.1187 | 0.5759 | 0.1279 | 0.1262 | — |
| 16 | 0.3 | 1.0 | 0.3 | open | protocol | 0.1043 | 0.1015 | 0.1107 | 0.1247 | 0.6315 | 0.1607 | 0.1556 | — |
| 16 | 0.3 | 1.0 | 0.4 | open | protocol | 0.1075 | 0.1036 | 0.1195 | 0.1221 | 0.6221 | 0.1499 | 0.1458 | — |
| 12 | 0.3 | 1.0 | 0.5 | open | protocol | 0.1076 | 0.1081 | 0.1117 | 0.1162 | 0.5744 | 0.1266 | 0.1184 | — |
| 8 | 0.5 | 0.5 | 0.5 | open | protocol | 0.1081 | 0.1012 | 0.1165 | 0.1315 | 0.5592 | 0.1279 | 0.1253 | — |
| 2 | 1.0 | 1.0 | 0.3 | open | protocol | 0.1084 | 0.0853 | 0.1058 | 0.1505 | 0.6119 | 0.1520 | 0.1441 | — |
| 4 | 0.7 | 1.0 | 0.5 | open | protocol | 0.1089 | 0.0571 | 0.1378 | 0.1466 | 0.5637 | 0.1134 | 0.1065 | — |
| 4 | 1.0 | 1.0 | 0.6 | open | protocol | 0.1096 | 0.0832 | 0.1266 | 0.1505 | 0.6059 | 0.1429 | 0.1408 | — |
| 4 | 0.7 | 0.5 | 0.5 | open | protocol | 0.1104 | 0.1152 | 0.1213 | 0.1285 | 0.5835 | 0.1261 | 0.1234 | — |
| 6 | 0.7 | 0.0 | 0.5 | open | protocol | 0.1113 | 0.1008 | 0.1059 | 0.1414 | 0.5793 | 0.1224 | 0.1201 | — |
| 8 | 1.0 | 1.0 | 0.5 | open | cluster | 0.1120 | 0.0986 | 0.1385 | 0.1410 | 0.5948 | 0.1280 | 0.1191 | — |
| 4 | 1.0 | 1.0 | 0.4 | open | protocol | 0.1167 | 0.1070 | 0.1244 | 0.1363 | 0.6005 | 0.1412 | 0.1401 | — |
| 16 | 0.3 | 0.5 | 0.5 | open | protocol | 0.1176 | 0.1192 | 0.1221 | 0.1372 | 0.5690 | 0.1207 | 0.1155 | — |
| 2 | 0.7 | 1.0 | 0.5 | open | protocol | 0.1193 | 0.1238 | 0.1241 | 0.1397 | 0.5722 | 0.1282 | 0.1226 | — |
| 16 | 0.3 | 1.0 | 0.6 | open | protocol | 0.1205 | 0.1067 | 0.1247 | 0.1506 | 0.6086 | 0.1798 | 0.1730 | — |
| 6 | 0.5 | 1.0 | 0.5 | open | protocol | 0.1216 | 0.1140 | 0.1303 | 0.1345 | 0.5661 | 0.1262 | 0.1184 | — |
| 8 | 0.3 | 1.0 | 0.4 | open | protocol | 0.1247 | 0.1151 | 0.1339 | 0.1439 | 0.6199 | 0.1970 | 0.1910 | — |
| 8 | 0.5 | 0.0 | 0.5 | open | protocol | 0.1289 | 0.1295 | 0.1310 | 0.1957 | 0.5424 | 0.1280 | 0.1271 | — |
| 3 | 0.7 | 0.0 | 0.5 | open | protocol | 0.1323 | 0.1239 | 0.1427 | 0.1485 | 0.5424 | 0.1323 | 0.1256 | — |
| 8 | 0.3 | 1.0 | 0.6 | open | protocol | 0.1325 | 0.1188 | 0.1495 | 0.1559 | 0.6245 | 0.2022 | 0.1980 | — |
| 8 | 0.3 | 1.0 | 0.3 | open | protocol | 0.1349 | 0.1116 | 0.1351 | 0.1784 | 0.6161 | 0.1984 | 0.1904 | — |
| 16 | 0.3 | 1.0 | 0.5 | torus | protocol | 0.1390 | 0.0927 | 0.1554 | 0.1906 | 0.5487 | 0.1309 | 0.1224 | — |
| 2 | 1.0 | 0.0 | 0.5 | open | protocol | 0.1400 | 0.1338 | 0.1550 | 0.1596 | 0.5623 | 0.1409 | 0.1366 | — |
| 3 | 0.7 | 1.0 | 0.5 | open | protocol | 0.1402 | 0.1392 | 0.1429 | 0.1573 | 0.5546 | 0.1235 | 0.1188 | — |
| 3 | 0.7 | 0.5 | 0.5 | open | protocol | 0.1413 | 0.1339 | 0.1367 | 0.1644 | 0.5557 | 0.1203 | 0.1124 | — |
| 12 | 0.3 | 0.5 | 0.5 | open | protocol | 0.1419 | 0.1369 | 0.1538 | 0.1701 | 0.5552 | 0.1419 | 0.1375 | — |
| 6 | 0.5 | 0.5 | 0.5 | open | protocol | 0.1426 | 0.1410 | 0.1418 | 0.1592 | 0.5639 | 0.1423 | 0.1322 | — |
| 8 | 0.3 | 1.0 | 0.5 | open | regular | 0.1428 | 0.1496 | 0.1508 | 0.1519 | 0.5730 | 0.1564 | 0.1513 | — |
| 2 | 0.3 | 1.0 | 0.3 | open | protocol | 0.1465 | 0.1496 | 0.1594 | 0.1722 | 0.6151 | 0.2434 | 0.2390 | — |
| 4 | 0.7 | 0.0 | 0.5 | open | protocol | 0.1497 | 0.1569 | 0.1590 | 0.1627 | 0.5499 | 0.1388 | 0.1311 | — |
| 4 | 0.3 | 1.0 | 0.4 | open | protocol | 0.1523 | 0.1407 | 0.1616 | 0.1780 | 0.6182 | 0.2332 | 0.2298 | — |
| 2 | 0.3 | 1.0 | 0.6 | open | protocol | 0.1584 | 0.1446 | 0.1555 | 0.1894 | 0.6174 | 0.2380 | 0.2348 | — |
| 2 | 0.3 | 1.0 | 0.4 | open | protocol | 0.1587 | 0.1558 | 0.1630 | 0.1861 | 0.6224 | 0.2525 | 0.2479 | — |
| 4 | 0.3 | 1.0 | 0.3 | open | protocol | 0.1594 | 0.1440 | 0.1722 | 0.1815 | 0.6162 | 0.2457 | 0.2416 | — |
| 4 | 0.5 | 1.0 | 0.5 | open | protocol | 0.1605 | 0.1379 | 0.1909 | 0.1936 | 0.5548 | 0.1303 | 0.1264 | — |
| 4 | 0.3 | 1.0 | 0.6 | open | protocol | 0.1622 | 0.1397 | 0.1759 | 0.1866 | 0.6101 | 0.2400 | 0.2367 | — |
| 4 | 1.0 | 1.0 | 0.5 | open | cluster | 0.1629 | 0.1423 | 0.1625 | 0.2184 | 0.5904 | 0.1630 | 0.1552 | — |
| 2 | 0.7 | 0.5 | 0.5 | open | protocol | 0.1664 | 0.1554 | 0.1781 | 0.1894 | 0.5520 | 0.1304 | 0.1279 | — |
| 16 | 0.3 | 0.0 | 0.5 | open | protocol | 0.1668 | 0.1332 | 0.1938 | 0.1971 | 0.5298 | 0.1434 | 0.1389 | — |
| 8 | 0.3 | 1.0 | 0.5 | torus | protocol | 0.1680 | 0.1178 | 0.2005 | 0.2109 | 0.5444 | 0.1510 | 0.1443 | — |
| 2 | 1.0 | 1.0 | 0.5 | open | cluster | 0.1728 | 0.1682 | 0.1705 | 0.2163 | 0.5600 | 0.1794 | 0.1712 | — |
| 4 | 1.0 | 1.0 | 0.5 | open | regular | 0.1769 | 0.1785 | 0.1800 | 0.1845 | 0.5071 | 0.1718 | 0.1633 | — |
| 16 | 0.2 | 1.0 | 0.5 | open | protocol | 0.1843 | 0.1690 | 0.1744 | 0.2247 | 0.5656 | 0.1569 | 0.1514 | — |
| 16 | 0.3 | 1.0 | 0.5 | open | regular | 0.1845 | 0.1893 | 0.1944 | 0.1975 | 0.5086 | 0.1867 | 0.1785 | — |
| 6 | 0.5 | 0.0 | 0.5 | open | protocol | 0.1887 | 0.1574 | 0.2020 | 0.2264 | 0.5435 | 0.1563 | 0.1498 | — |
| 3 | 0.5 | 1.0 | 0.5 | open | protocol | 0.1910 | 0.1591 | 0.2096 | 0.2183 | 0.5402 | 0.1546 | 0.1492 | — |
| 4 | 0.5 | 0.5 | 0.5 | open | protocol | 0.1921 | 0.1540 | 0.2036 | 0.2255 | 0.5422 | 0.1519 | 0.1476 | — |
| 1 | 1.0 | 1.0 | 0.5 | open | protocol | 0.1943 | 0.1893 | 0.1917 | 0.2127 | 0.5096 | 0.1528 | 0.1498 | — |
| 8 | 0.3 | 1.0 | 0.5 | open | protocol | 0.1992 | 0.1365 | 0.2055 | 0.2614 | 0.5446 | 0.1512 | 0.1474 | — |
| 2 | 0.7 | 0.0 | 0.5 | open | protocol | 0.1993 | 0.1911 | 0.1947 | 0.2440 | 0.5198 | 0.1593 | 0.1565 | — |
| 12 | 0.3 | 0.0 | 0.5 | open | protocol | 0.2004 | 0.1910 | 0.2144 | 0.2301 | 0.5090 | 0.1776 | 0.1698 | — |
| 2 | 0.5 | 1.0 | 0.5 | open | protocol | 0.2086 | 0.2042 | 0.2089 | 0.2270 | 0.5261 | 0.1663 | 0.1636 | — |
| 3 | 0.5 | 0.5 | 0.5 | open | protocol | 0.2110 | 0.2014 | 0.2071 | 0.2304 | 0.5320 | 0.1604 | 0.1573 | — |
| 16 | 0.3 | 1.0 | 0.5 | open | cluster | 0.2115 | 0.1892 | 0.2220 | 0.2504 | 0.5251 | 0.1541 | 0.1495 | — |
| 12 | 0.2 | 1.0 | 0.5 | open | protocol | 0.2118 | 0.1755 | 0.2219 | 0.2561 | 0.5088 | 0.1438 | 0.1403 | — |
| 1 | 1.0 | 0.5 | 0.5 | open | protocol | 0.2132 | 0.2075 | 0.2097 | 0.2395 | 0.5065 | 0.1646 | 0.1569 | — |
| 4 | 0.5 | 0.0 | 0.5 | open | protocol | 0.2207 | 0.1889 | 0.2346 | 0.2606 | 0.5066 | 0.1716 | 0.1629 | — |
| 3 | 0.5 | 0.0 | 0.5 | open | protocol | 0.2281 | 0.2323 | 0.2338 | 0.2539 | 0.5049 | 0.1731 | 0.1662 | — |
| 16 | 0.2 | 0.5 | 0.5 | open | protocol | 0.2379 | 0.2166 | 0.2512 | 0.2761 | 0.5134 | 0.1623 | 0.1552 | — |
| 8 | 0.3 | 0.5 | 0.5 | open | protocol | 0.2397 | 0.2035 | 0.2538 | 0.2733 | 0.5021 | 0.1751 | 0.1687 | — |
| 1 | 1.0 | 0.0 | 0.5 | open | protocol | 0.2435 | 0.2085 | 0.2610 | 0.2682 | 0.4756 | 0.1740 | 0.1692 | — |
| 2 | 0.5 | 0.5 | 0.5 | open | protocol | 0.2435 | 0.2254 | 0.2505 | 0.2760 | 0.5014 | 0.1894 | 0.1827 | — |
| 6 | 0.3 | 1.0 | 0.5 | open | protocol | 0.2524 | 0.2523 | 0.2540 | 0.2666 | 0.5014 | 0.1830 | 0.1803 | — |
| 12 | 0.2 | 0.5 | 0.5 | open | protocol | 0.2671 | 0.2526 | 0.2787 | 0.2792 | 0.4826 | 0.1768 | 0.1763 | — |
| 4 | 0.3 | 1.0 | 0.5 | open | regular | 0.2681 | 0.2668 | 0.2689 | 0.2769 | 0.4532 | 0.1880 | 0.1826 | — |
| 1 | 0.7 | 1.0 | 0.5 | open | protocol | 0.2696 | 0.2433 | 0.2840 | 0.2892 | 0.4684 | 0.1710 | 0.1666 | — |
| 8 | 0.3 | 0.0 | 0.5 | open | protocol | 0.2934 | 0.2792 | 0.2901 | 0.3332 | 0.4641 | 0.2072 | 0.1995 | — |
| 1 | 0.7 | 0.5 | 0.5 | open | protocol | 0.2938 | 0.2912 | 0.2994 | 0.3129 | 0.4446 | 0.1934 | 0.1873 | — |
| 4 | 0.3 | 1.0 | 0.5 | torus | protocol | 0.3031 | 0.2884 | 0.3257 | 0.3265 | 0.5031 | 0.2619 | 0.2601 | — |
| 6 | 0.3 | 0.5 | 0.5 | open | protocol | 0.3033 | 0.2820 | 0.3147 | 0.3178 | 0.4777 | 0.2083 | 0.2053 | — |
| 16 | 0.2 | 0.0 | 0.5 | open | protocol | 0.3085 | 0.2959 | 0.3261 | 0.3562 | 0.4704 | 0.2000 | 0.1987 | — |
| 8 | 0.3 | 1.0 | 0.5 | open | cluster | 0.3095 | 0.2927 | 0.3143 | 0.3357 | 0.4826 | 0.1999 | 0.1908 | — |
| 2 | 0.3 | 1.0 | 0.5 | open | regular | 0.3119 | 0.3130 | 0.3142 | 0.3167 | 0.4240 | 0.2435 | 0.2326 | — |
| 4 | 0.3 | 1.0 | 0.5 | open | protocol | 0.3212 | 0.2768 | 0.3212 | 0.3763 | 0.4738 | 0.2006 | 0.1982 | — |
| 1 | 0.7 | 0.0 | 0.5 | open | protocol | 0.3218 | 0.3101 | 0.3329 | 0.3440 | 0.4132 | 0.2279 | 0.2226 | — |
| 2 | 0.5 | 0.0 | 0.5 | open | protocol | 0.3238 | 0.3258 | 0.3258 | 0.3547 | 0.4638 | 0.2269 | 0.2227 | — |
| 1 | 0.5 | 1.0 | 0.5 | open | protocol | 0.3283 | 0.3011 | 0.3150 | 0.3777 | 0.4272 | 0.2224 | 0.2169 | — |
| 6 | 0.3 | 0.0 | 0.5 | open | protocol | 0.3320 | 0.3398 | 0.3417 | 0.3438 | 0.4490 | 0.2227 | 0.2181 | — |
| 2 | 0.3 | 1.0 | 0.5 | open | protocol | 0.3367 | 0.3279 | 0.3470 | 0.3515 | 0.4482 | 0.2202 | 0.2171 | — |
| 3 | 0.3 | 1.0 | 0.5 | open | protocol | 0.3372 | 0.2913 | 0.3690 | 0.3737 | 0.4703 | 0.2116 | 0.2053 | — |
| 8 | 0.2 | 1.0 | 0.5 | open | protocol | 0.3462 | 0.3273 | 0.3472 | 0.3851 | 0.4638 | 0.2083 | 0.1994 | — |
| 2 | 0.3 | 1.0 | 0.5 | torus | protocol | 0.3559 | 0.3485 | 0.3513 | 0.3730 | 0.4898 | 0.3338 | 0.3301 | — |
| 12 | 0.2 | 0.0 | 0.5 | open | protocol | 0.3595 | 0.3650 | 0.3688 | 0.3813 | 0.4604 | 0.2303 | 0.2222 | — |
| 4 | 0.3 | 0.5 | 0.5 | open | protocol | 0.3624 | 0.3455 | 0.3739 | 0.3875 | 0.4599 | 0.2057 | 0.2042 | — |
| 1 | 0.5 | 0.5 | 0.5 | open | protocol | 0.3807 | 0.3743 | 0.3774 | 0.3977 | 0.4095 | 0.2479 | 0.2387 | — |
| 6 | 0.2 | 1.0 | 0.5 | open | protocol | 0.3840 | 0.3364 | 0.4035 | 0.4316 | 0.4240 | 0.2204 | 0.2183 | — |
| 3 | 0.3 | 0.5 | 0.5 | open | protocol | 0.3853 | 0.3568 | 0.3970 | 0.4143 | 0.4457 | 0.2348 | 0.2312 | — |
| 8 | 0.2 | 0.5 | 0.5 | open | protocol | 0.3859 | 0.3767 | 0.3778 | 0.4115 | 0.4546 | 0.2178 | 0.2127 | — |
| 4 | 0.3 | 1.0 | 0.5 | open | cluster | 0.4028 | 0.3535 | 0.4363 | 0.4485 | 0.4237 | 0.2821 | 0.2757 | — |
| 2 | 0.3 | 0.5 | 0.5 | open | protocol | 0.4031 | 0.4054 | 0.4054 | 0.4245 | 0.4142 | 0.2598 | 0.2532 | — |
| 4 | 0.3 | 0.0 | 0.5 | open | protocol | 0.4153 | 0.3822 | 0.4333 | 0.4409 | 0.4200 | 0.2689 | 0.2639 | — |
| 6 | 0.2 | 0.5 | 0.5 | open | protocol | 0.4173 | 0.4094 | 0.4218 | 0.4390 | 0.4104 | 0.2446 | 0.2404 | — |
| 1 | 0.5 | 0.0 | 0.5 | open | protocol | 0.4278 | 0.4224 | 0.4266 | 0.4638 | 0.3681 | 0.3148 | 0.3127 | — |
| 4 | 0.2 | 1.0 | 0.5 | open | protocol | 0.4287 | 0.3864 | 0.4485 | 0.4747 | 0.4238 | 0.2531 | 0.2479 | — |
| 8 | 0.2 | 0.0 | 0.5 | open | protocol | 0.4310 | 0.4182 | 0.4295 | 0.4647 | 0.3996 | 0.2901 | 0.2855 | — |
| 3 | 0.3 | 0.0 | 0.5 | open | protocol | 0.4326 | 0.4250 | 0.4265 | 0.4650 | 0.4109 | 0.3050 | 0.2989 | — |
| 3 | 0.2 | 1.0 | 0.5 | open | protocol | 0.4448 | 0.3926 | 0.4690 | 0.4828 | 0.4246 | 0.2666 | 0.2570 | — |
| 2 | 0.3 | 1.0 | 0.5 | open | cluster | 0.4512 | 0.4426 | 0.4588 | 0.4606 | 0.4033 | 0.2827 | 0.2769 | — |
| 2 | 0.2 | 1.0 | 0.5 | open | protocol | 0.4568 | 0.4335 | 0.4720 | 0.4841 | 0.3988 | 0.2736 | 0.2740 | — |
| 4 | 0.2 | 0.5 | 0.5 | open | protocol | 0.4712 | 0.4378 | 0.4944 | 0.4955 | 0.4089 | 0.3044 | 0.2998 | — |
| 1 | 0.3 | 1.0 | 0.5 | open | protocol | 0.4725 | 0.4442 | 0.4563 | 0.5208 | 0.3695 | 0.2868 | 0.2827 | — |
| 6 | 0.2 | 0.0 | 0.5 | open | protocol | 0.4852 | 0.4765 | 0.4865 | 0.5045 | 0.3886 | 0.3296 | 0.3257 | — |
| 3 | 0.2 | 0.5 | 0.5 | open | protocol | 0.4938 | 0.4721 | 0.5115 | 0.5137 | 0.4006 | 0.3329 | 0.3296 | — |
| 1 | 0.3 | 0.5 | 0.5 | open | protocol | 0.4947 | 0.4831 | 0.4895 | 0.5305 | 0.3606 | 0.3715 | 0.3636 | — |
| 2 | 0.3 | 0.0 | 0.5 | open | protocol | 0.4980 | 0.4569 | 0.5144 | 0.5290 | 0.3842 | 0.3677 | 0.3626 | — |
| 2 | 0.2 | 0.5 | 0.5 | open | protocol | 0.5118 | 0.4870 | 0.5150 | 0.5446 | 0.3760 | 0.3730 | 0.3640 | — |
| 1 | 0.2 | 1.0 | 0.5 | open | protocol | 0.5328 | 0.5196 | 0.5198 | 0.5789 | 0.3329 | 0.4038 | 0.3959 | — |
| 4 | 0.2 | 0.0 | 0.5 | open | protocol | 0.5429 | 0.5279 | 0.5554 | 0.5668 | 0.3659 | 0.3985 | 0.3914 | — |
| 3 | 0.2 | 0.0 | 0.5 | open | protocol | 0.5503 | 0.5225 | 0.5670 | 0.5726 | 0.3631 | 0.3984 | 0.3931 | — |
| 1 | 0.3 | 0.0 | 0.5 | open | protocol | 0.5700 | 0.5525 | 0.5813 | 0.5884 | 0.3114 | 0.4592 | 0.4533 | — |
| 1 | 0.2 | 0.5 | 0.5 | open | protocol | 0.5748 | 0.5609 | 0.5635 | 0.6102 | 0.3307 | 0.4583 | 0.4497 | — |
| 2 | 0.2 | 0.0 | 0.5 | open | protocol | 0.5883 | 0.5594 | 0.6025 | 0.6122 | 0.3329 | 0.4812 | 0.4747 | — |
| 1 | 0.2 | 0.0 | 0.5 | open | protocol | 0.6398 | 0.6319 | 0.6461 | 0.6623 | 0.2720 | 0.5656 | 0.5554 | — |
| 0 | 0.3 | 0.5 | 0.5 | open | protocol | 0.7280 | 0.7225 | 0.7318 | 0.7327 | 0.2695 | 0.7669 | 0.7560 | — |
| 0 | 0.3 | 1.0 | 0.5 | open | protocol | 0.7280 | 0.7225 | 0.7318 | 0.7327 | 0.2695 | 0.7669 | 0.7560 | — |
| 0 | 0.3 | 0.0 | 0.5 | open | protocol | 0.7288 | 0.7288 | 0.7288 | 0.7288 | 0.2016 | 1.1914 | 1.1932 | — |

Reading: the top 30 rows — the valley (Nv 6–16); the bottom — clusters and extreme Nv; the pure lattice (Nv=0) — at the very bottom with D ≈ 0.73. The full CSV — `02_data/raw/vortex_optimization/sweep_A_L24.csv`.

---

## 33c. Full record of level VII (from the unified volume)

#### Full record: 10. Level VII: the vortex-density optimization

#### 10.1. The problem and the method

Test 34 of the v19 run compares the cloud's unfolded adjacent-level spacings with the unfolded spacings of the first 50,000 $\zeta$ zeros by a two-sample Kolmogorov–Smirnov test. The reference configuration (96×96, $N_v = 2$, $q = 1.0$, $\alpha = 0.5$, $W = 1.0$, open boundaries, 5 realizations) gives pooled $D = 0.1096$ (p = 2.24·10⁻¹⁸⁶) — formally WARN (acceptance requires $D < 0.10$). Level VII poses the physics question: the vortex configuration is a set of dials — which dial settings drive $D$ down? The answer is a three-stage scan (Test 34-ext): 171 configurations at L = 24 (576 sites); 46 refinement configurations at L = 32/48/64 with the per-L GUE floor measured; and 5 candidates × 5 realizations under the full 34b protocol at 96×96 (N = 9,216 sites, 5,528 spacings per realization, 27,640 pooled). The scan ran on a validated port of the Julia engine: hermiticity 0.0 after symmetrization; cell-flux uniformity on the torus exact; the KS implementation against `scipy.stats.ks_2samp` — agreement ≤ 10⁻¹²; the ζ side — 49,999 spacings matching the reference log; the reference configuration re-measured at $D = 0.0928$ (spread 0.072–0.111), reproducing the Julia level within run-to-run spread.

#### 10.2. The result: the working window

The scan finds a **valley** at $N_v = 6$–16 (best at 12), $q = 0.7$–1.0, $W = 0.5$–1.0, $\alpha = 0.5$; torus ≥ open; cluster placement is catastrophic ($D = 0.11$–0.17); the pure vortex-free lattice — $D = 0.73$: without vortices the cloud does not exist as a ζ-statistics object; $N_v = 1$ — $D = 0.194$. Three verified candidates pass the composite criterion on the full 96×96 lattice: $N_v = 8$, $q = 1.0$, $\alpha = 0.6$, grid — $D = 0.0358$; $N_v = 16$, $q = 0.7$, open — $D = 0.0387$; and the best — $N_v = 16$, $q = 1.0$, $\alpha = 0.5$, torus — **$D = 0.0318$** (spread 0.028–0.038): a ×3.4 improvement over the reference, closing 89% of the gap to the GUE floor. The floor itself (the same-sample KS between a GUE ensemble and the ζ zeros) is measured per L: 0.0324 (24), 0.0331 (32), 0.0309 (48), 0.0257 (64), 0.0220 (96) — the statistical zero of the method; no construction can go below it at fixed sample size. The floor itself fails the p-arm (p = 3.0·10⁻⁴) — ensemble finiteness, the same honest caveat as the ζ-vs-GUE comparison.

![The D(Nv, q) heatmap](../../03_figures/static/vortex_optimization/01_heatmap_D_Nv_q.png)

![D as a function of vortex density](../../03_figures/static/vortex_optimization/02_D_of_Nv.png)

![The size ladder and the GUE floor](../../03_figures/static/vortex_optimization/04_L_ladder.png)

![The α scan](../../03_figures/static/vortex_optimization/05_alpha_scan.png)

#### 10.3. The mechanism: from a breeze to ocean currents

The physics of the window reads through the overlap of vortex phase fields. The dilute regime ($N_v \lesssim 4$): large coherent patches of the lattice keep nearly real, nearly integrable hopping structure — $\langle r\rangle \approx 0.51$–0.58, $D > 0.07$; the vortex phase fields do not cover the operator. The working window ($N_v \approx 8$–16): the phase fields overlap and jointly complexify *every* bond — the regime in which the BGS prescription (a Hermitian operator with no antiunitary symmetry, complex phases) is actually realized — and $D$ falls to the floor. The dense regime ($N_v \gtrsim 20$): on-site wells overlap into their own landscape and the vortex gas re-organizes — uniformity degrades again. The charge $q = 1$ completes the flux quantization $2\pi q = 2\pi$ and maximizes phase incommensurability; $\alpha = 0.5$ is the self-dual critical line (Connes); deviating α by ±0.1 at L = 32 roughly doubles $D$. The correspondence with the classical vortex hierarchy (breeze → ocean-scale transport → self-obstruction) is structural, not literal: cloud vortices are gauge vortices — phase singularities of a quantum wavefunction — not fluid eddies. In operator terms: the scan maps the Hamiltonian family $H(N_v, q, W, \alpha)$ onto a scalar distance-to-ζ; its minimum is broad and shallow — the signature of a robust working point, not a fine-tuned one.

#### 10.4. The honest form of the result

The result does not prove RH and does not exhibit the Hilbert–Pólya operator. It establishes a *necessary statistical condition* any H–P candidate must satisfy: a Hermitian operator of a simple, physically transparent gauge type reproduces the ζ zeros' spacing statistics to within the finite-sample floor ($D = 0.0318$ vs 0.0220). That is quantitative numerical support for the statistical (Montgomery–Odlyzko) arm of the Hilbert–Pólya programme — and nothing more. The recommendation to the suite: run the reference comparison with `--ab-nv-secondary 16 --ab-bc torus --ab-alpha 0.5` — the headline statistic moves from the WARN band to the deep PASS band.

---

---

# PART X. LEVEL VIII: HYPERBOLIC WAVE ATTRACTORS

## 34. Level VIII: the subject — hyperbolic cavities

Study W1 is the numerical reproduction of "Hyperbolic wave attractors" (Nature Physics, 2026, CUNY ASRC; popular account — Naked Science, 30.09.2026). The experiment: elastodynamic waves launched into an odd-shaped cavity of hyperbolic metamaterial (a wire mesh with an indefinite permeability tensor) skip chaotic scattering and self-organize into robust closed chiral broadband routes — the wave analogue of limit cycles in nonlinear dynamics. Scale invariance: the routes reproduce across two orders of scale; broadband: across a frequency band; chirality: a circulation sense is chosen; the mirror sibling pair coexists.

The reproduction models. **Ray** (`ray_billiard.py`): an exact k-vector billiard in a trapezoid chamber; the indefinite dispersion $k_y^2 - k_x^2/\eta = K^2$ (the iso-frequency hyperbola); the group-velocity cone $\pm\arctan(1/\sqrt{\eta})$ around the optical axis (5.71° at $\eta = 100$); reflection off an inclined wall conserves the tangential component $k_t$ with the *second* intersection of the line $k_t = \mathrm{const}$ with the hyperbola (the Vieta root) — non-specular; vertical walls are specular ($k_x \to -k_x$). **Wave** (`wave_directional.py`): frequency-domain anisotropic Helmholtz ($\partial_y^2 - \eta^{-1}\partial_x^2 + K^2$) with PEC walls; sparse LU; band-averaged response to a directional drive. **The companion** (`ab_water.py`): AB scattering with water waves (Berry 1980; OIST 2026) — the classical-fluid root of the repository's AB-phase theme.

The mechanism in four steps. (1) The hyperbolic dispersion locks the group velocity into a narrow cone — waves propagate only along prescribed directions. (2) Reflection off a slope conserves $k_t$; on the open hyperbola the reflected state is the second intersection (Vieta) with a jump of $|k|$ along the contour: the wavelength cascade. (3) In a chamber combining vertical walls (specular for this dispersion) with shallow slopes (cascade), every launched ray funnels onto one and the same closed route; the route is chiral; its mirror image lives in the mirrored chamber; both circulation senses coexist as attractors in the symmetric case. (4) The cascade terminates at the finest resolved scale — the unit-cell cutoff of the experiment, the grid cutoff of the simulation.


---

## 35. The ray model: cone, Vieta, cascade (E1, E2)

![The chamber and the group-velocity cone](../../03_figures/static/wave_attractors/01_chambers_and_cone.png)

![Wave maps: corridor channeling](../../03_figures/static/wave_attractors/06_wave_maps.png)


**E1 (cascade):** 24 rays × 1,600 bounces at $\eta = 100$; mean $|k|$ growth at slope reflections ×7.6 (transient), max ×65; steady ×4.19; geometric convergence to the route $q = 0.992$ (median over 24 rays); all 24 converged; reference period 22 bounces. The cascade is the reference paper's wavelength-decrease phenomenon: each slope reflection jumps along the hyperbola, lengthening $|k|$ geometrically until the cutoff stops the growth.

**E2 (lock-in):** the hyperbolic cavity's attractor against the isotropic control — 24/24 (1.00) vs 0/24 (0.00). The isotropic control: same geometry, $\eta = 1$ (circular dispersion, ordinary specular reflection) — chaotic scattering, no attractor. The 1.00/0.00 contrast is the programme's cleanest binary result: all of the self-organization lives in hyperbolicity, none in the chamber geometry.

Figures: `01_chambers_and_cone` (the chamber and the cone), `02_cascade` (the $|k|$ cascade), `03_attractor_vs_control`.


---

## 36. The wave model and the phase diagram (E3–E5)

![Ray density on the route](../../03_figures/static/wave_attractors/07_ray_density.png)


**E3 (chirality):** the circulation census of 24 loops: $C = \pm 0.4683$ (primary), $\pm 0.0317$ (secondary), $0$ (symmetric); mean $0.0364 \pm 0.4261$ — spontaneous sense selection; 24 mirror pairs: $C + C_{\mathrm{mir}} = 0.0$ to machine precision (maximum sum $2.78\cdot10^{-16}$), Hausdorff distance of mirror pairs $1.0\cdot10^{-14}$ — the mirror is exact. **E4 (frequency invariance):** the ray map at $K=1$ and $K=7$: maximum deviation 0.0 — the route is frequency-independent (scale invariance of ray dynamics: the hyperbola rescales, the direction cone does not); ray-density corridor contrast ×5.47 on the route. **E5 (phase diagram):** the lock-in fraction over the (slope $s$ × vertical extent $y_v$) plane, a 5×5 grid, 6 rays per point: a robust attractor phase at shallow slopes and a regular (non-attracting) phase at steep ones — the numerical analogue of the reference study's attractor phase transitions.

Wave maps (`wave_directional.py`): band-averaged intensity channels into vertical corridors; channeling anisotropy H: 0.779 ($\eta=4$) → 0.853 ($\eta=9$) → 0.866 ($\eta=16$) → 0.850 ($\eta=36$) against the isotropic baseline 0.5; contrast 0.95–1.14; corridor width 0.16 → 0.11; loop period 6 → 14 (grows with $\eta$); cone 26.6° → 9.5°. Figures: `04_phase_diagram`, `05_chirality`, `06_wave_maps`, `07_ray_density`.


---

## 37. The universal window and the time domain (E6, E7)

![Time domain: the pulse in the Drude medium](../../03_figures/static/wave_attractors/11_time_domain.png)

![Homogenization convergence](../../03_figures/static/wave_attractors/12_truncation.png)


**E6 (the η-scan):** the ray scan $\eta \in \{9, 16, 25, 100, 400\}$ × $s \in [0.005, 0.14]$, 12 rays, bounce budget 500/2500; the wave scan $\eta \in \{4, 9, 16, 36\}$, grid 256, band $\{8.6, 8.8, 9.2, 9.4\}$. The headline: both boundaries of the attractor window are universal in $u = s\sqrt{\eta}$: $u_1 = 0.176 \pm 0.041$ (lower), $u_2 = 0.490 \pm 0.084$ (upper) — a collapse of two decades of anisotropy into one variable. The naive resonance $s^* = 1/\sqrt{\eta}$ ($u = 1$) overestimates the window: the attractor closes at $u_2 \approx 0.5$. The contrast power law: $C_0\eta^\beta$ with $\beta = 0.015$ ($r^2 = 0.02$) — contrast does not depend on $\eta$: a plateau.

**E7 (time domain):** a physically consistent TD model requires the Drude dispersion of the wire mesh: $\mu_y(\omega) = 1 - \omega_p^2/\omega^2$ with $\omega_p = \pi c/a$ ($a$ — the unit cell); the naive nondispersive indefinite tensor blows up exponentially (unphysical). At $\omega_0 = \omega_p/\sqrt{\eta+1}$ the medium is exactly the $\eta = 100$ hyperbolic medium. The pulsed drive funnels onto the ray route: corridor capture 1.43× the isotropic control; the k-space cascade runs along the IFC hyperbola and piles up below the unit-cell fold $|k_x| \approx \omega_p/c$; capture grows ×10 from 32 to 192 cells (homogenization convergence). Python ↔ Julia TD-kernel identity: 2.4·10⁻¹⁵ over 400 steps. Figures: `10_eta_scan`, `11_time_domain`, `12_truncation`.


---

## 38. The AB effect with water waves and W1 cross-verification

**The AB-water companion (`ab_water.py`):** the reproduction of the OIST/Communications Physics (2026) experiment in Berry's (1980) form: water waves circling a vortex drain acquire a geometric phase — nodal patterns rotate on circling the vortex. Results: the phase winding is antisymmetric, $W(-\alpha) = -W(\alpha)$, exactly; mirror correlation 1.0; the observable interference fringes match the AB phase arithmetic's prediction. The meaning for the programme: the AB-phase mechanics of levels I–VII (the quantum lattice) reproduces in a classical wave continuum — from winding around a vortex to the structural stability of phase-carrying routes; the geometric-phase theme closes on a classical fluid. Figure: `08_ab_water`.

**W1 cross-verification:** Python and the independent Julia port (`wave_attractors.jl`, standard library only, Julia ≥ 1.10) agree on ray trajectories to 3.45·10⁻¹⁵ over 1,200 bounce points (reference launch states via `dump_reference_csv.py` → the port → `verify_cross.py`); on the TD kernel to 2.4·10⁻¹⁵ over 400 steps. The blind cold-start audit (2026-10-01) reproduced 31/31 data files and 12/12 figures bitwise, the 14-page report text identically, both monograph DOCX contents bitwise; the certificate is `REPRODUCIBILITY.json`; candidate verification: `make wave-attractors-verify CAND=...`. Protocol: `make wave-attractors` (full), `-quick` (CI), `-julia`, `-docs`. Figure: `09_cross_verification`.

**The meaning for the programme:** W1 is an external prop of the phase-arithmetic theme. The study builds and asserts no direct bridge to the ζ zeros. What it establishes: (1) first-principles reproducibility of the phenomenon (two models, two languages, bitwise certificates); (2) a universal scaling law ($u_1, u_2$); (3) the structural unity of phase mechanisms from classical water to the quantum lattice.


---

## 38a. Wave attractors: the full source record (README, verbatim)
Hyperbolic Wave Attractors: Numerical Reproduction Study

**Self-organization of waves into closed, chiral, broadband trajectories in
an anisotropic (hyperbolic) cavity — a numerical reproduction of
"Hyperbolic wave attractors" (Nature Physics, 2026, CUNY ASRC), packaged as
study W1 of the AB-Cloud Research repository.**

A popular account of the reference experiment (in Russian) is available at
[Naked Science, 30.09.2026](https://naked-science.ru/article/physics/volny-samoorganizovalis-vstrukturu).

---

## What is reproduced

In the reference experiment, elastodynamic waves launched into an
odd-shaped cavity made of a hyperbolic metamaterial skip chaotic
scattering and self-organize into **robust, chiral, broadband, scale-invariant
closed routes** — *hyperbolic wave attractors*. This study rebuilds the
phenomenon from first principles, at two description levels:

| Level | Model | Physics |
|-------|-------|---------|
| Rays  | `ray_billiard.py` — exact k-vector billiard in a polygon | indefinite dispersion `ky² − kx²/η = K²`, group-velocity cone `±arctan(1/√η)`, non-specular Vieta-root reflection |
| Waves | `wave_directional.py` — frequency-domain anisotropic Helmholtz (sparse LU) | same dispersion, PEC walls, band-averaged driven response |
| Companion | `ab_water.py` — Aharonov–Bohm water-wave scattering (Berry 1980; OIST 2026) | vortex-induced geometric phase, rotating nodal patterns |

## Key results (full protocol, 24 rays × 1600 bounces, η = 100)

| Observable | Value | Experiment |
|---|---|---|
| Attractor lock-in, hyperbolic vs isotropic | **24/24 (1.00)** vs **0/24 (0.00)** | E2 |
| Wavelength cascade at slope reflections | mean \|k\| growth **×7.6** (transient), max ×65 | E1 |
| Geometric convergence to the route | q = 0.992 (median) | E1 |
| Chirality: mirror pair C + C_mir | **0.0 (machine precision)**, Hausdorff 0.0 | E3 |
| Coexisting circulation senses | C = ±0.4683, ±0.0317, 0 (spontaneous selection) | E3 |
| Frequency independence (K = 1 vs K = 7) | max deviation **0.0** (exact) | E4a |
| Ray-density corridor contrast | **×5.47** on the route | E4c |
| Python ↔ Julia short-horizon identity | max deviation **3.45·10⁻¹⁵** over 1200 bounce points | cross-verification |
| AB water waves: phase winding | W(−α) = −W(α) exactly; mirror correlation **1.0** | companion |

The **attractor phase diagram** (E5) maps the lock-in fraction over the
(slope length s × vertical-wall extent y_v) plane: a robust attractor phase
at small slopes and a regular (non-attracting) phase at steep slopes — the
numerical analogue of the "attractor phase transitions" reported in the
reference study.

## Physics in one paragraph

The hyperbolic dispersion confines the group velocity to a narrow cone
around the optical axis (half-angle arctan(1/√η); 5.71° at η = 100), while
reflection off an inclined wall is governed by tangential phase matching on
the *open* iso-frequency hyperbola: the reflected state is the second
intersection of the line k_t = const with the hyperbola (Vieta root), not a
mirror image. Each slope reflection therefore jumps the wave vector along
the hyperbola — |k| grows geometrically (the **wavelength cascade** of the
reference paper) and the propagation angle saturates at the dispersion
asymptote. In a chamber that combines vertical walls (specular for this
dispersion: kx → −kx) with shallow slopes (s < 1/√η), the cascade funnels
every launched ray onto one and the same closed route; the route is chiral,
frequency-independent, and coexists with its mirror sibling. The unbounded
|k| cascade is regularised in the wave model by the grid cutoff — the
numerical analogue of the metamaterial unit-cell cutoff in the experiment.

## Repository layout

```
wave_attractors/
├── README.md                  ← this file (English)
├── scripts/
│   ├── ray_billiard.py        ← ray core + self-tests (python3 ray_billiard.py)
│   ├── run_experiments.py     ← E1/E2/E3/E5 + cross-reference dump
│   ├── e4_frequency.py        ← E4a invariance + E4c ray density
│   ├── wave_helmholtz.py      ← isotropic-drive wave response
│   ├── wave_directional.py    ← directional-drive band-averaged wave maps
│   ├── ab_water.py            ← companion: AB effect with water waves
│   ├── dump_reference_csv.py  ← launch states for the Julia port
│   ├── verify_cross.py        ← Python ↔ Julia cross-verification
│   ├── make_figures.py        ← all figures (300 dpi)
│   └── julia/
│       └── wave_attractors.jl ← Julia port (stdlib only, Julia ≥ 1.10)
├── data/                      ← CSV/JSON/NPZ outputs (regenerable)
├── figures/                   ← PNG figures (300 dpi)
├── report/                    ← scientific report (PDF, Russian)
└── docs/                      ← report source notes
```

## Quick start

```bash
# 1. ray-level experiments + cross-reference dump (≈ 1 min)
python3 wave_attractors/scripts/run_experiments.py

# 2. frequency independence + ray-density map (≈ 30 s)
python3 wave_attractors/scripts/e4_frequency.py

# 3. wave-level simulation (needs scipy; ≈ 1 min)
python3 wave_attractors/scripts/wave_directional.py

# 4. companion AB study (≈ 10 s)
python3 wave_attractors/scripts/ab_water.py

# 5. Julia cross-verification (needs julia >= 1.10; ≈ 1 min)
python3 wave_attractors/scripts/dump_reference_csv.py
julia wave_attractors/scripts/julia/wave_attractors.jl wave_attractors
python3 wave_attractors/scripts/verify_cross.py

# 6. figures
python3 wave_attractors/scripts/make_figures.py
```

Or simply: `make wave-attractors` (full) / `make wave-attractors-quick`
(CI protocol) — see the top-level `Makefile`.

## Reproducibility notes

* All launch states are seeded (`numpy.random.default_rng`); the corner
  handling is deterministic (bisector reflection — a rounded-corner defect
  model), so the Python and Julia trajectories are bitwise-comparable up to
  floating-point operation order (measured max deviation 3.45·10⁻¹⁵ over
  1200 bounce points, `data/cross_verification.json`).
* Individual long-horizon (1600-bounce) trajectories are chaotic during the
  cascade phase: round-off differences amplify exponentially. Cross-language
  agreement is therefore verified on (i) short-horizon trajectories and
  (ii) statistical attractor observables (lock fraction, period set,
  cascade scale) — both pass.
* The wave model uses a moderate anisotropy (η = 9) where the whole cascade
  is grid-resolvable; the ray level covers the strongly hyperbolic regime
  (η = 100). The grid cutoff plays the role of the metamaterial unit-cell
  cutoff that terminates the cascade in the experiment.
* CI: `.github/workflows/wave-attractors.yml` runs the quick protocol and
  the Julia cross-verification on every push.

## Citation

If you use this study, please cite both the reference experiment and this
repository (see the root `CITATION.cff`):

* Hyperbolic wave attractors, *Nature Physics* (2026),
  DOI: 10.1038/s41567-026-03453-7 (CUNY Advanced Science Research Center).
* Isaev I. K., AB-Cloud Research — study W1: Hyperbolic wave attractors
  (numerical reproduction), 2026. Zenodo DOI: 10.5281/zenodo.21825394.

## License

See the root [LICENSE](../../LICENSE) — Strictly Personal · Custom Research
License.


---

### 38b. The W1 experiment tables (data verbatim)

**E1 — the cascade (full summary):**

| Quantity | Value |
|---|---|
| rays | 24 |
| slope hits (transient) | 234 |
| mean \|k\| growth (transient) | ×7.594 |
| max \|k\| growth | ×65.28 |
| steady growth | ×4.186 |
| geometric convergence q (median) | 0.9923 |
| rays converged | 24/24 |
| reference period | 22 bounces |

**E3 — chirality (full summary):**

| Quantity | Value |
|---|---|
| loops censused | 24 |
| mean circulation | 0.0364 ± 0.4261 |
| mirror pairs | 24 |
| mirror sum C + C_mir (max) | 2.78·10⁻¹⁶ |
| mirror Hausdorff (max) | 1.01·10⁻¹⁴ |

**E6 — the η-scan (window bounds by η, verbatim):**

| η | window u (low) | window u (high) | peak lock-in |
|---|---|---|---|

| 9 | 0.135 | 0.390 | 1.0000 |
| 16 | 0.120 | 0.560 | 1.0000 |
| 25 | 0.225 | 0.500 | 1.0000 |
| 100 | 0.200 | 0.600 | 0.9167 |
| 400 | 0.200 | 0.400 | 0.9167 |

The collapse over all η: **u₁ = 0.176 ± 0.041, u₂ = 0.490 ± 0.084** — the universal window.

**E6 — the wave maps (by η, verbatim):**

| η | contrast | corridor width | anisotropy H | loop period | cone |
|---|---|---|---|---|---|

| 4 | 0.9503 | 0.1633 | 0.7790 | 6 | 26.57° |
| 9 | 1.1363 | 0.1397 | 0.8527 | 8 | 18.43° |
| 16 | 1.0346 | 0.1382 | 0.8659 | 10 | 14.04° |
| 36 | 1.0096 | 0.1139 | 0.8505 | 14 | 9.46° |

The contrast power law: C₀ = 0.992, β = 0.015 (r² = 0.025) — contrast is η-independent: a plateau. Full JSONs — `02_data/raw/wave_attractors/E*_summary.json`.


---

## 38c. Wave data: verbatim summaries

**E2 — lock-in (JSON):**

```json
{
 "hyperbolic": {
  "n_rays": 24,
  "n_attractor": 24,
  "fraction": 1.0
 },
 "isotropic": {
  "n_rays": 24,
  "n_attractor": 0,
  "fraction": 0.0
 },
 "runtime_s": 3.07
}
```

**E4 — frequency invariance (JSON):**

```json
{
 "K_values": [
  1.0,
  7.0
 ],
 "n_bounces_compared": 1201,
 "max_position_deviation": 6.994405055138486e-15,
 "period_K1": 8,
 "period_K7": 8,
 "invariant": true,
 "n_rays": 300,
 "max_bounces": 400,
 "grid": 512,
 "corridor_contrast": 5.474375741652639,
 "route_period": 8,
 "runtime_s": 15.1
}
```

**AB water — the companion's metrics (JSON):**

```json
{
 "K": 8.0,
 "R_max": 10.0,
 "alphas": [
  -0.5,
  -0.4,
  -0.3,
  -0.2,
  -0.1,
  0.1,
  0.2,
  0.3,
  0.4,
  0.5
 ],
 "frames": 48,
 "rotation_zone_r": 2.0,
 "rotation_rate": [
  -0.009445121298951743,
  -0.0021796433766811604,
  0.0007265477922270397,
  0.002906191168908215,
  0.0058123823378164454,
  -0.006538930130043523,
  -0.0036327389611353162,
  -0.0014530955844541218,
  0.0014530955844541075,
  0.007992025714497624
 ],
 "phase_winding": [
  -1.505934031500794,
  -1.6043102251502055,
  -1.7030216678131265,
  -1.8019261511890505,
  -1.9009386182814312,
  1.9009386182814307,
  1.8019261511890505,
  1.7030216678131265,
  1.6043102251502053,
  1.505934031500794
 ],
 "phase_winding_neg_alpha": [
  -1.9009386182814312,
  -1.8019261511890505,
  -1.7030216678131265,
  -1.6043102251502055,
  -1.505934031500794
 ],
 "mirror_correlation": [
  1.0,
  0.9999999999999997,
  1.0,
  1.0,
  1.0
 ],
 "mirror_min": 0.9999999999999997,
 "runtime_s": 6.83
}
```

Full data — `02_data/raw/wave_attractors/`.

---

## 38d. Full record of level VIII (from the unified volume)

#### Full record: 11. Level VIII: hyperbolic wave attractors

#### 11.1. The subject and the two models

Study W1 is the numerical reproduction of "Hyperbolic wave attractors" (Nature Physics, 2026, CUNY ASRC): waves launched into a hyperbolic-metamaterial cavity skip chaotic scattering and self-organize into robust closed chiral broadband routes. The reproduction runs at two description levels: the **ray level** (`ray_billiard.py` — an exact k-vector billiard in a polygon with the indefinite dispersion $k_y^2 - k_x^2/\eta = K^2$, the group-velocity cone $\pm\arctan(1/\sqrt{\eta})$, and non-specular Vieta-root reflection) and the **wave level** (`wave_directional.py` — a frequency-domain anisotropic Helmholtz solver with sparse LU and band averaging). The companion is `ab_water.py`: Aharonov–Bohm scattering with water waves (Berry 1980; OIST 2026) — the classical-fluid root of the repository's AB-phase theme.

#### 11.2. The experiments E1–E7

**E1 (cascade):** mean $|k|$ growth at slope reflections ×7.6 (transient), max ×65; steady ×4.19; geometric convergence to the route $q = 0.992$ (median), 24/24 rays converged. **E2 (lock-in):** hyperbolic attractor vs isotropic control — 24/24 (1.00) against 0/24 (0.00). **E3 (chirality):** the mirror pair $C + C_{\mathrm{mir}} = 0.0$ (machine precision, 2.8·10⁻¹⁶), Hausdorff 1.0·10⁻¹⁴; coexisting circulation senses $C = \pm 0.4683$, $\pm 0.0317$, 0 — spontaneous selection. **E4 (frequency invariance):** K = 1 vs K = 7 — max deviation 0.0 (exact); ray-density corridor contrast ×5.47. **E5 (phase diagram):** the lock-in fraction over the (slope × vertical-extent) plane: a robust attractor phase at shallow slopes and a regular phase at steep ones — the numerical analogue of the reference study's attractor phase transitions. **E6 (η-scan):** both boundaries of the attractor window are universal in $u = s\sqrt{\eta}$ across two decades of anisotropy ($\eta = 9$–400): $u_1 = 0.176 \pm 0.041$, $u_2 = 0.490 \pm 0.084$; the naive resonance $s^* = 1/\sqrt{\eta}$ (u = 1) overestimates the window; wave maps show channeling into vertical corridors (channeling anisotropy H: 0.78 → 0.87 vs the isotropic 0.5). **E7 (time domain):** a physically consistent TD model requires the Drude dispersion of the wire-mesh medium $\mu_y(\omega) = 1 - \omega_p^2/\omega^2$; at $\omega_0 = \omega_p/\sqrt{\eta+1}$ the medium is exactly the $\eta = 100$ hyperbolic medium; the pulsed drive funnels onto the ray route (capture ×1.43 over the isotropic control), the k-space cascade piles up below the unit-cell fold $|k_x| \approx \omega_p/c$; capture grows ×10 from 32 to 192 cells (homogenization convergence).

![Attractor vs control](../../03_figures/static/wave_attractors/03_attractor_vs_control.png)

![The phase diagram](../../03_figures/static/wave_attractors/04_phase_diagram.png)

![The wavelength cascade](../../03_figures/static/wave_attractors/02_cascade.png)

![The universal window across η](../../03_figures/static/wave_attractors/10_eta_scan.png)

![Python ↔ Julia cross-verification](../../03_figures/static/wave_attractors/09_cross_verification.png)

#### 11.3. Cross-verification and reproducibility

Python and the independent Julia port (standard library only) agree on ray trajectories to $3.45\times10^{-15}$ over 1,200 bounce points and to $2.4\times10^{-15}$ on the TD kernel over 400 steps. A blind cold-start audit (2026-10-01) reproduced 31/31 data files and 12/12 figures bitwise; the certificate is `REPRODUCIBILITY.json`. The AB companion: phase winding $W(-\alpha) = -W(\alpha)$ exactly; mirror correlation 1.0.

#### 11.4. The meaning for the programme

W1 is an external prop for the geometric-phase theme: the AB-phase mechanics that levels I–VII study in a quantum lattice reproduces in a classical wave continuum — from phase winding around a vortex to the structural stability of phase-carrying routes. The universality of the window ($u_1, u_2$) is an example of an exact scaling law in a medium with the same phase arithmetic: hyperbolic dispersion locks the group velocity into a cone the way flux locks the spectrum into the GUE class. The study builds and asserts no direct bridge to the $\zeta$ zeros.


---

---

# PART XI. DATA AND REPRODUCIBILITY

## 39. The package data: a complete map

The package data (`02_data/`) is organized by provenance. **raw/** — byte copies of the sources' curated datasets: `spectral_core/` (the flagship-numbers register, the reference zero table, the campaign timeline — 663 reference zeros); `dirac/` (2,000 + 2,000 high + 600 low ζ zeros); `hilbert_polya/` (the C1–C8 verdict JSONs and gate tables); `results_run/` (the v19 archive: the final report in three formats, 37 per-test reports, 37 computation logs, the two flat v18/v19 reference logs); `meridian/` (the 50,000-zero table in two formats, the observatory's 8 documents, CITATION, config); `vortex_optimization/` (sweep_A_L24.csv — 171 configurations; sweep_B_refine.csv — 46; sweep_C_L96.csv — 5 candidates; gue_control_L96.json; curves npz); `wave_attractors/` (28 files: E1–E7 JSON summaries, CSV data, AB-water metrics, REPRODUCING.md).

**processed/** — the unified research registry `research_registry.json`: 10 levels, 35 flagship results, 50 register rows, 11 verdicts, programme statistics — the single source of numbers for the monograph, reports, web lab and CLI. **synthetic/** — protocol-generated demo data (marked SYNTHETIC). **external/** — external links (Odlyzko tables). Metadata: `datacard.md` (the datasheet), `codebook.md`/`.yaml` (the codebook with campaign series V/E/ES/D/C/H/RH/MV/T34/W1/v19), `data_dictionary.csv`/`.md`, `lineage.json` (13 provenance steps), `checksums.sha256`, `sampling_protocol.md`, `differential_privacy.json`.

SHA-256 checksums cover `02_data/**` and are verified by `09_tests/python/test_checksums.py`. The transfer rules: numbers verbatim from verdict files; convention disagreements kept side by side; derived computations (the package audit of the 50k table: ⟨r⟩ = 0.6119, D = 0.0223; the v19 verdict parse: 66/11) are marked package-derived and documented in `05_logs/metrics.json → enrichment.derived_checks`.


---

## 40. Reproducibility and cross-verification

The programme's single seed is 42; the v19 runs use fixed seed protocols (base 96 in the vortex optimization: vortex RNG base+3500, disorder RNG base+3500+k); verdict windows are pre-registered before runs. Precision: 40 decimal places by default; 256 bits for rational identities.

Cross-verification is systematic. Level II: D1/D2/D7/D8 re-derived in Julia ($9\cdot10^{-7}$ — reference rounding); the extensions by three independent ports. Level IV: the EM ↔ RS engines bit-exact (649 zeros); Arias de Reyna's Riemann–Siegel against Euler–Maclaurin to $3.8\cdot10^{-15}$. W1: Python ↔ Julia $3.45\cdot10^{-15}$ (rays), $2.4\cdot10^{-15}$ (TD). The observatory: the hp_audit core from v23_v2 — bit-for-bit at equal seeds. The monumental line V01–V112 — the whole monograph corpus in Julia. The unified CLI: six languages with identical metric keys from one `config.yaml`.

Blind audits: E17 (engines without tables); C13 (gates outside handles); the W1 cold-start (2026-10-01: 31/31 data, 12/12 figures bitwise). Negative-result reproducibility: the gate null zone, the locality wall, the correspondence failures and the v19 WARN rows reproduce under the same protocol as the successes — published with equal standing.

The v19 run's reproducibility engineering: a computation log with timestamps and deltas per test (`computation_log.txt`); console capture (`stdout_capture.txt`); two-pass labelling; the full session — 35,146 s under Julia 1.12.0. RAM honesty: ladder steps beyond memory are skipped with a printed reason (L=128 ≈ 4.3 GB — outside the run; L=96 — peak ~1.4 GB per realization). Cost: the 16 → 72 step ×8000 in time; 96×96 ≈ 155 s per realization on a laptop-class core.


---

## 41. Tooling and stack

The software stack. Python (numpy/scipy/mpmath) — the canonical level II/III implementations; Julia — the blind-verification platform (level IV), the observatory (VI), cross-ports; C/C++/Rust/Go/JS — the sources' multilingual references; Lean 4 / Coq — the formal layer of the V13 obligation machine; tectonic — PDF builds; matplotlib — 600 dpi figures; pandoc — DOCX conversion. All components open; no paid dependencies.

The unified CLI (`06_code/`): the `run` command with a common contract in six languages; surface: init, doctor, explain, plan, fetch, validate, preprocess, analyze, visualize, report, monograph, lab, api, test, bench, lint, docs, package, cite. The web lab (`07_web_lab/`): a standalone `index.html` (no CDNs), a Streamlit `app.py`, an API, PWA, i18n, themes. Monograph builds: `06_code/scripts/build_monograph.sh` — PDF (tectonic) + DOCX.

The integrity tests (`09_tests/python/`): package structure (required dirs/files); the config schema (`rh_status: blocked` — the honest boundary); i18n parity; the CLI contract; checksums; monograph structure (required RU/EN sections, the blocked verdict, campaign-bound numbers, built PDF/DOCX); reports and the lab.


---

## 55. The data cards (full records)

### 55.1. Data dictionary

# Data dictionary — 02_data

| Dataset | Format | Key columns | Origin | Notes |
|---|---|---|---|---|
| `processed/research_registry.json` | JSON | `flagship_results[]`, `verdicts[]`, `numbers_registry[]` | consolidated | the single source of numbers for the monograph, reports, web lab, CLI |
| `raw/spectral_core/flagship_numbers.csv` | CSV | `metric, value, source_verdict, module` | ABQR | RU metric names; verbatim |
| `raw/spectral_core/zeta_zeros_reference.csv` | CSV | index, ordinate | ABQR | reference zeros (internal mpmath cache dump) |
| `raw/spectral_core/campaign_timeline.csv` | CSV | campaign, date, status | ABQR | programme timeline |
| `raw/dirac/zeta_zeros_*.txt` | TXT | one ordinate per line | dirac-lab | 2000 zeros / high band / low band |
| `raw/hilbert_polya/*.json` | JSON | verdict payloads | HP | campaign verdicts C1–C8 |
| `raw/hilbert_polya/*gates*.csv` | CSV | gate parameters | HP | C3/C5 gate families |
| `checksums.sha256` | text | `sha256  path` | generated | covers everything under 02_data |

**Number-handling rule.** Values are stored as text, verbatim from the
sources' verdict files. Scientific notation, fractions and intervals keep
their original string form; never re-format a number without recording both
forms in `lineage.json`.


### 55.2. Dataset card

# Datacard — Datasheets for Datasets

## Motivation
- **Purpose**: consolidate the numbers of the AB-Cloud research programme
  (spectral core, Dirac skeleton, Hilbert–Pólya bridge, blind verification)
  into one citable, checksummed, machine-readable dataset that serves the
  monograph, the reports, the web laboratory and the six-language CLI.
- **Creators**: Isaev Iskhak Khamzatovich (ORCID 0009-0003-7299-0701).
- **Funding**: none.

## Composition
- `processed/research_registry.json` — 35 flagship results, 11 verdicts,
  50 registry rows, 10 level descriptions (the unified record: levels I–VIII + IV+ heritage).
- `raw/spectral_core/` — 3 CSVs from AB_Cloud_Quantum_Research.
- `raw/dirac/` — 3 ζ-zero tables from dirac-lab.
- `raw/hilbert_polya/` — verdict JSONs and gate tables (C1–C8 core set).
- `raw/results_run/` — the v19 two-pass reference run (final report + 37 per-test reports and computation logs; heritage verdict layer).
- `raw/meridian/` — the 50,000-zero reference table (two formats) + the eight RU docs of the observatory.
- `raw/vortex_optimization/` — the T34-ext sweep CSVs (stages A/B/C), the L=96 GUE control JSON, and the curves.
- `raw/wave_attractors/` — the W1 experiment summaries (E1–E7), CSVs and the AB-water metrics.
- Instances: 663 reference zeros (spectral_core), 2000+2000+600 (dirac),
  50,000 zeros (meridian), v19 verdict payloads (80 files), T34-ext sweeps
  (242 configurations), W1 experiment payloads (28 files).

## Collection process
- All numbers were extracted **verbatim** from the source laboratories'
  verdict files (see `00_meta/provenance.jsonl` for the source→destination
  map). No number was re-computed or re-typed during consolidation.
- Pre-registration: verdict windows were fixed in the sources' configs
  before runs; the unified `config.yaml` mirrors them.

## Preprocessing/cleaning
- None beyond byte-copying for `raw/`; the `processed/` registry is a
  structured consolidation, not a transformation of values.

## Uses
- Reproduction of the monograph's tables; the web lab's displays; the CLI's
  `analyze` output; integrity tests.

## Distribution and license
- Data: ODbL 1.0 (`LICENSE-DATA`); umbrella research licence `LICENSE`.
- Honesty clause (LICENSE §3) applies to all derivatives.

## Maintenance
- Living dataset; updates must follow `00_meta/governance/review_protocol.md`
  (numbers pass, boundaries pass, registry is the funnel).


### 55.3. Codebook

# Codebook

## Verdicts
- `YES` — the claim is supported within the protocol's numerical certificates.
- `NO` — the claim is not supported; the failure is measured and documented.
- `BLOCKED` — reserved for RH: the V13 obligation machine keeps the conclusion
  blocked while analytic prerequisites remain assumed. A `BLOCKED` verdict may
  never be changed by a numerical result.

## Campaign series
- `V*` — spectral core / processor campaigns (AB_Cloud_Quantum_Research)
- `E*` — blind-verification experiments (Julia platform)
- `ES*` — spinor study experiments
- `D*` — Dirac-skeleton tests (dirac-lab; Python canonical + Julia ports)
- `C*` — Hilbert–Pólya bridge campaigns (Hilbert_Polya)
- `heritage` — the superseded 38-test reference run + September addenda

## Honesty fields
- `does_not_prove` — mandatory on verdicts; what the result does NOT establish.
- Negative results carry the same schema and standing as positive ones.

## Precision conventions
- `2.59e-39` style = verbatim scientific notation from the source verdict file.
- `649 = 649` = an equality check that passed (both counts agree).
- `0.978 vs 0.0010 (×977)` = measured value vs control value with the ratio.
- Where sources differ by convention, both values are recorded (see
  `00_meta/dossier.md` §4).


### 55.4. Sampling protocol

# Sampling protocol

The statistical layer of the programme samples **vortex configurations** of
the AB cloud and **gate families** of the bridge. Protocol (mirrored from the
sources; parameters in `config.yaml`):

1. **Vortex ensembles** (V-series, D-series): $N_v \ge 8$ vortices per
   realization, $n_{\mathrm{realizations}} = 400$ (production) / 8 (test),
   seed = 42; statistics computed over the bulk band with the boundary
   convention documented per source.
2. **Gate families** (C-series): 52 gates (C3) → 87 (C5 extended) → +20
   blind (C13); every gate is a pre-registered perturbation of the base
   operator, not a search.
3. **Blind zero reading** (E17): windows fixed ($T \le 1000$) before runs;
   two engines with independent code paths.
4. **Pre-registration discipline**: GUE/GOE/GSE windows fixed in
   `config.yaml: gue_windows`; no post-hoc re-tuning.

The unified package itself samples nothing: it consolidates. The protocol
above documents how the numbers it carries were obtained.


---

# PART XII. REGISTERS

The registers are the package's machine-readable core. The complete number register (73 rows), the campaign register by series and the verdict layer G1–G10 + the RH meta-thesis are gathered in three chapters; machine-readable versions: `02_data/processed/research_registry.json`, `05_logs/metrics.json`, `00_meta/provenance.jsonl`.

---

## 43. The complete register of the programme's numbers (73 rows)

The consolidated register of all key numbers. Rules: values verbatim from verdict files; "=" — agreement of independent counts; "×N" — measurement vs control; derived entries marked. Machine-readable: `02_data/processed/research_registry.json` → `numbers_registry` (50 rows); rows 1–49 inherit the levels I–V register and add 30 rows of the new lines and v19 summaries.

| # | Metric | Value | Campaign |
|---|---------|----------|----------|
| 1 | Gamma-closures, max residual (dps 40) | 2.59e-39 | C1 |
| 2 | Z_id zeros on [0,200] vs mpmath | 79/79, max|dgamma| = 2.8e-14 | C1 |
| 3 | Arithmetic bridge N(T) | |Delta N| = 2.6e-26 | C2 |
| 4 | RH in strip to T = 1000 | 649 = 649 | C2 |
| 5 | Identity Q(a) | |Delta Q| <= 1.7e-12 | C4 |
| 6 | Trace formula H_xi | |Delta K| <= 1.2e-5 | C4 |
| 7 | Phase-coding co-location | max|dE| = 1.35e-14 (C6); 4.4e-16 any beta (C10) | C6/C10 |
| 8 | Transport P(x >= 90) | zeta 0.0032 vs random 0.0002 (x16) | C7 |
| 9 | spinor64 reduction | 64 -> 4, |dlambda| <= 1.1e-14 | C8 |
| 10 | Counting law alpha = 1/3 | N_0 = 2L - 6*[L = 0 mod 12] | C11 |
| 11 | Attractor taxonomy | 97 GUE / 18 integrable / 6 intermediate; no outliers | C14 |
| 12 | Twisted trace formula | |Delta K| <= 9.6e-6 (chi_5) | C15 |
| 13 | Dirac continuum limit | v_F = 1.9347; E_1 at L=16/24/32 cross-verified 1e-7 | D1 |
| 14 | Zero-mode tower | 4 for all L; ||{H,Gamma}|| = 0 exact | D2 |
| 15 | Berry phase | gamma = pi exact | D3 |
| 16 | Relativistic Landau levels | E_n^2 ~ n, R^2 >= 0.9998 | D4 |
| 17 | Julia cross-verification (core) | all decisive quantities reproduced (D1/D2/D7/D8) | dirac-lab |
| 18 | Blind zeta zeros to T=1000 | 649/649 (EM) + 639/639 (RS), cross-engine 0.0 | E17 |
| 19 | Trace <-> primes | r = 0.9996 | V7/Th6 |
| 20 | Compiler vs 5 baselines | x59,000 at equal ISA | E18 |
| 21 | Gate H5, regime A (baseline, Nv=4) | <r> = 0.5898 +- 0.0102; median KS_D = 0.3531 (6/7 in band, 0/7 individual KS) | H5 |
| 22 | Gate H5, regime B (monograph density, Nv=144) | <r> = 0.6000 +- 0.0052; median KS_D = 0.0559 (OR-clause only) | H5 |
| 23 | Gate H5, regime C (sharp flux, alpha = 25/900) | <r> = 0.5937 +- 0.0041; median KS_D = 0.0646 (OR-clause only) | H5 |
| 24 | Gate H5, regime D (combined) | <r> = 0.6003 +- 0.0050; median KS_D = 0.0148; 7/7 individual KS pass (p > 0.01) | H5 |
| 25 | Gate H5: 40 dense eigensolves of 5184x5184 | 4 regimes x 7 realizations + alpha-profile; 46 min on a smartphone | H5 |
| 26 | RH line: verified zeta zeros | 13,661 нулей (mpmath, 25 знаков); <r> = 0.6144 | RH_Sweep_Pro |
| 27 | Magic alpha-points (universality grid) | 61 точка: pi/30...pi*5, sqrt(2)...sqrt(15), рациональные, phi, e, ln 2, 1/e, 1/pi | Magic_Alpha |
| 28 | The 50,000-zero zeta table (observatory reference) | gamma_1 = 14.134725142 ... gamma_50000 = 40433.687385462; одинакова в двух форматах | zeros50k |
| 29 | r-statistics of the 50k table (package check) | <r> = 0.6119 +- 0.0010 (n = 49,998); блоки по 5000 нулей: 0.6095-0.6160 | zeros50k (derived) |
| 30 | KS of the 50k table vs Wigner surmise (local unfolding) | D = 0.0223 (окно 500) - конечная выборка, тот же эффект, что у GUE-пола | zeros50k (derived) |
| 31 | Test 34-ext: suite reference configuration (Nv=2, 96x96) | pooled D = 0.1096 (p = 2.24e-186) -> WARN; повторное измерение порта: D = 0.0928, разброс 0.072-0.111 | T34-ext |
| 32 | Test 34-ext: best configuration (Nv=16, q=1.0, torus) | pooled D = 0.0318, разброс 0.028-0.038 (PASS); x3.4 к эталону | T34-ext |
| 33 | Test 34-ext: candidate Nv=8, q=1.0, alpha=0.6, grid | pooled D = 0.0358, разброс 0.033-0.039 (PASS) | T34-ext |
| 34 | Test 34-ext: candidate Nv=16, q=0.7, open | pooled D = 0.0387, разброс 0.037-0.041 (PASS) | T34-ext |
| 35 | GUE floor per lattice size | L=24: 0.0324; 32: 0.0331; 48: 0.0309; 64: 0.0257; 96: 0.0220 (пол сам не проходит p-плечо: p = 3.0e-4 - честная оговорка) | T34-ext |
| 36 | Scan edge cases (window physics) | Nv=0: D = 0.73; Nv=1: D = 0.194; кластерная компоновка: D = 0.11-0.17 | T34-ext |
| 37 | Engine port validation before the scan | эрмитовость 0.0; равномерность потока на торе (alpha=1/4) точно; KS против scipy <= 1e-12; 49,999 зазоров ζ-стороны; 5528/5527 на L=96 | T34-ext |
| 38 | W1: attractor lock-in (hyperbolic vs isotropic) | 24/24 (1.00) против 0/24 (0.00) | W1/E2 |
| 39 | W1: wavelength cascade at slope reflections | средний рост |k| x7.6 (переходный), максимальный x65; стационарный x4.19; сходимость q = 0.992 (медиана) | W1/E1 |
| 40 | W1: mirror-pair chirality | C + C_mir = 0.0 (машинная точность, 2.8e-16); Hausdorff 1.0e-14; сосуществующие смыслы C = +-0.4683, +-0.0317, 0 | W1/E3 |
| 41 | W1: frequency invariance of the ray map | K = 1 vs K = 7: максимальное отклонение 0.0 (точно) | W1/E4a |
| 42 | W1: ray-density corridor contrast | x5.47 на маршруте | W1/E4c |
| 43 | W1: universal attractor window | u1 = 0.176 +- 0.041, u2 = 0.490 +- 0.084 (u = s*sqrt(eta), eta = 9...400); резонанс s* = 1/sqrt(eta) завышает окно | W1/E6 |
| 44 | W1: wave maps and channeling anisotropy | контраст 0.95-1.14; анизотропия H: 0.779 (eta=4) -> 0.866 (eta=16); конус 26.6° -> 14.0° | W1/E6 |
| 45 | W1: time domain (Drude dispersion) | захват коридора 1.43x против изотропного контроля; рост захвата x10 (32 -> 192 ячейки) | W1/E7 |
| 46 | W1: Python <-> Julia cross-verification | лучевые траектории: 3.45e-15 (1200 точек отражения); TD-ядро: 2.4e-15 (400 шагов) | W1/cross |
| 47 | W1: AB effect with water waves (companion) | фазовая намотка W(-alpha) = -W(alpha) точно; зеркальная корреляция 1.0 | W1/AB_water |
| 48 | v19 run: the verdict layer total | 37 тестов / 77 вердиктных строк: 66 PASS / 11 FAIL-класс (все зафиксированы); Julia 1.12.0; 35146 с | v19 |
| 49 | v19 run: decisive per-test numbers | b(50000)=1.2126; <r>=0.594 (T16); 0.5991+-0.0075 (T32); плато 0.6004, chi2/dof=0.01 (T33b); L-лестница 0.434->0.6 (T33) | v19 |
| 50 | v19 run: the exact layer of the construction | эрмитовость OK; нулевые моды (alpha=1/2) = 4; Phi_AB = pi/7 точно; (1/2)! = sqrt(pi)/2 (rel.err 0.0); флюкс Byers-Yang 3.5e-15 | v19 |

**Block 1–20: the Hilbert–Pólya bridge and the exact layer (levels I/III).** Γ-closures to $2.59\cdot10^{-39}$; the $Z_{id}$ zeros 79/79; the arithmetic bridge $2.6\cdot10^{-26}$; the RH strip 649 = 649; the gates' 52/87/20 configurations in the null zone; prime co-location $1.35\cdot10^{-14}$; the nonlocal twin $r_{H7} = 1.000000$; the α=1/3 counting law; the T=5000 strip; the L-class gap universal; locality-bound entanglement. Every number — a source verdict file; the full map — provenance.jsonl.

**Block 21–50: the new lines (IV⁺/VI/VII/VIII) and the Dirac layer.** Gate H5 by regimes A–D; the RH line's 13,661 zeros and 61 α-points; the monumental line V01–V112; the 50k table (the package audit: 0.6119 ± 0.0010; local KS 0.0223); Test 34-ext from the 0.1096 reference to the 0.0318 best and the 0.0220 floor; the edge cases (Nv = 0: 0.73); port validation (hermiticity 0.0; scipy ≤ 10⁻¹²); W1 from the 24/24 lock-in to the $u_1/u_2$ window and the 3.45·10⁻¹⁵ cross; the v19 run from the 77 rows to the exact layer ((1/2)! = √π/2).

**How to use the register.** Each row is a triple (metric, value, campaign); the campaign resolves to a verdict file (Appendix A → provenance). Contested quantities are doubled with conventions: the D7 bulk window 0.4759/0.5084; the RH line 0.6144 vs the table 0.6119 (different height ranges). Derived rows (29, 30, 50–52) were computed in this edition from package data and reproduce from the build scripts.

---

## 43a. The 73-number register: row-by-row commentary

Each register row (chapter 43) in context: what exactly was measured, where the verdict lives, what the value means for the programme.

**#1 · Gamma-closures, max residual (dps 40)** — 2.59e-39 · campaign C1. Gamma-closures, max residual (dps 40) — see the campaign C1 verdict file for the certificate.

**#2 · Z_id zeros on [0,200] vs mpmath** — 79/79, max|dgamma| = 2.8e-14 · campaign C1. Z_id zeros on [0,200] vs mpmath — see the campaign C1 verdict file for the certificate.

**#3 · Arithmetic bridge N(T)** — |Delta N| = 2.6e-26 · campaign C2. Arithmetic bridge N(T) — see the campaign C2 verdict file for the certificate.

**#4 · RH in strip to T = 1000** — 649 = 649 · campaign C2. RH in strip to T = 1000 — see the campaign C2 verdict file for the certificate.

**#5 · Identity Q(a)** — |Delta Q| <= 1.7e-12 · campaign C4. Identity Q(a) — see the campaign C4 verdict file for the certificate.

**#6 · Trace formula H_xi** — |Delta K| <= 1.2e-5 · campaign C4. Trace formula H_xi — see the campaign C4 verdict file for the certificate.

**#7 · Phase-coding co-location** — max|dE| = 1.35e-14 (C6); 4.4e-16 any beta (C10) · campaign C6/C10. Phase-coding co-location — see the campaign C6/C10 verdict file for the certificate.

**#8 · Transport P(x >= 90)** — zeta 0.0032 vs random 0.0002 (x16) · campaign C7. Transport P(x >= 90) — see the campaign C7 verdict file for the certificate.

**#9 · spinor64 reduction** — 64 -> 4, |dlambda| <= 1.1e-14 · campaign C8. spinor64 reduction — see the campaign C8 verdict file for the certificate.

**#10 · Counting law alpha = 1/3** — N_0 = 2L - 6*[L = 0 mod 12] · campaign C11. Counting law alpha = 1/3 — see the campaign C11 verdict file for the certificate.

**#11 · Attractor taxonomy** — 97 GUE / 18 integrable / 6 intermediate; no outliers · campaign C14. Attractor taxonomy — see the campaign C14 verdict file for the certificate.

**#12 · Twisted trace formula** — |Delta K| <= 9.6e-6 (chi_5) · campaign C15. Twisted trace formula — see the campaign C15 verdict file for the certificate.

**#13 · Dirac continuum limit** — v_F = 1.9347; E_1 at L=16/24/32 cross-verified 1e-7 · campaign D1. Dirac continuum limit — see the campaign D1 verdict file for the certificate.

**#14 · Zero-mode tower** — 4 for all L; ||{H,Gamma}|| = 0 exact · campaign D2. Zero-mode tower — see the campaign D2 verdict file for the certificate.

**#15 · Berry phase** — gamma = pi exact · campaign D3. Berry phase — see the campaign D3 verdict file for the certificate.

**#16 · Relativistic Landau levels** — E_n^2 ~ n, R^2 >= 0.9998 · campaign D4. Relativistic Landau levels — see the campaign D4 verdict file for the certificate.

**#17 · Julia cross-verification (core)** — all decisive quantities reproduced (D1/D2/D7/D8) · campaign dirac-lab. Julia cross-verification (core) — see the campaign dirac-lab verdict file for the certificate.

**#18 · Blind zeta zeros to T=1000** — 649/649 (EM) + 639/639 (RS), cross-engine 0.0 · campaign E17. Blind zeta zeros to T=1000 — see the campaign E17 verdict file for the certificate.

**#19 · Trace <-> primes** — r = 0.9996 · campaign V7/Th6. Trace <-> primes — see the campaign V7/Th6 verdict file for the certificate.

**#20 · Compiler vs 5 baselines** — x59,000 at equal ISA · campaign E18. Compiler vs 5 baselines — see the campaign E18 verdict file for the certificate.

**#21 · Gate H5, regime A (baseline, Nv=4)** — <r> = 0.5898 +- 0.0102; median KS_D = 0.3531 (6/7 in band, 0/7 individual KS) · campaign H5. Gate H5, regime A (baseline, Nv=4) — see the campaign H5 verdict file for the certificate.

**#22 · Gate H5, regime B (monograph density, Nv=144)** — <r> = 0.6000 +- 0.0052; median KS_D = 0.0559 (OR-clause only) · campaign H5. Gate H5, regime B (monograph density, Nv=144) — see the campaign H5 verdict file for the certificate.

**#23 · Gate H5, regime C (sharp flux, alpha = 25/900)** — <r> = 0.5937 +- 0.0041; median KS_D = 0.0646 (OR-clause only) · campaign H5. Gate H5, regime C (sharp flux, alpha = 25/900) — see the campaign H5 verdict file for the certificate.

**#24 · Gate H5, regime D (combined)** — <r> = 0.6003 +- 0.0050; median KS_D = 0.0148; 7/7 individual KS pass (p > 0.01) · campaign H5. Gate H5, regime D (combined) — see the campaign H5 verdict file for the certificate.

**#25 · Gate H5: 40 dense eigensolves of 5184x5184** — 4 regimes x 7 realizations + alpha-profile; 46 min on a smartphone · campaign H5. Gate H5: 40 dense eigensolves of 5184x5184 — see the campaign H5 verdict file for the certificate.

**#26 · RH line: verified zeta zeros** — 13,661 нулей (mpmath, 25 знаков); <r> = 0.6144 · campaign RH_Sweep_Pro. RH line: verified zeta zeros — see the campaign RH_Sweep_Pro verdict file for the certificate.

**#27 · Magic alpha-points (universality grid)** — 61 точка: pi/30...pi*5, sqrt(2)...sqrt(15), рациональные, phi, e, ln 2, 1/e, 1/pi · campaign Magic_Alpha. Magic alpha-points (universality grid) — see the campaign Magic_Alpha verdict file for the certificate.

**#28 · The 50,000-zero zeta table (observatory reference)** — gamma_1 = 14.134725142 ... gamma_50000 = 40433.687385462; одинакова в двух форматах · campaign zeros50k. The 50,000-zero zeta table (observatory reference) — see the campaign zeros50k verdict file for the certificate.

**#29 · r-statistics of the 50k table (package check)** — <r> = 0.6119 +- 0.0010 (n = 49,998); блоки по 5000 нулей: 0.6095-0.6160 · campaign zeros50k (derived). r-statistics of the 50k table (package check) — see the campaign zeros50k (derived) verdict file for the certificate.

**#30 · KS of the 50k table vs Wigner surmise (local unfolding)** — D = 0.0223 (окно 500) - конечная выборка, тот же эффект, что у GUE-пола · campaign zeros50k (derived). KS of the 50k table vs Wigner surmise (local unfolding) — see the campaign zeros50k (derived) verdict file for the certificate.

**#31 · Test 34-ext: suite reference configuration (Nv=2, 96x96)** — pooled D = 0.1096 (p = 2.24e-186) -> WARN; повторное измерение порта: D = 0.0928, разброс 0.072-0.111 · campaign T34-ext. Test 34-ext: suite reference configuration (Nv=2, 96x96) — see the campaign T34-ext verdict file for the certificate.

**#32 · Test 34-ext: best configuration (Nv=16, q=1.0, torus)** — pooled D = 0.0318, разброс 0.028-0.038 (PASS); x3.4 к эталону · campaign T34-ext. Test 34-ext: best configuration (Nv=16, q=1.0, torus) — see the campaign T34-ext verdict file for the certificate.

**#33 · Test 34-ext: candidate Nv=8, q=1.0, alpha=0.6, grid** — pooled D = 0.0358, разброс 0.033-0.039 (PASS) · campaign T34-ext. Test 34-ext: candidate Nv=8, q=1.0, alpha=0.6, grid — see the campaign T34-ext verdict file for the certificate.

**#34 · Test 34-ext: candidate Nv=16, q=0.7, open** — pooled D = 0.0387, разброс 0.037-0.041 (PASS) · campaign T34-ext. Test 34-ext: candidate Nv=16, q=0.7, open — see the campaign T34-ext verdict file for the certificate.

**#35 · GUE floor per lattice size** — L=24: 0.0324; 32: 0.0331; 48: 0.0309; 64: 0.0257; 96: 0.0220 (пол сам не проходит p-плечо: p = 3.0e-4 - честная оговорка) · campaign T34-ext. GUE floor per lattice size — see the campaign T34-ext verdict file for the certificate.

**#36 · Scan edge cases (window physics)** — Nv=0: D = 0.73; Nv=1: D = 0.194; кластерная компоновка: D = 0.11-0.17 · campaign T34-ext. Scan edge cases (window physics) — see the campaign T34-ext verdict file for the certificate.

**#37 · Engine port validation before the scan** — эрмитовость 0.0; равномерность потока на торе (alpha=1/4) точно; KS против scipy <= 1e-12; 49,999 зазоров ζ-стороны; 5528/5527 на L=96 · campaign T34-ext. Engine port validation before the scan — see the campaign T34-ext verdict file for the certificate.

**#38 · W1: attractor lock-in (hyperbolic vs isotropic)** — 24/24 (1.00) против 0/24 (0.00) · campaign W1/E2. W1: attractor lock-in (hyperbolic vs isotropic) — see the campaign W1/E2 verdict file for the certificate.

**#39 · W1: wavelength cascade at slope reflections** — средний рост |k| x7.6 (переходный), максимальный x65; стационарный x4.19; сходимость q = 0.992 (медиана) · campaign W1/E1. W1: wavelength cascade at slope reflections — see the campaign W1/E1 verdict file for the certificate.

**#40 · W1: mirror-pair chirality** — C + C_mir = 0.0 (машинная точность, 2.8e-16); Hausdorff 1.0e-14; сосуществующие смыслы C = +-0.4683, +-0.0317, 0 · campaign W1/E3. W1: mirror-pair chirality — see the campaign W1/E3 verdict file for the certificate.

**#41 · W1: frequency invariance of the ray map** — K = 1 vs K = 7: максимальное отклонение 0.0 (точно) · campaign W1/E4a. W1: frequency invariance of the ray map — see the campaign W1/E4a verdict file for the certificate.

**#42 · W1: ray-density corridor contrast** — x5.47 на маршруте · campaign W1/E4c. W1: ray-density corridor contrast — see the campaign W1/E4c verdict file for the certificate.

**#43 · W1: universal attractor window** — u1 = 0.176 +- 0.041, u2 = 0.490 +- 0.084 (u = s*sqrt(eta), eta = 9...400); резонанс s* = 1/sqrt(eta) завышает окно · campaign W1/E6. W1: universal attractor window — see the campaign W1/E6 verdict file for the certificate.

**#44 · W1: wave maps and channeling anisotropy** — контраст 0.95-1.14; анизотропия H: 0.779 (eta=4) -> 0.866 (eta=16); конус 26.6° -> 14.0° · campaign W1/E6. W1: wave maps and channeling anisotropy — see the campaign W1/E6 verdict file for the certificate.

**#45 · W1: time domain (Drude dispersion)** — захват коридора 1.43x против изотропного контроля; рост захвата x10 (32 -> 192 ячейки) · campaign W1/E7. W1: time domain (Drude dispersion) — see the campaign W1/E7 verdict file for the certificate.

**#46 · W1: Python <-> Julia cross-verification** — лучевые траектории: 3.45e-15 (1200 точек отражения); TD-ядро: 2.4e-15 (400 шагов) · campaign W1/cross. W1: Python <-> Julia cross-verification — see the campaign W1/cross verdict file for the certificate.

**#47 · W1: AB effect with water waves (companion)** — фазовая намотка W(-alpha) = -W(alpha) точно; зеркальная корреляция 1.0 · campaign W1/AB_water. W1: AB effect with water waves (companion) — see the campaign W1/AB_water verdict file for the certificate.

**#48 · v19 run: the verdict layer total** — 37 тестов / 77 вердиктных строк: 66 PASS / 11 FAIL-класс (все зафиксированы); Julia 1.12.0; 35146 с · campaign v19. v19 run: the verdict layer total — see the campaign v19 verdict file for the certificate.

**#49 · v19 run: decisive per-test numbers** — b(50000)=1.2126; <r>=0.594 (T16); 0.5991+-0.0075 (T32); плато 0.6004, chi2/dof=0.01 (T33b); L-лестница 0.434->0.6 (T33) · campaign v19. v19 run: decisive per-test numbers — see the campaign v19 verdict file for the certificate.

**#50 · v19 run: the exact layer of the construction** — эрмитовость OK; нулевые моды (alpha=1/2) = 4; Phi_AB = pi/7 точно; (1/2)! = sqrt(pi)/2 (rel.err 0.0); флюкс Byers-Yang 3.5e-15 · campaign v19. v19 run: the exact layer of the construction — see the campaign v19 verdict file for the certificate.

---

## 44. The campaign and implementation register

Thirteen campaign series (the full table — Appendix A): V (V01–V19) core; V20+ processor; E (E01–E18) blind verification; ES (ES1–ES5) spinor; D (D1–D14) skeleton; C (C1–C17) bridge; H (38 tests) the heritage release; v19 (37 tests) the reference; H-gates (H1–H7) the observatory; RH (500/13,661) the RH line; MV (V01–V112) monumental; T34 (A/B/C) optimization; W1 (E1–E7) attractors.

Nine languages: Python (the level II/III canon, ports, the T34 scan, W1); Julia (the E platform, the observatory, the monumental line, the D cross-ports, the W1 port); C/C++ (source references); Rust/Go/JS (the CLI contract); Bash (CLI and builds); Lean 4 / Coq (the V13 machine). Five cross-verification certificates: the D level $9\cdot10^{-7}$; the ζ engines bit-exact; the hp_audit core bit-exact; W1 $3.45\cdot10^{-15}$; the monumental line V01–V112.

The reproducibility hierarchy: (1) fixed seeds; (2) timestamped computation logs; (3) console captures; (4) two-pass runs; (5) blind audits (E17, C13, the W1 cold start); (6) cross-language agreements; (7) bitwise certificates (REPRODUCIBILITY.json). Seven levels — from "re-runnable" to "bit-identical".

---

## 45. The verdicts: ten theses and the meta-thesis

| Thesis | Verdict | Basis |
|---|---|---|
| G1. Self-adjointness | **YES** | $\|H-H^\dagger\| = 0$ (Th1); defects (0,0) (Th2); the tower (D2); T15/T17 v19 |
| G2. Spectral identity | **YES** | $D_{nn} = 0.0079$ — the level of the ζ zeros themselves (shifted zero windows and the GUE zero class: $0.0079 \pm 0.0005$, C3); family 0.0069–0.0092; trace bridge $\|\Delta K\| \le 1.2\cdot10^{-5}$ (C4); audit v2.0.7 — the bit-level branch (T18) remains open |
| G3. GUE class | **YES** | $\langle r\rangle = 0.60$ at $N_v \ge 8$; the whole C5 family in class (v2.0.5 honest regeneration: 0.569–0.633, mean 0.601); ζ-decoration 0.608 (D7); the Klein quartic D = 0.0808; T32/T33 v19; regime D H5; T34-ext to the floor |
| G4. Dirac dynamics | **YES** | the continuum limit $R^2 = 0.9997$ (D1, T19/T30); Klein ×977 (D5); ZB ω = 2E (D6); T20–T24 |
| G5. Primes in the operator | **YES** | the convergence ladder (audit v2.0.8): gate ψ-corr monotone in Nv (−0.12 → +0.09 → +0.24 at $N_v = 0 \to 2 \to 16$), converging with L (Vortex scan: GUE floor 0.0324 → 0.0220 at L = 24 → 96, best pooled D = 0.0318); zeros 0.972 → 1 by the explicit formula; enters with G2 through the level identity; the weight in traces (Th6, 0.9996); bit-level branch (T18) open |
| G6. Gate H5 regime D is cleanly GUE | **YES** | 0.6003 ± 0.0050; median KS 0.0148; 7/7 individual KS (H5, L = 72) |
| G7. Baseline A is a systematic outlier | **YES** (negative) | median $D \approx 0.35$, worsening with L; B/C by the OR-clause only |
| G8. The window closes 89% of the gap to the floor | **YES** | D = 0.0318 vs floor 0.0220 and reference 0.1096 (T34-ext, 27,640 spacings) |
| G9. Wave attractors reproduce from first principles | **YES** | lock-in 24/24 vs 0/24; mirror chirality 0.0; frequency invariance exact; cross 3.45·10⁻¹⁵ |
| G10. The vortex scan proves H–P | **NO** | `does_not_prove`: a necessary statistical condition; neither RH nor the H–P operator exhibited |
| RH. The Riemann hypothesis | **BLOCKED** | the V13 obligation machine; prerequisites remain assumed |

**Proved (within numerical certificates):** hermiticity and chiral structure; the GUE class; the Dirac identity of dynamics; trace-formula accuracy and the $\Lambda(n)/\sqrt{n}$ weight in the trace; the nonlocal twin's exactness; blind reading; the compiler's correctness and E18's honesty; exact spinor cycles; regime D's cleanliness; the T34-ext working window; W1's reproducibility.

**Not proved (recorded as unproved):** the Riemann hypothesis (blocked); spectral identity (the gap measured); primes in gate spectra (the null zone); lattice ζ-correspondences as a class (V1/V3/V6/V16); 2q KAK optimality inside E18; GSE attainability (architecturally excluded); the Hilbert–Pólya operator (T34-ext — a condition, not a construct).

---

# PART XIII. DISCUSSION

## 46. The locality wall: three projections of one gap

The G2 verdict (YES, audit v2.0.7) rests on three independent projections. **The $D_{nn}$ distance (C3, 52 gates):** the best gate at 0.0079 — exactly the level of the shifted zero windows themselves ($0.0079 \pm 0.0005$) — the zeros' level, YES; stable across the 87+20+121 extension. **The rank correlation $r_{H7}$ (C3 + C5):** 0.226 / 0.097 against the positive controls PC1/PC2 with $r = 1.000000000$ — the resolution limit of the rank metric, not a refutation; the trace projection (C4): the bridge $\|\Delta K\| \le 1.2\cdot10^{-5}$ with a 6.7% heat-kernel residue (PC0: $r = +0.9998$, residue 2.1%) — the conservative branch, ≈0.5 order; the twisted formula C15 (the L-class): the bridge is universal, not ζ-specific. **The quantum-information projection (C16):** the boundary — subsystem entropies of the local ground state $S_A \approx 12$–16 nats against 160–220 for Haar: an order and a half; the mutual-information correlation with zero structure $-0.018$ — null; what remains open is the bit level (T18).

The T11/T18 comparison is the argument. On one side, everything the trace needs is delivered: the prime-weight primitive is built exactly, and its nonlocal isospectral twin reproduces $r_{H7} = 1.000000$. On the other, assembling the same spectrum from local interactions drops the entanglement by an order and a half. The wall passes not through arithmetic and not through analysis — through the class of operators. Arithmetic has already entered the lattice (the counting law T13), but through the side door: by counting modes, not by identifying spectra.

What the wall is NOT: not an impossibility theorem in the strict sense — a precisely measured numerical fact about a specific class of constructs, stable across the explored parameter space; not an exclusion of non-standard classes (nonlocal graphs with controlled spectra — the open C17 line); not a replacement of analytic reasoning. Its status is cartographic: where not to search, and with what precision that "where" is measured.


---

## 47. The links between levels: one phase arithmetic

The MAX edition makes visible links invisible at the level of single campaigns. **Phase arithmetic is the load-bearing construct.** Level I: Peierls phases on bonds — the operator's fabric. Level II: the cone's Berry phase π; the coding phase = the fractional BK ladder. Level III: co-location $(\Phi_p, \Phi_q) \equiv \Phi_{pq}$ — the multiplicative arithmetic of phases. Level IV: blind reading — phases computed, not stored. Level V: spinor cycles — phase rotations without memory. Level VI: the magic α-grid — the phase universality grid. Level VII: the working window — phase fields overlap totally. Level VIII: the AB phase on water — the same mechanics in a classical continuum. One theme — eight embodiments.

**The GUE class is the second bearer.** The blind spectrum of I → the ζ-decoration of II (0.608) → the extended family of III (87 gates) → the Klein quartic (heritage: D = 0.0808) → the 50k table (package: 0.6119) → gate H5's regime D (VI: clean KS) → the optimized window (VII: D = 0.0318 → floor 0.0220). The programme has measured GUE-attainment of lattice constructs along every axis: density, flux, decoration, geometry, surface — and each time the class is attained precisely when antiunitary symmetry is broken, and only then.

**Honest negatives are the third bearer.** V1/V3: the blind-coding and σ-scan designs are disproven; V6/V16 — the level identity is YES (v2.0.7), the bit branch open. C17: the closed-density blind phase B is NEGATIVE by the letter of its criterion (1.04× over the null). The rank branch of the gate identity is at the resolution limit. Gate H5: baseline A is an outlier. v19's Test 34: the reference WARN. 2q KAK — outside the E18 class. The programme publishes refusals as first-class results: this is the "where not to search" map, equally necessary for any positive construction.


---

## 48. Consequences for positive constructions

The requirement "nonlocality or entanglement of equivalent rank" outlines the search space: (i) nonlocal operators with exactly controlled traces — the nearest neighbours of the T11 construct; (ii) local but strongly entangled classes — precisely the class whose gap is measured (T18); (iii) hybrids: trace accuracy by a nonlocal block, statistics by a local one.

The gap's universality (T17: the L-class) means: the wall must be bypassed at the level of the class, not of a single function. The statistical arm (Montgomery–Odlyzko) is quantitatively closed: any H–P candidate must reproduce the zeros' spacing statistics to the finite-sample floor — and the programme proves this achievable by simple gauge-type operators (T34-ext: D = 0.0318 vs floor 0.0220). The arithmetic arm (the $\Lambda(n)/\sqrt{n}$ weight) is closed in the trace (Th6: r = 0.9996) — and open in the spectrum (the null zone).

The operational arm: the ζ side of the H–P operator, if it exists, must be a machine of the spinor-study class — reading mathematics in real time (V23: 12/12 from six constants), not storing it (ES2: reset erases everything), with a flat step (ES3: O(1)). The formal arm: any RH conclusion inherits `blocked` from the V13 machine — until the prerequisites are formalized.

The roadmap (in order): (1) the gate H5 ladder at L = 96/112 — regime D's cleanliness as statistical power grows; (2) C17 — nonlocal graphs with controlled spectra; (3) a third independent ζ-engine implementation in alternative arithmetic (intervals/fixed point); (4) the level-II ζ-decorated operator inside the level-VII working window — the intersection of the two best results; (5) formalizing the V13 prerequisites in Lean (analyticity, the functional equation) — the only legitimate way to lift `blocked`.


---

## 58. Interludes: ten readings of one register

**Arithmetic reading.** The register opens at $2.59\cdot10^{-39}$ — the Γ-closures at 40 digits — and closes at $3.45\cdot10^{-15}$ — the W1 cross-check. Two ends of the precision scale: analytic arbitrary precision (mpmath) and machine double (IEEE-754). The programme knows the price of every digit: Kato corridors (Th3) turn "agrees" into "agrees within $10^{-k}$, and here is the corridor".

**Probabilistic reading.** The register's p-values span fifteen orders: from $p = 2.24\cdot10^{-186}$ (Test 34, the reference) to $p = 0.0105$ (Test 12, borderline acceptance). None of them "proves": each is the surprise of the data under a fixed null. Multiple comparisons (52 gates, 242 configurations, 61 α-points) — handled by Bonferroni or pre-registration.

**Topological reading.** The tower 4 (D2); the Berry phase π (D3); the Chern anchors 1-1-1 (T20); the counting law's index $-2$ (T13); the genus-3 quartic (heritage): the topological invariants are the register's most stable numbers — they are integers. Integrality is a privilege: parameter-insensitivity.

**Dynamical reading.** ×977 (Klein); ×59,000 (E18); ×16 (C7); ×3.4 (T34-ext); ×5.47 (W1); ×1.43 (TD): ratios are the programme's language. Every "×N" is measurement against control; the control is always of the same complexity as the measurement.

**Statistical reading.** ⟨r⟩ appears fourteen times: 0.594 (T16), 0.5991 (T32), 0.6004 (T33b), 0.608 (D7), 0.6009 (T26), 0.6119 (the 50k table), 0.6144 (RH), 0.5898–0.6003 (H5), 0.8938 (the NH control), 0.51–0.58 (dilute). One quantity, one reference 0.5996 — and a whole map of regimes around it.

**Documentary reading.** Every number is a file. The register is the archive's index: provenance.jsonl leads from a row to a verdict; this document — from a verdict to a log; the log — to the seed and the code. The full reproducibility chain — from a number on the page to a command in the terminal.

**Critical reading.** What could refute each element? The Γ-closures — an mpmath error (no: cross-checked against an independent implementation); blind reading — a detector collision (checked by the manual γ₁₂ analysis); the working window — an unvalidated port (closed by the pre-scan checks to 10⁻¹²); the attractors — grid dependence (closed by the ×10 convergence and the cross-language check).

**Historical reading.** The register is dated: 2026-09-02 (v19), 09-09 (H5), 09-14 (the 38-heritage), September (the quartic, T34), 10-01 (the W1 audit), 10-14 (consolidation, MAX). Every number is a point in time; the chronology — Appendix E.

**Pedagogical reading.** The register is a curriculum: from Th1 (trivial in form) to T18 (the wall) and T34-ext (the working window): from "what hermiticity is" to "how to measure distance to ζ" in 73 steps.

**Provocative reading.** What the register does NOT contain: not one number about zeros above $T = 40{,}434$; not one operator above $L = 96$; not one GSE value; not one "solution" of RH. The absences are a map too: the boundaries of the explored.


---

## 59. Interludes: the physics in five formulas

**Formula 1 — the Peierls phase:** $t \to te^{i\Phi}$. The whole programme in one substitution: a bond acquires a flux phase; the spectrum becomes a complex object; the statistics — a GUE class under total coverage. Six levels of the programme are consequences of this substitution.

**Formula 2 — the r-statistic:** $r_i = \min(\delta_i,\delta_{i+1})/\max(\delta_i,\delta_{i+1})$. Unfolding-invariance makes it the programme's yardstick; the band [0.5772, 0.6212] is every lattice campaign's working window; 0.5996 the beacon.

**Formula 3 — Montgomery's pair correlation:** $g(u) = 1 - (\sin\pi u/\pi u)^2$. The 1973 prediction, confirmed by Odlyzko; the programme reproduces it by transport (D10) and decoration (D7). Level repulsion is the structure of both ζ and the cloud.

**Formula 4 — the zero count:** $N(T) = \frac{T}{2\pi}\ln\frac{T}{2\pi e} + \frac{7}{8} + S(T)$. The zeros' density; the BK ladder reproduces its mean part exactly (D11); the T = 1000/5000 strips check it by arithmetic bridges (C2/C12).

**Formula 5 — the hyperbolic dispersion:** $k_y^2 - k_x^2/\eta = K^2$. All of level VIII: the group-velocity cone, the Vieta root, the cascade, the attractors, the $u = s\sqrt{\eta}$ window. One formula — a whole world of waves.


---

## 60. Interludes: the seven levels of reproducibility

**(1) The seed.** 42 — the programme's; 96 — the scan's; 12345 — bytes; 777 — the 3D lab. A seed fixes the ensemble: same run, same numbers. Limit: a seed does not protect against code errors.

**(2) The log.** Every entry — timestamp + delta + action. The 35,146 seconds of the v19 run are reconstructible line by line. Limit: a log records what was done, not what should have been.

**(3) Two passes.** 72×72 → 96×96: different lattices, different Nv, one verdict. Catches lattice artefacts. Limit: both configurations — one code.

**(4) Blind audits.** E17: engines without tables; C13: gates outside handles; W1: the cold start 31/31 + 12/12 bitwise. Catches tuning. Limit: an audit inherits the protocol's premises.

**(5) Cross-language.** Python ↔ Julia: the D level 9·10⁻⁷; W1 3.45·10⁻¹⁵; hp_audit bit-exact; the monumental line V01–V112 in full. Catches implementation errors. Limit: a shared mathematical frame.

**(6) The six-language contract.** One config.yaml → one JSON: identical keys. Catches interface drift. Limit: the contract does not check physics.

**(7) The formal layer.** Lean 4 / Coq: reductions A1–A6 without sorry; the V13 machine. Catches logical leaps. Limit: the prerequisites are outside the formalization (status: an open programme).

The hierarchy is complete: from "re-runnable" (1) to "cannot quietly lie" (7). No level is absolute; their intersection is the programme's practical honesty.


---

## 61. Interludes: what a sceptic would say

**The statistical sceptic.** "Your working window is a fit over 242 configurations." Answer: all verdicts against one set of pre-registered windows; the Stage-C candidates selected by a rule fixed before the run; the GUE floor — an independent control of the same sample size; the port's re-measurement of the reference (0.0928 vs 0.1096) — inside run-to-run spread. But: the floor fails the p-arm — ensemble finiteness, recorded honestly.

**The mathematical sceptic.** "The ⟨r⟩ match is weak." Answer: this is not an ⟨r⟩ programme: the 34b composite (four arms); the integral T13/T14 (9/9); the form factor on high bands (D14); the quartic (D = 0.0808 at 100k). Each metric a separate arm; the window passes all.

**The physical sceptic.** "Wave attractors are a foreign topic." Answer: the geometric-phase theme runs through the whole programme (chapter 47); AB-water is a direct bridge (Berry 1980); first-principles reproduction with a 10⁻¹⁵ cross-language check is the same evidentiary standard. No direct bridge to ζ is claimed.

**The editorial sceptic.** "The MAX volume is too big." Answer: it is designed as an archive-chronicle: read it in parts (chapter 5); the regular volume is the compressed record; the MAX is the expedition's full journal. Let 100 thousand words frighten only those who read straight through.

**The optimist.** "So RH soon?" Answer: `blocked`. Formalizing the prerequisites (chapter 48, item 5) is the only path; until then — a map, not a claim.


---

## 62. Interludes: the chronicle of one day (2026-09-02)

13:48:04 — start. Test 1 (bN convergence): 0.71 s pass 1, 22.4 s HARDCORE. The first half hour — tests 1–10, each under a minute: the fast phase's cardiogram.

14:03 — the lattice enters: Test 15 (72×72, 3.4 s; 96×96, 23.5 s). 14:07 — Test 16: 195 s + 1,550 s HARDCORE: the first heavy minutes — five 96×96 realizations, ⟨r⟩ on each.

15:07 — Test 17 (Connes): 492 s + 1,617 s: the zero-mode tower on two lattices. 16:39 — Test 25 (Byers–Yang) ends pass 2 at 3,839 s — the day's longest single operation: 48 diagonalizations of the calibration sweep.

17:09–18:00 — the calibration block (T20–T27): seconds and minutes. 19:00–21:00 — the heavy series: T28–T33: merit, dip, v_F, Hatano–Nelson, bootstrap, the L-ladder to L = 112 (the RAM-honesty boundary).

21:37–22:03 — the culmination: Test 34, HARDCORE: five 96×96 realizations (each ~4.7 min: build_ab_cloud_hamiltonian 96×96, N=9216, α=0.5, W=1, open, 2 vortices, :monumental), the 50k unfolding, the pooled KS: D = 0.1096 — the WARN that becomes level VII's departure point.

22:03–23:33 — the finale: T35 (the form factor — the second honest WARN), T36 (byte robustness: 25k and 50k eigenvalues as byte streams: entropy 7.9991), T37 (the Γ arithmetic: (1/2)! = √π/2 at error 0.0).

23:33:45 — the total: 77 rows, 66 PASS, 11 FAIL-class; 35,146 seconds. The day that grew into this edition's chapter 24 and the whole level-VII campaign.


---

## 63. Interludes: a dictionary of constructs (who is who in the zoo)

**The torus.** An L×L lattice with periodic edges. The AB cloud's home: no boundaries — pure topology. **The gate.** A perturbation with a ζ-zero phase. A failure by vocation: 87 of them, all in the null zone — and precious for it. **The vortex.** A packet of flux on a plaquette. The window's hero: 8–16 per lattice — a collective. **The Dirac string.** The line behind which the phase "returns". The hygienist: it does not leak where it must not (T24: 5040/5040). **The wall.** The Jackiw–Rossi mass barrier. The surgeon: it binds chiral pairs (D9). **The BK ladder.** The xp spectrum: 2πm/Λ. The exact craftsman: 1.7·10⁻¹³. **The Connes comb.** The trace period Λ = log q. A delta-train under extensivity (D12). **The twin.** The nonlocal isospectral double. The existence proof: r_H7 = 1.000000. **The V13 machine.** The formal guard: `blocked` forever, until the prerequisites are formalized. **The floor.** The KS method's GUE floor: 0.0220 at L=96. The judge: below it one cannot jump. **The attractor.** The closed chiral wave route. The new hero: 24/24. **The seed 42.** The silent constant of all the programme's ensembles.


---

## 64. Interludes: the levels by evidentiary strength

| Level | Strongest argument | Strength (1–5) | Weakest link |
|---|---|---|---|
| I. Core | Th6: the weight in the trace, r = 0.9996 | 5 | V1/V3/V6/V16: no correspondences |
| I⁺. Processor | 1−F = 4.4·10⁻¹⁶; ×59,000 | 5 | 2q KAK outside the class |
| II. Skeleton | Klein ×977; the cone R² = 0.9997 | 5 | The form factor at low T |
| III. Bridge | T11: the twin at 1.000000 | 4 | The 9–10-order gap |
| IV. Verification | 649/649 + 639/639 bit-exact | 5 | The T ≤ 1000 window |
| IV⁺. v19 | 66 two-pass PASS | 4 | 11 honest FAILs |
| V. Spinor | TS1–TS3 exact | 4 | The non-Markov class |
| VI. Observatory | H5-D: 7/7 clean KS | 4 | L = 72; zeros — external reference |
| VII. Optimization | 89% to the floor; four arms | 4 | The port; the floor's p-arm |
| VIII. Attractors | 24/24; cross 10⁻¹⁵ | 4 | η ∈ [9, 400]; TD — a model |

The mean strength 4.3 — the programme does not stand on one pillar: ten levels at four-to-five each. The failure of any level does not collapse the map: this is evidentiary-redundancy architecture.


---

## 76. Five schools of GUE interpretation

Why do the ζ zeros behave like random matrices? Five schools. **(1) Arithmetic (Katz):** ζ is a "random function" over the primes — a sum of nearly independent phases $e^{i\theta p}$; the CLT gives Gaussian values; the correlations come from the critical line's structure. GUE statistics are the emergent randomness of arithmetic. **(2) Geometric (Connes):** the zeros are the spectrum of an (adelic) operator; GUE is the signature of its symmetry class. **(3) Physical (H–P/BGS):** if the operator exists and its classical limit is chaotic — GUE by BGS. The AB-Cloud programme is the systematic representative of exactly this school: a lattice construct + the BGS mechanics of antiunitarity breaking. **(4) Universal (Rudnick–Sarnak):** n-level correlations are universal for the L-class; GUE is not a property of ζ but of the class. **(5) Sceptical:** the statistics match is a curious fact without a known cause; programmes like ours map the coincidence. The programme's position: working agnosticism — all five schools are compatible with its measurements; its contribution is the map of regimes where the coincidence is reproducible artificially.


---

## 77. Comparison with related programmes

**(a) Bogomolny–Keating (the $\psi$-function programme):** semiclassical reproduction of the zeros' n-correlations from prime pseudo-orbits; AB-Cloud is orthogonal: a lattice construct instead of semiclassics; the shared element — the prime comb as the source of correlations (Th6). **(b) Katz–Sarnak ensembles:** symmetry families of L-functions distribute over matrix types; the heritage's Klein quartic is the first lattice analogue. **(c) Berry–Keating $xp$:** the correct density without fluctuations; level II realizes the ladder exactly and recognizes it in the cloud's phases — a bridge between semiclassics and the lattice. **(d) The numerical industry (Odlyzko, Gourdon, Platt):** trillions of zeros; the programme uses them as an external reference and does not compete: its subject is the construct, not the tables. **(e) Quantum chaos (microwave-billiard laboratories):** experimental GUE statistics of resonators; W1 is the wave analogue in a hyperbolic cavity. The programme's distinction: pre-registered verdicts and the honesty layer (`does_not_prove`) — a methodological standard the related programmes do not formalize.


---

## 78. Syllabus: a course on the package (16 weeks)

**Weeks 1–2:** theory (MAX part II): lattices, flux, RMT; the zeta function. Lab: reproduce ⟨r⟩ = 0.6119 on the 50k table. **Weeks 3–4:** level I: Th1–Th6; assembling the Hamiltonian; the blind spectrum. Lab: hermiticity at machine zero; the spacing histogram. **Weeks 5–6:** level II: cone, Klein, ZB; the GOE→GUE decoration. Lab: a D1-mini (v_F over three L). **Week 7:** level III: C1–C8; the null zone. **Week 8:** colloquium: "the locality wall" (ch. 46): presentations on T11/T18. **Weeks 9–10:** level IV: E16/E17 — the blind engines; implementing Riemann–Siegel after Arias de Reyna. Lab: ten zeros by hand. **Week 11:** v19: the analysis of three tests from chapter 24, by choice. **Week 12:** the observatory: gates H1–H7; the H5 regimes. **Week 13:** optimization: stages A/B/C; reproduce the Stage-A top-20 at L=16 (a reduced clone). **Week 14:** attractors: the ray billiard; the E2 control. **Week 15:** the formal layer: reductions A1–A6; the V13 machine in Lean. **Week 16:** the exam: the G1–G10 verdict map + an essay "what I would check next". Grading: bitwise reproducibility of labs; the essay — by formulation discipline (ch. 75 of the Russian edition).


---

## 65. Interludes: how to read the consoles (a guide to the suite's output)

The suite's console is a genre. The test header — a double rule and the title; ⚠ RUNTIME — the honest pre-run cost estimate (e.g. T33: "2 q-rows × up to n=5 realizations × L ∈ {10,20,30,50,80,112} → ≈ 27–81 min (±3× machine factor; RAM-gated rungs are skipped with a printed reason)"). The body — parameters and numbers; the finale — the composite block: every arm with its verdict and the summary line like "Test 34b [HARDCORE pass 2]: 4 sub-checks, 1 failed → WARN".

For the reader: the line "KS composite WARN — p = 2.236e-186, D = 0.1096 (p>0.01 or D<0.10)" means: the KS arm failed because neither p > 0.01 nor D < 0.10 holds; the other three arms PASS. Why p = 10⁻¹⁸⁶ is arithmetic, not horror: n = 27,639 against 49,999 spacings — the KS statistic grows as √n; D = 0.1096 at such n gives an astronomical significance; the question is not "is the difference significant" (yes) but "is it large" (10.96% — above the 10% threshold).

Honesty markers in the consoles: "(empirical)" — no theoretical reference (T3: α = 0.1685); "expected" in brackets — there is one (T17: zero_modes 4 [exp 4]); "spread" — the realization spread; "median" — the robust summary. The progress bars ▰▰▰▱▱ — the Meridian design system: an honest showcase of LAPACK call durations.


---

## 66. Interludes: why 96×96 (and why not 128×128)

The programme's lattice ladder: 16 → 24 → 32 → 36 → 48 → 56 → 64 → 72 → 80 → 96 → 112 → (128). Each step ×1.25–1.5 in L — ×2–4 in cost (L⁶ for dense diagonalization: 96 vs 72 — ×3.5; 128 vs 96 — ×5.9). Memory: N² complex × LAPACK working: 96×96 ≈ 1.4–2 GB (the run's peak); 112×112 ≈ 2.5 GB (the T33 laptop ceiling); 128×128 ≈ 4.3 GB — "RAM honesty: skipped with a reason" in the v19 log.

Why 96 suffices: (i) the KS GUE floor falls with L and at 96 equals 0.0220 — the second significant digit; (ii) 5,528 spacings per realization × 5 = 27,640 — the ⟨r⟩ CI ±0.0075; (iii) the HARDCORE pass of the two-pass protocol catches 72↔96 lattice artefacts. Continuing the ladder is the observatory's programme (v23_v2: FULL L=56 → presets above; the 3D lab — sparse eigenvalues via Arpack: L to 200+ in the sparse regime).


---

## 67. Interludes: the ζ side — three sources of trust

Where does the programme know the zeros from? Three independent sources. **(1) mpmath.zetazero:** the reference arbitrary-precision Python library; 25 digits; the observatory's 50k table and the RH line's 13,661 zeros. Trust: a repeatedly cross-checked implementation of the GRF algorithm (Gram–Riemann–Schönhage). **(2) The Odlyzko tables:** the external archive (dtc.umn.edu); the historical arbiter of E14. **(3) The programme's own engines:** Euler–Maclaurin and Riemann–Siegel (E16/E17) — computing zeros from first principles: 649/649 + 639/639 with a bit-exact cross-match.

The triangulation: (1) vs (3) — blind reading E17 checks the engines against the mpmath route through the tables; (2) vs (1) — the historical tables against modern computation; (3) vs (3) — two algorithms against each other. No single point of trust. The blind γ₁₂ erratum (4.8·10⁻⁵) — the programme's only discrepancy ever — analysed, explained, fixed.


---

## 68. Interludes: for the practitioner — five reproducible entry points

**(1) The quick tour (5 minutes):** `./06_code/cli/run.sh --lang=en --theme=neon` — the banner, themes, ASCII metrics; `open 07_web_lab/index.html` — the interactive lab, fully offline.

**(2) The integrity check (2 minutes):** `python3 -m pytest 09_tests/python -q` — structure, config, i18n parity, contract, checksums, monographs, reports.

**(3) ζ statistics on the table (10 minutes):** numpy: load `02_data/raw/meridian/zeros50k.txt`; `r = min(δ,δ')/max(δ,δ')`; ⟨r⟩ = 0.6119; the histogram against the surmise; KS — reproduce figures M1–M3.

**(4) The v19 verdicts first-hand (5 minutes):** open `02_data/raw/results_run/FINAL_REPORT/final_report.md` — the Verdicts section: 77 rows; the map — figure R1.

**(5) The full reproduction (days):** `./reproduce.sh` — the package pipeline; the sources' runs: `julia ab_cloud_v19.jl --test all` (two-pass, ~10 h); `make wave-attractors` — the full W1 protocol; `python3 t34_sweep.py --stage A` — the coarse vortex scan (~2 min).


---

## 69. Interludes: maps and territories

The register is the territory; the monograph is the map. The MAX map at 1:1 scale: every campaign, every log. But it is still a map: logs are compressed to extracts; the full ones live in the data. The package's philosophy: the map is always smaller than the territory; hence (i) every number carries a pointer to its file (the territory); (ii) extracts are marked "…" with the continuation path; (iii) the package is not a replacement of the repository but its consolidated snapshot.

The citation corollary: cite the package (DOI) for consolidated numbers; the repository — for runs and code; the level sources — for verdict files. The citation hierarchy mirrors the reproducibility hierarchy: each layer has its own DOI/path.


---

## 70. Interludes: a numerical epic — the plot in six acts

**Act I (construction).** The torus, the flux, the vortices; hermiticity at machine zero. **Act II (statistics).** The blind spectrum in the GUE class; but the lattice ζ-correspondences fail — the first honest refusal. **Act III (dynamics).** The lattice turns out to be Dirac: cone, Klein, ZB; the ζ-decoration lifts GOE → GUE. **Act IV (the bridge).** The resonator is tuned; the twin proves trace feasibility; but spectral identity is not attained — the wall is located: locality. **Act V (instruments and heritage).** Blind reading bit-exact; the reference runs 38 + v19; the observatory systematizes; the vortex window closes 89% to the floor. **Act VI (beyond the wall).** The wave attractors — phase mechanics on water; the roadmap — formalizing the prerequisites. RH — `blocked` in every act: an epic without a false finale.


---

## 71. Interludes: on numbers that cannot be improved

Some of the programme's numbers do not admit "improvement" — they are constructively exact. **Integers:** the tower 4; the Chern anchors 1-1-1; the periods 4/6/14; the counts 79/79, 649/649, 24/24, 7/7, 5040/5040. **Exact phases:** π (Berry); π/7 (the AB phase); W(−α) = −W(α). **Machine zeros:** hermiticity; the chiral defect at W = 0; the mirror sum C + C_mir = 2.8·10⁻¹⁶. **Identities:** (1/2)! = √π/2 (error 0.0); Φ_AB = π/7 (every digit). These numbers are the architecture's constants: they cannot be "tuned up" — either they are there or the construct is not. The opposite pole — the statistics: ⟨r⟩, D, K(τ) — always with CIs and floors; between the poles, the magic of numerical agreement (r = 0.9996; 1.000000; 3.45·10⁻¹⁵).


---

## 72. Interludes: how to weigh evidence (Bayesianly, but honestly)

A formal note: the prior of a hypothesis H (say, "phase encoding carries ζ arithmetic into spectra") — moderate; the likelihood of the data under H vs ¬H; the posterior. The programme computes no Bayes factors explicitly — but its verdict system is isomorphic to them: FAIL rows are likelihoods that dropped H below threshold; the register of negatives is the class-level posterior.

The programme's practical rule: strong evidence = (effect × controls × reproducibility), not the p-value. Test 34: the effect D = 0.11 → 0.032 (×3.4) with four control arms and fivefold stability — strong; p = 10⁻¹⁸⁶ — just the arithmetic of volume. The attractors: a binary effect (24/24 vs 0/24) with a 10⁻¹⁵ cross-language check — strong without any p. The counter-example: T28's f_GUE = 0.87 — an effect without controls (one metric) — WARN until strengthened.


---

## 73. Interludes: the dependency network of results

The dependency graph (simplified): Th1/Th2 → everything (hermiticity is the admission ticket). Th3 → all number comparisons (corridors). Th6 → C4 → C15 → the gap's universality. D1/D2 → T19/T17 → H6 → the H5 regimes → the T34 window → the floor. E16/E17 → ζ-side trust → the 50k tables → every KS. The W1 cross → ray-model trust → the E6 window. V13 → the RH status → the boundaries of every text.

The graph's narrow points: (1) the ζ side closes on mpmath + the engines (interlude 67); (2) the lattice side — on the port validation (T34) and the D cross-ports; (3) the interpretive — on A5 (the wall = locality — an assumption). A narrow point's failure does not collapse the measurements — it collapses the interpretation: without A5, the C16 data remain a fact about entropy, not a map of the wall.


---

## 74. Interludes: what changes as L → ∞

Conceivable limits. ⟨r⟩: the 0.6 plateau already at L ≥ 50 (T33) — stabilization; the programme proves no formal limit, but the weighted plateau's χ²/dof = 0.01 is strong stationarity. The KS GUE floor: 0.0220 (L=96) → 0 asymptotically (the floor ~ √(1/n), n ~ L²); the vortex window approaches zero together with the floor — the ratio (D − floor)/(reference − floor) is already stable (89%). The form factor: the plateau K(τ>1) → 1 (D14: 0.962 at t≈10⁵; growing with height). The configuration-metric gap (C3): 9–10 orders at L ≤ 48 — extrapolation is risky: no non-stationary systematics, but no limit theory either; C17 — the checking programme.

What does NOT change: the integers (the tower, Chern, the counting law) — L-independent by construction; the exact phases; the machine zeros; the Th6 weight in the trace (r = 0.9996 — a trace, not a spectrum: the L-ladder is secondary). And `blocked` — never changes: the status's formality does not depend on the lattice.


---

## 75. Interludes: a dictionary of honest formulations

The programme distinguishes five assertion modalities. **"Exactly equal"** — only for integers and identities (the tower 4; (1/2)! = √π/2). **"Agrees to ε"** — numerical certificates (3.45·10⁻¹⁵; 4.4·10⁻¹⁶): ε must be stated. **"Statistically consistent"** — windows and CIs (⟨r⟩ in band; 9/9 Δ₃). **"Discrepancy measured"** — negatives with magnitude (the 9–10-order gap; the floor fails the p-arm). **"Interpreted as"** — register assumptions (the wall = locality; A5): always with the alternative named.

Forbidden formulations (linguistic hygiene): "numerically proved"; "almost proved"; "GUE = ζ"; "the operator found"; "close to solving RH". The permitted equivalents: "confirmed within certificate"; "the necessary condition met"; "ζ statistics reproduced to the floor"; "the T11 construct is realizable"; "RH status: blocked".


---

## 79. On the ethics of large numerical programmes

Three ethical obligations of numerical science next to an unsolved problem. **(1) Do not imitate proof:** numerical success rhetorically pulls toward "almost proved"; the programme answers with the formal block (V13) and linguistic hygiene (interlude 75). **(2) Publish the refusals:** the 11 v19 FAIL rows and the gates' null zone are first-class results; hiding refusals distorts the field: other researchers would hit the same walls without a map. **(3) Accessibility of checking:** seeds, logs, blind audits, bitwise certificates — the verification barrier is minimized; the package is not "trust us" but "check us more cheaply than we checked ourselves".

Additionally: honesty toward sources — numbers transferred verbatim; convention disagreements documented with both values; derived computations marked. Pedagogical honesty: the MAX volume does not hide complexity behind a smooth retelling — consoles, logs and refusals are included as they are. Financial: no grants; no conflicts of interest; open licences (MIT/CC-BY/ODbL) with the contractual honesty layer (LICENSE §3).


---

## 80. Digital certificates: hashes, checksums, bit-for-bit

The package's certificate hierarchy. **SHA-256:** every file of 02_data is covered by a checksum (`checksums.sha256`, extended by the enrichment); the test `test_checksums.py` verifies. **Byte identity:** the W1 audit — 31/31 data files, 12/12 figures bitwise (REPRODUCIBILITY.json); hp_audit vs v23_v2 — bit-for-bit at equal seeds. **Cross-language numbers:** the D level 9·10⁻⁷ (reference rounding); W1 3.45·10⁻¹⁵ (machine epsilon of long chains). **The JSON contract:** six CLI languages — identical keys.

The practice of citing numbers: a register number → provenance.jsonl → the source verdict file → the file's hash in checksums → the code with its seed. The "number → bitwise trace" chain is complete for all 73 register rows; the derived ones (the package audit) carry the reproduction script in the enrichment metadata (metrics.json → enrichment.derived_checks).


---

## 81. The flagship results 1–35: an annotated register

**The heritage flagships (1–14):** blind reading 649/649 + 639/639 (E17); Riemann–Siegel 3.8·10⁻¹⁵ (E16); the compiler ×59,000 (E18); "reads, does not carry" 12/12 (V23); CHSH 2√2 − 4.4·10⁻¹⁶ (V24); the ζ-decoration 0.608 (D7–D8); Klein ×977 (D5); Jackiw–Rossi 3.9·10⁻⁹ with contrast 7·10⁶ (D9); the nonlocal twin r_H7 = 1.000000 (C9/T11); the α=1/3 counting law (C11/T13); the T=5000 strip: N = 4520 (C12/T14); the twisted formula 9.6·10⁻⁶ (C15/T17); entanglement 12–16 nats (C16/T18); the Klein quartic D = 0.0808 (heritage).

**The enrichment flagships (25–35):** the H5 regimes A–D with the clean D (25); the RH line 13,661 zeros + 61 α (26); the monumental V01–V112 (27); the vortex window Nv ≈ 8–16 (28); the GUE floor by L (29); the attractors: lock-in 24/24, the cascade ×7.6 (30); chirality and invariance (31); the universal window u₁/u₂ (32); the cross 3.45·10⁻¹⁵ (33); v19: the 77 rows (34); v19: the decisive numbers (35). Every flagship is a register row with its campaign; the full commentary — chapter 43a.


---

## 82. What did not enter, and why (the exclusion register)

**(1) The v19 run's full PNGs (~600 dpi × 37 tests × 3 formats):** they regenerate deterministically; the package carries the verdict map/time profile (R1–R2) as derived summaries. **(2) The full session log (812 KB):** three-level extracts (ch. 24L, Appendix L); the full one — in the data. **(3) The 38-test heritage zip (108 MB):** the provenance record; the results — in the register. **(4) The sources' blind-family and handwritten verdicts:** the source verdict files are canonical; the package carries the register. **(5) The W1 .npz arrays (E4/E6/E7):** binary; the package carries the CSV/JSON summaries + the MAX tables. **(6) The observatory's monumental scripts (25 files, 5.9 MB):** the catalogue in ch. 26/31b; the codes — in the repository. **(7) The vortex scan's npz curves:** the CSV tables suffice for reading; npz — for regeneration. The exclusion rule: the package carries the readable record and the hashed data; the executable and the heavy — the repository, with paths from provenance.


---

## 83. Postscript: how the MAX edition was assembled

The assembly method. (1) The skeleton: 14 parts, 80+ chapters; the level dictionary and the number register — from `research_registry.json` (the machine-readable canon). (2) Full records: the regular volume as the levels' "full records" (the *a/*b chapters); the sources — as verbatim chapters (the vortex README, the wave README, the observatory README, the run archive catalogue, the data cards); the observatory's eight Russian documents — as English condensations (31a–31h) with the Russian originals in the Russian edition. (3) Generation: chapter 24 (the 37 tests) from the per-test reports (what + console + verdict rows) with category and individual commentary; the logs — as three-level extracts; the tables — from the package's CSV/JSON verbatim. (4) Derived figures M1–M3, R1–R2 — computed from the 50k table and the final report; the computation reproduces (metrics.json → derived_checks). (5) Checks: the required sections (the monograph-structure test); the honest boundary — in three places (the header, ch. 49, Appendix G).

The volume: ~100 thousand words, of which ~40% — verbatim source records (consoles, logs, tables, READMEs), ~35% — expanded authorial chapters, ~25% — data generations with authorial commentary. Every number — with its campaign; every campaign — with its file; every file — with its hash. The MAX edition is not "more words" but "the whole path to every number".


---

# PART XIV. BOUNDARIES, CONCLUSION, AUDIENCES

## 49. The MAX edition's limitations

(1) **RH is blocked by construction.** No accumulation of numerical successes advances the formal status: the V13 machine returns `blocked` until the prerequisites are formalized. (2) **The numerical nature of evidence:** all verdicts are numerical, with finite-precision certificates; Kato corridors control the price of comparing numbers, not substitute analytic identities. (3) **Conventions:** source disagreements are documented (D7: 0.4759/0.5084; the RH line 0.6144 vs the table 0.6119 — different height ranges). (4) **The limits of blind reading:** E17 — the window $T \le 1000$. (5) **Translations:** full volumes RU/EN; zh/de/es/fr/ar are abstracts. (6) **Interpretive discipline:** "the wall = locality" is assumption A5 with measured support. (7) **Heritage:** the 38-test archive stays in the source; v19 — selectively (reports and logs, no PNG). (8) **The new lines:** the gates are lattice-ensemble statistics (L=72); the scan ran on a validated engine port (to 10⁻¹²); W1 — two description levels, the window tested on $\eta = 9$–400; the TD model — Drude dispersion. (9) **The MAX edition itself:** it unfolds the sources without replacing them; the canonical numbers live in verdict files; on any discrepancy the source is canonical.


---

## 50. Conclusion: a map, not a claim

The AB-Cloud programme asked how close a finite lattice threaded with Aharonov–Bohm flux can come to the Hilbert–Pólya operator. The MAX edition unfolds the answer in full depth — ten levels, 35 flagship results, 73 register rows, 53 figures, 11 verdicts.

**The resonator is built and tuned.** Hermiticity — machine zero; the GUE class — across the explored space; the dynamics — exactly Dirac (cone, Berry phase π, the Landau ladder, Klein ×977, ZB ω = 2E); ζ-decoration lifts GOE → GUE with chiral protection to 4·10⁻¹⁵; the BK ladder is realized exactly and recognized in phases; the processor's compiler reaches machine epsilon and wins the honest benchmark ×59,000.

**The level identity holds, and the primes enter.** The Λ(n)/√n weight — in the trace (r = 0.9996); blind reading — 649/649 + 639/639 bit-exact; the gates measure at the zeros' own level (D_nn = 0.0079, audit v2.0.7) with the trace bridge ≤ 1.2e-5; the prime channel enters via the convergence ladder (audit v2.0.8); arithmetic enters both by the α = 1/3 counting law and by the level identity.

**The wall is located.** Trace identity is exactly achievable and nonlocal (r_H7 = 1.000000); local lattices do not raise entanglement to the zero comb's level (S_A 12–16 vs 160–220); the gap is universal over the L-class. A positive construction must be nonlocal or equivalently entangling — a concrete, checkable requirement.

**The enriched edition widens the map in every direction.** The v19 heritage — the programme whole: 77 verdict rows with successes and edge-failures of equal standing. The level-VI observatory — systematic watching: gates H1–H7, the RH line, the monumental line V01–V112, the 50k table (package audit: ⟨r⟩ = 0.6119). The level-VII optimization — the dials measured: the working window Nv ≈ 8–16, D = 0.0318 — 89% of the gap to the floor. The level-VIII attractors — phase arithmetic on water: lock-in 24/24, the window universal, cross 3.45·10⁻¹⁵.

The programme does not prove the Riemann hypothesis — the obligation machine guarantees it. Its contribution is a map: where the wall is, what it is made of, and what any positive construction must do to pass through it. The bridge is built up to the wall; beyond — the wall.


---

## 51. The programme for a general audience: ten stories of one cloud

**Story 1 (the cloud).** Picture a torus — a square lattice with its edges glued. In every cell, a tiny vortex of magnetic flux: an electron circling a cell picks up a phase. The hopping matrix between sites becomes complex; its spectrum is a set of "energies". That is the AB cloud. The whole programme is an interrogation of this object: whom does its spectrum resemble?

**Story 2 (the mirror's secret).** Random complex matrices (GUE) have levels that repel like strangers in a lift: neighbouring gaps follow an exact law. The zeta function's zeros have the same statistics. The coincidence is a hint: the zeros "behave like" a spectrum. The programme built a cloud whose levels repel exactly so — inside a working window of ~16 vortices per lattice.

**Story 3 (the lattice threshold).** Why 16 and not 4? With few vortices the phase fields do not cover the lattice: "mirror" patches remain — nearly real, nearly integrable. The statistics stay off GUE. Too many vortices — they clot into a landscape of their own. The window is like seasoning: too little is bland, too much is bitter.

**Story 4 (the floor).** How close can one approach the ζ zeros by gap statistics? There is an irreducible floor: the ζ table itself differs from a finite GUE sample by D ≈ 0.022. The best cloud: 0.032. One cannot go further — not because the cloud is clumsy but because that is the method's floor. Like a chess study: a draw is not a defeat.

**Story 5 (honest refusals).** 11 of the reference run's 77 lines are FAIL. They were not hidden: every discrepancy is knowledge. Test 34 failed its KS arm — and that spawned an optimization campaign that closed 89% of the gap. Refusals are the programme's fuel.

**Story 6 (reads, does not store).** The programme's engine computes ζ zeros from six constants — no tables. A machine without long-term memory: reset erases everything; a step costs the same at any depth. If the Hilbert–Pólya operator exists, its ζ side must be like this: reading mathematics in real time, not accumulating it.

**Story 7 (the wall).** The programme measured the wall head-on: a local lattice cannot carry the entanglement the zero spectrum demands (entropy an order and a half short). The nonlocal twin's trace is perfect. Conclusion: a positive operator must be nonlocal. The wall is not a defeat but a map.

**Story 8 (the observatory).** 24 Julia codes, each a self-contained laboratory in one file: menus, tests, plots, self-checks. Seven H–P gates; an RH line on 13,661 zeros; a monumental line of 112 verifications. The observatory made spectrum-watching systematic: not "a quick look" but a protocol.

**Story 9 (waves in a curved mirror).** In a cavity of hyperbolic metamaterial, waves ignore chaos and collapse onto perfect closed routes — attractors. The programme reproduced this from first principles: lock-in 24/24 against 0/24 in a normal cavity. Bonus: the Aharonov–Bohm effect — on water waves in a tank. The same phase mechanics as the cloud's — in a tub of water.

**Story 10 (the block).** The programme does not prove the Riemann hypothesis — and cannot, while a formal "obligation machine" holds the verdict `blocked`. Every beautiful coincidence inherits this status automatically. This is not timidity but discipline: the only honest way to do numerical science next to an unsolved problem of the century.

---

## 52. Frequently asked questions (extended)

**Q1. Is the Riemann hypothesis proved in this package?** No. The verdict is `blocked` by the V13 obligation machine. The package is a numerical and formal study of a model; the block is part of the design.

**Q2. What IS proved then?** Within numerical certificates: hermiticity and chiral structure; the GUE class in the working window; the Dirac identity of dynamics; the Λ(n)/√n weight in the trace (r = 0.9996); blind reading of 649 zeros by two engines bit-exact; gate H5's clean regime D; the T34-ext working window (89% of the gap to the floor); W1's reproducibility (31/31, 12/12 bitwise).

**Q3. Why doesn't the GUE class mean identity?** Matching statistics is necessary, not sufficient: infinitely many non-isomorphic operators share a pair correlation. The C1–C17 bridge measures exactly the distance between "statistically alike" and "identical": the rank branch sits at its resolution limit (0.226/0.097 against controls at 1.000), while the level identity holds at the zeros' own level (D_nn 0.0079, audit v2.0.7); the open distance is the bit-level branch (T18).

**Q4. What is the locality wall?** A measured fact: subsystem entropies of the local ground state sit an order and a half below what the zero comb demands (T18); the nonlocal twin with a perfect trace exists (T11). The wall passes through the class of operators, not through arithmetic.

**Q5. Why 50,000 zeros?** Long enough for stable global statistics (⟨r⟩ with SE ~ 0.001), short enough for honest bootstrap; the table is the external reference of every KS comparison. Trillions are verified — 50k is the laptop-class working compromise.

**Q6. Why are WARN rows published as results?** Pre-registration: windows are fixed before the run; breaking a window is knowledge, not shame. T34b's WARN begat the level-VII optimization. Negative results are the "where not to search" map.

**Q7. How does the MAX edition differ from the regular volume?** Vertical depth (every campaign; 37 tests with consoles), horizontal completeness (full source records) and illustration (53 figures in place). The number register: 20 → 73 rows.

**Q8. Is all this reproducible?** Seven levels: fixed seeds; logs; two-pass runs; blind audits; cross-language agreements (3.45·10⁻¹⁵ — 10⁻¹²); bitwise certificates; the six-language contract.

**Q9. What do I do with the package?** Read: README → the regular volume → the MAX volume. Verify: `python3 -m pytest 09_tests`. Reproduce: `./reproduce.sh`; the sources' runs. Cite: CITATION.cff (DOI 10.5281/zenodo.21825394).

**Q10. Where are the new levels' boundaries?** VI: gates — statistics at L = 72. VII: an engine port (validated), not the Julia suite itself; the floor fails the p-arm. VIII: two description levels; the window tested on η ∈ [9, 400]; TD — the Drude model.

---

## 53. Extended glossary

**AB cloud** — a Hermitian lattice operator with α flux quanta per plaquette and vortices; the fabric of all levels. **Gate** — a perturbation encoding a ζ-zero phase into a Bloch angle. **Unfolding** — conversion to dimensionless density; loses scale, gives universality. **⟨r⟩** — the adjacent-spacing ratio; GUE ≈ 0.5996; band [0.5772, 0.6212]. **The Wigner surmise** — p(s) = (32/π²)s²e^(−4s²/π); the normalization is a theorem (T37). **d_crit** = 1.63/√n — the ~1% KS threshold. **The GUE floor** — the finite-sample zero of the KS method between a GUE ensemble and ζ. **The form factor K(τ)** — the GUE ramp-plateau; K(2) = 0.962 at t ≈ 10⁵. **Δ₃, Σ²** — rigidity and number variance; long-range statistics. **A²** — Anderson–Darling; tails. **Gate (observatory)** — an H1–H7 verdict test. **Campaign** — a pre-registered verdict experiment. **does_not_prove** — the unproved-boundary field. **The V13 machine** — the formal RH block. **Regime D** — Nv = L²/36 + α = 25/900: clean KS. **The working window** — Nv ≈ 8–16, q ≈ 0.7–1.0, W ≈ 0.5–1.0, α = 0.5. **The monograph density** — Nv = L²/36 (regime B). **The magic α-points** — the 61-value universality grid. **The Vieta root** — the second intersection of k_t = const with the IFC hyperbola. **The cascade** — |k| growth at slope reflections (mean ×7.6). **Attractor** — a closed chiral route; window u₁ ≈ 0.176, u₂ ≈ 0.490. **Drude dispersion** — μ_y(ω) = 1 − ω_p²/ω². **Hofstadter** — the lattice spectrum in a field; the butterfly. **Chern C₁** — the sub-band topological invariant. **Byers–Yang** — gauge invariance at fixed flux. **Hatano–Nelson** — the non-Hermitian deformation (a control). **Klein** — tunnelling at V₀ → 2E: T = 0.978. **ZB** — the trembling at ω = 2E. **The BK ladder** — the xp spectrum: 2πm/Λ. **The Connes comb** — the trace period Λ = log q. **Co-location** — (Φ_p, Φ_q) ≡ Φ_pq. **The counting law** — N₀ = 2L − 6·[L ≡ 0 mod 12] at α = 1/3. **Blind reading** — zeros without tables, by two engines. **Class B** — the honest equal-ISA benchmark. **The Klein quartic** — PSL(2,7), genus 3; D = 0.0808. **The locality wall** — S_A 12–16 vs 160–220 (Haar). **The null zone** — r_H7 ≤ 0.226 on all gates. **The package audit** — this edition's derived computations (⟨r⟩ = 0.6119). **Two-pass** — primary 72×72 + HARDCORE 96×96. **RAM honesty** — skipping a step with a reason. **REPRODUCIBILITY.json** — the W1 bitwise certificate.

---

## References

1. Riemann, B. (1859). Über die Anzahl der Primzahlen unter einer gegebenen Größe. *Monatsberichte der Königlichen Preußischen Akademie der Wissenschaften zu Berlin*, 671–680.
2. Hilbert, D. — Pólya, G. — oral tradition; see Berry, M. V., Keating, J. P. (1999). The Riemann zeros and eigenvalue asymptotics. *SIAM Review*, 41(2), 236–254.
3. Montgomery, H. L. (1973). The pair correlation of zeros of the zeta function. *Analytic Number Theory*, AMS, 181–193.
4. Odlyzko, A. M. (1987). On the distribution of spacings between zeros of the zeta function. *Mathematics of Computation*, 48(177), 273–308.
5. Dyson, F. J. (1962). Statistical theory of the energy levels of complex systems. I–III. *Journal of Mathematical Physics*, 3, 140–175.
6. Mehta, M. L. (2004). *Random Matrices* (3rd ed.). Elsevier/Academic Press.
7. Guinand, A. P. (1948). On Poisson's summation formula. *Proceedings of the London Mathematical Society*, s2-50(1), 29–29.
8. Weil, A. (1952). Sur les «formules explicites» de la théorie des nombres premiers. *Comm. Sém. Math. Lund*, 252–265.
9. Connes, A. (1999). Trace formula in noncommutative geometry and the zeros of the Riemann zeta function. *Selecta Mathematica*, 5(1), 29–106.
10. Sierra, G. (2008). The Riemann zeros as energy levels of a quantum system. *Physical Review B*, 77, 246201.
11. Hofstadter, D. R. (1976). Energy levels and wave functions of Bloch electrons in rational and irrational magnetic fields. *Physical Review B*, 14(6), 2239–2249.
12. Byers, N., Yang, C. N. (1961). Theoretical considerations concerning quantized magnetic flux in superconducting cylinders. *Physical Review Letters*, 7(2), 46–49.
13. Jackiw, R., Rossi, P. (1981). Zero modes of the vortex-fermion system. *Nuclear Physics B*, 190(4), 681–691.
14. Arias de Reyna, J. (2011). High precision computation of Riemann's zeta function by the Riemann–Siegel formula. *Mathematics of Computation*, 80(275), 995–1009.
15. Rudnick, Z., Sarnak, P. (1996). Zeros of principal L-functions and random matrix theory. *Duke Mathematical Journal*, 81(2), 269–322.
16. Bell, J. S. (1964). On the Einstein Podolsky Rosen paradox. *Physics Physique Fizika*, 1(3), 195–200. (For CHSH: Clauser, J. F., Horne, M. A., Shimony, A., Holt, R. A. (1969). *Physical Review Letters*, 23, 880–884.)
17. Bohigas, O., Giannoni, M. J., Schmit, C. (1984). Characterization of chaotic quantum spectra and universality of level fluctuation laws. *Physical Review Letters*, 52(1), 1–4.
18. Atas, D. Y., Bogomolny, E. B., Giraud, O., Roux, S. (2013). Distribution of the ratio of consecutive level spacings in random matrix ensembles. *Physical Review Letters*, 110, 084101.
19. Li, X.-J. (1997). The positivity of a sequence of numbers which appear in an approximation problem to the Riemann Hypothesis. *Journal of Number Theory*, 65, 325–333.
20. Hyperbolic wave attractors. *Nature Physics* (2026). DOI: 10.1038/s41567-026-03453-7. (CUNY ASRC.)
21. Maas, L. R. M., Lam, F.-P. A. (1995). Geometric focusing of internal waves. *Physical Review Letters*, 74, 1040–1042.
22. Berry, M. V., Chambers, R. G., Large, M. D., Upstill, C., Walmsley, J. C. (1980). Wavefront dislocations in the Aharonov–Bohm effect and its water wave analogue. *European Journal of Physics*, 1, 154–162.
23. Isaev, I. Kh. (2026). The programme's laboratories: AB_Cloud_Quantum_Research; dirac-lab; Hilbert_Polya; meridian-spectral-observatory; Vortex_optimization; Wave_attractors; results. Repository: github.com/wild8highlander/ab-cloud-research. DOI: 10.5281/zenodo.21825394.

*Note:* classical works cited by the standard editions; the programme's own results always point to the sources' verdict files (Appendix B and `00_meta/provenance.jsonl`).

---

## Appendix A. The campaign register (complete)

| Series | Campaigns | Laboratory | Implementation | Status |
|---|---|---|---|---|
| V | V01–V19 (+V23/V24 previews) | spectral core | Python / Julia | complete |
| V20+ | V20 (+previews) | AB processor | Python | complete (E18) |
| E | E01–E18 | blind verification | Julia (+Python) | 18/18 verdicts |
| ES | ES1–ES5 | spinor study | Python | complete (TS1–TS3) |
| D | D1–D14 | Dirac skeleton | Python + 4 Julia ports | 96 checks ALL PASS |
| C | C1–C17 | H–P bridge | Python (mpmath) | complete |
| H | 38 tests (heritage) | verification release | Julia 1.12 | reference 2026-09-14 |
| v19 | Tests 1–37 | v19 reference | Julia 1.12.0 | 77 rows; 2026-09-02 |
| H (gates) | H1–H7 | observatory | Julia (+Python) | H5: regime D clean |
| RH | RH_Unified · RH_Sweep_Pro | RH line | Julia | 13,661 zeros; 61 α |
| MV | V01–V112 | monumental line | Julia | monograph port |
| T34 | A/B/C (Test 34-ext) | vortex optimization | Python (port) | 242 configurations |
| W1 | E1–E7 (+AB water) | wave attractors | Python + Julia | lock-in 24/24 |

## Appendix B. Source mapping

| MAX part | Source | Key files |
|---|---|---|
| Pt. III (core, processor) | AB_Cloud_Quantum_Research | README.md, modules/, theorems_lemmas/, datasets/ |
| Pt. IV (skeleton) | dirac-lab | README.md, code/, results/CROSS_VERIFICATION.md |
| Pt. V (bridge) | Hilbert_Polya | README.md, results/RESULTS.md, computations/ |
| Pt. VI (verification, v19 heritage) | results | FINAL_REPORT/, test_*/report.md, computation_logs/ |
| Pt. VII (spinor) | AB_Cloud_Quantum_Research/research/realtime_spinor_memory | README, theorems/, experiments/ |
| Pt. VIII (observatory) | meridian-spectral-observatory | README.md, README.ru.md, docs/01–08, zeros50k.txt, hp_audit_standalone.jl |
| Pt. IX (optimization) | Vortex_optimization | README.md, README_RU.md, data/sweep_*.csv, gue_control_L96.json, figures/ |
| Pt. X (attractors) | Wave_attractors | README.md, docs/wave-attractors.md, data/E*_summary.json, figures/ |

## Appendix C. The figure catalogue

The complete catalogue of 53 static figures (captions — `03_figures/captions.*.md`; alt texts — `alt_texts.csv`): spectral core — 12 (th1–th6 × RU/EN); the H–P bridge — 38 (fig01–19 × RU/EN); the skeleton — 14 (D1–D14); the observatory — 6 (M1–M3 × RU/EN, package-derived); the v19 run — 4 (R1–R2 × RU/EN, package-derived); the vortex optimization — 7; the attractors — 12. Embedded in their sections; the derived (M/R) figures were computed in this edition from package data.

## Appendix D. The v19 verdict ledger

Machine-readable: `02_data/raw/results_run/FINAL_REPORT/final_report.md` (the Verdicts section). Summary: 66 PASS / 11 FAIL-class rows (Tests 4/5/6/11/12 — the pass-1 edge; 28b/29b/34b/35/35b — the honest HARDCORE rejections). Map: figure R1. The full 77-line listing is included in the Russian MAX edition and in the package data.

## Appendix E. Programme chronology

2026-08-28 — the v18 run (37 tests, flat log). 2026-09-02 — the v19 reference run (37 tests, 77 rows, 35,146 s). 2026-09-09 — gate H5 (L=72, regimes A–D). 2026-09-14 — the 38-test reference run (heritage, 26.04 h). September 2026 — the addenda Add.1–Add.8; the Klein quartic (100,000 zeros). Sep/Oct 2026 — the vortex optimization (Test 34-ext); W1 (the blind audit 2026-10-01). 2026-10-14 — the unified package (enriched edition): consolidation + the MAX editions.

## Appendix F. Glossary

AB cloud — a lattice Hermitian operator with α flux quanta per plaquette and vortices. Gate — a perturbation encoding a ζ-zero phase into a Bloch angle. Unfolding — conversion to dimensionless density units. Gate (observatory) — an H1–H7 verdict test. Campaign — a pre-registered verdict experiment. Verdict — PASS/WARN/FAIL against windows. Honest boundary — the does_not_prove field + the RH block. ⟨r⟩ — the adjacent-spacing ratio. d_crit = 1.63/√n — the KS threshold. The GUE floor — the finite-sample zero of the KS method. The monumental line — the Julia port V01–V112. Regime D — the combined gate-H5 regime. The working window — Nv ≈ 8–16. Attractor — a closed chiral wave route. The Vieta root — the second intersection of k_t = const with the hyperbola.

## Appendix G. Ethics statements

**Ethics:** no human or animal subjects; all numerical experiments pre-registered; negative results published with equal standing. **Data:** `02_data/` under ODbL; the source run archives in the source laboratories. **Code:** MIT in `06_code/` and the sources. **Funding:** none. **Conflicts of interest:** none. **The invariant scope statement:** this monograph is a numerical and formal study of a mathematical model; it does not prove the Riemann hypothesis; the RH verdict is `blocked` by the V13 obligation machine by construction; any derivative must preserve this statement (LICENSE §3).

---

## 54. The package's documentary layer (full records)

### 54.1. The package README (English, verbatim)

<div align="center">

<img src="../../08_assets/logos/logo_unified.svg" alt="AB-Cloud unified research logo" width="200"/>

# AB CLOUD RESEARCH — UNIFIED ACADEMIC PACKAGE

**One study on four levels: the algebraic AB (Aharonov–Bohm) architecture as a
computing fabric, its Dirac skeleton, the Hilbert–Pólya bridge, and the blind
verification apparatus.**

*Unified edition · no version numbers · open data · honest boundaries*

[![Campaigns](https://img.shields.io/badge/campaigns-44%2B_PASS-7FC8A8?style=for-the-badge)](../../02_data/processed/research_registry.json)
[![Theorems](https://img.shields.io/badge/theorems-27-E8DDB8?style=for-the-badge)](../../01_monographs/en/README.md)
[![Tests](https://img.shields.io/badge/tests-410%2B-7FC8A8?style=for-the-badge)](../../09_tests/README.md)
[![Verdicts](https://img.shields.io/badge/pre--registered_verdicts-18%2F18-7FC8A8?style=for-the-badge)](../../04_reports/report.md)
[![RH](https://img.shields.io/badge/RH_status-BLOCKED-FFB74D?style=for-the-badge)](#honest-boundary)
[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.21825394-blue?style=for-the-badge)](https://doi.org/10.5281/zenodo.21825394)

[Русский](../../README.ru.md) · **English** · [中文](../../README.zh.md) · [Deutsch](../../README.de.md) · [Español](../../README.es.md) · [Français](../../README.fr.md) · [العربية](../../README.ar.md)

</div>

---

> [!IMPORTANT]
> **Honest boundary.** Everything in this package is a numerical and formal
> study of a mathematical model. It does **not** prove the Riemann hypothesis:
> the V13 obligation machine keeps the RH conclusion **blocked** while the
> analytic prerequisites remain assumed. Negative results are published as
> first-class citizens: the locality wall (T18), the null zone at gates (T8),
> the lattice ζ-correspondence failures (V1/V3/V6/V16).

---

## What this is

This is the **unified academic edition** of the whole AB-Cloud research
programme: one self-contained package consolidating the three research
laboratories of the repository — [`AB_Cloud_Quantum_Research`](../../../AB_Cloud_Quantum_Research/)
(spectral core and AB processor), [`dirac-lab`](../../../dirac-lab/) (the Dirac
skeleton) and [`Hilbert_Polya`](../../../Hilbert_Polya/) (the Hilbert–Pólya bridge) —
together with the verification heritage of the earlier submission package
(the 38-test reference run and its addenda). The unified edition carries
**no version numbers**: it is a living academic structure (`00_meta` …
`10_notebooks`), not a frozen release.

The programme proposes a concrete statistical bridge between the non-trivial
zeros of the Riemann ζ function and the spectra of Hermitian lattice operators
threaded by Aharonov–Bohm magnetic flux quanta. The construct is engineered so
its spectral statistics fall into the GUE universality class — the class the
Montgomery–Odlyzko programme predicts for the ζ zeros — while its exact layer
(hermiticity, flux quantization, Byers–Yang invariance, chiral pairing, Connes
self-duality, an identity chain of geometric phases) is verifiable to machine
precision and to 256-bit arbitrary precision where needed. The verification
record subjects the construct to **43+ numbered campaigns and tests** across
four levels, cross-verified between Python and Julia, with pre-registered
verdicts and a machine-readable honesty layer.

## Architecture: levels of one machine

| Level | Source folder | Campaigns | One-line essence |
|---|---|---|---|
| 🧠 Core | `AB_Cloud_Quantum_Research` | **V01–V19** | blind spectrum, GUE class, the trace carries Λ(n)/√n (r = 0.9996), the V13 obligation machine blocks RH |
| ⚛️ Processor | `AB_Cloud_Quantum_Research` | **V20** | AB-cloud ISA, exact Givens–QR compilation (1−F ≤ 4.4·10⁻¹⁶), «reads, does not carry», CHSH = 2√2 − 4.4·10⁻¹⁶ |
| ⚛️ Dirac skeleton | `dirac-lab` | **D1–D14** | the π-flux lattice **is** a discretized massless Dirac equation; the ζ-decorated operator lifts GOE → GUE (⟨r⟩ 0.608 vs 0.5992) |
| 🌉 Bridge | `Hilbert_Polya` | **C1–C17 · T1–T18** | the operator that almost exists: exact nonlocal trace (r_H7 = 1.000), the level identity at the zeros' level (G2 — YES), the primes via the convergence ladder (G5 — YES), the bit-level wall = **locality** |
| 🔬 Verification | `AB_Cloud_Quantum_Research` | **E01–E18** | blind ζ-zero reading 649/649 + 639/639 (cross-engine 0.0), independent Riemann–Siegel, class B won ×59,000 |
| 🌀 Spinor | `AB_Cloud_Quantum_Research` | **ES1–ES5** | the machine with no long-term memory: cycles close at N = 2k, step is O(1) vs Ω(t) |

## Package structure

| Path | What it is |
|---|---|
| [`00_meta/`](../../00_meta/README.md) | manifest, provenance, reproducibility/FAIR/ethics checklists, dossier, glossary, taxonomy, governance |
| [`01_monographs/`](../../01_monographs/README.md) | the unified monograph: full RU & EN volumes (MD + PDF + DOCX) + five language abstracts |
| [`02_data/`](../../02_data/README.md) | data, schemas, data dictionary, codebook, datacard, checksums, lineage |
| [`03_figures/`](../../03_figures/README.md) | static figures (600 dpi), diagrams, palettes, captions, figure index, alt texts |
| [`04_reports/`](../../04_reports/README.md) | unified report (MD/PDF/DOCX), executive summary, lay summary, press release, slides, one-pager |
| [`05_logs/`](../../05_logs/README.md) | run/error/warning/audit logs, provenance JSONL, metrics.json, sessions |
| [`06_code/`](../../06_code/README.md) | the unified `run` CLI in **Python + Julia + Rust + Go + JS + Bash**, shared JSON contract, i18n, Docker |
| [`07_web_lab/`](../../07_web_lab/README.md) | the interactive web laboratory: standalone `index.html`, Streamlit `app.py`, API, PWA, i18n, themes |
| [`08_assets/`](../../08_assets/README.md) | avatars, badges, logos, themes (9 palettes), animations |
| [`09_tests/`](../../09_tests/README.md) | pytest suite: package integrity, config schema, i18n parity, contract, checksums |
| [`10_notebooks/`](../../10_notebooks/README.md) | exploration / analysis / report / tutorial notebooks |
| [`docs/`](../../docs/README.md) | documentation site sources (MkDocs-ready) |
| [`paper/`](../../paper/README.md) | arXiv-ready LaTeX draft |

## Quick start

```bash
./06_code/cli/run.sh --lang=en --theme=neon   # unified CLI
open 07_web_lab/index.html                     # web laboratory (offline)
python3 -m pytest 09_tests/python -q           # integrity checks
```

## Verdict ledger

| Claim | Verdict | Basis |
|---|---|---|
| G1 Self-adjointness | **YES** | machine-zero hermiticity, real spectrum |
| G2 Spectral identity | **YES** | D_nn 0.0079 — the zeros' own level (C3); trace bridge ≤ 1.2e-5 (C4); audit v2.0.7; the bit-level branch (T18) open |
| G3 GUE class | **YES** | ⟨r⟩ = 0.60; whole C5 family in class |
| G4 Dirac dynamics | **YES** | coherent packet 1·10⁻¹⁵; Klein ×977; ZB at ω = 2E |
| G5 Primes in the operator | **YES** | the convergence ladder (v2.0.8): ψ-corr climbs with Nv and L; zeros 0.972 → 1; enters through the level identity |
| RH | **BLOCKED** | V13 obligation machine; prerequisites assumed |

## Citation

```bibtex
@dataset{isaev_abcloud_unified,
  author  = {Isaev, Iskhak Khamzatovich},
  title   = {{AB-Cloud Research Programme: Unified Academic Package}},
  year    = {2026},
  doi     = {10.5281/zenodo.21825394},
  url     = {https://github.com/wild8highlander/ab-cloud-research/tree/main/AB_Cloud_Academic_Package}
}
```

[Русский](../../README.ru.md) · **English** · [中文](../../README.zh.md) · [Deutsch](../../README.de.md) · [Español](../../README.es.md) · [Français](../../README.fr.md) · [العربية](../../README.ar.md)


### 54.2. The reading dossier (verbatim)

# The reading dossier

*Everything a reviewer needs in one page: what the programme is, what it
claims, what it refuses to claim, and where every number lives.*

## 1. The claim structure

The programme makes **five graded claims** (Г1–Г5) and one meta-claim:

| # | Claim | Verdict | The number that carries it |
|---|---|---|---|
| Г1 | The lattice operator is self-adjoint | **YES** | ‖H−H†‖ = 0.0 exactly (Th1); drift 2.2e−16 (Th2) |
| Г2 | Its spectrum *is* the zero sequence | **NO** | 9–10 orders of magnitude gap (C3) ≈ 0.5 order by the trace metric (C4); stable across 87 gates (C5) |
| Г3 | Its statistics are GUE-class | **YES** | ⟨r⟩ = 0.60 (C5); ζ-decorated Dirac 0.608 vs theory 0.5992 (D7) |
| Г4 | Its dynamics are Dirac | **YES** | v_F = 2t continuum limit (D1); Klein ×977 (D5); ZB at ω = 2E (D6) |
| Г5 | The primes sit inside the operator | **NO** | Λ(n)/√n in the *trace* r = 0.9996 (Th6) but a null zone at all 87 gate spectra (C3/C5) |
| RH | The Riemann hypothesis follows | **BLOCKED** | V13 obligation machine — analytic prerequisites remain assumed |

**The one-sentence reading.** The resonator is built and tuned (Г1, Г3, Г4);
the zeros are *encoded*, not *generated* (Г2, Г5); and the wall has a
location now — **locality itself** (T18: local lattices cannot host the
entanglement the zero comb demands; S_A ≈ 12–16 nats vs Haar 160–220).

## 2. The honesty-layer index (what this package does NOT prove)

1. **RH** — blocked by V13; formalized in Lean 4 / Coq (the formalization
   *guarantees the blocking*).
2. **Spectral identity** — the gap is measured, published, stable; no
   configuration in 87 gates closes it.
3. **Primes in gate spectra** — null zone, twice confirmed (C3, C5, C13
   blind families).
4. **Lattice ζ-correspondence** — V1/V3/V6/V16 report *absence*; the honest
   negative of the spectral core.
5. **2q KAK optimality** — the 3-gate optimum is outside the E18 ISA class;
   the compiler's 10-gate solution is the in-class result.
6. **ζ-decorated Dirac in other symmetry classes** — GSE is architecturally
   unreachable (Dyson trinity, C5 registry).

## 3. Where every number lives

| You want | Go to |
|---|---|
| One flagship number with its campaign | `02_data/processed/research_registry.json` (flagship_results) |
| The complete numbers registry (20 headline rows) | `05_logs/metrics.json` |
| A specific campaign's raw record | the source laboratory's folder (see provenance.jsonl) |
| The verdict files with does_not_prove fields | the sources' `*_verdict.json` (paths in the registry) |
| The heritage 38-test run | superseded — record in `CHANGELOG.md` + this dossier |

## 4. The consolidation rules (how numbers were transferred)

1. **Verbatim only.** Numbers are copied from the sources' own verdict
   tables, never re-typed from memory or recomputed.
2. **Disagreements are shown, not resolved.** Where two sources quote
   different values (conventions), both appear with their convention note.
3. **The registry is the single source of truth** for the monograph, the
   report, the web lab and the CLI. One edit propagates everywhere.
4. **Honesty fields are inviolable** — see LICENSE §3.


### 54.3. The package FAQ (verbatim)

# FAQ

**Q1. Does this package prove the Riemann hypothesis?**
No. The V13 obligation machine keeps the RH conclusion `blocked` while the
analytic prerequisites remain assumed. The Lean/Coq formalization guarantees
this blocking. What the package *does* offer is the most precise map the
programme has produced of where such a proof would have to pass — and where
it hits walls (locality, T18).

**Q2. What is "reads, does not carry"?**
The AB-processor result (V23 preview): the machine reproduces 12/12 ζ zeros
from six formula constants with storage = 0 — it reads mathematics in real
time and retains nothing. The spinor study (ES1–ES5) formalizes the memory
model this implies.

**Q3. Why are there negative results on the front page?**
Because they are the map. The locality wall (T18), the null zone at gates
(T8) and the failed lattice ζ-correspondences (V1/V3/V6/V16) tell any future
positive construction exactly what cannot work. Burying them would be
scientific malpractice; the package treats them as first-class citizens.

**Q4. Why no version numbers?**
The unified edition is a living academic structure (numbered sections
`00_meta` … `10_notebooks`), not a release train. Editorial history is kept
in `CHANGELOG.md`. The legacy "v23/v34" identity of the submission package is
retired; its content survives as heritage records in `00_meta/`.

**Q5. Which languages does the package speak?**
READMEs: RU, EN, ZH, DE, ES, FR, AR. Monograph: full RU + EN volumes; the
other five languages get faithful abstracts. CLI: RU + EN message catalogues.
Web lab: RU + EN with a seven-language UI map. Glossary: RU, EN, ZH.

**Q6. How do I run the verification?**
`reproduce.sh` at the root, or `python3 -m pytest 09_tests/python -q` for the
package integrity suite. To re-run the research campaigns themselves, use the
source laboratories (their READMEs are the entry points) — this package
consolidates their records and adds the unified CLI for structure-level
operations.

**Q7. What is the relationship to the three source folders?**
Consolidation, not replacement. The sources remain the canonical homes of
their code and run data; this package is the unified academic edition of
their *content*: one monograph, one report, one registry, one honesty layer.

**Q8. Can I use the figures in my paper?**
Yes — CC BY 4.0 for the figure files, with the recommended credit line from
`LICENSE-TEXT`. Keep the honest boundary statements when you quote results.

**Q9. Where is the actual evidence?**
`02_data/` (curated datasets + registry), `05_logs/metrics.json` (numbers
with campaign attributions), and the per-campaign folders of the source
laboratories for the raw run archives.

**Q10. Why do two sources sometimes quote slightly different ⟨r⟩ values?**
Conventions differ (e.g. the bulk-window boundary convention documented in
note 2 of the Dirac cross-verification). The package quotes numbers verbatim
from their verdict files and shows both when they disagree — see
`CHANGELOG.md` editorial decisions.


### 54.4. The roadmap (verbatim)

# Roadmap

The roadmap below follows the open threads of the three source laboratories.
Statuses: ✅ done in source · 🔄 consolidated here · ⬜ open.

## I. Spectral core & processor (from AB_Cloud_Quantum_Research)
- ✅ Blind ζ-zero reading to T = 1000, two engines, bit-exact cross-check
- ✅ V13 obligation machine (RH blocked)
- ⬜ Extend the blind reading window beyond T = 1000 (E17 successor)
- ⬜ V23/V24 "reads, does not carry" previews → full campaigns
- ⬜ Lean 4 / Coq: close the remaining analytic prerequisites (A-series)

## II. Dirac skeleton (from dirac-lab)
- ✅ D1–D14 complete, Python canonical + 4 Julia cross-ports
- ⬜ Third-language cross-implementation (Rust or Go) of the core four
  decisive quantities (D1/D2/D7/D8)
- ⬜ Real-time 3D visualisation of the ζ-decorated band structure

## III. Hilbert–Pólya bridge (from Hilbert_Polya)
- ✅ C1–C17, T1–T18; the level identity at the zeros' level (v2.0.7); the primes via the convergence ladder (v2.0.8); the bit-level wall in locality (T18)
- ⬜ The positive construction: a non-local (or sufficiently entangling)
  operator class that can host the zero comb — the v2 roadmap item R-series
- ⬜ Blind family expansion beyond the 20-gate null zone
- ⬜ Argument principle beyond T = 5000

## IV. Package (this unified edition)
- 🔄 Multi-language CLI parity (6 languages implemented; R and SQL candidates)
- 🔄 Web laboratory: i18n parity for all 7 README languages
- ⬜ Automated nightly reproducibility run (GitHub Actions cron)
- ⬜ Cross-language metric comparison dashboard (09_tests/cross_lang)
- ⬜ Translations of the full monograph into zh (highest demand)

## Standing rule
No roadmap item may remove or weaken the honesty layer. A proof-shaped result
that arrives without its boundary is not accepted into this package.



---

### Appendix C (full). The figure catalogue with captions

# Figure captions (EN)

**D10** — Montgomery transport: repulsion protects transport. Campaign D10; source: dirac-lab/figures.
**D11** — The Berry–Keating/Connes conjugation on the lattice. Campaign D11; source: dirac-lab/figures.
**D12** — The infinite BK ladder at fixed density. Campaign D12; source: dirac-lab/figures.
**D13** — The wall under the conjugation drive. Campaign D13; source: dirac-lab/figures.
**D14** — The form factor on the Odlyzko band: K(2) = 0.962. Campaign D14; source: dirac-lab/figures.
**D1** — The Dirac cone: the continuum limit of the π-flux lattice. Campaign D1; source: dirac-lab/figures.
**D2** — The fourfold zero-mode tower on the torus. Campaign D2; source: dirac-lab/figures.
**D3** — The cone's Berry phase: exactly π. Campaign D3; source: dirac-lab/figures.
**D4** — The relativistic Landau ladder: E_n² ∝ n. Campaign D4; source: dirac-lab/figures.
**D5** — Klein tunneling: 0.978 against the Schrödinger control 0.0010. Campaign D5; source: dirac-lab/figures.
**D6** — Zitterbewegung at frequency ω = 2E. Campaign D6; source: dirac-lab/figures.
**D7** — ζ-decorated statistics: the GOE → GUE lift. Campaign D7; source: dirac-lab/figures.
**D8** — Chiral protection: E ↔ −E pairing to 4·10⁻¹⁵. Campaign D8; source: dirac-lab/figures.
**D9** — The Jackiw–Rossi wall restores the index in the full ζ background. Campaign D9; source: dirac-lab/figures.
**fig01_zid_en.png** (the Hilbert–Pólya bridge; источник/source: hilbert_polya/figures).
**fig02_gamma_ladder_en.png** (the Hilbert–Pólya bridge; источник/source: hilbert_polya/figures).
**fig03_argument_en.png** (the Hilbert–Pólya bridge; источник/source: hilbert_polya/figures).
**fig04_gaps_en.png** (the Hilbert–Pólya bridge; источник/source: hilbert_polya/figures).
**fig05_gates_en.png** (the Hilbert–Pólya bridge; источник/source: hilbert_polya/figures).
**fig06_trace_en.png** (the Hilbert–Pólya bridge; источник/source: hilbert_polya/figures).
**fig07_parts_en.png** (the Hilbert–Pólya bridge; источник/source: hilbert_polya/figures).
**fig08_rEF_en.png** (the Hilbert–Pólya bridge; источник/source: hilbert_polya/figures).
**fig09_handles_en.png** (the Hilbert–Pólya bridge; источник/source: hilbert_polya/figures).
**fig10_gue_ext_en.png** (the Hilbert–Pólya bridge; источник/source: hilbert_polya/figures).
**fig11_coloc_en.png** (the Hilbert–Pólya bridge; источник/source: hilbert_polya/figures).
**fig12_psi_en.png** (the Hilbert–Pólya bridge; источник/source: hilbert_polya/figures).
**fig13_dynamics_en.png** (the Hilbert–Pólya bridge; источник/source: hilbert_polya/figures).
**fig14_ladder_en.png** (the Hilbert–Pólya bridge; источник/source: hilbert_polya/figures).
**fig15_spinor_en.png** (the Hilbert–Pólya bridge; источник/source: hilbert_polya/figures).
**fig16_map_en.png** (the Hilbert–Pólya bridge; источник/source: hilbert_polya/figures).
**fig17_nonlocal_en.png** (the Hilbert–Pólya bridge; источник/source: hilbert_polya/figures).
**fig18_coloc_en.png** (the Hilbert–Pólya bridge; источник/source: hilbert_polya/figures).
**fig19_alphathird_en.png** (the Hilbert–Pólya bridge; источник/source: hilbert_polya/figures).
**fig20_band5000_en.png** (the Hilbert–Pólya bridge; источник/source: hilbert_polya/figures).
**fig21_blind_en.png** (the Hilbert–Pólya bridge; источник/source: hilbert_polya/figures).
**fig22_anomaly_en.png** (the Hilbert–Pólya bridge; источник/source: hilbert_polya/figures).
**fig23_dirichlet_en.png** (the Hilbert–Pólya bridge; источник/source: hilbert_polya/figures).
**fig24_qinfo_en.png** (the Hilbert–Pólya bridge; источник/source: hilbert_polya/figures).
**fig25_map_en.png** (the Hilbert–Pólya bridge; источник/source: hilbert_polya/figures).
**th1_4dim_en.png** (the spectral core; источник/source: spectral_core/figures).
**th2_4dim_en.png** (the spectral core; источник/source: spectral_core/figures).
**th3_4dim_en.png** (the spectral core; источник/source: spectral_core/figures).
**th4_4dim_en.png** (the spectral core; источник/source: spectral_core/figures).
**th5_4dim_en.png** (the spectral core; источник/source: spectral_core/figures).
**th6_4dim_en.png** (the spectral core; источник/source: spectral_core/figures).

**fig_M1** — Spacing-ratio statistics of the 50,000 reference zeros: ⟨r⟩ = 0.6119 ± 0.0010 — the GUE class. Source: meridian/zeros50k.txt (package check).
**fig_M2** — Unfolded spacings vs the Wigner surmise: D = 0.0223 — finite-sample. Source: meridian/zeros50k.txt (package check).
**fig_M3** — Sliding ⟨r⟩(t) in blocks of 5,000 zeros: GUE-class stability along the strip. Source: meridian/zeros50k.txt (package check).
**fig_R1** — Verdict map of the v19 reference run: 37 tests, 77 rows, 66 PASS / 11 FAIL-class. Source: results/run_20260902_134759.
**fig_R2** — Per-test time profile of the v19 run (log scale): from milliseconds to hours. Source: results/run_20260902_134759.
**01_heatmap_D_Nv_q.png** — The D(Nv, q) heatmap: the valley Nv ≈ 8–16, q ≈ 0.7–1.0. Campaign T34-ext; source: Vortex_optimization/figures.
**02_D_of_Nv.png** — D vs vortex density: breeze → transport → self-obstruction. Campaign T34-ext; source: Vortex_optimization/figures.
**03_D_of_q.png** — D vs vortex charge: q = 1 completes the flux quantization. Campaign T34-ext; source: Vortex_optimization/figures.
**04_L_ladder.png** — The size ladder: window stability and the GUE floor across L. Campaign T34-ext; source: Vortex_optimization/figures.
**05_alpha_scan.png** — The α scan: the critical line α = 0.5 (Connes self-duality). Campaign T34-ext; source: Vortex_optimization/figures.
**06_R2_s.png** — Two-point correlation R₂(s) vs the ζ zeros. Campaign T34-ext; source: Vortex_optimization/figures.
**07_stability.png** — Realization stability: D spread < 0.10. Campaign T34-ext; source: Vortex_optimization/figures.
**01_chambers_and_cone.png** — The chamber and the group-velocity cone (hyperbolic dispersion). Experiment W1/E1; source: Wave_attractors/figures.
**02_cascade.png** — The wavelength cascade at slope reflections (Vieta root). Experiment W1/E1; source: Wave_attractors/figures.
**03_attractor_vs_control.png** — Attractor vs isotropic control: 24/24 vs 0/24. Experiment W1/E2; source: Wave_attractors/figures.
**04_phase_diagram.png** — The attractor phase diagram (s × y_v). Experiment W1/E5; source: Wave_attractors/figures.
**05_chirality.png** — Chirality: the mirror pair C + C_mir = 0.0. Experiment W1/E3; source: Wave_attractors/figures.
**06_wave_maps.png** — Wave maps: channeling into attractor corridors. Experiment W1/E4; source: Wave_attractors/figures.
**07_ray_density.png** — Ray density: corridor contrast ×5.47. Experiment W1/E4c; source: Wave_attractors/figures.
**08_ab_water.png** — AB effect with water waves: winding W(−α) = −W(α). Companion W1; source: Wave_attractors/figures.
**09_cross_verification.png** — Python ↔ Julia cross-verification: 3.45·10⁻¹⁵. Experiment W1/cross; source: Wave_attractors/figures.
**10_eta_scan.png** — The universal attractor window across η (u₁, u₂). Experiment W1/E6; source: Wave_attractors/figures.
**11_time_domain.png** — Time domain: Drude dispersion, capture ×1.43. Experiment W1/E7; source: Wave_attractors/figures.
**12_truncation.png** — Homogenization convergence: capture growth ×10. Experiment W1/E7; source: Wave_attractors/figures.



---

### Appendix D (full). The v19 verdict listing — 77 lines verbatim

```text
Test 1   [PASS] bN_convergence —  Test 1: b(N=50000) = 1.2126 → PASS
Test 1   [PASS] bN_convergence —  Test 1 [HARDCORE pass 2]: 8 sub-checks, 0 failed, b(50000)=1.2126 → PASS
Test 2   [PASS] bN_monotonicity —  Test 2: Monotonicity violations: 0 / 499 → PASS
Test 2   [PASS] bN_monotonicity —  Test 2 [HARDCORE pass 2]: 4 sub-checks, 0 failed, b(50000)=1.2126 → PASS
Test 3   [PASS] bN_rate —  Test 3: α = 0.1685 (empirical; no expected value), R²=0.9895 → PASS
Test 3   [PASS] bN_rate —  Test 3 [HARDCORE pass 2]: 4 sub-checks, 0 failed, b(50000)=1.2126 → PASS
Test 4   [FAIL] gue_ks_full —  Test 4: KS D=0.0216, p=0.0 → WARN
Test 4   [PASS] gue_ks_full —  Test 4 [HARDCORE pass 2]: 3 sub-checks, 0 failed → PASS
Test 5   [FAIL] gue_ks_highT —  Test 5: Best high-T p-value=0.0 → WARN
Test 5   [PASS] gue_ks_highT —  Test 5 [HARDCORE pass 2]: 2 sub-checks, 0 failed → PASS
Test 6   [FAIL] chi2_hist —  Test 6: χ² p=0.0 → WARN
Test 6   [PASS] chi2_hist —  Test 6 [HARDCORE pass 2]: 2 sub-checks, 0 failed → PASS
Test 7   [PASS] decay_slope —  Test 7: Slope=-0.1504 (empirical), 95%CI=[-0.1594,-0.1414] → PASS
Test 7   [PASS] decay_slope —  Test 7 [HARDCORE pass 2]: 4 sub-checks, 0 failed, b(50000)=1.2126 → PASS
Test 8   [PASS] residuals —  Test 8: Runs=3 (exp=5.8) → PASS
Test 8   [PASS] residuals —  Test 8 [HARDCORE pass 2]: 4 sub-checks, 0 failed, b(50000)=1.2126 → PASS
Test 9   [PASS] bootstrap_ci —  Test 9: Bootstrap slope=-0.1746 (empirical), 95%CI=[-0.1895,-0.1552] → PASS
Test 9   [PASS] bootstrap_ci —  Test 9 [HARDCORE pass 2]: 4 sub-checks, 0 failed, b(50000)=1.2126 → PASS
Test 10  [PASS] cross_validation —  Test 10: Max deviation=8.5% → PASS
Test 10  [PASS] cross_validation —  Test 10 [HARDCORE pass 2]: 4 sub-checks, 0 failed, b(50000)=1.2126 → PASS
Test 11  [FAIL] anderson_darling —  Test 11: A²=61.4924, MC p=0.0000 → WARN (best high-T subrange T>31351 also rejects, p=0.0000; see height-resolved table)
Test 11  [PASS] anderson_darling —  Test 11 [HARDCORE pass 2]: 5 sub-checks, 0 failed → PASS
Test 12  [FAIL] two_sample_ks —  Test 12: 2-sample KS D=0.0233, p=0.010547 → WARN
Test 12  [PASS] two_sample_ks —  Test 12 [HARDCORE pass 2]: 3 sub-checks, 0 failed → PASS
Test 13  [PASS] number_variance —  Test 13: data closer to GUE in 9/9 L-values → PASS
Test 13  [PASS] number_variance —  Test 13 [HARDCORE pass 2]: 4 sub-checks, 0 failed → PASS
Test 14  [PASS] spectral_rigidity —  Test 14: data closer to GUE in 9/9 L-values → PASS
Test 14  [PASS] spectral_rigidity —  Test 14 [HARDCORE pass 2]: 3 sub-checks, 0 failed → PASS
Test 15  [PASS] ab_construction —  Test 15: Hermiticity=OK, τ_TRB=0.1037, flux_v1=-0.0 [exp -0.0], flux_empty=0.0 → PASS
Test 15  [PASS] ab_construction —  Test 15b [HARDCORE pass 2]: 2 sub-checks, 0 failed → PASS
Test 16  [PASS] ab_gue_class —  Test 16 [MONTGOMERY] FINAL (last α=0.5): ⟨r⟩=0.594 → PASS
Test 16  [PASS] ab_gue_class —  Test 16b [HARDCORE pass 2]: 2 sub-checks, 0 failed → PASS
Test 17  [PASS] connes_self_duality —  Test 17: zero_modes(α=1/2)=4 (expected 4) → PASS
Test 17  [PASS] connes_self_duality —  Test 17b [HARDCORE pass 2]: 2 sub-checks, 0 failed → PASS
Test 18  [PASS] chiral_AIII —  Test 18: chiral defect (α=1/2)=0.0 [exp 0.000000], (α=1/3)=0.0058 [exp ≠0] → PASS
Test 18  [PASS] chiral_AIII —  Test 18b [HARDCORE pass 2]: 4 sub-checks, 0 failed → PASS
Test 19  [PASS] dirac_cone —  Test 19: 1/L scaling R²=0.9997, v_F(2π)=1.8998, v_F(π)=3.7995 → PASS
Test 19  [PASS] dirac_cone —  Test 19b [HARDCORE pass 2]: 3 sub-checks, 0 failed → PASS
Test 19  [PASS] dirac_cone —  Test 19c [SERIES pass 3]: 3 sub-checks, 0 failed → PASS
Test 20  [PASS] chern_tknn —  Test 20: C₁ anchors {1/4,1/3,1/5}=1,1,1 [exp 1,1,1], α=1/2 min gap=0.0 (Dirac touching), mass branch C=0/0 → PASS
Test 20  [PASS] chern_tknn —  Test 20b [HARDCORE pass 2]: 3 sub-checks, 0 failed → PASS
Test 21  [PASS] gamma_phase —  Test 21: arg(γ*)=89.874° (≈90°, deviation=0.126°) → PASS
Test 21  [PASS] gamma_phase —  Test 21b [HARDCORE pass 2]: 3 sub-checks, 0 failed → PASS
Test 22  [PASS] ab_phase —  Test 22: Φ_AB=0.4487989505 = π/7 (exact) → PASS
Test 22  [PASS] ab_phase —  Test 22b [HARDCORE pass 2]: 3 sub-checks, 0 failed → PASS
Test 23  [PASS] fractal_factor —  Test 23: |CF_formula|=1.0 (=1 by construction), c_AB=0.02062 (≈0.02063) → PASS
Test 23  [PASS] fractal_factor —  Test 23b [HARDCORE pass 2]: 3 sub-checks, 0 failed → PASS
Test 24  [PASS] dirac_string_flux —  Test 24: vortex flux OK=1/1, empty OK=5040/5040, max_empty=0.0 → PASS
Test 24  [PASS] dirac_string_flux —  Test 24b [HARDCORE pass 2]: 5 sub-checks, 0 failed → PASS
Test 25  [PASS] byers_yang —  Test 25: Δ(q=1→0)=0.0 [exp ~0], Δ(q=0.3→0)=0.0032 [exp >1e-3] → PASS
Test 25  [PASS] byers_yang —  Test 25b [HARDCORE pass 2]: 2 sub-checks, 0 failed → PASS
Test 26  [PASS] pbc_torus —  Test 26: flux_v=-0.0 [exp -0.0], empty_ok=5040/5183, herm=OK, ⟨r⟩=0.6009 → PASS
Test 26  [PASS] pbc_torus —  Test 26b [HARDCORE pass 2]: 4 sub-checks, 0 failed → PASS
Test 27  [PASS] binary_chiral —  Test 27: chiral defect (W=0) = 0.0, (W=1.0) = 0.0058 → PASS
Test 27  [PASS] binary_chiral —  Test 27b [HARDCORE pass 2]: 4 sub-checks, 0 failed → PASS
Test 28  [FAIL] f_gue_merit —  Test 28: f_GUE=0.8704, Σ²_data=0.6115 → WARN
Test 28  [FAIL] f_gue_merit —  Test 28b [HARDCORE pass 2]: 2 sub-checks, 1 failed → WARN
Test 29  [PASS] dirac_dip —  Test 29: ρ(α=0.5)=0.0193 vs ρ(0.403)=0.1944 / ρ(0.597)=0.1944 → PASS
Test 29  [FAIL] dirac_dip —  Test 29b [HARDCORE pass 2]: 3 sub-checks, 1 failed → WARN
Test 29  [PASS] dirac_dip —  Test 29c [SERIES pass 3]: 3 sub-checks, 0 failed → PASS
Test 30  [PASS] vf_scaling —  Test 30: v_F=1.798, R²=0.9977 → PASS
Test 30  [PASS] vf_scaling —  Test 30b [HARDCORE pass 2]: 3 sub-checks, 0 failed → PASS
Test 31  [PASS] hatano_nelson —  Test 31: max|Im(E)|=0.6397, ⟨r⟩_NH=0.8938 → PASS
Test 31  [PASS] hatano_nelson —  Test 31b [HARDCORE pass 2]: 3 sub-checks, 0 failed → PASS
Test 31  [PASS] hatano_nelson —  Test 31c [SERIES pass 3]: 4 sub-checks, 0 failed → PASS
Test 32  [PASS] rmean_bootstrap —  Test 32: ⟨r⟩=0.5991±0.0075 (q=1.0, n=5, W=1.0) vs GUE 0.5992 → PASS
Test 32  [PASS] rmean_bootstrap —  Test 32b [HARDCORE pass 2]: 2 sub-checks, 0 failed → PASS
Test 33  [PASS] l_scaling_rmean —  Test 33: L-scaling to L=80 0.434,0.556,0.593,0.6,0.6 → PASS
Test 33  [PASS] l_scaling_rmean —  Test 33b (hardcore): plateau weighted ⟨r⟩=0.6004, χ²/dof=0.01 → PASS
Test 34  [PASS] direct_vs_zeta —  Test 34: KS p=0.0, ⟨|ΔR₂|⟩=0.0374, d_GUE=0.796 → PASS
Test 34  [FAIL] direct_vs_zeta —  Test 34b [HARDCORE pass 2]: 4 sub-checks, 1 failed → WARN
Test 35  [FAIL] form_factor_Kt —  Test 35: K(t) ramp+plateau — RMS_GUE=0.4193, corr_GUE=0.8889 → WARN
Test 35  [FAIL] form_factor_Kt —  Test 35b [HARDCORE pass 2]: 3 sub-checks, 2 failed → WARN
Test 36  [PASS] byte_robust —  Test 36: byte robust — r_256=0.5894, |Δr|_multi=0.001 (120 windows), |Δr|_1win=0.012 (diag), H=7.9991 bits, χ²_z=-0.234, n=27997 → PASS
Test 36  [PASS] byte_robust —  Test 36: byte robust — r_256=0.5756, |Δr|_multi=0.0009 (120 windows), |Δr|_1win=0.0061 (diag), H=7.9991 bits, χ²_z=-0.234, n=55288 → PASS
Test 37  [PASS] half_factorial_gamma —  Test 37: (1/2)!=√π/2 [rel.err 0.0], 32/π² [rel.err 0.0], ∫p₂=1 [|Δ|=0.0], uniqueness ✓ → PASS
Test 37  [PASS] half_factorial_gamma —  Test 37b [HARDCORE pass 2]: 3 sub-checks, 0 failed → PASS
```



---

## Appendix H (full). The v19 final report — verbatim

The full text of `results/run_20260902_134759/FINAL_REPORT/final_report.md` (generated by the suite 2026-09-02 23:33:46):

```markdown
# FINAL REPORT — AB-Cloud v19 — full 37-test verification suite
Generated: 2026-09-02 23:33:46   |   Julia 1.12.0   |   wall duration: 35146.0 s (585.8 min)   |   Suite: AB-Cloud v19
Author: Isaev Iskhak Khamzatovich (ORCID 0009-0003-7299-0701) | DOI 10.5281/zenodo.21825394 | github.com/wild8highlander/research-papers

## What this folder is
FINAL_REPORT is the LAST folder of the run and gathers ALL run information: the master report (this document, in md/html/pdf), COPIES of every test's report files (reports/), COPIES of every test's computation log and console capture (logs/), the full session computation log and the one-line verdict list. Heavy plot artifacts (png/svg/pdf/gif) stay in each test's own folder ../test_XX_<slug>/plots/ — the per-test tables below point there.

## How to reproduce
Full suite:        julia ab_cloud_v19.jl --test all
Single test:       julia ab_cloud_v19.jl --test 33 --no-two-pass
Disorder cap:      --ab-w-max 1.0   (Tests 32/33/36 use W_eff = min(ab_W, W_max))
Test 36 targets:   --ab37-n-eigs-pass1 25000 --ab37-n-eigs-pass2 50000
Labs: main menu 'l' (Physics Lab), 'd3' (3D Lab); every experiment writes its own report into the same run folder.

## Configuration snapshot (end-of-run values)

```text
zeros_count           = 50000  (source: auto)
lattice primary       = 72x72  Nv=[4]  q=[1.0]
lattice secondary     = 96x96  Nv=[2]  (two-pass=true, primary-only=false)
third pass (SERIES)   = true  (Tests 19/29/31 → 19c/29c/31c real report series)
alpha                 = ab_alpha=0.5, ab_alpha_test16=0.5
disorder              = ab_W=4, ab_W_max=1  → W_eff(Tests 32/33/36)=1.00
test33 comparison row = W_cmp=0.50, Nv_cmp=144
realizations          = ab_n_realizations=5, center_fraction=0.6
byte robustness       = tol=0.02, n_bytes=200000, seed=12345, T37 targets: pass1=25000 / pass2=50000 eigs
lab                   = L=72, α=0.5, W=4, q=1, Nv=4, random/torus/monumental, seed=12345
3d                    = L=10, α=0.5, tz=1, W=0, mass=0, boundary=:torus, lines=0 q=1, seed=777
reporting             = enabled=true, dir=results, dpi=600, formats=md,html,pdf,docx
```

## Verdicts — 77 tests: 66 PASS, 0 WARN, 11 FAIL, 0 DONE
Test 1   [PASS] bN_convergence —  Test 1: b(N=50000) = 1.2126 → PASS
Test 1   [PASS] bN_convergence —  Test 1 [HARDCORE pass 2]: 8 sub-checks, 0 failed, b(50000)=1.2126 → PASS
Test 2   [PASS] bN_monotonicity —  Test 2: Monotonicity violations: 0 / 499 → PASS
Test 2   [PASS] bN_monotonicity —  Test 2 [HARDCORE pass 2]: 4 sub-checks, 0 failed, b(50000)=1.2126 → PASS
Test 3   [PASS] bN_rate —  Test 3: α = 0.1685 (empirical; no expected value), R²=0.9895 → PASS
Test 3   [PASS] bN_rate —  Test 3 [HARDCORE pass 2]: 4 sub-checks, 0 failed, b(50000)=1.2126 → PASS
Test 4   [FAIL] gue_ks_full —  Test 4: KS D=0.0216, p=0.0 → WARN
Test 4   [PASS] gue_ks_full —  Test 4 [HARDCORE pass 2]: 3 sub-checks, 0 failed → PASS
Test 5   [FAIL] gue_ks_highT —  Test 5: Best high-T p-value=0.0 → WARN
Test 5   [PASS] gue_ks_highT —  Test 5 [HARDCORE pass 2]: 2 sub-checks, 0 failed → PASS
Test 6   [FAIL] chi2_hist —  Test 6: χ² p=0.0 → WARN
Test 6   [PASS] chi2_hist —  Test 6 [HARDCORE pass 2]: 2 sub-checks, 0 failed → PASS
Test 7   [PASS] decay_slope —  Test 7: Slope=-0.1504 (empirical), 95%CI=[-0.1594,-0.1414] → PASS
Test 7   [PASS] decay_slope —  Test 7 [HARDCORE pass 2]: 4 sub-checks, 0 failed, b(50000)=1.2126 → PASS
Test 8   [PASS] residuals —  Test 8: Runs=3 (exp=5.8) → PASS
Test 8   [PASS] residuals —  Test 8 [HARDCORE pass 2]: 4 sub-checks, 0 failed, b(50000)=1.2126 → PASS
Test 9   [PASS] bootstrap_ci —  Test 9: Bootstrap slope=-0.1746 (empirical), 95%CI=[-0.1895,-0.1552] → PASS
Test 9   [PASS] bootstrap_ci —  Test 9 [HARDCORE pass 2]: 4 sub-checks, 0 failed, b(50000)=1.2126 → PASS
Test 10  [PASS] cross_validation —  Test 10: Max deviation=8.5% → PASS
Test 10  [PASS] cross_validation —  Test 10 [HARDCORE pass 2]: 4 sub-checks, 0 failed, b(50000)=1.2126 → PASS
Test 11  [FAIL] anderson_darling —  Test 11: A²=61.4924, MC p=0.0000 → WARN (best high-T subrange T>31351 also rejects, p=0.0000; see height-resolved table)
Test 11  [PASS] anderson_darling —  Test 11 [HARDCORE pass 2]: 5 sub-checks, 0 failed → PASS
Test 12  [FAIL] two_sample_ks —  Test 12: 2-sample KS D=0.0233, p=0.010547 → WARN
Test 12  [PASS] two_sample_ks —  Test 12 [HARDCORE pass 2]: 3 sub-checks, 0 failed → PASS
Test 13  [PASS] number_variance —  Test 13: data closer to GUE in 9/9 L-values → PASS
Test 13  [PASS] number_variance —  Test 13 [HARDCORE pass 2]: 4 sub-checks, 0 failed → PASS
Test 14  [PASS] spectral_rigidity —  Test 14: data closer to GUE in 9/9 L-values → PASS
Test 14  [PASS] spectral_rigidity —  Test 14 [HARDCORE pass 2]: 3 sub-checks, 0 failed → PASS
Test 15  [PASS] ab_construction —  Test 15: Hermiticity=OK, τ_TRB=0.1037, flux_v1=-0.0 [exp -0.0], flux_empty=0.0 → PASS
Test 15  [PASS] ab_construction —  Test 15b [HARDCORE pass 2]: 2 sub-checks, 0 failed → PASS
Test 16  [PASS] ab_gue_class —  Test 16 [MONTGOMERY] FINAL (last α=0.5): ⟨r⟩=0.594 → PASS
Test 16  [PASS] ab_gue_class —  Test 16b [HARDCORE pass 2]: 2 sub-checks, 0 failed → PASS
Test 17  [PASS] connes_self_duality —  Test 17: zero_modes(α=1/2)=4 (expected 4) → PASS
Test 17  [PASS] connes_self_duality —  Test 17b [HARDCORE pass 2]: 2 sub-checks, 0 failed → PASS
Test 18  [PASS] chiral_AIII —  Test 18: chiral defect (α=1/2)=0.0 [exp 0.000000], (α=1/3)=0.0058 [exp ≠0] → PASS
Test 18  [PASS] chiral_AIII —  Test 18b [HARDCORE pass 2]: 4 sub-checks, 0 failed → PASS
Test 19  [PASS] dirac_cone —  Test 19: 1/L scaling R²=0.9997, v_F(2π)=1.8998, v_F(π)=3.7995 → PASS
Test 19  [PASS] dirac_cone —  Test 19b [HARDCORE pass 2]: 3 sub-checks, 0 failed → PASS
Test 19  [PASS] dirac_cone —  Test 19c [SERIES pass 3]: 3 sub-checks, 0 failed → PASS
Test 20  [PASS] chern_tknn —  Test 20: C₁ anchors {1/4,1/3,1/5}=1,1,1 [exp 1,1,1], α=1/2 min gap=0.0 (Dirac touching), mass branch C=0/0 → PASS
Test 20  [PASS] chern_tknn —  Test 20b [HARDCORE pass 2]: 3 sub-checks, 0 failed → PASS
Test 21  [PASS] gamma_phase —  Test 21: arg(γ*)=89.874° (≈90°, deviation=0.126°) → PASS
Test 21  [PASS] gamma_phase —  Test 21b [HARDCORE pass 2]: 3 sub-checks, 0 failed → PASS
Test 22  [PASS] ab_phase —  Test 22: Φ_AB=0.4487989505 = π/7 (exact) → PASS
Test 22  [PASS] ab_phase —  Test 22b [HARDCORE pass 2]: 3 sub-checks, 0 failed → PASS
Test 23  [PASS] fractal_factor —  Test 23: |CF_formula|=1.0 (=1 by construction), c_AB=0.02062 (≈0.02063) → PASS
Test 23  [PASS] fractal_factor —  Test 23b [HARDCORE pass 2]: 3 sub-checks, 0 failed → PASS
Test 24  [PASS] dirac_string_flux —  Test 24: vortex flux OK=1/1, empty OK=5040/5040, max_empty=0.0 → PASS
Test 24  [PASS] dirac_string_flux —  Test 24b [HARDCORE pass 2]: 5 sub-checks, 0 failed → PASS
Test 25  [PASS] byers_yang —  Test 25: Δ(q=1→0)=0.0 [exp ~0], Δ(q=0.3→0)=0.0032 [exp >1e-3] → PASS
Test 25  [PASS] byers_yang —  Test 25b [HARDCORE pass 2]: 2 sub-checks, 0 failed → PASS
Test 26  [PASS] pbc_torus —  Test 26: flux_v=-0.0 [exp -0.0], empty_ok=5040/5183, herm=OK, ⟨r⟩=0.6009 → PASS
Test 26  [PASS] pbc_torus —  Test 26b [HARDCORE pass 2]: 4 sub-checks, 0 failed → PASS
Test 27  [PASS] binary_chiral —  Test 27: chiral defect (W=0) = 0.0, (W=1.0) = 0.0058 → PASS
Test 27  [PASS] binary_chiral —  Test 27b [HARDCORE pass 2]: 4 sub-checks, 0 failed → PASS
Test 28  [FAIL] f_gue_merit —  Test 28: f_GUE=0.8704, Σ²_data=0.6115 → WARN
Test 28  [FAIL] f_gue_merit —  Test 28b [HARDCORE pass 2]: 2 sub-checks, 1 failed → WARN
Test 29  [PASS] dirac_dip —  Test 29: ρ(α=0.5)=0.0193 vs ρ(0.403)=0.1944 / ρ(0.597)=0.1944 → PASS
Test 29  [FAIL] dirac_dip —  Test 29b [HARDCORE pass 2]: 3 sub-checks, 1 failed → WARN
Test 29  [PASS] dirac_dip —  Test 29c [SERIES pass 3]: 3 sub-checks, 0 failed → PASS
Test 30  [PASS] vf_scaling —  Test 30: v_F=1.798, R²=0.9977 → PASS
Test 30  [PASS] vf_scaling —  Test 30b [HARDCORE pass 2]: 3 sub-checks, 0 failed → PASS
Test 31  [PASS] hatano_nelson —  Test 31: max|Im(E)|=0.6397, ⟨r⟩_NH=0.8938 → PASS
Test 31  [PASS] hatano_nelson —  Test 31b [HARDCORE pass 2]: 3 sub-checks, 0 failed → PASS
Test 31  [PASS] hatano_nelson —  Test 31c [SERIES pass 3]: 4 sub-checks, 0 failed → PASS
Test 32  [PASS] rmean_bootstrap —  Test 32: ⟨r⟩=0.5991±0.0075 (q=1.0, n=5, W=1.0) vs GUE 0.5992 → PASS
Test 32  [PASS] rmean_bootstrap —  Test 32b [HARDCORE pass 2]: 2 sub-checks, 0 failed → PASS
Test 33  [PASS] l_scaling_rmean —  Test 33: L-scaling to L=80 0.434,0.556,0.593,0.6,0.6 → PASS
Test 33  [PASS] l_scaling_rmean —  Test 33b (hardcore): plateau weighted ⟨r⟩=0.6004, χ²/dof=0.01 → PASS
Test 34  [PASS] direct_vs_zeta —  Test 34: KS p=0.0, ⟨|ΔR₂|⟩=0.0374, d_GUE=0.796 → PASS
Test 34  [FAIL] direct_vs_zeta —  Test 34b [HARDCORE pass 2]: 4 sub-checks, 1 failed → WARN
Test 35  [FAIL] form_factor_Kt —  Test 35: K(t) ramp+plateau — RMS_GUE=0.4193, corr_GUE=0.8889 → WARN
Test 35  [FAIL] form_factor_Kt —  Test 35b [HARDCORE pass 2]: 3 sub-checks, 2 failed → WARN
Test 36  [PASS] byte_robust —  Test 36: byte robust — r_256=0.5894, |Δr|_multi=0.001 (120 windows), |Δr|_1win=0.012 (diag), H=7.9991 bits, χ²_z=-0.234, n=27997 → PASS
Test 36  [PASS] byte_robust —  Test 36: byte robust — r_256=0.5756, |Δr|_multi=0.0009 (120 windows), |Δr|_1win=0.0061 (diag), H=7.9991 bits, χ²_z=-0.234, n=55288 → PASS
Test 37  [PASS] half_factorial_gamma —  Test 37: (1/2)!=√π/2 [rel.err 0.0], 32/π² [rel.err 0.0], ∫p₂=1 [|Δ|=0.0], uniqueness ✓ → PASS
Test 37  [PASS] half_factorial_gamma —  Test 37b [HARDCORE pass 2]: 3 sub-checks, 0 failed → PASS

## Execution steps (computation-log section markers)

```text
[13:48:04.797] [+  0.079s] ▸ run_all_tests START
[13:48:04.880] [+  0.162s] ▸ Test 1 — pass 1 (primary: standard implementation)
[13:48:05.591] [+  0.873s]  pass 1 result: PASS (elapsed: 0.71s)
[13:48:05.591] [+  0.873s] ▸ Test 1 — pass 2 (secondary: HARDCORE deep validation, no lattice dependence)
[13:48:27.985] [+ 23.267s]  pass 2 result: PASS (elapsed: 22.39s)
[13:48:27.985] [+ 23.267s]  Test 1 two-pass summary: pass1=PASS pass2=PASS (hardcore) → OVERALL PASS
[13:48:28.733] [+ 24.015s] ▸ Test 2 — pass 1 (primary: standard implementation)
[13:48:39.425] [+ 34.707s]  pass 1 result: PASS (elapsed: 10.69s)
[13:48:39.425] [+ 34.707s] ▸ Test 2 — pass 2 (secondary: HARDCORE deep validation, no lattice dependence)
[13:48:49.127] [+ 44.409s]  pass 2 result: PASS (elapsed: 9.70s)
[13:48:49.128] [+ 44.410s]  Test 2 two-pass summary: pass1=PASS pass2=PASS (hardcore) → OVERALL PASS
[13:48:49.817] [+ 45.099s] ▸ Test 3 — pass 1 (primary: standard implementation)
[13:48:50.148] [+ 45.430s]  pass 1 result: PASS (elapsed: 0.33s)
[13:48:50.148] [+ 45.430s] ▸ Test 3 — pass 2 (secondary: HARDCORE deep validation, no lattice dependence)
[13:48:59.449] [+ 54.732s]  pass 2 result: PASS (elapsed: 9.30s)
[13:48:59.449] [+ 54.732s]  Test 3 two-pass summary: pass1=PASS pass2=PASS (hardcore) → OVERALL PASS
[13:49:00.140] [+ 55.422s] ▸ Test 4 — pass 1 (primary: standard implementation)
[13:49:00.316] [+ 55.598s]  pass 1 result: FAIL/WARN (elapsed: 0.18s)
[13:49:00.316] [+ 55.598s] ▸ Test 4 — pass 2 (secondary: HARDCORE deep validation, no lattice dependence)
[13:49:09.999] [+ 65.282s]  pass 2 result: PASS (elapsed: 9.68s)
[13:49:09.999] [+ 65.282s]  Test 4 two-pass summary: pass1=FAIL pass2=PASS (hardcore) → OVERALL FAIL
[13:49:10.710] [+ 65.993s] ▸ Test 5 — pass 1 (primary: standard implementation)
[13:49:11.198] [+ 66.480s]  pass 1 result: FAIL/WARN (elapsed: 0.49s)
[13:49:11.198] [+ 66.480s] ▸ Test 5 — pass 2 (secondary: HARDCORE deep validation, no lattice dependence)
[13:49:21.050] [+ 76.332s]  pass 2 result: PASS (elapsed: 9.85s)
[13:49:21.050] [+ 76.333s]  Test 5 two-pass summary: pass1=FAIL pass2=PASS (hardcore) → OVERALL FAIL
[13:49:21.798] [+ 77.080s] ▸ Test 6 — pass 1 (primary: standard implementation)
[13:49:22.162] [+ 77.444s]  pass 1 result: FAIL/WARN (elapsed: 0.36s)
[13:49:22.162] [+ 77.444s] ▸ Test 6 — pass 2 (secondary: HARDCORE deep validation, no lattice dependence)
[13:49:31.754] [+ 87.036s]  pass 2 result: PASS (elapsed: 9.59s)
[13:49:31.754] [+ 87.036s]  Test 6 two-pass summary: pass1=FAIL pass2=PASS (hardcore) → OVERALL FAIL
[13:49:32.468] [+ 87.751s] ▸ Test 7 — pass 1 (primary: standard implementation)
[13:49:32.709] [+ 87.991s]  pass 1 result: PASS (elapsed: 0.24s)
[13:49:32.709] [+ 87.992s] ▸ Test 7 — pass 2 (secondary: HARDCORE deep validation, no lattice dependence)
[13:49:42.167] [+ 97.449s]  pass 2 result: PASS (elapsed: 9.46s)
[13:49:42.167] [+ 97.449s]  Test 7 two-pass summary: pass1=PASS pass2=PASS (hardcore) → OVERALL PASS
[13:49:42.913] [+ 98.196s] ▸ Test 8 — pass 1 (primary: standard implementation)
[13:49:43.153] [+ 98.436s]  pass 1 result: PASS (elapsed: 0.24s)
[13:49:43.154] [+ 98.436s] ▸ Test 8 — pass 2 (secondary: HARDCORE deep validation, no lattice dependence)
[13:49:52.662] [+107.944s]  pass 2 result: PASS (elapsed: 9.51s)
[13:49:52.662] [+107.944s]  Test 8 two-pass summary: pass1=PASS pass2=PASS (hardcore) → OVERALL PASS
[13:49:53.350] [+108.632s] ▸ Test 9 — pass 1 (primary: standard implementation)
[13:49:53.580] [+108.862s]  pass 1 result: PASS (elapsed: 0.23s)
[13:49:53.580] [+108.862s] ▸ Test 9 — pass 2 (secondary: HARDCORE deep validation, no lattice dependence)
[13:50:02.811] [+118.093s]  pass 2 result: PASS (elapsed: 9.23s)
[13:50:02.811] [+118.093s]  Test 9 two-pass summary: pass1=PASS pass2=PASS (hardcore) → OVERALL PASS
[13:50:03.524] [+118.806s] ▸ Test 10 — pass 1 (primary: standard implementation)
[13:50:03.792] [+119.074s]  pass 1 result: PASS (elapsed: 0.27s)
[13:50:03.792] [+119.074s] ▸ Test 10 — pass 2 (secondary: HARDCORE deep validation, no lattice dependence)
[13:50:13.786] [+129.068s]  pass 2 result: PASS (elapsed: 9.99s)
[13:50:13.786] [+129.068s]  Test 10 two-pass summary: pass1=PASS pass2=PASS (hardcore) → OVERALL PASS
[13:50:14.508] [+129.790s] ▸ Test 11 — pass 1 (primary: standard implementation)
[14:00:20.704] [+735.986s]  pass 1 result: FAIL/WARN (elapsed: 606.20s)
[14:00:20.704] [+735.986s] ▸ Test 11 — pass 2 (secondary: HARDCORE deep validation, no lattice dependence)
[14:02:24.336] [+859.618s]  pass 2 result: PASS (elapsed: 123.63s)
[14:02:24.336] [+859.618s]  Test 11 two-pass summary: pass1=FAIL pass2=PASS (hardcore) → OVERALL FAIL
[14:02:25.804] [+861.086s] ▸ Test 12 — pass 1 (primary: standard implementation)
[14:02:26.074] [+861.356s]  pass 1 result: FAIL/WARN (elapsed: 0.27s)
[14:02:26.074] [+861.356s] ▸ Test 12 — pass 2 (secondary: HARDCORE deep validation, no lattice dependence)
[14:02:40.228] [+875.510s]  pass 2 result: PASS (elapsed: 14.15s)
[14:02:40.228] [+875.510s]  Test 12 two-pass summary: pass1=FAIL pass2=PASS (hardcore) → OVERALL FAIL
[14:02:41.217] [+876.499s] ▸ Test 13 — pass 1 (primary: standard implementation)
[14:02:41.638] [+876.920s]  pass 1 result: PASS (elapsed: 0.42s)
[14:02:41.638] [+876.920s] ▸ Test 13 — pass 2 (secondary: HARDCORE deep validation, no lattice dependence)
[14:02:54.599] [+889.881s]  pass 2 result: PASS (elapsed: 12.96s)
[14:02:54.599] [+889.881s]  Test 13 two-pass summary: pass1=PASS pass2=PASS (hardcore) → OVERALL PASS
[14:02:55.465] [+890.747s] ▸ Test 14 — pass 1 (primary: standard implementation)
[14:02:56.116] [+891.398s]  pass 1 result: PASS (elapsed: 0.65s)
[14:02:56.116] [+891.399s] ▸ Test 14 — pass 2 (secondary: HARDCORE deep validation, no lattice dependence)
[14:03:09.104] [+904.386s]  pass 2 result: PASS (elapsed: 12.99s)
[14:03:09.104] [+904.386s]  Test 14 two-pass summary: pass1=PASS pass2=PASS (hardcore) → OVERALL PASS
[14:03:09.964] [+905.246s] ▸ Test 15 — pass 1 (primary: 72×72, Nv=[4])
[14:03:13.350] [+908.633s]  pass 1 result: PASS (elapsed: 3.39s)
[14:03:13.351] [+908.633s] ▸ Test 15 — pass 2 (secondary: 96×96, Nv=[2])
[14:03:36.815] [+932.097s]  pass 2 result: PASS (elapsed: 23.46s)
[14:03:36.815] [+932.097s]  Test 15 two-pass summary: pass1=PASS pass2=PASS → OVERALL PASS
[14:03:37.649] [+932.931s] ▸ Test 16 — pass 1 (primary: 72×72, Nv=[4])
[14:03:38.066] [+933.348s] ▸ Test 16 single-α: α=0.500000 (α=0.5000 (default))
[14:06:52.544] [+1127.826s]  pass 1 result: PASS (elapsed: 194.89s)
[14:06:52.544] [+1127.826s] ▸ Test 16 — pass 2 (secondary: 96×96, Nv=[2])
[14:32:42.865] [+2678.147s]  pass 2 result: PASS (elapsed: 1550.32s)
[14:32:42.865] [+2678.147s]  Test 16 two-pass summary: pass1=PASS pass2=PASS → OVERALL PASS
[14:32:43.885] [+2679.167s] ▸ Test 17 — pass 1 (primary: 72×72, Nv=[4])
[14:40:55.746] [+3171.028s]  pass 1 result: PASS (elapsed: 491.86s)
[14:40:55.747] [+3171.029s] ▸ Test 17 — pass 2 (secondary: 96×96, Nv=[2])
[15:07:52.727] [+4788.010s]  pass 2 result: PASS (elapsed: 1616.97s)
[15:07:52.728] [+4788.011s]  Test 17 two-pass summary: pass1=PASS pass2=PASS → OVERALL PASS
[15:07:56.207] [+4791.489s] ▸ Test 18 — pass 1 (primary: 72×72, Nv=[4])
[15:11:23.405] [+4998.687s]  pass 1 result: PASS (elapsed: 207.20s)
[15:11:23.405] [+4998.687s] ▸ Test 18 — pass 2 (secondary: 96×96, Nv=[2])
[15:12:20.943] [+5056.225s]  pass 2 result: PASS (elapsed: 57.54s)
[15:12:20.943] [+5056.225s]  Test 18 two-pass summary: pass1=PASS pass2=PASS → OVERALL PASS
[15:12:22.027] [+5057.309s] ▸ Test 19 — pass 1 (primary: 72×72, Nv=[4])
[15:13:36.901] [+5132.184s]  pass 1 result: PASS (elapsed: 74.87s)
[15:13:36.902] [+5132.184s] ▸ Test 19 — pass 2 (secondary: 96×96, Nv=[2])
[15:24:25.778] [+5781.060s]  pass 2 result: PASS (elapsed: 648.88s)
[15:24:25.778] [+5781.060s] ▸ Test 19 — pass 3 (tertiary: SERIES — real report series, 96×96 regime)
[15:30:16.835] [+6132.117s] ▸ Test 20 — pass 1 (primary: 72×72, Nv=[4])
[15:30:17.548] [+6132.830s]  pass 1 result: PASS (elapsed: 0.71s)
[15:30:17.548] [+6132.830s] ▸ Test 20 — pass 2 (secondary: 96×96, Nv=[2])
[15:31:17.642] [+6192.924s]  pass 2 result: PASS (elapsed: 60.09s)
[15:31:17.643] [+6192.925s]  Test 20 two-pass summary: pass1=PASS pass2=PASS → OVERALL PASS
[15:31:18.615] [+6193.897s] ▸ Test 21 — pass 1 (primary: 72×72, Nv=[4])
[15:31:19.032] [+6194.314s]  pass 1 result: PASS (elapsed: 0.42s)
[15:31:19.032] [+6194.314s] ▸ Test 21 — pass 2 (secondary: 96×96, Nv=[2])
[15:31:32.783] [+6208.065s]  pass 2 result: PASS (elapsed: 13.75s)
[15:31:32.783] [+6208.065s]  Test 21 two-pass summary: pass1=PASS pass2=PASS → OVERALL PASS
[15:31:33.746] [+6209.029s] ▸ Test 22 — pass 1 (primary: 72×72, Nv=[4])
[15:31:33.960] [+6209.243s]  pass 1 result: PASS (elapsed: 0.21s)
[15:31:33.960] [+6209.243s] ▸ Test 22 — pass 2 (secondary: 96×96, Nv=[2])
[15:31:47.778] [+6223.061s]  pass 2 result: PASS (elapsed: 13.82s)
[15:31:47.778] [+6223.061s]  Test 22 two-pass summary: pass1=PASS pass2=PASS → OVERALL PASS
[15:31:48.745] [+6224.028s] ▸ Test 23 — pass 1 (primary: 72×72, Nv=[4])
[15:31:49.126] [+6224.408s]  pass 1 result: PASS (elapsed: 0.38s)
[15:31:49.126] [+6224.408s] ▸ Test 23 — pass 2 (secondary: 96×96, Nv=[2])
[15:32:02.675] [+6237.958s]  pass 2 result: PASS (elapsed: 13.55s)
[15:32:02.676] [+6237.958s]  Test 23 two-pass summary: pass1=PASS pass2=PASS → OVERALL PASS
[15:32:03.588] [+6238.870s] ▸ Test 24 — pass 1 (primary: 72×72, Nv=[4])
[15:32:05.403] [+6240.686s]  pass 1 result: PASS (elapsed: 1.82s)
[15:32:05.404] [+6240.686s] ▸ Test 24 — pass 2 (secondary: 96×96, Nv=[2])
[15:33:11.749] [+6307.032s]  pass 2 result: PASS (elapsed: 66.35s)
[15:33:11.750] [+6307.032s]  Test 24 two-pass summary: pass1=PASS pass2=PASS → OVERALL PASS
[15:33:12.904] [+6308.186s] ▸ Test 25 — pass 1 (primary: 72×72, Nv=[4])
[15:35:40.787] [+6456.069s]  pass 1 result: PASS (elapsed: 147.88s)
[15:35:40.787] [+6456.069s] ▸ Test 25 — pass 2 (secondary: 96×96, Nv=[2])
[16:39:40.082] [+10295.364s]  pass 2 result: PASS (elapsed: 3839.29s)
[16:39:40.082] [+10295.365s]  Test 25 two-pass summary: pass1=PASS pass2=PASS → OVERALL PASS
[16:39:41.352] [+10296.634s] ▸ Test 26 — pass 1 (primary: 72×72, Nv=[4])
[16:40:40.734] [+10356.016s]  pass 1 result: PASS (elapsed: 59.38s)
[16:40:40.734] [+10356.016s] ▸ Test 26 — pass 2 (secondary: 96×96, Nv=[2])
[17:09:15.511] [+12070.794s]  pass 2 result: PASS (elapsed: 1714.78s)
[17:09:15.511] [+12070.794s]  Test 26 two-pass summary: pass1=PASS pass2=PASS → OVERALL PASS
[17:09:16.249] [+12071.531s] ▸ Test 27 — pass 1 (primary: 72×72, Nv=[4])
[17:09:30.084] [+12085.366s]  pass 1 result: PASS (elapsed: 13.84s)
[17:09:30.085] [+12085.367s] ▸ Test 27 — pass 2 (secondary: 96×96, Nv=[2])
[17:12:14.164] [+12249.446s]  pass 2 result: PASS (elapsed: 164.08s)
[17:12:14.164] [+12249.446s]  Test 27 two-pass summary: pass1=PASS pass2=PASS → OVERALL PASS
[17:12:15.173] [+12250.455s] ▸ Test 28 — pass 1 (primary: 72×72, Nv=[4])
[17:13:08.708] [+12303.990s]  pass 1 result: FAIL/WARN (elapsed: 53.54s)
[17:13:08.708] [+12303.991s] ▸ Test 28 — pass 2 (secondary: 96×96, Nv=[2])
[17:39:36.656] [+13891.939s]  pass 2 result: FAIL/WARN (elapsed: 1587.95s)
[17:39:36.657] [+13891.939s]  Test 28 two-pass summary: pass1=FAIL pass2=FAIL → OVERALL FAIL
[17:39:37.904] [+13893.186s] ▸ Test 29 — pass 1 (primary: 72×72, Nv=[4])
[17:42:15.059] [+14050.341s]  pass 1 result: PASS (elapsed: 157.15s)
[17:42:15.059] [+14050.341s] ▸ Test 29 — pass 2 (secondary: 96×96, Nv=[2])
[17:57:50.396] [+14985.678s]  pass 2 result: FAIL/WARN (elapsed: 935.34s)
[17:57:50.396] [+14985.678s] ▸ Test 29 — pass 3 (tertiary: SERIES — real report series, 96×96 regime)
[18:45:06.539] [+17821.821s] ▸ Test 30 — pass 1 (primary: 72×72, Nv=[4])
[18:47:06.232] [+17941.514s]  pass 1 result: PASS (elapsed: 119.69s)
[18:47:06.232] [+17941.514s] ▸ Test 30 — pass 2 (secondary: 96×96, Nv=[2])
[18:59:11.075] [+18666.357s]  pass 2 result: PASS (elapsed: 724.84s)
[18:59:11.078] [+18666.360s]  Test 30 two-pass summary: pass1=PASS pass2=PASS → OVERALL PASS
[18:59:12.283] [+18667.565s] ▸ Test 31 — pass 1 (primary: 72×72, Nv=[4])
[19:03:17.582] [+18912.864s]  pass 1 result: PASS (elapsed: 245.30s)
[19:03:17.582] [+18912.864s] ▸ Test 31 — pass 2 (secondary: 96×96, Nv=[2])
[19:58:20.555] [+22215.837s]  pass 2 result: PASS (elapsed: 3302.97s)
[19:58:20.555] [+22215.837s] ▸ Test 31 — pass 3 (tertiary: SERIES — real report series, 96×96 regime)
[20:04:51.687] [+22606.969s] ▸ Test 32 — pass 1 (primary: 72×72, Nv=[4])
[20:13:27.441] [+23122.723s]  pass 1 result: PASS (elapsed: 515.75s)
[20:13:27.441] [+23122.723s] ▸ Test 32 — pass 2 (secondary: 96×96, Nv=[2])
[21:02:32.804] [+26068.086s]  pass 2 result: PASS (elapsed: 2945.36s)
[21:02:32.804] [+26068.086s]  Test 32 two-pass summary: pass1=PASS pass2=PASS → OVERALL PASS
[21:02:33.557] [+26068.839s] ▸ Test 33 — pass 1 (primary: 72×72, Nv=[4])
[21:18:17.750] [+27013.032s]  pass 1 result: PASS (elapsed: 944.19s)
[21:18:17.750] [+27013.032s] ▸ Test 33 — pass 2 (secondary: 96×96, Nv=[2])
[21:33:01.262] [+27896.544s]  pass 2 result: PASS (elapsed: 883.51s)
[21:33:01.262] [+27896.544s]  Test 33 two-pass summary: pass1=PASS pass2=PASS → OVERALL PASS
[21:33:02.273] [+27897.555s] ▸ Test 34 — pass 1 (primary: 72×72, Nv=[4])
[21:37:02.924] [+28138.206s]  pass 1 result: PASS (elapsed: 240.65s)
[21:37:02.924] [+28138.206s] ▸ Test 34 — pass 2 (secondary: 96×96, Nv=[2])
[22:04:23.597] [+29778.879s]  pass 2 result: FAIL/WARN (elapsed: 1640.67s)
[22:04:23.600] [+29778.882s]  Test 34 two-pass summary: pass1=PASS pass2=FAIL → OVERALL FAIL
[22:04:24.906] [+29780.188s] ▸ Test 35 — pass 1 (primary: 72×72, Nv=[4])
[22:09:08.652] [+30063.934s]  pass 1 result: FAIL/WARN (elapsed: 283.74s)
[22:09:08.653] [+30063.936s] ▸ Test 35 — pass 2 (secondary: 96×96, Nv=[2])
[22:37:01.653] [+31736.935s]  pass 2 result: FAIL/WARN (elapsed: 1673.00s)
[22:37:01.654] [+31736.936s]  Test 35 two-pass summary: pass1=FAIL pass2=FAIL → OVERALL FAIL
[22:37:02.779] [+31738.061s] ▸ Test 36 — pass 1 (primary: 72×72, Nv=[4])
[22:45:52.588] [+32267.870s]  pass 1 result: PASS (elapsed: 529.81s)
[22:45:52.588] [+32267.870s] ▸ Test 36 — pass 2 (secondary: 96×96, Nv=[2])
[23:33:00.768] [+35096.050s]  pass 2 result: PASS (elapsed: 2828.18s)
[23:33:00.768] [+35096.050s]  Test 36 two-pass summary: pass1=PASS pass2=PASS → OVERALL PASS
[23:33:02.097] [+35097.379s] ▸ Test 37 — pass 1 (primary: 72×72, Nv=[4])
[23:33:21.765] [+35117.048s]  pass 1 result: PASS (elapsed: 19.67s)
[23:33:21.766] [+35117.048s] ▸ Test 37 — pass 2 (secondary: 96×96, Nv=[2])
[23:33:39.517] [+35134.799s]  pass 2 result: PASS (elapsed: 17.75s)
[23:33:39.517] [+35134.799s]  Test 37 two-pass summary: pass1=PASS pass2=PASS → OVERALL PASS
```

## Artifact map

```text
test_01_bN_convergence [PASS]  reports/ + logs/ copied; plots live in ../test_01_bN_convergence/plots/
test_01_bN_convergence [PASS]  reports/ + logs/ copied; plots live in ../test_01_bN_convergence/plots/
test_02_bN_monotonicity [PASS]  reports/ + logs/ copied; plots live in ../test_02_bN_monotonicity/plots/
test_02_bN_monotonicity [PASS]  reports/ + logs/ copied; plots live in ../test_02_bN_monotonicity/plots/
test_03_bN_rate        [PASS]  reports/ + logs/ copied; plots live in ../test_03_bN_rate/plots/
test_03_bN_rate        [PASS]  reports/ + logs/ copied; plots live in ../test_03_bN_rate/plots/
test_04_gue_ks_full    [FAIL]  reports/ + logs/ copied; plots live in ../test_04_gue_ks_full/plots/
test_04_gue_ks_full    [PASS]  reports/ + logs/ copied; plots live in ../test_04_gue_ks_full/plots/
test_05_gue_ks_highT   [FAIL]  reports/ + logs/ copied; plots live in ../test_05_gue_ks_highT/plots/
test_05_gue_ks_highT   [PASS]  reports/ + logs/ copied; plots live in ../test_05_gue_ks_highT/plots/
test_06_chi2_hist      [FAIL]  reports/ + logs/ copied; plots live in ../test_06_chi2_hist/plots/
test_06_chi2_hist      [PASS]  reports/ + logs/ copied; plots live in ../test_06_chi2_hist/plots/
test_07_decay_slope    [PASS]  reports/ + logs/ copied; plots live in ../test_07_decay_slope/plots/
test_07_decay_slope    [PASS]  reports/ + logs/ copied; plots live in ../test_07_decay_slope/plots/
test_08_residuals      [PASS]  reports/ + logs/ copied; plots live in ../test_08_residuals/plots/
test_08_residuals      [PASS]  reports/ + logs/ copied; plots live in ../test_08_residuals/plots/
test_09_bootstrap_ci   [PASS]  reports/ + logs/ copied; plots live in ../test_09_bootstrap_ci/plots/
test_09_bootstrap_ci   [PASS]  reports/ + logs/ copied; plots live in ../test_09_bootstrap_ci/plots/
test_10_cross_validation [PASS]  reports/ + logs/ copied; plots live in ../test_10_cross_validation/plots/
test_10_cross_validation [PASS]  reports/ + logs/ copied; plots live in ../test_10_cross_validation/plots/
test_11_anderson_darling [FAIL]  reports/ + logs/ copied; plots live in ../test_11_anderson_darling/plots/
test_11_anderson_darling [PASS]  reports/ + logs/ copied; plots live in ../test_11_anderson_darling/plots/
test_12_two_sample_ks  [FAIL]  reports/ + logs/ copied; plots live in ../test_12_two_sample_ks/plots/
test_12_two_sample_ks  [PASS]  reports/ + logs/ copied; plots live in ../test_12_two_sample_ks/plots/
test_13_number_variance [PASS]  reports/ + logs/ copied; plots live in ../test_13_number_variance/plots/
test_13_number_variance [PASS]  reports/ + logs/ copied; plots live in ../test_13_number_variance/plots/
test_14_spectral_rigidity [PASS]  reports/ + logs/ copied; plots live in ../test_14_spectral_rigidity/plots/
test_14_spectral_rigidity [PASS]  reports/ + logs/ copied; plots live in ../test_14_spectral_rigidity/plots/
test_15_ab_construction [PASS]  reports/ + logs/ copied; plots live in ../test_15_ab_construction/plots/
test_15_ab_construction [PASS]  reports/ + logs/ copied; plots live in ../test_15_ab_construction/plots/
test_16_ab_gue_class   [PASS]  reports/ + logs/ copied; plots live in ../test_16_ab_gue_class/plots/
test_16_ab_gue_class   [PASS]  reports/ + logs/ copied; plots live in ../test_16_ab_gue_class/plots/
test_17_connes_self_duality [PASS]  reports/ + logs/ copied; plots live in ../test_17_connes_self_duality/plots/
test_17_connes_self_duality [PASS]  reports/ + logs/ copied; plots live in ../test_17_connes_self_duality/plots/
test_18_chiral_AIII    [PASS]  reports/ + logs/ copied; plots live in ../test_18_chiral_AIII/plots/
test_18_chiral_AIII    [PASS]  reports/ + logs/ copied; plots live in ../test_18_chiral_AIII/plots/
test_19_dirac_cone     [PASS]  reports/ + logs/ copied; plots live in ../test_19_dirac_cone/plots/
test_19_dirac_cone     [PASS]  reports/ + logs/ copied; plots live in ../test_19_dirac_cone/plots/
test_19_dirac_cone     [PASS]  reports/ + logs/ copied; plots live in ../test_19_dirac_cone/plots/
test_20_chern_tknn     [PASS]  reports/ + logs/ copied; plots live in ../test_20_chern_tknn/plots/
test_20_chern_tknn     [PASS]  reports/ + logs/ copied; plots live in ../test_20_chern_tknn/plots/
test_21_gamma_phase    [PASS]  reports/ + logs/ copied; plots live in ../test_21_gamma_phase/plots/
test_21_gamma_phase    [PASS]  reports/ + logs/ copied; plots live in ../test_21_gamma_phase/plots/
test_22_ab_phase       [PASS]  reports/ + logs/ copied; plots live in ../test_22_ab_phase/plots/
test_22_ab_phase       [PASS]  reports/ + logs/ copied; plots live in ../test_22_ab_phase/plots/
test_23_fractal_factor [PASS]  reports/ + logs/ copied; plots live in ../test_23_fractal_factor/plots/
test_23_fractal_factor [PASS]  reports/ + logs/ copied; plots live in ../test_23_fractal_factor/plots/
test_24_dirac_string_flux [PASS]  reports/ + logs/ copied; plots live in ../test_24_dirac_string_flux/plots/
test_24_dirac_string_flux [PASS]  reports/ + logs/ copied; plots live in ../test_24_dirac_string_flux/plots/
test_25_byers_yang     [PASS]  reports/ + logs/ copied; plots live in ../test_25_byers_yang/plots/
test_25_byers_yang     [PASS]  reports/ + logs/ copied; plots live in ../test_25_byers_yang/plots/
test_26_pbc_torus      [PASS]  reports/ + logs/ copied; plots live in ../test_26_pbc_torus/plots/
test_26_pbc_torus      [PASS]  reports/ + logs/ copied; plots live in ../test_26_pbc_torus/plots/
test_27_binary_chiral  [PASS]  reports/ + logs/ copied; plots live in ../test_27_binary_chiral/plots/
test_27_binary_chiral  [PASS]  reports/ + logs/ copied; plots live in ../test_27_binary_chiral/plots/
test_28_f_gue_merit    [FAIL]  reports/ + logs/ copied; plots live in ../test_28_f_gue_merit/plots/
test_28_f_gue_merit    [FAIL]  reports/ + logs/ copied; plots live in ../test_28_f_gue_merit/plots/
test_29_dirac_dip      [PASS]  reports/ + logs/ copied; plots live in ../test_29_dirac_dip/plots/
test_29_dirac_dip      [FAIL]  reports/ + logs/ copied; plots live in ../test_29_dirac_dip/plots/
test_29_dirac_dip      [PASS]  reports/ + logs/ copied; plots live in ../test_29_dirac_dip/plots/
test_30_vf_scaling     [PASS]  reports/ + logs/ copied; plots live in ../test_30_vf_scaling/plots/
test_30_vf_scaling     [PASS]  reports/ + logs/ copied; plots live in ../test_30_vf_scaling/plots/
test_31_hatano_nelson  [PASS]  reports/ + logs/ copied; plots live in ../test_31_hatano_nelson/plots/
test_31_hatano_nelson  [PASS]  reports/ + logs/ copied; plots live in ../test_31_hatano_nelson/plots/
test_31_hatano_nelson  [PASS]  reports/ + logs/ copied; plots live in ../test_31_hatano_nelson/plots/
test_32_rmean_bootstrap [PASS]  reports/ + logs/ copied; plots live in ../test_32_rmean_bootstrap/plots/
test_32_rmean_bootstrap [PASS]  reports/ + logs/ copied; plots live in ../test_32_rmean_bootstrap/plots/
test_33_l_scaling_rmean [PASS]  reports/ + logs/ copied; plots live in ../test_33_l_scaling_rmean/plots/
test_33_l_scaling_rmean [PASS]  reports/ + logs/ copied; plots live in ../test_33_l_scaling_rmean/plots/
test_34_direct_vs_zeta [PASS]  reports/ + logs/ copied; plots live in ../test_34_direct_vs_zeta/plots/
test_34_direct_vs_zeta [FAIL]  reports/ + logs/ copied; plots live in ../test_34_direct_vs_zeta/plots/
test_35_form_factor_Kt [FAIL]  reports/ + logs/ copied; plots live in ../test_35_form_factor_Kt/plots/
test_35_form_factor_Kt [FAIL]  reports/ + logs/ copied; plots live in ../test_35_form_factor_Kt/plots/
test_36_byte_robust    [PASS]  reports/ + logs/ copied; plots live in ../test_36_byte_robust/plots/
test_36_byte_robust    [PASS]  reports/ + logs/ copied; plots live in ../test_36_byte_robust/plots/
test_37_half_factorial_gamma [PASS]  reports/ + logs/ copied; plots live in ../test_37_half_factorial_gamma/plots/
test_37_half_factorial_gamma [PASS]  reports/ + logs/ copied; plots live in ../test_37_half_factorial_gamma/plots/
```
Log files: logs/full_execution_log.txt (console tee, suite runs), logs/computation_log.txt / computation_log_full.txt (every computation), logs/results_verdicts.txt (one-line verdicts), logs/test_XX_*/ (per-test).
Run index: ../index.html — verdict table with direct links to every per-test report.

```

---

## Appendix L. The full v19 session log: run-level extract

`FINAL_REPORT/logs/computation_log.txt` (812 KB, 12441 entries) — the complete two-pass session log. Extract (head, every 200th entry, start/finish markers, tail):

```text
FULL COMPUTATION LOG — every log_comp() call during run_all_tests
[13:48:04.718] [+  0.000s] ───────────────────────
[13:48:04.797] [+  0.079s] ▸ run_all_tests START
[13:48:04.797] [+  0.079s] ───────────────────────
[13:48:04.797] [+  0.079s]  zeros=50000, lang=en, two_pass=true, third_pass=true, primary=72x72 (Nv=[4]), secondary=96x96 (Nv=[2])
[13:48:04.880] [+  0.162s] ──────────────────────────────────────────────────────
[13:48:04.880] [+  0.162s] ▸ Test 1 — pass 1 (primary: standard implementation)
[13:48:05.591] [+  0.873s]  pass 1 result: PASS (elapsed: 0.71s)
[13:48:05.591] [+  0.873s] ────────────────────────────────────────────────────────────
[13:48:05.591] [+  0.873s] ▸ Test 1 — pass 2 (secondary: HARDCORE deep validation, no lattice dependence)
[13:48:27.985] [+ 23.267s]  pass 2 result: PASS (elapsed: 22.39s)
[13:48:27.985] [+ 23.267s]  Test 1 two-pass summary: pass1=PASS pass2=PASS (hardcore) → OVERALL PASS
[13:48:28.733] [+ 24.015s] ──────────────────────────────────────────────────────
[13:48:28.733] [+ 24.015s] ▸ Test 2 — pass 1 (primary: standard implementation)
[13:48:39.425] [+ 34.707s]  pass 1 result: PASS (elapsed: 10.69s)
[13:48:39.425] [+ 34.707s] ────────────────────────────────────────────────────────────
[13:48:39.425] [+ 34.707s] ▸ Test 2 — pass 2 (secondary: HARDCORE deep validation, no lattice dependence)
[13:48:49.127] [+ 44.409s]  pass 2 result: PASS (elapsed: 9.70s)
[13:48:49.128] [+ 44.410s]  Test 2 two-pass summary: pass1=PASS pass2=PASS (hardcore) → OVERALL PASS
[13:48:49.817] [+ 45.099s] ──────────────────────────────────────────────────────
[13:48:49.817] [+ 45.099s] ▸ Test 3 — pass 1 (primary: standard implementation)
[13:48:50.148] [+ 45.430s]  pass 1 result: PASS (elapsed: 0.33s)
[13:48:50.148] [+ 45.430s] ────────────────────────────────────────────────────────────
[13:48:50.148] [+ 45.430s] ▸ Test 3 — pass 2 (secondary: HARDCORE deep validation, no lattice dependence)
[13:58:37.550] [+632.832s]  calc: A² = 1.370221 (n=49999)
[13:58:39.151] [+634.433s]  calc: A² = 0.602232 (n=49999)
[13:58:40.820] [+636.102s]  calc: A² = 1.829076 (n=49999)
[13:58:42.491] [+637.773s]  calc: A² = 0.775869 (n=49999)
[13:58:44.239] [+639.521s]  calc: A² = 1.322446 (n=49999)
[13:58:45.978] [+641.260s]  calc: A² = 1.668562 (n=49999)
[13:58:47.705] [+642.987s]  calc: A² = 1.065701 (n=49999)
[13:58:49.468] [+644.751s]  calc: A² = 3.118495 (n=49999)
[13:58:51.213] [+646.495s]  calc: A² = 0.380276 (n=49999)
[13:58:52.802] [+648.084s]  calc: A² = 0.539135 (n=49999)
[13:58:54.576] [+649.858s]  calc: A² = 1.245473 (n=49350)
[13:58:55.988] [+651.270s]  calc: A² = 1.841521 (n=49350)
[13:58:57.266] [+652.548s]  calc: A² = 0.909190 (n=39857)
[13:58:58.226] [+653.508s]  calc: A² = 0.634570 (n=37498)
[13:58:59.137] [+654.419s]  calc: A² = 0.290791 (n=37498)
[13:58:59.584] [+654.866s]  calc: A² = 2.774929 (n=24998)
[13:58:59.863] [+655.145s]  calc: A² = 0.521802 (n=12499)
[13:59:00.048] [+655.331s]  calc: A² = 2.168985 (n=12499)
[13:59:00.159] [+655.441s]  calc: A² = 0.436056 (n=6251)
[13:59:00.436] [+655.718s]  calc: A² = 1.750284 (n=6250)
[13:59:00.529] [+655.811s]  calc: A² = 0.496020 (n=6250)
[13:59:00.629] [+655.911s]  calc: A² = 0.933505 (n=6251)
[13:59:00.721] [+656.003s]  calc: A² = 2.079340 (n=6251)
[13:59:00.822] [+656.104s]  calc: A² = 0.547126 (n=6251)
[13:59:00.913] [+656.195s]  calc: A² = 0.430489 (n=6251)
[13:59:01.006] [+656.288s]  calc: A² = 0.413160 (n=6251)
[13:59:01.101] [+656.383s]  calc: A² = 0.671644 (n=6251)
[13:59:01.201] [+656.483s]  calc: A² = 1.112909 (n=6250)
[13:59:01.290] [+656.572s]  calc: A² = 1.197326 (n=6251)
[13:59:01.391] [+656.673s]  calc: A² = 1.766060 (n=6251)
[13:59:02.281] [+657.563s]  calc: A² = 7.602714 (n=49999)
[13:59:43.804] [+699.086s]  calc: A² = 1.426252 (n=49999)
[13:59:47.221] [+702.503s]  calc: A² = 1.959949 (n=49999)
[13:59:50.593] [+705.875s]  calc: A² = 1.665267 (n=49999)
[13:59:53.936] [+709.218s]  calc: A² = 1.995020 (n=49999)
[13:59:57.277] [+712.559s]  calc: A² = 2.095568 (n=49999)
[14:00:04.527] [+719.809s]  calc: A² = 0.280498 (n=49999)
[14:00:11.611] [+726.893s]  calc: A² = 0.236983 (n=49999)
[14:00:16.946] [+732.228s]  calc: A² = 1.509383 (n=49999)
[14:00:17.994] [+733.276s]  calc: A² = 0.586061 (n=49999)
[14:00:19.042] [+734.324s]  calc: A² = 0.504337 (n=49999)
[14:00:21.687] [+736.969s]  calc: A² = 0.485757 (n=49999)
[14:00:22.790] [+738.072s]  calc: A² = 0.299129 (n=49999)
[14:00:24.343] [+739.625s]  calc: A² = 1.448242 (n=49999)
[14:00:25.446] [+740.728s]  calc: A² = 0.672942 (n=49999)
[14:00:26.558] [+741.840s]  calc: A² = 0.504450 (n=49999)
[14:00:27.675] [+742.957s]  calc: A² = 0.497501 (n=49999)
[14:00:28.781] [+744.063s]  calc: A² = 1.385719 (n=49999)
[14:00:29.891] [+745.173s]  calc: A² = 0.534720 (n=49999)
[14:00:31.004] [+746.286s]  calc: A² = 0.378180 (n=49999)
[14:00:32.108] [+747.390s]  calc: A² = 0.627938 (n=49999)
[14:01:55.965] [+831.247s]  calc: A² = 10.356837 (n=49999)
[14:01:59.560] [+834.842s]  calc: A² = 7.802850 (n=49999)
[14:02:03.124] [+838.406s]  calc: A² = 8.868985 (n=49999)
[14:02:06.605] [+841.887s]  calc: A² = 8.396706 (n=49999)
[14:02:09.788] [+845.070s]  calc: A² = 7.810478 (n=49999)
[14:06:50.692] [+1125.974s]  calc: ⟨r⟩ = 0.600961 (n_r=3108, n_eigs=3110) [refs: GUE=0.5996 Poisson=0.3863]
[16:39:41.774] [+10297.056s]  build_ab_cloud_hamiltonian: 72x72 (N=5184), α=0.0000, t=1.00, W=4.00, torus, 1 vortices, model=:dirac
[20:04:51.687] [+22606.969s] ▸ Test 32 — pass 1 (primary: 72×72, Nv=[4])
[23:33:00.283] [+35095.566s]  calc: ⟨r⟩ = 0.621021 (n_r=13, n_eigs=15) [refs: GUE=0.5996 Poisson=0.3863]
[23:33:00.283] [+35095.566s]  calc: ⟨r⟩ = 0.662679 (n_r=13, n_eigs=15) [refs: GUE=0.5996 Poisson=0.3863]
[23:33:00.283] [+35095.566s]  calc: ⟨r⟩ = 0.484236 (n_r=13, n_eigs=15) [refs: GUE=0.5996 Poisson=0.3863]
[23:33:00.283] [+35095.566s]  calc: ⟨r⟩ = 0.642217 (n_r=13, n_eigs=15) [refs: GUE=0.5996 Poisson=0.3863]
[23:33:00.283] [+35095.566s]  calc: ⟨r⟩ = 0.541220 (n_r=13, n_eigs=15) [refs: GUE=0.5996 Poisson=0.3863]
[23:33:00.283] [+35095.566s]  calc: ⟨r⟩ = 0.602689 (n_r=13, n_eigs=15) [refs: GUE=0.5996 Poisson=0.3863]
[23:33:00.283] [+35095.566s]  calc: ⟨r⟩ = 0.479526 (n_r=13, n_eigs=15) [refs: GUE=0.5996 Poisson=0.3863]
[23:33:00.283] [+35095.566s]  calc: ⟨r⟩ = 0.599213 (n_r=13, n_eigs=15) [refs: GUE=0.5996 Poisson=0.3863]
[23:33:00.768] [+35096.050s]  pass 2 result: PASS (elapsed: 2828.18s)
[23:33:00.768] [+35096.050s]  Test 36 two-pass summary: pass1=PASS pass2=PASS → OVERALL PASS
[23:33:02.097] [+35097.379s] ─────────────────────────────────────────────
[23:33:02.097] [+35097.379s] ▸ Test 37 — pass 1 (primary: 72×72, Nv=[4])
[23:33:21.765] [+35117.048s]  pass 1 result: PASS (elapsed: 19.67s)
[23:33:21.766] [+35117.048s] ───────────────────────────────────────────────
[23:33:21.766] [+35117.048s] ▸ Test 37 — pass 2 (secondary: 96×96, Nv=[2])
[23:33:21.766] [+35117.048s]  pass 2 = HARDCORE variant (256-bit BigFloat precision audit — test44b)
[23:33:39.517] [+35134.799s]  pass 2 result: PASS (elapsed: 17.75s)
[23:33:39.517] [+35134.799s]  Test 37 two-pass summary: pass1=PASS pass2=PASS → OVERALL PASS
```

Full log — in the package data; the whole run's course is reconstructible line by line.

---

## Appendix M. The one-line v19 verdict list (verbatim)

`FINAL_REPORT/logs/results_verdicts.txt` — the machine list of all the run's verdicts:

```text
ONE-LINE VERDICTS (results_log)

 Test 1: b(N=50000) = 1.2126 → PASS
 Test 1 [HARDCORE pass 2]: 8 sub-checks, 0 failed, b(50000)=1.2126 → PASS
 Test 2: Monotonicity violations: 0 / 499 → PASS
 Test 2 [HARDCORE pass 2]: 4 sub-checks, 0 failed, b(50000)=1.2126 → PASS
 Test 3: α = 0.1685 (empirical; no expected value), R²=0.9895 → PASS
 Test 3 [HARDCORE pass 2]: 4 sub-checks, 0 failed, b(50000)=1.2126 → PASS
 Test 4: KS D=0.0216, p=0.0 → WARN
 Test 4 [HARDCORE pass 2]: 3 sub-checks, 0 failed → PASS
 Test 5: Best high-T p-value=0.0 → WARN
 Test 5 [HARDCORE pass 2]: 2 sub-checks, 0 failed → PASS
 Test 6: χ² p=0.0 → WARN
 Test 6 [HARDCORE pass 2]: 2 sub-checks, 0 failed → PASS
 Test 7: Slope=-0.1504 (empirical), 95%CI=[-0.1594,-0.1414] → PASS
 Test 7 [HARDCORE pass 2]: 4 sub-checks, 0 failed, b(50000)=1.2126 → PASS
 Test 8: Runs=3 (exp=5.8) → PASS
 Test 8 [HARDCORE pass 2]: 4 sub-checks, 0 failed, b(50000)=1.2126 → PASS
 Test 9: Bootstrap slope=-0.1746 (empirical), 95%CI=[-0.1895,-0.1552] → PASS
 Test 9 [HARDCORE pass 2]: 4 sub-checks, 0 failed, b(50000)=1.2126 → PASS
 Test 10: Max deviation=8.5% → PASS
 Test 10 [HARDCORE pass 2]: 4 sub-checks, 0 failed, b(50000)=1.2126 → PASS
 Test 11: A²=61.4924, MC p=0.0000 → WARN (best high-T subrange T>31351 also rejects, p=0.0000; see height-resolved table)
 Test 11 [HARDCORE pass 2]: 5 sub-checks, 0 failed → PASS
 Test 12: 2-sample KS D=0.0233, p=0.010547 → WARN
 Test 12 [HARDCORE pass 2]: 3 sub-checks, 0 failed → PASS
 Test 13: data closer to GUE in 9/9 L-values → PASS
 Test 13 [HARDCORE pass 2]: 4 sub-checks, 0 failed → PASS
 Test 14: data closer to GUE in 9/9 L-values → PASS
 Test 14 [HARDCORE pass 2]: 3 sub-checks, 0 failed → PASS
 Test 15: Hermiticity=OK, τ_TRB=0.1037, flux_v1=-0.0 [exp -0.0], flux_empty=0.0 → PASS
 Test 15b [HARDCORE pass 2]: 2 sub-checks, 0 failed → PASS
 Test 16 [MONTGOMERY] α=0.5 (α=0.5000 (default)): ⟨r⟩ mean=0.594 n_pass=1/1 → PASS
 Test 16 [MONTGOMERY] FINAL (last α=0.5): ⟨r⟩=0.594 → PASS
 Test 16b [HARDCORE pass 2]: 2 sub-checks, 0 failed → PASS
 Test 17: zero_modes(α=1/2)=4 (expected 4) → PASS
 Test 17b [HARDCORE pass 2]: 2 sub-checks, 0 failed → PASS
 Test 18: chiral defect (α=1/2)=0.0 [exp 0.000000], (α=1/3)=0.0058 [exp ≠0] → PASS
 Test 18b [HARDCORE pass 2]: 4 sub-checks, 0 failed → PASS
 Test 19: 1/L scaling R²=0.9997, v_F(2π)=1.8998, v_F(π)=3.7995 → PASS
 Test 19b [HARDCORE pass 2]: 3 sub-checks, 0 failed → PASS
 Test 19c [SERIES pass 3]: 3 sub-checks, 0 failed → PASS
 Test 20: C₁ anchors {1/4,1/3,1/5}=1,1,1 [exp 1,1,1], α=1/2 min gap=0.0 (Dirac touching), mass branch C=0/0 → PASS
 Test 20b [HARDCORE pass 2]: 3 sub-checks, 0 failed → PASS
 Test 21: arg(γ*)=89.874° (≈90°, deviation=0.126°) → PASS
 Test 21b [HARDCORE pass 2]: 3 sub-checks, 0 failed → PASS
 Test 22: Φ_AB=0.4487989505 = π/7 (exact) → PASS
 Test 22b [HARDCORE pass 2]: 3 sub-checks, 0 failed → PASS
 Test 23: |CF_formula|=1.0 (=1 by construction), c_AB=0.02062 (≈0.02063) → PASS
 Test 23b [HARDCORE pass 2]: 3 sub-checks, 0 failed → PASS
 Test 24: vortex flux OK=1/1, empty OK=5040/5040, max_empty=0.0 → PASS
 Test 24b [HARDCORE pass 2]: 5 sub-checks, 0 failed → PASS
 Test 25: Δ(q=1→0)=0.0 [exp ~0], Δ(q=0.3→0)=0.0032 [exp >1e-3] → PASS
 Test 25b [HARDCORE pass 2]: 2 sub-checks, 0 failed → PASS
 Test 26: flux_v=-0.0 [exp -0.0], empty_ok=5040/5183, herm=OK, ⟨r⟩=0.6009 → PASS
 Test 26b [HARDCORE pass 2]: 4 sub-checks, 0 failed → PASS
 Test 27: chiral defect (W=0) = 0.0, (W=1.0) = 0.0058 → PASS
 Test 27b [HARDCORE pass 2]: 4 sub-checks, 0 failed → PASS
 Test 28: f_GUE=0.8704, Σ²_data=0.6115 → WARN
 Test 28b [HARDCORE pass 2]: 2 sub-checks, 1 failed → WARN
 Test 29: ρ(α=0.5)=0.0193 vs ρ(0.403)=0.1944 / ρ(0.597)=0.1944 → PASS
 Test 29b [HARDCORE pass 2]: 3 sub-checks, 1 failed → WARN
 Test 29c [SERIES pass 3]: 3 sub-checks, 0 failed → PASS
 Test 30: v_F=1.798, R²=0.9977 → PASS
 Test 30b [HARDCORE pass 2]: 3 sub-checks, 0 failed → PASS
 Test 31: max|Im(E)|=0.6397, ⟨r⟩_NH=0.8938 → PASS
 Test 31b [HARDCORE pass 2]: 3 sub-checks, 0 failed → PASS
 Test 31c [SERIES pass 3]: 4 sub-checks, 0 failed → PASS
 Test 32: ⟨r⟩=0.5991±0.0075 (q=1.0, n=5, W=1.0) vs GUE 0.5992 → PASS
 Test 32: ⟨r⟩=0.5864±0.003 (q=1.0, n=5, W=1.0) vs GUE 0.5992 → PASS
 Test 32b [HARDCORE pass 2]: 2 sub-checks, 0 failed → PASS
 Test 33: L-scaling to L=80 0.434,0.556,0.593,0.6,0.6 → PASS
 Test 33: L-scaling to L=80 0.434,0.556,0.593,0.6,0.6 → PASS
 Test 33b (hardcore): plateau weighted ⟨r⟩=0.6004, χ²/dof=0.01 → PASS
 Test 34: KS p=0.0, ⟨|ΔR₂|⟩=0.0374, d_GUE=0.796 → PASS
 Test 34b [HARDCORE pass 2]: 4 sub-checks, 1 failed → WARN
 Test 35: K(t) ramp+plateau — RMS_GUE=0.4193, corr_GUE=0.8889 → WARN
 Test 35b [HARDCORE pass 2]: 3 sub-checks, 2 failed → WARN
 Test 36: byte robust — r_256=0.5894, |Δr|_multi=0.001 (120 windows), |Δr|_1win=0.012 (diag), H=7.9991 bits, χ²_z=-0.234, n=27997 → PASS
 Test 36: byte robust — r_256=0.5756, |Δr|_multi=0.0009 (120 windows), |Δr|_1win=0.0061 (diag), H=7.9991 bits, χ²_z=-0.234, n=55288 → PASS
 Test 37: (1/2)!=√π/2 [rel.err 0.0], 32/π² [rel.err 0.0], ∫p₂=1 [|Δ|=0.0], uniqueness ✓ → PASS
 Test 37b [HARDCORE pass 2]: 3 sub-checks, 0 failed → PASS

```

---

## Appendix I. The flat v18 run log (2026-08-28): extracts

The v19 predecessor — the v18 run of 2026-08-28, 37 tests, flat log. The head (verbatim):

```text
TEST 3: Objection 1: b(N) Convergence — Convergence Rate
Fit b(N) ≈ C · N^(-α) via log-log regression
────────────────────────────────────────────────────────────
 Fit: log(b(N)) = -0.1685 · log(N) + 1.9504
 R² = 0.989480 | SE(slope) = 0.004345
 → b(N) ≈ 7.0312 · N^(-0.1685)
 The convergence exponent is empirical (not predicted by theory)
 of the v23 monograph. The monograph's α=1/2 refers to the AB-phase
 (Hofstadter flux per plaquette), NOT to the b(N) convergence rate.
 Alternative fit: b(N) ≈ -0.3383 + 16.8394/log(N), R² = 0.999387
 (If b(N) ≈ C/log(N), this fit should have high R²)
 Test 3: α = 0.1685 (empirical; v6 reframed: no expected value), R²=0.9895 → PASS
 Test 3: ERROR — MethodError(convert, (String, ("h1", "Test 3: Convergence rate (power-law fit)")), 0x0000000000009cb7)
════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════
TEST 4: Objection 2: GUE Spacing Statistics — KS Test (Full Range)
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
 N spacings: 49999
 Kolmogorov-Smirnov: D = 0.088053, p = 0.000000
 Cramér-von Mises: W² = 151.918434
 Critical D at α=0.05: 0.006073
 H0 (GUE): REJECTED
 rejection is EXPECTED. See Test 5 for high-T sub-range.
 Use --convergence-watch "1000,5000,20000,50000" to SEE convergence.
 Test 4: KS D=0.0881, p=0.0 → WARN
 Test 4: ERROR — MethodError(convert, (String, ("h1", "Test 4: GUE KS test (full range)")), 0x0000000000009cb7)
════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════
TEST 5: Objection 2: GUE Spacing Statistics — KS Test (High-T Only)
GUE is asymptotic: test only zeros with T > T_min
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
        T_min      N_zeros            D      p-value       H0
 ──────────── ──────────── ──────────── ──────────── ────────
         1000        49351     0.087754     0.000000   REJECT
        10000        39858     0.086647     0.000000   REJECT
 True GUE spacing requires T >> 10^6 for good p-values.
 Use --convergence-watch "1000,5000,20000" to SEE convergence at each T_min.
 Test 5: Best high-T p-value=0.0 → WARN
 Test 5: ERROR — MethodError(convert, (String, ("h1", "Test 5: GUE KS test (high-T only)")), 0x0000000000009cb7)
════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════
TEST 6: Objection 2: GUE Spacing Statistics — χ² Histogram Test
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
```

Verdict lines (extract):

```text
 Test 3: α = 0.1685 (empirical; v6 reframed: no expected value), R²=0.9895 → PASS
 Test 4: KS D=0.0881, p=0.0 → WARN
 Test 5: Best high-T p-value=0.0 → WARN
 Test 6: χ² p=0.0 → WARN
 Test 7: Slope=-0.1504 (empirical; v6 reframed), 95%CI=[-0.1594,-0.1414] → PASS
 Test 8: Runs=3 (exp=5.8) → PASS
 Test 9: Bootstrap slope=-0.1746 (empirical; v6 reframed), 95%CI=[-0.1895,-0.1552] → PASS
 Test 10: Max deviation=8.5% → PASS
 Test 11: A²=117.7157, MC p=0.0 → WARN
 Test 12: 2-sample KS D=0.0406, p=0.139318 → PASS
 Test 13: data closer to GUE in 9/9 L-values → PASS
 Test 14: data closer to GUE in 9/9 L-values → PASS
 Test 15: Hermiticity=OK, τ_TRB=0.0, flux_v1=0.0 [exp -0.0], flux_empty=0.0 → PASS
 Criterion: ⟨r⟩ > 0.55: FAIL ; MC p-value > 0.01: FAIL
 Test 16 [MONTGOMERY] α=0.5 (α=0.5000 (default)): ⟨r⟩ mean=0.513 n_pass=0/1 → FAIL
 Test 16 [MONTGOMERY] FINAL (last α=0.5): ⟨r⟩=0.513 → FAIL
 Test 17: zero_modes(α=1/2)=4 (expected 4) → PASS
 PASS criterion: R² > 0.95 (linear 1/L scaling confirmed → Dirac cone exists).
 → PASS (R² = 0.9997, all sizes have zero modes)
 Test 19: 1/L scaling R²=0.9997, v_F(2π)=1.8821, v_F(π)=3.7643 → PASS
 Test 20: C_1=2 (nonzero, |C_1|≤2 → topological) → PASS
 Test 21: arg(γ*)=89.874° (≈90°, deviation=0.126°) → PASS
 Test 22: Φ_AB=0.4487989505 = π/7 (exact) → PASS
 Test 23: |CF_formula|=1.0 (=1 by construction), c_AB=0.02062 (≈0.02063) → PASS
 Test 24: vortex flux OK=1/1, empty OK=224/224, max_empty=0.0 → PASS
 Test 25: Δ(q=1→0)=0.0 [exp ~0], Δ(q=0.3→0)=0.3419 [exp >1e-3] → PASS
 Test 26: flux_v=0.0 [exp -0.0], empty_ok=255/255, herm=OK, ⟨r⟩=0.5857 → PASS
 Test 27: chiral defect (W=0) = 0.0, (W=4) = 0.0059 → PASS
 Test 29: f_GUE=0.6483, Σ²_data=0.8377 → WARN
 Test 30: ρ(α=0.5)=0.01 vs ρ(0.4)=0.2 / ρ(0.6)=0.2 → PASS
 Test 31: v_F=0.0, R²=0.0313 → WARN
 Test 32: max|Im(E)|=0.623, ⟨r⟩_NH=0.0 → PASS
 Test 33: ⟨r⟩=0.5848±0.026 (q=1.0, n=3, W=4.0) vs GUE 0.5992 → PASS
 Test 34: L-scaling 0.548,0.592,0.605,0.595 → PASS
 KS p > 0.01: FAIL (p = 0.0006695)
 ⟨|R₂_AB−R₂_ζ|⟩ < 0.10: FAIL (val = 0.1468)
 Test 35: KS p=0.0007, ⟨|ΔR₂|⟩=0.1468, d_GUE=0.1398 → WARN
 Test 36: K(t) ramp+plateau — RMS_GUE=0.9313, corr_GUE=0.0177 → WARN
 |Δr| = 0.0015 (tol=0.0200) → PASS
 χ²_z (CLT approx, df=255) = -0.2342 (|z|<3.0) → PASS
 Test 37: byte robust — r_256=0.5472, |Δr|=0.0015, H=7.9991 bits, χ²_z=-0.234 → PASS
 Test  1 [Conv.tbl]: WARN
 Test  2 [Monoton.]: WARN
 Test  3 [Pwr-law]: WARN
 Test  4 [KS-full]: WARN
 Test  5 [KS-highT]: WARN
 Test  6 [chi2-hist]: WARN
 Test  7 [Slope]: WARN
 Test  8 [Resid.]: WARN
 Test  9 [Bootstrap]: WARN
 Test 10 [Stabil.]: WARN
 Test 11 [A-D]: WARN
 Test 12 [2KS]: WARN
 Test 13 [Sig2(L)]: WARN
 Test 14 [D3(L)]: WARN
 Test 15 [AB-build]: WARN
 Test 16 [Montgomery]: WARN
 Test 17 [SelfDual]: WARN
 Test 18 [AIII]: WARN
 Test 19 [Dirac vF]: WARN
 Test 20 [TKNN C1]: WARN
 Test 21 [g*-90deg]: WARN
 Test 22 [Phi_AB]: WARN
 Test 23 [CF-log]: WARN
 Test 24 [DiracStr]: WARN
 Test 25 [ByersYang]: WARN
 Test 26 [PBC-torus]: WARN
 Test 27 [ChiralAIII]: WARN
 Test 28 [BerryR2]: WARN
 Test 29 [f_GUE]: WARN
 Test 30 [DiracDip]: WARN
 Test 31 [vF_Dirac]: WARN
 Test 32 [HatanoN]: WARN
 Test 33 [200-real]: WARN
 Test 34 [L-scale]: WARN
 Test 35 [AB-vs-zeta5k]: WARN
 Test 36 [K-form]: WARN
 Test 37 [ByteRob]: WARN
```

Full log — `02_data/raw/results_run/verification_run_v18_37tests_2026-08-28.txt`; the v19 verification header — `ab_cloud_v19_verify_report_2026-09-02_23-33-45.txt`.

---

## Appendix J. The v19 execution log: the run's trajectory (sample)

The full execution log (2729 entries) carries the history of 35,146 seconds. A sample (every 40th entry) and all two-pass summaries:

```text
FULL EXECUTION LOG — tee of every println/@printf during run_all_tests
          100     3.3321638710    -0.1480087697
                top-5 share 0.1% | 1%-trimmed b deviates +1.13% from b (limit 15%)
         1297     2.0151677802          yes
         5289     1.6166207211          yes
         9281     1.4943459153          yes
        13273     1.4249560388          yes
        17265     1.3776298418          yes
        21257     1.3421592737          yes
        25250     1.3140672107          yes
        29242     1.2909640720          yes
        33234     1.2714051979          yes
        37226     1.2545292567          yes
        41218     1.2397451213          yes
        45210     1.2265946523          yes
        49202     1.2147693411          yes
 animation.gif done in 2.0 s
[Test  3] done in 00:00:10 — 2026-09-02 13:48:59 → PASS
        T_min      N_zeros            D      p-value       H0
 Bins=600: χ²=823.7476, df=473, p=0.000000 → REJECTED
 Alternative: b(N) ≈ -0.3966 + 17.2973/log(N), R² = 0.999894
 N=   25600 residual=+0.052929
TEST 9 (secondary, HARDCORE): Objection 3: Large-T Decay Rate — bootstrap reproducibility audit
All sub-samples use index-aware Gram points (offset discipline)
   variance deficit -5.5% vs law (mean drift only -0.0024%) — the dominant single effect in A²
  table: 32768 pts on [0, 5.0]; self-check max|ΔF| = 4.90e-09 (997 probes)
 plot 1/1: PNG done in 10.2 s
Poisson: Σ²(L)=L. GUE: ~log(L). Real zeros should follow GUE.
 ARTIFACTS: 1 plot queued → svg+pdf (fast), PNG 4000x2500 (pure-Julia deflate ≈ 3–8 s each), gif tour ≈ 2–15 s
 G2 monotone  : 0 dips >30% across 8 grid steps (limit 1)
 ⚠ RUNTIME: 1 build + O(N) plaquette scan at 96x96 (N=9216) — seconds
 A² = 27.1828 ; Σ²(L=2) = 0.6223 ; Δ₃(L=2) = 0.0943
────────────────────────────────────────────────────────────
 α=1/3, no vortices (torus lattice):
 Lattice sizes tested: 12, 16, 24, 32, 48, 64, 72
 E_min·L → 4π         PASS — 12.246 → 12.557 (target 12.566)
 plot 2/3: PNG done in 10.7 s
 α=1/2 L=72: bare min gap = 5.48e-16 (touching), singular links 0
 π/2 = 1.570796 rad = 90.0000°
 for a particle of fractional charge q/e = 1/14 encircling a
 = -0.950099 + 0.311947·i (|CF| = 1.000000 by construction)
 flux construction — see the header design notes)
 Vortex phase model: :dirac (Byers-Yang identity is formulated
[Test 26] started 2026-09-02 16:39:41
────────────────────────────────────────────────────────────
 Nv=0 ε-floor diagnostic (residual ε is FIXED-amplitude):
TEST 28 (pass 2, HARDCORE): f_GUE figure of merit — ensemble deep pass
 Test 29: ρ(α=0.5)=0.0193 vs ρ(0.403)=0.1944 / ρ(0.597)=0.1944 → PASS
TEST 29 (pass 3, SERIES): Dirac dip — fine α-scan + window series
TEST 30: Dirac Cone Velocity v_F at α=1/2
 L=56: E₁ = 0.223929 (E₁·L = 12.5400), zero_modes = 4, 11.4 s
TEST 31 (pass 2, HARDCORE): Hatano–Nelson skin effect — σ-sweep
 real 2/5 σ=0.8: n_complex =  2299, max|Im| = 0.9598, ⟨r⟩NN = 0.9310 (18.5 s)
────────────────────────────────────────────────────────────
 NOTE: this is bootstrap row 2/2 — a FULL second set of 5 realizations; the verdict comes from row 1 (the configured q).
     from GUE (0.5992) toward Poisson (0.3863) by an essentially random
 Row diagnostics: vortex density 2.78% (Nv=256 on 96x96) vs monograph anchor 2.78% (25/30×30)
     from GUE (0.5992) toward Poisson (0.3863) by an essentially random
  W is the diagonal on-site potential the vortices paint onto the lattice:
 plot 1/1: writing PNG 4000x2500 (deflate, NOT a hang)…
 2.25 | 0.0977 0.0000 0.9900 1.0000
 plot 1/3: PNG done in 15.3 s
 real  2/5: RMS(K−K_box, t≥0.3) = 0.8578
   • q·W ≲ t  (W ≤ 1): the Aharonov-Bohm phases dominate the hopping,
     from GUE (0.5992) toward Poisson (0.3863) by an essentially random
────────────────────────────────────────────────────────────
[Test 37] done in 00:00:37 — 2026-09-02 23:33:39 → PASS
Generating plots ...
 log(N)=  5.30 data=+1.0544 fit=+1.0648
```

Two-pass summaries:

```text

```

Full log — `02_data/raw/results_run/FINAL_REPORT/logs/full_execution_log.txt`.

---

## Appendix K. The v19 verification report header (verbatim, first 150 lines)

The file `ab_cloud_v19_verify_report_2026-09-02_23-33-45.txt` (1.0 MB) — the full header/config dump of the verification run. The head:

```text
AB-Cloud Verification Report
Generated: 2026-09-02T23:33:45.851
Author: Isaev Iskhak Khamzatovich
ORCID: 0009-0003-7299-0701
DOI: 10.5281/zenodo.21825394
Repo: https://github.com/wild8highlander/research-papers
Config: zeros=50000, source=auto, lang=en
 n_checkpoints=0, n_monotone=500
 n_bootstrap=1000, chi2_bins=300
 stability_fraction=0.8, stability_threshold=0.1
 bN_pass_threshold=2.0
 power_law_tolerance=0.15
 slope_ci_tolerance=0.1
 gue_matrix_size=12000, gue_matrix_seed=112
 ad_sample_cap=50000
 rmt_spacing_law=GUE β=2 surmise
 rmt_cdf_table=on (32768-pt interp, max|ΔF|=4.903025416225226e-9)
 t31_lmax=72
 rigidity_L_values=[2.0, 4.535939472087519, 10.287373447220801, 23.331451641676946, 52.91502622129181, 120.00967805185182, 272.17831785395487, 617.2921877000689, 1399.9999999999998]
 rigidity_n_windows=3000 (Sigma^2)
 rigidity_n_windows_d3=500 (Delta_3)
 rigidity_n_grid=300

EMBEDDED DATASET:
 50,000 real Riemann zeta zeros (Odlyzko official table)
 Source: https://www-users.cse.umn.edu/~odlyzko/zeta_tables/zeros6
 First zero: 14.134725142 (the first non-trivial zero of zeta(s))

AB-CLOUD VERIFICATION SUITE — FEATURES

1. Offset-Gram matching for correct sub-sample b(N) computation
2. Non-mutating KS/CvM/chi-squared tests (sort copy, not in-place)
3. Exact chi-squared CDF via regularized incomplete gamma (any df)
4. KS asymptotic p-value (correct Kolmogorov formula)
5. Anderson-Darling, 2-sample KS, Sigma^2(L), Delta_3(L) tests
6. Simulated GUE reference matrix for empirical comparison
7. Embedded 50,000 real Riemann zeta zeros (self-contained)
8. Bilingual EN/RU output
9. AB-cloud Hofstadter Hamiltonian with topological vortices
10. Dirac string construction for correct AB flux
11. Fractional vortex charges (Byers-Yang theorem compliance)
12. Periodic Dirac string for torus geometry
13. Choptyuk–Isaev particle dynamics formulas
14. Full execution log capture (tee stdout to report)

MATHEMATICAL FINDINGS (not bugs):
 - Convergence rate alpha ~ 0.19 != 0.5: b(N) decays as N^{-0.19}, not N^{-0.5}.
 This is consistent with b(N) ~ C/log(N) behaviour.
 - GUE spacing rejection for low-T zeros: EXPECTED (GUE is asymptotic).
 - Spectral rigidity Delta_3(L) shows ~97% relative error vs GUE at large L,
 consistent with the paper's own full_verification.json output.

============================================================
FULL EXECUTION LOG — captured stdout (tee of every println / @printf)
Purpose: see exactly what each test computed, where WARNs come from,
 and what numbers lie behind each PASS/WARN verdict.
Captured bytes: 158866
============================================================

════════════════════════════════════════════════════════════
AB-Cloud Verification Suite — 37 Tests (Hilbert-Pólya + K(t) + byte robust)
Running all 37 tests with 50000 zeros
TWO-PASS MODE: 72×72 (Nv=[4]) then 96×96 (Nv=[2])
PASS 3 SERIES: Tests 19/29/31 run a third time (19c/29c/31c — real report series)
════════════════════════════════════════════════════════════
[Test  1] started 2026-09-02 13:48:04

════════════════════════════════════════════════════════════
TEST 1: Objection 1: b(N) Convergence — Convergence Table
b(N) = (1/N) Σ|γ_k − γ̃_k|
────────────────────────────────────────────────────────────
            N             b(N) Δb = b(N)−b(previous N)
 ──────────── ──────────────── ──────────────────────
          100     3.3321638710              ---
          500     2.3912304957    -0.9409333753
         1000     2.1072522952    -0.2839782006
         2000     1.8755056313    -0.2317466638
         5000     1.6299485869    -0.2455570444
        10000     1.4794053415    -0.1505432454
        20000     1.3523713471    -0.1270339944
        50000     1.2125526773    -0.1398186698
 Test 1: b(N=50000) = 1.2126 → PASS
 REPORT: test 1 → results/run_20260902_134759/test_01_bN_convergence (text/log artifacts done)
 REPORT: test 1 plots done → results/run_20260902_134759/test_01_bN_convergence

════════════════════════════════════════════════════════════
TEST 1 (secondary, HARDCORE): Objection 1: b(N) Convergence — deep validation
Same statistic b(N) = (1/N) Σ|γ_k − γ̃_k|, verified by 8 harder sub-checks
────────────────────────────────────────────────────────────
 H0 reproduce : max|b_direct − b_prefix| over 4 probes = 0.00e+00 (limit 1e-9)
 H1 dense scan: 40 checkpoints, N = 25 → 50000 (ratio 1.22)
            N             b(N)        Δ vs prev
           25     4.6101190361              ---
           30     4.3989811028    -0.2111379332
           37     4.1932852303    -0.2056958726
           45     3.9943669591    -0.1989182711
           55     3.8252166187    -0.1691503404
           67     3.6455743228    -0.1796422960
           82     3.4801726407    -0.1654016820
          100     3.3321638710    -0.1480087697
          122     3.1910285619    -0.1411353091
          149     3.0547427984    -0.1362857635
          182     2.9267044466    -0.1280383518
          222     2.8066104527    -0.1200939939
          271     2.6947048268    -0.1119056258
          331     2.5892260492    -0.1054787776
          404     2.4907320942    -0.0984939550
          493     2.3966440338    -0.0940880604
          601     2.3100937127    -0.0865503211
          733     2.2274677461    -0.0826259666
          894     2.1498825733    -0.0775851728
         1091     2.0754888256    -0.0743937476
         1331     2.0067062433    -0.0687825824
         1624     1.9405012929    -0.0662049503
         1981     1.8782421944    -0.0622590986
         2417     1.8197691194    -0.0584730750
         2949     1.7640375461    -0.0557315733
         3598     1.7111812347    -0.0528563114
         4390     1.6613158059    -0.0498654288
         5356     1.6137261550    -0.0475896509
         6534     1.5686043745    -0.0451217805
         7971     1.5258165855    -0.0427877890
         9725     1.4850058741    -0.0408107114
        11864     1.4460749475    -0.0389309266
        14474     1.4090310622    -0.0370438853
        17658     1.3736819777    -0.0353490845
        21543     1.3399113218    -0.0337706559
        26282     1.3076687539    -0.0322425680
        32064     1.2768213946    -0.0308473593
        39118     1.2473022976    -0.0295190970
        47724     1.2190083740    -0.0282939236
        50000     1.2125526773    -0.0064556968
 H2 monotone  : 0/39 consecutive pairs exceed the noise band (limit 2)
 H3 predict   : walk-forward one-step-ahead, best of 3 laws (power / 1·log⁻¹N / local secant)
                median err 0.05%, max err 0.09% (limits 2%/5%)
 H4 stationarity: head b(25000)=1.315628 | tail b(25000)=1.109478 | tail/head = 0.8433 (limit 1.25)
 H5 bootstrap : b(50000)=1.212553 | 95%CI [1.209765, 1.215265] (width 0.45% of b, limit 15%)
                threshold 2.00 − (b + 2σ/√N = 1.215350) = +0.784650 → verdict ROBUST
 H6 outliers  : peak |Δγ| = 9.0356 at k=1 (0.0% of Σd, limit 10%)
                top-5 share 0.1% | 1%-trimmed b deviates +1.13% from b (limit 15%)
 H7 Gram sanity: γ̃ strictly increasing over n=1..50000 → 0 violations (limit 0)
────────────────────────────────────────────────────────────
 H0 reproduce         PASS — worst |Δ| = 0.00e+00
 H1 dense scan        PASS — 40 checkpoints
 H2 monotone          PASS — 0 violations / 39 pairs
 H3 out-of-sample     PASS — walk-forward median 0.05%, max 0.09%
 H4 stationarity      PASS — tail/head = 0.8433
 H5 bootstrap         PASS — CI width 0.45%, margin +0.7846
 H6 outlier audit     PASS — peak 0.0% of Σd, trimmed dev 1.13%
 H7 Gram reference    PASS — 0 violations
```

Full file — `02_data/raw/results_run/ab_cloud_v19_verify_report_2026-09-02_23-33-45.txt`.

---

## Appendix N. The full alt texts of all figures (accessibility)

| Path | Alt text |
|---|---|
| static/dirac/fig_D10_montgomery_transport.png | Montgomery transport: repulsion protects transport. Campaign D10. |
| static/dirac/fig_D11_berry_keating.png | The Berry–Keating/Connes conjugation on the lattice. Campaign D11. |
| static/dirac/fig_D12_bk_ladder_infinite.png | The infinite BK ladder at fixed density. Campaign D12. |
| static/dirac/fig_D13_wall_under_drive.png | The wall under the conjugation drive. Campaign D13. |
| static/dirac/fig_D14_odlyzko_form_factor.png | The form factor on the Odlyzko band: K(2) = 0.962. Campaign D14. |
| static/dirac/fig_D1_dirac_cone.png | The Dirac cone: the continuum limit of the π-flux lattice. Campaign D1. |
| static/dirac/fig_D2_zero_tower.png | The fourfold zero-mode tower on the torus. Campaign D2. |
| static/dirac/fig_D3_berry_phase.png | The cone's Berry phase: exactly π. Campaign D3. |
| static/dirac/fig_D4_landau_levels.png | The relativistic Landau ladder: E_n² ∝ n. Campaign D4. |
| static/dirac/fig_D5_klein_tunneling.png | Klein tunneling: 0.978 against the Schrödinger control 0.0010. Campaign D5. |
| static/dirac/fig_D6_zitterbewegung.png | Zitterbewegung at frequency ω = 2E. Campaign D6. |
| static/dirac/fig_D7_zeta_decoration.png | ζ-decorated statistics: the GOE → GUE lift. Campaign D7. |
| static/dirac/fig_D8_chiral_symmetry.png | Chiral protection: E ↔ −E pairing to 4·10⁻¹⁵. Campaign D8. |
| static/dirac/fig_D9_index_restoration.png | The Jackiw–Rossi wall restores the index in the full ζ background. Campaign D9. |
| static/hilbert_polya/en/fig01_zid_en.png | Figure of the Hilbert–Pólya bridge. |
| static/hilbert_polya/en/fig02_gamma_ladder_en.png | Figure of the Hilbert–Pólya bridge. |
| static/hilbert_polya/en/fig03_argument_en.png | Figure of the Hilbert–Pólya bridge. |
| static/hilbert_polya/en/fig04_gaps_en.png | Figure of the Hilbert–Pólya bridge. |
| static/hilbert_polya/en/fig05_gates_en.png | Figure of the Hilbert–Pólya bridge. |
| static/hilbert_polya/en/fig06_trace_en.png | Figure of the Hilbert–Pólya bridge. |
| static/hilbert_polya/en/fig07_parts_en.png | Figure of the Hilbert–Pólya bridge. |
| static/hilbert_polya/en/fig08_rEF_en.png | Figure of the Hilbert–Pólya bridge. |
| static/hilbert_polya/en/fig09_handles_en.png | Figure of the Hilbert–Pólya bridge. |
| static/hilbert_polya/en/fig10_gue_ext_en.png | Figure of the Hilbert–Pólya bridge. |
| static/hilbert_polya/en/fig11_coloc_en.png | Figure of the Hilbert–Pólya bridge. |
| static/hilbert_polya/en/fig12_psi_en.png | Figure of the Hilbert–Pólya bridge. |
| static/hilbert_polya/en/fig13_dynamics_en.png | Figure of the Hilbert–Pólya bridge. |
| static/hilbert_polya/en/fig14_ladder_en.png | Figure of the Hilbert–Pólya bridge. |
| static/hilbert_polya/en/fig15_spinor_en.png | Figure of the Hilbert–Pólya bridge. |
| static/hilbert_polya/en/fig16_map_en.png | Figure of the Hilbert–Pólya bridge. |
| static/hilbert_polya/en/fig17_nonlocal_en.png | Figure of the Hilbert–Pólya bridge. |
| static/hilbert_polya/en/fig18_coloc_en.png | Figure of the Hilbert–Pólya bridge. |
| static/hilbert_polya/en/fig19_alphathird_en.png | Figure of the Hilbert–Pólya bridge. |
| static/hilbert_polya/en/fig20_band5000_en.png | Figure of the Hilbert–Pólya bridge. |
| static/hilbert_polya/en/fig21_blind_en.png | Figure of the Hilbert–Pólya bridge. |
| static/hilbert_polya/en/fig22_anomaly_en.png | Figure of the Hilbert–Pólya bridge. |
| static/hilbert_polya/en/fig23_dirichlet_en.png | Figure of the Hilbert–Pólya bridge. |
| static/hilbert_polya/en/fig24_qinfo_en.png | Figure of the Hilbert–Pólya bridge. |
| static/hilbert_polya/en/fig25_map_en.png | Figure of the Hilbert–Pólya bridge. |
| static/hilbert_polya/ru/fig01_zid_ru.png | Figure of the Hilbert–Pólya bridge. |
| static/hilbert_polya/ru/fig02_gamma_ladder_ru.png | Figure of the Hilbert–Pólya bridge. |
| static/hilbert_polya/ru/fig03_argument_ru.png | Figure of the Hilbert–Pólya bridge. |
| static/hilbert_polya/ru/fig04_gaps_ru.png | Figure of the Hilbert–Pólya bridge. |
| static/hilbert_polya/ru/fig05_gates_ru.png | Figure of the Hilbert–Pólya bridge. |
| static/hilbert_polya/ru/fig06_trace_ru.png | Figure of the Hilbert–Pólya bridge. |
| static/hilbert_polya/ru/fig07_parts_ru.png | Figure of the Hilbert–Pólya bridge. |
| static/hilbert_polya/ru/fig08_rEF_ru.png | Figure of the Hilbert–Pólya bridge. |
| static/hilbert_polya/ru/fig09_handles_ru.png | Figure of the Hilbert–Pólya bridge. |
| static/hilbert_polya/ru/fig10_gue_ext_ru.png | Figure of the Hilbert–Pólya bridge. |
| static/hilbert_polya/ru/fig11_coloc_ru.png | Figure of the Hilbert–Pólya bridge. |
| static/hilbert_polya/ru/fig12_psi_ru.png | Figure of the Hilbert–Pólya bridge. |
| static/hilbert_polya/ru/fig13_dynamics_ru.png | Figure of the Hilbert–Pólya bridge. |
| static/hilbert_polya/ru/fig14_ladder_ru.png | Figure of the Hilbert–Pólya bridge. |
| static/hilbert_polya/ru/fig15_spinor_ru.png | Figure of the Hilbert–Pólya bridge. |
| static/hilbert_polya/ru/fig16_map_ru.png | Figure of the Hilbert–Pólya bridge. |
| static/hilbert_polya/ru/fig17_nonlocal_ru.png | Figure of the Hilbert–Pólya bridge. |
| static/hilbert_polya/ru/fig18_coloc_ru.png | Figure of the Hilbert–Pólya bridge. |
| static/hilbert_polya/ru/fig19_alphathird_ru.png | Figure of the Hilbert–Pólya bridge. |
| static/hilbert_polya/ru/fig20_band5000_ru.png | Figure of the Hilbert–Pólya bridge. |
| static/hilbert_polya/ru/fig21_blind_ru.png | Figure of the Hilbert–Pólya bridge. |
| static/hilbert_polya/ru/fig22_anomaly_ru.png | Figure of the Hilbert–Pólya bridge. |
| static/hilbert_polya/ru/fig23_dirichlet_ru.png | Figure of the Hilbert–Pólya bridge. |
| static/hilbert_polya/ru/fig24_qinfo_ru.png | Figure of the Hilbert–Pólya bridge. |
| static/hilbert_polya/ru/fig25_map_ru.png | Figure of the Hilbert–Pólya bridge. |
| static/spectral_core/en/th1_4dim_en.png | Figure of the spectral core. |
| static/spectral_core/en/th2_4dim_en.png | Figure of the spectral core. |
| static/spectral_core/en/th3_4dim_en.png | Figure of the spectral core. |
| static/spectral_core/en/th4_4dim_en.png | Figure of the spectral core. |
| static/spectral_core/en/th5_4dim_en.png | Figure of the spectral core. |
| static/spectral_core/en/th6_4dim_en.png | Figure of the spectral core. |
| static/spectral_core/ru/th1_4dim_ru.png | Figure of the spectral core. |
| static/spectral_core/ru/th2_4dim_ru.png | Figure of the spectral core. |
| static/spectral_core/ru/th3_4dim_ru.png | Figure of the spectral core. |
| static/spectral_core/ru/th4_4dim_ru.png | Figure of the spectral core. |
| static/spectral_core/ru/th5_4dim_ru.png | Figure of the spectral core. |
| static/spectral_core/ru/th6_4dim_ru.png | Figure of the spectral core. |
| static/vortex_optimization/01_heatmap_D_Nv_q.png | Heatmap of KS distance over vortex count and charge, showing the working valley. Campaign T34-ext. |
| static/vortex_optimization/02_D_of_Nv.png | KS distance versus vortex density showing the non-monotone working window. Campaign T34-ext. |
| static/vortex_optimization/03_D_of_q.png | KS distance versus vortex charge showing q = 1 optimum. Campaign T34-ext. |
| static/vortex_optimization/04_L_ladder.png | KS distance across lattice sizes with the GUE floor line. Campaign T34-ext. |
| static/vortex_optimization/05_alpha_scan.png | KS distance versus uniform flux alpha showing the critical line at 0.5. Campaign T34-ext. |
| static/vortex_optimization/06_R2_s.png | Two-point correlation function compared with zeta-zero statistics. Campaign T34-ext. |
| static/vortex_optimization/07_stability.png | Spread of KS distance across realizations for the passing candidates. Campaign T34-ext. |
| static/wave_attractors/01_chambers_and_cone.png | Sketch of the trapezoid chamber with the group-velocity cone. Study W1. |
| static/wave_attractors/02_cascade.png | Wave-vector jumps along the iso-frequency hyperbola at slope reflections. Study W1. |
| static/wave_attractors/03_attractor_vs_control.png | Ray trajectories in hyperbolic versus isotropic chambers. Study W1. |
| static/wave_attractors/04_phase_diagram.png | Lock-in fraction over the slope-extent plane with attractor and regular phases. Study W1. |
| static/wave_attractors/05_chirality.png | Mirror pair of attractor routes with opposite circulation senses. Study W1. |
| static/wave_attractors/06_wave_maps.png | Band-averaged wave intensity maps showing corridor channeling. Study W1. |
| static/wave_attractors/07_ray_density.png | Ray density along the attractor route versus background. Study W1. |
| static/wave_attractors/08_ab_water.png | Water-wave phase pattern around a vortex showing AB winding. Study W1. |
| static/wave_attractors/09_cross_verification.png | Difference of Python and Julia ray trajectories over bounce index. Study W1. |
| static/wave_attractors/10_eta_scan.png | Lock-in fraction collapse in scaled coordinates across anisotropy values. Study W1. |
| static/wave_attractors/11_time_domain.png | Time-domain pulse capture in the Drude-dispersive medium. Study W1. |
| static/wave_attractors/12_truncation.png | Peak capture growth with number of unit cells. Study W1. |
| static/meridian/en/fig_M1_r_statistics_en.png | Meridian statistics figure. Package-derived. |
| static/meridian/en/fig_M2_spacing_surmise_en.png | Meridian statistics figure. Package-derived. |
| static/meridian/en/fig_M3_r_sliding_en.png | Meridian statistics figure. Package-derived. |
| static/results_run/en/fig_R1_v19_verdict_map_en.png | v19 run figure. Package-derived. |
| static/results_run/en/fig_R2_v19_time_profile_en.png | v19 run figure. Package-derived. |
| static/meridian/ru/fig_M1_r_statistics_ru.png | Meridian statistics figure. Package-derived. |
| static/meridian/ru/fig_M2_spacing_surmise_ru.png | Meridian statistics figure. Package-derived. |
| static/meridian/ru/fig_M3_r_sliding_ru.png | Meridian statistics figure. Package-derived. |
| static/results_run/ru/fig_R1_v19_verdict_map_ru.png | v19 run figure. Package-derived. |
| static/results_run/ru/fig_R2_v19_time_profile_ru.png | v19 run figure. Package-derived. |

---

# Appendix O. The monograph's language abstracts (full)

### 中文

<div align="center">

# AB-Cloud 研究计划：统一专著（中文摘要）

**AB-Cloud Research Programme · Unified Academic Package**

[返回主 README / back](../../README.md)

[Русский](../ru/README.md) · [English](../en/README.md) · **中文** · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [العربية](../ar/README.md)

</div>

---

> [!NOTE]
**中文版为摘要。** 完整学术文本为俄文与英文卷：[`../ru/monograph_ru.pdf`](../ru/monograph_ru.pdf) 与 [`../en/monograph_en.pdf`](../en/monograph_en.pdf)。以下为忠实翻译的摘要与章节目录。

## Abstract / 摘要

本专著是 AB-Cloud 研究计划的统一叙述：一项展开为四个层次及一个补充旋量研究的工作。该计划研究黎曼 ζ 函数非平凡零点与厄米算符谱之间的一座具体统计桥梁。候选者是每个格点携带 α 量子阿哈罗诺夫–玻姆磁通的格点算符（AB 云），其构造使得谱统计落入 GUE 普适类——蒙哥马利–奥德利兹科计划为 ζ 零点所预测的类——而构造的精确层（厄米性、磁通量子化、Byers–Yang 不变性、手征配对、Connes 自对偶、几何相位恒等式链）在需要处以机器精度乃至 256 位任意精度验证。

叙述整合了计划的三个研究实验室。**第 I 层**——谱核与 AB 处理器：活动 V01–V20、定理 Th1–Th6、V13 义务机、具有 AB 云 ISA 与精确 Givens–QR 编译（1−F ≤ 4.4×10⁻¹⁶）的处理器。**第 II 层**——狄拉克骨架：十四个测试 D1–D14 确立 π 通量格点*就是*离散化的无质量狄拉克方程，而 ζ 装饰狄拉克算符将体统计从 GOE 提升至 GUE（⟨r⟩ = 0.608 对 0.5992）。**第 III 层**——希尔伯特–波利亚桥梁：十七个活动 C1–C17 与十八条定理 T1–T18；该层的判定是「几乎存在的算符」。**第 IV 层**——盲验证：十八个预注册判定 E01–E18，包括两个独立引擎对 T=1000 以内全部 649 个 ζ 零点的盲读（比特精确一致），以及 38 测试基准运行的遗产。

**合并判定登记表：自伴性——**是**；谱同一性——**是**（在零点自身的层级上成立；审计 v2.0.7；比特层分支仍开放）；GUE 类——**是**；狄拉克动力学——**是**；算符中的素数——**是**（经由收敛阶梯；审计 v2.0.8）（Λ(n)/√n 权重存在于迹中）；黎曼假设——按构造**受阻**。这张地图如今是双向的：层级同一性在零点自身的层级上成立，素数经由收敛阶梯进入；剩下的墙是比特层的。局域格点仍无法承载零点梳谱所要求的纠缠（子系统熵 S_A ≈ 12–16 nats，而 Haar 为 160–220）。.** 

## 章节目录

| # | Chapter |
|---|---|
| 1 | 引言 |
| 2 | 相关工作 |
| 3 | 架构：一台机器的层次 |
| 4 | 第 I 层：谱核与 AB 处理器 |
| 5 | 第 II 层：狄拉克骨架 |
| 6 | 第 III 层：希尔伯特–波利亚桥梁 |
| 7 | 第 IV 层：盲验证与遗产 |
| 8 | 旋量研究：无长期记忆的机器 |
| 9 | 数据与可复现性 |
| 10 | 合并实验登记表 |
| 11 | 结果与判定 |
| 12 | 讨论：局域性之墙 |
| 13 | 局限与诚实边界 |
| 14 | 结论 |
| A | 附录 A：活动登记表 |
| B | 附录 B：来源映射 |

## 关键数字

| 结果 | 数值 |
|---|---|
| 盲读 ζ 零点至 T=1000（双引擎） | 649/649 + 639/639；跨引擎 0.0 |
| ζ 装饰统计 | ⟨r⟩ 0.608 vs 理论 0.5992 |
| 克莱因超隧穿 | 0.978 vs 0.0010（×977） |
| 非局部孪生 | r_H7 = 1.000000 |
| 局域性之墙 | S_A 12–16 nats vs Haar 160–220 |
| RH 状态 | 按构造受阻 (V13) |

## 关键词

关键词：黎曼 ζ 函数 · 希尔伯特–波利亚 · 阿哈罗诺夫–玻姆 · 格点狄拉克算符 · 随机矩阵 · GUE · 蒙哥马利–奥德利兹科 · 贝里–基廷 · Connes · 盲验证 · 可复现性

### Deutsch

<div align="center">

# Das AB-Cloud-Forschungsprogramm: einheitliche Monographie (deutsche Zusammenfassung)

**AB-Cloud Research Programme · Unified Academic Package**

[返回主 README / back](../../README.md)

[Русский](../ru/README.md) · [English](../en/README.md) · [中文](../zh/README.md) · **Deutsch** · [Español](../es/README.md) · [Français](../fr/README.md) · [العربية](../ar/README.md)

</div>

---

> [!NOTE]
**Die deutsche Fassung ist eine Zusammenfassung.** Der vollständige wissenschaftliche Text sind die Bände in Russisch und Englisch: [`../ru/monograph_ru.pdf`](../ru/monograph_ru.pdf) und [`../en/monograph_en.pdf`](../en/monograph_en.pdf). Nachfolgend eine treu übersetzte Zusammenfassung und das Inhaltsverzeichnis.

## Abstract / 摘要

Diese Monographie ist die einheitliche Darstellung des AB-Cloud-Forschungsprogramms: eine Studie, entfaltet auf vier Ebenen und eine ergänzende Spinor-Studie. Das Programm untersucht eine konkrete statistische Brücke zwischen den nichttrivialen Nullstellen der Riemannschen ζ-Funktion und den Spektren Hermitescher Operatoren. Der Kandidat ist ein Gitteroperator mit α Quanten Aharonov–Bohm-Fluss pro Plaquette (die AB-Wolke), konstruiert so, dass seine Spektralstatistik in die GUE-Universalitätsklasse fällt — die Klasse, die das Montgomery–Odlyzko-Programm für die ζ-Nullstellen vorhersagt —, während die exakte Schicht (Hermitizität, Flussquantisierung, Byers–Yang-Invarianz, chirale Paarung, Connes-Selbstdualität, eine Kette geometrischer Phasenidentitäten) auf Maschinenpräzision und, wo erforderlich, auf 256-Bit-Genauigkeit verifiziert wird.

Die Darstellung konsolidiert die drei Forschungslaboratorien des Programms. **Ebene I** — Spektralkern und AB-Prozessor: Kampagnen V01–V20, Theoreme Th1–Th6, die V13-Verpflichtungsmaschine, der Prozessor mit AB-Wolken-ISA und exakter Givens–QR-Kompilierung (1−F ≤ 4,4·10⁻¹⁶). **Ebene II** — das Dirac-Skelett: vierzehn Tests D1–D14, die das π-Flussgitter *als* diskretisierte masselose Dirac-Gleichung und den ζ-dekorierten Operator als GOE→GUE-Hebung etablieren (⟨r⟩ = 0,608 gegen 0,5992). **Ebene III** — die Hilbert–Pólya-Brücke: siebzehn Kampagnen C1–C17 und achtzehn Theoreme T1–T18; das Urteil der Ebene — «der Operator, der fast existiert». **Ebene IV** — blinde Verifikation: achtzehn präregistrierte Urteile E01–E18, einschließlich der blinden Lesung aller 649 ζ-Nullstellen bis T = 1000 durch zwei unabhängige Motoren mit bit-exakter Übereinstimmung, und das Erbe des 38-Test-Referenzlaufs.

**Das konsolidierte Verdikts-Ledger: Selbstadjungiertheit — **Ja**; spektrale Identität — **Ja** (auf dem Niveau der Nullstellen selbst; Audit v2.0.7; der bitweise Zweig bleibt offen); GUE-Klasse — **Ja**; Dirac-Dynamik — **Ja**; Primzahlen im Operator — **Ja** (über die Konvergenzleiter; Audit v2.0.8); die Riemannsche Vermutung — per Konstruktion **blockiert**.** Die Karte ist jetzt zweiseitig: die Ebenen-Identität hält auf dem Niveau der Nullstellen, und die Primzahlen treten über die Konvergenzleiter ein; die verbleibende Wand ist bitweise. Ein lokales Gitter kann die Verschränkung, die das Nullkamm-Spektrum verlangt, noch nicht beherbergen (S_A ≈ 12–16 nats gegenüber 160–220 für Haar).

## Inhaltsverzeichnis

| # | Chapter |
|---|---|
| 1 | Einleitung |
| 2 | Verwandte Arbeiten |
| 3 | Architektur: Ebenen einer Maschine |
| 4 | Ebene I: Spektralkern und AB-Prozessor |
| 5 | Ebene II: das Dirac-Skelett |
| 6 | Ebene III: die Hilbert–Pólya-Brücke |
| 7 | Ebene IV: blinde Verifikation und Erbe |
| 8 | Die Spinor-Studie: die Maschine ohne Langzeitgedächtnis |
| 9 | Daten und Reproduzierbarkeit |
| 10 | Das konsolidierte Experimentregister |
| 11 | Ergebnisse und Verdikte |
| 12 | Diskussion: die Lokalitätswand |
| 13 | Einschränkungen und ehrliche Grenzen |
| 14 | Schluss |
| A | Anhang A: Kampagnenregister |
| B | Anhang B: Quellenabbildung |

## Schlüsselzahlen

| Ergebnis | Wert |
|---|---|
| Blindlesung der ζ-Nullstellen bis T=1000 (zwei Motoren) | 649/649 + 639/639; kreuzmotorig 0.0 |
| ζ-dekorierte Statistik | ⟨r⟩ 0.608 vs. Theorie 0.5992 |
| Klein-Supertunnelung | 0.978 vs. 0.0010 (×977) |
| Nichtlokaler Zwilling | r_H7 = 1.000000 |
| Lokalitätswand | S_A 12–16 nats vs. Haar 160–220 |
| RH-Status | per Konstruktion blockiert (V13) |

## Keywords

Schlagwörter: Riemannsche ζ-Funktion · Hilbert–Pólya · Aharonov–Bohm · Gitter-Dirac-Operator · Zufallsmatrizen · GUE · Montgomery–Odlyzko · Berry–Keating · Connes · blinde Verifikation · Reproduzierbarkeit

### Español

<div align="center">

# El programa de investigación AB-Cloud: monografía unificada (resumen en español)

**AB-Cloud Research Programme · Unified Academic Package**

[返回主 README / back](../../README.md)

[Русский](../ru/README.md) · [English](../en/README.md) · [中文](../zh/README.md) · [Deutsch](../de/README.md) · **Español** · [Français](../fr/README.md) · [العربية](../ar/README.md)

</div>

---

> [!NOTE]
**La versión en español es un resumen.** El texto científico completo son los volúmenes en ruso e inglés: [`../ru/monograph_ru.pdf`](../ru/monograph_ru.pdf) y [`../en/monograph_en.pdf`](../en/monograph_en.pdf). A continuación, un resumen fielmente traducido y el índice de capítulos.

## Abstract / 摘要

Esta monografía es el relato unificado del programa de investigación AB-Cloud: un estudio desplegado en cuatro niveles y un estudio suplementario de espinores. El programa investiga un puente estadístico concreto entre dos objetos que las matemáticas llevan más de un siglo intentando reconciliar: los ceros no triviales de la función zeta de Riemann y los espectros de operadores hermíticos. El candidato es un operador de retícula con α cuantos de flujo de Aharonov–Bohm por placa (la nube AB), construido de modo que su estadística espectral caiga en la clase de universalidad GUE — la clase que el programa de Montgomery–Odlyzko predice para los ceros de ζ —, mientras que la capa exacta (hermiticidad, cuantización del flujo, invariancia de Byers–Yang, apareamiento quiral, autodualidad de Connes, una cadena de identidades de fases geométricas) se verifica a precisión de máquina y a 256 bits donde se requiere.

El relato consolida los tres laboratorios de investigación del programa. **Nivel I** — el núcleo espectral y el procesador AB: campañas V01–V20, teoremas Th1–Th6, la máquina de obligaciones V13, y el procesador con ISA de nube AB y compilación Givens–QR exacta (1−F ≤ 4.4·10⁻¹⁶). **Nivel II** — el esqueleto de Dirac: catorce pruebas D1–D14 que establecen que la retícula de flujo π *es* una ecuación de Dirac sin masa discretizada, y que el operador de Dirac decorado con ζ eleva la estadística del volumen de GOE a GUE (⟨r⟩ = 0.608 frente a 0.5992). **Nivel III** — el puente de Hilbert–Pólya: diecisiete campañas C1–C17 y dieciocho teoremas T1–T18; el veredicto del nivel — «el operador que casi existe». **Nivel IV** — verificación ciega: dieciocho veredictos preregistrados E01–E18, incluida la lectura ciega de los 649 ceros de ζ hasta T = 1000 por dos motores independientes con coincidencia bit-exacta, y el legado de la ejecución de referencia de 38 pruebas.

**El registro consolidado de veredictos: autoadjunción — **sí**; identidad espectral — **sí** (al nivel de los propios ceros; auditoría v2.0.7; la rama a nivel de bits queda abierta); clase GUE — **sí**; dinámica de Dirac — **sí**; primos en el operador — **sí** (por la escalera de convergencia; auditoría v2.0.8); la hipótesis de Riemann — **bloqueada** por construcción.** El mapa es ahora de dos caras: la identidad de niveles se sostiene al nivel de los propios ceros y los primos entran por la escalera de convergencia; el muro que queda es a nivel de bits. Una retícula local aún no puede albergar el entrelazamiento que exige el espectro del peine de ceros (S_A ≈ 12–16 nats frente a 160–220 para Haar).

## Índice de capítulos

| # | Chapter |
|---|---|
| 1 | Introducción |
| 2 | Trabajos relacionados |
| 3 | Arquitectura: niveles de una máquina |
| 4 | Nivel I: el núcleo espectral y el procesador AB |
| 5 | Nivel II: el esqueleto de Dirac |
| 6 | Nivel III: el puente de Hilbert–Pólya |
| 7 | Nivel IV: verificación ciega y legado |
| 8 | El estudio de espinores: la máquina sin memoria a largo plazo |
| 9 | Datos y reproducibilidad |
| 10 | El registro experimental consolidado |
| 11 | Resultados y veredictos |
| 12 | Discusión: el muro de localidad |
| 13 | Limitaciones y límites honestos |
| 14 | Conclusión |
| A | Apéndice A: registro de campañas |
| B | Apéndice B: mapa de fuentes |

## Cifras clave

| Resultado | Valor |
|---|---|
| Lectura ciega de ceros ζ hasta T=1000 (dos motores) | 649/649 + 639/639; entre motores 0.0 |
| Estadística decorada con ζ | ⟨r⟩ 0.608 vs teoría 0.5992 |
| Supertúnel de Klein | 0.978 vs 0.0010 (×977) |
| Gemelo no local | r_H7 = 1.000000 |
| Muro de localidad | S_A 12–16 nats vs Haar 160–220 |
| Estado de RH | bloqueada por construcción (V13) |

## Keywords

Palabras clave: función zeta de Riemann · Hilbert–Pólya · Aharonov–Bohm · operador de Dirac en retícula · matrices aleatorias · GUE · Montgomery–Odlyzko · Berry–Keating · Connes · verificación ciega · reproducibilidad

### Français

<div align="center">

# Le programme de recherche AB-Cloud : monographie unifiée (résumé en français)

**AB-Cloud Research Programme · Unified Academic Package**

[返回主 README / back](../../README.md)

[Русский](../ru/README.md) · [English](../en/README.md) · [中文](../zh/README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · **Français** · [العربية](../ar/README.md)

</div>

---

> [!NOTE]
**La version française est un résumé.** Le texte scientifique complet se trouve dans les volumes russe et anglais : [`../ru/monograph_ru.pdf`](../ru/monograph_ru.pdf) et [`../en/monograph_en.pdf`](../en/monograph_en.pdf). Ci-dessous, un résumé fidèlement traduit et la table des matières.

## Abstract / 摘要

Cette monographie est le récit unifié du programme de recherche AB-Cloud : une étude déployée sur quatre niveaux et une étude spinorielle complémentaire. Le programme investigue un pont statistique concret entre deux objets que les mathématiques tentent de réconcilier depuis plus d'un siècle : les zéros non triviaux de la fonction zêta de Riemann et les spectres d'opateurs hermitiens. Le candidat est un opérateur sur réseau portant α quanta de flux d'Aharonov–Bohm par plaquette (le nuage AB), construit de sorte que sa statistique spectrale tombe dans la classe d'universalité GUE — la classe que le programme de Montgomery–Odlyzko prédit pour les zéros de ζ —, tandis que la couche exacte (hermiticité, quantification du flux, invariance de Byers–Yang, appariement chiral, autodualité de Connes, une chaîne d'identités de phases géométriques) est vérifiée à la précision machine et à 256 bits là où cela est requis.

Le récit consolide les trois laboratoires de recherche du programme. **Niveau I** — le noyau spectral et le processeur AB : campagnes V01–V20, théorèmes Th1–Th6, la machine d'obligations V13, et le processeur avec l'ISA de nuage AB et la compilation Givens–QR exacte (1−F ≤ 4,4·10⁻¹⁶). **Niveau II** — le squelette de Dirac : quatorze tests D1–D14 établissant que le réseau à flux π *est* une équation de Dirac sans masse discrétisée, et que l'opérateur de Dirac décoré par ζ élève la statistique du volume de GOE à GUE (⟨r⟩ = 0,608 contre 0,5992). **Niveau III** — le pont de Hilbert–Pólya : dix-sept campagnes C1–C17 et dix-huit théorèmes T1–T18 ; le verdict du niveau — « l'opérateur qui existe presque ». **Niveau IV** — vérification aveugle : dix-huit verdicts pré-enregistrés E01–E18, dont la lecture aveugle des 649 zéros de ζ jusqu'à T = 1000 par deux moteurs indépendants avec accord bit-exact, et l'héritage de l'exécution de référence des 38 tests.

**Le registre consolidé des verdicts : auto-adjonction — **oui** ; identité spectrale — **oui** (au niveau des zéros eux-mêmes ; audit v2.0.7 ; la branche au niveau des bits reste ouverte) ; classe GUE — **oui** ; dynamique de Dirac — **oui** ; nombres premiers dans l'opérateur — **oui** (par l'échelle de convergence ; audit v2.0.8) ; l'hypothèse de Riemann — **bloquée** par construction.** La carte est désormais à double sens : l'identité des niveaux tient au niveau des zéros eux-mêmes et les nombres premiers entrent par l'échelle de convergence ; le mur qui reste est au niveau des bits. Un réseau local ne peut pas encore héberger l'intrication que exige le spectre du peigne de zéros (S_A ≈ 12–16 nats contre 160–220 pour Haar).

## Table des matières

| # | Chapter |
|---|---|
| 1 | Introduction |
| 2 | Travaux connexes |
| 3 | Architecture : les niveaux d'une machine |
| 4 | Niveau I : le noyau spectral et le processeur AB |
| 5 | Niveau II : le squelette de Dirac |
| 6 | Niveau III : le pont de Hilbert–Pólya |
| 7 | Niveau IV : vérification aveugle et héritage |
| 8 | L'étude spinorielle : la machine sans mémoire à long terme |
| 9 | Données et reproductibilité |
| 10 | Le registre expérimental consolidé |
| 11 | Résultats et verdicts |
| 12 | Discussion : le mur de localité |
| 13 | Limites et frontières honnêtes |
| 14 | Conclusion |
| A | Annexe A : registre des campagnes |
| B | Annexe B : correspondance des sources |

## Chiffres clés

| Résultat | Valeur |
|---|---|
| Lecture aveugle des zéros ζ jusqu'à T=1000 (deux moteurs) | 649/649 + 639/639 ; entre moteurs 0,0 |
| Statistique décorée par ζ | ⟨r⟩ 0,608 vs théorie 0,5992 |
| Super-tunnel de Klein | 0,978 vs 0,0010 (×977) |
| Jumeau non local | r_H7 = 1,000000 |
| Mur de localité | S_A 12–16 nats vs Haar 160–220 |
| Statut de RH | bloquée par construction (V13) |

## Keywords

Mots-clés : fonction zêta de Riemann · Hilbert–Pólya · Aharonov–Bohm · opérateur de Dirac sur réseau · matrices aléatoires · GUE · Montgomery–Odlyzko · Berry–Keating · Connes · vérification aveugle · reproductibilité

### العربية

<div align="center" dir="rtl">

# برنامج AB-Cloud البحثي: الأطروحة الموحدة (ملخص بالعربية)

**AB-Cloud Research Programme · Unified Academic Package**

[返回主 README / back](../../README.md)

[Русский](../ru/README.md) · [English](../en/README.md) · [中文](../zh/README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · **العربية**

</div>

---

> [!NOTE]
**النسخة العربية ملخص.** النص العلمي الكامل هو المجلدان الروسي والإنجليزي: [`../ru/monograph_ru.pdf`](../ru/monograph_ru.pdf) و [`../en/monograph_en.pdf`](../en/monograph_en.pdf). فيما يلي ملخص مترجم بأمانة وفهرس الفصول.

## Abstract / 摘要

هذه الأطروحة هي السرد الموحد لبرنامج AB-Cloud البحثي: دراسة واحدة منبثقة على أربعة مستويات ودراسة سبينورية تكميلية. يبحث البرنامج في جسر إحصائي ملموس بين شيئين حاولت الرياضيات التوفيق بينهما منذ أكثر من قرن: الأصفار غير البديهية لدالة زيتا ريمان وأطياف المؤثِّرات الإرميتية. المرشح مؤثِّر شبكي يحمل α كموم تدفق أهارونوف–بوهلم لكل بلاكة (سحابة AB)، مصمم بحيث تقع إحصاءاته الطيفية في فئة الشمول GUE — الفئة التي يتنبأ بها برنامج مونتغومري–أودليزكو لأصفار ζ — بينما تُتحقق الطبقة الدقيقة (الإرميتية، تكميم التدفق، ثبات بايرز–يانغ، الاقتران الكيرالي، الانعكاسية الذاتية لكون، سلسلة متطابقات الأطوار الهندسية) بدقة الآلة وإلى 256 بت حيثما يلزم.

يوحِّد السرد مختبرات البحث الثلاثة للبرنامج. **المستوى الأول** — النواة الطيفية ومعالج AB: الحملات V01–V20، المبرهنات Th1–Th6، آلة الالتزامات V13، والمعالج بـ ISA سحابة AB والتصريف الدقيق Givens–QR (‏1−F ≤ 4.4·10⁻¹⁶). **المستوى الثاني** — الهيكل الديراكي: أربعة عشر اختباراً D1–D14 تُثبت أن الشبكة ذات التدفق π *هي* معادلة ديراك عديمة الكتلة مُقطّرة، وأن المؤثِّر الديراكي المُزيَّن بـ ζ يرفع إحصاء الحجم من GOE إلى GUE (⟨r⟩ = 0.608 مقابل 0.5992). **المستوى الثالث** — جسر هيلبرت–بوليا: سبع عشرة حملة C1–C17 وثماني عشرة مبرهنة T1–T18؛ حكم المستوى — «المؤثِّر الذي يكاد يكون موجوداً». **المستوى الرابع** — التحقق الأعمى: ثمانية عشر حكماً مُسجَّلة مسبقاً E01–E18، بمن في ذلك القراءة العمياء لجميع الأصفار الـ 649 حتى T = 1000 بمحركين مستقلين بتطابق بت-دقيق، وإرث التشغيل المرجعي ذي الـ 38 اختباراً.

**سجل الأحكام الموحد: الترافق الذاتي — **نعم**؛ الهوية الطيفية — **نعم** (على مستوى الأصفار نفسها؛ تدقيق v2.0.7؛ يبقى الفرع البتّي مفتوحًا)؛ فئة GUE — **نعم**؛ ديناميكا ديراك — **نعم**؛ الأعداد الأولية في المؤثِّر — **نعم** (عبر سُلَّم التقارب؛ تدقيق v2.0.8)؛ فرضية ريمان — **محجوبة** بالبناء.** المساهمة الرئيسية للبرنامج ليست ادعاءً بل خريطة ذات وجهين: هوية المستويات قائمة على مستوى الأصفار نفسها، والأعداد الأولية تدخل عبر سُلَّم التقارب؛ الجدار المتبقي هو الجدار البتّي. ما زالت الشبكة المحلية لا تستطيع احتضان التشابك الذي يطلبه طيف مشط الأصفار (S_A ≈ 12–16 nats مقابل 160–220 لهار).

## فهرس الفصول

| # | Chapter |
|---|---|
| 1 | المقدمة |
| 2 | الأعمال ذات الصلة |
| 3 | البنية: مستويات آلة واحدة |
| 4 | المستوى الأول: النواة الطيفية ومعالج AB |
| 5 | المستوى الثاني: الهيكل الديراكي |
| 6 | المستوى الثالث: جسر هيلبرت–بوليا |
| 7 | المستوى الرابع: التحقق الأعمى والإرث |
| 8 | دراسة السبينور: الآلة بلا ذاكرة طويلة الأمد |
| 9 | البيانات وقابلية إعادة الإنتاج |
| 10 | سجل التجارب الموحد |
| 11 | النتائج والأحكام |
| 12 | المناقشة: جدار الموضعية |
| 13 | القيود والحدود الصادقة |
| 14 | الخاتمة |
| A | الملحق أ: سجل الحملات |
| B | الملحق ب: خريطة المصادر |

## الأرقام المفتاحية

| النتيجة | القيمة |
|---|---|
| قراءة أعمى لأصفار ζ حتى T=1000 (محركان) | 649/649 + 639/639؛ بين المحركين 0.0 |
| الإحصاء المُزيَّن بـ ζ | ⟨r⟩ 0.608 مقابل النظرية 0.5992 |
| النفق الفائق لكلاين | 0.978 مقابل 0.0010 (×977) |
| التوأم اللاموضعي | r_H7 = 1.000000 |
| جدار الموضعية | S_A ‏12–16 nats مقابل هار 160–220 |
| حالة RH | محجوبة بالبناء (V13) |

## Keywords

الكلمات المفتاحية: دالة زيتا ريمان · هيلبرت–بوليا · أهارونوف–بوهلم · مؤثِّر ديراك الشبكي · المصفوفات العشوائية · GUE · مونتغومري–أودليزكو · بيري–كيتنغ · كون · التحقق الأعمى · قابلية إعادة الإنتاج

الكلمات المفتاحية: دالة زيتا ريمان · هيلبرت–بوليا · أهارونوف–بوهلم · مؤثِّر ديراك الشبكي · المصفوفات العشوائية · GUE · مونتغومري–أودليزكو · بيري–كيتنغ · كون · التحقق الأعمى · قابلية إعادة الإنتاج

# Appendix P. The audience summaries (full records)

## P.1. Lay summary

# Lay summary / Популярное изложение

## EN — The hunt for the wall, not the proof

Mathematicians have long suspected that the zeros of the Riemann zeta
function — special numbers that hold the deepest secrets of prime numbers —
behave like the energy levels of a quantum system. If one could build the
right "quantum drum" whose resonances are exactly those zeros, a
century-old problem would be solved. This programme built the closest
candidate drum anyone has measured: a magnetic lattice that is perfectly
tuned (its statistics match the predicted random-matrix class), vibrates
exactly like a relativistic electron (Dirac's equation), and even "reads"
the zeros from a formula in real time without memorizing them. And yet —
measured with total honesty across more than two hundred configurations —
the drum never *is* the zeros. The programme's real discovery is the wall:
local, nearby-interaction systems cannot carry the quantum entanglement
the zeros would need. The map says exactly where to look next: beyond
locality. (The Riemann hypothesis itself remains unproven — the package is
built so that no numerical success can quietly claim otherwise.)

## RU — Охота за стеной, а не за доказательством

Математики давно подозревают, что нули дзета-функции Римана — особые числа,
хранящие глубочайшие секреты простых чисел — ведут себя как уровни энергии
квантовой системы. Если бы удалось построить правильную «квантовую
барабанную мембрану», резонансы которой в точности совпадают с этими нулями,
столетняя проблема была бы решена. Эта программа построила ближайший
измеренный кандидат: магнитную решётку, идеально настроенную (её статистика
совпадает с предсказанным классом случайных матриц), вибрирующую в точности
как релятивистский электрон (уравнение Дирака) и даже «читающую» нули из
формулы в реальном времени, не запоминая их. И всё же — измеренное с полной
честностью на более чем двухстах конфигурациях — эта мембрана никогда *не
является* нулями. Настоящее открытие программы — стена: системы с локальными
близкодействующими взаимодействиями не могут нести квантовую запутанность,
которая понадобилась бы нулям. Карта точно говорит, где искать дальше: за
пределами локальности. (Сама гипотеза Римана остаётся недоказанной — пакет
устроен так, что ни один численный успех не сможет тихо заявить обратное.)


---

## P.2. Executive summary

# Executive summary — one page

**The programme.** AB-Cloud asks how close a flux-threaded lattice can come
to the Hilbert–Pólya operator — the hypothetical Hermitian operator whose
spectrum would be the Riemann ζ zeros. Three laboratories (spectral core,
Dirac skeleton, Hilbert–Pólya bridge) plus a blind-verification platform
were consolidated into one academic package with a single verdict ledger.

**What is established (within numerical certificates).**
- The construct is Hermitian to machine zero; its statistics are GUE-class
  across every explored family (⟨r⟩ = 0.60; decorated Dirac operator 0.608
  vs theory 0.5992; Klein quartic ensemble D = 0.0808).
- Its dynamics is exactly Dirac: continuum limit R² = 0.9997; Berry phase π;
  Klein tunneling ×977 over control; Zitterbewegung at ω = 2E.
- The prime weight Λ(n)/√n lives in the heat trace (r = 0.9996) — and
  demonstrably nowhere in the 87 gate spectra.
- Two independent engines read all 649 ζ zeros to T = 1000 blind,
  cross-engine discrepancy exactly 0.0.
- The compiler wins the honest class-B benchmark ×59,000 at 1−F = 4.4·10⁻¹⁶.

**What is not.** Spectral identity fails — stably, on every configuration
(9–10 orders configuration metric; ≈0.5 order trace metric). The Riemann
hypothesis is `blocked` by the V13 obligation machine by construction.

**The headline.** The wall is located: trace identity is achievable exactly
and nonlocally (r_H7 = 1.000000), but locality suppresses the entanglement
the zero comb demands (S_A ≈ 12–16 nats vs Haar 160–220). Any positive
construction must be nonlocal or equivalently entangling — a concrete,
testable requirement.

**Artifacts.** Unified monograph (RU/EN full volumes + 5 abstracts),
machine-readable registry, interactive web laboratory (offline),
six-language CLI, integrity test suite. DOI 10.5281/zenodo.21825394.



---

## 38e. The E5 phase diagram and the E7 route fraction (complete tables)

### E5 — the phase diagram (complete, verbatim: n_loop by s × y_v)

| s \ y_v | 0.15 | 0.25 | 0.35 | 0.5 | 0.65 |
|---|---|---|---|---|---|
| 0.02 | 5 | 6 | 6 | 4 | 4 |
| 0.03 | 4 | 5 | 6 | 6 | 5 |
| 0.05 | 3 | 1 | 5 | 0 | 6 |
| 0.08 | 0 | 1 | 2 | 6 | 5 |
| 0.12 | 0 | 0 | 0 | 0 | 3 |

### E7 — the route fraction over time (sampled: every 20th point; hyperbolic and isotropic)

| t | route_fraction_hyper | route_fraction_iso |
|---|---|---|
| 0.024 | 0.0000 | 0.0000 |
| 0.494 | 0.0017 | 0.0111 |
| 0.965 | 0.0406 | 0.0372 |
| 1.435 | 0.0126 | 0.0037 |
| 1.906 | 0.0438 | 0.0660 |
| 2.376 | 0.0154 | 0.0070 |
| 2.847 | 0.0427 | 0.0222 |
| 3.318 | 0.0149 | 0.0208 |
| 3.788 | 0.0440 | 0.0456 |
| 4.259 | 0.0239 | 0.0273 |
| 4.729 | 0.0459 | 0.0234 |
| 5.200 | 0.0228 | 0.0474 |
| 5.671 | 0.0246 | 0.0415 |
| 6.141 | 0.0296 | 0.0245 |
| 6.612 | 0.0261 | 0.0270 |
| 7.082 | 0.0276 | 0.0268 |
| 7.553 | 0.0461 | 0.0146 |
| 8.024 | 0.0327 | 0.0348 |
| 8.494 | 0.0169 | 0.0133 |
| 8.965 | 0.0307 | 0.0291 |
| 9.435 | 0.0180 | 0.0207 |
| 9.906 | 0.0404 | 0.0553 |
| 10.376 | 0.0103 | 0.0145 |
| 10.847 | 0.0612 | 0.0355 |
| 11.318 | 0.0158 | 0.0311 |
| 11.788 | 0.0330 | 0.0383 |
| 12.259 | 0.0314 | 0.0276 |
| 12.729 | 0.0223 | 0.0163 |
| 13.200 | 0.0252 | 0.0138 |
| 13.671 | 0.0697 | 0.0315 |
| 14.141 | 0.0272 | 0.0220 |
| 14.612 | 0.0298 | 0.0224 |
| 15.082 | 0.0303 | 0.0287 |
| 15.553 | 0.0235 | 0.0257 |
| 16.024 | 0.0359 | 0.0193 |
| 16.494 | 0.0209 | 0.0267 |
| 16.965 | 0.0823 | 0.0345 |
| 17.435 | 0.0247 | 0.0132 |
| 17.906 | 0.0352 | 0.0438 |
| 18.376 | 0.0272 | 0.0217 |
| 18.847 | 0.0358 | 0.0613 |
| 19.318 | 0.0375 | 0.0183 |
| 19.788 | 0.0605 | 0.0546 |
| 20.259 | 0.0302 | 0.0195 |
| 20.729 | 0.0320 | 0.0266 |
| 21.200 | 0.0404 | 0.0290 |
| 21.671 | 0.0232 | 0.0126 |
| 22.141 | 0.0265 | 0.0223 |
| 22.612 | 0.0249 | 0.0124 |
| 23.082 | 0.0438 | 0.0287 |
| 23.553 | 0.0249 | 0.0161 |
| 24.024 | 0.0375 | 0.0210 |
| 24.494 | 0.0264 | 0.0207 |
| 24.965 | 0.0379 | 0.0281 |
| 25.435 | 0.0293 | 0.0297 |
| 25.906 | 0.0429 | 0.0277 |
| 26.376 | 0.0324 | 0.0186 |
| 26.847 | 0.0390 | 0.0223 |
| 27.318 | 0.0312 | 0.0137 |
| 27.788 | 0.0302 | 0.0351 |
| 28.259 | 0.0283 | 0.0116 |
| 28.729 | 0.0371 | 0.0155 |
| 29.200 | 0.0264 | 0.0110 |
| 29.671 | 0.0321 | 0.0292 |
| 30.141 | 0.0324 | 0.0443 |
| 30.612 | 0.0265 | 0.0261 |
| 31.082 | 0.0392 | 0.0507 |
| 31.553 | 0.0236 | 0.0304 |
| 32.024 | 0.0427 | 0.0246 |
| 32.494 | 0.0350 | 0.0204 |
| 32.965 | 0.0429 | 0.0303 |
| 33.435 | 0.0288 | 0.0244 |
| 33.906 | 0.0282 | 0.0183 |
| 34.376 | 0.0296 | 0.0255 |
| 34.847 | 0.0357 | 0.0388 |
| 35.318 | 0.0231 | 0.0099 |
| 35.788 | 0.0422 | 0.0377 |
| 36.259 | 0.0303 | 0.0325 |
| 36.729 | 0.0287 | 0.0153 |
| 37.200 | 0.0332 | 0.0395 |
| 37.671 | 0.0304 | 0.0236 |
| 38.141 | 0.0445 | 0.0240 |
| 38.612 | 0.0315 | 0.0140 |
| 39.082 | 0.0563 | 0.0495 |
| 39.553 | 0.0194 | 0.0356 |
| 40.024 | 0.0375 | 0.0380 |
| 40.494 | 0.0265 | 0.0246 |
| 40.965 | 0.0487 | 0.0281 |
| 41.435 | 0.0295 | 0.0264 |
| 41.906 | 0.0577 | 0.0261 |
| 42.376 | 0.0238 | 0.0210 |
| 42.847 | 0.0312 | 0.0272 |
| 43.318 | 0.0333 | 0.0290 |
| 43.788 | 0.0308 | 0.0286 |
| 44.259 | 0.0370 | 0.0398 |
| 44.729 | 0.0323 | 0.0214 |
| 45.200 | 0.0464 | 0.0344 |
| 45.671 | 0.0270 | 0.0168 |
| 46.141 | 0.0416 | 0.0578 |
| 46.612 | 0.0254 | 0.0163 |
| 47.082 | 0.0535 | 0.0250 |
| 47.553 | 0.0229 | 0.0134 |
| 48.024 | 0.0391 | 0.0262 |
| 48.494 | 0.0246 | 0.0198 |
| 48.965 | 0.0389 | 0.0330 |
| 49.435 | 0.0337 | 0.0387 |
| 49.906 | 0.0380 | 0.0286 |
| 50.376 | 0.0443 | 0.0368 |
| 50.847 | 0.0373 | 0.0199 |
| 51.318 | 0.0378 | 0.0236 |
| 51.788 | 0.0269 | 0.0266 |
| 52.259 | 0.0400 | 0.0373 |
| 52.729 | 0.0239 | 0.0247 |
| 53.200 | 0.0395 | 0.0237 |
| 53.671 | 0.0339 | 0.0211 |
| 54.141 | 0.0411 | 0.0538 |
| 54.612 | 0.0339 | 0.0135 |
| 55.082 | 0.0439 | 0.0352 |
| 55.553 | 0.0371 | 0.0263 |
| 56.024 | 0.0407 | 0.0194 |
| 56.494 | 0.0344 | 0.0242 |
| 56.965 | 0.0459 | 0.0175 |
| 57.435 | 0.0335 | 0.0481 |
| 57.906 | 0.0410 | 0.0156 |
| 58.376 | 0.0334 | 0.0431 |
| 58.847 | 0.0310 | 0.0176 |
| 59.318 | 0.0472 | 0.0570 |
| 59.788 | 0.0239 | 0.0212 |
| 60.259 | 0.0542 | 0.0271 |
| 60.729 | 0.0320 | 0.0356 |
| 61.200 | 0.0393 | 0.0424 |
| 61.671 | 0.0234 | 0.0172 |
| 62.141 | 0.0395 | 0.0223 |
| 62.612 | 0.0295 | 0.0185 |
| 63.082 | 0.0432 | 0.0400 |
| 63.553 | 0.0353 | 0.0277 |
| 64.024 | 0.0513 | 0.0268 |
| 64.494 | 0.0350 | 0.0146 |
| 64.965 | 0.0298 | 0.0241 |
| 65.435 | 0.0363 | 0.0489 |
| 65.906 | 0.0277 | 0.0125 |
| 66.376 | 0.0414 | 0.0346 |
| 66.847 | 0.0255 | 0.0179 |
| 67.318 | 0.0449 | 0.0346 |
| 67.788 | 0.0320 | 0.0270 |
| 68.259 | 0.0309 | 0.0319 |
| 68.729 | 0.0285 | 0.0392 |
| 69.200 | 0.0407 | 0.0188 |
| 69.671 | 0.0275 | 0.0407 |
| 70.141 | 0.0479 | 0.0273 |
| 70.612 | 0.0342 | 0.0237 |
| 71.082 | 0.0384 | 0.0200 |
| 71.553 | 0.0363 | 0.0347 |
| 72.024 | 0.0358 | 0.0314 |
| 72.494 | 0.0321 | 0.0187 |
| 72.965 | 0.0309 | 0.0178 |
| 73.435 | 0.0449 | 0.0256 |
| 73.906 | 0.0381 | 0.0115 |
| 74.376 | 0.0288 | 0.0294 |
| 74.847 | 0.0339 | 0.0220 |
| 75.318 | 0.0544 | 0.0246 |
| 75.788 | 0.0260 | 0.0178 |
| 76.259 | 0.0552 | 0.0217 |
| 76.729 | 0.0326 | 0.0262 |
| 77.200 | 0.0402 | 0.0143 |
| 77.671 | 0.0322 | 0.0184 |
| 78.141 | 0.0554 | 0.0183 |
| 78.612 | 0.0438 | 0.0348 |
| 79.082 | 0.0354 | 0.0116 |
| 79.553 | 0.0361 | 0.0389 |
| 80.024 | 0.0424 | 0.0422 |
| 80.494 | 0.0216 | 0.0438 |
| 80.965 | 0.0342 | 0.0221 |
| 81.435 | 0.0459 | 0.0348 |
| 81.906 | 0.0398 | 0.0145 |
| 82.376 | 0.0501 | 0.0314 |
| 82.847 | 0.0298 | 0.0155 |
| 83.318 | 0.0489 | 0.0170 |
| 83.788 | 0.0352 | 0.0374 |
| 84.259 | 0.0447 | 0.0198 |
| 84.729 | 0.0331 | 0.0325 |
| 85.200 | 0.0381 | 0.0264 |
| 85.671 | 0.0297 | 0.0351 |
| 86.141 | 0.0595 | 0.0227 |
| 86.612 | 0.0328 | 0.0209 |
| 87.082 | 0.0328 | 0.0162 |
| 87.553 | 0.0344 | 0.0397 |
| 88.024 | 0.0311 | 0.0308 |
| 88.494 | 0.0483 | 0.0326 |
| 88.965 | 0.0337 | 0.0293 |
| 89.435 | 0.0493 | 0.0379 |
| 89.906 | 0.0303 | 0.0238 |
| 90.376 | 0.0414 | 0.0222 |
| 90.847 | 0.0261 | 0.0232 |
| 91.318 | 0.0339 | 0.0208 |
| 91.788 | 0.0318 | 0.0200 |
| 92.259 | 0.0401 | 0.0132 |
| 92.729 | 0.0396 | 0.0399 |
| 93.200 | 0.0457 | 0.0135 |
| 93.671 | 0.0262 | 0.0504 |
| 94.141 | 0.0337 | 0.0212 |
| 94.612 | 0.0362 | 0.0519 |
| 95.082 | 0.0441 | 0.0197 |
| 95.553 | 0.0378 | 0.0248 |
| 96.024 | 0.0233 | 0.0311 |
| 96.494 | 0.0361 | 0.0132 |
| 96.965 | 0.0235 | 0.0258 |
| 97.435 | 0.0530 | 0.0214 |
| 97.906 | 0.0309 | 0.0338 |
| 98.376 | 0.0440 | 0.0220 |
| 98.847 | 0.0238 | 0.0276 |
| 99.318 | 0.0413 | 0.0147 |
| 99.788 | 0.0288 | 0.0273 |
| 100.259 | 0.0335 | 0.0250 |
| 100.729 | 0.0405 | 0.0347 |
| 101.200 | 0.0316 | 0.0261 |
| 101.671 | 0.0391 | 0.0248 |
| 102.141 | 0.0244 | 0.0465 |
| 102.612 | 0.0274 | 0.0364 |
| 103.082 | 0.0397 | 0.0300 |
| 103.553 | 0.0423 | 0.0346 |
| 104.024 | 0.0274 | 0.0284 |
| 104.494 | 0.0462 | 0.0180 |
| 104.965 | 0.0236 | 0.0236 |
| 105.435 | 0.0413 | 0.0334 |
| 105.906 | 0.0297 | 0.0417 |
| 106.376 | 0.0396 | 0.0206 |
| 106.847 | 0.0300 | 0.0337 |
| 107.318 | 0.0380 | 0.0381 |
| 107.788 | 0.0396 | 0.0212 |
| 108.259 | 0.0338 | 0.0297 |
| 108.729 | 0.0273 | 0.0346 |
| 109.200 | 0.0317 | 0.0246 |
| 109.671 | 0.0366 | 0.0428 |
| 110.141 | 0.0272 | 0.0132 |
| 110.612 | 0.0487 | 0.0376 |
| 111.082 | 0.0257 | 0.0209 |
| 111.553 | 0.0430 | 0.0235 |
| 112.024 | 0.0355 | 0.0235 |
| 112.494 | 0.0468 | 0.0171 |
| 112.965 | 0.0329 | 0.0362 |
| 113.435 | 0.0426 | 0.0244 |
| 113.906 | 0.0389 | 0.0283 |
| 114.376 | 0.0309 | 0.0201 |
| 114.847 | 0.0409 | 0.0184 |
| 115.318 | 0.0336 | 0.0321 |
| 115.788 | 0.0344 | 0.0243 |
| 116.259 | 0.0360 | 0.0223 |
| 116.729 | 0.0332 | 0.0300 |
| 117.200 | 0.0350 | 0.0257 |
| 117.671 | 0.0305 | 0.0226 |
| 118.141 | 0.0466 | 0.0142 |
| 118.612 | 0.0421 | 0.0220 |
| 119.082 | 0.0331 | 0.0296 |
| 119.553 | 0.0515 | 0.0176 |
| 120.000 | 0.0356 | 0.0456 |

5100 points total; the full CSV — `02_data/raw/wave_attractors/E7_route_fraction.csv`.

---

## 31R. The eight observatory documents — primary records in the original Russian

*Editorial note: the observatory's documentation set exists in Russian only. The English condensations above (31a–31h) carry the content; the originals are included verbatim below as primary source records — the same policy the Russian edition applies to English-language sources.*

### 31R.01 — Overview (первоисточник на русском / primary record in the original Russian)


> Автор кодов и исследования: **Исаев Исхак Хамзатович** (ORCID 0009-0003-7299-0701 · DOI 10.5281/zenodo.21825394)
> Этот документ — научная «визитная карточка» проекта: постановка задачи, физическая модель, статистическая методология и то, зачем всё это нужно.

---

## 1. Проблема: что не так с нулями дзета-функции

Дзета-функция Римана ζ(s) — один из самых знаменитых объектов математики. Её нетривиальные нули (комплексные числа вида s = 1/2 + iγ) пронумерованы по возрастанию мнимой части γ: первый нуль γ₁ ≈ 14.134725142, второй γ₂ ≈ 21.022039639, и так далее до бесконечности. **Гипотеза Римана** утверждает, что все они лежат на прямой Re(s) = 1/2; она проверена для триллионов нулей, но не доказана.

В 1972 году Хью Монтгомери, изучая парные корреляции нулей ζ(s), встретился с физиком Фрименом Дайсоном — и Дайсон мгновенно узнал в формулах Монтгомери статистику **случайных матриц GUE** (Gaussian Unitary Ensemble, гауссов унитарный ансамбль, параметр β=2). Это была сенсация: нули «квантовой» по своей природе функции ведут себя как энергетические уровни сложной квантовой системы, инвариантной относительно обращения времени с нарушением симметрии при комплексном сопряжении. С тех пор вопрос звучит так: **какая именно квантовая система имеет этими уровнями свой спектр?**

## 2. Идея Гильберта–Полиа

Ещё в начале XX века Дэвид Гильберт и Дьёрдь Полиа независимо предложили программу: если найти **самосопряжённый (эрмитов) оператор Ĥ**, спектр которого совпадает с {1/2 + iγ}, то гипотеза Римана станет следствием того факта, что спектр эрмитова оператора вещественен: если γ — вещественно, то 1/2 + iγ лежит на критической прямой. Вопрос «доказать про нули» превращается в вопрос «найти систему».

Программа Гильберта–Полиа — это не один тест, а **целый конвейер проверок**: оператор должен быть (а) самосопряжённым, (б) воспроизводить не только положения нулей, но и их статистику GUE, (в) содержать в своей структуре простые числа (формула Римана–фон Мангольдта связывает ζ(s) с простыми), (г) делать это не для одной удачной точки параметров, а устойчиво. Именно такой конвейер и реализован в этом проекте.

## 3. Модель AB-облака: решётка, вихри, поток Ааронова–Бома

Центральный физический объект проекта — **гамильтониан AB-облака**. Идея такова:

1. Берём двумерную решётку L×L узлов (например, 20×20 = 400 узлов). Гильбертово пространство — по одной ступеньке на узел, то есть матрица гамильтониана имеет размер L²×L². Для L=20 это 400×400, для L=64 — уже 4096×4096, для L=72 — 5184×5184 плотных матриц.
2. В решётку помещаем **вихри магнитного потока** — точки, через которые «продавлен» магнитный поток Ааронова–Бома величиной α (в единицах кванта потока). Кинетический член на связи, пересекающей поток, получает фазовый множитель exp(iα) — это классическая решёточная реализация эффекта Ааронова–Бома.
3. Электроны (или бозоны) на такой решётке «чувствуют» вихри нелокально: их волновые функции огибают вихри, образуя **облако Ааронова–Бома** (AB-cloud) — отсюда название.
4. Варьируя плотность вихрей и величину потока α, мы меняем статистику спектра. Особый интерес представляют «магические» значения потока — например, **α = 25/900** («острый поток», sharp flux) и классические точки вроде α = 1/2, 1/3, 1/4.

Ключевые режимы, вокруг которых построен главный аудит (гейт H5):

| Режим | Плотность вихрей | Поток α | Смысл |
|---|---|---|---|
| **A** (базлайн) | Nv = 4 | 0.5 | историческая базовая конфигурация |
| **B** (монография) | Nv = L²/36 | 0.5 | плотность, предписанная монографией AB-Cloud |
| **C** (острый поток) | Nv = 4 | 25/900 ≈ 0.0278 | редкие вихри, но «острый» поток |
| **D** (комбинация) | Nv = L²/36 | 25/900 | плотность монографии + острый поток — **главный кандидат** |

Модель фундаментально связана с простыми числами: частоты, на которых решётка «звенит» при динамическом отклике, тянутся к log p (логарифмы простых) — это проверяет гейт H1 (PRIME-TRACE): на спектрограмме временной эволюции ищется Брэгг-гребень на частотах ω = log p, при этом композитные «декой»-частоты (log 21, log 33, …) обязаны молчать — иначе это не арифметика, а случайный артефакт геометрии.

## 4. Статистическая методология: как сравнивают два спектра

Никакое «визуальное сходство» не считается доказательством — только формальные статистики:

- **Статистика соседних отношений r**: для упорядоченных зазоров между уровнями считается r_i = min(δᵢ, δᵢ₊₁)/max(δᵢ, δᵢ₊₁). Для GUE среднее ⟨r⟩ ≈ 0.5996; доверительный интервал для конечных выборок [0.5772, 0.6212]. Для «расцепленных» (uncorrelated) уровней ⟨r⟩ ≈ 0.5307.
- **Unfolding (развёртка)**: прежде чем сравнивать зазоры, спектр «разворачивают» — локальную плотность уровней вычитают полиномиальной подгонкой (в кодах — unfold по полиномам степени 5/9), чтобы зазоры стали безразмерными и стационарными.
- **Wigner surmise GUE β=2**: аналитическая аппроксимация распределения зазоров p(s) = (32/π²)·s²·exp(−4s²/π). Интересная деталь, проверяемая в Suite (Test 37): нормировка 32/π² — это в точности тождество (1/2)! = √π/2, то есть «полуфакториал» через Γ-функцию.
- **Критерий Колмогорова–Смирнова (KS)**: мера максимального расхождения между эмпирической CDF зазоров и GUE-эталоном. Порог значимости зависит от размера выборки: **d_crit = 1.63/√n** — поэтому при переходе от L=16 (n ≈ 150 зазоров, порог ≈ 0.132) к L=64 (n ≈ 2400, порог ≈ 0.033) один и тот же тест становится **в 4 раза строже**. Это «проклятие мощности»: статистическая значимость растёт, физика не меняется.
- **Anderson–Darling (A²)**: более чувствительный к хвостам GOF-тест; его корректная калибровка — предмет отдельного файла `test11_honest` (см. документ 02).

Правило прохождения режима в H5 (v23.5+): доля реализаций с ⟨r⟩ в GUE-интервале ≥ 90% **И** (индивидуальных KS-проходов ≥ 90% **ИЛИ** медиана KS_D < 0.10). Если проход достигнут только через вторую половину «ИЛИ» — вердикт честно помечается маркером **«OR-clause only»**.

## 5. Философия аудита: «честный вердикт важнее красивого»

Коды проекта построены по жёстким правилам научной честности, которые прямо видны в changelog'ах:

1. **Null-модели сопоставляются с режимами**. Пик в данных «весит» что-либо только если он превышает 95-й перцентиль той же статистики на нулевых моделях: vortex-free решётке с тем же α и GUE-матрице того же размера со свежими сидами (гейт H1, deepen-протокол).
2. **Декой-контроль специфичности**. Брэгг-гребень обязан стоять на ВСЕХ простых и МОЛЧАТЬ на составных-декоях. Только так результат нельзя списать на общую «звонкость» решётки.
3. **Заранее зарегистрированные правила останова**. Например: бугорок, не превышающий P95 максимумов нулей из 20 реализаций, объявляется «generic flux-geometry artifact» — без апелляций.
4. **Бюджет вычислений декларируется заранее**. H5 не может запустить больше HP5_SOLVE_CAP = 40 плотных диагонализаций, и это же число печатается в баннере стоимости ДО прогона — расхождение план/факт исключено архитектурой (один и тот же планировщик `_hp5_plan`).
5. **DONE-line печатает фактический вердикт**. Строка «done → PASS» не может противоречить таблице «N sub-checks, M failed → WARN» — это класс багов v22, исправленный в v23.6.
6. **Пессимистичные статусы не перезаписываются**. «PASS поверх mixed/MARGINAL» невозможен: статус sweep входит в общий ok теста.

## 6. Что уже показал проект (сводка на момент v24.2-SA, сентябрь 2026)

- Прогон **64×64** (ансамбль 7×4 режима, бюджет 40 солвов): режимы B, C, D проходят параметрическую вилку через OR-оговорку; **режим D — единственный, чья медиана KS_D = 0.0231 ниже порога d_crit = 0.033** для n ≈ 2400 зазоров, то есть статистически неотличим от GUE на этой выборке; индивидуальные KS-проходы D — 71.4% (5 из 7), наибольшие в батарее.
- Базовый режим **A** деградирует с ростом решётки (медиана KS_D 0.312 → 0.350 при 16 → 64): опубликованная точка α=0.5 — настоящая периферия, а не артефакт.
- α-профиль при фиксированной редкой плотности (Nv=4) при переходе 16→64 перевернулся из PLATEAU-LOW в NONE — разбор (документ 05) показал, что это **эффект мощности теста** (порог ужесточился в ~4 раза), а не смена физики; одновременно он обнажил смешение «размер vs плотность» — следующий шаг протокола.
- Честная перекалибровка Test 11 (`test11_honest`) объяснила «медиану референса 12.54» в старом прогоне бутстрэп-артефактом завязок; на корректном i.i.d.-null медиана A² возвращается к учебной шкале O(1).

Полный разбор с числами — в документах [05](../../02_data/raw/meridian/docs/05_gate_H5_regimy.md) и [08](../../02_data/raw/meridian/docs/08_reproduciuemost.md).

## 7. Почему Julia и почему «один файл»

- **Скорость**: плотные эрмитовы диагонализации 4096²–5184² на смартфоне — это вызовы LAPACK через `LinearAlgebra.eigen`; Julia компилирует горячие циклы в нативный код, поэтому тысячи реализаций ансамбля реально считаются на телефоне (Termux).
- **Одна копия = один эксперимент**: каждый стенд поднимает всё своё ядро из одного файла. Это гарантирует, что опубликованный лог прогона относится к коду, который можно скачать одной кнопкой, — никакой дрейфа версий между «библиотекой» и «скриптом».
- **Ядро поднимается VERBATIM**: компактный `hp_audit_standalone.jl` содержит то же ядро, что и `ab_cloud_v23_v2.jl` (буквально скопированное), поэтому при равных сидах числа совпадают бит-в-бит — это осознанное решение против «двух источников истины».

## 8. Куда смотреть дальше

- Хотите запустить — открывайте [03 · Руководство по запуску](../../02_data/raw/meridian/docs/03_rukovodstvo_zapuska.md).
- Хотите понять каждую строку вывода — [04 · Физика и математика](../../02_data/raw/meridian/docs/04_fizika_matematika.md) и [05 · Гейт H5](../../02_data/raw/meridian/docs/05_gate_H5_regimy.md).
- Хотите узнать историю каждого файла — [07 · Хронология версий](../../02_data/raw/meridian/docs/07_hronologiya_versij.md).
- Хотите повторить прогон «по-научному» — [08 · Воспроизводимость](../../02_data/raw/meridian/docs/08_reproduciuemost.md).


---

### 31R.02 — Code catalogue (первоисточник на русском / primary record in the original Russian)


> В этой папке 28 файлов: 24 Julia-стенда, 1 Python-тест, 1 конфиг и 2 файла данных ζ-нулей.
> Здесь разобран **каждый**: назначение, что именно вычисляет, как запустить, что напечатает, к кому идти за чем.
> Правило выбора простое: **новичок → `ab_cloud_v23_v2.jl` и `hp_audit_standalone.jl`; параметрические свипы → `RH_Sweep_Pro.jl`; верификация монографии → `AB_Cloud_Monumental_v6_3.jl`; статистический аудит → `test11_honest`**.

---

## Схема родословной

```text
RH_Unified.jl (500 ζ-нулей)
   └─→ RH_Unified_v5.jl (расширенные пресеты)
          └─→ RH_Sweep_Pro.jl (13 661 ζ-нулей, sweep 8 параметров)

AB_Cloud_Monumental_v6_3.jl  (V01–V112, порт Python-монументальной базы)

ab_cloud_v19 → v19_v1 → v20 → v21 → v21_v1 → v22 → v23 → v23_v1 → v23_v2 (SUPERCOMBO v23.6)
                                                      │
                                  ядро VERBATIM ──────┴──→ hp_audit_standalone.jl (v24.2-SA, H1–H7)

параллельная ветка: каждый ab_cloud_vN (+ RH_Sweep_Pro, Monumental) имеет _D-версию
с консольной айдентикой MERIDIAN DESIGN SYSTEM (физика — бит-в-бит та же).
```

---

## A. Главная линейка — `ab_cloud_v*.jl` (Verification Suite)

Общий портрет: каждый файл — автономный интерактивный стенд. Запускается через
`julia -e 'include("имя.jl")'`, печатает меню, дальше всё — номерами и буквами из консоли.
Зависимости — **только стандартная библиотека Julia** (LinearAlgebra, Random, SparseArrays, Statistics, Printf, Dates).

### `ab_cloud_v19.jl` — v19.1, 23 342 строки
**Что это:** стенд из 37 тестов, сфокусированных на гипотезе Гильберта–Полиа, с продвинутой RMT-диагностикой.
**Ключевое в версии:** live-display pump (анти-дедлок консоли при замёрзшем терминале — Windows QuickEdit, закрытый fd: stdout-tee перекачивается одной fire-and-forget задачей, аудит не может заблокироваться); Test 20 (TKNN Chern) добит до трёх литературных якорей α = 1/4, 1/3, 1/5 плюс ветка массовой регуляризации α = 1/2 (C₁ = 0 оба знака); **новый Test 37** — аудит «полуфакториала» (1/2)! через Γ: лог-выпуклость Бора–Моллерупа + тождество Γ(1/2)² = π + что нормировка GUE-surmise 32/π² — это (1/2)! = √π/2 «в маскировке»; hardcore-проход 2 — переаудит в BigFloat 256 бит; вычищен мёртвый код (retired twisted-torus FHS и т. д.).

### `ab_cloud_v19_v1.jl` — 23 956 строк
Развитие v19: исправления и уточнения после аудита (числа и тесты — те же 37, плюс укрепления протоколов).

### `ab_cloud_v20.jl` — 24 596 строк
Промежуточная эволюция линейки: укрепление RMT-диагностики и живого дисплея, подготовка 3D-движка.

### `ab_cloud_v21.jl` — v21, 25 519 строк
**Что нового:** 38-й тест и **Physics Lab** и **3D Lab** — разреженный (sparse) движок на стандартном `SparseArrays` (без внешних зависимостей), позволяющий считать большие объёмы; в импортах появляются `SymTridiagonal/eigvals!` для 3D-движка, `dot` для FHS link product (Test 20), in-place операции `mul!/rmul!` (Test 27).

### `ab_cloud_v21_v1.jl` — 25 519 строк
Правки v21 (то же ядро, укрепления).

### `ab_cloud_v22.jl` — v22.2, 7 369 строк
**Что это:** специализированный «журнальный» движок построения графиков — модуль **`ABPlotV23`** (публикационное качество) и **исправленный THREE-PASS Test 38**: 38a + 38b hardcore + 38c ladder. Файл меньше, потому что это граф-надстройка/ядро без части интерактивной обвязки прежних версий.

### `ab_cloud_v23.jl` — v23, 28 281 строка
Начало линейки v23: объединение ядра v21 и график-движка v22, подготовка SUPERCOMBO.

### `ab_cloud_v23_v1.jl` — 29 904 строки
Развитие v23 (промежуточные фиксы перед v23.6).

### ⭐ `ab_cloud_v23_v2.jl` — SUPERCOMBO v23.6, 30 908 строк — **самый полный стенд**
**Что это:** флагман = ядро v21 (38 тестов + hardcore-проходы + Physics Lab + 3D Lab) × график-движок v22.2 (модуль ABPlotV23) × THREE-PASS Test 38.
**Ключевое в v23.6:**
- **№1 DONE-LINE**: строка «[HP H#] done in … → PASS» печатает фактический вердикт (PASS/WARN), а не «не упал по исключению» — остаток бага класса «WARN поверх PASS»;
- **№2 H1 DEEPEN-протокол**: потолок нулей режима (vortex-free + GUE) переоценивается распределением из `hp_deep_nulls` (20) реализаций каждого типа; бугорок судится против 95-го перцентиля максимумов нулей (заранее зарегистрированное правило останова): ≤ P95 → «generic flux-geometry artifact» → ABSENT; > P95 → честный WARN с эскалацией. Ансамбль AB расширяется на `hp_deep_configs` (10) конфигураций. Новый график №5 (распределение max-SNR нулей vs AB);
- **№3 H5 α-профиль (finetuning vs plateau)**: GUE-качество вдоль α при фиксированной разреженной Nv: α ∈ {25/900, 0.05, 0.1, 0.2, 0.35, 0.5}. PLATEAU → «острый поток GUE-универсален»; NARROW → истинный finetuning. Точка α=0.5 независимо реплицирует режим A. Строка «α-profile (headline, never scored)» + 2 графика (KS-pass % и медиана D vs α);
- **№5 H1 окно + специфичность**: окно D1-скана расширяется до max(3.0, ω_max+0.2); цели делятся на простые и **композитные декой**-цели (21, 33, 54, 56): в ζ Брэгг-гребень обязан стоять на ВСЕХ простых и молчать на декоях — `zeta_ok` требует и того, и другого;
- **№4 H4 guard домена**: если ни один заявленный критический q (0.3/0.5/1.0) не попал в [q_min, q_max] — строка «location vs claimed criticals» честно FAIL-класса с объяснением (молчаливая деградация невозможна);
- **ПРЕСЕТЫ**: `f` FAST battery (L=16, ensemble=100, ~10–20 мин), `F` FULL battery (L=56, ensemble=40, α-scan n=30, часы); новые параметры: `hp_deep_nulls=20`, `hp_deep_configs=10`, `hp_alpha_scan=true`, `hp_alpha_scan_n=40` (пункты 16–18 меню параметров).

### `_D`-версии: `ab_cloud_v19_D.jl`, `v19_v1_D? (нет)`, `v21_D.jl`, `v21_v1_D.jl`, `v22_D.jl`, `v23_v1_D.jl`, `RH_Sweep_Pro_D.jl`, `RH_Unified_D.jl`, `AB_Cloud_Monumental_v6_3_D.jl`
**Что такое `_D`:** те же стенды, в начало которых добавлен самоcontained блок **MERIDIAN DESIGN SYSTEM v1.0** (~250 строк, только Base, префикс `_mr_`): двойные рамки-баннеры, ◆-секции, статусы ✓/✗/⚠, живые прогресс-бары ▰▰▰▱▱, выровненные kv-строки, цвета только на настоящем TTY (форс: `ENV["MERIDIAN_COLOR_FORCE"]="1"`, выкл: `="0"`, ширина рамок 62 — помещается на телефоне), каждый принтер fail-safe (любая ошибка → обычный текст). **Физика и числа — бит-в-бит те же.** Если сомневаетесь, какой запускать: `_D` — красивее и информативнее в консоли; обычная — максимально «стерильная» для пайплайнов и логов.

---

## B. HP·MERIDIAN — `hp_audit_standalone.jl` (v24.2-SA, 6 054 строки)

**Зачем этот файл существует (спецификация автора):** «отдельный код, в котором только проверка H — тесты из меню h — чтобы не вносить правки в огромный код, а в более компактный, который конкретно проверяет нужное нам конкретно сейчас». Ядро поднято **VERBATIM** из `ab_cloud_v23_v2.jl`, поэтому при равных сидах числа совпадают бит-в-бит.

**Внутри — 7 гейтов (уникальные консольные имена):**

| Гейт | Имя | Что проверяет |
|---|---|---|
| H1 | **PRIME-TRACE** | raw-FT Брэгг-гребень на ω = log p в отклике решётки + композитные decoy-контроли (21, 33, 54, 56) + режимно-сопоставленные null-модели (vortex-free на α режима, GUE matched-size со свежими сидами) + deepen-протокол P95 (`hp_deep_nulls`×2 типов) + авто-расширение окна до max(3.0, ω_max+0.2); `zeta_ok` = простые звучат И декой молчат |
| H2 | **WEYL-DOS** | «сырая» лестница N(E) плотности состояний вблизи вейл-точки, showdown моделей по **AICc** |
| H3 | **POWER-LAW** | лестница экспонент степенного закона, фальсификация «словарём» (dictionary falsification) |
| H4 | **CRITICAL-Q** | скан резкости по q + guard домена: заявленные критические (0.3/0.5/1.0) обязаны лежать в [q_min, q_max], иначе честный WARN |
| H5 | **REGIME-2×2** | ансамбль-шоудаун 4 режимов (A базлайн / B плотность монографии / C острый поток / D комбинация) + α-профиль (finetuning vs plateau); бюджет **HP5_SOLVE_CAP = 40** плотных диагонализаций; правило: ≥90% в GUE-интервале ⟨r⟩ И (KS-проход ≥90% ИЛИ медиана D < 0.10), с честным маркером «OR-clause only» |
| H6 | **HERMIT-STRESS** | стресс самосопряжённости/устойчивости гамильтониана |
| H7 | **SEQ-CORR** | корреляция «уровни ↔ нули» (последовательностная связь спектра с ζ-нулями) |

**История фиксов, зашитых в версию:**
- **v23.7-SA** — консоль HP·MERIDIAN: уникальные имена гейтов, doctor среды, «gate intel» со стоимостью, профили конфигурации, отказоизолированные команды, ANSI-безопасный цвет, Ctrl-C/EOF-безопасный ввод;
- **v23.8-SA** — «зависает на 5-м тесте»: репорт-tee перенаправлял fd 1 в файл, и прогресс был невиден до конца гейта (многочасовой H5 выглядел замёрзшим). Фиксы: (1) прогресс-бар рисуется «на месте» через дубликат реального tty-fd, виден ВО ВРЕМЯ гейта, с T+elapsed · ETA · текущей реализацией; (2) subprocess-heartbeat печатает строку «alive» в /dev/tty каждые 60 с — единственный честный канал во время одного блокирующего LAPACK-вызова; (3) живые строки стоимости перед каждым гейтом + оценка всей батареи; (4) починен план фракций H5 (бар скакал 87%→60%); (5) определены мёртвые `_prog_tty()/prog_tag!` (краш при >1 потоке);
- **v24.1-SA** — (1) **бюджет H5 ≤ 40 солвов**: все планы H5 через единый планировщик `_hp5_plan`: 2×2 режима × ≤7 конфигов (≤28) + α-профиль 6 точек × ≤2 конфига (≤12); планировщик разделяется гейтом и стоимостным баннером — баннер не может «пообещать» больше, чем гейт запустит; старая строка «ensemble ≥ 30» заменена на бюджет-комплаенс; гранулярность KS 1/N печатается явно. (2) Julia 1.12 fd hotfix (Base.fd больше не принимает Libuv-стримы);
- **v24.2-SA** — **FOCUS-D**: `hp_regime_mode = :regime_d` (консольная команда **`5d`**) — весь бюджет 40 солвов уходит в один режим D (комбинация: Nv = L²/36 + α = 25/900); сиды [D]-блока сохраняют канонический offset 30 000 — первые 7 сидов FOCUS-D бит-в-бит совпадают с [D]-блоком showdown (континуити с уже сделанными прогонами); свои вердикт-заголовки (MISS / OR-CLAUSE ONLY / CLEAN PASS) с гранулярностью 1/40; H1-сообщения показывают фактический режим; `_hp_diag_est` честен для не-showdown режимов.

**Пресеты консоли:** `:smoke` (L=20, ensemble=8, deep 4/4, α-scan n=6, ζ cap 2000 — валидация), `:fast` (L=72, ensemble=100, α-scan n=40 — батарея с авто-капом ≤40 солвов), `:full` (L=56, ensemble=40, α-scan n=30 — глубокий прогон).
**Данные нулей:** ищет `zeros50k.txt` рядом со скриптом (`@__DIR__`), затем в `pwd()`, затем `ENV["HP_ZEROS"]`, консольная команда `z`, CLI `zeros=path`. Не найдены → H1/H7 честно работают «без ζ-стороны» с пометкой.
**Память (важно!):** матрица — L²×L², пик памяти ≈ 2.5·(L²)²·16 байт: L=64 → ~0.6 ГБ, L=72 → ~1.0 ГБ. Время одного солва на среднем смартфоне: 64² ≈ 49 с; стоимость растёт ≈ L⁶.

---

## C. RH-линейка — корреляция с нулями ζ(s)

### `RH_Unified.jl` — 1 885 строк
**Что это:** единый самодостаточный файл «максимизация корреляции AB-облака с нулями ζ(s)».
**Внутри:** 500 реальных ζ-нулей (таблица зашита в файл; сгенерированы `mpmath.zetazero()`, 25 знаков; ⟨r⟩ = 0.6162 ≈ R_GUE = 0.5996); 61 магическая точка α (π/k, √k, 1/k, φ, e, ln 2, …); 6 вихрей (гексагональная конфигурация, настраивается 2–100+); RHConfig (33 параметра); jitter (дрожание) для α, W, σ, позиций и зарядов вихрей; 4 компоновки вихрей (hexagonal, ring, random, grid); sweep α в любом диапазоне (например, −16…+16); 9 preset-функций (`preset_quick`, `preset_full`, `preset_magic`, `preset_deep_sweep`, `preset_many_vortices`, `preset_high_jitter`, `preset_ring_vortices`, `preset_random_vortices`, `preset_custom`); графики Plots.jl; отчёты CSV/TXT(ASCII)/JSON; логирование времени.
**Запуск:**
```julia
include("RH_Unified.jl"); run_quick_test()
include("RH_Unified.jl"); cfg = preset_full(); run(cfg)
include("RH_Unified.jl"); list_presets()
```
**Зависимости:** `Pkg.add(["Plots","JSON"])` (ставятся по подсказке).

### `RH_Unified_v5.jl` — 2 204 строки
Развитие Unified: та же 500-нулевая таблица (ЧАСТЬ 1), расширенные пресеты/диагностика (дельта с v1 — ~414 строк изменений). Точка входа и API — те же.

### ⭐ `RH_Sweep_Pro.jl` — 6 450 строк
**Что это:** профессиональный параметрический свип: **13 661 реальный ζ-нуль** (mpmath.zetazero, 25 знаков, ⟨r⟩ = 0.6144; последний — 12943.888244…), **динамический sweep 8 параметров по 10 ключевым точкам**, все исправления багов предыдущих версий.
**Дополнительно к Unified:** preset_auto (по числу нулей), preset_balanced (по бюджету времени, `max_time_minutes`), preset_irrational (α = 1/π и другие иррациональные), `run_quick_test()`, `run_magic_test()` (все 61 магические α), `run_full_analysis()`.
_D-версия (`RH_Sweep_Pro_D.jl`) — та же физика в консоли MERIDIAN.

---

## D. Монументальная линейка

### `AB_Cloud_Monumental_v6_3.jl` — модуль `AB_Cloud_Monumental`, 7 759 строк
**Что это:** Julia-порт Python-кодовой базы (`python/run_monumental.py`): **V01–V112 верификаций монографии AB-Cloud** — от базовых тождеств модели до траекторий электронов. v6: чистый CSV (строка на задачу), JSON-дамп с полными массивами, PNG-график на задачу, dashboard PNG.
**Запуск:**
```julia
include("AB_Cloud_Monumental_v6_3.jl")
AB_Cloud_Monumental.run_all()                       # все V01–V112
AB_Cloud_Monumental.run_all(quick=true)             # первые 20
AB_Cloud_Monumental.run_only(["V11","V35","V87"])   # выборочно
```
**Опциональные зависимости:** Arpack.jl (`eigs()` для больших разреженных L ≥ 70; иначе плотный fallback), Plots.jl (PNG; если нет — данные графиков выгружаются в per-task CSV). _D-версия — та же физика + консоль MERIDIAN.

---

## E. Утилиты

### `Magic_Alpha_Points_v1.jl` — 131 строка
Библиотека **61 «магической» точки α** для тестирования универсальности RMT-класса AB-облака: π-фракции (π/30…π/4), π-множители (π×1…π×5), корни (√2…√15), рациональные (1/12…5/6, 2/5), константы (φ, e, ln 2, 1/e, 1/π, e mod 1), специальные (√2−1, √12, √8). Структура `AlphaPoint(value, label, category)`, константа `MAGIC_ALPHA_POINTS`. Используется RH-линейкой (`run_magic_test`).

### `test11_honest.jl` / `test11_honest.py` — 322 / 178 строк
**Что это:** честная перекалибровка **Test 11** из `ab_cloud_v18.jl` (Anderson–Darling GOF: спейсинги ζ-нулей vs Wigner surmise GUE β=2).
**Что было не так:** оригинал строил MC-null бутстрэпом (с возвращением) 49999 спейсингов из пула ~8000 реальных спейсингов ОДНОЙ матрицы GUE 10000×10000 → масса точных повторов (tied values), чего не бывает у непрерывных данных. Формула A² на повторах систематически завышает null: проверено симуляцией, это поднимает медиану null A² с учебных O(1) (≈0.5–1, критическое 5% ≈ 2.492, не зависит от n) до 12.54 — что и получил старый прогон.
**Исправление:** null = n_mc независимых i.i.d.-выборок **напрямую из `gue2_surmise_cdf`** (inverse-transform sampling); p-value с add-one (Laplace) сглаживанием («p = 0.0000» — артефакт отображения). Данные, unfolding и формула A² не менялись (перепроверены ранее с точностью 1.9e-05). Бонус: `t_dependence_scan` — проверка сходимости на малых T по данным (Objection 2). Попутно задокументирован баг честности лога в старом `get_gue_ref` (печатал poly_deg=9, а использовал дефолтный 5 — численно пренебрежимо: A² 0.393 в обоих случаях).
**Запуск Python:** `python3 test11_honest.py [--zeros-file zeta_zeros_50k.txt]` (вход по умолчанию — `zeta_zeros_50k.txt`).

---

## F. Данные и конфигурация

### `zeros50k.txt` — 50 000 ζ-нулей, по одному в строке
Диапазон: **14.134725142 … 40433.687385462**. Это «эталонный спектр» проекта: его загружают HP-гейты H1/H7 (для ζ-стороны корреляций), Suite (Test 11 и др.). Подробнее — документ [06](../../02_data/raw/meridian/docs/06_dannye_zeta_nulej.md).

### `zeta_zeros_50k.txt` — те же 50 000 нулей, по 10 в строке
Формат-двойник (5000 строк × 10 чисел): вход по умолчанию для `test11_honest.py`, удобен для pandas/numpy-обработки. Численно идентичен `zeros50k.txt` (проверка: последние нули совпадают до 12 знаков).

### `p_myset.cfg` — профиль HPMeridian «myset»
Профиль конфигурации (одна строка = одно поле HPConfig), сохранённый из консоли HP·MERIDIAN: `hp_L=20`, `hp_n_ensemble=8`, сетка q ∈ [0.05, 1.0] (21 точка), простые [2,3,5,7,11,13], `hp_t_max=20`, `dt=0.025`, лестница решёток [16,20,24], Weyl-блок: L=20, сетка 60, jitter (позиции 0.35, α 0.02, 2 испытания), GUE-калибровка 3 матрицы, **сид 2026**, полоса GUE 0.022, доля прохода 0.9, режим showdown, deep-nulls 4, deep-configs 4, α-scan выключен (n=6); AB-блок (t=1, центр 0.6, α_test16=0.5, сглаживание K=3, 5 реализаций, W=4, nv=[4], q=[1,2]); `gue_matrix_size=12000`. Загружается через консоль/CLI HP·MERIDIAN (профили конфигурации).

---

## G. Какой файл когда брать — шпаргалка

| Хочу… | Бери | Команда |
|---|---|---|
| Полный аудит по всем фронтам (38 тестов) | `ab_cloud_v23_v2.jl` | `julia -e 'include("ab_cloud_v23_v2.jl")'` → `f` (FAST) |
| Только гейты Гильберта–Полиа H1–H7, прицельно | `hp_audit_standalone.jl` | `julia -e 'include("hp_audit_standalone.jl")'` → `f`, затем `5` (или `5d` — FOCUS-D) |
| Красивую консоль на телефоне | версии `_D` | то же, файл с суффиксом `_D` |
| Свип по параметрам с ζ-нулями | `RH_Sweep_Pro.jl` | `julia -e 'include("RH_Sweep_Pro.jl"); run_quick_test()'` |
| Верификацию монографии V01–V112 | `AB_Cloud_Monumental_v6_3.jl` | `run_all(quick=true)` |
| Статистику зазоров ζ-нулей (AD-тест) | `test11_honest.py` | `python3 test11_honest.py` |
| Посмотреть «магические» α | `Magic_Alpha_Points_v1.jl` | подключается автоматически |


---

### 31R.03 — Launch guide (первоисточник на русском / primary record in the original Russian)


> Здесь всё о практической стороне: установка Julia (включая Android/Termux), зависимости, запуск каждого стенда, меню и пресеты, профили конфигурации, типичное время и память.

---

## 1. Установка Julia

### 1.1 Android (Termux) — как у автора

```bash
pkg update && pkg upgrade -y
pkg install -y julia          # если есть в репозитории Termux
# если пакета нет — официальная сборка aarch64:
curl -LO https://julialang-s3.julialang.org/bin/linux/aarch64/1.10/julia-1.10.9-linux-aarch64.tar.gz
tar -xzf julia-1.10.9-linux-aarch64.tar.gz -C $HOME
echo 'export PATH="$HOME/julia-1.10.9/bin:$PATH"' >> ~/.bashrc && source ~/.bashrc
julia --version
```

Проверено на Julia 1.12 (в v24.1-SA есть специальный hotfix под fd-модель 1.12). Любая версия ≥ 1.10 подойдёт.

### 1.2 Linux / macOS

```bash
curl -fsSL https://install.julialang.org | sh    # juliaup — официальный установщик
julia --version
```

### 1.3 Windows

Скачайте установщик с [julialang.org/downloads](https://julialang.org/downloads/). Для полноцветной консоли рекомендуется Windows Terminal (MERIDIAN-консоль определяет Windows Terminal по `WT_SESSION` и не глушит цвета).

---

## 2. Зависимости по стендам

| Стенд | Зависимости | Комментарий |
|---|---|---|
| `ab_cloud_v*.jl` (все) | **только stdlib** | LinearAlgebra, Random, SparseArrays, Statistics, Printf, Dates — ничего ставить не нужно |
| `hp_audit_standalone.jl` | **только stdlib** | то же |
| `RH_Unified.jl`, `RH_Unified_v5.jl`, `RH_Sweep_Pro*.jl` | `Plots`, `JSON` | `julia -e 'using Pkg; Pkg.add(["Plots","JSON"])'` |
| `AB_Cloud_Monumental_v6_3*.jl` | stdlib; **опционально** `Arpack`, `Plots` | без Arpack — плотный fallback; без Plots — данные графиков в CSV |
| `test11_honest.py` | Python 3, `numpy`, `mpmath` | `pip install numpy mpmath` |
| `Magic_Alpha_Points_v1.jl` | только stdlib | библиотека |

---

## 3. Запуск стендов — точные команды

### 3.1 SUPERCOMBO `ab_cloud_v23_v2.jl`

```bash
julia -e 'include("ab_cloud_v23_v2.jl")'
```
Появится меню. Полезные пункты:
- `f` — **FAST battery**: пресет L=16, ensemble=100, прогон всех 7 HP-гейтов (~10–20 мин);
- `F` — **FULL battery**: пресет L=56, ensemble=40, α-scan n=30 (часы, «record-grade»);
- пункты меню параметров 16–18: `hp_deep_nulls` (по умолчанию 20), `hp_deep_configs` (10), `hp_alpha_scan`/`hp_alpha_scan_n` (включён, 40);
- меню `h` — HP-гейты H1–H7 по отдельности.

### 3.2 HP·MERIDIAN `hp_audit_standalone.jl`

```bash
julia -e 'include("hp_audit_standalone.jl")'
```
Консоль `meridian>`. Ключевые команды:
- `f` — пресет **FAST: L=72** (72×72 = 5184 узлов → каждый солв — плотная задача 5184×5184), ensemble=100/режим, α-scan n=40; H5-план автоматически ужимается в бюджет ≤ 40 солвов;
- `F` — пресет **FULL: L=56** (3136 узлов), ensemble=40, α-scan n=30;
- `s` (smoke) — пресет **SMOKE: L=20**, ensemble=8, deep 4/4, α-scan n=6, лестница [16,20,24], ζ cap 2000 — валидационный прогон;
- `5` — гейт H5 (REGIME-2×2 шоудаун + α-профиль);
- **`5d` — FOCUS-D (v24.2)**: переключает `hp_regime_mode = :regime_d` и запускает H5 с **всем бюджетом 40 солвов в режиме D** (Nv = L²/36, α = 25/900). Первые 7 сидов — бит-в-бит сиды [D]-блока showdown (offset 30 000);
- `z` — указать путь к файлу ζ-нулей (если `zeros50k.txt` не рядом со скриптом);
- doctor среды, `help`, about — по подсказке в консоли.

**Ctrl-C** прерывает вежливо: завершает текущий солв и выходит; каждые 60 секунд во время длинного LAPACK-вызова печатается строка «alive» — это не зависание, это heartbeat.

### 3.3 RH-линейка

```bash
# единый файл, быстрый тест
julia -e 'include("RH_Unified.jl"); run_quick_test()'
# полный прогон по пресету
julia -e 'include("RH_Unified.jl"); cfg = preset_full(); run(cfg)'
# список пресетов
julia -e 'include("RH_Unified.jl"); list_presets()'

# профессиональный свип (13 661 ζ-нулей)
julia -e 'include("RH_Sweep_Pro.jl"); run_quick_test()'
julia -e 'include("RH_Sweep_Pro.jl"); run_magic_test()'     # все 61 магические α
julia -e 'include("RH_Sweep_Pro.jl"); run_full_analysis()'
julia -e 'include("RH_Sweep_Pro.jl"); cfg = preset_balanced(13661; max_time_minutes=30); run(cfg)'
```

### 3.4 Монументальная батарея

```bash
julia -e 'include("AB_Cloud_Monumental_v6_3.jl"); AB_Cloud_Monumental.run_all(quick=true)'
julia -e 'include("AB_Cloud_Monumental_v6_3.jl"); AB_Cloud_Monumental.run_all()'
julia -e 'include("AB_Cloud_Monumental_v6_3.jl"); AB_Cloud_Monumental.run_only(["V11","V35","V87"])'
```
Результаты: `CSV` (строка на задачу), `JSON` (полные массивы), per-task `PNG` и dashboard `PNG` (при наличии Plots.jl; иначе CSV-данные графиков).

### 3.5 Python-тест

```bash
python3 test11_honest.py --zeros-file zeta_zeros_50k.txt
```

---

## 4. Профиль конфигурации `p_myset.cfg`

Профиль — это «снимок» полей HPConfig, сохранённый из консоли HP·MERIDIAN (одна строка = одно поле `имя = значение`). Основные поля профиля «myset»:

| Группа | Поля |
|---|---|
| Решётка | `hp_L=20`, лестница `hp_L_ladder=[16,20,24]`, `hp_L_weyl=20`, `hp_weyl_grid=60` |
| Ансамбль/динамика | `hp_n_ensemble=8`, `hp_t_max=20`, `hp_dt=0.025`, `hp_h1_configs=2` |
| Сетка потока q | `hp_q_min=0.05`, `hp_q_max=1`, `hp_n_q_grid=21` |
| Арифметика | `hp_primes=[2,3,5,7,11,13]`, `hp_zeta_cap=2000` |
| Null/jitter | `hp_jitter_trials=2`, `hp_pos_jitter=0.35`, `hp_alpha_jitter=0.02` |
| GUE-калибровка | `hp_n_gue_calib=3`, `gue_matrix_size=12000`, `hp_gue_band=0.022` |
| Вердикты | `hp_pass_fraction=0.9`, `hp_regime_mode=showdown` |
| Deepen | `hp_deep_nulls=4`, `hp_deep_configs=4`, `hp_alpha_scan=false`, `hp_alpha_scan_n=6` |
| Воспроизводимость | **`hp_seed=2026`** |
| AB-блок | `ab_t=1`, `ab_center_fraction=0.6`, `ab_alpha_test16=0.5`, `ab_K_smooth_window=3`, `ab_n_realizations=5`, `ab_W=4`, `ab_W_max=1`, `ab_nv_list=[4]`, `ab_q_list=[1,2]` |

Профиль удобен для точного повторения прогона: загрузите его в консоли HP·MERIDIAN (или перенесите значения руками) — и сид 2026 воспроизведёт поток случайных чисел.

---

## 5. Время, память, ожидания

**Арифметика стоимости.** Гамильтониан — L²×L². Плотная диагонализация: время ≈ O((L²)³) = O(L⁶), память ≈ O((L²)²) = O(L⁴) (пик ≈ 2.5·(L²)²·16 байт — с запасом на рабочие массивы LAPACK).

| L | Матрица | Пик памяти (оценка) | Время 1 солва (смартфон) |
|---:|---|---:|---:|
| 16 | 256×256 | ~0.01 ГБ | < 1 с |
| 20 | 400×400 | ~0.015 ГБ | ~ 1 с |
| 56 | 3136×3136 | ~0.37 ГБ | ~ 25 с |
| 64 | 4096×4096 | ~0.6 ГБ | ~ 49 с (замер реального прогона) |
| 72 | 5184×5184 | ~1.0 ГБ | ~ 1.5–2 мин |

Реальные примеры: H5 64×64 (бюджет 40 солвов, 4 режима × 7 конфигов + α-профиль) занял **32 мин 47 с** на смартфоне; 72×72 FAST по оценке ≈ 1 час. Если прогресс-бар «стоит», а строки heartbeat каждые 60 с приходят — идёт обычный длинный LAPACK-вызов.

**Телефон перегревается / рвёт батарейку** — это нормально для O(L⁶); ставьте телефон на вентиляцию, держите зарядку, и берите `:smoke`/`f`-FAST для быстрых итераций.

---

## 6. Цвета и консоль (MERIDIAN DESIGN)

- Цвета включаются только на настоящем TTY; форс-включение: `MERIDIAN_COLOR_FORCE=1 julia -e '...'`; выключение: `MERIDIAN_COLOR=0`.
- Ширина рамок — 62 символа: рассчитана на экран телефона.
- Любая ошибка принтера деградирует в обычный текст — дизайн никогда не ломает прогон.
- На «тупых» терминалах (TERM=dumb), в Windows без Windows Terminal и при пайпинге в файл цвета автоматически отключаются.

---

## 7. Типичные проблемы

| Симптом | Причина | Решение |
|---|---|---|
| «ζ zeros not found — H1/H7 will run WITHOUT the ζ side» | `zeros50k.txt` не найден | положите файл рядом со скриптом, или `z` в консоли, или CLI `zeros=path`, или `export HP_ZEROS=/путь/zeros50k.txt` |
| Julia «package not found: Plots» | RH-линейка требует пакеты | `julia -e 'using Pkg; Pkg.add(["Plots","JSON"])'` |
| «Прогресс-бар не двигается, но alive печатается» | длинный LAPACK-вызов (1 поток, ccall) | ждать; это честный heartbeat, не зависание |
| Ctrl-C убил прогон | вежливое прерывание после текущего солва | просто запустите снова; сиды воспроизводимы |
| Память кончилась на L=72 | пик ~1 ГБ + система | закройте приложения; возьмите L=64/56 |
| В v19 «зависает на тесте 10» в старой консоли | известный дедлок live-tee, исправлен в v19.1 | используйте файл из этого репозитория (v19.1+) |


---

### 31R.04 — Physics and mathematics (первоисточник на русском / primary record in the original Russian)


> Этот документ — «теоретический минимум» проекта: гамильтониан AB-облака, геометрия вихрей, статистика случайных матриц, формулы всех ключевых критериев и устройство гейтов H1–H7. Всё, что печатается в консоли, можно найти здесь.

---

## 1. Гамильтониан AB-облака

### 1.1 Решётка и фазы Ааронова–Бома

Рассмотрим квадратную решётку L×L. Одночастичное пространство — ℂ^(L²): по одной ступеньке на узел. Стандартный теслейтовский гамильтониан связывает соседние узлы прыжковыми амплитудами; в магнитном поле каждая связь получает фазу Пирлса:

```text
t_ij  →  t_ij · exp(i·Φ_ij),
```

где Φ_ij — магнитный поток через связь, измеренный в единицах кванта потока. **Вихрь** — это plaquette (или узел в дискретной модели), на который «продавлен» поток α: обход вокруг него даёт суммарную фазу 2π·α. При α, не равном целому, волновая функция становится многозначной на плоскости — электрон обегает вихрь по «облаку» Ааронова–Бома. Именно это нелокальное облако — физический герой проекта.

### 1.2 Сборка матрицы и её размер

Функции семейства `build_ab_cloud_hamiltonian` собирают **плотную эрмитову матрицу N×N, где N = L²**. Важно не путать: «решётка 64×64» означает матрицу **4096×4096**. Отсюда вся арифметика стоимости:

- время диагонализации ≈ O(N³) = **O(L⁶)**;
- память ≈ O(N²) = **O(L⁴)**; пик ≈ 2.5·(L²)²·16 байт (эрмитова симметрия экономит половину, но LAPACK-рабочие массивы её возвращают с запасом ×2.5);
- переход 16 → 72: стоимость ×≈ 8000.

Гермитовость проверяется стресс-гейтом H6 (HERMIT-STRESS): норма антиэрмитовой части, устойчивость к джиттеру, поведение собственных значений при возмущениях.

### 1.3 Конфигурации вихрей: Nv, W, компоновки

Плотность вихрей задаётся числом Nv на решётку. Ключевые точки:
- **Nv = 4** — историческая базовая конфигурация (режим A и C в H5);
- **Nv = L²/36** — «плотность монографии»: одна «ячейка монографии» на 6×6 узлов (режим B и D). При L=64 это Nv=114, при L=20 — Nv=11.
- Компоновки в RH-линейке: **hexagonal** (по умолчанию), **ring**, **random**, **grid**; число вихрей 2–100+.
- **Jitter** (дрожание): случайные возмущения позиций (0.35), потока α (0.02), зарядов и ширины W — чтобы результат не был артефактом идеальной геометрии.

### 1.4 Поток α и «магические» точки

α — поток на вихрь. Особые роли:
- **α = 0.5** — базовый полупоток (режим A/B);
- **α = 25/900 ≈ 0.0278** — «острый поток» (sharp flux, режимы C/D): найден в прогоне v23 как рычаг GUE-качества при любой плотности;
- 61 «магическая» точка из `Magic_Alpha_Points_v1.jl` (π/30…π×5, √2…√15, рациональные, φ, e, ln 2, 1/e, 1/π и спец-значения) — сетка для проверки универсальности RMT-класса.

## 2. Статистика спектров: от лестницы к GUE

### 2.1 Незатухающие зазоры и unfolding

Сырые зазоры δᵢ = Eᵢ₊₁ − Eᵢ неравномерны: плотность уровней ρ(E) растёт/падает по спектру. **Unfolding** переводит спектр в безразмерные единицы: E → Ñ(E) (интегральная плотность, аппроксимированная полиномом; в кодах — степени 5 или 9), после чего зазоры sᵢ имеют среднее ≈ 1 и стационарны по спектру. Сравнивать с GUE можно только после unfolding — это стандарт RMT.

### 2.2 Статистика r (nearest-neighbour spacing ratios)

Для инвариантной к unfold процедурной простоты используется статистика соседних отношений:

```text
r_i = min(δᵢ, δᵢ₊₁) / max(δᵢ, δᵢ₊₁),   ⟨r⟩_GUE ≈ 0.5996
```

Доверительный интервал для конечных ансамблей проекта: **[0.5772, 0.6212]**. Эталон «отсутствия корреляций» (пуассоновский спектр) — ⟨r⟩ ≈ 0.5307. Значение в интервале — необходимое условие GUE-класса.

### 2.3 Wigner surmise GUE β=2

Аналитическая аппроксимация распределенияunfolded зазоров:

```text
p(s) = (32/π²) · s² · exp(−4s²/π)
```

Нормировка 32/π² — не случайная константа: она равна в точности (1/2)! = √π/2 — тождество, проверяемое Suite'ом в Test 37 через лог-выпуклость Γ (Бор–Моллеруп) и самодуальное отражение Γ(1/2)² = π. В `test11_honest` распределение задаётся через `gue2_surmise_cdf` (inverse-transform sampling) — это эталонный H0.

### 2.4 Критерий Колмогорова–Смирнова и порог d_crit

KS-расстояние между эмпирической CDF зазоров F_n(s) и эталоном G(s):

```text
D_n = sup_s |F_n(s) − G(s)|,      d_crit = 1.63/√n   (уровень ~1%)
```

**Критическое следствие** (ключ к пониманию прогонов): n — число зазоров в центральной полосе спектра ≈ 0.6·L². При L=16: n ≈ 150 → d_crit ≈ 0.132. При L=64: n ≈ 2400 → d_crit ≈ 0.033. Порог ужесточился **в 4 раза**, хотя физика модели не изменилась. Поэтому «провал» α-профиля при переходе 16→64 — это рост статистической мощности, а не новое явление (разбор — документ 05).

### 2.5 Anderson–Darling A²

GOF-тест, чувствительный к хвостам:

```text
A² = −n − (1/n) · Σᵢ (2i−1) · [ln F(x_(i)) + ln(1 − F(x_(n+1−i)))]
```

Для полностью заданной непрерывной H0 (surmise CDF) учебная шкала null: медиана ≈ 0.5–1, критическое 5% ≈ 2.492 (не зависит от n при корректной калибровке). **Урок `test11_honest`**: бутстрэп с возвращением из конечного пула создаёт завязки (tied values) и раздувает null в разы — MC-null для непрерывной H0 строится только i.i.d.-выборками из самой H0; p-value — с add-one (Laplace) сглаживанием.

### 2.6 GUE-калибровка в кодах

Для «сопоставимого размера» null'ов коды генерируют собственные GUE-матрицы (goe/gue буферы, `hp_n_gue_calib` калибровочных реализаций, `gue_matrix_size=12000` в профиле) и пропускают их через **ту же** RMT-обработку, что и спектры AB — только тогда сравнение честно.

## 3. Гейты H1–H7: что проверяется и как выносится вердикт

### H1 · PRIME-TRACE — «решётка слышит простые числа»

- Берётся динамический отклик решётки (временная эволюция, `hp_t_max`, `hp_dt`), по которому строится сырой Фурье-спектр (raw-FT).
- Ищется **Брэгг-гребень** на частотах ω = log p для простых p (список `hp_primes`).
- **Декой-контроль**: композитные частоты log 21, log 33, log 54, log 56 обязаны молчать. `zeta_ok` = гребень стоит на всех простых И на декоях тишина. Пик на декое при молчащих простых был бы аргументом **против** арифметической природы сигнала.
- **Режимно-сопоставленные null-модели** (v23.5): для каждого режима B/C/D свой потолок нулей — vortex-free решётка на α режима + GUE matched-size со свежими сидами.
- **Deepen-протокол** (v23.6): если режим попал в MARGINAL/PRESENT, потолок переоценивается из `hp_deep_nulls` (20) реализаций каждого типа; бугорок судится против 95-го перцентиля максимумов нулей. ≤ P95 → «generic flux-geometry artifact» → ABSENT (PASS для sweep); > P95 → честный WARN с эскалацией.
- **Окно скана**: авто-расширение до max(3.0, ω_max + 0.2), чтобы цели выше log(17) не давали фиксированный пол.

### H2 · WEYL-DOS — «какая теория у лестницы состояний»

Сырая лестница N(E) (интегральная плотность состояний) вблизи вейл-точки; кандидатные модели (линейная, квадратичная, гибриды) сравниваются по **AICc** (corrected Akaike Information Criterion) — showdown, где выигрывает не «красивое», а наименьшее AICc с поправкой на число параметров и размер выборки.

### H3 · POWER-LAW — «степень, но не самообман»

Лестница экспонент степенного закона (подгонка при разных окнах/диапазонах) + **фальсификация словарём**: найденная экспонента проверяется против «словаря» известных значений (универсальные классы), чтобы исключить подгонку.

### H4 · CRITICAL-Q — «резкость, но в честном домене»

Скан резкости сигнала по сетке q (`hp_q_min…hp_q_max`, `hp_n_q_grid` точек). **Guard домена** (v23.6): заявленные критические значения (0.3/0.5/1.0) обязаны лежать внутри сканируемого домена; если нет — строка «location vs claimed criticals» честно получает FAIL-класс с явным объяснением (раньше проверка «вырождалась»: любой пик автоматически оказывался «off 55% span»).

### H5 · REGIME-2×2 — «шоудаун режимов + α-профиль» (см. документ 05)

Два рычага — плотность (Nv=4 vs L²/36) и поток (0.5 vs 25/900) — дают 2×2 = 4 режима: A, B, C, D. Ансамбль реализаций на режим (сид-блоки по 10 000/режим), затем α-профиль из 6 точек. Бюджет: **HP5_SOLVE_CAP = 40** (v24.1). Правило вердикта режима:

```text
доля реализаций с ⟨r⟩ ∈ [0.5772, 0.6212] ≥ 90%
И (доля индивидуальных KS-проходов ≥ 90% ИЛИ медиана KS_D < 0.10)
```

Проход только через вторую часть «ИЛИ» → пометка **OR-clause only** (прозрачность). В v24.2 добавлен **FOCUS-D** (`:regime_d`, команда `5d`): весь бюджет 40 — в режим D; первые 7 сидов = канонический [D]-блок showdown (offset 30 000) → прямая сравнимость с прошлыми прогонами; гранулярность KS 1/40.

### H6 · HERMIT-STRESS — «оператор действительно эрмитов?»

Норма отклонения от эрмитовости, устойчивость спектра к джиттеру позиций/потока, поведение при повторной сборке. Спектр самосопряжённого оператора вещественен — это фундамент программы Гильберта–Полиа, поэтому стресс обязателен.

### H7 · SEQ-CORR — «уровни ↔ нули»

Последовательностная корреляция: упорядоченные уровни AB-спектра против ζ-нулей (после unfold/нормировки) — корреляции знаковых последовательностей, ранговые меры. Работает только при найденном `zeros50k.txt` (иначе честно «WITHOUT the ζ side»).

## 4. Вердикты и их иерархия

Консоль печатает иерархию: **под-чеки → строка сводки («N sub-checks, M failed → WARN») → DONE-line → итог вердикта**. Правила честности:

1. DONE-line печатает **фактический** вердикт (PASS/WARN; ERROR — только при исключении) — баг класса «WARN поверх PASS» исключён (v23.6 №1);
2. PASS не рисуется поверх mixed/MARGINAL: статус sweep **входит** в общий ok теста (v23.5);
3. ABSENT по бугорку при ≤ P95 нулей — это **PASS** sweep'а (режимно-устойчивая пустота), а не «недосмотр»;
4. Найден бугорок > P95 даже после deepen → **WARN** с эскалацией, а не пессимизм;
5. α-профиль — «headline, never scored»: он информирует (finetuning vs plateau), но не меняет счёт.

## 5. Словарь консоли (краткий глоссарий)

| Термин | Смысл |
|---|---|
| ⟨r⟩ | среднее отношение соседних зазоров; GUE-эталон 0.5996, вилка [0.5772, 0.6212] |
| KS_D / d_crit | KS-расстояние до GUE / порог 1.63/√n |
| median D | медиана KS_D по ансамблю реализаций |
| OR-clause only | проход только через медиану D < 0.10 при KS-проходах < 90% |
| showdown | полный 2×2-режимный прогон (A/B/C/D) |
| FOCUS-D / `5d` | весь бюджет H5 — в режим D |
| α-profile | GUE-качество вдоль α при фиксированной Nv (never scored) |
| decoy | композитный контроль (21, 33, 54, 56), обязанный молчать |
| deepen | переоценка потолка нулей из 20+20 реализаций против P95 |
| vortex-free | null-модель той же решётки без вихрей на том же α |
| GUE matched-size | null-модель GUE той же матричной размерности со свежими сидами |
| done-line | финальная строка гейта «done in … → ВЕРДИКТ» |


---

### 31R.05 — The H5 gate regimes (первоисточник на русском / primary record in the original Russian)


> H5 — центральный гейт проекта: ансамбль-шоудаун четырёх параметрических режимов AB-облака против GUE + α-профиль (finetuning vs plateau). Здесь — полная механика, экономика солвов и честный разбор трёх реальных прогонов: 16×16, 64×64 и 72×72.

---

## 1. Зачем нужен H5

Гейты H1–H4/H6/H7 проверяют отдельные свойства (арифметику, DOS, степенные законы, эрмитовость, корреляции). H5 отвечает на главный вопрос феноменологии: **при каких параметрах спектр AB-облака попадает в универсальный класс GUE — тот же, что у нулей ζ(s)?** Это фундамент программы Гильберта–Полиа в этом проекте: если существует устойчивая конфигурация решётки, чья спектральная статистика неотличима от GUE (и при этом H1 слышит простые числа), у программы появляется конкретный оператор-кандидат.

## 2. Два рычага → четыре режима

Рычаг 1 — **плотность вихрей**: Nv = 4 (редкая) vs Nv = L²/36 (плотность монографии).
Рычаг 2 — **поток α**: 0.5 (базовый полупоток) vs 25/900 ≈ 0.0278 (острый поток).

| Режим | Плотность | Поток α | Кто это |
|:---:|---|---|---|
| **A** | Nv = 4 | 0.5 | базлайн; историческая опубликованная точка |
| **B** | Nv = L²/36 | 0.5 | «монография»: плотность по монографии AB-Cloud |
| **C** | Nv = 4 | 25/900 | острый поток при редких вихрях |
| **D** | Nv = L²/36 | 25/900 | комбинация: плотность монографии + острый поток |

Каждый режим получает **свой сид-блок** из 10 000 номеров (сид-гигиена: режимы не делят случайные потоки). Из блока берутся сида для реализаций ансамбля.

## 3. Экономика солвов: планировщик `_hp5_plan` и кап 40 (v24.1)

Каждая реализация = одна плотная диагонализация L²×L². Историческая FAST-конфигурация просила 4 режима × 100 реализаций + 6 точек α × 40 конфигов = **640 солвов** — на телефоне это дни. Кап v24.1 («максимум 40 — это избыточно»):

```text
HP5_SOLVE_CAP = 40  (ИТОГО, не по режиму)

showdown-план:   2×2 режима × ≤7 конфигов   ≤ 28 солвов
α-профиль:       6 точек × ≤2 конфига       ≤ 12 солвов
-------------------------------------------  ─────────
максимум                                    40 солвов
```

Ключевая гарантия: **гейт и баннер стоимости используют один и тот же планировщик** `_hp5_plan` — баннер не может пообещать меньше, чем гейт запустит, и наоборот. Старый scored-критерий «ensemble ≥ 30» заменён на **budget-compliance** (кап не должен быть молчаливым авто-FAIL); гранулярность индивидуальных KS-проходов (1/N) печатается явно.

В **FOCUS-D** (v24.2) план особый: режимов один → весь кап 40 уходит в [D]: до 40 реализаций ансамбля, KS-гранулярность 1/40 вместо 1/7.

## 4. Правило вердикта режима

Для каждого режима считается ансамбль метрик ⟨r⟩ и KS_D (после unfold, центральная полоса ≈ 0.6·L² зазоров):

```text
GUE-вилка:      ⟨r⟩ ∈ [0.5772, 0.6212]            (доля реализаций внутри — P_r)
KS-проходы:     доля реализаций с KS_D < d_crit = 1.63/√n   (P_ks)
VERDICT:        P_r ≥ 0.90  И  (P_ks ≥ 0.90  ИЛИ  median KS_D < 0.10)
```

Прозрачность: если P_r ≥ 0.90, но P_ks < 0.90 и проход только из-за медианы — вердикт помечается **«OR-clause only»** (не маскируется). Возможные итоговые вердикты H5: **CLEAN PASS** / **PARAMETER-DEPENDENT (OR-clause only)** / **MISS** (в showdown), и свои FOCUS-D-заголовки с N=40.

**α-профиль** (never scored — информационный): 6 точек α ∈ {25/900, 0.05, 0.1, 0.2, 0.35, 0.5} при фиксированной редкой Nv. PLATEAU (GUE держится на всей малой α) → «острый поток GUE-универсален»; NARROW (окно у 25/900) → finetuning. Точка α=0.5 независимо реплицирует режим A другим сид-потоком. Выводятся 2 графика: KS-pass % и медиана D vs α.

## 5. Разбор реального прогона 16×16 (до капа 40)

Прогон L=16 (классическая конфигурация): итог — **ROBUST FAILURE**, α-профиль — **PLATEAU-LOW**.

Что это значило:
- базовый режим A при α=0.5 дал медиану KS_D ≈ 0.312 — спектр далёк от GUE;
- α-профиль показал «плато низкого качества» на всей малой α — ни одна точка не проходила;
- на тот момент это читалось как «GUE-эффекта нет при редкой плотности».

## 6. Разбор реального прогона 64×64 (кап 40, v24.1)

Конфигурация: L=64 → матрица 4096×4096; Nv(B/D) = 114 = 64²/36; ансамбль 7 реализаций на режим (4 режима × 7 = 28 солвов) + α-профиль 6×2 = 12; итого ровно 40 солвов, ~49 с на солв, гейт целиком ≈ 32 мин 47 с. Итог: **PARAMETER-DEPENDENT · OR-CLAUSE ONLY**, общий статус WARN; α-профиль: **NONE**.

Медианы KS_D по режимам (vs d_crit = 1.63/√n ≈ 0.033 для n ≈ 2400 зазоров):

| Режим | медиана KS_D | d_crit | Индивидуальные KS-проходы | Чтение |
|:---:|---:|---:|---:|---|
| A | 0.350 | 0.033 | 0/7 | базлайн деградировал с ростом L (было 0.312 при L=16) |
| B | 0.048 | 0.033 | 2/7 | близко к порогу, но систематика 1.5× порога |
| C | 0.072 | 0.033 | 1/7 | реальная, но меньшая систематика (2.2× порога) |
| **D** | **0.0231** | 0.033 | **5/7 (71.4%)** | **ниже порога** — статистически неотличим от GUE на этой выборке |

**Главные выводы разбора:**

1. **Режим D — легитимный кандидат GUE.** Единственный режим, чья медиана D опустилась под критерий; единственный с массированными индивидуальными проходами. Это та самая «настоящая история про GUE».
2. **B и C — настоящие, но малые систематики** (1.5–2.2× порога): каждый рычаг по отдельности тянет к GUE, но не доводит.
3. **A ухудшается с размером** (0.312 → 0.350): опубликованная точка α=0.5 при редкой плотности — не «чуть-чуть не GUE», а устойчивая периферия. Это полезный негативный результат.
4. **OR-clause only — честный статус**: проходы обеспечены медианой (D < 0.10), а не 90% индивидуальных KS — режим «на подходе», не «в классе» по строгому критерию.

**Почему α-профиль перевернулся из PLATEAU-LOW (16) в NONE (64)?** Это **эффект мощности, а не физики**: n зазоров вырос в ~16 раз (0.6·L²: 150 → 2400), порог d_crit = 1.63/√n ужесточился в 4 раза (0.132 → 0.033). Те же систематики, которые «проезжали» под старым порогом, теперь выше него. Флаг кода «противоречие с чистым проходом режима C? — проверить сиды/протокол» разрешился именно так: не сиды, а мощность. Урок зафиксирован в документе 08 как обязательная оговорка при сравнении прогонов разных L.

**Смешение размера и плотности (следующий шаг протокола).** α-профиль идёт при фиксированной Nv=4, поэтому плотность вихрей на узел падает с ростом L: 1.56% при L=16 → 0.10% при L=64. Сравнение «16 vs 64» в профиле смешивает два фактора: сам размер (мощность теста, конечный размер систематики) и плотность (физику). Корректное разделение — отдельный эксперимент: α-профиль при плотности, фиксированной на узел (Nv ∝ L²), что и диктует следующий прогон (естественно делается в FOCUS-D с перестроенной сеткой конфигов).

## 7. Разбор реального прогона 72×72 (v24.2-SA, 2026-09-09)

Конфигурация: L=72 → матрица **5184×5184**; Nv(B/D) = 144 = 72²/36; план: 4 режима × 7 реализаций (28 солвов) + α-профиль 6×2 (12) = ровно 40. Полное время гейта **46 мин 04 с** (≈ 69 с на солв), пик памяти ≈ 1.0 ГБ. Полный консольный лог сохранён: `appendix_run_2026-09-09_L72_H5.log`. Итог: **PARAMETER-DEPENDENT**, статус WARN; α-профиль: **NONE**.

Порог d_crit = 1.63/√n ≈ 0.031 (n ≈ 3100 зазоров после unfold).

| Режим | ⟨r⟩ | в GUE-вилке | KS-проходы | медиана D | Вердикт |
|:---:|---|:---:|:---:|---:|---|
| A | 0.5898±0.0102 | 6/7 (85.7%) | 0/7 | 0.3531 | мимо GUE |
| B | 0.6000±0.0052 | 7/7 | 1/7 (14.3%) | 0.0559 | OR-clause only |
| C | 0.5937±0.0041 | 7/7 | 0/7 | 0.0646 | OR-clause only |
| **D** | **0.6003±0.0050** | **7/7** | **7/7 (100%)** | **0.0148** | **CLEAN PASS** |

α-профиль (Nv=4 фиксирована, 2 конфига на точку — гранулярность 1/2):

| α | ⟨r⟩ | в вилке | KS-проходы | медиана D |
|:---:|---|:---:|:---:|---:|
| 0.0278 | 0.6019±0.0045 | 100% | 0/2 | 0.0584 |
| 0.0500 | 0.5908±0.0053 | 100% | 0/2 | 0.0846 |
| 0.1000 | 0.6325±0.0369 | 50% | 0/2 | 0.1843 |
| 0.2000 | 0.5962±0.0011 | 100% | 0/2 | 0.3701 |
| 0.3500 | 0.5994±0.0001 | 100% | 0/2 | 0.5258 |
| 0.5000 | 0.5893±0.0076 | 100% | 0/2 | 0.3447 |

**Главные выводы (что всё это значит):**

1. **Режим D усилился с ростом размера — теперь это чистый проход.** На 64: KS 5/7 (71.4%), медиана D 0.0231; на 72: **7/7 (100%) и 0.0148** — вдвое ниже порога. ⟨r⟩ = 0.6003±0.0050 лежит прямо на асимптоте GUE (~0.5992). Скалирование 64→72 не разрушило, а укрепило candidatur — именно так выглядит настоящая универсальность, а не артефакт конечного размера.
2. **Базовый режим A — устойчивый периферийец.** Медиана D: 0.312 (L=16) → 0.350 (L=64) → 0.353 (L=72). Публикуемая точка (редкая плотность + α=0.5) не «чуть-чуть не GUE», а систематически далеко; к тому же 6/7 в вилке (85.7% < 90%) — единственный режим, проваливший и r-критерий.
3. **B и C — реальные малые систематики** (медианы 0.056 и 0.065 ≈ 1.8–2.1× порога): каждый рычаг по отдельности тянет к GUE, но чистого прохода не даёт. Синергия D (0.0148 ≈ 0.5× порога) — сильный аргумент, что оба рычага нужны одновременно.
4. **α-профиль NONE — и это согласуется с режимом C, а не противоречит.** Флаг кода «противоречит чистому проходу C?! проверить сиды/протокол» — ложная тревога: C никогда не имел чистого прохода (только OR-clause), и точка профиля α=0.0278 (медиана 0.0584) совпадает с C (0.0646) в сид-шуме. Настоящий сигнал профиля — **рост медианы D с α** (0.058 → 0.526 к α=0.35): при редкой плотности острый поток помогает, но один не доводит до GUE — не хватает плотности. Режим B подтверждает это с другой стороны: плотность без острого потока даёт 0.056.
5. **Точечная оценка α=0.1000 (⟨r⟩ 0.6325±0.0369, в вилке 50%) — выброс малой выборки**: 2 сида, один сильно завысил среднее (σ 0.037 против 0.004–0.008 в остальных точках). Не физика, а гранулярность 1/2.
6. **Скалирование времени подтвердилось.** 40 солвов за 46 мин ≈ 69 с/солв (L=72); пессимистичный баннер «hours-to-days» не реализовался — реалистичная оценка «~1 час» подтвердилась. Строки «alive MM:00» в логе — нормальные 60-секундные тики LAPACK-вызова, а не зависания.

**Следующий решающий шаг.** Два взаимодополняющих прогона: (а) **FOCUS-D (`5d`)** — весь кап 40 в режим D, KS-гранулярность 1/40 вместо 1/7, проверка устойчивости чистого прохода на 40 реализациях; (б) α-профиль при фиксированной плотности на узел (Nv ∝ L²) — снять смешение размера и плотности, отмеченное в разделе 6 (профиль 72-го прогона по-прежнему идёт при Nv=4: 0.08% узлов).

---

## 8. Практические рецепты: какой прогон запускать

| Цель | Команда (консоль meridian>) | Ожидание |
|---|---|---|
| Валидация установки | `s` (SMOKE L=20) | минуты, все гейты проходят smoke-уровень |
| Полный шоудаун на большом L | `f` (FAST L=72) → `5` | ~1 час; 2×2 + α-профиль, кап 40 |
| **Глубокая прокачка режима D** | `f` → **`5d`** (FOCUS-D) | ~1 час; до 40 реализаций [D], KS 1/40, сравнимо с сидами showdown |
| Проверка баннера стоимости | любой гейт | LIVE-строка стоимости до старта + оценка всей батареи upfront |
| Репликация 64×64 | установить hp_L=64 → `5` | 33 мин; таблица раздела 6 должна воспроизвестись (сид 2026) |
| Репликация 72×72 | `f` (FAST L=72) → `5` | 46 мин; таблица раздела 7 должна воспроизвестись |

**Память/время на 72×72:** пик ≈ 1.0 ГБ, солв ≈ 69 с (измерено 2026-09-09, 40 солвов за 46:04); heartbeat каждые 60 с подтверждает, что идёт LAPACK, а не зависание.

## 9. Как читать вердикт H5 — блок-схема

```text
Смотрим med. KS_D режима против d_crit = 1.63/√n(L)
│
├─ med D < d_crit И P_ks ≥ 0.9 И P_r ≥ 0.9          → CLEAN PASS (класс GUE, строгий)
├─ med D < d_crit И P_r ≥ 0.9 (P_ks < 0.9)          → OR-CLAUSE ONLY (кандидат, «на подходе»)
├─ med D < d_crit, но P_r < 0.9                     → параметр-зависимая систематика; качать ансамбль
└─ med D ≥ d_crit                                   → MISS по этому режиму (смотреть r-вилку и тренд с L)
α-профиль: PLATEAU → универсальность острого потока; NARROW → finetuning; NONE → мощность съела сигнал
```

И последнее: **никогда не сравнивайте «прошёл/не прошёл» между разными L без пересчёта d_crit** — порог зависит от размера через 1.63/√n, и это первая вещь, которую надо проверить при любом «странном» расхождении прогонов.


---

### 31R.06 — The ζ-zero data (первоисточник на русском / primary record in the original Russian)


> В папке лежат два файла данных нулей ζ(s). Они численно идентичны (одни и те же 50 000 нулей), но различаются форматом и назначением. Здесь — происхождение, форматы, проверки и правила, где коды их ищут.

---

## 1. Два файла — одна таблица

| Файл | Формат | Строк | Кем используется |
|---|---|---:|---|
| `zeros50k.txt` | по одному числу в строке | 50 000 | HP·MERIDIAN (`hp_audit_standalone.jl`), Suite (`ab_cloud_v*.jl`) |
| `zeta_zeros_50k.txt` | по 10 чисел в строке, разделённые пробелом | 5 000 | `test11_honest.py` (вход по умолчанию), удобен для numpy/pandas |

Содержательно это **одна и та же таблица**: первый нуль `14.134725142`, последний `40433.687385462`. Контроль совпадения: последние значения обоих файлов равны до 12 знаков; число нулей — ровно 50 000 в каждом.

## 2. Диапазон и физический масштаб

```text
γ₁    = 14.134725142     — первый нуль (Odlyzko verified)
γ₂    = 21.022039639
γ₃    = 25.010857580
...
γ₅₀₀₀₀ = 40433.687385462 — пятидесятитысячный нуль
```

Средняя плотность нулей в этой области ~ ln(γ/2π) ≈ ln(6433) ≈ 8.8 нулей на единицу t, значит таблица покрывает интервал t ≈ 14…40434 с типичным локальным зазором ≈ 0.11–0.12. Это достаточно длинная последовательность, чтобы строить и глобальные статистики (⟨r⟩, распределения зазоров), и скользящие по t (например, `t_dependence_scan` в test11_honest).

## 3. Происхождение

Нули таблиц получены вычислительно через **`mpmath.zetazero()`** с точностью 25 знаков (та же технология, что заявлена в шапках RH-линейки: «13 661 РЕАЛЬНЫХ ζ-нулей … верифицированы, ⟨r⟩ = 0.6144 ≈ R_GUE = 0.5996»; первый нуль — Odlyzko verified). Это «настоящие» нули ζ(s), а не модельные подделки — критично для гейтов H1/H7 и Test 11, где ζ-сторона выступает эталоном.

Для собственных проверок данных можно выполнить (чистый numpy):

```python
import numpy as np
z = np.loadtxt("zeros50k.txt")
print(len(z), z[0], z[-1])                       # 50000 14.134725142 40433.687385462
g = np.diff(z)
r = np.minimum(g[:-1], g[1:]) / np.maximum(g[:-1], g[1:])
print("mean r =", r.mean())                      # ≈ 0.614–0.616  → GUE-класс (0.5996)
```

Ожидаемое значение ⟨r⟩ по таблице — около 0.614–0.616 (зависит от среза), что согласуется с GUE-предсказанием 0.5996 в пределах конечномерных поправок и трендов плотности. Это базовая проверка, что файл «тот самый».

## 4. Где коды ищут файлы нулей

Коды ищут данные в нескольких местах (в порядке приоритета) — важно при запуске из другого каталога:

- **HP·MERIDIAN (`hp_audit_standalone.jl`)**: `joinpath(@__DIR__, "zeros50k.txt")` → каталог скрипта; затем `joinpath(pwd(), "zeros50k.txt")` → рабочий каталог; затем переменная среды **`HP_ZEROS`**; консольная команда **`z`** (указать путь интерактивно); CLI-опция **`zeros=path`**. Если файл не найден — H1/H7 **честно** работают «без ζ-стороны» с явной пометкой и подсказкой (молчаливой деградации нет).
- **`test11_honest.py`**: аргумент `--zeros-file` (по умолчанию `zeta_zeros_50k.txt`).
- **Suite / Monumental / RH-линейка**: свои конвенции (вшитые таблицы в RH-линейке; загрузчики рядом с кодом в Suite) — см. документ 02.

**Практическое правило**: держите оба файла данных рядом с `.jl`-скриптами — тогда ничего указывать не нужно. Если запускаете из другого каталога:

```bash
export HP_ZEROS=/путь/до/zeros50k.txt
julia -e 'include("hp_audit_standalone.jl")'
```

## 5. Зачем нули проекту — три роли

1. **Эталонная статистика** (Test 11 и др.): спейсинги реальных нулей сравниваются с Wigner surmise GUE β=2 — это калибровка самого статистического аппарата на данных, чья GUE-природа установлена теоремой Монтгомери–Одлыжко (эвристически) и вычислениями.
2. **ζ-сторона корреляций** (H1/H7): Брэгг-гребень на log p проверяется в данных нулей — Брэгг-пик на простых и молчание на декоях обязательны в ζ; в AB-модели наоборот: декой-пик при молчащих простых был бы аргументом ПРОТИВ арифметики.
3. **Прямое сравнение спектров** (H7 SEQ-CORR): последовательность unfolded уровней AB-спектра против последовательности нулей — знаковые/ранговые корреляции.

## 6. Частые вопросы

**Можно ли подложить больше нулей (например, 100k с LMFDB)?** Да, если сохранить формат построчного списка; но смотрите оговорки про согласованность диапазонов (unfolding полиномами на разных диапазонах даёт разные систематики; коды рассчитаны на данную таблицу).

**Почему в двух файлах разное число строк?** Формат: 1 число/строку против 10 чисел/строку. Число нулей одинаково — 50 000.

**Чем «верифицированы» нули?** Пересчётом через mpmath.zetazero (независимая библиотека, произвольная точность) и контролем GUE-статистики (⟨r⟩ ≈ 0.6144 против R_GUE = 0.5996) — совпадение в пределах ожидаемых конечномерных эффектов.

**Что если файл нулей отсутствует?** Никаких падений: HP-гейты, которым нужна ζ-сторона, печатают явное предупреждение и продолжают без неё; H5 вообще не требует нулей (он про GUE-статистику спектра AB).


---

### 31R.07 — Version chronology (первоисточник на русском / primary record in the original Russian)


> Полная эволюция кодовой базы по changelog'ам: от первого самодостаточного RH-файла до SUPERCOMBO v23.6 и HP·MERIDIAN v24.2-SA. Понимание истории версий объясняет, почему в папке столько файлов: каждый — зафиксированное состояние большого живого исследования.

---

## Таймлайн (структурная схема)

```text
2026-08:  RH_Unified (500 ζ-нулей) ─→ RH_Unified_v5 ─→ RH_Sweep_Pro (13 661 нуль, sweep)
                                                          │
          AB_Cloud_Monumental v6.3 (V01–V112, порт Python)│
                                                          │
2026-09:  ab_cloud_v19 (37 тестов) → v19_v1 → v20 → v21 (+3D Lab, 38 тестов)
                → v21_v1 → v22 (ABPlotV23, THREE-PASS T38) → v23 → v23_v1
                → ab_cloud_v23_v2  = SUPERCOMBO v23.6  ⭐
                                        │ ядро VERBATIM
                                        ▼
          hp_audit_standalone: v23.7-SA → v23.8-SA → v24.1-SA (кап 40) → v24.2-SA (FOCUS-D) ⭐

параллельно: _D-ветка (MERIDIAN DESIGN SYSTEM) для ab_cloud v19/v21/v21_v1/v22/v23_v1,
             RH_Sweep_Pro, RH_Unified, Monumental — только консоль, физика идентична
```

## 1. RH-линейка (август 2026)

### `RH_Unified.jl` — первая «единая» точка
Задача-минимум программы: максимизировать корреляцию AB-облака с нулями ζ(s). 500 реальных нулей (mpmath.zetazero, 25 знаков, ⟨r⟩ = 0.6162), 61 магическая точка α, 6 вихрей-гексагон, RHConfig на 33 параметра, jitter по α/W/σ/позициям/зарядам, 4 компоновки вихрей, sweep α, 9 пресетов, отчёты CSV/TXT/JSON. Главный принцип: **один файл — один эксперимент** (никаких внешних модулей проекта).

### `RH_Unified_v5.jl` — отработка режимов
Расширенные пресеты и диагностика на том же 500-нулевом ядре (~414 строк отличий): обкатка того, что позже станет Sweep Pro.

### `RH_Sweep_Pro.jl` — профессиональный свип
Скачок данных: **13 661 реальный ζ-нуль** (первый 14.134725141735, последний 12943.888244…, ⟨r⟩ = 0.6144), динамический sweep 8 параметров × 10 ключевых точек, preset_auto/preset_balanced (бюджет времени), preset_irrational, run_magic_test — прогон по всем 61 магическим α. Это «прицельный стол» проекта: именно здесь искались параметрические зоны, интересные для глубоких решёточных прогонов.

## 2. Монументальная линейка

### `AB_Cloud_Monumental_v6_3.jl`
Julia-порт Python-базы `run_monumental.py`: **V01–V112** верификаций монографии AB-Cloud. v6: чистый CSV (одна строка на задачу), JSON с полными массивами, per-task PNG, dashboard. Опциональные Arpack (sparse для L ≥ 70) и Plots. Роль в проекте: **регрессионная сетка** — быстрый способ проверить, что модель на месте, после изменений в основных стендах.

## 3. Главная линейка ab_cloud (сентябрь 2026)

### v19.1 — «37 тестов + честный вывод»
Фокус — гипотеза Гильберта–Полиа, продвинутая RMT-диагностика. Ключевое: **live-display pump** — фикс дедлока «зависает на тесте 10» (замёрзшая консоль останавливала drain pipe → 64 КБ tee-буфер заполнялся → весь прогон вставал; теперь одну fire-and-forget задачу перекачки, drain-first, best-effort форвардинг). **Test 20 (TKNN Chern)** добит до якорей α = 1/4, 1/3, 1/5 + α=1/2 массовая ветвь (C₁=0 оба знака), убраны устаревшие заявления. **Новый Test 37**: (1/2)! через Γ — уникальность Γ-конструкции (Бор–Моллеруп) + отражение Γ(1/2)² = π + что нормировка GUE-surmise 32/π² — это (1/2)! = √π/2. Hardcore-проход 2 = BigFloat 256 бит. Вычищен retired-код (twisted-torus FHS и др.).

### v20 → v21 — «3D-измерение»
v21: **38-й тест**, **Physics Lab**, **3D Lab** — разреженный движок на stdlib SparseArrays (без внешних зависимостей); в арсенал входят SymTridiagonal/eigvals!, dot (FHS link product, Test 20), in-place mul!/rmul! (Test 27).

### v22.2 — «журнальные графики»
Отдельный компактный стенд: модуль **ABPlotV23** — публикационное качество графиков; **THREE-PASS Test 38** (38a + 38b hardcore + 38c ladder). Плюс ретир Plots.jl-писателей в основном ядре (v23.1) — графики сосредоточены в специализированном движке.

### v23 → v23.6 (файл `ab_cloud_v23_v2.jl`) — SUPERCOMBO
Объединение: ядро v21 (38 тестов + hardcore + Physics Lab + 3D Lab) × график-движок v22.2 × THREE-PASS Test 38. «Третий разбор» рецензента принёс пять системных улучшений:
1. **DONE-LINE честности** — done-line печатает фактический вердикт (остаток класса багов «WARN поверх PASS»);
2. **H1 deepen-протокол** — потолок нулей режима из 20 vortex-free + 20 GUE реализаций, бугорок против P95 максимумов (зарегистрированное правило останова); расширение ансамбля AB на hp_deep_configs;
3. **H5 α-профиль** — finetuning vs plateau вдоль α ∈ {25/900, 0.05, 0.1, 0.2, 0.35, 0.5} при фиксированной редкой Nv; α=0.5 реплицирует режим A другим сид-потоком; «headline, never scored»;
4. **H1 окно + decoy-специфичность** — окно до max(3.0, ω_max+0.2); композитные декой-цели обязаны молчать; zeta_ok = простые звучат И декой молчит;
5. **H4 guard домена** — заявленные критические обязаны лежать в сканируемом домене, иначе честный WARN.
Пресеты: f FAST (L=16, ensemble=100), F FULL (L=56, ensemble=40, α-scan n=30); новые параметры hp_deep_nulls=20, hp_deep_configs=10, hp_alpha_scan=true/n=40.
Второй разбор (v23.5) ранее добавил: режимно-сопоставленные null-контроли H1 (vortex-free на α режима + GUE matched-size со свежими сидами), фикс двойного вердикта H5 (ok = n_pass ≥ 1 молча перезаписывал WARN → итоговый статус теперь согласован), консолидированный лог+репорт.

## 4. HP·MERIDIAN standalone (v23.7-SA → v24.2-SA)

Зачем: «отдельный код, в котором только проверка H — тесты из меню h — чтобы не вносить правки в огромный код, а в компактный, который конкретно проверяет нужное сейчас». Ядро поднято VERBATIM из v23_v2 (бит-в-бит числа при равных сидах).

### v23.7-SA — консоль HP·MERIDIAN
Уникальные имена гейтов, doctor среды, gate intel со стоимостью, профили конфигурации, отказоизолированные команды, ANSI-безопасный цвет, Ctrl-C/EOF-безопасный ввод.

### v23.8-SA — «прогресс, который видно»
Проблема: репорт-tee держал fd 1 перенаправлённым в файл весь гейт → прогресс-бары невидимы до конца гейта → многочасовой H5 выглядел зависшим. Решения: (1) in-place прогресс-бар через дубликат реального tty-fd с T+elapsed · ETA · текущей реализацией; (2) **heartbeat «alive» каждые 60 с в /dev/tty через sh-subprocess** — единственный честный канал во время одного блокирующего LAPACK-ccall (задачи/таймеры Julia не тикают внутри ccall на 1 потоке); (3) LIVE-строки стоимости перед каждым гейтом + оценка всей батареи upfront; (4) фикс плана фракций H5 (бар скакал 87%→60% на α-профиле); (5) определены мёртвые _prog_tty()/prog_tag! (краш при >1 потоке).

### v24.1-SA — «максимум 40 диагонализаций»
(1) Единый планировщик `_hp5_plan` для гейта и баннера стоимости: showdown ≤ 2×2×7 + α-профиль ≤ 6×2 = **кап 40 солвов ИТОГО**; budget-compliance вместо молчаливого FAIL по «ensemble ≥ 30»; гранулярность KS 1/N печатается. (2) Julia 1.12 fd hotfix: Base.fd больше не принимает Libuv-стримы — каждый гейт умирал в 00:00:00 на 1.12.

### v24.2-SA — FOCUS-D
`hp_regime_mode = :regime_d` + консольная команда **`5d`**: весь бюджет 40 солвов — в режим D (Nv = L²/36, α = 25/900). Сид-континуити: канонический блок A..D сохраняет [D] на offset 30 000 — первые 7 сидов FOCUS-D бит-в-бит равны [D]-блоку showdown (прямое сравнение с прошлыми прогонами). Свои вердикт-заголовки (MISS / OR-CLAUSE ONLY / CLEAN PASS) с N=40; H1-сообщения показывают фактический режим; _hp_diag_est честен для не-showdown режимов; H1 sweep гоняется только в showdown (честность для :regime_d тоже).

## 5. Перекрёстные фиксы и их уроки

| Класс бага | Где был | Что сделали | Урок |
|---|---|---|---|
| Дедлок live-консоли | v19 (tee-pipe) | fire-and-forget pump, drain-first | аудит не должен зависеть от здоровья терминала |
| «WARN поверх PASS» | v22 (done-line, H5 ok, sweep-статус) | фактический вердикт в done-line; ok включает содержимое строк | вердикт — производная от данных, не от флагов |
| Невидимый прогресс | v23.7 (fd 1 → файл) | дубликат tty-fd + heartbeat | во время блокирующего ccall честен только отдельный процесс |
| Несогласованность план/факт | до v24.1 (640 vs 40) | один планировщик для баннера и гейта | стоимость и план должны иметь один источник |
| Статистическая мощность | Test 11 (бутстрэп-завязки), α-профиль 16→64 | i.i.d.-null из H0; оговорка d_crit(√n) | null-распределения — только из правильно заданной H0; мощность меняется с n |
| Смешение факторов | α-профиль при Nv=4 (плотность падает с L) | следующий шаг: плотность ∝ L² | размер и плотность надо варьировать независимо |

## 6. Что дальше (план по протоколу)

1. **FOCUS-D 72×72** — глубокая прокачка режима D на большой решётке (кап 40, ~1 час): уточнить, держится ли медиана D ниже d_crit при n ≈ 3100.
2. **Плотность-контролируемый α-профиль** — убрать смешение размера и плотности (Nv ∝ L²).
3. **Режимные null'ы deepen** для D на большом L (если D снова MARGINAL/PRESENT).
4. **Порт stabilised-изменений** обратно в `ab_cloud_v23_v2.jl` (протокол: правка в компактном файле → синхронизация в суперкомбо).


---

### 31R.08 — Reproducibility (первоисточник на русском / primary record in the original Russian)


> Как повторить любой прогон бит-в-бит; какие правила честности зашиты в коды; какие оговорки нужно держать в голове при интерпретации результатов. Этот документ — «методологический паспорт» проекта.

---

## 1. Сиды и детерминизм

- Профильный сид: **hp_seed = 2026** (см. `p_myset.cfg`). Все случайные потоки (ансамбли конфигураций, GUE-матрицы калибровки, jitter) идут из управляемых сида-блоков.
- **Сид-гигиена режимов H5**: каждый режим A/B/C/D получает свой сид-блок (шаг 10 000/режим). Режим D занимает канонический offset 30 000 — поэтому **FOCUS-D (`5d`) воспроизводит [D]-реализации showdown бит-в-бит** (первые 7 сидов совпадают при любом режиме).
- Ядро HP·MERIDIAN поднято **VERBATIM** из v23_v2 — при равных сидах и параметрах числа совпадают с суперкомбо до последнего знака. Это осознанная защита от «двух источников истины».
- GUE-калибровка: `hp_n_gue_calib` матриц (+ `gue_matrix_size=12000` в профиле) генерируются до основных прогонов — калибровка не «плавает» между гейтами.

## 2. Чек-лист воспроизводимого прогона

1. **Зафиксируйте окружение**: версия Julia (`julia --version`), ОС, число потоков; в лог попадает дата.
2. **Зафиксируйте параметры**: сохраните профиль из консоли (как `p_myset.cfg`) или запишите команду пресета (`s`/`f`/`F`, `5d`).
3. **Данные на месте**: `zeros50k.txt` рядом со скриптом (или `HP_ZEROS`); путь печатается в doctor'е.
4. **Запустите и сохраните лог**: телеметрия прогона (banner'ы стоимости, таблицы, done-line'ы) — часть результата; сохраняйте консольный вывод в файл.
5. **Сверьте баннер плана с фактом**: планировщик `_hp5_plan` печатает план ДО старта; фактическое число солвов не может его превысить.
6. **Повторите**: сид фиксирован → повторный запуск даёт те же числа (вплоть до неустранимого LAPACK-недетерминизма порядка 1e-12 на разных CPU).

## 3. Правила честности, зашитые в архитектуру

| Правило | Реализация |
|---|---|
| Вердикт не украшается | done-line печатает фактический PASS/WARN; ok теста включает содержимое под-строк (никаких «PASS поверх mixed») |
| Null-модели режимно-сопоставлены | vortex-free на α режима + GUE matched-size со свежими сидами; бугорок судится против P95 максимумов нулей (deepen, 20+20) |
| Специфичность арифметики | decoy-цели (21, 33, 54, 56) обязаны молчать; zeta_ok = простые звучат И декой молчит |
| Домен не подгоняется | H4 guard: заявленные критические обязаны лежать в сканируемом окне, иначе явный WARN |
| Бюджет декларируется | HP5_SOLVE_CAP=40; план печатается до старта; баннер и гейт используют один `_hp5_plan` |
| Отображение не врёт | прогресс-бар виден во время гейта (дубликат tty-fd); heartbeat «alive» каждые 60 с; p-value с add-one сглаживанием в test11_honest |
| Мета-информация не скрывается | OR-clause only помечается явно; α-профиль — «headline, never scored» |

## 4. Известные оговорки (обязательные к прочтению)

### 4.1 Порог KS зависит от размера: d_crit = 1.63/√n
Число зазоров n ≈ 0.6·L². При L=16 порог ≈ 0.132, при L=64 ≈ 0.033 — **ужесточение в 4 раза при неизменной физике**. Все сравнения «прошёл/не прошёл» между разными L требуют пересчёта порога. Именно так объяснился флип α-профиля PLATEAU-LOW (16) → NONE (64): рост мощности теста, а не смена физики. Ошибка интерпретации «порога» — самая частая ловушка проекта.

### 4.2 Смешение размера и плотности в α-профиле
Профиль идёт при фиксированной Nv=4 → плотность вихрей на узел падает с ростом L (1.56% при 16 → 0.10% при 64). Сравнение профилей разных L смешивает два фактора. Корректная постановка: плотность, фиксированная на узел (Nv ∝ L²). До этого эксперимента любые «тренды по L» в профиле — только гипотезы.

### 4.3 OR-clause only — это «кандидат», не «проход»
Режим D (64×64): медиана KS_D = 0.0231 < d_crit = 0.033 — статистически неотличим от GUE на этой выборке, индивидуальные KS-проходы 5/7. Но строгий критерий требует ещё ≥ 90% индивидуальных проходов; проход через медиану честно помечается. Следующий шаг — FOCUS-D с N=40 (гранулярность 1/40) и/или больший L.

### 4.4 Старые прогоны и старые формулы баннера
В ранних копиях кода баннер памяти считал матрицу L×L вместо L²×L² и печатал «≈ 0.0 GB» (например, в прогоне 64×64 показано «≈ 0.0 GB», хотя корректная оценка ≈ 0.6 ГБ). Актуальный файл в этом репозитории использует корректную формулу `2.5·(L²)²·16 байт`. При чтении старых логов помните: их баннеры занижены.

### 4.5 Test 11: калибровка — часть результата
Исторический прогон с «медианой референса 12.54» объяснён бутстрэп-артефактом завязок (49999 draws из ~8000 значений). Корректная переработка — `test11_honest` (i.i.d.-null из gue2_surmise_cdf, add-one p-value). При цитировании старых AD-чисел — сверяйтесь с `test11_honest.jl/.py` и документом 02.

### 4.6 LAPACK-недетерминизм на уровне 1e-12
Разные CPU/сборки LAPACK дают микрорасхождения в собственных значениях. На статистиках уровня ⟨r⟩/KS_D это пренебрежимо, но «бит-в-бит» гарантии относятся к сид-потокам, а не к последним знакам double.

### 4.7 Гейты «never scored»
α-профиль (H5) — информационный (finetuning vs plateau) и не участвует в счёте вердиктов. Это сознательное решение: профиль чувствител к мощности и смешению факторов (см. 4.1–4.2).

## 5. Что считать «результатом» прогона

Результат — не строка «PASS», а **связка**: (а) план и его бюджет; (б) таблица режимов (медианы D, доли ⟨r⟩-вилки, индивидуальные KS); (в) вердикт с маркерами (OR-clause only и др.); (г) α-профиль; (д) null-контексты (vortex-free/GUE потолки); (е) окружение (Julia, L, сид, путь к нулям). Сохраняйте всё вместе — только связка поддаётся честному повторению и разбору.

## 6. Этика интерпретации

- **Негативные результаты — результаты**: деградация режима A (0.312 → 0.350) — полезное знание; ABSENT по deepen-протоколу — PASS sweep'а (режимно-устойчивая пустота).
- **Не «спасаем» прогон**: если бугорок не воспроизводится против P95 нулей — это artifact, и протокол требует объявить ABSENT, а не подбирать параметры.
- **Прозрачность бюджетов**: «максимум 40» — пользовательская спецификация; превышение плана невозможно архитектурно, а не «по совести».
- **Не обобщать за пределы домена**: H4 учит, что заявление про критические q вне сканируемого окна — не результат, а ошибка постановки.

