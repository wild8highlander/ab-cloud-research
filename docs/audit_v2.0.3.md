# GOE/GUE audit — v2.0.3

This page anchors the **GOE/GUE audit** line of the verification programme:
the dedicated high-precision audit suite that checks the spacing statistics
of the AB-cloud spectrum against the predictions of random matrix theory
(GOE and GUE universality classes).

## Where the code lives

- [`results/Test H1-H8 hp_audit_standalone.jl/`](https://github.com/wild8highlander/ab-cloud-research/tree/main/results/Test%20H1-H8%20hp_audit_standalone.jl)
  — the standalone audit wave: tests H-1…H-8 with per-test reports, plots,
  logs and verdict files (`final_report.md`, `results_verdicts.txt`).
- [`code/hp_audit_standalone.jl`](https://github.com/wild8highlander/ab-cloud-research/blob/main/code/hp_audit_standalone.jl)
  — the dependency-free Julia implementation of the audit suite.
- [`code/ab_cloud_full.jl`](https://github.com/wild8highlander/ab-cloud-research/blob/main/code/ab_cloud_full.jl)
  — the main suite whose GUE-related tests (ratios ⟨r⟩, KS against the GUE
  ratio law, χ² histogram) share the same diagnostics.

## How to read the artifacts

Each test folder under the audit wave contains the numeric verdict, the
parameters of the run and the plots produced. Verdicts distinguish PASS from
WARN; WARN entries carry the Wigner-surmise floor explanation documented in
the [results overview](results.md) and in the monograph.

## Cross-language replication

The same statistics are re-implemented in ten languages under
[`verification/`](verification.md) — including the browser: the dashboard's
"Live ζ statistics" tab recomputes the KS test against the exact GUE ratio
law from the embedded Odlyzko dataset.
