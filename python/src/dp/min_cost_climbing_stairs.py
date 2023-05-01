"""
You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you
pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.

## Example 1:

Input: cost = [10,15,20]
Output: 15
Explanation: You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.

## Thoughts

- We can have a table to store the cost to reach step i -> table[i]
- We have two ways to reach step i, with i - 1 or i -2
- The corresponding cost is table[i - 1] + cost[i - 1] and table[i - 2] + cost[i - 2]
- We should update the table with Min value of above
"""
from typing import List


def min_cost_climbing_stairs(cost: List[int]) -> int:
    N = len(cost)
    table = [0] * (N + 1)
    for i in range(2, N + 1):
        table[i] = min(table[i - 2] + cost[i - 2], table[i - 1] + cost[i - 1])

    return table[N]