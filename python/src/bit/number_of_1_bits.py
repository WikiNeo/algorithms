def hammingWeight(n: int) -> int:
    res = 0
    for digit in bin(n):
        if digit == "1":
            res += 1

    return res
