# Permutations

## Problem

Given an array `nums` of distinct integers, return *all the possible permutations*. You can return the answer in **any order**.

### Example 1:

```
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
```

### Example 2:

```
Input: nums = [0,1]
Output: [[0,1],[1,0]]
```

### Example 3:

```
Input: nums = [1]
Output: [[1]]
```

### Constraints:

- 1 <= nums.length <= 6
- -10 <= nums[i] <= 10
- All the integers of nums are unique.

## Thoughts

- If `nums` only has one element, we can just return the result
- If `nums` has more than one element, we can remove first element, find
  permutations of the remaining elements, add the removed element back, then
  we have one result.
    - We need do above operation n times.

## Reference

- [https://leetcode.com/problems/permutations/](https://leetcode.com/problems/permutations/)
