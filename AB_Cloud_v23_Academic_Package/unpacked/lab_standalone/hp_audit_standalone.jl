#!/usr/bin/env julia
# =============================================================================
#   ╔═════════════════════════════════════════════════════════════════════╗
#   ║  HP·MERIDIAN — Hilbert–Pólya Deep Audit · compact standalone         ║
#   ║  module HPMeridian · v24.1-SA · core from ab_cloud_v23_v2.jl (suite) ║
#   ╚═════════════════════════════════════════════════════════════════════╝
#  Author: Isaev Iskhak Khamzatovich (ORCID: 0009-0003-7299-0701)
#
#  WHY THIS FILE EXISTS (user spec 2026-09-07):
#    «отдельный код, в котором только проверка H — тесты из меню h — чтобы не
#     вносить правки в дальнейшем в огромный код, а в более компактный, который
#     конкретно проверяет нужное нам конкретно сейчас».
#    → This file contains ONLY the H1–H7 Hilbert–Pólya audits (plus their
#      physics/statistics core, lifted VERBATIM from the suite so every number
#      matches the full suite bit-for-bit at equal seeds). Edit HERE first;
#      port a stabilized change back into ab_cloud_v23_v2.jl when both must
#      stay in sync.
#
#  WHAT'S INSIDE
#    • 7 GATES (unique console names): H1 PRIME-TRACE (raw-FT Bragg comb at
#      ω = log p + composite DECOY control + regime-matched nulls + DEEPEN
#      P95 protocol), H2 WEYL-DOS (raw N(E) staircase, AICc showdown),
#      H3 POWER-LAW (exponent ladder, dictionary falsification), H4
#      CRITICAL-Q (sharpness scan + domain guard), H5 REGIME-2×2 (ensemble
#      showdown + α-profile: finetuning vs plateau), H6 HERMIT-STRESS
#      (self-adjointness/stability), H7 SEQ-CORR (level↔zero correlation);
#    • v23.6 honest done-line: "done → PASS/WARN" carries the REAL verdict;
#    • HP·MERIDIAN console (v23.7-SA): unique gate names, environment
#      doctor, gate intel with cost estimates, config profiles, failure-
#      isolated commands, ANSI-safe color, Ctrl-C/EOF-safe input.
#
#  v23.8-SA — «hangs on the 5th test / no progress bar» FIX (2026-09-09):
#    The report tee re-points fd 1 at a capture FILE for the whole gate, so
#    every prog_update line was invisible until the gate ENDED — a multi-hour
#    H5 looked frozen. Now:
#    1) the progress bar draws IN PLACE through a tee-bypassing dup of the
#       real terminal fd (_live_write) — visible DURING the gate, with
#       T+elapsed · ETA · the current realization;
#    2) a `sh` subprocess heartbeat prints an «alive» line to /dev/tty every
#       60 s over ONE blocking LAPACK call (tasks/timers cannot fire during a
#       ccall on 1 thread — this is the only honest feedback channel);
#    3) LIVE cost lines before every gate + a whole-battery estimate upfront
#       (H5 at FULL ≈ 340 dense 3136×3136 solves — hours, NOT a hang);
#    4) H5's fraction plan fixed (the bar jumped 87%→60% at the α-profile);
#    5) dead _prog_tty()/prog_tag! references defined (crashed on >1 thread).
#
#  v24.1-SA — «максимум 40 диагонализаций в H5» + Julia 1.12 TTY fd hotfix
#  (2026-09-09):
#    1) H5 SOLVE BUDGET (user cap: «максимум 40 — это избыточно»): every H5
#       plan now goes through ONE planner _hp5_plan → at most
#       HP5_SOLVE_CAP = 40 dense eigensolves TOTAL: 2×2 regimes × ≤7 configs
#       (≤28) + α-profile 6 points × ≤2 configs (≤12). The FAST preset used
#       to ask 4×100 + 6×40 = 640 solves. The planner is SHARED by the gate
#       and the cost estimator, so the «battery cost» banner can never again
#       promise more than the gate will run. The old scored «ensemble ≥ 30»
#       row became the budget-compliance row — a cap must not be a silent
#       auto-FAIL; per-config KS granularity (1/N) is printed instead.
#    2) Julia 1.12 fd hotfix (user device, real terminal): Base.fd no longer
#       accepts Libuv streams on 1.12 (methods remain only for IOStream /
#       File / Sockets) — EVERY gate died in 00:00:00 with
#       «MethodError: no method matching fd(::Base.TTY)» the moment
#       rep_tee_stdout opened. New _mr_fdof(): unwrap IOContext → Base.fd
#       (IOStream/File) → uv_fileno on the TTY's own uv handle. Bonus catch:
#       Base.isatty was REMOVED in 1.12 too — _prog_tty()'s try/catch had
#       been silently answering false there, demoting the live bar to
#       append-only lines; the check is now the TTY type itself.
#       Verified on sandbox julia 1.10.4 AND 1.12.0 under a real pty.
#
#  START — THREE WAYS
#    1) REPL:      julia> include("hp_audit_standalone.jl")
#                  → the HP·MERIDIAN console OPENS ITSELF.
#                    q / Ctrl-C returns to the REPL, code stays loaded;
#                    hp_console() reopens it anytime.
#    2) TERMINAL:  julia hp_audit_standalone.jl        (no args → console)
#    3) BATCH:     julia hp_audit_standalone.jl fast h1 h5 seed=777 zeros=path
#    Re-include SAFE: everything lives in module HPMeridian — including the
#    file twice (the natural edit-and-retry REPL loop) just replaces the
#    module; the v23.6.1 "invalid redefinition of constant" storm is gone.
#    Switches: ENV["HP_SA_NO_MENU"]="1" → no console on include;
#              ENV["HP_SA_COLOR"]="0" → plain ASCII output.
#
#  CONSOLE COMMANDS (all wired, all failure-isolated)
#    1..7 run gate · a all seven · gA gB gC gD reviewer groups A–D
#    s SMOKE (~2-3 min) · f FAST (~10-20 min) · F FULL (hours) · r reset
#    p parameters — ALL 35 HPConfig fields with short hints + full docs
#      (? field), soft sanity warnings, save/load/ls config profiles
#    i gate intel (decides-what + per-preset cost) · d doctor (zeros, output
#      dir, sanity) · v last run verdicts · z ζ-zeros path · h help · q quit
#
#  ζ ZEROS: H1/H7 need the zero ordinates. Auto-discovered: $HP_ZEROS →
#    zeros50k.txt next to this script → zeros50k.txt in the working dir.
#    Without zeros the battery still runs — H1/H7 skip their ζ side honestly.
#
#  OUTPUT (per run, results/run_<timestamp>/ of the WORKING directory)
#    test_30X_<slug>_REPORT.txt   per-test console capture (the full report)
#    test_30X_<slug>/plots/*.png  1600×1000 ABPlotV23-engine PNGs
#    logs/full_run_log.txt        ONE consolidated log: per-test computation
#                                 log + console capture + notes (run order)
#    final_report.md / .html      master report: verdicts, sub-check tables,
#                                 notes, plots (two-files contract: the whole
#                                 run is readable from final_report.md + this
#                                 run's logs/full_run_log.txt)
#    results_verdicts.txt         one-line verdicts (results-log mirror)
# =============================================================================

module HPMeridian

using LinearAlgebra
using Random
using Statistics
using Printf
using Dates

const HP_SA_VERSION = "24.2-SA"   # console identity: HP·MERIDIAN
export hp_console, hp_menu, main, make_hp_config, apply_preset!,
       hp_params_menu!, run_battery_core, load_zeros, register_audits!,
       HPConfig, HP_AUDITS

module ABPlotV23

using Printf: @sprintf

# == Hershey vector fonts (public domain, Dr. A.V. Hershey, NBS) ==
# ASCII simplex (95) + Greek simplex (48). record: count(3) left(1) right(1) pairs
# coords: x = ord(c)-82, y = ord(c)-82 (y down); " R" = pen-up
const _HERSHEY_RAW = Tuple{Int,String}[
    (32, "  1JZ"),
    (33, "  9MWRFRT RRYQZR[SZRY"),
    (34, "  6JZNFNM RVFVM"),
    (35, " 12H]SBLb RYBRb RLOZO RKUYU"),
    (36, " 27H\\PBP_ RTBT_ RYIWGTFPFMGKIKKLMMNOOUQWRXSYUYXWZT[P[MZKX"),
    (37, " 32F^[FI[ RNFPHPJOLMMKMIKIIJGLFNFPGSHVHYG[F RWTUUTWTYV[X[ZZ[X[VYTWT"),
    (38, " 35E_\\O\\N[MZMYNXPVUTXRZP[L[JZIYHWHUISJRQNRMSKSIRGPFNGMIMKNNPQUXWZY[[[\\Z\\Y"),
    (39, "  8MWRHQGRFSGSIRKQL"),
    (40, " 11KYVBTDRGPKOPOTPYR]T`Vb"),
    (41, " 11KYNBPDRGTKUPUTTYR]P`Nb"),
    (42, "  9JZRFRR RMIWO RWIMO"),
    (43, "  6E_RIR[ RIR[R"),
    (44, "  9MWSZR[QZRYSZS\\R^Q_"),
    (45, "  3E_IR[R"),
    (46, "  6MWRYQZR[SZRY"),
    (47, "  3G][BIb"),
    (48, " 18H\\QFNGLJKOKRLWNZQ[S[VZXWYRYOXJVGSFQF"),
    (49, "  5H\\NJPISFS["),
    (50, " 15H\\LKLJMHNGPFTFVGWHXJXLWNUQK[Y["),
    (51, " 16H\\MFXFRNUNWOXPYSYUXXVZS[P[MZLYKW"),
    (52, "  7H\\UFKTZT RUFU["),
    (53, " 18H\\WFMFLOMNPMSMVNXPYSYUXXVZS[P[MZLYKW"),
    (54, " 24H\\XIWGTFRFOGMJLOLTMXOZR[S[VZXXYUYTXQVOSNRNOOMQLT"),
    (55, "  6H\\YFO[ RKFYF"),
    (56, " 30H\\PFMGLILKMMONSOVPXRYTYWXYWZT[P[MZLYKWKTLRNPQOUNWMXKXIWGTFPF"),
    (57, " 24H\\XMWPURRSQSNRLPKMKLLINGQFRFUGWIXMXRWWUZR[P[MZLX"),
    (58, " 12MWRMQNROSNRM RRYQZR[SZRY"),
    (59, " 15MWRMQNROSNRM RSZR[QZRYSZS\\R^Q_"),
    (60, "  4F^ZIJRZ["),
    (61, "  6E_IO[O RIU[U"),
    (62, "  4F^JIZRJ["),
    (63, " 21I[LKLJMHNGPFTFVGWHXJXLWNVORQRT RRYQZR[SZRY"),
    (64, " 56E`WNVLTKQKOLNMMPMSNUPVSVUUVS RQKOMNPNSOUPV RWKVSVUXVZV\\T]Q]O\\L[JYHWGTFQFNGLHJJILHOHRIUJWLYNZQ[T[WZYYZX RXKWSWUXV"),
    (65, "  9I[RFJ[ RRFZ[ RMTWT"),
    (66, " 24G\\KFK[ RKFTFWGXHYJYLXNWOTP RKPTPWQXRYTYWXYWZT[K["),
    (67, " 19H]ZKYIWGUFQFOGMILKKNKSLVMXOZQ[U[WZYXZV"),
    (68, " 16G\\KFK[ RKFRFUGWIXKYNYSXVWXUZR[K["),
    (69, " 12H[LFL[ RLFYF RLPTP RL[Y["),
    (70, "  9HZLFL[ RLFYF RLPTP"),
    (71, " 23H]ZKYIWGUFQFOGMILKKNKSLVMXOZQ[U[WZYXZVZS RUSZS"),
    (72, "  9G]KFK[ RYFY[ RKPYP"),
    (73, "  3NVRFR["),
    (74, " 11JZVFVVUYTZR[P[NZMYLVLT"),
    (75, "  9G\\KFK[ RYFKT RPOY["),
    (76, "  6HYLFL[ RL[X["),
    (77, " 12F^JFJ[ RJFR[ RZFR[ RZFZ["),
    (78, "  9G]KFK[ RKFY[ RYFY["),
    (79, " 22G]PFNGLIKKJNJSKVLXNZP[T[VZXXYVZSZNYKXIVGTFPF"),
    (80, " 14G\\KFK[ RKFTFWGXHYJYMXOWPTQKQ"),
    (81, " 25G]PFNGLIKKJNJSKVLXNZP[T[VZXXYVZSZNYKXIVGTFPF RSWY]"),
    (82, " 17G\\KFK[ RKFTFWGXHYJYLXNWOTPKP RRPY["),
    (83, " 21H\\YIWGTFPFMGKIKKLMMNOOUQWRXSYUYXWZT[P[MZKX"),
    (84, "  6JZRFR[ RKFYF"),
    (85, " 11G]KFKULXNZQ[S[VZXXYUYF"),
    (86, "  6I[JFR[ RZFR["),
    (87, " 12F^HFM[ RRFM[ RRFW[ R\\FW["),
    (88, "  6H\\KFY[ RYFK["),
    (89, "  7I[JFRPR[ RZFRP"),
    (90, "  9H\\YFK[ RKFYF RK[Y["),
    (91, " 12KYOBOb RPBPb ROBVB RObVb"),
    (92, "  3KYKFY^"),
    (93, " 12KYTBTb RUBUb RNBUB RNbUb"),
    (94, " 11JZPLRITL RMORJWO RRJR["),
    (95, "  3JZJ]Z]"),
    (96, "  8MWSFRGQIQKRLSKRJ"),
    (97, " 18I\\XMX[ RXPVNTMQMONMPLSLUMXOZQ[T[VZXX"),
    (98, " 18H[LFL[ RLPNNPMSMUNWPXSXUWXUZS[P[NZLX"),
    (99, " 15I[XPVNTMQMONMPLSLUMXOZQ[T[VZXX"),
    (100, " 18I\\XFX[ RXPVNTMQMONMPLSLUMXOZQ[T[VZXX"),
    (101, " 18I[LSXSXQWOVNTMQMONMPLSLUMXOZQ[T[VZXX"),
    (102, "  9MYWFUFSGRJR[ ROMVM"),
    (103, " 23I\\XMX]W`VaTbQbOa RXPVNTMQMONMPLSLUMXOZQ[T[VZXX"),
    (104, " 11I\\MFM[ RMQPNRMUMWNXQX["),
    (105, "  9NVQFRGSFREQF RRMR["),
    (106, " 12MWRFSGTFSERF RSMS^RaPbNb"),
    (107, "  9IZMFM[ RWMMW RQSX["),
    (108, "  3NVRFR["),
    (109, " 19CaGMG[ RGQJNLMOMQNRQR[ RRQUNWMZM\\N]Q]["),
    (110, " 11I\\MMM[ RMQPNRMUMWNXQX["),
    (111, " 18I\\QMONMPLSLUMXOZQ[T[VZXXYUYSXPVNTMQM"),
    (112, " 18H[LMLb RLPNNPMSMUNWPXSXUWXUZS[P[NZLX"),
    (113, " 18I\\XMXb RXPVNTMQMONMPLSLUMXOZQ[T[VZXX"),
    (114, "  9KXOMO[ ROSPPRNTMWM"),
    (115, " 18J[XPWNTMQMNNMPNRPSUTWUXWXXWZT[Q[NZMX"),
    (116, "  9MYRFRWSZU[W[ ROMVM"),
    (117, " 11I\\MMMWNZP[S[UZXW RXMX["),
    (118, "  6JZLMR[ RXMR["),
    (119, " 12G]JMN[ RRMN[ RRMV[ RZMV["),
    (120, "  6J[MMX[ RXMM["),
    (121, " 10JZLMR[ RXMR[P_NaLbKb"),
    (122, "  9J[XMM[ RMMXM RM[X["),
    (123, " 40KYTBRCQDPFPHQJRKSMSOQQ RRCQEQGRISJTLTNSPORSTTVTXSZR[Q]Q_Ra RQSSUSWRYQZP\\P^Q`RaTb"),
    (124, "  3NVRBRb"),
    (125, " 40KYPBRCSDTFTHSJRKQMQOSQ RRCSESGRIQJPLPNQPURQTPVPXQZR[S]S_Ra RSSQUQWRYSZT\\T^S`RaPb"),
    (126, " 24F^IUISJPLONOPPTSVTXTZS[Q RISJQLPNPPQTTVUXUZT[Q[O"),
    (913, "  9I[RFJ[ RRFZ[ RMTWT"),
    (914, " 24G\\KFK[ RKFTFWGXHYJYLXNWOTP RKPTPWQXRYTYWXYWZT[K["),
    (915, "  6HYLFL[ RLFXF"),
    (916, "  9I[RFJ[ RRFZ[ RJ[Z["),
    (917, " 12H[LFL[ RLFYF RLPTP RL[Y["),
    (918, "  9H\\YFK[ RKFYF RK[Y["),
    (919, "  9G]KFK[ RYFY[ RKPYP"),
    (920, " 25G]PFNGLIKKJNJSKVLXNZP[T[VZXXYVZSZNYKXIVGTFPF ROPUP"),
    (921, "  3NVRFR["),
    (922, "  9G\\KFK[ RYFKT RPOY["),
    (923, "  6I[RFJ[ RRFZ["),
    (924, " 12F^JFJ[ RJFR[ RZFR[ RZFZ["),
    (925, "  9G]KFK[ RKFY[ RYFY["),
    (926, "  9I[KFYF ROPUP RK[Y["),
    (927, " 22G]PFNGLIKKJNJSKVLXNZP[T[VZXXYVZSZNYKXIVGTFPF"),
    (928, "  9G]KFK[ RYFY[ RKFYF"),
    (929, " 14G\\KFK[ RKFTFWGXHYJYMXOWPTQKQ"),
    (931, " 10I[KFRPK[ RKFYF RK[Y["),
    (932, "  6JZRFR[ RKFYF"),
    (933, " 19I[KKKILGMFOFPGQIRMR[ RYKYIXGWFUFTGSIRM"),
    (934, " 21H\\RFR[ RPKMLLMKOKRLTMUPVTVWUXTYRYOXMWLTKPK"),
    (935, "  6H\\KFY[ RK[YF"),
    (936, " 18G]RFR[ RILJLKMLQMSNTQUSUVTWSXQYMZL[L"),
    (937, " 17H\\K[O[LTKPKLLINGQFSFVGXIYLYPXTU[Y["),
    (945, " 24H]QMONMPLRKUKXLZN[P[RZUWWTYPZM RQMSMTNUPWXXZY[Z["),
    (946, " 31I\\UFSGQIOMNPMTLZKb RUFWFYHYKXMWNUORO RROTPVRWTWWVYUZS[Q[OZNYMV"),
    (947, " 17I\\JPLNNMOMQNROSRSVR[ RZMYPXRR[P_Ob"),
    (948, " 24I[TMQMONMPLSLVMYNZP[R[TZVXWUWRVOTMRKQIQGRFTFVGXI"),
    (949, " 19JZWOVNTMQMONOPPRSS RSSOTMVMXNZP[S[UZWX"),
    (950, " 23JYTFRGQHQIRJUKXK RXKTMQONRMUMWNYP[S]T_TaSbQbP`"),
    (951, " 19H\\IQJOLMNMONOPNTL[ RNTPPRNTMVMXOXRWWTb"),
    (952, " 27G\\HQIOKMMMNNNPMUMXNZO[Q[SZUWVUWRXMXJWGUFSFRHRJSMUPWRZT"),
    (953, "  9LWRMPTOXOZP[R[TYUW"),
    (954, " 19I[OMK[ RYNXMWMUNQROSNS RNSPTQUSZT[U[VZ"),
    (955, "  9JZKFMFOGPHX[ RRML["),
    (956, " 21H]OMIb RNQMVMYO[Q[SZUXWT RYMWTVXVZW[Y[[Y\\W"),
    (957, " 14I[LMOMNSMXL[ RYMXPWRUURXOZL["),
    (958, " 29JZTFRGQHQIRJUKXK RUKRLPMOOOQQSTTVT RTTPUNVMXMZO\\S^T_TaRbPb"),
    (959, " 18J[RMPNNPMSMVNYOZQ[S[UZWXXUXRWOVNTMRM"),
    (960, " 13G]PML[ RUMVSWXX[ RIPKNNM[M"),
    (961, " 19I[MSMVNYOZQ[S[UZWXXUXRWOVNTMRMPNNPMSIb"),
    (963, " 18I][MQMONMPLSLVMYNZP[R[TZVXWUWRVOUNSM"),
    (964, "  8H\\SMP[ RJPLNOMZM"),
    (965, " 16H\\IQJOLMNMONOPMVMYO[Q[TZVXXTYPYM"),
    (966, " 21G]ONMOKQJTJWKYLZN[Q[TZWXYUZRZOXMVMTORSPXMb"),
    (967, " 14I[KMMMOOU`WbYb RZMYOWRM]K`Jb"),
    (968, " 20F]VFNb RGQHOJMLMMNMPLULXMZO[Q[TZVXXUZP[M"),
    (969, " 23F]NMLNJQITIWJZK[M[OZQW RRSQWRZS[U[WZYWZTZQYNXM"),
]

# hand-drawn math glyphs (unicode → stroke glyph)
const _MATH_GLYPHS = Dict{Char,Tuple{Float64,Float64,Vector{Vector{Tuple{Float64,Float64}}}}}()
_MATH_GLYPHS[Char(0x00AB)] = (-5.0f0, 5.0f0, Vector{Tuple{Float64,Float64}}[Tuple{Float64,Float64}[(4.0, 17.0), (-1.0, 10.5), (4.0, 4.0)], Tuple{Float64,Float64}[(1.0, 17.0), (-4.0, 10.5), (1.0, 4.0)]])
_MATH_GLYPHS[Char(0x00B0)] = (-1.0f0, 6.0f0, Vector{Tuple{Float64,Float64}}[Tuple{Float64,Float64}[(2.5, 18.5), (0.8, 17.5), (0.5, 15.8), (2.5, 14.8), (4.2, 15.8), (4.3, 17.5), (2.5, 18.5)]])
_MATH_GLYPHS[Char(0x00B1)] = (-6.0f0, 6.0f0, Vector{Tuple{Float64,Float64}}[Tuple{Float64,Float64}[(0.0, 6.0), (0.0, 18.0)], Tuple{Float64,Float64}[(-5.0, 12.0), (5.0, 12.0)], Tuple{Float64,Float64}[(-5.0, 1.0), (5.0, 1.0)]])
_MATH_GLYPHS[Char(0x00B7)] = (-1.0f0, 1.0f0, Vector{Tuple{Float64,Float64}}[Tuple{Float64,Float64}[(-0.7, 10.0), (0.7, 10.0), (0.7, 11.4), (-0.7, 11.4), (-0.7, 10.0)]])
_MATH_GLYPHS[Char(0x00BB)] = (-5.0f0, 5.0f0, Vector{Tuple{Float64,Float64}}[Tuple{Float64,Float64}[(-4.0, 17.0), (1.0, 10.5), (-4.0, 4.0)], Tuple{Float64,Float64}[(-1.0, 17.0), (4.0, 10.5), (-1.0, 4.0)]])
_MATH_GLYPHS[Char(0x00D7)] = (-6.0f0, 6.0f0, Vector{Tuple{Float64,Float64}}[Tuple{Float64,Float64}[(-5.0, 15.0), (5.0, 5.0)], Tuple{Float64,Float64}[(-5.0, 5.0), (5.0, 15.0)]])
_MATH_GLYPHS[Char(0x2026)] = (-7.0f0, 7.0f0, Vector{Tuple{Float64,Float64}}[Tuple{Float64,Float64}[(-6.0, 10.0), (-4.8, 10.0), (-4.8, 11.2), (-6.0, 11.2), (-6.0, 10.0)], Tuple{Float64,Float64}[(-0.6, 10.0), (0.6, 10.0), (0.6, 11.2), (-0.6, 11.2), (-0.6, 10.0)], Tuple{Float64,Float64}[(4.8, 10.0), (6.0, 10.0), (6.0, 11.2), (4.8, 11.2), (4.8, 10.0)]])
_MATH_GLYPHS[Char(0x2191)] = (-4.0f0, 4.0f0, Vector{Tuple{Float64,Float64}}[Tuple{Float64,Float64}[(0.0, 1.0), (0.0, 18.0)], Tuple{Float64,Float64}[(-3.5, 14.5), (0.0, 19.0), (3.5, 14.5)]])
_MATH_GLYPHS[Char(0x2192)] = (-8.0f0, 8.0f0, Vector{Tuple{Float64,Float64}}[Tuple{Float64,Float64}[(-8.0, 10.5), (6.5, 10.5)], Tuple{Float64,Float64}[(3.2, 13.4), (7.0, 10.5), (3.2, 7.6)]])
_MATH_GLYPHS[Char(0x2193)] = (-4.0f0, 4.0f0, Vector{Tuple{Float64,Float64}}[Tuple{Float64,Float64}[(0.0, 19.0), (0.0, 2.0)], Tuple{Float64,Float64}[(-3.5, 6.5), (0.0, 1.0), (3.5, 6.5)]])
_MATH_GLYPHS[Char(0x2212)] = (-7.0f0, 7.0f0, Vector{Tuple{Float64,Float64}}[Tuple{Float64,Float64}[(-6.0, 10.5), (6.0, 10.5)]])
_MATH_GLYPHS[Char(0x221A)] = (-6.0f0, 10.0f0, Vector{Tuple{Float64,Float64}}[Tuple{Float64,Float64}[(-6.0, 8.0), (-3.0, 8.0), (0.0, 1.0), (4.0, 19.0), (10.0, 19.0)]])
_MATH_GLYPHS[Char(0x221E)] = (-9.0f0, 9.0f0, Vector{Tuple{Float64,Float64}}[Tuple{Float64,Float64}[(-8.0, 10.5), (-5.0, 14.0), (-2.0, 10.5), (-5.0, 7.0), (-8.0, 10.5)], Tuple{Float64,Float64}[(2.0, 10.5), (5.0, 14.0), (8.0, 10.5), (5.0, 7.0), (2.0, 10.5)]])
_MATH_GLYPHS[Char(0x2248)] = (-7.0f0, 7.0f0, Vector{Tuple{Float64,Float64}}[Tuple{Float64,Float64}[(-7.0, 14.0), (-3.0, 12.0), (1.0, 14.0), (6.0, 12.0)], Tuple{Float64,Float64}[(-7.0, 8.0), (-3.0, 6.0), (1.0, 8.0), (6.0, 6.0)]])
_MATH_GLYPHS[Char(0x2264)] = (-6.0f0, 7.0f0, Vector{Tuple{Float64,Float64}}[Tuple{Float64,Float64}[(4.0, 17.0), (-5.0, 10.0), (4.0, 3.0)], Tuple{Float64,Float64}[(-5.0, 0.0), (5.0, 0.0)]])
_MATH_GLYPHS[Char(0x2265)] = (-6.0f0, 7.0f0, Vector{Tuple{Float64,Float64}}[Tuple{Float64,Float64}[(-4.0, 17.0), (5.0, 10.0), (-4.0, 3.0)], Tuple{Float64,Float64}[(-5.0, 0.0), (5.0, 0.0)]])
_MATH_GLYPHS[Char(0x22A5)] = (-5.0f0, 5.0f0, Vector{Tuple{Float64,Float64}}[Tuple{Float64,Float64}[(0.0, 2.0), (0.0, 19.0)], Tuple{Float64,Float64}[(-5.0, 2.0), (5.0, 2.0)]])
_MATH_GLYPHS[Char(0x27E8)] = (-5.0f0, 5.0f0, Vector{Tuple{Float64,Float64}}[Tuple{Float64,Float64}[(4.0, 19.0), (-5.0, 10.5), (4.0, 2.0)]])
_MATH_GLYPHS[Char(0x27E9)] = (-5.0f0, 5.0f0, Vector{Tuple{Float64,Float64}}[Tuple{Float64,Float64}[(-4.0, 19.0), (5.0, 10.5), (-4.0, 2.0)]])

# == Viridis colormap (matplotlib/BIDS, CC0) 256 RGB hex ==
const _VIRIDIS_HEX = "44015444025645045745055946075A46085C460A5D460B5E470D60470E6147106347116447136548146748166848176948186A481A6C481B6D481C6E481D6F481F70482071482173482374482475482576482677482878482979472A7A472C7A472D7B472E7C472F7D46307E46327E46337F463480453581453781453882443983443A83443B84433D84433E85423F854240864241864142874144874045884046883F47883F48893E49893E4A893E4C8A3D4D8A3D4E8A3C4F8A3C508B3B518B3B528B3A538B3A548C39558C39568C38588C38598C375A8C375B8D365C8D365D8D355E8D355F8D34608D34618D33628D33638D32648E32658E31668E31678E31688E30698E306A8E2F6B8E2F6C8E2E6D8E2E6E8E2E6F8E2D708E2D718E2C718E2C728E2C738E2B748E2B758E2A768E2A778E2A788E29798E297A8E297B8E287C8E287D8E277E8E277F8E27808E26818E26828E26828E25838E25848E25858E24868E24878E23888E23898E238A8D228B8D228C8D228D8D218E8D218F8D21908D21918C20928C20928C20938C1F948C1F958B1F968B1F978B1F988B1F998A1F9A8A1E9B8A1E9C891E9D891F9E891F9F881FA0881FA1881FA1871FA28720A38620A48621A58521A68522A78522A88423A98324AA8325AB8225AC8226AD8127AD8128AE8029AF7F2AB07F2CB17E2DB27D2EB37C2FB47C31B57B32B67A34B67935B77937B87838B9773ABA763BBB753DBC743FBC7340BD7242BE7144BF7046C06F48C16E4AC16D4CC26C4EC36B50C46A52C56954C56856C66758C7655AC8645CC8635EC96260CA6063CB5F65CB5E67CC5C69CD5B6CCD5A6ECE5870CF5773D05675D05477D1537AD1517CD2507FD34E81D34D84D44B86D54989D5488BD6468ED64590D74393D74195D84098D83E9BD93C9DD93BA0DA39A2DA37A5DB36A8DB34AADC32ADDC30B0DD2FB2DD2DB5DE2BB8DE29BADE28BDDF26C0DF25C2DF23C5E021C8E020CAE11FCDE11DD0E11CD2E21BD5E21AD8E219DAE319DDE318DFE318E2E418E5E419E7E419EAE51AECE51BEFE51CF1E51DF4E61EF6E620F8E621FBE723FDE725"


# ============================================================================
# inlined component: 02_plot_engine.jl
# ============================================================================

# ==============================================================================
# PART 2 — PNG WRITER (pure stdlib; zlib stream with stored deflate blocks)
# ==============================================================================

using Printf

const _CRC32_TABLE = let t = Vector{UInt32}(undef, 256)
    for n in 0:255
        c = UInt32(n)
        for _ in 1:8
            c = (c & 0x1) == 0x1 ? (0xEDB88320 ⊻ (c >> 1)) : (c >> 1)
        end
        t[n+1] = c
    end
    t
end

function _crc32(data::Vector{UInt8})::UInt32
    c = 0xFFFFFFFF
    for b in data
        c = _CRC32_TABLE[((c ⊻ UInt32(b)) & 0xFF)+1] ⊻ (c >> 8)
    end
    c ⊻ 0xFFFFFFFF
end

function _adler32(data::Vector{UInt8})::UInt32
    a = UInt32(1); b = UInt32(0)
    for b8 in data
        a = (a + UInt32(b8)) % UInt32(65521)
        b = (b + a) % UInt32(65521)
    end
    (b << 16) | a
end

function _png_chunk(io, tag::Vector{UInt8}, data::Vector{UInt8})
    write(io, hton(UInt32(length(data))))
    write(io, tag)
    write(io, data)
    crcdata = vcat(tag, data)
    write(io, hton(_crc32(crcdata)))
end

# --- DEFLATE (RFC1951): LZ77 hash-chain + fixed Huffman ---
mutable struct _BitW
    buf::Vector{UInt8}
    cur::UInt32
    n::Int
end
_BitW() = _BitW(Vector{UInt8}(undef, 0), 0x00, 0)

@inline function _wb(bw::_BitW, v::Unsigned, n::Int)  # LSB-first
    bw.cur |= (v & ((UInt32(1) << n) - 1)) << bw.n
    bw.n += n
    while bw.n >= 8
        push!(bw.buf, UInt8(bw.cur & 0xFF))
        bw.cur >>= 8
        bw.n -= 8
    end
end
@inline function _whuf(bw::_BitW, code::Unsigned, n::Int)  # MSB-first (huffman)
    r = UInt32(0)
    for i in 0:n-1
        r = r | UInt32(((code >> (n - 1 - i)) & UInt32(1)) << i)
    end
    _wb(bw, r, n)
end
@inline _flushbits!(bw::_BitW) = (bw.n > 0 && push!(bw.buf, UInt8(bw.cur & 0xFF)); nothing)

const _LEN_BASE = UInt16[3,4,5,6,7,8,9,10,11,13,15,17,19,23,27,31,35,43,51,59,67,83,99,115,131,163,195,227,258]
const _LEN_EXTRA = UInt8[0,0,0,0,0,0,0,0,1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,0]
const _DIST_BASE = UInt16[1,2,3,4,5,7,9,13,17,25,33,49,65,97,129,193,257,385,513,769,1025,1537,2049,3073,4097,6145,8193,12289,16385,24577]
const _DIST_EXTRA = UInt8[0,0,0,0,1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10,11,11,12,12,13,13]

@inline function _lit_code(bw::_BitW, lit::UInt16)
    if lit < 144
        _whuf(bw, 0x30 + UInt32(lit), 8)
    elseif lit < 256
        _whuf(bw, 0x190 + UInt32(lit - 144), 9)
    elseif lit < 280
        _whuf(bw, UInt32(lit - 256), 7)
    else
        _whuf(bw, 0xC0 + UInt32(lit - 280), 8)
    end
end

function _deflate_fixed(raw::Vector{UInt8})
    bw = _BitW()
    _wb(bw, UInt32(1), 1)     # BFINAL
    _wb(bw, UInt32(1), 2)     # fixed huffman
    n = length(raw)
    HEAD = 30323  # hash of 3 bytes
    head = fill(0, HEAD)      # most recent pos with hash
    prev = fill(0, n)         # chain
    MAXCHAIN = 48
    i = 1
    hash3(p) = p + 2 <= n ? (UInt32(raw[p]) * 31 + UInt32(raw[p+1]) * 131 + UInt32(raw[p+2])) % HEAD + 1 : 0
    while i <= n
        bestlen = 0; bestdist = 0
        if i + 2 <= n
            h = hash3(i)
            cand = head[h]
            chain = 0
            lim = min(258, n - i + 1)
            while cand != 0 && chain < MAXCHAIN && i - cand <= 32768
                # measure match
                L = 0
                while L < lim && raw[cand + L] == raw[i + L]
                    L += 1
                end
                if L > bestlen
                    bestlen = L; bestdist = i - cand
                    L >= lim && break
                end
                cand = prev[cand]; chain += 1
            end
            prev[i] = head[h]; head[h] = i
        end
        if bestlen >= 3
            # find length code: first-fit over 29 codes (sym = 256 + k)
            lc = 29
            for k in 1:29
                if bestlen < _LEN_BASE[k] + (UInt16(1) << _LEN_EXTRA[k])
                    lc = k; break
                end
            end
            _lit_code(bw, UInt16(256 + lc))
            eb = _LEN_EXTRA[lc]
            eb > 0 && _wb(bw, UInt32(bestlen - _LEN_BASE[lc]), Int(eb))
            # distance code
            dc = 29
            for k in 1:30
                if bestdist < _DIST_BASE[k] + (UInt16(1) << _DIST_EXTRA[k]) || k == 30
                    dc = k; break
                end
            end
            _whuf(bw, UInt32(dc - 1), 5)
            deb = _DIST_EXTRA[dc]
            deb > 0 && _wb(bw, UInt32(bestdist - _DIST_BASE[dc]), Int(deb))
            # register skipped positions in hash chains
            for p in i+1:min(i + bestlen - 1, n - 2)
                h = hash3(p)
                prev[p] = head[h]; head[h] = p
            end
            i += bestlen
        else
            _lit_code(bw, UInt16(raw[i]))
            i += 1
        end
    end
    _lit_code(bw, UInt16(256))  # end of block
    _flushbits!(bw)
    return bw.buf
end

"""
    save_png(path, w, h, rgb::Vector{UInt8})

Write an 8-bit RGB PNG (row-major, 3 bytes/pixel). Fully self-contained.
"""
function save_png(path::AbstractString, w::Int, h::Int, rgb::Vector{UInt8})
    @assert length(rgb) == w * h * 3
    raw = Vector{UInt8}(undef, (w * 3 + 1) * h)
    for y in 1:h
        base_in = (y - 1) * w * 3
        base_out = (y - 1) * (w * 3 + 1)
        raw[base_out+1] = 0x00 # filter none
        copyto!(raw, base_out + 2, rgb, base_in + 1, w * 3)
    end
    zbuf = try
        _deflate_fixed(raw)
    catch
        # fallback: stored blocks
        sb = UInt8[0x78, 0x01]
        pos = 1; n = length(raw)
        while pos <= n
            blk = min(65535, n - pos + 1)
            final = pos + blk - 1 >= n ? 0x01 : 0x00
            push!(sb, final)
            push!(sb, UInt8(blk & 0xFF), UInt8((blk >> 8) & 0xFF))
            push!(sb, UInt8((~blk) & 0xFF), UInt8(((~blk) >> 8) & 0xFF))
            append!(sb, raw[pos:pos+blk-1])
            pos += blk
        end
        sb
    end
    ad = _adler32(raw)
    zbuf = vcat(UInt8[0x78, 0x01], zbuf)
    append!(zbuf, UInt8[((ad >> 24) & 0xFF) % UInt8, ((ad >> 16) & 0xFF) % UInt8,
                        ((ad >> 8) & 0xFF) % UInt8, (ad & 0xFF) % UInt8])
    io = open(path, "w")
    try
        write(io, UInt8[0x89, 0x50, 0x4E, 0x47, 0x0D, 0x0A, 0x1A, 0x0A])
        ihdr = Vector{UInt8}(undef, 13)
        reinterpret(UInt8, [hton(UInt32(w))])      |> d -> copyto!(ihdr, 1, d, 1, 4)
        reinterpret(UInt8, [hton(UInt32(h))])      |> d -> copyto!(ihdr, 5, d, 1, 4)
        ihdr[9] = 0x08; ihdr[10] = 0x02; ihdr[11] = 0x00
        ihdr[12] = 0x00; ihdr[13] = 0x00
        _png_chunk(io, UInt8['I','H','D','R'], ihdr)
        _png_chunk(io, UInt8['I','D','A','T'], zbuf)
        _png_chunk(io, UInt8['I','E','N','D'], UInt8[])
    finally
        close(io)
    end
    return path
end

# ==============================================================================
# PART 3 — COLOR, CANVAS, RASTER PRIMITIVES (supersampled, alpha, dashes)
# ==============================================================================

struct RGBA32
    r::Float32; g::Float32; b::Float32; a::Float32
end
hexcol(s::AbstractString) = RGBA32(
    parse(Int, s[2:3], base = 16) / 255,
    parse(Int, s[4:5], base = 16) / 255,
    parse(Int, s[6:7], base = 16) / 255, 1.0f0)
withalpha(c::RGBA32, a::Real) = RGBA32(c.r, c.g, c.b, Float32(a))
mutable struct Canvas
    w::Int; h::Int          # device pixels
    ss::Int                 # supersample factor (1,2,3)
    W::Int; H::Int          # raster pixels = w*ss, h*ss
    buf::Vector{Float32}    # RGB raster
end
Canvas(w::Int, h::Int; ss::Int = 2) =
    Canvas(w, h, ss, w * ss, h * ss, zeros(Float32, w * ss * h * ss * 3))

@inline function _blend!(cv::Canvas, X::Int, Y::Int, c::RGBA32)
    (X < 1 || X > cv.W || Y < 1 || Y > cv.H) && return nothing
    a = c.a
    a <= 0 && return nothing
    o = (Y - 1) * cv.W * 3 + (X - 1) * 3
    b = cv.buf
    if a >= 1
        @inbounds b[o+1] = c.r; b[o+2] = c.g; b[o+3] = c.b
    else
        @inbounds begin
            b[o+1] = c.r * a + b[o+1] * (1 - a)
            b[o+2] = c.g * a + b[o+2] * (1 - a)
            b[o+3] = c.b * a + b[o+3] * (1 - a)
        end
    end
    nothing
end

# NaN/Inf-safe device mapping: non-finite input → far off-canvas sentinel
# (bounded magnitude so Bresenham walks stay cheap; bounds check in _blend! clips)
@inline function _sx(cv::Canvas, x::Real)
    v = Float64(x) * cv.ss
    isfinite(v) || return -100_000
    return round(Int, v) + 1
end
@inline function _sy(cv::Canvas, y::Real)
    v = Float64(y) * cv.ss
    isfinite(v) || return -100_000
    return round(Int, v) + 1
end

function fill_rect!(cv::Canvas, x0::Real, y0::Real, x1::Real, y1::Real, c::RGBA32)
    X0, X1 = _sx(cv, min(x0, x1)), _sx(cv, max(x0, x1)) - 1
    Y0, Y1 = _sy(cv, min(y0, y1)), _sy(cv, max(y0, y1)) - 1
    X0 = max(X0, 1); Y0 = max(Y0, 1); X1 = min(X1, cv.W); Y1 = min(Y1, cv.H)
    for Y in Y0:Y1, X in X0:X1
        _blend!(cv, X, Y, c)
    end
end

"""Thick line via Bresenham walk with square pen (device coords, width device px)."""
function draw_line!(cv::Canvas, x0::Real, y0::Real, x1::Real, y1::Real,
                    c::RGBA32, width::Real = 1.5, dash::AbstractString = "")
    X0, Y0 = _sx(cv, x0), _sy(cv, y0)
    X1, Y1 = _sx(cv, x1), _sy(cv, y1)
    rw = max(1, round(Int, Float64(width) * cv.ss))
    r = rw ÷ 2
    dx, dy = abs(X1 - X0), abs(Y1 - Y0)
    n = max(dx, dy)
    n == 0 && (n = 1)
    len_px = sqrt(Float64(dx * dx + dy * dy))
    if dash == "" || len_px == 0
        _stamp_line(cv, X0, Y0, X1, Y1, r, c)
    else
        # dash pattern "a,b" in device px
        parts = split(dash, ',')
        on = max(1, round(Int, parse(Float64, parts[1]) * cv.ss))
        off = max(1, round(Int, parse(Float64, parts[2]) * cv.ss))
        pen = 0; state = true
        stepx = (X1 - X0) / n; stepy = (Y1 - Y0) / n
        X = Float64(X0); Y = Float64(Y0)
        traveled = 0.0; period = on + off
        for i in 0:n
            ph = mod(traveled, period)
            visible = ph < on
            if visible
                _stamp_line(cv, round(Int, X), round(Int, Y), round(Int, X), round(Int, Y), r, c)
            end
            traveled += sqrt(stepx^2 + stepy^2)
            X += stepx; Y += stepy
        end
    end
end

function _stamp_line(cv::Canvas, X0, Y0, X1, Y1, r, c)
    dx, dy = abs(X1 - X0), abs(Y1 - Y0)
    sx = X0 < X1 ? 1 : -1; sy = Y0 < Y1 ? 1 : -1
    err = dx - dy
    X, Y = X0, Y0
    while true
        if r == 0
            _blend!(cv, X, Y, c)
        else
            for oy in -r:r, ox in -r:r
                _blend!(cv, X + ox, Y + oy, c)
            end
        end
        (X == X1 && Y == Y1) && break
        e2 = 2err
        if e2 > -dy; err -= dy; X += sx; end
        if e2 < dx;  err += dx; Y += sy; end
    end
end

function fill_circle!(cv::Canvas, cx::Real, cy::Real, rad::Real, c::RGBA32)
    R = rad * cv.ss
    X0, X1 = _sx(cv, cx - rad), _sx(cv, cx + rad)
    Y0, Y1 = _sy(cv, cy - rad), _sy(cv, cy + rad)
    cxd, cyd = (X0 + X1) / 2, (Y0 + Y1) / 2
    for Y in max(1, round(Int, Y0)):min(cv.H, round(Int, Y1))
        dy2 = (Y - cyd)^2
        span = sqrt(max(0.0, R^2 - dy2))
        Xa = round(Int, cxd - span); Xb = round(Int, cxd + span)
        for X in max(1, Xa):min(cv.W, Xb)
            _blend!(cv, X, Y, c)
        end
    end
end

"""Even-odd scanline polygon fill. pts = Vector{Tuple{Float64,Float64}} device coords.
Non-finite vertices are dropped defensively (never crash on NaN data)."""
function fill_polygon!(cv::Canvas, pts::Vector{Tuple{Float64,Float64}}, c::RGBA32)
    all(isfinite(p[1]) && isfinite(p[2]) for p in pts) ||
        (pts = [p for p in pts if isfinite(p[1]) && isfinite(p[2])])
    n = length(pts); n < 3 && return nothing
    ys = [p[2] for p in pts]
    Ylo = _sy(cv, minimum(ys)); Yhi = _sy(cv, maximum(ys))
    Ylo = max(Ylo, 1); Yhi = min(Yhi, cv.H)
    xs = Vector{Float64}(undef, n)
    for Y in Ylo:Yhi
        yc = (Y - 0.5) / cv.ss
        k = 0
        for i in 1:n
            j = i == 1 ? n : i - 1
            yi, yj = pts[i][2], pts[j][2]
            if (yi <= yc && yj > yc) || (yj <= yc && yi > yc)
                k += 1
                xs[k] = pts[i][1] + (yc - yi) / (yj - yi) * (pts[j][1] - pts[i][1])
            end
        end
        k >= 2 || continue
        sort!(view(xs, 1:k))
        for m in 1:2:k-1
            Xa, Xb = _sx(cv, xs[m]), _sx(cv, xs[m+1]) - 1
            for X in max(1, Xa):min(cv.W, Xb)
                _blend!(cv, X, Y, c)
            end
        end
    end
end

# ==============================================================================
# PART 3b — HERSHEY VECTOR TEXT
# ==============================================================================

const _FONT_GLYPHS = let d = Dict{Char,Tuple{Float64,Float64,Vector{Vector{Tuple{Float64,Float64}}}}}()
    for (code, rec) in _HERSHEY_RAW
        ch = Char(code)
        left = Float64(Int(rec[4]) - 82)
        right = Float64(Int(rec[5]) - 82)
        s = rec[6:end]
        polys = Vector{Tuple{Float64,Float64}}[]
        cur = Tuple{Float64,Float64}[]
        i = 1
        while i <= length(s)
            if s[i] == ' '
                i += 2
                if !isempty(cur); push!(polys, cur); cur = Tuple{Float64,Float64}[]; end
                continue
            end
            c2 = i + 1 <= length(s) ? s[i+1] : 'R'
            push!(cur, (Float64(Int(s[i]) - 82), 9.0 - Float64(Int(c2) - 82))) # y-up, baseline at 0
            i += 2
        end
        !isempty(cur) && push!(polys, cur)
        d[ch] = (left, right, polys)
    end
    merge!(d, _MATH_GLYPHS)
    d
end

# unicode sub/superscript normalization → ^{..} / _{..} markup
const _SUBSUP_MAP = Dict('²' => "^{2}", '³' => "^{3}", '⁴' => "^{4}", '⁵' => "^{5}",
    '⁶' => "^{6}", '⁷' => "^{7}", '⁸' => "^{8}", '⁹' => "^{9}", '⁰' => "^{0}",
    '¹' => "^{1}", '⁻' => "^{-}", '⁺' => "^{+}", 'ⁿ' => "^{n}",
    '₀' => "_{0}", '₁' => "_{1}", '₂' => "_{2}", '₃' => "_{3}", '₄' => "_{4}",
    '₅' => "_{5}", '₆' => "_{6}", '₇' => "_{7}", '₈' => "_{8}", '₉' => "_{9}",
    'ₙ' => "_{n}", 'ᵢ' => "_{i}", 'ⱼ' => "_{j}", 'ₖ' => "_{k}", 'ₘ' => "_{m}",
    '₊' => "_{+}", '₋' => "_{-}")

function _norm_text(s::AbstractString)
    haskey(_SUBSUP_MAP, '²') || return String(s)
    out = IOBuffer()
    for ch in s
        if haskey(_SUBSUP_MAP, ch)
            write(out, _SUBSUP_MAP[ch])
        else
            write(out, ch)
        end
    end
    String(take!(out))
end

# text layout: Vector of (Char, scale, dy) with ^{..}/_{..} markup resolved
function _layout_text(s::AbstractString)
    sn = collect(Char, _norm_text(s))
    out = Tuple{Char,Float64,Float64}[]
    i = 1
    n = length(sn)
    while i <= n
        c = sn[i]
        if (c == '^' || c == '_') && i + 1 <= n && sn[i+1] == '{'
            j = i + 2
            depth = 1
            while j <= n && depth > 0
                sn[j] == '{' && (depth += 1)
                sn[j] == '}' && (depth -= 1)
                depth == 0 && break
                push!(out, (sn[j], 0.62, c == '^' ? 8.5 : -5.0))
                j += 1
            end
            i = j + 1
        else
            push!(out, (c, 1.0, 0.0))
            i += 1
        end
    end
    return out
end
const _FONT_CAP = 21.0   # hershey cap-height units (baseline 0, cap top 21)

"Text width in device px (does not include trailing advance)."
function text_width(s::AbstractString, size_px::Real)
    sz = Float64(size_px); sc = sz / _FONT_CAP
    w = 0.0
    for (ch, scl, _) in _layout_text(s)
        w += (ch == ' ' ? 9.0 : _glyph_adv(ch)) * sc * scl
    end
    w
end
_glyph_adv(ch::Char) = begin
    g = get(_FONT_GLYPHS, ch, nothing)
    g === nothing ? 9.0 : (g[2] - g[1] + 2)
end

"""Render stroke text. (x,y) = baseline anchor. align: :left, :center, :right. angle deg CCW."""
function draw_text!(cv::Canvas, x::Real, y::Real, s::AbstractString, size_px::Real,
                    col::RGBA32; align::Symbol = :left, angle::Real = 0.0,
                    lw::Real = 1.4, spacing::Real = 1.0)
    sz = Float64(size_px); sc = sz / _FONT_CAP * cv.ss
    total = text_width(s, size_px) * cv.ss
    th = Float64(angle) * π / 180
    ca, sa = cos(th), sin(th)
    # anchor adjust (in unrotated text frame)
    px = Float64(x) * cv.ss; py = Float64(y) * cv.ss
    if align == :center; px -= total / 2 * ca; py -= total / 2 * sa; end
    if align == :right;  px -= total * ca;     py -= total * sa;     end
    penx, peny = 0.0, 0.0
    lwss = max(1.0, lw * cv.ss)
    for (ch, scl, dyu) in _layout_text(s)
        ch == ' ' && (penx += 9 * sc * spacing * scl; continue)
        g = get(_FONT_GLYPHS, ch, nothing)
        g === nothing && (penx += 9 * sc * spacing * scl; continue)
        gl, gr, polys = g
        for poly in polys
            for k in 1:length(poly)-1
                x0 = penx + poly[k][1] * sc * scl
                y0 = peny + (poly[k][2] + dyu) * sc * scl
                x1 = penx + poly[k+1][1] * sc * scl
                y1 = peny + (poly[k+1][2] + dyu) * sc * scl
                rx0 = px + x0 * ca - y0 * sa; ry0 = py - (x0 * sa + y0 * ca)
                rx1 = px + x1 * ca - y1 * sa; ry1 = py - (x1 * sa + y1 * ca)
                _stamp_line(cv, round(Int, rx0), round(Int, ry0),
                            round(Int, rx1), round(Int, ry1), 0, col)
            end
        end
        penx += (gr - gl + 2) * sc * spacing * scl
    end
    nothing
end

# ==============================================================================
# PART 4 — THEMES, COLORMAPS, FIGURE / PANEL SYSTEM
# ==============================================================================

struct Theme
    name::String
    bg::RGBA32; panel::RGBA32; frame::RGBA32
    grid::RGBA32; gridminor::RGBA32
    text::RGBA32; dim::RGBA32
    title::RGBA32
    series::Vector{RGBA32}
    good::RGBA32; bad::RGBA32; warn::RGBA32
    legendbg::RGBA32
end

function make_theme(name::String)
    if name == "light"
        Theme(name,
            hexcol("#FFFFFF"), hexcol("#FFFFFF"), hexcol("#22252A"),
            hexcol("#C9CDD4"), hexcol("#E4E7EC"),
            hexcol("#1A1D23"), hexcol("#6B7280"), hexcol("#0B3D6B"),
            RGBA32[hexcol("#1F77B4"), hexcol("#D62728"), hexcol("#2CA02C"),
                   hexcol("#FF7F0E"), hexcol("#9467BD"), hexcol("#8C564B"),
                   hexcol("#17BECF"), hexcol("#7F7F7F")],
            hexcol("#2CA02C"), hexcol("#D62728"), hexcol("#E6A100"),
            RGBA32(1.0f0, 1.0f0, 1.0f0, 0.88f0))
    else # "dark" — deep navy-black, journal-grade on screen
        Theme(name,
            hexcol("#0A0E1A"), hexcol("#0D1322"), hexcol("#5F6F94"),
            hexcol("#1D2A47"), hexcol("#141D33"),
            hexcol("#D8E1F3"), hexcol("#8B98B8"), hexcol("#EAF0FB"),
            RGBA32[hexcol("#4FC3F7"), hexcol("#FF9E4A"), hexcol("#62D99A"),
                   hexcol("#FF5D5D"), hexcol("#5B8DFF"), hexcol("#E06BFF"),
                   hexcol("#FFD166"), hexcol("#7FE3D2")],
            hexcol("#62D99A"), hexcol("#FF5D5D"), hexcol("#FFD166"),
            RGBA32(0.05f0, 0.08f0, 0.16f0, 0.90f0))
    end
end

# --- colormaps ---
const _VIRIDIS_LUT = let lut = Vector{RGBA32}(undef, 256)
    h = _VIRIDIS_HEX
    for i in 0:255
        lut[i+1] = RGBA32(
            parse(Int, h[6i+1:6i+2], base = 16) / 255,
            parse(Int, h[6i+3:6i+4], base = 16) / 255,
            parse(Int, h[6i+5:6i+6], base = 16) / 255, 1.0f0)
    end
    lut
end

"""Inferno-like fallback computed from viridis anchors (rotated); plus simple maps."""
function cmap(name::String, t::Real)
    t = clamp(t, 0.0, 1.0)
    if name == "viridis" || name == "default"
        _VIRIDIS_LUT[round(Int, t * 255)+1]
    elseif name == "thermal"  # black-red-yellow-white
        stops = [hexcol("#000004"), hexcol("#3B0F70"), hexcol("#8C2981"),
                 hexcol("#DE4968"), hexcol("#FE9F6D"), hexcol("#FCFDBF")]
        _ramp(stops, t)
    elseif name == "ice"     # black-blue-white
        stops = [hexcol("#02030B"), hexcol("#0B2A6B"), hexcol("#1C6FD4"),
                 hexcol("#63C5F5"), hexcol("#EAF7FF")]
        _ramp(stops, t)
    elseif name == "sign"    # diverging blue-white-red
        stops = [hexcol("#2166AC"), hexcol("#67A9CF"), hexcol("#F7F7F7"),
                 hexcol("#EF8A62"), hexcol("#B2182B")]
        _ramp(stops, t)
    elseif name == "bin"     # binary pattern: background → bright cyan
        _ramp([hexcol("#0D1322"), hexcol("#1C6FD4"), hexcol("#63E5FF")], t)
    else
        _VIRIDIS_LUT[round(Int, t * 255)+1]
    end
end
function _ramp(stops::Vector{RGBA32}, t::Real)
    n = length(stops) - 1
    f = t * n
    i = min(n - 1, floor(Int, f)) + 1
    u = f - (i - 1)
    a, b = stops[i], stops[i+1]
    RGBA32(a.r + (b.r - a.r) * u, a.g + (b.g - a.g) * u, a.b + (b.b - a.b) * u, 1.0f0)
end

_t(t, lo, hi) = lo + t * (hi - lo)
function _mapx(p, x::Real)
    v = Float64(x)
    if p.xlog
        v <= 0 && (v = eps())
        v = log10(v)
        return p.px0 + (v - p.xlo_t) / max(p.xhi_t - p.xlo_t, eps()) * (p.px1 - p.px0)
    end
    return p.px0 + (v - p.xlo) / max(p.xhi - p.xlo, eps()) * (p.px1 - p.px0)
end
function _mapy(p, y::Real)
    v = Float64(y)
    if p.ylog
        v <= 0 && (v = eps())
        v = log10(v)
        return p.py1 - (v - p.ylo_t) / max(p.yhi_t - p.ylo_t, eps()) * (p.py1 - p.py0)
    end
    return p.py1 - (v - p.ylo) / max(p.yhi - p.ylo, eps()) * (p.py1 - p.py0)
end

function nice_ticks(lo::Float64, hi::Float64, n::Int = 5)
    if !(hi > lo)
        hi = lo + 1.0
    end
    span = hi - lo
    raw = span / max(n, 1)
    mag = 10.0^floor(log10(raw))
    norm = raw / mag
    step = (norm < 1.5 ? 1.0 : norm < 3.5 ? 2.0 : norm < 7.5 ? 5.0 : 10.0) * mag
    t0 = ceil(lo / step) * step
    ticks = Float64[]
    t = t0
    while t <= hi + step * 1e-6
        push!(ticks, abs(t) < step * 1e-9 ? 0.0 : t)
        t += step
    end
    return ticks, step
end

_fmt_tick(v::Float64) = begin
    if v == 0; return "0"; end
    a = abs(v)
    if 1e-3 <= a < 1e6 && (a >= 1 || isinteger(v) || abs(v - round(v, digits = 6)) < 1e-12)
        s = a >= 1e4 ? @sprintf("%.0f", v) : a >= 100 ? @sprintf("%.0f", v) :
            a >= 10 ? @sprintf("%g", v) : @sprintf("%g", v)
        return s
    end
    e = floor(Int, log10(a))
    m = v / 10.0^e
    @sprintf("%ge%d", m, e)
end
_fmt_log(v::Float64) = begin
    e = floor(Int, round(v))
    m = 10.0^(v - e)
    if abs(m - 1) < 1e-9
        # decade ticks: plain decimal for the common range (no caret clutter)
        -4 <= e <= 4 ? (e >= 0 ? @sprintf("%g", 10.0^e) :
                                      (e == -1 ? "0.1" : e == -2 ? "0.01" :
                                       @sprintf("1e%d", e))) :
            @sprintf("10^%d", e)
    else
        @sprintf("%g×10^%d", m, e)
    end
end

# --- plot spec storage ---
mutable struct PlotEl
    kind::Symbol           # :line :scatter :hist :band :text :hline :vline :heat :ann
    args::Any
    kwargs::Any
end

mutable struct Panel
    # device-space panel rect (content box)
    px0::Float64; py0::Float64; px1::Float64; py1::Float64
    # world coords
    xlo::Float64; xhi::Float64; ylo::Float64; yhi::Float64
    xlo_t::Float64; xhi_t::Float64; ylo_t::Float64; yhi_t::Float64
    xlog::Bool; ylog::Bool
    xlim_fixed::Bool; ylim_fixed::Bool
    title::String; xlabel::String; ylabel::String
    tag::String
    els::Vector{PlotEl}
    legend::Bool
    legend_loc::Symbol
    infobox::Vector{String}
    infoloc::Symbol
    cb::Bool              # colorbar
    cblab::String
    aspect::Float64       # 0 = free
    xticks_c::Union{Nothing,Tuple{Vector{Float64},Vector{String}}}
    yticks_c::Union{Nothing,Tuple{Vector{Float64},Vector{String}}}
    # grid placement (for two-phase layout)
    gr::Int; gc::Int; grows::Int; gcols::Int; gtop::Float64
    ml_used::Float64      # adaptive left margin (set by _layout_panel!)
    lims_done::Bool       # _padlim! already applied (padding is not idempotent)
end
Panel() = Panel(0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, false, false, false, false,
                "", "", "", "", PlotEl[], false, :topright, String[], :topright,
                false, "", 0.0, nothing, nothing, 1, 1, 1, 1, 0.0, 52.0, false)

mutable struct Fig
    cv::Canvas
    theme::Theme
    title::String
    subtitle::String
    footer::String
    panels::Vector{Panel}
    cur::Int
    w::Int; h::Int
end

"""
    make_fig(w, h; title, subtitle, footer, theme="dark", ss=2)
"""
function make_fig(w::Int, h::Int; title::String = "", subtitle::String = "",
                  footer::String = "", theme::String = "dark", ss::Int = 2)
    Fig(Canvas(w, h; ss = ss), make_theme(theme), title, subtitle, footer,
        Panel[], 0, w, h)
end

"""
    add_panel!(fig, r, c, rows, cols; kwargs...) -> Panel

Add panel at grid position (r, c) of a rows×cols grid (1-based). kw: title,
xlabel, ylabel, xlog, ylog, tag, legend, legend_loc, xlim, ylim, colorbar, cblab, infobox.
"""
function add_panel!(f::Fig, r::Int, c::Int, rows::Int, cols::Int;
                    title::String = "", xlabel::String = "", ylabel::String = "",
                    xlog::Bool = false, ylog::Bool = false, tag::String = "",
                    legend::Bool = false, legend_loc::Symbol = :topright,
                    xlim::Union{Nothing,Tuple{Float64,Float64}} = nothing,
                    ylim::Union{Nothing,Tuple{Float64,Float64}} = nothing,
                    colorbar::Bool = false, cblab::String = "",
                    infobox::Vector{String} = String[], infoloc::Symbol = :topright,
                    top_pad::Float64 = 0.0,
                    xticks::Union{Nothing,Tuple{Vector{Float64},Vector{String}}} = nothing,
                    yticks::Union{Nothing,Tuple{Vector{Float64},Vector{String}}} = nothing)
    p = Panel()
    p.gr, p.gc, p.grows, p.gcols, p.gtop = r, c, rows, cols, top_pad
    # provisional rect (final layout happens in _relayout! at save_fig time)
    top_band0 = isempty(f.title) ? 10.0 : (isempty(f.subtitle) ? 44.0 : 62.0)
    bot_band0 = isempty(f.footer) ? 8.0 : 26.0
    pw0 = (f.w - 20.0) / cols; ph0 = (f.h - bot_band0 - top_band0) / rows
    p.px0 = 10.0 + (c - 1) * pw0 + 52.0
    p.px1 = 10.0 + c * pw0 - 12.0 - (colorbar ? 34.0 : 0.0)
    p.py0 = top_band0 + (r - 1) * ph0 + (isempty(title) ? 8.0 : 24.0) + top_pad
    p.py1 = top_band0 + r * ph0 - 34.0
    p.xlo, p.xhi = Inf, -Inf
    p.ylo, p.yhi = Inf, -Inf
    p.xlo_t = 0.0; p.xhi_t = 1.0; p.ylo_t = 0.0; p.yhi_t = 1.0
    p.xlog, p.ylog = xlog, ylog
    p.title, p.xlabel, p.ylabel, p.tag = title, xlabel, ylabel, tag
    p.legend, p.legend_loc = legend, legend_loc
    p.infobox, p.infoloc = infobox, infoloc
    p.cb, p.cblab = colorbar, cblab
    p.xticks_c, p.yticks_c = xticks, yticks
    if xlim !== nothing
        p.xlo, p.xhi = xlim; p.xlim_fixed = true
    end
    if ylim !== nothing
        p.ylo, p.yhi = ylim; p.ylim_fixed = true
    end
    push!(f.panels, p)
    f.cur = length(f.panels)
    return p
end

"""Compute panel device rect from grid placement + measured margins.
Called from _relayout! (save_fig phase), so late-assigned titles and
wide tick labels get correct geometry (fixes title/subtitle collisions and
tick-label clipping)."""
function _layout_panel!(f::Fig, p::Panel)
    W, H = f.w, f.h
    top_band = isempty(f.title) ? 10.0 : (isempty(f.subtitle) ? 44.0 : 62.0)
    bot_band = isempty(f.footer) ? 8.0 : 26.0
    gx0 = 10.0; gx1 = W - 10.0
    gy0 = top_band; gy1 = H - bot_band
    pw = (gx1 - gx0) / p.gcols; ph = (gy1 - gy0) / p.grows
    # adaptive left margin: widest y-tick label + ylabel clearance
    _padlim!(p)
    ylabs = _ytick_labels(p)
    wlab = isempty(ylabs) ? 0.0 : maximum(text_width(s, 12) for s in ylabs)
    ml = clamp(wlab + 26.0, 52.0, 130.0) + (p.ylabel == "" ? 0.0 : 16.0)
    p.ml_used = ml
    mr = 12.0 + (p.cb ? 34.0 : 0.0)
    mt = (isempty(p.title) ? 8.0 : 24.0) + p.gtop
    mb = 34.0
    p.px0 = gx0 + (p.gc - 1) * pw + ml
    p.px1 = gx0 + p.gc * pw - mr
    p.py0 = gy0 + (p.gr - 1) * ph + mt
    p.py1 = gy0 + p.gr * ph - mb
    nothing
end

"""Two-phase layout pass: called at the top of save_fig, after all plot
elements are pushed, so titles/labels/limits are final. Recomputes every
panel rect with measured tick-label widths (no more clipped '1e-14' labels,
no more subtitle/panel-title collisions from late pa.title assignment)."""
function _relayout!(f::Fig)
    for p in f.panels
        _layout_panel!(f, p)
    end
end

"Y-tick label strings for the current limits (for margin measurement)."
function _ytick_labels(p::Panel)
    yt = p.yticks_c !== nothing ? p.yticks_c[1] :
         p.ylog ? _logticks(p.ylo_t, p.yhi_t)[1] : nice_ticks(p.ylo_t, p.yhi_t, 5)[1]
    String[p.yticks_c !== nothing ? p.yticks_c[2][i] :
           p.ylog ? _fmt_log(v) : _fmt_tick(v) for (i, v) in enumerate(yt)]
end

_setpanel!(f::Fig, p::Panel) = (f.cur = findfirst(==(p), f.panels); nothing)
_cur(f::Fig) = f.panels[f.cur]

function _update_lim!(p::Panel, xs::AbstractVector, ys::AbstractVector)
    p.lims_done = false        # new data → limits must be re-padded at layout
    if !p.xlim_fixed && !isempty(xs)
        lo = Inf; hi = -Inf
        for v in xs
            isfinite(v) || continue
            p.xlog && v <= 0 && continue
            v < lo && (lo = v); v > hi && (hi = v)
        end
        lo <= hi && (p.xlo = min(p.xlo, lo); p.xhi = max(p.xhi, hi))
    end
    if !p.ylim_fixed && !isempty(ys)
        p.lims_done = false
        lo = Inf; hi = -Inf
        for v in ys
            isfinite(v) || continue
            p.ylog && v <= 0 && continue
            v < lo && (lo = v); v > hi && (hi = v)
        end
        lo <= hi && (p.ylo = min(p.ylo, lo); p.yhi = max(p.yhi, hi))
    end
end

function _padlim!(p::Panel)
    p.lims_done && return nothing      # padding must not be applied twice
    p.lims_done = true
    # fallback when no data
    if isinf(p.xlo)
        p.xlo, p.xhi = 0.0, 1.0
    end
    if isinf(p.ylo)
        p.ylo, p.yhi = p.ylog ? 0.1 : 0.0, 1.0
    end
    # 4% margin, handle log
    if p.xlog
        p.xlo_t = log10(max(p.xlo, eps())); p.xhi_t = log10(max(p.xhi, p.xlo * (1 + 1e-9)))
        if !p.xlim_fixed
            d = p.xhi_t - p.xlo_t; p.xlo_t -= 0.02d; p.xhi_t += 0.02d
        end
    else
        if !p.xlim_fixed
            d = p.xhi - p.xlo; d = d == 0 ? 1.0 : d
            p.xlo -= 0.04d; p.xhi += 0.04d
        end
        p.xlo_t, p.xhi_t = p.xlo, p.xhi
    end
    if p.ylog
        p.ylo_t = log10(max(p.ylo, eps())); p.yhi_t = log10(max(p.yhi, p.ylo * (1 + 1e-9)))
        if !p.ylim_fixed
            d = p.yhi_t - p.ylo_t; p.ylo_t -= 0.02d; p.yhi_t += 0.02d
        end
    else
        if !p.ylim_fixed
            d = p.yhi - p.ylo; d = d == 0 ? 1.0 : d
            p.ylo -= 0.05d; p.yhi += 0.05d
        end
        p.ylo_t, p.yhi_t = p.ylo, p.yhi
    end
end

# --- plotting API (operate on current panel) ---

"Line plot. kw: color(Int|RGBA32), width, label, dash, alpha, marker+msize (adds markers)."
function plot!(f::Fig, xs::AbstractVector, ys::AbstractVector;
               color::Union{Int,RGBA32} = 1, width::Real = 2.0,
               label::String = "", dash::String = "", alpha::Real = 1.0,
               marker::Union{Symbol,Nothing} = nothing, msize::Real = 3.0)
    p = _cur(f)
    c = color isa Int ? f.theme.series[color] : color
    c = withalpha(c, alpha)
    _update_lim!(p, xs, ys)
    push!(p.els, PlotEl(:line, (collect(Float64, xs), collect(Float64, ys)),
                        (c, Float64(width), label, dash)))
    label != "" && _legend_used!(p)
    if marker !== nothing
        push!(p.els, PlotEl(:scatter, (collect(Float64, xs), collect(Float64, ys)),
                            (c, marker, Float64(msize), "")))
    end
    p
end

"Scatter. kw: color, marker(:circle :square :tri :diamond :cross :plus :dot), size, label, alpha."
function scatter!(f::Fig, xs::AbstractVector, ys::AbstractVector;
                  color::Union{Int,RGBA32} = 1, marker::Symbol = :circle,
                  size::Real = 3.5, msize::Union{Nothing,Real} = nothing,
                  label::String = "", alpha::Real = 1.0)
    sz = msize === nothing ? size : msize   # msize alias (compat)
    p = _cur(f)
    c = color isa Int ? f.theme.series[color] : color
    c = withalpha(c, alpha)
    _update_lim!(p, xs, ys)
    push!(p.els, PlotEl(:scatter, (collect(Float64, xs), collect(Float64, ys)),
                        (c, marker, Float64(sz), label)))
    label != "" && _legend_used!(p)
    p
end

# v23.1: module hist!/_ebin/heatmap! removed — no test ever called them; the
# :hist/:heat renderer branches stay as harmless engine internals.

"Filled band between ylo and yhi arrays (confidence envelope)."
function band!(f::Fig, xs::AbstractVector, ylo::AbstractVector, yhi::AbstractVector;
               color::Union{Int,RGBA32} = 1, alpha::Real = 0.18, label::String = "")
    p = _cur(f)
    c = color isa Int ? f.theme.series[color] : color
    _update_lim!(p, xs, [ylo; yhi])
    push!(p.els, PlotEl(:band, (collect(Float64, xs), collect(Float64, ylo),
                                collect(Float64, yhi)), (c, Float64(alpha), label)))
    label != "" && _legend_used!(p)
    p
end

function hline!(f::Fig, y::Real; color::Union{Int,RGBA32} = 2, dash::String = "6,4",
                width::Real = 1.6, label::String = "", alpha::Real = 1.0)
    p = _cur(f)
    c = color isa Int ? f.theme.series[color] : color
    if !p.ylim_fixed
        p.lims_done = false
        p.ylo = min(p.ylo, Float64(y)); p.yhi = max(p.yhi, Float64(y))
    end
    push!(p.els, PlotEl(:hline, Float64(y), (c, dash, Float64(width), label, Float32(alpha))))
    label != "" && _legend_used!(p)
    p
end
function vline!(f::Fig, x::Real; color::Union{Int,RGBA32} = 2, dash::String = "6,4",
                width::Real = 1.6, label::String = "", alpha::Real = 1.0)
    p = _cur(f)
    c = color isa Int ? f.theme.series[color] : color
    if !p.xlim_fixed
        p.lims_done = false
        p.xlo = min(p.xlo, Float64(x)); p.xhi = max(p.xhi, Float64(x))
    end
    push!(p.els, PlotEl(:vline, Float64(x), (c, dash, Float64(width), label, Float32(alpha))))
    label != "" && _legend_used!(p)
    p
end

"Axis-anchored text in world coords."
function text!(f::Fig, x::Real, y::Real, s::String; size::Real = 13,
               color::Union{Int,RGBA32} = 0, align::Symbol = :left, alpha::Real = 1.0)
    p = _cur(f)
    c = color isa Int ? (color == 0 ? f.theme.text : f.theme.series[color]) : color
    push!(p.els, PlotEl(:text, (Float64(x), Float64(y), s),
                        (c, Float64(size), align, Float32(alpha))))
    p
end

"Annotation with optional leader line from (tx,ty) label to (x,y) target in world coords."
function annotate!(f::Fig, x::Real, y::Real, s::String; tx::Real = x, ty::Real = y,
                   size::Real = 12, color::Union{Int,RGBA32} = 0, arrow::Bool = true)
    p = _cur(f)
    c = color isa Int ? (color == 0 ? f.theme.dim : f.theme.series[color]) : color
    push!(p.els, PlotEl(:ann, (Float64(x), Float64(y), s, Float64(tx), Float64(ty)),
                        (c, Float64(size), arrow)))
    p
end

_legend_used!(p::Panel) = (p.legend = true; nothing)

# --- rendering ---
function _render_els!(cv::Canvas, p::Panel, th::Theme, f::Fig)
    for el in p.els
        if el.kind == :line
            xs, ys = el.args
            c, w, _, dash = el.kwargs
            _clip_line_series!(cv, p, xs, ys, c, w, dash)
        elseif el.kind == :scatter
            xs, ys = el.args
            c, mk, sz, _ = el.kwargs
            for i in eachindex(xs)
                (isnan(xs[i]) || isnan(ys[i])) && continue
                _marker!(cv, p, xs[i], ys[i], mk, sz, c)
            end
        elseif el.kind == :hist
            edges, ys = el.args
            c, al, _, outline = el.kwargs
            for k in eachindex(ys)
                x0 = _mapx(p, edges[k]); x1 = _mapx(p, edges[k+1])
                yv = _mapy(p, ys[k]); yb = _mapy(p, _base_y(p))
                fill_rect!(cv, x0 + 0.5, min(yv, yb), x1 - 0.5, max(yv, yb), withalpha(c, al))
                if outline
                    draw_line!(cv, x0 + 0.5, yv, x1 - 0.5, yv, c, 1.4)
                    draw_line!(cv, x0 + 0.5, yv, x0 + 0.5, yb, withalpha(c, 0.7), 1.0)
                    draw_line!(cv, x1 - 0.5, yv, x1 - 0.5, yb, withalpha(c, 0.7), 1.0)
                end
            end
        elseif el.kind == :band
            xs, yl, yh = el.args
            c, al, _ = el.kwargs
            pts = Tuple{Float64,Float64}[]
            for i in eachindex(xs)
                (isfinite(xs[i]) && isfinite(yl[i])) || continue
                push!(pts, (_mapx(p, xs[i]), _mapy(p, clamp(yl[i], _ymin(p), _ymax(p)))))
            end
            for i in length(xs):-1:1
                (isfinite(xs[i]) && isfinite(yh[i])) || continue
                push!(pts, (_mapx(p, xs[i]), _mapy(p, clamp(yh[i], _ymin(p), _ymax(p)))))
            end
            _clip_pts!(pts, p)
            fill_polygon!(cv, pts, withalpha(c, al))
        elseif el.kind == :hline
            y, kw = el.args, el.kwargs
            c, dash, w, _, al = kw
            draw_line!(cv, p.px0, _mapy(p, y), p.px1, _mapy(p, y), withalpha(c, al), w, dash)
        elseif el.kind == :vline
            x, kw = el.args, el.kwargs
            c, dash, w, _, al = kw
            draw_line!(cv, _mapx(p, x), p.py0, _mapx(p, x), p.py1, withalpha(c, al), w, dash)
        elseif el.kind == :text
            x, y, s = el.args
            c, sz, align, al = el.kwargs
            if p.xlo <= x <= p.xhi && p.ylo <= y <= p.yhi
                draw_text!(cv, _mapx(p, x), _mapy(p, y), s, sz,
                           withalpha(c, al); align = align)
            end
        elseif el.kind == :ann
            x, y, s, tx, ty = el.args
            c, sz, arrow = el.kwargs
            X, Y = _mapx(p, x), _mapy(p, y)
            TX, TY = _mapx(p, tx), _mapy(p, ty)
            w = text_width(s, sz) * cv.ss
            hx = TX < X ? TX + w + 6 * cv.ss : TX - w - 6 * cv.ss
            draw_text!(cv, hx, TY + 4 * cv.ss, s, sz, c; align = TX < X ? :left : :right)
            if arrow && hypot(X - TX, Y - TY) > 8cv.ss
                draw_line!(cv, TX, TY, X, Y, withalpha(c, 0.8), 1.2)
                # arrowhead
                ang = atan(Y - TY, X - TX)
                ah = 6 * cv.ss
                p1 = (X - ah * cos(ang - 0.4), Y - ah * sin(ang - 0.4))
                p2 = (X - ah * cos(ang + 0.4), Y - ah * sin(ang + 0.4))
                fill_polygon!(cv, [(X, Y), p1, p2], withalpha(c, 0.9))
            end
        elseif el.kind == :heat
            xs, ys, M, zl, zh = el.args
            cname, _ = el.kwargs
            nx, ny = length(xs), length(ys)
            for j in 1:ny-1, i in 1:nx-1
                v = (M[j, i] - zl) / (zh - zl)
                col = cmap(cname, v)
                fill_rect!(cv, _mapx(p, xs[i]), _mapy(p, ys[j+1]),
                           _mapx(p, xs[i+1]), _mapy(p, ys[j]),
                           withalpha(col, 1.0))
            end
        end
    end
end
_base_y(p::Panel) = max(p.ylo, min(0.0, p.yhi))
_ymin(p::Panel) = p.ylog ? 10.0^(p.ylo_t) : p.ylo
_ymax(p::Panel) = p.ylog ? 10.0^(p.yhi_t) : p.yhi

function _clip_line_series!(cv, p, xs, ys, c, w, dash)
    # simple clip to panel box, then map & draw segments
    lo_x, hi_x = p.xlo, p.xhi
    prev_ok = false; prevX = prevY = 0.0
    started = false
    for i in eachindex(xs)
        x, y = xs[i], ys[i]
        ok = isfinite(x) && isfinite(y) && (p.xlog ? x > 0 : true) && (p.ylog ? y > 0 : true)
        if ok && started
            X, Y = _mapx(p, x), _mapy(p, clamp(y, _ymin(p), _ymax(p)))
            draw_line!(cv, prevX, prevY, X, Y, c, w, ok ? dash : "")
            prevX, prevY = X, Y
        elseif ok && !started
            prevX, prevY = _mapx(p, x), _mapy(p, clamp(y, _ymin(p), _ymax(p)))
            started = true
        else
            started = false
        end
        prev_ok = ok
    end
end

function _clip_pts!(pts, p)
    lo, hi = p.py0, p.py1
    for i in eachindex(pts)
        pts[i] = (pts[i][1], clamp(pts[i][2], lo, hi))
    end
end

function _marker!(cv, p, x::Real, y::Real, mk::Symbol, sz::Real, c::RGBA32)
    (p.xlog ? x <= 0 : false) && return
    (p.ylog ? y <= 0 : false) && return
    X = _mapx(p, x); Y = _mapy(p, y)
    (isnan(X) || isnan(Y)) && return
    (X < p.px0 - 2 || X > p.px1 + 2 || Y < p.py0 - 2 || Y > p.py1 + 2) && return
    s = sz * cv.ss
    if mk == :circle
        fill_circle!(cv, X, Y, s, c)
    elseif mk == :square
        fill_rect!(cv, X - s, Y - s, X + s, Y + s, c)
    elseif mk == :dot
        fill_circle!(cv, X, Y, max(1, s * 0.55), c)
    elseif mk == :tri
        fill_polygon!(cv, [(X, Y - s * 1.2), (X - s, Y + s * 0.8), (X + s, Y + s * 0.8)], c)
    elseif mk == :diamond
        fill_polygon!(cv, [(X, Y - s * 1.3), (X - s * 1.1, Y), (X, Y + s * 1.3), (X + s * 1.1, Y)], c)
    elseif mk == :cross
        draw_line!(cv, X - s, Y - s, X + s, Y + s, c, 1.6)
        draw_line!(cv, X - s, Y + s, X + s, Y - s, c, 1.6)
    elseif mk == :plus
        draw_line!(cv, X - s, Y, X + s, Y, c, 1.6)
        draw_line!(cv, X, Y - s, X, Y + s, c, 1.6)
    end
end

"Draw panel: bg, grid, data, frame, ticks, labels, legend, infobox, tag."
function _render_panel!(f::Fig, p::Panel)
    cv, th = f.cv, f.theme
    fill_rect!(cv, p.px0 - 1, p.py0 - 1, p.px1 + 1, p.py1 + 1, th.panel)
    # grid + ticks
    _padlim!(p)
    xt, _ = p.xticks_c !== nothing ? (p.xticks_c[1], 1.0) :
            p.xlog ? _logticks(p.xlo_t, p.xhi_t) : nice_ticks(p.xlo_t, p.xhi_t, 6)
    yt, _ = p.yticks_c !== nothing ? (p.yticks_c[1], 1.0) :
            p.ylog ? _logticks(p.ylo_t, p.yhi_t) : nice_ticks(p.ylo_t, p.yhi_t, 5)
    xminor = p.xlog ? _logminor(p.xlo_t, p.xhi_t) : Float64[]
    yminor = p.ylog ? _logminor(p.ylo_t, p.yhi_t) : Float64[]
    for v in xminor
        X = _mapx(p, 10.0^v)
        draw_line!(cv, X, p.py0, X, p.py1, th.gridminor, 1.0)
    end
    for v in yminor
        Y = _mapy(p, 10.0^v)
        draw_line!(cv, p.px0, Y, p.px1, Y, th.gridminor, 1.0)
    end
    for v in xt
        X = _mapx(p, p.xlog ? 10.0^v : v)
        draw_line!(cv, X, p.py0, X, p.py1, th.grid, 1.0)
    end
    for v in yt
        Y = _mapy(p, p.ylog ? 10.0^v : v)
        draw_line!(cv, p.px0, Y, p.px1, Y, th.grid, 1.0)
    end
    _render_els!(cv, p, th, f)
    # frame
    draw_line!(cv, p.px0, p.py0, p.px1, p.py0, th.frame, 1.4)
    draw_line!(cv, p.px1, p.py0, p.px1, p.py1, th.frame, 1.4)
    draw_line!(cv, p.px0, p.py1, p.px1, p.py1, th.frame, 1.4)
    draw_line!(cv, p.px0, p.py0, p.px0, p.py1, th.frame, 1.4)
    # tick labels + tick marks
    for (i, v) in enumerate(xt)
        X = _mapx(p, p.xlog ? 10.0^v : v)
        (X < p.px0 - 1 || X > p.px1 + 1) && continue
        draw_line!(cv, X, p.py1, X, p.py1 + 5, th.frame, 1.2)
        lab = p.xticks_c !== nothing ? p.xticks_c[2][i] :
              p.xlog ? _fmt_log(v) : _fmt_tick(v)
        draw_text!(cv, X, p.py1 + 9 + 7, lab, 12, th.text; align = :center)
    end
    for (i, v) in enumerate(yt)
        Y = _mapy(p, p.ylog ? 10.0^v : v)
        (Y < p.py0 - 1 || Y > p.py1 + 1) && continue
        draw_line!(cv, p.px0 - 5, Y, p.px0, Y, th.frame, 1.2)
        lab = p.yticks_c !== nothing ? p.yticks_c[2][i] :
              p.ylog ? _fmt_log(v) : _fmt_tick(v)
        draw_text!(cv, p.px0 - 8, Y + 4, lab, 12, th.text; align = :right)
    end
    # titles
    if p.title != ""
        draw_text!(cv, (p.px0 + p.px1) / 2, p.py0 - 10, p.title, 15, th.title; align = :center)
    end
    if p.xlabel != ""
        draw_text!(cv, (p.px0 + p.px1) / 2, p.py1 + 33, p.xlabel, 13.5, th.text; align = :center)
    end
    if p.ylabel != ""
        # centered in the (adaptive) left margin, clear of tick labels
        draw_text!(cv, p.px0 - max(p.ml_used, 40.0) + 12, (p.py0 + p.py1) / 2,
                   p.ylabel, 13.5, th.text; align = :center, angle = 90)
    end
    if p.tag != ""
        draw_text!(cv, p.px0 + 2, p.py0 - 10, p.tag, 14, th.title; align = :left)
    end
    # colorbar
    if p.cb
        cwx = p.px1 + 8
        cw = 12
        chh = p.py1 - p.py0
        n = 100
        cname = "viridis"
        for el in p.els
            el.kind == :heat && (cname = el.kwargs[1])
        end
        for i in 0:n-1
            t = i / (n - 1)
            col = cmap(cname, t)
            fill_rect!(cv, cwx, p.py1 - t * chh, cwx + cw, p.py1 - (t + 1 / n) * chh - 0.5, col)
        end
        draw_line!(cv, cwx, p.py0, cwx, p.py1, th.frame, 1.2)
        draw_line!(cv, cwx + cw, p.py0, cwx + cw, p.py1, th.frame, 1.2)
        draw_line!(cv, cwx, p.py0, cwx + cw, p.py0, th.frame, 1.2)
        draw_line!(cv, cwx, p.py1, cwx + cw, p.py1, th.frame, 1.2)
        vlo = p.ylog ? 10.0^p.ylo_t : p.ylo
        vhi = p.ylog ? 10.0^p.yhi_t : p.yhi
        draw_text!(cv, cwx + cw + 4, p.py0 + 6, _fmt_num_short(vhi), 10.5, th.text)
        draw_text!(cv, cwx + cw + 4, p.py1 + 6, _fmt_num_short(vlo), 10.5, th.text)
        if p.cblab != ""
            draw_text!(cv, cwx + cw + 16, (p.py0 + p.py1) / 2, p.cblab, 11.5, th.text;
                       align = :center, angle = 90)
        end
    end
    # legend
    if p.legend
        _draw_legend!(f, p)
    end
    # infobox
    if !isempty(p.infobox)
        _draw_infobox!(f, p)
    end
end

_fmt_num_short(v) = begin
    a = abs(v)
    if a >= 1e4 || (a < 1e-3 && a > 0)
        @sprintf("%.1e", v)
    elseif a >= 100
        @sprintf("%.0f", v)
    elseif a >= 1
        @sprintf("%.2f", v)
    else
        @sprintf("%.3f", v)
    end
end

function _logticks(lo::Float64, hi::Float64)
    e0 = floor(lo); e1 = ceil(hi)
    ticks = Float64[]
    span = hi - lo
    stepd = span > 8 ? 2 : 1
    e = e0
    while e <= e1
        push!(ticks, Float64(e))
        e += stepd
    end
    return ticks, 1.0
end
function _logminor(lo::Float64, hi::Float64)
    m = Float64[]
    span = hi - lo
    e0 = floor(lo); e1 = ceil(hi)
    span > 6 && return m
    for e in Int(e0):Int(e1)
        for k in 2:9
            v = e + log10(k)
            lo <= v <= hi && push!(m, v)
        end
    end
    m
end

function _legend_items(p::Panel, th::Theme)
    items = Tuple{String,Any,Symbol,Float64,String}[]  # label, color, marker, size, dash
    for el in p.els
        if el.kind == :line && el.kwargs[3] != ""
            push!(items, (el.kwargs[3], el.kwargs[1], :line, el.kwargs[2], el.kwargs[4]))
        elseif el.kind == :scatter && el.kwargs[4] != ""
            push!(items, (el.kwargs[4], el.kwargs[1], el.kwargs[2], el.kwargs[3], ""))
        elseif el.kind == :hist && el.kwargs[3] != ""
            push!(items, (el.kwargs[3], el.kwargs[1], :box, 8.0, ""))
        elseif el.kind == :band && el.kwargs[3] != ""
            push!(items, (el.kwargs[3], el.kwargs[1], :band, 8.0, ""))
        elseif el.kind == :hline && el.kwargs[4] != ""
            push!(items, (el.kwargs[4], el.kwargs[1], :dash, 2.0, el.kwargs[2]))
        elseif el.kind == :vline && el.kwargs[4] != ""
            push!(items, (el.kwargs[4], el.kwargs[1], :vdash, 2.0, el.kwargs[2]))
        end
    end
    items
end

function _draw_legend!(f::Fig, p::Panel)
    cv, th = f.cv, f.theme
    items = _legend_items(p, th)
    isempty(items) && return
    fs = 12.0
    lh = 17.0
    wmax = maximum(text_width(it[1], fs) for it in items)
    boxw = wmax + 58
    boxh = length(items) * lh + 10
    (lx, ly) = _corner_pos(p, f, p.legend_loc, boxw, boxh)
    fill_rect!(cv, lx, ly, lx + boxw, ly + boxh, th.legendbg)
    draw_line!(cv, lx, ly, lx + boxw, ly, th.frame, 1.0)
    draw_line!(cv, lx + boxw, ly, lx + boxw, ly + boxh, th.frame, 1.0)
    draw_line!(cv, lx, ly + boxh, lx + boxw, ly + boxh, th.frame, 1.0)
    draw_line!(cv, lx, ly, lx, ly + boxh, th.frame, 1.0)
    for (i, (lab, col, mk, sz, dash)) in enumerate(items)
        yy = ly + i * lh - 4
        c = col isa RGBA32 ? col : th.series[mod1(Int(col), length(th.series))]
        xc = lx + 26
        if mk == :line
            draw_line!(cv, xc - 20, yy - 3, xc + 6, yy - 3, c, sz)
        elseif mk == :dash
            draw_line!(cv, xc - 20, yy - 3, xc + 6, yy - 3, c, sz, dash == "" ? "6,4" : dash)
        elseif mk == :vdash
            draw_line!(cv, xc - 20, yy - 3, xc + 6, yy - 3, c, sz, dash == "" ? "2,3" : dash)
        elseif mk == :box
            fill_rect!(cv, xc - 18, yy - 9, xc + 2, yy + 1, withalpha(c, 0.5))
            draw_line!(cv, xc - 18, yy - 9, xc + 2, yy - 9, c, 1.2)
            draw_line!(cv, xc + 2, yy - 9, xc + 2, yy + 1, c, 1.2)
        elseif mk == :band
            fill_rect!(cv, xc - 18, yy - 9, xc + 2, yy + 1, withalpha(c, 0.25))
            draw_line!(cv, xc - 18, yy - 5, xc + 2, yy - 5, c, 1.4)
        else
            _marker_direct!(cv, xc - 7, yy - 3, mk, sz, c)
        end
        draw_text!(cv, xc + 12, yy, lab, fs, th.text)
    end
end

function _marker_direct!(cv, X, Y, mk, s, c)
    if mk == :circle; fill_circle!(cv, X, Y, s, c)
    elseif mk == :square; fill_rect!(cv, X - s, Y - s, X + s, Y + s, c)
    elseif mk == :tri
        fill_polygon!(cv, [(X, Y - s * 1.2), (X - s, Y + s * 0.8), (X + s, Y + s * 0.8)], c)
    elseif mk == :diamond
        fill_polygon!(cv, [(X, Y - s * 1.3), (X - s * 1.1, Y), (X, Y + s * 1.3), (X + s * 1.1, Y)], c)
    elseif mk == :cross
        draw_line!(cv, X - s, Y - s, X + s, Y + s, c, 1.6)
        draw_line!(cv, X - s, Y + s, X + s, Y - s, c, 1.6)
    elseif mk == :plus
        draw_line!(cv, X - s, Y, X + s, Y, c, 1.6)
        draw_line!(cv, X, Y - s, X, Y + s, c, 1.6)
    end
end

function _corner_pos(p::Panel, f::Fig, loc::Symbol, boxw, boxh)
    m = 6.0
    if loc == :topright
        return (p.px1 - boxw - m, p.py0 + m)
    elseif loc == :topleft
        return (p.px0 + m, p.py0 + m)
    elseif loc == :bottomright
        return (p.px1 - boxw - m, p.py1 - boxh - m)
    else
        return (p.px0 + m, p.py1 - boxh - m)
    end
end

function _draw_infobox!(f::Fig, p::Panel)
    cv, th = f.cv, f.theme
    fs = 12.0; lh = 16.0
    wmax = maximum(text_width(s, fs) for s in p.infobox)
    boxw = wmax + 16
    boxh = length(p.infobox) * lh + 10
    (lx, ly) = _corner_pos(p, f, p.infoloc, boxw, boxh)
    fill_rect!(cv, lx, ly, lx + boxw, ly + boxh, th.legendbg)
    for (frame_edge) in ((lx, ly, lx + boxw, ly), (lx + boxw, ly, lx + boxw, ly + boxh),
                         (lx, ly + boxh, lx + boxw, ly + boxh), (lx, ly, lx, ly + boxh))
        draw_line!(cv, frame_edge..., th.frame, 1.0)
    end
    for (i, s) in enumerate(p.infobox)
        draw_text!(cv, lx + 8, ly + i * lh - 2, s, fs, th.text)
    end
end

"Finalize and save figure PNG."
function save_fig(f::Fig, path::AbstractString)
    cv, th = f.cv, f.theme
    _relayout!(f)          # two-phase layout: titles/labels/limits are final here
    fill_rect!(cv, 0, 0, cv.w, cv.h, th.bg)
    # title
    if f.title != ""
        draw_text!(cv, cv.w / 2, 26, f.title, 20, th.title; align = :center)
    end
    if f.subtitle != ""
        draw_text!(cv, cv.w / 2, 50, f.subtitle, 13, th.dim; align = :center)
    end
    for p in f.panels
        _render_panel!(f, p)
    end
    if f.footer != ""
        draw_text!(cv, 12, f.h - 10, f.footer, 11.5, th.dim)
    end
    # downsample
    ss = cv.ss
    W, H = cv.w, cv.h
    out = Vector{UInt8}(undef, W * H * 3)
    n2 = ss * ss
    buf = cv.buf
    Ws = cv.W
    for y in 1:H, x in 1:W
        r = g = b = 0.0f0
        for dy in 1:ss, dx in 1:ss
            o = ((y - 1) * ss + dy - 1) * Ws * 3 + ((x - 1) * ss + dx - 1) * 3
            r += buf[o+1]; g += buf[o+2]; b += buf[o+3]
        end
        o = ((y - 1) * W + (x - 1)) * 3
        out[o+1] = round(UInt8, clamp(r / n2, 0, 1) * 255)
        out[o+2] = round(UInt8, clamp(g / n2, 0, 1) * 255)
        out[o+3] = round(UInt8, clamp(b / n2, 0, 1) * 255)
    end
    save_png(path, W, H, out)
end



"""
    render_rgb(f) -> Array{UInt8,3} (H, W, 3)

Paint the finished figure (title, panels, footer) and downsample the
supersampled raster to 8-bit RGB — the bridge to the v21 report writer
(write_png / GIF encoder expect exactly this layout). Same painting and
downsampling math as `save_fig`, minus the file I/O.
"""
function render_rgb(f::Fig)::Array{UInt8,3}
    cv, th = f.cv, f.theme
    _relayout!(f)          # two-phase layout: titles/labels/limits final here
    fill_rect!(cv, 0, 0, cv.w, cv.h, th.bg)
    if f.title != ""
        draw_text!(cv, cv.w / 2, 26, f.title, 20, th.title; align = :center)
    end
    if f.subtitle != ""
        draw_text!(cv, cv.w / 2, 50, f.subtitle, 13, th.dim; align = :center)
    end
    for p in f.panels
        _render_panel!(f, p)
    end
    if f.footer != ""
        draw_text!(cv, 12, f.h - 10, f.footer, 11.5, th.dim)
    end
    ss = cv.ss
    W, H = cv.w, cv.h
    out = Array{UInt8,3}(undef, H, W, 3)
    n2 = ss * ss
    buf = cv.buf
    Ws = cv.W
    for y in 1:H, x in 1:W
        r = g = b = 0.0f0
        for dy in 1:ss, dx in 1:ss
            o = ((y - 1) * ss + dy - 1) * Ws * 3 + ((x - 1) * ss + dx - 1) * 3
            r += buf[o+1]; g += buf[o+2]; b += buf[o+3]
        end
        out[y, x, 1] = round(UInt8, clamp(r / n2, 0, 1) * 255)
        out[y, x, 2] = round(UInt8, clamp(g / n2, 0, 1) * 255)
        out[y, x, 3] = round(UInt8, clamp(b / n2, 0, 1) * 255)
    end
    return out
end

end # module ABPlotV23


# ═════════════════════════════════════════════════════════════════════════════
# §1. REPLOT MODEL + ABPlotV23 BRIDGE (the suite's plot pipeline, compact)
# ═════════════════════════════════════════════════════════════════════════════

mutable struct RepPlot
    title::String
    xlabel::String
    ylabel::String
    series::Vector{Tuple{String,Vector{Float64},Vector{Float64},Char}} # name,xs,ys,style('l','s','L'=line+markers)
end
RepPlot(title::String, xlabel::String, ylabel::String) =
    RepPlot(title, xlabel, ylabel, Tuple{String,Vector{Float64},Vector{Float64},Char}[])

function add_series!(p::RepPlot, name::String, xs::Vector{<:Real}, ys::Vector{<:Real}, style::Char = 'l')
    push!(p.series, (name, float.(xs), float.(ys), style))
    return p
end

_utc_stamp_v23() = Dates.format(Dates.now(), "yyyy-mm-dd HH:MM") * " UTC"

"""Translate a RepPlot into an ABPlotV23 journal figure (dark theme,
supersampled, real legend) — verbatim bridge from the suite."""
function _repplot_to_fig(p::RepPlot, w::Int, h::Int)::ABPlotV23.Fig
    f = ABPlotV23.make_fig(w, h;
        title = p.title, subtitle = "",
        footer = @sprintf("hp_audit_standalone v23.6 · ABPlotV23 engine · %s", _utc_stamp_v23()),
        theme = "dark", ss = 2)
    nser = length(p.series)
    ABPlotV23.add_panel!(f, 1, 1, 1, 1;
        xlabel = p.xlabel, ylabel = p.ylabel,
        legend = nser > 1, legend_loc = :topright)
    for (i, (name, xs, ys, style)) in enumerate(p.series)
        isempty(xs) && continue
        if style == 's'
            ABPlotV23.scatter!(f, xs, ys; color = i, marker = :circle,
                               size = 3.6, label = name)
        else # 'l' and 'L' both draw the line; 'L' adds the markers
            ABPlotV23.plot!(f, xs, ys; color = i, width = 2.2, label = name,
                            marker = style == 'L' ? :circle : nothing, msize = 3.4)
        end
    end
    return f
end

function save_repplot_png(p::RepPlot, path::String)
    f = _repplot_to_fig(p, 1600, 1000)
    ABPlotV23.save_fig(f, path)
    return path
end

# ═════════════════════════════════════════════════════════════════════════════
# §2. MINI RUNTIME — logs, reports state, progress, verdict tables
#     (signatures match the suite so the H1–H7 runners stay VERBATIM)
# ═════════════════════════════════════════════════════════════════════════════

# ══════════════════════════════════════════════════════════════════════════
# MERIDIAN DESIGN SYSTEM v1.0-HP — консольная айдентика (self-contained)
#   Двойные рамки, ◆-секции, ✓/✗/⚠/● статусы, ▰▱ прогресс, kv-строки,
#   панельные таблицы. Только Base. Префикс _mr_ — без коллизий.
#   Цвет только на TTY; ENV["MERIDIAN_COLOR_FORCE"]="1" форс,
#   ENV["HP_SA_COLOR"]="0" или ENV["MERIDIAN_COLOR"]="0" — всё выключает.
# ══════════════════════════════════════════════════════════════════════════

_MR_W = 62  # ширина рамок (помещается даже на телефоне)
_MR_ANSI = Dict{String,String}(
    "title" => "1;36", "gold" => "1;33", "dim" => "2", "ok" => "32",
    "warn" => "1;33", "err" => "1;31", "accent" => "36", "bold" => "1",
    "violet" => "35")
_MR_COLOR = Ref{Bool}(false)
const _MR_BOOTED = Ref{Bool}(false)

function _mr_init_color!()
    force = get(ENV, "MERIDIAN_COLOR_FORCE", "0") == "1"
    off   = get(ENV, "MERIDIAN_COLOR", "1") == "0" ||
            get(ENV, "HP_SA_COLOR", "1") == "0"
    dumb  = get(ENV, "TERM", "xterm") in ("dumb", "")
    win   = Sys.iswindows() && !haskey(ENV, "WT_SESSION") &&
            !haskey(ENV, "TERM_PROGRAM") && !haskey(ENV, "ANSICON")
    _MR_COLOR[] = !off && (force || (!dumb && !win && stdout isa Base.TTY))
    _MR_BOOTED[] = true
    return _MR_COLOR[]
end

function _mr_c(s::AbstractString, key::String)
    _MR_BOOTED[] || _mr_init_color!()
    return _MR_COLOR[] ? string("\e[", _MR_ANSI[key], "m", s, "\e[0m") : String(s)
end

"""Strip ANSI SGR sequences — used to keep file reports plain."""
_mr_strip_ansi(s::AbstractString) =
    replace(String(s), r"\e\[[0-9;]*m" => "")

function _mr_fit(s::AbstractString, w::Int)
    s = String(s)
    tw = textwidth(s)
    tw <= w && return s * " "^max(0, w - tw)
    out = ""; acc = 0
    for ch in s
        cw = textwidth(ch)
        acc + cw > w - 1 && break
        out *= ch; acc += cw
    end
    return out * "…"
end

function _mr_center(s::AbstractString, w::Int = _MR_W)
    tw = textwidth(s)
    if tw > w
        s = _mr_fit(s, w)
        tw = textwidth(s)
    end
    pad = max(0, w - tw); l = pad ÷ 2
    return " "^l * String(s) * " "^(pad - l)
end

"""Word-wrap a string to width w (textwidth-aware, no hyphenation)."""
function _mr_wrap(s::AbstractString, w::Int)
    out = String[]
    for para in split(String(s), '\n')
        isempty(strip(para)) && (push!(out, ""); continue)
        cur = ""
        for word in split(para)
            wd = String(word)
            if isempty(cur)
                cur = wd
            elseif textwidth(cur) + 1 + textwidth(wd) <= w
                cur *= " " * wd
            else
                push!(out, cur); cur = wd
            end
        end
        isempty(cur) || push!(out, cur)
    end
    return out
end

"""Big identity frame — printed once by the CLI entry."""
function _mr_banner(title::AbstractString, version::AbstractString,
                    subtitle::AbstractString...; brand::AbstractString = "◆")
    try
        _mr_init_color!()
        W = _MR_W
        hdr = string(brand, " ", title, "  ", version)
        println()
        println(_mr_c("╔" * "═"^W * "╗", "title"))
        println(_mr_c("║", "title") * _mr_c(_mr_center(hdr, W), "title") *
                _mr_c("║", "title"))
        println(_mr_c("╠" * "═"^W * "╣", "title"))
        for s in subtitle
            isempty(s) && continue
            println(_mr_c("║", "title") * _mr_c(_mr_center(s, W), "dim") *
                    _mr_c("║", "title"))
        end
        println(_mr_c("╚" * "═"^W * "╝", "title"))
        flush(stdout)
    catch
        println(title, " — ", version)
    end
    return nothing
end

"""Section header:   ── ◆ NAME ─────────────"""
function _mr_section(name::AbstractString)
    try
        n = String(name)
        rest = max(4, _MR_W - 6 - textwidth(n))
        println("  " * _mr_c("── ", "dim") * _mr_c("◆ " * n * " ", "gold") *
                _mr_c("─"^rest, "dim"))
        flush(stdout)
    catch
        println("\n── ", name, " ──")
    end
    return nothing
end

"""Gate head: double frame with the unique codename + dim question line."""
function _mr_gate_head(k::Int, codename::AbstractString, title::AbstractString,
                       question::AbstractString)
    try
        println()
        W = _MR_W
        println(_mr_c("╔" * "═"^W * "╗", "title"))
        println(_mr_c("║", "title") *
                _mr_c(_mr_center("GATE H" * string(k) * " · " * String(codename), W), "title") *
                _mr_c("║", "title"))
        println(_mr_c("╠" * "═"^W * "╣", "title"))
        for ln in _mr_wrap(String(title), W - 2)
            println(_mr_c("║", "title") * _mr_c(_mr_center(ln, W), "gold") *
                    _mr_c("║", "title"))
        end
        println(_mr_c("╚" * "═"^W * "╝", "title"))
        for ln in _mr_wrap(String(question), W - 2)
            println("  " * _mr_c(ln, "dim"))
        end
        flush(stdout)
    catch
        println("\n── ", title, " ──")
    end
    return nothing
end

function _mr_status(glyph::String, color::String, msg::AbstractString)
    try
        println("  " * _mr_c(glyph, color) * " " * String(msg))
        flush(stdout)
    catch
        println("  ", msg)
    end
    return nothing
end
_mr_ok(m)   = _mr_status("✓", "ok",    m)
_mr_warn(m) = _mr_status("⚠", "warn",  m)
_mr_fail(m) = _mr_status("✗", "err",   m)
_mr_info(m) = _mr_status("●", "accent", m)

"""Aligned «key : value» line."""
function _mr_kv(k::AbstractString, v; w::Int = 14)
    try
        println("  " * _mr_c(_mr_fit(string(k) * ":", w), "accent") * " " *
                _mr_c(string(v), "bold"))
    catch
        println("  ", k, ": ", v)
    end
    return nothing
end

"""Rounded result panel. Leading ✓ green, ! → ⚠ yellow, ✗ red, else dim."""
function _mr_panel(title::AbstractString, rows::Vector{<:AbstractString})
    try
        W = _MR_W
        println(_mr_c("╭─", "title") * _mr_c("◆ ", "gold") *
                _mr_c(_mr_fit(String(title), W - 3), "title") *
                _mr_c("╮", "title"))
        for r in rows
            s = String(r)
            if startswith(s, "!")
                body = "  ⚠ " * s[nextind(s, 1):end]; key = "warn"
            elseif startswith(s, "✗")
                body = "  " * s; key = "err"
            elseif startswith(s, "✓")
                body = "  " * s; key = "ok"
            else
                body = "  " * s; key = "dim"
            end
            for ln in _mr_wrap(body, W)
                println(_mr_c("│", "title") * _mr_c(_mr_fit(ln, W), key) *
                        _mr_c("│", "title"))
            end
        end
        println(_mr_c("╰" * "─"^W * "╯", "title"))
        flush(stdout)
    catch
        println("── ", title, " ──")
        for r in rows; println("  ", r); end
    end
    return nothing
end

mutable struct MiniTestState
    id::Int; slug::String; title::String
    status::String; headline::String
    rows::Vector{Tuple{String,Bool,String}}
    notes::Vector{String}; plots::Vector{RepPlot}
    console::String
    comp_lo::Int; comp_hi::Int
    pngs::Vector{String}
end

Base.@kwdef mutable struct RepStateMini
    current::Union{Nothing,MiniTestState} = nothing
end
const REP = RepStateMini()
const ALL_STATES = Vector{MiniTestState}()

const COMP_LINES = Vector{String}()
const RESULT_LINES = Vector{String}()
const _LAST_LOG_LINE_REF = Ref{String}("")
last_log_line() = _LAST_LOG_LINE_REF[]
_prog_now_str() = Dates.format(Dates.now(), "yyyy-mm-dd HH:MM:SS")
function _prog_hms(s::Real)
    s = max(0, round(Int, s))
    return @sprintf("%02d:%02d:%02d", s ÷ 3600, (s % 3600) ÷ 60, s % 60)
end
const _PROG_LABEL = Ref{String}("HP")
const _PROG_T0 = Ref{Float64}(time())
const _PROG_LAST = Ref{Float64}(-1.0)
const _PROG_LAST_T = Ref{Float64}(-1.0)   # wall clock of the last DRAWN bar frame
const _PROG_TAG = Ref{String}("")         # live phase tag (e.g. "LAPACK eigvals 12000×12000: 300 s")
const _LIVE_FD = Ref{Cint}(-1)            # while a report tee is active: dup of the REAL stdout fd
const _LIVE_DRAWN = Ref{Bool}(false)      # an in-place bar frame currently sits on the live line
const _HEARTBEAT = Ref{Union{Nothing, Base.Process}}(nothing)

"""Is the real stdout a terminal? (Checked on the ORIGINAL stdout object —
the report tee re-points the fd at the OS level, but the TTY identity still
answers for the same underlying device.) v24.1: Base.isatty was REMOVED in
Julia 1.12 — the old try/catch silently answered FALSE there and demoted the
live bar to append-only lines. The check is now the TTY type itself, with
legacy isatty as the fallback and IOContext unwrapping (1.12 wraps stdout)."""
function _mr_istty(io::IO)::Bool
    try
        io isa IOContext ? _mr_istty(io.io) :
        io isa Base.TTY ? true :
        isdefined(Base, :isatty) ? Base.isatty(io)::Bool : false
    catch
        false
    end
end
_prog_tty() = _mr_istty(stdout)

prog_tag!(s::AbstractString) = (_PROG_TAG[] = String(s); nothing)

"""Direct-to-terminal write that BYPASSES the report tee. While
rep_tee_stdout has fd 1 pointed at the capture temp file (fd-level dup2 —
the only deadlock-free capture on a single thread), _LIVE_FD holds a dup of
the REAL terminal fd and a raw write() reaches the screen instantly. This is
what makes the progress bar visible DURING a multi-hour gate instead of
being replayed from the capture when the gate is already over."""
function _live_write(s::String)
    fd = _LIVE_FD[]
    if fd >= 0
        b = codeunits(s)
        nb = sizeof(s)
        off = 1
        while off <= nb # robust partial-write loop (a tty can short-write)
            w = ccall(:write, Cssize_t, (Cint, Ptr{UInt8}, Csize_t),
                      fd, pointer(b, off), nb - off + 1)
            w <= 0 && break
            off += w
        end
    else
        print(stdout, s)
        flush(stdout)
    end
    return
end

function log_comp(msg::String)
    push!(COMP_LINES, @sprintf("[%s]  %s", _prog_now_str(), msg))
    return nothing
end

function log_result(s::String)
    push!(RESULT_LINES, s)
    _LAST_LOG_LINE_REF[] = s
    return nothing
end

const TEST_META = Dict{Int,Tuple{String,String,String}}()
const SLUGS = Dict{Int,String}()
msg(cfg, key::String) = key == "pass" ? "PASS" : key == "warn" ? "WARN" :
                         key == "fail" ? "FAIL" : key

"""LIVE progress bar (v23.8). Draws IN PLACE on a terminal (\r + erase-to-EOL)
through the tee-bypassing _live_write channel, so it is visible while the gate
runs — not replayed after it. Updates are TIME-throttled (≥ 0.8 s between
frames), so the ≤ 40-solve H5 (v24.1 budget) draws one frame per solve
instead of being silenced by the old 2%-step rule. Shows elapsed,
ETA (linear extrapolation from frac) and the current sub-step text."""
function prog_update(frac::Real, extra::AbstractString = "")
    f = clamp(Float64(frac), 0.0, 1.0)
    now = time()
    first = _PROG_LAST[] < 0
    (first || f >= 1.0 || (f != _PROG_LAST[] && now - _PROG_LAST_T[] >= 0.8)) || return
    _PROG_LAST[] = f
    _PROG_LAST_T[] = now
    el = now - _PROG_T0[]
    eta = 0.02 < f < 1.0 ? el * (1.0 - f) / f : NaN
    pct = clamp(round(Int, 100f), 0, 100)
    full = pct ÷ 10
    body = string(
        _mr_c("▰"^full * "▱"^(10 - full), "accent"), " ",
        _mr_c(@sprintf("%5.1f%%", 100f), "bold"), " ",
        _mr_c(_PROG_LABEL[], "title"),
        _mr_c(" · T+" * _prog_hms(el), "dim"),
        isnan(eta) ? "" : _mr_c(" · ETA " * _prog_hms(eta), "dim"),
        isempty(_PROG_TAG[]) ? "" : _mr_c(" · " * _PROG_TAG[], "warn"),
        isempty(extra) ? "" : _mr_c(" · " * extra, "gold"))
    if _prog_tty()
        _live_write("\r\033[K  " * body) # in-place redraw: one line, always current
        _LIVE_DRAWN[] = true
    else
        _live_write("  " * body * "\n") # non-tty (file/pipe): append-only lines
    end
    return
end

function ab_gc!()
    GC.gc(true); GC.gc(true)
    try
        ccall((:malloc_trim, "libc"), Cint, (Csize_t,), 0)
    catch
    end
    return nothing
end

function rep_begin!(id::Int, title::String)
    global _PROG_LAST[] = -1.0
    global _PROG_LAST_T[] = -1.0
    global _PROG_T0[] = time()
    global _PROG_TAG[] = ""
    REP.current = MiniTestState(id, get(SLUGS, id, @sprintf("test_%d", id)), title,
                                "RUN", "", Tuple{String,Bool,String}[], String[],
                                RepPlot[], "", length(COMP_LINES) + 1,
                                length(COMP_LINES), String[])
    return
end

function rep_finish!(id::Int, verdict::String, headline::String)
    rt = REP.current
    rt === nothing && return
    rt.status = verdict
    rt.headline = headline
    rt.comp_hi = length(COMP_LINES)
    return
end

rep_plot!(p::RepPlot) = (REP.current !== nothing && push!(REP.current.plots, p); p)
rep_note!(s::String) = (REP.current !== nothing && push!(REP.current.notes, s); nothing)

"""fd number of a stdout-like stream, version-proof (v24.1 hotfix). Julia 1.12
REMOVED Base.fd for Libuv streams (methods remain only for IOStream / File /
Sockets) — on a real terminal stdout is a Base.TTY, so the old Base.fd(orig)
crashed EVERY gate in 00:00:00 with «MethodError: no method matching
fd(::Base.TTY)» (user device, 2026-09-09). Recovery chain: unwrap IOContext →
Base.fd (IOStream/File; TTY also on older Base) → uv_fileno on the TTY's own
uv handle. Julia may bind the TTY handle to a dup'd fd (13/15 — measured),
which is fine: we resolve the fd of the SAME object Julia writes through, so
the number never has to be 1."""
function _mr_fdof(io::IO)::Cint
    io isa IOContext && return _mr_fdof(io.io) # color/lock wrappers first — the fallback must see the raw stream
    try
        v = Base.fd(io) # Int (Base ≤ 1.11) · RawFD primitive (1.12 — no fields, reinterpret it)
        return v isa Base.Libc.RawFD ? reinterpret(Cint, v) : Cint(v)
    catch
        Sys.iswindows() && rethrow() # Windows HANDLE-sized fds — out of scope
        io isa Base.TTY || rethrow()
        r = Ref{Cint}(0)
        rc = ccall(:uv_fileno, Cint, (Ptr{Cvoid}, Ptr{Cint}), io.handle, r)
        rc == 0 || error("uv_fileno failed on stdout TTY (rc=$rc)")
        return r[]
    end
end

"""Capture stdout during a test at the FILE-DESCRIPTOR level (dup2): the
runner's prints keep going to the same fd NUMBER Julia's stdout stream holds,
but that number now points at a temp file. No pipes, no reader tasks — the
pipe+task tee deadlocks single-threaded (the reader only gets scheduled when
the writer yields, and LAPACK eigen-solves never yield — measured). The
flush(orig) in finally DRAINS Julia's async uv write queue into the file
before we restore the fd and read the capture back."""
function rep_tee_stdout(thunk::Function)
    orig = stdout
    tmppath, io = mktemp()
    val = nothing; threw = nothing; cap = "" # pre-init: variables assigned ONLY in `finally` are NOT visible after the try block (Julia scoping, measured)
    ofd = _mr_fdof(orig) # the fd number Julia's stdout writes to (v24.1: 1.12-safe — Base.fd(::TTY) is gone)
    ffd = _mr_fdof(io)
    saved_fd = ccall(:dup, Cint, (Cint,), ofd)
    _LIVE_FD[] = saved_fd # LIVE ESCAPE HATCH: this dup still points at the REAL
    # terminal, so prog_update/_live_write reach the screen DURING the test while
    # fd 1 itself is pointed at the capture file below.
    ccall(:dup2, Cint, (Cint, Cint), ffd, ofd)
    try
        val = thunk()
    catch err
        threw = err
    finally
        try; flush(orig); catch; end # drain the ios/uv write queue → into the temp file
        # Close the live bar's line + shut the escape channel BEFORE the replay,
        # so the captured report starts on a fresh line under the final frame.
        _LIVE_DRAWN[] && _live_write("\n")
        _LIVE_DRAWN[] = false
        _LIVE_FD[] = -1
        try; ccall(:fsync, Cint, (Cint,), ofd); catch; end
        try; ccall(:dup2, Cint, (Cint, Cint), saved_fd, ofd); catch; end
        try; ccall(:close, Cint, (Cint,), saved_fd); catch; end
        try; close(io); catch; end
        try; cap = read(tmppath, String); catch; cap = ""; end
        print(orig, cap)
        flush(orig)
        rm(tmppath; force = true)
    end
    threw === nothing || throw(threw)
    cap = _mr_strip_ansi(cap) # file reports stay plain; the screen got the color
    return val, cap
end

"""Verdict table (the suite's hc_verdict_table, compact): prints the rows,
logs the aggregate line, stores the rows for the master report. Returns true
iff every row passed."""
function hc_verdict_table(cfg, label::String, rec::Vector{Tuple{String,Bool,String}};
                          pass_label::String = "PASS")
    n_fail = count(!r[2] for r in rec)
    status = n_fail == 0 ? "PASS" : "WARN"
    _mr_panel(label * "  ·  " * string(length(rec)) * " sub-checks → " * status,
              [(r[2] ? "✓ " : "! ") * r[1] * " — " * r[3] for r in rec])
    log_result(@sprintf(" %s [%s]: %d sub-checks, %d failed → %s",
                        label, pass_label, length(rec), n_fail, status))
    REP.current !== nothing && append!(REP.current.rows, rec)
    return n_fail == 0
end

# ═════════════════════════════════════════════════════════════════════════════
# §3. STANDALONE CONFIG — the exact cfg.* slice the H1–H7 runners touch,
#     with the SUITE launch defaults (so numbers match the suite runs)
# ═════════════════════════════════════════════════════════════════════════════

mutable struct HPConfig
    hp_L::Int; hp_n_ensemble::Int; hp_n_q_grid::Int
    hp_q_min::Float64; hp_q_max::Float64; hp_primes::Vector{Int}
    hp_t_max::Float64; hp_dt::Float64; hp_h1_configs::Int; hp_zeta_cap::Int
    hp_L_ladder::Vector{Int}; hp_L_weyl::Int; hp_weyl_grid::Int
    hp_jitter_trials::Int; hp_pos_jitter::Float64; hp_alpha_jitter::Float64
    hp_n_gue_calib::Int; hp_seed::Int; hp_gue_band::Float64
    hp_pass_fraction::Float64; hp_regime_mode::Symbol
    hp_deep_nulls::Int; hp_deep_configs::Int
    hp_alpha_scan::Bool; hp_alpha_scan_n::Int
    # AB physics constants (suite defaults)
    ab_t::Float64; ab_center_fraction::Float64; ab_alpha_test16::Float64
    ab_K_smooth_window::Int; ab_n_realizations::Int
    ab_W::Float64; ab_W_max::Float64
    ab_nv_list::Vector{Int}; ab_q_list::Vector{Float64}; gue_matrix_size::Int
end

function make_hp_config()::HPConfig
    return HPConfig(
        56, 40, 21, 0.05, 1.0, [2, 3, 5, 7, 11, 13], 40.0, 0.025, 3, 20_000,
        [28, 36, 44, 52, 60], 56, 60, 12, 0.35, 0.02, 5, 2026, 0.022, 0.90,
        :showdown, 20, 10, true, 40,
        1.0, 0.6, 0.5, 3, 5, 4.0, 1.0, [4], [1.0], 12_000)
end

ab_w_eff(cfg::HPConfig) = min(cfg.ab_W, cfg.ab_W_max)

function resolve_vortex_count(cfg::HPConfig; pass::Symbol = :primary)::Int
    cfg.gue_matrix_size == 0 && return 4
    return isempty(cfg.ab_nv_list) ? 4 : cfg.ab_nv_list[1]
end

resolve_q_magnitude(cfg::HPConfig)::Float64 = isempty(cfg.ab_q_list) ? 1.0 : cfg.ab_q_list[1]

function params_banner(cfg::HPConfig)
    _mr_section("parameters")
    _mr_kv("lattice",   "L=$(cfg.hp_L)  ($(cfg.hp_L)² = $(cfg.hp_L^2) sites)")
    _mr_kv("α / W_eff", @sprintf("%.4f / %.2f", cfg.ab_alpha_test16, ab_w_eff(cfg)))
    _mr_kv("ensemble",  "$(cfg.hp_n_ensemble) configs · seed $(cfg.hp_seed)")
    _mr_kv("deep",      "nulls=$(cfg.hp_deep_nulls) · configs=$(cfg.hp_deep_configs)")
    _mr_kv("α-profile", (cfg.hp_alpha_scan ? "ON" : "OFF") *
                        " (n=$(cfg.hp_alpha_scan_n)) · sweep=:$((cfg.hp_regime_mode))")
    _mr_kv("primes",    join(cfg.hp_primes, ",") *
                        "  |  q-grid $(cfg.hp_n_q_grid) pts on " *
                        "[" * @sprintf("%.2f", cfg.hp_q_min) * ", " *
                        @sprintf("%.2f", cfg.hp_q_max) * "]")
    _mr_kv("ladder",    join(cfg.hp_L_ladder, " → ") *
                        "  |  t_max=" * @sprintf("%.0f", cfg.hp_t_max) *
                        " · dt=" * @sprintf("%.3f", cfg.hp_dt))
    return
end

# ═════════════════════════════════════════════════════════════════════════
# §4. STATISTICS CORE — verbatim lifts from ab_cloud_v23_v2.jl (v23.6)
#     (equal seeds ⇒ bit-for-bit equal numbers with the suite)
# ═════════════════════════════════════════════════════════════════════════

const _LANCZOS_G = 7
const _LANCZOS_COEF = (
 0.99999999999980993, 676.5203681218851, -1259.1392167224028,
 771.32342877765313, -176.61502916214059, 12.507343278686905,
 -0.13857109526572012, 9.9843695780195716e-6, 1.5056327351493116e-7,
)

"""Lanczos approximation of ln(Γ(x)) for x > 0 (reflection formula for x < 0.5)."""
function lgamma_lanczos(x::Float64)::Float64
 if x < 0.5
 return log(π / sin(π * x)) - lgamma_lanczos(1.0 - x)
 end
 x -= 1.0
 a = _LANCZOS_COEF[1]
 t = x + _LANCZOS_G + 0.5
 for i in 1:(_LANCZOS_G + 1)
 a += _LANCZOS_COEF[i+1] / (x + i)
 end
 return 0.5 * log(2π) + (x + 0.5) * log(t) - t + log(a)
end

"""Regularized lower incomplete gamma P(a,x) via series expansion (valid x < a+1)."""
function _gammp_series(a::Float64, x::Float64)::Float64
 ap = a
 total = 1.0 / a
 δ = total
 for _ in 1:200
 ap += 1.0
 δ *= x / ap
 total += δ
 abs(δ) < abs(total) * 1e-15 && break
 end
 return total * exp(-x + a * log(x) - lgamma_lanczos(a))
end

"""Regularized upper incomplete gamma Q(a,x) via Lentz continued fraction (valid x >= a+1)."""
function _gammq_cf(a::Float64, x::Float64)::Float64
 FPMIN = 1e-300
 b = x + 1.0 - a
 c = 1.0 / FPMIN
 d = 1.0 / b
 h = d
 for i in 1:200
 an = -i * (i - a)
 b += 2.0
 d = an * d + b
 abs(d) < FPMIN && (d = FPMIN)
 c = b + an / c
 abs(c) < FPMIN && (c = FPMIN)
 d = 1.0 / d
 δ = d * c
 h *= δ
 abs(δ - 1.0) < 1e-15 && break
 end
 return exp(-x + a * log(x) - lgamma_lanczos(a)) * h
end

"""Regularized lower incomplete gamma P(a,x) = γ(a,x)/Γ(a), any a>0, x>=0."""
function regularized_gamma_p(a::Float64, x::Float64)::Float64
 x <= 0.0 && return 0.0
 return x < a + 1.0 ? _gammp_series(a, x) : 1.0 - _gammq_cf(a, x)
end

"""Exact χ² CDF for ANY (not just even) degrees of freedom df."""
chi2_cdf(x::Float64, df::Real)::Float64 = regularized_gamma_p(Float64(df) / 2.0, x / 2.0)

function ks_asymptotic_pvalue(λ::Float64)::Float64
 λ <= 0.0 && return 1.0
 # Small-λ branch (dual theta series). The alternating series
 # 2·Σ(−1)^{k−1}·exp(−2k²λ²) needs ≈ 4.6/λ terms to converge; the hard
 # 100-term cap silently corrupted the p-value for λ ≲ 0.02 (e.g. λ=0.0015
 # returned p≈0.044 instead of the exact p≈1.0 — a false rejection of a
 # PERFECTLY consistent sample). For λ < 0.6 use the complementary
 # (Poisson-summation) form instead, which converges in a handful of terms:
 #   P(D > λ) = 1 − (√(2π)/λ)·Σ_{k≥1} exp(−(2k−1)²π²/(8λ²)).
 # Validated against scipy.stats.kstwobign.sf across λ ∈ [1e-4, 10].
 if λ < 0.6
     s2 = 0.0
     for k in 1:1000
         term2 = exp(-((2k - 1)^2 * π^2) / (8 * λ^2))
         s2 += term2
         term2 < 1e-18 && break
     end
     return clamp(1.0 - sqrt(2π) / λ * s2, 0.0, 1.0)
 end
 s = 0.0
 for k in 1:100
 term = (-1)^(k-1) * exp(-2 * k^2 * λ^2) # exponent is k²·λ², not (k·λ+λ)²
 s += term
 abs(term) < 1e-18 && break
 end
 return clamp(2.0 * s, 0.0, 1.0)
end

function ks_test(spacings::Vector{Float64}; cdf_func::Function=gue_cdf)
 n = length(spacings)
 sorted_sp = sort(spacings)
 D = 0.0
 for i in 1:n
 F_emp = i / n
 F_theory = cdf_func(sorted_sp[i])
 d = max(abs(F_emp - F_theory), abs((i-1)/n - F_theory))
 D = max(D, d)
 end
 # Use Stephens (1970) finite-sample correction
 # for better p-value accuracy on small samples. The simple sqrt(n)*D
 # formula is only asymptotically correct (n → ∞). Stephens' correction:
 # λ = (sqrt(n) + 0.12 + 0.11/sqrt(n)) * D
 # This matches what ks_test_2sample already uses and what SciPy uses.
 λ = (sqrt(n) + 0.12 + 0.11/sqrt(n)) * D
 pval = ks_asymptotic_pvalue(λ) #
 # log computation
 log_comp(@sprintf(" calc: KS D = %.6f, p_asymptotic = %.6e (n=%d, λ=%.4f)", D, pval, n, λ))
 return D, pval
end

goe_surmise_cdf(s::Float64) = 1.0 - exp(-π * s^2 / 4)

# v23.1: goe_surmise_pdf removed (its only caller, the gue_pdf overlay
# helper, was retired with the Plots.jl writers).

"""GUE (β=2) Wigner surmise CDF:
F₂(s) = erf(2s/√π) − (4s/π)·exp(−4s²/π); p₂(0)=0 (quadratic repulsion)."""
function gue2_surmise_cdf(s::Float64)::Float64
 s < 0 && return 0.0
 x2 = 4.0 * s^2 / π
 regularized_gamma_p(0.5, x2) - (4.0 * s / π) * exp(-x2)
end

"""GUE (β=2) Wigner surmise PDF: p₂(s) = (32/π²)·s²·exp(−4s²/π)."""
gue2_surmise_pdf(s::Float64) = (32.0 / π^2) * s^2 * exp(-4.0 * s^2 / π)


# gue_cdf — standalone wrapper. The suite dispatches to a 32 768-point
# interpolation table (|ΔF| ≤ 1e-9 vs the exact surmise); here the EXACT
# β=2 Wigner surmise is used directly — same law, difference ≪ statistical
# noise of any verdict.
gue_cdf(s::Float64)::Float64 = gue2_surmise_cdf(s)


function linreg(x::Vector{Float64}, y::Vector{Float64})
 n = length(x)
 mx = mean(x); my = mean(y)
 Sxx = sum((xi - mx)^2 for xi in x)
 Sxy = sum((xi - mx) * (yi - my) for (xi, yi) in zip(x, y))
 # Protect against Sxx == 0 (all x identical) and n < 3
 if Sxx == 0.0 || n < 2
 return 0.0, 0.0, 0.0, NaN, zeros(Float64, n)
 end
 b = Sxy / Sxx
 a = my - b * mx
 residuals = [yi - (a + b * xi) for (xi, yi) in zip(x, y)]
 ss_res = sum(r^2 for r in residuals)
 ss_tot = sum((yi - my)^2 for yi in y)
 R2 = ss_tot > 0 ? 1.0 - ss_res / ss_tot : 0.0
 # se_b requires n > 2 (else n-2 ≤ 0 → negative sqrt domain)
 se_b = (n > 2 && Sxx > 0) ? sqrt(ss_res / ((n-2) * Sxx)) : NaN
 return a, b, R2, se_b, residuals
end

function polyfit(x::Vector{Float64}, y::Vector{Float64}, deg::Int)::Vector{Float64}
 n = length(x)
 V = Matrix{Float64}(undef, n, deg + 1)
 for i in 1:n, j in 0:deg
 V[i, j+1] = x[i]^j
 end
 return V \ y
end

function polyval(coef::Vector{Float64}, x::Float64)::Float64
 s = 0.0
 for j in 0:(length(coef)-1)
 s += coef[j+1] * x^j
 end
 return s
end

function gue_matrix_eigenvalues(N::Int; seed::Int=42)::Vector{Float64}
 # Use LOCAL RNG instead of default_rng() + seed! — was
 # polluting the global default_rng() state for subsequent tests.
 rng = MersenneTwister(seed)
 # FIX 2026-09-02c: name the silent phase honestly — one blocking LAPACK
 # eigensolve produces NO output until it returns, which is exactly the
 # "зависает на тесте 11" look. State the ETA, the RAM and the override.
 N ≥ 8000 && begin
  _mr_warn("Large GUE reference: " * string(N) * "x" * string(N) *
           " complex matrix ≈ " * @sprintf("%.1f", N * N * 16 / 2^30) *
           " GB + LAPACK workspace — ONE silent LAPACK eigensolve, NO output until done, NOT a hang (O(N³), ≈ " *
           @sprintf("%.0f", max(1, round((N / 8000)^3 * 2.2))) * " min).")
  _mr_info("Lower it via the parameter editor (gue_matrix_size) if needed.")
 end
 G = Matrix{ComplexF64}(undef, N, N)
 rv = reinterpret(Float64, vec(G))
 randn!(rng, view(rv, 1:2:length(rv))) # real parts (same seeded stream)
 randn!(rng, view(rv, 2:2:length(rv))) # imaginary parts
 G ./= sqrt(2.0) # entries: re, im ~ N(0, 1/2) — matches (R + i·I)/√2
 # In-place Hermitian symmetrization A = (G + G†)/2 — no temporaries, no
 # broadcast-aliasing hazard: upper triangle consumes the lower, lower
 # mirrors the upper, diagonal collapses to Re(G_jj) — exactly what the
 # old two-copy version computed (up to the new draw order above).
 @inbounds for j in 1:N, i in (j+1):N
  G[j, i] = (G[j, i] + conj(G[i, j])) / 2
  G[i, j] = conj(G[j, i])
 end
 @inbounds for j in 1:N # (G_jj + conj(G_jj))/2 = Re(G_jj) exactly
  G[j, j] = complex(real(G[j, j]), 0.0)
 end
 # FIX 2026-09-02c: live ticker over the blocking eigvals call. Julia's
 # scheduler is cooperative — a ccall monopolizes its thread, so the ticker
 # can only run when ≥ 2 threads exist; on a 1-thread run the pre-solve
 # advisory above is the honest fallback. TTY: refreshes the bar's phase
 # tag every 2 s; non-TTY: one line per 60 s into the tee/report.
 tick_t0 = time()
 tick_stop = Ref{Bool}(false)
 local tick_task = nothing
 if Threads.nthreads() > 1 && N ≥ 4000
  tick_task = Threads.@spawn begin
   last_line = 0.0
   while !tick_stop[]
    sleep(2.0)
    tick_stop[] && break
    el = time() - tick_t0
    if _prog_tty()
     prog_tag!(@sprintf("LAPACK eigvals %dx%d: %.0f s (NOT a hang)", N, N, el))
    elseif el - last_line ≥ 60.0
     last_line = el
     _mr_warn("GUE diag still running: " * @sprintf("%.0f", el) *
              " s elapsed (one silent LAPACK phase, NOT a hang)")
    end
   end
  end
 end
 ev = try
  eigvals(Hermitian(G)) # LAPACK solver overwrites G in place
 finally
  tick_stop[] = true
  tick_task === nothing || wait(tick_task) # bounded by the 2 s sleep
  prog_tag!("") # the LAPACK phase tag must not leak into later bar frames
 end
 G = nothing
 GC.gc()
 return ev
end

function smooth_counting_function(T::Float64)::Float64
 T <= 0.0 && return 0.0
 x = T / (2π)
 return x * log(x) - x + 7.0/8.0
end

function random_vortex_configuration(Nv::Int, Nx::Int, Ny::Int;
 q_magnitude::Float64=1.0,
 enforce_neutrality::Bool=true,
 rng=default_rng(),
 place_at_centers::Bool=false)
 vortices = Vector{Vortex}(undef, Nv)
 for k in 1:Nv
 if place_at_centers
 # Place at center of a random plaquette (ix+0.5, iy+0.5)
 # Avoid the boundary plaquettes to keep the Dirac string well-defined.
 # OFF-BY-ONE FIX: the old `1 + rand(1:Nx-1)` sampled ix ∈ 2..Nx →
 # x ∈ 2.5..Nx+0.5, i.e. the LAST "plaquette" stuck out past the right
 # edge (x = Nx+0.5 is the boundary, not a plaquette center) and the
 # leftmost plaquette (x = 1.5) could never be drawn. Plaquette centers
 # of an Nx-column lattice are ix+0.5 for ix ∈ 1..Nx-1.
 ix = rand(rng, 1:Nx-1)
 iy = rand(rng, 1:Ny-1)
 x = Float64(ix) + 0.5
 y = Float64(iy) + 0.5
 else
 x = Nx * (0.5 + 0.4 * (rand(rng) - 0.5)) # avoid lattice edges
 y = Ny * (0.5 + 0.4 * (rand(rng) - 0.5))
 end
 # Odd-Nv charge assignment. With enforce_neutrality=true and
 # an EVEN Nv the split is exactly Nv/2 vs Nv/2 (net charge 0). The old code
 # fell through to a RANDOM ±q draw when Nv is odd — the net charge then
 # performed a random walk of size ±√Nv across realizations (e.g. preset_full
 # uses Nv=25: net charge varied 0,±2,±4,… run to run, silently changing the
 # vortex potential between realizations). True neutrality is impossible for
 # odd Nv with equal |q|, so we now use the DETERMINISTIC minimal-imbalance
 # split ⌈Nv/2⌉ vs ⌊Nv/2⌋ (|net| = 1, fixed) — reproducible and unbiased.
 q = if enforce_neutrality && iseven(Nv)
 k ≤ Nv ÷ 2 ? q_magnitude : -q_magnitude
 elseif enforce_neutrality && isodd(Nv)
 k ≤ (Nv + 1) ÷ 2 ? q_magnitude : -q_magnitude # 13 vs 12, |net|=1
 else
 rand(rng, [-q_magnitude, +q_magnitude])
 end
 vortices[k] = Vortex(x, y, q)
 end
 return vortices
end

const R_MEAN_POISSON = 2 * log(2) - 1 # ≈ 0.38629
const R_MEAN_GOE = 0.5307 # (Atas et al. 2013, exact)
const R_MEAN_GUE = 0.59960 # (Atas et al. 2013, exact)

function compute_K_form_factor(eigs::AbstractVector{<:Real},
 t_values::AbstractVector{<:Real};
 smooth_window::Int=3,
 preserve_ramp::Bool=true,
 ramp_threshold::Float64=0.5,
 eigs_per_seed::Int=0)
 n = length(eigs)
 n < 10 && return zeros(Float64, length(t_values))
 if eigs_per_seed > 0 && n > eigs_per_seed
 n_seeds_actual = n ÷ eigs_per_seed
 K_sum = zeros(Float64, length(t_values))
 K_count = 0
 for s in 0:(n_seeds_actual - 1)
 i_start = s * eigs_per_seed + 1
 i_end = min((s + 1) * eigs_per_seed, n)
 if i_end - i_start < 10
 continue
 end
 K_seed = _compute_K_single_seed(eigs[i_start:i_end], t_values;
 smooth_window=smooth_window,
 preserve_ramp=preserve_ramp,
 ramp_threshold=ramp_threshold)
 K_sum .+= K_seed
 K_count += 1
 end
 if K_count > 0
 return K_sum ./ K_count
 end
 end
 return _compute_K_single_seed(eigs, t_values;
 smooth_window=smooth_window,
 preserve_ramp=preserve_ramp,
 ramp_threshold=ramp_threshold)
end

function _compute_K_single_seed(eigs::AbstractVector{<:Real},
 t_values::AbstractVector{<:Real};
 smooth_window::Int=3,
 preserve_ramp::Bool=true,
 ramp_threshold::Float64=0.5)
 n = length(eigs)
 n < 10 && return zeros(Float64, length(t_values))
 s = sort(Float64.(eigs))
 n_pts = length(s)
 window = max(3, round(Int, n_pts * 0.05))
 unfolded = zeros(Float64, n_pts)
 unfolded[1] = 0.0
 @inbounds for i in 2:n_pts
 i_lo = max(1, i - window)
 i_hi = min(n_pts, i + window)
 local_eigs = s[i_lo:i_hi]
 local_density = length(local_eigs) / (local_eigs[end] - local_eigs[1] + 1e-12)
 unfolded[i] = unfolded[i-1] + (s[i] - s[i-1]) * local_density
 end
 mean_spacing = (unfolded[end] - unfolded[1]) / (n_pts - 1)
 if mean_spacing > 1e-12
 unfolded ./= mean_spacing
 end
 K = zeros(Float64, length(t_values))
 @inbounds for (idx, t) in enumerate(t_values)
 if t == 0.0
 K[idx] = 0.0
 continue
 end
 phase = 2π * t * unfolded
 ph = exp.(im .* phase)
 # NO "-1" here. For ABSOLUTE unfolded positions (mean spacing
 # 1, spanning [0, n]) the analytic GUE form factor is K(τ) = 1 − tri(τ)
 # (tri = triangle on [0,1]) — i.e. the ramp K=τ for τ≤1 and the plateau
 # K=1 for τ≥1 arise from (1/n)|Σ|² DIRECTLY. Subtracting 1 (the
 # self-pair count for CENTERED positions) clipped the whole ramp to 0
 # (measured: K ≈ 0 at every t, RMS vs min(t,1) = 0.63).
 K[idx] = max(0.0, abs2(sum(ph)) / n)
 end
 if length(K) > 2 * smooth_window
 K_smoothed = copy(K)
 @inbounds for i in (smooth_window+1):(length(K) - smooth_window)
 if preserve_ramp && t_values[i] < ramp_threshold
 continue
 end
 K_smoothed[i] = mean(K[(i - smooth_window):(i + smooth_window)])
 end
 K = K_smoothed
 end
 return K
end

# ═════════════════════════════════════════════════════════════════════════
# §5. PHYSICS CORE — AB-cloud Hamiltonian etc. (verbatim lifts)
# ═════════════════════════════════════════════════════════════════════════

struct Vortex
 x::Float64
 y::Float64
 q::Float64
end

struct ABCloudConfig
 Nx::Int
 Ny::Int
 vortices::Vector{Vortex}
 alpha::Float64
 t::Float64
 lattice::Symbol
 W::Float64 # diagonal disorder strength (monograph: W=4)
 disorder_seed::Int # RNG seed for residual ε
 vortex_phase_model::Symbol # :monumental (default) | :dirac (legacy)
end

ABCloudConfig(Nx::Int, Ny::Int, vortices::Vector{Vortex}, alpha::Float64,
 t::Float64, lattice::Symbol, W::Float64) =
 ABCloudConfig(Nx, Ny, vortices, alpha, t, lattice, W, 96, :monumental)
 # 8-arg form defaults model=:monumental
ABCloudConfig(Nx::Int, Ny::Int, vortices::Vector{Vortex}, alpha::Float64,
 t::Float64, lattice::Symbol, W::Float64, disorder_seed::Int) =
 ABCloudConfig(Nx, Ny, vortices, alpha, t, lattice, W, disorder_seed, :monumental)

function ab_phase_vortex_monumental(ri::Tuple{Float64,Float64}, rj::Tuple{Float64,Float64},
 vortices::Vector{Vortex})::Float64
 phase = 0.0
 for vk in vortices
 dx1 = ri[1] - vk.x
 dy1 = ri[2] - vk.y
 dx2 = rj[1] - vk.x
 dy2 = rj[2] - vk.y
 arg1 = (dx1 != 0 || dy1 != 0) ? atan(dy1, dx1) : 0.0
 arg2 = (dx2 != 0 || dy2 != 0) ? atan(dy2, dx2) : 0.0
 phase += vk.q * (arg2 - arg1) * 0.5
 end
 return phase
end

function vortex_onsite_potential(ri::Tuple{Float64,Float64},
 vortices::Vector{Vortex},
 W::Float64, N::Int,
 rng=MersenneTwister(96))::Float64
 # Clean-lattice fast path: if no vortices AND no disorder,
 # return 0 exactly — preserves chiral symmetry at α=1/2 (Test 33).
 if isempty(vortices) && W == 0.0
 return 0.0
 end
 v = 0.0
 ninv = 1.0 / max(N, 1)
 for vk in vortices
 dx = ri[1] - vk.x
 dy = ri[2] - vk.y
 r2 = dx*dx + dy*dy
 v += vk.q * W / (r2 * ninv + 1.0)
 end
 # residual ε ~ U(-0.01, 0.01) (only if W > 0)
 if W > 0
 v += (rand(rng) - 0.5) * 0.02
 end
 return v
end


# :dirac stub — the HP audits run ONLY :monumental (see every ABCloudConfig
# construction in the H-runners); lift the real ab_phase_2d_full from the
# suite if a :dirac experiment is ever added here.
function ab_phase_2d_full(ri, rj, rk, qk; torus=false, Nx=0)
    error("ab_phase_2d_full: :dirac phase model is not part of the HP standalone (all audits run :monumental)")
end


function build_ab_cloud_hamiltonian(cfg::ABCloudConfig)
 Nx, Ny = cfg.Nx, cfg.Ny
 N = Nx * Ny
 H = zeros(ComplexF64, N, N)
 α = cfg.alpha
 t = cfg.t
 vortices = cfg.vortices
 torus = (cfg.lattice === :torus)
 W = cfg.W # diagonal disorder strength
 # vortex phase model selection
 model = cfg.vortex_phase_model
 @assert model === :monumental || model === :dirac "vortex_phase_model must be :monumental or :dirac, got $model"
 # log this Hamiltonian build to COMP_LOG
 log_comp(@sprintf(" build_ab_cloud_hamiltonian: %dx%d (N=%d), α=%.4f, t=%.2f, W=%.2f, %s, %d vortices, model=:%s",
 Nx, Ny, N, α, t, W, torus ? "torus" : "open", length(vortices), model))

 # For torus geometry, magnetic translation consistency requires α·Ny ∈ ℤ.
 # CLEANED 2026-08-31 (audit fix №2): the old clamp chain also accepted
 # HALF-integer α·Ny (the ±0.5 clauses — an anti-periodic up-wrap that breaks
 # magnetic translations and contradicted this function's own docstring);
 # the ±1/±2/±0.0 clauses were dead code (|frac(α·Ny)| ≤ 0.5 always). All
 # current call sites produce integer α·L (Т29 snaps α to m/L since Task 13),
 # so the contract is now the strict integer assert it always claimed to be.
 if torus
 @assert abs(α * Ny - round(α * Ny)) < 1e-10 "Torus geometry needs α·Ny ∈ ℤ (magnetic-translation consistency); got α·Ny = $(α*Ny). Snap α to m/Ny (Test 29's snap_alpha pattern) or use :open."
 end

 # Single RNG for reproducible on-site disorder ε
 # Must NOT be a fixed per-test constant: every realization of the Test 32
 # ⟨r⟩ bootstrap needs its OWN disorder pattern (that is the point of the
 # bootstrap). Uses cfg.disorder_seed; Test 32 varies it per-realization.
 rng_dis = MersenneTwister(cfg.disorder_seed)

 for iy in 1:Ny
 for ix in 1:Nx
 i = (iy - 1) * Nx + ix
 ri = (Float64(ix), Float64(iy))

 # --- Right neighbour ---
 jx = ix + 1
 jy = iy
 wrap = false
 if jx > Nx
 if torus
 jx = 1
 wrap = true
 else
 jx = 0 # sentinel: skip
 end
 end
 if jx != 0
 j = (jy - 1) * Nx + jx
 rj = (Float64(jx), Float64(jy))
 # Peierls phase (Landau gauge A = B·x̂·y):
 # φ_right = 2π·α·iy — the phase is proportional to the transverse Y
 # coordinate, so it is UNIFORM along X and the plaquette curl
 # (φ_right(iy+1) − φ_right(iy)) = 2π·α on EVERY plaquette.
 φ = 2π * α * iy
 # Vortex phase on x-hops:
 # - :dirac model — SMOOTH gauge part only (the explicit Dirac string lives
 #   on vertical bonds, so it contributes nothing here; kept explicit via
 #   ab_phase_2d_full for documentation symmetry — it returns 0 on x-hops).
 #   On the torus x-wrap bond pass the UNWRAPPED coordinate (Nx+1, iy) so
 #   the smooth polar angles stay continuous across the seam.
 # - :monumental model — NONE (Monumental puts vortex phases
 # on vertical bonds only; x-hops carry the pure Landau Peierls phase)
 if model === :dirac
 rj_phase = wrap ? (Float64(Nx + 1), Float64(iy)) : rj
 for v in vortices
 rk = (v.x, v.y)
 φ += ab_phase_2d_full(ri, rj_phase, rk, v.q; torus=torus, Nx=Nx)
 end
 end
 H[i, j] += -t * exp(im * φ)
 H[j, i] += -t * exp(-im * φ) # hermiticity
 end

 # --- Up neighbour ---
 jx = ix
 jy = iy + 1
 wrap = false
 if jy > Ny
 if torus
 jy = 1
 wrap = true
 else
 jy = 0 # sentinel: skip
 end
 end
 if jy != 0
 j = (jy - 1) * Nx + jx
 rj = (Float64(jx), Float64(jy))
 φ = 0.0 # vertical hopping has zero Peierls phase in Landau gauge
 if wrap
 φ += 2π * α * Ny
 end
 # Vortex phase on vertical bonds (model selection:
 if model === :monumental
 # Monumental atan smooth gauge. NOTE: for the torus wrap bond the
 # phase uses the UNWRAPPED top coordinate (ix, iy+1) — identical to
 # Monumental, which evaluates atan at y+1 (0-based, ≤ L) for wrap bonds.
 rj_phase = wrap ? (Float64(ix), Float64(iy + 1)) : rj
 φ += ab_phase_vortex_monumental(ri, rj_phase, vortices)
 else # :dirac — smooth polar-angle gauge + EXPLICIT Dirac string
 # (ab_phase_2d_full = ab_phase_2d + dirac_string_phase). This is the
 # formulation the Dirac-string flux theorems (Tests 15/24/26) are
 # stated for: the smooth part alone has zero curl, the explicit
 # right-going string localizes +2πq on the vortex plaquette and 0 on
 # every other plaquette (on the torus the string wraps and returns,
 # leaving the documented −2πq artifact one column left of the vortex).
 # The previous solid-angle (signed-area) form produced a POSITION-
 # INDEPENDENT uniform flux 4π·Σq on EVERY plaquette — the flux
 # theorems then passed only vacuously at integer q and FAILED at
 # fractional q (monograph Appendix A.1 formula — implementation
 # removed in the v19.1 audit, see the header historical note).
 # For the torus y-wrap bond pass the UNWRAPPED top coordinate
 # (ix, iy+1) — same discipline as the :monumental branch above.
 rj_phase = wrap ? (Float64(ix), Float64(iy + 1)) : rj
 for v in vortices
 rk = (v.x, v.y)
 φ += ab_phase_2d_full(ri, rj_phase, rk, v.q; torus=torus, Nx=Nx)
 end
 end
 H[i, j] += -t * exp(im * φ)
 H[j, i] += -t * exp(-im * φ)
 end

 # Diagonal disorder: vortex Coulomb potential + ε
 V_onsite = vortex_onsite_potential(ri, vortices, W, N, rng_dis)
 H[i, i] += V_onsite
 end
 end

 # Hermitian symmetrization: H → (H + H†)/2 (kills any imaginary leakage)
 H = (H + H') ./ 2
 GC.gc() # release the pre-hermitianization copy immediately

 return H # plain Matrix to avoid Julia 1.10.4 Hermitian eigvals bug
end

function central_band_eigs(sorted_eigs::Vector{Float64}, frac::Float64)::Vector{Float64}
 n = length(sorted_eigs)
 n == 0 && return Float64[]
 frac = clamp(frac, 0.05, 1.0)
 frac >= 1.0 && return copy(sorted_eigs) # old form dropped the top eig of an ODD-length spectrum at frac=1.0
 half = Int(fld(n * frac, 2))
 j_lo = max(1, fld(n, 2) - half)
 j_hi = min(n, fld(n, 2) + half)
 return sorted_eigs[j_lo:j_hi]
end

function ab_gc!()
 GC.gc(true); GC.gc(true)
 try
 ccall((:malloc_trim, "libc"), Cint, (Csize_t,), 0)
 catch
 end
 return nothing
end

function mean_adjacent_spacing_ratio(eigs::Vector{<:Real})::Tuple{Float64,Int}
 n = length(eigs)
 n < 3 && return (NaN, 0)
 sorted = sort(Float64.(eigs))
 deltas = [sorted[i+1] - sorted[i] for i in 1:(n-1)]
 n_r = length(deltas) - 1
 n_r <= 0 && return (NaN, 0)
 s = 0.0
 cnt = 0
 for i in 1:n_r
 a = deltas[i]
 b = deltas[i+1]
 m = max(a, b)
 # Robustness: guard 0/0 → NaN. Spectra with EXACT degeneracies
 # (e.g. |E| proxies of complex-conjugate pairs in the non-Hermitian Test 31,
 # or symmetry-protected degeneracies) contain zero spacings; the old code
 # computed min/max = 0/0 = NaN and poisoned the whole mean. Degenerate
 # pairs now contribute a ratio of 0 (their spacing ratio is genuinely 0),
 # identical spacings are skipped entirely.
 if a == 0.0 && b == 0.0
 continue # 0/0 — indeterminate, skip
 end
 s += min(a, b) / m
 cnt += 1
 end
 cnt <= 0 && return (NaN, 0)
 r_mean = s / cnt
 # log computation
 log_comp(@sprintf(" calc: ⟨r⟩ = %.6f (n_r=%d, n_eigs=%d) [refs: GUE=%.4f Poisson=%.4f]",
 r_mean, cnt, n, R_MEAN_GUE, R_MEAN_POISSON))
 return (r_mean, cnt)
end

# ═════════════════════════════════════════════════════════════════════════
# §6. HP AUDITS H1–H7 — verbatim lift of the v23.6 HP block
#     (helpers, regimes, H1 DEEPEN protocol, H5 α-profile, H4 domain guard)
# ═════════════════════════════════════════════════════════════════════════

struct HPAudit
    id::Int          # 301..307 (menu H1..H7; report/test_301_… directories)
    group::String    # "A".."D"
    slug::String
    title::String
    about::String    # one line in the menu
    detail::String   # printed before the run (physics explanation)
    runner::Function # hp_hNN(cfg, zeta_zeros)
end

const HP_AUDITS = HPAudit[]

"""Standard HP vortex configuration (same recipe as Test 35b: neutral set at
plaquette centers, suite-resolved Nv/q; the rng drives BOTH the placement and,
via the seed, the residual ε pattern)."""
function _hp_std_vortices(cfg::HPConfig, L::Int, rng::MersenneTwister)
    Nv = resolve_vortex_count(cfg)
    q_mag = resolve_q_magnitude(cfg)
    return Nv == 0 ? Vortex[] :
           random_vortex_configuration(Nv, L, L; q_magnitude = q_mag,
                                       enforce_neutrality = true, rng = rng,
                                       place_at_centers = true)
end

"""Standard HP ABCloudConfig. `alpha = NaN` → suite α (ab_alpha_test16).
`lattice` defaults to :open (launch standard, no torus α·L ∈ ℤ constraint —
H4/H6 deliberately scan/jitter α, which a torus would forbid)."""
function _hp_std_config(cfg::HPConfig, L::Int, seed::Int; lattice::Symbol = :open,
                        alpha::Float64 = NaN,
                        vortices::Union{Nothing,Vector{Vortex}} = nothing)
    α = isnan(alpha) ? cfg.ab_alpha_test16 : alpha
    v = vortices === nothing ? _hp_std_vortices(cfg, L, MersenneTwister(seed)) : vortices
    return ABCloudConfig(L, L, v, α, cfg.ab_t, lattice, ab_w_eff(cfg), seed, :monumental)
end

"""Build + full dense diagonalization (values only) with a progress-bar
heartbeat + computation log — the lab `_lab_spectrum` discipline."""
function _hp_spectrum(cfg::HPConfig, c::ABCloudConfig)
    log_comp(@sprintf(" heevr values-only solve: N=%d — _hp_spectrum (%dx%d, seed=%d)",
                      c.Nx * c.Ny, c.Nx, c.Ny, c.disorder_seed))
    return sort(real.(eigvals(Hermitian(build_ab_cloud_hamiltonian(c)))))
end

"""Local-mean unfolding (the SAME scheme compute_K_form_factor uses
internally): sliding window of `win_frac`·n points, cumulative density
integral, normalized to unit mean spacing. Returns unfolded positions
u ≈ [0, n] with uₙ − n = the fluctuation the H7 test correlates."""
function _hp_unfold_local(eigs::AbstractVector{<:Real}; win_frac::Float64 = 0.05)
    s = sort(Float64.(eigs))
    n = length(s)
    n < 10 && return collect(0.0:(n - 1))
    window = max(3, round(Int, n * win_frac))
    u = zeros(Float64, n)
    for i in 2:n
        i_lo = max(1, i - window)
        i_hi = min(n, i + window)
        local_density = (i_hi - i_lo + 1) / (s[i_hi] - s[i_lo] + 1e-12)
        u[i] = u[i - 1] + (s[i] - s[i - 1]) * local_density
    end
    mean_spacing = (u[end] - u[1]) / max(n - 1, 1)
    mean_spacing > 1e-12 && (u ./= mean_spacing)
    return u
end

"""Connected GUE envelope used by H1 (Test-35 convention): the finite-box
reference K_box(t) = t·(1 − sinc(2πt)) on the ramp region t < 1 (its cubic
small-t onset is the level-repulsion curvature Test 35 verified to RMS 0.21)
and the universal plateau 1 for t ≥ 1. `sinc_norm(x) = sin(x)/x` (Test 35's
own normalized-sinc, NOT Julia's π-scaled sinc)."""
_hp_sinc_norm(x::Float64) = abs(x) < 1e-12 ? 1.0 : sin(x) / x
_hp_kgue_envelope(t::Float64) = t < 1.0 ? t * (1.0 - _hp_sinc_norm(2π * t)) : 1.0

"""Angular-frequency direct periodogram of a uniformly sampled residual
(values r at times ts; mean-removed, Hann-windowed) evaluated on an EXPLICIT
ω-grid — a Lomb-style scan, so no FFTW dependency and no frequency-grid
aliasing. P(ω) = |Σ wₖrₖe^{−iωtₖ}|²·2/Σwₖ² ≈ sinusoid-amplitude² at ω.
White noise of unit std → P ~ O(1) at every ω (the SNR yardstick is the
median of P over the scanned band, not a theoretical constant)."""
function _hp_periodogram(res::Vector{Float64}, ts::Vector{Float64},
                         ωgrid::Vector{Float64})
    n = length(res)
    n == 0 && return zeros(Float64, length(ωgrid))
    m = mean(res)
    r = res .- m
    w = [0.5 * (1.0 - cos(2π * (k - 1) / max(n - 1, 1))) for k in 1:n] # Hann
    sw2 = sum(abs2, w)
    sw2 > 1e-300 || (sw2 = 1.0)
    P = zeros(Float64, length(ωgrid))
    t0 = ts[1]
    for (fi, ω) in enumerate(ωgrid)
        acc_re = 0.0
        acc_im = 0.0
        @inbounds for k in 1:n
            ph = ω * (ts[k] - t0)
            wk = w[k] * r[k]
            acc_re += wk * cos(ph)
            acc_im -= wk * sin(ph)
        end
        P[fi] = 2.0 * (acc_re^2 + acc_im^2) / sw2
    end
    return P
end

"""H1 PRIMARY detector — raw-position 1-level Fourier transform (D1):
P(ω) = |Σₖ wₖ e^{−iωTₖ}|²/Σwₖ² over the RAW (never-unfolded) sorted positions
Tₖ with a Hann index window. The Riemann–Weil explicit formula makes the zero-
density fluctuation δρ(T) = −(1/π)Σ_{p,k}(log p)/p^{k/2}·cos(kT·log p) a sum of
PURE TONES in the raw ordinate T, so a spectrum carrying arithmetic information
shows Bragg peaks at ω = log p (and harmonics k·log p). Normalization by Σw²
makes white-noise phases → P ≈ 1; the SNR yardstick is P(log p)/median(P) over
the scanned band (empirically calibrated: ζ control 10⁶–10⁹, GUE/vortex-free
nulls ≤ 5). This is where the explicit formula LIVES — the two-level K(t)
residual route (D2, the reviewer's literal estimator) is retained as a
cross-check but is intrinsically less sensitive (the 1-level signal enters
the 2-level statistic only at subleading order)."""
function _hp_raw_ft(T::Vector{Float64}, ωgrid::Vector{Float64})
    n = length(T)
    n < 10 && return zeros(Float64, length(ωgrid))
    w = [0.5 * (1.0 - cos(2π * (k - 1) / max(n - 1, 1))) for k in 1:n]
    sw2 = sum(abs2, w)
    sw2 > 1e-300 || return zeros(Float64, length(ωgrid))
    P = zeros(Float64, length(ωgrid))
    for (fi, ω) in enumerate(ωgrid)
        acc_re = 0.0
        acc_im = 0.0
        @inbounds for k in 1:n
            acc_re += w[k] * cos(ω * T[k])
            acc_im -= w[k] * sin(ω * T[k])
        end
        P[fi] = (acc_re^2 + acc_im^2) / sw2
    end
    return P
end

"""K(t) residual for H1: measured form factor minus the analytic GUE
envelope, then a degree-`dpoly` polynomial detrend (removes the residual
slow plateau drift; a quadratic CANNOT absorb the log-p oscillations, whose
periods are ≥ 2π/log 13 ≈ 2.45 — the fit is computed on the full window and
the oscillations average out of it by construction)."""
function _hp_k_residual(K::Vector{Float64}, tvals::Vector{Float64}; dpoly::Int = 3)
    base = [_hp_kgue_envelope(t) for t in tvals]
    res = K .- base
    X = [Float64(t)^k for t in tvals, k in 0:dpoly]
    coef = X \ res
    return res .- X * coef
end

"""Average-rank transform (ties → average rank) for Spearman's ρ."""
function _hp_rankdata(x::Vector{Float64})
    n = length(x)
    ord = sortperm(x)
    ranks = zeros(Float64, n)
    i = 1
    while i <= n
        j = i
        while j < n && x[ord[j + 1]] == x[ord[i]]
            j += 1
        end
        avg = (i + j) / 2
        for k in i:j
            ranks[ord[k]] = avg
        end
        i = j + 1
    end
    return ranks
end
_hp_spearman(x::Vector{Float64}, y::Vector{Float64}) = cor(_hp_rankdata(x), _hp_rankdata(y))

"""H7 fluctuation high-pass: subtract the centered moving average (half-width
`win`) from a fluctuation series. The local-window unfolding leaves a SLOW
deterministic bias (window-position structure + support curvature) that is
COMMON to every spectrum processed by the same estimator — a shared smooth
component inflates the correlation of even perfectly independent series
(measured: untrimmed GUE–GUE pairs at |r| ≈ 0.65, edge-trimmed still 0.2–0.5).
A pointwise sequence identity signal — the thing H7 tests — is a LOCAL,
high-frequency feature and survives this filter intact; the smooth estimator
artifact does not. Every H7 correlation (AB–ζ, calibration pairs, shuffled
control) applies the same filter, so the empirical null band stays honest."""
function _hp_fluct_hp(f::Vector{Float64}; win::Int)
    n = length(f)
    win = max(1, min(win, n ÷ 2))
    smooth = [mean(f[max(1, i - win):min(n, i + win)]) for i in 1:n]
    return f .- smooth
end

"""Linear least squares y ≈ X·c for an explicit basis matrix X (n×k).
Returns (coef, RSS, R²). The H2 fits use basis matrices, so a single helper
covers both the 3-parameter ζ-ansatz and the 2-parameter lattice reference."""
function _hp_linlsq(X::Matrix{Float64}, y::Vector{Float64})
    c = X \ y
    res = y .- X * c
    rss = sum(abs2, res)
    my = mean(y)
    sst = sum(abs2, y .- my)
    r2 = sst > 1e-300 ? 1.0 - rss / sst : 0.0
    return c, rss, r2
end

"""Small-sample-corrected AIC (AICc, Burnham–Anderson): n·ln(RSS/n) + 2k +
2k(k+1)/(n−k−1). AICc is used because H2 compares a 3-parameter model
against a 2-parameter one on n = 40–60 points — plain AIC over-rewards the
extra parameter at this n."""
function _hp_aicc(n::Int, rss::Float64, k::Int)
    denom = n - k - 1
    aic = n * log(max(rss, 1e-300) / n) + 2k
    return denom > 0 ? aic + 2k * (k + 1) / denom : aic
end

"""Spacings of a sorted central band normalized to unit mean — the input
format every GUE goodness-of-fit helper of the suite expects."""
_hp_unit_spacings(band::Vector{Float64}) =
    (d = diff(band); m = mean(d); m > 1e-300 ? d ./ m : d)

"""Wald 95% CI on a binomial fraction (the honest %-passed band of H5)."""
function _hp_wald_ci(k::Int, n::Int)
    n == 0 && return (0.0, 0.0, 0.0)
    p = k / n
    h = 1.96 * sqrt(p * (1 - p) / n)
    return (p, clamp(p - h, 0.0, 1.0), clamp(p + h, 0.0, 1.0))
end

# ── HP parameter regimes (reviewer action 2026-09-06) ──────────────────
# The first H5 run measured the ensemble ONLY at the HP-standard point
# (sparse Nv = resolve_vortex_count = 4, α = ab_alpha_test16 = 0.5) and found
# a REPRODUCIBLE GUE miss (KS 0/40, σ = 0.0087). The reviewer's objection:
# "the model systematically misses GUE" is indistinguishable from "we tested
# the wrong parameter point" until the ensemble is re-measured at the model's
# best-faith points. Two suite-own reference points motivate the 2×2:
#   (i)  the monograph DENSITY anchor 25/900 = 2.78% of sites → Nv = L²/36
#        (87 vortices at L = 56 — 22× the sparse count). This is the SAME
#        lever that lifted the Test-32 comparison row to ⟨r⟩ = 0.5975 = GUE
#        (validated run_20260829: Nv_cmp = 144 = 2.78% at 72×72), and the
#        Test-38 density law is Nv = f·L²/36 with f = 1.
#   (ii) the SHARP-FLUX screening length α = 25/900 ≈ 0.0278 — the ORIGINAL
#        design default of ab_alpha_test16 (the field comment still reads
#        "default 25/900 ≈ 0.0278"; the v23 launch default was later moved to
#        0.5, the critical line). α = 0.028 is genuinely different physics:
#        near-unscreend flux tubes vs fat soft vortices at α = 0.5.
# The 2×2 factorial {density} × {α} attributes every ensemble outcome to its
# lever; regime A reproduces the published baseline bit-for-bit (identical
# seed streams). The same regimes re-check H1's fingerprint-absent verdict
# ("для чистоты", per the same reviewer action). W stays at the HP standard
# everywhere (ab_w_eff ≤ 1.0) so density and α are the ONLY moving levers.
const HP_ALPHA_SMALL = 25.0 / 900.0 # ≈ 0.0278 — sharp-flux screening length (monograph 30×30 density read as α)

"""The v23.6 H5 α-profile grid (module-level so the battery COST ESTIMATOR
accounts for the same 6×Nα diagonalizations the gate actually runs)."""
const HP_ALPHA_GRID = [HP_ALPHA_SMALL, 0.05, 0.1, 0.2, 0.35, 0.5]

struct HPRegime
    key::String        # "A".."D"
    tag::String        # short label for report rows / plot legends
    nv_mode::Symbol    # :suite (resolve_vortex_count) | :density (max(4, round(L²/36)))
    alpha_mode::Symbol # :suite (ab_alpha_test16) | :small (HP_ALPHA_SMALL)
end

function hp_regimes(cfg::HPConfig)
    base = HPRegime("A", "baseline (published run)", :suite, :suite)
    combined = HPRegime("D", "combined (density + sharp-flux)", :density, :small)
    cfg.hp_regime_mode === :baseline && return [base]
    cfg.hp_regime_mode === :regime_d && return [combined] # v24.2: FOCUS-D — the whole budget on the combined regime
    return [base,
            HPRegime("B", "monograph density Nv=L²/36", :density, :suite),
            HPRegime("C", "sharp-flux α=25/900", :suite, :small),
            combined]
end

_hp_regime_Nv(cfg::HPConfig, L::Int, R::HPRegime) =
    R.nv_mode === :density ? max(4, round(Int, L^2 / 36)) : resolve_vortex_count(cfg)
_hp_regime_alpha(cfg::HPConfig, R::HPRegime) =
    R.alpha_mode === :small ? HP_ALPHA_SMALL : cfg.ab_alpha_test16

"""One-line parameter descriptor of a regime (printed everywhere the regime
is used, so the report never says just 'regime B')."""
function _hp_regime_desc(cfg::HPConfig, L::Int, R::HPRegime)
    Nv = _hp_regime_Nv(cfg, L, R)
    α = _hp_regime_alpha(cfg, R)
    return @sprintf("Nv=%d (%.2f%% of sites%s), α=%.4f%s", Nv, 100 * Nv / Float64(L^2),
                    R.nv_mode === :density ? ", L²/36 anchor" : "",
                    α, R.alpha_mode === :small ? ", 25/900 sharp-flux" : "")
end

# ── H5 solve budget (v24.1, user cap 2026-09-09: «максимум 40 — избыточно») ──
# The 2×2 showdown + α-profile used to scale freely with the preset
# (FAST = 4×100 + 6×40 = 640 dense solves). Every H5 plan now comes from THIS
# one planner, and the cost estimator reads the same plan — the gate and the
# «battery cost» banner can never disagree again.
const HP5_SOLVE_CAP = 40 # hard ceiling on dense eigensolves issued by gate H5

"""Budget split for H5's dense eigensolves (≤ HP5_SOLVE_CAP total): `E`
configs per regime (2×2 = 4 regimes) + `Nα` configs per α-point of the
6-point profile. The α-profile is shaved first (it is a never-scored readout),
then the ensemble. `asked`/`capped` record what the config REQUESTED, so the
gate can say honestly what was reduced and by how much."""
function _hp5_plan(cfg::HPConfig)
    n_reg = length(hp_regimes(cfg))
    if n_reg == 1 # :baseline legacy AND v24.2 :regime_d focus — the WHOLE cap goes to one regime (N=40)
        E = clamp(cfg.hp_n_ensemble, 1, HP5_SOLVE_CAP)
        return (n_reg = 1, E = E, Nα = 0, total = E,
                asked = cfg.hp_n_ensemble, capped = cfg.hp_n_ensemble > HP5_SOLVE_CAP)
    end
    E  = clamp(cfg.hp_n_ensemble, 1, 7)                            # 4 × ≤7  ≤ 28
    Nα = cfg.hp_alpha_scan ? clamp(cfg.hp_alpha_scan_n, 1, 2) : 0  # 6 × ≤2  ≤ 12
    total = n_reg * E + length(HP_ALPHA_GRID) * Nα
    while total > HP5_SOLVE_CAP && Nα > 0 # shave the readout first
        Nα -= 1
        total = n_reg * E + length(HP_ALPHA_GRID) * Nα
    end
    while total > HP5_SOLVE_CAP && E > 1
        E -= 1
        total = n_reg * E + length(HP_ALPHA_GRID) * Nα
    end
    asked = n_reg * cfg.hp_n_ensemble +
            (cfg.hp_alpha_scan ? length(HP_ALPHA_GRID) * cfg.hp_alpha_scan_n : 0) # the RAW config request
    return (n_reg = n_reg, E = E, Nα = Nα, total = total, asked = asked,
            capped = total < asked)
end

"""Standard HP config in a parameter REGIME. Regime A ≡ _hp_std_config
bit-for-bit (same vortex recipe, same MersenneTwister(seed) stream); the
other regimes override only their own levers (Nv and/or α)."""
function _hp_regime_config(cfg::HPConfig, L::Int, seed::Int, R::HPRegime;
                           lattice::Symbol = :open)
    α = _hp_regime_alpha(cfg, R)
    local v::Vector{Vortex}
    if R.nv_mode === :density
        Nv = _hp_regime_Nv(cfg, L, R)
        v = Nv == 0 ? Vortex[] :
            random_vortex_configuration(Nv, L, L; q_magnitude = resolve_q_magnitude(cfg),
                                        enforce_neutrality = true,
                                        rng = MersenneTwister(seed),
                                        place_at_centers = true)
    else
        v = _hp_std_vortices(cfg, L, MersenneTwister(seed))
    end
    return ABCloudConfig(L, L, v, α, cfg.ab_t, lattice, ab_w_eff(cfg), seed, :monumental)
end

# ── HP registration ─────────────────────────────────────────────────────
function _hp_register!()
    isempty(HP_AUDITS) || return
    audits = (
        HPAudit(301, "A", "prime_oscillations",
            "H1. Prime oscillations (Berry–Keating fingerprint)",
            "K(t) residual periodogram: peaks exactly at ω = log(2), log(3), log(5)… — the only suite test specific to ζ",
            "Subtracts the analytic GUE envelope (Test-35 K_box) from the ensemble form factor K(t) and scans the RESIDUAL " *
            "periodogram at the prime-log angular frequencies ω = log p. The Riemann–Weil explicit formula links the zero " *
            "sequence to a sum over prime powers, so ζ's own K(t) oscillates at exactly these frequencies (positive control) " *
            "while independent GUE spectra do not (null control). A generic chaotic system leaves no such fingerprint — " *
            "this is the single test in the suite that is SPECIFIC to the zeta function, not just to GUE universality. " *
            "REGIME SWEEP (reviewer actions 2026-09-06, rounds 1+2): an ABSENT verdict must be regime-robust to count as a " *
            "model-class statement, so the AB spectra are re-checked at the H5 showdown's parameter points (monograph " *
            "density Nv = L²/36, sharp-flux α = 25/900, combined); every extra regime ALSO runs its OWN regime-matched " *
            "null controls (vortex-free at the same α + GUE at matched size), and the sweep sub-check is SCORED against " *
            "that ceiling — a bump reproduced by the nulls is a generic lattice artifact (PASS), an unexplained one is " *
            "an honest WARN. :baseline mode skips the sweep. v23.6 (round 3): the window auto-extends to every target " *
            "and the list splits into primes vs COMPOSITE DECOYS (the ζ comb must be silent on the decoys — a real " *
            "specificity control); a MARGINAL/PRESENT regime triggers the DEEPEN protocol — the null ceiling is " *
            "re-estimated from hp_deep_nulls + hp_deep_nulls realizations and the bump is judged against the P95 of " *
            "the null maxima (pre-registered rule): bump ≤ P95 → generic artifact → absent (question closed); " *
            "bump > P95 → honest WARN with escalation.",
            hp_h01_berry_keating),
        HPAudit(302, "A", "weyl_law_density",
            "H2. Weyl-law density test (raw N(E), never unfolded)",
            "raw staircase N(E): ζ-type {E·lnE, E, 1} ansatz vs lattice-DOS reference — R²/AIC showdown",
            "The suite's local window unfolding FORCES mean spacing 1 everywhere and thereby erases exactly the information " *
            "this test restores: does the RAW (never-unfolded) level count of the AB-cloud grow like the ζ smooth counting " *
            "function N̄(T) = (T/2π)ln(T/2π) − T/2 + 7/8 (the {E·lnE, E, 1} basis with free coefficients), or like the " *
            "natural lattice DOS of the vortex-free Hofstadter band? Both models are fitted to the same staircase; R² and " *
            "the small-sample AICc decide, with |ΔAICc| > 10 the decisive-separation convention.",
            hp_h02_weyl_law),
        HPAudit(303, "B", "power_law_real_spectrum",
            "H3. Power-law exponent on the REAL lattice spectrum",
            "Eₙ ~ (n−n₀)^p log-log fit + L→∞ extrapolation (Test-38 scheme): does p → 2, or to the lattice values 1/2 / 1?",
            "The Eₙ = (n−q)² dictionary lives on a TOY ring (lab E8) and is never fitted to the real, independently " *
            "diagonalized lattice spectrum — until now. For every rung of the refinement ladder the positive branch of the " *
            "true spectrum is fitted by Eₙ ~ (n)^p in a near-edge and a bulk window (Test-3 log-log machinery, R² as the " *
            "yardstick), and p̂(L) is extrapolated L→∞ exactly like Test 38's hardcore A1. Theory anchors: dictionary p = 2, " *
            "2D Dirac DOS p = 1/2 (N(E) ∝ E² near the cone), quadratic band bottom p = 1. VERDICT SEMANTICS (reviewer sync " *
            "2026-09-06): a REJECTED dictionary is the EXPECTED honest negative and passes the audit exactly like H1's " *
            "absent fingerprint or H7's zero correlation — the test fails only on method grounds (bad fits, or the " *
            "spectrum actually approaching p = 2). The verdict rests on the per-L fits (each ≫5σ from 2), NOT on the " *
            "unstable L→∞ extrapolation, which is reported as an informational note; the Dirac-cone proximity of the " *
            "low window is promoted to its own headline row.",
            hp_h03_power_law),
        HPAudit(304, "B", "critical_q_scan",
            "H4. Critical-q sharpness scan (falsifying the 'critical line' analogy)",
            "fine q-grid × 2 disorder seeds: does GUE quality PEAK sharply at the claimed critical q or drift smoothly?",
            "If q really plays the role of '1/2' in Re(s) = 1/2 (the orbit-levels / Gram-point dictionary claim), the " *
            "GUE-quality metrics (KS distance to the Wigner surmise, ⟨r⟩) must be SHARPLY peaked at the claimed critical " *
            "charge — a smooth drift would falsify the analogy. Fixed vortex positions across the grid (only the charge " *
            "varies), two independent disorder seeds per point for a noise floor, a quadratic baseline minus profile test " *
            "for prominence, and the claimed criticals q = 1/2 (self-dual analog), 0.3 (toy dictionary) and 1.0 " *
            "(Byers–Yang) marked on the profile. LOCATION HONESTY (reviewer sync 2026-09-06): a sharp feature is scored " *
            "for EXISTENCE only — a resonance AWAY from every claimed critical is reported as 'real but UNPREDICTED' and " *
            "does NOT corroborate the critical-line analogy; a dedicated verdict row states the distance explicitly.",
            hp_h04_critical_q),
        HPAudit(305, "C", "large_ensemble",
            "H5. Large ensemble × parameter-regime showdown (density × α, 2×2)",
            "⟨r⟩/KS-D across the 2×2 {sparse | L²/36 density} × {α=0.5 | α=25/900} under a ≤40-solve budget: model property vs finetuned parameter point",
            "Every suite average rests on n_realizations = 2–6, and the first H5 run measured the ensemble ONLY at the " *
            "sparse HP-standard point (Nv=4, α=0.5) — 22× below the suite's own monograph density anchor (25/900 = 2.78% " *
            "→ Nv = L²/36 = 87 at L=56; the SAME lever that lifted the Test-32 comparison row to ⟨r⟩ = 0.5975 = GUE). " *
            "The reviewer's objection: 'the model systematically misses GUE' is indistinguishable from 'we tested the " *
            "wrong parameter point' until the ensemble is re-measured at the model's best-faith points. This audit now " *
            "runs the full 2×2 factorial — A: published baseline (reproduced bit-for-bit), B: monograph density, " *
            "C: sharp-flux α = 25/900 ≈ 0.0278 (the ORIGINAL ab_alpha_test16 design value), D: both levers combined — " *
            "each with its planned configs (v24.1 budget: ≤7/regime, ≤ 40 dense solves total; placement AND disorder vary), and reports per-regime " *
            "⟨r⟩/KS distributions, Wald 95% CIs, the scatter σ, and the regime-robustness headline: a GUE failure that " *
            "survives all four regimes is a model-class property; recovery at any regime is parameter-dependent. " *
            "v23.5 (reviewer round 2): the RAW individual KS-pass % is explicit in every regime row; a regime passing " *
            "only via the median-D OR-clause is flagged 'OR-clause only' (near-0% individual passes = systematic, not " *
            "noise); a dedicated row tracks whether a CLEAN pass exists at all; and the test status is the strict AND " *
            "of all scored rows — a failing baseline propagates, no silent WARN→PASS override; the only clean pass " *
            "sitting at the doubly-tuned point is reported as the finetuning story it is. (regime table = evidence; " *
            "best-of-4 selection is pre-registered, not post hoc). :baseline mode runs regime A only (≈4× faster). " *
            "v24.2: :regime_d mode runs the OPPOSITE focus — ALL 40 solves on regime [D] alone at N=40 (seeds continue " *
            "the showdown's [D] stream) to test whether its OR-clause pass survives full-power individual KS. " *
            "v23.6 (round 3): a new α-PROFILE stage sweeps GUE quality ALONG the screening axis at fixed sparse Nv " *
            "(α ∈ {25/900, 0.05, 0.1, 0.2, 0.35, 0.5} × ≤2 configs under the budget): PLATEAU-LOW = the whole sharp-flux " *
            "side is GUE-universal (the α=0.5 baseline is the outlier); NARROW = finetuning confirmed along the axis. " *
            "The α-profile is a readout row (never scored); the regime table remains the scored evidence.",
            hp_h05_ensemble),
        HPAudit(306, "C", "stability_stress",
            "H6. Self-adjointness & stability stress test",
            "open↔torus, vortex/α jitter, L-growth: hermiticity max|H−H†| at machine ε on EVERY rung + spectral drift",
            "A genuine Hilbert–Pólya operator must be self-adjoint STABLY — not 'hermitian because we built it so'. Three " *
            "systematic probes around the H–P parameters: (a) the same configuration on :open vs :torus (bulk window must " *
            "be boundary-blind up to edge states), (b) hp_jitter_trials realizations with vortex-position and α jitter " *
            "(spectral drift of the aligned central band must stay O(noise), no NaN/complex), (c) the L-ladder with the " *
            "hermiticity defect max|H−H†| verified at machine ε on EVERY rung (the systematic version of the one-off 3D " *
            "hardcore H1 check).",
            hp_h06_stability),
        HPAudit(307, "D", "sequence_correlation",
            "H7. Sequence-level correlation vs γₙ (Pearson/Spearman)",
            "n-th unfolded level vs n-th zero: independent GUE ⇒ correlation 0 — calibrated by independent GUE–GUE pairs",
            "Test 34 compares DISTRIBUTIONS (KS on spacings, R₂ curves); nobody ever checked SEQUENCE identity: after " *
            "unfolding, does the n-th AB-cloud level correlate with the n-th real zero γₙ? Raw correlations are trivially " *
            "~1 (both sequences increase), so the test correlates the FLUCTUATIONS around the mean density and calibrates " *
            "the answer against independent GUE–GUE pairs (whose |r| distribution IS the null) plus a shuffled control. " *
            "Honest expectation: zero — and the suite now states it explicitly instead of leaving the hole open.",
            hp_h07_sequence_correlation),
    )
    for a in audits
        push!(HP_AUDITS, a)
        TEST_META[a.id] = ("hp_" * a.slug, a.title, a.detail)
    end
    return
end

# ═══════════════════════════════════════════════════════════════════════════
# GROUP A — "does the spectrum know about primes?"
# ═══════════════════════════════════════════════════════════════════════════

# ── H1: prime oscillations (Berry–Keating fingerprint) ─────────────────
# TWO detectors, run through the IDENTICAL pipeline for all four spectra
# (AB ensemble / ζ positive control / vortex-free nulls / GUE nulls):
#
#   D1 (PRIMARY) — raw-position 1-level Fourier transform (_hp_raw_ft).
#       The Riemann–Weil explicit formula makes the zero-density fluctuation a
#       sum of PURE TONES in the raw ordinate T: δρ(T) ∝ Σ_{p,k}(log p)/p^{k/2}
#       cos(kT·log p). A spectrum with arithmetic information shows Bragg peaks
#       at ω = log p. Empirical calibration (v23.3 run): ζ fires at SNR 10⁶–10⁹
#       (peaks at log 2, log 3, log 5, log 13 AND the harmonics 3·log 2, 4·log 2);
#       GUE nulls ≤ 5.2; vortex-free Hofstadter nulls ≤ 2.1.
#   D2 (cross-check, the reviewer's literal estimator) — K(t) minus the analytic
#       GUE envelope (Test-35 K_box), quadratic detrend, angular periodogram.
#       Retained and reported honestly: the 1-level explicit-formula signal
#       enters the TWO-level statistic only at subleading order, so D2's ζ
#       control does NOT fire at suite scale — the report says so explicitly.
#
# HONESTY: the test's PASS/FAIL certifies the DETECTOR (positive control fires,
# nulls stay silent); the AB fingerprint verdict is the headline, never forced
# into pass/fail.
"""Primality by trial division (the H1 target lists are tiny — no Primes.jl
dependency). v23.6: the hp_primes list may legally contain COMPOSITES (they
become specificity decoys in H1), so the split must be exact."""
function _hp_isprime(n::Int)::Bool
    n < 2 && return false
    n < 4 && return true
    iseven(n) && return false
    d = 3
    while d * d <= n
        n % d == 0 && return false
        d += 2
    end
    return true
end

function hp_h01_berry_keating(cfg::HPConfig, zeta_zeros::Vector{Float64})
    _mr_gate_head(1, "PRIME-TRACE",
                  "Prime oscillations — Berry-Keating fingerprint (arithmetic specificity)",
                  "Does the 1-level density oscillate EXACTLY at ω = log(p) once generic structure is removed?")

    L = cfg.hp_L
    n_t = max(50, round(Int, cfg.hp_t_max / cfg.hp_dt))
    tvals = [cfg.hp_dt * k for k in 1:n_t] # t = 0 dropped: K(0) is the self-pair artifact
    # v23.6 (reviewer round 3, №5): the target list may contain COMPOSITES
    # (21, 33, 54, 56 in run_20260906_185208) and targets above the old hardcoded
    # window [0.3, 3.0] (log 21 = 3.0445 > 3.0) — those scored a meaningless
    # floor (0.093) and made "7/14 primes ≥ 100" read as "half the primes silent".
    # The window now AUTO-EXTENDS to cover every target, and the list SPLITS into
    # true primes (the Bragg comb must fire on all of them) and composite DECOYS
    # (a REAL specificity control: the comb must be SILENT there — a comb that
    # also fires at log(21)/log(33) would be a generic periodicity, not primes).
    primes = sort(unique([p for p in cfg.hp_primes if _hp_isprime(p)]))
    decoys = sort(unique([p for p in cfg.hp_primes if !_hp_isprime(p)]))
    isempty(primes) && (primes = [2, 3, 5, 7, 11, 13]) # degenerate list guard
    ω_targets = [log(p) for p in primes]
    ω_decoys = [log(p) for p in decoys]
    ωgrid = collect(0.3:0.004:max(3.0, maximum(vcat(ω_targets, ω_decoys)) + 0.2))
    snr_min = 50.0        # D1 fingerprint threshold (empirical null ceiling ≤ 5.2 → 10× margin + floor)
    ctrl_min = 100.0      # D1 ζ-control threshold (empirical: 10⁶+)
    null_lim = 10.0       # D1 null ceiling limit

    @printf(" AB spectrum: %d configs on %d×%d (FULL raw spectrum, no unfolding) | ζ control: first %s zeros\n",
            cfg.hp_h1_configs, L, L, isempty(zeta_zeros) ? "0" : @sprintf("%d", min(length(zeta_zeros), cfg.hp_zeta_cap)))
    @printf(" D1 scan: ω ∈ [0.3, %.1f] step 0.004 (auto-extended to every target, v23.6) | thresholds: fingerprint ≥ %.0f, control ≥ %.0f, null ceiling < %.0f\n",
            ωgrid[end], snr_min, ctrl_min, null_lim)
    @printf(" Prime targets (%d): %s\n",
            length(primes), join([@sprintf("log(%d)=%.4f", p, log(p)) for p in primes], "  "))
    isempty(decoys) || @printf(" Composite decoys (%d): %s — SPECIFICITY controls: the Bragg comb must stay SILENT there\n",
            length(decoys), join([@sprintf("log(%d)=%.4f", p, log(p)) for p in decoys], "  "))

    snr_of(P, med, ω) = begin
        i = argmin(abs.(ωgrid .- ω))
        return med > 1e-300 ? P[i] / med : 0.0
    end

    # ── stage 1: AB-cloud spectra (kept for BOTH routes) ──
    P_ab = zeros(Float64, length(ωgrid))
    K_ab = zeros(Float64, length(tvals))
    n_used = 0
    n_raw = 0
    rms_env_acc = 0.0
    for k in 1:cfg.hp_h1_configs
        seed = cfg.hp_seed + 100 + k
        prog_update(0.02 + 0.20 * (k - 1) / max(cfg.hp_h1_configs, 1),
                    @sprintf("H1 config %d/%d", k, cfg.hp_h1_configs))
        c = _hp_std_config(cfg, L, seed)
        evals = _hp_spectrum(cfg, c)
        n_raw = length(evals)
        P_ab .+= _hp_raw_ft(evals, ωgrid) # power averaging across configs
        band = central_band_eigs(evals, cfg.ab_center_fraction)
        K_ab .+= compute_K_form_factor(band, tvals; smooth_window = cfg.ab_K_smooth_window)
        n_used += 1
        rms_env_acc += sqrt(mean((K_ab[tvals .>= 0.3] ./ max(n_used, 1) .-
                                  [_hp_kgue_envelope(t) for t in tvals[tvals .>= 0.3]]).^2))
        log_comp(@sprintf(" H1: config seed=%d raw FT + K(t) accumulated (%d levels)", seed, n_raw))
    end
    P_ab ./= max(n_used, 1)
    K_ab ./= max(n_used, 1)
    rms_env = rms_env_acc / max(n_used, 1)
    med_ab = median(P_ab)
    snrs_ab = [snr_of(P_ab, med_ab, ω) for ω in ω_targets]
    snrs_ab_decoy = [snr_of(P_ab, med_ab, ω) for ω in ω_decoys]
    prog_update(0.30, "H1: AB spectra done")

    # ── stage 2: ζ positive control ──
    snrs_z = Float64[]; snrs_z_k = Float64[]; snrs_z_decoy = Float64[]
    Pz = Float64[]; med_z = 1.0
    decoy_max_z = 0.0
    decoys_silent = true
    zeta_ok = false
    if isempty(zeta_zeros)
        println(" ζ positive control: SKIPPED (no zeros loaded) — detector cannot be validated → WARN")
    else
        zslice = zeta_zeros[1:min(end, cfg.hp_zeta_cap)]
        prog_update(0.38, @sprintf("H1: ζ control on %d zeros", length(zslice)))
        Pz = _hp_raw_ft(zslice, ωgrid)
        med_z = median(Pz)
        snrs_z = [snr_of(Pz, med_z, ω) for ω in ω_targets]
        snrs_z_decoy = [snr_of(Pz, med_z, ω) for ω in ω_decoys]
        k_sig = count(>=(ctrl_min), snrs_z)
        # v23.6 specificity clause: the Bragg comb must fire on the primes AND be
        # silent on the composite decoys — a comb that also fires at log(21)/
        # log(33) is a generic periodicity artifact, not arithmetic.
        decoy_max_z = isempty(snrs_z_decoy) ? 0.0 : maximum(snrs_z_decoy)
        decoys_silent = decoy_max_z < ctrl_min
        zeta_ok = (k_sig >= max(2, length(primes) ÷ 2)) && decoys_silent
        @printf(" ζ control D1 (%d zeros): SNR at log p = %s\n", length(zslice),
                join([@sprintf("%.1e", s) for s in snrs_z], " / "))
        @printf("   → %d/%d primes ≥ %.0f → Bragg structure at prime logs %s\n",
                k_sig, length(primes), ctrl_min,
                k_sig >= max(2, length(primes) ÷ 2) ? "CONFIRMED (Riemann–Weil expectation)" : "NOT CONFIRMED")
        isempty(snrs_z_decoy) || @printf("   → composite decoys: max SNR %.1e at log(%d) → %s (specificity %s)\n",
                decoy_max_z, decoys[argmax(snrs_z_decoy)],
                decoys_silent ? "SILENT" : "FIRING — generic comb alarm!",
                decoys_silent ? "ok" : "VIOLATED")
        # D2 route on ζ (the reviewer's literal estimator — sensitivity cross-check)
        K_z = compute_K_form_factor(zslice, tvals; smooth_window = cfg.ab_K_smooth_window)
        res_z = _hp_k_residual(K_z, tvals)
        Pz2 = _hp_periodogram(res_z, tvals, ωgrid)
        med_z2 = median(Pz2)
        snrs_z_k = [snr_of(Pz2, med_z2, ω) for ω in ω_targets]
        @printf(" ζ control D2 (K-residual route): SNR = %s → %s\n",
                join([@sprintf("%.1f", s) for s in snrs_z_k], " / "),
                count(>=(3.0), snrs_z_k) >= 3 ? "fires" :
                "does NOT fire at this scale — the 1-level signal enters the 2-level K(t) only at subleading order (reported honestly)")
    end

    # ── stage 3: null controls — vortex-free (same smooth DOS skeleton) + GUE ──
    prog_update(0.55, "H1: null controls")
    max_snr_null = 0.0
    null_desc = String[]
    for k in 1:2 # vortex-free Hofstadter nulls: same band edges / van-Hove structure, NO vortex phases
        c0 = ABCloudConfig(L, L, Vortex[], cfg.ab_alpha_test16, cfg.ab_t, :open,
                           0.0, cfg.hp_seed + 710 + k, :monumental)
        ev0 = _hp_spectrum(cfg, c0)
        P0 = _hp_raw_ft(ev0, ωgrid)
        med0 = median(P0)
        s0 = [snr_of(P0, med0, ω) for ω in ω_targets]
        max_snr_null = max(max_snr_null, maximum(s0))
        push!(null_desc, @sprintf("vortex-free #%d: max %.1f", k, maximum(s0)))
    end
    for k in 1:2 # GUE nulls at matched size: generic-chaos noise floor
        gue = gue_matrix_eigenvalues(n_raw; seed = cfg.hp_seed + 730 + k)
        Pg = _hp_raw_ft(gue, ωgrid)
        sg = [snr_of(Pg, median(Pg), ω) for ω in ω_targets]
        max_snr_null = max(max_snr_null, maximum(sg))
        push!(null_desc, @sprintf("GUE #%d: max %.1f", k, maximum(sg)))
    end
    @printf(" Nulls D1: %s → empirical ceiling %.1f (limit %.0f)\n",
            join(null_desc, " | "), max_snr_null, null_lim)

    # ── stage 4: the AB verdict (the headline) ──
    prog_update(0.75, "H1: AB verdict")
    k_ab = count(>=(snr_min), snrs_ab)
    threshold = max(snr_min, 10.0 * max_snr_null)
    fp_present = !isempty(snrs_ab) && maximum(snrs_ab) >= threshold
    fp_marginal = !fp_present && !isempty(snrs_ab) && maximum(snrs_ab) >= max_snr_null
    @printf("\n AB-cloud D1 (%d-config ensemble, %d raw levels): SNR at log p = %s\n",
            n_used, n_raw, join([@sprintf("%.1f", s) for s in snrs_ab], " / "))
    @printf("   → %d/%d primes ≥ %.0f (threshold %.0f = max(50, 10× ceiling %.1f))\n",
            k_ab, length(primes), snr_min, threshold, max_snr_null)
    isempty(snrs_ab_decoy) || @printf("   → AB composite decoys: max SNR %.1f at log(%d) → %s\n",
            maximum(snrs_ab_decoy), decoys[argmax(snrs_ab_decoy)],
            maximum(snrs_ab_decoy) < threshold ? "below threshold — no comb at non-arithmetic frequencies" :
                                                "ABOVE threshold at a COMPOSITE — argues AGAINST arithmetic (generic periodicity)")
    _fp_txt = fp_present ? "PRESENT — Bragg peaks at prime logs (generic chaos would not show them)" :
              fp_marginal ? "MARGINAL — above the null ceiling but below the decisive threshold; raise L/hp_zeta_cap" :
                            "ABSENT — no prime-log signature above the noise ceiling (GUE-universal statistics only)"
    _mr_status(fp_present ? "◆" : fp_marginal ? "⚠" : "●",
               fp_present ? "gold" : fp_marginal ? "warn" : "accent",
               "ARITHMETIC FINGERPRINT " * _fp_txt)
    @printf(" Cross-check vs Test 35: RMS(K_AB − K_box, t ≥ 0.3) = %.4f (Test 35 target < 0.30)\n", rms_env)

    # ── stage 5: fingerprint regime sweep (reviewer actions 2026-09-06, rounds 1+2) ──
    # ROUND 1: "перепрогнать H1 ... с Nv по формуле L²/36 и на α≈0.028". The ABSENT
    # verdict above is measured at the HP-standard point (sparse Nv,
    # α = ab_alpha_test16 = 0.5). Before "no prime signature" becomes a
    # MODEL-CLASS statement it must hold at the model's best-faith parameter
    # points too — the same 2×2 {density × α} the H5 showdown uses.
    # ROUND 2: the round-1 sweep found bumps of SNR 7–20 at log(2) in EVERY
    # extra regime while labeling the sub-check PASS — a stretch, because an
    # ISOLATED single-prime bump is not the ζ signature (the ζ control fires on
    # ALL 6 primes SIMULTANEOUSLY at SNR 10⁷–10⁹; log 2 ≈ 0.693 is nothing
    # arithmetically special and square-lattice periodicities can easily resona-
    # te nearby). Fix (exactly the reviewer's prescription): every extra regime
    # now runs its OWN regime-matched null controls — a vortex-free lattice at
    # the SAME α (same smooth DOS skeleton, no vortex phases) and a GUE spectrum
    # at matched size (fresh seeds). A bump reproduced by the nulls at the same
    # parameters = generic lattice/flux-geometry artifact → ABSENT is regime-
    # robust (PASS). A bump ABOVE the regime nulls = the single place of the
    # audit that earns an honest WARN and deeper study before any claim.
    reg_rows = Tuple{String,Float64,Int,String,Float64}[] # (key, maxSNR, argmax prime, verdict, regime null ceiling)
    reg_ctx = Dict{String,Tuple{Int,Vector{Float64}}}() # key → (raw levels/config, averaged periodogram) — for the deepen stage
    deep_info = Tuple{String,Float64,Float64,Int,String,Int}[] # (key, deep AB max, P95 null, n draws, verdict, deep prime)
    deep_draws = Dict{String,Vector{Float64}}() # key → pooled null max-SNR draws (plot data)
    sweep_ok = true
    if cfg.hp_regime_mode === :showdown
        sweep = [R for R in hp_regimes(cfg) if !(R.nv_mode === :suite && R.alpha_mode === :suite)] # regime A already measured above
        @printf("\n Regime sweep (reviewer actions): %d extra parameter points × %d configs, each vs its OWN regime-matched nulls\n",
                length(sweep), cfg.hp_h1_configs)
        println("   (the ζ fingerprint signature is a simultaneous Bragg comb on ALL primes at SNR ≥ 10²; an isolated")
        println("    log(2) bump is the classic generic resonance — the regime-matched nulls below decide which it is)")
        for (j, R) in enumerate(sweep)
            prog_update(0.78 + 0.16 * (j - 1) / max(length(sweep), 1),
                        @sprintf("H1 regime %s (%d/%d)", R.key, j, length(sweep)))
            P_r = zeros(Float64, length(ωgrid))
            n_r = 0
            n_rraw = 0
            for k in 1:cfg.hp_h1_configs
                seed = cfg.hp_seed + 40_000 + 1_000 * j + k # disjoint from every other HP stream
                ev = _hp_spectrum(cfg, _hp_regime_config(cfg, L, seed, R))
                n_rraw = length(ev)
                P_r .+= _hp_raw_ft(ev, ωgrid)
                n_r += 1
            end
            P_r ./= max(n_r, 1)
            snrs_r = [snr_of(P_r, median(P_r), ω) for ω in ω_targets]
            mx = isempty(snrs_r) ? 0.0 : maximum(snrs_r)
            pm = primes[argmax(snrs_r)]
            reg_ctx[R.key] = (n_rraw, copy(P_r)) # deepen stage extends exactly this ensemble
            # regime-matched nulls (reviewer round 2): SAME parameters, NO arithmetic
            c_vf = ABCloudConfig(L, L, Vortex[], _hp_regime_alpha(cfg, R), cfg.ab_t, :open,
                                 0.0, cfg.hp_seed + 40_000 + 1_000 * j + 900, :monumental)
            Pv = _hp_raw_ft(_hp_spectrum(cfg, c_vf), ωgrid)
            sv = [snr_of(Pv, median(Pv), ω) for ω in ω_targets]
            Pg = _hp_raw_ft(gue_matrix_eigenvalues(n_rraw;
                                seed = cfg.hp_seed + 40_000 + 1_000 * j + 950), ωgrid)
            sg = [snr_of(Pg, median(Pg), ω) for ω in ω_targets]
            reg_nc = max(maximum(sv), maximum(sg)) # THIS regime's null ceiling
            reg_thr = max(snr_min, 10.0 * reg_nc)  # same 10× margin logic as the baseline threshold
            verd = mx >= reg_thr ? "PRESENT" :
                   mx >= reg_nc ? "MARGINAL (above regime nulls)" : "absent (within regime nulls)"
            push!(reg_rows, (R.key, mx, pm, verd, reg_nc))
            @printf(" regime %s (%s): max prime-SNR %.1f at log(%d) | regime nulls: vortex-free %.1f, GUE %.1f → ceiling %.1f → fingerprint %s\n",
                    R.key, _hp_regime_desc(cfg, L, R), mx, pm, maximum(sv), maximum(sg), reg_nc, verd)
            log_comp(@sprintf(" H1 regime %s: %d raw levels/config, max prime-SNR %.2f, regime null ceiling %.2f (%s)",
                              R.key, n_rraw, mx, reg_nc, verd))
            sweep_ok &= verd == "absent (within regime nulls)"
            ab_gc!() # suite convention: explicit collection after every heavy solve (OOM guard)
        end

        # ── v23.6 DEEPEN protocol (reviewer round 3, №2) ──
        # The round-2 ceiling is estimated from ONE vortex-free + ONE GUE
        # realization per regime — an extreme-value statistic whose single-draw
        # noise is comparable to the observed 7.6-vs-6.8 margin (regime C,
        # run_20260906_185208), so a MARGINAL verdict is not decision-grade.
        # PRE-REGISTERED stop rule: re-estimate the null-maximum DISTRIBUTION
        # with hp_deep_nulls realizations per type, extend the regime AB
        # ensemble by hp_deep_configs configs, and judge the bump against the
        # 95th percentile of the null maxima:
        #   bump ≤ P95 → generic flux-geometry artifact → regime ABSENT — the
        #                reviewer's question ("lattice artifact or primes?") is
        #                CLOSED by data, the sweep returns to PASS;
        #   bump > P95 → unexplained even against deep nulls → honest WARN +
        #                escalation (zoom scan around the bump, per-config check).
        marginal_keys = [rr[1] for rr in reg_rows if !startswith(rr[4], "absent")]
        if !isempty(marginal_keys) && cfg.hp_deep_nulls >= 2
            @printf("\n DEEPEN protocol (v23.6): %d regime(s) at/above their 1+1-realization ceiling (%s) → null distribution from %d vortex-free + %d GUE realizations, AB ensemble +%d configs; pre-registered rule: deep AB bump ≤ P95(null maxima) → generic artifact → absent\n",
                    length(marginal_keys), join(marginal_keys, ","),
                    cfg.hp_deep_nulls, cfg.hp_deep_nulls, cfg.hp_deep_configs)
            for (j, R) in enumerate(sweep)
                R.key in marginal_keys || continue
                n_rraw_d, P_r0 = reg_ctx[R.key]
                prog_update(0.78 + 0.16 * (j - 0.5) / max(length(sweep), 1),
                            @sprintf("H1 deepen regime %s", R.key))
                null_maxima = Float64[]
                for i in 1:cfg.hp_deep_nulls # vortex-free at the SAME regime α
                    c_vf = ABCloudConfig(L, L, Vortex[], _hp_regime_alpha(cfg, R), cfg.ab_t, :open,
                                         0.0, cfg.hp_seed + 40_000 + 1_000 * j + 700 + i, :monumental)
                    Pv = _hp_raw_ft(_hp_spectrum(cfg, c_vf), ωgrid)
                    push!(null_maxima, maximum([snr_of(Pv, median(Pv), ω) for ω in ω_targets]))
                    log_comp(@sprintf(" H1 deepen [%s] vortex-free null %d/%d: max prime-SNR %.2f",
                                      R.key, i, cfg.hp_deep_nulls, null_maxima[end]))
                end
                for i in 1:cfg.hp_deep_nulls # size-matched GUE nulls
                    Pg = _hp_raw_ft(gue_matrix_eigenvalues(n_rraw_d;
                                        seed = cfg.hp_seed + 40_000 + 1_000 * j + 800 + i), ωgrid)
                    push!(null_maxima, maximum([snr_of(Pg, median(Pg), ω) for ω in ω_targets]))
                    log_comp(@sprintf(" H1 deepen [%s] GUE null %d/%d: max prime-SNR %.2f",
                                      R.key, i, cfg.hp_deep_nulls, null_maxima[end]))
                end
                p95 = quantile(null_maxima, 0.95)
                deep_draws[R.key] = copy(null_maxima)
                P_ext = copy(P_r0)
                n_ext = cfg.hp_h1_configs
                for i in 1:cfg.hp_deep_configs
                    seed = cfg.hp_seed + 40_000 + 1_000 * j + 600 + i # disjoint sub-stream
                    ev = _hp_spectrum(cfg, _hp_regime_config(cfg, L, seed, R))
                    P_ext .+= _hp_raw_ft(ev, ωgrid)
                    n_ext += 1
                    log_comp(@sprintf(" H1 deepen [%s] AB config %d/%d (seed=%d)", R.key, i, cfg.hp_deep_configs, seed))
                end
                P_ext ./= max(n_ext, 1)
                snrs_deep = [snr_of(P_ext, median(P_ext), ω) for ω in ω_targets]
                deep_mx = maximum(snrs_deep)
                deep_pm = primes[argmax(snrs_deep)]
                was_present = startswith(reg_rows[findfirst(rr -> rr[1] == R.key, reg_rows)][4], "PRESENT")
                deep_verd = deep_mx <= p95 ? "absent" : was_present ? "PRESENT" : "MARGINAL"
                push!(deep_info, (R.key, deep_mx, p95, length(null_maxima), deep_verd, deep_pm))
                @printf("   [%s] deep AB max prime-SNR %.1f at log(%d) (%d configs) | deep nulls: min %.1f / median %.1f / P95 %.1f / max %.1f (%d draws) → %s\n",
                        R.key, deep_mx, deep_pm, n_ext, minimum(null_maxima), median(null_maxima), p95,
                        maximum(null_maxima), length(null_maxima),
                        deep_verd == "absent" ?
                            "bump ≤ P95 → GENERIC FLUX-GEOMETRY ARTIFACT — fingerprint absent (the reviewer's question closed by data)" :
                        deep_verd == "PRESENT" ?
                            "bump > P95 AND above the decisive threshold — headline discovery candidate, ESCALATE" :
                            "bump > P95 → unexplained even vs deep nulls — ESCALATE (zoom scan around the bump, per-config persistence)")
                log_comp(@sprintf(" H1 deepen [%s]: deep AB max %.2f, null P95 %.2f (%d draws) → %s",
                                  R.key, deep_mx, p95, length(null_maxima), deep_verd))
                idx = findfirst(rr -> rr[1] == R.key, reg_rows)
                reg_rows[idx] = (R.key, deep_mx, deep_pm,
                                 deep_verd == "absent" ?
                                     @sprintf("absent (deep nulls: %.1f ≤ P95 %.1f)", deep_mx, p95) :
                                 deep_verd == "PRESENT" ?
                                     @sprintf("PRESENT (deep nulls: %.1f > P95 %.1f)", deep_mx, p95) :
                                     @sprintf("MARGINAL (deep nulls: %.1f > P95 %.1f)", deep_mx, p95),
                                 p95)
                ab_gc!()
            end
            sweep_ok = all(startswith(rr[4], "absent") for rr in reg_rows)
        end
    else
        println("\n Regime sweep: SKIPPED (:$((cfg.hp_regime_mode)) mode — HP-standard point only; switch hp_regime_mode to :showdown for the reviewer's cross-check)")
    end

    rec = Tuple{String,Bool,String}[]
    push!(rec, ("ζ control fires (D1)", zeta_ok,
        isempty(snrs_z) ? "skipped — no zeros loaded" :
        @sprintf("%d/%d prime Bragg peaks with SNR ≥ %.0f (Riemann–Weil expectation)%s",
                 count(>=(ctrl_min), snrs_z), length(primes), ctrl_min,
                 isempty(snrs_z_decoy) ? "" :
                     @sprintf("; composite decoys %s (%s)",
                              decoys_silent ? "silent" : @sprintf("FIRING, max %.1e", decoy_max_z),
                              decoys_silent ? "specificity ok — the comb is arithmetic, not generic" :
                                              "SPECIFICITY VIOLATED — generic comb"))))
    # null row: absolute ceiling < 10, OR (scale-free) ≥ 100× below the weakest
    # significant ζ peak — at toy lattices the median-P estimate is noisy and the
    # exponential tail of 6 draws can reach ~13 without any arithmetic content
    # (measured on the smoke run); the ζ-vs-null gulf is what validates the
    # detector, and it sits at 10⁷ here.
    min_sig_z = isempty(snrs_z) ? Inf : minimum(filter(>=(ctrl_min), snrs_z); init = Inf)
    null_ok = (max_snr_null < null_lim) || (min_sig_z < Inf && max_snr_null * 100.0 < min_sig_z)
    push!(rec, ("nulls silent (D1)", null_ok,
        @sprintf("vortex-free + GUE ceiling = %.1f (abs limit %.0f; weakest ζ peak %.1e — 100× margin %s)",
                 max_snr_null, null_lim, min_sig_z, null_ok ? "ok" : "VIOLATED")))
    push!(rec, ("AB fingerprint verdict", true,
        fp_present ? @sprintf("PRESENT — max SNR %.1e at log(%d)", maximum(snrs_ab), primes[argmax(snrs_ab)]) :
            fp_marginal ? @sprintf("MARGINAL — max SNR %.1f vs ceiling %.1f", maximum(snrs_ab), max_snr_null) :
                          @sprintf("ABSENT — max SNR %.1f < threshold %.0f", isempty(snrs_ab) ? 0.0 : maximum(snrs_ab), threshold)))
    # regime sweep headline (reviewer actions, rounds 1+2): the negative must
    # survive the model's best-faith parameter points AND be distinguishable
    # from generic lattice resonances (regime-matched nulls) before it counts
    # as a model-class statement. v23.5: the row is SCORED (its boolean enters
    # ok) — a mixed/MARGINAL content can no longer hide under a PASS label.
    reg_all_absent = !isempty(reg_rows) && all(startswith(rr[4], "absent") for rr in reg_rows)
    reg_any_present = any(startswith(rr[4], "PRESENT") for rr in reg_rows)
    reg_unexpl = [rr for rr in reg_rows if startswith(rr[4], "MARGINAL")]
    deep_tail = isempty(deep_info) ? "" :
        @sprintf(" DEEPENED (v23.6, pre-registered P95 rule): %s", join([
            @sprintf("[%s] deep AB %.1f vs P95 %.1f → %s", di[1], di[2], di[3], di[5]) for di in deep_info], "; "))
    # v23.5: this row is now a GENUINE sub-check (its boolean enters ok) — no
    # more PASS painted over "mixed/MARGINAL" content (reviewer round 2).
    push!(rec, ("fingerprint regime-robust (sweep)", sweep_ok,
        isempty(reg_rows) ? "skipped — :baseline mode (single HP-standard point)" :
        @sprintf("max SNR per regime (own null ceiling in parens): %s → %s%s",
                 join([@sprintf("[%s] %.1f (%.1f)", rr[1], rr[2], rr[5]) for rr in reg_rows], " "),
                 reg_all_absent ? "every regime bump sits WITHIN its regime-matched null ceiling → generic lattice/flux-geometry artifact, NOT primes — ARITHMETIC FINGERPRINT ABSENT is regime-robust" :
                 reg_any_present ? "PRESENT above the regime-matched nulls — headline discovery: deepen (more seeds/configs) before any claim" :
                 @sprintf("MARGINAL above regime nulls at %s → NOT explained by non-arithmetic spectra at the same parameters — deepen before any claim (reviewer round 2)",
                          join([@sprintf("[%s] %.1f vs ceiling %.1f", rr[1], rr[2], rr[5]) for rr in reg_unexpl], ", ")),
                 deep_tail)))
    # v23.5: this row GATES the test status (same consistency rule as H5 — a
    # failed row may never be silently overridden in the final log line).
    env_ok = rms_env < 0.30
    push!(rec, ("Envelope cross-check (D2)", env_ok,
        @sprintf("RMS(K−K_box, t≥0.3) = %.4f (Test-35 family target < 0.30; gates the test status)", rms_env)))
    hc_verdict_table(cfg, "Test H1", rec; pass_label = "HP audit")

    # ── report plots: periodograms (D1) and the K(t) curves (D2) ──
    if REP.current !== nothing
        p1 = RepPlot(@sprintf("H1 — D1 raw-position periodogram (ζ peaks at 10⁶+, null ceiling %.1f, AB max %.1f)",
                              max_snr_null, isempty(snrs_ab) ? 0.0 : maximum(snrs_ab)),
                     "angular frequency ω", "P(ω)/median(P)  [log scale intent: series ratios]")
        isempty(zeta_zeros) || add_series!(p1, "ζ control SNR", ωgrid, Pz ./ med_z, 'l')
        add_series!(p1, "AB-cloud SNR", ωgrid, P_ab ./ med_ab, 'l')
        add_series!(p1, "prime targets ω=log(p)", ω_targets, snrs_ab, 's')
        rep_plot!(p1)
        p2 = RepPlot("H1 — D2 cross-check: K(t) vs GUE envelope (Test-35 route)",
                     "t (unfolded units)", "K(t)")
        add_series!(p2, "K_AB (ensemble mean)", tvals, K_ab, 'l')
        add_series!(p2, "GUE envelope K_box", tvals, [_hp_kgue_envelope(t) for t in tvals], 'l')
        rep_plot!(p2)
        isempty(snrs_z_k) || begin
            res_ab = _hp_k_residual(K_ab, tvals)
            Pab2 = _hp_periodogram(res_ab, tvals, ωgrid)
            med_ab2 = median(Pab2)
            p3 = RepPlot("H1 — D2 K-residual periodogram (AB vs ζ control)",
                         "angular frequency ω", "P(ω)/median(P)")
            add_series!(p3, "AB SNR (K-residual)", ωgrid, Pab2 ./ med_ab2, 'l')
            add_series!(p3, "ζ SNR (K-residual)", ω_targets, snrs_z_k, 's')
            rep_plot!(p3)
        end
        # regime sweep: max prime-SNR per regime vs ITS OWN regime-matched null ceiling
        isempty(reg_rows) || begin
            reg_all = vcat([("A", isempty(snrs_ab) ? 0.0 : maximum(snrs_ab))],
                           [(rr[1], rr[2]) for rr in reg_rows])
            p4 = RepPlot(@sprintf("H1 — fingerprint regime sweep: max prime-SNR per regime vs its own null ceiling (verdict: %s)",
                                  reg_all_absent ? "ABSENT regime-robust (lattice artifact, not primes)" :
                                             reg_any_present ? "PRESENT at a regime — unexplained" :
                                                               "MARGINAL above nulls — unexplained"),
                         "parameter regime (A = baseline, then B/C/D of the H5 showdown)",
                         "max SNR at ω = log(p)")
            add_series!(p4, "max prime-SNR per regime", collect(1.0:Float64(length(reg_all))),
                        [rr[2] for rr in reg_all], 's')
            add_series!(p4, @sprintf("decisive threshold %.0f", threshold),
                        [0.5, Float64(length(reg_all)) + 0.5], [threshold, threshold], 'l')
            add_series!(p4, @sprintf("baseline null ceiling %.1f", max_snr_null),
                        [0.5, Float64(length(reg_all)) + 0.5], [max_snr_null, max_snr_null], 'l')
            add_series!(p4, "regime-matched null ceiling",
                        collect(2.0:Float64(length(reg_all))), [rr[5] for rr in reg_rows], 's')
            rep_plot!(p4)
        end
        # v23.6: DEEPEN protocol — the null max-SNR distribution vs the deep AB bump
        isempty(deep_info) || begin
            p5 = RepPlot("H1 — DEEPEN protocol (v23.6): null max-SNR distributions vs the deep AB bump; pre-registered rule: bump ≤ P95 → generic flux-geometry artifact",
                         "null draw # (sorted within each deepened regime; vortex-free + GUE pooled)", "max prime-SNR of the realization")
            xoff = 0.0
            for di in deep_info
                key = di[1]
                draws = get(deep_draws, key, Float64[])
                isempty(draws) && continue
                sd = sort(draws)
                add_series!(p5, @sprintf("[%s] null maxima (n=%d)", key, length(sd)),
                            collect(1.0:Float64(length(sd))) .+ xoff, sd, 's')
                add_series!(p5, @sprintf("[%s] P95 = %.1f", key, di[3]),
                            [xoff + 0.5, xoff + length(sd) - 0.5], [di[3], di[3]], 'l')
                add_series!(p5, @sprintf("[%s] deep AB bump = %.1f", key, di[2]),
                            [xoff + 0.5, xoff + length(sd) - 0.5], [di[2], di[2]], 'l')
                xoff += length(sd) + 1.0
            end
            rep_plot!(p5)
        end
    end
    rep_note!("D1 (primary) is the 1-level raw-position Fourier transform: the Riemann–Weil explicit formula " *
              "puts the arithmetic information into pure tones ω = k·log(p) of the RAW density, so a spectrum " *
              "carrying it shows Bragg peaks there. Empirical calibration at v23.3 defaults: ζ control fires at " *
              "SNR 10⁶–10⁹ (log 2, log 3, log 5, log 13 AND harmonics 3·log 2, 4·log 2 — the explicit-formula " *
              "signature), vortex-free Hofstadter nulls ≤ 2.1, GUE nulls ≤ 5.2. D2 (the K(t)-residual route) is " *
              "the two-level cross-check: intrinsically less sensitive because the 1-level explicit-formula " *
              "signal enters the 2-level statistic only at subleading order — its ζ control honestly does NOT " *
              "fire at suite scale, which the report states explicitly. The AB verdict compares against the " *
              "EMPIRICAL null ceiling with a 10× margin. REGIME SWEEP (reviewer actions 2026-09-06, rounds 1+2): " *
              "the AB spectra are re-measured at the H5 showdown's parameter points — monograph density Nv = L²/36, " *
              "sharp-flux α = 25/900, and both combined — because an ABSENT fingerprint counts as a model-class " *
              "statement only if it survives the model's best-faith points. Round 2: each extra regime ALSO runs its " *
              "own regime-matched null controls (vortex-free lattice at the same α + GUE at matched size, fresh " *
              "seeds), and the regime bump is judged against THAT ceiling: an isolated log(2) bump that the nulls " *
              "reproduce at the same parameters is a generic lattice/flux-geometry artifact (the ζ signature is a " *
              "simultaneous comb on ALL primes at SNR 10⁷+, not a single-prime bump), while a bump above the regime " *
              "nulls earns an honest WARN and deeper study; the sweep status enters the test status — no PASS " *
              "painted over MARGINAL content. v23.6 (reviewer round 3): (a) the D1 window AUTO-EXTENDS to every " *
              "target and the target list SPLITS into primes vs composite DECOYS — the ζ Bragg comb must be silent " *
              "on the decoys (specificity clause folded into zeta_ok), and the AB decoy SNR is reported alongside; " *
              "(b) a MARGINAL/PRESENT regime triggers the DEEPEN protocol: the regime null ceiling is re-estimated " *
              "from hp_deep_nulls vortex-free + hp_deep_nulls GUE realizations (the round-2 ceiling came from ONE " *
              "of each — an extreme-value statistic whose single-draw noise is comparable to the observed 7.6-vs-6.8 " *
              "margin), the AB ensemble is extended by hp_deep_configs configs, and the pre-registered rule fires: " *
              "deep bump ≤ P95(null maxima) → generic flux-geometry artifact → regime absent (question closed by " *
              "data); bump > P95 → unexplained even vs deep nulls → honest WARN with escalation.")
    ok = zeta_ok && null_ok && sweep_ok && env_ok # detector validity + regime-robust absence + envelope family; the AB verdict is the headline
    reg_tail = isempty(reg_rows) ? "" :
        @sprintf("; sweep: %s%s", reg_all_absent ? "bumps within regime-matched nulls → lattice artifact, ABSENT regime-robust" :
                                   reg_any_present ? "PRESENT at a regime (unexplained — deepen)" :
                                                     "MARGINAL above regime nulls (unexplained → WARN, deepen)",
                 isempty(deep_info) ? "" :
                     @sprintf(" → deepened: %s", join([@sprintf("[%s] %.1f vs P95 %.1f → %s", di[1], di[2], di[3], di[5]) for di in deep_info], ", ")))
    log_result(@sprintf(" Test H1: ζ control %s, null ceiling %.1f, AB max prime-SNR %.1f (threshold %.0f) → fingerprint %s%s → %s",
                        zeta_ok ? "validated" : "NOT validated", max_snr_null,
                        isempty(snrs_ab) ? 0.0 : maximum(snrs_ab), threshold,
                        fp_present ? "PRESENT" : fp_marginal ? "MARGINAL" : "absent",
                        reg_tail, ok ? msg(cfg, "pass") : msg(cfg, "warn")))
    return ok
end

# ── H2: Weyl-law density test on the RAW (never-unfolded) spectrum ─────
# The local window unfolding used everywhere else FORCES mean spacing 1 and
# erases exactly the growth-law information this test restores.
function hp_h02_weyl_law(cfg::HPConfig, zeta_zeros::Vector{Float64})
    _mr_gate_head(2, "WEYL-DOS",
                  "Weyl-law density — raw N(E) of the AB-cloud (no unfolding)",
                  "ζ-type {E·lnE, E, 1} counting ansatz vs the natural lattice DOS — R²/AICc showdown")

    L = cfg.hp_L_weyl
    seed = cfg.hp_seed + 101
    prog_update(0.05, "H2: raw spectrum (with vortices)")
    raw = _hp_spectrum(cfg, _hp_std_config(cfg, L, seed))
    prog_update(0.45, "H2: vortex-free lattice reference")
    ref = _hp_spectrum(cfg, ABCloudConfig(L, L, Vortex[], cfg.ab_alpha_test16,
                                          cfg.ab_t, :open, 0.0, seed + 1, :monumental))
    pos = filter(>(1e-9), raw) # positive branch of the RAW spectrum
    n_grid = clamp(cfg.hp_weyl_grid, 20, 400)
    Eg = collect(range(pos[1], pos[end]; length = n_grid))
    N_raw = Float64[searchsortedlast(pos, E) for E in Eg]
    N_ref = Float64[searchsortedlast(ref, E) for E in Eg]
    n = length(Eg)
    @printf(" Raw spectrum: %d×%d, %d levels total, positive branch %d levels on E ∈ [%.4f, %.4f]\n",
            L, L, length(raw), length(pos), pos[1], pos[end])
    @printf(" Staircase: %d grid points | models fitted on the SAME grid\n", n)

    # Model A — the ζ (Riemann–Weil) counting shape with FREE coefficients:
    # N̄(T) = (T/2π)ln(T/2π) − T/2 + 7/8 is EXACTLY the basis {T·lnT, T, 1}.
    XA = [E * log(E) for E in Eg]  # column 1
    XA = hcat(XA, Eg, ones(Float64, n))
    cA, rssA, r2A = _hp_linlsq(XA, N_raw)
    aiccA = _hp_aicc(n, rssA, 3)
    # Model B — the natural lattice DOS: the vortex-free cumulative spectrum
    # rescaled (2 free parameters: amplitude + offset). This is the "ordinary
    # lattice physics" hypothesis (van-Hove/Dirac structure, bounded band).
    XB = hcat(N_ref, ones(Float64, n))
    cB, rssB, r2B = _hp_linlsq(XB, N_raw)
    aiccB = _hp_aicc(n, rssB, 2)
    daicc = aiccA - aiccB
    winner = daicc > 10 ? "LATTICE DOS (Model B)" :
             daicc < -10 ? "ζ-type E·lnE counting (Model A)" : "INCONCLUSIVE (|ΔAICc| ≤ 10)"
    @printf("\n Model A (ζ-type):  N(E) = %.4g·E·lnE %+ .4g·E %+ .4g   R² = %.5f  AICc = %.1f\n",
            cA[1], cA[2], cA[3], r2A, aiccA)
    @printf("   (ζ's own Weyl coefficient would be 1/2π ≈ 0.1592 — here the coefficient is FREE: this is a shape test)\n")
    @printf(" Model B (lattice): N(E) = %.4g·N_ref(E) %+ .4g                R² = %.5f  AICc = %.1f\n",
            cB[1], cB[2], r2B, aiccB)
    @printf(" ΔAICc (A−B) = %+.1f  (|Δ| > 10 = decisive; negative favors the ζ ansatz)\n", daicc)
    _mr_status("◆", "gold", "RAW density follows: " * winner)

    rec = Tuple{String,Bool,String}[]
    fits_ok = n >= 30 && isfinite(r2A) && isfinite(r2B)
    push!(rec, ("both fits computed", fits_ok, @sprintf("n = %d grid points, models A (3-par) / B (2-par)", n)))
    push!(rec, ("fit quality floor", min(r2A, r2B) >= 0.95,
        @sprintf("R²_A = %.5f, R²_B = %.5f (floor 0.95)", r2A, r2B)))
    push!(rec, ("decisive separation", abs(daicc) > 10, @sprintf("ΔAICc = %+.1f", daicc)))
    push!(rec, ("winner (headline)", true,
        daicc > 0 ? @sprintf("lattice DOS wins by %.1f AICc — raw density is ORDINARY lattice physics", daicc) :
                    @sprintf("ζ-type ansatz wins by %.1f AICc — raw density carries the T·lnT shape", -daicc)))

    hc_verdict_table(cfg, "Test H2", rec; pass_label = "HP audit")

    if REP.current !== nothing
        p = RepPlot(@sprintf("H2 — raw N(E): R²_A=%.4f vs R²_B=%.4f, ΔAICc=%+.1f (%s)",
                             r2A, r2B, daicc, winner), "E (hopping units)", "cumulative count N(E)")
        add_series!(p, "raw N(E) staircase", Eg, N_raw, 's')
        add_series!(p, "Model A: a·E·lnE + b·E + c", Eg, XA * cA, 'l')
        add_series!(p, "Model B: s·N_ref(E) + o", Eg, XB * cB, 'l')
        rep_plot!(p)
    end
    rep_note!("Model A embeds the Riemann–Weil smooth counting form N̄(T)=(T/2π)ln(T/2π)−T/2+7/8 with free " *
              "coefficients — a pure shape test. Model B is the vortex-free Hofstadter cumulative spectrum " *
              "(same L, α, t; W=0): the 'ordinary lattice' hypothesis. The everywhere-used local-mean " *
              "unfolding would force unit mean spacing and make this comparison impossible — that is why the " *
              "test runs on the raw spectrum.")
    ok = fits_ok && min(r2A, r2B) >= 0.95 && abs(daicc) > 10
    log_result(@sprintf(" Test H2: R²_A=%.5f, R²_B=%.5f, ΔAICc=%+.1f → %s → %s",
                        r2A, r2B, daicc, winner, ok ? msg(cfg, "pass") : msg(cfg, "warn")))
    return ok
end

# ── H3: power-law exponent on the REAL lattice spectrum ────────────────
function hp_h03_power_law(cfg::HPConfig, zeta_zeros::Vector{Float64})
    _mr_gate_head(3, "POWER-LAW",
                  "Power-law exponent of the REAL spectrum (dictionary falsification)",
                  "Eₙ ~ n^p on the independently-diagonalized lattice; p→2 (dictionary) vs p=1/2 (Dirac) vs p=1 (band)")

    ladder = cfg.hp_L_ladder
    invL = Float64[]; p_low = Float64[]; p_bulk = Float64[]
    se_low = Float64[]; se_bulk = Float64[]
    r2_low = Float64[]; r2_bulk = Float64[]
    for (k, L) in enumerate(ladder)
        prog_update(0.02 + 0.75 * (k - 1) / max(length(ladder), 1), @sprintf("H3: L=%d", L))
        raw = _hp_spectrum(cfg, _hp_std_config(cfg, L, cfg.hp_seed + 200 + L))
        pos = filter(>(1e-9), raw) # positive branch; the α=1/2 zero tower / mid-band exact zeros excluded
        M = length(pos)
        (M >= 40) || (println(" L=$L: only $M positive levels — rung skipped"); continue)
        i_lo = (max(1, round(Int, 0.02 * M) + 1), max(1, round(Int, 0.20 * M)))
        i_bu = (max(1, round(Int, 0.30 * M)), max(2, round(Int, 0.70 * M)))
        # window fits: log E = p·log n + c, n = 1-based rank in the positive branch.
        # (a fixed shift n−q with q < 1 changes log n by O(q/n) — negligible beyond
        # the first few ranks, which the 2% window trim already excludes.)
        function _fit(a::Int, b::Int)
            ns = collect(Float64, a:b)
            a0, b0, R2, se, _ = linreg(log.(ns), log.(pos[a:b]))
            return b0, se, R2
        end
        pl, sl, rl = _fit(i_lo[1], i_lo[2])
        pb, sb, rb = _fit(i_bu[1], i_bu[2])
        push!(invL, 1.0 / L); push!(p_low, pl); push!(se_low, sl); push!(r2_low, rl)
        push!(p_bulk, pb); push!(se_bulk, sb); push!(r2_bulk, rb)
        @printf(" L=%2d: M=%4d | low window [%d..%d]: p̂=%.4f±%.4f (R²=%.5f) | bulk [%d..%d]: p̂=%.4f±%.4f (R²=%.5f)\n",
                L, M, i_lo[1], i_lo[2], pl, sl, rl, i_bu[1], i_bu[2], pb, sb, rb)
        log_comp(@sprintf(" H3: L=%d p_low=%.4f (R²=%.5f) p_bulk=%.4f (R²=%.5f)", L, pl, rl, pb, rb))
        ab_gc!() # suite convention: explicit collection after every heavy solve (OOM guard)
    end
    @printf("\n Theory anchors: dictionary (n−q)² → p = 2 | 2D Dirac DOS (N(E)∝E²) → p = 1/2 | quadratic band bottom → p = 1\n")
    println(" (the Eₙ=(n−q)² dictionary of lab E8 is a 1D-ring identity — the REAL 2D spectrum decides)")

    # ── Dirac-cone readout (reviewer observation 2026-09-06, promoted to a
    # headline row): the low window (vortex-dominated near-edge, where the
    # dictionary WOULD live if it were real) sits much closer to the 2D-Dirac
    # anchor 1/2 than the bulk — worth stating on its own line, not burying
    # it inside "REJECTED".
    d_dir_low = isempty(p_low) ? NaN : mean(abs.(p_low .- 0.5))
    d_dir_bu = isempty(p_bulk) ? NaN : mean(abs.(p_bulk .- 0.5))
    if isfinite(d_dir_low) && isfinite(d_dir_bu)
        @printf(" Physics readout: mean |p̂ − 1/2| = %.3f (low window) vs %.3f (bulk) → %s\n",
                d_dir_low, d_dir_bu,
                d_dir_low < d_dir_bu ?
                    "the near-edge spectrum hugs the 2D-Dirac cone anchor (vortex-dominated DOS) — the honest alternative to the rejected dictionary" :
                    "no special proximity of the low window to the Dirac anchor")
    end

    # L→∞ extrapolation (Test-38 hardcore A1 scheme): p̂(L) = p_∞ + c/L
    function _extrap(ps::Vector{Float64})
        (length(ps) >= 3) || return NaN, NaN
        a, b, R2, se, _ = linreg(invL, ps)
        return a, se # intercept = p_∞
    end
    p_inf_lo, se_inf_lo = _extrap(p_low)
    p_inf_bu, se_inf_bu = _extrap(p_bulk)
    @printf("\n L→∞ extrapolation:  low window:  p_∞ = %.4f ± %.4f\n", p_inf_lo, se_inf_lo)
    @printf("                     bulk window: p_∞ = %.4f ± %.4f\n", p_inf_bu, se_inf_bu)
    dic_dev_lo = abs(p_inf_lo - 2.0)
    dic_dev_bu = abs(p_inf_bu - 2.0)
    dic_supported = (dic_dev_bu < 0.25 || dic_dev_lo < 0.25)
    _mr_status(dic_supported ? "◆" : "●", dic_supported ? "gold" : "accent",
               "Dictionary check (|p_∞ − 2|): low = " * @sprintf("%.3f", dic_dev_lo) *
               ", bulk = " * @sprintf("%.3f", dic_dev_bu) * " → " *
               (dic_supported ? "SUPPORTED (would be a headline)" :
                "REJECTED — expected honest negative: the real spectrum is not (n−q)² lattice physics"))

    # ── per-L decisive evidence (reviewer sync 2026-09-06): the unstable
    # L→∞ fit must not carry the verdict — with per-L se ≈ 0.001–0.009 and
    # every p̂ ≈ 0.3–0.7, EACH rung already rejects p = 2 by ≫ 5σ on its own.
    perL_decisive = false
    perL_min_dev = NaN
    perL_min_sigma = NaN
    if !isempty(p_low) && !isempty(p_bulk)
        devs = vcat([abs(p - 2.0) for p in p_low], [abs(p - 2.0) for p in p_bulk])
        sigs = vcat([(2.0 - p) / max(se, 1e-12) for (p, se) in zip(p_low, se_low)],
                    [(2.0 - p) / max(se, 1e-12) for (p, se) in zip(p_bulk, se_bulk)])
        perL_min_dev = minimum(devs)
        perL_min_sigma = minimum(sigs)
        # decisive = every rung sits at least half an anchor-unit below p = 2
        # AND at least 5σ away (a genuine approach to the dictionary would
        # break either condition and flip the test to WARN — real pass/fail
        # power is preserved)
        perL_decisive = perL_min_dev > 0.5 && perL_min_sigma >= 5.0
    end

    rec = Tuple{String,Bool,String}[]
    r2min_lo = isempty(r2_low) ? 0.0 : minimum(r2_low)
    r2min_bu = isempty(r2_bulk) ? 0.0 : minimum(r2_bulk)
    push!(rec, ("low-window fit quality", r2min_lo >= 0.98, @sprintf("min R² over ladder = %.5f (floor 0.98)", r2min_lo)))
    push!(rec, ("bulk-window fit quality", r2min_bu >= 0.98, @sprintf("min R² over ladder = %.5f (floor 0.98)", r2min_bu)))
    # per-L falsification — THE decisive row: min |p̂−2| across all rungs and
    # windows, in units of the per-rung standard error
    push!(rec, ("per-L falsification (decisive)", perL_decisive,
        isfinite(perL_min_dev) ?
            @sprintf("min |p̂−2| = %.3f at ≥ %.0fσ (every rung/window; se ≤ %.4f) — the rejection does NOT rest on the L→∞ extrapolation",
                     perL_min_dev, perL_min_sigma, max(maximum(se_low, init = 0.0), maximum(se_bulk, init = 0.0))) :
            "needs ≥ 1 ladder rung"))
    # L→∞ extrapolation — INFORMATIONAL note (reviewer sync): an unstable
    # extrapolation (se ≫ estimate, non-monotone rung scatter) is a property
    # of the 5-point linear-in-1/L fit, NOT a physics alarm; the verdict is
    # already carried by the per-L row above. Row fails only when the ladder
    # is too short to extrapolate at all.
    extrap_finite = isfinite(p_inf_bu) && isfinite(se_inf_bu)
    extrap_stable = extrap_finite && se_inf_bu < 0.15
    push!(rec, ("L→∞ extrapolation (note)", extrap_finite,
        !extrap_finite ? "needs ≥ 3 ladder rungs" :
        extrap_stable ?
            @sprintf("stable: p_∞ = %.4f ± %.4f (se limit 0.15)", p_inf_bu, se_inf_bu) :
            @sprintf("UNSTABLE (informational): p_∞ = %.4f ± %.4f, se ≫ estimate — non-monotone rung scatter; the verdict rests on the per-L fits, NOT on this extrapolation (reviewer sync 2026-09-06)",
                     p_inf_bu, se_inf_bu)))
    # dictionary verdict — semantics synchronized with H1/H7 (reviewer action
    # 2026-09-06): a REJECTED dictionary is the EXPECTED honest negative
    # (same status as H1's absent fingerprint / H7's zero correlation), so
    # the row is true either way and carries the headline; SUPPORTED would be
    # a discovery headline. Only method rows above can fail the test.
    push!(rec, ("dictionary verdict", true,
        dic_supported ? @sprintf("SUPPORTED — |p_∞−2|: low %.3f / bulk %.3f (HEADLINE: the toy ring dictionary as real lattice physics)",
                                 dic_dev_lo, dic_dev_bu) :
                        @sprintf("REJECTED (expected honest negative, status synced with H1/H7) — |p_∞−2|: low %.3f / bulk %.3f; the real 2D spectrum is not (n−q)² lattice physics",
                                 dic_dev_lo, dic_dev_bu)))
    push!(rec, ("Dirac-cone readout (low window)", true,
        (isfinite(d_dir_low) && isfinite(d_dir_bu)) ?
            (d_dir_low < d_dir_bu ?
                @sprintf("mean |p̂−1/2|: low %.3f < bulk %.3f → the near-edge (vortex-dominated) spectrum is Dirac-cone-like, not dictionary-like — reviewer observation 2026-09-06, promoted to a headline",
                         d_dir_low, d_dir_bu) :
                @sprintf("mean |p̂−1/2|: low %.3f vs bulk %.3f — no special Dirac proximity", d_dir_low, d_dir_bu)) :
            "no ladder rungs fitted"))

    hc_verdict_table(cfg, "Test H3", rec; pass_label = "HP audit")

    if REP.current !== nothing && !isempty(invL)
        x_hi = maximum(invL)
        p = RepPlot(@sprintf("H3 — exponent p̂(L) vs 1/L: per-L min|p̂−2|=%.3f (≥%.0fσ); p_∞ note: low=%.3f±%.3f, bulk=%.3f±%.3f",
                             perL_min_dev, perL_min_sigma, p_inf_lo, se_inf_lo, p_inf_bu, se_inf_bu),
                    "1/L", "exponent p̂")
        length(invL) >= 2 && begin
            add_series!(p, "p̂ low window", invL, p_low, 's')
            add_series!(p, "p̂ bulk window", invL, p_bulk, 's')
            add_series!(p, "low extrapolation", [0.0, x_hi],
                        [p_inf_lo, p_inf_lo + (p_low[end] - p_inf_lo) * invL[end] / max(invL[end], 1e-12)], 'l')
            add_series!(p, "bulk extrapolation", [0.0, x_hi],
                        [p_inf_bu, p_inf_bu + (p_bulk[end] - p_inf_bu) * invL[end] / max(invL[end], 1e-12)], 'l')
        end
        for (pv, nm) in [(2.0, "dictionary p=2"), (1.0, "quadratic band p=1"), (0.5, "2D Dirac p=1/2")]
            add_series!(p, nm, [0.0, x_hi], [pv, pv], 'l')
        end
        rep_plot!(p)
    end
    rep_note!("Fitting the REAL spectrum (not the toy ring of lab E8) answers the reviewer's question " *
              "directly: if the (n−q)² dictionary were the lattice physics, p̂(L) would extrapolate to 2. " *
              "The honest 2D alternatives are p = 1/2 (Dirac cone: N(E) ∝ E² near E = 0) in the low window " *
              "and p ≈ 1 (constant DOS of a quadratic band) in the bulk — both falsify the dictionary claim. " *
              "VERDICT SEMANTICS (reviewer sync 2026-09-06): a REJECTED dictionary is the EXPECTED honest " *
              "negative and PASSES the audit exactly like H1's absent fingerprint and H7's zero correlation " *
              "(one and the same outcome class must not split into PASS and WARN across tests); the test fails " *
              "only on method grounds — fit quality below floor, too few rungs, or the spectrum actually " *
              "approaching p = 2. The unstable L→∞ extrapolation (5 rungs, non-monotone scatter, se ≫ estimate) " *
              "is reported as an INFORMATIONAL note because the verdict rests on the per-L fits, each ≫5σ from " *
              "the dictionary anchor; the Dirac-cone proximity of the low window is stated as its own physics " *
              "headline rather than being buried inside the rejection.")
    ok = r2min_lo >= 0.98 && r2min_bu >= 0.98 && perL_decisive && extrap_finite
    # v23.6: extrap_finite added — the table's "L→∞ (note)" row must never
    # disagree with the runner verdict (needs ≥ 3 ladder rungs; ALWAYS true at
    # the real-scale 5-rung ladder, so real-scale semantics are unchanged;
    # the done-line, the aggregate line and the runner now share one verdict). && extrap_finite
    # v23.6: extrap_finite added — the table's "L→∞ (note)" row must never
    # disagree with the runner verdict (needs ≥ 3 ladder rungs; ALWAYS true at
    # the real-scale 5-rung ladder, so real-scale semantics are unchanged;
    # the done-line, the aggregate line and the runner now share one verdict).
    log_result(@sprintf(" Test H3: per-L min|p̂−2| = %.3f (≥ %.0fσ), p_∞ note: low=%.3f±%.3f / bulk=%.3f±%.3f → dictionary %s (expected negative) → %s",
                        perL_min_dev, perL_min_sigma, p_inf_lo, se_inf_lo, p_inf_bu, se_inf_bu,
                        dic_supported ? "supported" : "REJECTED",
                        ok ? msg(cfg, "pass") : msg(cfg, "warn")))
    return ok
end

# ═══════════════════════════════════════════════════════════════════════════
# GROUP B (cont.) — critical-q sharpness — and GROUP C — ensemble/stability
# ═══════════════════════════════════════════════════════════════════════════

# ── H4: critical-q sharpness scan ──────────────────────────────────────
# Fixed vortex positions across the grid (only the CHARGE varies), two
# independent disorder seeds per point → profile + noise floor. Sharpness =
# prominence of the largest profile deviation from a quadratic baseline,
# in units of the noise floor. A claimed critical q predicts a spike; a
# smooth profile falsifies the "critical line" analogy.
function hp_h04_critical_q(cfg::HPConfig, zeta_zeros::Vector{Float64})
    _mr_gate_head(4, "CRITICAL-Q",
                  "Critical-q sharpness scan — is GUE quality peaked at a critical charge?",
                  "Fine q-grid, fixed vortex positions, 2 disorder seeds per point → profile vs noise floor")

    L = cfg.hp_L
    n_q = clamp(cfg.hp_n_q_grid, 5, 81)
    qgrid = collect(range(cfg.hp_q_min, cfg.hp_q_max; length = n_q))
    # FIXED vortex positions for every q (only the charge moves) — otherwise a
    # per-q re-placement would add placement noise on top of the q-response.
    pos_fixed = _hp_std_vortices(cfg, L, MersenneTwister(cfg.hp_seed + 300))
    @printf(" Scan: %d charges on q ∈ [%.3f, %.3f] × 2 seeds, %d×%d lattice, %d vortices (fixed positions)\n",
            n_q, qgrid[1], qgrid[end], L, L, length(pos_fixed))
    println(" Claimed criticals marked on the profile: q = 1/2 (self-dual analog), 0.3 (toy dictionary), 1.0 (Byers–Yang)")
    # v23.6 DOMAIN GUARD (reviewer round 3, №4): run_20260906_185208 scanned
    # q ∈ [5, 81] with the claimed criticals 0.3/0.5/1.0 ALL outside — the
    # location check degraded silently (any resonance is trivially "off 55% of
    # span"). A domain that contains no claimed critical makes this test's
    # location row INFORMATION-FREE → the row now fails honestly and the test
    # WARNs until the default domain [0.05, 1.0] (menu item 3) is restored.
    claimed_all = [0.5, 0.3, 1.0]
    domain_covers = any(qc -> qc >= qgrid[1] && qc <= qgrid[end], claimed_all)
    domain_covers || println(" ⚠ DOMAIN GUARD (v23.6): NONE of the claimed criticals (0.3, 0.5, 1.0) lies inside the scan domain — the location check below is DEGENERATE. Restore q ∈ [0.05, 1.0] (HP parameter menu item 3) to test the claimed criticals.")

    ks_prof = Float64[] # mean KS_D profile (lower = better GUE match)
    r_prof = Float64[]  # mean ⟨r⟩ profile
    noise_ks = Float64[]# per-point |seed1 − seed2|/√2 noise floor
    all_finite = true
    for (k, q) in enumerate(qgrid)
        prog_update(0.02 + 0.82 * (k - 1) / max(n_q, 1), @sprintf("H4: q=%.3f (%d/%d)", q, k, n_q))
        vs = [Vortex(v.x, v.y, q * sign(v.q)) for v in pos_fixed] # SAME positions, charge q
        ds = Float64[]
        rs = Float64[]
        for rep in 1:2
            c = ABCloudConfig(L, L, vs, cfg.ab_alpha_test16, cfg.ab_t, :open,
                              ab_w_eff(cfg), cfg.hp_seed + 400 + 10 * k + rep, :monumental)
            ev = _hp_spectrum(cfg, c)
            band = central_band_eigs(ev, cfg.ab_center_fraction)
            D, _ = ks_test(_hp_unit_spacings(band))
            r, _ = mean_adjacent_spacing_ratio(band)
            (isfinite(D) && isfinite(r)) || (all_finite = false)
            push!(ds, D); push!(rs, r)
        end
        push!(ks_prof, mean(ds)); push!(r_prof, mean(rs))
        push!(noise_ks, abs(ds[1] - ds[2]) / √2)
        log_comp(@sprintf(" H4: q=%.4f KS_D=[%.4f, %.4f] ⟨r⟩=[%.4f, %.4f]",
                          q, ds[1], ds[2], rs[1], rs[2]))
        ab_gc!() # suite convention: explicit collection after every heavy solve (OOM guard)
    end

    # prominence of the sharpest KS_D dip vs the cubic baseline
    qf = Float64.(qgrid)
    coef = polyfit(qf, ks_prof, 3) # cubic baseline: generic smooth curvature of KS_D(q); a NARROW spike survives it
    base = [polyval(coef, q) for q in qf]
    dip_res = base .- ks_prof # positive = the profile DIPS below baseline (unusually good match)
    k_dip = argmax(dip_res)
    q_star = qf[k_dip]
    σ_floor = mean(noise_ks)
    σ_floor = σ_floor > 1e-12 ? σ_floor : 1e-12
    z_dip = dip_res[k_dip] / σ_floor
    # width of the feature: contiguous run around k_dip where the dip stays above
    # half prominence. A genuine critical point is NARROW (≪ scan span); smooth
    # baseline-mismatch curvature produces wide residual humps. Both criteria
    # (prominence z AND width fraction) must hold — z alone false-alarms on a
    # too-rigid baseline (measured on the toy smoke run: z = 13 at width 1.0).
    half = dip_res[k_dip] / 2.0
    i_lo = k_dip
    while i_lo > 1 && dip_res[i_lo - 1] >= half
        i_lo -= 1
    end
    i_hi = k_dip
    while i_hi < length(dip_res) && dip_res[i_hi + 1] >= half
        i_hi += 1
    end
    dq = qf[2] - qf[1]
    width_frac = (i_hi - i_lo + 1) * dq / (qf[end] - qf[1])
    claimed = [0.5, 0.3, 1.0]
    nearest = claimed[argmin(abs.(claimed .- q_star))]
    sharp = (z_dip >= 3.0) && (width_frac <= 0.35)
    # LOCATION HONESTY (reviewer sync 2026-09-06): the scan certifies the
    # EXISTENCE of sharp structure, never the critical-line analogy — a
    # resonance away from every claimed critical is 'real but UNPREDICTED'.
    # Coincidence window: 2 grid steps (the profile resolution limit).
    on_claim = abs(q_star - nearest) <= 2.0 * dq
    @printf("\n KS_D profile: min %.4f at q* = %.3f | cubic-baseline dip = %.4f | noise floor σ = %.4f\n",
            ks_prof[k_dip], q_star, dip_res[k_dip], σ_floor)
    _mr_status(sharp ? "◆" : z_dip >= 3.0 ? "⚠" : "●",
               sharp ? "gold" : z_dip >= 3.0 ? "warn" : "accent",
               "Sharpness: z = dip/σ = " * @sprintf("%.2f", z_dip) *
               ", half-prominence width = " * @sprintf("%.2f", width_frac) * " of the scan span → " *
               (sharp ? "SHARP feature — narrow dip beyond the seed noise" :
                (z_dip >= 3.0 ? "wide residual hump (z ≥ 3 but width > 0.35 span) — baseline curvature, not a critical point" :
                                "SMOOTH profile — no critical-q signature above the noise floor (z < 3)")))
    _loc_txt = on_claim ? "COINCIDES with the claimed critical (within 2 grid steps)" :
               @sprintf("OFF-PREDICTION (%.0f%% of the scan span) — real but UNPREDICTED, the critical-line analogy is NOT corroborated",
                        100 * abs(q_star - nearest) / (qf[end] - qf[1]))
    _mr_status(on_claim ? "◆" : "●", on_claim ? "gold" : "accent",
               "Nearest claimed critical to q*: q = " * @sprintf("%.1f", nearest) *
               " (|q* − q_c| = " * @sprintf("%.3f", abs(q_star - nearest)) * ") → " * _loc_txt)
    @printf(" ⟨r⟩ profile: mean %.4f, range [%.4f, %.4f] (smooth drift expected — ⟨r⟩ is a coarse statistic)\n",
            mean(r_prof), minimum(r_prof), maximum(r_prof))

    rec = Tuple{String,Bool,String}[]
    push!(rec, ("scan completed", all_finite, @sprintf("%d q-points × 2 seeds, all metrics finite", n_q)))
    push!(rec, ("noise floor resolved", σ_floor > 1e-9,
        @sprintf("σ(noise) = %.5f from per-point seed pairs", σ_floor)))
    push!(rec, ("sharp-feature verdict", true,
        sharp ? @sprintf("SHARP: z = %.2f at q* = %.3f, width %.2f span (nearest claimed %.1f)", z_dip, q_star, width_frac, nearest) :
                @sprintf("SMOOTH: max z = %.2f, width %.2f span — no narrow critical-q feature", z_dip, width_frac)))
    push!(rec, ("location vs claimed criticals", on_claim || domain_covers,
        !domain_covers ?
            @sprintf("DEGENERATE (v23.6 guard): claimed criticals 0.3/0.5/1.0 all OUTSIDE the scan domain [%.3f, %.3f] — the off/coincide verdict carries no information; set the q-domain back to [0.05, 1.0] (menu item 3) and rerun", qgrid[1], qgrid[end]) :
        on_claim ? @sprintf("resonance at q* = %.3f COINCIDES with q_c = %.1f (within 2 grid steps) — supports the critical-line analogy",
                            q_star, nearest) :
                   @sprintf("resonance at q* = %.3f does NOT coincide with any claimed critical (nearest %.1f, off by %.3f = %.0f%% of span) → the sharp feature is real but UNPREDICTED — the analogy is NOT corroborated (reviewer sync 2026-09-06)",
                            q_star, nearest, abs(q_star - nearest), 100 * abs(q_star - nearest) / (qf[end] - qf[1]))))
    push!(rec, ("⟨r⟩ scan range", true,
        @sprintf("%.4f … %.4f across the grid", minimum(r_prof), maximum(r_prof))))

    hc_verdict_table(cfg, "Test H4", rec; pass_label = "HP audit")

    if REP.current !== nothing
        p = RepPlot(@sprintf("H4 — KS_D(q): %s (z = %.2f at q* = %.3f)",
                             sharp ? "sharp feature" : "smooth profile", z_dip, q_star),
                    "vortex charge q", "KS distance vs GUE surmise")
        add_series!(p, "KS_D (seed-averaged)", qf, ks_prof, 'L')
        add_series!(p, "cubic baseline", qf, base, 'l')
        for qc in (0.5, 0.3, 1.0)
            (qc >= qf[1] && qc <= qf[end]) && add_series!(p, @sprintf("claimed q_c=%.1f", qc),
                [qc, qc], [minimum(ks_prof) - 0.002, maximum(ks_prof) + 0.002], 'l')
        end
        rep_plot!(p)
        p2 = RepPlot("H4 — ⟨r⟩(q) profile (coarse cross-check)", "vortex charge q", "⟨r⟩")
        add_series!(p2, "⟨r⟩ (seed-averaged)", qf, r_prof, 'L')
        add_series!(p2, "GUE 0.5992", qf, fill(0.5992, n_q), 'l')
        rep_plot!(p2)
    end
    rep_note!("Design: vortex POSITIONS are frozen across the grid so the profile responds only to the charge; " *
              "two disorder seeds per point give the honest noise floor. Prominence = largest baseline-corrected " *
              "dip of the cubic-smoothed profile in units of that floor, AND the half-prominence width must stay " *
              "below 35% of the scan span — a wide residual hump is baseline curvature, not a critical point. " *
              "A smooth profile is the expected outcome for a generic vortex model and FALSIFIES the " *
              "'q plays the role of 1/2' analogy. LOCATION HONESTY (reviewer sync 2026-09-06): the scan answers " *
              "'is there sharp structure' — it does NOT answer 'does the structure sit where the theory needs " *
              "it'; a resonance away from every claimed critical is reported as real-but-unpredicted, and the " *
              "analog claim is scored by the dedicated location row. Noise-floor caveat: 2 seeds per point make " *
              "σ a 1-parameter estimate — z is indicative, not distribution-level proof.")
    ok = all_finite && σ_floor > 1e-9 && domain_covers # v23.6: a degenerate domain (no claimed critical inside) fails the test honestly
    log_result(@sprintf(" Test H4: %d q-points, KS_D min %.4f at q*=%.3f, z=%.2f → %s%s%s → %s",
                        n_q, ks_prof[k_dip], q_star, z_dip,
                        sharp ? "sharp" : "smooth",
                        on_claim ? "" : ", NOT at a claimed critical (real but unpredicted)",
                        domain_covers ? "" : ", DOMAIN DEGENERATE (no claimed critical inside) → guard",
                        ok ? msg(cfg, "pass") : msg(cfg, "warn")))
    return ok
end

# ── H5: large ensemble × parameter-regime showdown ─────────────────────
# (reviewer action 2026-09-06) The v23.3 first run measured the ensemble ONLY
# at the HP-standard point (sparse Nv=4, α=0.5): ⟨r⟩ in-band 87.5%, KS-vs-GUE
# 0/40 with a tiny realization scatter σ = 0.0087 — a REPRODUCIBLE miss, but
# is it a property of the MODEL or of the PARAMETER POINT? This audit runs a
# 2×2 factorial {vortex density × screening α} (regimes A–D, see HPRegime):
# every regime gets hp_n_ensemble independent configurations, and the
# headline compares a REGIME-ROBUST failure (model-class property) against a
# parameter artifact (recovery at ≥ 1 regime). W stays at the HP standard
# everywhere, so density and α are the ONLY moving levers.
function hp_h05_ensemble(cfg::HPConfig, zeta_zeros::Vector{Float64})
    regs = hp_regimes(cfg)
    n_reg = length(regs)
    plan = _hp5_plan(cfg) # v24.1: ONE budget plan (≤ 40 solves), shared with the cost estimator
    focus_d = cfg.hp_regime_mode === :regime_d # v24.2: FOCUS-D — single-regime deep run, ALL solves on [D]
    _mr_gate_head(5, focus_d ? "FOCUS-D" : "REGIME-2×2",
                  focus_d ?
                  "Focused regime-D deep run — ALL $(plan.total) solves on [D] combined (density + sharp-flux) × $(plan.E) configs" :
                  "Large ensemble × parameter-regime showdown — $(n_reg) regime(s) × $(plan.E) configs (≤ $(HP5_SOLVE_CAP)-solve budget)",
                  focus_d ?
                  "does regime [D]'s GUE pass survive N=$(plan.E) individual-level KS testing — or does it live on the median-D OR-clause alone?" :
                  "⟨r⟩/KS-D distributions per regime across {vortex density × screening α} — model property or parameter artifact?")

    L = cfg.hp_L
    N = plan.E # v24.1: budgeted ensemble size (the config's hp_n_ensemble is capped)
    band_hw = cfg.hp_gue_band
    α_on = cfg.hp_alpha_scan && n_reg > 1 && plan.Nα > 0 # v24.2 single source of truth: does the α-profile stage run?
    @printf(" GUE band: ⟨r⟩ ∈ [%.4f, %.4f] (monograph §11.1 ±%.3f) | KS pass: p > 0.01\n",
            0.5992 - band_hw, 0.5992 + band_hw, band_hw)
    @printf(" Regime pass rule: in-band ≥ %.0f%% AND (KS-pass ≥ 90%% OR median KS_D < 0.10) — scored PER regime\n",
            100 * cfg.hp_pass_fraction)
    println("   (v23.5 transparency, reviewer round 2: the RAW individual KS-pass % is always shown; a regime")
    @printf("    passing only via the median-D OR-clause is flagged 'OR-clause only' — 0%% individual passes on %d\n", N)
    println("    seeds is a systematic, reproducible deviation, not noise)")
    println(focus_d ?
            " Regime (v24.2 FOCUS-D: ALL budget on [D]; seeds continue the showdown's [D] stream 7 → $(N)):" :
            " Regimes (2×2 factorial, reviewer action 2026-09-06; W fixed at the HP standard):")
    for R in regs
        @printf("   [%s] %s — %s\n", R.key, R.tag, _hp_regime_desc(cfg, L, R))
    end
    @printf(" Cost: %d independent dense diagonalizations at %d×%d%s\n",
            plan.total, L, L,
            focus_d ? " (focused [D] run — switch hp_regime_mode to :showdown for the reviewer's 2×2)" :
            n_reg > 1 ? " (switch hp_regime_mode to :baseline for the single-regime fast run)" : "")
    plan.capped && @printf("   solve budget (v24.1 cap = %d, user 2026-09-09 «максимум 40»): config asked ≈ %d solves → plan %d regime(s) × %d configs%s = %d (per-config KS granularity 1/%d)\n",
                           HP5_SOLVE_CAP, plan.asked, n_reg, plan.E,
                           plan.Nα > 0 ? " + $(length(HP_ALPHA_GRID)) α-points × $(plan.Nα)" : "",
                           plan.total, plan.E)

    results = Any[] # one NamedTuple per regime (identical field layout)
    for (i, R) in enumerate(regs)
        @printf("\n ── Regime [%s] %s — %s\n", R.key, R.tag, _hp_regime_desc(cfg, L, R))
        rs = Float64[]; ksD = Float64[]; ksP = Float64[]
        n_band = 0
        for k in 1:N
            # v23.8 fraction plan: the ENSEMBLE owns 0.02…0.60 when the α-profile
            # follows (which owns 0.60…0.90); v24.2 focus runs have NO α-profile
            # → the ensemble owns 0.02…0.97 (the old ceiling made the bar JUMP).
            prog_update(0.02 + (α_on ? 0.58 : 0.95) * ((i - 1) + (k - 1) / max(N, 1)) / max(n_reg, 1),
                        @sprintf("H5 [%s]: realization %d/%d", R.key, k, N))
            # v24.2: canonical A..D seed BLOCK — [D] keeps its 30 000 offset in
            # EVERY mode, so a focus run's first 7 seeds are bit-for-bit the
            # 2×2's [D] realizations (direct continuity check across modes).
            i_blk = R.key == "A" ? 1 : R.key == "B" ? 2 : R.key == "C" ? 3 : 4
            seed = cfg.hp_seed + 10_000 * (i_blk - 1) + 500 + k # regime A: IDENTICAL to the published stream (bit-for-bit)
            c = _hp_regime_config(cfg, L, seed, R) # placement AND residual-ε pattern both vary
            ev = _hp_spectrum(cfg, c)
            band = central_band_eigs(ev, cfg.ab_center_fraction)
            n_band = length(band)
            r, _ = mean_adjacent_spacing_ratio(band)
            D, pv = ks_test(_hp_unit_spacings(band))
            push!(rs, r); push!(ksD, D); push!(ksP, pv)
            log_comp(@sprintf(" H5 [%s] realization %d (seed=%d): ⟨r⟩=%.4f KS_D=%.4f p=%.3f",
                              R.key, k, seed, r, D, pv))
            ab_gc!() # suite convention: explicit collection after every heavy solve (OOM guard)
        end
        m_r, s_r = mean(rs), std(rs)
        in_band = count(x -> abs(x - 0.5992) <= band_hw, rs)
        frac_band, ci_lo, ci_hi = _hp_wald_ci(in_band, N)
        n_ks = count(>(0.01), ksP)
        frac_ks, klo, khi = _hp_wald_ci(n_ks, N)
        @printf("   ⟨r⟩:  mean %.4f | σ %.4f | range [%.4f, %.4f] | median %.4f\n",
                m_r, s_r, minimum(rs), maximum(rs), median(rs))
        @printf("   in GUE band: %d/%d = %.1f%%  (95%% Wald CI %.1f%%–%.1f%%)\n",
                in_band, N, 100 * frac_band, 100 * ci_lo, 100 * ci_hi)
        @printf("   KS vs GUE (p > 0.01): %d/%d = %.1f%%  (95%% Wald CI %.1f%%–%.1f%%) | median KS_D %.4f\n",
                n_ks, N, 100 * frac_ks, 100 * klo, 100 * khi, median(ksD))
        push!(results, (R = R, rs = rs, ksD = ksD, m_r = m_r, s_r = s_r,
                        in_band = in_band, frac_band = frac_band, ci_lo = ci_lo, ci_hi = ci_hi,
                        n_ks = n_ks, frac_ks = frac_ks, klo = klo, khi = khi,
                        med_D = median(ksD), n_band = n_band))
        ab_gc!()
    end
    @printf(" → for comparison: the standard suite averages rest on n_realizations = %d (Tests 28/32 family)\n",
            cfg.ab_n_realizations)

    # ── regime synthesis: the reviewer's question, answered with a table ──
    pass_reg = [r.frac_band >= cfg.hp_pass_fraction &&
                (r.frac_ks >= 0.90 || r.med_D < 0.10) for r in results]
    # v23.5 (reviewer round 2): a regime can "pass" through the OR-clause while
    # 0% of its individual realizations pass KS — that is a SYSTEMATIC,
    # reproducible deviation (40 seeds!), not noise, and must not be hidden
    # behind the disjunction. Track CLEAN (no OR-clause) separately:
    clean_reg = [r.frac_band >= cfg.hp_pass_fraction && r.frac_ks >= 0.90 for r in results]
    n_pass = count(pass_reg)
    n_clean = count(clean_reg)
    pass_keys = [results[i].R.key for i in 1:n_reg if pass_reg[i]]
    clean_keys = [results[i].R.key for i in 1:n_reg if clean_reg[i]]
    or_keys = [results[i].R.key for i in 1:n_reg if pass_reg[i] && !clean_reg[i]]
    max_s_r = maximum(r.s_r for r in results)
    best_i = argmax([(r.frac_ks, r.frac_band) for r in results]) # primary: KS-pass, tie-break: in-band
    println("\n ── Regime synthesis (robust failure vs parameter-dependence vs finetuning?) ──")
    for (i, r) in enumerate(results)
        @printf("   [%s] %-30s ⟨r⟩ %.4f±%.4f | in-band %.1f%% | KS-pass %.1f%% (raw, individual) | median D %.4f → %s\n",
                r.R.key, r.R.tag * ",", r.m_r, r.s_r, 100 * r.frac_band, 100 * r.frac_ks, r.med_D,
                pass_reg[i] ? (clean_reg[i] ? "GUE REACHED (clean)" : "GUE reached — OR-clause only") : "misses GUE")
    end
    best = results[best_i]
    # v23.5 headline (reviewer round 2): "PARAMETER ARTIFACT … not a model
    # property" was too comforting — the only clean pass sits at the point
    # where BOTH levers are tuned simultaneously, which READS AS FINETUNING
    # (the Test-38 story), not as evidence against it. Say exactly that.
    # v24.2 FOCUS-D: the single-regime deep run gets its own decision-grade headlines.
    headline = focus_d ?
        (n_pass == 0 ?
         @sprintf("FOCUS-D MISS — regime [D] at the FULL N=%d ensemble misses GUE (in-band %d/%d, raw individual KS-pass %d/%d, median D %.4f): the N=7 near-pass does not survive full-power testing",
                  N, best.in_band, N, best.n_ks, N, best.med_D) :
         n_clean == 0 ?
         @sprintf("FOCUS-D, OR-CLAUSE ONLY — [D] 'reaches' GUE via median D < 0.10 alone at N=%d (raw individual KS-pass %d/%d): the 1/%d granularity excuse is gone — a real per-realization systematic remains",
                  N, best.n_ks, N, N) :
         @sprintf("FOCUS-D CLEAN PASS — [D] reaches GUE at raw individual level, N=%d (KS-pass %d/%d ≥ 90%%, in-band %d/%d): the combined regime (density + sharp-flux) is the model's genuine GUE candidate — the sparse α=0.5 baseline was the outlier",
                  N, best.n_ks, N, best.in_band, N)) :
        (n_pass == 0 ?
        @sprintf("ROBUST FAILURE — no regime reaches GUE across all %d tested regime(s): the failure is a MODEL-CLASS property (best attempt: [%s] %s)",
                 n_reg, best.R.key, _hp_regime_desc(cfg, L, best.R)) :
        n_clean == 0 ?
        @sprintf("PARAMETER-DEPENDENT, OR-CLAUSE ONLY — GUE is 'reached' at regime(s) %s but via the median-D clause ALONE (raw individual KS-pass ≈ 0%% everywhere) — the GUE claim does not survive individual-level testing at ANY regime",
                 join(pass_keys, ",")) :
        @sprintf("PARAMETER-DEPENDENT — GUE recovers at regime(s) %s, but CLEAN pass (raw individual KS-pass ≥ 90%%, no OR-clause) only at [%s] = %s; OR-clause-only: %s → GUE quality appears only at a specifically tuned parameter point — a finetuning story (Test-38 flavor), NOT evidence against it",
                 join(pass_keys, ","), join(clean_keys, ","),
                 join([_hp_regime_desc(cfg, L, results[i].R) for i in 1:n_reg if clean_reg[i]], " & "),
                 isempty(or_keys) ? "none" : join(or_keys, ",")))
    _hd = _mr_wrap(headline, _MR_W - 4)
    for (_i, _ln) in enumerate(_hd)
        println("  " * (_i == 1 ? _mr_c("◆ ", "gold") * _mr_c(_ln, "bold")
                                : _mr_c(_ln, "bold")))
    end

    # ── v23.6 α-PROFILE (reviewer round 3, №3): finetuning vs plateau ──
    # run_20260906_185208 showed the clean GUE pass rides on α = 25/900 in BOTH
    # densities ([C] and [D]) — so the story is about the SCREENING AXIS, not
    # the (Nv, α) pair. The missing experiment: GUE quality ALONG α at fixed
    # sparse Nv. PLATEAU (clean pass for every small α up to some α*) reads as
    # "the sharp-flux regime is GUE-universal — the published α = 0.5 baseline
    # is the outlier"; NARROW (clean only in a small window at 25/900) reads as
    # true finetuning. The α = 0.5 endpoint independently replicates regime A
    # from a DIFFERENT seed stream (internal consistency check).
    α_prof = NamedTuple[]
    α_class = ""
    if α_on # v24.2: single source of truth — never in the :regime_d focus (n_reg = 1)
        αgrid = HP_ALPHA_GRID
        Nα = plan.Nα # v24.1: ≤ 2 configs per α-point under the solve budget
        Nv_sparse = resolve_vortex_count(cfg)
        @printf("\n ── α-PROFILE (v23.6, finetuning vs plateau): %d α-points × %d configs at FIXED sparse Nv=%d — where along the screening axis does GUE live?\n",
                length(αgrid), Nα, Nv_sparse)
        println("   (clean pass across the small-α side → PLATEAU: 'sharp-flux regime is GUE-universal, the α=0.5 baseline is the outlier';")
        println("    clean pass only near 25/900 → NARROW: finetuning confirmed; the α=0.5 endpoint independently replicates regime A)")
        for (ai, α) in enumerate(αgrid)
            rs_a = Float64[]; ksD_a = Float64[]; ksP_a = Float64[]
            nb_a = 0
            for k in 1:Nα
                prog_update(0.60 + 0.30 * ((ai - 1) + (k - 1) / max(Nα, 1)) / max(length(αgrid), 1),
                            @sprintf("H5 α-profile: α=%.4f (%d/%d) config %d/%d", α, ai, length(αgrid), k, Nα))
                seed = cfg.hp_seed + 900_000 + 1_000 * ai + k # disjoint stream; α=0.5 endpoint ≠ regime-A stream on purpose
                vs_a = random_vortex_configuration(Nv_sparse, L, L; q_magnitude = resolve_q_magnitude(cfg),
                                                   enforce_neutrality = true,
                                                   rng = MersenneTwister(seed), place_at_centers = true)
                c_a = ABCloudConfig(L, L, vs_a, α, cfg.ab_t, :open, ab_w_eff(cfg), seed, :monumental)
                ev_a = _hp_spectrum(cfg, c_a)
                band_a = central_band_eigs(ev_a, cfg.ab_center_fraction)
                nb_a = length(band_a)
                r_a, _ = mean_adjacent_spacing_ratio(band_a)
                D_a, p_a = ks_test(_hp_unit_spacings(band_a))
                push!(rs_a, r_a); push!(ksD_a, D_a); push!(ksP_a, p_a)
                log_comp(@sprintf(" H5 α-profile α=%.4f config %d (seed=%d): ⟨r⟩=%.4f KS_D=%.4f p=%.3f",
                                  α, k, seed, r_a, D_a, p_a))
                ab_gc!()
            end
            n_ks_a = count(>(0.01), ksP_a)
            fb_a = count(x -> abs(x - 0.5992) <= band_hw, rs_a) / Nα
            push!(α_prof, (α = α, m_r = mean(rs_a), s_r = std(rs_a),
                           frac_ks = n_ks_a / Nα, n_ks = n_ks_a, med_D = median(ksD_a),
                           frac_band = fb_a, n_cfg = Nα))
            @printf("   α=%.4f: ⟨r⟩ %.4f±%.4f | in-band %.0f%% | KS-pass %d/%d = %.0f%% | median D %.4f → %s\n",
                    α, mean(rs_a), std(rs_a), 100 * fb_a, n_ks_a, Nα, 100 * n_ks_a / Nα, median(ksD_a),
                    n_ks_a / Nα >= 0.90 ? "clean GUE" : n_ks_a / Nα >= 0.5 ? "partial" : "misses GUE")
            ab_gc!()
        end
        # classification: the contiguous clean-pass PREFIX along the α-axis
        plateau_len = 0
        for a in α_prof
            a.frac_ks >= 0.90 || break
            plateau_len += 1
        end
        α_class = plateau_len == length(α_prof) ?
            "PLATEAU-ALL (clean GUE at EVERY tested α incl. 0.5 — cross-check: this CONTRADICTS regime A's failure at the α=0.5 point; investigate seeds/protocol before any claim)" :
            plateau_len >= 2 ?
            @sprintf("PLATEAU-LOW — clean GUE for all α ≤ %.4g (the whole sharp-flux side is GUE-universal); the published α=0.5 baseline is the OUTLIER, not the model", α_prof[plateau_len].α) :
            plateau_len == 1 ?
            @sprintf("NARROW — clean pass only at α = %.4g = 25/900 → the GUE claim is a FINETUNING story (confirmed along the screening axis)", α_prof[1].α) :
            "NONE — no clean pass anywhere on the α-line (contradicts regime C's clean pass?! check seeds/protocol)"
        println("  " * _mr_c("◆ α-PROFILE ", "gold") * _mr_c(α_class, "bold"))
    end

    rec = Tuple{String,Bool,String}[]
    push!(rec, ("solve plan ≤ $(HP5_SOLVE_CAP) eigensolves (v24.1 budget)", plan.total <= HP5_SOLVE_CAP,
        @sprintf("plan: %d config(s) × %d regime(s)%s = %d diagonalizations (user cap 2026-09-09 — the old «N ≥ 30» row retired: a cap must not be a silent auto-FAIL; per-config KS granularity 1/%d)",
                 N, n_reg, plan.Nα > 0 ? " + $(plan.Nα * length(HP_ALPHA_GRID)) α-profile" : "",
                 plan.total, N)))
    for (i, r) in enumerate(results)
        push!(rec, (@sprintf("[%s] %s", r.R.key, r.R.tag), pass_reg[i],
            @sprintf("⟨r⟩ %.4f±%.4f, in-band %.1f%% (%d/%d, CI %.1f–%.1f%%) | RAW individual KS-pass %.1f%% (%d/%d) | median D %.4f → %s",
                     r.m_r, r.s_r, 100 * r.frac_band, r.in_band, N, 100 * r.ci_lo, 100 * r.ci_hi,
                     100 * r.frac_ks, r.n_ks, N, r.med_D,
                     pass_reg[i] ? (clean_reg[i] ? "GUE reached (clean)" :
                                    "GUE reached via OR-clause ONLY — median D < 0.10 hides a systematic per-realization shift (raw KS-pass tells the truth)") :
                                   "misses GUE")))
    end
    push!(rec, ("⟨r⟩ scatter (worst regime)", max_s_r <= 0.02,
        @sprintf("max σ = %.4f over %d regime(s) (limit 0.02 — a lucky seed would show σ ≈ its own deviation)",
                 max_s_r, n_reg)))
    push!(rec, ("clean GUE pass (no OR-clause)", n_clean >= 1,
        n_clean == 0 ? @sprintf("NO regime passes the raw individual KS test at ≥ 90%% — every 'GUE reached' verdict rides the median-D clause (systematic per-realization deviation, %d seeds/regime)", N) :
        @sprintf("clean at [%s] (raw individual KS-pass ≥ 90%%); OR-clause-only at [%s]",
                 join(clean_keys, ","), isempty(or_keys) ? "none" : join(or_keys, ","))))
    push!(rec, ("synthesis (headline, never scored)", true, headline))
    # v23.6: α-profile row — a READOUT (headline), never scored: it qualifies
    # the finetuning narrative (plateau vs narrow) but the regime table above
    # remains the scored evidence.
    isempty(α_prof) || push!(rec, ("α-profile (headline, never scored)", true,
        @sprintf("%s — %s", α_class,
                 join([@sprintf("α=%.4f: KS-pass %.0f%% (%d/%d), median D %.4f, in-band %.0f%%",
                                a.α, 100 * a.frac_ks, a.n_ks, a.n_cfg, a.med_D, 100 * a.frac_band) for a in α_prof], "; "))))

    prog_update(1.0, "H5: verdict") # close the bar before the verdict panel replays
    hc_verdict_table(cfg, "Test H5", rec; pass_label = "HP audit")

    if REP.current !== nothing
        # ⟨r⟩ strip chart across regimes (sorted within each regime block)
        p = RepPlot(@sprintf("H5 — ⟨r⟩ across %d regime(s): %s", n_reg,
                             n_pass == 0 ? "failure ROBUST (model-class)" : "failure parameter-dependent (finetuning-flavored)"),
                    "realization # (blocks = regimes, sorted by ⟨r⟩ within block)", "⟨r⟩")
        for (i, r) in enumerate(results)
            add_series!(p, @sprintf("[%s] %s", r.R.key, r.R.tag),
                        collect(Float64((i - 1) * N + 1):Float64(i * N)), sort(r.rs), 's')
        end
        xspan = [1.0, Float64(N * n_reg)]
        add_series!(p, "GUE 0.5992", xspan, [0.5992, 0.5992], 'l')
        add_series!(p, "GUE band ±$(band_hw)", xspan, [0.5992 - band_hw, 0.5992 - band_hw], 'l')
        add_series!(p, "GUE band +$(band_hw)", xspan, [0.5992 + band_hw, 0.5992 + band_hw], 'l')
        rep_plot!(p)
        # KS-D per realization across regimes + the p = 0.01 critical distance
        d_crit = 1.63 / sqrt(max(results[end].n_band, 1)) # Stephens λ_c(p=0.01) ≈ 1.63 → D = λ/√n
        p2 = RepPlot("H5 — KS distance vs GUE per realization (regime blocks)",
                     "realization # (blocks = regimes)", "KS_D")
        for (i, r) in enumerate(results)
            add_series!(p2, @sprintf("[%s] KS_D", r.R.key),
                        collect(Float64((i - 1) * N + 1):Float64(i * N)), r.ksD, 's')
        end
        add_series!(p2, @sprintf("critical D at p=0.01 (n=%d)", results[end].n_band),
                    xspan, fill(d_crit, 2), 'l')
        rep_plot!(p2)
        # regime means summary
        p3 = RepPlot(@sprintf("H5 — regime means ⟨r⟩±σ: GUE reached in %d/%d regime(s), clean in %d", n_pass, n_reg, n_clean),
                     "regime (A=baseline, B=density, C=sharp-flux, D=combined)", "⟨r⟩")
        add_series!(p3, "mean ⟨r⟩ per regime", collect(1.0:Float64(n_reg)),
                    [r.m_r for r in results], 'L')
        add_series!(p3, "GUE 0.5992", [0.5, Float64(n_reg) + 0.5], [0.5992, 0.5992], 'l')
        add_series!(p3, "GUE band ±$(band_hw)", [0.5, Float64(n_reg) + 0.5],
                    [0.5992 - band_hw, 0.5992 - band_hw], 'l')
        add_series!(p3, "GUE band +$(band_hw)", [0.5, Float64(n_reg) + 0.5],
                    [0.5992 + band_hw, 0.5992 + band_hw], 'l')
        rep_plot!(p3)
        # v23.6: α-profile plots (KS-pass % and median D along the screening axis)
        isempty(α_prof) || begin
            Nv_sp = resolve_vortex_count(cfg)
            p5 = RepPlot(@sprintf("H5 — α-profile (v23.6): %s — individual KS-pass %% vs screening α at sparse Nv=%d", α_class, Nv_sp),
                         "screening length α", "individual KS-pass % (p > 0.01)")
            add_series!(p5, "KS-pass %", [a.α for a in α_prof], [100 * a.frac_ks for a in α_prof], 'L')
            add_series!(p5, "clean threshold 90%", [0.0, 0.5], [90.0, 90.0], 'l')
            rep_plot!(p5)
            p6 = RepPlot("H5 — α-profile: median KS_D vs screening α (small D = close to GUE; OR-clause bound 0.10)",
                         "screening length α", "median KS_D")
            add_series!(p6, "median KS_D", [a.α for a in α_prof], [a.med_D for a in α_prof], 'L')
            add_series!(p6, "OR-clause bound 0.10", [0.0, 0.5], [0.10, 0.10], 'l')
            rep_plot!(p6)
        end
    end
    rep_note!("Placement AND residual-disorder patterns vary across realizations (independent MersenneTwister " *
              "streams), so the scatter σ is the honest realization noise of the model, not a bootstrap " *
              "resample of one configuration; the Wald CI quantifies the binomial uncertainty of each in-band " *
              "fraction. REGIME DESIGN (reviewer action 2026-09-06): a PRE-REGISTERED 2×2 factorial — {sparse " *
              "Nv | monograph density Nv = L²/36 (the 25/900 = 2.78% anchor; the same lever that lifted the " *
              "Test-32 comparison row to GUE)} × {α = ab_alpha_test16 | sharp-flux α = 25/900 ≈ 0.0278 (the " *
              "ORIGINAL design default of ab_alpha_test16)}; regime A reproduces the published baseline " *
              "bit-for-bit (identical seed streams) and W stays at the HP standard everywhere. The headline " *
              "contrasts a REGIME-ROBUST failure (model-class property at every tested point) against a " *
              "PARAMETER-DEPENDENT outcome; the regime TABLE is the evidence, the 'best' regime is reported " *
              "for orientation, and best-of-4 selection is pre-registered, not post hoc. A model-class " *
              "property needs ≥ 90% of realizations inside the band at a regime. STATUS SEMANTICS v23.5 " *
              "(reviewer round 2): the test status is the strict AND of all scored rows — a regime that " *
              "misses GUE (e.g. the published baseline) propagates to the test status instead of being " *
              "silently overridden by the synthesis ('1 failed → WARN' and the final line now always agree). " *
              "A 'GUE reached' via the median-D OR-clause is flagged separately from a CLEAN pass, because " *
              "0/40→near-0% individual KS passes is a systematic, reproducible deviation, not noise; and the only " *
              "clean pass in the 2×2 sits at the doubly-tuned point (density AND sharp-flux together), which " *
              "reads as finetuning — consistent with the Test-38 story — rather than as evidence against it. " *
              "v23.6 α-PROFILE (reviewer round 3): run 185208 showed the clean pass rides on α = 25/900 in BOTH " *
              "densities ([C],[D]), so the missing experiment is the GUE-quality profile ALONG the screening axis " *
              "at fixed sparse Nv — α ∈ {25/900, 0.05, 0.1, 0.2, 0.35, 0.5} × ≤2 configs under the v24.1 ≤40-solve " *
              "budget on a disjoint seed stream. PLATEAU-LOW (clean for all α ≤ α*) reads as 'the sharp-flux side is " *
              "GUE-universal — the published α = 0.5 baseline is the outlier'; NARROW (clean only at 25/900) " *
              "confirms finetuning along the axis; the α = 0.5 endpoint independently replicates regime A from a " *
              "different stream (internal consistency check). The α-profile is a READOUT row (never scored) — " *
              "the regime table remains the scored evidence.")
    # STATUS SEMANTICS v23.5 (the reviewer's bug report, fixed at the root):
    # previously ok = … && n_pass >= 1 while the verdict table counted the
    # per-regime rows → "7 sub-checks, 1 failed → WARN" was silently overwritten
    # by "… → PASS" on the next line. The status is now the strict AND of every
    # SCORED row above (solve budget, all regimes, scatter, clean-pass); the
    # synthesis row is a headline and is never scored. A failing regime now
    # propagates to the test status; the synthesis TEXT explains the structure
    # of the failure instead of overriding the status.
    # v24.1: the «N ≥ 30» clause is RETIRED from the status — the budget caps
    # the plan at ≤ 40 solves, and a user cap must not double as an auto-FAIL
    # (its honesty lives in the printed granularity 1/N and the CI columns).
    ok = max_s_r <= 0.02 && all(pass_reg) && n_clean >= 1
    log_result(@sprintf(" Test H5: %d regime(s) × N=%d, GUE reached in %d/%d (clean: %s; OR-clause only: %s) → %s%s → %s",
                        n_reg, N, n_pass, n_reg,
                        isempty(clean_keys) ? "none" : join(clean_keys, ","),
                        isempty(or_keys) ? "none" : join(or_keys, ","),
                        n_pass == 0 ? "failure ROBUST (model-class)" : "failure PARAMETER-DEPENDENT (finetuning-flavored)",
                        isempty(α_prof) ? "" : @sprintf("; α-profile: %s", α_class),
                        ok ? msg(cfg, "pass") : msg(cfg, "warn")))
    return ok
end

# ── H6: self-adjointness / stability stress test ───────────────────────
function hp_h06_stability(cfg::HPConfig, zeta_zeros::Vector{Float64})
    _mr_gate_head(6, "HERMIT-STRESS",
                  "Self-adjointness & stability stress test around the H-P parameters",
                  "(a) open↔torus  (b) vortex/α jitter ×$(cfg.hp_jitter_trials)  (c) L-growth with hermiticity audit")

    L = cfg.hp_L
    ok_all = true

    # ── (a) boundary switch: the bulk window must be boundary-blind ──
    prog_update(0.04, "H6a: open vs torus")
    vs_base = _hp_std_vortices(cfg, L, MersenneTwister(cfg.hp_seed + 600))
    (iseven(L) && abs(cfg.ab_alpha_test16 * L - round(cfg.ab_alpha_test16 * L)) < 1e-10) ||
        (println(" (torus rung skipped: α·L = $(cfg.ab_alpha_test16 * L) ∉ ℤ at L=$L — boundary probe runs open-only)"))
    r_open = r_torus = NaN
    d_boundary = NaN
    if iseven(L) && abs(cfg.ab_alpha_test16 * L - round(cfg.ab_alpha_test16 * L)) < 1e-10
        ev_o = _hp_spectrum(cfg, ABCloudConfig(L, L, vs_base, cfg.ab_alpha_test16,
                                               cfg.ab_t, :open, ab_w_eff(cfg), cfg.hp_seed + 601, :monumental))
        ev_t = _hp_spectrum(cfg, ABCloudConfig(L, L, vs_base, cfg.ab_alpha_test16,
                                               cfg.ab_t, :torus, ab_w_eff(cfg), cfg.hp_seed + 601, :monumental))
        r_open, _ = mean_adjacent_spacing_ratio(central_band_eigs(ev_o, cfg.ab_center_fraction))
        r_torus, _ = mean_adjacent_spacing_ratio(central_band_eigs(ev_t, cfg.ab_center_fraction))
        d_boundary = abs(r_open - r_torus)
        @printf(" (a) boundary: ⟨r⟩ open = %.4f | torus = %.4f | |Δ| = %.4f (limit %.3f; edge states live OUTSIDE the bulk window)\n",
                r_open, r_torus, d_boundary, cfg.hp_gue_band)
    end
    a_ok = isfinite(d_boundary) && d_boundary <= cfg.hp_gue_band
    ok_all &= a_ok

    # ── (b) jitter: positions AND α, independent disorder each trial ──
    prog_update(0.20, "H6b: jitter trials")
    n_tr = cfg.hp_jitter_trials
    ev_base = _hp_spectrum(cfg, ABCloudConfig(L, L, vs_base, cfg.ab_alpha_test16,
                                              cfg.ab_t, :open, ab_w_eff(cfg), cfg.hp_seed + 602, :monumental))
    band_base = central_band_eigs(ev_base, cfg.ab_center_fraction)
    r_base, _ = mean_adjacent_spacing_ratio(band_base)
    bw = band_base[end] - band_base[1]
    nq = 50
    qlevels = collect(range(0.0, 1.0; length = nq))
    qbase = [band_base[1] + qv * bw for qv in qlevels] # quantile grid of the base band
    rng_j = MersenneTwister(cfg.hp_seed + 603)
    r_jit = Float64[]
    drift_max = 0.0
    jitter_finite = true
    for k in 1:n_tr
        n_tr > 0 || break
        vs_j = [Vortex(clamp(v.x + cfg.hp_pos_jitter * (rand(rng_j) * 2 - 1), 1.0, Float64(L) - 1.0),
                       clamp(v.y + cfg.hp_pos_jitter * (rand(rng_j) * 2 - 1), 1.0, Float64(L) - 1.0), v.q)
                for v in vs_base]
        α_j = cfg.ab_alpha_test16 + cfg.hp_alpha_jitter * (rand(rng_j) * 2 - 1)
        ev_j = _hp_spectrum(cfg, ABCloudConfig(L, L, vs_j, α_j, cfg.ab_t, :open,
                                               ab_w_eff(cfg), cfg.hp_seed + 603 + k, :monumental))
        band_j = central_band_eigs(ev_j, cfg.ab_center_fraction)
        r_j, _ = mean_adjacent_spacing_ratio(band_j)
        (isfinite(r_j) && length(band_j) == length(band_base)) || (jitter_finite = false; continue)
        push!(r_jit, r_j)
        # spectral drift: align bands on the shared quantile grid (positions may
        # shift rigidly — that is physical — but the SHAPE must not deform)
        ej = [band_j[1] + qv * (band_j[end] - band_j[1]) for qv in qlevels]
        drift_max = max(drift_max, maximum(abs.(ej .- qbase)) / max(bw, 1e-12))
        ab_gc!() # suite convention: explicit collection after every heavy solve (OOM guard)
    end
    r_drift = isempty(r_jit) ? NaN : maximum(abs.(r_jit .- r_base))
    @printf(" (b) jitter: %d trials, σ_pos = %g, |Δα| ≤ %g\n", length(r_jit), cfg.hp_pos_jitter, cfg.hp_alpha_jitter)
    @printf("     ⟨r⟩ drift ≤ %.4f | aligned-band spectral drift ≤ %.4f·BW (limits 0.05 / 0.05)\n",
            r_drift, drift_max)
    b_ok = jitter_finite && isfinite(r_drift) && r_drift <= 0.05 && drift_max <= 0.05
    ok_all &= b_ok

    # ── (c) L-growth: hermiticity at machine ε on EVERY rung + bounded ⟨r⟩ ──
    prog_update(0.55, "H6c: L-ladder + hermiticity")
    ladder = cfg.hp_L_ladder
    r_series = Float64[]
    L_series = Float64[]
    herm_worst = 0.0
    for (k, Lk) in enumerate(ladder)
        c = _hp_std_config(cfg, Lk, cfg.hp_seed + 700 + Lk)
        H = build_ab_cloud_hamiltonian(c)
        dh = maximum(abs.(H - H'))
        herm_worst = max(herm_worst, dh)
        ev = sort(real.(eigvals(Hermitian(H))))
        r, _ = mean_adjacent_spacing_ratio(central_band_eigs(ev, cfg.ab_center_fraction))
        push!(r_series, r); push!(L_series, Float64(Lk))
        @printf(" (c) L=%2d: max|H−H†| = %.2e | ⟨r⟩ = %.4f\n", Lk, dh, r)
        log_comp(@sprintf(" H6c: L=%d hermiticity %.2e, ⟨r⟩ %.4f", Lk, dh, r))
        ab_gc!() # suite convention: explicit collection after every heavy solve (OOM guard)
        prog_update(0.55 + 0.38 * k / max(length(ladder), 1), @sprintf("H6c: L=%d done", Lk))
    end
    herm_ok = herm_worst < 1e-9
    r_in_band = all(x -> isfinite(x) && 0.53 <= x <= 0.67, r_series)
    @printf(" (c) hermiticity worst-case: %.2e (limit 1e-9) | ⟨r⟩ ladder %s\n",
            herm_worst, r_in_band ? "inside [0.53, 0.67] at every rung" : "OUTSIDE the GUE plateau band at some rung")
    c_ok = herm_ok && r_in_band
    ok_all &= c_ok

    rec = Tuple{String,Bool,String}[]
    push!(rec, ("(a) open↔torus bulk", a_ok,
        isfinite(d_boundary) ? @sprintf("|Δ⟨r⟩| = %.4f ≤ %.3f", d_boundary, cfg.hp_gue_band) :
                               "skipped — α·L ∉ ℤ (use even L for the torus rung)"))
    push!(rec, ("(b) jitter stability", b_ok,
        @sprintf("⟨r⟩ drift %.4f, spectral drift %.4f·BW over %d trials", r_drift, drift_max, length(r_jit))))
    push!(rec, ("(c) hermiticity every rung", herm_ok, @sprintf("worst max|H−H†| = %.2e (machine-ε limit 1e-9)", herm_worst)))
    push!(rec, ("(c) ⟨r⟩ bounded on ladder", r_in_band,
        isempty(r_series) ? "no rungs" : @sprintf("%.4f … %.4f over L = %s", minimum(r_series), maximum(r_series),
                                                  join(Int.(L_series), ","))))

    hc_verdict_table(cfg, "Test H6", rec; pass_label = "HP audit")

    if REP.current !== nothing
        p = RepPlot("H6 — stability: ⟨r⟩ vs L (c) and jitter trials (b)", "L  /  jitter trial #", "⟨r⟩")
        isempty(L_series) || add_series!(p, "⟨r⟩ vs L (rung ladder)", L_series, r_series, 'L')
        isempty(r_jit) || add_series!(p, "jitter trials", collect(1.0:Float64(length(r_jit))), r_jit, 's')
        add_series!(p, "GUE 0.5992", [0.0, max(maximum(L_series, init = L), Float64(max(length(r_jit), 1)))],
                    [0.5992, 0.5992], 'l')
        rep_plot!(p)
    end
    rep_note!("A Hilbert–Pólya operator must survive the three probes that would break a fine-tuned artifact: " *
              "a boundary switch (edge states must stay OUTSIDE the bulk window), parameter jitter (the spectrum " *
              "may shift rigidly but must not deform — measured as the aligned-quantile drift in units of the " *
              "bandwidth), and lattice growth with the hermiticity defect max|H−H†| re-verified at machine ε on " *
              "EVERY rung (the systematic version of the one-off 3D hardcore H1 check).")
    ok = ok_all
    log_result(@sprintf(" Test H6: boundary %s, jitter %s, hermiticity %.1e → %s",
                        a_ok ? "ok" : "DRIFT", b_ok ? "ok" : "DRIFT", herm_worst,
                        ok ? msg(cfg, "pass") : msg(cfg, "warn")))
    return ok
end

# ── H7: sequence-level correlation vs γₙ (the check nobody ran) ─────────
function hp_h07_sequence_correlation(cfg::HPConfig, zeta_zeros::Vector{Float64})
    _mr_gate_head(7, "SEQ-CORR",
                  "Sequence-level correlation — n-th unfolded level vs n-th zero γₙ",
                  "Distribution tests (Test 34) say nothing about pointwise sequence identity — this one does")

    L = cfg.hp_L
    seed = cfg.hp_seed + 800
    prog_update(0.05, "H7: AB spectrum")
    ev = _hp_spectrum(cfg, _hp_std_config(cfg, L, seed))
    band = central_band_eigs(ev, cfg.ab_center_fraction)
    m_ab = length(band)
    @printf(" AB spectrum: %d×%d seed=%d → central band %d levels\n", L, L, seed, m_ab)

    # fluctuations around the mean density: uₙ − n for the locally unfolded band
    u_ab = _hp_unfold_local(band)
    fl_ab = u_ab .- collect(0.0:Float64(m_ab - 1))

    isempty(zeta_zeros) && begin
        println(" ζ zeros NOT loaded — the sequence test needs γₙ. Run the calibration part only.")
        fl_ab_mean = mean(fl_ab)
        @printf(" AB fluctuation diagnostics (no ζ side): mean %.4f, std %.4f\n", fl_ab_mean, std(fl_ab))
        log_result(" Test H7: skipped — no zeros loaded → WARN")
        return false
    end

    m = min(m_ab, length(zeta_zeros))
    gam = zeta_zeros[1:m]
    # ζ side: the standard smooth-counting fluctuation N̄(γₙ) − (n−1) — the
    # exact Riemann–Weil unfolding, NOT a window estimate (the AB side uses the
    # local window because its true counting function is unknown — that
    # asymmetry is inherent and is noted in the report)
    fl_z = [smooth_counting_function(g) - Float64(k - 1) for (k, g) in enumerate(gam)]
    fl_ab_m = fl_ab[1:m]
    # EDGE TRIM (calibration round 2 fix): the local-window unfolding is biased
    # at the sequence EDGES (half the window falls outside the support), and
    # that bias is the SAME shape for every spectrum — untrimmed GUE–GUE pairs
    # correlated at |r| ≈ 0.65 (measured) instead of the theoretical 1/√m ≈ 0.06
    # because both partners carried the identical edge artifact. Trim the outer
    # 10% on BOTH sides for every correlation in this test (AB-ζ, calibration
    # pairs, shuffled control) — apples to apples.
    trim = max(1, round(Int, 0.1 * m))
    keep = (trim + 1):(m - trim)
    m_kept = length(keep)
    # MA high-pass (see _hp_fluct_hp): removes the slow common estimator bias;
    # window matches the unfolding window (5% of m)
    win_hp = max(3, round(Int, 0.05 * m))
    fl_a = _hp_fluct_hp(fl_ab_m[keep]; win = win_hp)
    fl_zt = _hp_fluct_hp(fl_z[keep]; win = win_hp)

    prog_update(0.40, "H7: correlation + calibration")
    r_pearson = cor(fl_a, fl_zt)
    ρ_spear = _hp_spearman(fl_a, fl_zt)
    @printf(" ζ side: first %d zeros, γ ∈ [%.1f, %.1f], fluctuations N̄(γₙ)−(n−1)\n",
            m, gam[1], gam[end])
    @printf(" Sequence correlation (aligned indices %d..%d after the 10%% edge trim):\n", trim + 1, m - trim)
    @printf("   Pearson  r = %+.5f\n   Spearman ρ = %+.5f\n", r_pearson, ρ_spear)

    # calibration: |r| distribution of INDEPENDENT GUE–GUE pairs (the honest null:
    # two independent GUE spectra of the same length correlate at |r| ~ 1/√m)
    n_cal = clamp(cfg.hp_n_gue_calib, 2, 50)
    cal_abs = Float64[]
    for k in 1:n_cal
        g1 = central_band_eigs(gue_matrix_eigenvalues(m; seed = cfg.hp_seed + 900 + k), 1.0)
        g2 = central_band_eigs(gue_matrix_eigenvalues(m; seed = cfg.hp_seed + 900 + k + n_cal), 1.0)
        f1 = _hp_fluct_hp((_hp_unfold_local(g1) .- collect(0.0:Float64(m - 1)))[keep]; win = win_hp)
        f2 = _hp_fluct_hp((_hp_unfold_local(g2) .- collect(0.0:Float64(m - 1)))[keep]; win = win_hp)
        push!(cal_abs, abs(cor(f1, f2)))
        prog_update(0.40 + 0.40 * k / n_cal, @sprintf("H7: GUE pair %d/%d", k, n_cal))
        ab_gc!() # suite convention: explicit collection after every heavy solve (OOM guard)
    end
    band_null = maximum(cal_abs)
    @printf(" Calibration: %d independent GUE–GUE pairs (trimmed + high-pass) → |r| ∈ [%.5f, %.5f], max %.5f (theory ~%.5f = 1/√m)\n",
            n_cal, minimum(cal_abs), band_null, band_null, 1.0 / sqrt(m_kept))

    # shuffled control: destroys sequence alignment, keeps the marginals
    rng_sh = MersenneTwister(cfg.hp_seed + 950)
    fl_sh = _hp_fluct_hp(fl_z[randperm(rng_sh, m)][keep]; win = win_hp)
    r_shuf = cor(fl_a, fl_sh)
    @printf(" Shuffled control: r = %+.5f (must collapse to ~0 — validates the alignment test itself)\n", r_shuf)

    inside = abs(r_pearson) <= max(band_null, 2.5 / sqrt(m_kept))
    _in_txt = inside ? "INSIDE the independent-GUE band — sequence-level independence confirmed\n           (GUE universality does NOT require pointwise H-P identification; the suite now states it explicitly)" :
                       "OUTSIDE the null band — SEQUENCE-LEVEL CORRELATION DETECTED (would be a direct H-P identification signal!)"
    println()
    _mr_status(inside ? "●" : "◆", inside ? "accent" : "gold",
               "VERDICT: |r_AB| = " * @sprintf("%.5f", abs(r_pearson)) *
               " vs null band " * @sprintf("%.5f", max(band_null, 2.5 / sqrt(m_kept))) *
               " → " * _in_txt)

    rec = Tuple{String,Bool,String}[]
    push!(rec, ("calibration pairs", n_cal >= 3,
        @sprintf("%d independent GUE–GUE pairs, max |r| = %.5f", n_cal, band_null)))
    push!(rec, ("shuffled control", abs(r_shuf) <= max(band_null, 2.5 / sqrt(m_kept)),
        @sprintf("|r_shuffled| = %.5f within the band", abs(r_shuf))))
    push!(rec, ("sequence correlation", true,
        inside ? @sprintf("|r| = %.5f ≤ band %.5f → independence confirmed (honest expected result)",
                          abs(r_pearson), max(band_null, 2.5 / sqrt(m_kept))) :
                 @sprintf("|r| = %.5f > band %.5f → CORRELATION DETECTED", abs(r_pearson), max(band_null, 2.5 / sqrt(m_kept)))))
    push!(rec, ("Spearman consistency", abs(ρ_spear) <= max(band_null, 0.05) + 0.05,
        @sprintf("ρ = %+.5f (rank-level agreement with the Pearson verdict)", ρ_spear)))

    hc_verdict_table(cfg, "Test H7", rec; pass_label = "HP audit")

    if REP.current !== nothing
        p = RepPlot(@sprintf("H7 — aligned fluctuations: Pearson r = %+.5f, Spearman ρ = %+.5f", r_pearson, ρ_spear),
                    "level index n", "fluctuation around mean density")
        ns = collect(1.0:Float64(m))
        add_series!(p, "AB-cloud: uₙ − n", ns, fl_ab_m, 'l')
        add_series!(p, "ζ: N̄(γₙ) − (n−1)", ns, fl_z, 'l')
        rep_plot!(p)
        p2 = RepPlot(@sprintf("H7 — sequence scatter (|r| = %.5f vs GUE-pair band %.5f)", abs(r_pearson),
                              max(band_null, 2.5 / sqrt(m_kept))),
                     "ζ fluctuation N̄(γₙ)−(n−1)", "AB fluctuation uₙ − n")
        add_series!(p2, "aligned pairs (trimmed)", fl_zt, fl_a, 's')
        rep_plot!(p2)
    end
    rep_note!("Raw level-index correlations are trivially ≈ 1 (both sequences increase) — the honest statistic " *
              "correlates the FLUCTUATIONS around the respective mean densities, with the outer 10% of the " *
              "sequence trimmed and a moving-average high-pass applied to BOTH sides of every correlation " *
              "(the local-window estimator leaves a slow common bias: untrimmed independent GUE–GUE pairs " *
              "falsely correlate at |r| ≈ 0.65, edge-trimming alone still 0.2–0.5 — measured during calibration; " *
              "the high-pass restores the theoretical 1/√m band). A genuine pointwise H-P identification would " *
              "be a LOCAL, high-frequency feature and survives the filter. The null band is EMPIRICAL: " *
              "independent GUE–GUE pairs of the same length processed by the identical pipeline. ζ uses the " *
              "exact Riemann–Weil unfolding N̄; the AB side necessarily uses the local window estimate (its " *
              "true counting function is the thing under test). Independent GUE realizations correlate at " *
              "zero — that is exactly why GUE universality is compatible with NO pointwise H-P identification.")
    ok = n_cal >= 3 && abs(r_shuf) <= max(band_null, 2.5 / sqrt(m_kept)) &&
         abs(ρ_spear) <= max(band_null, 0.05) + 0.05 # method validity + table alignment (v23.6); the AB verdict is the headline
    log_result(@sprintf(" Test H7: Pearson r=%+.5f (band %.5f), Spearman ρ=%+.5f → %s → %s",
                        r_pearson, max(band_null, 2.5 / sqrt(m_kept)), ρ_spear,
                        inside ? "sequence independence confirmed" : "CORRELATION DETECTED",
                        ok ? msg(cfg, "pass") : msg(cfg, "warn")))
    return ok
end


# ═════════════════════════════════════════════════════════════════════════════
# §6. RUNNER SHELL — honest done-line (v23.6 №1), plots flush, battery
# ═════════════════════════════════════════════════════════════════════════════

function register_audits!()
    isempty(HP_AUDITS) || return
    _hp_register!() # verbatim suite registration (fills HP_AUDITS + TEST_META)
    for a in HP_AUDITS
        SLUGS[a.id] = @sprintf("test_%d_%s", a.id, a.slug)
    end
    return
end

"""Subprocess heartbeat (v23.8): a tiny `sh` loop that prints a dim «alive»
line to the controlling terminal every 60 s while a gate runs. This is the
ONLY way to get feedback over ONE blocking LAPACK call on a single-threaded
Julia: a ccall monopolizes the thread, so Timers and @spawn tasks never get
scheduled until the solve returns (the same physics that deadlocked the old
pipe-tee). The child writes to /dev/tty — NOT to our redirected fd 1 — and
self-terminates when julia exits (kill -0 \$PPID) or when the first write
fails (no controlling terminal → silent no-op). _hp_run! SIGTERMs and reaps
it in its finally. Worst-case orphan: one `sleep 60` that exits without
printing (the loop body died with the shell)."""
function _heartbeat_start!(label::AbstractString)
    _heartbeat_stop!()
    try
        scr = "i=0; while kill -0 \$PPID 2>/dev/null; do sleep 60; i=\$((i+60)); " *
              "printf '\\033[2m  alive %02d:%02d — " * String(label) *
              " still computing (one silent LAPACK call, NOT a hang)\\033[0m\\n' " *
              "\$((i/60)) \$((i%60)) > /dev/tty 2>/dev/null || exit 0; done"
        _HEARTBEAT[] = run(`sh -c $scr`; wait = false)
    catch
        _HEARTBEAT[] = nothing # no sh / no fork — proceed without a heartbeat
    end
    return
end
function _heartbeat_stop!()
    p = _HEARTBEAT[]
    p === nothing && return
    _HEARTBEAT[] = nothing
    try; kill(p); catch; end        # SIGTERM — if it is mid-sleep it dies quietly
    try; wait(p);  catch; end       # reap (no zombie)
    return
end

"""Run one audit: tee console → REPORT, honest done-line with the REAL verdict
(v23.6 №1 — the suite printed "done → PASS" from the exception flag, painting
over WARN; the standalone was born honest). v23.8: a subprocess heartbeat
(«alive» lines to the terminal) covers the silent blocking LAPACK phases."""
function _hp_run!(a::HPAudit, cfg::HPConfig, zeta_zeros::Vector{Float64})
    rep_begin!(a.id, a.title)
    global _PROG_LABEL[] = @sprintf("HP H%d", a.id - 300)
    t0 = time()
    verdict = "ERROR"
    console = ""
    _heartbeat_start!(_PROG_LABEL[]) # alive-lines over the blocking eigensolves
    try
        res, console = rep_tee_stdout() do
            a.runner(cfg, zeta_zeros)
        end
        verdict = res === true ? "PASS" : "WARN"
        rt = REP.current
        if rt !== nothing
            rt.headline = last_log_line()
            rep_finish!(a.id, verdict, last_log_line())
        end
        return res
    catch err
        rt = REP.current
        rt !== nothing && rep_finish!(a.id, "FAIL", "EXCEPTION: " * sprint(showerror, err))
        rethrow(err)
    finally
        _heartbeat_stop!() # stop the ticker BEFORE the captured replay lands
        rt = REP.current
        if rt !== nothing
            rt.console = console
            rt.comp_hi = length(COMP_LINES)
            _dg = verdict == "PASS" ? "✓" : verdict == "ERROR" ? "✗" : "●"
            _dc = verdict == "PASS" ? "ok" : verdict == "ERROR" ? "err" : "warn"
            println(_mr_c("  " * _dg * " [" * _PROG_LABEL[] * "] done in " *
                          _prog_hms(time() - t0) * " — " * _prog_now_str() * " → ", "dim") *
                    _mr_c(verdict, _dc))
            flush(stdout)
        end
    end
end

function _hp_flush_plots!(st::MiniTestState, run_dir::String)
    isempty(st.plots) && return
    pdir = joinpath(run_dir, st.slug, "plots")
    mkpath(pdir)
    for (i, p) in enumerate(st.plots)
        path = joinpath(pdir, @sprintf("plot_%d.png", i))
        try
            save_repplot_png(p, path)
            push!(st.pngs, path)
            println(@sprintf("   plot %d/%d → %s", i, length(st.plots), path))
        catch err
            println(@sprintf("   plot %d/%d FAILED: %s", i, length(st.plots), sprint(showerror, err)))
        end
        flush(stdout)
    end
    return
end

function _hp_write_test_report!(st::MiniTestState, run_dir::String)
    open(joinpath(run_dir, st.slug * "_REPORT.txt"), "w") do io
        println(io, "="^69)
        @printf(io, "REPORT — %s   [%s]\n", st.title, st.status)
        println(io, "="^69)
        print(io, st.console)
        isempty(st.notes) || begin
            println(io, "\n", "-"^69)
            println(io, "NOTES / METHODOLOGY")
            for n in st.notes
                println(io, " • ", n)
            end
        end
        isempty(st.pngs) || begin
            println(io, "\nPLOTS:")
            for p in st.pngs; println(io, "   ", p); end
        end
    end
    return
end

"""Honest heavy-solve bookkeeping (v23.8): how many dense L×L-class
eigensolves gate H<k> issues at the CURRENT config. Order-of-magnitude
honest, not exact — it exists so the console can say BEFORE a gate starts
what the user is about to spend (H5 at the FULL preset used to ask ≈ 340
silent LAPACK calls of 3136×3136 = the «hangs on the 5th test» experience;
v24.1 caps every H5 plan at HP5_SOLVE_CAP = 40 and reads the SAME planner
the gate runs — banner and reality can never drift apart again)."""
function _hp_diag_est(cfg::HPConfig, k::Int)::Int
    n_sweep = cfg.hp_regime_mode === :showdown ? 3 : 0 # regimes B/C/D in H1's sweep (H1 sweeps ONLY in :showdown — v24.2 honesty for :regime_d too)
    if k == 1
        return cfg.hp_h1_configs + 2 + n_sweep * (cfg.hp_h1_configs + 1) +
               2 * cfg.hp_deep_nulls + cfg.hp_deep_configs
    elseif k == 2
        return 2
    elseif k == 3
        return length(cfg.hp_L_ladder)
    elseif k == 4
        return 2 * cfg.hp_n_q_grid # two disorder seeds per q-point
    elseif k == 5
        return _hp5_plan(cfg).total # v24.1: the plan IS the estimate — banner == reality
    elseif k == 6
        return 2 + cfg.hp_jitter_trials + length(cfg.hp_L_ladder)
    elseif k == 7
        return 1 # + 2·n_cal GUE pairs, but those are m-sized (≈ central band), ~100× cheaper
    end
    return 0
end

"""Largest lattice the gate diagonalizes (H3/H6 walk the ladder — their cost
sits at the ladder's TOP, not at hp_L). Used to size-weight cost estimates."""
_hp_gate_L(cfg::HPConfig, k::Int)::Int =
    (k == 3 || k == 6) ? max(cfg.hp_L_ladder..., cfg.hp_L) : cfg.hp_L

"""LIVE per-gate cost line, printed BEFORE the tee hides everything the gate
itself prints until the gate ends. Small solves are lumped in honestly."""
function _hp_print_gate_cost(cfg::HPConfig, k::Int)
    n = _hp_diag_est(cfg, k)
    n > 0 || return
    L = cfg.hp_L
    peak_gb = 2.5 * (L^2)^2 * 16 / 2^30 # the matrix is N×N with N=L² (build_ab_cloud_hamiltonian): N²·16 B × 2.5 (copy + LAPACK workspace), per solve
    println("  " * _mr_c(@sprintf("cost: ≈ %d dense eigensolves (≤ %d×%d, O(N³), ≈ %.1f GB peak each) — ONE solve can run silent for MINUTES;",
                                  n, L, L, peak_gb), "dim"))
    println("  " * _mr_c("the bar below redraws after EACH solve · an «alive» line ticks every 60 s · Ctrl-C lands after the current solve (NOT stuck)",
                          "dim"))
    return
end

function _hp_run_all!(cfg::HPConfig, zeta_zeros::Vector{Float64}, sel::Vector{Int},
                      run_dir::String, tag::String)
    npass = 0
    t_all = time()
    for k in sel
        idx = findfirst(x -> x.id == 300 + k, HP_AUDITS)
        idx === nothing && (println("no audit H$k"); continue)
        a = HP_AUDITS[idx]
        println("\n" * _mr_c("▶ GATE H" * string(k), "gold") *
                "  " * _mr_c(replace(a.title, r"^H\d+\.\s*" => ""), "bold"))
        _hp_print_gate_cost(cfg, k) # visible NOW — the gate's own header replays only when the gate ends
        flush(stdout)
        res = _hp_run!(a, cfg, zeta_zeros)
        res === true && (npass += 1)
        st = REP.current
        st !== nothing && begin
            _hp_flush_plots!(st, run_dir)
            _hp_write_test_report!(st, run_dir)
            push!(ALL_STATES, st)
            REP.current = nothing
        end
        ab_gc!()
    end
    println()
    _mr_panel("deep audit · " * tag * "  ·  wall " * _prog_hms(time() - t_all), [
        @sprintf("%s %d/%d gates PASS (detector-validity verdicts; physics headlines inside)",
                 npass == length(sel) ? "✓" : "!", npass, length(sel)),
    ])
    return npass
end

# ═════════════════════════════════════════════════════════════════════════════
# §7. RUN REPORTS — the two-files contract (master log + master report)
# ═════════════════════════════════════════════════════════════════════════════

function _md_esc(s::String)
    s2 = replace(s, "|" => "\\|")
    return replace(s2, "\n" => " ")
end

function write_run_reports(run_dir::String, cfg::HPConfig, tag::String, t_wall::Float64,
                           zeta_loaded::Bool)
    logs_dir = joinpath(run_dir, "logs")
    mkpath(logs_dir)

    # 1) results_verdicts.txt — the one-line index
    open(joinpath(run_dir, "results_verdicts.txt"), "w") do io
        println(io, "ONE-LINE VERDICTS (standalone HP audit, $tag)")
        for s in RESULT_LINES
            println(io, s)
        end
    end

    # 2) logs/full_run_log.txt — ONE consolidated log (computation + console)
    open(joinpath(logs_dir, "full_run_log.txt"), "w") do io
        println(io, "FULL RUN LOG — $(basename(run_dir)) (hp_audit_standalone v23.6, $tag)")
        println(io, "ONE consolidated file: every test's computation log + console capture, in run order")
        println(io, "(two-files contract: the whole run is readable from final_report.md/html + this log)")
        for st in ALL_STATES
            println(io)
            println(io, "═"^69)
            @printf(io, "%s   [%s]\n", st.slug * " — " * st.title, st.status)
            println(io, "═"^69)
            println(io, "--- computation log (every log_comp while this test ran) ---")
            for i in st.comp_lo:min(st.comp_hi, length(COMP_LINES))
                println(io, COMP_LINES[i])
            end
            println(io, "--- console capture (the REPORT) ---")
            print(io, st.console)
            isempty(st.notes) || begin
                println(io, "--- notes ---")
                for n in st.notes
                    println(io, " • ", n)
                end
            end
        end
    end

    # 3) final_report.md — master report (verdicts + tables + notes + plots)
    md = IOBuffer()
    println(md, "# Hilbert-Pólya Deep Audit — standalone battery report")
    println(md)
    println(md, "**Run:** `$(basename(run_dir))` · **preset:** $tag · **date:** $(_prog_now_str()) · ",
                "**wall:** $(_prog_hms(t_wall))")
    println(md)
    println(md, "ζ zeros loaded: **$(zeta_loaded ? "yes" : "NO — H1/H7 controls skipped honestly")**")
    println(md)
    println(md, "## Parameters")
    println(md, "```")
    println(md, "L=$(cfg.hp_L)  L_weyl=$(cfg.hp_L_weyl)  ensemble=$(cfg.hp_n_ensemble)  seed=$(cfg.hp_seed)")
    println(md, "α=$(cfg.ab_alpha_test16)  W_eff=$(ab_w_eff(cfg))  sweep=:$((cfg.hp_regime_mode))")
    println(md, "deep-nulls=$(cfg.hp_deep_nulls)  deep-configs=$(cfg.hp_deep_configs)  α-profile=$(cfg.hp_alpha_scan) (n=$(cfg.hp_alpha_scan_n))")
    println(md, "primes=$(join(cfg.hp_primes, ","))  q-grid=$(cfg.hp_n_q_grid) on [$(cfg.hp_q_min), $(cfg.hp_q_max)]")
    println(md, "ladder=$(join(cfg.hp_L_ladder, "→"))  t_max=$(cfg.hp_t_max)  dt=$(cfg.hp_dt)")
    println(md, "```")
    println(md)
    n_pass = count(st.status == "PASS" for st in ALL_STATES)
    println(md, "**Battery verdict:** $n_pass/$(length(ALL_STATES)) PASS + $(length(ALL_STATES) - n_pass) WARN ",
                "(detector-validity semantics; the physics headlines live inside the tests)")
    println(md)
    for st in ALL_STATES
        println(md, "---")
        println(md)
        println(md, "## $(st.title)  — **$(st.status)**")
        println(md)
        isempty(st.headline) || println(md, "> $(st.headline)")
        println(md)
        isempty(st.rows) || begin
            println(md, "| sub-check | status | detail |")
            println(md, "|---|---|---|")
            for (name, ok, note) in st.rows
                println(md, "| $(_md_esc(name)) | $(ok ? "PASS" : "WARN") | $(_md_esc(note)) |")
            end
            println(md)
        end
        for (i, p) in enumerate(st.pngs)
            rel = relpath(p, run_dir)
            println(md, "![plot $i]($(rel))")
        end
        isempty(st.notes) || begin
            println(md)
            for n in st.notes
                println(md, "_Note:_ ", n)
                println(md)
            end
        end
    end
    open(joinpath(run_dir, "final_report.md"), "w") do io
        print(io, String(take!(md)))
    end

    # 4) final_report.html — same content, minimal self-contained styling
    html = IOBuffer()
    println(html, "<!DOCTYPE html><html><head><meta charset=\"utf-8\">")
    println(html, "<title>HP deep audit — $(basename(run_dir))</title>")
    println(html, "<style>body{font-family:Georgia,serif;max-width:1100px;margin:2em auto;padding:0 1em;color:#1a1a2e;background:#fafafa}",
            "h1,h2,h3{font-family:'Helvetica Neue',Arial,sans-serif}h2{border-bottom:2px solid #16324f;padding-bottom:.2em;margin-top:2em}",
            "table{border-collapse:collapse;width:100%;font-size:.92em}td,th{border:1px solid #bbb;padding:.35em .5em;vertical-align:top}",
            "th{background:#16324f;color:#fff;text-align:left}.pass{color:#0a7d32;font-weight:bold}.warn{color:#b8860b;font-weight:bold}",
            "code,pre{background:#eef1f4;border-radius:4px;padding:.1em .3em}img{max-width:100%;border:1px solid #ccc;margin:.4em 0}",
            "blockquote{border-left:4px solid #16324f;margin:0;padding:.1em 1em;color:#333}</style></head><body>")
    println(html, "<h1>Hilbert-Pólya Deep Audit — standalone battery</h1>")
    @printf(html, "<p><b>Run:</b> %s · <b>preset:</b> %s · <b>date:</b> %s · <b>wall:</b> %s · ζ zeros: <b>%s</b></p>",
            basename(run_dir), tag, _prog_now_str(), _prog_hms(t_wall), zeta_loaded ? "yes" : "NO")
    @printf(html, "<p><b>Battery verdict:</b> %d/%d PASS + %d WARN (detector-validity semantics)</p>",
            n_pass, length(ALL_STATES), length(ALL_STATES) - n_pass)
    for st in ALL_STATES
        println(html, "<h2>", st.title, " — <span class=\"", st.status == "PASS" ? "pass" : "warn", "\">", st.status, "</span></h2>")
        isempty(st.headline) || println(html, "<blockquote>", st.headline, "</blockquote>")
        isempty(st.rows) || begin
            println(html, "<table><tr><th>sub-check</th><th>status</th><th>detail</th></tr>")
            for (name, ok, note) in st.rows
                @printf(html, "<tr><td>%s</td><td class=\"%s\">%s</td><td>%s</td></tr>",
                        name, ok ? "pass" : "warn", ok ? "PASS" : "WARN", note)
            end
            println(html, "</table>")
        end
        for p in st.pngs
            println(html, "<img src=\"", relpath(p, run_dir), "\" alt=\"plot\">")
        end
        for n in st.notes
            println(html, "<p><i>", n, "</i></p>")
        end
    end
    println(html, "</body></html>")
    open(joinpath(run_dir, "final_report.html"), "w") do io
        print(io, String(take!(html)))
    end
    return nothing
end

# ═════════════════════════════════════════════════════════════════════════
# §8. HP·MERIDIAN CONSOLE + CLI (v23.7-SA)
#     Unique-identity interactive console: gates, doctor, intel, profiles.
#     Bullet-proof input: Ctrl-C safe · EOF safe · Enter repaints ·
#     re-include safe (everything lives in module HPMeridian).
# ═════════════════════════════════════════════════════════════════════════

function apply_preset!(cfg::HPConfig, which::Symbol)
    if which === :fast
        cfg.hp_L = 72; cfg.hp_L_weyl = 72; cfg.hp_n_ensemble = 100
        cfg.hp_alpha_scan_n = 40; cfg.hp_regime_mode = :showdown
        _mr_info("PRESET FAST: L=72 (72×72=5184 sites → each solve is a 5184×5184 dense eigensolve), ensemble=100/regime, α-scan n=40 — battery · H5 plan auto-caps at ≤ 40 solves (v24.1)")
    elseif which === :full
        cfg.hp_L = 56; cfg.hp_L_weyl = 56; cfg.hp_n_ensemble = 40
        cfg.hp_alpha_scan_n = 30; cfg.hp_regime_mode = :showdown
        _mr_info("PRESET FULL: L=56 (56×56=3136 sites), ensemble=40/regime, α-scan n=30 — deep run · H5 plan auto-caps at ≤ 40 solves (v24.1)")
    elseif which === :smoke
        cfg.hp_L = 20; cfg.hp_L_weyl = 20; cfg.hp_n_ensemble = 8
        cfg.hp_h1_configs = 2; cfg.hp_deep_nulls = 4; cfg.hp_deep_configs = 4
        cfg.hp_alpha_scan_n = 6; cfg.hp_zeta_cap = 2000; cfg.hp_jitter_trials = 2
        cfg.hp_L_ladder = [16, 20, 24]; cfg.hp_weyl_grid = 60; cfg.hp_n_gue_calib = 3
        cfg.hp_t_max = 20.0
        _mr_info("PRESET SMOKE: L=20, ensemble=8, deep=4/4, α-scan n=6, ladder=[16,20,24], ζ cap=2000 — validation run")
    else
        error("unknown preset $which")
    end
    return cfg
end

function load_zeros(path::String)::Vector{Float64}
    isfile(path) || return Float64[]
    out = Float64[]
    for tok in split(read(path, String))
        isempty(tok) && continue
        startswith(tok, '#') && continue
        v = tryparse(Float64, tok)
        v !== nothing && push!(out, v)
    end
    return out
end

function usage()
    println(_mr_c("usage: ", "bold") *
            _mr_c("julia hp_audit_standalone.jl [fast|full|smoke] [h1..h7|all] [seed=N] [zeros=path]", "title"))
    println("  " * _mr_c("no args + terminal", "gold") *
            _mr_c(" → HP·MERIDIAN console; with args → batch battery", "dim"))
    println("  " * _mr_c("REPL", "gold") *
            _mr_c(":  include(\"hp_audit_standalone.jl\") auto-opens the console (module HPMeridian)", "dim"))
    return
end

# ── console identity: unique gate names + honest per-preset cost hints ──
const GATE_NAME = Dict{Int,String}(
    1 => "PRIME-TRACE", 2 => "WEYL-DOS", 3 => "POWER-LAW", 4 => "CRITICAL-Q",
    5 => "REGIME-2×2", 6 => "HERMIT-STRESS", 7 => "SEQ-CORR")
const GATE_MIN = Dict{Int,Tuple{Float64,Float64,Float64}}( # (smoke, fast, full), minutes
    1 => (0.4, 0.5, 25.0), 2 => (0.15, 0.05, 2.0), 3 => (0.3, 0.4, 20.0),
    4 => (0.2, 0.2, 15.0), 5 => (0.4, 2.0, 90.0), 6 => (0.5, 0.5, 45.0),
    7 => (0.05, 0.05, 5.0))

function _fmt_min(m::Float64)
    m <= 0 && return "—"
    m < 1.0 && return @sprintf("~%d s", max(5, round(Int, m * 60)))
    m < 90.0 && return @sprintf("~%d m", round(Int, m))
    return @sprintf("~%.1f h", m / 60)
end

# ── ANSI color: on only when safe (TTY, not dumb term, not legacy conhost,
#    opt-out ENV["HP_SA_COLOR"]="0"). Every consumer must go through _hpc. ──
const _ANSI = Dict{String,String}("title" => "1;36", "dim" => "2", "ok" => "32",
    "warn" => "33", "err" => "31", "accent" => "36", "bold" => "1")
const _COLOR_ON = Ref{Bool}(false)
function _color_init!()
    tty = stdout isa Base.TTY
    dumb = get(ENV, "TERM", "xterm") in ("dumb", "")
    off = get(ENV, "HP_SA_COLOR", "1") == "0"
    win_legacy = Sys.iswindows() && !haskey(ENV, "WT_SESSION") &&
                 !haskey(ENV, "TERM_PROGRAM") && !haskey(ENV, "ANSICON")
    _COLOR_ON[] = tty && !dumb && !off && !win_legacy
    return _COLOR_ON[]
end
_hpc(s::AbstractString, key::String) =
    _COLOR_ON[] ? string("\e[", _ANSI[key], "m", s, "\e[0m") : String(s)

# true when fd 0 is a terminal — the ground truth for "a human is typing"
# (Base has no isatty in 1.10; ccall works on linux/windows/mac alike)
_hp_stdin_tty() = ccall(:isatty, Cint, (Cint,), 0) == 1

# ── one prompt of the console (the ONLY stdin reader) ────────────────────
#   returns: String command · "" = Enter (repaint) · nothing = quit
#   (dead stdin, or Ctrl-C at the prompt). Interactive Enter NEVER blocks:
#   the v23.6.1 eof() freeze is gone by design.
function _hp_ask(prompt::String)
    print(prompt)
    flush(stdout)
    line = try
        String(strip(readline(stdin)))
    catch e
        e isa InterruptException && return nothing   # Ctrl-C at the prompt
        rethrow()
    end
    isempty(line) || return line
    isinteractive() && return ""                     # Enter → repaint
    isopen(stdin) && !eof(stdin) && return ""        # automation empty line
    return nothing                                   # stdin closed
end

# ── parameter reference: short hint (params list) + full doc (? field) ──
const HP_FIELD_HINT = Dict{Symbol,String}(
    :hp_L              => "primary lattice size L (L×L sites)",
    :hp_n_ensemble     => "H5: configs per regime (plan caps to ≤7 → ≤40 solves)",
    :hp_n_q_grid       => "H4: number of q points in the scan",
    :hp_q_min          => "H4: lower edge of the q window",
    :hp_q_max          => "H4: upper edge of the q window",
    :hp_primes         => "H1: prime targets of the Bragg comb",
    :hp_t_max          => "H1: unfolded time window T (resolution)",
    :hp_dt             => "H1: time-grid step (must resolve log p)",
    :hp_h1_configs     => "H1: AB configs averaged in stage 1",
    :hp_zeta_cap       => "cap on ζ zeros loaded (50000 = full)",
    :hp_L_ladder       => "H3: ladder of lattice sizes for p̂(L)",
    :hp_L_weyl         => "H2: lattice size for raw N(E) stairs",
    :hp_weyl_grid      => "H2: energy-grid density for the DOS",
    :hp_jitter_trials  => "H6: jitter trials per rung",
    :hp_pos_jitter     => "H6: position jitter amplitude (rel.)",
    :hp_alpha_jitter   => "H6: α jitter amplitude (relative)",
    :hp_n_gue_calib    => "H7: GUE–GUE calibration pair count",
    :hp_seed           => "master seed (all streams derive from it)",
    :hp_gue_band       => "H7: |r| band for 'independent' verdict",
    :hp_pass_fraction  => "H5: in-band ⟨r⟩ fraction threshold",
    :hp_regime_mode    => "H5: :showdown 2×2 | :regime_d focus-D ×40 | :baseline legacy",
    :hp_deep_nulls     => "H1 DEEPEN: null realizations (P95)",
    :hp_deep_configs   => "H1 DEEPEN: extra AB configs",
    :hp_alpha_scan     => "H5 α-profile on/off (finetuning axis)",
    :hp_alpha_scan_n   => "H5 α-profile: configs per α point (plan caps to ≤2)",
    :ab_t              => "AB hopping t (suite default 1.0)",
    :ab_center_fraction=> "central band fraction kept (0.6)",
    :ab_alpha_test16   => "α screening length — THE finetuning axis",
    :ab_K_smooth_window=> "H1 D2/form-factor smoothing window",
    :ab_n_realizations => "form-factor realizations for K(t)",
    :ab_W              => "disorder width W",
    :ab_W_max          => "disorder width cap (W_eff = min)",
    :ab_nv_list        => "vortex counts; first entry is used",
    :ab_q_list         => "vortex flux q (units of flux quantum)",
    :gue_matrix_size   => "GUE matrix size for calibrations")

const HP_FIELD_DOC = Dict{Symbol,String}(
    :hp_L => "Primary lattice edge for H1/H3/H4/H5/H6 scans. The diagonalized matrix is L²×L², so per-solve cost grows ≈ L⁶ (16→72 ≈ 8000×; memory ≈ L⁴ — at 72 plan ~1 GB peak per solve). L=72 = the standard battery (fast preset), L=56 = the monograph-scale full run.",
    :hp_n_ensemble => "Number of independent AB configurations per regime in the H5 2×2 showdown. The reviewer explicitly required N ≥ 30 for the Kolmogorov–Smirnov statistics to mean anything; FAST preset uses 100, FULL uses 40 at a larger L. v24.1 solve budget: the PLAN is capped at ≤7 configs/regime + ≤2 per α-point = ≤ 40 dense solves total (user cap 2026-09-09), whatever the preset asks — the gate prints the actual budget before running.",
    :hp_n_q_grid => "Resolution of the H4 critical-q scan. 21 points over [hp_q_min, hp_q_max] was enough to resolve the smooth profile (z=2.46); the domain-guard check needs the claimed criticals inside the window.",
    :hp_q_min => "Lower edge of the H4 q-scan window. The claimed critical values from the monograph are 0.3, 0.5 and 1.0 — if 0.3 < hp_q_min the 'location vs claimed criticals' check degrades (v23.6 domain guard fires).",
    :hp_q_max => "Upper edge of the H4 q-scan window. The claimed critical 1.0 must satisfy hp_q_max ≥ 1.0, otherwise the H4 location check is invalid (domain guard fires, test WARNs honestly).",
    :hp_primes => "Primes whose log p positions carry the expected Bragg comb in H1. Composites are added AUTOMATICALLY as decoy controls (v23.6 №5): the ζ-side validation requires loudness on primes AND silence on decoys.",
    :hp_t_max => "Length of the unfolded time window in H1. Frequency resolution ≈ 2π/T; T=40 resolves the log-2/log-3 pair comfortably; SMOKE lowers it to 20.",
    :hp_dt => "Step of the unfolded time grid. Must satisfy Nyquist for the largest target ω = log(largest prime) ≈ 4.11. 0.025 gives safe headroom; lowering it costs FFT size linearly.",
    :hp_h1_configs => "How many AB configurations are averaged before the 1-level raw FT in H1 stage 1. More configs = smoother noise floor, better SNR ceiling estimate; each config is a full diagonalization.",
    :hp_zeta_cap => "Cap on the number of ζ zero ordinates loaded for H1/H7. 50000 (full embedded Odlyzko set) gives ζ-side control SNR 10⁷–10⁹; smaller caps make the ζ side faster but the control weaker.",
    :hp_L_ladder => "Lattice sizes for the H3 exponent ladder p̂(L) and its L→∞ extrapolation. Needs ≥ 3 rungs for a finite-difference extrapolation flag; the rungs should be far apart for a real trend.",
    :hp_L_weyl => "Lattice size for the H2 raw N(E) staircase. H2 is cheap relative to H1/H5 — the density verdict (ζ-type vs lattice DOS, ΔAICc) is one of the most robust signals in the battery.",
    :hp_weyl_grid => "Energy-grid density for the H2 density-of-states comparison. 60 points resolve the E·lnE curvature; raising it does not change the AICc verdict, only smooths the plot.",
    :hp_jitter_trials => "H6 stability stress: how many independent jitter perturbations (vortex positions + α) are applied per rung. Each trial is a fresh diagonalization at the same L.",
    :hp_pos_jitter => "Relative amplitude of the positional jitter of vortices in H6 (fraction of the lattice spacing). 0.35 is the suite value; larger values probe deeper into the disorder landscape.",
    :hp_alpha_jitter => "Relative amplitude of the α (screening length) jitter in H6. Together with positional jitter it defines the 'stability plateau' of the spectrum against parameter noise.",
    :hp_n_gue_calib => "Number of independent GUE–GUE level pairs used to calibrate the |r| band of H7 (sequence correlation). The band is the honest null: the AB-vs-ζ correlation must fall INSIDE it.",
    :hp_seed => "Master seed. Every random stream (configs, nulls, GUE calibrations, α-profile) is derived from it deterministically — equal seeds give bit-for-bit equal numbers with the big suite.",
    :hp_gue_band => "Half-width of the 'sequence independence' band in H7, calibrated from GUE–GUE pairs (v23.6: edge-trimmed + MA-filtered, theory 1/√m). Verdict: r inside band = independence confirmed.",
    :hp_pass_fraction => "H5 regime scoring: fraction of ensemble configs whose mean adjacent-spacing ratio ⟨r⟩ must fall inside the GUE band for the regime to count as 'clean'. 0.90 = suite convention.",
    :hp_regime_mode => "H5 protocol. :showdown = the reviewer's 2×2: {sparse | L²/36 density} × {α=0.5 | α=25/900} (4 regimes A/B/C/D with regime-matched nulls). :baseline = the legacy single-regime ensemble. :regime_d (v24.2) = the FOCUSED deep run: ALL ≤40 solves go to regime [D] combined (density + sharp-flux) at N=40 realizations — seeds continue the showdown's [D] stream (first 7 bit-for-bit), α-profile off. Answers: does [D]'s OR-clause pass survive full-power individual KS?",
    :hp_deep_nulls => "H1 DEEPEN protocol: number of regime-matched null realizations (vortex-free + GUE) used to build the P95 ceiling of the max-SNR distribution. 20 = publication-grade (v23.6 №2).",
    :hp_deep_configs => "H1 DEEPEN: extra AB configurations run when a regime is MARGINAL/PRESENT, judged against the null P95. Pre-registered stop rule: below P95 → generic artifact, above → escalate.",
    :hp_alpha_scan => "H5 α-profile (v23.6 №3): scans GUE quality along α ∈ {25/900, 0.05, 0.1, 0.2, 0.35, 0.5} at sparse Nv to distinguish 'narrow tuned peak' from 'plateau of small α'. Never scored — headline only.",
    :hp_alpha_scan_n => "Configs per α point of the H5 α-profile (independent seed stream +900000). The v24.1 budget caps this at ≤2 per point (≤ 40 total solves); the α=0.5 endpoint independently replicates regime A.",
    :ab_t => "Hopping amplitude t of the AB cloud Hamiltonian (suite default 1.0). Sets the overall bandwidth scale; keep 1.0 unless you deliberately probe the t-dependence.",
    :ab_center_fraction => "Fraction of the spectrum kept as the 'central band' after diagonalization (0.6 = suite). The unfolded statistics are computed inside this window; wider = more levels but harder edges.",
    :ab_alpha_test16 => "THE finetuning axis of the whole audit (v23.6 H5 α-profile): α=0.5 is the published baseline where GUE FAILS; α=25/900≈0.0278 (sharp-flux, monograph value) is where GUE is restored. Do not change casually.",
    :ab_K_smooth_window => "Smoothing window for the K(t) form factor / D2 cross-check in H1. Small window = sharper peaks, noisier; large = the opposite. 3 = suite default.",
    :ab_n_realizations => "Number of realizations averaged in the K(t) form-factor estimate (D2 route). The D1 raw-FT detector is primary; D2 stays as the reviewer's literal cross-check.",
    :ab_W => "Disorder width W of the AB cloud. Effective disorder is min(ab_W, ab_W_max). Together with α and Nv it defines the spectral statistics regime.",
    :ab_W_max => "Cap on the effective disorder width. Keep at 1.0 (suite); the monograph regime works at W_eff = 1.",
    :ab_nv_list => "Vortex count list; the FIRST entry is used by every gate (resolve_vortex_count). [4] = sparse regime; [⌊L²/36⌋] = the monograph density anchor (Test 38). H5 regime B overrides it internally.",
    :ab_q_list => "Vortex flux magnitude in units of the flux quantum; first entry is used. [1.0] = π-flux (the suite standard). q is the axis of the H4 critical-q scan.",
    :gue_matrix_size => "Size N of the GUE matrices used for calibrations (H7 band, H1 GUE nulls). 12000 = suite-grade; 0 disables GUE (Nv=4 fallback — diagnostics only).")

_hp_fmt_val(v) = v isa Vector{Int} ? "[" * join(v, ",") * "]" :
                 v isa Vector{Float64} ? "[" * join(_hp_g6.(v), ",") * "]" :
                 v isa Float64 ? @sprintf("%.8g", v) : string(v)
_hp_g6(x::Float64) = @sprintf("%.6g", x)

function _hp_set_field!(cfg::HPConfig, name::Symbol, raw::AbstractString)
    hasfield(HPConfig, name) || throw(ErrorException("no field `$name` in HPConfig — try ? <field>"))
    raw = String(raw) # readline+strip yields SubString — normalize once
    T = fieldtype(HPConfig, name)
    val = try
        if T === Int
            parse(Int, raw)
        elseif T === Float64
            parse(Float64, raw)
        elseif T === Bool
            b = lowercase(raw)
            if occursin(r"^(true|1|yes|on)$", b)
                true
            elseif occursin(r"^(false|0|no|off)$", b)
                false
            else
                throw(ErrorException("cannot parse \"$raw\" as Bool (true/false)"))
            end
        elseif T === Symbol
            Symbol(lowercase(raw))
        elseif T === Vector{Int}
            toks = strip.(split(replace(raw, r"[\[\]]" => ""), ","))
            Int[parse(Int, t) for t in toks if !isempty(t)]
        elseif T === Vector{Float64}
            toks = strip.(split(replace(raw, r"[\[\]]" => ""), ","))
            Float64[parse(Float64, t) for t in toks if !isempty(t)]
        elseif T === String
            String(raw)
        else
            throw(ErrorException("unsupported field type $T"))
        end
    catch e
        e isa ErrorException && rethrow()
        throw(ErrorException("cannot parse \"$raw\" as $T"))
    end
    setfield!(cfg, name, val)
    return val
end

"""Soft, non-blocking sanity notes after a parameter change (the console
stays usable; the notes echo what the reviewer/community would flag)."""
function _hp_soft_warn(cfg::HPConfig, name::Symbol)::String
    if name === :hp_q_min || name === :hp_q_max
        (cfg.hp_q_min <= 0.3 && cfg.hp_q_max >= 1.0) ||
            return "q-window [$(cfg.hp_q_min), $(cfg.hp_q_max)] misses the claimed criticals 0.3…1.0 — the H4 domain guard will fire"
    end
    name === :hp_L && cfg.hp_L > 60 && return "L>60: run time grows ≈ L³ — record-grade territory, plan hours"
    name === :hp_L && cfg.hp_L < 12 && return "L<12: too few levels for unfolding statistics"
    name === :hp_n_ensemble && cfg.hp_n_ensemble > 7 &&
        return "ensemble > 7/regime: the v24.1 H5 plan caps it (≤ 40 dense solves total, user cap 2026-09-09)"
    name === :hp_zeta_cap && cfg.hp_zeta_cap < 20_000 &&
        return "ζ cap < 20000: Bragg-comb resolution reduced (50000 = full control)"
    name === :hp_deep_nulls && cfg.hp_deep_nulls < 20 &&
        return "deep-nulls < 20: DEEPEN P95 ceiling will be noisy (20 = publication-grade)"
    name === :ab_nv_list && isempty(cfg.ab_nv_list) &&
        return "empty nv list → falls back to Nv=4"
    return ""
end

# ── config profiles: save / load / list (hp_profiles/ next to the file) ──
_hp_profiles_dir() = joinpath(@__DIR__, "hp_profiles")
function _hp_profile_path(name::AbstractString)
    nm = String(name)
    occursin(r"^[A-Za-z0-9_\-]{1,32}$", nm) ||
        throw(ErrorException("profile name must match [A-Za-z0-9_-]{1,32} (got \"$nm\")"))
    return joinpath(_hp_profiles_dir(), "p_" * nm * ".cfg")
end
function hp_profile_save(cfg::HPConfig, name::AbstractString)
    path = _hp_profile_path(name)
    mkpath(dirname(path))
    open(path, "w") do io
        println(io, "# HPMeridian profile \"", name, "\" — ",
                Dates.format(Dates.now(), "yyyy-mm-dd HH:MM:SS"))
        println(io, "# one line per HPConfig field: name = value")
        for f in fieldnames(HPConfig)
            println(io, f, " = ", _hp_fmt_val(getfield(cfg, f)))
        end
    end
    return path
end
function hp_profile_load!(cfg::HPConfig, name::AbstractString)
    path = _hp_profile_path(name)
    isfile(path) || throw(ErrorException("profile \"$name\" not found at $path"))
    n = 0
    for line in eachline(path)
        s = strip(line)
        (isempty(s) || startswith(s, "#") || !occursin('=', s)) && continue
        parts = split(s, '=')
        nm = Symbol(strip(parts[1]))
        hasfield(HPConfig, nm) || continue
        try
            _hp_set_field!(cfg, nm, strip(join(parts[2:end], '=')))
            n += 1
        catch
        end
    end
    return n
end
function hp_profile_list()
    d = _hp_profiles_dir()
    isdir(d) || return String[]
    out = String[]
    for f in sort(readdir(d))
        startswith(f, "p_") && endswith(f, ".cfg") && push!(out, f[3:end-4])
    end
    return out
end

"""Shared run pipeline for the CLI and the console: ζ load →
results/run_<timestamp>/ → battery → two-files reports → summary.
Returns the run directory."""
function run_battery_core(cfg::HPConfig, sel::Vector{Int}, tag::String;
                          zeros_path::String = "")
    t_start = time()
    n_prev = length(ALL_STATES) # console may run several batteries in one session
    zpath = isempty(zeros_path) ? joinpath(@__DIR__, "zeros50k.txt") : zeros_path
    zeta = load_zeros(zpath)
    zeta_loaded = !isempty(zeta)
    zeta_loaded ?
        _mr_ok("ζ zeros: " * string(length(zeta)) * " loaded from " * zpath) :
        _mr_warn("ζ zeros: NOT FOUND at " * zpath *
                 " — H1/H7 will skip the ζ side honestly")
    ts = Dates.format(Dates.now(), "yyyy-mm-dd_HHMMSS")
    run_dir = joinpath("results", "run_$ts")
    k = 1
    while isdir(run_dir) # back-to-back console runs must not overwrite a report
        k += 1
        run_dir = joinpath("results", "run_$(ts)_$k")
    end
    mkpath(run_dir)
    println("  " * _mr_c("output dir:", "accent") * " " * _mr_c(run_dir, "bold"))
    # v23.8: the WHOLE-battery cost, stated BEFORE anything heavy starts, so a
    # FULL run on a phone is a decision, not a surprise. SIZE-WEIGHTED: 160
    # solves at 20×20 are minutes, 160 at 56×56 are hours — a bare count lies.
    _tot = sum(_hp_diag_est(cfg, k) for k in sel; init = 0)
    _w = sum(_hp_diag_est(cfg, k) * ((_hp_gate_L(cfg, k)^2) / 1024.0)^3 for k in sel;
             init = 0.0) # ~GOp units: 1 unit ≈ one 32×32-lattice (N=1024 matrix) dense eigensolve × 100 — solve cost is O(N³) = O(L⁶)
    _Lmx = maximum(_hp_gate_L(cfg, k) for k in sel)
    _peak = 2.5 * (_Lmx^2)^2 * 16 / 2^30
    println("  " * _mr_c("battery cost:", "gold") *
            _mr_c(@sprintf(" ≈ %d dense eigensolves over %d gate(s) (largest lattice %d×%d, ≈ %.1f GB peak) — on a phone count MINUTES per solve",
                           _tot, length(sel), _Lmx, _Lmx, _peak), "warn") *
            _mr_c(_w >= 500.0 ? " → hours-to-days total; try s SMOKE or f FAST first" : "",
                  "warn"))
    flush(stdout)
    _hp_run_all!(cfg, zeta, sel, run_dir, tag)
    write_run_reports(run_dir, cfg, tag, time() - t_start, zeta_loaded)
    fresh = n_prev < length(ALL_STATES) ? ALL_STATES[n_prev+1:end] : ALL_STATES
    _np = count(st.status == "PASS" for st in fresh)
    _rows = String[@sprintf("%s %s  [%s]  %s", st.status == "PASS" ? "✓" : "!",
                            st.slug, st.status,
                            isempty(st.headline) ? "" : st.headline) for st in fresh]
    push!(_rows, "outputs: " * run_dir * "/{final_report.md, final_report.html,")
    push!(_rows, "          logs/full_run_log.txt, results_verdicts.txt}")
    _mr_panel("battery summary · " * tag * "  →  " * string(_np) * "/" *
              string(length(fresh)) * " PASS", _rows)
    return run_dir
end

# ── PARAMETERS editor: all fields, described, profiled, guarded ──────────
function _hp_describe(cfg::HPConfig, nm::Symbol)
    hasfield(HPConfig, nm) || (println(_hpc("  ✗ no field `$nm` in HPConfig", "err")); return)
    println(_hpc("  " * string(nm) * " :: " * string(fieldtype(HPConfig, nm)), "bold"),
            "  = ", _hp_fmt_val(getfield(cfg, nm)))
    println("    ", get(HP_FIELD_DOC, nm, "(no description)"))
    w = _hp_soft_warn(cfg, nm)
    isempty(w) || println(_hpc("    note: " * w, "warn"))
    return
end

"""HP·MERIDIAN parameter editor — every HPConfig field, with a short hint in
the list and a full description via `? field`. Direct set: field=value.
Profiles: save <name> / load <name> / ls. Empty line goes back."""
function hp_params_menu!(cfg::HPConfig)
    flds = collect(fieldnames(HPConfig))
    while true
        println(_hpc("─"^100, "dim"))
        println(_hpc(" PARAMETERS — $(length(flds)) fields", "bold"),
                _hpc("   direct set: field=value · edit: <number> · describe: ? field", "dim"))
        println(_hpc("   profiles: save <name> · load <name> · ls        empty line = back to the console", "dim"))
        println(_hpc("─"^100, "dim"))
        for (i, f) in enumerate(flds)
            f === :ab_t && println(_hpc("   ── AB physics constants (suite defaults; bit-equal with the big suite) ──", "dim"))
            @printf("  %2d  %-20s = %-16s %s\n", i, string(f),
                    _hp_fmt_val(getfield(cfg, f)),
                    _hpc(get(HP_FIELD_HINT, f, ""), "dim"))
        end
        ans = _hp_ask(_hpc(" params", "accent") * _hpc("> ", "dim"))
        (ans === nothing || isempty(ans)) && return nothing
        line = ans
        low = lowercase(line)
        try
            if startswith(low, "save ")
                nm = strip(line[6:end])
                isempty(nm) && (println("  usage: save <name>"); continue)
                p = hp_profile_save(cfg, nm)
                println(_hpc("  ✓ profile saved → ", "ok"), p)
            elseif startswith(low, "load ")
                nm = strip(line[6:end])
                n = hp_profile_load!(cfg, nm)
                println(_hpc("  ✓ profile \"$nm\" loaded ($n fields)", "ok"))
                params_banner(cfg)
            elseif low == "ls"
                ps = hp_profile_list()
                println(isempty(ps) ?
                        _hpc("  (no profiles yet — save one with: save mysetup)", "dim") :
                        "  profiles: " * join(ps, ", "))
            elseif startswith(line, "?")
                nm = Symbol(strip(line[2:end]))
                _hp_describe(cfg, nm)
            elseif !isempty(line) && all(isdigit, line)
                i = parse(Int, line)
                (1 <= i <= length(flds)) ||
                    (println(_hpc("  ✗ no field #$i (1…$(length(flds)))", "err")); continue)
                f = flds[i]
                print("  ", f, " [", _hp_fmt_val(getfield(cfg, f)), "] = ")
                flush(stdout)
                raw = strip(readline(stdin))
                isempty(raw) && continue
                _hp_set_field!(cfg, f, raw)
                println(_hpc("  → ", "ok"), f, " = ", _hp_fmt_val(getfield(cfg, f)))
                w = _hp_soft_warn(cfg, f)
                isempty(w) || println(_hpc("  note: " * w, "warn"))
            elseif occursin('=', line)
                parts = split(line, '=')
                name = Symbol(strip(parts[1]))
                raw = strip(join(parts[2:end], '='))
                _hp_set_field!(cfg, name, raw)
                println(_hpc("  → ", "ok"), name, " = ", _hp_fmt_val(getfield(cfg, name)))
                w = _hp_soft_warn(cfg, name)
                isempty(w) || println(_hpc("  note: " * w, "warn"))
            else
                println(_hpc("  ✗ use <number>, field=value, ? field, save/load/ls", "err"))
            end
        catch e
            println(_hpc("  ✗ ", "err"), e isa ErrorException ? e.msg : sprint(showerror, e))
        end
    end
end

# ── environment helpers ──────────────────────────────────────────────────
function _hp_discover_zeros()::String
    cands = String[]
    get(ENV, "HP_ZEROS", "") != "" && push!(cands, ENV["HP_ZEROS"])
    push!(cands, joinpath(@__DIR__, "zeros50k.txt"))
    push!(cands, joinpath(pwd(), "zeros50k.txt"))
    for c in cands
        isfile(c) && return c
    end
    return joinpath(@__DIR__, "zeros50k.txt") # default (missing → honest NOT FOUND)
end

function _hp_zero_status(zeros_path::String)::String
    isfile(zeros_path) || return _hpc("ζ: NOT FOUND (z to fix)", "err")
    return _hpc(@sprintf("ζ: %d ordinates", length(load_zeros(zeros_path))), "ok")
end

function _hp_hpcenter(t::AbstractString, w::Int)
    pad = max(0, w - textwidth(String(t)))
    l = pad ÷ 2
    return " "^l * String(t) * " "^(pad - l)
end

function _hp_banner(cfg::HPConfig, preset::Symbol, zeros_path::String)
    W = 72
    println(_hpc("╔" * "═"^W * "╗", "title"))
    println(_hpc("║", "title") * _hp_hpcenter("HP·MERIDIAN — Hilbert–Pólya Audit Console", W) * _hpc("║", "title"))
    println(_hpc("║", "title") * _hp_hpcenter("7 gates between prime arithmetic and GUE spectral statistics", W) * _hpc("║", "title"))
    println(_hpc("╚" * "═"^W * "╝", "title"))
    for a in HP_AUDITS
        k = a.id - 300
        short = replace(a.title, r"^H\d+\.\s*" => "")
        @printf("  %d  %s %s %s\n", k, _hpc("[" * a.group * "]", "accent"),
                _hpc(rpad(get(GATE_NAME, k, ""), 13), "bold"), short)
    end
    println(_hpc("─"^W, "dim"))
    println("  1-7 run gate · a all · gA gB gC gD reviewer group · f/F/s preset · r reset")
    println("  p parameters (all fields, profiles) · i intel · d doctor · v last run")
    println("  z ζ-zeros path · b params banner · h help · q quit (code stays loaded)")
    println(_hpc("─"^W, "dim"))
    println(" ", _hpc("preset :$preset", "bold"), " · L=$(cfg.hp_L) · ensemble=$(cfg.hp_n_ensemble) · ",
            "seed=$(cfg.hp_seed) · ", _hp_zero_status(zeros_path))
    println(_hpc(" out: " * joinpath(pwd(), "results") * " · HP·MERIDIAN v" * HP_SA_VERSION, "dim"))
    return
end

function _hp_intel(cfg::HPConfig, preset::Symbol)
    pi_ = preset === :smoke ? 1 : preset === :fast ? 2 : 3
    println(_hpc("═"^72, "dim"))
    println(_hpc(" GATE INTEL — what each audit decides · cost at preset :$preset", "bold"))
    println(_hpc("═"^72, "dim"))
    total = 0.0
    for a in HP_AUDITS
        k = a.id - 300
        m = get(GATE_MIN, k, (0.0, 0.0, 0.0))[pi_]
        total += m
        println(_hpc(" H$k · $(get(GATE_NAME, k, ""))  [$(a.group)]  $(a.title)", "bold"))
        println("    ", a.about)
        println(_hpc("    cost at :$preset ≈ " * _fmt_min(m) * " (CPU-dependent; ensemble multiplies)", "dim"))
        println()
    end
    println(_hpc(" full battery at :$preset ≈ " * _fmt_min(total), "bold"),
            _hpc("  (detector-validity verdicts; physics headlines inside)", "dim"))
    return
end

function _hp_doctor(cfg::HPConfig, preset::Symbol, zeros_path::String)
    println(_hpc("═"^72, "dim"))
    println(_hpc(" ENVIRONMENT DOCTOR — is everything the gates need in place?", "bold"))
    println(_hpc("═"^72, "dim"))
    os = Sys.iswindows() ? "windows" : Sys.isapple() ? "macos" : "linux"
    @printf("  julia %s · threads %d · %s · stdin tty %s · stdout tty %s · color %s\n",
            string(VERSION), Threads.nthreads(), os,
            _hp_stdin_tty() ? "yes" : "no", stdout isa Base.TTY ? "yes" : "no",
            _COLOR_ON[] ? "on" : "off")
    if isfile(zeros_path)
        z = load_zeros(zeros_path)
        rng = isempty(z) ? "EMPTY FILE" : @sprintf("γ₁=%.4f … γ%d=%.4f", z[1], length(z), z[end])
        println("  ", _hpc("✓", "ok"), " ζ zeros: $zeros_path — $(length(z)) ordinates ($rng)")
    else
        println("  ", _hpc("✗", "err"), " ζ zeros NOT FOUND at $zeros_path — H1/H7 run WITHOUT the ζ side")
        println("      fix: console z · CLI zeros=path · ENV[\"HP_ZEROS\"] (need the zeros50k.txt)")
    end
    od = joinpath(pwd(), "results")
    okw = false
    try
        mkpath(od)
        tp = joinpath(od, ".hp_write_test")
        touch(tp); rm(tp)
        okw = true
    catch
    end
    println("  ", okw ? _hpc("✓", "ok") : _hpc("✗", "err"), " output dir: $od ",
            okw ? "(writable)" : "(NOT writable — cd to a writable dir first)")
    plan5 = _hp5_plan(cfg)
    println("  ", _hpc("✓", "ok"), " H5 solve plan = ", _hpc("$(plan5.total)", "bold"),
            " dense eigensolves (v24.1 cap ", string(HP5_SOLVE_CAP), ": ",
            "$(plan5.n_reg)×$(plan5.E) ensemble", plan5.Nα > 0 ? " + 6×$(plan5.Nα) α-profile" : "",
            ")")
    cfg.hp_zeta_cap >= 20_000 ?
        println("  ", _hpc("✓", "ok"), " ζ cap = $(cfg.hp_zeta_cap)") :
        println("  ", _hpc("△", "warn"), " ζ cap = $(cfg.hp_zeta_cap) < 20000 — Bragg-comb control reduced")
    (cfg.hp_q_min <= 0.3 && cfg.hp_q_max >= 1.0) ?
        println("  ", _hpc("✓", "ok"), " H4 q-window [$(cfg.hp_q_min), $(cfg.hp_q_max)] contains claimed criticals") :
        println("  ", _hpc("△", "warn"), " H4 q-window [$(cfg.hp_q_min), $(cfg.hp_q_max)] MISSES 0.3…1.0 — domain guard will fire")
    cfg.hp_deep_nulls >= 20 ?
        println("  ", _hpc("✓", "ok"), " DEEPEN nulls = $(cfg.hp_deep_nulls) (P95 ceiling stable)") :
        println("  ", _hpc("△", "warn"), " DEEPEN nulls = $(cfg.hp_deep_nulls) < 20 — P95 ceiling noisy")
    println(_hpc("─"^72, "dim"))
    params_banner(cfg)
    return
end

function _hp_view_last()
    rdir = joinpath(pwd(), "results")
    isdir(rdir) || (println(_hpc(" no runs yet in $rdir — run a gate first (1-7 or a)", "warn")); return)
    ds = [d for d in readdir(rdir) if startswith(d, "run_") && isdir(joinpath(rdir, d))]
    isempty(ds) && (println(_hpc(" no run_* directories yet in $rdir", "warn")); return)
    sort!(ds; by = d -> stat(joinpath(rdir, d)).mtime)
    last_dir = joinpath(rdir, ds[end])
    println(_hpc(" LAST RUN: ", "bold"), last_dir)
    vf = joinpath(last_dir, "results_verdicts.txt")
    if isfile(vf)
        println(_hpc("─"^72, "dim"))
        for line in eachline(vf)
            println("  ", line)
        end
        println(_hpc("─"^72, "dim"))
    else
        println(_hpc(" (results_verdicts.txt missing — run interrupted?)", "warn"))
    end
    return
end

function _hp_help()
    println(_hpc("─"^72, "dim"))
    println("  RUN     1..7 one gate · a all seven · gA/gB/gC/gD reviewer groups")
    println("  SCALE   s SMOKE (~2-3 min, validation) · f FAST (L=72, hours — heavy, phone: plan days for H5) ·")
    println("          F FULL (L=56, hours, record-grade) · r reset parameters")
    println("  H5 FOCUS 5d — focused regime-D run: ALL 40 solves on [D], N=40 (p: hp_regime_mode=:regime_d|:showdown)")
    println("  TUNE    p parameters — edit ALL fields (field=value), ? field docs,")
    println("          save/load/ls config profiles (hp_profiles/ next to this file)")
    println("  INFO    i gate intel (what decides what, cost per preset) · d doctor")
    println("          (zeros/output/sanity check) · v last run verdicts · b banner")
    println("  EXIT    q or Ctrl-C at the prompt — code STAYS loaded (hp_console()")
    println("          reopens); Ctrl-C during a run aborts the run, console stays")
    println("  FILES   ./results/run_<timestamp>/: final_report.md+html,")
    println("          logs/full_run_log.txt, results_verdicts.txt, per-gate REPORT+PNG")
    println("  BATCH   main([\"fast\"]) · main([\"full\",\"h1\",\"h5\",\"seed=777\"]) — no console")
    println(_hpc("─"^72, "dim"))
    return
end

"""HP·MERIDIAN console — the interactive front-end. Opens itself on include()
in a live REPL. q / Ctrl-C return to the REPL with all code still loaded.
Every command is failure-isolated: an error in one command never kills the
console (v23.6.1 lesson)."""
function hp_console(cfg::HPConfig = make_hp_config())
    _color_init!()
    register_audits!()
    isempty(HP_AUDITS) && (println("no audits registered — file corrupted?"); return nothing)
    zeros_path = _hp_discover_zeros()
    preset = :fast
    apply_preset!(cfg, preset) # safe default: an accidental 'a' stays cheap
    isfile(zeros_path) ||
        println(_hpc(" (note) ζ zeros not found — H1/H7 will run WITHOUT the ζ side; press z to set the path (need zeros50k.txt next to this file or in the working dir)", "warn"))
    println()
    while true
        _hp_banner(cfg, preset, zeros_path)
        ask = _hp_ask(_hpc(" meridian", "title") * _hpc("> ", "dim"))
        if ask === nothing
            println()
            println(_hpc(" console closed — code stays loaded: hp_console() reopens · main([\"fast\"]) batch-runs", "dim"))
            return nothing
        end
        isempty(ask) && continue
        c = lowercase(ask)
        try
            if c in ("q", "quit", "exit", "x")
                println(_hpc(" console closed — the audit code STAYS LOADED in this session:", "dim"))
                println("   hp_console()            reopen this console")
                println("   main([\"full\"])          batch battery (fast|full|smoke · h1..h7 · seed= · zeros=)")
                println("   hp_params_menu!(cfg)    parameter editor on your own config")
                return nothing
            elseif occursin(r"^[1-7]$", c)
                run_battery_core(cfg, [parse(Int, c)], "menu"; zeros_path = zeros_path)
            elseif c in ("a", "all")
                run_battery_core(cfg, collect(1:7), "menu"; zeros_path = zeros_path)
            elseif occursin(r"^g[abcd]$", c)
                grp = uppercase(string(c[2]))
                sel = Int[a.id - 300 for a in HP_AUDITS if a.group == grp]
                isempty(sel) || run_battery_core(cfg, sel, "menu-g$grp"; zeros_path = zeros_path)
            elseif c == "5d" # v24.2: focused regime-D H5 run — one command, mode persists until switched back
                cfg.hp_regime_mode = :regime_d
                println(_hpc(" mode → :regime_d (FOCUS-D: all 40 solves on [D]; p → hp_regime_mode=:showdown to return)", "accent"))
                run_battery_core(cfg, [5], "menu-focus-d"; zeros_path = zeros_path)
            elseif ask == "F" || c == "full"
                preset = :full
                apply_preset!(cfg, preset)
            elseif c in ("f", "fast")
                preset = :fast
                apply_preset!(cfg, preset)
            elseif c in ("s", "smoke")
                preset = :smoke
                apply_preset!(cfg, preset)
            elseif c in ("r", "reset")
                cfg = make_hp_config()
                apply_preset!(cfg, preset)
                println(_hpc(" parameters reset to code defaults (+ preset :$preset)", "ok"))
            elseif c == "p"
                hp_params_menu!(cfg)
            elseif c == "i"
                _hp_intel(cfg, preset)
            elseif c == "d"
                _hp_doctor(cfg, preset, zeros_path)
            elseif c == "v"
                _hp_view_last()
            elseif c == "b"
                params_banner(cfg)
            elseif c == "z"
                print(" path to ζ-zeros file [", zeros_path, "] > ")
                flush(stdout)
                np = strip(readline(stdin))
                isempty(np) || (zeros_path = String(np))
                println(isfile(zeros_path) ?
                        _hpc(@sprintf(" ζ zeros: OK — %d ordinates (used by the next run)", length(load_zeros(zeros_path))), "ok") :
                        _hpc(" ζ zeros: NOT FOUND at $zeros_path — H1/H7 will skip the ζ side honestly (WARN)", "warn"))
            elseif c in ("h", "help", "?")
                _hp_help()
            else
                println(_hpc(" unknown command: \"$ask\"", "err"),
                        _hpc(" — h = help, q = quit", "dim"))
            end
        catch e
            if e isa InterruptException
                REP.current = nothing
                println(_hpc("\n run interrupted (Ctrl-C) — back to the console (the aborted run's master report was not finalized)", "warn"))
            else
                println(_hpc("\n command failed: ", "err"), sprint(showerror, e))
                println(_hpc(" console stays alive — h = help; if this repeats, report the text above", "dim"))
            end
        end
    end
end
"Backward-compatible alias for hp_console (v23.6.1 name)."
hp_menu(cfg::HPConfig = make_hp_config()) = hp_console(cfg)

function main(args::Vector{String} = ARGS)
    isempty(args) || (args == ["-h"] || args == ["--help"]) && (usage(); return)
    if isempty(args) && _hp_stdin_tty() && get(ENV, "HP_SA_NO_MENU", "0") != "1"
        # started with no arguments from a terminal → console, not a surprise battery
        println(_hpc(" no CLI args → opening the HP·MERIDIAN console", "dim"))
        println(_hpc(" (batch: julia hp_audit_standalone.jl [fast|full|smoke] [h1..h7|all] [seed=N] [zeros=path])", "dim"))
        return hp_console()
    end
    mode = :fast
    sel = Int[]
    zeros_path = ""
    cfg = make_hp_config()
    for a in args
        la = lowercase(a)
        if la in ("fast", "full", "smoke")
            mode = Symbol(la)
        elseif startswith(la, "zeros=")
            zeros_path = String(split(a, '=')[2])
        elseif startswith(la, "seed=")
            cfg.hp_seed = parse(Int, split(a, '=')[2])
        elseif occursin(r"^h[1-7]$", la)
            push!(sel, parse(Int, la[2]))
        elseif la == "all"
            empty!(sel)
        else
            println("ignoring unknown arg: $a"); usage()
        end
    end
    isempty(sel) && (sel = collect(1:7))

    _mr_banner("HP·MERIDIAN — HILBERT–PÓLYA DEEP AUDIT", "v" * HP_SA_VERSION,
               "arithmetic specificity, not just universality — 7 falsifiable gates H1–H7",
               "core from ab_cloud_v23_v2.jl (suite) · ABPlotV23 journal engine")
    apply_preset!(cfg, mode)
    register_audits!()
    params_banner(cfg)

    run_battery_core(cfg, sel, string(mode); zeros_path = zeros_path)
    return nothing
end

end # module HPMeridian

# ═════════════════════════════════════════════════════════════════════════
# Main-scope bootstrap — executes on include() and on script start.
# Re-include SAFE: module HPMeridian is simply replaced (no struct
# redefinition errors — the v23.6.1 «include twice → error storm» is gone).
# The public API is bound DIRECTLY into Main (instead of `using`) so every
# re-include refreshes the bindings: no "both HPMeridian and HPMeridian
# export ..." ambiguity, no stale functions from the previous module world.
# ═════════════════════════════════════════════════════════════════════════
for _nm in (:hp_console, :hp_menu, :main, :make_hp_config, :apply_preset!,
            :hp_params_menu!, :run_battery_core, :load_zeros,
            :register_audits!, :HPConfig, :HP_AUDITS, :HP_SA_VERSION)
    @eval Main $_nm = getfield(HPMeridian, $(QuoteNode(_nm)))
end

if abspath(PROGRAM_FILE) == @__FILE__
    HPMeridian.main(ARGS) # no args + terminal → console; args → batch battery
elseif get(ENV, "HP_SA_NO_MENU", "0") == "1"
    println(" HPMeridian v$(HPMeridian.HP_SA_VERSION) loaded (console off: HP_SA_NO_MENU=1) — hp_console() opens it")
elseif isinteractive() || HPMeridian._hp_stdin_tty()
    println(" HPMeridian v$(HPMeridian.HP_SA_VERSION) loaded — opening the HP·MERIDIAN console")
    println(" (q or Ctrl-C returns to the REPL · h = help · disable: ENV[\"HP_SA_NO_MENU\"]=\"1\")")
    try
        HPMeridian.hp_console()
    catch err
        err isa InterruptException ||
            rethrow()
        println("(console closed by Ctrl-C — code stays loaded; hp_console() reopens)")
    end
else
    println(" HPMeridian v$(HPMeridian.HP_SA_VERSION) loaded (non-interactive include — console not started)")
    println(" call  hp_console()  to open it, or  main([\"fast\"])  for a batch battery")
end
