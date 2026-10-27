# -*- coding: utf-8 -*-
"""gen_appendix_table.py — генерирует строки таблицы А.1 из реального
amap_results.json и заменяет блок _ROWS в amap_content2.py."""
import json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
R = json.load(open(os.path.join(HERE, '..', '..', 'data', 'amap_results.json')))

al = R['alphas_exact_float']          # 24
b2 = R['betas2_exact_float']          # 23
be = [x ** 0.5 for x in b2]
logD = R['hankel_mp']['log10_D']      # D_1..D_24
logh = R['hankel_mp']['log10_h']      # h_0..h_23

rows = []
for n in range(24):
    a = '%.6f' % al[n]
    if n < 23:
        b = '%.6f' % be[n]
        b2s = '%.3f' % b2[n]
    else:
        b = '—'; b2s = '—'
    lD = '%.3f' % logD[n]            # log10 D_{n+1} (n = 23 -> D_24)
    lh = '%.3f' % logh[n]            # log10 h_n
    rows.append(" ['%d', '%s', '%s', '%s', '%s', '%s']," % (n, a, b, b2s, lh, lD))

new_block = "_ROWS = [\n" + "\n".join(rows) + "\n]"

path = os.path.join(HERE, 'amap_content2.py')
src = open(path).read()
src = re.sub(r"_ROWS = \[.*?\n\]", new_block, src, flags=re.S)
# поправить заголовок колонки β²
src = src.replace("'β² (×10³)',", "'β<sub>n+1</sub>²',")
open(path, 'w').write(src)
print('ROWS regenerated:', len(rows))
print('\n'.join(rows[:4]))
print('...')
print('\n'.join(rows[-2:]))
