class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        LEN1, LEN2 = len(word1), len(word2)

        dp = [[0 for _ in range(LEN2 + 1)] for _ in range(LEN1 + 1)]
        for j in range(LEN2 + 1):
            dp[0][j] = j
        for i in range(LEN1 + 1):
            dp[i][0] = i

        for i in range(1, LEN1 + 1):
            for j in range(1, LEN2 + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i][j - 1], dp[i - 1][j - 1], dp[i - 1][j])

        return dp[LEN1][LEN2]
