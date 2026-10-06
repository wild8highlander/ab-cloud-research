# tools/ — repository maintenance utilities

Self-contained scripts that regenerate the **per-test documentation suite**
(`tests/D01…D14`) from the validated code modules. Both scripts use paths
relative to the repository root, so they work from any checkout.

## `run_into_folder.py` — per-test artifact regeneration

Runs a single test (or a whole group) with the original harness while
redirecting its outputs into that test's folder:

```bash
python3 tools/run_into_folder.py core            # D1–D8  (~2 min)
python3 tools/run_into_folder.py ext             # D9–D10 (~1 min)
python3 tools/run_into_folder.py ext2            # D11    (~20 s)
python3 tools/run_into_folder.py ext3            # D12–D14 (~4.5 min)
```

For every test this produces, inside `tests/<folder>/`:

| Artifact | How |
|---|---|
| the canonical 600-dpi figure | the test function itself (`_fig_d*`) |
| the canonical CSV data table | the test function itself (`save_csv`) |
| `results.json` | the verdict ledger, machine-readable |

This is exactly how the committed per-test folders were produced (v1.4);
rerunning a group is a full-fidelity refresh, not an approximation.

## `make_extra_figures.py` — companion 600-dpi panels

Adds the companion figure set to `tests/<folder>/figures/` (one or two
additional panels per test: spacing histograms, pairing audits, comb
envelopes, three-band form factors, chiral-breaking law, …). All panels are
recomputed from the same modules and seed — no decorative data:

```bash
python3 tools/make_extra_figures.py      # ~25 s, writes into tests/*/
```

## What is *not* here

The LaTeX monograph emitters used during the v1.4 build live outside the
repository, but their **outputs are fully in-repo**: every
`tests/*/monograph.tex` compiles standalone (see the root `Makefile`,
target `make monograph D=D7`), and the two main editions compile from
`monographs/tex/` (target `make monographs-tex`) with the figures copied
into `monographs/tex/figures/`. Any TeX distribution with XeTeX support
(the repository CI used [Tectonic](https://tectonic-typesetting.github.io))
builds them without extra assets.
