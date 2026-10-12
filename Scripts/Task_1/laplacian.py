import numpy as np

def laplacian(u,dx):
    return ((
        np.roll(u,1,0)+np.roll(u,-1,0)+ #np.roll acts as the shift like in the equation, for example np.roll(u,1,0) = f(x,y+1)
        np.roll(u,1,1)+np.roll(u,-1,1) 
        -4*u)/ dx**2
    )