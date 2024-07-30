from typing import List
from random import randint


def my_shuffle(arr: List[int]) -> List[int]:
    LEN = len(arr)

    for i in range(LEN - 1, 0, -1):
        j = randint(0, i + 1)

        arr[i], arr[j] = arr[j], arr[i]

    return arr


if __name__ == "__main__":
    print(my_shuffle([1, 2, 3, 4, 5, 6, 7, 8, 9]))
