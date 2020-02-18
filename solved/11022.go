package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	var T int
	fmt.Scan(&T)

	r := bufio.NewReader(os.Stdin)

	for i := 0; i < T; i++ {
		str, _ := r.ReadString('\n')
		num := strings.Fields(str)
		if len(num) > 0 {
			a, _ := strconv.Atoi(num[0])
			b, _ := strconv.Atoi(num[1])
			fmt.Printf("Case #%d: %d + %d = %d\n", i+1, a, b, a+b)
		}
	}
}
