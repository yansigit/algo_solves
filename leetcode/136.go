package main

import "sort"

func main() {
	println(singleNumber([]int{1}))
}

func singleNumber(nums []int) int {
	sort.Slice(nums, func(i, j int) bool {
		return nums[i] < nums[j]
	})

	if len(nums) == 1 {
		return nums[0]
	}

	for i := 0; i < len(nums); i += 2 {
		if i+1 == len(nums) {
			return nums[i]
		}

		if i == 0 && nums[i] != nums[i+1] {
			return nums[0]
		}

		if nums[i] == nums[i+1] {
			continue
		}

		if nums[i] != nums[i-1] {
			return nums[i]
		}
	}

	return -1
}

// 1,1,2,2,3,3,4,7,7
// 1,1,2,3,3,4,4,8,8
// 1,1,2,2,3,4,4,6,6
// 0
// 1
// 0, 0, 1
