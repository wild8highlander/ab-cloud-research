# V13 · The Formal Bridge

![version](https://img.shields.io/badge/version-1.2.0-298bbc) ![](https://img.shields.io/badge/series-V01--V19-3b4f58) ![](https://img.shields.io/badge/status-honest-3a6b4f)

> **Is the RH conclusion formally blocked? The obligation DAG and the status machine.**

[← Back to the main README](../../README.md)

## Contents

1. [Campaign question](#campaign-question)
2. [Results](#results)
3. [Method](#method)
4. [Figures](#figures)
5. [Monographs](#monographs)
6. [Data](#data)
7. [Reproduction](#reproduction)
8. [Honest remarks](#honest-remarks)
9. [Verdict](#verdict)

---

## Campaign question

Is the RH conclusion formally blocked? The obligation DAG and the status machine.

## Results

| Quantity | Value | Status |
|---|---|---|
| Campaign | V13 (plan Solution 13) | committed verdict |
| Key numbers | RH: blocked; 7 blockers (4 assumed, 3 computed); proven 5/12; the DAG is valid. | measured/proved |
| Machine soundness | B1–B5 all green on every run: DAG valid, all 12 artifacts resolve, sorry/oops = 0 across the four assistants, 18 declared reduction axioms, committed verdict consistent. | machine-checked |
| Verdict note | the formal machine BLOCKS the RH conclusion: the path to the conclusion contains the hypotheses O08/O09/O11/O12; no numerical check raises the status; the A1–A6 reduction axioms keep the blocking in force by construction | honest |

## Method

`rpbridge/formaloblig.py` — the obligation machine, five checks per run
(single source of the DAG: `formal/obligations.json`):

- **B1 DAG** — unique ids, references to existing nodes, acyclicity;
- **B2 blocking** — the RH conclusion stays blocked while any node on the
  path O01→O12 has status ≠ proven; any declared reduction axiom forces
  the blocking;
- **B3 artifact gate** — every node cites an artifact that exists in the
  module tree (`#anchors` stripped for the existence check); a stale
  citation makes the machine unsound;
- **B4 formal audit** — zero unfinished proofs (`sorry`/`admit`/`oops`)
  across `formal/` Lean 4 / Coq / Agda / Isabelle after comment
  stripping; the declared axioms (the explicit A1–A6 reduction line) are
  counted and reported per assistant;
- **B5 verdict consistency** — the committed verdict
  `data/v13_verdict.json` must match the machine output field-by-field
  (statuses, artifacts, deps, counters, blockers).

What the machine completely proves: the reduction chain itself — every
propositionally-reducible step of Th1–Th6 is proved in kernel syntax,
every deep classical input is an explicitly named axiom, and the
conclusion gate is enforced. The blocking is not a deficiency of the
machine; it is the machine working as specified.

## Figures

| File | Where |
|---|---|
| `fig13_ru.png` | 600 dpi — `../../figures_hires/ru/`; infographics — `figures/ru/` |

## Monographs

| File | Format |
|---|---|
| `monograph_ru.pdf` | PDF |
| `monograph_ru.docx` | DOCX |

## Data

| File | Content |
|---|---|
| `data/v13_verdict.json` | committed verdict of the campaign |
| `data/` | campaign artifacts |

## Reproduction

```bash
python3 campaigns/run_v13_formal_bridge.py   # live machine run, exit code = soundness gate
python3 scripts/compute_all.py v13           # fresh recomputation
python3 -m pytest tests/test_formal_blocked.py -q   # B1–B5 test battery
```

## Honest remarks

- Metrics are pre-registered; verdicts are committed and independent of
  fresh recomputation — and locked to the machine by check B5.
- The zero file is the only external data; no third-party research code
  is imported.
- Every claim of this campaign has a claim file (V14 audit) with the
  list of what it does NOT prove.
- The machine is complete for its scope and honest about its boundary:
  no accumulation of numerical successes advances the RH status — only
  discharging the assumed obligations O08/O09/O11/O12 (or the A1–A6
  axiom line) can change the verdict, and the machine would re-derive
  that verdict automatically.

## Verdict

**The RH conclusion is blocked honestly and automatically**

---

*AB Research Program v1.1.0 · V13 · The Formal Bridge*
