package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"slices"
	"strconv"
)

var (
	sc = bufio.NewScanner(os.Stdin)
	wr = bufio.NewWriter(os.Stdout)
)

func getInt() int {
	sc.Scan()

	val, err := strconv.Atoi(sc.Text())
	if err != nil {
		log.Fatal("Error converting input to integer:", err)
	}
	return val
}

func main() {
	defer wr.Flush()
	sc.Split(bufio.ScanWords)

	n, k, x := getInt(), getInt(), int64(getInt())

	a := make([]int64, n)
	for i := range n {
		a[i] = int64(getInt())
	}

	slices.Sort(a)

	ans := n - k
	var volume int64 = 0

	for i := k - 1; i >= 0; i-- {
		ans++
		volume += a[i]

		if volume >= x {
			_, err := fmt.Fprintln(wr, ans)
			if err != nil {
				log.Fatal("Error writing output:", err)
			}
			return
		}
	}

	_, err := fmt.Fprintln(wr, -1)
	if err != nil {
		log.Fatal("Error writing output:", err)
	}
}
