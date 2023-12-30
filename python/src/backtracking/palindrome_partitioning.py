from typing import List


class Solution:
    def isPalin(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1

        return True

    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []
        LEN = len(s)

        def dfs(i):
            # add current partition to result
            if i >= LEN:
                res.append(part.copy())
                return

            # check if the s[i:j+1] is palindrome
            for j in range(i, LEN):
                if self.isPalin(s, i, j):
                    part.append(s[i:j + 1])
                    dfs(j + 1)  # continue from j + 1
                    part.pop()  # backtracking

        dfs(0)

        return res
