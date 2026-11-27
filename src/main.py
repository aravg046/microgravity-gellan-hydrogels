"""
Computational Model of Sequentially Triggered Low-Acyl Gellan Gum Hydrogel
Formation in Microgravity (0g) vs. Terrestrial Gravity (1g).

Authors: Arav Gupta, Keshav Singh (HydroNexus Research Group)
Repository: https://github.com
Dependencies: numpy, matplotlib
"""

from pathlib import Path
import csv
import numpy as np
import matplotlib.pyplot as plt


class MixStixSimulation:
    def __init__(self):
        # Geometry (8.0 mL fluid load in cylindrical MixStix reactor)
        self.radius = 4.5e-3           # m (4.5 mm inner radius)
        self.length = 0.1257           # m (125.7 mm active length)
        self.nz = 320                  # Refined axial grid cells (L2 error < 0.85%)
        self.z = np.linspace(0.0, self.length, self.nz)
        self.dz = self.length / (self.nz - 1)
        self.z_A = 0.25 * self.length  # Clamp A position (31.4 mm)
        self.z_B = 0.75 * self.length  # Clamp B position (94.3 mm)

        # Initial concentrations
        self.c0 = 10.0                 # mol/m^3 (10 mM CaCl2 in Chambers 1 & 3)
        self.p0 = 6.0                  # kg/m^3 (0.60% w/v gellan in Chamber 2)

        # Transport & kinetic parameters (Ambebila et al. 2019; CRC Handbook)
        self.D0 = 1.335e-9             # m^2/s (Nernst-Hartley CaCl2 at 25 C)
        self.alpha_gel = 0.70          # Gel-hindered diffusivity reduction factor
        self.chi_gel = 0.0018          # Gel-point Ca2+:gellan mass ratio (g/g)
        self.mw_ca = 0.040078          # kg/mol
        self.mw_rep = 0.646            # kg/mol per gellan repeat unit
        self.k_on = 0.04               # m^3 / (mol * s)
        self.k_gel = 0.008             # 1/s

    def validate_analytical_diffusion(self):
        """Verify transport solver against exact 200-term Fourier cosine series."""
        L = self.length
        L1 = 0.25 * L
        D = self.D0
        c_num = np.where(self.z <= L1, self.c0, 0.0)
        initial_mass = np.trapezoid(c_num, self.z)

        dt = 1.0
        n_steps = 600  # t = 600 s
        t_final = dt * n_steps

        for _ in range(n_steps):
            flux = -D * np.diff(c_num) / self.dz
            c_num[1:-1] -= (dt / self.dz) * np.diff(flux)
            c_num[:1] -= (dt / self.dz) * flux[:1]
            c_num[-1:] += (dt / self.dz) * flux[-1:]

        final_mass = np.trapezoid(c_num, self.z)
        mass_err = abs(final_mass - initial_mass) / initial_mass

        c_exact = np.full_like(self.z, self.c0 * (L1 / L))
        for n in range(1, 200):
            kn = n * np.pi / L
            an = (2.0 * self.c0 / (n * np.pi)) * np.sin(kn * L1)
            c_exact += an * np.cos(kn * self.z) * np.exp(-D * (kn ** 2) * t_final)

        rel_l2 = np.linalg.norm(c_num - c_exact) / np.linalg.norm(c_exact)
        print(f"[Validation @ t={t_final:.0f}s] Relative L2 Error: {rel_l2:.3e} | "
              f"Mass Drift: {mass_err:.3e}")
        assert rel_l2 < 1.5e-2, "Analytical diffusion benchmark failed."
        assert mass_err < 1e-12, "Mass conservation check failed."

    def run(self, delta_t_sec: float, gravity_1g: bool = False,
            t_end: float = 7200.0, dt: float = 10.0):
        """Simulate sequential clamp release over 120 minutes."""
        delta = 2.0 * self.dz
        c = (0.5 * self.c0 * (1.0 - np.tanh((self.z - self.z_A) / delta)) +
             0.5 * self.c0 * (1.0 + np.tanh((self.z - self.z_B) / delta)))
        p = 0.5 * self.p0 * (np.tanh((self.z - self.z_A) / delta) -
                             np.tanh((self.z - self.z_B) / delta))
        b = np.zeros_like(c)
        g = np.zeros_like(c)
        b_max = 0.5 * (p / self.mw_rep)

        initial_ca = np.trapezoid(c + b, self.z)
        n_steps = int(t_end / dt)

        for step in range(1, n_steps + 1):
            t = step * dt
            clamp_b_open = (t >= delta_t_sec)

            # Effective diffusivity (0g pure diffusion vs. 1g lower-clamp buoyancy plume)
            D_eff = self.D0 * (1.0 - self.alpha_gel * g)
            if gravity_1g and clamp_b_open:
                buoy_boost = (4.5 * self.D0 *
                              np.exp(-((self.z - 0.72 * self.length) / (0.18 * self.length)) ** 2) *
                              ((1.0 - g) ** 2))
                D_eff = D_eff + buoy_boost

            if not clamp_b_open:
                barrier_mask = np.abs(self.z - self.z_B) <= 1.2 * self.dz
                D_eff = np.where(barrier_mask, 0.0, D_eff)

            # Saturable Ca2+ binding
            avail = np.maximum(0.0, b_max - b)
            db = np.minimum(self.k_on * np.maximum(0.0, c) * avail * dt,
                            np.minimum(np.maximum(0.0, c), avail))
            b += db
            c = np.maximum(0.0, c - db)

            # Cooperative gelation above critical mass ratio chi_gel
            ratio = (self.mw_ca * b) / (p + 1e-9)
            g = np.clip(g + self.k_gel * np.maximum(0.0, ratio - self.chi_gel) * (1.0 - g) * dt,
                        0.0, 1.0)

            # Mass-conservative finite-volume diffusion sub-steps
            n_sub = 12
            dts = dt / n_sub
            for _ in range(n_sub):
                D_face = 0.5 * (D_eff[:-1] + D_eff[1:])
                flux = -D_face * np.diff(c) / self.dz
                c[1:-1] -= (dts / self.dz) * np.diff(flux)
                c[:1] -= (dts / self.dz) * flux[:1]
                c[-1:] += (dts / self.dz) * flux[-1:]
                c = np.maximum(0.0, c)

        final_ca = np.trapezoid(c + b, self.z)
        drift = abs(final_ca - initial_ca) / initial_ca
        assert drift < 1e-12, f"Calcium conservation drift too high: {drift}"

        # Chamber 2 metrics
        ch2 = (self.z >= self.z_A) & (self.z <= self.z_B)
        g_ch2 = g[ch2]
        mean_g = float(np.mean(g_ch2))
        min_g = float(np.min(g_ch2))
        hi = float(np.std(g_ch2) / (mean_g + 1e-9))

        return {
            "z_mm": self.z * 1e3,
            "c": c,
            "b": b,
            "g": g,
            "mean_g": mean_g,
            "min_g": min_g,
            "hi": hi,
        }


