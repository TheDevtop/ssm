#!/usr/bin/env python3

# Program: SSM - Simple State Machine
# Version: 2.0
# Auhtors: Thijs Haker

tap = [] # Tape
hdr = 0  # Header
scs = 0  # Current state

def State4():
    global tap,hdr,scs
    print("State: ",scs)
    if tap[hdr] == '0':
        scs = 3
    elif tap[hdr] == '1':
        scs = 4
    else:
        Reset()
    return

def State3():
    global tap,hdr,scs
    print("State: ",scs)
    if tap[hdr] == '0':
        scs = 1
    elif tap[hdr] == '1':
        scs = 2
    else:
        Reset()
    return

def State2():
    global tap,hdr,scs
    print("State: ",scs)
    if tap[hdr] == '0':
        scs = 4
    elif tap[hdr] == '1':
        scs = 0
    else:
        Reset()
    return

def State1():
    global tap,hdr,scs
    print("State: ",scs)
    if tap[hdr] == '0':
        scs = 2
    elif tap[hdr] == '1':
        scs = 3
    else:
        Reset()
    return

def State0():
    global tap,hdr,scs
    print("State: ",scs)
    if tap[hdr] == '0':
        scs = 0
    elif tap[hdr] == '1':
        scs = 1
    else:
        Reset()
    return

def Run():
    global tap,hdr,scs
    if hdr == len(tap):
        Reset()
    
    if scs == 0:
        State0()
        return
    elif scs == 1:
        State1()
        return
    elif scs == 2:
        State2()
        return
    elif scs == 3:
        State3()
        return
    elif scs == 4:
        State4()
        return
    else:
        Reset()
    return

def Reset():
    global tap,hdr,scs
    print("State: Reset")
    tap = list(input(">"))
    hdr = 0
    scs = 0
    return

if __name__ == "__main__":
    print("Simple State Machine (SSM)")
    Reset()
    while True:
        if hdr == len(tap):
            Reset()
        Run()
        hdr = hdr+1
