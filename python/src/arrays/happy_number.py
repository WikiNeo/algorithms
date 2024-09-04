def isHappy(n: int) -> bool:
    n_str = str(n)

    while len(n_str) > 1:
        temp_n = sum([pow(int(num), 2) for num in n_str])
        n_str = str(temp_n)

    return n_str == "1" or n_str == "7"
