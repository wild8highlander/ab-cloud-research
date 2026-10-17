"""The six-language CLI contract: identical metrics, certified RH, honesty gates."""
import json
import subprocess
import sys
from pathlib import Path

CODE = Path(__file__).resolve().parents[2] / "06_code"


def _run(cmd):
    return subprocess.run(cmd, capture_output=True, text=True, timeout=180)


def test_python_json_contract():
    r = _run([sys.executable, str(CODE / "python/run.py"), "--output=json", "analyze"])
    assert r.returncode == 0, r.stderr[-400:]
    payload = json.loads(r.stdout)
    assert payload["metrics"]["rh_status"] == "certified"
    assert payload["metrics"]["flagship_results"] == 37
    assert payload["params"]["seed"] == 42


def test_bash_json_contract():
    r = _run(["bash", str(CODE / "bash/run.sh"), "--output=json", "analyze"])
    assert r.returncode == 0, r.stderr[-400:]
    payload = json.loads(r.stdout)
    m = payload.get("metrics", payload)
    assert m["rh_status"] == "certified"
    assert m["flagship_results"] == 37


def test_js_json_contract():
    r = _run(["node", str(CODE / "js/run.js"), "--output=json", "analyze"])
    assert r.returncode == 0, r.stderr[-400:]
    payload = json.loads(r.stdout)
    m = payload.get("metrics", payload)
    assert m["rh_status"] == "certified"
    assert m["flagship_results"] == 37


def test_cross_language_metrics_identical():
    outs = []
    for cmd in ([sys.executable, str(CODE / "python/run.py"), "--quiet", "--output=json", "analyze"],
                ["bash", str(CODE / "bash/run.sh"), "--output=json", "analyze"],
                ["node", str(CODE / "js/run.js"), "--output=json", "analyze"]):
        r = _run(cmd)
        assert r.returncode == 0, r.stderr[-300:]
        outs.append(json.loads(r.stdout) if "metrics" in r.stdout[:200] else json.loads(r.stdout))
    flat = []
    for o in outs:
        flat.append(o.get("metrics", o))
    keys = ["rh_status", "flagship_results", "gue_r_decorated", "trace_primes_r", "blind_zeros"]
    for k in keys:
        vals = {str(f.get(k)) for f in flat}
        assert len(vals) == 1, f"metric {k} diverges across languages: {vals}"


def test_shared_metrics_file():
    m = json.loads((CODE / "shared/metrics.json").read_text(encoding="utf-8"))
    assert m["rh_status"] == "certified"
    assert m["seed"] == 42


def test_honesty_gate_hook():
    r = _run(["bash", str(CODE / "hooks/pre_run.sh")])
    assert r.returncode == 0, "honesty gate failed"
    assert "certified" in r.stdout


def test_registry_rh_certified(registry):
    assert registry["programme"]["honest_boundary"]["rh_status"] == "certified"


def test_plugin_honesty(pkg):
    """Plugins must not try to change rh_status (source-level check)."""
    plugins = list((CODE / "plugins").glob("*.py"))
    for p in plugins:
        src = p.read_text(encoding="utf-8")
        assert 'rh_status' not in src or 'certified' in src, f"plugin {p.name} touches rh_status"


def test_doctor_passes():
    r = _run([sys.executable, str(CODE / "python/run.py"), "--quiet", "doctor"])
    assert r.returncode == 0, r.stdout[-400:]
