from filter_synthesis.chebyshev import chebyshev_prototype
from filter_synthesis.coupling_matrix import coupling_matrix_from_g
from filter_synthesis.utils import print_matrix

g = chebyshev_prototype(5, 0.1)

M = coupling_matrix_from_g(g)

print_matrix(M)