from collections import defaultdict
from typing import List


class DetectSquares:
    def __init__(self):
        self.map_count = defaultdict(int)
        self.points = []

    def add(self, point: List[int]) -> None:
        # store the point count mapping
        self.map_count[tuple(point)] += 1
        self.points.append(point)

    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point
        for x, y in self.points:
            # we try to find diagonal point
            if abs(px - x) != abs(py - y) or x == px or y == py:
                continue
            res += self.map_count[(x, py)] * self.map_count[(px, y)]

        return res


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
