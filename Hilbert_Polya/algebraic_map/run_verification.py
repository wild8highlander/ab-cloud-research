# -*- coding: utf-8 -*-
"""run_verification.py — верификация алгебраической карты Φ на реальных
данных пиксельного протокола Hilbert_Polya (24 нуля ζ, веса 1/|ζ'(ρ)|).

Что делается (всё на закоммиченных video/pixel_decoding_data.json):
  1.  Санкция: Ланцош воспроизводит JSON (α, β).
  2.  ТОЧНАЯ (Fraction) ветвь Φ: моменты → Стилтьес-процедура → (α, β², h).
  3.  Сравнение точной Φ с закоммиченным Ланцошем.
  4.  Обратная задача: char-полином из (α, β²) == Π(λ−γ) ТОЧНО в ℚ (24 коэфф.).
  5.  Аннигиляция: Σ c_i μ_{i+j} = 0 точно → D_25 = 0.
  6.  Произведение Πβ² = h_23/h_0 точно; Σα = Σγ точно; Σα²+2Σβ² = Σγ² точно.
  7.  mpmath-ветвь определителей (D, S) при dps=350 против точных рациональностей.
  8.  Тождества следов tr J^k = Σγ^k (k = 1..10, float).
  9.  Резольвента: продолженная дробь ≡ прямая сумма ≡ Q/P (комплексные z).
  10. Квантование Q22: погрешности гейтов, граница Вейля для собственных чисел.
  11. Демонстрация «алгебраической контрольной суммы» (integrity).
  12. Эмпирические профили α_n, β_n (фиты, сравнения с классическими мерами).

Выход: data/amap_results.json, figures/{ru,en}/fig26..28, консольный отчёт.
Запуск:  python3 run_verification.py
"""
import os, sys, json, time
import numpy as np
from fractions import Fraction
from mpmath import mp, mpf

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(REPO, "scripts"))

import jacobi_map as jm          # noqa: E402
import figstyle                  # noqa: E402

DATA_IN = os.path.join(REPO, "video", "pixel_decoding_data.json")
OUT_JSON = os.path.join(HERE, "data", "amap_results.json")
FIG_DIR = os.path.join(HERE, "figures")

t0 = time.time()
R = {"meta": {
    "source": "video/pixel_decoding_data.json (commit e913629 + canon-fix)",
    "N": 24, "Q": 22,
    "weights": "w_n = 1/|zeta'(1/2+i*gamma_n)|, normalized; nu = w^2/sum(w^2)",
    "map": "Phi: (gamma, nu) -> (alpha_0..alpha_23, beta_1..beta_23)",
}}

d = json.load(open(DATA_IN))
gams = np.array(d["typed_zeros"], dtype=float)
w = np.array(d["weights"], dtype=float)
al_json = np.array(d["alphas"], dtype=float)
be_json = np.array(d["betas"], dtype=float)
N = len(gams)

# ---------------------------------------------------------------- 1. санкция
al_l, be_l = jm.lanczos_jacobi(gams, w)
R["sanity_lanczos"] = dict(
    alpha_max_abs=float(np.abs(al_l - al_json).max()),
    beta_max_abs=float(np.abs(be_l - be_json).max()))
print("[1] Lanczos vs JSON: dAlpha_max = %.3e, dBeta_max = %.3e"
      % (R["sanity_lanczos"]["alpha_max_abs"], R["sanity_lanczos"]["beta_max_abs"]))

# ------------------------------------------------------- 2-3. точная ветвь Φ
nu_f = jm.masses_from_weights(w)
al_ex, b2_ex, h_ex = jm.alpha_beta_sequential(gams, nu_f, exact=True)
al_ex_f = np.array([float(a) for a in al_ex])
b2_ex_f = np.array([float(b) for b in b2_ex])
R["exact_vs_lanczos"] = dict(
    alpha_max_abs=float(np.abs(al_ex_f - al_json).max()),
    beta2_max_rel=float(np.abs(b2_ex_f - be_json ** 2).max() / np.abs(be_json ** 2).max()),
    beta_max_rel=float(np.abs(np.sqrt(b2_ex_f) - be_json).max() / be_json.max()))
