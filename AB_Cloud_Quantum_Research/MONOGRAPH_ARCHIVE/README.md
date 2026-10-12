<div align="center">

<img src="../assets/logo_abcloud_light.png" width="120" alt="AB Cloud Quantum Research"/>

# MONOGRAPH ARCHIVE

**The monograph archive of the AB Cloud Quantum Research program: one large main
monograph in Russian and English (DOCX + PDF), four level research program
monographs, and full LaTeX sources for every document.**

Версия **1.1.0** · стиль *Critical Line & Copper* · © Исаев И. Х.

![badge-docs](https://img.shields.io/badge/documents-24%20RU%2FEN%20%C3%97%20PDF%2FDOCX-C96F4A?style=for-the-badge)
![badge-latex](https://img.shields.io/badge/latex-10%20sources%20.tex-0E7C86?style=for-the-badge)
![badge-pages](https://img.shields.io/badge/main%20monograph-104%2B%20pages-8C6D1F?style=for-the-badge)
![badge-license](https://img.shields.io/badge/license-proprietary-6B6455?style=for-the-badge)

</div>

> [!IMPORTANT]
> **Honest boundary.** Everything in these monographs is a numerical and formal
> study of a mathematical model. It does **not** prove the Riemann hypothesis:
> the V13 obligation machine keeps the RH conclusion **blocked** while the
> analytic prerequisites remain assumed. Every claim carries a verdict source;
> every verdict carries a `does_not_prove` field.

---

## 📖 Contents

- [What is here](#-what-is-here)
- [The main monograph](#-the-main-monograph)
- [Research programs](#-research-programs)
- [LaTeX sources](#-latex-sources)
- [Provenance and style](#-provenance-and-style)
- [How to verify](#-how-to-verify)
- [Русская версия](#русская-версия)

---

## 📚 What is here

This folder is the **publication layer** of the program: everything the other
folders measure and prove is collected here into monograph form, in both
program languages, in both common formats, with LaTeX sources for re-typesetting.

```
MONOGRAPH_ARCHIVE/
├── README.md                      ← this file
├── LICENSE                        ← the repository license (duplicated verbatim)
├── main_monograph/                ← the main monograph of the whole program
│   ├── ..._Monograph_RU.pdf       ← Russian, ~107 pages, with figures
│   ├── ..._Monograph_RU.docx      ← Russian, editable Word version
│   ├── ..._Monograph_EN.pdf       ← English, ~104 pages, with figures
│   ├── ..._Monograph_EN.docx      ← English, editable Word version
│   └── latex/                     ← monograph_RU.tex · monograph_EN.tex
└── research_programs/             ← the four level research programs
    ├── Program_Core_RU|EN.pdf     ← the spectral core program (V01–V19, Th1–Th6, V13)
    ├── Program_Processor_RU|EN.pdf← the AB processor program (V20, P0–P6)
    ├── Program_Verification_RU|EN.pdf ← the verification program (E01–E18, O-J)
    ├── Program_Spinor_RU|EN.pdf   ← the memoryless machine program (ES1–ES5, TS1–TS3)
    ├── *.docx                     ← editable Word versions of all eight
    └── latex/                     ← program_*.tex — eight LaTeX sources
```

---

## 📕 The main monograph

**AB Cloud Quantum Research: the architecture that reads mathematics and stores
nothing** — the complete account of the program in 43 chapters and appendices:

- the idea and the honesty discipline (pre-registration, blind protocols,
  SHA256 pins, cross-language replication, errata);
- the architecture of levels and their numerical links;
- the spectral core and theorems **Th1–Th6** in detail;
- the obligation machine **V13** and the audit **V14**;
- the AB processor: ISA, exact compilation **V20**, the *reads-does-not-carry*
  previews **V23/V24**;
- the verification platform: blind zero reading **E17**, the independent
  Riemann–Siegel **E16**, the class-B benchmark **E18**;
- the spinor study: models θ = π/2, π/3, π/7 and theorems **TS1–TS3**;
- the full texts of the four level research programs (Part VII);
- the level verdict summaries (Part VIII);
- appendices A–Q: the table of 43 campaigns, flagship numbers, the theorem
  summary, glossaries, pins, verdict excerpts, the referee checklist and more.

Every number in the text traces to a committed verdict file; every figure is
rebuilt from verdicts by the program scripts. The monographs contain **28
figures** at print resolution, **44 tables**, and a clickable table of contents.

## 📗 Research programs

Each level carries its own research program document: goals, methodology, the
executed campaigns with their certificates, the detailed campaign walkthroughs,
the next wave with readiness criteria, the honest boundaries, reproduction
commands and a further-reading map. The programs are chained: P3 (V23) relies
on E17; P4 (V24) on E13/E14; O-J3 on E07 and V21; the spinor study formalizes
"reads, does not carry" for P1.

## 📜 LaTeX sources

The `latex/` folders contain complete, compilable sources generated from the
same content model as the PDF/DOCX versions — one source of truth, three
formats. Compile with `pdflatex` (Russian versions need the `babel` + `T2A`
support shipped with any full TeX distribution):

```bash
cd main_monograph/latex
pdflatex monograph_EN.tex && pdflatex monograph_EN.tex   # twice for the TOC
```

The figures are referenced by relative paths into the repository, so compile
with this folder inside the repository checkout.

## 🧭 Provenance and style

- **Style:** *Critical Line & Copper* — copper `#C96F4A`, teal `#0E7C86`,
  dark warm background on covers; the same identity as the program tiles.
- **Provenance:** no hand-typed numbers. Campaign tables come from
  `datasets/campaign_timeline.csv`; flagship numbers from
  `datasets/flagship_numbers.csv`; verdict excerpts from the committed
  verdict JSON files.
- **License:** this folder duplicates the repository license verbatim —
  the individual proprietary personal license of the author
  (© 2026 Isaev Iskhak Khamzatovich). See [`LICENSE`](LICENSE).

## ✅ How to verify

```bash
# integrity of the whole package (95+ checks)
python3 scripts/validate_package.py

# the campaigns behind appendix A
python3 -c "import csv; [print(r['campaign'], '-', r['title']) for r in csv.DictReader(open('datasets/campaign_timeline.csv'))]"

# the flagship numbers behind appendix B
python3 -c "import csv; [print(r['metric'], '=', r['value']) for r in csv.DictReader(open('datasets/flagship_numbers.csv'))]"
```

## Русская версия

**MONOGRAPH_ARCHIVE** — публикационный слой программы: одна большая основная
монография на русском и английском (DOCX + PDF, 104+ страницы, 28 фигур,
44 таблицы), четыре монографии исследовательских программ уровней и полные
LaTeX-исходники всех десяти документов. Все числа прослеживаются до вердикт-файлов,
все фигуры пересобираются скриптами, лицензия репозитория продублирована
в этой папке дословно. Честная граница неизменна: RH остаётся заблокированным
машиной обязательств V13.

---

<div align="center">

*Собрано дисциплиной: предрегистрация · слепые протоколы · репликация ·
отрицательные результаты публикуются*

**AB Cloud Quantum Research** · MONOGRAPH_ARCHIVE · v1.1.0 · © Исаев И. Х.

</div>
