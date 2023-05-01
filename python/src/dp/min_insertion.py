"""
Find minimum number of insertion needed to make a string Palindrome
"""


def min_insertion(s: str, n: int) -> int:

    # know what the table tries to represent
    # table[i][j] stores min number of insertion need for s[i:j+1]
    table = [[0]*n for _ in range(n)]

    # think of how the table is constructed based on the recursive formula
    for gap in range(1, n):
        i = 0
        for j in range(gap, n):
            if s[i] == s[j]:
                table[i][j] = table[i + 1][j - 1]
            else:
                table[i][j] = min(table[i][j - 1], table[i + 1][j]) + 1
            i += 1

    return table[0][n - 1]