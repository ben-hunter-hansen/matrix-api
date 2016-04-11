"""
matrix-api v0.1
@author Ben Hansen
@created on 04/10/2016
matrixspec.py

Test specification for the mathutil module.
"""

import unittest
from app.util import math

class MathUtilSpec(unittest.TestCase):
    def testDotProduct(self):
        with self.assertRaises(TypeError):
            math.dot(2.3, 'abc')

if __name__ == '__main__':
    unittest.main()
