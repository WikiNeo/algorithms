# have a dict to store valueToIndex, and check if we can get target with current value
from typing import List


class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        value_to_index = {}
        for index, value in enumerate(nums):
            # check if we have remain as key in value_to_index
            if target - value in value_to_index:
                return [index, value_to_index[target - value]]
            # update value to index
            value_to_index[value] = index
