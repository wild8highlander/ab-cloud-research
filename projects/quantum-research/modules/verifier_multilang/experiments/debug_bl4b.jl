# debug_bl4b.jl — точечная диагностика первого отражения
using LinearAlgebra

d = 4
U = ComplexF64[cis(2π * j * k / 4) / 2 for j in 0:3, k in 0:3]
println("U[:,1] = ", U[:, 1])
a = Vector{ComplexF64}(U[:, 1])
nrm = norm(a)
α = -(iszero(a[1]) ? 1.0 + 0im : a[1] / abs(a[1])) * nrm
println("a[1]=", a[1], "  |a[1]|=", abs(a[1]), "  a[1]/|a[1]|=", a[1] / abs(a[1]),
        "  nrm=", nrm, "  α=", α)
v = a .- α
println("v = ", v, "  ‖v‖=", norm(v), "  v†v=", dot(v, v), "  v†a=", dot(v, a))
H = Matrix{ComplexF64}(I, 4, 4)
H .-= 2 .* (v * v') ./ dot(v, v)
println("H*a = ", H * a, "   αe1 = ", α .* [1.0; 0.0; 0.0; 0.0])
println("‖H*a − αe1‖ = ", norm(H * a .- α .* [1.0; 0.0; 0.0; 0.0]))
