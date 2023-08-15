import unittest
from src.dp.decode_ways import Solution


class TestDecodeWays(unittest.TestCase):
    def test_decode_ways(self):
        solution = Solution()

        res = solution.numDecodings("12")
        self.assertEqual(res, 2)

        res = solution.numDecodings("226")
        self.assertEqual(res, 3)

        res = solution.numDecodings("06")
        self.assertEqual(res, 0)
