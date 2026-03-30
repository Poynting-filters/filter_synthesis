import numpy as np

from filter_synthesis.chebyshev import chebyshev_prototype
from filter_synthesis.coupling_matrix import coupling_matrix_from_g
from filter_synthesis.utils import print_coupling_matrix
from filter_synthesis.sparameters import compute_sparameters
from filter_synthesis.plotting import plot_response
g = chebyshev_prototype(3, 0.1)

M = coupling_matrix_from_g(g)

w = np.linspace(-3, 3, 1000)


S11, S21 = compute_sparameters(M, w)
print("Max S21 dB:", np.max(20*np.log10(np.abs(S21))))
print("Max S11 dB:", np.max(20*np.log10(np.abs(S11))))
plot_response(w, S11, S21)