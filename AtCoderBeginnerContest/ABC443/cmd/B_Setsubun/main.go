package main

import "fmt"

func main() {
	var n, k int
	fmt.Scan(&n)
	fmt.Scan(&k)

	cnt := n
	year := 0
	for cnt < k {
		n += 1
		cnt += n
		year += 1
	}
	fmt.Println(year)
}
