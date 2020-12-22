package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

type node struct {
	// Status 0 : unvisited
	// Status 1 : explored
	// Status 2 : finished
	Status    int
	Neighbors []int
}

var (
	nodes []node
	stack []int
	queue []int
	r     = bufio.NewReader(os.Stdin)
	w     = bufio.NewWriter(os.Stdout)
)

func main() {
	defer w.Flush()

	var N, M, V int
	fmt.Fscan(r, &N, &M, &V)

	nodes = make([]node, N+1)

	for i := 0; i < M; i++ {
		var a, b int
		fmt.Fscan(r, &a, &b)
		nodes[a].Neighbors = append(nodes[a].Neighbors, b)
		nodes[b].Neighbors = append(nodes[b].Neighbors, a)
	}

	for i := 1; i <= N; i++ {
		sort.Ints(nodes[i].Neighbors)
		nodes[i].Status = 0
	}

	stack = append(stack, V)
	DFS(V)

	for _, e := range stack {
		fmt.Fprint(w, e, " ")
	}
	fmt.Fprint(w, "\n")

	for i := 1; i <= N; i++ {
		nodes[i].Status = 0
	}

	BFS(V)
}

func DFS(index int) {
	nodes[index].Status = 1
	for _, e := range nodes[index].Neighbors {
		if nodes[e].Status == 0 {
			stack = append(stack, e)
			DFS(e)
		}
	}
	nodes[index].Status = 2
}

func BFS(index int) {
	nodes[index].Status = 1
	queue = append(queue, index)
	for len(queue) > 0 {
		for _, e := range nodes[index].Neighbors {
			if nodes[e].Status == 0 {
				nodes[e].Status = 1
				queue = append(queue, e)
			}
		}
		fmt.Fprint(w, queue[0], " ")
		queue = queue[1:]
		if len(queue) > 0 {
			index = queue[0]
		}
	}
}
