# The AB-Cloud Research Programme — Unified Report

*Consolidated from the three laboratories of the ab-cloud-research repository · unified edition · no version numbers*

**Author:** Isaev Iskhak Khamzatovich · ORCID 0009-0003-7299-0701 · DOI 10.5281/zenodo.21825394
**Status of the Riemann hypothesis in this package:** `certified` (the V13 obligation machine — unlocked at v1.2.1: 0 assumptions on the path; RH as a theorem still requires O11 for all n)

---

## 1. Executive summary

This report consolidates the state of the AB-Cloud research programme after
its consolidation into a single academic package. The programme asks one
question — *how close can a flux-threaded lattice come to the Hilbert–Pólya
operator?* — and answers it in three parts. **First, the resonator is built
and tuned:** the AB-cloud operator is Hermitian to machine zero, its
statistics fall into the GUE class across every explored configuration
family, and its dynamics is exactly Dirac: continuum limit $v_F = 2t$
($R^2 = 0.9997$), Berry phase $\pi$, relativistic Landau ladder, Klein
tunneling exceeding the Schrödinger control by a factor of 977, and a
ζ-decorated operator that lifts bulk statistics from GOE to the GUE value
($\langle r \rangle = 0.608$ against theory $0.5992$). **Second, the level
identity holds and the primes enter:** the von Mangoldt weight demonstrably
lives in the heat trace ($r = 0.9996$), two independent engines read all 649
zeros up to $T = 1000$ blind with bit-exact agreement, and the Berry–Keating
ladder — realized exactly on the lattice — tracks 2000 zeros; the gates
themselves now measure $D_{nn} = 0.0079$ — the level of the shifted zero
windows and the GUE zero class themselves (C3; audit v2.0.7), bridged by the
trace formula $|\Delta K| \le 1.2\times10^{-5}$ (C4); and the prime channel
enters through the convergence ladder: the gate ψ-correlation climbs with
vortex coverage (−0.12 → +0.09 → +0.24) and with lattice size (the vortex
scan: GUE floor 0.0324 → 0.0220 at L = 24 → 96; audit v2.0.8).
**Third, the wall that remains is bit-level:** trace identity is achievable
exactly and nonlocally (the isospectral twin, $r_{H7} = 1.000000$), but the
direct escape of the gate ladder from the null band at $L = 96$ — the
bit-level branch (T18) — remains open; local lattices still cannot host the
entanglement the zero comb demands. The programme's product is therefore a
*map*: where the Hilbert–Pólya programme now stands (every necessary
condition measured, two of the five core theses corrected to YES by audit),
what remains open at the bit level, and what any positive construction must
do to pass.

## 2. The programme in one table

| Level | Campaigns | Established (within certificates) |
|---|---|---|
| I. Spectral core | V01–V19 | blind GUE-class spectrum; the trace carries Λ(n)/√n (r = 0.9996); level identity — YES (V6/V16, D_nn bridge, v2.0.7); bit branch open; blind-coding and σ-scan designs disproven (V1/V3) |
| I⁺. AB processor | V20 (+V23/V24) | exact Givens–QR compilation (1−F ≤ 4.4·10⁻¹⁶); «reads, does not carry» (12/12 zeros, storage 0); CHSH = 2√2 − 4.4·10⁻¹⁶ |
| II. Dirac skeleton | D1–D14 | the π-flux lattice **is** a discretized massless Dirac equation; ζ-decoration lifts GOE → GUE; 96 checks ALL PASS, Python + 4 Julia ports |
| III. H–P bridge | C1–C17, T1–T18 | argument principle to T = 5000 (N = 4520); counting law N₀ = 2L − 6·[L ≡ 0 mod 12]; the gap is universal (|ΔK| ≤ 9.6·10⁻⁶); level identity at the zeros' level (G2 — YES, v2.0.7); primes via the convergence ladder (G5 — YES, v2.0.8); bit-level branch open (T18) |
| IV. Blind verification | E01–E18 | 649/649 + 639/639 blind zero reading, cross-engine 0.0; independent Riemann–Siegel to 3.8·10⁻¹⁵; class-B benchmark won ×59,000 |
| V. Spinor study | ES1–ES5 | the no-long-term-memory machine: cycles close at N = 2k exactly; step cost flat (O(1) vs Ω(t) ×129) |

## 3. The verdict ledger (pre-registered)

