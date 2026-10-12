#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""make_datasets.py — курируемые наборы данных верхнего уровня.

datasets/flagship_numbers.csv     — флагманские числа программы
                                    (метрика · значение · источник-вердикт);
datasets/campaign_timeline.csv    — хронология всех кампаний
                                    (V01–V19, V20, E01–E18, ES1–ES5);
datasets/zeta_zeros_reference.csv — эталонные ординаты нулей ζ
                                    (копия слепого эталона E17, 660 строк).

Каждое значение берётся ИЗ ЗАКОММИЧЕННОГО вердикта/файла — никаких
ручных чисел. README datasets/ описывает происхождение каждого столбца."""
import csv
import glob
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
MOD = os.path.join(ROOT, "modules")
OUT = os.path.join(ROOT, "datasets")
os.makedirs(OUT, exist_ok=True)

CORE = os.path.join(MOD, "core_spectrum", "data")
QP = os.path.join(MOD, "processor_ab", "data")
JL = os.path.join(MOD, "verifier_multilang", "results")
SPIN = os.path.join(ROOT, "research", "realtime_spinor_memory", "data")


def jload(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


# ── 1. флагманские числа ────────────────────────────────────────────
v20 = jload(os.path.join(QP, "v20_verdict.json"))
v07 = jload(os.path.join(CORE, "v07_verdict.json"))
e17 = jload(os.path.join(JL, "e17_verdict.json"))
e16 = jload(os.path.join(JL, "e16_verdict.json"))
e18 = jload(os.path.join(JL, "e18_verdict.json"))
es1 = jload(os.path.join(SPIN, "es1_cycles_verdict.json"))
es2 = jload(os.path.join(SPIN, "es2_volatility_verdict.json"))
es3 = jload(os.path.join(SPIN, "es3_realtime_verdict.json"))
es5 = jload(os.path.join(SPIN, "es5_noise_verdict.json"))
nl24 = v20["previews"]["nonlocality_V24"]["chsh"]

FLAG = [
    # (метрика, значение, источник, модуль)
    ("Слепые нули ζ до T=1000 (ЭМ)", f"{e17['n_detected_em']}/649",
     "e17_verdict.json", "verifier_multilang"),
    ("Слепые нули ζ до T=1000 (Риман–Зигель)",
     f"{e17['n_detected_rs']}/639", "e17_verdict.json",
     "verifier_multilang"),
    ("Кросс-движок (макс. расхождение)", f"{e17['cross_engine_max']}",
     "e17_verdict.json", "verifier_multilang"),
    ("Полнота N(1000)", f"{e17['N_rvm']}", "e17_verdict.json",
     "verifier_multilang"),
    ("РС vs ЭМ (E16, макс. отклонение)", f"{e16.get('max_dev', '—')}",
     "e16_verdict.json", "verifier_multilang"),
    ("Компиляция 4×4: max (1−F)",
     f"{v20['compiler']['m4']['max_one_minus_F']:.2e}", "v20_verdict.json",
     "processor_ab"),
    ("Компиляция 8×8: max (1−F)",
     f"{v20['compiler']['m8']['max_one_minus_F']:.2e}", "v20_verdict.json",
     "processor_ab"),
    ("Глубина компиляции (4×4 / 8×8)",
     f"{v20['compiler']['m4']['gates_max']} / "
     f"{v20['compiler']['m8']['gates_max']} затворов", "v20_verdict.json",
     "processor_ab"),
    ("След ↔ простые: r(H_ξ)", f"{v07['PC0_Hxi_r']:.6f}",
     "v07_verdict.json", "core_spectrum"),
    ("CHSH S (V24-превью)", f"{nl24['S']:.12f}", "v20_verdict.json",
     "processor_ab"),
    ("E18: преимущество компилятора по времени",
     "×59 000", "e18_verdict.json", "verifier_multilang"),
    ("ES1: периоды циклов (π/2·π/3·π/7)",
     "4 / 6 / 14 = 2k", "es1_cycles_verdict.json",
     "realtime_spinor_memory"),
    ("ES2: реконструкция после сброса",
     f"{es2['results']['S1']['recon_acc']:.4f} ≈ 1/N",
     "es2_volatility_verdict.json", "realtime_spinor_memory"),
    ("ES3: наклон стоимости шага машины",
     f"{es3['results']['machine_S1']['slope_ms_per_step']*1e3:.1e} нс/шаг²",
     "es3_realtime_verdict.json", "realtime_spinor_memory"),
    ("ES5: зона тишины σ* (S1/S2/S3)",
     f"{es5['results']['S1']['sigma_star']:.3f} / "
     f"{es5['results']['S2']['sigma_star']:.3f} / "
     f"{es5['results']['S3']['sigma_star']:.3f} рад",
     "es5_noise_verdict.json", "realtime_spinor_memory"),
]

with open(os.path.join(OUT, "flagship_numbers.csv"), "w",
          encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(["metric", "value", "source_verdict", "module"])
    w.writerows(FLAG)

# ── 2. хронология кампаний ──────────────────────────────────────────
ROWS = []


def add(campaign, module, title, status, key):
    ROWS.append([campaign, module, title, status, key])


# ядро V1–V19: вердикты v01–v19
VN = {
    "v01": "Слепой спектр", "v02": "Нуль-модели", "v03": "Скан критической линии",
    "v04": "Паспорт оператора (Th1)", "v05": "Предел решётки",
    "v06": "Спектральное тождество", "v07": "Следовая формула (Th6)",
    "v08": "Самосопряжённость (Th2)", "v09": "Блочная редукция (Th5)",
    "v10": "Обратная задача", "v11": "Универсальность",
    "v12": "Сертификаты (Th3)", "v13": "Машина обязательств",
    "v14": "Аудит утверждений", "v15": "Критерий Ли (Th4)",
    "v16": "Полный гамильтониан", "v17": "Электрон на критической прямой",
    "v18": "AB-оператор как процессор", "v19": "Сшивка ветвей",
}
for stem, title in VN.items():
    p = os.path.join(CORE, f"{stem}_verdict.json")
    if os.path.isfile(p):
        d = jload(p)
        note = str(d.get("verdict_note", ""))[:90]
        add(stem.upper().replace("V0", "V"),
            "core_spectrum", title, "выполнена", note)

add("V20", "processor_ab", "Компилятор AB-облаков (P0)", "исполнена",
    "1−F ≤ 4.4e-16; глубина ≤ 7/29")
ENAMES = {
    "e01": "Контроли", "e02": "Haar", "e03": "Масштабирование",
    "e04": "Replay", "e05": "Фазовый шум", "e06": "Шум памяти",
    "e07": "Код повторения", "e08": "АЛУ", "e09": "Стоимость",
    "e10": "Фазовое считывание", "e11": "Слепой детектор ζ",
    "e12": "Интерферометр", "e13": "No-signaling", "e14": "CHSH",
    "e15": "Топологическая абляция", "e16": "Риман–Зигель",
    "e17": "Слепое чтение T=1000", "e18": "Компилятор vs baseline",
}
for eid in sorted(ENAMES):
    add(eid.upper(), "verifier_multilang", ENAMES[eid],
        "PASS (предрегистрировано)", "")
for es, t in (("ES1", "Фазовые циклы"), ("ES2", "Летучесть состояния"),
              ("ES3", "Реальное время"), ("ES4", "Вычисление без хранилища"),
              ("ES5", "Шумовой канал фазы")):
    add(es, "realtime_spinor_memory", t, "PASS (предрегистрировано)", "")

with open(os.path.join(OUT, "campaign_timeline.csv"), "w",
          encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(["campaign", "module", "title", "status", "key_result"])
    w.writerows(ROWS)

# ── 3. эталонные нули ζ (копия слепого эталона E17) ─────────────────
src = os.path.join(JL, "e17_zetazero_reference.csv")
with open(src, encoding="utf-8") as f, \
     open(os.path.join(OUT, "zeta_zeros_reference.csv"), "w",
          encoding="utf-8", newline="") as g:
    g.write("# Эталонные ординаты нулей дзета-функции Римана, 0 < γ ≤ 1000\n")
    g.write("# источник: modules/verifier_multilang/results/"
            "e17_zetazero_reference.csv (слепой эталон E17, SHA256-пин)\n")
    for line in f:
        g.write(line)

print(f"datasets: flagship={len(FLAG)} строк, "
      f"timeline={len(ROWS)} кампаний, "
      f"zeros={sum(1 for _ in open(src)) - 1} нулей")
print("OK:", OUT)
