"""V14: аудит claims — форма и покрытие."""
from rpbridge.audit import run


def test_audit_all_a1():
    d = run()
    assert d['all_a1']


def test_coverage():
    d = run()
    assert d['covered']
