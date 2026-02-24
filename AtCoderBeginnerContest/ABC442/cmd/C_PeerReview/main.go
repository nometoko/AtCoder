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
	m := next(sc)

	cnts := make([]int, n)
	for range m {
		a := next(sc)
		b := next(sc)
		cnts[a-1]++
		cnts[b-1]++
	}

	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()

	// fmt.Println(cnts)

	for _, cnt := range cnts {
		res := (n - 1) - cnt
		if res < 0 {
			fmt.Fprintf(out, "0 ")
		} else {
			ans := res * (res - 1) * (res - 2) / 6
			fmt.Fprintf(out, "%d ", ans)
		}
	}
	fmt.Fprintln(out)
}
