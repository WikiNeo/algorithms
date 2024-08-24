from typing import List


def insert(intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    res = []

    for i in range(len(intervals)):
        # new interval is to the left of current interval
        if newInterval[1] < intervals[i][0]:
            # we will add the new interval and the remaining
            res.append(newInterval)
            return res + intervals[i:]
        # new interval is to the right of current interval
        elif newInterval[0] > intervals[i][1]:
            # we will just add the current interval
            res.append(intervals[i])
        else:
            # if there is overlap, we will update the new interval
            newInterval = [
                min(newInterval[0], intervals[i][0]),
                max(newInterval[1], intervals[i][1]),
            ]

    # if we don't early return, append newInterval here.
    res.append(newInterval)
    return res


if __name__ == "__main__":
    print(insert([[1, 3], [6, 9]], [2, 5]))
