from filter_synthesis.chebyshev import chebyshev_prototype
g = chebyshev_prototype(5, 0.1)
for i, val in enumerate(g):
    print(f"g{i} = {val:.6f}")