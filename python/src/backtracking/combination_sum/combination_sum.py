from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        LEN = len(candidates)

        cur = []

        def dfs(i, acc):
            if i >= LEN or acc > target:
                return
            if acc == target:
                res.append(cur.copy())
                return

            # take current value and stay the index
            cur.append(candidates[i])
            dfs(i, acc + candidates[i])

            # not take current value and continue
            cur.pop()
            dfs(i + 1, acc)

        dfs(0, 0)

        return res
