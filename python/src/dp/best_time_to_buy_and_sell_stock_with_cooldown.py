from typing import List


class Solution:
    def max_profit(self, prices: List[int]) -> int:
        """
        on day i, we can either own a stock or not_own a stock, let's use own[i] and not_own[i]
        to represent the max profit we can have on day i.

        Then we have:
            own[i] = max(own[i - 1], not_own[i - 2] - prices[i]) -> cooldown on day i, or purchase on day i
            not_own[i] = max(not_own[i - 1], own[i - 1] + price[i]) -> cooldown on day i, or sell on day i.
        """
        res = 0
        own_last = -prices[0]
        not_own_last = 0
        not_own_last2 = 0

        for i in range(1, len(prices)):
            # follow the equations
            own = max(own_last, not_own_last2 - prices[i])
            not_own = max(not_own_last, own_last + prices[i])

            # update state for next i
            own_last = own
            not_own_last2 = not_own_last
            not_own_last = not_own

            # calculate
            res = max(res, own, not_own)

        # return result here
        return res
