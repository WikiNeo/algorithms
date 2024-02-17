"""
## Problem

Consider every subsequence of an array of integers
    - Sort the subsequence in increasing order
    - Determine the sum of differences of elements in the subsequence
    - Return the length of the longest subsequence where this sum is even

### Example

arr = [2, 4, 1, 7]
subsequence = [2, 4, 1, 7], sorted = [1, 2, 4, 7], diff = [1, 2, 3], sum = 6, valid, length = 4
subsequence = [2, 4, 1], sorted = [1, 2, 4], diff = [1, 2], sum = 3, invalid(odd)

### returns
    int: the length of the longest subsequence as described

### Constraints

- 3 <= n <= 10^5
- 0 <= arr[i] <= 10^9

## Thoughts

- Intuition is to enumerate all possible subsequences, sort it, calculate diff, sum, then compare
- However, n is large, so above is not practical
- Note we only want the LENGTH of the subsequence, not the subsequence itself, so we should have
    an easy way to get the LENGTH
- Note that the max length we can get is the length of the original array
    - So if the original array diff sum is even, we have a winner!
    - If the above sum is odd, we can try to remove an odd value to make it even
        - We either remove from left or right, get the min counts we need
        - The result should be original_length - count!
- GO!
"""

data = [1, 3, 5, 7]


# sorted 1, 2, 4, 7
# diff 1, 2, 3
# sum 6

# 2, 4, 1

# sorted 1, 2, 4
# diff  1, 2
# sum 3


def longest_subsequence_even_diff_sum(arr):
    """Find the longest sorted subsequence length of an array, where the diff between each element
    in the sorted one is even
    """

    # sort the array first
    arr.sort()

    # get the diff array
    diff = []
    for i in range(0, len(arr) - 1):
        diff.append(arr[i + 1] - arr[i])

    # temporarily set the result to be the max possible value
    res = len(arr)
    # we assume the sum is even
    is_even_sum = True
    # store the evenness of even value in diff array
    is_diff_even_arr = []
    for num in diff:
        if num % 2 == 0:  # even
            is_diff_even_arr.append(True)
        else:  # odd
            is_diff_even_arr.append(False)
            # we don't need to really calculate the sum
            is_even_sum = not is_even_sum

    # ideal case
    if is_even_sum:
        return res

    # [7, 5, 6, 2, 3, 2, 4]
    # [2, 2, 3, 4, 5, 6, 7]
    # [0, 1, 1, 1, 1, 1] sum: 5
    # [T, F, F, F, F, F]
    # find the count -> number of element we need to remove
    left, right = 0, len(is_diff_even_arr) - 1
    count = 0
    # typical two pointers condition
    while left <= right:
        # note how we handle the edge case here
        count += 1
        # we can return if an odd value is found
        if not is_diff_even_arr[left] or not is_diff_even_arr[right]:
            break
        # remember to move the pointers
        left += 1
        right -= 1

    # winner here!
    return res - count
