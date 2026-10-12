    #heavily inspired by the images/readme.md
from pathlib import Path
import sys
import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

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

# ----------------------------------------------------
# Initial condition
# ----------------------------------------------------
c = 0.05*np.random.randn(N, N) #random concentration field

#c = np.zeros((N, N))   #empty concentration field      
#c[N//2, N//2] = 1.0   #only one "seed" in the empty concentration field  
#c.fill(0.5)          #constant concentration field  

# ----------------------------------------------------
# Time integration
# ----------------------------------------------------
if __name__ == "__main__":
    plt.figure(figsize=(6,6))

    for step in range(steps):
        do_time_step(c, dx, dt, M, kappa) #does the actual calcualation
        #just plotting
        if step % plot_every == 0:
            plt.clf()
            plt.imshow(c,
                        cmap="RdBu",
                        origin="lower",
                        vmin=-1,
                        vmax=1)
            plt.title(f"Step {step}")
            plt.colorbar()
            plt.pause(0.01)

    plt.show()