"""Th3/V12: сертификаты содержат истинные значения (коммит)."""
import json
import os


def test_all_certificates_valid():
    d = json.load(open(os.path.join(os.path.dirname(os.path.dirname(
        os.path.abspath(__file__))), 'data', 'v12_verdict.json')))
    assert d['all_valid']
    assert all(c['contains_true'] for c in d['certificates'])