print("[2] exact Φ vs Lanczos: dAlpha_max = %.3e, beta2_rel = %.3e"
      % (R["exact_vs_lanczos"]["alpha_max_abs"], R["exact_vs_lanczos"]["beta2_max_rel"]))

# ------------------------------------------- 4. обратная задача (точно в ℚ)
cp = jm.charpoly_coeffs(al_ex, b2_ex, exact=True)
cr, e_roots = jm.charpoly_of_roots([Fraction(float(x)) for x in gams], exact=True)
coeff_ok = [cp[i] == cr[i] for i in range(N + 1)]
R["inverse_exact"] = dict(
    coeffs_total=N + 1, coeffs_equal_exact=int(sum(coeff_ok)),
    all_exact=bool(all(coeff_ok)))
print("[3] charpoly(α,β²) == Π(λ−γ): %d/%d коэффициентов равны ТОЧНО"
      % (R["inverse_exact"]["coeffs_equal_exact"], R["inverse_exact"]["coeffs_total"]))

# --------------------------------------------------- 5. аннигиляция, D_25 = 0
res_ann = jm.annihilation_residuals(gams, nu_f, 4, exact=True)
R["annihilation"] = dict(
    kmax=4, residuals_all_zero=bool(all(r == 0 for r in res_ann)),
    statement="rank of moment matrix = N = 24, hence D_25 = 0 exactly")
print("[4] annihilation (=> D_25 = 0):", R["annihilation"]["residuals_all_zero"])

# -------------------------------------- 6. точные тождества на (α, β², h, γ)
p1 = sum((Fraction(float(x)) for x in gams), Fraction(0))
p2 = sum((Fraction(float(x)) ** 2 for x in gams), Fraction(0))
sum_alpha = sum(al_ex, Fraction(0))
sum_a2_2b2 = sum((a * a for a in al_ex), Fraction(0)) + 2 * sum(b2_ex, Fraction(0))
prod_b2 = Fraction(1)
for b in b2_ex:
    prod_b2 *= b
h_ratio = h_ex[-1] / h_ex[0]
R["exact_identities"] = dict(
    sum_alpha_eq_sum_gamma=bool(sum_alpha == p1),
    sum_a2_2b2_eq_p2=bool(sum_a2_2b2 == p2),
    prod_beta2_eq_h_last_over_h0=bool(prod_b2 == h_ratio),
    alpha0_eq_mu1=bool(al_ex[0] == jm.moments(gams, nu_f, 1, exact=True)[1]),
    h_all_positive=bool(all(h > 0 for h in h_ex)),
    alphas_in_spectrum=bool(all(Fraction(float(gams[0])) <= a <= Fraction(float(gams[-1]))
                                for a in al_ex)))
print("[5] exact identities: Σα=Σγ %s, Σα²+2Σβ²=Σγ² %s, Πβ²=h23/h0 %s, α∈[γ1,γ24] %s"
      % (R["exact_identities"]["sum_alpha_eq_sum_gamma"],
         R["exact_identities"]["sum_a2_2b2_eq_p2"],
         R["exact_identities"]["prod_beta2_eq_h_last_over_h0"],
         R["exact_identities"]["alphas_in_spectrum"]))

# witness-мост: mean_alpha и mean_gamma в закоммиченной witness-полосе
wit = dict(d["witness"])
R["witness_checksum"] = dict(
    mean_alpha=wit["mean_alpha"], mean_gamma=wit["mean_gamma"],
    abs_diff=abs(wit["mean_alpha"] - wit["mean_gamma"]),
    note="Σα_n = Σγ_n exactly => witness mean_alpha must equal mean_gamma")
print("[6] witness bridge: mean_alpha − mean_gamma = %.3e (точно равно 0 в ℚ)"
      % R["witness_checksum"]["abs_diff"])

# --------------------------------- 7. ветвь определителей (mpmath dps = 350)
MPDPS = 350
al_mp, b2_mp, logD, logS = jm.alpha_beta_hankel_mp(gams, nu_f, dps=MPDPS)
mp_dps = mp.dps
mp.dps = MPDPS
da = max(abs(al_mp[i] - mpf(al_ex[i].numerator) / mpf(al_ex[i].denominator))
         for i in range(N))
