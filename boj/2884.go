package main

import "fmt"

func main() {
	var H, M int
	fmt.Scanln(&H, &M)
	if M < 45 {
		M += 60
		H -= 1
		if H == -1 {
			H = 23
		}
	}
	M -= 45

	fmt.Println(H, M)
}
