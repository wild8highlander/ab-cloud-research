"""config.yaml must validate against config.schema.json (structure level)."""
import json

import yaml


def _load(pkg):
    cfg = yaml.safe_load((pkg / "config.yaml").read_text(encoding="utf-8"))
    schema = json.loads((pkg / "config.schema.json").read_text(encoding="utf-8"))
    return cfg, schema


def test_schema_is_valid_json(pkg):
    json.loads((pkg / "config.schema.json").read_text(encoding="utf-8"))


def test_required_keys(pkg):
    cfg, schema = _load(pkg)
    for key in schema["required"]:
        assert key in cfg, f"missing required key: {key}"


def test_honesty_gate(pkg):
    """rh_status mirrors the V13 machine verdict — 'certified' (unlocked v1.2.1)."""
    cfg, _ = _load(pkg)
    assert cfg["programme"]["honest_boundary"]["rh_status"] == "certified"
    assert "does_not_prove" in cfg["programme"]["honest_boundary"]


def test_seed_and_lattice(pkg):
    cfg, _ = _load(pkg)
    assert isinstance(cfg["seed"], int) and cfg["seed"] >= 0
    assert 0 < cfg["lattice"]["alpha"] <= 1
    assert cfg["lattice"]["boundary"] == "torus"


def test_gue_windows_registered(pkg):
    cfg, _ = _load(pkg)
    g = cfg["gue_windows"]["r_ratio"]["gue"]
    assert len(g) == 2 and g[0] < g[1]


def test_jsonschema_full(pkg):
    """If jsonschema is installed, run the full validation."""
    try:
        import jsonschema
    except ImportError:
        return  # soft dependency
    cfg, schema = _load(pkg)
    jsonschema.validate(cfg, schema)
