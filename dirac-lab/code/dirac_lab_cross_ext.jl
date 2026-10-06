# =============================================================================
# AB-Cloud Dirac Laboratory — Julia cross-verification, EXTENSIONS (D9) — v1.1
# Independent re-implementation of the Jackiw–Rebbi domain-wall test on the
# grid Dirac operator. LinearAlgebra only (dense; reduced grid 48x48).
#
# Conventions match code/dirac_lab_extensions.py exactly:
#   H = vf(σx px + σy py) + m(y)·σx
#   (px)_{(x,y),(x+1,y)} = -i/(2dx), (py)_{(x,y),(x,y+1)} = -i/(2dx), open BC
#   spinor [c1; c2], C-order i = x*Ny + y, dx = 0.4, vf = 1, m0 = 0.8, w = 2.0
#   chiral Γ = diag(+1...+1, -1...-1); mass wall m(y) = m0·Π_k sgn_k·tanh((y-yc_k)/w)
#   with sgn_k = -1,+1,... (alternating, 0-based k) — two walls = index 2.
# =============================================================================
using LinearAlgebra

const DX = 0.4
const VF = 1.0
const M0 = 0.8
const WW = 2.0

function grid_dirac_wall(Nx::Int, Ny::Int, wall_ys::Vector{Float64})
    N = Nx * Ny
    H = zeros(ComplexF64, 2N, 2N)
    t = VF / (2DX)
    # σx·px: upper-right (c=1 <- c=2) gets px_{ij}; lower-left gets px_{ji}
    for x in 1:Nx-1, y in 1:Ny
        i = (x-1)*Ny + y; j = x*Ny + y
        H[i, N+j] += -1im * t
        H[N+j, i] += +1im * t
    end
    # σy·py: upper-right gets (σy)_{12}·py_{ij} = (-i)·(-i/(2dx)) = -1/(2dx)
    #        lower-left gets (σy)_{21}·py_{ji} = (+i)·(+i/(2dx)) = -1/(2dx)
    for x in 1:Nx, y in 1:Ny-1
        i = (x-1)*Ny + y; j = (x-1)*Ny + y + 1
        H[i, N+j] += -t
        H[N+j, i] += -t
    end
    # mass wall m(y)·σx (off-diagonal in σ ⇒ chiral symmetry exact)
    for x in 1:Nx, y in 1:Ny
        i = (x-1)*Ny + y
        m = M0
        for (k0, yc) in enumerate(wall_ys)
            sgn = (k0 % 2 == 1) ? -1.0 : 1.0     # 0-based even k → -1
            m *= sgn * tanh(((y-1)*DX - yc) / WW)
        end
        if isempty(wall_ys); m = 0.0; end
        H[i, N+i] += m
        H[N+i, i] += m
    end
    return H
end

function analyze(H::Matrix{ComplexF64}, Nx::Int, Ny::Int, tag::String)
    N = Nx * Ny
    G = diagm(vcat(fill(1.0, N), fill(-1.0, N)))
    ac = maximum(abs.(G * H + H * G))
    w = eigvals(Hermitian(H))          # real, ascending (Julia 1.13: no eigvalsh)
    e0 = minimum(abs.(w))
    nker = count(abs.(w) .< 1e-6)
    println("[$tag]  {H,Γ} = $(round(ac, sigdigits=2))   min|E| = $(round(e0, sigdigits=3))   n(|E|<1e-6) = $nker")
    return (ac=ac, e0=e0, nker=nker)
end

# ---- main: reduced 48x48 grid (dense diagonalization) ----
Nx = Ny = 40
println("Julia cross-check (extensions D9): grid $(Nx)x$(Ny), dx=$DX, m0=$M0, w=$WW")
H1 = grid_dirac_wall(Nx, Ny, [(Ny-1)*DX/2])
r1 = analyze(H1, Nx, Ny, "one wall (index 1)  ")
H2 = grid_dirac_wall(Nx, Ny, [(Ny-1)*DX/4, 3*(Ny-1)*DX/4])
r2 = analyze(H2, Nx, Ny, "two walls (index 2)")

ok1 = (r1.ac < 1e-10) && (r1.e0 < 1e-5) && (r1.nker >= 4)
ok2 = (r2.nker > r1.nker) && (r2.e0 < 1e-5)
println("\nCROSS-CHECK VERDICTS (Julia, extensions D9)")
println("  wall binds pinned chiral-pair multiplet: ", ok1 ? "PASS" : "FAIL",
        "  (n=", r1.nker, ", min|E|=", round(r1.e0, sigdigits=2), ")")
println("  kernel grows with the wall count:        ", ok2 ? "PASS" : "FAIL",
        "  (n: ", r1.nker, " -> ", r2.nker, ")")
println("  → ", (ok1 && ok2) ? "ALL PASS" : "MISMATCH — investigate")
