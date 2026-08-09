"""
https://leetcode.com/problems/longest-increasing-subsequence/description/

Given an integer array nums, return the length of the longest strictly
increasing subsequence.

## Thought

Maintain a list `tails` where tails[i] is the smallest possible tail value of
an increasing subsequence of length i + 1 seen so far. For each new number,
binary search for the first element in `tails` that is >= num (leftmost
insertion point) and replace it, or append if num is larger than everything
in `tails`. The length of `tails` at the end is the answer.

Time: O(n log n)
Space: O(n)
"""

import bisect
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = []

        for num in nums:
            i = bisect.bisect_left(tails, num)
            if i == len(tails):
                tails.append(num)
            else:
                tails[i] = num

        return len(tails)
