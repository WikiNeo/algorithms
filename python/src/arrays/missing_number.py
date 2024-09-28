from typing import List


def missingNumber(nums: List[int]) -> int:
    LEN = len(nums)
    # calculate the expected sum
    expected_sum = (0 + LEN) * (LEN + 1) // 2

    # subtract to find the missing one
    return expected_sum - sum(nums)
