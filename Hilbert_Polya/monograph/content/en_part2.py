# -*- coding: utf-8 -*-
"""content/en_part2.py — monographs C5–C8 (English series)."""
from content.en_part1 import _meta

C5 = {
"meta": _meta("The Extended Gate Family",
              "Six new handles beyond the protocol; the stability of the H2 gap",
              "C5"),
"sections": [
{"h1": "Introduction and setting",
 "paras": [
 "Campaign C5 answers the natural objection to C3: perhaps identity is "
 "reached not on the protocol handles Nv, q, W, α but on something "
 "else? We extend the handle space by six new dimensions: boundary "
 "twists (φx, φy) — spin structures in the sense of C8; hopping "
 "anisotropy t_x/t_y ∈ {0.8, 1.25}; flux shift δα = ±0.02 about the "
 "self-dual line (±1/24 on the torus, where the constraint α·Ny ∈ ℤ is "
 "exact); a staggered mass m ∈ {0.15, 0.35} breaking the chiral "
 "structure; the vortex profile — point-like (site) versus a "
 "finite-radius core (midpoint); the charge sign pattern — neutral "
 "(protocol), all-plus, random; and the boundary type — open versus "
 "torus.",
 "In total 35 new gates plus 2 random-sign decoys, all at the same "
 "master seed 96, the same unfolding pipeline and the same three "
 "statistics as C3 — the comparison is batch-consistent."]},
{"h1": "Method and safeguards",
 "paras": [
 "Every handle is implemented in the engine.hamiltonian kernel and "
 "covered by a regression control: the protocol reference gate "
 "(Nv = 0, W = 0.5, α = 0.5) reproduces the mean level spacing of the "
 "C3 CSV bit-for-bit (deviation 1.4e-16) — the extended pipeline has "
 "not shifted the base. The degenerate corner W = 0 with the midpoint "
 "profile produces exact multiplicities and breaks the polynomial "
 "unfolding; that corner is replaced by W = 0.1 with an explicit note "
 "in the data table.",
 "On the torus the flux shift is rounded to the realisable ±1/24: the "
 "constraint α·Ny ∈ ℤ on the 24-lattice is rigid, and these are exact "
 "neighbouring points of the self-dual line, not approximations."]},
{"h1": "Results: the gap is stable",
 "paras": [
 "The main result is negative and therefore valuable. All 35 new gates "
 "sit in the GUE class: ⟨r⟩ = 0.498–0.505 (0.500 ± 0.002 across the "
 "family). The correlation with the zeros satisfies |r_H7| ≤ 0.043 "
 "against the best protocol value 0.226 and positive controls of 1.000; "
 "the trace projection r_EF (C4) is distributed as 0.52 ± 0.52 — exactly "
 "inside the null clouds (surrogate, Poisson, GUE), and the decoys "
 "behave the same. No handle — alone or in combinations (anisotropy+mass, "
 "twist+mass, midpoint+torus) — moves a gate out of the null zone.",
 "Handle by handle: twists give |r_H7| ≤ 0.033 (spin structures change "
 "the global phase but not the spectral class); anisotropy ≤ 0.030; "
 "flux shift ≤ 0.034; mass ≤ 0.032 — the chiral breaking is the safest; "
 "profile ≤ 0.033; signs and boundaries ≤ 0.044. The family maximum is "
 "reached on a random-sign decoy — the expected noise maximum."],
 "table": {"caption": "Table 1. The six new handles: maxima of |r_H7|",
  "header": ["Handle", "Values", "max |r_H7|"],
  "rows": [["Twists (φx, φy)", "3 spin-structure classes", "0.033"],
           ["Anisotropy t_x/t_y", "0.8; 1.25", "0.030"],
           ["Flux shift δα", "±0.02; ±1/24 (torus)", "0.034"],
           ["Staggered mass m", "0.15; 0.35", "0.032"],
           ["Vortex profile", "site; midpoint", "0.033"],
           ["Signs and boundaries", "neutral/all_plus/random; open/torus", "0.044"]],
  "ratios": [0.34, 0.42, 0.24]},
 "figure": {"path": "figures_hires/{lang}/fig09_handles_{lang}.png",
  "caption": "Fig. 1. |r_H7| across the 37 extended gates: gold line — best protocol value 0.226, copper — positive controls 1.000; red bars — decoys."},
 "figure2": {"path": "figures_hires/{lang}/fig10_gue_ext_{lang}.png",
  "caption": "Fig. 2. ⟨r⟩ across the extended family: every point in the 0.47–0.53 band — the GUE class is universal for all handles."}},
{"h1": "Conclusions",
 "paras": [
 "The H2 gap is stable against a six-dimensional extension of the handle "
 "space. Combined with C3 this means: in the class of local Hermitian "
 "Hamiltonians with vortex phases, GUE universality is an attractor that "
 "erases the arithmetic setting no matter how it is imposed. A "
 "hypothetical operator carrying the Λ(n)/√n weight in its trace (T6) "
 "cannot be obtained by local deformation of the lattice resonator — "
 "a statement now supported by 87 configurations across two campaigns."]},
]}

