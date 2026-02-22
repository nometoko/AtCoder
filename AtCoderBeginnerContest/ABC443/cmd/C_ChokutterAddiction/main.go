package main

import "fmt"

func main() {
	var n, t int
	fmt.Scan(&n)
	fmt.Scan(&t)

	// var a [n]int
	a := make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Scan(&a[i])
	}

	cnt := 0
	startTime := 0
	for _, val := range a {
		if val > startTime {
			cnt += val - startTime
			startTime = val + 100
		}
	}

	if t > startTime {
		cnt += t - startTime
	}
	fmt.Println(cnt)
}
