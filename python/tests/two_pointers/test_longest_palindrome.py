import unittest

from src.two_pointers import longest_palindrome


class TestLongestPalindrome(unittest.TestCase):
    def test_longest_palindrome(self):
        s = "babad"
        self.assertEqual(longest_palindrome(s), "bab")

        s = "cbbd"
        self.assertEqual(longest_palindrome(s), "bb")
