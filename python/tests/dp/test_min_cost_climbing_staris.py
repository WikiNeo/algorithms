import unittest

from src.dp import min_cost_climbing_stairs


class TestMinCostClimbingStairs(unittest.TestCase):
    def test_min_cost_climbing_stairs(self):
        cost = [10, 15, 20]
        res = min_cost_climbing_stairs(cost)
        self.assertEqual(res, 15)

        cost = [1,100,1,1,1,100,1,1,100,1]
        res = min_cost_climbing_stairs(cost)
        self.assertEqual(res, 6)
