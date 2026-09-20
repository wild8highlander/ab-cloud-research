# =============================================================================
#
#   ████ TEST 34 · STANDALONE LABORATORY ████
#   AB-cloud model  vs  Riemann zeta zeros  —  exclusive Test 34 research
#
#   File        :  finite-size_lab.jl
#   Language    :  Julia >= 1.9   (no external packages, stdlib only)
#   Usage (REPL):  include("finite-size_lab.jl")     -> interactive menu opens
#   Usage (CLI) :  julia finite-size_lab.jl                 -> interactive menu
#                  julia finite-size_lab.jl --selftest      -> environment check
#                  julia finite-size_lab.jl --mode=1 --headless --count=50000
#                     [--mode=1|2|3|4|5] [--zeros=path] [--count=N] [--L=96]
#                     [--alpha=0.5] [--Nv=2] [--q=1.0] [--W=1.0] [--reps=5]
#                     [--geometry=torus|klein|pillow|cubic|psl27|psl28|psl213]
#                     [--geoms=torus,psl27,...]  [--reps5=3] [--lang=en|ru]
#                     [--headless]
#
#   BIG-MATRIX FIX (v1.1, 2026-09-19):
#     Previously geom_L_eff silently DEGRADED the requested lattice on every
#     non-torus geometry: the cube sphere was clamped to L <= 12 (<= 728 sites
#     instead of the 96x96 = 9216-site big matrix), the Klein bottle / pillow
#     fold carried only L^2/2 sites (half the torus at the same L), and the
#     Hurwitz Cayley groups ignored L entirely. That turned every non-torus
#     selection into a small synthetic-looking run. Now ALL scalable geometries
#     auto-scale to the SAME site budget as the L x L torus (default L = 96 ->
#     ~9216 sites: Klein/pillow 136 (9248 sites), cube sphere L=40 (9128
#     sites)) and are genuinely diagonalized there. Toggle: menu [8] -> [a],
#     lab_settings.ini "autoscale=", CLI --autoscale=on|off. The three Hurwitz
#     surfaces PSL(2,q) are fixed by mathematics (|G| = 168/504/1092 = 84(g-1)
#     sites) — they are still fully computed, just at their irreducible size.
#
#   HURWITZ BIG-MATRIX + HONEST-SIZE FIX (v1.2, 2026-09-19):
#     * NEW geometry :psl227 — the Hurwitz surface PSL(2,27): |G| = 9828 =
#       84(g-1), genus 118, chi = -234. (3,7)-generation verified
#       computationally (Macbeath: q = 27 = -1 mod 7 is Hurwitz); GF(27) =
#       GF(3)[x]/(x^3 + 2x + 1) arithmetic added to FieldCtx. At the default
#       L = 96 this is the BIG Hurwitz matrix (9828 sites ~ the 96x96 torus
#       budget of 9216) that the small Hurwitz groups (168/504/1092) can
#       never provide.
#     * HONEST SIZING (fixes "menu ignores my L"): the status panel, the
#       geometry menu and the model menu no longer claim "~L^2 sites" for
#       fixed-size Hurwitz groups — they now state plainly that L is NOT
#       applied and show the fixed |G|. Every mode prints a matrix-size
#       warning when the built matrix is < 90% of the L^2 budget, with a
#       concrete remedy (switch geometry / enable autoscale).
#     * Fixed string-interpolation bug in MODE 5 ("L=$saved.L" printed the
#       whole settings tuple instead of the number).
#
#   HURWITZ STRETCH — "stretch the space" (v1.3, 2026-09-19):
#     The user asked: "when you pick the torus it grows with L; stretch the
#     space for the other geometries too — the matrix size must equal the
#     space of that geometry." Done: every Hurwitz Cayley geometry now STRETCHES
#     by a Z_k voltage lift — sites = |G|*k with k in {1, 7, 14, 21, ...}, the
#     multiple of 7 landing closest to the L^2 budget (same envelope as the
#     torus, LAB_MAX_SITES). At the default L = 96:
#       psl27  |G|=168  × k=56 -> 9408 sites  (102% of 9216)
#       psl28  |G|=504  × k=21 -> 10584 sites (115%)
#       psl213 |G|=1092 × k=7  -> 7644 sites  (83%)
#       psl227 |G|=9828 × k=1  -> 9828 sites  (107%, lift not needed)
#     Construction: vertices (g, t), g in G, t in Z_k; B-bond (g,t)-(gB, t+vB),
#     C-bond (g,t)-(gC, t+vC). The lift is 4-regular, locally identical to the
#     base Cayley graph and verified connected (BFS). k is ALWAYS a multiple of
#     7 and vC = k/7, so every C-orbit closes into an honest heptagon carrying
#     exactly 2*pi*q*alpha*Nv — the flux knob is preserved bit-for-bit. The
#     zero-flux B-triangles open into 3k-cycles (phiB = 0: no physics lost).
#     vB is drawn from the units of Z_k by a seeded deterministic search.
#     autoscale OFF keeps the historical fixed-|G| matrix (k = 1) verbatim.
#     MODE 3 finite-size scaling now also works on Hurwitz geometries (the
#     ladder k = 1 -> 7 -> 14 ... realizes the L sweep).
#
#   Modes:
#     [1] NORMAL      — refined primary pass   (default 5  realizations)
#     [2] HARDCORE    — refined ensemble pass  (default 20 realizations)
#     [3] DEEP DIAG   — CDF differential, short-range repulsion profile,
#                       seed forensics, bootstrap CI, lattice scaling
#     [4] CONFIGURATOR— vortex parameter sweep (alpha/Nv/q/W) with
#                       stabilization-zone map   (exploratory / response
#                       fitting tool — by explicit request)
#     [5] UNIVERSAL   — GEOMETRY SWEEP: every geometry x tests 1-4 x N
#                       realizations each (default 3) in one light pass;
#                       pooled verdicts per geometry and a global verdict.
#
#   Geometries (menu [8] / --geometry=..., used by ALL modes):
#     torus   T^2 flat periodic lattice          genus 1   (original model)
#     klein   Klein bottle  = T^2 / glide tau    demigenus 2 (non-orientable)
#     pillow  Pillow orbifold = T^2 / (x~-x)     sphere w/ 4 cone points
#     cubic   Cube sphere: cube surface subdivided L x L per face (octahedral)
#     psl27   Klein quartic       PSL(2,7)  |G|=168  = 84(g-1), g=3   HURWITZ
#     psl28   Macbeath surface    PSL(2,8)  |G|=504  = 84(g-1), g=7   HURWITZ
#     psl213  Fricke-Klein        PSL(2,13) |G|=1092 = 84(g-1), g=14  HURWITZ
#     psl227  Hurwitz-118         PSL(2,27) |G|=9828 = 84(g-1), g=118 HURWITZ
#             (BIG Hurwitz matrix: ~9828 sites ~ the L=96 torus budget 9216;
#              verified (3,7)-generated, Macbeath q=-1 mod 7 Hurwitz family)
#   Hurwitz surfaces are modeled as magnetic Cayley graphs Cay(G; B, C) with
#   ord(B)=3, ord(C)=7 (the (2,3,7) Hurwitz generators, found by a deterministic
#   search): every heptagonal C-face carries exactly the vortex flux
#   2*pi*q*alpha*Nv — the same flux knob as the torus vortex ring.
#
#   Test 34 metrics:  two-sample KS  D and p (unfolded spacings),
#     Montgomery pair correlation R2(s), d_GUE / d_Pois distances,
#     R2 plateau over s in [1.0, 2.0], composite verdict (v23-compatible):
#       PASS  <=>  (p > 0.01  OR  D < 0.10)  AND  d_GUE < d_Pois
#                  AND  0.75 <= plateau <= 1.25
#
#   Zeros files: the script AUTO-SCANS its own directory (and cwd) for text
#     files that look like Riemann zeros (one per line, "n gamma", "0.5 gamma",
#     comma separated, comment lines "#" allowed). The best candidate is
#     auto-selected; you can pick file + number of zeros in the menu.
#
#   Output: results/run_<timestamp>_m<mode>/  with FINAL_REPORT.md,
#     index.html, PNG plots 1600x1000 (built-in engine, zero dependencies),
#     CSV data and config.json. All timing is recorded.
#
# =============================================================================

using LinearAlgebra
using LinearAlgebra: LAPACK
using Random
using Statistics
using Printf
using Dates
using Libdl

const LAB_SCRIPT_DIR = @__DIR__
const LAB_T0_GLOBAL  = time()

# -----------------------------------------------------------------------------
# Settings (mutable singleton) + persistence
# -----------------------------------------------------------------------------

mutable struct LabSettings
    lang         :: Symbol      # :en | :ru
    zeros_file   :: String      # path to selected zeros file
    zeros_avail  :: Int         # zeros available in that file
    n_zeros      :: Int         # how many zeros to use
    L            :: Int         # lattice side (L x L sites)
    Nv           :: Int         # number of AB vortices
    q            :: Float64     # charge (multiplier of flux)
    alpha        :: Float64     # flux per vortex alpha (units of Phi0)
    W            :: Float64     # onsite disorder width
    reps1        :: Int         # mode 1 realizations
    reps2        :: Int         # mode 2 realizations
    reps3seeds   :: Int         # mode 3 seed-forensics runs
    reps4        :: Int         # mode 4 realizations per sweep point
    reps5        :: Int         # mode 5 realizations per test per geometry
    sweep_param  :: Symbol      # :alpha | :Nv | :q | :W
    seed_base    :: Int
    out_root     :: String      # results root (relative to script dir)
    plots_on     :: Bool
    nchunks      :: Int         # eigenvalue chunks (progress granularity)
    window_frac  :: Float64     # central fraction of spectrum used
    geometry     :: Symbol      # :torus | :klein | :pillow | :cubic | :psl27 | :psl28 | :psl213
    autoscale    :: Bool        # BIG-MATRIX FIX: scale every geometry to the L^2 site budget
end

function LabSettings()
    LabSettings(
        :en, "", 0, 50_000,
        96, 2, 1.0, 0.5, 1.0,
        5, 20, 5, 1, 3,
        :alpha, 20260916,
        joinpath(LAB_SCRIPT_DIR, "results"),
        true, 10, 0.5,
        :torus, true,
    )
end

const LAB = LabSettings()

const LAB_SETTINGS_FILE = joinpath(LAB_SCRIPT_DIR, "lab_settings.ini")

const LAB_ALLOWED_L = (32, 48, 64, 80, 96, 112, 128, 144)

function lab_save_settings()
    try
        open(LAB_SETTINGS_FILE, "w") do io
            println(io, "# finite-size_lab.jl settings (auto-saved)")
            println(io, "lang=", LAB.lang)
            println(io, "zeros_file=", LAB.zeros_file)
            println(io, "n_zeros=", LAB.n_zeros)
            println(io, "L=", LAB.L)
            println(io, "Nv=", LAB.Nv)
            println(io, "q=", LAB.q)
            println(io, "alpha=", LAB.alpha)
            println(io, "W=", LAB.W)
            println(io, "reps1=", LAB.reps1)
            println(io, "reps2=", LAB.reps2)
            println(io, "reps3seeds=", LAB.reps3seeds)
            println(io, "reps4=", LAB.reps4)
            println(io, "reps5=", LAB.reps5)
            println(io, "sweep_param=", LAB.sweep_param)
            println(io, "seed_base=", LAB.seed_base)
            println(io, "plots_on=", LAB.plots_on)
            println(io, "window_frac=", LAB.window_frac)
            println(io, "geometry=", LAB.geometry)
            println(io, "autoscale=", LAB.autoscale)
        end
    catch
        # settings persistence is best-effort only
    end
    nothing
end

function lab_load_settings()
    isfile(LAB_SETTINGS_FILE) || return nothing
    try
        for line in eachline(LAB_SETTINGS_FILE)
            line = strip(line)
            (isempty(line) || startswith(line, "#")) && continue
            k, v = (split(line, '='; limit=2)..., "", "")
            k = strip(String(k)); v = strip(String(v))
            k == "lang"        && (LAB.lang = Symbol(v))
            k == "zeros_file"  && (LAB.zeros_file = v)
            k == "n_zeros"     && (LAB.n_zeros = something(tryparse(Int, v), LAB.n_zeros))
            k == "L"           && (LAB.L = something(tryparse(Int, v), LAB.L))
            k == "Nv"          && (LAB.Nv = something(tryparse(Int, v), LAB.Nv))
            k == "q"           && (LAB.q = something(tryparse(Float64, v), LAB.q))
            k == "alpha"       && (LAB.alpha = something(tryparse(Float64, v), LAB.alpha))
            k == "W"           && (LAB.W = something(tryparse(Float64, v), LAB.W))
            k == "reps1"       && (LAB.reps1 = something(tryparse(Int, v), LAB.reps1))
            k == "reps2"       && (LAB.reps2 = something(tryparse(Int, v), LAB.reps2))
            k == "reps3seeds"  && (LAB.reps3seeds = something(tryparse(Int, v), LAB.reps3seeds))
            k == "reps4"       && (LAB.reps4 = something(tryparse(Int, v), LAB.reps4))
            k == "reps5"       && (LAB.reps5 = something(tryparse(Int, v), LAB.reps5))
            k == "sweep_param" && (LAB.sweep_param = Symbol(v))
            k == "seed_base"   && (LAB.seed_base = something(tryparse(Int, v), LAB.seed_base))
            k == "plots_on"    && (LAB.plots_on = v == "true")
            k == "window_frac" && (LAB.window_frac = something(tryparse(Float64, v), LAB.window_frac))
            k == "geometry"    && begin
                gid = Symbol(v)
                any(g -> g.id === gid, GEOMETRY_LIST) && (LAB.geometry = gid)
            end
            k == "autoscale"   && (LAB.autoscale = v == "true")
        end
    catch
        # ignore corrupt settings
    end
    nothing
end

# -----------------------------------------------------------------------------
# Run directory / run id
# -----------------------------------------------------------------------------

const LAB_RUN_ID = Ref(Dates.format(Dates.now(), "yyyymmdd_HHMMSS"))

function lab_new_run_dir(mode::Int)
    ts = Dates.format(Dates.now(), "yyyymmdd_HHMMSS")
    LAB_RUN_ID[] = ts * "_m$mode"
    dir = joinpath(LAB.out_root, "run_" * LAB_RUN_ID[])
    mkpath(dir)
    return dir
end

const RNG_TYPE = isdefined(Random, :Xoshiro) ? Random.Xoshiro : Random.MersenneTwister

lab_rng(seed::Integer) = RNG_TYPE(UInt64(seed) ⊻ 0x9e3779b97f4a7c15)

lab_seed(mode::Int, k::Int) = LAB.seed_base * 1_000_003 + mode * 10_007 + k * 101
# =============================================================================
# Console utilities: colors, formatting, prompts, ONE-LINE realtime progress bar
# =============================================================================

const LAB_TTY = Ref(true)
lab_use_color() = LAB_TTY[] && (stdout isa Base.TTY)

const C_RST  = "\e[0m"
const C_B    = "\e[1m"
const C_DIM  = "\e[2m"
const C_RED  = "\e[31m"
const C_GRN  = "\e[32m"
const C_YLW  = "\e[33m"
const C_BLU  = "\e[34m"
const C_MAG  = "\e[35m"
const C_CYN  = "\e[36m"
const C_GRY  = "\e[90m"
const C_WHT  = "\e[97m"

function cc(text::AbstractString, codes::AbstractString...)
    lab_use_color() || return String(text)
    return string(join(codes), text, C_RST)
end

lab_clearscreen() = lab_use_color() && print(stdout, "\e[H\e[2J")

function fmt_hms(sec::Real)
    s = max(0, round(Int, sec))
    h, r = divrem(s, 3600)
    m, sec2 = divrem(r, 60)
    return h > 0 ? @sprintf("%02d:%02d:%02d", h, m, sec2) : @sprintf("%02d:%02d", m, sec2)
end

fmt_sec(sec::Real) = sec < 60 ? @sprintf("%.2fs", sec) : fmt_hms(sec)

fmt_bytes(n::Integer) = n < 1024            ? "$n B"  :
                        n < 1024^2          ? @sprintf("%.1f KB", n/1024) :
                        n < 1024^3          ? @sprintf("%.1f MB", n/1024^2) :
                                              @sprintf("%.2f GB", n/1024^3)

# ---------------------------------------------------------------- console I/O

# BUGFIX (hang-on-EOF): stdin can be closed in headless/piped runs; without an
# explicit EOF guard the interactive menu re-rendered forever, because
# readline() returns "" at end-of-file and the menu treated it as "invalid
# choice". LAB_STDIN_OPEN flips to false at the first EOF and every
# lab_ask/main_menu call short-circuits gracefully.
const LAB_STDIN_OPEN = Ref(true)

function lab_ask(prompt::AbstractString, default::AbstractString = "")
    print(stdout, prompt)
    if !isempty(default)
        print(stdout, cc(" [$default]", C_GRY))
    end
    print(stdout, " ")
    flush(stdout)
    !LAB_STDIN_OPEN[] && return String(default)
    s = ""
    try
        if eof(stdin)                       # true on closed/piped-exhausted stdin
            LAB_STDIN_OPEN[] = false
            println(stdout)
            return String(default)
        end
        s = strip(readline(stdin))
    catch
        LAB_STDIN_OPEN[] = false
        return String(default)
    end
    return isempty(s) ? String(default) : String(s)
end

function lab_ask_int(prompt::AbstractString, default::Int; lo::Int = typemin(Int), hi::Int = typemax(Int))
    for _ in 1:6
        s = lab_ask(prompt, string(default))
        v = tryparse(Int, s)
        if v !== nothing && lo <= v <= hi
            return v
        end
        println(stdout, cc("  ! " * t(:err_int_range) * " ($lo..$hi)", C_YLW))
    end
    return default
end

function lab_ask_float(prompt::AbstractString, default::Float64; lo::Real = -Inf, hi::Real = Inf)
    for _ in 1:6
        s = lab_ask(prompt, string(default))
        v = tryparse(Float64, replace(s, "," => "."))
        if v !== nothing && lo <= v <= hi
            return v
        end
        println(stdout, cc("  ! " * t(:err_float_range) * " ($lo..$hi)", C_YLW))
    end
    return default
end

function lab_pause()
    lab_ask(cc(t(:press_enter), C_GRY), "")
    nothing
end

# ------------------------------------------------------------------ tables

function lab_table_header(cols::Vector{String}, widths::Vector{Int})
    line0 = "┌" * join(("─"^w for w in widths), "┬") * "┐"
    line1 = "├" * join(("─"^w for w in widths), "┼") * "┤"
    line2 = "└" * join(("─"^w for w in widths), "┴") * "┘"
    hdr = "│" * join((rpad(c, w) for (c, w) in zip(cols, widths)), "│") * "│"
    println(cc(line0, C_GRY)); println(cc(hdr, C_B)); println(cc(line1, C_GRY))
    return (top = line0, mid = line1, bot = line2)
end

lab_table_row(cells::Vector{String}, widths::Vector{Int}) =
    println("│" * join((rpad(c, w) for (c, w) in zip(cells, widths)), "│") * "│")

lab_table_footer(f) = println(cc(f.bot, C_GRY))

# =============================================================================
#  ONE-LINE REALTIME PROGRESS BAR
#  [label] ▕███████████░░░░░░░░░░▏ 43.2% · 12/28 · ⏱ 00:01:23 · ETA 00:01:49
#  Rendered with \r on a single terminal line; throttled; ETA from pace.
# =============================================================================

mutable struct PBar
    label   :: String
    sub     :: String
    frac    :: Float64        # 0..1
    t0      :: Float64
    width   :: Int
    last    :: Float64        # last render time
    active  :: Bool
    finished:: Bool
    spin    :: Int
end

PBar(width::Int = 26) = PBar("", "", 0.0, time(), width, 0.0, false, false, 0)

const SPIN_CHARS = ('⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏')

function pbar_start!(p::PBar, label::AbstractString; sub::AbstractString = "")
    p.label = String(label); p.sub = String(sub)
    p.frac = 0.0; p.t0 = time(); p.last = 0.0
    p.active = true; p.finished = false
    pbar_render(p; force = true)
    nothing
end

function pbar_set!(p::PBar, frac::Real; sub::AbstractString = p.sub, force::Bool = false)
    p.frac = clamp(Float64(frac), 0.0, 1.0)
    p.sub = String(sub)
    pbar_render(p; force = force)
    nothing
end

# asymptotic "crawl" for long un-hookable phases (e.g. LAPACK tridiagonalization):
# frac_local = w * (1 - exp(-t/tau))  — honest estimate, marked with '~'
function pbar_crawl!(p::PBar, units_done::Float64, units_total::Float64, weight::Float64, tau::Float64;
                     sub::AbstractString = p.sub)
    telapsed = time() - p.t0
    local_frac = weight * (1.0 - exp(-telapsed / max(tau, 0.5)))
    pbar_set!(p, (units_done + local_frac) / units_total; sub = sub)
    nothing
end

function pbar_render(p::PBar; force::Bool = false)
    (p.active || force) || return nothing
    now_t = time()
    if !force && (now_t - p.last) < 0.12
        return nothing
    end
    p.last = now_t
    p.spin += 1
    el = now_t - p.t0
    if lab_use_color()
        nel = round(Int, p.frac * p.width)
        bar = "█"^nel * "░"^(p.width - nel)
        eta = p.frac > 0.01 ? el / p.frac - el : NaN
        tail = isnan(eta) ? @sprintf("⏱ %s", fmt_hms(el)) :
               @sprintf("⏱ %s · ETA %s", fmt_hms(el), fmt_hms(eta))
        sub = isempty(p.sub) ? "" : " · " * p.sub
        line = @sprintf("%s ▕%s▏ %5.1f%%%s%s", p.label, bar, 100p.frac, sub, tail)
        line = length(line) > 160 ? line[1:160] : line
        print(stdout, "\r\e[K", line)
        flush(stdout)
    else
        # non-tty: milestone lines every 10%
        milestone = floor(Int, p.frac * 100)
        if force || (milestone % 10 == 0 && milestone > 0)
            println(stdout, @sprintf("[%s] %5.1f%% · %s · %.0fs", p.label, 100p.frac, p.sub, el))
        end
    end
    flush(stdout)
    return nothing
end

function pbar_finish!(p::PBar, msg::AbstractString = "")
    p.finished = true
    el = time() - p.t0
    if lab_use_color()
        bar = "█"^p.width
        print(stdout, "\r\e[K", @sprintf("%s ▕%s▏ 100.0%% · ⏱ %s %s\n",
              p.label, bar, fmt_hms(el), msg))
        flush(stdout)
    else
        println(stdout, @sprintf("[%s] 100.0%% · %.0fs %s", p.label, el, msg))
    end
    p.active = false
    nothing
end

pbar_abort!(p::PBar) = (lab_use_color() && print(stdout, "\r\e[K"); p.active = false; nothing)

# phase clock (fixation of durations for the report)

mutable struct PhaseClock
    name::String
    t0::Float64
end
const PHASES = Ref((PhaseClock[], String[], Float64[]))

function phase_begin!(name::AbstractString)
    push!(PHASES[][1], PhaseClock(String(name), time()))
    nothing
end

function phase_end!(name::AbstractString)
    list = PHASES[][1]
    for i in length(list):-1:1
        if list[i].name == String(name)
            push!(PHASES[][2], String(name))
            push!(PHASES[][3], time() - list[i].t0)
            deleteat!(list, i)
            return nothing
        end
    end
    nothing
end

phases_reset!() = (PHASES[] = (PhaseClock[], String[], Float64[]); nothing)

function phases_print(total_override::Union{Nothing,Float64} = nothing)
    names, secs = PHASES[][2], PHASES[][3]
    isempty(names) && return nothing
    total = total_override === nothing ? sum(secs) : total_override
    println(stdout, cc("  " * t(:timing_summary), C_B))
    for (n, s) in zip(names, secs)
        pct = total > 0 ? 100s / total : 0.0
        @printf(stdout, "    %-34s %10s  %5.1f%%\n", n, fmt_sec(s), pct)
    end
    @printf(stdout, "    %-34s %10s  100.0%%\n", t(:timing_total), fmt_sec(total))
    nothing
end
# =============================================================================
# Statistics of Test 34: unfolding, KS tests, pair correlation R2, distances
# =============================================================================

# ----------------------------------------------------------------- erf (A&S 7.1.26)

function erf_as(x::Float64)
    sgn = x < 0.0 ? -1.0 : 1.0
    x = abs(x)
    t = 1.0 / (1.0 + 0.3275911 * x)
    poly = t * (0.254829592 + t * (-0.284496736 + t * (1.421413741 +
           t * (-1.453152027 + t * 1.061405429))))
    return sgn * (1.0 - poly * exp(-x * x))
end

# GUE Wigner surmise CDF (exact closed form)
gue_cdf(s::Float64) = erf_as(2.0 * s / sqrt(pi)) - (4.0 * s / pi) * exp(-4.0 * s * s / pi)
gue_pdf(s::Float64) = (32.0 / pi^2) * s^2 * exp(-4.0 * s * s / pi)
pois_cdf(s::Float64) = 1.0 - exp(-s)

# Montgomery pair correlation for GUE:  R2(s) = 1 - (sin(pi s)/(pi s))^2
# NOTE: Base.sinc(x) = sin(pi x)/(pi x)  =>  R2(s) = 1 - sinc(s)^2
gue_r2(s::Float64) = 1.0 - Base.sinc(s)^2

# --------------------------------------------------------------- unfolding: zeta

"""
    unfold_zeta(gammas; patch_a = true) -> spacings

Suite-canonical log-density unfolding of Riemann zeros (Riemann-von Mangoldt
smooth counting function N̄(T) = T/2π·log(T/2πe) + 7/8), optionally followed by
the Patch-A local polynomial detrend (degree 4) of the unfolded staircase.
Mean spacing is normalized to exactly 1.
"""
function unfold_zeta(gammas::Vector{Float64}; patch_a::Bool = true)
    n = length(gammas)
    n >= 3 || error("need at least 3 zeros")
    g = sort(gammas)
    nbar = similar(g)
    @inbounds for i in 1:n
        T = g[i]
        nbar[i] = T / (2.0pi) * (log(T / (2.0pi)) - 1.0) + 7.0 / 8.0
    end
    u = nbar .- nbar[1]
    if patch_a && n >= 50
        x = collect(1.0:n)
        # normalize x to [-1,1] for conditioning
        xm = 0.5 * (x[1] + x[n]); xr = 0.5 * (x[n] - x[1])
        xn = (x .- xm) ./ xr
        # least squares fit of degree-4 polynomial to u(x)
        A = [xi^k for xi in xn, k in 0:4]
        coef = A \ u
        trend = A * coef
        u = u .- trend .+ (trend[n] - trend[1]) * (x .- x[1]) ./ (x[n] - x[1])
    end
    s = diff(u)
    s .*= length(s) / sum(s)
    return s
end

# ----------------------------------------------------------------- unfolding: AB

"""
    unfold_levels(E; trim, m) -> spacings

Local-window unfolding of a finite lattice spectrum: raw spacings divided by a
moving-average local mean level spacing (window 2m+1), edge-trimmed, mean = 1.
"""
function unfold_levels(E::Vector{Float64}; trim::Int = 20, m::Int = 25)
    Es = sort(E)
    d = diff(Es)
    n = length(d)
    n > 4m + 8 || error("spectrum too short for local unfolding")
    loc = Vector{Float64}(undef, n)
    csum = cumsum(d)
    @inbounds for k in 1:n
        a = max(1, k - m); b = min(n, k + m)
        loc[k] = (csum[b] - (a > 1 ? csum[a-1] : 0.0)) / (b - a + 1)
    end
    s = d ./ loc
    lo = min(trim + 1, n); hi = max(lo, n - trim)
    s = s[lo:hi]
    s ./= mean(s)
    return s
end

# ------------------------------------------------------------------------- KS

"""
    ks_two(x, y) -> (D, p)

Two-sample Kolmogorov-Smirnov: D statistic and asymptotic p-value.
For N ~ 1e5 p underflows to ~0 — judge by D (v23 guidance).
"""
function ks_two(x::Vector{Float64}, y::Vector{Float64})
    xs = sort(x); ys = sort(y)
    nx, ny = length(xs), length(ys)
    nx > 0 && ny > 0 || return (NaN, NaN)
    i = j = 0
    D = 0.0
    while i < nx || j < ny
        if i == nx
            j += 1
        elseif j == ny
            i += 1
        elseif xs[i+1] < ys[j+1]
            i += 1
        elseif xs[i+1] > ys[j+1]
            j += 1
        else
            i += 1; j += 1
        end
        D = max(D, abs(i / nx - j / ny))
    end
    lam = sqrt(nx * ny / (nx + ny)) * D
    p = 0.0
    for k in 1:100
        term = (isodd(k) ? 1.0 : -1.0) * exp(-2.0 * k^2 * lam^2)
        p += term
        abs(term) < 1e-300 && break
    end
    return (D, clamp(2.0 * p, 0.0, 1.0))
end

function ks_one(s_sorted::Vector{Float64}, F::Function)
    n = length(s_sorted)
    n > 0 || return NaN
    D = 0.0
    @inbounds for i in 1:n
        Fi = F(s_sorted[i])
        D = max(D, Fi - (i - 1) / n, i / n - Fi)
    end
    return D
end

ks_gue(s::Vector{Float64})  = ks_one(sort(s), gue_cdf)
ks_pois(s::Vector{Float64}) = ks_one(sort(s), pois_cdf)

# --------------------------------------------------------------- pair correl.

"""
    pair_correlation(u; smax, nbins, kmax) -> (centers, R2)

Montgomery pair correlation R2(s) of unfolded levels `u`.
Pairs restricted to index gap <= kmax (enough for s <= smax since <s> = 1).
Poisson normalization: expected pairs per point per ds equals ds.
"""
function pair_correlation(u::Vector{Float64}; smax::Float64 = 3.0, nbins::Int = 150, kmax::Int = 40)
    ds = smax / nbins
    cnt = zeros(Float64, nbins)
    M = length(u)
    @inbounds for i in 1:M
        jmax = min(M, i + kmax)
        ui = u[i]
        @inbounds for j in (i+1):jmax
            s = u[j] - ui
            s > smax && break
            b = floor(Int, s / ds) + 1
            if 1 <= b <= nbins
                cnt[b] += 1.0
            end
        end
    end
    centers = [(b - 0.5) * ds for b in 1:nbins]
    return (centers, cnt ./ (M * ds))
end

r2_plateau(centers, R2; lo = 1.0, hi = 2.0) =
    mean(R2[lo .<= centers .<= hi])

r2_band_dev(centers, R2; lo = 0.2, hi = 2.0) =
    mean(abs.(R2[lo .<= centers .<= hi] .- gue_r2.(centers[lo .<= centers .<= hi])))

# ------------------------------------------------------------------ composite

"""
Composite Test 34 verdict (v23-compatible):
  c1: (p > 0.01 || D < 0.10)     — KS compatible (p unreliable at N~1e5)
  c2: d_GUE < d_Pois             — GUE discriminates better than Poisson
  c3: 0.75 <= R2 plateau <= 1.25 — universal plateau near 1
"""
function composite_verdict(D::Float64, p::Float64, dGUE::Float64, dPois::Float64, plateau::Float64)
    c1 = (p > 0.01) || (D < 0.10)
    c2 = dGUE < dPois
    c3 = (0.75 <= plateau <= 1.25)
    pass = c1 && c2 && c3
    return (pass = pass, c1 = c1, c2 = c2, c3 = c3)
end

verdict_symbol(v) = v.pass ? :GUE_LIKE : :DEVIANT

# ------------------------------------------------------------------ bootstrap

function bootstrap_D_ci(s::Vector{Float64}, F::Function; B::Int = 500, seed::Integer = 1)
    rng = lab_rng(seed)
    n = length(s)
    Ds = Vector{Float64}(undef, B)
    for b in 1:B
        idxs = rand(rng, 1:n, n)
        samp = sort!(s[idxs])
        Ds[b] = ks_one(samp, F)
    end
    lo, hi = quantile(Ds, 0.025), quantile(Ds, 0.975)
    return (lo = lo, hi = hi, mean = mean(Ds), samples = Ds)
end

function mad_outliers(Ds::Vector{Float64}; k::Float64 = 3.0)
    med = median(Ds)
    mad = median(abs.(Ds .- med))
    thr = k * 1.4826 * max(mad, 1e-9)
    # with tiny ensembles MAD is degenerate — only flag when n >= 5
    flags = length(Ds) >= 5 ? abs.(Ds .- med) .> thr : falses(length(Ds))
    return (med = med, mad = mad, thr = thr, flags = flags)
end
# =============================================================================
# Zeros file discovery + AB-cloud model + chunked diagonalization
# =============================================================================

# ------------------------------------------------------------- zeros discovery

mutable struct ZerosCandidate
    path      :: String
    count     :: Int
    first     :: Float64
    last      :: Float64
    monotone  :: Float64     # fraction of non-decreasing steps
    score     :: Float64
end

function _parse_line_floats(line::AbstractString)
    h = findfirst('#', line)
    h !== nothing && (line = line[1:h-1])
    line = replace(line, ',' => ' ', ';' => ' ', '\t' => ' ')
    out = Float64[]
    for tok in split(line)
        v = tryparse(Float64, tok)
        v !== nothing && push!(out, v)
    end
    return out
end

"""
    sniff_zeros_file(path) -> Union{Nothing,ZerosCandidate}

Robust detection of Riemann-zero text files. Accepts formats:
one gamma per line, "n gamma", "0.5 gamma", comma/tab separated, "#" comments.
A line may contain an index column; the largest value > 13.0 is taken as gamma
(the lowest Riemann zero has Im = 14.1347).
"""
function sniff_zeros_file(path::AbstractString; maxlines::Int = 2_000_000)
    try
        isfile(path) || return nothing
        filesize(path) == 0 && return nothing
        vals = Float64[]
        nread = 0
        for line in eachline(path)
            nread += 1
            nread > maxlines && break
            vs = _parse_line_floats(line)
            isempty(vs) && continue
            cand = filter(v -> 13.0 < v < 1e10, vs)
            isempty(cand) || push!(vals, maximum(cand))
        end
        length(vals) < 30 && return nothing
        v1 = vals[1]
        (10.0 < v1 < 1e7) || return nothing
        mono = count(i -> vals[i+1] >= vals[i] - 1e-9, 1:length(vals)-1) / (length(vals) - 1)
        mono >= 0.90 || return nothing
        score = mono * min(length(vals), 1e6) / 1e6 + (v1 > 14.0 && v1 < 14.5 ? 0.05 : 0.0)
        return ZerosCandidate(String(path), length(vals), v1, vals[end], mono, score)
    catch
        return nothing
    end
