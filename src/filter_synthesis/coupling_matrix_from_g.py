import numpy as np

def coupling_matrix_from_g(g):
    """
    Convert lowpass prototype g-values to coupling matrix.
    
    Parameters:
        g   : list of g-values [g0, g1, g2, ..., gN, g_{N+1}]
        BW  : fractional bandwidth
    
    Returns:
        M   : NxN coupling matrix
        qs : input external Q
        ql : output external Q
    """
    N = len(g) - 2  # number of resonators
    M = np.zeros((N, N))

    # Fill in inter-resonator couplings (off-diagonal)
    for i in range(N - 1):
        M[i, i+1] = 1.0 / np.sqrt(g[i+1] * g[i+2])
        M[i+1, i] = M[i, i+1]  # symmetric

    # External quality factors
    qs = (g[0] * g[1])
    ql = (g[N] * g[N+1])

    return M, qs, ql
