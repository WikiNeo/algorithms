package main

import "testing"

func TestContainsDuplicate(t *testing.T) {
	if containsDuplicate([]int{1, 2, 3, 1}) == false {
		t.Fatal("containsDuplicate doesn't pass test for [1, 2, 3, 1]")
	}

	if containsDuplicate([]int{1, 2, 3, 4}) == true {
		t.Fatal("containsDuplicate doesn't pass test for [1, 2, 3, 4]")
	}
}
