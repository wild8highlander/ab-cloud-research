"""checksums.sha256 must cover and match the data funnel."""
import hashlib
from pathlib import Path


def test_checksums_file_exists(pkg):
    assert (pkg / "02_data/checksums.sha256").is_file()


def test_checksums_verify(pkg):
    data = pkg / "02_data"
    listed = {}
    for line in (data / "checksums.sha256").read_text(encoding="utf-8").splitlines():
        if "  " in line:
            h, p = line.split("  ", 1)
            listed[p] = h
    assert len(listed) >= 30, f"too few checksummed files: {len(listed)}"
    bad = []
    for rel, h in listed.items():
        p = data / rel
        if not p.exists():
            bad.append(f"missing {rel}")
            continue
        digest = hashlib.sha256(p.read_bytes()).hexdigest()
        if digest != h:
            bad.append(rel)
    assert not bad, f"checksum mismatches: {bad[:5]}"


def test_raw_is_readonly_registry(pkg):
    """The processed registry is the funnel — it must exist and carry honesty."""
    import json
    reg = json.loads((pkg / "02_data/processed/research_registry.json").read_text(encoding="utf-8"))
    assert reg["programme"]["honest_boundary"]["rh_status"] == "blocked"
