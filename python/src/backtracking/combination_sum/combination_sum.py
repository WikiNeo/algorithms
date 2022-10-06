from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        LEN = len(candidates)

        cur = []

        def exec(i, acc):
            if i >= LEN or acc > target:
                return
            if acc == target:
                res.append(cur.copy())
                return

            # take current value and stay the index
            cur.append(candidates[i])
            exec(i, acc + candidates[i])

            # not take current value and continue
            cur.pop()
            exec(i + 1, acc)

        exec(0, 0)

        return res
