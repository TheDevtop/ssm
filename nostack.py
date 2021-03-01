#!/usr/bin/env python3

# Program: SSM - Simple State Machine
# Version: 2.0
# Auhtors: Thijs Haker

# Current state & Next state
cs = 0
ns = 0

# Tape and Index pointer
tp = ['0']
ip = 0

def State4():
    global cs,ns
    global tp,ip
    cs = ns
    print("State: ", cs)
    if tp[ip] == '0':
        ns = 3
    elif tp[ip] == '1':
        ns = 4
    else:
        ns = -1
    ip = ip+1
    return

def State3():
    global cs,ns
    global tp,ip
    cs = ns
    print("State: ", cs)
    if tp[ip] == '0':
        ns = 1
    elif tp[ip] == '1':
        ns = 2
    else:
        ns = -1
    ip = ip+1
    return

def State2():
    global cs,ns
    global tp,ip
    cs = ns
    print("State: ", cs)
    if tp[ip] == '0':
        ns = 4
    elif tp[ip] == '1':
        ns = 0
    else:
        ns = -1
    ip = ip+1
    return

def State1():
    global cs,ns
    global tp,ip
    cs = ns
    print("State: ", cs)
    if tp[ip] == '0':
        ns = 2
    elif tp[ip] == '1':
        ns = 3
    else:
        ns = -1
    ip = ip+1
    return

def State0():
    global cs,ns
    global tp,ip
    cs = ns
    print("State: ", cs)
    if tp[ip] == '0':
        ns = 0
    elif tp[ip] == '1':
        ns = 1
    else:
        ns = -1
    ip = ip+1
    return

def Reset():
    global cs,ns
    global tp,ip
    print("State: Reset")
    i = list(input(">"))
    if i == []:
        tp = ['0']
    else:
        tp = i
    cs = 0
    ns = 0
    ip = 0
    return

def Run():
    global ip,tp,ns
    while True:
        if ip == len(tp):
            Reset()
        
        if ns == 0:
            State0()
        elif ns == 1:
            State1()
        elif ns == 2:
            State2()
        elif ns == 3:
            State3()
        elif ns == 4:
            State4()
        else:
            Reset()
    return

if __name__ == "__main__":
    print("Simple State Machine (SSM)")
    Run()