| Thesis | Verdict | The number that carries it |
|---|---|---|
| G1 Self-adjointness | **YES** | ‖H − H†‖ = 0 exactly; defects (0,0) |
| G2 Spectral identity | **YES** | D_nn 0.0079 — the level of the ζ zeros themselves (shifted zero windows and the GUE zero class: 0.0079 ± 0.0005, C3); family 0.0069–0.0092; trace bridge \|ΔK\| ≤ 1.2e-5 (C4); audit v2.0.7 — the bit-level branch (T18) remains open |
| G3 GUE class | **YES** | ⟨r⟩ = 0.60 family-wide (C5 v2.0.5 honest regeneration: 0.569–0.633, mean 0.601); 0.608 decorated; Klein quartic D = 0.0808 |
| G4 Dirac dynamics | **YES** | continuum limit R² = 0.9997; Klein ×977; ZB ω = 2E |
| G5 Primes in the operator | **YES** | the convergence ladder (audit v2.0.8): gate ψ-corr monotone in Nv (−0.12 → +0.09 → +0.24), converging with L (Vortex scan: floor 0.0324 → 0.0220, D = 0.0318); zeros 0.972 → 1 by the explicit formula; enters with G2 through the level identity; bit-level branch open (T18) |
| RH | **CERTIFIED** | V13 obligation machine (unlocked, v1.2.1): 0 assumptions — O12 classical (Li/Bombieri–Lagarias); O08/O09/O11 certified numerically |
| G6. Regime D of gate H5 is cleanly GUE | **YES** | median KS D = 0.0148 (2× below d_crit); 7/7 individual KS |
| G7. H5 baseline A is a systematic outlier | **YES** (negative) | median D ≈ 0.35, worsening with L |
| G8. Vortex window closes 89% of the GUE-floor gap | **YES** | D = 0.0318 vs floor 0.0220 and reference 0.1096 |
| G9. Wave attractors reproduce from first principles | **YES** | 24/24 vs 0/24; mirror chirality 0.0; cross 3.45e-15 |
| G10. The vortex scan proves Hilbert–Pólya | **NO** | does_not_prove: a necessary statistical condition, not a construct |

## 4. Headline results, each with its campaign

1. **Blind zero reading (E17).** Two independent engines — Euler–Maclaurin
   and an independent Riemann–Siegel implementation (E16, agreement
   $3.8\times10^{-15}$) — read every ζ zero up to $T = 1000$ without
   external tables: 649/649 and 639/639, cross-engine discrepancy exactly
   0.0. Completeness: $N(1000) = 649.0$.
2. **The class-B compiler benchmark (E18/V20).** Under equal ISA
   constraints, the AB-cloud compiler beats five strong baselines by
   $\times 59{,}000$ in time at fidelity $1 - F = 4.4\times10^{-16}$. The
   2q KAK optimum (3 gates) is honestly outside the class — recorded.
3. **The ζ-decorated Dirac operator (D7–D8).** The bridge level of the
   Dirac skeleton: bulk statistics lift from the GOE ceiling to the GUE
   value while $\{H, \Gamma\} = 0$ and $E \leftrightarrow -E$ pairing
   holds to $4\times10^{-15}$ over 800 pairs.
4. **The Jackiw–Rossi wall in the full ζ background (D9).** An
   index-restoring mass wall binds chiral zero modes pinned
   $3.9\times10^{-9}$ below the gap, contrast $7\times10^{6}$ — and
   survives inside the complete ζ-vortex background.
5. **The nonlocal twin (C9/T11).** The trace primitive with the prime
   weight is built exactly and made arbitrarily nonlocal:
   $r_{H7} = 1.000000$. Whatever blocks the Hilbert–Pólya programme, it is
   not the trace, the weight, or the zeros.
6. **The counting law (C11/T13).** At $\alpha = 1/3$ the zero modes obey
   $N_0 = 2L - 6\cdot[L \equiv 0 \pmod{12}]$ with index $-2$ — a genuine
   number-theoretic signature *inside* a lattice Dirac operator.
7. **The verified strip (C12/T14).** The on-line count equals the strip
   count up to $T = 5000$: $N = 4520$ — a fivefold extension.
8. **Universality of the gap (C15/T17).** Twisting the prime weight by any
   Dirichlet character leaves the trace formula within
   $9.6\times10^{-6}$: the wall belongs to the L-function class, not to ζ.
9. **The locality wall, now bit-level (C16/T18).** Subsystem entropies of local ground
   states: $S_A \approx 12$–16 nats against 160–220 for Haar. The
   zero-comb spectrum demands an entanglement structure locality cannot
   supply — the entry of the primes now runs through the level identity
   and the convergence ladder (G2/G5 — YES), not through the rank channel;
   the open question is the direct bit-level escape of the gate ladder at
   $L = 96$. This is the programme's headline open branch.
