from pathlib import Path
import sys

import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from calculate_mass import calc_mass
from Task_1.do_time_step import do_time_step

# ----------------------------------------------------
# Parameters
# ----------------------------------------------------
N = 128              # grid size
dx = 1.0
dt = 0.01

M = 1.0              # mobility
kappa = 1.0

steps = 5000
plot_every = 500

c = 0.05*np.random.randn(N, N)

if __name__ == "__main__":
    masses = np.zeros((steps))
    print(masses)
    for step in range(steps):
        current_mass = calc_mass(c)
        masses[step] = current_mass
        do_time_step(c, dx, dt, M, kappa)
    
    plt.plot(masses)
    plt.show()