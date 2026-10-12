#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""build_workbook.py — сборка tables/qp_workbook.xlsx (openpyxl).

Листы: Headline, Program V20, ISA, Previews, Thresholds P0–P6, Data files.
Запуск: python3 scripts/build_workbook.py
"""
import json
import os

from openpyxl import Workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

HEADER_FILL = PatternFill('solid', fgColor='3B4F58')
STRIPE = PatternFill('solid', fgColor='EBEDEE')
THIN = Side(style='thin', color='C7D3D9')
BORDER = Border(left=THIN, right=THIN, top=THIN, bottom=THIN)


def sheet(wb, name, header, rows, widths=None, note=None):
    ws = wb.create_sheet(name)
    ws.append(header)
    for c in ws[1]:
        c.fill = HEADER_FILL
        c.font = Font(color='FFFFFF', bold=True, size=9)
        c.alignment = Alignment(vertical='center')
        c.border = BORDER
    for i, row in enumerate(rows):
        ws.append([str(x) for x in row])
        for c in ws[i + 2]:
            c.font = Font(size=9)
            c.border = BORDER
            if i % 2 == 1:
                c.fill = STRIPE
    for j, w in enumerate(widths or [22] * len(header)):
        ws.column_dimensions[chr(65 + j)].width = w
    ws.freeze_panes = 'A2'
    if note:
        r = ws.max_row + 2
        ws.cell(row=r, column=1, value=note).font = Font(italic=True,
                                                         size=8)
    return ws


def main():
    v = json.load(open(os.path.join(ROOT, 'data', 'v20_verdict.json'),
                       encoding='utf-8'))
    wb = Workbook()
    wb.remove(wb.active)

    head = [
        ('1', 'V20 компилятор 4×4', 'min F = 1−4.44e-16 (M=200, сид 96)',
         'порог ≥ 1−1e-12'),
        ('2', 'V20 компилятор 8×8', 'min F = 1−6.66e-16 (M=100, сид 296)',
         'порог ≥ 1−1e-10'),
        ('3', 'контроли', 'identity/permutation/DFT4/CL(2) точны', 'точно'),
        ('4', 'бит-в-бит реплей', 'float64 идентичен', 'требуется'),
        ('5', 'глубина (макс.)', '7 затворов (4×4) / 29 (8×8)',
         'фиксируется'),
        ('6', 'память P1 (превью)', 'RAM 64/64; b = 4.0 ≤ 6; фазовые '
         'слова 256/256', 'пороги V21'),
        ('7', 'ALU V22 (превью)', '256/256 + 128/128 + 16/16 + 256/256',
         'пороги V22'),
        ('8', 'считывание V23 (превью)', '12/12 нулей точно; dev 2.98e-3; '
         'хранение 0 нулей / 6 констант', 'пороги V23'),
        ('9', 'нелокальность V24 (превью)', 'интерферометр 6.7e-16; '
         'защита 1000/1000; CHSH 2√2; коммутаторы 0', 'пороги V24'),
        ('10', 'вердикт P0', 'PROCESSOR_SPEC_EXECUTED', 'committed'),
    ]
    sheet(wb, 'Headline', ['#', 'Результат', 'Значение', 'Статус'], head,
          [5, 34, 52, 16],
          'AB Quantum Processor Program 0.1.0 · все числа из '
          'data/v20_verdict.json')

    m = v['meta']
    sheet(wb, 'Program V20', ['ID', 'Кампания', 'Дата', 'Время, с',
                              'Вердикт'],
          [(m['campaign'], m['name'], m['date'], v['runtime_s'],
            v['verdict_note']['ru'][:160])], [7, 40, 12, 10, 100])

    sheet(wb, 'ISA', ['Затвор', 'Тип', 'Параметры', 'Механизм'],
          v['isa']['primitives'], [22, 30, 26, 52],
          'ISA AB-облака: фазовый континуум φ = 2πΦ/Φ₀; калибровка '
          'fidelity ≥ 1−1e-14 на каждом примитиве')

    c = v['compiler']
    sheet(wb, 'Compiler', ['Метрика', '4×4 (сид 96)', '8×8 (сид 296)'],
          [('n унитарных', c['m4']['n'], c['m8']['n']),
           ('порог 1−F', '1e-12', '1e-10'),
           ('max 1−F', c['m4']['max_one_minus_F'],
            c['m8']['max_one_minus_F']),
           ('min F', c['m4']['min_fidelity'], c['m8']['min_fidelity']),
           ('gates (max)', c['m4']['gates_max'], c['m8']['gates_max']),
           ('2q-эквивалент (max)', c['m4']['two_qubit_equiv_max'],
            c['m8']['two_qubit_equiv_max']),
           ('identity', c['controls']['identity'], ''),
           ('permutation', c['controls']['permutation'], ''),
           ('DFT 4×4', c['controls']['dft4'], ''),
           ('CL(2)', c['controls']['cl2'], ''),
           ('бит-в-бит реплей', c['bit_exact_replay'], '')],
          [24, 26, 26])

    p = v['previews']
    prev_rows = [
        ('Память P1', 'RAM, полный перебор',
         f"{p['memory_P1']['ram']['read_back']}/"
         f"{p['memory_P1']['ram']['patterns']} бит-в-бит"),
        ('Память P1', 'Латентность b',
         f"{p['memory_P1']['latency']['b']:.2f} (порог V21 ≤ 6)"),
        ('Память P1', 'Фазовые слова',
         f"{p['memory_P1']['phase_word']['exact_words']}/"
         f"{p['memory_P1']['phase_word']['N']}"),
        ('ALU V22', 'Сумматор mod 16',
         f"{p['alu_V22']['adder_mod16']['passed']}/"
         f"{p['alu_V22']['adder_mod16']['total']}"),
        ('ALU V22', 'Умножение mod 16',
         f"{p['alu_V22']['mulmod16_odd']['passed']}/"
         f"{p['alu_V22']['mulmod16_odd']['total']}"),
        ('ALU V22', 'Инкремент',
         f"{p['alu_V22']['inc_mod16']['passed']}/"
         f"{p['alu_V22']['inc_mod16']['total']}"),
        ('ALU V22', 'Компаратор (фазовый)',
         f"{p['alu_V22']['comparator_phase']['passed']}/"
         f"{p['alu_V22']['comparator_phase']['total']}"),
        ('Чтение V23', 'Нули ζ на [2, 58]',
         f"{p['reading_V23']['zeros_read']}/"
         f"{p['reading_V23']['zeros_reference']} точно"),
        ('Чтение V23', 'Макс. позиционное отклонение',
         f"{p['reading_V23']['max_position_dev']:.2e}"),
        ('Чтение V23', 'Хранение',
         f"{p['reading_V23']['storage']['stored_zeros']} нулей / "
         f"{p['reading_V23']['storage']['stored_formula_constants']} "
         f"констант"),
        ('Нелок. V24', 'Интерферометр',
         f"{p['nonlocality_V24']['interferometer']['max_resid']:.1e}"),
        ('Нелок. V24', 'Защита',
         f"{p['nonlocality_V24']['protection']['protected']}/"
         f"{p['nonlocality_V24']['protection']['n_seeds']}"),
        ('Нелок. V24', 'CHSH S',
         f"{p['nonlocality_V24']['chsh']['S']:.6f}"),
        ('Нелок. V24', 'Коммутаторы [A⊗I, I⊗B]',
         f"{p['nonlocality_V24']['chsh']['comm_max']:.1e}"),
    ]
    sheet(wb, 'Previews', ['Слой', 'Метрика', 'Значение'], prev_rows,
          [14, 34, 44],
          'ПРЕДВАРИТЕЛЬНЫЕ измерения (превью); строгие пороги '
          'закреплены за V21–V24 в results/ROADMAP.md')

    thr = [
        ('P0 · v0.1.0', 'V20 Компилятор',
         'F ≥ 1−1e-12 / 1−1e-10', 'ВЫПОЛНЕНО: 1−4.4e-16 / 1−6.7e-16'),
        ('P1 · v0.2.0', 'V21 Память',
         'RAM 64/64; персистентность T=10³; b ≤ 6',
         'превью согласовано: 64/64, b = 4.0'),
        ('P2 · v0.3.0', 'V22 ALU',
         'сумматор/mulmod/компаратор 256/256',
         'превью согласовано: 256/256 и др.'),
        ('P3 · v0.4.0', 'V23 Считывание',
         '16 чисел ≤ 1e-12; замкнутость f∘g ≤ 1e-12; слепые нули '
         'K=138 @ T=300 dev ≤ 1e-8',
         'механизм подтверждён: 12/12, dev 3e-3'),
        ('P4 · v0.5.0', 'V24 Нелокальность',
         'интерферометр ≤ 1e-14; защита 1000/1000 dev ≤ 1e-12; CHSH '
         'S ≥ 2.8; [A,B] = 0',
         'превью согласовано: все четыре'),
        ('P5 · v0.6.0', 'V25 Бенчмарки',
         'RB ≥ 0.999; передача ≥ 0.99; квантовый объём', '—'),
        ('P6 · v1.0.0', 'V26 Datasheet',
         'универсальность {H,T,AB(π/4)} ≤ 12 затворов @ 1e-8; Lean '
         'O-uni; полный паспорт', '—'),
    ]
    sheet(wb, 'Thresholds', ['Фаза · версия', 'Кампания', 'Порог PASS',
                             'Статус v0.1.0'], thr, [16, 16, 52, 40])

    sheet(wb, 'Data files', ['Файл', 'Содержимое'],
          [('data/v20_verdict.json', 'закоммиченный вердикт кампании V20'),
           ('computations/V20_processor_compiler/data/results.json',
            'копия вердикта в папке расчётов'),
           ('computations/V20_processor_compiler/monograph_{ru,en}.pdf',
            'монографии (PDF)'),
           ('computations/V20_processor_compiler/monograph_{ru,en}.docx',
            'монографии (DOCX)'),
           ('figures_hires/{ru,en}/fig01..fig06',
            'рисунки 600 dpi × 2 языка'),
           ('verification/claim_audit/claims/claim_v20.json',
            'claim-файл (схема V14)'),
           ('tables/qp_workbook.xlsx', 'эта книга')],
          [52, 56])
    out = os.path.join(ROOT, 'tables', 'qp_workbook.xlsx')
    wb.save(out)
    print('WORKBOOK OK:', out)


if __name__ == '__main__':
    main()
