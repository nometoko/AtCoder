package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
)

func next(sc *bufio.Scanner) int {
	sc.Scan()
	val, err := strconv.Atoi(sc.Text())
	if err != nil {
		log.Fatal("Error converting input to integer:", err)
	}
	return val
}

func main() {
	sc := bufio.NewScanner(os.Stdin)
	sc.Split(bufio.ScanWords)

	n := next(sc)
	q := next(sc)

	a := make([]int, n)
	sumA := make([]int, n+1)

	for i := range n {
		a[i] = next(sc)
		sumA[i+1] = sumA[i] + a[i]
	}
	// fmt.Println(a)

	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()

	for range q {
		query := next(sc)

		switch query {
		case 1:
			x := next(sc)

			a[x-1], a[x] = a[x], a[x-1]
			sumA[x] = sumA[x+1] - a[x]

		case 2:
			x := next(sc)
			y := next(sc)
			fmt.Fprintln(out, sumA[y]-sumA[x-1])
		}
	}
}
