import numpy as np

def compute_sparameters(M,w)
    """
    Computes S11 and S21 from coupling matrix using Cameron's formulation.
    
    Parameters
    ----------
    M : ndarray
        Coupling matrix
    w : ndarray
        Frequency points (normalized)

    Returns
    -------
    S11 : ndarray
    S21 : ndarray
    """
    N = M.shape[0]

    I = np.eye(N)
    S11 = np.zeros(len(w), dtype = complex)
    S21 = np.zeros(len(w), dtype = complex)

    #Computation of S-parameters without using matrix inversion, but rather solving linear systems
    b1 = np.zeros(N, dtype=complex)
    b1[0] = 1

    b2 = np.zeros(N, dtype=complex)
    b2[N-1] = 1

    for i, omega in enumerate(w):

        A = 1j * omega * I - M

        x1 = np.linalg.solve(A, b1)
        x2 = np.linalg.solve(A, b2)

        S11[i] = 1 - 2 * x1[0]

        S21[i] = 2 * x2[0]

    return S11, S21