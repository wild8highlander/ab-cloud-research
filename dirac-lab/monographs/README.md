<!-- AB-ENRICHED:v1 · sub -->
<div align="center">

<img src="https://capsule-render.vercel.app/api?type=venice&height=48&color=0:00e5ff,100:05060f&section=header" alt="" width="100%"/>

**🧭 [⬆ dirac-lab/](../README.md) · [🏠 Root README](../../README.md)**

</div>
# monographs/ — The research monograph, three editions

> **🧭 Navigation:** [dirac-lab/](../README.md) · [Root README](../../README.md)

The full research monograph — *The Dirac Skeleton of the AB-Cloud* — weaves all
fourteen tests into one argument. It exists in three synchronized editions; the
numbers, section structure and verdict ledger are identical across all of them.

| Edition | Files | Language | Role |
|---|---|---|---|
| **LaTeX (canonical typeset)** | [`tex/Dirac_Lab_Monograph_EN.pdf`](tex/Dirac_Lab_Monograph_EN.pdf) · [`tex/Dirac_Lab_Monograph_EN.tex`](tex/Dirac_Lab_Monograph_EN.tex) | English | reference typesetting, compiled with **Tectonic**; sources included |
| **LaTeX (canonical typeset)** | [`tex/Dirac_Lab_Monograph_RU.pdf`](tex/Dirac_Lab_Monograph_RU.pdf) · [`tex/Dirac_Lab_Monograph_RU.tex`](tex/Dirac_Lab_Monograph_RU.tex) | Russian | full parallel edition, same Tectonic pipeline |
| **DOCX (editable)** | [`en/Dirac_Lab_Monograph_EN.docx`](en/Dirac_Lab_Monograph_EN.docx) · [`ru/Dirac_Lab_Monograph_RU.docx`](ru/Dirac_Lab_Monograph_RU.docx) | EN / RU | editable Word editions (figures embedded) |
| **DOCX print rendering** | [`en/Dirac_Lab_Monograph_EN.pdf`](en/Dirac_Lab_Monograph_EN.pdf) · [`ru/Dirac_Lab_Monograph_RU.pdf`](ru/Dirac_Lab_Monograph_RU.pdf) | EN / RU | LibreOffice print rendering of the DOCX (30 pp. EN / 33 pp. RU) |

The LaTeX figures resolve against the canonical
[`../figures/`](../figures/) folder (`../../figures/` from `tex/`),
so a recompile after a fresh run picks up the new 600-dpi panels automatically:

```bash
cd tex && tectonic Dirac_Lab_Monograph_EN.tex     # ≈ 1 min, self-contained
cd tex && tectonic Dirac_Lab_Monograph_RU.tex
```

`tex/cover_{EN,RU}.html|pdf` — the cover pages, rendered from HTML at vector
quality via the html2poster pipeline.

**Structure (both languages, v1.3 content):** abstract & keywords → table of
contents → 16 sections (introduction · lattice Dirac equation D1 · zero tower
D2 · Berry phase D3 · Landau ladder D4 · real-time D5–D6 · the ζ bridge D7–D8 ·
implications for Hilbert–Pólya · **index restoration D9** · **Montgomery in
motion D10** · **the conjugation action D11 (Berry–Keating / Connes)** ·
**the infinite BK ladder D12** · **the D9+D11 pairing D13** · **the second form
factor D14** · methods · conclusions) → verdict-ledger table (96 checks) →
24 references. All fourteen laboratory figures are embedded; every number is
traceable to [`../results/run_20261006_081031/`](../results/run_20261006_081031/).

**Per-test monographs.** In addition to the unified monograph, every one of the
fourteen tests owns a focused monograph (LaTeX source + compiled PDF, 4–5 pp.)
inside its own folder — see [`../tests/`](../tests/), one folder per test with
its own README, verdict ledger, data table and 600-dpi figure set.

---

<!-- enriched-r3 -->

This folder is a small but functional **shelf of its module**: it keeps a focused set of artifacts that the parent README references. The listing below is generated from the folder itself, so it is exact; the parent README explains how these pieces fit into the study. Nothing here is a compiled binary or an external download — everything is committed source, data or documentation.

The research monograph of the laboratory in three editions: English, Russian and the LaTeX sources.

## Folder contents

**Subfolders:** `en/` · `ru/` · `tex/`

<div align="center">

<img src="../../assets/svg/divider-cyan.svg" alt="—" width="100%" height="12"/>
<sub>⚡ Part of <a href="../../README.md">AB-Cloud Research</a> — numbers are verbatim from the unified registry; no result on this page is a claim about the Riemann hypothesis · <a href="../README.md">⬆ parent section</a></sub>

</div>
