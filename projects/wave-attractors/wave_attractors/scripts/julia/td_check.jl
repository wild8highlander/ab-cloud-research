# td_check.jl — Julia cross-verification of the E7 time-domain kernel.
#
# Study W1 extension (Hyperbolic wave attractors, AB-Cloud Research).
#
# Implements the SAME leapfrog ADE-FDTD step as e7_time_domain.py
# (Drude-regularised hyperbolic medium), on a small square domain with
# Dirichlet boundaries, from a fixed Gaussian initial condition, and
# dumps field snapshots to CSV for pointwise comparison with the Python
# implementation (verify_td_cross.py).
#
# Determinism contract: the arithmetic per grid node is written in the
# SAME operation order as the numpy implementation, so a passing
# comparison (max |dE| ~ 1e-15) verifies the port bit-near-exactly.
#
# Usage:  julia td_check.jl <output_prefix>
#         (writes <prefix>_td_snapshots.csv)

function main()
    prefix = length(ARGS) >= 1 ? ARGS[1] : "julia_td"
    n = 48
    dx = 1.0 / (n - 1)
    dt = 0.3 * dx
    sigma = 0.01
    damp = exp(-sigma * dt)
    n_cells = 24
    omega_p = pi * n_cells
    omega_p2 = omega_p * omega_p
    dx2 = dx * dx

    # initial condition (same formula as Python side)
    E = zeros(n, n)
    chi = zeros(n, n)
    vE = zeros(n, n)
    vchi = zeros(n, n)
    for j in 1:n, i in 1:n
        x = (i - 1) * dx
        y = (j - 1) * dx
        E[i, j] = exp(-((x - 0.5)^2 + (y - 0.45)^2) / 1e-3)
    end

    snap_steps = [0, 100, 200, 300, 400]
    snaps = Dict{Int, Tuple{Matrix{Float64}, Matrix{Float64}}}()
    snaps[0] = (copy(E), copy(chi))

    function step_once(E, chi, vE, vchi)
        # padded arrays (Dirichlet halo)
        Ep = zeros(n + 2, n + 2)
        Ep[2:n+1, 2:n+1] .= E
        chip = zeros(n + 2, n + 2)
        chip[2:n+1, 2:n+1] .= chi
        lap = (Ep[3:n+2, 2:n+1] + Ep[1:n, 2:n+1] +
               Ep[2:n+1, 3:n+2] + Ep[2:n+1, 1:n] - 4.0 .* E) ./ dx2
        dx_e = (Ep[3:n+2, 2:n+1] - Ep[1:n, 2:n+1]) ./ (2.0 * dx)
        dx_chi = (chip[3:n+2, 2:n+1] - chip[1:n, 2:n+1]) ./ (2.0 * dx)
        vE_new = vE .* damp .+ dt .* (lap .+ dx_chi)
        vchi_new = vchi .* damp .- dt .* omega_p2 .* (chi .+ dx_e)
        E_new = E .+ dt .* vE_new
        chi_new = chi .+ dt .* vchi_new
        return (E_new, chi_new, vE_new, vchi_new)
    end

    for s in 1:400
        (E, chi, vE, vchi) = step_once(E, chi, vE, vchi)
        if s in snap_steps
            snaps[s] = (copy(E), copy(chi))
        end
    end

    out = prefix * "_td_snapshots.csv"
    open(out, "w") do f
        println(f, "step,i,j,E,chi")
        for s in snap_steps
            Es, chis = snaps[s]
            for j in 1:n, i in 1:n
                println(f, "$s,$i,$j,$(repr(Es[i, j])),$(repr(chis[i, j]))")
            end
        end
    end
    println("td_check: wrote $out (n=$n, steps=400, omega_p=$omega_p)")
end

main()
