"""V13: DAG корректен, RH заблокирован (машина обязательств)."""
from rpbridge.formaloblig import check_dag, path_to_rh_blocked


def test_dag_valid():
    ok, msgs = check_dag()
    assert ok, msgs


def test_rh_blocked():
    blk = path_to_rh_blocked()
    assert blk['blocked'] and blk['n_blockers'] > 0
