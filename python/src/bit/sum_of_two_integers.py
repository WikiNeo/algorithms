class Solution:
    def getSum(self, a: int, b: int) -> int:

        MASK = 0xFFFFF

        # we only care about the last few bits since -1000 <= a, b <= 1000
        while (b & MASK) != 0:
            # get the carry vaule by AND and left shift by 1
            temp = (a & b) << 1
            # get the sum without carry by XOR
            a = a ^ b
            b = temp

        # handles overflow
        return (a & MASK) if b > 0 else a
