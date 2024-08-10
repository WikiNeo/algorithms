from typing import List


def mergeTriplets(triplets: List[List[int]], target: List[int]) -> bool:
    # let's use a set to store if we can get the target value for index
    good_index = set()

    for t in triplets:
        # we filter out the triplets if any digit is larger than our target
        if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
            continue

        # for the good triplets, we check which index it can format and
        # update the set
        for i, v in enumerate(t):
            if target[i] == v:
                good_index.add(i)

    # we are good if we can get targer value for all 3 indices
    return len(good_index) == 3
