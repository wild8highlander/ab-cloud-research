"""V18: AB-оператор как процессор (живой пересчёт).

Проверяет:
  1. Ворота {X,Y,Z,H,S,T} — точные (fidelity > 1 − 1e-12).
  2. Зацепление двух кубитов: concurrence > 0.5.
  3. AB-Pong исполняется на операторе и детерминирован
     (повтор партии бит-в-бит).
  4. Итоговый флаг processor = True.
"""
from rpbridge.processor import (gate_fidelities, concurrence,
                                entanglement_experiment, play_pong,
                                run as run_v18)


def test_gates_exact():
    gates = gate_fidelities()
    assert set(gates.keys()) >= {'X', 'Y', 'Z', 'H', 'S', 'T'}
    for name, g in gates.items():
        assert g['fidelity'] > 1 - 1e-12, (name, g['fidelity'])


def test_entanglement_strong():
    ent = entanglement_experiment()
    assert ent['best_concurrence'] > 0.5


def test_pong_deterministic():
    g1 = play_pong(serve_right=True)
    g2 = play_pong(serve_right=True)
    assert g1['score'] == g2['score']
    assert g1['kicks'] == g2['kicks']
    assert g1['final_centroid'] == g2['final_centroid']


def test_pong_played_on_operator():
    g = play_pong(serve_right=True)
    assert set(g['score'].keys()) == {'left', 'right'}
    assert g['kicks'] > 0
    assert len(g['log']) > 0


def test_processor_verdict():
    v = run_v18()
    assert v['summary']['gates_universal'] is True
    assert v['summary']['entanglement'] is True
    assert v['summary']['game_runs'] is True
    assert v['summary']['processor'] is True
    assert v['p3_pong']['replay_bit_exact'] is True
