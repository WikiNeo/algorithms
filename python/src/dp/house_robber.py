"""
## Problem

You are a professional robber planning to rob houses along a street. Each house has a certain
amount of money stashed, the only constraint stopping you from robbing each of them is that
adjacent houses have security systems connected and it will automatically contact the police if
two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum
amount of money you can rob tonight without alerting the police.

## Example 1

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

## Example 2

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.

## Constraints

- 1 <= nums.length <= 100
- 0 <= nums[i] <= 400

## Thoughts

[rob1, rob2, ... robn]

- rob3 = max(rob1 + num3, rob2)
"""

from typing import List


def rob(nums: List[int]) -> int:
    rob1, rob2 = 0, 0

    for num in nums:
        # either we rob num -> rob1 + num
        # or not -> rob2
        temp = max(rob1 + num, rob2)
        rob1 = rob2
        rob2 = temp

    return rob2


def rob_dp(self, nums: List[int]) -> int:
    LEN = len(nums)
    if LEN == 1:
        return nums[0]
    if LEN == 2:
        return max(nums[0], nums[1])

    # res represents the max value we can rob at i
    res = [0] * LEN
    res[0] = nums[0]
    res[1] = max(nums[0], nums[1])
    for i in range(2, LEN):
        # we have two choices at i, one is to rob it, the other is to skip it.
        res[i] = max(res[i - 2] + nums[i], res[i - 1])

    return res[LEN - 1]
