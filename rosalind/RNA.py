#!/usr/bin/env python

from util import read_input

raw_input = read_input('./rosalind_data/rosalind_rna.txt')
dna = raw_input[0]

rna = ""

for letter in dna:
    if letter == "G":
        rna += 'G'
    if letter == "A":
        rna += 'A'
    if letter == "C":
        rna += 'C'   
    if letter == "T":
        rna += 'U'

print(rna)


    
    