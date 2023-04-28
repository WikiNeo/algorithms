data = [1, 3, 5, 7]


# sorted 1, 2, 4, 7
# diff 1, 2, 3
# sum 6

# 2, 4, 1

# sorted 1, 2, 4
# diff  1, 2
# sum 3

def solve(arr):
    arr.sort()
    diff = []
    for i in range(0, len(arr) - 1):
        diff.append(arr[i + 1] - arr[i])
    res = len(arr)
    flag = 0
    bool_res = []
    for num in diff:
        if num % 2 == 0:  # even
            bool_res.append(True)
        else:  # odd
            bool_res.append(False)
            flag += 1

    if flag % 2 == 0:
        return res

    # [7, 5, 6, 2, 3, 2, 4]
    # [2, 2, 3, 4, 5, 6, 7]
    # [0, 1, 1, 1, 1, 1] sum: 5
    # [T, F, F, F, F, F]
    left, right = 0, len(bool_res) - 1
    count = 0
    while left <= right:
        count += 1
        if not bool_res[left] or not bool_res[right]:
            break
        left += 1
        right -= 1

    return res - count


print(solve(data))
