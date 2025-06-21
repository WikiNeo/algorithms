from typing import List
import heapq


def minInterval(intervals: List[List[int]], queries: List[int]) -> List[int]:
    # we sort the intervals first
    intervals.sort()
    # prepare a min heap to store (length_of_interval, right_value)
    minHeap = []
    # have res[q] = value mapping and i for interval pointer
    res, i = {}, 0
    # we try to query the sorted queries
    for q in sorted(queries):
        # we add all intervals data with left index less than or equal to q
        while i < len(intervals) and intervals[i][0] <= q:
            left, right = intervals[i]
            heapq.heappush(minHeap, (right - left + 1, right))
            i += 1
        # let's pop out the invalid values whose right value is less than q
        while minHeap and minHeap[0][1] < q:
            heapq.heappop(minHeap)
        # let's update the result here with potential -1
        res[q] = minHeap[0][0] if minHeap else -1

    # construct the final list
    return [res[q] for q in queries]
