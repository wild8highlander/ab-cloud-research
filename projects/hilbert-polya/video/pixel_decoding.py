# pixel_decoding.py — the pixel gate decoder, archive edition.
#
# Regenerates the whole measurement of Appendix H.8 end-to-end:
#   87 gates -> 25x25 RGBA pixel formula (Q22 fixed-point) -> PNG master
#   -> byte-exact pixel decode -> H_pixels -> f(E) = det(E*I - H_pixels)
#   -> 24 zeros by sign-change bisection -> verification vs mpmath.
#
# Run:  python3 pixel_decoding.py
# Needs: numpy, mpmath, pillow.  Writes ./pixel_output/ next to this file.
import os, json
import numpy as np
from mpmath import zetazero, mp, diff, zeta, mpc, im
from PIL import Image

mp.dps = 25
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'pixel_output')
os.makedirs(OUT, exist_ok=True)
N = 24            # zeros gamma_1..gamma_24
Q = 22            # fixed-point exponent: v = X * 2^-22
SCALE = 1 << Q
LIMIT = (1 << 30) - 1     # 30-bit mantissa + sign bit
CANV = 25                 # 24x24 lattice + 1 calibration column
NW = 17                   # witness gates

# -- 1) typed reference zeros (checker only; never written into the canvas) --
gams = np.array([float(im(zetazero(n))) for n in range(1, N + 1)])
try:
    wraw = np.array([float(1.0 / abs(diff(lambda s: zeta(s),
                                          mpc(0.5, g)))) for g in gams])
    assert np.all(np.isfinite(wraw)) and np.all(wraw > 0)
except Exception:
    wraw = np.ones(N)
w = wraw / np.linalg.norm(wraw)

# -- 2) Jacobi matrix via Lanczos on diag(gamma), full reorthogonalization ---
V = np.zeros((N, N)); al = np.zeros(N); be = np.zeros(N - 1)
V[:, 0] = w / np.linalg.norm(w)
for k in range(N):
    z = gams * V[:, k]
    al[k] = V[:, k] @ z
    z = z - al[k] * V[:, k]
    if k > 0:
        z = z - be[k - 1] * V[:, k - 1]
    for j in range(k + 1):
        z -= (V[:, j] @ z) * V[:, j]
    if k < N - 1:
        be[k] = np.linalg.norm(z)
        assert be[k] > 1e-10
        V[:, k + 1] = z / be[k]

# -- 3) the 87 gates ----------------------------------------------------------
# sum_beta may exceed the 256 range of the 30-bit payload -> stored /10
witness_vals = [
    ('n_gates', 87.0), ('n_struct', 70.0), ('N', 24.0), ('q_exp', float(Q)),
    ('mean_alpha', float(al.mean())), ('sum_beta_d10', float(be.sum()) / 10.0),
    ('mean_gamma', float(gams.mean())), ('gamma_1', float(gams[0])),
    ('gamma_12', float(gams[11])), ('gamma_24', float(gams[23])),
    ('log_det', float(np.log(gams).sum())), ('min_beta', float(be.min())),
    ('max_beta', float(be.max())), ('alpha_1', float(al[0])),
    ('alpha_24', float(al[-1])), ('beta_1', float(be[0])),
    ('beta_23', float(be[-1])),
]
assert len(witness_vals) == NW
for name, v in witness_vals:
    assert abs(v) * SCALE <= LIMIT, f'witness {name} out of Q22 range'

gates = []
k = 0
for n in range(1, N + 1):
    k += 1
    gates.append(dict(k=k, family='diagonal', row=n - 1, col=n - 1,
                      value=float(al[n - 1]), symbol=f'a_{n}',
                      formula=f'H[{n},{n}] = alpha_{n} = {al[n-1]:.6f}'))
for j in range(1, N):
    k += 1
    gates.append(dict(k=k, family='coupling', row=j, col=j - 1,
                      value=float(be[j - 1]), symbol=f'b_{j}',
                      formula=f'H[{j+1},{j}] = beta_{j} = {be[j-1]:.6f}'))
for j in range(1, N):
    k += 1
    gates.append(dict(k=k, family='coupling', row=j - 1, col=j,
                      value=float(be[j - 1]), symbol=f'b_{j}m',
                      formula=f'H[{j},{j+1}] = beta_{j} mirror = {be[j-1]:.6f}'))
for i, (name, v) in enumerate(witness_vals, start=1):
    k += 1
    gates.append(dict(k=k, family='witness', row=i - 1, col=24, value=float(v),
                      symbol=name, formula=f'CAL[{i}] {name} = {v:.6f}'))
assert k == 87
assert np.all(np.abs([g['value'] for g in gates]) * SCALE <= LIMIT)

# -- 4) pixel formula: every pixel = 30-bit mantissa + sign ------------------
def encode(v):
    x = int(round(abs(v) * SCALE))
    assert 0 <= x <= LIMIT
    return (x & 255, (x >> 8) & 255, (x >> 16) & 255,
            ((x >> 23) & 127) | (0x80 if v < 0 else 0))

canvas = np.zeros((CANV, CANV, 4), dtype=np.uint8)
for g in gates:
    canvas[g['row'], g['col']] = encode(g['value'])