end

function discover_zeros_files(dirs::Vector{String} = unique([LAB_SCRIPT_DIR, pwd()]))
    found = ZerosCandidate[]
    seen = Set{String}()
    for d in dirs
        isdir(d) || continue
        try
            for f in readdir(d; join = true)
                isfile(f) || continue
                okext = any(endswith(lowercase(f), ext) for ext in (".txt", ".dat", ".csv", ".out", ".zeros"))
                okext || continue
                f in seen && continue
                push!(seen, f)
                cand = sniff_zeros_file(f)
                cand !== nothing && push!(found, cand)
            end
            # one level of subdirectories (e.g. zeros/, data/)
            for sub in readdir(d; join = true)
                isdir(sub) || continue
                try
                    for f in readdir(sub; join = true)
                        isfile(f) || continue
                        okext = any(endswith(lowercase(f), ext) for ext in (".txt", ".dat", ".csv", ".out", ".zeros"))
                        okext || continue
                        f in seen && continue
                        push!(seen, f)
                        cand = sniff_zeros_file(f)
                        cand !== nothing && push!(found, cand)
                    end
                catch
                end
            end
        catch
        end
    end
    sort!(found; by = c -> (c.score, c.count), rev = true)
    return found
end

function load_zeros(path::AbstractString, kmax::Int; pbar::Union{Nothing,PBar} = nothing)
    gammas = Float64[]
    open(path, "r") do io
        for line in eachline(io)
            vs = _parse_line_floats(line)
            isempty(vs) && continue
            cand = filter(v -> 13.0 < v < 1e10, vs)
            isempty(cand) || push!(gammas, maximum(cand))
            if pbar !== nothing && length(gammas) % 100_000 == 0
                pbar_set!(pbar, min(0.98, length(gammas) / max(kmax, 1)))
            end
            length(gammas) >= kmax && break
        end
    end
    return gammas
end

# =============================================================================
# GEOMETRY ENGINE — universal closed surfaces for the AB-cloud model
# =============================================================================
# The original lab measured ONE geometry: the flat torus (L x L periodic
# square). This section generalizes the model to a registry of closed surfaces
# while keeping the torus path bit-for-bit identical (geometry = :torus).
#
# A geometry = identification (deck) action on the lattice/graph + AB flux rule:
#
#   :torus   T^2 = R^2/Z^2. Periodic L x L, genus 1. Vortex ring (original).
#   :klein   Klein bottle = T^2 / tau_glide with the free involution
#            tau(x,y) = (x + L/2, L+1-y). Non-orientable (demigenus 2): the
#            deck reflection maps a vortex to an ANTI-vortex (flux is a
#            pseudoscalar), so vortices enter as vortex-antivortex pairs and
#            the net flux vanishes, as it must on a non-orientable surface.
#   :pillow  Pillow orbifold = T^2 / (x ~ -x) (the pi-rotation quotient,
#            free on lattice sites for even L): topologically a sphere with
#            4 order-2 cone points. Vortices are duplicated at their
#            tau-images with the same flux (tau is orientation-preserving).
#   :cubic   Cube sphere: the surface of the cube [-1,1]^3 subdivided L x L
#            per face (6L^2-12L+8 sites, octahedral symmetry). Vortices sit
#            on a ring on the +z face; the gauge is azimuthal around the
#            polar axis (the same atan2 phase formula as on the torus,
#            applied to the equatorial (x, y) projections of the 3D bond
#            endpoints — face plaquettes enclosing a vortex carry 2*pi*q*alpha).
#   :psl27   Klein quartic        g=3,  PSL(2,7),  |G| = 168  = 84(g-1)
#   :psl28   Macbeath surface     g=7,  PSL(2,8),  |G| = 504  = 84(g-1)
#   :psl213  Fricke-Klein         g=14, PSL(2,13), |G| = 1092 = 84(g-1)
#            The three classical Hurwitz surfaces (they attain the Hurwitz
#            automorphism bound 84(g-1) and carry the (2,3,7) triangle-group
#            action). Model: magnetic Cayley graph Cay(G; B, C) of the Hurwitz
#            group G = PSL(2,q) with ord(B) = 3, ord(C) = 7 (C = A*B for a
#            Hurwitz pair (A,B), found by a deterministic search and cached).
#            Bond phases are multiplication-direction gauges: H[g, gB] gets
#            e(+i*phi_B), H[g, gC] gets e(+i*phi_C) — consistent because B and
#            C have odd order, so each undirected bond has a unique {g, gX}
#            representation. With phi_B = 0 and phi_C = 2*pi*q*alpha*Nv/7 the
#            flux through EVERY heptagonal C-face is exactly 2*pi*q*alpha*Nv:
#            the torus vortex-flux knob transplanted to the Hurwitz tiling.
#            Onsite disorder W plays the same seeded role as on the torus.
#
# All builders return a Hermitian ComplexF64 matrix; every downstream stage
# (spectrum_window!, unfolding, KS, R2, verdicts) is geometry-agnostic.
# =============================================================================

struct GeometrySpec
    id        :: Symbol      # :torus :klein :pillow :cubic :psl27 :psl28 :psl213 :psl227
    name      :: String      # display name
    group     :: String      # isometry / symmetry group label
    genus     :: Int         # orientable genus (Klein: demigenus 2)
    orientable:: Bool
    chi       :: Int         # Euler characteristic
    hurwitz   :: Bool        # attains the 84(g-1) Hurwitz bound
    aut_order :: Int         # |Aut| for Hurwitz surfaces, 0 otherwise
    q_field   :: Int         # GF(q) base field for :cayley models
    model     :: Symbol      # :flat | :fold | :sphere | :cayley
end

const GEOMETRY_LIST = [
    GeometrySpec(:torus,  "Torus",          "Z^2 x Z^2 periodic",  1, true,   0, false,    0,  0, :flat),
    GeometrySpec(:klein,  "Klein bottle",   "T^2 / glide tau",     2, false,  0, false,    0,  0, :fold),
    GeometrySpec(:pillow, "Pillow orbifold","T^2 / (x ~ -x)",      0, true,   2, false,    0,  0, :fold),
    GeometrySpec(:cubic,  "Cube sphere",    "octahedral quadmesh", 0, true,   2, false,    0,  0, :sphere),
    GeometrySpec(:psl27,  "Klein quartic",  "PSL(2,7)",            3, true,  -4, true,   168,  7, :cayley),
    GeometrySpec(:psl28,  "Macbeath surf.", "PSL(2,8)",            7, true, -12, true,   504,  8, :cayley),
    GeometrySpec(:psl213, "Fricke-Klein",   "PSL(2,13)",          14, true, -26, true,  1092, 13, :cayley),
    GeometrySpec(:psl227, "Hurwitz-118",    "PSL(2,27)",         118, true, -234, true,  9828, 27, :cayley),
]

const GEOM = Ref(GEOMETRY_LIST[1])
current_geometry() = GEOM[]

geom_by_id(id::Symbol) = begin
    k = findfirst(g -> g.id === id, GEOMETRY_LIST)
    k === nothing && throw(ArgumentError("unknown geometry :$id"))
    GEOMETRY_LIST[k]
end

set_geometry!(id::Symbol) = begin
    GEOM[] = geom_by_id(id)
    LAB.geometry = id
    lab_save_settings()
    GEOM[]
end

# BIG-MATRIX FIX (v1.1): feasibility guard for the auto-scaled geometries.
# 20736 sites = the historical torus ceiling L=144 (20736^2 ComplexF64 ≈ 6.9 GB
# with LAPACK workspace) — every auto-scaled matrix stays within the same
# envelope the torus always had.
const LAB_MAX_SITES = 144 * 144

"""
    geom_L_for_sites(geo, target) -> L

Inverse of the site-count formula: the geometry size parameter L whose
Hamiltonian carries ≈ `target` sites (first L with sites >= target for the
fold, ≈ target for the cube sphere). Used by the BIG-MATRIX autoscale so that
klein/pillow/cubic run on the same site budget as the L x L torus.
"""
function geom_L_for_sites(geo::GeometrySpec, target::Int)
    if geo.model === :sphere
        # 6L^2 - 12L + 8 ≈ target  →  L ≈ sqrt((target - 8)/6 + 1)
        return max(4, ceil(Int, sqrt((target - 8) / 6.0 + 1.0)))
    elseif geo.model === :fold
        # L^2/2 >= target (even L)  →  L = even ceil(sqrt(2*target))
        Lf = ceil(Int, sqrt(2.0 * target))
        Lf += Lf % 2
        # hard feasibility cap: even Ls overshoot the site budget by up to one
        # step — step back down if the rounded-up fold exceeds the envelope
        (Lf * Lf ÷ 2 > LAB_MAX_SITES) && (Lf -= 2)
        return Lf
    end
    return max(8, ceil(Int, sqrt(Float64(target))))
end

"""
Effective lattice parameter for a geometry.

BIG-MATRIX FIX (v1.1) — the historical behaviour silently DEGRADED every
non-torus geometry, so selecting e.g. the cube sphere at L = 96 diagonalized a
12-per-face cube (728 sites) and the Hurwitz groups ignored L altogether —
the "synthetic small run" the big-matrix comparisons were missing:

  :cayley  |G| is FIXED by mathematics (84(g-1) with g = 3/7/14 → 168/504/1092
           sites). No L can change it; the run is real, the size is irreducible
           and is now reported as such instead of being hidden.
  :sphere  WAS clamp(L, 4, 12). With autoscale ON (default) L is re-derived so
           the cube carries ≈ L^2 sites — at the default L = 96 → L = 40 →
           9128 sites, the same big matrix as the 96 x 96 torus (9216).
  :fold    n = L^2/2 — at the same L the Klein bottle / pillow carried HALF the
           torus spectrum. With autoscale ON the fold L is scaled so n ≈ L^2
           (96 → L = 136 → 9248 sites).
  :torus   unchanged (max(L, 8)) — the original model stays bit-for-bit.

With LAB.autoscale = false the historical (degraded) mapping is kept verbatim.
Returns (L_eff, was_adjusted).
"""
function geom_L_eff(geo::GeometrySpec, L::Int)
    if geo.model === :cayley
        return (L, false)                    # |G| is fixed; L is ignored
    elseif geo.model === :sphere
        if LAB.autoscale
            target = min(L * L, LAB_MAX_SITES)
            Le = geom_L_for_sites(geo, target)
            return (Le, Le != L)
        end
        Le = clamp(L, 4, 12)                 # historical small-matrix clamp
        return (Le, Le != L)
    elseif geo.id === :torus
        return (max(L, 8), L < 8)
    else                                     # :fold — needs even L (free action)
        if LAB.autoscale
            target = min(L * L, LAB_MAX_SITES)
            Le = geom_L_for_sites(geo, target)
            return (Le, Le != L)
        end
        Le = max(L + L % 2, 8)
        return (Le, Le != L)
    end
end

geom_nsites(geo::GeometrySpec, L::Int) =
    geo.model === :cayley ? geo.aut_order * cayley_lift_k(geo, L) :
    geo.model === :sphere ? 6L^2 - 12L + 8 :
    geo.model === :fold   ? L * L ÷ 2 :
                            L * L

function geometry_label(geo::GeometrySpec, L::Int)
    Le, _ = geom_L_eff(geo, L)
    n = geom_nsites(geo, Le)
    k = geo.model === :cayley ? cayley_lift_k(geo, L) : 1
    head = geo.model === :cayley ?
           (k > 1 ?
            @sprintf("%s PSL(2,%d) |G|=%d ×%d lift", geo.name, geo.q_field, geo.aut_order, k) :
            @sprintf("%s PSL(2,%d) |G|=%d", geo.name, geo.q_field, geo.aut_order)) :
           geo.model === :sphere ?
           @sprintf("%s L=%d", geo.name, Le) :
           @sprintf("%s %dx%d", geo.name, Le, Le)
    # STRETCH FIX (v1.3): Hurwitz geometries now STRETCH toward the L² budget
    # by voltage lifts — the "L ignored" disclaimer survives only when the
    # stretch is off (autoscale OFF). k = 1 with autoscale ON means |G| is
    # already ≈ L² (psl227 at the default budget) — nothing to disclaim.
    tail = geo.model === :cayley && k == 1 && !LAB.autoscale ? " · " * t(:geo_L_ignored) : ""
    return @sprintf("%s · %d sites · g=%d · χ=%d%s%s", head, n, geo.genus, geo.chi,
                    geo.hurwitz ? " · HURWITZ 84(g-1)=|Aut|" : "",
                    tail)
end

function geom_site_label(geo::GeometrySpec, L::Int)
    geo.model === :cayley || return (
        geo.model === :sphere ? @sprintf("cube L=%d", L) : @sprintf("%dx%d", L, L))
    k = cayley_lift_k(geo, L)
    return k > 1 ? @sprintf("Cayley |G|=%d ×%d", geo.aut_order, k) :
                   @sprintf("Cayley |G|=%d", geo.aut_order)
end

"""
L list for the mode-3 finite-size scaling probe, adapted to the geometry.

BIG-MATRIX FIX (v1.1): the historical fixed lists ([24,32,48] for the fold,
[4,6,8] for the cube) probed toy matrices regardless of the selected size.
The returned values are LAB.L BUDGETS (what the mode-3 loop assigns), chosen
so the realized site counts walk ≈ 25% → 55% → 100% of the selected budget
(torus keeps the historical [48, 64, L] baseline; STRETCH FIX (v1.3): Cayley
groups scale too through the ×7 lift ladder — they skip the probe only with
autoscale OFF, where the matrix stays at the fixed |G|).
"""
function geom_scaling_Ls(geo::GeometrySpec, L::Int)
    geo.model === :cayley && !LAB.autoscale && return Int[]
    geo.id === :torus     && return sort(unique([48, 64, L]))
    if !LAB.autoscale
        # historical behaviour (autscale OFF)
        return geo.model === :sphere ? [4, 6, 8] : sort(unique([24, 32, 48]))
    end
    b1 = max(8, round(Int, 0.50 * L))
    b2 = max(b1 + 1, round(Int, sqrt(0.55) * L))
    return sort(unique([b1, b2, L]))
end

# --------------------------------------------------------------- GF(q) fields
# GF(q) for prime q (7, 13) and GF(8) = GF(2)[x]/(x^3 + x + 1) for PSL(2,8).

struct FieldCtx
    q     :: Int
    gf8   :: Bool
    gf27  :: Bool            # GF(27) = GF(3)[x]/(x^3 + 2x + 1)  (PSL(2,27))
    logt  :: Vector{Int}     # GF(8) only: log table (index = value+1)
    expt  :: Vector{Int}     # GF(8) only: exp table
    tadd  :: Matrix{Int}     # GF(27) only: addition table (elements 0..26)
    tmul  :: Matrix{Int}     # GF(27) only: multiplication table
    tneg  :: Vector{Int}     # GF(27) only: negation table
end

function FieldCtx(q::Int)
    if q == 8
        expt = Vector{Int}(undef, 13)
        logt = fill(-1, 8)
        v = 1
        for k in 0:12
            expt[k+1] = v
            k < 7 && (logt[v+1] = k)
            v <<= 1
            (v & 0b1000) != 0 && (v ⊻= 0b1011)   # reduce by x^3 + x + 1
        end
        return FieldCtx(8, true, false, logt, expt,
                        Matrix{Int}(undef, 0, 0), Matrix{Int}(undef, 0, 0), Int[])
    elseif q == 27
        # GF(27) = GF(3)[x]/(x^3 + 2x + 1); element a <-> a0 + 3a1 + 9a2.
        # x^3 = -2x - 1 ≡ x + 2 (mod 3).  Verified irreducible (no roots in GF(3)).
        c3(a) = (a % 3, (a ÷ 3) % 3, (a ÷ 9) % 3)
        fromc(c0, c1, c2) = c0 + 3c1 + 9c2
        tadd = Matrix{Int}(undef, 27, 27)
        for a in 0:26, b in 0:26
            a0, a1, a2 = c3(a); b0, b1, b2 = c3(b)
            tadd[a+1, b+1] = fromc(mod(a0 + b0, 3), mod(a1 + b1, 3), mod(a2 + b2, 3))
        end
        tmul = fill(0, 27, 27)
        for a in 0:26, b in 0:26
            a0, a1, a2 = c3(a); b0, b1, b2 = c3(b)
            c = zeros(Int, 6)                      # c[k] = coeff of x^(k-1)
            for (i, ai) in enumerate((a0, a1, a2)), (j, bj) in enumerate((b0, b1, b2))
                c[i+j-1] += ai * bj
            end
            # x^(k-1) -> x^(k-3) + 2 x^(k-4):  c[k-2] += t;  c[k-3] += 2t
            for k in 6:-1:4
                t = mod(c[k], 3); c[k] = 0
                t != 0 || continue
                c[k-2] = mod(c[k-2] + t, 3)
                c[k-3] = mod(c[k-3] + 2t, 3)
            end
            tmul[a+1, b+1] = fromc(mod(c[1], 3), mod(c[2], 3), mod(c[3], 3))
        end
        tneg = [begin
                    a0, a1, a2 = c3(a)
                    fromc(mod(-a0, 3), mod(-a1, 3), mod(-a2, 3))
                end for a in 0:26]
        return FieldCtx(27, false, true, Int[], Int[], tadd, tmul, tneg)
    end
    return FieldCtx(q, false, false, Int[], Int[],
                    Matrix{Int}(undef, 0, 0), Matrix{Int}(undef, 0, 0), Int[])
end

@inline f_add(F::FieldCtx, a::Int, b::Int) =
    F.gf8 ? (a ⊻ b) : F.gf27 ? F.tadd[a+1, b+1] : (a + b) % F.q
@inline f_neg(F::FieldCtx, a::Int) =
    F.gf8 ? a : F.gf27 ? F.tneg[a+1] : mod(-a, F.q)
function f_mul(F::FieldCtx, a::Int, b::Int)
    if F.gf8
        (a == 0 || b == 0) && return 0
        return F.expt[F.logt[a+1] + F.logt[b+1] + 1]
    elseif F.gf27
        return F.tmul[a+1, b+1]
    end
    return (a * b) % F.q
end

# ------------------------------------------------------- PSL(2,q) Hurwitz group

struct PSLGroup
    q     :: Int
    F     :: FieldCtx
    elems :: Vector{NTuple{4,Int}}     # canonical reps [[a,b],[c,d]], det = 1 (mod ±I)
    index :: Dict{NTuple{4,Int},Int}
    mulB  :: Vector{Int}               # i -> idx(e_i · B)
    mulC  :: Vector{Int}               # i -> idx(e_i · C),  C = A·B (ord 7)
    genB  :: Int
    genC  :: Int
end

_m2(F::FieldCtx, M::NTuple{4,Int}, N::NTuple{4,Int}) =
    ( f_add(F, f_mul(F, M[1], N[1]), f_mul(F, M[2], N[3])),
      f_add(F, f_mul(F, M[1], N[2]), f_mul(F, M[2], N[4])),
      f_add(F, f_mul(F, M[3], N[1]), f_mul(F, M[4], N[3])),
      f_add(F, f_mul(F, M[3], N[2]), f_mul(F, M[4], N[4])) )

# canonical representative of the ±I class (char-2 fields: -M = M, no-op)
_psl_canon(F::FieldCtx, M::NTuple{4,Int}) =
    F.gf8 ? M :
    (let Mn = (f_neg(F, M[1]), f_neg(F, M[2]), f_neg(F, M[3]), f_neg(F, M[4])); min(M, Mn) end)

_psl_det1(F::FieldCtx, a::Int, b::Int, c::Int, d::Int) =
    F.gf8 ? (f_mul(F, a, d) ⊻ f_mul(F, b, c)) == 1 :
            f_add(F, f_mul(F, a, d), f_neg(F, f_mul(F, b, c))) == 1

"""
Deterministic construction of PSL(2,q) as 2x2 determinant-1 matrices over GF(q)
modulo ±I, plus a deterministic search for a (3,7) generating pair (B, C):
ord(B) = 3, ord(C) = 7, <B, C> = G. Such a pair exists exactly for the Hurwitz
groups PSL(2,q), q = 7, 8, 13, 27 (Macbeath's theorem; q = 27 = -1 mod 7 is the
first BIG Hurwitz group, |G| = 9828) — C = A·B for the classical
Hurwitz pair (A, B) of orders (2, 3). The first pair in canonical element order
is taken, so the Cayley graph (and hence the spectrum at fixed seed) is
reproducible run-to-run.
"""
function build_psl(q::Int)
    q in (7, 8, 13, 27) || throw(ArgumentError("PSL(2,$q) is not a supported Hurwitz group"))
    F = FieldCtx(q)
    rng = 0:(q-1)
    elems = NTuple{4,Int}[]
    index = Dict{NTuple{4,Int},Int}()
    for a in rng, b in rng, c in rng, d in rng
        _psl_det1(F, a, b, c, d) || continue
        M = _psl_canon(F, (a, b, c, d))
        haskey(index, M) && continue
        push!(elems, M)
        index[M] = length(elems)
    end
    n = length(elems)
    nexpect = q == 8 ? q * (q^2 - 1) : q * (q^2 - 1) ÷ 2
    n == nexpect || error("PSL(2,$q): enumerated $n elements, expected $nexpect")

    idm = index[_psl_canon(F, (1, 0, 0, 1))]
    mul(i, j) = index[_psl_canon(F, _m2(F, elems[i], elems[j]))]
    ord(i) = begin
        x = mul(i, i); k = 2
        while x != idm && k <= 4q
            x = mul(x, i); k += 1
        end
        x == idm ? k : -1
    end
    orders = [ord(i) for i in 1:n]
    cand3 = findall(==(3), orders)
    cand7 = findall(==(7), orders)

    genB = genC = 0
    for j in cand7, i in cand3
        # closure test: Cayley graph by right multiplication with {i, j}
        seen = falses(n); seen[idm] = true
        stack = [idm]; cnt = 1
        while !isempty(stack)
            x = pop!(stack)
            for g in (i, j)
                y = mul(x, g)
                if !seen[y]
                    seen[y] = true; cnt += 1; push!(stack, y)
                end
            end
        end
        if cnt == n
            genB = i; genC = j
            break
        end
    end
    genB != 0 || error("PSL(2,$q): (3,7) generating pair not found")

    mulB = [mul(i, genB) for i in 1:n]
    mulC = [mul(i, genC) for i in 1:n]
    return PSLGroup(q, F, elems, index, mulB, mulC, genB, genC)
end

const _PSL_CACHE = Dict{Int,PSLGroup}()
get_psl(q::Int) = get!(() -> build_psl(q), _PSL_CACHE, q)

# ---------------------------------------------------------------------------
# HURWITZ STRETCH (v1.3): voltage lifts of the magnetic Cayley graph.
#
#   sites = |G| * k,  k in {1, 7, 14, 21, ...}
#
# Vertices (g, t), g in G, t in Z_k;  B-bond (g,t)--(gB, t+vB),
# C-bond (g,t)--(gC, t+vC). 4-regular, locally identical to the base Cayley
# graph. k is a multiple of 7 and vC = k/7, so 7*vC = k = 0 (mod k): every
# lifted C-orbit closes into an honest heptagon carrying exactly the vortex
# flux 2*pi*q*alpha*Nv — the model's flux knob is preserved bit-for-bit.
# The zero-flux B-triangles (phiB = 0) open into 3k-cycles: no physics lost.
# Connectivity: the lift is the Cayley graph of Z_k x G generated by
# (vB, B), (vC, C); vB is a unit of Z_k picked by a seeded deterministic
# search and the lift is verified connected by an explicit BFS.
# ---------------------------------------------------------------------------

const _VOLT_CACHE = Dict{Tuple{Int,Int},Tuple{Int,Int}}()

"""
    cayley_lift_k(geo, L) -> k

Stretch factor of the Hurwitz Cayley geometry: the multiple of 7 whose site
count |G|*k lands closest to the L² site budget (same envelope as the torus,
LAB_MAX_SITES; ties resolve to the bigger k). autoscale OFF — or any
non-cayley geometry — returns k = 1: the historical fixed-|G| matrix,
bit-for-bit.
"""
function cayley_lift_k(geo::GeometrySpec, L::Int)
    geo.model === :cayley || return 1
    LAB.autoscale || return 1
    budget = min(max(L, 1) * L, LAB_MAX_SITES)
    k0 = max(1, 7 * round(Int, budget / (7.0 * geo.aut_order)))
    cand = unique!(filter!(x -> x >= 1, [1, k0 - 7, k0, k0 + 7, k0 + 14]))
    cand = filter!(x -> geo.aut_order * x <= LAB_MAX_SITES, cand)
    isempty(cand) && return 1
    best = cand[1]
    bestd = abs(geo.aut_order * best - budget)
    for x in cand[2:end]
        d = abs(geo.aut_order * x - budget)
        if d < bestd || (d == bestd && x > best)
            best, bestd = x, d
        end
    end
    return best
end

"""
    cayley_lift_connected(G, k, vB, vC) -> Bool

BFS over the lifted graph. The four neighbours of (g, t) are
(gB, t+vB), (gB², t-vB), (gC, t+vC), (gC⁻¹, t-vC) — each base bond
{(g,t),(gB,t+vB)} is undirected and (g,t) is the second endpoint of the bond
started at (gB², t-vB). n <= 20736 sites, degree 4 — microseconds.
"""
function cayley_lift_connected(G::PSLGroup, k::Int, vB::Int, vC::Int)
    nG = length(G.elems)
    n = nG * k
    mulB2 = [G.mulB[G.mulB[g]] for g in 1:nG]        # g·B²
    mulC6 = let f = G.mulC                            # g·C⁶ = g·C⁻¹
        x = collect(1:nG)
        for _ in 1:6
            x = f[x]
        end
        x
    end
    seen = falses(n)
    stk = [1]; seen[1] = true; cnt = 1
    while !isempty(stk)
        x = pop!(stk)
        g = (x - 1) ÷ k + 1
        t = (x - 1) % k
        for (jg, dv) in ((G.mulB[g], vB), (mulB2[g], -vB),
                         (G.mulC[g], vC), (mulC6[g], -vC))
            y = (jg - 1) * k + mod(t + dv, k) + 1
            seen[y] || (seen[y] = true; cnt += 1; push!(stk, y))
        end
    end
    return cnt == n
end

"""
    cayley_voltages(G, k) -> (vB, vC)

Deterministic voltage selection (seeded by (q, k), cached): vC = k/7 closes
every lifted C-heptagon; vB is a unit of Z_k whose lift is verified connected
by BFS (100 seeded draws, then an exhaustive scan). k = 1 returns (0, 0) —
the exact base graph.
"""
function cayley_voltages(G::PSLGroup, k::Int)
    k <= 1 && return (0, 0)
    mod(k, 7) == 0 || error("cayley lift: k must be a multiple of 7 (got $k)")
    key = (G.q, k)
    haskey(_VOLT_CACHE, key) && return _VOLT_CACHE[key]
    vC = k ÷ 7
    rng = lab_rng(0x5717c4e4 ⊻ (UInt64(G.q) * 0x9e3779b97f4a7c15) ⊻
                  (UInt64(k) * 0xbf58476d1ce4e5b9))
    for _ in 1:100
        vB = rand(rng, 0:(k-1))
        gcd(vB, k) == 1 || continue
        cayley_lift_connected(G, k, vB, vC) || continue
        _VOLT_CACHE[key] = (vB, vC)
        return (vB, vC)
    end
    for vB in 1:(k-1)                                # exhaustive fallback
        if gcd(vB, k) == 1 && cayley_lift_connected(G, k, vB, vC)
            _VOLT_CACHE[key] = (vB, vC)
            return (vB, vC)
        end
    end
    error("cayley lift k=$k: no connected voltage assignment found")
end

# --------------------------------------------------- geometry Hamiltonians

"""
Folded (quotient) torus Hamiltonian for :klein and :pillow.

Construction: build the flat torus Hamiltonian with the tau-closed (and for
the Klein bottle sign-flipped) vortex set, then project onto the tau-even
sector — H[i, j] accumulates exp(+i*phi) over EVERY preimage bond of the
folded bond {i, j}. For the Klein bottle tau is orientation-reversing, so
tau-images of vortices carry the OPPOSITE flux (vortex-antivortex pairs —
the net flux on a non-orientable surface must vanish); for the pillow tau is
the orientation-preserving pi-rotation and images keep the flux.
"""
function build_hamiltonian_fold(geo::GeometrySpec, L::Int, Nv::Int,
                                alpha::Float64, q::Float64, W::Float64, seed::Integer)
    L2 = L ÷ 2
    istklein = geo.id === :klein
    tau = istklein ?
          ((x, y) -> (mod1(x + L2, L), mod1(L + 1 - y, L))) :
          ((x, y) -> (L + 1 - x, L + 1 - y))
    # canonical representative index of every torus site (free involution)
    rep = fill(0, L, L)
    n = 0
    for y in 1:L, x in 1:L
        rep[x, y] != 0 && continue
        n += 1
        rep[x, y] = n
        tx, ty = tau(x, y)
        rep[tx, ty] = n
    end
    n == L * L ÷ 2 || error("fold: site count mismatch ($n)")
    H = zeros(ComplexF64, n, n)
    rng = lab_rng(seed)
    @inbounds for i in 1:n
        H[i, i] = ComplexF64((rand(rng) - 0.5) * W, 0.0)
    end
    Nv == 0 && return H
    # tau-closed signed vortex set (continuous coordinates, site centers at i-0.5)
    wrapL(v) = (m = mod(v, L)) == 0 ? Float64(L) : Float64(m)
    vorts = Tuple{Float64,Float64,Float64}[]
    for (vx, vy) in vortex_positions(L, Nv)
        push!(vorts, (vx, vy, 1.0))
        if istklein
            push!(vorts, (wrapL(vx + L2), Float64(L - vy), -1.0))   # anti-vortex image
        else
            push!(vorts, (Float64(L - vx), Float64(L - vy), 1.0))   # duplicated vortex
        end
    end
    # sum over ALL torus preimage bonds (each folded bond gets both copies)
    @inbounds for y in 1:L, x in 1:L
        i = rep[x, y]
        ax = x - 0.5; ay = y - 0.5
        for (dx, dy) in ((1.0, 0.0), (0.0, 1.0))
            bx = ax + dx; by = ay + dy
            ph = 0.0
            for (vx, vy, s) in vorts
                dax = ax - vx; day = ay - vy
                dbx = bx - vx; dby = by - vy
                dth = _wrap_pi(atan(dby, dbx) - atan(day, dax))
                ph += s * q * alpha * dth
            end
            j = rep[mod1(x + round(Int, dx), L), mod1(y + round(Int, dy), L)]
            H[i, j] += exp(ComplexF64(0.0, ph))
            H[j, i] += exp(ComplexF64(0.0, -ph))
        end
    end
    return H
end

"""
Cube sphere: surface of the cube [-1,1]^3 subdivided L x L per face.
Sites = surface grid crossings (integer coords -m, -m+2, ..., m with m = L-1,
exactly one |coord| = m), n = 6L^2-12L+8; bonds = single-coordinate +-2 steps
(degree 4, degree 3 at the 8 cube corners; the graph is exactly the quad mesh:
V - E + F = 6L^2-12L+8 - (2V-4) + 6(L-1)^2 = 2). Vortices: Nv points evenly on
a ring on the +z face (z = m); gauge = azimuthal around the polar axis, i.e.
the torus atan2 phase formula applied to the equatorial (x, y) projections of
the 3D bond endpoints — plaquettes of the +z face enclosing a vortex carry
exactly 2*pi*q*alpha, all other plaquettes stay (nearly) flux-free.
"""
function build_hamiltonian_cubic(L::Int, Nv::Int, alpha::Float64, q::Float64,
                                 W::Float64, seed::Integer)
    m = L - 1
    coords = collect(-m:2:m)
    site = Dict{NTuple{3,Int},Int}()
    pts = NTuple{3,Int}[]
    for Z in coords, Y in coords, X in coords
        max(abs(X), abs(Y), abs(Z)) == m || continue
        push!(pts, (X, Y, Z))
        site[(X, Y, Z)] = length(pts)
    end
    n = length(pts)
    n == 6L^2 - 12L + 8 || error("cubic: site count mismatch ($n)")
    H = zeros(ComplexF64, n, n)
    rng = lab_rng(seed)
    @inbounds for i in 1:n
        H[i, i] = ComplexF64((rand(rng) - 0.5) * W, 0.0)
    end
    Nv == 0 && return H
    # vortices: ring on the +z face, radius m/2+1/2 (off the grid points),
    # same ring convention as the torus vortex_positions
    vorts = NTuple{2,Float64}[]
    if Nv > 0
        R = m / 2.0 + 0.5
        for k in 0:(Nv-1)
            th = 2.0pi * k / Nv + pi / Nv
            push!(vorts, (R * cos(th), R * sin(th)))
        end
    end
    @inbounds for i in 1:n
        X, Y, Z = pts[i]
        for d in ((2, 0, 0), (0, 2, 0), (0, 0, 2))     # +directions only: each bond once
            Q = (X + d[1], Y + d[2], Z + d[3])
            (abs(Q[1]) <= m && abs(Q[2]) <= m && abs(Q[3]) <= m) || continue
            haskey(site, Q) || continue
            j = site[Q]
            ph = 0.0
            for (vx, vy) in vorts
                dax = X - vx; day = Y - vy
                dbx = Q[1] - vx; dby = Q[2] - vy
                dth = _wrap_pi(atan(dby, dbx) - atan(day, dax))
                ph += q * alpha * dth
            end
            H[i, j] += exp(ComplexF64(0.0, ph))
            H[j, i] += exp(ComplexF64(0.0, -ph))
        end
    end
    return H
end

