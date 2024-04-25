"""
The rod-cutting problem is the following. Given a rod of length n inches and a
table of prices pi for i in [1...n] , determine the maximum revenue rn obtainable
by cutting up the rod and selling the pieces.

## Thought


"""

length_to_price = {
    0: 0,
    1: 1,
    2: 5,
    3: 8,
    4: 9,
    5: 10,
    6: 17,
    7: 17,
    8: 20,
    9: 24,
    10: 30,
}


def cut_rod_top_down(n):
    length_to_max_profit = {0: 0}

    def dfs(length):
        # base case
        if length in length_to_max_profit:
            return length_to_max_profit[length]

        max_profit = 0
        for i in range(1, length + 1):
            # we can get max profit for length by either selling it as a whole
            # OR cut it with length i first and sell remaining
            max_profit = max(max_profit, length_to_price[i] + dfs(length - i))

        # cache it
        length_to_max_profit[length] = max_profit

        # return result
        return max_profit

    return dfs(n)


def cut_rod_bottom_up(n):
    length_to_max_profit = [0] * (n + 1)

    for i in range(1, n + 1):
        for j in range(1, i + 1):
            length_to_max_profit[i] = max(
                length_to_max_profit[i],
                length_to_price[j] + length_to_max_profit[i - j],
            )

    return length_to_max_profit[n]
