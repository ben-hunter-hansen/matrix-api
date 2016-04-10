
from . import MathUtilSpec
from . import MatrixSpec
import unittest

def run():
    suite = unittest.TestLoader().loadTestsFromTestCase(MatrixSpec)
    unittest.TextTestRunner(verbosity=2).run(suite)
