import numpy as np

def chebyshev_prototype(n, ripple_db):
    """
    Returns lowpass prototype g-values for a Chebyshev Type I filter.
    """

    print(f"Order: {n}, Ripple: {ripple_db} dB")