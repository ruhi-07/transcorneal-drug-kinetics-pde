import numpy as np
import matplotlib.pyplot as plt

# 1. Structural & Biological Parameters (Human Corneal Architecture)
L = 0.05             # Total thickness of central human cornea (cm) -> 500 Microns
Nx = 100             # Spatial grid resolution steps
dx = L / (Nx - 1)    # Spatial delta step size
x = np.linspace(0, L, Nx)

D = 3.2e-6           # Diffusion coefficient of topical drug in stroma matrix (cm^2/s)
k_el = 1.5e-4        # First-order physiological clearance rate via conjunctival vessels (1/s)

# 2. Temporal Discretization (Explicit Finite Difference Framework)
dt = 0.02            # Time step (seconds)
Nt = 15000           # Total iterations (Simulates exactly 300 seconds of saturation)

# 3. Boundary & Initial Conditions Setup
C = np.zeros(Nx)     # Cornea initialized with zero trace drug concentration
C_tear_film = 1.0    # Continuous drug concentration saturation threshold at tear film (x = 0)

# 4. Numerical Solver for Transient Diffusion-Loss PDE
C[0] = C_tear_film
for t in range(Nt):
    C_new = C.copy()
    C_new[1:-1] = C[1:-1] + dt * (D * (C[2:] - 2*C[1:-1] + C[:-2]) / (dx**2) - k_el * C[1:-1])
    C_new[0] = C_tear_film       # Epithelial drop contact interface
    C_new[-1] = C_new[-2]        # Endothelial barrier boundary condition
    C = C_new

# 5. Render Publication-Quality Visualization
plt.figure(figsize=(9, 5.5))
plt.plot(x * 10000, C, color='#1E88E5', linewidth=2.5, label='Topical Diffusion Front')
plt.title('Transcorneal Pharmacokinetics: 1D Transient Diffusion Model', fontsize=12, fontweight='bold', pad=15)
plt.xlabel('Corneal Depth from Tear Film Epithelium (Microns / μm)', fontsize=10)
plt.ylabel('Normalized Drug Concentration ($C / C_0$)', fontsize=10)
plt.axvspan(400, 500, color='#FFF59D', alpha=0.3, label='Endothelial End-Stage Permeation Target')
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend(loc='upper right', frameon=True, facecolor='white', edgecolor='none')
plt.tight_layout()

# Save locally
plt.savefig('transcorneal_diffusion.png', dpi=300)
plt.show()
