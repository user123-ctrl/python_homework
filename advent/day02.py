#!/usr/bin/env python

from util import read_input

# first, read the raw data
data = read_input("./advent_input/day02.txt")
data = [[int(x) for x in line.split()] for line in data]

#test for fluctuation
for report in data:
    safe = True
    
    for i in range(len(report)-1):
        if abs(report[i]- report[i+1]) in (1, 2, 3):
            safe = True
        else:
            safe = False
            break

#if safe:
#    print("safe")
#else:
#    print("unsafe")

#test for direction
    if safe:
        increasing = None
        for i in range(len(report)-1):
            difference = (report[i+1] - report[i])
            if difference == 0:
                safe = False
                break
            if difference > 0:
                increasing = True
            if difference < 0:
                increasing = False
            


if safe:
    print("safe")
else:
    print("unsafe")