C6 = {
"meta": _meta("The Prime Flow, the Co-location Kernel and the ψ-Ladder",
              "Φ_p = ½ln p; (Φ_p, Φ_q) ≡ Φ_pq; the resolution kernel δ(d); "
              "universality of codings", "C6"),
"sections": [
{"h1": "Introduction and setting",
 "paras": [
 "Campaign C6 looks for the arithmetic of primes where the Hilbert–Pólya "
 "programme expects it — in the phase layer of the vortex cloud. Three "
 "questions. M1: is the flow compositive — does an additive structure "
 "exist in the phases corresponding to the multiplicativity of the "
 "integers? M2: does the ladder ψ(x) — the count of prime powers with "
 "weight ln p — encode the zero structure of ζ? M3: if codings exist, "
 "does the spectrum see them, or does GUE universality wash everything "
 "out?",
 "The answers form a coherent picture: the flow composites exactly "
 "(1.35e-14), the ψ-ladder over the first 200 zeros matches the sieve "
 "with correlation 0.972, and spectral codings collapse into a single "
 "GUE class. Primes live in the phase and in the zeros, but not in the "
 "statistics of the spectrum."]},
{"h1": "T4. Co-location of the flow",
 "theorem": {"label": "Theorem T4 (co-location).",
  "text": "Let Φ_p := ½ln p be the flow of the prime. Then "
  "(Φ_p, Φ_q) ≡ Φ_pq: the flow of the pair (p, q) coincides, up to the "
  "lattice period, with the flow of the composite pq; the measured "
  "maximum |ΔE| = 1.35e-14.",
  "proof": "The flow is half a logarithm: Φ_pq = ½ln(pq) = ½ln p + ½ln q "
  "= Φ_p + Φ_q — multiplicativity of numbers becomes additivity of the "
  "flow by construction. The measurement confirms that the lattice "
  "realisation of the phases (θ_k = atan2) preserves the identity at "
  "machine level: the discrepancy is 1.35e-14 on the 24×24 grid."},
 "paras": [
 "The resolution kernel of the flow — the response of a composite node "
 "to the distance d between its factors — is measured on d ∈ {0, 0.5, …}: "
 "0 → 3.2e-3 (d = 0.5) → 1.5e-2 (d = 2) → saturation ~2e-2 at d ≈ 4–6. "
 "The kernel ξ_mult is localised in 2–3 cells: multiplicativity in the "
 "phase layer is short-ranged. Importantly, first-order additivity does "
 "NOT hold (~1e-2): the response is nonlinear, and it is the "
 "nonlinearity that carries compositeness — a linear approximation of "
 "the kernel would destroy the co-location."],
 "figure": {"path": "figures_hires/{lang}/fig11_coloc_{lang}.png",
  "caption": "Fig. 1. The resolution kernel δ(d): growth from 0 to saturation ~2e-2 at d ≈ 4–6; multiplicativity is localised in 2–3 cells."}},
{"h1": "M2. The ψ-ladder: sieve against zeros",
 "paras": [
 "The reference ladder is built from the first 200 zeros: ψ_ζ(x) = x − "
 "√x·Σ_{k≤200} e^{iγ_k ln x}/(½+iγ_k) − ln 2π − ½ln(1−x⁻²). A "
 "methodological finding of the debugging stage: a window at heights "
 "γ ~ 500 gives a correlation of only 0.48 — the reference must live at "
 "the same heights as the sieve; with the window on the first 200 zeros "
 "the correlation of ψ_ζ with the von Mangoldt sieve up to 10⁶ is "
 "+0.972 at a maximal error of 4.2.",
 "The same test applied to the gates yields +0.24/+0.13/+0.09/−0.12 — "
 "all inside the null zones (GUE +0.154±0.197, decoys +0.050±0.153). "
 "This is the second projection of the H2 gap: the ladder of primes is "
 "the prerogative of the zeros, and the gates do not reproduce it. "
 "Together with the rank correlation of C3 and the heat trace of C4 "
 "this gives a triple, mutually independent confirmation of one and the "
 "same fact."],
 "table": {"caption": "Table 1. M2: ψ-ladder correlations",
  "header": ["Object", "corr with sieve", "Zone"],
  "rows": [["Reference: first 200 zeros", "+0.972", "identity (prime weight)"],
           ["Best gate (Nv=16)", "+0.239", "null zone"],
           ["Nv=32", "+0.133", "null zone"],
           ["Clean lattice", "−0.116", "null zone"],
           ["GUE null (12 runs)", "+0.154±0.197", "null zone"]],
  "ratios": [0.44, 0.26, 0.3]},
 "figure2": {"path": "figures_hires/{lang}/fig12_psi_{lang}.png",
  "caption": "Fig. 2. ψ(x): the von Mangoldt sieve (teal, thick) against the 200-zero ladder (copper, dashed); correlation 0.972."}},
{"h1": "M3. Universality washes the arithmetic out",
 "paras": [
 "Four codings of the flow into vortex positions — random, prime with "
 "weight 1/√p, logarithmic ln p and the D10 convention — at fixed "
 "positions give ⟨r⟩ = 0.585–0.611 and D(ζ) = 0.049–0.096: one and the "
 "same GUE class. The spread between codings (0.026) is half the "
 "within-coding spread — universality erases the arithmetic content of "
 "the phase as reliably as annealing erases thermal history. This is "
 "exactly why encoding primes into a spectrum (say, the ±E dictionary) "
 "is a universal mechanism without RH-proving force, and why an honest "
 "coding must present itself in the flow (T4) and in the ladder (M2), "
 "not in the level statistics."],
 "conclusion": [
 "The verdict of C6: co-location is exact (T4, proven), the resolution "
 "kernel is short-ranged (T5, measured), the prime ladder matches the "
 "zeros (0.972) and not the gates (H5 — NO, measured), universality "
 "washes the codings out (M3). Primes are encoded in the structure of "
 "the zeros; the road to the operator runs through generating them, "
 "not through copying them."]},
]}

