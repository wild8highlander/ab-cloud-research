#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""run_all.py — полный прогон кампаний ES1–ES5 вспомогательного исследования
«машина без долговременной памяти». Возвращает 0, если все вердикты PASS."""
import os
import runpy
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ORDER = ["run_es1_cycles.py", "run_es2_volatility.py", "run_es3_realtime.py",
         "run_es4_task.py", "run_es5_noise.py"]


def main():
    fails = []
    for script in ORDER:
        print(f"\n═══ {script} ═══")
        g = runpy.run_path(os.path.join(HERE, script))
        # каждый run_* возвращает 0 при успехе через sys.exit(main())
    # сводный вердикт по файлам
    import json
    data = os.path.join(os.path.dirname(HERE), "data")
    for f in sorted(os.listdir(data)):
        if f.endswith("_verdict.json"):
            v = json.load(open(os.path.join(data, f), encoding="utf-8"))
            print(f"{v['experiment']}: pass={v['pass']}")
            if not v["pass"]:
                fails.append(v["experiment"])
    if fails:
        print("FAILED:", fails)
        return 1
    print("ALL ES CAMPAIGNS: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
