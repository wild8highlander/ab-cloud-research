# debug_bl4.jl — изолированная диагностика Householder-программы E18
include(joinpath(@__DIR__, "e18_baselines.jl"))
using .E18Baselines
using LinearAlgebra

d = 4
U = ComplexF64[cis(2π * j * k / 4) / 2 for j in 0:3, k in 0:3]   # DFT4
V4, nab2, nph, off, nrefl = E18Baselines.householder_program(U)
println("DFT4: 1-F = ", max(0.0, 1 - E18Baselines.fidelity18(U, V4)),
        "  n_ab2=", nab2, " n_ph=", nph, " off=", off, " nrefl=", nrefl)

# Ручное воспроизведение: V_manual = H1' H2' H3' D
R = copy(U)
Hs = Matrix{ComplexF64}[]
for k in 1:d-1
    a = Vector{ComplexF64}(R[k:end, k])
    m = length(a)
    nrm = norm(a)
    α = -(iszero(a[1]) ? 1.0 + 0im : a[1] / abs(a[1])) * nrm
    v = a .- α
    println("k=", k, "  ‖v‖=", norm(v), "  nrm=", nrm)
    norm(v) < 1e-13 * max(1.0, nrm) && continue
    H = Matrix{ComplexF64}(I, m, m)
    H .-= 2 .* (v * v') ./ dot(v, v)
    println("   H*a - αe1 = ", norm(H * a .- α .* [1.0; zeros(m-1)]))
    E = Matrix{ComplexF64}(I, d, d)
    E[k:end, k:end] .= H
    push!(Hs, E)
    R[k:end, :] = H * R[k:end, :]
end
println("R после всех H (должна быть диагональ): off=", norm(R - Diagonal(diag(R)), Inf))
Vman = Matrix{ComplexF64}(I, d, d)
for E in Hs
    Vman = Vman * E'
end
dph = [iszero(R[i, i]) ? 1.0 + 0im : R[i, i] / abs(R[i, i]) for i in 1:d]
Vman = Vman * Diagonal(dph)
println("V_manual: 1-F = ", max(0.0, 1 - abs(tr(U' * Vman))^2 / d^2))
println("‖V4 - Vman‖ = ", norm(V4 - Vman))
