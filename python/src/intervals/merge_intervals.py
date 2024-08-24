from typing import List


def merge(intervals: List[List[int]]) -> List[List[int]]:
    LEN = len(intervals)
    if LEN == 1:
        return intervals

    intervals.sort()
    res = []
    tmpInterval = intervals[0]

    for i in range(len(intervals)):
        # tmpInterval is to the left of the current interval
        if tmpInterval[1] < intervals[i][0]:
            res.append(tmpInterval)
            tmpInterval = intervals[i]
        # tmpInterval is to the right of the current interval
        elif tmpInterval[0] > intervals[i][1]:
            res.append(intervals[i])
        else:
            tmpInterval = [
                min(tmpInterval[0], intervals[i][0]),
                max(tmpInterval[1], intervals[i][1]),
            ]

    res.append(tmpInterval)
    return res
