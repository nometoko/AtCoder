package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
)

var sc = bufio.NewScanner(os.Stdin)

func scanInt() int {
	sc.Scan()

	val, err := strconv.Atoi(sc.Text())
	if err != nil {
		log.Fatal("Error occured at strconv.Atoi: ", err)
	}

	return val
}

func scanStr() string {
	sc.Scan()
	return sc.Text()
}

func main() {
	sc.Split(bufio.ScanWords)

	p, q := scanInt(), scanInt()
	x, y := scanInt(), scanInt()

	if p <= x && x < p+100 && q <= y && y < q+100 {
		fmt.Print("Yes")
	} else {
		fmt.Print("No")
	}
}
