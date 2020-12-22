package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

var (
	r = bufio.NewReader(os.Stdin)
	w = bufio.NewWriter(os.Stdout)
)

func main() {
	defer w.Flush()

	var T int
	fmt.Fscan(r, &T)

	var str string
	for z := 0; z < T; z++ {
		succeed := false
		fmt.Fscan(r, &str)
		if strings.Count(str, "(") != strings.Count(str, ")") {
			fmt.Fprintln(w, "NO")
			continue
		}
		for i, e := range str {
			if e == '(' {
				if !(strings.Contains(str[i+1:], ")")) {
					succeed = false
					fmt.Fprintln(w, "NO")
					break
				}
				t1 := strings.Replace(str[:i+1], "(", "_", 1)
				t2 := strings.Replace(str[i+1:], ")", "_", 1)
				tmp := t1 + t2
				str = tmp
				succeed = true
			}
		}
		if succeed == true {
			fmt.Fprintln(w, "YES")
		}
	}
}
