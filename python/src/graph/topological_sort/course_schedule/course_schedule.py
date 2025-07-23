from typing import List
from collections import defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # initialize the graph based on prerequisites [dst, src]
        graph = defaultdict(list)
        for dst, src in prerequisites:
            graph[src].append(dst)

        visiting, visited = set(), set()

        def dfs(node) -> bool:
            """return True if there is no cycle for topological sort ordering
            False otherwise"""

            # cycle detected
            if node in visiting:
                return False
            # already visited
            if node in visited:
                return True

            # mark current node as visiting
            visiting.add(node)
            for neighbour in graph[node]:
                if not dfs(neighbour):
                    return False

            # we have finished visited node so
            #   1. remove it from visiting
            #   2. mark it as visited
            visiting.remove(node)
            visited.add(node)

            return True

        for node in list(graph.keys()):
            if not dfs(node):
                return False

        return True
