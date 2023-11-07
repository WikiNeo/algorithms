"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

## Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

## Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

## Constraints

1 <= n <= 45

## Thoughts

- We can either reach step N from N - 1 or N - 2, so res[N] = res[N - 1] + res[N - 2]
- Clearly we have base case for N == 1 or N == 2
- We can use memoization method to save some calculation
- We can use tabulation method to reach the result from bottom up
"""


def climb_stairs_memoization(n: int) -> int:
    step_to_ways = {}

    def solve(steps):
        # base case
        if steps == 1 or steps == 2:
            return steps
        # cache case
        if steps in step_to_ways:
            return step_to_ways[steps]

        # calculate res and update cache
        res = solve(steps - 1) + solve(steps - 2)
        step_to_ways[steps] = res

        # return cache
        return res

    return solve(n)


def climb_stairs_tabulation(n: int) -> int:
    if n <= 2:
        return n

    # table to store
    step_to_ways = [0]*(n + 1)
    step_to_ways[1] = 1
    step_to_ways[2] = 2

    # update table based on the formula
    for i in range(3, n + 1):
        step_to_ways[i] = step_to_ways[i - 1] + step_to_ways[i - 2]

    return step_to_ways[n]
