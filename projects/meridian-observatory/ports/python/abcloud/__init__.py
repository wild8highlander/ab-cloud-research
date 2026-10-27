# -*- coding: utf-8 -*-
"""abcloud — portable Python kernel of the meridian-spectral-observatory suite.

Bit-faithful port of ab_cloud_full.jl / hp_audit_standalone.jl /
AB_Cloud_Monumental_v6_3.jl (computational core), verified against
ports/golden/abcloud_golden.json (generated from the UNMODIFIED Julia
originals by ports/golden/gen_golden.jl).

Run:  python3 -m abcloud selftest | zeros | suite | ham | bN | gram | test11 | hp | sweep
"""

__version__ = "1.1.0"

from .mt19937 import MT19937                      # noqa: F401
from . import (mt19937, special, rmt_table, gof, lattice, unfold,  # noqa: F401
               golden, suite)
