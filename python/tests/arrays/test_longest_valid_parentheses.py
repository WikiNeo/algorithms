import unittest

from src.arrays.longest_valid_parentheses import longest_valid_parentheses


class TestLongestValidParentheses(unittest.TestCase):
    def test_longest_valid_parentheses(self):
        self.assertEqual(longest_valid_parentheses("(()"), 2)
        self.assertEqual(longest_valid_parentheses(")()())"), 4)
        self.assertEqual(longest_valid_parentheses(""), 0)
        self.assertEqual(longest_valid_parentheses("()(())"), 6)
        self.assertEqual(longest_valid_parentheses("(((("), 0)
        self.assertEqual(longest_valid_parentheses("))))"), 0)
        self.assertEqual(longest_valid_parentheses("()(()"), 2)
        self.assertEqual(longest_valid_parentheses("()()"), 4)
