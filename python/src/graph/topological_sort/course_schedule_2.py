from typing import List
from collections import defaultdict, deque


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # build graph based on prerequisites
        graph = defaultdict(list)
        for dst, src in prerequisites:
            graph[src].append(dst)

        # initialize sets and result
        visited, visiting = set(), set()
        result = deque()

        def dfs(node):
            # cycle detected
            if node in visiting:
                return False
            if node in visited:
                return True

            # mark current visiting node
            visiting.add(node)
            for neighbour in graph[node]:
                if neighbour not in visited:
                    if not dfs(neighbour):
                        return False

            # remove current visiting node and update result
            visiting.remove(node)
            visited.add(node)
            result.appendleft(node)

            return True

        # driver for all courses
        for i in range(numCourses):
            if not dfs(i):
                return []

        return list(result)
