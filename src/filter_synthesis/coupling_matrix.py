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


def similarity_transform(n: int, i: int, j: int, theta: int) -> np.ndarray:
    """
    Generates the nxn similarity transform with parameters [i,j,theta]

    Parameters
    ----------
    n: size of matrix nxn
    i: pivot row
    j: pivot column
    theta: pivot angle

    Returns
    ----------
    R : np.ndarray corresponding to the nxn similarity transform with parameters [i,j,theta]
    """

    if (i == j) or (max(i, j) >= n - 1) or (min(i, j) <= 0):
        raise RuntimeError("Invalid pivot")

    R = np.identity(n)
    s_theta = np.sin(theta)
    c_theta = np.cos(theta)

    R[i][i] = c_theta
    R[j][j] = c_theta
    R[i][j] = -s_theta
    R[j][i] = s_theta

    return R

