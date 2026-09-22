# Original Author Monograph v21 — with Verification (RU + EN) and the v21.1 Corrections

This folder preserves the **original author monograph** (v21) exactly as
supplied, together with its **full English edition**, the 16-slide decks, the
shared figure media — and, since v1.1.0, the **corrected v21.1 editions**
that carry the errata note. The v21 text carries the
author's own analytical interpretations and the V01–V115 verification-runs
narrative (Appendix F); the rewritten v22 editions
(`../../ru`, `../../en`, `../../zh`) are independent works sharing the same
verified numerics.

## Contents

| Path | Description |
|---|---|
| `ru/text/AB_Cloud_Monograph_v21_RU_with_Verification.docx` | original monograph, Russian (DOCX with figures) |
| `ru/text/AB_Cloud_Monograph_v21_RU_with_Verification.pdf` | PDF of the original |
| `ru/text/AB_Cloud_Monograph_v21_RU.html` | interactive HTML (sticky TOC, lightbox) |
| `ru/text/monograph_v21_RU.md` | Markdown source — **updated in v21.1** with the errata note |
| `ru/presentation/AB_Cloud_Monograph_v21_RU_presentation.pptx` | 16-slide deck (dark scientific theme) |
| `en/text/AB_Cloud_Monograph_v21_EN_with_Verification.docx` | full English edition |
| `en/text/AB_Cloud_Monograph_v21_EN_with_Verification.pdf` | PDF of the English edition |
| `en/text/AB_Cloud_Monograph_v21_EN.html` | interactive HTML (English) |
| `en/text/monograph_v21_EN.md` | Markdown source, English — updated in v21.1 |
| `en/presentation/AB_Cloud_Monograph_v21_EN_presentation.pptx` | 16-slide deck (English) |
| `ru/text/monograph_v21_RU_corrected.{docx,html,pdf}` | **v21.1 corrected Russian edition** |
| `en/text/monograph_v21_EN_corrected.{docx,html,pdf}` | **v21.1 corrected English edition** |
| `media/` | 73 shared figure images referenced by the HTML/MD files as `../../media/imageNN.png` |

## Key claims of the original v21 (as supplied)

- Montgomery test: KS = 0.047, p = 0.27 (N = 500 certified mpmath zeros) —
  H₀ not rejected;
  below;
- GUE statistics independent of substrate geometry (torus vs Klein surface
  give ⟨r⟩ ≈ 0.937);
- GUE-optimality of the critical line: σ = 1/2 → KS = 0.152 (minimum);
- vortex q = +1 at α = 1/2 — linear dispersion E(k) (Dirac cone,
  v_F ≈ 0.125).

## v21.1 corrections (2026-09-03) — what exactly changed

The full verification run over ALL 64 spinor structures
(`verification/spinor64/`) showed that **all 64 structures give
GUE-consistent statistics**: PSL(2,7) orbits 28/21/7/7/1, exact
isospectrality within orbits (max|Δλ| ≈ 9·10⁻¹⁵), ⟨r⟩ = 0.5984 ± 0.0035 in
the AB-cloud model. Therefore:

1. **Errata note** added at the top of both `.md` sources;
4. the transposed orbit counts 28/36 in the appendices were fixed.

The pre-correction files (`AB_Cloud_Monograph_v21_*`) are kept unchanged for
reference. Internal inconsistency of v21: by its own formula

## Which file to use

- *Original narrative, untouched* → `*_with_Verification.{docx,pdf}`;
- *Citing the corrected state* → `*_corrected.{docx,html,pdf}` (v21.1);
- *Slide decks* → `*/presentation/*_presentation.pptx`.

## Кратко (по-русски)

- Каталог хранит оригинальную монографию автора v21 (RU + полное EN издание,
  16-слайдовые презентации, общие рисунки в media/).
  приложениях; исправленные сборки — `*_corrected.{docx,html,pdf}`.
- Оригинальные файлы оставлены без изменений для истории; цитировать
  исправленные издания.

## 📁 Complete file inventory

| Entry | Size | Kind |
|---|---|---|
| `en/` | 9 files, 90.9 MB | directory |
| `media/` | 74 files, 17.4 MB | directory |
| `ru/` | 9 files, 77.4 MB | directory |
| `README.md` | 4.2 KB | file |
| **Total (recursive)** | **93 files, 185.7 MB** | |

## 🔬 Deep dive — provenance, and what exactly v21.1 corrects

This folder is the project's **historical layer** and is kept byte-faithful
to what the author supplied. The v21 text narrates the discovery path in
its own voice: Appendix F walks through verification runs V01–V115 — the
iteration sequence in which the AB-cloud model, the GUE comparison
protocol and the objection tests took shape. Alongside the Russian
original and its full English edition, the folder stores the 16-slide
decks, the shared figure media consumed by both editions, and the
stylesheet `mono.css` that the pandoc HTML builds of **all** monograph
editions still use — which is why deleting this folder would break the
rebuild chain of the newer texts too.

The **v21.1 corrections** are minimal by design. The single withdrawn
quartic are GUE-consistent, that the PSL(2,7) orbit structure is
28/21/7/7/1 with exact isospectrality at the 1e-14 level, and that the
`*_corrected.*` suffix, patch §3.2.5 accordingly, and change nothing
else; if you need the physics as currently verified, cite the v22/v22.1
editions, and reach for this folder when you need the author's original
narrative or the exact wording of the withdrawn claim.

## Кратко (по-русски)

- Папка — исторический слой: авторский текст v21 (RU+EN), Приложение F
  с прогонами V01–V115, слайды, общие рисунки и `mono.css`, которым
  пользуются и новые издания.
- v21.1 = минимальная правка исходного текста (примечание об ошибках),
  остальное без изменений.
- Для физики цитируем v22/v22.1; для истории и точной формулировки
  снятого тезиса — эту папку.
