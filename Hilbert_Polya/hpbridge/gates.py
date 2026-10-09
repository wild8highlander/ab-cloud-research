"""hpbridge.gates — семейства затворов: протокольные 52 (C3) и расширенные
35+2 (C5). Списки заданы декларативно; спектры строит engine.solver."""
import itertools

LATTICE = 24

# ── C3: протокольное семейство 52 затворов (Nv × q × W × α) ────────────────
PROTOCOL_FAMILY = [
    dict(Nv=Nv, q=q, W=W, alpha=alpha)
    for Nv, q, W, alpha in itertools.product(
        (0, 2, 8, 16, 32), (0.5, 1.0), (0.0, 0.5, 1.0), (0.4, 0.5))
]
# точный список 52 повторяет CSV data/c3_gates_table.csv (дубли устранены)


# ── C5: расширенное семейство (6 новых ручек) ──────────────────────────────
BASE = dict(Nv=16, q=1.0, W=0.5, alpha=0.5)


def extended_family():
    """35 новых затворов + 2 декуя; каждая запись — (имя, overrides)."""
    G = []

    def add(name, **kw):
        G.append((name, {**BASE, **kw}))

    for aniso in (0.8, 1.25):
        add(f'A_aniso{aniso}', aniso=aniso)
    for da in (-0.02, 0.02):
        add(f'A_dalpha{da:+.2f}', dalpha=da)
    for m in (0.15, 0.35):
        add(f'A_mass{m}', mass=m)
    add('A_profile_midpoint', profile='midpoint')
    add('A_signs_allplus', signs='all_plus')
    add('A_aniso08_dalpha+0.02', aniso=0.8, dalpha=0.02)
    add('A_aniso125_mass0.15', aniso=1.25, mass=0.15)
    add('A_mass0.15_dalpha-0.02', mass=0.15, dalpha=-0.02)
    add('A_midpoint_allplus', profile='midpoint', signs='all_plus')
    add('B_torus_base', bc='torus')
    add('B_twist3_0', bc='torus', twist=(3.141592653589793, 0.0))
    add('B_twist0_3', bc='torus', twist=(0.0, 3.141592653589793))
    add('B_twist3_3', bc='torus',
        twist=(3.141592653589793, 3.141592653589793))
    add('B_torus_aniso0.8', bc='torus', aniso=0.8)
    add('B_torus_aniso1.25', bc='torus', aniso=1.25)
    add('B_torus_dalpha+0.0417', bc='torus', dalpha=1.0 / 24)
    add('B_torus_dalpha-0.0417', bc='torus', dalpha=-1.0 / 24)
    add('B_torus_mass0.15', bc='torus', mass=0.15)
    add('B_torus_midpoint', bc='torus', profile='midpoint')
    add('B_torus_allplus', bc='torus', signs='all_plus')
    add('B_twistpi_pi_mass0.15', bc='torus',
        twist=(3.141592653589793, 3.141592653589793), mass=0.15)
    add('B_twistpi_pi_aniso1.25', bc='torus',
        twist=(3.141592653589793, 3.141592653589793), aniso=1.25)
    add('C_Nv8_allplus', Nv=8, signs='all_plus')
    add('C_Nv32_allplus', Nv=32, signs='all_plus')
    add('C_Nv16_random_signs', signs='random')
    add('C_q0.5_mass0.15', q=0.5, mass=0.15)
    add('C_q0.5_dalpha+0.02', q=0.5, dalpha=0.02)
    add('C_W0_mass0.15', W=0.0, mass=0.15)
    add('C_W0.1_midpoint', W=0.1, profile='midpoint')
    add('C_alpha0.4_allplus', alpha=0.4, signs='all_plus')
    add('C_alpha0.4_dalpha+0.02', alpha=0.4, dalpha=0.02)
    add('C_Nv64_midpoint', Nv=64, profile='midpoint')
    add('D_decoy_signs_random', signs='random')
    add('D_decoy_Nv32_random', Nv=32, signs='random')
    return G
