import heapq
from collections import Counter, deque
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        q = deque()  # (cnt, expected time)

        time = 0
        while maxHeap or q:
            time += 1

            # if maxHeap is empty, we advance time to the first task in queue
            if not maxHeap:
                time = q[0][1]
            else:
                # we decrease count for max element in heap
                cnt = 1 + heapq.heappop(maxHeap)

                # if new cnt is not 0, we store the new count and expected time to queue
                if cnt:
                    q.append((cnt, time + n))

            # if we can process the task when the time is right
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])

        return time
