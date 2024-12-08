#!/usr/bin/env python

from util import read_input
corrupted = read_input("./advent_input/day03.txt")

#extract only valid mul
def extract_mul(corrupted):
    sum = 0
    for i in range(len(corrupted)-3):
        if corrupted[i] == 'm' and corrupted[i+1] == 'u' and corrupted[i+2] == 'l' and corrupted[i+3] == '(':
            