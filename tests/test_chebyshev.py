import numpy as np

from filter_synthesis.chebyshev import chebyshev_prototype
from filter_synthesis.coupling_matrix_from_g import coupling_matrix_from_g
from filter_synthesis.utils import print_coupling_matrix
from filter_synthesis.sparameters import compute_sparameters
from filter_synthesis.plotting import plot_response
g = chebyshev_prototype(3, 20)
print(g)
test_g = [1.0, 1.0000, 2.0000, 1.0000, 1.0] # g values for a 3rd order butterworth lowpass filter
M, Qe1, QeN = coupling_matrix_from_g(g)
print_coupling_matrix(M)
print(f"Qe1 = {Qe1:.4f}")
print(f"QeN = {QeN:.4f}")

f0   = 2.45e9   # 2.45 GHz centre
BW   = 100e6    # 100 MHz bandwidth
f, S11, S21 = compute_sparameters(M, Qe1, QeN, f0, BW)
#print("Max S21 dB:", np.max(20*np.log10(np.abs(S21))))
#print("Max S11 dB:", np.max(20*np.log10(np.abs(S11))))
plot_response(f, S11, S21)