"""
## Problem

Given a string s, return the longest palindromic substring in s.

### Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

### Example 2:

Input: s = "cbbd"
Output: "bb"

### Constraints:

- 1 <= s.length <= 1000
- s consist of only digits and English letters.

## Thoughts

- There are two ways we can check if a substring is palindromic, from middle or from both end
- Note the length of the palindrome can be ood or even
"""


def longest_palindrome(s: str) -> str:
    res = ""
    res_len = 0

    # odd case
    for i in range(len(s)):
        l, r = i, i

        while l >= 0 and r < len(s) and s[l] == s[r]:
            cur_len = r - l + 1
            if cur_len > res_len:
                res_len = cur_len
                res = s[l : r + 1]
            l -= 1
            r += 1

    # even case
    for i in range(len(s)):
        l, r = i, i + 1

        while l >= 0 and r < len(s) and s[l] == s[r]:
            cur_len = r - l + 1
            if cur_len > res_len:
                res_len = cur_len
                res = s[l : r + 1]
            l -= 1
            r += 1

    return res


def longest_palindrome2(s: str) -> str:
    LEN = len(s)
    if LEN == 1:
        return s[0]

    odd_max_len = 1
    odd_res = s[0]
    for i in range(1, LEN):
        # odd length case
        left, right = i, i
        while left >= 0 and right < LEN:
            if s[left] != s[right]:
                break
            else:
                cur_len = right - left + 1
                if cur_len > odd_max_len:
                    odd_max_len = cur_len
                    odd_res = s[left : right + 1]
            left -= 1
            right += 1

    even_max_len = 1
    even_res = s[0]
    for i in range(1, LEN):
        left, right = i - 1, i
        while left >= 0 and right < LEN:
            if s[left] != s[right]:
                break
            else:
                cur_len = right - left + 1
                if cur_len > even_max_len:
                    even_max_len = cur_len
                    even_res = s[left : right + 1]
            left -= 1
            right += 1

    if odd_max_len > even_max_len:
        return odd_res
    else:
        return even_res
