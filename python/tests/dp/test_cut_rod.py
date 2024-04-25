import unittest
from src.dp.cut_rod import cut_rod_bottom_up, cut_rod_top_down


class TestCutRod(unittest.TestCase):

    def setUp(self):
        self.length_to_profit = {
            1: 1,
            2: 5,
            3: 8,
            4: 10,
            5: 13,
            6: 17,
            7: 18,
            8: 22,
            9: 25,
            10: 30,
        }

    def test_cut_rod_top_down(self):
        print(f"{self.test_cut_rod_top_down.__name__}")
        for length, profit in self.length_to_profit.items():
            print(f"length = {length}, expected profit = {profit}")
            self.assertEqual(profit, cut_rod_top_down(length))

    def test_cut_rod_bottom_up(self):
        print(f"{self.test_cut_rod_bottom_up.__name__}")
        for length, profit in self.length_to_profit.items():
            print(f"length = {length}, expected profit = {profit}")
            self.assertEqual(profit, cut_rod_bottom_up(length))
