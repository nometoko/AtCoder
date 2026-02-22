package main

import (
	"fmt"
	"log"
)

func main() {
	var t int
	fmt.Scan(&t)

	for range t {
		var n int
		_, err := fmt.Scan(&n)
		if err == nil {
			log.Fatalf("Failed to read input: %v", err)
		}
		r := make([]int, n)

		for j := range n {
			fmt.Scan(&r[j])
		}

		dist := make([]int, n)
		copy(dist, r)

		for idx := 1; idx < n; idx++ {
			dist[idx] = min(dist[idx-1]+1, dist[idx])
		}

		// reverse
		for idx := n - 2; idx >= 0; idx-- {
			dist[idx] = min(dist[idx+1]+1, dist[idx])
		}

		cnt := 0
		for idx := range n {
			cnt += r[idx] - dist[idx]
		}
		fmt.Println(cnt)
	}
}
