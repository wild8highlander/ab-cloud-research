"""V13: the obligation machine (B1–B5) — DAG, blocking, artifacts, audit."""
from rpbridge.formaloblig import (
    audit_formal_sources,
    check_artifacts,
    check_dag,
    check_verdict_consistency,
    load_obligations,
    path_to_rh_blocked,
    run,
)

EXPECTED_BLOCKERS = ["O05", "O07", "O08", "O09", "O10", "O11", "O12"]


def test_b1_dag_valid():
    ok, msgs = check_dag()
    assert ok, msgs


def test_b2_rh_blocked():
    blk = path_to_rh_blocked()
    assert blk["blocked"] and blk["n_blockers"] > 0


def test_b2_blockers_are_exactly_the_unproven_nodes():
    nodes, _ = load_obligations()
    blk = path_to_rh_blocked(nodes)
    assert blk["blockers"] == EXPECTED_BLOCKERS


def test_b3_every_artifact_exists():
    ok, msgs = check_artifacts()
    assert ok, msgs


def test_b4_no_unfinished_proofs_anywhere():
    audit = audit_formal_sources()
    for sysname, rep in audit["systems"].items():
        assert not rep["unfinished_proofs"], (
            sysname, rep["unfinished_proofs"])
    assert audit["clean"]


def test_b4_reduction_axioms_are_declared():
    # The A1-A6 reduction line is explicit, not hidden: every assistant
    # declares its classical inputs as named axioms/postulates.
    audit = audit_formal_sources()
    assert audit["n_axioms_total"] > 0
    for sysname in ("lean", "coq", "agda", "isabelle"):
        assert audit["systems"][sysname]["files"], sysname


def test_b4_axioms_force_blocking():
    r = run()
    if r["formal_audit"]["n_axioms_total"] > 0:
        assert r["rh_conclusion"] == "blocked"
        assert r["axioms_force_block"]


def test_b5_committed_verdict_consistent():
    ok, msgs = check_verdict_consistency()
    assert ok, msgs


def test_machine_sound_end_to_end():
    r = run()
    assert r["machine_sound"] is True
    assert r["dag_valid"] and r["artifact_gate"]["ok"]
    assert r["verdict_consistency"]["ok"]


def test_verdict_counters_match_the_dag():
    r = run()
    assert (r["n_proven"], r["n_computed"], r["n_assumed"]) == (5, 3, 4)
    assert r["n_proven"] + r["n_computed"] + r["n_assumed"] == len(
        r["obligations"])
