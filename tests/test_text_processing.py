# tests/test_text_processing.py

import unittest
from my_awesome_lib.text_processing import count_words, remove_punctuation


class TestTextProcessing(unittest.TestCase):

    def test_count_words(self):
        self.assertEqual(count_words("Hello world"), 2)
        self.assertEqual(count_words(""), 0)
        self.assertEqual(count_words("One two three"), 3)

    def test_remove_punctuation(self):
        self.assertEqual(remove_punctuation("Hello, world!"), "Hello world")
        self.assertEqual(remove_punctuation("No punctuations"), "No punctuations")


if __name__ == '__main__':
    unittest.main()
