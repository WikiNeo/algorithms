class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        LEN_S, LEN_T = len(s), len(t)

        # dp[i][j] represents how many distinct subsequences of s[0..i] which equals t[0..j]
        dp = [[0 for _ in range(LEN_T + 1)] for _ in range(LEN_S + 1)]

        # we will initialize dp[i][0] = 1 since for an empty t, we can always find 1
        for i in range(LEN_S + 1):
            dp[i][0] = 1

        # now let's update the dp table
        for i in range(1, LEN_S + 1):
            for j in range(1, LEN_T + 1):
                # if we have the same character, then we can either include it or not.
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                else:  # otherwise, we can just skip it
                    dp[i][j] = dp[i - 1][j]

        return dp[LEN_S][LEN_T]
