# Original Author Monograph v21 — with Verification (RU + EN Edition)

This folder preserves the **original author monograph** (v21) exactly as supplied,
together with its **full English edition**. It complements the rewritten trilingual
v22 monographs (`../../ru`, `../../en`, `../../zh`) — the v22 editions were written
from scratch on top of the verified 37-test suite; this folder keeps the author's
original text with its own analytical interpretations and verification code.

## Состав / Contents

| Путь / Path | Описание / Description |
|---|---|
| `ru/text/AB_Cloud_Monograph_v21_RU_with_Verification.docx` | Оригинальная монография (русский, DOCX с рисунками) |
| `ru/text/AB_Cloud_Monograph_v21_RU_with_Verification.pdf` | PDF-версия оригинала |
| `ru/text/AB_Cloud_Monograph_v21_RU.html` | Интерактивная HTML-версия (липкая навигация, MathJax-совместимая разметка, лайтбокс для рисунков) |
| `ru/text/monograph_v21_RU.md` | Исходник в Markdown (для diff и цитирования) |
| `ru/presentation/AB_Cloud_Monograph_v21_RU_presentation.pptx` | Презентация, 16 слайдов (тёмная научная тема) |
| `en/text/AB_Cloud_Monograph_v21_EN_with_Verification.docx` | English edition (full translation of the v21 monograph) |
| `en/text/AB_Cloud_Monograph_v21_EN_with_Verification.pdf` | PDF of the English edition |
| `en/text/AB_Cloud_Monograph_v21_EN.html` | Interactive HTML (English edition) |
| `en/text/monograph_v21_EN.md` | Markdown source (English edition) |
| `en/presentation/AB_Cloud_Monograph_v21_EN_presentation.pptx` | Presentation, 16 slides (dark scientific theme) |
| `media/` | Общие рисунки монографии (на них ссылаются HTML и MD: `../../media/imageNN.png`) |

## Ключевые результаты монографии / Key results

- Тест Монтгомери: KS = 0.047, p = 0.27 (N = 500 сертифицированных нулей ζ, mpmath) — H₀ не отвергается;
- из 64 спинорных структур квартики Клейна только idx=38 даёт GUE-согласие (p = 0.598), пермутационный тест Z = 14.10;
- GUE-статистика не зависит от геометрии подложки (тор и поверхность Клейна дают ⟨r⟩ ≈ 0.937);
- GUE-оптимальность критической прямой: σ = 1/2 → KS = 0.152 (минимум);
- вихрь q = +1 при α = 1/2 — линейная дисперсия E(k) (дираковский конус, v_F ≈ 0.125).

Author: Isaev Iskhak Khamzatovich · ORCID 0009-0003-7299-0701 · DOI 10.5281/zenodo.21825394

## Как цитировать / How to cite

Cite the v22 editions for the verified numerics (`docs/ab-cloud-v22/{ru,en,zh}`),
and this folder for the original author narrative and the V01–V115 verification
runs (Appendix F).
