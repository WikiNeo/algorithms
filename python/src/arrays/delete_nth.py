"""
Given a list lst and a number N, create a new list
that contains each number of the list at most N times without reordering.

For example if N = 2, and the input is [1,2,3,1,2,1,2,3], you take [1,2,3,1,2],
drop the next [1,2] since this would lead to 1 and 2 being in the result 3 times, and then take 3,
which leads to [1,2,3,1,2,3]
"""
import collections
from typing import List, Dict

def delete_nth(nums: List[int], n: int) -> List[int]:
    result: List[int] = []
    counts: Dict[int, int] = collections.defaultdict(int)

    for num in nums:
        if counts[num] < n:
            result.append(num)
            counts[num] += 1

    return result
