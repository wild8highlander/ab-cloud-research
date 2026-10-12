#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""content/parts_theorems_v2.py — том теорем v2.0 (T11–T18), ru+en."""

AUTHOR_RU = "Исаев Исхак Хамзатович"
AFFIL_RU = "Независимый исследователь, Нальчик, КБР"
AUTHOR_EN = "Ishak Khamzatovich Isaev"
AFFIL_EN = "Independent researcher, Nalchik, KBR"
DATE = "12 октября 2026 / October 12, 2026"

_T = [
 ("T11", "Уникальность теплового следа / Heat-trace uniqueness",
  "Если Tr e^{−xH} = (1/π)∫₀^∞ Q(a)sin(ax)da для всех x > 0, где "
  "Q(a) = Σ_{γ>0} 2a/(a²+γ²), то spec H = {±γ_n} (с кратностями). "
  "Доказательство: обе стороны — преобразования Лапласа–Стилтьеса; "
  "единственность меры; (1/π)∫2a sin(ax)/(a²+γ²)da = e^{−xγ}.",
  "If Tr e^{−xH} = (1/π)∫₀^∞ Q(a)sin(ax)da for all x > 0, where "
  "Q(a) = Σ_{γ>0} 2a/(a²+γ²), then spec H = {±γ_n} with multiplicity. "
  "Proof: both sides are Laplace–Stieltjes transforms; uniqueness of the "
  "measure; the per-zero identity.",
  "доказано / proven"),
 ("T12", "Классификация ко-локации / Co-location classification",
  "Системы фаз с Φ_pq ≡ Φ_p + Φ_q (mod 2π) — гомоморфизмы ⟨p⟩ → ℝ/2πℤ; "
  "нормальная форма Φ_p = 2π{β ln p}. Системы со значениями {0, π} "
  "калибровочно тривиальны в оверлей-канале (ψ → (−1)^y ψ).",
  "Phase systems with Φ_pq ≡ Φ_p + Φ_q (mod 2π) are homomorphisms "
  "⟨p⟩ → ℝ/2πℤ; normal form Φ_p = 2π{β ln p}. {0, π}-valued systems are "
  "gauge-trivial in the overlay channel (ψ → (−1)^y ψ).",
  "доказано+измерено / proven+measured (4.4e-16; 8.4e-15)"),
 ("T13", "Счётный закон α=1/3 / α=1/3 counting law",
  "N₀ = 2L − 6·[L ≡ 0 (mod 12)] при L ≡ 0 (mod 6); иначе N₀ = 0. Индекс "
  "Σ sign(ε) = −2·[L ≡ 0 (mod 12)]. Решающие проверки: L=36→66, L=48→90.",
  "N₀ = 2L − 6·[L ≡ 0 (mod 12)] for L ≡ 0 (mod 6); else N₀ = 0. Index "
  "Σ sign(ε) = −2·[L ≡ 0 (mod 12)]. Decisive checks: L=36→66, L=48→90.",
  "измерено (закон) / measured (law)"),
 ("T14", "Полоса T=5000 / Band T=5000",
  "RH верифицирована в полосе T ≤ 5000: N_online = N_strip = 4520, "
  "N̄ = 4520.08, S_max = 0.91 ≤ 2, якоря v1 воспроизведены.",
  "RH verified in the band T ≤ 5000: N_online = N_strip = 4520, "
  "N̄ = 4520.08, S_max = 0.91 ≤ 2, v1 anchors reproduced.",
  "измерено / measured"),
 ("T15", "Демаркация слепых семейств / Blind demarcation",
  "20 затворов 5 новых семейств (вне пространства ручек v1) — все в "
  "нулевой зоне (|r_H7| ≤ 0.040) при PC0' = 1.000.",
  "20 gates from 5 new families (outside the v1 handle space) — all in "
  "the null zone (|r_H7| ≤ 0.040) with PC0' = 1.000.",
  "измерено / measured"),
 ("T16", "Таксономия аттрактора / Attractor taxonomy",
  "Скан 121 конфигурации: 97 GUE / 18 интегрируемых (Nv=0) / 6 "
  "промежуточных (Nv≤8, q=0.5, ⟨r⟩=0.47–0.53); ранговых выбросов нет.",
  "Scan of 121 configurations: 97 GUE / 18 integrable (Nv=0) / 6 "
  "intermediate (Nv≤8, q=0.5, ⟨r⟩=0.47-0.53); no rank outliers.",
  "измерено / measured"),
 ("T17", "Скрученная следовая формула / Twisted trace formula",
  "K_χ(x) = Σe^{−xγ_χ} = (1/π)∫Q_χ(a)sin(ax)da, Q_χ = Λ'/Λ(½+a,χ) − B_χ "
  "− C₀^χ, C₀^χ = Λ'/Λ(½) − B_χ; несёт χ(n)Λ(n)/√n. Верификация: "
  "|ΔK| ≤ 9.6e-6 (χ₅), 6.1e-6 (χ₇).",
  "K_χ(x) = Σe^{−xγ_χ} = (1/π)∫Q_χ(a)sin(ax)da, Q_χ = Λ'/Λ(½+a,χ) − B_χ "
  "− C₀^χ, C₀^χ = Λ'/Λ(½) − B_χ; carries χ(n)Λ(n)/√n. Verified to "
  "|ΔK| ≤ 9.6e-6 (χ5), 6.1e-6 (χ7).",
  "доказано+верифицировано / proven+verified"),
 ("T18", "Квантовое эхо локальности / Quantum echo of locality",
  "Фермионная запутанность морского уголка затвора подавлена локальностью "
  "(S_A ≈ 12–16 нат против 160–220 у Haar-базы, z > 100); MI-профиль не "
  "несёт нулевой подписи (−0.018 vs −0.121 случайная).",
  "The gate's Fermi-sea fermionic entanglement is suppressed by locality "
  "(S_A ≈ 12-16 nats vs 160-220 Haar baseline, z > 100); the MI profile "
  "carries no zero signature (−0.018 vs −0.121 random).",
  "измерено / measured"),
]


