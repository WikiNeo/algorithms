"""
## Problem

You are given an array points representing integer coordinates of some points on a 2D-plane,
where points[i] = [xi, yi].

The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them:
|xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.

Return the minimum cost to make all points connected. All points are connected if there is exactly
one simple path between any two points.

## Thoughts

- This is a typical MST problem
- We can build the graph first, then implement the Prim's Algorithm
"""

from typing import List
import heapq


def min_cost_connect_points(points: List[List[int]]) -> int:
    # initialize the weighted graph
    N = len(points)
    graph = {i: [] for i in range(N)}  # i: [cost, point]

    # build the weighted graph
    for i in range(N):
        x1, y1 = points[i]
        for j in range(i + 1, N):
            x2, y2 = points[j]
            cost = abs(x1 - x2) + abs(y1 - y2)
            graph[i].append([cost, j])
            graph[j].append([cost, i])

    # implement Prim's Algorithm
    visited = set()
    res = 0
    min_h = [[0, 0]]  # min heap [cost, point]
    while len(visited) < N:
        cost, i = heapq.heappop(min_h)
        if i in visited:
            continue
        visited.add(i)
        res += cost
        for neighCost, nei in graph[i]:
            if nei not in visited:
                heapq.heappush(min_h, [neighCost, nei])

    return res
