import heapq
from typing import List


class Solution:
    """build a min heap with distance and points, and get first k points. Note that tuple is faster than List"""

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pts = [(x * x + y * y, (x, y)) for x, y in points]
        heapq.heapify(pts)

        res = []
        for i in range(k):
            res.append(heapq.heappop(pts)[1])
        return res
