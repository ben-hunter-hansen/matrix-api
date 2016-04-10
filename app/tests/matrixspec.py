"""
matrix-api v0.1
@author Ben Hansen
@created on 04/10/2016
matrixspec.py

Test specification for the Matrix class.
"""

import unittest
from app.matrix import Matrix

class MatrixSpec(unittest.TestCase):
    def setUp(self):
        self.matrix = Matrix.fromArray([
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ])

        self.zeroMatrix =  Matrix.fromArray([
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ])

        self.identity = Matrix.fromArray([
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 1]
        ])

    def testConstructor(self):
        """
        A new Matrix instance should be a 3 x 3 by default,
        unless a different number of rows and columns are specified.
        The matrix should be the zero matrix.
        """
        with self.assertRaises(TypeError):
            badArguments = Matrix(2.5, 'foo')

        matrix1 = Matrix()
        self.assertEqual(matrix1.identity(), self.identity)

        matrix2 = Matrix(4,2)
        self.assertEqual(matrix2.rows(), 4)
        self.assertEqual(matrix2.columns(), 2)

    def testTranspose(self):
        """
        The transpose method return a copy of the matrix
        with the columns and rows exchanged.
        """

        transpose = Matrix.fromArray([
            [1, 4, 7],
            [2, 5, 8],
            [3, 6, 9]
        ])
        self.assertEqual(self.matrix.transpose(), transpose)

    def testIdentity(self):
        """
        The static identity method should return a 3 x 3
        identity matrix, unless a different number of rows and columns
        are specified
        """
        mat = Matrix()
        self.assertEqual(mat.identity(), self.identity)


if __name__ == '__main__':
    unittest.main()
