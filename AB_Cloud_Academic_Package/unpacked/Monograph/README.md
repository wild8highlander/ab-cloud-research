# `Monograph/` — Alternate Copies of the Monograph
> Duplicate editions (DOCX + PDF) of the main manuscript, shipped by the package for submission systems that require documents inside a dedicated directory.

_Location: [unpacked/](../README.md) › [Monograph/](README.md)_

The monograph itself — *"An Aharonov–Bohm Lattice Operator Framework for the Riemann ζ Zeros: A 38-Test Computational Verification Suite"* — already sits at the root of `unpacked/` (see [`../README.md`](../README.md)). This folder holds the **alternate copies** that the package ships so that submission portals which scan a `Monograph/` directory can find the manuscript without reaching into the package root. The files are byte-identical to the root copies (both editions are checksummed in the original freeze's `SHA256SUMS.txt` and in this edition's [`../../SHA256SUMS_unpacked.txt`](../../SHA256SUMS_unpacked.txt)); only their location differs.

## What the monograph contains

The manuscript is organised in three parts plus five appendices. **Part I** develops the framework: the AB-cloud lattice operator, its Aharonov–Bohm flux structure, the Gram-point ladder that carries the ζ zeros into the spectral dictionary, and the tolerance philosophy of the verification suite. **Part II** devotes one chapter to each of the 38 tests of the reference run — every chapter states the claim under test, the pre-registered criteria, the measured statistics, and the verdict, with 46 figures and 10 data tables drawn from the run archive. **Part III** synthesises: the composite verdict algebra, the scope of validity, and the outlook. The appendices carry the full results tables (A), the complete v3.3 source code reproduced verbatim at 32,095 lines (B), the code-audit and patch record of v3.1–v3.2 including the estimator-audit resolution (C), the Python guide (D) and the audit-tier data guide (E). The September 2026 addendum (Add.1–Add.8) forms the final chapter and documents the Test 34 chain through the Klein quartic pass at 100,000 zeros.

## Which copy should a reader open?

For reading and refereeing, the **PDF** preserves the intended typography of the cover and the two-column-free PLOS-style layout. For editing, collaborative review or extracting text, the **DOCX** edition is provided; its table of contents updates via right-click → *Update Field* after any edit. Both carry identical content, page for page, as of the v34 freeze.

## Complete contents inventory

| File | Size | Description |
|---|---|---|
| `AB_Cloud_v23_Monograph_MG.docx` | 3.1 MB | The monograph — editable Microsoft Word edition (TOC updates via right-click → Update Field). |
| `AB_Cloud_v23_Monograph_MG.pdf` | 11.1 MB | The monograph — PDF edition (cover, abstract, TOC, Parts I–III with 38 test chapters and 46 figures, references, Appendices A–E, September 2026 addendum Add.1–Add.8). |

---
_This README is part of the GitHub edition of the AB-Cloud v23 package (v34). Package overview: [../README.md](../README.md)._