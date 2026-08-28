# Contributing to AB-Cloud Research

First of all — thank you for your interest in the AB-cloud programme! 🔭

This repository is **fully dedicated to one topic**: the AB-cloud as a phase
resonator for the zeros of the Riemann zeta function. Contributions that stay
on-topic are welcome.

## Ways to contribute

| Type | Welcome? | How |
|---|---|---|
| Bug reports (code or numerics) | ✅ yes | [Bug report template](.github/ISSUE_TEMPLATE/bug_report.yml) |
| Reproducibility reports (you ran the suite, numbers differ) | ✅ yes — especially valuable | Bug template, attach your full log |
| New language ports for the 10-language verification suite | ✅ yes | PR with a `verification/<lang>/` folder following the existing protocol |
| Performance improvements (Julia suite, 3D lab) | ✅ yes | PR with before/after timings |
| Documentation fixes (typos, broken links, clarifications) | ✅ yes | PR |
| Zeta-zero data sources (higher N, verified provenance) | ✅ yes | Issue first — datasets need provenance notes |
| Changes to the monographs' scientific content | ❌ by the Author only | Contact the Author (see README) |
| Off-topic material | ❌ no | This repo is single-topic by design |

## Development workflow

1. Fork the repository and create a feature branch:
   ```bash
   git checkout -b feat/my-contribution
   ```
2. Make your changes. For code, keep the style of the surrounding files;
   the Julia suite is intentionally **dependency-free** — do not introduce
   external packages.
3. Verify locally:
   ```bash
   julia code/ab_cloud_v19.jl --quick          # must pass both passes
   cd verification/python && python3 ab_cloud_verify.py --zeros ../data/zeta_zeros_50000.txt
   ```
4. Commit with a [conventional message](https://www.conventionalcommits.org/):
   ```
   feat(verification): add Zig port of the spacing protocol
   fix(julia): guard W=0 Byers–Yang edge case
   docs(readme): fix broken link to 3D lab
   ```
5. Open a pull request. CI will run markdownlint, link-checker, CodeQL and the
   Julia quick test.

## Reporting numerical discrepancies

If ⟨r⟩, KS or any other number differs from
[`results/verification_run_v18_37tests_2026-08-28.txt`](results/verification_run_v18_37tests_2026-08-28.txt):

1. State your Julia version (`julia --version`), OS and CPU;
2. Attach the **full log** of your run (the suite writes it next to the report);
3. Note any flags you used (`--quick`, `--ab-W`, …).

Numerical reproducibility reports are treated as high-priority issues.

## License

By contributing, you agree that your contributions are made under the terms of
the repository's [Custom Research License](LICENSE) (attribution to the Author
is preserved; contributions are acknowledged in the commit history).
