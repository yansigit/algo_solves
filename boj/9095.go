package main

import "fmt"

var chart [12]int

func init() {
	for i := 0; i < len(chart); i++ {
		chart[i] = -1
	}
	chart[0] = 0
	chart[1] = 1
	chart[2] = 2
	chart[3] = 4
}

func main() {
	var T int
	fmt.Scan(&T)
	for i := 0; i < T; i++ {
		var temp int
		fmt.Scan(&temp)
		doSlice(temp)
		fmt.Println(chart[temp])
	}
}

func doSlice(n int) int {
	if chart[n] != -1 {
		return chart[n]
	}
	chart[n] = doSlice(n-3) + doSlice(n-2) + doSlice(n-1)
	return chart[n]
}