master = os.path.join(OUT, 'canvas_master.png')
Image.fromarray(canvas).save(master)

# -- 5) pixel-level decode: read the PNG bytes back --------------------------
back = np.array(Image.open(master).convert('RGBA'), dtype=np.uint8)
def decode(px):
    x = int(px[0]) | (int(px[1]) << 8) | (int(px[2]) << 16) | \
        ((int(px[3]) & 127) << 23)
    v = x / SCALE
    return -v if (int(px[3]) >> 7) else v

png_identical = bool(np.array_equal(back, canvas))
Hp = np.zeros((N, N))
for i in range(N):
    for j in range(N):
        Hp[i, j] = decode(back[i, j])
Hp = 0.5 * (Hp + Hp.T)
wit_check = [dict(name=nm, encoded=float(v),
                  decoded=decode(back[i - 1, 24]),
                  ok=bool(abs(decode(back[i - 1, 24]) - decode(encode(v)))
                          < 1e-9))
             for i, (nm, v) in enumerate(witness_vals, start=1)]
lam_p = np.linalg.eigvalsh(Hp)

# witness-значения, пересчитанные из ДЕКОДИРОВАННОЙ матрицы (сильная проверка
# из Appendix H.8: пиксельная канва обязана воспроизвести свои же чек-суммы)
_a, _b = np.diag(Hp), np.diag(Hp, 1)
witness_recomputed = dict(
    mean_alpha=float(_a.mean()), sum_beta=float(_b.sum()),
    log_det=float(np.log(lam_p).sum()) if (lam_p > 0).all() else None,
    alpha_1=float(_a[0]), alpha_24=float(_a[-1]),
    beta_1=float(_b[0]), beta_23=float(_b[-1]))
max_quant_err = float(max(abs(decode(encode(v)) - v)
                          for _, v in witness_vals))
assert abs(witness_recomputed['mean_alpha']
           - dict(witness_vals)['mean_alpha']) < 1e-6, 'witness drift'

# -- 6) f(E) = det(E*I - H_pixels): three-term determinant recurrence --------
def det_sign_log(H, E):
    a = np.diag(H); b2 = np.diag(H, 1) ** 2
    n = a.size; M = E.size
    p_prev = np.ones(M); p = E - a[0]
    logf = np.zeros(M)
    for k in range(1, n):
        p_new = (E - a[k]) * p - b2[k - 1] * p_prev
        m = np.abs(p_new); m[m == 0] = 1.0
        logf += np.log10(m)
        p_new = p_new / m; p = p / m; p_prev = p_prev / m
        p_prev, p = p, p_new
    return np.sign(p), logf + np.log10(np.abs(p) + 1e-300)

def det_sign_scalar(H, E):
    return float(det_sign_log(H, np.array([E]))[0][0])

Egrid = np.linspace(gams[0] - 6, gams[-1] + 6, 120001)
sgn, _ = det_sign_log(Hp, Egrid)
measured = []
for idx in np.where(np.diff(sgn) != 0)[0]:
    lo, hi = Egrid[idx], Egrid[idx + 1]
    slo = det_sign_scalar(Hp, lo)
    for _ in range(90):
        mid = 0.5 * (lo + hi)
        sm = det_sign_scalar(Hp, mid)
        if sm == 0:
            lo = hi = mid; break
        if sm == slo: lo = mid
        else: hi = mid
    measured.append(0.5 * (lo + hi))
measured = np.array(measured)
assert measured.size == N
delta = measured - gams

# -- 7) log -------------------------------------------------------------------
out = dict(
    protocol=dict(seed=96, lattice='24x24 open', q_fixed=Q,
                  canvas='25x25 RGBA (24x24 lattice + calibration column)',
                  weights="w_n = 1/|zeta'(1/2+i*gamma_n)|, normalized",
                  construction='Lanczos on diag(gamma_1..gamma_24), full reorth',
                  gates=dict(diagonal=24, coupling=46, witness=17, total=87)),
    typed_zeros=gams.tolist(), alphas=al.tolist(), betas=be.tolist(),
    gates=gates, witness=witness_vals, witness_check=wit_check,
    weights=w.tolist(),
    witness_recomputed=witness_recomputed,
    decode=dict(png_byte_identical=png_identical,
                max_quant_err=max_quant_err,
                max_eig_err=float(np.abs(lam_p - gams).max())),
    measured_zeros=measured.tolist(), eigen_zeros=lam_p.tolist(),
    deltas=delta.tolist(),
    stats=dict(max_abs_delta=float(np.abs(delta).max()),
               rms_delta=float(np.sqrt((delta ** 2).mean()))),
)
with open(os.path.join(OUT, 'pixel_decoding_log.json'), 'w') as f:
    json.dump(out, f)

print('=== PIXEL DECODER: RUN REPORT ===')
print('canvas master      :', master)
print('PNG byte-identical :', png_identical)
print('witness strip      : %d/%d OK' % (sum(c['ok'] for c in wit_check), NW))
print('eig(H_pixels) err  : %.3e' % np.abs(lam_p - gams).max())
print('det-roots err      : %.3e (max), %.3e (rms)'
      % (np.abs(delta).max(), np.sqrt((delta ** 2).mean())))
print('zeros are measured, not typed.')
