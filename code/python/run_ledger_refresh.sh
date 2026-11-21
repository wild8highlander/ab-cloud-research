#!/bin/bash
# Ledger refresh: the deterministic, fast subset of the port suite.
# Stage A (tests 1-14,37, exact defaults) + T27 (two-pass) + T39 (fast sweep).
# T38 (~23 min, 2 seeds) is documented separately in PORT_STATUS.md.
cd /home/z/my-project/ab-cloud-research/code/python
DL=/home/z/my-project/download/abcloud-full-port
mkdir -p "$DL/results"

echo "=== STAGE A: ζ-statistics family (1-14, 37), exact defaults ===" >> "$DL/run_full_staged.log"
python3 -u ab_cloud_full.py --test 1-14,37 --output-dir "$DL/results/stats" >> "$DL/run_full_staged.log" 2>&1
echo "STAGE_A_EXIT=$?" >> "$DL/run_full_staged.log"

echo "=== T27 protocol run ===" >> "$DL/run_full_staged.log"
python3 -u ab_cloud_full.py --profile fast --test 27 --output-dir "$DL/results/lattice_t27_protocol" >> "$DL/run_full_staged.log" 2>&1
echo "T27_EXIT=$?" >> "$DL/run_full_staged.log"

echo "=== T39 geometry sweep (fast) ===" >> "$DL/run_full_staged.log"
python3 -u ab_cloud_full.py --profile fast --test 39 --output-dir "$DL/results/lattice_t39" >> "$DL/run_full_staged.log" 2>&1
echo "T39_EXIT=$?" >> "$DL/run_full_staged.log"
echo "LEDGER_REFRESH_DONE $(date +%H:%M:%S)" >> "$DL/run_full_staged.log"
