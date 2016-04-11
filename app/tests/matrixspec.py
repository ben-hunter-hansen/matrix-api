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

        self.assertEqual(Matrix.identity(), self.identity)


    def testMultiply(self):
        """
        The binary multiplication operator
        should, when applied to two matricies, produce
        the matrix product if and only if the number of rows in the left
        operand is equal to the number of columns in the right operand.

        Matrix multiplication is generally not communitive, so
        the product AB should differ from the product BA (usually)
        """
        matrixA = self.matrix
        matrixB = self.matrix.transpose()

        productAB = matrixA * matrixB
        productBA = matrixB * matrixA

        self.assertEqual(productAB, [
            [14,32,50],
            [32,77,122],
            [50,122,194]
        ])

        self.assertEqual(productBA, [
            [66,78,90],
            [78,93,108],
            [90,108,126]
        ])

        matrixC = Matrix.fromArray([
            [1,2,3],
            [4,5,6]
        ])

        self.assertEqual(matrixA * matrixC, None)

    def testAddition(self):
        """
        The binary addition operator
        should, when applied to two matricies, product
        the sum of the two matricies if and only if
        their dimensions are equal.
        """

        A = Matrix.fromArray([
            [0,2,3],
            [4,2,6],
            [4,5,6]
        ])
        B = Matrix.fromArray([
            [4, 9, 6],
            [7, 8, 1],
            [0, 13,2]
        ])
        C = Matrix.fromArray([
            [1,2,3],
            [4,5,6]
        ])
        sumAB = Matrix.fromArray([
            [4, 11, 9],
            [11, 10, 7],
            [4, 18, 8]
        ])
        self.assertEqual(A + B, sumAB)
        self.assertEqual(A + C, None)

    def testSubtraction(self):
        """
        The binary subtraction operator
        should, when applied to two matricies, product
        the difference of the two matricies if and only if
        their dimensions are equal.
        """
        A = Matrix.fromArray([
            [0,2,3],
            [4,2,6],
            [4,5,6]
        ])
        B = Matrix.fromArray([
            [4, 9, 6],
            [7, 8, 1],
            [0, 13,2]
        ])
        C = Matrix.fromArray([
            [1,2,3],
            [4,5,6]
        ])
        diffAB = Matrix.fromArray([
            [-4, -7, -3],
            [-3, -6, 5],
            [4, -8, 4]
        ])
        self.assertEqual(A - B, diffAB)
        self.assertEqual(A - C, None)

    
    def testDeterminant(self):
        """
        The determinant method should return None if the
        matrix is not square. It should return zero
        if the matrix is singular.
        """

        nonSquare = Matrix.fromArray([
            [1,2,3],
            [4,5,6]
        ])
        singularMatrix = self.matrix
        self.assertEqual(nonSquare.determinant(), None)
        self.assertEqual(singularMatrix.determinant(), 0)

if __name__ == '__main__':
    unittest.main()
