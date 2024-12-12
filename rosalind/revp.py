#!/usr/bin/env python

from util import read_input
from util import complement

raw_input = read_input('./rosalind_data/rosalind_revp.txt')
dna = "".join(raw_input[1:]) #this line was my biggest problem somehow
reversed_dna = dna[::-1]
reversed_complement = ""

for base in reversed_dna:
     reversed_complement += complement(base)

# print(dna)
# print(reversed_complement)

# dna = "TCAATGCATGCGGGTCTATATGCAT"
# reversed_complement = "ATGCATATAGACCCGCATGCATTGA"

def find_palindrom(dna, reversed_complement):
    min_len = 4
    max_len = 12
    results = []

    for base in range(len(dna)):
        for length in range(min_len, max_len + 1):
            if base + length <= len(dna):
                string = dna[base:base + length]
                rev_base = len(dna) - (base + length)
                rev_end = len(dna) - base
                rev_string = reversed_complement[rev_base:rev_end] 
                if string == rev_string:
                    results.append((base + 1, length))
    return results 
    

palindromes = find_palindrom(dna, reversed_complement)
for base, length in palindromes:
    print(base, length)

