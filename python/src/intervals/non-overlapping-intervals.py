from typing import List


def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
    intervals.sort()
    res = 0
    prev_end = intervals[0][1]

    for start, end in intervals[1:]:
        # no overlapping, update end
        if start >= prev_end:
            prev_end = end
        else:  # overlapping, remove the one with larger end and keeping the small one
            res += 1
            prev_end = min(prev_end, end)

    return res
