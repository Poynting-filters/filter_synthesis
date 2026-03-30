import numpy as np

from filter_synthesis.chebyshev import chebyshev_prototype
from filter_synthesis.coupling_matrix import coupling_matrix_from_g
from filter_synthesis.utils import print_coupling_matrix
from filter_synthesis.sparameters import compute_sparameters
from filter_synthesis.plotting import plot_response
g = chebyshev_prototype(3, 20)
print(g)
M = coupling_matrix_from_g(g)

S11, S21, freq = compute_sparameters(M,6)
print("Max S21 dB:", np.max(20*np.log10(np.abs(S21))))
print("Max S11 dB:", np.max(20*np.log10(np.abs(S11))))
plot_response(freq, S11, S21)