def _doc(lang):
    ru = lang == "ru"
    sections = [{"h1": "Обозначения / Notation" if not ru else "Обозначения",
                 "paras": ["γ_n — ординаты нулей дзеты; Λ(n) — функция фон "
                           "Мангольдта; Φ_p — поток простых; Q(a), K(x) — "
                           "стороны явной формулы (см. docs/trace_formula.md "
                           "v1); ε — стаггерд-структура; L — размер решётки."
                           if ru else
                           "γ_n — zeta zero ordinates; Λ(n) — von Mangoldt "
                           "function; Φ_p — prime flow; Q(a), K(x) — sides "
                           "of the explicit formula (see docs/trace_formula.md "
                           "v1); ε — staggered structure; L — lattice size."]}]
    for tid, title, ru_t, en_t, status in _T:
        sections.append({
            "h1": f"{tid}. {title if ru else title.split(' / ')[-1]}",
            "theorem": {"label": f"Теорема {tid}." if ru else f"Theorem {tid}.",
                        "text": ru_t if ru else en_t,
                        "proof": "См. монографию v2.0, соответствующая глава; "
                                 "полные выводы — в computations/C*/README и "
                                 "docs/v2/." if ru else
                                 "See monograph v2.0, the corresponding "
                                 "chapter; full derivations in "
                                 "computations/C*/README and docs/v2/."},
            "paras": [f"Статус: {status}." if ru else f"Status: {status}."]})
    meta = {"title": "Теоремы v2.0 (T11–T18)" if ru else
            "Theorems v2.0 (T11–T18)",
            "subtitle": "Hilbert Polya Bridge · v2.0 «The Operator That "
                        "Almost Exists»",
            "author": AUTHOR_RU if ru else AUTHOR_EN,
            "affil": AFFIL_RU if ru else AFFIL_EN,
            "series": "Hilbert Polya Bridge · theorems volume v2",
            "volume": "theorems_v2", "version": "2.0.0", "date": DATE}
    return {"meta": meta, "sections": sections}


RU = _doc("ru")
EN = _doc("en")
DOCS = {"theorems_v2_ru": RU, "theorems_v2_en": EN}