"""
Magnetic Cayley-graph Hamiltonian of a Hurwitz surface (PSL(2,q)):
sites = group elements; bonds = right multiplication by the (3,7) Hurwitz
generators B and C (4-regular graph). Gauge: H[g, gX] = e(+i*phi_X) in the
multiplication direction (well-defined because ord(B), ord(C) are odd), so
every B-triangle carries flux 3*phi_B and every C-heptagon carries
7*phi_C = 2*pi*q*alpha*Nv — exactly the torus vortex flux, uniformly over the
(2,3,7) faces. Onsite disorder W as on the torus (seed-driven).

HURWITZ STRETCH (v1.3): k > 1 builds the Z_k voltage lift (cayley_lift_k):
|G|*k sites, same local (2,3,7) structure, same heptagon flux knob, verified
connected. k = 1 is the historical base graph, bit-for-bit (vB = vC = 0).
"""
function build_hamiltonian_cayley_lift(G::PSLGroup, k::Int, Nv::Int, alpha::Float64,
                                       q::Float64, W::Float64, seed::Integer)
    nG = length(G.elems)
    n = nG * k
    H = zeros(ComplexF64, n, n)
    rng = lab_rng(seed)
    @inbounds for i in 1:n
        H[i, i] = ComplexF64((rand(rng) - 0.5) * W, 0.0)
    end
    vB, vC = cayley_voltages(G, k)
    phiB = 0.0                                 # clean B-direction (zero flux)
    phiC = 2.0pi * q * alpha * Nv / 7.0        # flux 2*pi*q*alpha*Nv per heptagon
    @inbounds for g in 1:nG, t in 0:(k-1)
        i  = (g - 1) * k + t + 1
        jB = (G.mulB[g] - 1) * k + mod(t + vB, k) + 1
        jC = (G.mulC[g] - 1) * k + mod(t + vC, k) + 1
        H[i, jB] += exp(ComplexF64(0.0, phiB))
        H[jB, i] += exp(ComplexF64(0.0, -phiB))
        H[i, jC] += exp(ComplexF64(0.0, phiC))
        H[jC, i] += exp(ComplexF64(0.0, -phiC))
    end
    return H
end

# k = 1 wrapper: the exact historical (v1.2) base-graph constructor
build_hamiltonian_cayley(G::PSLGroup, Nv::Int, alpha::Float64,
                         q::Float64, W::Float64, seed::Integer) =
    build_hamiltonian_cayley_lift(G, 1, Nv, alpha, q, W, seed)

"""
Geometry dispatcher. The torus branch calls the ORIGINAL build_hamiltonian —
the historical model and its results are untouched.
"""
function build_hamiltonian_geo(geo::GeometrySpec, L::Int, Nv::Int, alpha::Float64,
                               q::Float64, W::Float64, seed::Integer)
    geo.model === :flat   && return build_hamiltonian(L, Nv, alpha, q, W, seed)
    geo.model === :fold   && return build_hamiltonian_fold(geo, L, Nv, alpha, q, W, seed)
    geo.model === :sphere && return build_hamiltonian_cubic(L, Nv, alpha, q, W, seed)
    geo.model === :cayley && return build_hamiltonian_cayley_lift(get_psl(geo.q_field),
                                                                  cayley_lift_k(geo, L),
                                                                  Nv, alpha, q, W, seed)
    error("unknown geometry model $(geo.model)")
end

"""
Flux through the C-heptagon face-cycle starting at the identity element:
sum of bond phases along (e,0) -> (eC, vC) -> ... -> (eC⁷, 7vC = 0).
Gauge-invariant; must equal 2*pi*q*alpha*Nv (mod 2*pi) for the magnetic
Cayley model at any stretch k (default k = 1: the historical base graph).
"""
function psl_heptagon_flux(G::PSLGroup, H::Matrix{ComplexF64}, k::Int = 1)
    vB, vC = cayley_voltages(G, k)
    gid = G.index[_psl_canon(G.F, (1, 0, 0, 1))]
    g, t = gid, 0
    acc = 0.0
    for _ in 1:7
        i = (g - 1) * k + t + 1
        g2 = G.mulC[g]; t2 = mod(t + vC, k)
        j = (g2 - 1) * k + t2 + 1
        acc += angle(H[i, j])
        g, t = g2, t2
    end
    (g == gid && t == 0) || error("C-orbit of identity is not a lifted 7-cycle")
    return acc
end

# ------------------------------------------------------------------- the model

"""
Vortex positions: evenly placed on a ring of radius L/4 around the lattice
center, half-integer offset to break residual lattice symmetries.
"""
function vortex_positions(L::Int, Nv::Int)
    Nv <= 0 && return Tuple{Float64,Float64}[]
    c = (L + 0.5) / 2
    R = L / 4
    return Tuple{Float64,Float64}[
        (c + R * cos(2pi * k / Nv + pi / Nv), c + R * sin(2pi * k / Nv + pi / Nv))
        for k in 0:(Nv-1)
    ]
end

@inline _mimg(d::Float64, L::Int) = d - L * round(d / L)

@inline _wrap_pi(th::Float64) = mod(th + pi, 2pi) - pi

"""
    build_hamiltonian(L, Nv, alpha, q, W, seed) -> Matrix{ComplexF64}

LxL tight-binding Hamiltonian on a torus with Peierls phases from Nv
Aharonov-Bohm vortices (flux alpha each, charge q), plus onsite disorder
uniform in [-W/2, W/2]. Plaquette flux through the cell enclosing a vortex is
exactly 2*pi*q*alpha.

BUGFIX (full-determinization bug #1): the AB phase per bond must be computed
from the TRUE (covering-space) offsets between the bond endpoints and the
vortex. The previous implementation applied minimum-image wrapping to those
offsets, which moved each vortex's flux onto remote "image" branch-cut cells
(at torus distance L/2). For the default Nv = 2 ring the vortices are exactly
L/2 apart, their image branch cuts coincided and cancelled ALL plaquette
flux: the spectrum became a pure gauge — bit-for-bit identical for any
alpha and q (verified: max|dE| ~ 1e-14 for alpha 0.5 vs 0.9). Without the
minimum-image wrapping each vortex keeps its own 2*pi*q*alpha flux in the
cell that contains it, and the spectrum responds to alpha/q for every Nv.
"""
function build_hamiltonian(L::Int, Nv::Int, alpha::Float64, q::Float64, W::Float64, seed::Integer)
    n = L * L
    H = zeros(ComplexF64, n, n)
    rng = lab_rng(seed)
    @inbounds for i in 1:n
        H[i, i] = ComplexF64((rand(rng) - 0.5) * W, 0.0)
    end
    Nv == 0 && return H
    vorts = vortex_positions(L, Nv)
    idx(x, y) = (y - 1) * L + x
    @inbounds for y in 1:L, x in 1:L
        i = idx(x, y)
        ax = x - 0.5; ay = y - 0.5
        for (dx, dy) in ((1.0, 0.0), (0.0, 1.0))
            bx = ax + dx; by = ay + dy
            ph = 0.0
            for (vx, vy) in vorts
                # covering-space (true) offsets: NO minimum-image wrapping here
                dax = ax - vx; day = ay - vy
                dbx = bx - vx; dby = by - vy
                dth = _wrap_pi(atan(dby, dbx) - atan(day, dax))
                ph += q * alpha * dth
            end
            j = idx(mod1(x + round(Int, dx), L), mod1(y + round(Int, dy), L))
            H[i, j] += exp(ComplexF64(0.0, ph))
            H[j, i] += exp(ComplexF64(0.0, -ph))
        end
    end
    return H
end

hetrd_time_est(n::Int) = 1.2e-9 * n^3 / max(1, Threads.nthreads())

"""
    spectrum_window!(H, ilo, ihi; nchunks, pbar, units_done, units_total, weight)

Dense Hermitian diagonalization with realtime progress:
  stage 1: LAPACK hetrd! tridiagonalization (progress crawled with honest
           time-based estimate, marked '~'),
  stage 2: eigenvalues ilo..ihi via LAPACK stebz! in `nchunks` chunks
           (true progress per chunk).
Destroys H. Returns eigenvalues ilo..ihi (ascending).
"""
function spectrum_window!(H::Matrix{ComplexF64}, ilo::Int, ihi::Int;
                          nchunks::Int = 10,
                          pbar::Union{Nothing,PBar} = nothing,
                          units_done::Float64 = 0.0,
                          units_total::Float64 = 1.0,
                          weight_tri::Float64 = 0.55,
                          weight_eig::Float64 = 0.40,
                          phase::String = "diag")
    n = size(H, 1)
    1 <= ilo <= ihi <= n || throw(ArgumentError("bad window"))
    t0 = time()
    # ---- stage 1: tridiagonalize
    d = Vector{Float64}(undef, 0); e = Vector{Float64}(undef, 0)
    if pbar !== nothing && Threads.nthreads() > 1
        tsk = Threads.@spawn LAPACK.hetrd!('L', H)
        tau = max(hetrd_time_est(n) / 3.0, 1.0)
        while !istaskdone(tsk)
            pbar_crawl!(pbar, units_done, units_total, weight_tri, tau;
                        sub = @sprintf("%s: tridiag ~%s n=%d", phase, fmt_hms(time() - t0), n))
            sleep(0.2)
        end
        _, _, dd, ee = fetch(tsk)
        d, e = dd, ee
    else
        _, _, dd, ee = LAPACK.hetrd!('L', H)
        d, e = dd, ee
        pbar !== nothing && pbar_set!(pbar, (units_done + weight_tri) / units_total; sub = "$phase: tridiag done")
    end
    # ---- stage 2: eigenvalues by index window, chunked
    nchunks = max(1, min(nchunks, ihi - ilo + 1))
    edges = [round(Int, ilo + (ihi - ilo) * c / nchunks) for c in 0:nchunks]
    evals = Vector{Float64}(undef, ihi - ilo + 1)
    pos = 0
    for ci in 1:nchunks
        a = edges[ci] + (ci == 1 ? 0 : 1)
        b = edges[ci+1]
        b >= a || continue
        w = LAPACK.stebz!('I', 'B', 0.0, 0.0, a, b, -1.0, d, e)[1]
        copyto!(evals, pos + 1, w, 1, length(w))
        pos += length(w)
        pbar !== nothing && pbar_set!(pbar,
            (units_done + weight_tri + weight_eig * ci / nchunks) / units_total;
            sub = @sprintf("%s: eigen %d/%d chunks", phase, ci, nchunks))
    end
    pos == length(evals) || error("eigen chunking mismatch: $pos / $(length(evals))")
    return evals
end

# ------------------------------------------------------------- pipeline pieces

struct ABResult
    E      :: Vector{Float64}   # central-window eigenvalues
    s      :: Vector{Float64}   # unfolded spacings
    t_build:: Float64
    t_diag :: Float64
end

function ab_realization(seed::Integer, pbar::Union{Nothing,PBar},
                        units_done::Float64, units_total::Float64;
                        phase::String = "rep")
    geo = GEOM[]
    L, _ = geom_L_eff(geo, LAB.L)
    # weights inside one realization: build .06, tri .60, eig .28, unfold .06
    t0 = time()
    H = build_hamiltonian_geo(geo, L, LAB.Nv, LAB.alpha, LAB.q, LAB.W, seed)
    n = size(H, 1)
    pbar !== nothing && pbar_set!(pbar, (units_done + 0.06) / units_total;
                                  sub = @sprintf("%s: H built %s (%d sites)", phase,
                                                 geom_site_label(geo, L), n))
    ilo = max(2, floor(Int, n * (1 - LAB.window_frac) / 2))
    ihi = min(n - 1, ceil(Int, n * (1 + LAB.window_frac) / 2))
    E = spectrum_window!(H, ilo, ihi;
                         nchunks = LAB.nchunks, pbar = pbar,
                         units_done = units_done + 0.06, units_total = units_total,
                         weight_tri = 0.60, weight_eig = 0.28, phase = phase)
    t1 = time()
    # adaptive unfolding for small spectra (Hurwitz groups, cube sphere):
    # for the torus L >= 32 the window is >= 512 levels and these reduce to
    # the historical trim = 20, m = 25 — the torus baseline is unchanged.
    nwin = ihi - ilo + 1
    trim_eff = min(20, max(3, nwin ÷ 8))
    m_eff    = min(25, max(5, nwin ÷ 12))
    s = unfold_levels(E; trim = trim_eff, m = m_eff)
    t2 = time()
    pbar !== nothing && pbar_set!(pbar, (units_done + 1.0) / units_total;
                                  sub = "$phase: unfolded $(length(s)) spacings")
    return ABResult(E, s, t1 - t0, t2 - t1), seed
end
# =============================================================================
# Built-in PNG plot engine (zero dependencies) — ABPlot-style 1600x1000 charts
#   * 5x7 bitmap font (ASCII; plot labels in English by design)
#   * 2x supersampling antialiasing
#   * PNG writer: standard CRC-32 + zlib (libz via ccall, stored-block fallback)
# =============================================================================

# ------------------------------------------------------------------ 5x7 font

const _FONT = Dict{Char,NTuple{7,UInt8}}()

function _fontdef!(ch::Char, rows::AbstractString)
    parts = split(rows)
    length(parts) == 7 || error("font glyph $ch needs 7 rows")
    _FONT[ch] = ntuple(i -> parse(UInt8, parts[i]; base = 2), 7)
    nothing
end

function _font_init!()
    isempty(_FONT) || return nothing
    G = _fontdef!
    G('A', "01110 10001 10001 11111 10001 10001 10001")
    G('B', "11110 10001 10001 11110 10001 10001 11110")
    G('C', "01110 10001 10000 10000 10000 10001 01110")
    G('D', "11110 10001 10001 10001 10001 10001 11110")
    G('E', "11111 10000 10000 11110 10000 10000 11111")
    G('F', "11111 10000 10000 11110 10000 10000 10000")
    G('G', "01110 10001 10000 10111 10001 10001 01111")
    G('H', "10001 10001 10001 11111 10001 10001 10001")
    G('I', "01110 00100 00100 00100 00100 00100 01110")
    G('J', "00111 00010 00010 00010 00010 10010 01100")
    G('K', "10001 10010 10100 11000 10100 10010 10001")
    G('L', "10000 10000 10000 10000 10000 10000 11111")
    G('M', "10001 11011 10101 10101 10001 10001 10001")
    G('N', "10001 11001 10101 10011 10001 10001 10001")
    G('O', "01110 10001 10001 10001 10001 10001 01110")
    G('P', "11110 10001 10001 11110 10000 10000 10000")
    G('Q', "01110 10001 10001 10001 10101 10010 01101")
    G('R', "11110 10001 10001 11110 10100 10010 10001")
    G('S', "01111 10000 10000 01110 00001 00001 11110")
    G('T', "11111 00100 00100 00100 00100 00100 00100")
    G('U', "10001 10001 10001 10001 10001 10001 01110")
    G('V', "10001 10001 10001 10001 01010 01010 00100")
    G('W', "10001 10001 10001 10101 10101 11011 10001")
    G('X', "10001 10001 01010 00100 01010 10001 10001")
    G('Y', "10001 10001 01010 00100 00100 00100 00100")
    G('Z', "11111 00001 00010 00100 01000 10000 11111")
    G('0', "01110 10001 10011 10101 11001 10001 01110")
    G('1', "00100 01100 00100 00100 00100 00100 01110")
    G('2', "01110 10001 00001 00010 00100 01000 11111")
    G('3', "11111 00010 00100 00010 00001 10001 01110")
    G('4', "00010 00110 01010 10010 11111 00010 00010")
    G('5', "11111 10000 10000 11110 00001 00001 11110")
    G('6', "00110 01000 10000 11110 10001 10001 01110")
    G('7', "11111 00001 00010 00100 01000 01000 01000")
    G('8', "01110 10001 10001 01110 10001 10001 01110")
    G('9', "01110 10001 10001 01111 00001 00010 01100")
    G(' ', "00000 00000 00000 00000 00000 00000 00000")
    G('.', "00000 00000 00000 00000 00000 01100 01100")
    G(',', "00000 00000 00000 00000 00110 00110 01100")
    G(':', "00000 01100 01100 00000 01100 01100 00000")
    G(';', "00000 01100 01100 00000 01100 01100 00110")
    G('-', "00000 00000 00000 11111 00000 00000 00000")
    G('_', "00000 00000 00000 00000 00000 00000 11111")
    G('+', "00000 00100 00100 11111 00100 00100 00000")
    G('/', "00001 00010 00010 00100 01000 01000 10000")
    G('(', "00010 00100 01000 01000 01000 00100 00010")
    G(')', "01000 00100 00010 00010 00010 00100 01000")
    G('[', "01110 01000 01000 01000 01000 01000 01110")
    G(']', "01110 00010 00010 00010 00010 00010 01110")
    G('=', "00000 00000 11111 00000 11111 00000 00000")
    G('<', "00010 00100 01000 10000 01000 00100 00010")
    G('>', "01000 00100 00010 00001 00010 00100 01000")
    G('%', "11001 11010 00010 00100 01000 01011 10011")
    G('!', "00100 00100 00100 00100 00100 00000 00100")
    G('?', "01110 10001 00001 00110 00100 00000 00100")
    G('\'', "00100 00100 01000 00000 00000 00000 00000")
    G('"', "01010 01010 00000 00000 00000 00000 00000")
    G('*', "00000 00100 10101 01110 10101 00100 00000")
    G('|', "00100 00100 00100 00100 00100 00100 00100")
    G('#', "01010 11111 01010 01010 01010 11111 01010")
    G('&', "01100 10010 10100 01000 10101 10010 01101")
    G('@', "01110 10001 10111 10101 10111 10000 01110")
    G('^', "00100 01010 10001 00000 00000 00000 00000")
    G('~', "00000 00000 11001 10110 00000 00000 00000")
    G('$', "00100 01111 10100 01110 00101 11110 00100")
    G('·', "00000 00000 00000 01100 01100 00000 00000")
    nothing
end

# ------------------------------------------------------------------- canvas

const RGBA_BLACK = (0, 0, 0)

struct Canvas
    w   :: Int          # final width
    h   :: Int          # final height
    ss  :: Int          # supersampling factor
    buf :: Array{UInt8, 3}   # (3, w*ss, h*ss) RGB
end

function Canvas(w::Int, h::Int; ss::Int = 2, bg::Tuple{Int,Int,Int} = (250, 250, 250))
    _font_init!()
    buf = Array{UInt8,3}(undef, 3, w * ss, h * ss)
    for c in 1:3
        fill!(view(buf, c, :, :), clamp(bg[c], 0, 255) % UInt8)
    end
    return Canvas(w, h, ss, buf)
end

@inline function _px!(c::Canvas, X::Int, Y::Int, col::Tuple{Int,Int,Int}, alpha::Float64 = 1.0)
    W = c.w * c.ss; H = c.h * c.ss
    (1 <= X <= W && 1 <= Y <= H) || return nothing
    a = clamp(alpha, 0.0, 1.0)
    @inbounds for ch in 1:3
        old = c.buf[ch, X, Y]
        c.buf[ch, X, Y] = round(UInt8, old * (1 - a) + clamp(col[ch], 0, 255) * a)
    end
    nothing
end

"Draw in FINAL coordinates (floats); supersampling applied internally."
function fill_rect!(c::Canvas, x0::Real, y0::Real, x1::Real, y1::Real,
                    col::Tuple{Int,Int,Int}, alpha::Float64 = 1.0)
    ss = c.ss
    X0 = clamp(round(Int, x0 * ss), 1, c.w * ss)
    X1 = clamp(round(Int, x1 * ss), 1, c.w * ss)
    Y0 = clamp(round(Int, y0 * ss), 1, c.h * ss)
    Y1 = clamp(round(Int, y1 * ss), 1, c.h * ss)
    @inbounds for Y in Y0:Y1, X in X0:X1
        _px!(c, X, Y, col, alpha)
    end
    nothing
end

function hline!(c::Canvas, y::Real, x0::Real, x1::Real, col, wpx::Real = 1.0, alpha::Float64 = 1.0)
    ss = c.ss
    half = wpx * ss / 2
    Y0 = round(Int, y * ss - half + 0.5); Y1 = round(Int, y * ss + half - 0.5)
    X0 = round(Int, min(x0, x1) * ss); X1 = round(Int, max(x0, x1) * ss)
    for Y in Y0:Y1, X in X0:X1
        _px!(c, X, Y, col, alpha)
    end
    nothing
end

function vline!(c::Canvas, x::Real, y0::Real, y1::Real, col, wpx::Real = 1.0, alpha::Float64 = 1.0)
    ss = c.ss
    half = wpx * ss / 2
    X0 = round(Int, x * ss - half + 0.5); X1 = round(Int, x * ss + half - 0.5)
    Y0 = round(Int, min(y0, y1) * ss); Y1 = round(Int, max(y0, y1) * ss)
    for Y in Y0:Y1, X in X0:X1
        _px!(c, X, Y, col, alpha)
    end
    nothing
end

function line!(c::Canvas, x0::Real, y0::Real, x1::Real, y1::Real,
               col, wpx::Real = 2.0, alpha::Float64 = 1.0)
    ss = c.ss
    X0 = x0 * ss; Y0 = y0 * ss; X1 = x1 * ss; Y1 = y1 * ss
    dx = X1 - X0; dy = Y1 - Y0
    n = max(1, ceil(Int, max(abs(dx), abs(dy))))
    half = wpx * ss / 2
    for i in 0:n
        t = i / n
        cx = X0 + t * dx; cy = Y0 + t * dy
        for oy in -ceil(half):ceil(half), ox in -ceil(half):ceil(half)
            (ox^2 + oy^2 <= half^2 + 0.5) && _px!(c, round(Int, cx + ox), round(Int, cy + oy), col, alpha)
        end
    end
    nothing
end

function dash_line!(c::Canvas, x0::Real, y0::Real, x1::Real, y1::Real,
                    col, wpx::Real = 1.0, alpha::Float64 = 0.6; dash::Int = 6, gap::Int = 5)
    dx = x1 - x0; dy = y1 - y0
    len = hypot(dx, dy)
    len == 0 && return nothing
    nseg = ceil(Int, len / (dash + gap))
    for k in 0:(nseg-1)
        ta = (k * (dash + gap)) / len
        tb = min(1.0, (k * (dash + gap) + dash) / len)
        line!(c, x0 + ta * dx, y0 + ta * dy, x0 + tb * dx, y0 + tb * dy, col, wpx, alpha)
    end
    nothing
end

function marker!(c::Canvas, x::Real, y::Real, col; r::Real = 4.0, alpha::Float64 = 1.0)
    ss = c.ss
    cx = x * ss; cy = y * ss; rr = r * ss
    for oy in -ceil(rr):ceil(rr), ox in -ceil(rr):ceil(rr)
        (ox^2 + oy^2 <= rr^2) && _px!(c, round(Int, cx + ox), round(Int, cy + oy), col, alpha)
    end
    nothing
end

# ----------------------------------------------------------------- text draw

"Uppercase-only rendering (smallcaps). Returns text width in final px."
function text!(c::Canvas, x::Real, y::Real, s::AbstractString,
               col; scale::Int = 4, align::Symbol = :left, alpha::Float64 = 1.0)
    _font_init!()
    str = uppercase(String(s))
    for (from, to) in (("—", "-"), ("–", "-"), ("’", "'"), ("‘", "'"), ("“", "\""), ("”", "\""), ("×", "X"), ("≈", "~"))
        str = replace(str, from => to)
    end
    ss = c.ss
    gw = 6 * scale * ss          # 5 px glyph + 1 px gap
    total = (length(str) * 6 - 1) * scale
    xoff = align === :center ? -total / 2 : align === :right ? -total : 0.0
    for (ci, chr) in enumerate(str)
        glyph = get(_FONT, chr, _FONT['?'])
        for (ry, bits) in enumerate(glyph), gx in 1:5
            ((bits >> (5 - gx)) & 0x1) == 0x1 || continue
            X0 = round(Int, (x + xoff + (ci - 1) * 6 * scale + (gx - 1) * scale) * ss)
            Y0 = round(Int, (y + (ry - 1) * scale) * ss)
            for oy in 0:(scale*ss-1), ox in 0:(scale*ss-1)
                _px!(c, X0 + ox, Y0 + oy, col, alpha)
            end
        end
    end
    return total
end

text_width(s::AbstractString, scale::Int = 4) = (length(uppercase(String(s))) * 6 - 1) * scale

# ---------------------------------------------------------------- PNG writer

const _CRC_TABLE = let t = Vector{UInt32}(undef, 256)
    for n in 0:255
        c::UInt32 = UInt32(n)
        for _ in 1:8
            c = (c & 0x1 == 0x1) ? (0xEDB88320 ⊻ (c >> 1)) : (c >> 1)
        end
        t[n+1] = c
    end
    t
end

function crc32_png(data::AbstractVector{UInt8}, crc::UInt32 = 0xffffffff)
    for b in data
        crc = _CRC_TABLE[((crc ⊻ UInt32(b)) & 0xff) + 1] ⊻ (crc >> 8)
    end
    return crc ⊻ 0xffffffff
end

"CRC-32 over several buffers (PNG chunk = type + payload), finalized once."
function crc32_parts(parts::AbstractVector{UInt8}...)
    crc = 0xffffffff
    for part in parts
        for b in part
            crc = _CRC_TABLE[((crc ⊻ UInt32(b)) & 0xff) + 1] ⊻ (crc >> 8)
        end
    end
    return crc ⊻ 0xffffffff
end

function adler32_jl(data::AbstractVector{UInt8})
    a::UInt32 = 1; b::UInt32 = 0
    for x in data
        a = (a + UInt32(x)) % 65521
        b = (b + a) % 65521
    end
    return (b << 16) | a
end

function zlib_stored(data::AbstractVector{UInt8})
    io = IOBuffer()
    write(io, 0x78, 0x01)
    i = 1; n = length(data)
    while true
        chunk = min(65535, n - i + 1)
        lastb = (i + chunk - 1 >= n)
        write(io, UInt8(lastb ? 1 : 0))
        write(io, UInt8(chunk & 0xff), UInt8((chunk >> 8) & 0xff))
        write(io, UInt8((~chunk) & 0xff), UInt8(((~chunk) >> 8) & 0xff))
        write(io, view(data, i:(i + chunk - 1)))
        i += chunk
        i > n && break
    end
    ad = adler32_jl(data)
    for sh in (24, 16, 8, 0)
        write(io, UInt8((ad >> sh) & 0xff))
    end
    return take!(io)
end

const _ZLIB_HANDLES = Ref{Ptr{Nothing}}(C_NULL)
const _ZLIB_TRIED = Ref(false)

function _zlib_handle()
    if !_ZLIB_TRIED[]
        _ZLIB_TRIED[] = true
        for name in ("libz.so.1", "libz.so", "libz.dylib", "libz")
            h = try
                dlopen(name)
            catch
                C_NULL
            end
            if h != C_NULL
                _ZLIB_HANDLES[] = h
                break
            end
        end
    end
    return _ZLIB_HANDLES[]
end

function zlib_compress(data::AbstractVector{UInt8})
    h = _zlib_handle()
    if h != C_NULL
        try
            dest = Vector{UInt8}(undef, length(data) + 512)
            destlen = Ref{Culong}(length(dest))
            rc = ccall(dlsym(h, :compress2), Int32,
                       (Ptr{UInt8}, Ptr{Culong}, Ptr{UInt8}, Culong, Int32),
                       dest, destlen, data, length(data), 6)
            rc == 0 || error("compress2 rc=$rc")
            return resize!(dest, Int(destlen[]))
        catch
        end
    end
    return zlib_stored(data)
end

function save_png(c::Canvas, path::AbstractString)
    W = c.w; H = c.h; ss = c.ss
    raw = Vector{UInt8}(undef, H * (1 + W * 3))
    rp = 1
    @inbounds for y in 1:H
        raw[rp] = 0x00            # filter: none
        rp += 1
        for x in 1:W
            r = g = b = 0; s = 0
            for oy in 0:(ss-1), ox in 0:(ss-1)
                X = (x - 1) * ss + ox + 1; Y = (y - 1) * ss + oy + 1
                r += c.buf[1, X, Y]; g += c.buf[2, X, Y]; b += c.buf[3, X, Y]; s += 1
            end
            raw[rp] = round(UInt8, r / s); raw[rp+1] = round(UInt8, g / s); raw[rp+2] = round(UInt8, b / s)
            rp += 3
        end
    end
    idat = zlib_compress(raw)
    ihdr = zeros(UInt8, 13)
    for (i, v) in enumerate((W, H))
        for sh in (24, 16, 8, 0)
            ihdr[(i-1)*4 + (24 - sh) ÷ 8 + 1] = UInt8((v >> sh) & 0xff)
        end
    end
    ihdr[9] = 0x08   # bit depth
    ihdr[10] = 0x02  # color type: truecolor
    open(path, "w") do io
        write(io, 0x89, 'P', 'N', 'G', '\r', '\n', 0x1a, '\n')
        for (tname, payload) in (("IHDR", ihdr), ("IDAT", idat), ("IEND", UInt8[]))
            write(io, hton(UInt32(length(payload))))
            tb = codeunits(tname)
            write(io, tb)
            isempty(payload) || write(io, payload)
            crc = crc32_parts(tb, payload)
            write(io, hton(UInt32(crc)))
        end
    end
    return nothing
end

# ------------------------------------------------------------------- palette

const COL_BG     = (250, 250, 250)
const COL_INK    = (35, 38, 44)
const COL_GRID   = (215, 218, 224)
const COL_AXIS   = (120, 124, 132)
const COL_AB     = (28, 100, 180)
const COL_ZETA   = (200, 40, 40)
const COL_GUE    = (44, 160, 44)
const COL_POIS   = (130, 130, 130)
const COL_ORANGE = (235, 130, 32)
const COL_PURPLE = (140, 80, 190)
const COL_GOLD   = (255, 214, 64)
const COL_CYAN   = (0, 150, 170)
const COL_PINK   = (214, 90, 150)
const COL_RED    = COL_ZETA
const COL_DARKGR = (90, 94, 102)
# =============================================================================
# Plot builders (ABPlotV23-style): frame, axes, series, legend, footers
# =============================================================================

mutable struct Plot2D
    c    :: Canvas
    px0  :: Float64; py0 :: Float64; px1 :: Float64; py1 :: Float64   # plot rect (final px)
    xmin :: Float64; xmax :: Float64; ymin :: Float64; ymax :: Float64
    legend :: Vector{Tuple{String,Tuple{Int,Int,Int},Symbol}}
    title  :: String
    subttl :: String
    xlab   :: String
    ylab   :: String
    footer :: String
end

function Plot2D(title::AbstractString; sub = "", w::Int = 1600, h::Int = 1000)
    c = Canvas(w, h; ss = 2, bg = COL_BG)
    return Plot2D(c, 135.0, 118.0, w - 35.0, h - 140.0, 0.0, 1.0, 0.0, 1.0,
                  Tuple{String,Tuple{Int,Int,Int},Symbol}[],
                  String(title), String(sub), "", "", "")
end

Xmap(p::Plot2D, x::Real) = p.px0 + (x - p.xmin) / max(p.xmax - p.xmin, eps()) * (p.px1 - p.px0)
Ymap(p::Plot2D, y::Real) = p.py1 - (y - p.ymin) / max(p.ymax - p.ymin, eps()) * (p.py1 - p.py0)

function set_xlim!(p::Plot2D, a::Real, b::Real); p.xmin, p.xmax = Float64(a), Float64(b); nothing end
function set_ylim!(p::Plot2D, a::Real, b::Real); p.ymin, p.ymax = Float64(a), Float64(b); nothing end

nice_ticks(a::Real, b::Real; target::Int = 6) = begin
    span = b - a
    span <= 0 && return collect(a:1.0:b)
    raw = span / max(target, 1)
    mag = 10.0^floor(log10(raw))
    norm = raw / mag
    step = mag * (norm < 1.5 ? 1.0 : norm < 3.5 ? 2.0 : norm < 7.5 ? 5.0 : 10.0)
    t0 = ceil(a / step) * step
    ts = collect(t0:step:b)
    return ts
end

function frame!(p::Plot2D; xlab::AbstractString = "", ylab::AbstractString = "")
    p.xlab = String(xlab); p.ylab = String(ylab)
    c = p.c
    # title & subtitle
    text!(c, 40, 22, p.title, COL_INK; scale = 5)
    isempty(p.subttl) || text!(c, 40, 62, p.subttl, COL_AXIS; scale = 3)
    # frame
    rect!(p)
    # ticks
    for tv in nice_ticks(p.xmin, p.xmax)
        xv = Xmap(p, tv)
        (xv < p.px0 - 1 || xv > p.px1 + 1) && continue
        hline!(c, p.py1, xv, xv + 0.001, COL_AXIS, 4.0)
        lab = abs(tv) >= 1000 ? @sprintf("%.0fk", tv / 1000) :
              abs(tv - round(tv)) < 1e-9 ? @sprintf("%d", round(Int, tv)) : @sprintf("%.2f", tv)
        text!(c, xv, p.py1 + 12, lab, COL_AXIS; scale = 3, align = :center)
    end
    for tv in nice_ticks(p.ymin, p.ymax)
        yv = Ymap(p, tv)
        (yv < p.py0 - 1 || yv > p.py1 + 1) && continue
        vline!(c, p.px0, yv, yv + 0.001, COL_AXIS, 4.0)
        lab = abs(tv) >= 1000 ? @sprintf("%.0fk", tv / 1000) :
              abs(tv - round(tv)) < 1e-9 ? @sprintf("%d", round(Int, tv)) : @sprintf("%.2f", tv)
        text!(c, p.px0 - 10, yv - 9, lab, COL_AXIS; scale = 3, align = :right)
    end
    # axis labels
    isempty(xlab) || text!(c, (p.px0 + p.px1) / 2, p.py1 + 52, xlab, COL_INK; scale = 4, align = :center)
    isempty(ylab) || begin
        cx = 34; cy = (p.py0 + p.py1) / 2
        # rotated 90 degrees: draw vertically char by char
        chars = collect(uppercase(ylab))
        totalh = (length(chars) * 6) * 3
        yy = cy - totalh / 2
        for chr in chars
            text!(c, cx, yy, string(chr), COL_INK; scale = 3)
            yy += 6 * 3
        end
    end
    nothing
end

rect!(p::Plot2D) = begin
    c = p.c
    hline!(c, p.py0, p.px0, p.px1, COL_INK, 2.0)
    hline!(c, p.py1, p.px0, p.px1, COL_INK, 2.0)
    vline!(c, p.px0, p.py0, p.py1, COL_INK, 2.0)
    vline!(c, p.px1, p.py0, p.py1, COL_INK, 2.0)
    nothing
end

function gridlines!(p::Plot2D; alpha = 0.8)
    c = p.c
    for tv in nice_ticks(p.xmin, p.xmax)
        xv = Xmap(p, tv)
        (p.px0 + 1 < xv < p.px1 - 1) && vline!(c, xv, p.py0 + 1, p.py1 - 1, COL_GRID, 1.0, alpha)
    end
    for tv in nice_ticks(p.ymin, p.ymax)
        yv = Ymap(p, tv)
        (p.py0 + 1 < yv < p.py1 - 1) && hline!(c, yv, p.px0 + 1, p.px1 - 1, COL_GRID, 1.0, alpha)
    end
    nothing
