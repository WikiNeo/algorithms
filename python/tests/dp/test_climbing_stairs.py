import unittest
from src.dp import climb_stairs_tabulation, climb_stairs_memoization


class TestClimbingStairs(unittest.TestCase):
    def test_climb_stairs_tabulation(self):
        res = climb_stairs_tabulation(2)
        self.assertEqual(res, 2)

        res = climb_stairs_tabulation(3)
        self.assertEqual(res, 3)

    def test_climb_stairs_memoization(self):
        res = climb_stairs_memoization(2)
        self.assertEqual(res, 2)

        res = climb_stairs_memoization(3)
        self.assertEqual(res, 3)
