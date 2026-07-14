# LeetCode 32: Longest Valid Parentheses
# https://leetcode.com/problems/longest-valid-parentheses/
#
# Given a string containing just '(' and ')', find the length of the longest
# substring of well-formed (matched) parentheses.
#
# Example 1: s = "(()"    -> 2   (the "()" at index 1..2)
# Example 2: s = ")()())"  -> 4   (the "()()" at index 1..4)
# Example 3: s = ""        -> 0
#
# Approach: maintain a stack of indices. Push the index of every '(' seen.
# On ')', pop the stack (matching the most recent unmatched '('); if the
# stack becomes empty, there's no opening to match, so push the current
# index as a new "wall" that future matches can't cross. Otherwise the
# current valid run extends from the new stack top + 1 through i.
#
# This generalizes the brace-matching depth-counter used in
# adf-schema-migration/migrate.py:_match_brace (which only needs the single
# matching index for one known '{'): here we don't know the opening index in
# advance, so a stack tracks all currently-unmatched opens at once.
#
# Time:  O(n) — each character pushed/popped at most once.
# Space: O(n) — worst case (all opens) the stack holds every index.

from typing import List


def longest_valid_parentheses(s: str) -> int:
    stack: List[int] = [-1]  # sentinel "wall" before the string starts
    best = 0

    for i, c in enumerate(s):
        if c == "(":
            stack.append(i)
        else:
            stack.pop()
            if not stack:
                stack.append(i)  # no matching '(': new wall
            else:
                best = max(best, i - stack[-1])

    return best


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        return longest_valid_parentheses(s)


if __name__ == "__main__":
    assert longest_valid_parentheses("(()") == 2, "Example 1"
    assert longest_valid_parentheses(")()())") == 4, "Example 2"
    assert longest_valid_parentheses("") == 0, "Empty string"
    assert longest_valid_parentheses("()(())") == 6, "Fully valid, nested"
    assert longest_valid_parentheses("((((") == 0, "All unmatched opens"
    assert longest_valid_parentheses("))))") == 0, "All unmatched closes"
    assert longest_valid_parentheses("()(()") == 2, "Trailing unmatched open"

    print("All tests passed.")
