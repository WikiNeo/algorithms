from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # base case
        if len(nums) == 1:
            return [nums.copy()]

        # hold the final result
        res = []

        # we iterate through each number in list and remove it
        for i in range(len(nums)):
            nums_copy = nums.copy()
            nums_copy.pop(i)
            # get the remaining permutation and append the removed value in the end
            for temp in self.permute(nums_copy):
                temp.append(nums[i])
                res.append(temp)

        return res


solution = Solution()
print(solution.permute([1, 2]))
