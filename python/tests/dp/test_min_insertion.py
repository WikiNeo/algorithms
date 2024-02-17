import unittest
from src.dp import min_insertion


class TestMinInsertion(unittest.TestCase):
    def test_min_insertion(self):
        s = "ab"
        res = min_insertion(s, len(s))
        self.assertEqual(res, 1)

        s = "geeks"
        res = min_insertion(s, len(s))
        self.assertEqual(res, 3)

        s = "mbadm"
        res = min_insertion(s, len(s))
        self.assertEqual(res, 2)

        s = "zzazz"
        res = min_insertion(s, len(s))
        self.assertEqual(res, 0)

        s = "leetcode"
        res = min_insertion(s, len(s))
        self.assertEqual(res, 5)
