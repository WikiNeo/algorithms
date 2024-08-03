from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # initialize cur_sum and res
        cur_sum = 0
        res = nums[0]

        for num in nums:
            # we will ignore negative cur_sum and start again
            if cur_sum < 0:
                cur_sum = 0

            # add current number to cur_sum
            cur_sum += num
            res = max(cur_sum, res)

        return res
