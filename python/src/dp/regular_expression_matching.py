class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        LEN_S, LEN_P = len(s), len(p)
        table = [[False for _ in range(LEN_P + 1)] for _ in range(LEN_S + 1)]
        table[0][0] = True  # empty string matches empty pattern
        for j in range(LEN_P + 1):
            if p[j - 1] == "*" and j - 2 >= 0:
                table[0][j] = table[0][
                    j - 2
                ]  # '*' matches zero occurrence of the preceding element

        for i in range(1, LEN_S + 1):
            for j in range(1, LEN_P + 1):
                if (
                    s[i - 1] == p[j - 1] or p[j - 1] == "."
                ):  # we have a match with . or the same character
                    table[i][j] = table[i - 1][j - 1]
                elif p[j - 1] == "*":
                    table[i][j] = table[i][
                        j - 2
                    ]  # '*' matches zero occurrence of the preceding element
                    if (
                        p[j - 2] == "." or p[j - 2] == s[i - 1]
                    ):  # '*' matches one or more occurrence of the preceding element
                        table[i][j] = table[i][j] or table[i - 1][j]

        return table[LEN_S][LEN_P]