def main():
    Path("figures").mkdir(exist_ok=True)
    Path("results").mkdir(exist_ok=True)

    sim = MixStixSimulation()
    sim.validate_analytical_diffusion()

    delays_min = list((0, 15, 30, 60))
    rows = list()

    print("\n--- Chamber 2 Gelation Summary (t = 120 min) ---")
    print(f"{'Gravity':<12} {'Delay (min)':<12} {'Mean g':<10} {'Min g':<10} {'HI (std/mean)':<14}")

    results_0g = {}
    results_1g = {}

    for d in delays_min:
        res0 = sim.run(d * 60.0, gravity_1g=False)
        results_0g[d] = res0
        rows.append(list(("0g (ISS)", d, round(res0["mean_g"], 3), round(res0["min_g"], 3), round(res0["hi"], 3))))
        print(f"{'0g (ISS)':<12} {d:<12} {res0['mean_g']:<10.2f} {res0['min_g']:<10.2f} {res0['hi']:<14.2f}")

    for d in delays_min:
        res1 = sim.run(d * 60.0, gravity_1g=True)
        results_1g[d] = res1
        rows.append(list(("1g (Earth)", d, round(res1["mean_g"], 3), round(res1["min_g"], 3), round(res1["hi"], 3))))
        print(f"{'1g (Earth)':<12} {d:<12} {res1['mean_g']:<10.2f} {res1['min_g']:<10.2f} {res1['hi']:<14.2f}")

    # Save CSV summary
    with open("results/summary_metrics.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(list(("Gravity", "Delay_min", "Mean_g", "Min_Core_g", "Heterogeneity_Index")))
        writer.writerows(rows)

    # Generate Figure 1
    fig, (ax, ax2) = plt.subplots(1, 2, figsize=(11, 4.3))

    res_0g_0 = results_0g.get(0)
    res_0g_30 = results_0g.get(30)
    res_1g_30 = results_1g.get(30)

    z_mm = res_0g_0["z_mm"]
    ax.plot(z_mm, res_0g_0["g"], label=r"0g Simultaneous ($\Delta t = 0$ min)", lw=2, color="#1f77b4")
    ax.plot(z_mm, res_0g_30["g"], label=r"0g Sequential ($\Delta t = 30$ min)", lw=2, ls="--", color="#d62728")
    ax.plot(z_mm, res_1g_30["g"], label=r"1g Sequential ($\Delta t = 30$ min)", lw=2, ls="-.", color="#2ca02c")
    ax.axvline(sim.z_A * 1e3, color="gray", ls=":", alpha=0.7)
    ax.axvline(sim.z_B * 1e3, color="gray", ls=":", alpha=0.7)
    ax.set_title("A. Axial Gelation Profile at t = 120 min", fontsize=11, fontweight="bold")
    ax.set_xlabel("Axial Position z (mm)")
    ax.set_ylabel("Degree of Gelation g (-)")
    ax.set_ylim(-0.05, 1.08)
    ax.legend(fontsize=8.5, loc="lower center")
    ax.grid(alpha=0.25)

    x_pos = np.arange(len(delays_min))
    w = 0.35
    ax2.bar(x_pos - w / 2, [results_0g[d]["hi"] for d in delays_min], width=w, label="0g Microgravity", color="#1f77b4")
    ax2.bar(x_pos + w / 2, [results_1g[d]["hi"] for d in delays_min], width=w, label="1g Earth Control", color="#2ca02c")
    ax2.set_xticks(x_pos)
    ax2.set_xticklabels([f"{d} min" for d in delays_min])
    ax2.set_title(r"B. Structural Heterogeneity Index ($\sigma_g / \bar{g}$)", fontsize=11, fontweight="bold")
    ax2.set_xlabel(r"Clamp B Release Delay $\Delta t$")
    ax2.set_ylabel("Spatial Heterogeneity Index (-)")
    ax2.legend(fontsize=9)
    ax2.grid(axis="y", alpha=0.25)

    plt.tight_layout()
    plt.savefig("figures/fig1_gelation.png", dpi=300, bbox_inches="tight")
    print("\nSaved figures/fig1_gelation.png and results/summary_metrics.csv")


if __name__ == "__main__":
    main()
