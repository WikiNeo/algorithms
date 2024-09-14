from typing import List


def countBits(n: int) -> List[int]:
    """
    0 -> 0000
    1 -> 0001 offset 1
    2 -> 0010        2
    3 -> 0011        2
    4 -> 0100        4
    5 -> 0101        4
    6 -> 0110        4
    7 -> 0111        4
    8 -> 1000        8
    """
    dp = [0] * (n + 1)
    # we will store the most significant bit
    offset = 1
    for i in range(1, n + 1):
        # we will update the most significant bit whenever
        if offset * 2 == i:
            offset = i
        # the current number of 1 bit equals 1 + the numebr of 1 bit in i - offset
        dp[i] = 1 + dp[i - offset]

    return dp
