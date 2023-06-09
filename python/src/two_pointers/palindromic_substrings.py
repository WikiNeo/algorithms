"""
## Problem

Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.

### Example 1:

Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".

### Example 2:

Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

### Constraints:

- 1 <= s.length <= 1000
- s consists of lowercase English letters.

## Thoughts

- We can check the palindrome substring from mid
- The palindrome substring can be of odd/even length
"""


def count_substrings(s: str) -> int:
    res = 0

    for i in range(len(s)):
        res += count_pali(s, i, i)      # odd length
        res += count_pali(s, i, i + 1)  # even length

    return res


def count_pali(s, left, right):
    """
    Give a string and left & right, we count number of palindromes we can form
    """
    res = 0

    # as long as we are not out of boundary and the can form a palindrome, we increase the count
    # by 1 and move the pointers
    while left >= 0 and right < len(s) and s[left] == s[right]:
        res += 1
        left -= 1
        right += 1

    return res
