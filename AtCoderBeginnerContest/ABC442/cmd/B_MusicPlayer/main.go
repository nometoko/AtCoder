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

	q := next(sc)

	volume := 0
	isPlaying := false
	for range q {
		a := next(sc)
		switch a {
		case 1:
			volume++
		case 2:
			volume = max(volume-1, 0)
		case 3:
			isPlaying = !isPlaying
		}

		if isPlaying && volume >= 3 {
			fmt.Println("Yes")
		} else {
			fmt.Println("No")
		}
	}
}
