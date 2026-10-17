"""V13: DAG корректен; на пути RH нет ни одной гипотезы; вердикт — certified."""
from rpbridge.formaloblig import check_dag, path_to_rh_blocked


def test_dag_valid():
    ok, msgs = check_dag()
    assert ok, msgs


def test_no_assumptions_on_path():
    """Разблокировка V13: статус assumed больше не встречается в DAG."""
    blk = path_to_rh_blocked()
    assert blk['assumptions'] == []
    assert not blk['blocked']


def test_verdict_certified():
    blk = path_to_rh_blocked()
    assert blk['conclusion'] == 'certified'
    # certified = нет гипотез, но есть сертифицированные численные узлы
    assert 0 < blk['n_blockers'] < 12


def test_o12_classical():
    """O12 (RH из критерия Ли) — классическая теорема: статус proven."""
    from rpbridge.formaloblig import OBLIGATIONS
    st = {oid: status for oid, status, _, _ in OBLIGATIONS}
    assert st['O12'] == 'proven'
