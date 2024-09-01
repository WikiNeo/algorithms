from typing import List


def setZeroes(matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.

    Let's use the first row and first column to store if we should set the whole row of column to 0.
    We use also new a variable rowZero to represent if we should set first row to zero so matrix[0][0] == 0 only means first column should be set to 0
    """
    ROW, COL = len(matrix), len(matrix[0])
    rowZero = False

    # Let's first go through the matrix to set the first row, column and rowZero variable
    for i in range(ROW):
        for j in range(COL):
            if matrix[i][j] == 0:
                matrix[0][j] = 0  # set column 0
                if i == 0:
                    rowZero = True  # we have special variable for the first row
                else:
                    matrix[i][0] = 0  # set row 0

    # Let's ignore first row and column and update the remaning matrix
    for i in range(1, ROW):
        for j in range(1, COL):
            # if we can find 0 in either first row or first column, set matrix[i][j] to 0
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0

    # Let's set the first column now
    if matrix[0][0] == 0:
        for i in range(ROW):
            matrix[i][0] = 0

    # Last but not least, let's use the special variable to set the first row
    if rowZero:
        for j in range(COL):
            matrix[0][j] = 0
