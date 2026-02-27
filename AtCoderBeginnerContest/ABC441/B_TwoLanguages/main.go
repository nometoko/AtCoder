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
	scanInt()
	scanInt()

	s := scanStr()
	t := scanStr()

	q := scanInt()

	for range q {
		word := scanStr()

		sFlag := true
		tFlag := true

		for _, char := range word {
			ok := false
			for _, refChar := range s {
				if char == refChar {
					ok = true
					break
				}
			}
			if !ok {
				sFlag = false
			}

			ok = false
			for _, refChar := range t {
				if char == refChar {
					ok = true
					break
				}
			}
			if !ok {
				tFlag = false
			}
		}

		if sFlag && !tFlag {
			fmt.Println("Takahashi")
		} else if sFlag && tFlag {
			fmt.Println("Unknown")
		} else if !sFlag && tFlag {
			fmt.Println("Aoki")
		}
	}
}
