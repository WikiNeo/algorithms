from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int] | None:
        LEN = len(edges)
        parent = [i for i in range(LEN + 1)]
        size = [1] * (LEN + 1)

        def find(x):
            # if x is not the root
            if parent[x] != x:
                # path compression
                parent[x] = find(parent[x])
            return parent[x]

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            # n1 and n2 have the same parent, which means they are in the same set,
            # hence a cycle
            if p1 == p2:
                return False

            # we will set the larger size as parent and increase its size
            if size[p1] > size[p2]:
                parent[p2] = p1
                size[p1] += size[p2]
            else:
                parent[p1] = p2
                size[p2] += size[p1]

            return True

        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]
