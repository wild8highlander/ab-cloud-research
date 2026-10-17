# TS2 · The state volatility theorem

**Status:** proved (analytically) · **Certificate:** campaign ES2, verdict
PASS (with erratum ES2a) · **Documents:** `theorem_ts2_{ru,en}.{pdf,docx}`
(4 documents) · **Figure:** `figures/ts2_4dim_{lang}.png` (2×2, 600 dpi).

## Statement

The machine has a single register — the phase s ∈ G_θ; reset: G_θ → {0} —
erasure into the canonical state. Then for any prior distribution P on G_θ:

1. **I(S_pre; S_post) = 0** — the post-state is degenerate; the mutual
   information with the pre-state is exactly zero;
2. no observer function g(S_post) recovers S_pre with a probability above
   max_i P(i); for a uniform P — above **1/N**
   (measured 0.2501 against 1/N = 0.25 for N = 4 over 120 000 trials);
3. about the time t the state carries exactly s_t ≡ (s_0 + t) (mod N): the
   share of consistent t′ ∈ [0, 10⁶) equals 1/N — the full history of t is
   **not contained** in the state.

Corollary: such a machine has no long-term memory by construction — the
state carries log₂N bits regardless of the uptime.

## Derivation idea

(i) A constant carries no information: H(S_post) = 0 ⇒ I = 0. (ii) The
classical bound of blind guessing: P[g(0) = S_pre] = Σ_i P(i)·1{g(0)=i} ≤
max_i P(i). (iii) From the deterministic dynamics the set of consistent
moments is a residue class modulo N, with asymptotic share 1/N. The full
proof is in the documents.

## The four dimensions of the certificate (ES2)

| Dimension | What is measured | Result |
|-----------|--------------|------|
| metric | the accuracy of the pre-state reconstruction after the reset | 0.2501/0.1674/0.0717 ≈ 1/N |
| per-instance behaviour | the three models N = 4, 6, 14 | all at the chance level |
| control | the readout of the live state without a reset | deterministic, 1.0 |
| threshold | C1: within the 1/N + 3σ band | PASS (erratum ES2a) |

## Erratum ES2a

The primary wording of the threshold C1 ("acc ≤ 1/N + 1e-9") did not
account for the binomial noise of the estimate over 120 000 trials
(σ_bin ≈ 1.2e-3) and was replaced by the 3σ band **before the verdict was
accepted**; the raw data were not changed. The erratum is recorded in the
verdict `data/es2_volatility_verdict.json` — in the spirit of the
program's discipline (errata are published, not retouched).

## Boundaries (honest)

The theorem is about the informational irreversibility of erasure **in the
model**. It states nothing about the thermodynamic cost of erasure (the
Landauer principle), about physical carriers or about readout noise (the
channel boundary — ES5).

## How to reproduce

```bash
python3 experiments/run_es2_volatility.py  # verdict data/es2_volatility_verdict.json
python3 make_figures.py                    # figures/{ru,en}/ts2_4dim_*.png
python3 make_theorem_docs.py TS2           # 4 documents
python3 -m pytest tests/ -q                # invariants (test_reset_erases)
```
