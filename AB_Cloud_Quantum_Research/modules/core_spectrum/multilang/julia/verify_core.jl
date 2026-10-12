# verify_core.jl — двойник Julia ≥ 1.9: Γ-замыкание + Λ-сито
using Printf
# Запуск: julia verify_core.jl [verify_control.txt]

function verify(N::Int = 100_000)
    maxres = 0.0
    for u in (0.5, 1.0, 2.0, 3.0)
        lhs = abs2(gamma(0.5 + u*im))
        rhs = pi / cosh(pi * u)
        maxres = max(maxres, abs(lhs - rhs) / rhs)
    end
    spf = zeros(Int, N)
    lsum = 0.0
    for i in 2:N
        if spf[i] == 0
            p = i
            while p <= N
                lsum += log(i) / p^1.5
                j = i
                while j <= N
                    if spf[j] == 0; spf[j] = i; end
                    j += i
                end
                p *= i
            end
        end
    end
    (maxres, lsum)
end

(maxres, lsum) = verify()
println("gamma_closure_max_res = $(Printf.@sprintf %.3e maxres)")
println("lambda_sum_check = $(Printf.@sprintf %.10f lsum)")
println("n_sieve = 100000")
if length(ARGS) >= 1
    open(ARGS[1], "w") do f
        println(f, "gamma_closure_max_res = $(Printf.@sprintf %.3e maxres)")
        println(f, "lambda_sum_check = $(Printf.@sprintf %.10f lsum)")
        println(f, "n_sieve = 100000")
    end
end
