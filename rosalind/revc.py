#!/usr/bin/env python

from util import read_input

raw_input = read_input('./rosalind_data/rosalind_revc.txt')
dna = raw_input[0]  #inputs first line of input file as a string

reversed_dna = dna[::-1] #reverses dna string
reversed_complement = ""

def complement(x):
    if x == "A":
        return "T"
    elif x == "T":
        return "A"
    elif x == "G":
        return "C"
    elif x == "C":
        return "G"
    else:
        return None
    
for base in reversed_dna:
    reversed_complement += complement(base)

print (reversed_complement)