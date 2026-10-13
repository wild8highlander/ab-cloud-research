# monograph/ — the summary volumes and their content sources

<p align="center"><img src="../assets/illustrations/ill_critical_line.png" width="600" alt="The critical line drawn as a bound volume spine"/></p>

<p align="center"><img src="../assets/avatars/hp_cast_strip.svg" width="720" alt="Bridge avatar cast"/></p>
<p align="center"><em>Where the numbers become prose: one content source, two typesetters, four bound volumes per generation.</em></p>

[← Back to the main README](../README.md)

## What this folder is

The bound, human-readable layer of the series. While `data/` keeps raw
verdicts and `computations/C*/` keeps per-campaign material, this folder holds
the consolidated volumes: a theorem volume (T1–T10), a reproduction-protocol
appendix, and the v2.0 generation of both. Each volume exists in Russian and
English and in two formats (PDF and DOCX), all rendered from a single source
of content so that the languages and formats cannot drift apart.

## Folder map

```
canon_volume/     monograph_canon_{ru,en}.{docx,pdf}  — канонический том: единая версия (T1–T18)
theorems_volume/  monograph_theorems_{ru,en}.{docx,pdf}  — том теорем T1–T10 (приложение к канону)
appendix_volume/  monograph_appendix_{ru,en}.{docx,pdf}  — протоколы воспроизведения (приложение)
content/          single source of content (ru_part1-4.py, en_part1-4.py, canon_ru/en.py)
```

The full inventory of the folder:

| Path | Contents |
|------|----------|
| `canon_volume/` | `monograph_canon_{ru,en}.{docx,pdf}` — **the canonical volume, the primary version of the package**: one continuous text T1–T18, campaigns C1–C16, the scorecard, the pixel protocol, reproduction protocols, the honesty ledger and the expanded roadmap «the operator that encodes the zeros» |
| `theorems_volume/` | `monograph_theorems_{ru,en}.{docx,pdf}` — the four files of the T1–T10 theorem volume (predecessor of the canon) |
| `appendix_volume/` | `monograph_appendix_{ru,en}.{docx,pdf}` — the four files of the reproduction-protocol appendix |
| `v2_volume/` | `monograph_v2_{ru,en}.{docx,pdf}` — the consolidated v2.0 monograph (chapters C9–C16 feed the canon verbatim) |
| `theorems_v2_volume/` | `monograph_theorems_v2_{ru,en}.{docx,pdf}` — the v2 theorem volume (T11–T18 era) |
| `preprint/` | `preprint.tex`, `preprint.pdf` — the LaTeX preprint distilled from the series |
| `content/` | the single content source: `ru_part1.py` … `ru_part4.py`, `en_part1.py` … `en_part4.py`, `parts_theorems_v2.py`, and the canon sources `canon_ru.py` / `canon_en.py` (fresh chapters only — C9–C16 chapters and T-blocks are imported from the part modules) |
| `src/` | reserved slot for future template overrides (cover, styles); see `src/README.md` |
| `../audit/` | the package audit report (pdf/docx): monograph layer, pixel protocol, scientific review, roadmap |

**The reading order for newcomers is: main README → canon → detail
volumes.** The canon supersedes the v1/v2 split: the theorem volumes and
the v2 monograph remain as detailed appendices, and their titles are best
read as «приложение к канону». Rebuild the canon alone with
`python3 scripts/make_monographs.py canon` (or `make canon`).

Monographs of the individual computations live separately, in
`computations/C*/monograph_{ru,en}.{docx,pdf}` — one pair per campaign
directory, next to that campaign's figures and data.

## How to use it

The same content-JSON is rendered twice:

- **PDF** — ReportLab, with an html2poster cover and final assembly via pypdf;
- **DOCX** — docx-js, with the R1 cover recipe, three-section numbering, and
  TOC placeholders.

Rebuild everything from the committed content:

```bash
make monographs
```

The renderers themselves live in `scripts/` (`render_pdf.py`,
`render_docx.js`, `postprocess_docx.py`, `make_monographs.py`); this folder
only stores sources and outputs. To change what the volumes *say*, edit
`content/`; to change how they *look*, see the conventions below.

## Conventions

- Language and format are encoded in the file name as suffix pairs
  `{ru,en}` × `{docx,pdf}`; the four combinations of a volume are always
  produced together.
- `content/` is the single source of truth: part files are plain Python
  modules of content blocks, so the ru/en pairs stay in lockstep by review,
  and the v2 generation reuses the same block schema
  (`parts_theorems_v2.py`).
- DOCX files carry TOC placeholders that `postprocess_docx.py` resolves, plus
  ROMAN/arabic footer numbering over three sections; PDF files get their
  cover from the html2poster recipe and are merged with pypdf.
- The preprint in `preprint/` is plain LaTeX (`preprint.tex`) compiled to
  `preprint.pdf`; it cites the same committed numbers as the volumes, never
  fresh ones.

## See also

- [src/README.md](src/README.md) — the reserved template-override slot
- [../computations/C1_identity_function/README.md](../computations/C1_identity_function/README.md) — a per-campaign monograph next to its data
- [../scripts/README.md](../scripts/README.md) — the render pipeline that builds this folder
- [../results/RESULTS.md](../results/RESULTS.md) — the ledger every volume quotes from
