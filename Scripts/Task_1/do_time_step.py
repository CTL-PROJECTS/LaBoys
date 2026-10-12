from .laplacian import laplacian

def do_time_step(c, dx, dt, M, kappa):
    """
    Perform a single time step of the Cahn-Hilliard equation.

    Parameters:
    c : 2D numpy array
        The concentration field.
    dx : float
        The spatial grid spacing.
    dt : float
        The time step size.
    M : float
        The mobility parameter.
    kappa : float
        The gradient energy coefficient.

    Returns:
    c_new : 2D numpy array
        The updated concentration field after one time step.
    """
    
    # Compute the Laplacian of c
    lap_c = laplacian(c, dx)

        # chemical potential
    mu = c**3 - c - kappa*lap_c

        # Cahn-Hilliard equation
    c += dt * M * laplacian(mu, dx)
    return c