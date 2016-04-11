"""
matrix-api v0.1
@author Ben Hansen
@created on 04/10/2016
utilspec.py

Test specification for the util namespace.
"""

import unittest
from app.matrix import util
from app.matrix import Matrix

class UtilSpec(unittest.TestCase):
    def testDotProduct(self):
        vectorA = [1,2,3]
        vectorB = [4,5,6]
        self.assertEqual(util.dot(vectorA,vectorB), 32)

    def testDimension(self):
        matrix = Matrix.fromArray([
            [1,2,3],
            [4,5,6]
        ])
        self.assertEqual(util.dimension(matrix), (3,2))
