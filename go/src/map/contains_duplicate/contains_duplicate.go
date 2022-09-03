package main

func containsDuplicate(nums []int) bool {
	s := map[int]bool{}

	for _, num := range nums {
		if _, ok := s[num]; ok {
			return true
		}
		s[num] = true
	}

	return false
}
