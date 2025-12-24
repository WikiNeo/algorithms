"""
## Problem

Given a string s, find the length of the longest substring without repeating characters.

### Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

### Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

### Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

### Constraints:

- 0 <= s.length <= 5 * 10^4
- s consists of English letters, digits, symbols and spaces.

## Thoughts

- Use sliding window technique with two pointers (left and right)
- Use a set to track characters in the current window
- When we encounter a duplicate character, shrink the window from the left
- Keep track of the maximum length found
"""


def length_of_longest_substring(s: str) -> int:
    """
    Find the length of the longest substring without repeating characters.
    
    Uses sliding window technique with two pointers and a set to track characters.
    Time complexity: O(n) where n is the length of the string
    Space complexity: O(min(n, m)) where m is the size of the character set
    """
    if not s:
        return 0
    
    char_set = set()
    left = 0
    max_length = 0
    
    for right in range(len(s)):
        # Shrink window from left until we can add s[right]
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        
        # Add current character to set
        char_set.add(s[right])
        
        # Update max length
        max_length = max(max_length, right - left + 1)
    
    return max_length

