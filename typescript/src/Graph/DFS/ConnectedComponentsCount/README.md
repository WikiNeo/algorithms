# [Graph] Connected Components Count

## Problem

Write a function, connectedComponentsCount, that takes in the adjacency list of an undirected graph. The function should return the number of connected components within the graph.

## Thoughts

We can start DFS or BFS for a component, and return true when it has done exploration, then increase the count by 1.

Since the graph is undirected, we will use a Set to store visited node.

And note the key value type by default in Hash is String, and the value in graph array is integer, so we may need conversion for the value in Set
