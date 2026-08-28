#!/usr/bin/env python3
"""
run_all_75_tasks.py
Запуск ВСЕХ 75 задач монографии.
Run ALL 75 monograph tasks.

Использование / Usage:
    python3 run_all_75_tasks.py
"""

import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

# Импорт всех задач
from monograph_verification import (
    CONFIG, task_01, task_02, task_03, task_04, task_05,
    task_06, task_07, task_08, task_09, task_10,
    task_11, task_12, task_13, task_14, task_15,
    task_16, task_17, task_18, task_19, task_20,
    task_21, task_22, task_23, task_24, task_25,
    task_26, task_27, task_28, task_29, task_30,
)
from monograph_verification_part2 import (
    task_31, task_32, task_33, task_34, task_35, task_36,
    task_37, task_38, task_39, task_40,
    task_41, task_42, task_43, task_44, task_45,
    task_46, task_47, task_48, task_49, task_50,
)
from monograph_verification_part3 import (
    task_51, task_52, task_53, task_54, task_55, task_56,
    task_57, task_58, task_59, task_60,
    task_61, task_62, task_63, task_64, task_65, task_66,
    task_67, task_68, task_69, task_70,
    task_71, task_72, task_73, task_74, task_75,
)


def main():
    print("=" * 78)
    print("ЗАПУСК ВСЕХ 75 ЗАДАЧ МОНОГРАФИИ")
    print("RUNNING ALL 75 MONOGRAPH TASKS")
    print("=" * 78)
    print(f"Директория вывода / Output: {CONFIG['output_dir']}")
    print()

    all_tasks = []
    for i in range(1, 76):
        task_name = f"task_{i:02d}"
        task_func = globals().get(task_name)
        if task_func:
            all_tasks.append((task_name, task_func))

    print(f"Всего задач / Total tasks: {len(all_tasks)}")
    print()

    results = {}
    total_time = 0.0

    for name, func in all_tasks:
        print(f">>> {name}...", end=' ', flush=True)
        t0 = time.time()
        try:
            paths = func()
            dt = time.time() - t0
            total_time += dt
            results[name] = {"status": "OK", "time": dt}
            print(f"OK ({dt:.2f}s)")
        except Exception as e:
            dt = time.time() - t0
            total_time += dt
            results[name] = {"status": "ERROR", "time": dt, "error": str(e)}
            print(f"ERROR ({dt:.2f}s): {e}")

    # Сводка
    print()
    print("=" * 78)
    print("ИТОГ / SUMMARY")
    print("=" * 78)
    ok = sum(1 for r in results.values() if r['status'] == 'OK')
    err = sum(1 for r in results.values() if r['status'] == 'ERROR')
    print(f"Всего задач / Total tasks: {len(all_tasks)}")
    print(f"Успешных / Successful: {ok}")
    print(f"Ошибок / Errors: {err}")
    print(f"Общее время / Total time: {total_time:.2f} сек / sec")
    print(f"Данные / Data: {CONFIG['output_dir']}/{CONFIG['data_subdir']}/")
    print(f"Графики / Figures: {CONFIG['output_dir']}/{CONFIG['figures_subdir']}/")

    if err > 0:
        print("\nОшибки / Errors:")
        for name, r in results.items():
            if r['status'] == 'ERROR':
                print(f"  {name}: {r['error']}")

    return results


if __name__ == "__main__":
    main()
