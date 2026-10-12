
import numpy as np
import matplotlib.pyplot as plt


def simulate(
    L=0.05,
    D=3.2e-6,
    k_el=1.5e-4,
    nx=101,
    duration=600.0,
    surface_concentration=1.0,
):
    """Solve a 1D diffusion-reaction PDE using explicit finite differences."""
    if L <= 0 or D <= 0 or k_el < 0 or duration <= 0:
        raise ValueError("Invalid physical parameters.")
    if nx < 3 or surface_concentration < 0:
        raise ValueError("Invalid grid or concentration.")

    x = np.linspace(0, L, nx)
    dx = x[1] - x[0]

    # Conservative timestep for a positive, stable scheme.
    dt_limit = 1.0 / (2.0 * D / dx**2 + k_el)
    nt = int(np.ceil(duration / (0.9 * dt_limit)))
    dt = duration / nt
    r = D * dt / dx**2

    C = np.zeros(nx)
    C[0] = surface_concentration

    times = [0.0]
    history = [C.copy()]

    sample_every = max(1, nt // 200)

    for step in range(1, nt + 1):
        old = C.copy()

        C[1:-1] = (
            old[1:-1]
            + r * (old[2:] - 2 * old[1:-1] + old[:-2])
            - k_el * dt * old[1:-1]
        )

        # Zero-flux posterior boundary using a reflected ghost node.
        C[-1] = (
            old[-1]
            + 2 * r * (old[-2] - old[-1])
            - k_el * dt * old[-1]
        )

        C[0] = surface_concentration

        if step % sample_every == 0 or step == nt:
            times.append(step * dt)
            history.append(C.copy())

    return x, np.array(times), np.array(history)


if __name__ == "__main__":
    x, times, concentrations = simulate()

    plt.figure(figsize=(9, 5))

    for target in [0, 30, 60, 120, 300, 600]:
        idx = np.argmin(np.abs(times - target))
        plt.plot(
            x * 1e4,
            concentrations[idx],
            label=f"{times[idx]:.0f} s"
        )

    plt.xlabel("Corneal depth (µm)")
    plt.ylabel("Normalised drug concentration")
    plt.title("Transient Transcorneal Drug Diffusion")
    plt.legend()
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig("concentration_profiles.png", dpi=200)
    plt.show()
