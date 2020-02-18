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
	w := bufio.NewWriter(os.Stdout)
	for i:=0; i<T; i++ {
		s,_ := r.ReadString('\n')
		a := strings.Fields(s)

		c,_ := strconv.Atoi(a[0])
		for _,e := range a[1] {
			for j := 0; j < c; j++ {
				fmt.Fprint(w, string(e))
			}
		}
		fmt.Fprint(w, "\n")
	}
	w.Flush()
}
