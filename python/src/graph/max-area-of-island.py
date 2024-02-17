from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()

        def getArea(row, col):
            """get the island area starting from (row, col)"""

            # Stop condition
            if (
                row < 0
                or row == ROWS
                or col < 0
                or col == COLS
                or grid[row][col] == 0
                or (row, col) in visited
            ):
                return 0

            # mark as visited
            visited.add((row, col))

            # recursively get the result
            return (
                1
                + getArea(row, col - 1)
                + getArea(row - 1, col)
                + getArea(row, col + 1)
                + getArea(row + 1, col)
            )

        # driver functions here
        area = 0
        for r in range(ROWS):
            for c in range(COLS):
                area = max(area, getArea(r, c))

        # return result here
        return area