end

function series!(p::Plot2D, xs::AbstractVector, ys::AbstractVector,
                 col; label::AbstractString = "", wpx::Real = 3.0,
                 style::Symbol = :solid, markers::Bool = false, alpha::Float64 = 1.0)
    n = min(length(xs), length(ys))
    n == 0 && return nothing
    prev_in = false
    for i in 2:n
        xa, ya = Xmap(p, xs[i-1]), Ymap(p, ys[i-1])
        xb, yb = Xmap(p, xs[i]), Ymap(p, ys[i])
        inside = (xa >= p.px0 - 2 && xa <= p.px1 + 2 && ya >= p.py0 - 2 && ya <= p.py1 + 2) ||
                 (xb >= p.px0 - 2 && xb <= p.px1 + 2 && yb >= p.py0 - 2 && yb <= p.py1 + 2)
        inside || (prev_in = false; continue)
        if style === :dashed
            dash_line!(p.c, xa, ya, xb, yb, col, wpx, alpha)
        else
            line!(p.c, xa, ya, xb, yb, col, wpx, alpha)
        end
        prev_in = true
    end
    markers && for i in 1:n
        xv, yv = Xmap(p, xs[i]), Ymap(p, ys[i])
        (p.px0 <= xv <= p.px1 && p.py0 <= yv <= p.py1) && marker!(p.c, xv, yv, col; r = 3.5, alpha = alpha)
    end
    isempty(label) || push!(p.legend, (String(label), col, style))
    nothing
end

function hline_data!(p::Plot2D, y::Real, col; label::AbstractString = "", style::Symbol = :dashed)
    yv = clamp(Ymap(p, y), p.py0, p.py1)
    if style === :dashed
        dash_line!(p.c, p.px0, yv, p.px1, yv, col, 2.0, 0.8)
    else
        hline!(p.c, yv, p.px0, p.px1, col, 2.0, 0.9)
    end
    isempty(label) || push!(p.legend, (String(label), col, style))
    nothing
end

function vline_data!(p::Plot2D, x::Real, col; label::AbstractString = "", style::Symbol = :dashed)
    xv = clamp(Xmap(p, x), p.px0, p.px1)
    if style === :dashed
        dash_line!(p.c, xv, p.py0, xv, p.py1, col, 2.0, 0.8)
    else
        vline!(p.c, xv, p.py0, p.py1, col, 2.0, 0.9)
    end
    isempty(label) || push!(p.legend, (String(label), col, style))
    nothing
end

function shade_yspan!(p::Plot2D, ylo::Real, yhi::Real, col; alpha::Float64 = 0.25, label = "")
    ya = clamp(Ymap(p, yhi), p.py0, p.py1)
    yb = clamp(Ymap(p, ylo), p.py0, p.py1)
    fill_rect!(p.c, p.px0 + 1, ya, p.px1 - 1, yb, col, alpha)
    isempty(String(label)) || push!(p.legend, (String(label), col, :band))
    nothing
end

function shade_xspan!(p::Plot2D, xlo::Real, xhi::Real, col; alpha::Float64 = 0.25, label = "")
    xa = clamp(Xmap(p, xlo), p.px0, p.px1)
    xb = clamp(Xmap(p, xhi), p.px0, p.px1)
    fill_rect!(p.c, xa, p.py0 + 1, xb, p.py1 - 1, col, alpha)
    isempty(String(label)) || push!(p.legend, (String(label), col, :band))
    nothing
end

function bars!(p::Plot2D, xs, ys, col; label::AbstractString = "", alpha::Float64 = 0.85, base = nothing)
    ybase = base === nothing ? max(p.ymin, 0.0) : base
    n = min(length(xs), length(ys))
    span = (p.px1 - p.px0) / max(n, 1)
    for i in 1:n
        xv = Xmap(p, xs[i]); yv = Ymap(p, ys[i]); yb = Ymap(p, ybase)
        wbar = max(2.0, span * 0.7)
        fill_rect!(p.c, xv - wbar / 2, yv, xv + wbar / 2, yb, col, alpha)
    end
    isempty(label) || push!(p.legend, (String(label), col, :bar))
    nothing
end

function legend!(p::Plot2D; scale::Int = 3)
    isempty(p.legend) && return nothing
    c = p.c
    pad = 12
    lh = 8 * scale + 6
    wmax = maximum(text_width(e[1], scale) for e in p.legend) + 34 + 2 * pad
    hgt = length(p.legend) * lh + 2 * pad
    x0 = p.px1 - wmax - 10; y0 = p.py0 + 10
    fill_rect!(c, x0, y0, x0 + wmax, y0 + hgt, (255, 255, 255), 0.92)
    hline!(c, y0, x0, x0 + wmax, COL_AXIS, 1.5)
    hline!(c, y0 + hgt, x0, x0 + wmax, COL_AXIS, 1.5)
    vline!(c, x0, y0, y0 + hgt, COL_AXIS, 1.5)
    vline!(c, x0 + wmax, y0, y0 + hgt, COL_AXIS, 1.5)
    for (i, (lab, col, style)) in enumerate(p.legend)
        yy = y0 + pad + (i - 1) * lh + lh / 2
        if style === :band || style === :bar
            fill_rect!(c, x0 + pad, yy - 5, x0 + pad + 26, yy + 5, col, style === :bar ? 0.9 : 0.35)
        else
            if style === :dashed
                dash_line!(c, x0 + pad, yy, x0 + pad + 26, yy, col, 3.0, 1.0)
            else
                hline!(c, yy, x0 + pad, x0 + pad + 26, col, 3.0)
            end
        end
        text!(c, x0 + pad + 34, yy - 7 * scale / 2 - 1, lab, COL_INK; scale = scale)
    end
    nothing
end

function footer!(p::Plot2D, s::AbstractString)
    p.footer = String(s)
    text!(p.c, 40, p.c.h - 24, s, COL_AXIS; scale = 2)
    nothing
end

function save!(p::Plot2D, path::AbstractString)
    legend!(p)
    isempty(p.footer) || footer!(p, p.footer)
    save_png(p.c, path)
    nothing
end

"standard footer text for all plots"
plot_footer(mode::AbstractString) =
    "Test 34 standalone lab · $mode · run $(LAB_RUN_ID[]) · L=$(LAB.L) Nv=$(LAB.Nv) q=$(LAB.q) alpha=$(LAB.alpha) W=$(LAB.W) · zeros=$(LAB.n_zeros)"
# =============================================================================
# Concrete report plots (1600x1000, English labels — bitmap font is ASCII)
# =============================================================================

function plot_R2_comparison(path, cen_ab, R2ab, cen_z, R2z; mode = "MODE", note = "")
    p = Plot2D("Test 34 · Pair correlation R2(s)"; sub = note)
    allc = vcat(cen_ab, cen_z)
    lo, hi = 0.0, min(3.0, maximum(allc) + 0.05)
    set_xlim!(p, 0.0, hi)
    set_ylim!(p, 0.0, max(1.9, maximum(vcat(R2ab, R2z)) + 0.15))
    gridlines!(p)
    sg = collect(0.0:0.01:hi)
    shade_yspan!(p, 0.75, 1.25, COL_GOLD; alpha = 0.18, label = "plateau band")
    series!(p, sg, [1.0 for _ in sg], COL_POIS; label = "Poisson (R2 = 1)", wpx = 2.0, style = :dashed)
    series!(p, sg, gue_r2.(sg), COL_GUE; label = "GUE theory", wpx = 3.0)
    series!(p, cen_z, R2z, COL_ZETA; label = "zeta zeros", wpx = 3.0)
    series!(p, cen_ab, R2ab, COL_AB; label = "AB cloud", wpx = 3.0, markers = true)
    frame!(p; xlab = "unfolded spacing s", ylab = "R2(s)")
    footer!(p, plot_footer(mode))
    save!(p, path)
    nothing
end

function plot_pdf_spacings(path, s_ab, s_z; mode = "MODE", note = "")
    p = Plot2D("Test 34 · Spacing distribution p(s)"; sub = note)
    nb = 60; smax = 4.0
    h_ab = fit_hist_pdf(s_ab, 0.0, smax, nb)
    h_z  = fit_hist_pdf(s_z,  0.0, smax, nb)
    set_xlim!(p, 0.0, smax); set_ylim!(p, 0.0, 1.15)
    gridlines!(p)
    sg = collect(0.0:0.01:smax)
    cb = [(h_ab.edges[i] + h_ab.edges[i+1]) / 2 for i in 1:nb]
    cz = [(h_z.edges[i]  + h_z.edges[i+1])  / 2 for i in 1:nb]
    series!(p, sg, [gue_pdf(s) for s in sg], COL_GUE; label = "GUE Wigner", wpx = 3.0)
    series!(p, sg, [exp(-s) for s in sg], COL_POIS; label = "Poisson", wpx = 2.0, style = :dashed)
    series!(p, cb, h_z.w, COL_ZETA; label = "zeta zeros", wpx = 3.0, style = :solid)
    series!(p, cb, h_ab.w, COL_AB; label = "AB cloud", wpx = 3.0, markers = true)
    frame!(p; xlab = "unfolded spacing s", ylab = "p(s)")
    footer!(p, plot_footer(mode))
    save!(p, path)
    nothing
end

struct HistPdf
    edges :: Vector{Float64}
    w     :: Vector{Float64}
end

function fit_hist_pdf(x::Vector{Float64}, lo::Real, hi::Real, nb::Int)
    edges = collect(range(Float64(lo), Float64(hi); length = nb + 1))
    w = zeros(Float64, nb)
    dx = edges[2] - edges[1]
    for v in x
        b = floor(Int, (v - lo) / dx) + 1
        (1 <= b <= nb) && (w[b] += 1.0)
    end
    total = length(x) > 0 ? length(x) * dx : 1.0
    return HistPdf(edges, w ./ total)
end

function plot_D_distribution(path, Ds; thresh = 0.10, mode = "MODE", note = "", flagged = Bool[])
    p = Plot2D("Test 34 · KS distance D per realization"; sub = note)
    n = length(Ds)
    med = median(Ds)
    set_xlim!(p, 0.0, n + 1.0)
    set_ylim!(p, 0.0, max(0.05, maximum(Ds) * 1.25))
    gridlines!(p)
    hline_data!(p, thresh, COL_ORANGE; label = "threshold D = 0.10")
    hline_data!(p, med, COL_GUE; label = @sprintf("median = %.4f", med), style = :solid)
    xs = collect(1.0:n)
    cols = [isempty(flagged) || !flagged[i] ? COL_AB : COL_RED for i in 1:n]
    for i in 1:n
        xv = Xmap(p, xs[i]); yv = Ymap(p, Ds[i]); yb = Ymap(p, 0.0)
        wbar = max(2.0, (p.px1 - p.px0) / n * 0.6)
        fill_rect!(p.c, xv - wbar / 2, yv, xv + wbar / 2, yb, cols[i], 0.85)
    end
    for i in 1:n
        isempty(flagged) || flagged[i] || continue
        text!(p.c, Xmap(p, xs[i]), Ymap(p, Ds[i]) - 22, "#$i", COL_RED; scale = 3, align = :center)
    end
    push!(p.legend, ("outlier (MAD)", COL_RED, :bar))
    push!(p.legend, ("realization D", COL_AB, :bar))
    frame!(p; xlab = "realization #", ylab = "D (two-sample KS vs zeta)")
    footer!(p, plot_footer(mode))
    save!(p, path)
    nothing
end

function plot_cdf_compare(path, s_ab, s_z; mode = "MODE", note = "")
    p = Plot2D("Test 34 · CDF of unfolded spacings"; sub = note)
    sab = sort(s_ab); sz = sort(s_z)
    set_xlim!(p, 0.0, min(4.0, maximum(sab)))
    set_ylim!(p, 0.0, 1.02)
    gridlines!(p)
    sg = collect(0.0:0.01:4.0)
    series!(p, sg, [gue_cdf(s) for s in sg], COL_GUE; label = "GUE", wpx = 3.0)
    series!(p, sg, [pois_cdf(s) for s in sg], COL_POIS; label = "Poisson", wpx = 2.0, style = :dashed)
    series!(p, sz, collect(1:length(sz)) ./ length(sz), COL_ZETA; label = "zeta zeros", wpx = 3.0)
    series!(p, sab, collect(1:length(sab)) ./ length(sab), COL_AB; label = "AB cloud", wpx = 3.0)
    frame!(p; xlab = "s", ylab = "CDF(s)")
    footer!(p, plot_footer(mode))
    save!(p, path)
    nothing
end

function plot_cdf_differential(path, sg, dabs, dsigned; mode = "MODE", note = "")
    p = Plot2D("Test 34 · CDF differential |F_AB - F_zeta|"; sub = note)
    set_xlim!(p, 0.0, maximum(sg))
    set_ylim!(p, 0.0, max(0.01, maximum(dabs) * 1.2))
    gridlines!(p)
    vline_data!(p, sg[argmax(dabs)], COL_ORANGE;
                label = @sprintf("max |dF| = %.4f at s = %.2f", maximum(dabs), sg[argmax(dabs)]))
    series!(p, sg, dabs, COL_AB; label = "|F_AB - F_zeta|", wpx = 3.0)
    series!(p, sg, dsigned, COL_ZETA; label = "signed difference", wpx = 2.0, style = :solid)
    hline_data!(p, 0.0, COL_POIS; style = :solid)
    frame!(p; xlab = "s", ylab = "F_AB(s) - F_zeta(s)")
    footer!(p, plot_footer(mode))
    save!(p, path)
    nothing
end

function plot_shortrange(path, cen_ab, R2ab, cen_z, R2z; mode = "MODE", note = "")
    p = Plot2D("Test 34 · Short-range repulsion zone (s < 1.2)"; sub = note)
    set_xlim!(p, 0.0, 1.2)
    ymax = max(1.1, maximum(vcat(R2ab[cen_ab .<= 1.2], R2z[cen_z .<= 1.2])) * 1.15)
    set_ylim!(p, 0.0, ymax)
    gridlines!(p)
    sg = collect(0.0:0.005:1.2)
    shade_xspan!(p, 0.2, 0.6, COL_GOLD; alpha = 0.20, label = "deficit zone 0.2-0.6")
    series!(p, sg, gue_r2.(sg), COL_GUE; label = "GUE theory", wpx = 3.0)
    series!(p, cen_z, R2z, COL_ZETA; label = "zeta zeros", wpx = 3.0)
    series!(p, cen_ab, R2ab, COL_AB; label = "AB cloud", wpx = 3.0, markers = true)
    frame!(p; xlab = "unfolded spacing s", ylab = "R2(s)")
    footer!(p, plot_footer(mode))
    save!(p, path)
    nothing
end

function plot_lattice_scaling(path, Ls, Ds; mode = "MODE", note = "")
    p = Plot2D("Test 34 · Finite-size scaling of D"; sub = note)
    set_xlim!(p, minimum(Ls) - 8, maximum(Ls) + 8)
    set_ylim!(p, 0.0, max(0.05, maximum(Ds) * 1.3))
    gridlines!(p)
    hline_data!(p, 0.10, COL_ORANGE; label = "D = 0.10")
    series!(p, collect(Ls), Ds, COL_AB; label = "D(L)", wpx = 3.0, markers = true)
    for (L, D) in zip(Ls, Ds)
        text!(p.c, Xmap(p, L), Ymap(p, D) - 24, @sprintf("%.4f", D), COL_INK; scale = 3, align = :center)
    end
    frame!(p; xlab = "lattice side L", ylab = "D")
    footer!(p, plot_footer(mode))
    save!(p, path)
    nothing
end

function plot_stability_map(path, xs, Ds, dGs, dPs, goldmask, xstar, xlab, mode; note = "", plabel = "alpha")
    p = Plot2D("Test 34 · Vortex sweep stabilization map"; sub = note)
    allv = vcat(Ds, dGs, dPs)
    set_xlim!(p, minimum(xs) - (xlab == "Nv" ? 0.5 : 0.03), maximum(xs) + (xlab == "Nv" ? 0.5 : 0.03))
    set_ylim!(p, 0.0, max(0.05, maximum(allv) * 1.25))
    gridlines!(p)
    # shade gold zone along x (contiguous runs)
    i = 1
    n = length(xs)
    while i <= n
        if goldmask[i]
            j = i
            while j < n && goldmask[j+1]; j += 1; end
            shade_xspan!(p, xs[i] - 0.005, xs[j] + 0.005, COL_GOLD; alpha = 0.30, label = "stabilization zone")
            i = j + 1
        else
            i += 1
        end
    end
    hline_data!(p, 0.10, COL_ORANGE; label = "D = 0.10")
    series!(p, xs, dPs, COL_POIS; label = "d_Pois", wpx = 2.5, style = :dashed)
    series!(p, xs, dGs, COL_ZETA; label = "d_GUE", wpx = 2.5)
    series!(p, xs, Ds, COL_AB; label = "D (KS vs zeta)", wpx = 3.0, markers = true)
    xstar !== nothing && vline_data!(p, xstar, COL_GUE; label = @sprintf("crossover %s* = %.3f", plabel, xstar))
    frame!(p; xlab = plabel, ylab = "distance")
    footer!(p, plot_footer(mode))
    save!(p, path)
    nothing
end

function plot_R2_evolution(path, curves; mode = "MODE", note = "")
    # curves: Vector of (label, centers, R2, color)
    p = Plot2D("Test 34 · R2(s) evolution across sweep"; sub = note)
    allc = Float64[]; allv = Float64[]
    for (_, c, v, _) in curves
        append!(allc, c); append!(allv, v)
    end
    set_xlim!(p, 0.0, min(3.0, maximum(allc)))
    set_ylim!(p, 0.0, max(1.3, maximum(allv) * 1.1))
    gridlines!(p)
    sg = collect(0.0:0.01:min(3.0, maximum(allc)))
    series!(p, sg, gue_r2.(sg), COL_GUE; label = "GUE theory", wpx = 2.5)
    for (lab, c, v, col) in curves
        series!(p, c, v, col; label = lab, wpx = 2.5)
    end
    frame!(p; xlab = "unfolded spacing s", ylab = "R2(s)")
    footer!(p, plot_footer(mode))
    save!(p, path)
    nothing
end

function plot_seed_forensics(path, Ds, seedlabels; mode = "MODE", note = "")
    p = Plot2D("Test 34 · Seed forensics (same params, different seeds)"; sub = note)
    n = length(Ds)
    med = median(Ds)
    set_xlim!(p, 0.0, n + 1.0)
    set_ylim!(p, 0.0, max(0.02, maximum(Ds) * 1.3))
    gridlines!(p)
    hline_data!(p, med, COL_GUE; label = @sprintf("median = %.4f", med))
    for i in 1:n
        xv = Xmap(p, i); yv = Ymap(p, Ds[i]); yb = Ymap(p, 0.0)
        wbar = max(3.0, (p.px1 - p.px0) / n * 0.55)
        col = abs(Ds[i] - med) > 3 * 1.4826 * max(median(abs.(Ds .- med)), 1e-9) ? COL_RED : COL_AB
        fill_rect!(p.c, xv - wbar / 2, yv, xv + wbar / 2, yb, col, 0.9)
        text!(p.c, xv, p.py1 + 14, let sl = seedlabels[i]; length(sl) > 6 ? sl[end-5:end] : sl end, COL_AXIS; scale = 2, align = :center)
    end
    push!(p.legend, ("D per seed", COL_AB, :bar))
    push!(p.legend, ("MAD outlier", COL_RED, :bar))
    frame!(p; xlab = "seed #", ylab = "D")
    footer!(p, plot_footer(mode))
    save!(p, path)
    nothing
end

function plot_bootstrap(path, Ds; mode = "MODE", note = "")
    p = Plot2D("Test 34 · Bootstrap distribution of D"; sub = note)
    nb = 50
    lo, hi = minimum(Ds), maximum(Ds)
    edges = collect(range(lo, hi; length = nb + 1))
    w = zeros(Int, nb)
    for v in Ds
        b = clamp(floor(Int, (v - lo) / (hi - lo) * nb) + 1, 1, nb)
        w[b] += 1
    end
    set_xlim!(p, lo - 0.2 * (hi - lo) - eps(), hi + 0.05 * (hi - lo) + eps())
    set_ylim!(p, 0.0, maximum(w) * 1.2)
    gridlines!(p)
    cb = [(edges[i] + edges[i+1]) / 2 for i in 1:nb]
    bars!(p, cb, float.(w), COL_AB; label = "bootstrap resamples")
    ci_lo, ci_hi = quantile(Ds, 0.025), quantile(Ds, 0.975)
    shade_xspan!(p, ci_lo, ci_hi, COL_GUE; alpha = 0.18,
                 label = @sprintf("95%% CI [%.4f, %.4f]", ci_lo, ci_hi))
    frame!(p; xlab = "D", ylab = "count")
    footer!(p, plot_footer(mode))
    save!(p, path)
    nothing
end
# =============================================================================
# Report generators: FINAL_REPORT.md, index.html, CSV, config.json
# =============================================================================

struct RealizationRow
    idx      :: Int
    seed     :: Int
    nspac    :: Int
    D        :: Float64
    p        :: Float64
    dGUE     :: Float64
    dPois    :: Float64
    plateau  :: Float64
    banddev  :: Float64
    tbuild   :: Float64
    tdiag    :: Float64
    flag     :: Bool
end

struct RunReport
    mode       :: Int
    mode_name  :: String
    rundir     :: String
    verdict    :: Tuple{Bool,Bool,Bool,Bool}   # pass, c1, c2, c3 (pooled)
    pooled     :: Union{Nothing,RealizationRow}
    rows       :: Vector{RealizationRow}
    notes      :: Vector{String}
    extra      :: Vector{Pair{String,String}}   # key -> value lines
end

_boolmark(b) = b ? "[OK]" : "[!!]"

function verdict_verbal(pass::Bool)
    return pass ? t(:v_pass) : t(:v_fail)
end

function write_csv_realizations(rundir, rows::Vector{RealizationRow})
    path = joinpath(rundir, "data_realizations.csv")
    open(path, "w") do io
        println(io, "idx,seed,n_spacings,D,p,d_GUE,d_Pois,plateau,band_dev,t_build_s,t_diag_s,flagged")
        for r in rows
            @printf(io, "%d,%d,%d,%.6f,%.3e,%.6f,%.6f,%.6f,%.6f,%.2f,%.2f,%s\n",
                    r.idx, r.seed, r.nspac, r.D, r.p, r.dGUE, r.dPois, r.plateau, r.banddev,
                    r.tbuild, r.tdiag, r.flag ? "yes" : "no")
        end
    end
    return path
end

function write_csv_r2(rundir, cen_ab, R2ab, cen_z, R2z)
    path = joinpath(rundir, "data_R2.csv")
    open(path, "w") do io
        println(io, "s,R2_AB,R2_zeta,R2_GUE_theory")
        for (ca, za) in zip(cen_ab, R2ab)
            @printf(io, "%.4f,%.6f,,%.6f\n", ca, za, gue_r2(ca))
        end
        for (cz, zz) in zip(cen_z, R2z)
            @printf(io, "%.4f,,%.6f,%.6f\n", cz, zz, gue_r2(cz))
        end
    end
    return path
end

function write_csv_spacings(rundir, s_ab, s_z)
    path = joinpath(rundir, "data_spacings.csv")
    open(path, "w") do io
        println(io, "s_AB,s_zeta")
        n = max(length(s_ab), length(s_z))
        for i in 1:n
            a = i <= length(s_ab) ? @sprintf("%.8f", s_ab[i]) : ""
            z = i <= length(s_z) ? @sprintf("%.8f", s_z[i]) : ""
            println(io, a * "," * z)
        end
    end
    return path
end

function write_config_json(rundir, mode::Int = 0)
    path = joinpath(rundir, "config.json")
    open(path, "w") do io
        println(io, "{")
        @printf(io, "  \"run_id\": \"%s\",\n", LAB_RUN_ID[])
        @printf(io, "  \"mode\": %d,\n", mode)
        @printf(io, "  \"julia\": \"%s\",\n", string(VERSION))
        @printf(io, "  \"zeros_file\": \"%s\",\n", replace(LAB.zeros_file, "\\" => "/"))
        @printf(io, "  \"n_zeros\": %d,\n", LAB.n_zeros)
        @printf(io, "  \"geometry\": \"%s\",\n", String(GEOM[].id))
        @printf(io, "  \"L\": %d,\n", LAB.L)
        begin
            Le_c, _ = geom_L_eff(GEOM[], LAB.L)
            @printf(io, "  \"L_effective\": %d,\n", Le_c)
            @printf(io, "  \"matrix_sites\": %d,\n", geom_nsites(GEOM[], Le_c))
            @printf(io, "  \"lift_k\": %d,\n", cayley_lift_k(GEOM[], LAB.L))
        end
        @printf(io, "  \"autoscale\": %s,\n", LAB.autoscale ? "true" : "false")
        @printf(io, "  \"Nv\": %d,\n", LAB.Nv)
        @printf(io, "  \"q\": %.6f,\n", LAB.q)
        @printf(io, "  \"alpha\": %.6f,\n", LAB.alpha)
        @printf(io, "  \"W\": %.6f,\n", LAB.W)
        @printf(io, "  \"reps1\": %d,\n", LAB.reps1)
        @printf(io, "  \"reps2\": %d,\n", LAB.reps2)
        @printf(io, "  \"reps5\": %d,\n", LAB.reps5)
        @printf(io, "  \"sweep_param\": \"%s\",\n", String(LAB.sweep_param))
        @printf(io, "  \"seed_base\": %d,\n", LAB.seed_base)
        @printf(io, "  \"window_frac\": %.4f,\n", LAB.window_frac)
        @printf(io, "  \"threads\": %d,\n", Threads.nthreads())
        @printf(io, "  \"generated\": \"%s\"\n", Dates.format(Dates.now(), "yyyy-mm-dd HH:MM:SS"))
        println(io, "}")
    end
    return path
end

# --------------------------------------------------------------------- markdown

function write_report_md(rep::RunReport; extra_blocks::Vector{String} = String[])
    path = joinpath(rep.rundir, "FINAL_REPORT.md")
    open(path, "w") do io
        println(io, "# Test 34 — FINAL REPORT")
        println(io)
        @printf(io, "**Run:** `%s` · **Mode:** %d — %s · **Generated:** %s\n\n",
                LAB_RUN_ID[], rep.mode, rep.mode_name,
                Dates.format(Dates.now(), "yyyy-mm-dd HH:MM:SS"))
        println(io, "## Configuration")
        println(io)
        println(io, "| parameter | value |")
        println(io, "|---|---|")
        @printf(io, "| zeros file | `%s` |\n", LAB.zeros_file)
        @printf(io, "| zeros used | %d |\n", LAB.n_zeros)
        @printf(io, "| geometry | %s |\n", geometry_label(current_geometry(), LAB.L))
        let Leff_big = geom_L_eff(current_geometry(), LAB.L)[1]
            @printf(io, "| lattice | requested L = %d → effective %s (%d sites) |\n", LAB.L,
                    geom_site_label(current_geometry(), Leff_big), geom_nsites(current_geometry(), Leff_big))
        end
        @printf(io, "| vortices Nv | %d |\n", LAB.Nv)
        @printf(io, "| charge q | %.4f |\n", LAB.q)
        @printf(io, "| flux alpha | %.4f |\n", LAB.alpha)
        @printf(io, "| disorder W | %.4f |\n", LAB.W)
        @printf(io, "| threads | %d |\n", Threads.nthreads())
        println(io)
        println(io, "## Composite verdict (v23-compatible)")
        println(io)
        pass, c1, c2, c3 = rep.verdict
        @printf(io, "%s **%s**\n\n", _boolmark(pass), verdict_verbal(pass))
        println(io, "| criterion | rule | status |")
        println(io, "|---|---|---|")
        @printf(io, "| c1 | (p > 0.01 OR D < 0.10) | %s |\n", _boolmark(c1))
        @printf(io, "| c2 | d_GUE < d_Pois | %s |\n", _boolmark(c2))
        @printf(io, "| c3 | 0.75 <= R2 plateau <= 1.25 | %s |\n", _boolmark(c3))
        println(io)
        if rep.pooled !== nothing
            pl = rep.pooled
            println(io, "## Pooled statistics")
            println(io)
            println(io, "| metric | value |")
            println(io, "|---|---|")
            @printf(io, "| pooled D (two-sample KS vs zeta) | %.4f |\n", pl.D)
            @printf(io, "| pooled p | %.3e |\n", pl.p)
            @printf(io, "| d_GUE | %.4f |\n", pl.dGUE)
            @printf(io, "| d_Pois | %.4f |\n", pl.dPois)
            @printf(io, "| R2 plateau (1.0-2.0) | %.4f |\n", pl.plateau)
            @printf(io, "| mean |R2-GUE| band 0.2-2.0 | %.4f |\n", pl.banddev)
            @printf(io, "| spacings | %d |\n", pl.nspac)
            println(io)
        end
        if !isempty(rep.rows)
            println(io, "## Realizations")
            println(io)
            println(io, "| # | seed | spacings | D | p | d_GUE | d_Pois | plateau | flag |")
            println(io, "|---|---|---|---|---|---|---|---|---|")
            for r in rep.rows
                @printf(io, "| %d | %d | %d | %.4f | %.2e | %.4f | %.4f | %.4f | %s |\n",
                        r.idx, r.seed, r.nspac, r.D, r.p, r.dGUE, r.dPois, r.plateau,
                        r.flag ? "**outlier**" : "-")
            end
            println(io)
        end
        for blk in extra_blocks
            println(io, blk)
            println(io)
        end
        for (k, v) in rep.extra
            println(io, "- **$k:** $v")
        end
        isempty(rep.extra) || println(io)
        println(io, "## Notes")
        println(io)
        for n in rep.notes
            println(io, " - ", n)
        end
        println(io)
        println(io, "## Files")
        println(io)
        for f in sort(readdir(rep.rundir))
            println(io, " - `$f`")
        end
        println(io)
        println(io, "## Timing")
        println(io)
        names, secs = PHASES[][2], PHASES[][3]
        for (n, s) in zip(names, secs)
            println(io, " - $n: ", fmt_sec(s))
        end
        println(io, " - **TOTAL**: ", fmt_sec(sum(secs)))
    end
    return path
end

# ------------------------------------------------------------------------- html

const _HTML_CSS = """
body{font-family:'Segoe UI',system-ui,Arial,sans-serif;margin:0;background:#f4f5f7;color:#23262c}
header{background:linear-gradient(120deg,#101828,#1c3a6e);color:#fff;padding:28px 40px}
header h1{margin:0 0 6px;font-size:26px;letter-spacing:.4px}
header .meta{color:#b8c4dc;font-size:13px}
main{max-width:1100px;margin:26px auto;padding:0 20px}
.cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(170px,1fr));gap:14px;margin:18px 0}
.card{background:#fff;border-radius:12px;padding:16px 18px;box-shadow:0 1px 4px rgba(20,30,60,.08)}
.card .k{font-size:12px;color:#7a808c;text-transform:uppercase;letter-spacing:.6px}
.card .v{font-size:24px;font-weight:700;margin-top:4px}
.verdict{border-radius:12px;padding:18px 22px;margin:18px 0;color:#fff;font-size:17px;font-weight:600}
.ok{background:linear-gradient(120deg,#1d7a3a,#2ea052)} .bad{background:linear-gradient(120deg,#a33228,#d05a3a)}
table{border-collapse:collapse;width:100%;background:#fff;border-radius:10px;overflow:hidden;box-shadow:0 1px 4px rgba(20,30,60,.08);font-size:14px}
th{background:#eef1f6;text-align:left;padding:9px 12px;font-size:12px;text-transform:uppercase;color:#5a6070}
td{padding:8px 12px;border-top:1px solid #eef0f4}
img{max-width:100%;border-radius:10px;box-shadow:0 1px 5px rgba(20,30,60,.12);margin:10px 0}
h2{font-size:19px;margin:30px 0 10px;border-left:4px solid #1c64b4;padding-left:10px}
.note{background:#fff8e0;border-left:4px solid #e8b931;padding:10px 14px;border-radius:6px;font-size:14px;margin:12px 0}
footer{text-align:center;color:#9aa0ab;font-size:12px;padding:24px}
"""

