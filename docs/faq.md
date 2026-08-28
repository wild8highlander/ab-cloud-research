---
title: FAQ
---

# Frequently asked questions

## Is this a proof of the Riemann Hypothesis?

No. The repository provides a **computational laboratory** for the
Hilbert–Pólya programme: it shows that a concrete quantum system (the
AB-cloud) reproduces GUE statistics and the ζ-zero spectrum to high
precision. Statements about the RH itself remain conjectural; every claim
here is bounded by its named verification test.

## Why is the Julia suite dependency-free?

Reproducibility. A single `julia code/ab_cloud_v19.jl --quick` on any
machine with Julia ≥ 1.10 (including Termux on Android) must produce the
same verdicts and full logs. External packages are the most common source
of silent breakage.

## Can the 10-language suite really be run anywhere?

Yes — each folder in `verification/` is standalone for its language, reads
the same zero files, and writes the same summary format. See
[Verification](verification.md).

## What is the relation to the parent repository (research-papers)?

This repository is the **single-topic home** of everything AB-cloud:
monographs, suites, 3D lab and data. The parent
[research-papers](https://github.com/wild8highlander/research-papers)
keeps the full multi-topic corpus (NSE, KdV, Klein attractor, etc.).
The two are cross-referenced via the Zenodo concept DOI.

## How do I cite a specific figure?

Cite the monograph edition that contains it (see [Citation](citation.md))
and the repository DOI; figure sources are named in the figure captions.

## I found a number that does not reproduce — what now?

Open a bug report with your **full log** attached (see
[CONTRIBUTING](https://github.com/wild8highlander/ab-cloud-research/blob/main/CONTRIBUTING.md)).
Numerical reproducibility reports are treated as high priority.
