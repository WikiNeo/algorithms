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

## Solutions

### Solution 1: Expand Around Center (Current)
For each position in the string, expand outward to find palindromes:
- Odd-length palindromes: center at a single character
- Even-length palindromes: center between two characters

Time Complexity: O(n²)
Space Complexity: O(1)

### Solution 2: Manacher's Algorithm (Optimized)
Uses dynamic programming with palindrome mirroring to avoid redundant checks.
- Preprocesses string with separators to handle odd/even uniformly
- Uses previously computed palindrome lengths to skip checks

Time Complexity: O(n)
Space Complexity: O(n)
"""


def longest_palindrome(s: str) -> str:
    """
    Find the longest palindromic substring using expand-around-center approach.
    
    Args:
        s: Input string
        
    Returns:
        The longest palindromic substring
    """
    if not s:
        return ""
    
    start = 0
    max_length = 0
    
    def expand_around_center(left: int, right: int) -> tuple[int, int]:
        """
        Expand around center and return the longest palindrome boundaries.
        
        Args:
            left: Left boundary index
            right: Right boundary index
            
        Returns:
            Tuple of (start_index, length) of the longest palindrome found
        """
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        # After the loop, left and right are one step beyond the palindrome
        # So the palindrome is from left+1 to right-1
        return left + 1, right - left - 1
    
    for i in range(len(s)):
        # Check for odd-length palindromes (center at i)
        left, length = expand_around_center(i, i)
        if length > max_length:
            start = left
            max_length = length
        
        # Check for even-length palindromes (center between i and i+1)
        left, length = expand_around_center(i, i + 1)
        if length > max_length:
            start = left
            max_length = length
    
    return s[start:start + max_length]


def longest_palindrome_manacher(s: str) -> str:
    """
    Find the longest palindromic substring using Manacher's Algorithm.
    
    This is the optimal solution with O(n) time complexity.
    
    Args:
        s: Input string
        
    Returns:
        The longest palindromic substring
    """
    if not s:
        return ""
    
    # Preprocess: insert separators to handle odd/even uniformly
    # e.g., "abc" -> "^#a#b#c#$"
    processed = ['^']
    for char in s:
        processed.append('#')
        processed.append(char)
    processed.append('#')
    processed.append('$')
    processed_str = ''.join(processed)
    
    n = len(processed_str)
    # P[i] stores the radius of the palindrome centered at i
    P = [0] * n
    center = 0  # Center of the rightmost palindrome found so far
    right = 0   # Right boundary of the rightmost palindrome
    
    max_len = 0
    center_index = 0
    
    for i in range(1, n - 1):  # Skip ^ and $
        # Mirror index: if i is within the current rightmost palindrome,
        # we can use the mirror to get a starting value
        if i < right:
            mirror = 2 * center - i
            P[i] = min(right - i, P[mirror])
        
        # Try to expand around center i
        while processed_str[i + (1 + P[i])] == processed_str[i - (1 + P[i])]:
            P[i] += 1
        
        # Update center and right if we found a palindrome extending beyond right
        if i + P[i] > right:
            center = i
            right = i + P[i]
        
        # Track the longest palindrome
        if P[i] > max_len:
            max_len = P[i]
            center_index = i
    
    # Extract the original substring
    # center_index is in processed string, convert back to original
    start = (center_index - max_len) // 2
    return s[start:start + max_len]


if __name__ == "__main__":
    # Test cases for both solutions
    test_cases = [
        "babad",
        "cbbd",
        "a",
        "ac",
        "racecar",
        "noon",
        "abcdef",
    ]
    
    print("Testing Expand Around Center (O(n²)):")
    for test in test_cases:
        result = longest_palindrome(test)
        print(f"  '{test}' -> '{result}'")
    
    print("\nTesting Manacher's Algorithm (O(n)):")
    for test in test_cases:
        result = longest_palindrome_manacher(test)
        print(f"  '{test}' -> '{result}'")
    
    # Verify both solutions give the same results
    print("\nVerifying both solutions match:")
    all_match = True
    for test in test_cases:
        result1 = longest_palindrome(test)
        result2 = longest_palindrome_manacher(test)
        if len(result1) != len(result2):
            print(f"  MISMATCH for '{test}': '{result1}' vs '{result2}'")
            all_match = False
    
    if all_match:
        print("  ✓ All solutions match!")
    else:
        print("  ✗ Some solutions don't match")
