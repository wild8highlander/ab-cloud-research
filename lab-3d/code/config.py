"""
config.py — Configuration system for the monograph verification suite.

Provides a Config dataclass with all adjustable parameters, loaded from
JSON config files. Users can create custom configs to run specific
chapters, adjust grid sizes, time horizons, etc.

Usage:
    from config import Config
    cfg = Config.default()          # default configuration
    cfg = Config.from_json("config/my_config.json")
    cfg.N_kdv = 2048                 # override individual parameters
    cfg.save_json("config/my_config.json")
"""
from __future__ import annotations

import json
from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import List, Optional


@dataclass
class Config:
    """Master configuration for the verification suite.

    All parameters are adjustable. The suite reads this config at startup
    and uses it to control every aspect of the verification: grid sizes,
    time steps, which chapters to run, output formats, etc.
    """

    # ===== Universal constants (from the monograph) =====
    b_universal: float = 0.0785
    theta_b_rad: float = 0.0785 * 3.141592653589793 / 2.0  # b·π/2
    theta_b_deg: float = 0.0785 * 180.0 / 2.0               # in degrees
    beta_K: float = 5.0 / 3.0                               # Kolmogorov exponent
    L_min_klein: float = 2.0 * 2.89815                      # Klein geodesic length
    alpha_klein: float = 1.0 + 2.0 * (3.141592653589793 / 7.0).__cos__() if hasattr(float, '__cos__') else 2.246979603717467
    C_K_predicted: float = 1.5
    C_s_lilly: float = 0.17327
    golden_ratio: float = 1.618033988749895
    euler_e: float = 2.718281828459045

    # ===== KdV solver parameters =====
    N_kdv: int = 1024              # grid points for KdV
    L_kdv: float = 100.0           # domain length
    dt_kdv: float = 0.002          # time step
    T_kdv_short: float = 10.0      # short simulation
    T_kdv_long: float = 50.0       # long simulation
    c_soliton: float = 0.5         # soliton parameter
    c1_collision: float = 0.8      # fast soliton
    c2_collision: float = 0.4      # slow soliton

    # ===== mKdV parameters =====
    N_mkdv: int = 512
    L_mkdv: float = 100.0
    dt_mkdv: float = 0.002
    T_mkdv: float = 10.0

    # ===== BBM parameters =====
    N_bbm: int = 512
    L_bbm: float = 100.0
    dt_bbm: float = 0.002
    T_bbm: float = 10.0
    c_bbm: float = 0.5

    # ===== Kawahara parameters =====
    N_kawahara: int = 512
    L_kawahara: float = 100.0
    dt_kawahara: float = 0.002
    T_kawahara: float = 10.0

    # ===== KP (2D) parameters =====
    Nx_kp: int = 192
    Ny_kp: int = 64
    Lx_kp: float = 80.0
    Ly_kp: float = 30.0
    dt_kp: float = 0.005
    T_kp: float = 8.0
    sigma_sq_kp: float = 1.0       # +1 for KP-II, -1 for KP-I

    # ===== 3D NSE parameters =====
    N_nse3d: int = 32
    L_nse3d: float = 6.283185307179586  # 2π
    dt_nse3d: float = 0.008
    T_nse3d: float = 2.0
    nu_nse3d: float = 0.02
    ic_nse3d: str = "taylor_green"  # or "abc"

    # ===== Polchinski RG parameters =====
    n_rg_steps: int = 50
    theta_per_step: float = 0.0785 * 3.141592653589793 / 2.0 / 5.0  # θ_b/5
    rg_cutoff_factor: float = 1.0 / 3.0  # Λ = k_max/3

    # ===== Isospectral b parameters =====
    theta_scan_points: int = 25
    theta_scan_max: float = 4.0    # max multiplier of θ_b

    # ===== Angle scan parameters =====
    n_angles: int = 12

    # ===== Statistics parameters =====
    n_random_ic: int = 50

    # ===== Output control =====
    chapters_to_run: List[int] = field(default_factory=lambda: [0] + list(range(1, 17)))
    tasks_per_chapter: int = 15    # ~15 tasks × 16 chapters = 240 tasks
    save_figures: bool = True
    save_data: bool = True
    figure_dpi: int = 200
    figure_format: str = "png"     # png, svg, pdf

    # ===== Report formats =====
    report_formats: List[str] = field(default_factory=lambda: [
        "txt", "csv", "json", "md", "html"
    ])

    # ===== Paths =====
    output_dir: str = "/home/z/my-project/download/verification_suite"
    figures_dir: str = "figures"
    reports_dir: str = "reports"
    results_dir: str = "results"
    config_dir: str = "config"

    # ===== Verbosity =====
    verbose: bool = True
    timing: bool = True

    # ===== Random seed =====
    random_seed: int = 42

    @classmethod
    def default(cls) -> "Config":
        """Create default configuration."""
        import math
        cfg = cls()
        cfg.alpha_klein = 1.0 + 2.0 * math.cos(2.0 * math.pi / 7.0)
        cfg.theta_b_rad = cfg.b_universal * math.pi / 2.0
        cfg.theta_b_deg = math.degrees(cfg.theta_b_rad)
        cfg.L_min_klein = 2.0 * math.acosh(cfg.alpha_klein)
        return cfg

    @classmethod
    def from_json(cls, path: str) -> "Config":
        """Load configuration from JSON file."""
        with open(path, "r") as f:
            data = json.load(f)
        cfg = cls.default()
        for key, val in data.items():
            if hasattr(cfg, key):
                setattr(cfg, key, val)
        return cfg

    def save_json(self, path: str):
        """Save configuration to JSON file."""
        Path(path).parent.mkdir(parents=True, exist_ok=True)
        with open(path, "w") as f:
            json.dump(asdict(self), f, indent=2)

    def to_dict(self) -> dict:
        """Convert to dictionary."""
        return asdict(self)

    def summary(self) -> str:
        """Return a human-readable summary."""
        lines = [
            "=" * 60,
            "  VERIFICATION SUITE CONFIGURATION",
            "=" * 60,
            f"  b_universal    = {self.b_universal}",
            f"  θ_b            = {self.theta_b_deg:.4f}° ({self.theta_b_rad:.6f} rad)",
            f"  α (Klein)      = {self.alpha_klein:.6f}",
            f"  L_min          = {self.L_min_klein:.6f}",
            f"  β_K            = {self.beta_K:.6f}",
            f"  C_K            = {self.C_K_predicted}",
            f"  C_s (Lilly)    = {self.C_s_lilly}",
            f"  φ (golden)     = {self.golden_ratio:.6f}",
            "-" * 60,
            f"  KdV:  N={self.N_kdv}, L={self.L_kdv}, dt={self.dt_kdv}, T={self.T_kdv_long}",
            f"  mKdV: N={self.N_mkdv}, T={self.T_mkdv}",
            f"  BBM:  N={self.N_bbm}, T={self.T_bbm}",
            f"  Kaw:  N={self.N_kawahara}, T={self.T_kawahara}",
            f"  KP:   {self.Nx_kp}×{self.Ny_kp}, T={self.T_kp}",
            f"  NSE3D: N={self.N_nse3d}, ν={self.nu_nse3d}, T={self.T_nse3d}",
            f"  RG:   {self.n_rg_steps} steps",
            "-" * 60,
            f"  Chapters: {self.chapters_to_run}",
            f"  Tasks/chapter: {self.tasks_per_chapter}",
            f"  Total tasks: ~{len(self.chapters_to_run) * self.tasks_per_chapter}",
            f"  Figure DPI: {self.figure_dpi}",
            f"  Report formats: {self.report_formats}",
            "=" * 60,
        ]
        return "\n".join(lines)


