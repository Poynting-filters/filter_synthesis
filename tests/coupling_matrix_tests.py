import unittest
from filter_synthesis.src.filter_synthesis import coupling_matrix as cm
import numpy as np


class CouplingMatrixTests(unittest.TestCase):

    def test_similarity_transform(self):
        """
        Test similarity transform with dummy data and an error tolerance of 1E-15
        :return:
        """
        r = cm.similarity_transform(7, 2, 4, np.pi/2)

        assert abs(r[2][2] - 0) < 1E-15
        assert abs(r[4][4] - 0) < 1E-15
        assert abs(r[2][4] + 1) < 1E-15
        assert abs(r[4][2] - 1) < 1E-15
        assert abs(r[0][5] - 0) < 1E-15
        assert abs(r[1][1] - 1) < 1E-15

        try:
            r = cm.similarity_transform(7, 6, 4, np.pi/2)
            assert False, "Invalid pivot accepted"
        except RuntimeError:
            assert True

        return

    def test_generate_folded_form_annihilation_sequence(self):

        correct = [(0, 5, (4, 5), 0, 4, -1), (0, 4, (3, 4), 0, 3, -1), (0, 3, (2, 3), 0, 2, -1), (0, 2, (1, 2), 0, 1, -1),
(2, 6, (2, 3), 3, 6, 1), (3, 6, (3, 4), 4, 6, 1), (4, 6, (4, 5), 5, 6, 1), (1, 4, (3, 4), 1, 3, -1), (1, 3, (2, 3), 1, 2, -1),
(3, 5, (3, 4), 4, 5, 1)]
        output = cm.generate_folded_form_annihilation_sequence(7)
        assert len(output) == len(correct)
        for i in range(0, len(output)):
            assert output[i][0] == correct[i][0]
            assert output[i][1] == correct[i][1]
            assert output[i][2][0] == correct[i][2][0]
            assert output[i][2][1] == correct[i][2][1]
            assert output[i][3] == correct[i][3]
            assert output[i][4] == correct[i][4]
            assert output[i][5] == correct[i][5]

        return

    def test_n_coupling_matrix_to_canonical_folded_form(self):

        M = np.array([[0.31, 1.00, 0.98, 0.51, 0.88, 0.45, 0.91],
                             [1.00, 0.06, 0.04, 0.42, 0.19, 0.77, 0.55],
                             [0.98, 0.04, 0.05, 0.19, 0.09, 0.60, 0.78],
                             [0.51, 0.42, 0.19, 0.97, 0.16, 1.00, 0.70],
                             [0.88, 0.19, 0.09, 0.16, 0.54, 0.20, 0.14],
                             [0.45, 0.77, 0.60, 1.00, 0.20, 0.14, 0.77],
                             [0.91, 0.55, 0.78, 0.70, 0.14, 0.77, 0.75]])

        A = cm.n_coupling_matrix_to_canonical_folded_form(M)

        assert A[0][5] == 0
        assert A[0][4] == 0
        assert A[0][3] == 0
        assert A[0][2] == 0
        assert A[2][6] == 0
        assert A[3][6] == 0
        assert A[4][6] == 0
        assert A[1][4] == 0
        assert A[1][3] == 0
        assert A[3][5] == 0



if __name__ == '__main__':
    unittest.main()
