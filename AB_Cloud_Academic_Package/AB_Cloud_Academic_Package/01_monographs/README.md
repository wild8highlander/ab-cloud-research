# 01_monographs — the unified monograph

One monograph consolidates the whole programme: ten levels (spectral core, AB processor,
Dirac skeleton, Hilbert–Pólya bridge, blind verification + heritage, spinor study,
Meridian observatory, vortex optimization, wave attractors), one verdict ledger,
one honesty layer. Two editions per full-volume language:

| Edition | What it is |
|---|---|
| **Regular volume** (RU/EN) | the compressed scientific record — every number names its campaign |
| **MAX edition** (RU/EN) | the full-depth archive edition (~100,000 words each): every campaign, every test with console listings, every log extract, every table, every figure — the whole path to every number |

| Language | Status | Files |
|---|---|---|
| [Русский](ru/README.md) | **full volume** + **MAX edition** | `monograph_ru.{md,pdf,docx}` · `monograph_ru_max.{md,pdf,docx}` |
| [English](en/README.md) | **full volume** + **MAX edition** | `monograph_en.{md,pdf,docx}` · `monograph_en_max.{md,pdf,docx}` |
| [中文](zh/README.md) | abstract + TOC + key numbers | `README.md` |
| [Deutsch](de/README.md) | Abstract + Inhalt + Kernzahlen | `README.md` |
| [Español](es/README.md) | Resumen + índice + cifras | `README.md` |
| [Français](fr/README.md) | Résumé + sommaire + chiffres | `README.md` |
| [العربية](ar/README.md) | ملخص + فهرس + أرقام | `README.md` |

## Sources consolidated

The unified monograph was written anew from the source laboratories' records (their
monographs remain canonical in their folders): the narrative centre of the package is
the regular volume; the MAX edition additionally includes the sources' full records
(the vortex README, the wave-attractor README, the observatory's eight documents,
the v19 final report and logs) as verbatim chapters. Every number names its campaign;
the machine-readable register is [`../02_data/processed/research_registry.json`](../02_data/processed/research_registry.json).

## Templates

[`_templates/`](_templates/README.md) holds the chapter, figure, table and
bibliography templates for future translations and extensions.

## Build

```bash
bash ../../06_code/scripts/build_monograph.sh   # PDF (tectonic) + DOCX (pandoc)
```
