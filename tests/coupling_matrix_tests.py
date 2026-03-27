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




if __name__ == '__main__':
    unittest.main()
