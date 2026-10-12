import numpy as np


def free_energy(c, kappa, dx=1.0):
    grad_x = (np.roll(c, -1, axis=0) - c) / dx
    grad_y = (np.roll(c, -1, axis=1) - c) / dx
    return (c**2 - 1) ** 2 / 4 + kappa / 2 * (grad_x**2 + grad_y**2)