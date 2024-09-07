from functools import cache


def myPow(x: float, n: int) -> float:
    @cache
    def helper(x, n):
        # base case
        if x == 0:
            return 0
        if n == 0:
            return 1

        is_even = n % 2 == 0
        # we can divide by half if it is an even number
        if is_even:
            tmp = helper(x, n // 2)
            return tmp * tmp
        else:
            return x * helper(x, n - 1)

    # negative handling
    res = helper(x, abs(n))
    return res if n > 0 else 1 / res
