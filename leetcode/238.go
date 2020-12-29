package main

import "fmt"

func main() {
	fmt.Printf("%v", productExceptSelf([]int{1, 2, 3, 4}))
}

func productExceptSelf(nums []int) []int {
	length := len(nums)
	result := make([]int, len(nums))

	result[0] = 1
	for i := 1; i < length; i++ {
		result[i] = result[i-1] * nums[i-1]
	}

	tmp := 1
	for i := length - 1; i >= 0; i-- {
		result[i] = tmp * result[i]
		tmp = tmp * nums[i]
	}

	return result
}
