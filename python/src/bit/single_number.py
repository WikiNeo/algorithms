from typing import List


def singleNumber(nums: List[int]) -> int:
    res = 0
    for num in nums:
        # XOR remove even number of duplicates
        res ^= num

    return res
