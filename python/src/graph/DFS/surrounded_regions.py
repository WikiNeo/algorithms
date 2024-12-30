"""preprocess with DFS from edges"""

from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROW, COL = len(board), len(board[0])

        def capture(row, col):
            """mark cells starting from (row, col) as 'T'"""
            if row not in range(ROW) or col not in range(COL) or board[row][col] != "O":
                return

            board[row][col] = "T"
            capture(row, col - 1)
            capture(row - 1, col)
            capture(row, col + 1)
            capture(row + 1, col)

        # mark all connected cells starting from edge as 'T'
        for r in range(ROW):
            for c in range(COL):
                if (r == 0 or r == ROW - 1 or c == 0 or c == COL - 1) and board[r][
                    c
                ] == "O":
                    capture(r, c)

        # mark remaining 'O' cells as 'X'
        for r in range(ROW):
            for c in range(COL):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"
