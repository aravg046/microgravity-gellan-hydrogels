# Microgravity and Gellan Gum Hydrogels (HydroNexus)

**Authors:** Arav Gupta, Keshav Singh  
**Research Group:** HydroNexus Research Group  
**Target Venue:** *Gravitational and Space Research* (ASGSR)

Computational modeling of sequentially triggered low-acyl gellan gum ($0.60\%\text{ w/v}$, $4\text{ mL}$) hydrogel formation crosslinked with flanking $\text{CaCl}_2$ ($10\text{ mM}$, $2\text{ mL}$ each) doses inside a three-chamber MixStix flight reactor under microgravity ($0g$) and terrestrial gravity ($1g$).

## Key Findings

- **Stoichiometric Calcium Excess:** A single $20\text{ }\mu\text{mol}$ $\text{Ca}^{2+}$ dose supplies $0.0334\text{ g Ca}^{2+}/\text{g gellan}$ ($\approx 18.5\times$ the critical gelation threshold of $0.0018\text{ g/g}$), shifting sequential clamp actuation from bulk gelation initiation to spatial core–shell architecture control.
- **Microgravity ($0g$) Core–Shell Tunability:** Increasing Clamp B release delay $\Delta t$ from $0\text{ min}$ to $60\text{ min}$ over a $120\text{ min}$ reaction horizon increases the axial heterogeneity index ($\sigma_g / \bar{g}$) from $2.05$ to $2.46$ while reducing crosslinked shell thickness ($g \ge 0.50$) from $11.39\text{ mm}$ to $8.25\text{ mm}$.
- **Terrestrial ($1g$) Buoyancy Homogenization:** Because $0.60\%\text{ w/v}$ gellan sol ($999.40\text{ kg/m}^3$) is denser than $10\text{ mM CaCl}_2$ ($997.98\text{ kg/m}^3$), buoyant overturning at the lower clamp interface doubles crosslinked shell thickness at $\Delta t = 30\text{ min}$ ($18.46\text{ mm}$ in $1g$ vs. $9.82\text{ mm}$ in $0g$) and lowers spatial heterogeneity from $2.23$ to $1.50$.

## Quick Start

```bash
pip install numpy matplotlib
python src/main.py
```

Running `src/main.py` automatically:
1. Verifies the finite-volume transport solver against the exact 200-term analytical Fourier cosine series ($L_2$ error $= 0.084\%$, mass drift $< 10^{-15}$).
2. Executes the parameter sweep across clamp-release delays $\Delta t \in \{0, 15, 30, 60\}\text{ min}$ for $0g$ and $1g$.
3. Generates `figures/fig1_gelation.png` and `results/summary_metrics.csv`.

## Repository Structure

- `paper/main.tex` — Publication-ready LaTeX manuscript
- `paper/HydroNexus_Gellan_Microgravity.pdf` — Compiled PDF manuscript
- `src/main.py` — Self-contained simulation, analytical validation, and plotting script
- `figures/fig1_gelation.png` — Axial gelation profiles and structural heterogeneity index plots
- `results/summary_metrics.csv` — Quantitative Chamber 2 gelation metrics across $\Delta t$ and gravity regimes

## Citation

```bibtex
@article{gupta2026gellan,
  title={Computational Modeling of Sequentially Triggered Low-Acyl Gellan Gum Hydrogel Formation in Microgravity vs. Terrestrial Gravity},
  author={Gupta, Arav and Singh, Keshav},
  year={2026},
  note={HydroNexus Research Group\(, \url{https://github.com}\)}
}
```
