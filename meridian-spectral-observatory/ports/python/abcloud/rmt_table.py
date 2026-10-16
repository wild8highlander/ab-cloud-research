# -*- coding: utf-8 -*-
"""RMT reference-law engine — 32768-point GUE2 CDF table + exact-law sampler.

The Julia original evaluates gue_cdf analytically (openlibm); the ports use
a 32768-point table on [0, 5] with linear interpolation (|dF| <= 1e-9, inside
the 1e-7 cross-libm tolerance). The exact-law sampler for Test 11 uses a
4096-point quantile grid built by 48-step bisection.

set_spacing_law('gue2' | 'goe') mirrors the Julia Ref{Symbol} law switch.
"""

from .special import goe_surmise_cdf, gue2_surmise_cdf

_TN = 32768
_QN = 4096
_SMAX = 5.0


class _RmtTable(object):
    def __init__(self):
        self.law = 0          # 0 = gue2, 1 = goe
        self.table_on = True
        self._cdf = None      # lazily built
        self._quant = None
        self._quant_umax = None

    # -- law handling -------------------------------------------------------
    def set_spacing_law(self, name):
        name = name.lower()
        if name in ("gue2", "gue", "gue2_surmise"):
            self.law = 0
        elif name in ("goe", "goe_surmise"):
            self.law = 1
        else:
            raise ValueError("unknown spacing law: %r" % (name,))

    # -- CDF ----------------------------------------------------------------
    @staticmethod
    def gue2_exact(s):
        return gue2_surmise_cdf(s)

    def _build_cdf(self):
        self._cdf = [self.gue2_exact(i * _SMAX / (_TN - 1)) for i in range(_TN)]

    def table_cdf(self, s):
        if s < 0:
            return 0.0
        if self.law == 1:
            return goe_surmise_cdf(s)
        if self._cdf is None:
            self._build_cdf()
        if s >= _SMAX:
            return self.gue2_exact(s)
        x = s * (_TN - 1) / _SMAX
        i = int(x)          # floor for s >= 0
        if i < 0 or i >= _TN - 1:
            return self.gue2_exact(s)
        t = x - i
        return (1.0 - t) * self._cdf[i] + t * self._cdf[i + 1]

    def gue_cdf(self, s):
        if self.law == 1:
            return goe_surmise_cdf(s)
        if self.table_on:
            return self.table_cdf(s)
        return self.gue2_exact(s)

    # -- exact-law sampler ---------------------------------------------------
    def _build_quant(self):
        self._quant_umax = self.gue_cdf(_SMAX)
        q = [0.0] * (_QN + 1)
        for j in range(_QN + 1):
            u = self._quant_umax * float(j) / _QN
            lo, hi = 0.0, _SMAX
            for _ in range(48):
                mid = 0.5 * (lo + hi)
                if self.gue_cdf(mid) < u:
                    lo = mid
                else:
                    hi = mid
            q[j] = 0.5 * (lo + hi)
        self._quant = q

    def sample(self, rng, out):
        """Fill list `out` with draws from the active spacing law (in place)."""
        if self._quant is None:
            self._build_quant()
        q = self._quant
        for k in range(len(out)):
            x = rng.random() * _QN
            j = int(x)
            if j > _QN - 1:
                j = _QN - 1
            if j < 0:
                j = 0
            t = x - j
            if t > 1.0:
                t = 1.0
            out[k] = (1.0 - t) * q[j] + t * q[j + 1]


RMT = _RmtTable()          # active reference law (process-wide, like the Julia Ref)


def set_spacing_law(name):
    RMT.set_spacing_law(name)


def gue_cdf(s):
    return RMT.gue_cdf(s)


def rmt_sample(rng, out):
    RMT.sample(rng, out)
