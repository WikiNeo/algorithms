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
                res = s[l:r + 1]
            l -= 1
            r += 1

    # even case
    for i in range(len(s)):
        l, r = i, i + 1

        while l >= 0 and r < len(s) and s[l] == s[r]:
            cur_len = r - l + 1
            if cur_len > res_len:
                res_len = cur_len
                res = s[l:r + 1]
            l -= 1
            r += 1

    return res
