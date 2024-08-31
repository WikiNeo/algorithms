from typing import List


def rotate(self, matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """

    LEN = len(matrix[0])

    # let's first transpose the matrix
    for i in range(LEN):
        for j in range(i + 1, LEN):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # then let's reverse each line
    for line in matrix:
        line.reverse()
