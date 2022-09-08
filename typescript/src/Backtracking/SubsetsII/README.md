# Subsets II

## Problem

Given an integer array `nums` that may contain duplicates, return all possible subsets (the power set).

The solution set **must not** contain duplicate subsets. Return the solution in **any order**.

### Example 1:

```
Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
```

### Example 2:

```
Input: nums = [0]
Output: [[],[0]]
```

#### Constraints:

- `1 <= nums.length <= 10`
- `-10 <= nums[i] <= 10`

## Thoughts

- In the decision tree, we ignore the values that can cause duplicated
  results, sort `nums` first, and do some consecutive check with `while` loop
- Pointer location for end/success condition

## Reference

- [https://leetcode.com/problems/subsets-ii/](https://leetcode.com/problems/subsets-ii/)
