from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        LEN = len(nums)

        cur = []

        def dfs(i: int):
            if i == LEN:
                res.append(cur.copy())
                return

            # add current element to cur
            cur.append(nums[i])
            dfs(i + 1)

            # not adding current element to cur
            cur.pop()
            dfs(i + 1)

        dfs(0)

        return res