db = max(abs(b2_mp[i - 1] - mpf(b2_ex[i - 1].numerator) / mpf(b2_ex[i - 1].denominator))
         / (mpf(b2_ex[i - 1].numerator) / mpf(b2_ex[i - 1].denominator))
         for i in range(1, N))
mp.dps = mp_dps
R["hankel_mp"] = dict(
    dps=MPDPS,
    alpha_max_abs_diff=float(da), beta2_max_rel_diff=float(db),
    log10_D=[float(x) for x in logD[1:]],
    log10_S=[float(x) for x in logS[1:]],
    log10_h=[float(mp.log10(mpf(abs(h.numerator)) / mpf(h.denominator))
                   * (1 if h > 0 else -1))
             for h in h_ex])
print("[7] determinant branch (dps=%d): |α_mp − α_exact|max = %.3e, rel(β²) = %.3e"
      % (MPDPS, R["hankel_mp"]["alpha_max_abs_diff"], R["hankel_mp"]["beta2_max_rel_diff"]))

# ------------------------------------------------- 8. тождества следов (float)
J = jm.tridiag(al_ex_f, np.sqrt(b2_ex_f))
p_k = np.array([float(np.sum(gams ** k)) for k in range(1, 11)])
tr_k = jm.trace_powers(J, 10)
rel_tr = np.abs(tr_k - p_k) / np.abs(p_k)
R["trace_identities"] = dict(
    k=list(range(1, 11)), rel_residual=[float(x) for x in rel_tr],
    max_rel=float(rel_tr.max()))
print("[8] trace identities tr J^k = Σγ^k: max rel resid (k=1..10) = %.3e"
      % R["trace_identities"]["max_rel"])

# ----------------------------------------------------------- 9. резольвента
zpts = [5 + 5j, 40 + 30j, 100 + 2j, 3 + 60j, 90 + 0.5j]
b2_f = [float(b) for b in b2_ex]
res_pts = []
for z in zpts:
    s1 = jm.resolvent_cf(z, al_ex_f, b2_f)
    s2 = jm.resolvent_direct(z, gams, nu_f)
    s3 = jm.resolvent_qp(z, gams, nu_f)
    res_pts.append(dict(z=str(z), cf_vs_direct=abs(s1 - s2), cf_vs_qp=abs(s1 - s3)))
R["resolvent"] = dict(points=res_pts,
                      max_diff=float(max(max(p["cf_vs_direct"], p["cf_vs_qp"])
                                         for p in res_pts)))
print("[9] resolvent CF == direct == Q/P: max |ΔS| = %.3e" % R["resolvent"]["max_diff"])

# ------------------------------------------------------- 10. квантование Q22
gate_err = [abs(jm.decode(jm.encode(g["value"])) - g["value"]) for g in d["gates"]]
R["quantization"] = dict(
    n_gates=len(gate_err),
    max_gate_err=float(max(gate_err)),
    half_ulp_2p23=2.0 ** -23,
    within_half_ulp=bool(max(gate_err) <= 2.0 ** -23))
J_dec = np.zeros((N, N))
for i in range(N):
    for j in range(N):
        J_dec[i, j] = jm.decode(jm.encode(J[i, j]))
J_dec = 0.5 * (J_dec + J_dec.T)
deltaJ = J_dec - J
weyl = float(np.linalg.norm(deltaJ, 2))
frob = float(np.linalg.norm(deltaJ, "fro"))
R["quantization"].update(
    weyl_norm_2=weyl, frobenius=frob,
    max_eig_err_reported=d["decode"]["max_eig_err"],
    weyl_bound_holds=bool(d["decode"]["max_eig_err"] <= weyl),
    det_root_err_max=d["stats"]["max_abs_delta"],
    det_root_err_rms=d["stats"]["rms_delta"])
print("[10] Q22: max gate err = %.3e ≤ 2^-23 = %.3e; Weyl ‖ΔJ‖₂ = %.3e ≥ eig err %.3e"
      % (R["quantization"]["max_gate_err"], 2.0 ** -23, weyl,
         R["quantization"]["max_eig_err_reported"]))

# ---------------------------------------- 11. алгебраическая контрольная сумма
id_pristine = float(abs(np.sum(al_ex_f ** 2) + 2 * np.sum(b2_ex_f)
                        - float(np.sum(gams ** 2))) / float(np.sum(gams ** 2)))