C7 = {
"meta": _meta("Wave-Packet Dynamics",
              "Coherent propagation on L=96; the ζ-cloud is more transparent than random",
              "C7"),
"sections": [
{"h1": "Introduction and setting",
 "paras": [
 "Campaign C7 tests the dynamical dimension of the Hilbert–Pólya "
 "programme: if the lattice resonator is an electron on a flux lattice, "
 "a wave packet must propagate coherently, reflect from the boundaries "
 "and scatter on the vortices. We use a sparse 96×96 Hamiltonian with "
 "open boundaries, integration step dt = 0.1 and horizon T = 40; the "
 "energy is conserved to 1e-15 on every trajectory — the dynamics is "
 "honest.",
 "The key comparison: the ζ-cloud (vortices whose positions are encoded "
 "by the heights of the zeros) against a random cloud of the same "
 "density. If the phase structure is physical, it must show up in the "
 "transport."]},
{"h1": "Results: three effects",
 "paras": [
 "The first effect is coherence: on the clean lattice ⟨x⟩ moves from 24 "
 "to the wall (t ≈ 14.5, reflection) and back out to 44 — a classical "
 "billiard trajectory without decay. The second is vortex scattering: "
 "Nv = 16 hardly interferes (the ζ-cloud is nearly transparent), "
 "Nv = 64 brakes the packet (R = 0.39), and Nv = 256 gives R = 0.47 "
 "plus a transverse drift ⟨y⟩: 48 → 38; a random cloud produces no "
 "drift — the vortex phase structure steers, the random one only "
 "brakes.",
 "The third effect is transport: the probability of reaching the far "
 "wing P(x ≥ 90) is ~16 times higher for the ζ-cloud than for the "
 "random one (0.0032 against 0.0002) — an independent reproduction of "
 "the repulsion-protects-transport effect of the D10 convention. This "
 "is the dynamical face of the Montgomery pair correlations: "
 "regularity of phases reduces backscattering."],
 "figure": {"path": "figures_hires/{lang}/fig13_dynamics_{lang}.png",
  "caption": "Fig. 1. ⟨x⟩(t) for five configurations: clean lattice (teal), ζ-clouds Nv=16/64/256 (copper/gold/slate), random Nv=256 (grey)."}},
{"h1": "Conclusions and boundaries",
 "paras": [
 "The claim that the lattice reproduces the motion of an electron is "
 "confirmed in the honest dynamical sense: coherent propagation, "
 "reflection, scattering, energy conservation. All of the dynamics "
 "lives on the self-dual line α = ½, where the π flux turns the lattice "
 "into a discretised massless Dirac equation (criterion H4 — YES). The "
 "identification of this line with Re(s) = ½ remains a conjectural "
 "bridge: statistical support exists (D7/D10), identity does not, and "
 "campaigns C3–C5 measured the distance to it in three projections."]},
]}

