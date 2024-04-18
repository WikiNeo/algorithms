from typing import List


class Solution:
    def can_partition(self, nums: List[int]) -> bool:
        sum_nums = sum(nums)
        if sum_nums % 2 == 1:
            return False

        target = sum_nums // 2
        dp = set()
        dp.add(0)

        for i in range(len(nums) - 1, -1, -1):
            new_dp = set()
            for value in dp:
                temp_sum = value + nums[i]
                if temp_sum == target:
                    return True
                new_dp.add(temp_sum)
            dp.update(new_dp)

        return True if target in dp else False
