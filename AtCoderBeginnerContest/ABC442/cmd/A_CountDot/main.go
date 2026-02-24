package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	sc := bufio.NewScanner(os.Stdin)
	sc.Split(bufio.ScanWords)

	sc.Scan()

	cnt := 0
	for _, char := range sc.Text() {
		if char == 'i' || char == 'j' {
			cnt++
		}
	}

	fmt.Println(cnt)
}
