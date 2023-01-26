from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # get boundary values for 2-D problems first
        ROWS: int = len(grid)
        COLS: int = len(grid[0])

        # stores visited coordinate
        visited = set()

        # final result count
        count = 0

        def dfs(row: int, col: int) -> bool:
            """return true if we can find an island starting from (row, col)

            The side effect is that we will mark the visited location
            """

            # fail conditions
            if row < 0 or row >= ROWS or col < 0 or col >= COLS: # out of boudary
                return False
            if grid[row][col] == '0':   # find water
                return False
            if (row, col) in visited:   # visited already
                return False

            # mark (row, col) as visited
            visited.add((row, col))

            # visit neighbours and mark them
            dfs(row, col - 1)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row + 1, col)

            return True

        # start from each location and check results
        for i in range(ROWS):
            for j in range(COLS):
                if dfs(i, j):
                    count += 1

        return count


if __name__ == '__main__':
    grid1 = [
      ["1","1","1","1","0"],
      ["1","1","0","1","0"],
      ["1","1","0","0","0"],
      ["0","0","0","0","0"]
    ]
    solution1: Solution = Solution()
    assert solution1.numIslands(grid1) == 1

    grid2 = [
      ["1","1","0","0","0"],
      ["1","1","0","0","0"],
      ["0","0","1","0","0"],
      ["0","0","0","1","1"]
    ]
    solution2: Solution = Solution()
    assert solution2.numIslands(grid2) == 3

