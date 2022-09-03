package main

func productExceptSelf(nums []int) []int {
	var res []int

	var prefix int = 1
	for index := range nums {
		if index == 0 {
			res = append(res, prefix)
		} else {
			prefix *= nums[index-1]
			res = append(res, prefix)
		}
	}

	var LEN int = len(nums)
	var postfix int = 1
	for index := LEN - 1; index >= 0; index-- {
		if index == LEN-1 {
			res[index] *= postfix
		} else {
			postfix *= nums[index+1]
			res[index] *= postfix
		}
	}

	return res
}