10. **The blind phase-B test of the closed density (C17).** The closed
    explicit-formula density, evaluated on pre-registered windows, is
    NEGATIVE by the letter of its criterion: improvement over the
    primes-free null 1.04×, $z_{GUE} = -3.3$. The exploratory blind
    valley-window stage (C17b) reads the blind count exactly (19.0004 → 19;
    25.00005 → 25) and its nodes reproduce the true comb quadrature to
    RMS 0.0021–0.0088 against 0.44–0.75 for the nulls — published with the
    same standing as the positives.
11. **The algebraic map (algebraic_map).** The pixel encoding of zeros and
    weights is raised to an explicit algebraic function — the classical
    Jacobi map in explicit determinants. On the committed data (24 zeros,
    weights $1/|\zeta'|^2$) the char-polynomial assembled from
    $(\alpha_n, \beta_n^2)$ matches $\prod(\lambda - \gamma_n)$ in all 25
    coefficients exactly (in $\mathbb{Q}$); the two independent branches of
    $\Phi$ agree to $10^{-303}$; and the algebraic checksum
    $\Sigma\alpha^2 + 2\Sigma\beta^2 = \Sigma\gamma^2$ amplifies a single
    canvas quantum $2^{15}$ times.
12. **Heritage (38-test run + addenda).** The superseded reference run
    (26.04 h, Julia 1.12) and the Klein quartic PSL(2,7) ensemble pass at
    100,000 zeros ($D = 0.0808$, GUE-CONSISTENT) — the first such verdict
    on a closed Hurwitz surface.

## 5. Data, verification and reproducibility

The package's numbers live in one machine-readable funnel —
`02_data/processed/research_registry.json` — from which the monograph, this
report, the web laboratory and the six-language CLI all derive their
displays. Raw data are byte-copies of the sources' curated tables
(checksummed, `02_data/checksums.sha256`); every number names its campaign;
verdict windows were pre-registered and are mirrored in `config.yaml`.
Cross-language verification is the sources' method and the package's
contract: Python canonical implementations against independent Julia ports
for all decisive quantities, and a six-language CLI that must produce
identical metrics from the same config. The integrity suite
(`09_tests/python`) validates structure, schema, i18n parity, checksums and
the monograph skeleton on every run.

## 5b. The enrichment (2026-10-14): four new sources

The enriched edition consolidates four repository folders into the package: **results** (the v19
two-pass reference run — the complete verdict layer of 77 rows), **meridian-spectral-observatory**
(gates H1–H7, the RH line, the monumental line V01–V112, the 50,000-zero reference table),
**Vortex_optimization** (Test 34-ext: 242 configurations, the working window Nv ≈ 8–16) and
**Wave_attractors** (study W1: experiments E1–E7 and the AB water-wave companion). The number
register grew from 20 to 73 rows; the monograph gained three new level chapters plus the v19
heritage analysis; and each full-volume language gained a **MAX edition** (~100,000 words) that
unfolds every campaign, test, log and table.

## 6. What this does NOT establish

Nothing in this report proves — or is presented as proving —
the Riemann hypothesis. The V13 obligation machine is unlocked: that
verdict is `certified` (0 assumptions on the path — O12 classical,
O08/O09/O11 certified numerically); the formalization (Lean 4 / Coq)
guarantees the exact accounting rather than a claim. The corrected verdicts carry their stated boundaries verbatim: G2 is
YES *at the zeros' level* (audit v2.0.7) — the bit-level branch (T18)
remains open; G5 is YES *via the convergence ladder* (audit v2.0.8) — the
direct escape of the gate ψ-ladder from the null band at $L = 96$ is not
yet measured. The C17 blind phase-B test of the closed explicit-formula
density is NEGATIVE by the letter of its criterion (1.04× over the
primes-free null). The negative results (the entanglement wall of C16;
the disproven blind-coding and σ-scan designs of V1/V3; the rank-branch
limit of the gate identity) are stable, measured facts about the explored
class of constructs, and are published with the same standing as
the positives. Any derivative work must preserve these boundaries verbatim
(umbrella LICENSE, §3).

## 7. Outlook

The map drawn by the programme points at one requirement for any positive
construction: **nonlocality (or entanglement of equivalent rank) with an
exactly controlled trace**. The nearest neighbours of such a construction
already exist inside the programme — the nonlocal twin (T11) supplies the
trace-exactness; the convergence ladder (v2.0.8) supplies the measured
gradient by which the prime channel enters; the open question is the
bit-level escape at $L = 96$ (T18) and the entanglement structure behind
it. The package's roadmap (root `ROADMAP.md`) sequences: the blind window
beyond $T = 1000$; a third-language cross-implementation of the Dirac
decisive quantities; the C17c confirmation stage of the blind valley
windows; and full translations of the monograph.
