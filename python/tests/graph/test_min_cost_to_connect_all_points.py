import unittest
from src.graph import min_cost_connect_points


class TestMinCostConnectPoints(unittest.TestCase):
    def test_min_cost_connect_points(self):
        points = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]
        res = min_cost_connect_points(points)
        self.assertEqual(res, 20)

        points = [[3, 12], [-2, 5], [-4, 1]]
        res = min_cost_connect_points(points)
        self.assertEqual(res, 18)
