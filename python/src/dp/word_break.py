from typing import List


class Solution:
    def word_break(self, s: str, word_dict: List[str]) -> bool:
        s_len = len(s)
        dp = [False] * (s_len + 1)
        dp[s_len] = True

        for i in range(s_len - 1, -1, -1):
            for word in word_dict:
                word_len = len(word)
                if i + word_len <= s_len and s[i : i + word_len] == word:
                    dp[i] = dp[i + word_len]
                if dp[i]:
                    break

        return dp[0]
