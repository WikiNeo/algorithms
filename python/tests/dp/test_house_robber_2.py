import unittest
from src.dp import rob2

class TestHouseRobber2(unittest.TestCase):
    def test_rob2(self):
        nums = [2, 3, 2]
        res = rob2(nums)
        self.assertEqual(res, 3)

        nums = [1, 2, 3, 1]
        res = rob2(nums)
        self.assertEqual(res, 4)

        nums = [1, 2, 3]
        res = rob2(nums)
        self.assertEqual(res, 3)
