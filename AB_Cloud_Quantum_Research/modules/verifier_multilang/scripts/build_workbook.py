#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""build_workbook.py — рабочая книга ABQP_Julia_Research_Program v0.4.0
(7 листов: Overview / Verdicts / E11_zeros / E17_zeros / E18_baselines /
CrossLang / Prereg)."""
import csv
import json
import os

from openpyxl import Workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RES = os.path.join(ROOT, "results")
OUT = os.path.join(ROOT, "tables")
os.makedirs(OUT, exist_ok=True)

HDR_FILL = PatternFill("solid", fgColor="3B4F58")
HDR_FONT = Font(color="FFFFFF", bold=True, size=10)
ALT_FILL = PatternFill("solid", fgColor="EBEDEE")
PASS_FILL = PatternFill("solid", fgColor="D8EAD3")
FAIL_FILL = PatternFill("solid", fgColor="F4CCCC")
THIN = Side(style="thin", color="C7D3D9")
BORDER = Border(left=THIN, right=THIN, top=THIN, bottom=THIN)
WRAP = Alignment(vertical="top", wrap_text=True)


def read_csv(name):
    with open(os.path.join(RES, name + ".csv"), newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))


def sheet_from_rows(ws, header, rows, widths=None):
    ws.append(header)
    for c in range(1, len(header) + 1):
        cell = ws.cell(row=1, column=c)
        cell.fill = HDR_FILL
        cell.font = HDR_FONT
        cell.border = BORDER
        cell.alignment = Alignment(vertical="center", horizontal="center",
                                   wrap_text=True)
    for i, row in enumerate(rows, start=2):
        for c, v in enumerate(row, start=1):
            cell = ws.cell(row=i, column=c, value=v)
            cell.border = BORDER
            cell.alignment = WRAP
            if i % 2 == 0:
                cell.fill = ALT_FILL
    for c in range(1, len(header) + 1):
        ws.column_dimensions[get_column_letter(c)].width = (
            widths[c - 1] if widths else 22)
    ws.freeze_panes = "A2"


wb = Workbook()

# ── Лист 1: Overview ─────────────────────────────────────────────
ws = wb.active
ws.title = "Overview"
master = json.load(open(os.path.join(RES, "verdicts_master.json")))
summary = json.load(open(os.path.join(RES, "summary.json")))
rows = [
    ["ABQP Julia Research Program", "v0.4.0 (исполнение E01–E18; O-J1 + O-J2)", ""],
    ["Дата прогона (UTC)", summary.get("run_utc", ""), ""],
    ["Julia", summary.get("julia", ""), ""],
    ["Все предрегистрированные PASS", master["all_pre_registered_pass"], ""],
    ["", "", ""],
    ["Ключевые метрики", "значение", ""],
    ["E02 max(1−F) 4×4 (seed 96)", "4.4e−16", "порог 1e−12"],
    ["E03 наклон масштабирования b", round(summary["e03_slope_b"], 3),
     "CI95 [2.63, 3.25] — O(d³)"],
    ["E04 байт-в-байт реплей", summary["e04_byte_exact_replay"], ""],
    ["E05 σ* (p95 бюджет 1e−8)", "1e−5 рад", ""],
    ["E09 ошибки полного перебора", 0, "n=2..8, 87380 входов"],
    ["E11 найдено нулей", summary["e11_n_detected"], "[0.3, 60]"],
    ["E11 max |Δγ| к mpmath.zetazero", "1.42e−14", "Гаусс–Ньютон: 0"],
    ["E11 N(60) Риман–Мангольдт", round(summary["e11_N_rvm"], 12), "= 13"],
    ["E12 макс. невязка интерферометра", "6.7e−16", ""],
    ["E13 worst no-signaling D", "6.2e−16", "контроль CNOT ≥ 0.062"],
    ["E14 S Монте-Карло (10⁶)", round(summary["e14_S_sampled"], 6),
     "0.48σ от 2√2; LHV max = 2"],
    ["E15 M1 / M3 полный / M3 полу", "3.6e−16 / 1.1e−16 / 0.309",
     "абляция 0; линейный контроль 0.309"],
    ["Кросс-язык: max |Δγ| py↔jl", 0.0, "побитовое совпадение"],
    ["E16 согласие RS↔ЭМ (сетка+бенчмарк)", "3.8e−15 / 3.1e−17", "порог 1e−9"],
    ["E16 RS быстрее ЭМ при t=10000", "25.2 мс против 1.0 мс", "кроссовер ≈ t≈500"],
    ["E17 найдено нулей (ЭМ / РС)", "649 / 639", "[0.3,1000] / [50,1000]"],
    ["E17 max |Δγ| к mpmath.zetazero", "3.0e−10 (Гаусс–Ньютон)", "порог 1e−9; детектор 2.3e−13"],
    ["E17 кросс-движок (ЭМ ↔ РС)", "0.0", "побитово"],
    ["E17 N(1000) принцип аргумента", 649.0, "= числу найденных"],
    ["E17 слепая репликация Python [900,960]", "48/48 нулей", "max |Δ| = 2.3e−13"],
]
sheet_from_rows(ws, ["Параметр", "Значение", "Примечание"], rows,
                [42, 30, 34])

# ── Лист 2: Verdicts ─────────────────────────────────────────────
ws2 = wb.create_sheet("Verdicts")
vrows = []
for k in sorted(master["passes"]):
    vd = json.load(open(os.path.join(RES, f"{k}_verdict.json")))
    vrows.append([k.upper(), master["passes"][k],
                  vd.get("pre_registered", ""),
                  vd.get("does_not_prove", "")])
sheet_from_rows(ws2, ["Эксперимент", "PASS", "Предрегистрированный критерий",
                      "Не доказывает"], vrows, [14, 9, 60, 52])
for i in range(2, len(vrows) + 2):
    ws2.cell(row=i, column=2).fill = (PASS_FILL if ws2.cell(row=i, column=2).value
                                      else FAIL_FILL)

# ── Лист 3: E11_zeros ────────────────────────────────────────────
ws3 = wb.create_sheet("E11_zeros")
mrows = []
for r in read_csv("experiment_11_matched"):
    mrows.append([int(r["experiment"]) if False else None, float(r["gamma_reference"]),
                  float(r["gamma_detected"]), float(r["delta"])])
val = {r["quantity"]: r["value"] for r in read_csv("experiment_11_validation")}
mrows = [[i + 1, float(r["gamma_reference"]), float(r["gamma_detected"]),
          float(r["delta"])] for i, r in enumerate(read_csv("experiment_11_matched"))]
sheet_from_rows(ws3, ["№", "γ (mpmath.zetazero)", "γ (детектор, слепо)", "Δ"],
                mrows, [6, 24, 24, 14])
r0 = len(mrows) + 3
meta = [("precision", val.get("precision")), ("recall", val.get("recall")),
        ("max_position_error", val.get("max_position_error")),
        ("gauss_newton_max_error", val.get("gauss_newton_max_error_vs_reference")),
        ("N(60) Риман–Мангольдт", val.get("N_rvm")),
        ("SHA256 выхода детектора",
         open(os.path.join(RES, "e11_detector_sha256.txt")).read().strip())]
ws3.cell(row=r0, column=1, value="Валидация").font = Font(bold=True)
for i, (k, v) in enumerate(meta, start=1):
    ws3.cell(row=r0 + i, column=1, value=k)
    ws3.cell(row=r0 + i, column=2, value=str(v))

# ── Лист 4: E17_zeros ────────────────────────────────────────────
ws35 = wb.create_sheet("E17_zeros")
m17 = []
import csv as _csv
with open(os.path.join(RES, "experiment_17_matched_em.csv"), newline='') as _f:
    _rows17 = list(_csv.DictReader(_f))
# показываем каждые 25-й нуль + первые 13 + последние 5 (компактность)
_idx = list(range(0, 13)) + list(range(13, len(_rows17), 25)) + \
       list(range(max(14, len(_rows17) - 5), len(_rows17)))
_seen = set()
for _i in _idx:
    if _i in _seen or _i >= len(_rows17):
        continue
    _seen.add(_i)
    r = _rows17[_i]
    m17.append([_i + 1, float(r["gamma_reference"]), float(r["gamma_detected"]),
                float(r["delta"])])
sheet_from_rows(ws35, ["№", "γ (mpmath.zetazero)", "γ (детектор ЭМ, слепо)", "Δ"],
                m17, [8, 24, 24, 14])
r17 = len(m17) + 3
val17 = {}
with open(os.path.join(RES, "experiment_17_validation.csv"), newline='') as _f:
    for _r in _csv.DictReader(_f):
        val17[_r["quantity"]] = _r["value"]
meta17 = [
    ("precision ЭМ / РС", val17.get("em_precision") + " / " + val17.get("rs_precision")),
    ("recall ЭМ / РС", val17.get("em_recall") + " / " + val17.get("rs_recall")),
    ("max |Δγ| ЭМ (Гаусс–Ньютон)", val17.get("em_max_err")),
    ("max |Δγ| РС (Гаусс–Ньютон)", val17.get("rs_max_err")),
    ("кросс-движок max |Δγ|", val17.get("cross_engine_max_err")),
    ("N(1000) стандартный путь", val17.get("N_rvm") + " → " + val17.get("N_rvm_rounded")),
    ("устойчивость сетки [900,1000]", val17.get("grid_robustness_max_shift")),
    ("SHA256 детектора ЭМ", open(os.path.join(RES, "e17_detector_em_sha256.txt")).read().strip()),
    ("SHA256 детектора РС", open(os.path.join(RES, "e17_detector_rs_sha256.txt")).read().strip()),
]
ws35.cell(row=r17, column=1, value="Валидация E17").font = Font(bold=True)
for i, (k, v) in enumerate(meta17, start=1):
    ws35.cell(row=r17 + i, column=1, value=k)
    ws35.cell(row=r17 + i, column=2, value=str(v))

# ── Лист 5: CrossLang ────────────────────────────────────────────
ws4 = wb.create_sheet("CrossLang")
cl = json.load(open(os.path.join(RES, "cross_language_validation.json")))
crows = [
    ["E11 нулей: python / julia", cl["e11"]["n_python"], cl["e11"]["n_julia"]],
    ["E11 max |Δγ| py↔jl", cl["e11"]["max_delta_python_vs_julia"], "рад"],
    ["E11 max |Δγ| py↔zetazero", cl["e11"]["max_err_python_vs_mpmath_zetazero"], "рад"],
    ["E11 max |Δγ| jl↔zetazero", cl["e11"]["max_err_julia_vs_mpmath_zetazero"], "рад"],
    ["E11 SHA256 детектора совпал", cl["e11"]["detector_sha256_match"], ""],
    ["E02 numpy max (1−F), 200 матриц", cl["e02"]["max_1mF"], "порог 1e−12"],
    ["E02 numpy median (1−F)", cl["e02"]["median_1mF"], ""],
    ["E12 numpy max невязка", cl["e12"]["max_residual"], ""],
    ["E13 numpy worst D", cl["e13"]["worst_trace_distance"], ""],
    ["E14 S аналитика / LHV max", cl["e14"]["S_analytic"], cl["e14"]["lhv_max"]],
    ["E16 Python-RS vs mpmath, max |Δζ|",
     cl.get("e16", {}).get("max_err_python_rs_vs_mpmath"), "9 высот [250,1000]"],
    ["E16 Julia бенчмарк agree max",
     cl.get("e16", {}).get("julia_benchmark_agree_max"), "порог 1e−9"],
    ["E17 SHA256 детекторов/эталона совпали",
     "%s/%s/%s" % (cl.get("e17", {}).get("sha_match_em"),
                   cl.get("e17", {}).get("sha_match_rs"),
                   cl.get("e17", {}).get("sha_match_reference")), ""],
    ["E17 все 649 позиций vs zetazero",
     cl.get("e17", {}).get("max_delta_julia_em_vs_zetazero_all649"), "детектор, до ГН"],
    ["E17 слепая репликация py [900,960]",
     "%s нулей; max|Δ|=%s" % (cl.get("e17", {}).get("n_python_blind_window"),
                              cl.get("e17", {}).get("max_delta_python_vs_julia_window")), ""],
]
sheet_from_rows(ws4, ["Проверка", "Python (mpmath+numpy)", "Комментарий"],
                crows, [40, 26, 26])

# ── Лист 6: Prereg ───────────────────────────────────────────────
ws5 = wb.create_sheet("Prereg")
prows = [
    ["E01", "невязка ≤ 1e−12; фазовый контроль; испорченный ≥ 1e−4"],
    ["E02", "max (1−F) ≤ 1e−12 (4×4) / ≤ 1e−10 (8×8), репликация и новые seeds"],
    ["E03", "все размеры завершены; наклон b ∈ [2.6, 3.4] (O(d³))"],
    ["E04", "байт-в-байт; 20 seeds max ≤ 1e−12; независимость порядка"],
    ["E05", "σ* для бюджета p95(1−F) ≤ 1e−8; глобальная фаза не влияет"],
    ["E06", "p=q=0 → 1.0; |сим − аналит| ≤ 4σ"],
    ["E07", "независимый: логическая < некодированной (p ≤ 0.05, CI95); коррелированный — выигрыш исчезает"],
    ["E08", "сумматор 256/256 биективен; mulmod: нечёт/чёт паттерн"],
    ["E09", "перебор n=2..8 без ошибок; Toffoli = 4n−2; CNOT = 10n−3; мусор ≡ 0"],
    ["E10", "круговая ошибка ≤ 1e−12; отрицательный контроль ≥ 5e−3"],
    ["E11", "precision=recall=1; max |Δγ| ≤ 1e−9; сетка h∈{0.02,0.005}; Гаусс–Ньютон ≤ 1e−9; N(60)=13"],
    ["E12", "макс. невязка ≤ 1e−15; конечные точки; глобальная фаза"],
    ["E13", "D ≤ 1e−12 (унитарные+CPTP); CNOT ≥ 0.01; разделение ≥ 1e10"],
    ["E14", "|S−2√2| ≤ 3σ; LHV max = 2"],
    ["E15", "M1 ≤ 1e−12; M3 полный ≤ 1e−12; M3 полу ≥ 0.2; абляция ≈ 0; линейная ≥ 0.1"],
    ["E16", "F-ряд ≤ 1e−30; вещественность Z ≤ 1e−12; согласие RS↔ЭМ ≤ 1e−9 на [250,1000]"],
    ["E17", "precision=recall=1 (оба движка); max|Δγ| ≤ 1e−9; кросс-движок ≤ 1e−9; N(1000)=найденным; сетка ≤ 1e−9"],
    ["E18", "ABQP: 1−F ≤ 1e−12 на 100% набора; примитивы ≤ BL1/BL2/BL4 на каждой цели; медиана времени ×50 ≤ BL3; identity — 0 AB2; испорченная компилируется"],
]
sheet_from_rows(ws5, ["Эксперимент", "Предрегистрированный порог (до данных)"],
                prows, [14, 96])

# ── Лист 5b: E18_baselines (O-J2) ─────────────────────────────
ws18 = wb.create_sheet("E18_baselines")
rows18 = []
import csv as _csv
with open(os.path.join(RES, "experiment_18_summary.csv"), newline='', encoding='utf-8') as f:
    for r in _csv.DictReader(f):
        rows18.append([r["method"], int(r["n_targets"]),
                       float(r["median_compile_ms"]),
                       float(r["max_one_minus_F"]),
                       float(r["success_rate_1e12"])])
sheet_from_rows(ws18, ["Метод", "Целей", "Медиана времени, мс",
                       "max (1−F)", "Доля успехов 1e−12"],
                rows18, [30, 10, 20, 20, 20])

path = os.path.join(OUT, "abqp_workbook.xlsx")
wb.save(path)
print("Workbook OK:", path)
