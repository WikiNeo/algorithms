import unittest

from src.arrays import flatten, flatten_iter

class TestFlatten(unittest.TestCase):

    def test_flatten(self):

        nested_list = [2, 1, [3, [4, 5], 6], 7, [8]]
        flattened = flatten(nested_list)
        self.assertEqual(flattened, [2, 1, 3, 4, 5, 6, 7, 8])

        nested_list = [[3, [4, 5], 6], 7, [8]]
        flattened = flatten(nested_list)
        self.assertEqual(flattened, [3, 4, 5, 6, 7, 8])

        nested_list = [[], [8]]
        flattened = flatten(nested_list)
        self.assertEqual(flattened, [8])

    def test_flatten_iter(self):

        nested_list = [2, 1, [3, [4, 5], 6], 7, [8]]
        flattened = flatten_iter(nested_list)
        self.assertEqual(next(flattened), 2)
        self.assertEqual(next(flattened), 1)
        self.assertEqual(next(flattened), 3)
        self.assertEqual(next(flattened), 4)
        self.assertEqual(next(flattened), 5)
        self.assertEqual(next(flattened), 6)
        self.assertEqual(next(flattened), 7)
        self.assertEqual(next(flattened), 8)
        self.assertRaises(StopIteration, next, flattened)

        nested_list = [[3, [4, 5], 6], 7, [8]]
        flattened = flatten_iter(nested_list)
        self.assertEqual(next(flattened), 3)
        self.assertEqual(next(flattened), 4)
        self.assertEqual(next(flattened), 5)
        self.assertEqual(next(flattened), 6)
        self.assertEqual(next(flattened), 7)
        self.assertEqual(next(flattened), 8)
        self.assertRaises(StopIteration, next, flattened)

        nested_list = [[], [8]]
        flattened = flatten_iter(nested_list)
        self.assertEqual(next(flattened), 8)
        self.assertRaises(StopIteration, next, flattened)