
from . import UtilSpec
from . import MatrixSpec
import unittest

def run():
    matrixSuite = unittest.TestLoader().loadTestsFromTestCase(MatrixSpec)
    mathUtilSuite = unittest.TestLoader().loadTestsFromTestCase(UtilSpec)
    unittest.TextTestRunner(verbosity=2).run(matrixSuite)
    unittest.TextTestRunner(verbosity=2).run(mathUtilSuite)
