"""Módulo pai de execução dos testes unitários"""
import unittest
from tests.utils_test import UtilsTest


def suite():
    """Test suite"""
    suite_return = unittest.TestSuite()
    suite_return.addTests(tests=unittest.TestLoader().loadTestsFromTestCase(UtilsTest))
    return suite_return


if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=3).run(suite())
