from typing import List


class Solution:
    def max_product(self, nums: List[int]) -> int:
        cur_min, cur_max = 1, 1
        res = nums[0]

        for num in nums:
            temp_min = cur_min
            cur_min = min(cur_min * num, cur_max * num, num)
            cur_max = max(temp_min * num, cur_max * num, num)
            if cur_max > res:
                res = cur_max

        return res
