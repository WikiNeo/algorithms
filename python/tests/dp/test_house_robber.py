import unittest
from src.dp import rob


class TestHouseRobber(unittest.TestCase):
    def test_rob(self):
        nums = [1, 2, 3, 1]
        res = rob(nums)
        self.assertEqual(res, 4)

        nums = [2, 7, 9, 3, 1]
        res = rob(nums)
        self.assertEqual(res, 12)
