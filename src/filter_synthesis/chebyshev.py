import numpy as np


def chebyshev_prototype(n: int, return_loss:float):
    """
    Computes Chebyshev lowpass prototype element values.

    Parameters
    ----------
    n : int
        Filter order
    return_loss : float
            Return loss in dB

    Returns
    -------
    g : ndarray
        Prototype element values g0 ... g(n+1)
    """
    # Calculate epsilon from return loss
    epsilon = np.sqrt(10**(return_loss/10) - 1)

    # Calculate beta and gamma
    beta = np.arcsinh(1/epsilon) / n
    gamma = np.sinh(beta)

    # Calculate prototype element values
    g = np.zeros(n+2)
    g[0] = 1
    for i in range(1, n+1):
        g[i] = (2 * gamma * np.sin((2*i-1)*np.pi/(2*n)) + 2 * np.sin((2*i-1)*np.pi/(2*n))**2) / (gamma**2 + np.sin((2*i-1)*np.pi/(2*n))**2)
    g[n+1] = 1

    return g