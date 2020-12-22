package main

import (
	"fmt"
)

func main() {
	var A, B int
	var X3, X4, X5 int
	fmt.Scanln(&A)
	fmt.Scanln(&B)

	X3 = A * (B % 10)
	X4 = A * ((B / 10) % 10)
	X5 = A * ((B / 100) % 10)

	fmt.Println(X3)
	fmt.Println(X4)
	fmt.Println(X5)
	fmt.Println(X3 + X4*10 + X5*100)
}
