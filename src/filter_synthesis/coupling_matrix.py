import numpy as np

def coupling_matrix_from_g(g: np.ndarray):
    """
    Constructs canonical coupling matrix from prototype values.
    
    Parameters
    ----------
    g : ndarray
        Prototype values g0...g(n+1)
    Returns
    ----------
    M : ndarray
        Coupling matrix (n + 2) x (n + 2)
    """

    N = len(g) - 2

    size = N + 2

    M = np.zeros((size, size))

    for i in range(size-1):
        coupling = 1/np.sqrt(g[i] * g[i+1])\
        
        M[i, i+1] = coupling
        M[i+1, i] = coupling
    return M