from typing import List


class Solution:
    """we can use the following 3 methods to solve the problem

    1. sort
    2. max heap
    3. quick select
    """

    @staticmethod
    def find_kth_largest(nums: List[int], k: int) -> int:
        expected_index: int = len(nums) - k

        def quick_select(left: int, right: int) -> int:
            pivot_value, pivot_ptr = nums[right], left
            for i in range(left, right):
                # if current value is less than pivot value, we swap current value with pivot pointer value
                if nums[i] <= pivot_value:
                    nums[pivot_ptr], nums[i] = nums[i], nums[pivot_ptr]
                    pivot_ptr += 1
            # after the iteration, we swap pivot value (right value) with pivot ptr value
            nums[pivot_ptr], nums[right] = nums[right], nums[pivot_ptr]

            # in the end, we call quick_select recursively
            if expected_index < pivot_ptr:  # quick select to the left of pivot ptr
                return quick_select(left, pivot_ptr - 1)
            elif expected_index > pivot_ptr:  # quick select to the right of pivot ptr
                return quick_select(pivot_ptr + 1, right)
            else:  # we find the result!
                return nums[pivot_ptr]

        return quick_select(0, len(nums) - 1)
