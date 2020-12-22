package main

import (
	"bufio"
	"fmt"
	"os"
)

var (
	r = bufio.NewReader(os.Stdin)
	w = bufio.NewWriter(os.Stdout)
)

func main() {
	//  a  A  b  B   z   Z
	// [97 65 98 66 122 90]
	defer w.Flush()
	var str string
	fmt.Fscan(r, &str)

	m := make(map[rune]int)

	for _, e := range str {
		if e >= 'a' {
			e -= 32
		}
		m[e]++
	}

	var t rune
	var c int
	for alphabet, count := range m {
		if count > c {
			t = alphabet
			c = count
		}
	}

	flag := false
	for alphabet, count := range m {
		if count == c && t != alphabet {
			flag = true
		}
	}

	if flag {
		fmt.Fprintln(w, "?")
	} else {
		fmt.Fprintf(w, "%s", string(t))
	}
}
