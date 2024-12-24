from typing import List
from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        myDeque = deque()
        time, freshCount = 0, 0
        ROW, COL = len(grid), len(grid[0])

        # preprocessing to
        #   1. initialize the deque for multiple source BFS
        #   2. update fresh orange count
        for row in range(ROW):
            for col in range(COL):
                if grid[row][col] == 2:
                    myDeque.append((row, col))
                if grid[row][col] == 1:
                    freshCount += 1

        # prepare directions to iterate
        directions = [[0, -1], [-1, 0], [0, 1], [1, 0]]
        # loop while we have rotten oranges in deque AND there are fresh oranges
        while len(myDeque) > 0 and freshCount > 0:
            # we need popleft for all current rotten oranges in deque
            #   note len(myDeque) is fixed and will only be calulated once
            for _ in range(len(myDeque)):
                row, col = myDeque.popleft()
                for dr, dc in directions:
                    newRow, newCol = row + dr, col + dc
                    # ensure the new position is in range AND is fresh
                    if (
                        newRow in range(ROW)
                        and newCol in range(COL)
                        and grid[newRow][newCol] == 1
                    ):
                        # rotten it AND add it to the deque
                        grid[newRow][newCol] = 2
                        myDeque.append((newRow, newCol))
                        # update fresh count
                        freshCount -= 1

            # one loop means 1 min
            time += 1

        return time if freshCount == 0 else -1
