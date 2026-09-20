# `zip_archive/` — The Original Package, Preserved Bit-for-Bit

This folder holds the original submission archive exactly as it was frozen: **`AB_Cloud_v23_Full_Package_Academic_v34.zip`** (39,652,607 bytes ≈ 39.4 MB). Nothing inside the ZIP has been modified, renamed or re-compressed; the unpacked, reader-friendly edition of its content lives one level up in [`../unpacked/`](../unpacked/README.md). Keeping the original archive alongside the unpacked tree is deliberate archival practice: the ZIP is the canonical artefact whose checksum the author can quote in correspondence, while the unpacked tree is the browsing edition optimised for GitHub.

## Integrity verification

| Field | Value |
|---|---|
| File | `AB_Cloud_v23_Full_Package_Academic_v34.zip` |
| Size | 39,652,607 bytes |
| SHA-256 | `3febd8b0761777822bc1cd0f3f423f4d01672b79b059f456d4cf1a412a4b2100` |

To verify on any machine with `sha256sum` (Linux, macOS via `shasum -a 256`, Termux, WSL):

```bash
sha256sum AB_Cloud_v23_Full_Package_Academic_v34.zip
# must print 3febd8b0...a4b2100
```

Windows users can run `certutil -hashfile AB_Cloud_v23_Full_Package_Academic_v34.zip SHA256` in `cmd.exe`. A mismatch means the file was corrupted or altered in transit — re-download rather than trust it.

## What the ZIP contains

The archive is the v34 freeze of the journal-submission package (v3.3 reference build): the monograph (PDF + DOCX), the Academic Essence companion, both preprint sources and compilations, the cover letter, submission forms, checklist, journal short-list, the cover-design HTML with its fonts, the standalone Julia laboratories, the Python clone with the embedded 50,000-zero dataset, and the complete run-data archives of the reference run and the three September 2026 Test 34 addendum runs. The authoritative contents listing — including the original freeze's own `SHA256SUMS.txt` register — is documented in the unpacked edition: start at [`../unpacked/README.md`](../unpacked/README.md) and [`../FILE_INDEX.md`](../FILE_INDEX.md).

## Why v34?

The package version line (v33 → v34) tracks the September 2026 addendum series: v34 adds the Test 34 HARDCORE pass on the Klein quartic PSL(2,7) Hurwitz surface (100,000 zeros, pooled D = 0.0808, d_GUE = 0.0044, GUE-CONSISTENT), updates the suite source to v3.3 (TEST 34G geometry sweep / Test 39 inside the suite; finite-size laboratory to v1.3), regenerates Appendix B and all PDFs, and rebuilds the internal checksum register. The full delta is documented in the original package README, preserved at [`../unpacked/README_original.md`](../unpacked/README_original.md).