function write_report_html(rep::RunReport; extra_blocks::Vector{String} = String[])
    path = joinpath(rep.rundir, "index.html")
    pass, c1, c2, c3 = rep.verdict
    open(path, "w") do io
        println(io, "<!DOCTYPE html><html><head><meta charset='utf-8'>")
        println(io, "<title>Test 34 — ", rep.mode_name, " — ", LAB_RUN_ID[], "</title>")
        println(io, "<style>", _HTML_CSS, "</style></head><body>")
        println(io, "<header><h1>TEST 34 · STANDALONE LAB — ", uppercase(rep.mode_name), "</h1>")
        println(io, "<div class='meta'>run ", LAB_RUN_ID[], " · ", Dates.format(Dates.now(), "yyyy-mm-dd HH:MM:SS"),
                " · Julia ", VERSION, " · threads ", Threads.nthreads(), "</div></header><main>")
        println(io, "<div class='verdict ", pass ? "ok" : "bad", "'>",
                pass ? "GUE-CONSISTENT" : "DEVIATION DETECTED",
                " — composite verdict (v23): c1 ", _boolmark(c1), " · c2 ", _boolmark(c2),
                " · c3 ", _boolmark(c3), "</div>")
        println(io, "<div class='cards'>")
        if rep.pooled !== nothing
            pl = rep.pooled
            for (k, v) in (("pooled D", @sprintf("%.4f", pl.D)),
                           ("p-value", @sprintf("%.2e", pl.p)),
                           ("d_GUE", @sprintf("%.4f", pl.dGUE)),
                           ("d_Pois", @sprintf("%.4f", pl.dPois)),
                           ("R2 plateau", @sprintf("%.4f", pl.plateau)),
                           ("spacings", string(pl.nspac)))
                println(io, "<div class='card'><div class='k'>", k, "</div><div class='v'>", v, "</div></div>")
            end
        end
        println(io, "</div>")
        println(io, "<h2>Configuration</h2><table>")
        Leff_html = geom_L_eff(current_geometry(), LAB.L)[1]
        for (k, v) in (("zeros file", "`" * LAB.zeros_file * "`"),
                       ("zeros used", string(LAB.n_zeros)),
                       ("geometry", geometry_label(current_geometry(), LAB.L)),
                       ("lattice", "requested L = $(LAB.L) → effective $(geom_site_label(current_geometry(), Leff_html)) ($(geom_nsites(current_geometry(), Leff_html)) sites)"),
                       ("vortices Nv / charge q", "$(LAB.Nv) / $(LAB.q)"),
                       ("flux alpha / disorder W", "$(LAB.alpha) / $(LAB.W)"))
            println(io, "<tr><th>", k, "</th><td>", v, "</td></tr>")
        end
        println(io, "</table>")
        if !isempty(rep.rows)
            println(io, "<h2>Realizations</h2><table><tr><th>#</th><th>seed</th><th>spacings</th><th>D</th><th>p</th><th>d_GUE</th><th>d_Pois</th><th>plateau</th><th>flag</th></tr>")
            for r in rep.rows
                println(io, "<tr><td>", r.idx, "</td><td>", r.seed, "</td><td>", r.nspac,
                        "</td><td>", @sprintf("%.4f", r.D), "</td><td>", @sprintf("%.2e", r.p),
                        "</td><td>", @sprintf("%.4f", r.dGUE), "</td><td>", @sprintf("%.4f", r.dPois),
                        "</td><td>", @sprintf("%.4f", r.plateau), "</td><td>",
                        r.flag ? "<b style='color:#c33'>outlier</b>" : "-", "</td></tr>")
            end
            println(io, "</table>")
        end
        for blk in extra_blocks
            println(io, blk)
        end
        println(io, "<h2>Plots</h2>")
        for f in sort(readdir(rep.rundir))
            endswith(f, ".png") && println(io, "<img src='", f, "' alt='", f, "'>")
        end
        println(io, "<h2>Notes</h2><ul>")
        for n in rep.notes
            println(io, "<li>", n, "</li>")
        end
        println(io, "</ul>")
        isempty(rep.extra) || begin
            println(io, "<h2>Extra results</h2><table>")
            for (k, v) in rep.extra
                println(io, "<tr><th>", k, "</th><td>", v, "</td></tr>")
            end
            println(io, "</table>")
        end
        names, secs = PHASES[][2], PHASES[][3]
        println(io, "<h2>Timing</h2><table>")
        for (n, s) in zip(names, secs)
            println(io, "<tr><th>", n, "</th><td>", fmt_sec(s), "</td></tr>")
        end
        println(io, "<tr><th><b>TOTAL</b></th><td><b>", fmt_sec(sum(secs)), "</b></td></tr></table>")
        println(io, "</main><footer>finite-size_lab.jl · Test 34 standalone laboratory · AB-cloud vs Riemann zeros</footer>")
        println(io, "</body></html>")
    end
    return path
end
# =============================================================================
# Shared mode helpers + MODE 1 (NORMAL) + MODE 2 (HARDCORE)
# =============================================================================

function mode_header(mode::Int, name::AbstractString, subtitle::AbstractString)
    println()
    println(cc("═"^78, C_CYN))
    println(cc("  MODE $mode — $name  ·  $subtitle", C_B))
    println(cc("═"^78, C_CYN))
    nothing
end

"""
    matrix_size_banner(quiet) -> nothing

HONEST-SIZE FIX (v1.2) — the anti-"menu ignores my parameters" guard, printed
before every mode run: whenever the matrix that is about to be diagonalized is
smaller than 90% of the requested L² budget (fixed-size Hurwitz group, or
autoscale OFF clamps), the run says so LOUDLY — the true matrix size, the
reason, and the concrete remedy (psl227 / torus / klein / pillow / cubic for
a big Hurwitz-like matrix, or menu [8] → [a] to enable autoscale).
"""
function matrix_size_banner(quiet::Bool = false)
    quiet && return nothing
    geo = GEOM[]
    Le, _ = geom_L_eff(geo, LAB.L)
    n = geom_nsites(geo, Le)
    budget = LAB.L * LAB.L
    n >= round(Int, 0.90 * budget) && return nothing
    println(cc("  [!] " * t(:warn_matrix_head) * " $(n)x$(n) = $(n) " * t(:warn_matrix_sites) *
               " = $(round(Int, 100n / budget))% " * t(:warn_matrix_of_budget) *
               " L²=$(budget) (L=$(LAB.L))", C_YLW))
    if geo.model === :cayley
        println(cc("      " * t(:warn_matrix_reason_cayley), C_YLW))
        println(cc("      " * t(:warn_matrix_hint_cayley), C_YLW))
    else
        println(cc("      " * t(:warn_matrix_reason_autoscale_off), C_YLW))
        println(cc("      " * t(:warn_matrix_hint_autoscale), C_YLW))
    end
    nothing
end

function ensure_zeros!()
    if !isfile(LAB.zeros_file)
        println(cc("  ! " * t(:no_zeros_selected), C_YLW))
        isinteractive() || return false
        menu_zeros()
        isfile(LAB.zeros_file) || return false
    end
    LAB.n_zeros > 0 || (LAB.n_zeros = min(50_000, LAB.zeros_avail))
    LAB.n_zeros = min(LAB.n_zeros, LAB.zeros_avail)
    return true
end

function load_zeta_data!(pbar::Union{Nothing,PBar}; units_done = 0.0, units_total = 1.0, weight = 0.2)
    phase_begin!(t(:ph_load_zeros))
    gammas = load_zeros(LAB.zeros_file, LAB.n_zeros; pbar = nothing)
    pbar !== nothing && pbar_set!(pbar, (units_done + weight * 0.7) / units_total;
                                  sub = "zeta: loaded $(length(gammas)) zeros")
    s_z = unfold_zeta(gammas; patch_a = true)
    pbar !== nothing && pbar_set!(pbar, (units_done + weight) / units_total;
                                  sub = "zeta: unfolded $(length(s_z)) spacings")
    phase_end!(t(:ph_load_zeros))
    return gammas, s_z
end

function compute_row(idx::Int, seed::Int, s_ab::Vector{Float64}, s_z::Vector{Float64},
                     tbuild::Float64, tdiag::Float64)
    D, p = ks_two(s_ab, s_z)
    dG = ks_gue(s_ab)
    dP = ks_pois(s_ab)
    cen, R2 = pair_correlation(cumsum(s_ab))
    pl = r2_plateau(cen, R2)
    bd = r2_band_dev(cen, R2)
    return RealizationRow(idx, seed, length(s_ab), D, p, dG, dP, pl, bd, tbuild, tdiag, false)
end

# null-safe progress update (sub-runs of MODE 5 run without a bar)
_pset!(p::Union{Nothing,PBar}, frac::Real; sub::AbstractString = "") =
    p === nothing ? nothing : pbar_set!(p, frac; sub = sub)

const _ROW_COLS = ["#", "seed", "spacings", "D", "p", "d_GUE", "d_Pois", "plateau", "time"]
const _ROW_W    = [4, 13, 9, 8, 10, 8, 8, 9, 9]

function print_row(r::RealizationRow; flagcolor = true)
    flag = flagcolor && r.flag
    seed_s = length(string(r.seed)) > 8 ? ("…" * string(r.seed)[end-7:end]) : string(r.seed)
    cells = [@sprintf("%d", r.idx), seed_s, @sprintf("%d", r.nspac),
             @sprintf("%.4f", r.D), @sprintf("%.1e", r.p),
             @sprintf("%.4f", r.dGUE), @sprintf("%.4f", r.dPois),
             @sprintf("%.4f", r.plateau), fmt_sec(r.tbuild + r.tdiag)]
    lab_table_row(cells, _ROW_W)
    nothing
end

function print_pooled(pl::RealizationRow)
    println()
    println(cc("  " * t(:pooled_header), C_B))
    @printf(stdout, "    D(pooled) = %.4f   p = %.3e   d_GUE = %.4f   d_Pois = %.4f   plateau = %.4f   |R2-GUE| = %.4f\n",
            pl.D, pl.p, pl.dGUE, pl.dPois, pl.plateau, pl.banddev)
    nothing
end

function print_verdict(v::NamedTuple)
    ok = v.pass
    mark = ok ? cc("[OK] ", C_GRN, C_B) : cc("[!!] ", C_RED, C_B)
    line = mark * (ok ? cc(t(:v_pass), C_GRN, C_B) : cc(t(:v_fail), C_RED, C_B))
    println("  ", line)
    @printf(stdout, "      c1 (p>0.01 || D<0.10): %s   c2 (d_GUE<d_Pois): %s   c3 (0.75<=plateau<=1.25): %s\n",
            v.c1 ? "OK" : "FAIL", v.c2 ? "OK" : "FAIL", v.c3 ? "OK" : "FAIL")
    nothing
end

function mode_footer(rep::RunReport, run_t0::Float64)
    println(cc("  " * "-"^74, C_GRY))
    println(cc("  " * t(:out_dir) * ": ", C_B), rep.rundir)
    println(cc("  " * t(:report_files) * ": ", C_B), "FINAL_REPORT.md · index.html · data_*.csv · config.json")
    println(cc("  " * t(:timing_total) * ": ", C_B), fmt_sec(time() - run_t0))
    lab_save_settings()
    nothing
end

# =============================================================================
# MODE 1 — NORMAL (refined primary pass)
# =============================================================================

function run_mode1(; reps::Int = LAB.reps1, parent_dir::Union{Nothing,String} = nothing,
                   quiet::Bool = false, zeta::Union{Nothing,Vector{Float64}} = nothing)
    ensure_zeros!() || return nothing
    run_t0 = time()
    phases_reset!()
    quiet || mode_header(1, t(:m1_name), t(:m1_sub))
    quiet || matrix_size_banner(quiet)
    total_units = 1.0 + reps  # zeta load + reps
    pbar = PBar(28)
    quiet || pbar_start!(pbar, "MODE1")

    if zeta !== nothing
        s_z = zeta
    else
        gammas, s_z = load_zeta_data!(quiet ? nothing : pbar; units_done = 0.0,
                                      units_total = total_units, weight = 1.0)
    end

    rows = RealizationRow[]
    s_per_rep = Vector{Vector{Float64}}()
    for k in 1:reps
        seed = lab_seed(1, k)
        res, seed = ab_realization(seed, pbar, 1.0 + (k - 1), total_units; phase = @sprintf("rep %d/%d", k, reps))
        row = compute_row(k, seed, res.s, s_z, res.t_build, res.t_diag)
        push!(rows, row)
        push!(s_per_rep, res.s)
        _pset!(pbar, (1.0 + k) / total_units; sub = "rep $k/$reps done")
        quiet || println(cc("  ↳ ", C_GRY), "rep $k/$reps · D = ", @sprintf("%.4f", row.D),
                " · d_GUE = ", @sprintf("%.4f", row.dGUE), " · plateau = ", @sprintf("%.4f", row.plateau))
    end

    phase_begin!(t(:ph_analysis))
    s_pooled = vcat(s_per_rep...)
    pl = compute_row(0, 0, s_pooled, s_z, 0.0, 0.0)
    v = composite_verdict(pl.D, pl.p, pl.dGUE, pl.dPois, pl.plateau)
    out = mad_outliers([r.D for r in rows])
    rows = [RealizationRow(r.idx, r.seed, r.nspac, r.D, r.p, r.dGUE, r.dPois, r.plateau, r.banddev,
                           r.tbuild, r.tdiag, out.flags[i]) for (i, r) in enumerate(rows)]
    phase_end!(t(:ph_analysis))
    quiet || pbar_finish!(pbar, "· " * t(:done))

    # ---- console summary
    println()
    lab_table_header(_ROW_COLS, _ROW_W)
    foreach(print_row, rows)
    lab_table_footer((top = "", mid = "", bot = "└" * join(("─"^w for w in _ROW_W), "┴") * "┘"))
    print_pooled(pl)
    print_verdict(v)

    # ---- plots
    rundir = parent_dir !== nothing ? mkpath(parent_dir) : lab_new_run_dir(1)
    phase_begin!(t(:ph_plots))
    if LAB.plots_on
        println(cc("  " * t(:plots_rendering), C_GRY))
        u_ab = cumsum(s_pooled)
        u_z  = cumsum(s_z)
        cen_ab, R2ab = pair_correlation(u_ab)
        cen_z,  R2z  = pair_correlation(u_z)
        note = "pooled $reps realizations · $(length(s_pooled)) AB spacings vs $(length(s_z)) zeta spacings"
        plot_R2_comparison(joinpath(rundir, "plot_01_R2_comparison.png"), cen_ab, R2ab, cen_z, R2z;
                           mode = "MODE 1 NORMAL", note = note)
        plot_pdf_spacings(joinpath(rundir, "plot_02_spacing_pdf.png"), s_pooled, s_z;
                          mode = "MODE 1 NORMAL", note = note)
        plot_D_distribution(joinpath(rundir, "plot_03_D_per_realization.png"), [r.D for r in rows];
                            mode = "MODE 1 NORMAL", note = "D per realization", flagged = out.flags)
        plot_cdf_compare(joinpath(rundir, "plot_04_cdf.png"), s_pooled, s_z;
                         mode = "MODE 1 NORMAL", note = note)
        write_csv_r2(rundir, cen_ab, R2ab, cen_z, R2z)
        write_csv_spacings(rundir, s_pooled, s_z)
    end
    phase_end!(t(:ph_plots))

    rep = RunReport(1, t(:m1_name), rundir, (v.pass, v.c1, v.c2, v.c3), pl, rows,
                    [t(:n_mode1_note1), t(:n_mode1_note2)], Pair{String,String}[])
    write_csv_realizations(rundir, rows)
    write_config_json(rundir, 1)
    write_report_md(rep)
    write_report_html(rep)
    quiet || mode_footer(rep, run_t0)
    return rep
end

# =============================================================================
# MODE 2 — HARDCORE (refined ensemble pass)
# =============================================================================

function run_mode2(; reps::Int = LAB.reps2, parent_dir::Union{Nothing,String} = nothing,
                   quiet::Bool = false, zeta::Union{Nothing,Vector{Float64}} = nothing)
    ensure_zeros!() || return nothing
    run_t0 = time()
    phases_reset!()
    quiet || mode_header(2, t(:m2_name), t(:m2_sub))
    quiet || matrix_size_banner(quiet)
    total_units = 1.0 + reps
    pbar = PBar(28)
    quiet || pbar_start!(pbar, "MODE2")

    if zeta !== nothing
        s_z = zeta
    else
        gammas, s_z = load_zeta_data!(quiet ? nothing : pbar; units_done = 0.0,
                                      units_total = total_units, weight = 1.0)
    end

    rows = RealizationRow[]
    s_per_rep = Vector{Vector{Float64}}()
    for k in 1:reps
        seed = lab_seed(2, k)
        res, seed = ab_realization(seed, pbar, 1.0 + (k - 1), total_units; phase = @sprintf("rep %d/%d", k, reps))
        row = compute_row(k, seed, res.s, s_z, res.t_build, res.t_diag)
        push!(rows, row)
        push!(s_per_rep, res.s)
        _pset!(pbar, (1.0 + k) / total_units; sub = "rep $k/$reps done")
        quiet || println(cc("  ↳ ", C_GRY), "rep $k/$reps · D = ", @sprintf("%.4f", row.D),
                " · d_GUE = ", @sprintf("%.4f", row.dGUE))
    end

    phase_begin!(t(:ph_analysis))
    s_pooled = vcat(s_per_rep...)
    pl = compute_row(0, 0, s_pooled, s_z, 0.0, 0.0)
    v = composite_verdict(pl.D, pl.p, pl.dGUE, pl.dPois, pl.plateau)
    out = mad_outliers([r.D for r in rows])
    rows = [RealizationRow(r.idx, r.seed, r.nspac, r.D, r.p, r.dGUE, r.dPois, r.plateau, r.banddev,
                           r.tbuild, r.tdiag, out.flags[i]) for (i, r) in enumerate(rows)]
    # leave-one-out pooled D (realization-17 style forensics)
    loo_D = Float64[]
    for i in 1:reps
        s_loo = vcat([j == i ? Float64[] : s_per_rep[j] for j in 1:reps]...)
        push!(loo_D, ks_two(s_loo, s_z)[1])
    end
    phase_end!(t(:ph_analysis))
    quiet || pbar_finish!(pbar, "· " * t(:done))

    # ensemble stability
    Ds = [r.D for r in rows]
    med = out.med
    iqr = quantile(Ds, 0.75) - quantile(Ds, 0.25)
    nout = count(out.flags)
    stable = (iqr < 0.02) && (nout <= 2)
    loo_spread = maximum(loo_D) - minimum(loo_D)

    # ---- console summary
    println()
    lab_table_header(_ROW_COLS, _ROW_W)
    foreach(print_row, rows)
    lab_table_footer((top = "", mid = "", bot = "└" * join(("─"^w for w in _ROW_W), "┴") * "┘"))
    print_pooled(pl)
    println()
    println(cc("  " * t(:ensemble_header), C_B))
    @printf(stdout, "    median D = %.4f · IQR = %.4f · min = %.4f · max = %.4f · MAD-outliers = %d\n",
            med, iqr, minimum(Ds), maximum(Ds), nout)
    st_mark = stable ? cc("[OK] " * t(:ens_stable), C_GRN) : cc("[!!] " * t(:ens_unstable), C_YLW)
    println("    ", st_mark)
    print_verdict(v)

    # ---- plots
    rundir = parent_dir !== nothing ? mkpath(parent_dir) : lab_new_run_dir(2)
    phase_begin!(t(:ph_plots))
    if LAB.plots_on
        println(cc("  " * t(:plots_rendering), C_GRY))
        u_ab = cumsum(s_pooled)
        u_z  = cumsum(s_z)
        cen_ab, R2ab = pair_correlation(u_ab)
        cen_z,  R2z  = pair_correlation(u_z)
        note = "pooled $reps realizations · $(length(s_pooled)) AB spacings vs $(length(s_z)) zeta spacings"
        plot_R2_comparison(joinpath(rundir, "plot_01_R2_comparison.png"), cen_ab, R2ab, cen_z, R2z;
                           mode = "MODE 2 HARDCORE", note = note)
        plot_D_distribution(joinpath(rundir, "plot_02_D_per_realization.png"), Ds;
                            mode = "MODE 2 HARDCORE", note = "ensemble of $reps", flagged = out.flags)
        plot_pdf_spacings(joinpath(rundir, "plot_03_spacing_pdf.png"), s_pooled, s_z;
                          mode = "MODE 2 HARDCORE", note = note)
        plot_cdf_compare(joinpath(rundir, "plot_04_cdf.png"), s_pooled, s_z;
                         mode = "MODE 2 HARDCORE", note = note)
        write_csv_r2(rundir, cen_ab, R2ab, cen_z, R2z)
        write_csv_spacings(rundir, s_pooled, s_z)
    end
    phase_end!(t(:ph_plots))

    notes = [t(:n_mode2_note1), t(:n_mode2_note2)]
    if any(out.flags)
        push!(notes, t(:n_mode2_outliers) * " " * string(findall(out.flags)))
    end
    rep = RunReport(2, t(:m2_name), rundir, (v.pass, v.c1, v.c2, v.c3), pl, rows, notes,
                    Pair{String,String}[
                        "ensemble median D" => @sprintf("%.4f", med),
                        "ensemble IQR" => @sprintf("%.4f", iqr),
                        "leave-one-out D range" => @sprintf("%.4f .. %.4f (spread %.4f)", minimum(loo_D), maximum(loo_D), loo_spread),
                        "MAD outliers" => string(findall(out.flags)),
                        "ensemble stability" => (stable ? "STABLE" : "UNSTABLE"),
                    ])
    write_csv_realizations(rundir, rows)
    write_config_json(rundir, 2)
    write_report_md(rep)
    write_report_html(rep)
    quiet || mode_footer(rep, run_t0)
    return rep
end
# =============================================================================
# MODE 3 — DEEP DIAGNOSTICS (stability lab)
# =============================================================================

function _ecdf_at(s_sorted::Vector{Float64}, sg::Float64)
    n = length(s_sorted)
    n == 0 && return 0.0
    return searchsortedlast(s_sorted, sg) / n
end

function run_mode3(; seeds::Int = LAB.reps3seeds, parent_dir::Union{Nothing,String} = nothing,
                   quiet::Bool = false, zeta::Union{Nothing,Vector{Float64}} = nothing)
    ensure_zeros!() || return nothing
    run_t0 = time()
    phases_reset!()
    quiet || mode_header(3, t(:m3_name), t(:m3_sub))
    quiet || matrix_size_banner(quiet)
    Ls_full = geom_scaling_Ls(GEOM[], LAB.L)
    nL = length(Ls_full)
    total_units = 1.0 + 1.0 + seeds + nL + 0.3
    pbar = PBar(28)
    quiet || pbar_start!(pbar, "MODE3")

    # ---- (a) zeta + main realization
    if zeta !== nothing
        s_z = zeta
    else
        gammas, s_z = load_zeta_data!(quiet ? nothing : pbar; units_done = 0.0,
                                      units_total = total_units, weight = 1.0)
    end
    seed_main = lab_seed(3, 0)
    res_main, seed_main = ab_realization(seed_main, pbar, 1.0, total_units; phase = "main rep")
    row_main = compute_row(1, seed_main, res_main.s, s_z, res_main.t_build, res_main.t_diag)
    v_main = composite_verdict(row_main.D, row_main.p, row_main.dGUE, row_main.dPois, row_main.plateau)

    # ---- (b) CDF differential + short-range + bootstrap (reuse main rep)
    phase_begin!(t(:ph_cdf_diff))
    sab_sorted = sort(res_main.s)
    sz_sorted  = sort(s_z)
    sg = collect(0.0:0.01:3.0)
    Fab = [_ecdf_at(sab_sorted, s) for s in sg]
    Fz  = [_ecdf_at(sz_sorted, s) for s in sg]
    dsigned = Fab .- Fz
    dabs = abs.(dsigned)
    imax = argmax(dabs)
    ci = bootstrap_D_ci(res_main.s, gue_cdf; B = 300, seed = lab_seed(3, 99))
    phase_end!(t(:ph_cdf_diff))
    _pset!(pbar, (2.0 + seeds) / total_units; sub = "cdf differential done")

    # ---- (c) seed forensics: same params, different seeds
    phase_begin!(t(:ph_seed_forensics))
    rows_seeds = RealizationRow[]
    for k in 1:seeds
        seed = lab_seed(3, 100 + k)
        res, seed = ab_realization(seed, pbar, 2.0 + (k - 1), total_units; phase = @sprintf("seed %d/%d", k, seeds))
        push!(rows_seeds, compute_row(k, seed, res.s, s_z, res.t_build, res.t_diag))
    end
    phase_end!(t(:ph_seed_forensics))
    Ds_seeds = [r.D for r in rows_seeds]
    out_seeds = mad_outliers(Ds_seeds)
    seed_spread = maximum(Ds_seeds) - minimum(Ds_seeds)

    # ---- (d) lattice finite-size scaling (geometry-adapted; with the v1.3
    #          stretch the Hurwitz groups scale too — skipped only when
    #          autoscale OFF pins them to the fixed |G|)
    phase_begin!(t(:ph_lattice_scaling))
    Ls = Ls_full
    Ds_L = Float64[]
    Lsave = LAB.L
    for (iL, L) in enumerate(Ls)
        LAB.L = L
        seed = lab_seed(3, 200 + iL)
        res, seed = ab_realization(seed, pbar, 2.0 + seeds + (iL - 1), total_units;
                                   phase = @sprintf("L=%d", L))
        row = compute_row(iL, seed, res.s, s_z, res.t_build, res.t_diag)
        push!(Ds_L, row.D)
    end
    LAB.L = Lsave
    phase_end!(t(:ph_lattice_scaling))
    _pset!(pbar, 0.99; sub = "reports")
    quiet || pbar_finish!(pbar, "· " * t(:done))

    # ---- console summary
    println()
    println(cc("  " * t(:m3_main_header), C_B))
    @printf(stdout, "    D = %.4f · p = %.2e · d_GUE = %.4f · d_Pois = %.4f · plateau = %.4f\n",
            row_main.D, row_main.p, row_main.dGUE, row_main.dPois, row_main.plateau)
    print_verdict(v_main)
    println()
    println(cc("  " * t(:m3_cdf_header), C_B))
    @printf(stdout, "    max |F_AB - F_zeta| = %.4f at s* = %.2f  (signed: %+.4f)\n",
            dabs[imax], sg[imax], dsigned[imax])
    @printf(stdout, "    bootstrap 95%% CI of D vs GUE: [%.4f, %.4f] (mean %.4f)\n", ci.lo, ci.hi, ci.mean)
    println()
    println(cc("  " * t(:m3_seed_header), C_B))
    lab_table_header(["#", "seed", "D", "d_GUE", "d_Pois", "plateau", "flag"], [4, 13, 8, 8, 8, 9, 7])
    for (i, r) in enumerate(rows_seeds)
        lab_table_row([@sprintf("%d", r.idx), length(string(r.seed)) > 8 ? string(r.seed)[end-7:end] : string(r.seed), @sprintf("%.4f", r.D),
                       @sprintf("%.4f", r.dGUE), @sprintf("%.4f", r.dPois),
                       @sprintf("%.4f", r.plateau), out_seeds.flags[i] ? "OUT" : "-"],
                      [4, 13, 8, 8, 8, 9, 7])
    end
    lab_table_footer((top = "", mid = "", bot = "└" * join(("─"^w for w in [4, 13, 8, 8, 8, 9, 7]), "┴") * "┘"))
    @printf(stdout, "    seed spread of D = %.4f\n", seed_spread)
    println()
    if isempty(Ls)
        println(cc("  " * t(:m3_scaling_header), C_B))
        println(cc("    (skipped: stretch is OFF — " * String(GEOM[].id) * " stays at |G| = " *
                   string(GEOM[].aut_order) * " sites; enable autoscale to stretch)", C_GRY))
    else
        println(cc("  " * t(:m3_scaling_header), C_B))
        for (L, D) in zip(Ls, Ds_L)
            @printf(stdout, "    L = %3d  ->  D = %.4f\n", L, D)
        end
        trend = length(Ls) == 3 && Ds_L[1] > Ds_L[end] ? t(:m3_trend_down) : t(:m3_trend_flat)
        println("    ", trend)
    end

    # ---- plots
    rundir = parent_dir !== nothing ? mkpath(parent_dir) : lab_new_run_dir(3)
    phase_begin!(t(:ph_plots))
    if LAB.plots_on
        println(cc("  " * t(:plots_rendering), C_GRY))
        u_ab = cumsum(res_main.s); u_z = cumsum(s_z)
        cen_ab, R2ab = pair_correlation(u_ab)
        cen_z,  R2z  = pair_correlation(u_z)
        note = "single realization · $(length(res_main.s)) AB spacings vs $(length(s_z)) zeta"
        plot_cdf_differential(joinpath(rundir, "plot_01_cdf_differential.png"), sg, dabs, dsigned;
                              mode = "MODE 3 DEEP DIAG", note = note)
        plot_shortrange(joinpath(rundir, "plot_02_short_range.png"), cen_ab, R2ab, cen_z, R2z;
                        mode = "MODE 3 DEEP DIAG", note = note)
        plot_seed_forensics(joinpath(rundir, "plot_03_seed_forensics.png"), Ds_seeds,
                            [string(r.seed) for r in rows_seeds];
                            mode = "MODE 3 DEEP DIAG", note = "same params, $seeds seeds")
        isempty(Ls) || plot_lattice_scaling(joinpath(rundir, "plot_04_lattice_scaling.png"), float.(Ls), Ds_L;
                             mode = "MODE 3 DEEP DIAG", note = "finite-size probe")
        plot_bootstrap(joinpath(rundir, "plot_05_bootstrap.png"), ci.samples;
                       mode = "MODE 3 DEEP DIAG", note = @sprintf("D vs GUE, 300 resamples, 95%% CI [%.4f, %.4f]", ci.lo, ci.hi))
        plot_cdf_compare(joinpath(rundir, "plot_06_cdf.png"), res_main.s, s_z;
                         mode = "MODE 3 DEEP DIAG", note = note)
        write_csv_r2(rundir, cen_ab, R2ab, cen_z, R2z)
        open(joinpath(rundir, "data_cdf_differential.csv"), "w") do io
            println(io, "s,F_AB,F_zeta,signed,abs")
            for i in eachindex(sg)
                @printf(io, "%.2f,%.6f,%.6f,%+.6f,%.6f\n", sg[i], Fab[i], Fz[i], dsigned[i], dabs[i])
            end
        end
    end
    phase_end!(t(:ph_plots))

    main_row = RealizationRow(1, seed_main, row_main.nspac, row_main.D, row_main.p, row_main.dGUE,
                              row_main.dPois, row_main.plateau, row_main.banddev,
                              row_main.tbuild, row_main.tdiag, false)
    rep = RunReport(3, t(:m3_name), rundir, (v_main.pass, v_main.c1, v_main.c2, v_main.c3),
                    main_row, rows_seeds,
                    [t(:n_mode3_note1), t(:n_mode3_note2), isempty(Ls) ? "lattice scaling skipped (fixed-size Cayley geometry)" : trend],
                    Pair{String,String}[
                        "max |F_AB - F_zeta|" => @sprintf("%.4f at s* = %.2f", dabs[imax], sg[imax]),
                        "bootstrap CI D vs GUE" => @sprintf("[%.4f, %.4f]", ci.lo, ci.hi),
                        "seed spread of D" => @sprintf("%.4f", seed_spread),
                        "lattice scaling" => isempty(Ls) ? "-" :
                            join((@sprintf("L=%d: %.4f", L, D) for (L, D) in zip(Ls, Ds_L)), " - "),
                    ])
    write_csv_realizations(rundir, rows_seeds)
    write_config_json(rundir, 3)
    write_report_md(rep)
    write_report_html(rep)
    quiet || mode_footer(rep, run_t0)
    return rep
end

# =============================================================================
# MODE 4 — VORTEX CONFIGURATOR (parameter sweep + stabilization map)
# =============================================================================

sweep_grid(param::Symbol) =
    param === :Nv ? collect(0.0:1.0:6.0) :
    param === :q  ? collect(0.25:0.25:3.0) :
    param === :W  ? collect(0.0:0.25:2.5) :
                    collect(0.0:0.05:1.0)

function _set_sweep_param!(param::Symbol, v::Float64)
    param === :Nv ? (LAB.Nv = clamp(round(Int, v), 0, 16)) :
    param === :q  ? (LAB.q = v) :
    param === :W  ? (LAB.W = v) :
                    (LAB.alpha = v)
    nothing
end

_get_sweep_param(param::Symbol) =
    param === :Nv ? Float64(LAB.Nv) :
    param === :q  ? LAB.q :
    param === :W  ? LAB.W :
                    LAB.alpha

function run_mode4(; param::Symbol = LAB.sweep_param, reps::Int = LAB.reps4,
                   grid::Union{Nothing,Vector{Float64}} = nothing,
                   parent_dir::Union{Nothing,String} = nothing,
                   quiet::Bool = false, zeta::Union{Nothing,Vector{Float64}} = nothing)
    ensure_zeros!() || return nothing
    run_t0 = time()
    phases_reset!()
    param in (:alpha, :Nv, :q, :W) || (param = :alpha)
    LAB.sweep_param = param
    grid = grid === nothing ? sweep_grid(param) : grid
    quiet || mode_header(4, t(:m4_name), t(:m4_sub) * " ($(String(param)), $(length(grid)) points x $reps)")
    quiet || matrix_size_banner(quiet)
    quiet || println(cc("  ", C_YLW), cc(t(:m4_disclaimer), C_YLW))
    total_units = 1.0 + length(grid) * reps
    pbar = PBar(28)
    quiet || pbar_start!(pbar, "MODE4")

    if zeta !== nothing
        s_z = zeta
    else
        gammas, s_z = load_zeta_data!(quiet ? nothing : pbar; units_done = 0.0,
                                      units_total = total_units, weight = 1.0)
    end

    vsave = _get_sweep_param(param)
    xs = Float64[]; Dm = Float64[]; dGs = Float64[]; dPs = Float64[]; pls = Float64[]; bds = Float64[]
    curves = Vector{Tuple{String,Vector{Float64},Vector{Float64},Tuple{Int,Int,Int}}}()
    curve_colors = (COL_AB, COL_PURPLE, COL_CYAN, COL_PINK)

    println()
    cols4 = ["x", "D", "d_GUE", "d_Pois", "plateau", "|R2-GUE|", "zone"]
    w4 = [8, 8, 8, 8, 9, 9, 6]
    lab_table_header(cols4, w4)
    for (ip, xv) in enumerate(grid)
        accD = 0.0; accG = 0.0; accP = 0.0; accL = 0.0; accB = 0.0
        best_curve = nothing
        for k in 1:reps
            _set_sweep_param!(param, xv)
            seed = lab_seed(4, ip * 97 + k)
            res, seed = ab_realization(seed, pbar, 1.0 + (ip - 1) * reps + (k - 1), total_units;
                                       phase = @sprintf("%s=%.3f [%d/%d]", String(param), xv, ip, length(grid)))
            row = compute_row(ip, seed, res.s, s_z, res.t_build, res.t_diag)
            accD += row.D; accG += row.dGUE; accP += row.dPois; accL += row.plateau; accB += row.banddev
            best_curve = res.s
        end
        mD = accD / reps; mG = accG / reps; mP = accP / reps; mL = accL / reps; mB = accB / reps
        push!(xs, xv); push!(Dm, mD); push!(dGs, mG); push!(dPs, mP); push!(pls, mL); push!(bds, mB)
        gold = (mD < 0.10) && (mG < mP) && (0.75 <= mL <= 1.25)
        lab_table_row([@sprintf("%.3f", xv), @sprintf("%.4f", mD), @sprintf("%.4f", mG),
                       @sprintf("%.4f", mP), @sprintf("%.4f", mL), @sprintf("%.4f", mB),
                       gold ? cc("GOLD", C_YLW, C_B) : "-"], w4)
        if length(curves) < 4 && best_curve !== nothing && gold
            cen, R2 = pair_correlation(cumsum(best_curve))
            push!(curves, (@sprintf("%s=%.2f", String(param), xv), cen, R2,
                           curve_colors[min(length(curves) + 1, end)]))
        end
    end
    lab_table_footer((top = "", mid = "", bot = "└" * join(("─"^w for w in w4), "┴") * "┘"))
    _set_sweep_param!(param, vsave)

    phase_begin!(t(:ph_analysis))
    goldmask = [(Dm[i] < 0.10) && (dGs[i] < dPs[i]) && (0.75 <= pls[i] <= 1.25) for i in eachindex(xs)]
    # per-point rows for the report / MODE 5 absorption
    rows4 = [RealizationRow(i, 0, 0, Dm[i], NaN, dGs[i], dPs[i], pls[i], bds[i], 0.0, 0.0, false)
             for i in eachindex(xs)]
    # crossover: first index from which dG < dP holds for 2 consecutive points
    xstar = nothing
    for i in 1:(length(xs) - 1)
        if dGs[i] < dPs[i] && dGs[i+1] < dPs[i+1]
            # linear interpolation of sign change before i (if any)
            if i > 1 && dGs[i-1] >= dPs[i-1]
                g1 = dGs[i-1] - dPs[i-1]; g2 = dGs[i] - dPs[i]
                xstar = xs[i-1] + (xs[i] - xs[i-1]) * (-g1) / (g2 - g1)
            else
                xstar = xs[i]
            end
            break
        end
    end
    ibest = argmin(Dm)
    phase_end!(t(:ph_analysis))
    quiet || pbar_finish!(pbar, "· " * t(:done))

    println()
    println(cc("  " * t(:m4_result_header), C_B))
    if any(goldmask)
        @printf(stdout, "    %s: %s\n", t(:m4_gold_points), join([@sprintf("%.3f", xs[i]) for i in findall(goldmask)], ", "))
    else
        println("    ", t(:m4_no_gold))
    end
    xstar !== nothing && @printf(stdout, "    %s ≈ %.4f\n", t(:m4_crossover), xstar)
    @printf(stdout, "    %s: %s = %.3f (D = %.4f)\n", t(:m4_best), String(param), xs[ibest], Dm[ibest])

    # ---- plots
    rundir = parent_dir !== nothing ? mkpath(parent_dir) : lab_new_run_dir(4)
    phase_begin!(t(:ph_plots))
    if LAB.plots_on
        println(cc("  " * t(:plots_rendering), C_GRY))
        note = "sweep $(String(param)) · $(length(grid)) points x $reps · L=$(LAB.L)"
        plot_stability_map(joinpath(rundir, "plot_01_stability_map.png"), xs, Dm, dGs, dPs,
                           goldmask, xstar, String(param), "MODE 4 CONFIGURATOR";
                           note = note, plabel = String(param))
        if !isempty(curves)
            plot_R2_evolution(joinpath(rundir, "plot_02_R2_evolution.png"), curves;
                              mode = "MODE 4 CONFIGURATOR", note = note)
        end
    end
    phase_end!(t(:ph_plots))
    # sweep data are written regardless of the plots switch (they are data, not plots)
    open(joinpath(rundir, "data_sweep.csv"), "w") do io
        println(io, "$(String(param)),D,d_GUE,d_Pois,plateau,band_dev,gold")
        for i in eachindex(xs)
            @printf(io, "%.4f,%.6f,%.6f,%.6f,%.6f,%.6f,%s\n",
                    xs[i], Dm[i], dGs[i], dPs[i], pls[i], bds[i], goldmask[i] ? "yes" : "no")
        end
    end

    rep = RunReport(4, t(:m4_name), rundir, (any(goldmask), true, any(goldmask), any(goldmask)),
                    nothing, rows4,
                    [t(:n_mode4_note1), t(:n_mode4_note2), t(:m4_disclaimer)],
                    Pair{String,String}[
                        "swept parameter" => String(param),
                        "grid" => @sprintf("%d points, %.3f .. %.3f", length(grid), xs[1], xs[end]),
                        "stabilization points" => (any(goldmask) ?
                            join((@sprintf("%.3f", xs[i]) for i in findall(goldmask)), ", ") : "none"),
                        "best point" => @sprintf("%s = %.3f (D = %.4f)", String(param), xs[ibest], Dm[ibest]),
                        "crossover" => (xstar === nothing ? "-" : @sprintf("%.4f", xstar)),
                    ])
    write_config_json(rundir, 4)
    write_report_md(rep)
    write_report_html(rep)
    quiet || mode_footer(rep, run_t0)
    return rep