b2_pert = list(b2_ex_f)
b2_pert[4] += 2.0 ** -22          # один квант канвы в β₅²
id_perturbed = float(abs(np.sum(al_ex_f ** 2) + 2 * np.sum(b2_pert)
                         - float(np.sum(gams ** 2))) / float(np.sum(gams ** 2)))
R["integrity_checksum"] = dict(
    identity="Σα² + 2Σβ² − Σγ² (k=2), relative",
    residual_pristine=id_pristine,
    residual_one_quantum=id_perturbed,
    amplification=id_perturbed / max(id_pristine, 1e-300))
print("[11] checksum: pristine %.2e -> one-quantum %.2e (x%.0f)"
      % (id_pristine, id_perturbed, R["integrity_checksum"]["amplification"]))

# ------------------------------------------------------ 12. профили α, β
nn = np.arange(1, N + 1)
ca = np.polyfit(nn, al_ex_f, 1)
ra = np.polyval(ca, nn)
r2_alpha = float(1 - np.sum((al_ex_f - ra) ** 2) / np.sum((al_ex_f - al_ex_f.mean()) ** 2))
ca2 = np.polyfit(nn, al_ex_f, 2)
ra2 = np.polyval(ca2, nn)
r2_alpha2 = float(1 - np.sum((al_ex_f - ra2) ** 2) / np.sum((al_ex_f - al_ex_f.mean()) ** 2))
mn = np.arange(1, N)             # n = 1..23 — номера β
mb = be_json                     # β_1..β_23
A = np.polyfit(np.log(mn), np.log(mb), 1)
beta_pow = (float(np.exp(A[1])), float(A[0]))
pred = beta_pow[0] * mn ** beta_pow[1]
r2_beta_pow = float(1 - np.sum((mb - pred) ** 2) / np.sum((mb - mb.mean()) ** 2))
B = np.polyfit(mn, np.log(mb), 1)
beta_exp = (float(np.exp(B[1])), float(B[0]))
pred2 = beta_exp[0] * np.exp(beta_exp[1] * mn)
r2_beta_exp = float(1 - np.sum((mb - pred2) ** 2) / np.sum((mb - mb.mean()) ** 2))
a_rng = (float(gams[-1] - gams[0]))
R["profiles"] = dict(
    alpha_linear=dict(slope=float(ca[0]), intercept=float(ca[1]), r2=r2_alpha),
    alpha_quadratic_r2=r2_alpha2,
    beta_power=dict(A=beta_pow[0], p=beta_pow[1], r2=r2_beta_pow),
    beta_exponential=dict(A=beta_exp[0], k=beta_exp[1], r2=r2_beta_exp),
    semicircle_ref=dict(alpha_const=float(0.5 * (gams[0] + gams[-1])),
                        beta_const=a_rng / 4.0),
    mean_beta=float(be_json.mean()), sum_beta=float(be_json.sum()),
    mu1=float(al_ex[0]), mean_gamma=float(gams.mean()),
    nu1=float(nu_f[0]))
print("[12] profiles: α lin R²=%.3f, quad R²=%.3f | β power A=%.2f p=%.3f R²=%.3f, exp R²=%.3f"
      % (r2_alpha, r2_alpha2, beta_pow[0], beta_pow[1], r2_beta_pow, r2_beta_exp))

# ------------------------------------------------------------- сохранить JSON
R["alphas_exact_float"] = al_ex_f.tolist()
R["betas2_exact_float"] = b2_ex_f.tolist()
R["h_float"] = [float(mp.mpf(h.numerator) / mp.mpf(h.denominator)) for h in h_ex]
R["exact_fractions_head"] = {
    "alpha_0": str(al_ex[0])[:60] + "...",
    "beta1_2": str(b2_ex[0])[:60] + "...",
    "alpha_0_num_digits": len(str(al_ex[0].numerator)),
    "alpha_0_den_digits": len(str(al_ex[0].denominator)),
}
os.makedirs(os.path.dirname(OUT_JSON), exist_ok=True)
json.dump(R, open(OUT_JSON, "w"), indent=1, ensure_ascii=False)
print("JSON ->", OUT_JSON, "(%.1f s)" % (time.time() - t0))

