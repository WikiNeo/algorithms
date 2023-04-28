import unittest

from src.two_pointers import longest_subsequence_even_diff_sum


class TestLongestSubsequenceEvenDiffSum(unittest.TestCase):
    def test_longest_subsequence_even_diff_sum(self):
        arr = [2, 4, 1, 7]
        self.assertEqual(longest_subsequence_even_diff_sum(arr), 4)

        arr = [7, 5, 6, 2, 3, 2, 4]
        self.assertEqual(longest_subsequence_even_diff_sum(arr), 6)

        arr = [2, 4, 1]
        self.assertEqual(longest_subsequence_even_diff_sum(arr), 2)