end
# =============================================================================
# MODE 5 — UNIVERSAL GEOMETRY SWEEP: all geometries x tests 1-4 x reps
# (light pass: reduced realizations, cached zeta, per-subrun data without plots)
# =============================================================================

const _CLI_GEOMS = Ref{Union{Nothing,Vector{GeometrySpec}}}(nothing)   # --geoms=a,b,c

struct UniversalRow
    geo      :: String
    group    :: String
    genus    :: Int
    test     :: Int
    testname :: String
    rep      :: Int          # 0 = pooled over the reps of this subtest
    seed     :: Int
    nspac    :: Int
    D        :: Float64
    p        :: Float64
    dGUE     :: Float64
    dPois    :: Float64
    plateau  :: Float64
    pass     :: Bool
    tbuild   :: Float64
    tdiag    :: Float64
end

function write_csv_universal(rundir, rows::Vector{UniversalRow})
    path = joinpath(rundir, "data_universal.csv")
    open(path, "w") do io
        println(io, "geometry,group,genus,test,test_name,rep,seed,n_spacings,D,p,d_GUE,d_Pois,plateau,verdict,t_build_s,t_diag_s")
        for r in rows
            @printf(io, "%s,%s,%d,%d,%s,%d,%d,%d,%.6f,%.3e,%.6f,%.6f,%.6f,%s,%.2f,%.2f\n",
                    r.geo, replace(r.group, "," => ";"), r.genus, r.test, r.testname, r.rep,
                    r.seed, r.nspac, r.D, r.p, r.dGUE, r.dPois, r.plateau,
                    r.pass ? "PASS" : "FAIL", r.tbuild, r.tdiag)
        end
    end
    return path
end

function _m5_absorb!(rows_u::Vector{UniversalRow}, geo::GeometrySpec, test::Int,
                     testname::String, rep::RunReport)
    pass = rep.verdict[1]
    if rep.pooled !== nothing
        pl = rep.pooled
        push!(rows_u, UniversalRow(String(geo.id), geo.group, geo.genus, test, testname, 0, 0,
                                   pl.nspac, pl.D, pl.p, pl.dGUE, pl.dPois, pl.plateau, pass,
                                   pl.tbuild, pl.tdiag))
    elseif !isempty(rep.rows)
        # MODE 4 has no pooled row — synthesize one as the mean over sweep points
        push!(rows_u, UniversalRow(String(geo.id), geo.group, geo.genus, test, testname, 0, 0,
                                   0, mean(r.D for r in rep.rows), NaN,
                                   mean(r.dGUE for r in rep.rows),
                                   mean(r.dPois for r in rep.rows),
                                   mean(r.plateau for r in rep.rows), pass, 0.0, 0.0))
    end
    for r in rep.rows
        push!(rows_u, UniversalRow(String(geo.id), geo.group, geo.genus, test, testname, r.idx,
                                   r.seed, r.nspac, r.D, r.p, r.dGUE, r.dPois, r.plateau, pass,
                                   r.tbuild, r.tdiag))
    end
end

const _M5_TESTCOLORS = (COL_AB, COL_PURPLE, COL_CYAN, COL_ORANGE)
_m5_shortname(geo::GeometrySpec) =
    geo.model === :cayley ? "PSL(2,$(geo.q_field))" :
    geo.id === :cubic     ? "cube" : String(geo.id)

function plot_universal_summary(path, geoms::Vector{GeometrySpec}, rows_u::Vector{UniversalRow};
                                note = "")
    ng = length(geoms)
    Dm = fill(NaN, ng, 4)
    Pm = fill(false, ng, 4)
    for r in rows_u
        r.rep == 0 || continue
        ig = findfirst(g -> String(g.id) == r.geo, geoms)
        ig === nothing && continue
        1 <= r.test <= 4 || continue
        Dm[ig, r.test] = r.D
        Pm[ig, r.test] = r.pass
    end
    validD = filter(!isnan, Dm)
    ymax = max(0.30, 1.08 * (isempty(validD) ? 0.3 : maximum(validD)))
    p = Plot2D("Test 34 · MODE 5 — universal geometry sweep"; sub = note)
    set_xlim!(p, 0.5, ng + 0.5)
    set_ylim!(p, 0.0, ymax)
    frame!(p; xlab = "", ylab = "pooled D (two-sample KS vs zeta)")
    gridlines!(p)
    for t in 1:4
        firstpush = true
        for ig in 1:ng
            v = Dm[ig, t]
            isnan(v) && continue
            xc = ig + (t - 2.5) * 0.21
            x0 = Xmap(p, xc - 0.09); x1 = Xmap(p, xc + 0.09)
            yv = Ymap(p, v); yb = Ymap(p, 0.0)
            col = Pm[ig, t] ? _M5_TESTCOLORS[t] : COL_RED
            fill_rect!(p.c, x0, yv, x1, yb, col, 0.9)
            firstpush && push!(p.legend, ("test $t", _M5_TESTCOLORS[t], :bar))
            firstpush = false
        end
    end
    hline_data!(p, 0.10, COL_RED; label = "D < 0.10 gate")
    for (ig, g) in enumerate(geoms)
        text!(p.c, Xmap(p, ig), p.py1 + 30, _m5_shortname(g), COL_INK; scale = 3, align = :center)
    end
    footer!(p, "red bar = subtest failed the composite verdict · " * plot_footer("MODE 5 UNIVERSAL"))
    save!(p, path)
    nothing
end

function write_report_universal(rundir, rows_u::Vector{UniversalRow}, reps::Int,
                                geoms::Vector{GeometrySpec}, total_secs::Float64)
    path = joinpath(rundir, "FINAL_REPORT.md")
    pooled = filter(r -> r.rep == 0, rows_u)
    npass = count(r -> r.pass, pooled)
    open(path, "w") do io
        println(io, "# Test 34 — MODE 5 · UNIVERSAL GEOMETRY REPORT")
        println(io)
        @printf(io, "**Run:** `%s` · **reps per test:** %d · **generated:** %s\n\n",
                LAB_RUN_ID[], reps, Dates.format(Dates.now(), "yyyy-mm-dd HH:MM:SS"))
        println(io, "## Geometry registry")
        println(io)
        println(io, "| # | geometry | group | genus | χ | orientable | sites | Hurwitz |")
        println(io, "|---|---|---|---|---|---|---|---|")
        for (i, g) in enumerate(geoms)
            Le, _ = geom_L_eff(g, LAB.L)
            @printf(io, "| %d | %s | %s | %d | %d | %s | %d | %s |\n", i, g.name, g.group,
                    g.genus, g.chi, g.orientable ? "yes" : "no", geom_nsites(g, Le),
                    g.hurwitz ? "**yes** (|Aut| = $(g.aut_order) = 84(g-1))" : "-")
        end
        println(io)
        println(io, "## Pooled verdicts (geometry × test, $reps realizations each)")
        println(io)
        println(io, "| geometry | test | spacings | D | d_GUE | d_Pois | plateau | verdict |")
        println(io, "|---|---|---|---|---|---|---|---|")
        for r in pooled
            @printf(io, "| %s | %d %s | %d | %.4f | %.4f | %.4f | %.4f | %s |\n",
                    r.geo, r.test, r.testname, r.nspac, r.D, r.dGUE, r.dPois, r.plateau,
                    r.pass ? "**PASS**" : "FAIL")
        end
        println(io)
        println(io, "## Universal verdict")
        println(io)
        @printf(io, "%s **%d / %d** geometry×test subtests GUE-consistent\n\n",
                _boolmark(npass == length(pooled)), npass, length(pooled))
        println(io, "Composite criterion per subtest: (p > 0.01 OR D < 0.10) AND d_GUE < d_Pois AND 0.75 <= plateau <= 1.25, pooled over $reps realizations.")
        println(io)
        println(io, "## Notes")
        println(io)
        println(io, " - Light universal pass: $reps realizations per (geometry, test), zeta loaded once, window widened to min 0.70 for small groups, sub-run plots off (data CSVs are always written).")
        println(io, " - Per-subtest full reports: FINAL_REPORT.md / index.html / data_*.csv in each test subdirectory.")
        println(io, " - Hurwitz surfaces are magnetic Cayley graphs Cay(PSL(2,q); B, C), ord B = 3, ord C = 7; heptagon flux = 2·pi·q·alpha·Nv.")
        println(io)
        println(io, "## Files")
        println(io)
        for f in sort(readdir(rundir))
            println(io, " - `$f`")
        end
        println(io)
        println(io, "## Timing")
        println(io)
        println(io, " - **TOTAL**: ", fmt_sec(total_secs))
    end
    return path
end

function write_report_universal_html(rundir, rows_u::Vector{UniversalRow}, reps::Int,
                                     geoms::Vector{GeometrySpec}, total_secs::Float64)
    path = joinpath(rundir, "index.html")
    pooled = filter(r -> r.rep == 0, rows_u)
    npass = count(r -> r.pass, pooled)
    open(path, "w") do io
        println(io, "<!DOCTYPE html><html><head><meta charset='utf-8'>")
        println(io, "<title>Test 34 — MODE 5 universal — ", LAB_RUN_ID[], "</title>")
        println(io, "<style>", _HTML_CSS, "</style></head><body>")
        println(io, "<header><h1>TEST 34 · MODE 5 — UNIVERSAL GEOMETRY SWEEP</h1>")
        println(io, "<div class='meta'>run ", LAB_RUN_ID[], " · ", Dates.format(Dates.now(), "yyyy-mm-dd HH:MM:SS"),
                " · Julia ", VERSION, " · threads ", Threads.nthreads(), "</div></header><main>")
        allpass = npass == length(pooled)
        println(io, "<div class='verdict ", allpass ? "ok" : "bad", "'>UNIVERSAL VERDICT: ",
                npass, " / ", length(pooled), " geometry×test subtests GUE-consistent</div>")
        println(io, "<h2>Geometry registry</h2><table><tr><th>#</th><th>geometry</th><th>group</th><th>genus</th><th>χ</th><th>sites</th><th>Hurwitz</th></tr>")
        for (i, g) in enumerate(geoms)
            Le, _ = geom_L_eff(g, LAB.L)
            println(io, "<tr><td>", i, "</td><td>", g.name, "</td><td>", g.group, "</td><td>",
                    g.genus, "</td><td>", g.chi, "</td><td>", geom_nsites(g, Le), "</td><td>",
                    g.hurwitz ? "<b>yes (|Aut| = $(g.aut_order))</b>" : "-", "</td></tr>")
        end
        println(io, "</table>")
        println(io, "<h2>Pooled verdicts ($reps reps per subtest)</h2><table><tr><th>geometry</th><th>test</th><th>spacings</th><th>D</th><th>d_GUE</th><th>d_Pois</th><th>plateau</th><th>verdict</th></tr>")
        for r in pooled
            println(io, "<tr><td>", r.geo, "</td><td>", r.test, " ", r.testname, "</td><td>",
                    r.nspac, "</td><td>", @sprintf("%.4f", r.D), "</td><td>",
                    @sprintf("%.4f", r.dGUE), "</td><td>", @sprintf("%.4f", r.dPois), "</td><td>",
                    @sprintf("%.4f", r.plateau), "</td><td>",
                    r.pass ? "<b style='color:#2a5'>PASS</b>" : "<b style='color:#c33'>FAIL</b>",
                    "</td></tr>")
        end
        println(io, "</table>")
        println(io, "<h2>Plots</h2>")
        for f in sort(readdir(rundir))
            endswith(f, ".png") && println(io, "<img src='", f, "' alt='", f, "'>")
        end
        println(io, "<h2>Timing</h2><p>TOTAL: ", fmt_sec(total_secs), "</p>")
        println(io, "</main><footer>finite-size_lab.jl · MODE 5 universal geometry sweep · AB-cloud vs Riemann zeros on every surface</footer>")
        println(io, "</body></html>")
    end
    return path
end

"""
MODE 5 — UNIVERSAL GEOMETRY SWEEP.

Runs the light configuration of tests 1-4 (default 3 realizations each) on
EVERY geometry of the registry (or the --geoms=... subset), reuses one zeta
load for the whole sweep, and produces:
  data_universal.csv        — one row per (geometry, test, realization) + pooled
  FINAL_REPORT.md / index.html / plot_05_universal_summary.png / config.json
  <geo>/test<k>_<name>/     — full per-subtest reports (plots off, data on)
The lab configuration is snapshotted and restored, so MODE 5 leaves no trace
on the interactive settings.
"""
function run_mode5(; reps::Int = LAB.reps5,
                   geoms::Vector{GeometrySpec} = _CLI_GEOMS[] === nothing ?
                                               GEOMETRY_LIST : _CLI_GEOMS[])
    isempty(geoms) && (geoms = GEOMETRY_LIST)
    ensure_zeros!() || return nothing
    run_t0 = time()
    phases_reset!()
    mode_header(5, t(:m5_name), t(:m5_sub) * " · $(length(geoms)) geometries x 4 tests x $reps reps")
    rundir = lab_new_run_dir(5)
    println(cc("  " * t(:out_dir) * ": ", C_B), rundir)
    testnames = Dict(1 => "NORMAL", 2 => "HARDCORE", 3 => "DEEP-DIAG", 4 => "CONFIG")

    # ---- snapshot & light configuration
    saved = (L = LAB.L, Nv = LAB.Nv, alpha = LAB.alpha, q = LAB.q, W = LAB.W,
             window_frac = LAB.window_frac, reps1 = LAB.reps1, reps2 = LAB.reps2,
             reps3seeds = LAB.reps3seeds, reps4 = LAB.reps4, sweep_param = LAB.sweep_param,
             plots_on = LAB.plots_on, nchunks = LAB.nchunks, geo = GEOM[].id)
    LAB.plots_on = false                       # sub-runs: data only, one summary PNG at the end
    LAB.window_frac = max(LAB.window_frac, 0.70)  # small Hurwitz groups need a wider window
    LAB.nchunks = min(LAB.nchunks, 4)

    rows_u = UniversalRow[]
    try
        gammas, s_z = load_zeta_data!(nothing)   # one zeta load for the whole sweep
        ngeo = length(geoms)
        for (ig, geo) in enumerate(geoms)
            GEOM[] = geo
            Le, clamped = geom_L_eff(geo, saved.L)
            LAB.L = Le
            println()
            println(cc("  ▶ [$ig/$ngeo] " * geometry_label(geo, saved.L), C_B, C_CYN))
            clamped && println(cc("    (L=$(saved.L) adjusted to $Le for this geometry)", C_GRY))
            geodir = mkpath(joinpath(rundir, @sprintf("%02d_%s", ig, String(geo.id))))
            rep1 = run_mode1(reps = reps, parent_dir = joinpath(geodir, "test1_normal"),
                             quiet = true, zeta = s_z)
            rep1 === nothing || _m5_absorb!(rows_u, geo, 1, testnames[1], rep1)
            rep2 = run_mode2(reps = reps, parent_dir = joinpath(geodir, "test2_hardcore"),
                             quiet = true, zeta = s_z)
            rep2 === nothing || _m5_absorb!(rows_u, geo, 2, testnames[2], rep2)
            rep3 = run_mode3(seeds = reps, parent_dir = joinpath(geodir, "test3_deepdiag"),
                             quiet = true, zeta = s_z)
            rep3 === nothing || _m5_absorb!(rows_u, geo, 3, testnames[3], rep3)
            rep4 = run_mode4(param = :alpha, reps = reps,
                             grid = [0.2, 0.4, 0.6, 0.8],
                             parent_dir = joinpath(geodir, "test4_config"),
                             quiet = true, zeta = s_z)
            rep4 === nothing || _m5_absorb!(rows_u, geo, 4, testnames[4], rep4)
        end
    finally
        # ---- restore the lab configuration (including the plots switch!)
        LAB.L = saved.L; LAB.Nv = saved.Nv; LAB.alpha = saved.alpha; LAB.q = saved.q
        LAB.W = saved.W; LAB.window_frac = saved.window_frac
        LAB.reps1 = saved.reps1; LAB.reps2 = saved.reps2
        LAB.reps3seeds = saved.reps3seeds; LAB.reps4 = saved.reps4
        LAB.sweep_param = saved.sweep_param; LAB.nchunks = saved.nchunks
        LAB.plots_on = saved.plots_on
        GEOM[] = geom_by_id(saved.geo)
    end

    # ---- console summary
    pooled = filter(r -> r.rep == 0, rows_u)
    println()
    println(cc("  " * t(:m5_summary), C_B))
    cols5 = ["geometry", "test", "D(pooled)", "d_GUE", "d_Pois", "plateau", "verdict"]
    w5    = [12, 12, 11, 9, 9, 9, 8]
    lab_table_header(cols5, w5)
    for r in pooled
        lab_table_row([r.geo, @sprintf("%d %s", r.test, r.testname), @sprintf("%.4f", r.D),
                       @sprintf("%.4f", r.dGUE), @sprintf("%.4f", r.dPois),
                       @sprintf("%.4f", r.plateau),
                       r.pass ? cc("PASS", C_GRN, C_B) : cc("FAIL", C_RED, C_B)], w5)
    end
    lab_table_footer((top = "", mid = "", bot = "└" * join(("─"^w for w in w5), "┴") * "┘"))
    npass = count(r -> r.pass, pooled)
    allpass = npass == length(pooled) && !isempty(pooled)
    println()
    println("  ", allpass ? cc("[OK] ", C_GRN, C_B) : cc("[!!] ", C_RED, C_B),
            cc(t(:m5_verdict) * ": ", C_B),
            @sprintf("%d / %d %s", npass, length(pooled), t(:m5_subtests)),
            allpass ? cc(" — " * t(:m5_universal_ok), C_GRN) : cc("", C_YLW))

    # ---- artifacts
    total_secs = time() - run_t0
    write_csv_universal(rundir, rows_u)
    write_config_json(rundir, 5)
    write_report_universal(rundir, rows_u, reps, geoms, total_secs)
    write_report_universal_html(rundir, rows_u, reps, geoms, total_secs)
    if saved.plots_on
        phase_begin!(t(:ph_plots))
        println(cc("  " * t(:plots_rendering), C_GRY))
        plot_universal_summary(joinpath(rundir, "plot_05_universal_summary.png"), geoms, rows_u;
                               note = "$reps reps per (geometry, test) · order: " *
                                      join(_m5_shortname.(geoms), ", "))
        phase_end!(t(:ph_plots))
    end
    println(cc("  " * t(:out_dir) * ": ", C_B), rundir)
    println(cc("  " * t(:report_files) * ": ", C_B),
            "FINAL_REPORT.md · index.html · data_universal.csv · config.json")
    println(cc("  " * t(:timing_total) * ": ", C_B), fmt_sec(total_secs))
    lab_save_settings()
    return rows_u
end

# =============================================================================
# SELFTEST — environment & algorithm checks (also runnable from the menu)
# =============================================================================