# ================================================================= FIGURES ==
from matplotlib import pyplot as plt  # noqa: E402

LANG = {
    "ru": dict(
        f26="Профили коэффициентов Якоби ζ-меры (N = 24)",
        f26a="диагональ αₙ", f26b="внедиагональ βₙ", nx="n (номер гейта)",
        sumline="Σαₙ = Σγₙ (точно)", mu1line="α₀ = μ₁ = 44.85",
        fitpow="фит βₙ ≈ %.1f·n^(−%.2f)  (R² = %.3f)" % (beta_pow[0], beta_pow[1], r2_beta_pow),
        semicirc="полукруг (b−a)/4 = 18.32",
        f27a="определители моментов ζ-меры", logD="log₁₀ Dₙ", logS="log₁₀ Sₙ",
        d25="D₂₅ = 0 точно", nn="размер n",
        f27b="ошибка декодирования и граница Вейля",
        dgamma="|Δγᵢ| (корни det-рекурсии)", weyl="‖ΔJ‖₂ = %.2e" % weyl,
        q22="квант 2⁻²²", yi="i", dg="|Δγᵢ|",
        f28a="S(z), z = x + 15i", imS="Im S(z)", xax="x",
        cf="продолженная дробь (α, β)", direct="прямая сумма Σν/(z−γ)",
        qp="Q(z)/P(z)", f28b="невязки представлений", resid="log₁₀ |ΔS|",
        cfd="дробь − сумма", cfq="дробь − Q/P"),
    "en": dict(
        f26="Jacobi coefficient profiles of the ζ-measure (N = 24)",
        f26a="diagonal αₙ", f26b="off-diagonal βₙ", nx="n (gate index)",
        sumline="Σαₙ = Σγₙ (exact)", mu1line="α₀ = μ₁ = 44.85",
        fitpow="fit βₙ ≈ %.1f·n^(−%.2f)  (R² = %.3f)" % (beta_pow[0], beta_pow[1], r2_beta_pow),
        semicirc="semicircle (b−a)/4 = 18.32",
        f27a="moment determinants of the ζ-measure", logD="log₁₀ Dₙ", logS="log₁₀ Sₙ",
        d25="D₂₅ = 0 exact", nn="size n",
        f27b="decode error and the Weyl bound",
        dgamma="|Δγᵢ| (det-recursion roots)", weyl="‖ΔJ‖₂ = %.2e" % weyl,
        q22="quantum 2⁻²²", yi="i", dg="|Δγᵢ|",
        f28a="S(z), z = x + 15i", imS="Im S(z)", xax="x",
        cf="continued fraction (α, β)", direct="direct sum Σν/(z−γ)",
        qp="Q(z)/P(z)", f28b="representation residuals", resid="log₁₀ |ΔS|",
        cfd="fraction − sum", cfq="fraction − Q/P"),
}

tok = figstyle.apply("light")
TEAL, COPPER, SLATE = tok["line"], tok["copper"], tok["slate"]


def save(fig, stem, lang):
    ddir = os.path.join(FIG_DIR, lang)
    os.makedirs(ddir, exist_ok=True)
    fig.savefig(os.path.join(ddir, "%s_%s.png" % (stem, lang)), dpi=220)
    plt.close(fig)


def draw_fig26(L):
    fig, axs = plt.subplots(1, 2, figsize=(10.6, 4.0), constrained_layout=True)
    ax = axs[0]
    ax.plot(nn, al_ex_f, "o", ms=5.5, color=COPPER, label=L["f26a"])
    ax.axhline(float(gams.mean()), color=TEAL, ls="--", lw=1.2, label=L["sumline"])
    ax.axhline(float(al_ex[0]), color=SLATE, ls=":", lw=1.2, label=L["mu1line"])
    ax.set_title(L["f26"]); ax.set_xlabel(L["nx"]); ax.set_ylabel("αₙ")
    ax.legend(loc="lower right"); figstyle.clean_axis(ax)
    ax = axs[1]
    nbe = np.arange(1, N)          # β₁..β₂₃
    ax.plot(nbe, be_json, "o", ms=5.5, color=COPPER, label=L["f26b"])
    xx = np.linspace(1, N, 300)
    ax.plot(xx[1:], beta_pow[0] * xx[1:] ** beta_pow[1], "-", color=TEAL, lw=1.4,
            label=L["fitpow"])
    ax.axhline(a_rng / 4.0, color=SLATE, ls=":", lw=1.2, label=L["semicirc"])
    ax.set_xlabel(L["nx"]); ax.set_ylabel("βₙ")
    ax.legend(loc="upper right"); figstyle.clean_axis(ax)
    return fig


