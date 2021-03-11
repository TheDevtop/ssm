package main

// Program: Simple State Machine (Go)
// Version: 0.2
// Authors: Thijs Haker

import (
	"log"
)

// Temporary
var input string = "011001010110"

// Control box: cs,tp,ti
// cs = Current state
// tp = Tape length
// ti = Tape index
var cbx [3]int

func reset() {
	log.Println("State = Reset!")
	cbx[1] = len(input)
	cbx[2] = 0
	return
}

func main() {
	
}
