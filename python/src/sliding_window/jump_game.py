from typing import List


def can_jump1(nums: List[int]) -> bool:
    """Let's assume we are driving a car to travel through the array, and each index cost 1 gas.
    If we have less than 0 gas during the process, we can't reach the end, and return False.
    Otherwise, we return True
    During the process, if we n > gas, we can increase our gas by setting gas = n
    """
    gas = 0
    for n in nums:
        if gas < 0:
            return False
        elif n > gas:
            gas = n
        gas -= 1

    return True


def can_jump2(nums: List[int]) -> bool:
    """Let's do it from backward by setting goal to be the last index"""
    LEN = len(nums)
    goal = LEN - 1

    for n in range(LEN - 2, -1, -1):
        # if we can reach the goal from index n, then we set our goal to n instead
        if nums[n] + n >= goal:
            goal = n

    # then we check if we have the final goal as first index
    return goal == 0
