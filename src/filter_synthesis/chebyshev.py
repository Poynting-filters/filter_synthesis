import numpy as np


def chebyshev_prototype(n: int, ripple_db: float):

    epsilon = np.sqrt(10**(ripple_db / 10) - 1)

    alpha = np.arcsinh(1 / epsilon) / n

    sigma = np.sinh(alpha)

    g = np.zeros(n + 2)

    g[0] = 1

    a = np.zeros(n)
    b = np.zeros(n)

    for k in range(1, n + 1):

        a[k - 1] = np.sin((2 * k - 1) * np.pi / (2 * n))

        b[k - 1] = sigma**2 + np.sin(k * np.pi / n)**2

    g[1] = (2 * a[0]) / sigma

    for k in range(2, n + 1):

        g[k] = (4 * a[k - 2] * a[k - 1]) / (b[k - 2] * g[k - 1])

    if n % 2 == 0:

        g[n + 1] = (np.cosh(alpha / 2) / np.sinh(alpha / 2))**2

    else:

        g[n + 1] = 1

    return g
