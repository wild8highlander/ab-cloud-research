# -*- coding: utf-8 -*-
"""gen_content_json.py — собирает content_amap.json из amap_content{,2}.py
для DOCX-сборки (теги <b>/<sub>/<super> парсятся в amap_docx.js)."""
import json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from amap_content import BLOCKS, TITLE, SUBTITLE, AUTHOR, DATE
from amap_content2 import BLOCKS2, BIBLIO

blocks = []
for t, p in list(BLOCKS) + list(BLOCKS2):
    blocks.append({'t': t, 'p': p})

out = {'title': TITLE, 'subtitle': SUBTITLE, 'author': AUTHOR, 'date': DATE,
       'blocks': blocks, 'biblio': BIBLIO}
path = os.path.join(HERE, 'content_amap.json')
json.dump(out, open(path, 'w'), ensure_ascii=False, indent=1)
print('content_amap.json:', len(blocks), 'blocks')
