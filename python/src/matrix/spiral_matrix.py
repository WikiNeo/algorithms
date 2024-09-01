from typing import List


def spiralOrder(matrix: List[List[int]]) -> List[int]:
    res = []
    # let's set boundary for the loop
    left, right = 0, len(matrix[0])
    top, bottom = 0, len(matrix)

    while left < right and top < bottom:
        # process top
        for j in range(left, right):
            res.append(matrix[top][j])
        top += 1

        # process right
        for i in range(top, bottom):
            res.append(matrix[i][right - 1])
        right -= 1

        # if the condition is invalid, break
        if not (left < right and top < bottom):
            break

        # process bottom
        for j in range(right - 1, left - 1, -1):
            res.append(matrix[bottom - 1][j])
        bottom -= 1

        # process left
        for i in range(bottom - 1, top - 1, -1):
            res.append(matrix[i][left])
        left += 1

    return res
