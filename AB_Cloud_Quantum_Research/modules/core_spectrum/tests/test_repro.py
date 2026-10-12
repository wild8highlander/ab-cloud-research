"""Воспроизводимость: кампании читают вердикты, сюжеты данных сходятся."""
import json
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def test_campaign_replays():
    camps = sorted(f for f in os.listdir(os.path.join(ROOT, 'campaigns'))
                   if f.startswith('run_v'))
    for c in camps:
        r = subprocess.run([sys.executable,
                            os.path.join(ROOT, 'campaigns', c)],
                           capture_output=True, text=True)
        assert r.returncode == 0, c


def test_verdicts_have_meta():
    for k in range(1, 16):
        p = os.path.join(ROOT, 'data', f'v{k:02d}_verdict.json')
        d = json.load(open(p))
        assert 'meta' in d and 'verdict_note' in d
