package main

import (
	"fmt"
	"strconv"
)

func main() {
	const limit = 10000
	mark := make([]int, limit+1)

	for i := 1; i <= limit; i++ {
		n := i
		for n <= limit {
			n = d(n)
			if n <= limit {
				mark[n]++
			}
		}
	}

	for i, e := range mark {
		if i != 0 && e == 0 {
			fmt.Println(i)
		}
	}
}

func d(n int) int {
	for _, e := range strconv.Itoa(n) {
		num, _ := strconv.Atoi(string(e))
		n = n + num
	}
	return n
}
