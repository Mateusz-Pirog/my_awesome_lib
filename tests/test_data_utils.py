# tests/test_data_utils.py

import unittest
from my_awesome_lib.data_utils import flatten, chunk_list


class TestDataUtils(unittest.TestCase):

    def test_flatten(self):
        self.assertEqual(flatten([1, [2, [3, 4], 5], 6]), [1, 2, 3, 4, 5, 6])
        self.assertEqual(flatten([]), [])
        self.assertEqual(flatten([1, 2, 3]), [1, 2, 3])

    def test_chunk_list(self):
        self.assertEqual(chunk_list([1, 2, 3, 4], 2), [[1, 2], [3, 4]])
        self.assertEqual(chunk_list([1, 2, 3], 1), [[1], [2], [3]])
        self.assertEqual(chunk_list([], 3), [])


if __name__ == '__main__':
    unittest.main()
