package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

var stack []int

func main() {
	var T int
	fmt.Scan(&T)

	r := bufio.NewReader(os.Stdin)

	for i := 0; i < T; i++ {
		str, _ := r.ReadString('\n')
		cmd := strings.Fields(str)

		var num int
		if len(cmd) > 1 {
			num, _ = strconv.Atoi(cmd[1])
		}
		switch cmd[0] {
		case "push":
			push(num)
		case "top":
			top()
		case "size":
			size()
		case "empty":
			empty()
		case "pop":
			pop()
		case "print":
			fmt.Println(stack)
		}
	}
}

func push(x int) {
	stack = append(stack, x)
}

func pop() {
	if len(stack) == 0 {
		fmt.Println(-1)
		return
	}
	fmt.Println(stack[len(stack)-1])
	stack = stack[:len(stack)-1]
}

func size() {
	fmt.Println(len(stack))
}

func empty() {
	if len(stack) == 0 {
		fmt.Println(1)
	} else {
		fmt.Println(0)
	}
}

func top() {
	if len(stack) == 0 {
		fmt.Println(-1)
		return
	}
	fmt.Println(stack[len(stack)-1])
}
