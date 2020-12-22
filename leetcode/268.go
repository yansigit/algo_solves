//Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
//
//Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?
//
//
//
//Example 1:
//
//Input: nums = [3,0,1]
//Output: 2
//Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.
//Example 2:
//
//Input: nums = [0,1]
//Output: 2
//Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.
//Example 3:
//
//Input: nums = [9,6,4,2,3,5,7,0,1]
//Output: 8
//Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.
//Example 4:
//
//Input: nums = [0]
//Output: 1
//Explanation: n = 1 since there is 1 number, so all numbers are in the range [0,1]. 1 is the missing number in the range since it does not appear in nums.

package main

import "sort"

func main() {
	missingNumber([]int{0, 1, 2})
}

func missingNumber(nums []int) int {
	sort.Slice(nums, func(i, j int) bool {
		return nums[i] < nums[j]
	})

	if nums[0] != 0 {
		return 0
	}

	if len(nums) == 1 {
		if nums[0] == 0 {
			return 1
		} else if nums[0] == 1 {
			return 0
		}
	}

	for i, v := range nums {
		if i == len(nums)-1 {
			break
		}
		if v != nums[i+1]-1 {
			// println(v, nums[i+1]-1)
			return nums[i+1] - 1
		}
	}

	return nums[len(nums)-1] + 1
}
