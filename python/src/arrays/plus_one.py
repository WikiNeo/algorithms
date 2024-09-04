from typing import List


def plusOne(digits: List[int]) -> List[int]:
    res = []
    carry = 1  # set to 1 so we can do the first +1

    for i in range(len(digits) - 1, -1, -1):
        if carry:
            new_digit = digits[i] + carry
            # insert with carry
            res.insert(0, new_digit % 10)
            # update carry
            carry = 1 if new_digit >= 10 else 0
        else:  # insert without carry
            res.insert(0, digits[i])

    # first digit 1
    if carry:
        res.insert(0, 1)

    return res
