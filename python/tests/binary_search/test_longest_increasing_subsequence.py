import unittest

from src.binary_search.longest_increasing_subsequence import Solution


class TestLongestIncreasingSubsequence(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        nums = [10, 9, 2, 5, 3, 7, 101, 18]
        self.assertEqual(4, self.solution.lengthOfLIS(nums))

    def test_example_2(self):
        nums = [0, 1, 0, 3, 2, 3]
        self.assertEqual(4, self.solution.lengthOfLIS(nums))

    def test_example_3(self):
        nums = [7, 7, 7, 7, 7, 7, 7]
        self.assertEqual(1, self.solution.lengthOfLIS(nums))

    def test_single_element(self):
        nums = [5]
        self.assertEqual(1, self.solution.lengthOfLIS(nums))

    def test_strictly_increasing(self):
        nums = [1, 2, 3, 4, 5]
        self.assertEqual(5, self.solution.lengthOfLIS(nums))

    def test_strictly_decreasing(self):
        nums = [5, 4, 3, 2, 1]
        self.assertEqual(1, self.solution.lengthOfLIS(nums))
