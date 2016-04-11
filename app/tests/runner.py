
from . import MathUtilSpec
from . import MatrixSpec
import unittest

def run():
    matrixSuite = unittest.TestLoader().loadTestsFromTestCase(MatrixSpec)
    mathUtilSuite = unittest.TestLoader().loadTestsFromTestCase(MathUtilSpec)
    unittest.TextTestRunner(verbosity=2).run(matrixSuite)
    unittest.TextTestRunner(verbosity=2).run(mathUtilSuite)
