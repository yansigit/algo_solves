//Given an array of integers, find if the array contains any duplicates.
//
//Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

//Example 1:
//
//Input: [1,2,3,1]
//Output: true
//Example 2:
//
//Input: [1,2,3,4]
//Output: false
//Example 3:
//
//Input: [1,1,1,3,3,4,3,2,4,2]
//Output: true

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
