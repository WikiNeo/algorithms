from typing import List


class Solution:
    def can_partition(self, nums: List[int]) -> bool:
        sum_nums = sum(nums)
        # we can skip odd sum nums
        if sum_nums % 2 == 1:
            return False

        target = sum_nums // 2
        # we store possible sum with nums in dp
        # 0 is always a possible value/base case
        dp = set()
        dp.add(0)

        for i in range(0, len(nums)):
            # we can't modify a Set as we loop through it, so let's create a new one
            new_dp = set()
            for value in dp:
                temp_sum = value + nums[i]
                if temp_sum == target:
                    return True
                new_dp.add(temp_sum)
            dp.update(new_dp)

        return True if target in dp else False
