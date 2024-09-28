def hammingWeight(n: int) -> int:
    res = 0
    while n:
        # we check last bit and shift the number until it is 0
        res += n & 1
        n >>= 1

    return res


def hammingWeight2(n: int) -> int:
    res = 0
    # we use string manipulation
    for digit in bin(n):
        if digit == "1":
            res += 1

    return res
