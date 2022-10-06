from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        cur = []

        def dfs(i, acc):
            # note we have success condition first here
            if acc == target:
                res.append(cur.copy())
                return
            if i >= len(candidates) or acc > target:
                return

            # take the value
            cur.append(candidates[i])
            dfs(i + 1, acc + candidates[i])

            # not take the value and ignore all same values
            cur.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, acc)

        dfs(0, 0)

        return res