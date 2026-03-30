import numpy as np
import matplotlib.pyplot as plt

def compute_sparameters(M, w_start, RS = 50, RL = 50, points = 5000):
    # Computes S-parameters from the coupling matrix M at normalised frequencies w.
    # RS and RL are the source and load impedances, respectively.
    N = len(M)

    # Define Resistance matrix
    R = np.diag([RS] + [0]*(N-2) + [RL])

    # Define plotting range
    points = 5000                      # number of discrete points
    w_start = -w_start                    # start point
    delta = (-w_start - (w_start)) / points        # step size between frequency points

    # Allocate memory for data vectors
    s21 = np.zeros(points)
    s11 = np.zeros(points)
    freq = np.zeros(points)

    # Generate vectors of transmission and reflection coefficients (in dB)
    w = w_start
    for k in range(points):
        s = 1j * w
        Z = s * np.eye(N) + R - 1j * M
        Zi = np.linalg.inv(Z)
        s21[k] = 20 * np.log10(abs(2 * np.sqrt(RS * RL) * Zi[N-1, 0]))
        s11[k] = 20 * np.log10(abs(1 - 2 * RS * Zi[0, 0]))
        freq[k] = w
        w += delta

    return s11, s21, freq