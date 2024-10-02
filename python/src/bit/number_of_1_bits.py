def hammingWeight(n: int) -> int:
    res = 0
    while n:
        # we check last bit and shift the number until it is 0
        res += n & 1
        n >>= 1

    return res
