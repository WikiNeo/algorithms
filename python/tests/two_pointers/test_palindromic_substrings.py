import unittest

from src.two_pointers import count_substrings


class TestPalindromicSubstrings(unittest.TestCase):
    def test_palindromic_substrings(self):
        s = "abc"
        res = count_substrings(s)
        self.assertEqual(res, 3)

        s = "aaa"
        res = count_substrings(s)
        self.assertEqual(res, 6)
