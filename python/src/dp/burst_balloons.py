from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        memory = {}  # (left, right) -> maxCoins mapping
        nums = [1] + nums + [1]  # add dummy 1s at begnning and in the end
        LEN_NUMS = len(nums)

        for offset in range(
            2, LEN_NUMS
        ):  # let's check the interval with size 2 to LEN_NUMS exclusive
            for left in range(
                LEN_NUMS - offset
            ):  # let's set left from 0 to the max possible value, which is LEN_NUMS - offset
                right = left + offset  # natually, we can get the right index
                for pivot in range(
                    left + 1, right
                ):  # check all possible pivot as the last balloon to burst
                    coins = (
                        nums[left] * nums[pivot] * nums[right]
                    )  # get the last balloon bursing coins
                    coins += memory.get((left, pivot), 0) + memory.get(
                        (pivot, right), 0
                    )  # we add two subinterval coins
                    memory[(left, right)] = max(coins, memory.get((left, right), 0))

        return memory.get((0, LEN_NUMS - 1), 0)
