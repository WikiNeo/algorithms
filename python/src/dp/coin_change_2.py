from typing import List


class Solution:
    def change_memo(self, amount: int, coins: List[int]) -> int:
        # stores (amount, index) = res
        dp = {}
        LEN = len(coins)

        def dfs(cur_amount, index):
            """return number of ways to get cur_amount with coins starting at index"""
            # some base cases
            if cur_amount < 0:
                return 0
            if cur_amount == 0:  # base case with 0 amount
                return 1
            if index == LEN:  # base case with out of bound index
                return 0
            if (cur_amount, index) in dp:  # cache hit
                return dp[(cur_amount, index)]

            # cache update
            #   we can either take coin at current index, or skip it
            dp[(cur_amount, index)] = dfs(cur_amount - coins[index], index) + dfs(
                cur_amount, index + 1
            )

            # return result
            return dp[(cur_amount, index)]

        # driver
        return dfs(amount, 0)
