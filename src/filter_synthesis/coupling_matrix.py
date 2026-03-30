import numpy as np


def coupling_matrix_from_g(g):

    N = len(g)

    M = np.zeros((N, N))

    for i in range(N-1):

        coupling = 1 / np.sqrt(g[i] * g[i+1])

        # Apply correct scaling to source/load couplings
        if i == 0 or i == N-2:
            coupling *= np.sqrt(2)

        M[i,i+1] = coupling
        M[i+1,i] = coupling

    return M
