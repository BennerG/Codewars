// Provided Instructions:
// The new "Avengers" movie has just been released! There are a lot
// of people at the cinema box office standing in a huge line. Each
// of them has a single 100, 50 or 25 dollar bill. An "Avengers"
// ticket costs 25 dollars.
// Vasya is currently working as a clerk. He wants to sell a ticket
// to every single person in this line.
// Can Vasya sell a ticket to every person and give change if he
// initially has no money and sells the tickets strictly in the
// order people queue?
// Return YES, if Vasya can sell a ticket to every person and give
// change with the bills he has at hand at that moment. Otherwise
// return NO.

package main

import "fmt"

func tickets(peopleInLine []int) string {
	// variable to hold the bills
	register := make(map[int]int)
	// iterate though the list of people
	for _, personsBill := range peopleInLine {
		// calculate change
		change := personsBill - 25
		// start with big bills for change; no 100s needed for change
		for _, billSize := range []int{50, 25} {
			if _, ok := register[billSize]; ok {
				for register[billSize] > 0 && change > 0 && billSize <= change {
					change -= billSize
					register[billSize]--
				}
			}
		}
		// return "NO" if change != 0
		if change != 0 {
			return "NO"
		}
		// add bill to register
		register[personsBill]++
	}
	return "YES"
}

func main() {
	fmt.Println(tickets([]int{25, 25, 50}))
	fmt.Println(tickets([]int{25, 100}))
	fmt.Println(tickets([]int{25, 25, 50, 50, 100}))
}
