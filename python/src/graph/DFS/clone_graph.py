"""hashmap + DFS solution to clone a graph."""

from typing import Optional


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    @staticmethod
    def clone_graph(node: Optional["Node"]) -> Optional["Node"]:
        old_to_new = {}

        def dfs(_node: "Node"):
            """For a given node in old graph, return a copy of the new node."""

            # return the new node if we already have the mapping
            if _node in old_to_new:
                return old_to_new[_node]

            # create the new node and update the mapping
            copy = Node(_node.val)
            old_to_new[_node] = copy

            # update the new node neighbours
            for nei in _node.neighbors:
                copy.neighbors.append(dfs(nei))

            # return the new node
            return copy

        return dfs(node) if node else None