# Preset configurations
PRESETS = {
    "quick": {
        "N_kdv": 256, "N_mkdv": 128, "N_bbm": 128, "N_kawahara": 128,
        "Nx_kp": 64, "Ny_kp": 32, "N_nse3d": 16,
        "T_kdv_short": 5.0, "T_kdv_long": 10.0,
        "T_mkdv": 5.0, "T_bbm": 5.0, "T_kawahara": 5.0,
        "T_kp": 3.0, "T_nse3d": 1.0,
        "n_rg_steps": 10, "n_random_ic": 10,
        "tasks_per_chapter": 8,
    },
    "standard": {},  # use defaults
    "high_res": {
        "N_kdv": 2048, "N_mkdv": 1024, "N_bbm": 1024, "N_kawahara": 1024,
        "Nx_kp": 384, "Ny_kp": 128, "N_nse3d": 64,
        "T_kdv_long": 100.0, "T_nse3d": 5.0,
        "n_rg_steps": 100, "n_random_ic": 100,
        "figure_dpi": 300,
        "nu_nse3d": 0.01,
    },
    "production": {
        "N_kdv": 4096, "N_mkdv": 2048, "N_bbm": 2048, "N_kawahara": 2048,
        "Nx_kp": 512, "Ny_kp": 256, "N_nse3d": 96,
        "T_kdv_long": 200.0, "T_nse3d": 10.0,
        "n_rg_steps": 200, "n_random_ic": 200,
        "figure_dpi": 300, "nu_nse3d": 0.005,
        "tasks_per_chapter": 20,
    },
}


def get_preset(name: str) -> Config:
    """Get a preset configuration by name."""
    cfg = Config.default()
    if name in PRESETS:
        for key, val in PRESETS[name].items():
            if hasattr(cfg, key):
                setattr(cfg, key, val)
    return cfg


if __name__ == "__main__":
    cfg = Config.default()
    print(cfg.summary())
    cfg.save_json("/home/z/my-project/download/verification_suite/config/default.json")
    print("\nSaved to config/default.json")

    # Also save presets
    for name in PRESETS:
        preset_cfg = get_preset(name)
        preset_cfg.save_json(f"/home/z/my-project/download/verification_suite/config/preset_{name}.json")
        print(f"Saved preset_{name}.json")
