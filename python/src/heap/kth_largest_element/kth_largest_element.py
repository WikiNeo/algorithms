import heapq
from typing import List


class KthLargest:
    """Maintain min heap of size k to find k-th largest element in O(1) time.
    """

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)

        # we keep a min heap of size k
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        # maintain min heap of size k
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)

        return self.heap[0]
