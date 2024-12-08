#!/usr/bin/env python

from util import read_input

# first, read the raw data
data = read_input("./advent_input/day02.txt")
data = [[int(x) for x in line.split()] for line in data]

safe_counter = 0
#test for safety
for report in data:
    safe = False # define safe as False
    def safety_check(report):
        for i in range(len(report)-1):
            if abs(report[i]- report[i+1]) not in (1, 2, 3):
             return False

#test for direction
        increasing = False #define increasing as False to work with it
        for i in range(len(report)-1):
            difference = (report[i+1] - report[i])
            if difference == 0:
                return False
            elif increasing is False:
                increasing = difference > 0
            elif increasing and difference < 0:
                return False
            elif not increasing and difference > 0:
                return False

        return True

    if safety_check(report):
        safe = True

    if not safe:
        for i in range(len(report)):
            modified = report[:i] + report[i+1:]
            if safety_check(modified):
                safe = True
                break


    if safe:
        safe_counter += 1

print(safe_counter)