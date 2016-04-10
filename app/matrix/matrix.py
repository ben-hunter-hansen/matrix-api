"""
matrix-api v0.1
@author Ben Hansen
@created on 04/10/2016
matrix.py
"""

from app.decorators import require
from app.util import math

class Matrix:
    """
    The Matrix class models an n x m matrix.
    """
    @require(rows = int, cols = int)
    def __init__(self, rows = 3, cols = 3):
        """
        Matrix class constructor. By default, contructs a 3 x 3
        zero matrix.

        @param rows (int)   Number of rows in the matrix. Default: 3
        @param cols (int)   Number of columns in the matrix. Default: 3

        """
        self.__matrix = [[0 for x in range(cols)] for x in range(rows)]
        self.__rows = rows
        self.__cols = cols

    @classmethod
    @require(array = list)
    def fromArray(cls, array = []):
        """
        Creates a Matrix object from a two dimensional array
        of numeric values.

        @param array (list2d)   Two dimensional array of numbers.
        @return      (Matrix)   New Matrix object.

        """
        rows = len(array)
        cols = len(array[0])
        mat = cls(rows, cols)
        mat.__matrix = array

        return mat

    @staticmethod
    @require(rows = int, cols = int)
    def identity(rows = 3, cols = 3):
        """
        Creates an n x m identity Matrix.

        @param rows (int)    Number of desired rows. Default: 3
        @param cols (int)    Number of desired columns. Default: 3
        @return     (Matrix) New identity Matrix.

        """
        matrix = Matrix.zero(rows, cols)
        for i in range(0, rows):
            for j in range(0, cols):
                if i == j: matrix[i][j] = 1

        return matrix

    @staticmethod
    @require(rows = int, cols = int)
    def zero(rows = 3, cols = 3):
        """
        Creates an n x m zero Matrix.

        @param rows (int)    Number of desired rows. Default: 3
        @param cols (int)    Number of desired columns. Default: 3
        @return     (Matrix) New zero Matrix.

        """
        return Matrix.fromArray([[0 for x in range(cols)] for x in range(rows)])

    def rows(self):
        """
        Gets the number of rows in the current matrix instance.

        @return (int)   Row count.
        """
        return len(self.__matrix)

    def columns(self):
        """
        Gets the number of columns in the current matrix instance.

        @return (int)   Column count.
        """
        return len(self.__matrix[0])

    def transpose(self):
        """
        Creates a transposed copy of the current matrix instance.
        @return (Matrix)   Transpose of the current matrix.
        """
        return Matrix.fromArray([list(x) for x in zip(*self.__matrix)])

    def __mul__(self, other):
        """
        Computes the matrix product of the current instance, and
        another Matrix.

        @param self  (Matrix)    Current instance, right operand.
        @param other (Matrix)    Other matrix, left operand.
        @return      (Matrix)    The matrix product A*B
        """
        product = Matrix(self.rows(), other.columns())
        for i in range(0, product.rows()):
            for j in range(0, product.columns()):
                product[i][j] = math.dot(self[i], other.transpose()[j])
        return product

    def __getitem__(self,index):
        """
        Gets the entry at the specified index.
        """
        return self.__matrix[index]

    def __setitem__(self, key, item):
        """
        Sets the entry at the specified index.
        """
        self.__matrix[key] = item

    def __eq__(self, other):
        """
        Determines if two Matrix objects are equal.
        """
        return list(self) == list(other)

    def __str__(self):
        """
        Returns the string representation of the current
        matrix instance.
        """
        ret = ""
        for i in range(0, self.__rows):
            for j in range(0, self.__cols):
                ret += str(self.__matrix[i][j]) + " "
            ret += "\n"
        return ret
