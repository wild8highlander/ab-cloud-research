# Open Challenge: Close the H7 Gap

**v2.0 · Hilbert–Pólya Bridge · public metric, blind protocol, positive controls**

---

## The metric

The measured boundary of the v1/v2 program is the rank projection of the
spectral-identity gap (**H2**): over 87 v1 gates + 16 v2 blind gates +
121 anomaly-scan configurations the best rank correlation with the zeta
zero window is

```
r_H7  ≤  0.226   (v1 protocol)        p_r = 0.169, Bonferroni 0.80
|r_H7| ≤  0.092   (v2 protocol)        min p = 0.29
```

while the positive controls — the only places where identity is known to
exist — give **r = 1.000** (PC1 isospectral twins) and **r = 1.000000**
(PC0′ twin pipeline). The gate family sits at the **surrogate-null
saturation level** of the D_nn metric (gates 0.238–0.295 vs 0.26 ± 0.01 for
GUE surrogates and shifted zero windows — indistinguishable from random; the
controls' 1e-14…1e-10 values are machine-precision identity, not a scale,
so "orders of magnitude" are undefined on this bounded metric — correction
v2.0.1).

## The challenge

> **Demonstrate r_H7 ≥ 0.7 under the v2 protocol — a rank correlation far
> above the surrogate null cloud (r_H7 is a bounded correlation, so the
> former "reduce by 2 orders of magnitude" phrasing was undefined; correction
> v2.0.1) — while keeping all positive controls passing and the GUE class
> intact.** Recognition in the repository
> AUTHORS/CHANGELOG and a joint paper offer for any accepted result.

## Submission format

A JSON gate specification (one file per gate):

```json
{
  "name": "my-gate-001",
  "family": "protocol | phased | custom-code-ref",
  "lattice": 24,
  "handles": {"Nv": 16, "q": 1.0, "W": 0.5, "alpha": 0.5,
               "aniso": 1.0, "dalpha": 0.0, "mass": 0.0,
               "profile": "site", "signs": "neutral", "bc": "open",
               "twist": [0.0, 0.0]},
  "phase_encoding": null,
  "seed": 96,
  "notes": "free-form rationale"
}
```

## Scoring protocol (blind)

1. The scorer rebuilds the Hamiltonian from the spec with the **package
   engine** (no side channels), `seed` fixed and logged.
2. Metrics computed by `hpbridge.metrics_v2`: r_H7 (unfolded-vs-unfolded
   window, k0 = 224, K = 200), permutation p (64 shifts), GUE z-score
   (40 matrices), ⟨r⟩ class, r_EF fluct (heat projection, fixed scale).
3. **Positive controls must pass in the same run**: PC0′ (isospectral twin
   → r = 1.000), PC0 (zeros window vs prime comb → r ≈ +0.999).
4. **Blind rule**: the scorer must not have seen the spectrum before the
   run; the spec + full metric report are committed to
   `challenge/submissions/` regardless of outcome.
5. Bonferroni correction over the number of simultaneously submitted gates.

## What does NOT count

- Any construction that encodes the zeros themselves (the twin pipeline
  already sits at r = 1 by construction — see C9/T11: the primitive exists
  at the trace level; the open problem is a **local** realization);
- Metrics with free fitted scales or windows chosen post hoc (the C4/M2
  lesson: fixed scale only);
- Submissions breaking the GUE class (⟨r⟩ outside 0.5±0.03) — those are
  interesting, but belong to the anomaly hunt (C14/T16), not to H2.

## How to run the scorer

```bash
python3 challenge/score_submission.py challenge/examples/example_gate.json
```

## Leaderboard

See `challenge/LEADERBOARD.md` (empty at v2.0 — be the first entry).
