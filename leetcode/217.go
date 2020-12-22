package main

import "sort"

func main() {
	print(containsDuplicate([]int{1, 2, 3, 4, 5, 5}))
}

func containsDuplicate(nums []int) bool {
	sort.Slice(nums, func(i, j int) bool {
		return nums[i] < nums[j]
	})
	for i, v := range nums {
		if i == len(nums)-1 {
			break
		}
		if v == nums[i+1] {
			return true
		}
	}
	return false
}
