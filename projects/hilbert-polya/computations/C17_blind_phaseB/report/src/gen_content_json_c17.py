# -*- coding: utf-8 -*-
"""gen_content_json_c17.py — собирает content_c17.json из c17_content{,2}.py."""
import json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from c17_content import BLOCKS, TITLE, SUBTITLE, AUTHOR, DATE
from c17_content2 import BLOCKS2, BIBLIO

blocks = []
for t, p in list(BLOCKS) + list(BLOCKS2):
    blocks.append({'t': t, 'p': p})

out = {'title': TITLE, 'subtitle': SUBTITLE, 'author': AUTHOR, 'date': DATE,
       'blocks': blocks, 'biblio': BIBLIO}
path = os.path.join(HERE, 'content_c17.json')
json.dump(out, open(path, 'w'), ensure_ascii=False, indent=1)
print('content_c17.json:', len(blocks), 'blocks')
