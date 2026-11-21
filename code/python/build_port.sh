#!/bin/bash
# Build the single-file Python port from the part files (order matters).
set -e
cd /home/z/my-project
cat scripts/abpy_parts/part1_core.py \
    scripts/abpy_parts/part2_stats1.py \
    scripts/abpy_parts/part3_stats2.py \
    scripts/abpy_parts/part4_lattice1.py \
    scripts/abpy_parts/part5_lattice2.py \
    scripts/abpy_parts/part5b_lattice3.py \
    scripts/abpy_parts/part5c_t38.py \
    scripts/abpy_parts/part5d_t39.py \
    scripts/abpy_parts/part6_runner.py \
    > ab-cloud-research/code/python/ab_cloud_full.py
python3 -m py_compile ab-cloud-research/code/python/ab_cloud_full.py
echo "BUILD OK: $(wc -l < ab-cloud-research/code/python/ab_cloud_full.py) lines"
