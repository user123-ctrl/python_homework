#!/usr/bin/env python

from util import read_input

input_file = read_input("./rosalind_data/rosalind_hamm.txt")
template_s = input_file[0] #reading only the the first part of the string
mutation_t = input_file[1] #reading only the second part of the string


#count the number of differences between the two sequences(hamming_distance)
hamming_distance = 0

for i in range(len(template_s)): #going over every letter from 0 to lengh of template
    if template_s[i] != mutation_t[i]: #comparing the letter at the same position
        hamming_distance += 1

print(hamming_distance)
