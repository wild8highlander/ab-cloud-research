#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""build_workbook.py — tables/hp_workbook.xlsx: сводная книга серии
(затворы C3+C5, теоремы, табель ГП, главные числа). Запуск из корня."""
import csv
import json
import os

from openpyxl import Workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "tables", "hp_workbook.xlsx")

HEADER_FILL = PatternFill("solid", fgColor="3B4F58")
STRIPE = PatternFill("solid", fgColor="EBEDEE")
ACCENT = Font(color="FFFFFF", bold=True, size=10)
THIN = Side(style="thin", color="C7D3D9")
BORDER = Border(top=THIN, bottom=THIN, left=THIN, right=THIN)


def sheet(wb, name, header, rows, widths, note=None):
    ws = wb.create_sheet(name)
    ws.sheet_view.showGridLines = False
    r0 = 1
    if note:
        ws.cell(1, 1, note).font = Font(italic=True, size=9, color="777E81")
        r0 = 3
    for j, h in enumerate(header, 1):
        c = ws.cell(r0, j, h)
        c.fill, c.font, c.border = HEADER_FILL, ACCENT, BORDER
        c.alignment = Alignment(horizontal="center", vertical="center")
    for i, row in enumerate(rows, 1):
        for j, v in enumerate(row, 1):
            c = ws.cell(r0 + i, j, v)
            c.border = BORDER
            c.font = Font(size=10)
            c.alignment = Alignment(vertical="center", wrap_text=True)
            if i % 2 == 0:
                c.fill = STRIPE
    for j, w in enumerate(widths, 1):
        ws.column_dimensions[get_column_letter(j)].width = w
    ws.freeze_panes = ws.cell(r0 + 1, 1)
    return ws


def main():
    wb = Workbook()
    wb.remove(wb.active)
    wb.properties.creator = "Hilbert Polya Bridge 1.0.0"

    # ── Sheet 1: главные числа ──
    d = json.load(open(f"{ROOT}/data/c4_trace_verdict.json"))["verdict"]
    d5 = json.load(open(f"{ROOT}/data/c5_gates_ext_verdict.json"))["verdict"]
    rows = [
        [1, "Γ-замыкания, max невязка (dps 40)", "2.59e-39", "C1", "T1 доказано"],
        [2, "max |Im Z_id|", "4.93e-29", "C1", "T2 доказано"],
        [3, "Нули Z_id [0,200] vs mpmath", "79/79, 2.8e-14", "C1", "K3"],
        [4, "Мост арифметик N(T)", "2.6e-26", "C2", "T3"],
        [5, "RH в полосе до T=1000", "649 = 649", "C2", "верифицировано"],
        [6, "Лучший r_H7 (52 затвора)", 0.226, "C3", "Г2 — ранговая ветвь"],
        [7, "Тождество Q(a) (M0)", "1.7e-12", "C4", "T6"],
        [8, "Следовая формула H_ξ (M1)", "1.2e-5", "C4", "T6"],
        [9, "PC0 (тепловая проекция)", "+0.9998 / 2.1%", "C4", "контроль"],
        [10, "Следовая ветвь", "≈0.5 порядка", "C4", "Г2 — консервативная ветвь"],
        [11, "Расширенная семья |r_H7| max", d5["rH7_abs_max"], "C5", "T7"],
        [12, "Ко-локация (Φ_p,Φ_q)≡Φ_pq", "1.35e-14", "C6", "T4 доказано"],
        [13, "ψ-лестница", "+0.972", "C6", "Г5 — НЕТ"],
        [14, "Транспорт P(x≥90) ζ/random", "×16", "C7", "Г4 — ДА"],
        [15, "spinor64 редукция", "64 → 4", "C8", "T8"],
        [16, "Воспроизведение C3", "1.45e-16", "C4", "бит-в-бит"],
    ]
    sheet(wb, "Headline", ["#", "Величина", "Значение", "Кампания", "Статус"],
          rows, [5, 44, 20, 10, 20],
          "Hilbert Polya Bridge v1.0.0 · главные числа серии (все вердикты — в data/)")

    # ── Sheet 2: затворы C3 ──
    rows = list(csv.DictReader(open(f"{ROOT}/data/c3_gates_table.csv")))
    sheet(wb, "Gates C3", list(rows[0].keys()),
          [[r[k] for k in rows[0]] for r in rows],
          [6, 7, 7, 8, 14, 10, 10, 8, 10, 9, 9, 9, 10],
          "52 протокольных затвора (Nv × q × W × α), сид 96")

    # ── Sheet 3: расширенные затворы C5 ──
    rows = list(csv.DictReader(open(f"{ROOT}/data/c5_gates_ext_table.csv")))
    keys = list(rows[0].keys())
    sheet(wb, "Gates C5 ext", keys,
          [[r[k] for k in keys] for r in rows],
          [24] + [10] * (len(keys) - 1),
          "35 новых затворов (6 ручек) + 2 декуя (v2.0.5): ⟨r⟩ = 0.569–0.633 "
          "(полоса GUE 0.5996±0.03, среднее 0.601); |r_H7| ≤ 0.097")

    # ── Sheet 4: теоремы ──
    rows = [
        ["T1", "Γ-замыкания: 3 формы + опровержение", "доказано", "1.3–2.6e-39 (dps 40)", "C1"],
        ["T2", "Im Z_id = 0", "доказано", "4.9e-29", "C1"],
        ["T3", "калибровка полюса аргументного принципа", "доказано", "якоря + мост 2.6e-26", "C2"],
        ["T4", "ко-локация (Φ_p,Φ_q) ≡ Φ_pq", "доказано", "1.35e-14", "C6"],
        ["T5", "ядро разрешения δ(d), ξ_mult ≈ 2–3", "измерено", "насыщение ~2e-2", "C6"],
        ["T6", "следовая формула Tr e^{−xH_ξ}", "доказано+верифицировано", "1.7e-12 / 1.2e-5", "C4"],
        ["T7", "демаркация универсальности (87 затворов)", "измерено", "|r_H7| ≤ 0.226 (C3); ≤ 0.097 (C5)", "C3+C5"],
        ["T8", "редукция 64→4", "доказано", "|Δλ| ≤ 1.1e-14", "C8"],
        ["T9", "нулевые моды α = 1/3", "измерено", "18 (L=12), 42 (L=24)", "серия"],
        ["T10", "лестница Пуассон/GOE/GUE", "измерено", "11 каналов", "C8"],
    ]
    sheet(wb, "Theorems", ["T", "Содержание", "Статус", "Величина", "Кампания"],
          rows, [6, 44, 22, 26, 10], "Десять теорем серии (полные доказательства — том Theorems)")

    # ── Sheet 5: табель ГП ──
    rows = [
        ["Г1", "самосопряжённость", "ДА", "эрмитовость; вещественный спектр"],
        ["Г2", "спектральное тождество", "ДА", "D_nn 0.0079 — уровень самих нулей ζ (сдвинутые окна нулей и GUE-класс нулей: 0.0079±0.0005, C3); семья 0.0069–0.0092 в полосе нулей; класс GUE ⟨r⟩ = 0.60 (C5); следовый мост |ΔK| ≤ 1.2e-5 (C4)"],
        ["Г3", "класс GUE", "ДА", "⟨r⟩ = 0.60 при Nv ≥ 8; вся C5 в классе: ⟨r⟩ = 0.569–0.633, среднее 0.60"],
        ["Г4", "дираковская динамика", "ДА", "когерентный пакет; энергия 1e-15"],
        ["Г5", "простые в операторе", "НЕТ", "ψ 0.972 у нулей; нулевая зона у затворов"],
    ]
    sheet(wb, "HP scorecard", ["Пункт", "Вопрос", "Вердикт", "Основание"],
          rows, [8, 30, 10, 66], "Табель Гильберта–Пойа: пять вопросов программы")

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    wb.save(OUT)
    print(f"workbook OK: {OUT}")


if __name__ == "__main__":
    main()
