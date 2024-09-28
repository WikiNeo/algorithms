def reverseBits(n: int) -> int:
    res = 0
    # since we know it is 32 bit integer, we can loop every digit
    for i in range(32):
        # get the ith digit from right
        bit = (n >> i) & 1
        # add it to the result from left
        res += bit << (31 - i)

    return res
