import unittest
from src.dp.coin_change import Solution


class TestCoinChange(unittest.TestCase):
    def test_coin_change(self):
        solution = Solution()

        res = solution.coinChange([1, 2, 5], 11)
        self.assertEqual(res, 3)

        res = solution.coinChange([2], 3)
        self.assertEqual(res, -1)

        res = solution.coinChange([1], 0)
        self.assertEqual(res, 0)
