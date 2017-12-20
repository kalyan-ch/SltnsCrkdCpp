#!/bin/python

import sys


n = int(raw_input().strip())
c = map(int,raw_input().strip().split(' '))
jumps = 0
i = 0
while i < n:
    if i < n-2:
        if c[i+2] == 0:
            jumps+=1
            i += 2
        else:
            jumps+=2
            i += 3
    elif i == n-2:
        jumps += 1
        i += 1
    else:
        i += 1
            
print jumps

