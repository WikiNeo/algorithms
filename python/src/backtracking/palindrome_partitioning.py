from typing import List


class Solution:
    def isPalin(self, s, left_index, right_index):
        while left_index < right_index:
            if s[left_index] != s[right_index]:
                return False
            left_index, right_index = left_index + 1, right_index - 1

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
                    part.append(s[i : j + 1])
                    dfs(j + 1)  # continue from j + 1
                    part.pop()  # backtracking

        dfs(0)

        return res
