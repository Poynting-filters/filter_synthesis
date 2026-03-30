import numpy as np
import matplotlib.pyplot as plt

def plot_response(w, S11, S21):
    """
    Plots the magnitude of S11 and S21 in dB.

    Parameters
    ----------
    w : ndarray
        Frequency points (normalized)
    S11 : ndarray
        S11 values
    S21 : ndarray
        S21 values
    """
    S11_dB = 20 * np.log10(np.abs(S11))
    S21_dB = 20 * np.log10(np.abs(S21))

    plt.figure(figsize=(8,5))

    plt.plot(w, S21_dB, label='|S21| (dB)', color='red')
    plt.plot(w, S11_dB, label='|S11| (dB)', color='blue')

    plt.xlabel('Normalized Frequency ω')
    plt.ylabel('Magnitude (dB)')
    plt.title('Filter Response')
    plt.grid()
    plt.legend()
    plt.tight_layout()
    plt.show()