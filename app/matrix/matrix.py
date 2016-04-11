"""
matrix-api v0.1
@author Ben Hansen
@created on 04/10/2016
matrix.py
"""
import copy
from app.decorators import require

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
        self.__matrix = [[0 for x in range(rows)] for x in range(cols)]
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

    @staticmethod
    def dim(A):
        return (A.rows(), A.columns())

    def rows(self):
        """
        Gets the number of rows in the current matrix instance.

        @return (int)   Row count.
        """
        return len(list(self[0]))

    def columns(self):
        """
        Gets the number of columns in the current matrix instance.

        @return (int)   Column count.
        """
        return len(list(self))


    def transpose(self):
        """
        Creates a transposed copy of the current matrix instance.
        @return (Matrix)   Transpose of the current matrix.
        """
        return Matrix.fromArray([list(x) for x in zip(*self.__matrix)])


    def determinant(self):
        """
        Computes the determinant of the current Matrix instance
        by cofactors.
        @return (int|None)  The determinant if the matrix is square, else None
        """

        if self.rows() != self.columns():
            return None

        def minor(matrix, i):
            minor = copy.deepcopy(matrix)
            del minor[0]
            for b in range(len(matrix)-1):
                del minor[b][i]
            return minor

        def det(matrix):
            if len(matrix) == 1:
                return matrix[0][0]
            else:
                determinant = 0
                for x in range(len(matrix)):
                    determinant += matrix[0][x] * (-1)**(2+x) * det(minor(matrix,x))
                return determinant

        return det(self.__matrix)

    def __mul__(self, other):
        """
        Computes the matrix product of the current
        matrix and another, with the constraint that
        the number of rows in this matrix is equal to
        the columns of the other.

        @param self  (Matrix)       Current instance, right operand.
        @param other (Matrix)       Other matrix, left operand.
        @return      (Matrix|None)   The matrix product A*B, else None
        """
        if self.rows() != other.columns():
            return None

        product = Matrix(self.rows(), other.columns())
        for i in range(0, product.rows()):
            for j in range(0, product.columns()):
                product[i][j] = util.dot(self[i], other.transpose()[j])
        return product

    def __add__(self, other):
        """
        Computes the sum of the current matrix instance and another,
        with the constraint that the dimensions of each operand are
        equivalent.  If they are not, return None.

        @param self  (Matrix)       Current instance, right operand.
        @param other (Matrix)       Other matrix, left operand.
        @return      (Matrix|None)  The sum, else None
        """
        if util.dimension(self) != util.dimension(other):
            return None

        return Matrix.fromArray([[a + b for a, b in zip(row1, row2)] for row1, row2 in zip(self,other)])

    def __sub__(self, other):
        """
        Computes the difference of the current matrix instance and another,
        with the constraint that the dimensions of each operand are
        equivalent.  If they are not, return None.

        @param self  (Matrix)       Current instance, right operand.
        @param other (Matrix)       Other matrix, left operand.
        @return      (Matrix|None)  The difference, else None
        """
        if util.dimension(self) != util.dimension(other):
            return None

        return Matrix.fromArray([[a - b for a, b in zip(row1, row2)] for row1, row2 in zip(self,other)])


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
        Returns the JSON encoded string value of this matrix.
        """
        ret = "["
        for i in range(0, self.__rows):
            for j in range(0, self.__cols):
                if j == 0:
                    ret += "["
                ret += str(self.__matrix[i][j])
                if j != self.__cols - 1:
                    ret +=", "
                if j == self.__cols - 1:
                    ret += "]"

            ret += "]" if i < self.__rows - 1 else "],"

        return ret

class util:
    """
    Namespace for utility functions that arent directly
    associated with a Matrix, or matrix instance.
    """
    @staticmethod
    @require(u = list, v = list)
    def dot(u, v):
        """
        Given two vectors represented as
        one dimensional lists, return their
        dot product.

        @param u  (list)      First vector.
        @param v  (list)      Second vector.
        @return   (number)    The dot product of u and v

        """
        return sum(p * q for p, q in zip(u, v))

    @staticmethod
    @require(A = Matrix)
    def dimension(A):
        return (A.rows(), A.columns())
