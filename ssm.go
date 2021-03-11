package main

// Program: Simple State Machine (Go)
// Version: 1.0
// Authors: Thijs Haker

import "fmt"

// Control box:
// 0 = Current state
// 1 = Tape length
// 2 = Tape index
var cbx [3]int

// Tape
var tap string

// Reset function
func reset() {
	fmt.Println("State: Reset!")
	fmt.Printf("-> ")
	fmt.Scanf("%s", &tap)
	cbx[0] = 0
	cbx[1] = len(tap)
	return
}

func main() {
	for {
		// Initial state == reset state
		reset()

		// For the index = 0; index < length; index++
		for cbx[2] = 0; cbx[2] < cbx[1]; cbx[2]++ {

			// Switch current state
			switch cbx[0] {

			// Print state, check input, set state or break
			case 0:
				fmt.Printf("State: %d\n", cbx[0])
				if tap[cbx[2]] == '0' {
					cbx[0] = 0
				} else if tap[cbx[2]] == '1' {
					cbx[0] = 1
				} else {
					break
				}
			case 1:
				fmt.Printf("State: %d\n", cbx[0])
				if tap[cbx[2]] == '0' {
					cbx[0] = 2
				} else if tap[cbx[2]] == '1' {
					cbx[0] = 3
				} else {
					break
				}
			case 2:
				fmt.Printf("State: %d\n", cbx[0])
				if tap[cbx[2]] == '0' {
					cbx[0] = 4
				} else if tap[cbx[2]] == '1' {
					cbx[0] = 0
				} else {
					break
				}
			case 3:
				fmt.Printf("State: %d\n", cbx[0])
				if tap[cbx[2]] == '0' {
					cbx[0] = 1
				} else if tap[cbx[2]] == '1' {
					cbx[0] = 2
				} else {
					break
				}
			case 4:
				fmt.Printf("State: %d\n", cbx[0])
				if tap[cbx[2]] == '0' {
					cbx[0] = 3
				} else if tap[cbx[2]] == '1' {
					cbx[0] = 4
				} else {
					break
				}
			default:
				break
			}
		}
	}
}
