# tests/test_math_tools.py

import unittest
from my_awesome_lib.math_tools import factorial, is_prime


class TestMathTools(unittest.TestCase):

    def test_factorial(self):
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(5), 120)
        with self.assertRaises(ValueError):
            factorial(-1)

    def test_is_prime(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(13))
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(100))


if __name__ == '__main__':
    unittest.main()
