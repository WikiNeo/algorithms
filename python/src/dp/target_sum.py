from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        LEN = len(nums)
        dp = {}  # (index, cur_sum) => number of ways to get target starting at index with cur_sum

        def dfs(index, cur_sum):
            """return number of ways to get target starting at index with cur_sum"""
            # base case
            if index == LEN:
                return 1 if cur_sum == target else 0
            key = (index, cur_sum)
            # cache hit
            if key in dp:
                return dp[key]

            # cache miss
            #   we can either add or minus nums[index] from cur_sum and move to index + 1
            dp[key] = dfs(index + 1, cur_sum + nums[index]) + dfs(
                index + 1, cur_sum - nums[index]
            )

            return dp[key]

        return dfs(0, 0)
