import numpy as np


def compute_sparameters(M, w):

    N = M.shape[0]

    I = np.eye(N)

    # Source/load excitation matrix
    W = np.zeros((N, 2), dtype=complex)

    W[0, 0] = 1      # source
    W[N-1, 1] = 1    # load

    S11 = np.zeros(len(w), dtype=complex)
    S21 = np.zeros(len(w), dtype=complex)

    for i, omega in enumerate(w):

        A = omega * I - M + 1j * (W @ W.T)

        A_inv = np.linalg.inv(A)

        S = np.eye(2) - 2j * (W.T @ A_inv @ W)

        S11[i] = S[0, 0]
        S21[i] = S[1, 0]

    return S11, S21
