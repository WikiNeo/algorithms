from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROW, COL = len(matrix), len(matrix[0])
        res = 0
        dp = {}

        def dfs(i, j, prev_value):
            if i < 0 or i >= ROW or j < 0 or j >= COL or matrix[i][j] <= prev_value:
                return 0
            if (i, j) in dp:
                return dp[(i, j)]

            cur_value = matrix[i][j]
            cur_res = 1
            cur_res = max(
                cur_res,
                1 + dfs(i - 1, j, cur_value),
                1 + dfs(i + 1, j, cur_value),
                1 + dfs(i, j - 1, cur_value),
                1 + dfs(i, j + 1, cur_value),
            )
            dp[(i, j)] = cur_res

            return cur_res

        for i in range(ROW):
            for j in range(COL):
                res = max(res, dfs(i, j, -1))

        return res
