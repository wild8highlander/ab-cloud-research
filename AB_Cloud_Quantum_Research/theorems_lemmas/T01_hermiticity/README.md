# Th1. Эрмитовость и вещественность спектра — вывод теоремы

**Кампания:** V4 · **Формальная редукция:** A1 (спектральная теорема) · **Документы:**
`theorem_th1_ru.pdf/.docx`, `theorem_th1_en.pdf/.docx` ·
**Фигура:** `figures/th1_4dim_ru.png`, `figures/th1_4dim_en.png`
(плитка 2×2, четыре измерения, 600 dpi)

## Постановка

Для любого набора вихрей, W, α и границ оператор H_L удовлетворяет H_L = H_L†; следовательно spec(H_L) ⊂ ℝ. При α = ½ и W = 0 спектр симметричен: λ ∈ spec ⇒ −λ ∈ spec.

## Идея вывода

Каждая связь вносится парой H[i,j] = −t·e^{iφ}, H[j,i] = −t·e^{−iφ} = conj(H[i,j]) — эрмитовость по построению; диагональ вещественна (вихревой потенциал, беспорядок, стэггерд-масса). Симметрия при W = 0 — двудольность решётки по чётности ix+iy: в этом базисе H = [[0, B], [B†, 0]], и спектр зеркалится относительно нуля.

## Четыре измерения фигуры

a) ‖H−H†‖ по затворам L = 12/16/24/32 — ровно 0.0 (log-шкала); b) невязка вещественности спектра по затворам — ≤ 8.8e−15; c) спаривание λ ↔ −λ — до 8.2e−15; d) остатки собственных пар — ≤ 8.8e−15. Порог ε = 1e−12 отмечен на каждой панели.

## Сертификат и артефакты кампании

test_th1_passport.py (сертификат, Nv = 16/64/256, сид 96); computations/V04_operator_passport/ (монографии, фигуры); verification/claim_audit/claims/claim_v04.json

## Границы (честно)

Th1 ничего не говорит о соответствии спектра нулям ζ (отрицательные вердикты V1, V3, V6, V16). Симметрия λ ↔ −λ нарушается уже при W > 0 и не восстанавливается вихрями.

## English summary

**Statement.** For any set of vortices, W, α and boundaries the operator H_L satisfies H_L = H_L†; hence spec(H_L) ⊂ ℝ. At α = ½ and W = 0 the spectrum is symmetric: λ ∈ spec ⇒ −λ ∈ spec.

**Proof idea.** Every bond is inserted as a pair H[i,j] = −t·e^{iφ}, H[j,i] = −t·e^{−iφ} = conj(H[i,j]) — hermiticity by construction; the diagonal is real. The W = 0 symmetry comes from bipartiteness in ix+iy parity: in that basis H = [[0, B], [B†, 0]] and the spectrum mirrors about zero.

**Figure dimensions.** a) ‖H−H†‖ across gates L = 12/16/24/32 — exactly 0.0 (log scale); b) spectrum-realness residuals ≤ 8.8e−15; c) λ ↔ −λ pairing to 8.2e−15; d) eigenpair residuals ≤ 8.8e−15. The ε = 1e−12 threshold is marked on every panel.

**Boundaries.** Th1 says nothing about matching the spectrum to the ζ zeros: the series' verdicts there are the level identity — YES at the zeros' level (V6/V16, the D_nn bridge, v2.0.7) with the bit-level branch open (V16) and the blind-coding / σ-scan design claims refuted (V1, V3). The λ ↔ −λ symmetry breaks at W > 0 and is not restored by vortices.
