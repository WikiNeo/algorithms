from collections import defaultdict, Counter
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        LEN = len(word)
        visited = set()

        def dfs(row, col, i):
            if i == LEN:
                return True
            if row < 0 or row >= ROWS or col < 0 or col >= COLS:
                return False
            if board[row][col] != word[i]:
                return False
            if (row, col) in visited:
                return False

            visited.add((row, col))
            res = (dfs(row, col - 1, i + 1) or
                   dfs(row - 1, col, i + 1) or
                   dfs(row, col + 1, i + 1) or
                   dfs(row + 1, col, i + 1))
            visited.remove((row, col))

            return res

        # To prevent TLE,reverse the word if frequency of the first letter is more than the last letter's
        count = defaultdict(int, sum(map(Counter, board), Counter()))
        if count[word[0]] > count[word[-1]]:
            word = word[::-1]

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0) == True:
                    return True

        return False