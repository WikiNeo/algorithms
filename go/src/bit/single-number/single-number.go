package main

func singleNumber(nums []int) int {
	var res int = 0

	for _, v := range nums {
		res ^= v
	}

	return res
}

func singleNumber2(nums []int) int {
	var res int = nums[0]

	for index := 1; index < len(nums); index++ {
		res ^= nums[index]
	}

	return res
}
