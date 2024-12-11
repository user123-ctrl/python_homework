#!/usr/bin/env python

from util import read_input
corrupted = ''.join(read_input("./advent_input/day03.txt"))

#extract only valid mul

def extract_valid_mul(corrupted):

def sum_mul(corrupted):
    instructions = extract_valid_mul(corrupted)
    total_sum = 0
    for num1, num2 in instructions:
        total_sum += num1 * num2
    return total_sum

result = sum_mul(corrupted)
print(result)