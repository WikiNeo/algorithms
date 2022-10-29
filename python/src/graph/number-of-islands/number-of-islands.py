from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS: int = len(grid)
        COLS: int = len(grid[0])
        visited = set()
        count = 0

        def dfs(row: int, col: int) -> bool:
            """return true if we can find an island starting from (row, col)"""
            ...

            # fail condition
            if row < 0 or row >= ROWS or col < 0 or col >= COLS:
                return False
            if grid[row][col] == '0':
                return False
            if (row, col) in visited:
                return False

            # mark (row, col) as visited
            visited.add((row, col))

            # visit neighbours and mark them
            dfs(row, col - 1)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row + 1, col)

            return True

        for i in range(ROWS):
            for j in range(COLS):
                if dfs(i, j):
                    count += 1

        return count