C8 = {
"meta": _meta("The Statistics Ladder and Spin Structures",
              "Poisson/GOE/GUE governed by symmetry; the 64→4 reduction (T8)",
              "C8"),
"sections": [
{"h1": "Introduction and setting",
 "paras": [
 "Campaign C8 fixes the statistical frame in which every spectral "
 "campaign of the series lives. Two questions. First: which classes of "
 "random matrices does the lattice realise, and what governs them? "
 "Second: what do discrete phase structures actually encode — spins, "
 "twists, the spin structures of the Klein quartic — and is there a "
 "hidden variable for arithmetic among them?"]},
{"h1": "T10. The statistics ladder",
 "theorem": {"label": "Theorem T10 (ladder, measured).",
  "text": "The statistics class is set by symmetry: the clean lattice — "
  "Poisson (⟨r⟩ = 0.324–0.386, clustering below Poisson under "
  "frustration); real disorder w = 1–4 — a GOE plateau (0.520–0.538); "
  "strong disorder w = 16–32 — Poisson (Anderson localization); complex "
  "vortex phases Nv ≥ 8 — GUE (0.597–0.612).",
  "proof": "Measured on a ladder of 11 channels (n_real up to 5, "
  "n_spacings up to 1715); classification by ⟨r⟩ and the KS statistic "
  "against three references. GSE is structurally unreachable: a "
  "spinless system has T² = +1, while GSE requires Kramers symmetry "
  "T² = −1 — an architectural, not numerical, constraint."},
 "paras": [
 "The claim all statistics of the source material is confirmed in the "
 "volume of the Dyson triplet: Poisson, GOE, GUE — and not a step "
 "further. This is an important demarcation: universality is an "
 "attractor and cannot witness arithmetic, because it erases everything "
 "except symmetry. The channel with vortices and extra disorder "
 "(Nv=16, torus, w=0.2) gives ⟨r⟩ = 0.597 with a KS-to-GUE p-value of "
 "0.68 — the plateau is robust."],
 "figure": {"path": "figures_hires/{lang}/fig14_ladder_{lang}.png",
  "caption": "Fig. 1. The ⟨r⟩ ladder across 11 channels: reference lines Poisson/GOE/GUE; the vortex channel (first bar) is GUE."}},
{"h1": "T8. spinor64: the 64→4 reduction",
 "theorem": {"label": "Theorem T8 (reduction).",
  "text": "The E2 spin structures (φx = π(e1+e3+e5), φy = π(e2+e4+e6) "
  "mod 2π) yield only 4 distinct Hamiltonians out of 64; the project "
  "table confirms it: exactly 4 unique values ⟨r⟩ = 0.59348/0.59682/"
  "0.60054/0.60271, each rigidly bound to its pair (φx, φy).",
  "proof": "Six basis 1-forms give 64 sign patterns, but the phases "
  "enter only through two sums of three elements; mod 2π each sum has "
  "2 essential values (0 or π) — hence 2×2 = 4 classes. Isospectrality "
  "within classes is machine precision: max|Δλ| = 1.1e-14 (E1: orbits "
  "28/21/7/7/1, Arf 28 odd / 36 even, the odd set matches the reference "
  "bit-for-bit)."},
 "paras": [
 "The practical consequence of the reduction: statements like 64/64 "
 "GUE-consistent are honest but substantively these are 4 spectra, not "
 "64. The encoding in discrete phase structures exists and is absolutely "
 "reliable (isospectrality 1e-14), but its capacity is set by the "
 "symmetry of the phases, not by the number of structures. For the "
 "RH programme the conclusion is transparent: discrete spin structures "
 "carry the universal class, not the arithmetic."],
 "figure2": {"path": "figures_hires/{lang}/fig15_spinor_{lang}.png",
  "caption": "Fig. 2. The four unique ⟨r⟩ values of the spin structures: 64 sign patterns collapse into 4 Hamiltonians by the pairs (φx, φy)."}},
{"h1": "Conclusions",
 "paras": [
 "The statistical frame of the series is fixed: the class is set by "
 "symmetry (T10), discrete phases give exact but universal codings "
 "(T8), and GSE is architecturally closed. Whatever claims arithmetic "
 "further on, it must present it outside statistics — in the flow "
 "identities (T4), in the counting (C2) or in the trace (T6). This is "
 "the discipline the series keeps."]},
]}

DOCS = {"C5": C5, "C6": C6, "C7": C7, "C8": C8}
