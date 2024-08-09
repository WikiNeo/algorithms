def cancompletecircuit(gas: list[int], cost: list[int]) -> int:
    LEN = len(gas)
    net = [gas[i] - cost[i] for i in range(LEN)]

    # we can't reach the start again with 0 sum
    if sum(net) < 0:
        return -1

    res = 0
    total = 0
    for i in range(LEN):
        total += net[i]
        # if we ever has negative sum, it means the current starting station is invalid, we need try the next one
        if total < 0:
            total = 0
            res = i + 1

    return res
