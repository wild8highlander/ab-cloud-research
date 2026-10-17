# sbom/ — Software Bill of Materials

- `cyclonedx.json` — CycloneDX 1.5 (runtime + cross-language stdlib components)
- `spdx.json` — SPDX 2.3

The six CLI runners are deliberately dependency-light: Python needs
numpy/pyyaml/typer/rich; Julia uses only stdlib LinearAlgebra; Rust, Go and
the Node runner use only their standard libraries; Bash needs coreutils.
