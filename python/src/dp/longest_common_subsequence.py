class Solution:
    def longest_common_subsequence(self, text1: str, text2: str) -> int:
        LEN1 = len(text1)
        LEN2 = len(text2)

        # LEN2 + 1 is the column
        # LEN1 + 1 is the row
        # The LCS is 0 by default for all edge
        dp = [[0 for _ in range(LEN2 + 1)] for _ in range(LEN1 + 1)]

        for i in range(1, LEN1 + 1):
            for j in range(1, LEN2 + 1):
                if text1[i - 1] == text2[j - 1]:
                    # we have same end character, then we move both back by 1
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    # let's compare text1 substring i - 1 with text2 substring j - 1
                    if dp[i - 1][j] >= dp[i][j - 1]:
                        dp[i][j] = dp[i - 1][j]
                    else:
                        dp[i][j] = dp[i][j - 1]

        return dp[LEN1][LEN2]
