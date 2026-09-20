"""
AB-Cloud v23 SUPERCOMBO — Python reimplementation.

A faithful, dependency-light clone of the Julia verification suite
(ab_cloud_v23.jl): all 38 tests, the two-pass verdict algebra, report
generation and plotting.  See README.md and the monograph Appendix D.

Quick start:
    python -m abcloud.cli --list
    python -m abcloud.cli --test 1 --no-two-pass
    python -m abcloud.cli --test all          # fast profile
    python -m abcloud.cli --test all --full   # reference scale (hours)
"""

__version__ = "1.0.0"