function run_selftest()
    run_t0 = time()
    println()
    println(cc("═"^78, C_CYN))
    println(cc("  SELFTEST — environment & algorithm checks", C_B))
    println(cc("═"^78, C_CYN))
    results = Tuple{String,Bool,String}[]

    _check(name::String, ok::Bool, info::String = "") =
        push!(results, (name, ok, info))

    # 1. Julia version
    _check("Julia version >= 1.9", VERSION >= v"1.9", string(VERSION))

    # 2. threads / BLAS
    _check("threads available", Threads.nthreads() >= 1,
           @sprintf("nthreads=%d, BLAS=%d (use julia -t auto for live bar during tridiag)",
                    Threads.nthreads(), BLAS.get_num_threads()))

    # 3. font engine
    try
        _font_init!()
        n_glyphs = length(_FONT)
        ok = n_glyphs >= 60
        _check("bitmap font 5x7", ok, "$n_glyphs glyphs")
    catch e
        _check("bitmap font 5x7", false, sprint(showerror, e))
    end

    # 4. PNG writer
    try
        c = Canvas(1600, 1000)
        fill_rect!(c, 0, 0, 1600, 1000, COL_BG)
        text!(c, 40, 30, "Selftest ABC 0123", COL_INK; scale = 5)
        line!(c, 100.0, 100.0, 1500.0, 900.0, COL_AB, 3.0)
        rundir = joinpath(LAB.out_root, "selftest"); mkpath(rundir)
        f = joinpath(rundir, "selftest_canvas.png")
        save_png(c, f)
        bytes = filesize(f)
        sig_ok = open(f, "r") do io
            b = read(io, 8)
            b[2] == UInt8('P') && b[3] == UInt8('N') && b[4] == UInt8('G')
        end
        _check("PNG writer 1600x1000", sig_ok && bytes > 10000, fmt_bytes(bytes))
    catch e
        _check("PNG writer 1600x1000", false, sprint(showerror, e))
    end

    # 5. statistics sanity: GUE sample vs GUE cdf, Poisson sample vs Poisson cdf
    try
        rng = lab_rng(42)
        gue_sample = Float64[]
        maxpdf = gue_pdf(sqrt(pi) / 2.0)
        while length(gue_sample) < 6000
            s = 3.0 * rand(rng)
            rand(rng) * maxpdf < gue_pdf(s) && push!(gue_sample, s)
        end
        pois_sample = [-log(rand(rng)) for _ in 1:6000]
        normalize!(x) = (x ./= mean(x); x)
        normalize!(gue_sample); normalize!(pois_sample)
        d1 = ks_gue(gue_sample); d2 = ks_pois(pois_sample)
        d12 = ks_gue(pois_sample)
        ok = d1 < 0.04 && d2 < 0.04 && d12 > 0.10
        _check("KS statistics sanity", ok,
               @sprintf("GUE vs GUE: %.4f · Pois vs Pois: %.4f · Pois vs GUE: %.4f", d1, d2, d12))
    catch e
        _check("KS statistics sanity", false, sprint(showerror, e))
    end

    # 6. unfolding sanity: RVM + Patch A on synthetic zeros
    try
        rng = lab_rng(7)
        n = 5000
        # synthetic "zeros": Poisson jitter around RVM flow starting at 14.13
        g = Vector{Float64}(undef, n)
        T = 14.1347
        for i in 1:n
            g[i] = T
            T += 2pi / log(T / (2pi)) * (0.5 + rand(rng))
        end
        s = unfold_zeta(g; patch_a = true)
        ok = abs(mean(s) - 1.0) < 1e-9 && 0.2 < std(s) < 2.0
        _check("zeta unfolding (RVM + Patch A)", ok,
               @sprintf("mean=%.6f std=%.4f (Poisson std would be 1.0)", mean(s), std(s)))
    catch e
        _check("zeta unfolding (RVM + Patch A)", false, sprint(showerror, e))
    end

    # 7. model + chunked diagonalization vs reference eigvals
    try
        L = 24
        H = build_hamiltonian(L, 2, 0.5, 1.0, 1.0, 12345)
        n = L * L
        Her = Hermitian(H)
        ilo = div(n, 2) - 20; ihi = div(n, 2) + 20
        w_ref = eigvals(Her, ilo:ihi)
        _, _, d, e = LAPACK.hetrd!('L', copy(H))
        w_test = LAPACK.stebz!('I', 'B', 0.0, 0.0, ilo, ihi, -1.0, d, e)[1]
        err = maximum(abs.(w_ref .- w_test))
        _check("AB model 24x24 + chunked spectrum", err < 1e-8,
               @sprintf("max |diff| vs eigvals = %.2e", err))
    catch e
        _check("AB model 24x24 + chunked spectrum", false, sprint(showerror, e))
    end

    # 8. plaquette flux check: vortex encloses 2*pi*q*alpha
    try
        L = 16
        H = build_hamiltonian(L, 1, 0.5, 1.0, 0.0, 999)
        n = L * L
        w = eigvals(Hermitian(H))
        _check("Hamiltonian Hermitian & real spectrum", all(isreal, w) && issorted(w),
               @sprintf("n=%d, E in [%.3f, %.3f]", n, w[1], w[end]))
    catch e
        _check("Hamiltonian hermiticity", false, sprint(showerror, e))
    end

    # 8b. AB flux quantization guard (catches the pure-gauge determinization bug):
    #     every vortex cell must carry exactly 2*pi*q*alpha; interior non-vortex
    #     cells must carry zero flux. (Boundary row/column carries the torus
    #     twist and is excluded.)
    try
        L = 24
        idxf(x, y) = (y - 1) * L + x
        alpha_t = 0.5; q_t = 1.0
        Hf = build_hamiltonian(L, 2, alpha_t, q_t, 0.0, 7)
        vcells = Set{Tuple{Int,Int}}()
        for (vx, vy) in vortex_positions(L, 2)
            push!(vcells, (clamp(Int(floor(vx + 0.5)), 1, L), clamp(Int(floor(vy + 0.5)), 1, L)))
        end
        worst = 0.0
        for y in 1:(L-1), x in 1:(L-1)
            s00 = idxf(x, y); s10 = idxf(x + 1, y)
            s11 = idxf(x + 1, y + 1); s01 = idxf(x, y + 1)
            Phi = angle(Hf[s00, s10] * Hf[s10, s11] * conj(Hf[s01, s11]) * conj(Hf[s00, s01]))
            expected = (x, y) in vcells ? 2pi * q_t * alpha_t : 0.0
            d = abs(mod(Phi - expected + pi, 2pi) - pi)   # mod-2pi distance
            worst = max(worst, d)
        end
        _check("AB flux 2*pi*q*alpha per vortex cell (Nv=2)", worst < 1e-9,
               @sprintf("max flux deviation = %.2e", worst))
    catch e
        _check("AB flux 2*pi*q*alpha per vortex cell (Nv=2)", false, sprint(showerror, e))
    end

    # 8c. geometry registry: 8 surfaces, unique ids, positive site counts
    try
        ok = length(GEOMETRY_LIST) == 8 &&
             length(unique(g.id for g in GEOMETRY_LIST)) == 8 &&
             all(g -> geom_nsites(g, 32) > 0, GEOMETRY_LIST)
        info = join([@sprintf("%s:%d", String(g.id), geom_nsites(g, g.model === :sphere ? 8 : 32))
                     for g in GEOMETRY_LIST], " ")
        _check("geometry registry (8 surfaces)", ok, info)
    catch e
        _check("geometry registry (8 surfaces)", false, sprint(showerror, e))
    end

    # 8d. Klein bottle fold: n = L^2/2, Hermitian, responds to alpha
    try
        L = 16
        gk = geom_by_id(:klein)
        H1 = build_hamiltonian_geo(gk, L, 2, 0.5, 1.0, 0.5, 11)
        H2 = build_hamiltonian_geo(gk, L, 2, 0.9, 1.0, 0.5, 11)
        herm = maximum(abs.(H1 - H1')) < 1e-12
        dE = maximum(abs.(eigvals(Hermitian(H2)) .- eigvals(Hermitian(H1))))
        _check("Klein bottle fold (n=$(size(H1,1)))", herm && size(H1, 1) == L * L ÷ 2 && dE > 1e-6,
               @sprintf("hermitian, max|dE(alpha)| = %.2e", dE))
    catch e
        _check("Klein bottle fold", false, sprint(showerror, e))
    end

    # 8e. pillow orbifold fold: n = L^2/2, Hermitian, vortex duplication works
    try
        L = 16
        gp = geom_by_id(:pillow)
        H1 = build_hamiltonian_geo(gp, L, 2, 0.5, 1.0, 0.5, 12)
        H2 = build_hamiltonian_geo(gp, L, 2, 0.9, 1.0, 0.5, 12)
        herm = maximum(abs.(H1 - H1')) < 1e-12
        dE = maximum(abs.(eigvals(Hermitian(H2)) .- eigvals(Hermitian(H1))))
        _check("Pillow orbifold fold (n=$(size(H1,1)))", herm && size(H1, 1) == L * L ÷ 2 && dE > 1e-6,
               @sprintf("hermitian, max|dE(alpha)| = %.2e", dE))
    catch e
        _check("Pillow orbifold fold", false, sprint(showerror, e))
    end

    # 8f. cube sphere: site count, degree profile, Euler characteristic V-E+F = 2
    try
        L = 8
        gc = geom_by_id(:cubic)
        H1 = build_hamiltonian_geo(gc, L, 2, 0.5, 1.0, 0.5, 13)
        n = size(H1, 1)
        E = (count(!iszero, H1) - count(!iszero, diag(H1))) ÷ 2     # undirected bonds
        F = 6 * (L - 1)^2
        chi = n - E + F
        dE = maximum(abs.(eigvals(Hermitian(build_hamiltonian_geo(gc, L, 2, 0.9, 1.0, 0.5, 13))) .-
                          eigvals(Hermitian(H1))))
        _check("Cube sphere (n=$n, V-E+F=$chi)", n == 6L^2 - 12L + 8 && chi == 2 && E == 2n - 4 && dE > 1e-6,
               @sprintf("E=%d bonds, chi=2, max|dE(alpha)| = %.2e", E, dE))
    catch e
        _check("Cube sphere", false, sprint(showerror, e))
    end

    # 8g. PSL(2,7) Klein quartic: |G| = 168 = 84(g-1), (3,7) generators,
    #     degree-4 Cayley graph, heptagon flux = 2*pi*q*alpha*Nv
    try
        G = get_psl(7)
        H1 = build_hamiltonian_cayley(G, 2, 0.5, 1.0, 0.0, 5)
        herm = maximum(abs.(H1 - H1')) < 1e-12
        flux = psl_heptagon_flux(G, H1)
        ferr = abs(mod(flux - 2pi * 1.0 * 0.5 * 2 + pi, 2pi) - pi)
        nbonds = (count(!iszero, H1) - count(!iszero, diag(H1))) ÷ 2
        _check("PSL(2,7) Klein quartic (|G|=168, flux/7g)",
               length(G.elems) == 168 && herm && ferr < 1e-9 && nbonds == 2 * 168,
               @sprintf("bonds=%d (4-reg), heptagon flux dev = %.2e", nbonds, ferr))
    catch e
        _check("PSL(2,7) Klein quartic", false, sprint(showerror, e))
    end

    # 8g-lift. HURWITZ STRETCH (v1.3): Z_k voltage lift of the Klein quartic —
    # |G|*7 sites, 4-regular, connected, heptagon flux preserved, responds to alpha
    try
        G = get_psl(7)
        k = 7
        vB, vC = cayley_voltages(G, k)
        H1 = build_hamiltonian_cayley_lift(G, k, 2, 0.5, 1.0, 0.0, 5)
        n = size(H1, 1)
        herm = maximum(abs.(H1 - H1')) < 1e-12
        conn = cayley_lift_connected(G, k, vB, vC)
        flux = psl_heptagon_flux(G, H1, k)
        ferr = abs(mod(flux - 2pi * 1.0 * 0.5 * 2 + pi, 2pi) - pi)
        nbonds = (count(!iszero, H1) - count(!iszero, diag(H1))) ÷ 2
        dE = maximum(abs.(eigvals(Hermitian(build_hamiltonian_cayley_lift(G, k, 2, 0.9, 1.0, 0.0, 5))) .-
                          eigvals(Hermitian(H1))))
        _check("PSL(2,7) stretch ×7 (n=$n, flux/7g)",
               n == 168 * 7 && herm && conn && ferr < 1e-9 && nbonds == 2 * n && dE > 1e-6,
               @sprintf("vB=%d vC=%d, 4-reg bonds=%d, connected, flux dev = %.2e, max|dE(alpha)| = %.2e",
                        vB, vC, nbonds, ferr, dE))
    catch e
        _check("PSL(2,7) stretch ×7", false, sprint(showerror, e))
    end

    # 8h. PSL(2,8) Macbeath (504), PSL(2,13) Fricke-Klein (1092) and
    #     PSL(2,27) Hurwitz-118 (9828) — the BIG Hurwitz matrix of the L=96 budget
    try
        n8 = length(get_psl(8).elems)
        n13 = length(get_psl(13).elems)
        n27 = length(get_psl(27).elems)
        _check("PSL(2,8)=504 · PSL(2,13)=1092 · PSL(2,27)=9828 (Hurwitz 84(g-1))",
               n8 == 504 && n13 == 1092 && n27 == 9828,
               @sprintf("Macbeath g=7: %d · Fricke-Klein g=14: %d · Hurwitz-118 g=118: %d", n8, n13, n27))
    catch e
        _check("PSL(2,8) & PSL(2,13) & PSL(2,27) groups", false, sprint(showerror, e))
    end

    # 8i. end-to-end mini pipeline on a Hurwitz geometry: window -> unfold -> KS
    try
        G = get_psl(7)
        H1 = build_hamiltonian_cayley(G, 2, 0.5, 1.0, 0.5, 21)
        n = size(H1, 1)
        ilo = max(2, floor(Int, n * 0.25)); ihi = min(n - 1, ceil(Int, n * 0.75))
        _, _, d, e = LAPACK.hetrd!('L', copy(H1))
        E = LAPACK.stebz!('I', 'B', 0.0, 0.0, ilo, ihi, -1.0, d, e)[1]
        s = unfold_levels(E; trim = 10, m = 8)
        dG = ks_gue(s)
        _check("Hurwitz end-to-end (unfold+KS on PSL(2,7))", length(s) > 20 && 0.0 < dG < 1.0,
               @sprintf("%d spacings, d_GUE = %.4f", length(s), dG))
    catch e
        _check("Hurwitz end-to-end", false, sprint(showerror, e))
    end

    # 9. progress bar render (non-destructive)
    try
        p = PBar(20)
        pbar_start!(p, "SELFTEST")
        pbar_set!(p, 0.5; sub = "render check")
        pbar_abort!(p)
        _check("progress bar one-line render", true, "rendered without error")
    catch e
        _check("progress bar one-line render", false, sprint(showerror, e))
    end

    # 9b. BIG-MATRIX parity (v1.1): at L = 96 with autoscale ON every scalable
    #     geometry must reach ≈ 96² = 9216 sites (the torus big matrix), so a
    #     non-torus selection no longer degrades into a small synthetic run.
    try
        saved_as = LAB.autoscale
        LAB.autoscale = true
        target = 96 * 96
        got = Tuple{Symbol,Int,Bool}[]
        okall = true
        for g in GEOMETRY_LIST
            Le, _ = geom_L_eff(g, 96)
            n = geom_nsites(g, Le)
            # cayley (v1.3): stretched by the ×7 lift ladder toward the budget
            okg = g.model === :cayley ?
                  (n == g.aut_order * cayley_lift_k(g, 96) && n >= 0.75 * target) :
                  n >= 0.90 * target
            okg && n <= LAB_MAX_SITES || (okg = false)
            okall &= okg
            push!(got, (g.id, n, okg))
        end
        LAB.autoscale = saved_as
        info = join(["$(String(g.id)):$n" *
                     (g.model === :cayley ? "(k=$(cayley_lift_k(g, 96)))" : "") *
                     (ok ? "" : " FAIL")
                     for (g, n, ok) in zip(GEOMETRY_LIST, [x[2] for x in got], [x[3] for x in got])], " ")
        _check("big-matrix 96-scale parity", okall, info * " (target ≥ $(round(Int, 0.9 * target)))")
    catch e
        _check("big-matrix 96-scale parity", false, sprint(showerror, e))
    end

    # 10. i18n completeness
    try
        miss = Symbol[]
        for (k, _) in STRINGS[:en]
            haskey(STRINGS[:ru], k) || push!(miss, k)
        end
        _check("i18n EN/RU key parity", isempty(miss),
               isempty(miss) ? "$(length(STRINGS[:en])) keys, both languages" :
               "missing RU: " * join(string.(miss), ","))
    catch e
        _check("i18n EN/RU key parity", false, sprint(showerror, e))
    end

    println()
    width = 42
    lab_table_header(["check", "status", "info"], [width, 8, 46])
    for (name, ok, info) in results
        lab_table_row([rpad(name, width), ok ? cc("PASS", C_GRN, C_B) : cc("FAIL", C_RED, C_B), info],
                      [width, 8, 46])
    end
    lab_table_footer((top = "", mid = "", bot = "└" * join(("─"^w for w in [width, 8, 46]), "┴") * "┘"))
    nfail = count(x -> !x[2], results)
    println(cc(nfail == 0 ? "  ALL CHECKS PASSED " : "  $nfail CHECK(S) FAILED ", C_B, nfail == 0 ? C_GRN : C_RED),
            cc("· " * fmt_sec(time() - run_t0), C_GRY))
    println()
    return nfail == 0
end
# =============================================================================
# INTERACTIVE MENU — opens immediately when the file is included in the REPL
# =============================================================================

const LAB_ZEROS_LIST = Ref(ZerosCandidate[])

function rescan_zeros!(; quiet::Bool = false)
    quiet || println(cc("  " * t(:scan_scanning), C_GRY))
    LAB_ZEROS_LIST[] = discover_zeros_files()
    if !isempty(LAB_ZEROS_LIST[])
        best = LAB_ZEROS_LIST[][1]
        if !isfile(LAB.zeros_file) || !any(c -> c.path == LAB.zeros_file, LAB_ZEROS_LIST[])
            LAB.zeros_file = best.path
            LAB.zeros_avail = best.count
            LAB.n_zeros = min(max(LAB.n_zeros, 1000), best.count)
        else
            c = findfirst(c -> c.path == LAB.zeros_file, LAB_ZEROS_LIST[])
            LAB.zeros_avail = LAB_ZEROS_LIST[][c].count
            LAB.n_zeros = min(LAB.n_zeros, LAB.zeros_avail)
        end
    end
    quiet || println(cc("  " * t(:scan_done) * ": " * string(length(LAB_ZEROS_LIST[])), C_GRY))
    lab_save_settings()
    nothing
end

function lab_banner()
    println()
    W = 74
    println(cc("  █" * "█"^W * "█", C_BLU))
    println(cc("  █" * lpad("", W) * "█", C_BLU))
    println(cc("  █ " * rpad("TEST 34 · STANDALONE LAB · AB-cloud model vs RIEMANN ZEROS", W - 2) * "█", C_BLU, C_B))
    println(cc("  █ " * rpad("KS D · R2(s) · d_GUE / d_Pois · composite verdict (v23)", W - 2) * "█", C_BLU))
    println(cc("  █" * lpad("", W) * "█", C_BLU))
    println(cc("  █" * "█"^W * "█", C_BLU))
    @printf(stdout, "  Julia %s · threads %s · BLAS %s · %s\n",
            string(VERSION), string(Threads.nthreads()), string(BLAS.get_num_threads()),
            cc("julia -t auto " * t(:hint_threads), C_GRY))
    nothing
end

function status_panel()
    zf = isfile(LAB.zeros_file) ? basename(LAB.zeros_file) : t(:status_nofile)
    println()
    println(cc("  ─"^39, C_GRY))
    println("  ", cc(t(:status_zeros_file), C_B), zf, cc(@sprintf("  [%d available]", LAB.zeros_avail), C_GRY))
    println("  ", cc(t(:status_zeros_count), C_B), format_count(LAB.n_zeros))
    # STRETCH FIX (v1.3): the tag tells the truth for EVERY geometry.
    geo_tag = if GEOM[].model === :cayley
        k = cayley_lift_k(GEOM[], LAB.L)
        n = GEOM[].aut_order * k
        k > 1 ?
            "  [" * t(:tag_stretch) * " ×" * string(k) * " → " * string(n) * " " *
            t(:tag_sites) * " ≈ L²=" * string(LAB.L * LAB.L) * "]" :
        LAB.autoscale ?
            "  [|G|=$(GEOM[].aut_order) " * t(:tag_stretch_na) * "]" :
            "  [|G|=$(GEOM[].aut_order) " * t(:tag_stretch_off) * "]"
    elseif LAB.autoscale
        "  [autoscale ON → ~L² = $(LAB.L * LAB.L) " * t(:tag_sites) * "]"
    else
        "  [autoscale OFF — " * t(:tag_autoscale_off) * "]"
    end
    println("  ", cc(t(:status_geometry), C_B), geometry_label(GEOM[], LAB.L),
            cc(geo_tag, C_GRY))
    println("  ", cc(t(:status_model), C_B),
            @sprintf("L=%d · Nv=%d · q=%.2f · alpha=%.2f · W=%.2f · window=%.2f",
                     LAB.L, LAB.Nv, LAB.q, LAB.alpha, LAB.W, LAB.window_frac))
    println("  ", cc(t(:status_reps), C_B),
            @sprintf("M1=%d · M2=%d · M3 seeds=%d · M4=%d/pt · M5=%d · sweep=%s", LAB.reps1, LAB.reps2, LAB.reps3seeds, LAB.reps4, LAB.reps5, String(LAB.sweep_param)))
    println("  ", cc(t(:status_lang), C_B), (LAB.lang === :en ? "English" : "Русский"))
    println(cc("  ─"^39, C_GRY))
    nothing
end

format_count(n::Int) = n >= 1000 ? @sprintf("%d (%.0fk)", n, n / 1000) : string(n)

function main_menu()
    while true
        try
            lab_clearscreen()
            lab_banner()
            status_panel()
            println()
            println(cc("  ── RUN ", C_CYN) * cc("─"^54, C_CYN))
            @printf(stdout, "   %s  %s\n", cc("[1]", C_B), t(:opt1))
            @printf(stdout, "   %s  %s\n", cc("[2]", C_B), t(:opt2))
            @printf(stdout, "   %s  %s\n", cc("[3]", C_B), t(:opt3))
            @printf(stdout, "   %s  %s\n", cc("[4]", C_B), t(:opt4))
            @printf(stdout, "   %s  %s\n", cc("[5]", C_B), t(:opt5))
            println(cc("  ── SETTINGS ", C_CYN) * cc("─"^49, C_CYN))
            @printf(stdout, "   %s  %s\n", cc("[6]", C_B), t(:menu_zeros))
            @printf(stdout, "   %s  %s\n", cc("[7]", C_B), t(:menu_model))
            @printf(stdout, "   %s  %s\n", cc("[8]", C_B), t(:menu_geometry))
            @printf(stdout, "   %s  %s\n", cc("[9]", C_B), t(:menu_runs))
            @printf(stdout, "   %s  %s    %s  %s\n", cc("[l]", C_B), t(:menu_lang), cc("[r]", C_B), t(:menu_rescan))
            @printf(stdout, "   %s  %s    %s  %s\n", cc("[s]", C_B), t(:menu_selftest), cc("[h]", C_B), t(:menu_help))
            @printf(stdout, "   %s  %s\n", cc("[0]", C_B), t(:menu_exit))
            println(cc("  " * "─"^61, C_CYN))
            choice = lowercase(lab_ask(cc("  " * t(:menu_select), C_B, C_CYN)))
            if !LAB_STDIN_OPEN[]
                println(cc("  stdin closed — leaving menu (use --mode=N for headless runs)", C_GRY))
                return nothing
            end
            if choice == "1"
                run_mode1()
                lab_pause()
            elseif choice == "2"
                run_mode2()
                lab_pause()
            elseif choice == "3"
                run_mode3()
                lab_pause()
            elseif choice == "4"
                run_mode4()
                lab_pause()
            elseif choice == "5"
                run_mode5()
                lab_pause()
            elseif choice == "6"
                menu_zeros()
            elseif choice == "7"
                menu_model()
            elseif choice == "8"
                menu_geometry()
            elseif choice == "9"
                menu_runs()
            elseif choice == "l"
                menu_lang()
            elseif choice == "r"
                rescan_zeros!()
                lab_pause()
            elseif choice == "s"
                run_selftest()
                lab_pause()
            elseif choice == "h"
                menu_help()
                lab_pause()
            elseif choice == "0" || choice == "q" || choice == "exit"
                println(cc("  " * t(:bye), C_GRY))
                return nothing
            else
                println(cc("  ! " * t(:invalid_choice), C_YLW))
                sleep(0.6)
            end
        catch e
            e isa InterruptException && return nothing
            println(cc("  ! " * t(:menu_error) * ": " * sprint(showerror, e), C_RED))
            lab_pause()
        end
    end
    nothing
end

# ------------------------------------------------------------------ zeros menu

function menu_zeros()
    println()
    println(cc("  " * t(:zeros_title), C_B))
    if isempty(LAB_ZEROS_LIST[])
        rescan_zeros!(; quiet = true)
    end
    if isempty(LAB_ZEROS_LIST[])
        println(cc("  " * t(:zeros_none), C_YLW))
        println(cc("  " * t(:zeros_none_hint), C_GRY))
    else
        println(cc("  " * t(:zeros_found) * ":", C_B))
        for (i, c) in enumerate(LAB_ZEROS_LIST[])
            mark = c.path == LAB.zeros_file ? cc(" <== ", C_GRN, C_B) : "     "
            @printf(stdout, "    %s[%d] %s\n", mark, i, basename(c.path))
            @printf(stdout, "         %s zeros · %.4f ... %.1f · monotone %.1f%% · %s\n",
                    format_count(c.count), c.first, c.last, 100c.monotone, fmt_bytes(filesize(c.path)))
        end
    end
    println()
    println("    ", cc("[r]", C_B), " ", t(:menu_rescan), "   ", cc("[m]", C_B), " ", t(:zeros_manual))
    println("    ", cc("[n]", C_B), " ", t(:zeros_count_title))
    choice = lowercase(lab_ask(cc("  " * t(:menu_select), C_B, C_CYN)))
    if choice == "r"
        rescan_zeros!()
    elseif choice == "m"
        p = lab_ask("  " * t(:zeros_path_prompt))
        if isfile(p)
            cand = sniff_zeros_file(p)
            if cand === nothing
                println(cc("  ! " * t(:zeros_bad_path), C_YLW))
            else
                LAB.zeros_file = cand.path
                LAB.zeros_avail = cand.count
                LAB.n_zeros = min(max(LAB.n_zeros, 1000), cand.count)
                println(cc("  " * t(:zeros_selected) * ": " * basename(p) * " (" * format_count(cand.count) * ")", C_GRN))
            end
        else
            println(cc("  ! " * t(:zeros_bad_path), C_YLW))
        end
    elseif choice == "n"
        menu_zeros_count()
    elseif all(isdigit, choice) && !isempty(choice)
        i = parse(Int, choice)
        if 1 <= i <= length(LAB_ZEROS_LIST[])
            c = LAB_ZEROS_LIST[][i]
            LAB.zeros_file = c.path
            LAB.zeros_avail = c.count
            LAB.n_zeros = min(max(LAB.n_zeros, 1000), c.count)
            println(cc("  " * t(:zeros_selected) * ": " * basename(c.path) * " (" * format_count(c.count) * ")", C_GRN))
        else
            println(cc("  ! " * t(:invalid_choice), C_YLW))
        end
    end
    lab_save_settings()
    nothing
end

function menu_zeros_count()
    avail = LAB.zeros_avail
    println()
    println(cc("  " * t(:zeros_count_title) * @sprintf(" [%s %s]", t(:available), format_count(avail)), C_B))
    presets = Int[]
    for v in (1_000, 5_000, 10_000, 25_000, 50_000, 100_000, 200_000, 500_000, 1_000_000)
        if v <= avail
            push!(presets, v)
        end
    end
    for (i, v) in enumerate(presets)
        mark = v == LAB.n_zeros ? cc(" <==", C_GRN, C_B) : ""
        @printf(stdout, "    [%d] %s%s\n", i, format_count(v), mark)
    end
    @printf(stdout, "    [a] %s (%d)\n", t(:zeros_count_all), avail)
    mark = LAB.n_zeros == avail ? cc(" <==", C_GRN, C_B) : ""
    @printf(stdout, "    [c] %s%s\n", t(:zeros_count_custom), mark)
    choice = lowercase(lab_ask(cc("  " * t(:menu_select), C_B, C_CYN)))
    if choice == "a"
        LAB.n_zeros = avail
    elseif choice == "c"
        LAB.n_zeros = lab_ask_int("  " * t(:zeros_count_prompt), LAB.n_zeros; lo = 100, hi = avail)
    elseif all(isdigit, choice) && !isempty(choice)
        i = parse(Int, choice)
        if 1 <= i <= length(presets)
            LAB.n_zeros = presets[i]
        end
    end
    println(cc("  " * t(:zeros_count_set) * ": " * format_count(LAB.n_zeros), C_GRN))
    lab_save_settings()
    nothing
end

# ---------------------------------------------------------------- geometry menu

function menu_geometry()
    println()
    println(cc("  " * t(:geo_title), C_B))
    for (i, g) in enumerate(GEOMETRY_LIST)
        Le, cl = geom_L_eff(g, LAB.L)
        n = geom_nsites(g, Le)
        mark = g.id === GEOM[].id ? cc(" <==", C_GRN, C_B) : ""
        hw = g.hurwitz ? cc(" HURWITZ", C_YLW, C_B) : ""
        fix = ""
        if g.model === :cayley
            k = cayley_lift_k(g, LAB.L)
            fix = k > 1 ? cc(" [×" * string(k) * "]", C_CYN, C_B) : cc(t(:geo_fixed_short), C_GRY)
        end
        @printf(stdout, "    [%d] %-17s %-21s g=%-2d χ=%-3d sites=%-6d%s%s%s%s\n",
                i, g.name, g.group, g.genus, g.chi, n, hw, fix,
                cl ? cc(@sprintf("  (L→%d)", Le), C_GRY) : "", mark)
    end
    println()
    println("    ", cc("[a]", C_B), " ", t(:geo_autoscale), " ",
            LAB.autoscale ? cc("[ON]", C_GRN, C_B) : cc("[OFF]", C_YLW, C_B))
    println("    ", cc("[r]", C_B), " ", t(:geo_stay))
    choice = lowercase(lab_ask(cc("  " * t(:menu_select), C_B, C_CYN)))
    if choice == "a"
        LAB.autoscale = !LAB.autoscale
        println(cc("  ", C_GRY), t(:geo_autoscale) * ": ",
                LAB.autoscale ? cc("ON", C_GRN, C_B) : cc("OFF", C_YLW, C_B),
                " — ", LAB.autoscale ? t(:geo_autoscale_on) : t(:geo_autoscale_off))
    elseif all(isdigit, choice) && !isempty(choice)
        i = parse(Int, choice)
        if 1 <= i <= length(GEOMETRY_LIST)
            g = GEOMETRY_LIST[i]
            GEOM[] = g
            LAB.geometry = g.id
            Le, cl = geom_L_eff(g, LAB.L)
            println(cc("  " * t(:geo_selected) * ": " * g.name *
                       (cl ? "  (" * t(:geo_L_note) * " L→" * string(Le) * ")" : ""), C_GRN))
            # STRETCH FIX (v1.3): report the stretched size at once; warn only
            # when the matrix stays far below the L² budget.
            g.model === :cayley && begin
                k = cayley_lift_k(g, LAB.L)
                n = g.aut_order * k
                if k > 1
                    println(cc("    " * t(:geo_stretched) * " ×" * string(k) * " → " *
                               string(n) * " " * t(:tag_sites) * " (L² = " *
                               string(LAB.L * LAB.L) * ")", C_GRN))
                elseif LAB.autoscale
                    println(cc("  |G|=" * string(g.aut_order) * " " * t(:tag_stretch_na), C_GRN))
                else
                    println(cc("  ! " * t(:model_L_cayley_a) * string(g.aut_order) *
                               t(:model_L_cayley_b) * string(LAB.L * LAB.L) *
                               t(:model_L_cayley_c), C_YLW))
                end
            end
        else
            println(cc("  ! " * t(:invalid_choice), C_YLW))
        end
    end
    lab_save_settings()
    nothing
end

# ------------------------------------------------------------------ model menu

function menu_model()
    println()
    println(cc("  " * t(:model_title), C_B))
    @printf(stdout, "    %s [32 48 64 80 96 112 128 144]:\n", t(:model_L))
    LAB.L = lab_ask_int("  L", LAB.L; lo = 8, hi = 256)
    if !(LAB.L in LAB_ALLOWED_L)
        println(cc("  ! " * t(:model_L_warn), C_YLW))
    end
    # STRETCH FIX (v1.3): report from the TRUE effective size. A Hurwitz group
    # with the stretch ON lands on the ×7 lift ladder closest to L²; warn only
    # when the landed matrix is far below the budget (or stretch is OFF).
    Le, cl = geom_L_eff(GEOM[], LAB.L)
    n_eff = geom_nsites(GEOM[], Le)
    budget = LAB.L * LAB.L
    if GEOM[].model === :cayley
        k = cayley_lift_k(GEOM[], LAB.L)
        if k > 1 && n_eff >= round(Int, 0.9 * budget)
            println(cc("  " * t(:mstretch_head) * " |G|=" * string(GEOM[].aut_order) *
                       " ×" * string(k) * " = " * string(n_eff) * " " * t(:tag_sites) *
                       " (L² = " * string(budget) * ")", C_GRN))
        elseif LAB.autoscale
            println(cc("  ! " * t(:warn_matrix_reason_cayley), C_YLW))
            println(cc("      " * t(:warn_matrix_hint_cayley), C_YLW))
        else
            println(cc("  ! " * t(:model_L_cayley_a) * string(GEOM[].aut_order) *
                       t(:model_L_cayley_b) * string(budget) *
                       t(:model_L_cayley_c), C_YLW))
        end
    elseif n_eff < round(Int, 0.9 * budget)
        cl && println(cc("  ! " * t(:geo_L_note) * " (" * String(GEOM[].id) * ": L→" * string(Le) * ")", C_YLW))
        !LAB.autoscale && println(cc("  ! " * t(:model_L_autoscale_off_hint), C_YLW))
    end
    # BIG-MATRIX FIX (v1.1): the memory estimate used L^4 bytes (= 16 B × L^4,
    # i.e. an L×L torus) even for geometries whose matrix is NOT L×L — the
    # cube sphere at L=96 showed ~845 GB while the real auto-scaled matrix has
    # 9128 sites (~1.3 GB). Estimate from the EFFECTIVE site count instead.
    mem = 16.0 * geom_nsites(GEOM[], Le)^2
    if mem > 3e9
        println(cc("  ! " * t(:model_mem_warn) * @sprintf(" (~%.1f GB)", mem / 1e9), C_YLW))
    end
    @printf(stdout, "    %s:\n", t(:model_Nv))
    LAB.Nv = lab_ask_int("  Nv", LAB.Nv; lo = 0, hi = 16)
    @printf(stdout, "    %s:\n", t(:model_q))
    LAB.q = lab_ask_float("  q", LAB.q; lo = 0.0, hi = 10.0)
    @printf(stdout, "    %s [0..1]:\n", t(:model_alpha))
    LAB.alpha = lab_ask_float("  alpha", LAB.alpha; lo = 0.0, hi = 1.0)
    @printf(stdout, "    %s:\n", t(:model_W))
    LAB.W = lab_ask_float("  W", LAB.W; lo = 0.0, hi = 10.0)
    @printf(stdout, "    %s (0.25..0.9):\n", t(:model_window))
    LAB.window_frac = lab_ask_float("  window", LAB.window_frac; lo = 0.05, hi = 0.9)
    lab_save_settings()
    nothing
end

# ------------------------------------------------------------------- runs menu

function menu_runs()
    println()
    println(cc("  " * t(:runs_title), C_B))
    @printf(stdout, "    %s:\n", t(:runs_reps1))
    LAB.reps1 = lab_ask_int("  reps1", LAB.reps1; lo = 1, hi = 200)
    @printf(stdout, "    %s:\n", t(:runs_reps2))
    LAB.reps2 = lab_ask_int("  reps2", LAB.reps2; lo = 1, hi = 500)
    @printf(stdout, "    %s:\n", t(:runs_reps3))
    LAB.reps3seeds = lab_ask_int("  seeds3", LAB.reps3seeds; lo = 1, hi = 50)
    @printf(stdout, "    %s:\n", t(:runs_reps4))
    LAB.reps4 = lab_ask_int("  reps4", LAB.reps4; lo = 1, hi = 20)
    @printf(stdout, "    %s:\n", t(:runs_reps5))
    LAB.reps5 = lab_ask_int("  reps5", LAB.reps5; lo = 1, hi = 50)
    @printf(stdout, "    %s (alpha/Nv/q/W):\n", t(:runs_sweep))
    sp = lowercase(lab_ask("  sweep", String(LAB.sweep_param)))
    sp in ("alpha", "nv", "q", "w") && (LAB.sweep_param = sp == "nv" ? :Nv : Symbol(sp))
    @printf(stdout, "    %s:\n", t(:runs_seed))
    LAB.seed_base = lab_ask_int("  seed", LAB.seed_base; lo = 1, hi = 10^9)
    @printf(stdout, "    %s [y/n]:\n", t(:runs_plots))
    pa = lowercase(lab_ask("  plots", LAB.plots_on ? "y" : "n"))
    LAB.plots_on = pa in ("y", "yes", "1", "да")
    @printf(stdout, "    %s:\n", t(:runs_nchunks))
    LAB.nchunks = lab_ask_int("  chunks", LAB.nchunks; lo = 1, hi = 100)
    lab_save_settings()
    nothing
end

function menu_lang()
    println()
    println(cc("  " * t(:lang_title), C_B))
    @printf(stdout, "    [1] English%s\n", LAB.lang === :en ? cc(" <==", C_GRN, C_B) : "")
    @printf(stdout, "    [2] Русский%s\n", LAB.lang === :ru ? cc(" <==", C_GRN, C_B) : "")
    choice = lowercase(lab_ask(cc("  " * t(:menu_select), C_B, C_CYN)))
    if choice == "1"
        LAB.lang = :en
    elseif choice == "2"
        LAB.lang = :ru
    end
    lab_save_settings()
    nothing
end

function menu_help()
    println()
    println(cc("  " * t(:help_title), C_B))
    for line in t(:help_text)
        println("  ", line)
    end
    nothing
end
# =============================================================================
# I18N: English (default) + Russian.  t(key) returns the current language.
# =============================================================================

const STRINGS = Dict{Symbol,Dict{Symbol,Any}}(:en => Dict{Symbol,Any}(), :ru => Dict{Symbol,Any}())

function _tr!(lang::Symbol, key::Symbol, val)
    STRINGS[lang][key] = val
    nothing
end

t(key::Symbol) = begin
    d = STRINGS[LAB.lang]
    haskey(d, key) && return d[key]
    haskey(STRINGS[:en], key) && return STRINGS[:en][key]
    return string(key)
end

function _i18n_init!()
    # ---------------------------------------------------------------- ENGLISH
    _tr!(:en, :err_int_range, "please enter an integer in range")
    _tr!(:en, :err_float_range, "please enter a number in range")
    _tr!(:en, :press_enter, "Press Enter to return to the menu")
    _tr!(:en, :timing_summary, "Timing per phase")
    _tr!(:en, :timing_total, "TOTAL")
    _tr!(:en, :done, "done")
    _tr!(:en, :no_zeros_selected, "no zeros file selected — please pick one first")
    _tr!(:en, :ph_load_zeros, "load & unfold zeta zeros")
    _tr!(:en, :ph_analysis, "statistics & verdict")
    _tr!(:en, :ph_plots, "rendering plots")
    _tr!(:en, :ph_cdf_diff, "CDF differential |F_AB - F_zeta|")
    _tr!(:en, :ph_seed_forensics, "seed forensics (same params, new seeds)")
    _tr!(:en, :ph_lattice_scaling, "lattice finite-size scaling")
    _tr!(:en, :pooled_header, "POOLED statistics (all realizations combined)")
    _tr!(:en, :v_pass, "GUE-CONSISTENT — Test 34 composite criterion satisfied")
    _tr!(:en, :v_fail, "DEVIATION DETECTED — composite criterion not satisfied")
    _tr!(:en, :ensemble_header, "ENSEMBLE stability (realization-17 forensics)")
    _tr!(:en, :ens_stable, "ensemble STABLE")
    _tr!(:en, :ens_unstable, "ensemble UNSTABLE")
    _tr!(:en, :n_mode1_note1, "p is unreliable at N ~ 1e5 (always ~0); judge by effect size D (v23 guidance).")
    _tr!(:en, :n_mode1_note2, "D converges to its true value as N grows — compare D, not p.")
    _tr!(:en, :n_mode2_note1, "MAD outlier flag: |D - median| > 3 x 1.4826 x MAD (realization-17 style).")
    _tr!(:en, :n_mode2_note2, "Leave-one-out pooled D shows how strongly each realization drives the verdict.")
    _tr!(:en, :n_mode2_outliers, "Flagged outliers:")
    _tr!(:en, :n_mode3_note1, "CDF differential localizes WHERE in s the KS distance is generated.")
    _tr!(:en, :n_mode3_note2, "Lattice scaling probes the finite-size (96x96) origin of the s ~ 0.3 excess.")
    _tr!(:en, :n_mode4_note1, "Each sweep point uses one realization — treat borders as noisy.")
    _tr!(:en, :n_mode4_note2, "GOLD zone = D < 0.10 AND d_GUE < d_Pois AND plateau in [0.75, 1.25].")
    _tr!(:en, :out_dir, "Output directory")
    _tr!(:en, :report_files, "Reports")
    _tr!(:en, :m1_name, "NORMAL")
    _tr!(:en, :m1_sub, "refined primary pass — direct AB vs zeta comparison")
    _tr!(:en, :m2_name, "HARDCORE")
    _tr!(:en, :m2_sub, "refined ensemble pass — strict statistics & outliers")
    _tr!(:en, :m3_name, "DEEP DIAGNOSTICS")
    _tr!(:en, :m3_sub, "CDF differential · short-range R2 · seeds · bootstrap · scaling")
    _tr!(:en, :m4_name, "VORTEX CONFIGURATOR")
    _tr!(:en, :m4_sub, "sweep stabilization map")
    _tr!(:en, :m3_main_header, "MAIN realization (default vortex parameters)")
    _tr!(:en, :m3_cdf_header, "CDF differential analysis")
    _tr!(:en, :m3_seed_header, "Seed forensics — same parameters, different seeds")
    _tr!(:en, :m3_scaling_header, "Lattice scaling — finite-size probe")
    _tr!(:en, :m3_trend_down, "Trend: D decreases with L — consistent with a finite-lattice effect.")
    _tr!(:en, :m3_trend_flat, "Trend: D does not decrease with L — deviation is not (only) finite-size.")
    _tr!(:en, :m4_disclaimer, "EXPLORATORY / response-fitting tool: it shows which vortex values stabilize the spectrum, it is not a proof.")
    _tr!(:en, :m4_result_header, "Sweep result")
    _tr!(:en, :m4_gold_points, "Stabilization (GOLD) points")
    _tr!(:en, :m4_no_gold, "No GOLD points on this grid — consider refining the grid around the best point.")
    _tr!(:en, :m4_crossover, "GUE/Poisson crossover")
    _tr!(:en, :m4_best, "Best point (min D)")
    _tr!(:en, :plots_rendering, "rendering plots ...")
    _tr!(:en, :scan_scanning, "scanning directory for Riemann zeros files ...")
    _tr!(:en, :scan_done, "zeros files found")
    _tr!(:en, :hint_threads, "recommended for live progress during diagonalization")
    _tr!(:en, :status_zeros_file, "zeros file : ")
    _tr!(:en, :status_zeros_count, "zeros used : ")
    _tr!(:en, :status_model, "model      : ")
    _tr!(:en, :status_reps, "runs       : ")
    _tr!(:en, :status_lang, "language   : ")
    _tr!(:en, :status_nofile, "*** none ***  (put zeros .txt next to the script or press [6])")
    _tr!(:en, :opt1, "MODE 1  NORMAL  — primary pass, direct Test 34")
    _tr!(:en, :opt2, "MODE 2  HARDCORE — ensemble pass, outliers & stability")
    _tr!(:en, :opt3, "MODE 3  DEEP DIAGNOSTICS — CDF diff, seeds, bootstrap, scaling")
    _tr!(:en, :opt4, "MODE 4  VORTEX CONFIGURATOR — sweep + stabilization map")
    _tr!(:en, :menu_zeros, "Zeros: choose file / number of zeros")
    _tr!(:en, :menu_model, "Model: L, Nv, q, alpha, W, window")
    _tr!(:en, :menu_runs, "Runs: realizations, seeds, sweep, plots")
    _tr!(:en, :menu_lang, "Language / Язык")
    _tr!(:en, :menu_rescan, "Rescan zeros directory")
    _tr!(:en, :menu_selftest, "Self-test")
    _tr!(:en, :menu_help, "Help / about Test 34")
    _tr!(:en, :menu_exit, "Exit menu")
    _tr!(:en, :opt5, "MODE 5  UNIVERSAL — all geometries x 4 tests x 3 realizations")
    _tr!(:en, :m5_name, "UNIVERSAL GEOMETRY SWEEP")
    _tr!(:en, :m5_sub, "all geometries x tests 1-4 x N realizations each")
    _tr!(:en, :m5_summary, "UNIVERSAL SUMMARY (pooled verdicts)")
    _tr!(:en, :m5_verdict, "UNIVERSAL VERDICT")
    _tr!(:en, :m5_subtests, "geometry x test subtests GUE-consistent")
    _tr!(:en, :m5_universal_ok, "the Test 34 pipeline is geometry-universal")
    _tr!(:en, :menu_geometry, "Geometry: surface for all runs (torus, Klein, Hurwitz PSL(2,q), ...)")
    _tr!(:en, :geo_title, "GEOMETRY / SURFACE  (used by every mode)")
    _tr!(:en, :geo_selected, "geometry selected")
    _tr!(:en, :geo_stay, "keep current geometry")
    _tr!(:en, :geo_L_note, "L auto-adjusted for this geometry:")
    _tr!(:en, :geo_L_ignored, "L ignored (stretch OFF, fixed |G|)")
    _tr!(:en, :geo_fixed_short, " [fixed]")
    _tr!(:en, :geo_stretched, "stretched")
    _tr!(:en, :mstretch_head, "Hurwitz stretch:")
    _tr!(:en, :tag_stretch, "stretch ON")
    _tr!(:en, :tag_stretch_off, "stretch OFF — fixed size")
    _tr!(:en, :tag_stretch_na, "already ≈ L² — no lift needed")
    _tr!(:en, :tag_fixed_by_math, "fixed by mathematics")
    _tr!(:en, :tag_not_applied, "not applied")
    _tr!(:en, :tag_sites, "sites")
    _tr!(:en, :tag_autoscale_off, "historical sizes")
    _tr!(:en, :model_L_cayley_a, "Hurwitz surface: |G| = ")
    _tr!(:en, :model_L_cayley_b, " — the stretch is OFF (autoscale OFF), so the matrix stays at the fixed |G| (requested L² budget = ")
    _tr!(:en, :model_L_cayley_c, "). Turn autoscale ON (menu [8] → [a]) to stretch ×7, ×14, … up to ≈ L².")
    _tr!(:en, :model_L_autoscale_off_hint, "autoscale is OFF — this geometry runs at its historical (small) size; enable it in menu [8] → [a]")
    _tr!(:en, :warn_matrix_head, "MATRIX SIZE:")
    _tr!(:en, :warn_matrix_sites, "sites")
    _tr!(:en, :warn_matrix_of_budget, "of the budget")
    _tr!(:en, :warn_matrix_reason_cayley, "the Hurwitz stretch ladder moves in steps of ×7 — it keeps the heptagon flux 2*pi*q*alpha*Nv intact — and this L lands between ladder steps.")
    _tr!(:en, :warn_matrix_hint_cayley, "Steps give |G|·k sites for k = 1, 7, 14, … — pick L so that L² ≈ |G|·k, or accept the nearest step (larger L moves to the next step).")
    _tr!(:en, :warn_matrix_reason_autoscale_off, "autoscale is OFF: this geometry falls back to its historical (small) size.")
    _tr!(:en, :warn_matrix_hint_autoscale, "Enable it in menu [8] → [a] (or CLI --autoscale=on) to run ≈ L² sites.")
    _tr!(:en, :geo_autoscale, "Big-matrix autoscale — every geometry stretches to ≈ L² sites (96 → ~9200; Hurwitz via the ×7 lift ladder)")
    _tr!(:en, :geo_autoscale_on, "ON — Klein/pillow scale to 136×136 (9248 sites), cube to L=40 (9128) at L=96; Hurwitz groups stretch ×7, ×14, … toward L² (psl27 → ×56 = 9408 at L=96)")
    _tr!(:en, :geo_autoscale_off, "OFF — historical per-geometry clamps (cube ≤ 12, fold n = L²/2)")
    _tr!(:en, :status_geometry, "geometry   : ")
    _tr!(:en, :runs_reps5, "MODE 5 realizations per test per geometry")
    _tr!(:en, :menu_open_hint, "opening interactive menu — type a number and press Enter ...")
    _tr!(:en, :menu_select, "Select and press Enter:")
    _tr!(:en, :invalid_choice, "invalid choice")
    _tr!(:en, :menu_error, "error")
    _tr!(:en, :bye, "menu closed — reopen any time with main_menu() or Test34Lab()")
    _tr!(:en, :zeros_title, "ZEROS SOURCE")
    _tr!(:en, :zeros_none, "no Riemann-zeros-like text files found in the script directory.")
    _tr!(:en, :zeros_none_hint, "put a zeros file (e.g. zeros_100k.txt, one gamma per line) next to finite-size_lab.jl and rescan.")
    _tr!(:en, :zeros_found, "Detected zeros files")
    _tr!(:en, :zeros_manual, "enter path manually")
    _tr!(:en, :zeros_path_prompt, "path to zeros file:")
    _tr!(:en, :zeros_bad_path, "file not found or does not look like Riemann zeros")
    _tr!(:en, :zeros_selected, "selected")
    _tr!(:en, :zeros_count_title, "NUMBER OF ZEROS to use")
    _tr!(:en, :available, "available")
    _tr!(:en, :zeros_count_all, "use ALL available")
    _tr!(:en, :zeros_count_custom, "custom number")
    _tr!(:en, :zeros_count_prompt, "number of zeros:")
    _tr!(:en, :zeros_count_set, "zeros to use")
    _tr!(:en, :model_title, "MODEL PARAMETERS")
    _tr!(:en, :model_L, "lattice side L (L x L sites)")
    _tr!(:en, :model_L_warn, "non-standard L — allowed: 32 48 64 80 96 112 128 144 (will run anyway)")
    _tr!(:en, :model_mem_warn, "large lattice — memory estimate")
    _tr!(:en, :model_Nv, "number of AB vortices Nv (0 = pure Anderson)")
    _tr!(:en, :model_q, "charge q (flux multiplier)")
    _tr!(:en, :model_alpha, "flux per vortex alpha (0..1, in flux quanta)")
    _tr!(:en, :model_W, "onsite disorder W")
    _tr!(:en, :model_window, "central spectrum window fraction used")
    _tr!(:en, :runs_title, "RUN SETTINGS")
    _tr!(:en, :runs_reps1, "MODE 1 realizations")
    _tr!(:en, :runs_reps2, "MODE 2 realizations")
    _tr!(:en, :runs_reps3, "MODE 3 seed-forensics runs")
    _tr!(:en, :runs_reps4, "MODE 4 realizations per sweep point")
    _tr!(:en, :runs_sweep, "MODE 4 swept parameter")
    _tr!(:en, :runs_seed, "seed base")
    _tr!(:en, :runs_plots, "render plots")
    _tr!(:en, :runs_nchunks, "eigenvalue chunks (progress granularity)")
    _tr!(:en, :runs_reps5, "MODE 5 realizations per test per geometry")
    _tr!(:en, :lang_title, "LANGUAGE / ЯЗЫК")
    _tr!(:en, :help_title, "ABOUT TEST 34")
    _tr!(:en, :help_text, [
        "Test 34 compares the AB-cloud spectrum with Riemann zeta zeros:",
        "  * unfold both spectra (log-density unfolding),",
        "  * two-sample KS: D and p on unfolded spacings,",
        "  * Montgomery pair correlation R2(s) vs GUE theory & Poisson,",
        "  * d_GUE / d_Pois — KS distance to GUE / Poisson spacing law,",
        "  * composite verdict: (p>0.01 OR D<0.10) AND d_GUE<d_Pois",
        "    AND plateau(R2, 1.0..2.0) in [0.75, 1.25].",
        "",
        "At N ~ 1e5 p-values are always ~0 — judge by D (effect size).",
        "",
        "GEOMETRIES (menu [8], used by every mode):",
        "  torus  - flat periodic lattice (original model), genus 1,",
        "  klein  - Klein bottle (vortex-antivortex pairs),",
        "  pillow - T^2/(x~-x) spherical orbifold, 4 cone points,",
        "  cubic  - cube sphere, quad mesh 6L^2-12L+8 sites,",
        "  psl27  - Klein quartic,    PSL(2,7),  |G|=168,  g=3,  HURWITZ",
        "  psl28  - Macbeath surface, PSL(2,8),  |G|=504,  g=7,  HURWITZ",
        "  psl213 - Fricke-Klein,     PSL(2,13), |G|=1092, g=14, HURWITZ",
        "  psl227 - Hurwitz-118,      PSL(2,27), |G|=9828, g=118, HURWITZ",
        "           (the BIG Hurwitz matrix: ~9828 sites ~ the L=96 torus",
        "           budget 9216; already ≈ L² — no lift needed there)",
        "  Hurwitz model: magnetic Cayley graph Cay(G;B,C), ord B=3,",
        "  ord C=7; heptagon flux = 2*pi*q*alpha*Nv (same flux knob as the",
        "  torus vortex ring).",
        "  STRETCH (v1.3): with autoscale ON every Hurwitz geometry STRETCHES",
        "  by a Z_k voltage lift: sites = |G|*k, k = 7, 14, 21, ... — the step",
        "  closest to L² (psl27 at L=96: 168 × 56 = 9408 sites). Every lifted",
        "  heptagon keeps the exact flux 2*pi*q*alpha*Nv; the lift is verified",
        "  connected. autoscale OFF keeps the historical fixed |G|.",
        "  BIG-MATRIX autoscale (menu [8] -> [a]): every scalable geometry",
        "  runs ≈ L² sites — at the default L=96 the Klein bottle/pillow",
        "  auto-scale to 136 (9248 sites) and the cube sphere to L=40",
        "  (9128 sites), i.e. the SAME big matrix as the 96x96 torus; no",
        "  more small clamped runs on non-torus geometries. The Hurwitz",
        "  surfaces keep their irreducible |G| (mathematically fixed).",
        "",
        "MODE 1 NORMAL  - 5 realizations, quick check.",
        "MODE 2 HARDCORE - 20 realizations, MAD outliers, leave-one-out.",
        "MODE 3 DEEP     - where D is generated (CDF diff), seed forensics,",
        "                  bootstrap CI, lattice scaling (geometry-aware).",
        "MODE 4 SWEEP    - vortex scan (alpha/Nv/q/W) with GOLD stabilization",
        "                  zone map (exploratory / response fitting).",
        "MODE 5 UNIVERSAL - every geometry x tests 1-4 x 3 realizations,",
        "                  one light pass, pooled verdicts + global verdict.",
        "",
        "Tips: start julia with -t auto for live progress; place zeros files",
        "(one gamma per line, 'n gamma' also OK) next to this script.",
    ])

    # ---------------------------------------------------------------- RUSSIAN
    _tr!(:ru, :err_int_range, "введите целое число в диапазоне")
    _tr!(:ru, :err_float_range, "введите число в диапазоне")
    _tr!(:ru, :press_enter, "Нажмите Enter для возврата в меню")
    _tr!(:ru, :timing_summary, "Время по фазам")
    _tr!(:ru, :timing_total, "ИТОГО")
    _tr!(:ru, :done, "готово")
    _tr!(:ru, :no_zeros_selected, "файл нулей не выбран — сначала выберите его в меню")
    _tr!(:ru, :ph_load_zeros, "загрузка и развёртка нулей дзета")
    _tr!(:ru, :ph_analysis, "статистика и вердикт")
    _tr!(:ru, :ph_plots, "построение графиков")
    _tr!(:ru, :ph_cdf_diff, "дифференциал CDF |F_AB - F_дзета|")
    _tr!(:ru, :ph_seed_forensics, "форензика сидов (те же параметры, новые сиды)")
    _tr!(:ru, :ph_lattice_scaling, "скейлинг по размеру решётки")
    _tr!(:ru, :pooled_header, "ОБЪЕДИНЁННАЯ статистика (все реализации вместе)")
    _tr!(:ru, :v_pass, "СОГЛАСУЕТСЯ С GUE — композитный критерий теста 34 выполнен")
    _tr!(:ru, :v_fail, "ОБНАРУЖЕНО ОТКЛОНЕНИЕ — композитный критерий не выполнен")
    _tr!(:ru, :ensemble_header, "УСТОЙЧИВОСТЬ ансамбля (форензика реализации-17)")
    _tr!(:ru, :ens_stable, "ансамбль УСТОЙЧИВ")
    _tr!(:ru, :ens_unstable, "ансамбль НЕУСТОЙЧИВ")
    _tr!(:ru, :n_mode1_note1, "p ненадёжно при N ~ 1e5 (всегда ~0); оценивайте по эффект-размеру D (рекомендация v23).")
    _tr!(:ru, :n_mode1_note2, "D сходится к истинному значению с ростом N — сравнивайте D, а не p.")
    _tr!(:ru, :n_mode2_note1, "Флаг выброса MAD: |D - медиана| > 3 x 1.4826 x MAD (как у реализации-17).")
    _tr!(:ru, :n_mode2_note2, "Leave-one-out D показывает, насколько каждая реализация влияет на вердикт.")
    _tr!(:ru, :n_mode2_outliers, "Помеченные выбросы:")
    _tr!(:ru, :n_mode3_note1, "Дифференциал CDF локализует, ГДЕ по s формируется расстояние KS.")
    _tr!(:ru, :n_mode3_note2, "Скейлинг решётки проверяет конечномерное (96x96) происхождение избытка при s ~ 0.3.")
    _tr!(:ru, :n_mode4_note1, "Каждая точка свипа — одна реализация; границы сетки шумные.")
    _tr!(:ru, :n_mode4_note2, "ЗОЛОТАЯ зона = D < 0.10 И d_GUE < d_Pois И плато в [0.75, 1.25].")
    _tr!(:ru, :out_dir, "Каталог вывода")
    _tr!(:ru, :report_files, "Отчёты")
    _tr!(:ru, :m1_name, "NORMAL (ОБЫЧНЫЙ)")
    _tr!(:ru, :m1_sub, "уточнённый основной проход — прямое сравнение AB vs дзета")
    _tr!(:ru, :m2_name, "HARDCORE (ЖЁСТКИЙ)")
    _tr!(:ru, :m2_sub, "уточнённый ансамблевый проход — строгая статистика и выбросы")
    _tr!(:ru, :m3_name, "ГЛУБОКАЯ ДИАГНОСТИКА")
    _tr!(:ru, :m3_sub, "дифференциал CDF · короткодействие R2 · сиды · бутстреп · скейлинг")
    _tr!(:ru, :m4_name, "КОНФИГУРАТОР ВИХРЕЙ")
    _tr!(:ru, :m4_sub, "карта зон стабилизации")
    _tr!(:ru, :m3_main_header, "ОСНОВНАЯ реализация (вихри по умолчанию)")
    _tr!(:ru, :m3_cdf_header, "Анализ дифференциала CDF")
    _tr!(:ru, :m3_seed_header, "Форензика сидов — те же параметры, разные сиды")
    _tr!(:ru, :m3_scaling_header, "Скейлинг решётки — проверка конечномерности")
    _tr!(:ru, :m3_trend_down, "Тренд: D убывает с ростом L — согласуется с конечнорешёточным эффектом.")
    _tr!(:ru, :m3_trend_flat, "Тренд: D не убывает с ростом L — отклонение не (только) конечномерное.")
    _tr!(:ru, :m4_disclaimer, "ИССЛЕДОВАТЕЛЬСКИЙ инструмент подгонки: показывает, при каких вихрях спектр стабилизируется, но не является доказательством.")
    _tr!(:ru, :m4_result_header, "Результат свипа")
    _tr!(:ru, :m4_gold_points, "Точки стабилизации (ЗОЛОТЫЕ)")
    _tr!(:ru, :m4_no_gold, "ЗОЛОТЫХ точек на сетке нет — уточните сетку вокруг лучшей точки.")
    _tr!(:ru, :m4_crossover, "Переход GUE/Пуассон")
    _tr!(:ru, :m4_best, "Лучшая точка (мин D)")
    _tr!(:ru, :plots_rendering, "построение графиков ...")
    _tr!(:ru, :scan_scanning, "поиск файлов с нулями Римана в каталоге ...")
    _tr!(:ru, :scan_done, "найдено файлов с нулями")
    _tr!(:ru, :hint_threads, "рекомендуется для живого прогресс-бара при диагонализации")
    _tr!(:ru, :status_zeros_file, "файл нулей  : ")
    _tr!(:ru, :status_zeros_count, "нулей брать : ")
    _tr!(:ru, :status_model, "модель      : ")
    _tr!(:ru, :status_reps, "прогоны     : ")
    _tr!(:ru, :status_lang, "язык        : ")
    _tr!(:ru, :status_nofile, "*** не найден ***  (положите .txt с нулями рядом со скриптом или нажмите [6])")
    _tr!(:ru, :opt1, "РЕЖИМ 1  NORMAL  — основной проход, прямой тест 34")
    _tr!(:ru, :opt2, "РЕЖИМ 2  HARDCORE — ансамбль, выбросы и устойчивость")
    _tr!(:ru, :opt3, "РЕЖИМ 3  ГЛУБОКАЯ ДИАГНОСТИКА — CDF, сиды, бутстреп, скейлинг")
    _tr!(:ru, :opt4, "РЕЖИМ 4  КОНФИГУРАТОР ВИХРЕЙ — свип + карта стабилизации")
    _tr!(:ru, :menu_zeros, "Нули: выбрать файл / количество нулей")
    _tr!(:ru, :menu_model, "Модель: L, Nv, q, alpha, W, окно")
    _tr!(:ru, :menu_runs, "Прогоны: реализации, сиды, свип, графики")
    _tr!(:ru, :menu_lang, "Язык / Language")
    _tr!(:ru, :menu_rescan, "Пересканировать каталог нулей")
    _tr!(:ru, :menu_selftest, "Самотест")
    _tr!(:ru, :menu_help, "Справка о тесте 34")
    _tr!(:ru, :menu_exit, "Выход из меню")
    _tr!(:ru, :opt5, "РЕЖИМ 5  UNIVERSAL — все геометрии x 4 теста x 3 реализации")
    _tr!(:ru, :m5_name, "УНИВЕРСАЛЬНЫЙ ПРОГОН ГЕОМЕТРИЙ")
    _tr!(:ru, :m5_sub, "все геометрии x тесты 1–4 x по N реализаций")
    _tr!(:ru, :m5_summary, "УНИВЕРСАЛЬНАЯ СВОДКА (объединённые вердикты)")
    _tr!(:ru, :m5_verdict, "УНИВЕРСАЛЬНЫЙ ВЕРДИКТ")
    _tr!(:ru, :m5_subtests, "подтестов «геометрия x тест» согласуются с GUE")
    _tr!(:ru, :m5_universal_ok, "конвейер теста 34 универсален по геометриям")
    _tr!(:ru, :menu_geometry, "Геометрия: поверхность для прогонов (тор, Кляйн, Гурвиц PSL(2,q), ...)")
    _tr!(:ru, :geo_title, "ГЕОМЕТРИЯ / ПОВЕРХНОСТЬ  (действует для всех режимов)")
    _tr!(:ru, :geo_selected, "выбрана геометрия")
    _tr!(:ru, :geo_stay, "оставить текущую геометрию")
    _tr!(:ru, :geo_L_note, "L автоматически скорректирована для геометрии:")
    _tr!(:ru, :geo_L_ignored, "L не применяется (растяжение ВЫКЛ, |G| фиксирован)")
    _tr!(:ru, :geo_fixed_short, " [фикс.]")
    _tr!(:ru, :geo_stretched, "растяжение")
    _tr!(:ru, :mstretch_head, "Растяжение Гурвица:")
    _tr!(:ru, :tag_stretch, "растяжение ВКЛ")
    _tr!(:ru, :tag_stretch_off, "растяжение ВЫКЛ — фиксированный размер")
    _tr!(:ru, :tag_stretch_na, "уже ≈ L² — lift не нужен")
    _tr!(:ru, :tag_fixed_by_math, "фиксирован математикой")
    _tr!(:ru, :tag_not_applied, "не применяется")
    _tr!(:ru, :tag_sites, "узлов")
    _tr!(:ru, :tag_autoscale_off, "исторические размеры")
    _tr!(:ru, :model_L_cayley_a, "Поверхность Гурвица: |G| = ")
    _tr!(:ru, :model_L_cayley_b, " — растяжение ВЫКЛ (autoscale OFF), матрица остаётся на фиксированном |G| (запрошенный бюджет L² = ")
    _tr!(:ru, :model_L_cayley_c, "). Включите autoscale (меню [8] → [a]), чтобы растянуть ×7, ×14, … до ≈ L².")
    _tr!(:ru, :model_L_autoscale_off_hint, "автоскейл ВЫКЛ — геометрия считается в историческом (малом) размере; включите его в меню [8] → [a]")
    _tr!(:ru, :warn_matrix_head, "РАЗМЕР МАТРИЦЫ:")
    _tr!(:ru, :warn_matrix_sites, "узлов")
    _tr!(:ru, :warn_matrix_of_budget, "от бюджета")
    _tr!(:ru, :warn_matrix_reason_cayley, "лестница растяжения Гурвица идёт шагами ×7 — так сохраняется поток гептагонов 2*pi*q*alpha*Nv — и это L попадает между шагами.")
    _tr!(:ru, :warn_matrix_hint_cayley, "Шаги дают |G|·k узлов для k = 1, 7, 14, … — подберите L так, чтобы L² ≈ |G|·k, либо примите ближайший шаг (большие L двигают к следующему шагу).")
    _tr!(:ru, :warn_matrix_reason_autoscale_off, "автоскейл ВЫКЛ: геометрия считается в историческом (малом) размере.")
    _tr!(:ru, :warn_matrix_hint_autoscale, "Включите его в меню [8] → [a] (или CLI --autoscale=on), чтобы считать ≈ L² узлов.")
    _tr!(:ru, :geo_autoscale, "Автоскейл большой матрицы — каждая геометрия растягивается к ≈ L² узлов (96 → ~9200; Гурвиц — лестницей ×7)")
    _tr!(:ru, :geo_autoscale_on, "ВКЛ — Кляйн/подушка масштабируются к 136×136 (9248 узлов), куб к L=40 (9128) при L=96; Гурвиц группы растягиваются ×7, ×14, … к L² (psl27 → ×56 = 9408 при L=96)")
    _tr!(:ru, :geo_autoscale_off, "ВЫКЛ — исторические ограничения (куб ≤ 12, fold n = L²/2)")
    _tr!(:ru, :status_geometry, "геометрия   : ")
    _tr!(:ru, :runs_reps5, "реализаций в РЕЖИМЕ 5 (на тест и геометрию)")
    _tr!(:ru, :menu_open_hint, "открываю интерактивное меню — введите номер и нажмите Enter ...")
    _tr!(:ru, :menu_select, "Выберите и нажмите Enter:")
    _tr!(:ru, :invalid_choice, "неизвестный пункт")
    _tr!(:ru, :menu_error, "ошибка")
    _tr!(:ru, :bye, "меню закрыто — открыть снова: main_menu()")
    _tr!(:ru, :zeros_title, "ИСТОЧНИК НУЛЕЙ")
    _tr!(:ru, :zeros_none, "в каталоге скрипта не найдено файлов, похожих на нули Римана.")
    _tr!(:ru, :zeros_none_hint, "положите файл нулей (напр. zeros_100k.txt, по одной гамме в строке) рядом с finite-size_lab.jl и пересканируйте.")
    _tr!(:ru, :zeros_found, "Обнаруженные файлы нулей")
    _tr!(:ru, :zeros_manual, "ввести путь вручную")
    _tr!(:ru, :zeros_path_prompt, "путь к файлу нулей:")
    _tr!(:ru, :zeros_bad_path, "файл не найден или не похож на нули Римана")
    _tr!(:ru, :zeros_selected, "выбрано")
    _tr!(:ru, :zeros_count_title, "СКОЛЬКО НУЛЕЙ использовать")
    _tr!(:ru, :available, "доступно")
    _tr!(:ru, :zeros_count_all, "использовать ВСЕ доступные")
    _tr!(:ru, :zeros_count_custom, "своё число")
    _tr!(:ru, :zeros_count_prompt, "количество нулей:")
    _tr!(:ru, :zeros_count_set, "нулей будет использовано")
    _tr!(:ru, :model_title, "ПАРАМЕТРЫ МОДЕЛИ")
    _tr!(:ru, :model_L, "сторона решётки L (L x L узлов)")
    _tr!(:ru, :model_L_warn, "нестандартное L — допустимы: 32 48 64 80 96 112 128 144 (запуск возможен)")
    _tr!(:ru, :model_mem_warn, "большая решётка — оценка памяти")
    _tr!(:ru, :model_Nv, "число AB-вихрей Nv (0 = чистый Андерсон)")
    _tr!(:ru, :model_q, "заряд q (множитель потока)")
    _tr!(:ru, :model_alpha, "поток на вихрь alpha (0..1, в квантах потока)")
    _tr!(:ru, :model_W, "беспорядок W")
    _tr!(:ru, :model_window, "доля центрального окна спектра")
    _tr!(:ru, :runs_title, "НАСТРОЙКИ ПРОГОНОВ")
    _tr!(:ru, :runs_reps1, "реализаций в РЕЖИМЕ 1")
    _tr!(:ru, :runs_reps2, "реализаций в РЕЖИМЕ 2")
    _tr!(:ru, :runs_reps3, "форензика сидов в РЕЖИМЕ 3 (число запусков)")
    _tr!(:ru, :runs_reps4, "реализаций на точку свипа в РЕЖИМЕ 4")
    _tr!(:ru, :runs_sweep, "параметр свипа РЕЖИМА 4")
    _tr!(:ru, :runs_seed, "база сидов")
    _tr!(:ru, :runs_plots, "строить графики")
    _tr!(:ru, :runs_nchunks, "число чанков спектра (гранулярность прогресса)")
    _tr!(:ru, :runs_reps5, "реализаций в РЕЖИМЕ 5 (на тест и геометрию)")
    _tr!(:ru, :lang_title, "ЯЗЫК / LANGUAGE")
    _tr!(:ru, :help_title, "О ТЕСТЕ 34")
    _tr!(:ru, :help_text, [
        "Тест 34 сравнивает спектр AB-cloud с нулями дзета Римана:",
        "  * развёртка обоих спектров (log-density unfolding),",
        "  * двухвыборочный KS: D и p по развёрнутым расщеплениям,",
        "  * парная корреляция Монтгомери R2(s) против теории GUE и Пуассона,",
        "  * d_GUE / d_Pois — KS-расстояние до закона GUE / Пуассона,",
        "  * композитный вердикт: (p>0.01 ИЛИ D<0.10) И d_GUE<d_Pois",
        "    И плато(R2, 1.0..2.0) в [0.75, 1.25].",
        "",
        "При N ~ 1e5 p-значения всегда ~0 — судите по D (эффект-размер).",
        "",
        "ГЕОМЕТРИИ (меню [8], действуют во всех режимах):",
        "  torus  - плоская периодическая решётка (исходная модель), род 1,",
        "  klein  - бутылка Кляйна (пары вихрь-антивихрь),",
        "  pillow - орбиобраз T^2/(x~-x), сфера с 4 коническими точками,",
        "  cubic  - куб-сфера, квад-сетка 6L^2-12L+8 узлов,",
        "  psl27  - квартика Кляйна,   PSL(2,7),  |G|=168,  g=3,  ГУРВИЦ",
        "  psl28  - поверхность Макбита, PSL(2,8),  |G|=504,  g=7,  ГУРВИЦ",
        "  psl213 - Фрике–Клейн,      PSL(2,13), |G|=1092, g=14, ГУРВИЦ",
        "  psl227 - Гурвиц-118,       PSL(2,27), |G|=9828, g=118, ГУРВИЦ",
        "           (БОЛЬШАЯ матрица Гурвица: ~9828 узлов ~ бюджет тора L=96",
        "           9216; уже ≈ L² — lift там не нужен)",
        "  Модель Гурвица: магнитный граф Кэли Cay(G;B,C), ord B=3, ord C=7;",
        "  поток через гептагон = 2*pi*q*alpha*Nv (тот же регулятор потока,",
        "  что и вихревое кольцо на торе).",
        "  РАСТЯЖЕНИЕ (v1.3): при autoscale ВКЛ каждая геометрия Гурвица",
        "  растягивается Z_k-накрытием: узлов = |G|·k, k = 7, 14, 21, ... —",
        "  шаг, ближайший к L² (psl27 при L=96: 168 × 56 = 9408 узлов).",
        "  Каждый гептагон накрытия несёт точный поток 2*pi*q*alpha*Nv;",
        "  связность накрытия проверяется явно. autoscale ВЫКЛ оставляет",
        "  исторический фиксированный |G|.",
        "  АВТОСКЕЙЛ большой матрицы (меню [8] -> [a]): каждая масштабируемая",
        "  геометрия считает ≈ L² узлов — при L=96 по умолчанию Кляйн/подушка",
        "  автоматически выходят на 136 (9248 узлов), куб-сфера на L=40",
        "  (9128 узлов) — ТА ЖЕ большая матрица, что и тор 96x96; никаких",
        "  маленьких прогонов на не-торических геометриях. Поверхности",
        "  Гурвица растягиваются Z_k-накрытием к ≈ L² узлов (шаги ×7).",
        "",
        "РЕЖИМ 1 NORMAL   - 5 реализаций, быстрая проверка.",
        "РЕЖИМ 2 HARDCORE - 20 реализаций, MAD-выбросы, leave-one-out.",
        "РЕЖИМ 3 DEEP     - где формируется D (дифференциал CDF), форензика сидов,",
        "                   бутстреп-ДИ, скейлинг решётки (адаптирован по геометрии).",
        "РЕЖИМ 4 SWEEP    - скан вихрей (alpha/Nv/q/W) с картой ЗОЛОТЫХ зон",
        "                   стабилизации (исследовательская подгонка).",
        "РЕЖИМ 5 UNIVERSAL - каждая геометрия x тесты 1–4 x по 3 реализации,",
        "                   один лёгкий проход, сводные вердикты + общий вердикт.",
        "",
        "Советы: запускайте julia с -t auto для живого прогресс-бара; файлы",
        "нулей (одна гамма в строке, формат 'n gamma' тоже подходит) кладите",
        "рядом со скриптом.",
    ])
    nothing
end
# =============================================================================
# BOOT: init, zeros auto-scan, menu-on-include, CLI arguments
# =============================================================================

function _parse_cli_and_run()::Bool
    has_mode = false
    lang_set = false
    for a in ARGS
        kv = split(a, '='; limit = 2)
        k = startswith(a, "--") ? String(kv[1])[3:end] : ""
        v = length(kv) == 2 ? String(kv[2]) : ""
        try
            k == "lang"   && (LAB.lang = Symbol(lowercase(v)); lang_set = true)
            k == "zeros"  && (cand = sniff_zeros_file(v);
                              if cand !== nothing
                                  LAB.zeros_file = cand.path
                                  LAB.zeros_avail = cand.count
                              end)
            k == "count"  && (LAB.n_zeros = something(tryparse(Int, v), LAB.n_zeros))
            k == "L"      && (LAB.L = something(tryparse(Int, v), LAB.L))
            k == "Nv"     && (LAB.Nv = something(tryparse(Int, v), LAB.Nv))
            k == "q"      && (LAB.q = something(tryparse(Float64, v), LAB.q))
            k == "alpha"  && (LAB.alpha = something(tryparse(Float64, v), LAB.alpha))
            k == "W"      && (LAB.W = something(tryparse(Float64, v), LAB.W))
            k == "reps"   && begin
                r = something(tryparse(Int, v), 0)
                r > 0 && (LAB.reps1 = r; LAB.reps2 = r; LAB.reps3seeds = min(r, 50);
                          LAB.reps4 = r; LAB.reps5 = r)
            end
            k == "reps5"  && (r = something(tryparse(Int, v), 0); r > 0 && (LAB.reps5 = r))
            k == "sweep"  && (s = Symbol(v); s in (:alpha, :Nv, :q, :W) && (LAB.sweep_param = s))
            k == "seed"   && (LAB.seed_base = something(tryparse(Int, v), LAB.seed_base))
            k == "geometry" && begin
                gid = Symbol(lowercase(v))
                if any(g -> g.id === gid, GEOMETRY_LIST)
                    GEOM[] = geom_by_id(gid)
                    LAB.geometry = gid
                end
            end
            k == "geom"   && begin
                gid = Symbol(lowercase(v))
                if any(g -> g.id === gid, GEOMETRY_LIST)
                    GEOM[] = geom_by_id(gid)
                    LAB.geometry = gid
                end
            end
            k == "geoms"  && begin
                list = GeometrySpec[]
                for tok in split(v, ',')
                    gid = Symbol(lowercase(strip(tok)))
                    any(g -> g.id === gid, GEOMETRY_LIST) && push!(list, geom_by_id(gid))
                end
                isempty(list) || (_CLI_GEOMS[] = list)
            end
            # BIG-MATRIX FIX (v1.1): --autoscale=on|off — scale every geometry
            # to the L^2 site budget (default ON) or keep the historical
            # per-geometry clamps.
            k == "autoscale" && (LAB.autoscale = lowercase(v) in ("on", "true", "yes", "1", "да"))
        catch
        end
    end
    if any(a -> a == "--selftest", ARGS)
        run_selftest()
        return true
    end
    for a in ARGS
        if startswith(a, "--mode=")
            m = something(tryparse(Int, String(split(a, '=')[2])), 0)
            if m in (1, 2, 3, 4, 5)
                has_mode = true
                m == 1 && run_mode1()
                m == 2 && run_mode2()
                m == 3 && run_mode3()
                m == 4 && run_mode4()
                m == 5 && run_mode5()
            end
        end
    end
    return has_mode
end

function _auto_boot()
    _i18n_init!()
    lab_load_settings()
    GEOM[] = geom_by_id(LAB.geometry)      # restore the geometry selected in a previous session
    LAB_TTY[] = (stdout isa Base.TTY)
    mkpath(LAB.out_root)
    println()
    lab_banner()
    println(cc("  " * t(:scan_scanning), C_GRY))
    rescan_zeros!(; quiet = true)
    if isempty(LAB_ZEROS_LIST[])
        println(cc("  ! " * t(:zeros_none), C_YLW))
        println(cc("    " * t(:zeros_none_hint), C_GRY))
    else
        for (i, c) in enumerate(LAB_ZEROS_LIST[])
            mark = c.path == LAB.zeros_file ? cc("<== " * t(:zeros_selected), C_GRN, C_B) : ""
            @printf(stdout, "  %s %s · %s zeros · %.4f ... %.1f  %s\n",
                    i == 1 ? "✓" : "·", basename(c.path), format_count(c.count), c.first, c.last, mark)
        end
    end
    println(cc("  " * t(:status_lang) * (LAB.lang === :en ? "English (default — change in menu [8] / Язык)" : "Русский"), C_GRY))
    println()
    # CLI?
    if !isempty(ARGS)
        _parse_cli_and_run()
        return nothing
    end
    # interactive menu when included in the REPL or run without arguments
    if isinteractive() || get(ENV, "LAB_NO_MENU", "0") != "1"
        println(cc("  " * t(:menu_open_hint), C_CYN, C_B))
        main_menu()
    end
    return nothing
end

# reopen the menu any time from the REPL:  Test34Lab()
Test34Lab = main_menu

_auto_boot()
