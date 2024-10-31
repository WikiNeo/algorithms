import math


class Solution:
    def reverse(self, x: int) -> int:
        MIN = -(2**31)
        MAX = 2**31 - 1
        PRE_MAX = MAX // 10
        LAST_DIGIT_MAX = MAX % 10
        PRE_MIN = MIN // 10
        LAST_DIGIT_MIN = MIN % 10

        res = 0
        while x:
            # get last digit to handle -1 % 10
            digit = int(math.fmod(x, 10))
            # integer division to handl -1 // 10
            x = int(x / 10)

            # check if without last digit we are already overflow
            #   or with last digit we will be overflow
            if res > PRE_MAX or (res == PRE_MAX and digit > LAST_DIGIT_MAX):
                return 0
            if res < PRE_MIN or (res == PRE_MIN and digit < LAST_DIGIT_MIN):
                return 0

            res = res * 10 + digit

        return res
