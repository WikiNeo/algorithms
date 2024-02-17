import heapq
from typing import List


class Solution:
    """Maintain a max heap by updating it with first 2 largest values"""

    def last_stone_weight(self, stones: List[int]) -> int:
        # reverse the values in stones so we can create max heap
        stones = [-stone for stone in stones]
        heapq.heapify(stones)

        # get largest two stones while LEN > 1, and push result to the heap
        while len(stones) > 1:
            first: int = heapq.heappop(stones)
            second: int = heapq.heappop(stones)
            heapq.heappush(stones, first - second)

        # empty case handle
        stones.append(0)
        return abs(stones[0])
