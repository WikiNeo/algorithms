from typing import List


def partitionLabels(s: str) -> List[int]:
    LEN = len(s)
    cur_s = set()  # use set to maintain characters for current interval
    cur_l, cur_r = 0, 0  # left and right index of current interval
    res = []

    while cur_l < LEN:
        # we will keep moving a pointer until we are out of right boundary
        p = cur_l
        while p <= cur_r and p < LEN:
            # update set here
            if s[p] not in cur_s:
                cur_s.add(s[p])
            else:
                # skip and increase pointer if we have seen it before
                p += 1
                continue

            # update right boundary and increase pointer
            cur_r = max(cur_r, s.rfind(s[p]))
            p += 1

        # we are done with one interval, reset for next one
        cur_s.clear()
        res.append(cur_r - cur_l + 1)
        cur_l = cur_r + 1
        cur_r = cur_l

    return res
