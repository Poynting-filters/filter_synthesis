import numpy as np


def print_coupling_matrix(M):

    labels = ["S"] + [f"{i}" for i in range(1, M.shape[0]-1)] + ["L"]

    print("     ", end="")
    for label in labels:
        print(f"{label:>8}", end="")
    print()

    for i, row in enumerate(M):

        print(f"{labels[i]:>5}", end="")

        for val in row:
            print(f"{val:8.4f}", end="")

        print()