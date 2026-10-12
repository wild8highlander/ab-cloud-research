#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""make_whitepaper.py — белый отчёт AB Cloud Quantum Research (RU/EN, PDF).

Компактная витрина всего исследования одним документом (~9 стр):
архитектура, уровни, флагманы, теоремы, дисциплина, спинор-исследование,
дорожная карта. Числа внедряются из закоммиченных вердиктов.
Выход: whitepaper/whitepaper_{ru,en}.pdf (рендер — modules/core_spectrum)."""
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
CORE = os.path.join(ROOT, "modules", "core_spectrum")
MOD = os.path.join(ROOT, "modules")
TMP = os.path.join(ROOT, "whitepaper", "_tmp")
os.makedirs(TMP, exist_ok=True)


def jload(p):
    with open(p, encoding="utf-8") as f:
        return json.load(f)


v20 = jload(os.path.join(MOD, "processor_ab", "data", "v20_verdict.json"))
v07 = jload(os.path.join(MOD, "core_spectrum", "data", "v07_verdict.json"))
e17 = jload(os.path.join(MOD, "verifier_multilang", "results",
                         "e17_verdict.json"))
vm = jload(os.path.join(MOD, "verifier_multilang", "results",
                        "verdicts_master.json"))
es5 = jload(os.path.join(ROOT, "research", "realtime_spinor_memory",
                         "data", "es5_noise_verdict.json"))
m4 = v20["compiler"]["m4"]
m8 = v20["compiler"]["m8"]

FLAG_TABLE = {
    "header": ["Результат" if "ru" else "" , "Числа"],
    "rows": [],
    "ratios": [0.55, 0.45],
}

RU = {
    "meta": {
        "title": "AB Cloud Quantum Research: белый отчёт",
        "subtitle": "Одно исследование: алгебраическая AB-архитектура "
                    "(Aharonov–Bohm) как вычислитель, который читает "
                    "математику в реальном времени и не хранит ничего",
        "author": "Исаев Исхак Хамзатович",
        "affil": "Независимый исследователь, г. Нальчик, КБР",
        "series": "AB Cloud Quantum Research · белый отчёт",
        "volume": "WP", "version": "1.0.0", "date": "2026-10-11",
    },
    "sections": [
        {"h1": "1. Резюме",
         "paras": [
            "AB Cloud Quantum Research — единое исследование вокруг одной "
            "идеи: алгебраическая AB-архитектура (Aharonov–Bohm) как "
            "вычислительная ткань, которая читает математику — от спектров "
            "операторов до нулей дзета-функции — в реальном времени и не "
            "хранит ничего. Исследование построено из четырёх уровней "
            "(ядро → процессор → верификация → вспомогательные модели), "
            "общего формального слоя (Lean 4 / Coq) и слоя теорем, каждая "
            "из которых снабжена сертификатом и плиточной фигурой "
            "«4 измерения».",
            "Флагманские результаты: слепое чтение всех нулей ζ до T = 1000 "
            f"двумя независимыми движками ({e17['n_detected_em']}/649 "
            f"Эйлера–Маклорена + {e17['n_detected_rs']}/639 Римана–Зигеля, "
            f"кросс-движок {e17['cross_engine_max']} побитово); точная "
            f"компиляция унитарной логики в AB-облака с 1−F ≤ "
            f"{m4['max_one_minus_F']:.1e}; следовая формула Гуинанда–Вейля "
            f"с весом простых в тепловом следе H_ξ (r = {v07['PC0_Hxi_r']:.4f}); "
            "нелокальность без сигналинга; и формализованный принцип "
            "«читает, а не несёт» — машина без долговременной памяти.",
         ],
         "table": {
             "header": ["Направление", "Ключевой результат", "Источник"],
             "rows": [
                 ["Слепые нули ζ (E17)",
                  f"{e17['n_detected_em']}+{e17['n_detected_rs']} слепо; "
                  f"N(1000) = {e17['N_rvm']}", "verifier_multilang"],
                 ["Компилятор AB-облаков (V20)",
                  f"1−F ≤ {m4['max_one_minus_F']:.1e} (4×4), "
                  f"{m8['max_one_minus_F']:.1e} (8×8)", "processor_ab"],
                 ["След ↔ простые (V7/Th6)",
                  f"r = {v07['PC0_Hxi_r']:.4f}; контроль 0.76",
                  "core_spectrum"],
                 ["Класс B (E18)",
                  "×59 000 по времени против 5 baseline",
                  "verifier_multilang"],
                 ["Вердикты",
                  f"{len(vm['passes'])} PASS (предрегистрировано)",
                  "verdicts_master"],
             ],
             "ratios": [0.34, 0.42, 0.24],
             "caption": "Таблица 1. Флагманские числа исследования."},
        },
        {"h1": "2. Архитектура: уровни одной машины",
         "paras": [
            "Спектральное ядро (modules/core_spectrum) даёт математику: "
            "оператор H_ξ, кампании V01–V19, теоремы Th1–Th6 и машину "
            "обязательств V13, которая держит вывод RH заблокированным, "
            "пока аналитические предпосылки не доказаны. Процессорный "
            "уровень (modules/processor_ab) исполняет её: ISA AB-облаков, "
            "замкнутая форма компиляции Гивенса-QR и принцип «читает, а не "
            "несёт». Верификационный уровень (modules/verifier_multilang) "
            "перепроверяет оба слоя независимыми движками на Julia: слепые "
            "протоколы с SHA256-пинами, кросс-языковая репликация, "
            f"{len(vm['passes'])} предрегистрированных вердиктов.",
            "Формальный слой фиксирует постановки всех шести теорем в "
            "Lean 4 и Coq (редукции A1–A6, без sorry/admit); слой теорем "
            "делает их читаемыми: 24 документа теорем Th1–Th6 и 12 "
            "документов теорем TS1–TS3, каждый с внедрённой плиточной "
            "фигурой. Вспомогательное исследование realtime_spinor_memory "
            "доводит центральный тезис до трёх явных моделей спинорных "
            "фаз.",
         ]},
        {"h1": "3. Принцип «читает, а не несёт»",
         "paras": [
            "Ключевой тезис программы состоит в том, что вычислитель "
            "AB-архитектуры не нуждается в долговременном хранилище "
            "результатов: нули дзета-функции воспроизводятся из шести "
            "констант следовой формулы в момент запроса (12/12 точно в "
            "V23-превью; 649+639 нулей читаются слепо в E17), а вес "
            "простых Λ(n)/√n доказательно живёт в тепловом следе H_ξ. "
            "Хранение = 0 — это не оптимизация, а архитектурный принцип.",
            "Строгая формулировка вынесена во вспомогательное "
            "исследование: три спинорные фазовые модели (θ = π/2, π/3, "
            "π/7) с единственным летучим регистром. Теорема TS1 "
            "доказывает замкнутость фазовых циклов (N = 2k: 4, 6, 14), "
            "TS2 — необратимость стирания (реконструкция прошлого не выше "
            "уровня случайности 1/N), TS3 — что шаг машины стоит O(1) при "
            "любом t, тогда как вечный журнал несёт Ω(t) и срывает "
            "дедлайны. Жёсткое реальное время и долговременная память "
            "архитектурно несовместимы: летучесть — условие детерминизма.",
         ]},
        {"h1": "4. Дисциплина честности",
         "paras": [
            "Все пороги предрегистрированы и зафиксированы до прогона; "
            "вердикты сравниваются с ними механически. Детекторы и "
            "валидаторы разделены (слепые протоколы), выходы детекторов "
            "пинованы SHA256 до валидации. Кросс-языковая репликация "
            "(Julia BigFloat ↔ Python mpmath, numpy-порты компилятора) "
            "воспроизводит ключевые числа с расхождением 0.0–2.2e-16. "
            "Отрицательные результаты публикуется без ретуши: "
            "ζ-соответствия на решётке НЕ найдены (V1/V3/V6/V16), вихри "
            "ломают Th5, 2q-оптимум KAK недостижим в ISA-классе E18. "
            "Эрратумы публикуются в вердиктах (константы B/C₀ Th6; "
            "γ₁₂; пороги ES2a/ES5a).",
            "Вывод о гипотезе Римана остаётся заблокированным машиной "
            "обязательств V13: программа изучает математическую модель и "
            "не претендует на доказательство RH. Формализация Lean/Coq "
            "гарантирует эту блокировку, а не снимает её.",
         ]},
        {"h1": "5. Витрина и дорожная карта",
         "paras": [
            "Витрина исследования: атлас флагманов (atlas/, плитка 2×2), "
            "хронология 43 кампаний (timeline/), курируемые датасеты "
            "(datasets/), глоссарий (glossary/), три веб-лаборатории "
            "(портал web_lab/ + 10 вкладок ядра + 8 вкладок процессора). "
            "Все вычисления в лабораториях исполняются локально в "
            "браузере.",
            "Дорожная карта сцеплена: процессор P1 память (V21) → P2 АЛУ "
            "(V22) → P3 чтение (V23) → P4 нелокальность (V24) → P5 "
            "бенчмарки → P6 Datasheet 1.0; верификация O-J3 (QEC-память) "
            "→ O-J4 (цифровой двойник) → O-J5; ядро — остаток сшивки V19 "
            "(r_align ≤ 0.135) и монодромия ζ; спинор-исследование — фазы "
            "θ = π/k для k > 7 и компиляция задач в фазовые циклы.",
         ],
         "figure": {
             "path": "../../atlas/atlas_flagships_{lang}.png",
             "caption": ("Рис. 1. Атлас флагманов: слепое чтение нулей ζ, "
                         "точный компилятор, след ↔ простые, нелокальность "
                         "(плитка 2×2, 600 dpi, из закоммиченных вердиктов).")},
        },
    ],
}

RU["sections"][0]["table"]["header"] = ["Результат", "Числа", "Модуль"]

EN = {
    "meta": {
        "title": "AB Cloud Quantum Research: White Paper",
        "subtitle": "One study: the algebraic AB (Aharonov–Bohm) "
                    "architecture as a computing fabric that reads "
                    "mathematics in real time and stores nothing",
        "author": "Isaev Iskhak Khamzatovich",
        "affil": "Independent researcher, Nalchik, KBR",
        "series": "AB Cloud Quantum Research · white paper",
        "volume": "WP", "version": "1.0.0", "date": "2026-10-11",
    },
    "sections": [
        {"h1": "1. Executive summary",
         "paras": [
            "AB Cloud Quantum Research is a single study built around one "
            "idea: the algebraic AB (Aharonov–Bohm) architecture as a "
            "computing fabric that reads mathematics — from operator "
            "spectra to zeta zeros — in real time and stores nothing. The "
            "study is organized in four levels (core → processor → "
            "verification → supplementary models), a shared formal layer "
            "(Lean 4 / Coq) and a theorem layer, every theorem carrying a "
            "certificate and a 2×2 four-dimension tile.",
            "Flagship results: blind reading of all ζ zeros up to T = 1000 "
            f"by two independent engines ({e17['n_detected_em']}/649 "
            f"Euler–Maclaurin + {e17['n_detected_rs']}/639 "
            f"Riemann–Siegel, cross-engine {e17['cross_engine_max']} "
            "bit-exact); exact compilation of unitary logic into AB clouds "
            f"with 1−F ≤ {m4['max_one_minus_F']:.1e}; the Guinand–Weil "
            "trace formula with the prime weight living in the heat trace "
            f"of H_ξ (r = {v07['PC0_Hxi_r']:.4f}); no-signaling "
            "nonlocality; and the formalized 'reads, does not carry' "
            "principle — a machine with no long-term memory.",
         ],
         "table": {
             "header": ["Result", "Numbers", "Module"],
             "rows": [
                 ["Blind ζ zeros (E17)",
                  f"{e17['n_detected_em']}+{e17['n_detected_rs']} blind; "
                  f"N(1000) = {e17['N_rvm']}", "verifier_multilang"],
                 ["AB-cloud compiler (V20)",
                  f"1−F ≤ {m4['max_one_minus_F']:.1e} (4×4), "
                  f"{m8['max_one_minus_F']:.1e} (8×8)", "processor_ab"],
                 ["Trace ↔ primes (V7/Th6)",
                  f"r = {v07['PC0_Hxi_r']:.4f}; control 0.76",
                  "core_spectrum"],
                 ["Class B (E18)",
                  "×59,000 in time vs 5 baselines", "verifier_multilang"],
                 ["Verdicts",
                  f"{len(vm['passes'])} PASS (pre-registered)",
                  "verdicts_master"],
             ],
             "ratios": [0.34, 0.42, 0.24],
             "caption": "Table 1. Flagship numbers of the study."},
        },
        {"h1": "2. Architecture: the levels of one machine",
         "paras": [
            "The spectral core (modules/core_spectrum) supplies the "
            "mathematics: the operator H_ξ, campaigns V01–V19, theorems "
            "Th1–Th6, and the V13 obligation machine keeping the RH "
            "conclusion blocked until the analytic prerequisites are "
            "proved. The processor level (modules/processor_ab) executes "
            "it: the AB-cloud ISA, the closed-form Givens-QR compiler, and "
            "the 'reads, does not carry' principle. The verification level "
            "(modules/verifier_multilang) re-checks both layers with "
            "independent Julia engines: blind SHA-pinned protocols, "
            f"cross-language replication, {len(vm['passes'])} "
            "pre-registered verdicts.",
            "The formal layer pins the statements of all six theorems in "
            "Lean 4 and Coq (reductions A1–A6, no sorry/admit); the "
            "theorem layer makes them readable: 24 documents for Th1–Th6 "
            "and 12 for TS1–TS3, each with an embedded four-dimension "
            "tile. The supplementary study realtime_spinor_memory reduces "
            "the central claim to three explicit spinor phase models.",
         ]},
        {"h1": "3. 'Reads, does not carry'",
         "paras": [
            "The key claim is that the AB-architecture computer needs no "
            "long-term storage of results: ζ zeros are reproduced from six "
            "constants of the trace formula at request time (12/12 exactly "
            "in the V23 preview; 649+639 zeros read blindly in E17), and "
            "the prime weight Λ(n)/√n provably lives in the heat trace of "
            "H_ξ. Storage = 0 is not an optimization but an architectural "
            "principle.",
            "The strict formulation lives in the supplementary study: "
            "three spinor phase models (θ = π/2, π/3, π/7) with a single "
            "volatile register. Theorem TS1 proves phase cycles close "
            "(N = 2k: 4, 6, 14), TS2 — that erasure is irreversible "
            "(reconstruction no better than the chance level 1/N), TS3 — "
            "that the machine step costs O(1) for all t while an eternal "
            "log carries Ω(t) and misses deadlines. Hard real time and "
            "long-term memory are architecturally incompatible: "
            "volatility is the condition of determinism.",
         ]},
        {"h1": "4. The honesty discipline",
         "paras": [
            "All thresholds are pre-registered and fixed before the run; "
            "verdicts compare mechanically. Detectors and validators are "
            "separated (blind protocols), detector outputs are SHA256-"
            "pinned before validation. Cross-language replication (Julia "
            "BigFloat ↔ Python mpmath, numpy ports of the compiler) "
            "reproduces the key numbers with 0.0–2.2e-16 disagreement. "
            "Negative results are published without retouching: lattice "
            "ζ-correspondences are NOT found (V1/V3/V6/V16), vortices "
            "break Th5, the 2q KAK optimum is unreachable in the E18 "
            "ISA class. Errata are published in verdicts (B/C₀ of Th6; "
            "γ₁₂; ES2a/ES5a thresholds).",
            "The conclusion about the Riemann hypothesis remains blocked "
            "by the V13 obligation machine: the program studies a "
            "mathematical model and claims no proof of RH. The Lean/Coq "
            "formalization guarantees this blocking rather than removing "
            "it.",
         ]},
        {"h1": "5. Showcase and roadmap",
         "paras": [
            "The showcase: the flagship atlas (atlas/, a 2×2 tile), the "
            "timeline of 43 campaigns (timeline/), curated datasets "
            "(datasets/), a glossary (glossary/), and three web "
            "laboratories (the web_lab/ portal + 10 core tabs + 8 "
            "processor tabs). All laboratory computations run locally in "
            "the browser.",
            "The roadmap is chained: processor P1 memory (V21) → P2 ALU "
            "(V22) → P3 reading (V23) → P4 nonlocality (V24) → P5 "
            "benchmarks → P6 Datasheet 1.0; verification O-J3 (QEC "
            "memory) → O-J4 (digital twin) → O-J5; core — the remainder "
            "of V19 stitching (r_align ≤ 0.135) and ζ monodromy; the "
            "spinor study — phases θ = π/k for k > 7 and task compilation "
            "into phase cycles.",
         ],
         "figure": {
             "path": "../../atlas/atlas_flagships_{lang}.png",
             "caption": ("Fig. 1. The flagship atlas: blind ζ-zero reading, "
                         "the exact compiler, trace ↔ primes, nonlocality "
                         "(2×2 tile, 600 dpi, from committed verdicts).")},
        },
    ],
}


def main():
    n = 0
    for lang, doc in (("ru", RU), ("en", EN)):
        jp = os.path.join(TMP, f"whitepaper_{lang}.json")
        with open(jp, "w", encoding="utf-8") as f:
            json.dump(doc, f, ensure_ascii=False, indent=1)
        out = os.path.join(ROOT, "whitepaper", f"whitepaper_{lang}.pdf")
        subprocess.run([sys.executable,
                        os.path.join(CORE, "scripts", "render_pdf.py"),
                        jp, out, lang], check=True)
        os.remove(jp)
        n += 1
    os.rmdir(TMP)
    print(f"WHITEPAPER DONE: {n} PDF")


if __name__ == "__main__":
    main()
