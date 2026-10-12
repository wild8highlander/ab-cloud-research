#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""new_experiment.py — скаффолд новой кампании (V16+).

Создаёт скелет по образцу серии: модуль rpbridge, кампанию, папку
вычисления, claim-файл и тест. Запуск:
    python3 scripts/new_experiment.py 16 "Название решения"
"""
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 1
    num = int(sys.argv[1])
    title = sys.argv[2] if len(sys.argv) > 2 else f'Новая кампания V{num:02d}'
    slug = sys.argv[3] if len(sys.argv) > 3 else 'new_campaign'
    vid = f'v{num:02d}'
    vdir = f'V{num:02d}_{slug}'
    print(f'=== Скаффолд кампании {vid.upper()} «{title}» ===')

    module = os.path.join(ROOT, 'rpbridge', f'{slug}.py')
    with open(module, 'w', encoding='utf-8') as f:
        f.write(f'''"""rpbridge.{slug} — Решение {num} (V{num:02d}): {title}.

Заполните по образцу серии V1–V15 (см. docs/plan15.md):
  1. точное математическое утверждение;
  2. перечень предпосылок;
  3. воспроизводимое вычисление (детерминированные seeds);
  4. контрольные модели;
  5. перечень того, что результат НЕ доказывает.
"""
import numpy as np


def run():
    """Полный протокол V{num:02d} → verdict dict."""
    return {{
        'meta_note': 'заполните вычисление',
        'verdict_note': 'статус: измерено (заполните честно)',
    }}
''')

    campaign = os.path.join(ROOT, 'campaigns', f'run_{vid}_{slug}.py')
    with open(campaign, 'w', encoding='utf-8') as f:
        f.write(f'''#!/usr/bin/env python3
"""Кампания {vid.upper()} — {title} (экскурсия по вердикту)."""
import json, os

def main():
    R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    d = json.load(open(f"{{R}}/data/{vid}_verdict.json"))
    print("== {vid.upper()} {title} ==")
    print(" ", d.get("verdict_note"))

if __name__ == "__main__":
    main()
''')

    comp = os.path.join(ROOT, 'computations', vdir)
    os.makedirs(os.path.join(comp, 'data'), exist_ok=True)
    os.makedirs(os.path.join(comp, 'figures', 'ru'), exist_ok=True)
    os.makedirs(os.path.join(comp, 'figures', 'en'), exist_ok=True)

    claim = os.path.join(ROOT, 'verification', 'claim_audit', 'claims',
                         f'claim_{vid}.json')
    os.makedirs(os.path.dirname(claim), exist_ok=True)
    import json
    with open(claim, 'w', encoding='utf-8') as f:
        json.dump({'claim': f'{vid.upper()} {title}', 'statement': '',
                   'premises': [], 'code': [f'rpbridge/{slug}.py'],
                   'controls': [], 'does_not_prove': [], 'status': 'measured'},
                  f, ensure_ascii=False, indent=1)

    print(f'  модуль:      rpbridge/{slug}.py')
    print(f'  кампания:    campaigns/run_{vid}_{slug}.py')
    print(f'  вычисление:  computations/{vdir}/')
    print(f'  claim:       verification/claim_audit/claims/claim_{vid}.json')
    print('Дальше: запустите scripts/compute_all.py ' + vid +
          ', добавьте фигуру в make_figures.py и секцию в content/ru_part*.py.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
