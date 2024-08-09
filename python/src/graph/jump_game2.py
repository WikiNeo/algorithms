from typing import List


def jump1(nums: List[int]) -> int:
    """We will use left and right to represent the interval we can currently
    jump to
    """
    res, left, right = 0, 0, 0

    # we will stop when the final index is included in the interval, in this
    # case, the right will be equal or larger than it
    while right < len(nums) - 1:
        new_right = 0
        for i in range(left, right + 1):
            # the maximum we can jump to is current index + current value
            new_right = max(new_right, i + nums[i])

        # new left will be right + 1
        left = right + 1
        right = new_right
        res += 1

    return res


def jump2(nums: List[int]) -> int:
    """Since we can always jump to the end, so let's just backward greedily."""
    LEN = len(nums)
    cur_index = LEN - 1
    count = 0

    # we will keep jumping until we reach index 0
    while cur_index != 0:
        # we try to jump as long as we can
        i = cur_index
        while i > 0:
            # if we can't jump with i length, decreasee it
            if nums[cur_index - i] < i:
                i -= 1
                continue
            else:
                # other wise, we jump, increase the count, and update current
                # index
                count += 1
                cur_index = cur_index - i
                break

    return count
