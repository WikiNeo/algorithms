from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """We can create visited set to mark the squares that can be reached
        starting from the edge
        """
        ROW, COL = len(heights), len(heights[0])
        pacVisited, atlVisited = set(), set()

        def dfs(row, col, visited, prevHeight):
            """Mark visited square starting at (row, col)"""
            if (
                row not in range(0, ROW)
                or col not in range(0, COL)
                or (row, col) in visited
                or heights[row][col] < prevHeight
            ):
                return

            visited.add((row, col))
            curHeight = heights[row][col]
            dfs(row, col - 1, visited, curHeight)
            dfs(row - 1, col, visited, curHeight)
            dfs(row, col + 1, visited, curHeight)
            dfs(row + 1, col, visited, curHeight)

        for row in range(ROW):
            dfs(row, 0, pacVisited, 0)
            dfs(row, COL - 1, atlVisited, 0)

        for col in range(COL):
            dfs(0, col, pacVisited, 0)
            dfs(ROW - 1, col, atlVisited, 0)

        return list(pacVisited & atlVisited)
