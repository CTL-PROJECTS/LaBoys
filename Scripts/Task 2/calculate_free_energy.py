from pathlib import Path
import sys

import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from calculate_mass import calc_mass
from Task_1.laplacian import laplacian

def free_energy(c, kappa):
    free_energy = (c**2-1)**2/4 + kappa/2 * laplacian(c, 1.0)**2
    return free_energy