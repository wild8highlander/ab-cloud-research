# -*- coding: utf-8 -*-
"""Classic MT19937 (init_genrand) — bit-identical across the language ports.

Julia's MersenneTwister is dSFMT-based and NOT reproducible outside Julia, so
the golden layer substitutes this classic MT19937 everywhere (see
ports/golden/gen_golden.jl). The double conversion is the CPython one:

    random() = ((a >> 5) * 2**26 + (b >> 6)) / 2**53     # two draws per double
"""

from math import log, cos, pi

_N = 624
_M = 397
_MATRIX_A = 0x9908B0DF
_UPPER = 0x80000000
_LOWER = 0x7FFFFFFF


class MT19937(object):
    """Classic MT19937 with the mt19937ar reference block semantics."""

    def __init__(self, seed=5489):
        if isinstance(seed, float):
            # accept Julia-style UInt32 seeds passed as floats
            seed = int(seed) & 0xFFFFFFFF
        self.mt = [0] * _N
        self.mt[0] = seed & 0xFFFFFFFF
        for i in range(1, _N):
            prev = self.mt[i - 1]
            self.mt[i] = (1812433253 * (prev ^ (prev >> 30)) + i) & 0xFFFFFFFF
        # mt19937ar reference: first draw triggers the twist (idx past the end)
        self.idx = _N

    def next_u32(self):
        if self.idx >= _N:
            for kk in range(_N):
                y = (self.mt[kk] & _UPPER) | (self.mt[(kk + 1) % _N] & _LOWER)
                nxt = self.mt[(kk + _M) % _N] ^ (y >> 1)
                if y & 1:
                    nxt ^= _MATRIX_A
                self.mt[kk] = nxt
            self.idx = 0
        y = self.mt[self.idx]
        self.idx += 1
        y ^= y >> 11
        y ^= (y << 7) & 0x9D2C5680
        y ^= (y << 15) & 0xEFC60000
        y ^= y >> 18
        return y & 0xFFFFFFFF

    def random(self):
        """[0,1) double from two draws — identical to CPython random.random()."""
        a = self.next_u32() >> 5
        b = self.next_u32() >> 6
        return (a * 67108864.0 + b) / 9007199254740992.0

    def randn(self):
        """Box-Muller normal draw: u1<=0 is redrawn (u2 NOT consumed on redraw).

        Mirrors Random.randn on the MT19937RNG shim in gen_golden.jl.
        """
        u1 = self.random()
        while u1 <= 0.0:
            u1 = self.random()
        u2 = self.random()
        return (-2.0 * log(u1)) ** 0.5 * cos(2.0 * pi * u2)

    def rand_u8(self):
        """rand(rng, UInt8): top 8 bits of the next UInt32."""
        return self.next_u32() >> 24
