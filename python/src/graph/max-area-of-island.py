from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        ROW = len(grid)
        COL = len(grid[0])
        visited = set()

        def getIslandArea(row: int, col: int):
            """return the size of the island starting at (row, col).
            It also marks the explored grid
            """
            # out of boundary
            if row < 0 or row >= ROW or col < 0 or col >= COL:
                return 0
            # water
            if grid[row][col] == 0:
                return 0
            # visited
            if (row, col) in visited:
                return 0

            # mark as visited
            visited.add((row, col))

            # explore all four directions
            return (
                1
                + getIslandArea(row, col - 1)
                + getIslandArea(row - 1, col)
                + getIslandArea(row, col + 1)
                + getIslandArea(row + 1, col)
            )

        for row in range(ROW):
            for col in range(COL):
                res = max(res, getIslandArea(row, col))

        return res
