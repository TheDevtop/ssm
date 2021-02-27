#!/usr/bin/env python3

# Program: SSM - Simple State Machine
# Version: 1.0
# Auhtors: Thijs Haker

tap = [] # Tape
lth = 0  # Length
hdr = 0  # Header

def State4():
    global tap,lth,hdr
    print("State: 4")
    if hdr == lth:
        StateR()
    if tap[hdr] == '0':
        hdr = hdr+1
        State3()
    elif tap[hdr] == '1':
        hdr = hdr+1
        State4()
    else:
        StateR()
    return

def State3():
    global tap,lth,hdr
    print("State: 3")
    if hdr == lth:
        StateR()
    if tap[hdr] == '0':
        hdr = hdr+1
        State1()
    elif tap[hdr] == '1':
        hdr = hdr+1
        State2()
    else:
        StateR()
    return

def State2():
    global tap,lth,hdr
    print("State: 2")
    if hdr == lth:
        StateR()
    if tap[hdr] == '0':
        hdr = hdr+1
        State4()
    elif tap[hdr] == '1':
        hdr = hdr+1
        State0()
    else:
        StateR()
    return

def State1():
    global tap,lth,hdr
    print("State: 1")
    if hdr == lth:
        StateR()
    if tap[hdr] == '0':
        hdr = hdr+1
        State2()
    elif tap[hdr] == '1':
        hdr = hdr+1
        State3()
    else:
        StateR()
    return

def State0():
    global tap,lth,hdr
    print("State: 0")
    if hdr == lth:
        StateR()
    if tap[hdr] == '0':
        hdr = hdr+1
        State0()
    elif tap[hdr] == '1':
        hdr = hdr+1
        State1()
    else:
        StateR()
    return

def StateR():
    global tap,lth,hdr
    print("State: Reset")
    tap = list(input(">"))
    lth = len(tap)
    hdr = 0
    State0()
    return

if __name__ == "__main__":
    print("Simple State Machine (SSM)")
    StateR()
