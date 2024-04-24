"""
## Problem

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed.
All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one.
Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two
adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can
rob tonight without alerting the police.

## Example 1:

Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.

## Example 2:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

## Example 3:

Input: nums = [1,2,3]
Output: 3

## Constraints:

- 1 <= nums.length <= 100
- 0 <= nums[i] <= 1000

## Thoughts

- We can rob nums[1:]
- We can rob nums[:-1]
- Special case nums[0]
"""

from typing import List


def rob2(nums: List[int]) -> int:
    return max(nums[0], helper(nums[1:]), helper(nums[:-1]))


def helper(nums):
    rob1, rob2 = 0, 0

    for n in nums:
        new_rob = max(rob1 + n, rob2)
        rob1 = rob2
        rob2 = new_rob
    return rob2


def rob2_dp(self, nums: List[int]) -> int:
    LEN = len(nums)
    if LEN == 1:
        return nums[0]
    if LEN == 2:
        return max(nums[0], nums[1])

    # don't rob first, we can rob last
    res1 = [0] * LEN
    res1[0] = 0
    res1[1] = nums[1]
    # rob first, we can't rob last
    res2 = [0] * LEN
    res2[0] = nums[0]
    res2[1] = nums[0]

    for i in range(2, LEN):
        if i == LEN - 1:
            res2[i] = res2[i - 1]
        else:
            res2[i] = max(res2[i - 2] + nums[i], res2[i - 1])
        res1[i] = max(res1[i - 2] + nums[i], res1[i - 1])

    return max(res1[LEN - 1], res2[LEN - 1])
