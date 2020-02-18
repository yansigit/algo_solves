package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	w := bufio.NewWriter(os.Stdout)

	for scanner.Scan() {
		line := scanner.Text()
		num := strings.Fields(line)
		if len(num) > 0 {
			a, _ := strconv.Atoi(num[0])
			b, _ := strconv.Atoi(num[1])
			fmt.Fprintln(w, a+b)
		} else {
			break
		}
	}

	w.Flush()
}
