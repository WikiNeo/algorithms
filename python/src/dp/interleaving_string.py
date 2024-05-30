from functools import cache


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        LEN1, LEN2, LEN3 = len(s1), len(s2), len(s3)
        if LEN3 != LEN1 + LEN2:
            return False

        @cache
        def check(i, j, k):
            if i == LEN1 and j == LEN2 and k == LEN3:
                return True
            return k < LEN3 and (
                (i < LEN1 and s1[i] == s3[k] and check(i + 1, j, k + 1))
                or (j < LEN2 and s2[j] == s3[k] and check(i, j + 1, k + 1))
            )

        return check(0, 0, 0)