def draw_fig27(L):
    fig, axs = plt.subplots(1, 2, figsize=(10.6, 4.0), constrained_layout=True)
    ax = axs[0]
    ax.plot(range(1, N + 1), R["hankel_mp"]["log10_D"], "s-", ms=4, color=TEAL,
            label=L["logD"])
    ax.plot(range(1, N + 1), R["hankel_mp"]["log10_S"], "o--", ms=4, color=SLATE,
            label=L["logS"])
    ax.set_title(L["f27a"]); ax.set_xlabel(L["nn"]); ax.set_ylabel("log₁₀ |·|")
    ax.annotate(L["d25"], xy=(23.5, R["hankel_mp"]["log10_D"][-1]),
                xytext=(9, R["hankel_mp"]["log10_D"][-1] + 5),
                arrowprops=dict(arrowstyle="->", color=COPPER), color=COPPER)
    ax.legend(loc="upper right"); figstyle.clean_axis(ax)
    ax = axs[1]
    ax.semilogy(range(1, N + 1), np.abs(np.array(d["deltas"])) + 1e-16, "o", ms=5,
                color=COPPER, label=L["dgamma"])
    ax.axhline(weyl, color=TEAL, ls="--", lw=1.3, label=L["weyl"])
    ax.axhline(2.0 ** -22, color=SLATE, ls=":", lw=1.3, label=L["q22"])
    ax.set_title(L["f27b"]); ax.set_xlabel(L["yi"]); ax.set_ylabel(L["dg"])
    ax.legend(loc="lower right"); figstyle.clean_axis(ax)
    return fig


xx = np.linspace(3.0, 98.0, 400)
zz = xx + 15j
b2_f = [float(b) for b in b2_ex]
S_cf = np.array([jm.resolvent_cf(z, al_ex_f, b2_f) for z in zz])
S_di = np.array([jm.resolvent_direct(z, gams, nu_f) for z in zz])
S_qp = np.array([jm.resolvent_qp(z, gams, nu_f) for z in zz])
res_cf_d = np.abs(S_cf - S_di) + 1e-18
res_cf_q = np.abs(S_cf - S_qp) + 1e-18


def draw_fig28(L):
    fig, axs = plt.subplots(1, 2, figsize=(10.6, 4.0), constrained_layout=True)
    ax = axs[0]
    ax.plot(xx, S_cf.imag, "-", color=TEAL, lw=2.2, label=L["cf"])
    ax.plot(xx, S_di.imag, "--", color=COPPER, lw=1.2, label=L["direct"])
    ax.plot(xx, S_qp.imag, ":", color=SLATE, lw=2.0, label=L["qp"])
    ax.set_title(L["f28a"]); ax.set_xlabel(L["xax"]); ax.set_ylabel(L["imS"])
    ax.legend(loc="upper right"); figstyle.clean_axis(ax)
    ax = axs[1]
    ax.semilogy(xx, res_cf_d, "-", color=TEAL, lw=1.5, label=L["cfd"])
    ax.semilogy(xx, res_cf_q, "--", color=COPPER, lw=1.5, label=L["cfq"])
    ax.set_title(L["f28b"]); ax.set_xlabel(L["xax"]); ax.set_ylabel(L["resid"])
    ax.legend(loc="upper right"); figstyle.clean_axis(ax)
    return fig


for lang in ("ru", "en"):
    L = LANG[lang]
    save(draw_fig26(L), "fig26_jacobi_profiles", lang)
    save(draw_fig27(L), "fig27_hankel_integrity", lang)
    save(draw_fig28(L), "fig28_resolvent", lang)

print("figures ->", FIG_DIR, "(total %.1f s)" % (time.time() - t0))
