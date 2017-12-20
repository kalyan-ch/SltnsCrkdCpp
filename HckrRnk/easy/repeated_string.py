#!/bin/python

import sys


s = raw_input().strip()
n = long(raw_input().strip())

count = 0
l = len(s)
for i in range(n):
    ind = i%l
    if s[ind] == "a":
        count += 1

print count
