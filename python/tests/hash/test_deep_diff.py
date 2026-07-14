import unittest

from src.hash.deep_diff import deep_diff


class TestDeepDiff(unittest.TestCase):
    def test_no_change(self):
        base = {"a": 1, "b": {"c": 2}}
        override = {"a": 1, "b": {"c": 2}}
        self.assertEqual(deep_diff(base, override), ({}, []))

    def test_nested_change_and_new_key(self):
        base = {"a": 1, "b": {"c": 2, "d": 3}}
        override = {"a": 1, "b": {"c": 20, "d": 3}, "e": 5}
        self.assertEqual(deep_diff(base, override), ({"b": {"c": 20}, "e": 5}, []))

    def test_deletion_is_undeletable(self):
        base = {"a": 1, "b": 2}
        override = {"a": 1}
        self.assertEqual(deep_diff(base, override), ({}, ["b"]))

    def test_dict_replaced_by_scalar(self):
        base = {"a": {"x": 1}}
        override = {"a": 5}
        self.assertEqual(deep_diff(base, override), ({"a": 5}, []))

    def test_nested_deletion_path(self):
        base = {"a": {"x": 1, "y": 2}}
        override = {"a": {"x": 1}}
        self.assertEqual(deep_diff(base, override), ({}, ["a.y"]))

    def test_list_is_whole_replacement(self):
        base = {"a": [1, 2, 3]}
        override = {"a": [1, 2]}
        self.assertEqual(deep_diff(base, override), ({"a": [1, 2]}, []))
