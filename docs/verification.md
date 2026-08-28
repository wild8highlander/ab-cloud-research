---
title: 10-language verification suite
---

# Independent verification in 10 languages

`verification/` re-implements the core AB-cloud protocol in **ten
programming languages** with an identical output contract:

C++ · Fortran · Go · Haskell · JavaScript · Julia · MATLAB · Python · R · Rust

## Why

A single-implementation result can always be questioned as an
implementation artefact. Ten independent implementations, each reading the
same ζ-zero data and printing the same statistics, remove that objection.

## The three referee objections (answered in-repo)

1. *"Is it just the Hofstadter butterfly?"* — the pure Hofstadter Hamiltonian
   (V30) does not reproduce the ζ-spacings; the vortex phases are essential.
2. *"Is it just Poisson noise?"* — the correlation hole test: R₂ of the cloud
   is closer to GUE (d = 0.140) than to Poisson (d = 0.227).
3. *"Is the agreement cherry-picked?"* — the permutation test with
   Z = 14.10 (r_resid = 0.9963 vs null 0.001 ± 0.071).

## ζ-zero datasets

`verification/data/` — 13,661 / 50,000 / 500,000 / **2,000,000** zeros
(compiled from Odlyzko's public tables; provenance notes in the folder).

## Running

```bash
cd verification/python
python3 ab_cloud_verify.py --zeros ../data/zeta_zeros_50000.txt
```

Each language folder contains its own README with build/run instructions.
