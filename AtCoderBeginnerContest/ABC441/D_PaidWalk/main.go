package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
)

type Edge struct {
	endPoint int
	cost     int
}

func next(sc *bufio.Scanner) int {
	sc.Scan()
	val, err := strconv.Atoi(sc.Text())
	if err != nil {
		log.Fatal("Error converting input to integer:", err)
	}
	return val
}

func dfs(currentPoint int, depth int, costSum int, edges map[int][]Edge, costMin int, costMax int, idealDepth int, endPoints *[]bool) {
	if depth == idealDepth {
		if costMin <= costSum && costSum <= costMax {
			(*endPoints)[currentPoint-1] = true
		}
		return
	}

	if costSum > costMax {
		return
	}

	for _, edge := range edges[currentPoint] {
		dfs(edge.endPoint, depth+1, costSum+edge.cost, edges, costMin, costMax, idealDepth, endPoints)
	}
}

func main() {
	sc := bufio.NewScanner(os.Stdin)
	sc.Split(bufio.ScanWords)

	n := next(sc)
	m := next(sc)
	l := next(sc)
	s := next(sc)
	t := next(sc)

	edges := make(map[int][]Edge)

	for range m {
		u := next(sc)
		v := next(sc)
		c := next(sc)

		edges[u] = append(edges[u], Edge{endPoint: v, cost: c})
	}

	endPoints := make([]bool, n)
	dfs(1, 0, 0, edges, s, t, l, &endPoints)

	for i, ok := range endPoints {
		if ok {
			fmt.Printf("%d ", i+1)
		}
	}
	fmt.Println()
}
