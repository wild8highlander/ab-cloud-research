"""Shared fixtures for the package integrity suite."""
from pathlib import Path

import pytest

PKG_ROOT = Path(__file__).resolve().parents[2]


@pytest.fixture(scope="session")
def pkg() -> Path:
    return PKG_ROOT


@pytest.fixture(scope="session")
def registry(pkg):
    import json
    return json.loads((pkg / "02_data/processed/research_registry.json").read_text(encoding="utf-8"))
